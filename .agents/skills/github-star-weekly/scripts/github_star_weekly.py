#!/usr/bin/env python3
"""Generate/update a gitweekly weekly report from GitHub stars.

This script is intentionally stdlib-only. It fetches a GitHub user's starred
repositories for a local-week date range and appends missing rows to
weekly/weekly-YYYY-MM-DD_YYYY-MM-DD.md.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    from zoneinfo import ZoneInfo
except Exception:  # pragma: no cover - old Python fallback
    ZoneInfo = None  # type: ignore

GITHUB_API = "https://api.github.com"
URL_RE = re.compile(r"https://github\.com/[^\s)\]|]+", re.I)
CVE_RE = re.compile(r"CVE-\d{4}-\d+", re.I)


def get_tz(name: str) -> dt.tzinfo:
    if ZoneInfo is not None:
        try:
            return ZoneInfo(name)  # type: ignore[misc]
        except Exception:
            pass
    if name in {"Asia/Taipei", "Asia/Shanghai", "UTC+8", "+08:00"}:
        return dt.timezone(dt.timedelta(hours=8), name)
    if name.upper() == "UTC":
        return dt.timezone.utc
    raise SystemExit(f"Unsupported timezone without zoneinfo data: {name}")


def parse_date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def week_range(args: argparse.Namespace) -> Tuple[dt.date, dt.date, dt.datetime, dt.datetime]:
    tz = get_tz(args.timezone)
    if args.week_start or args.week_end:
        if not (args.week_start and args.week_end):
            raise SystemExit("--week-start and --week-end must be used together")
        start_date = parse_date(args.week_start)
        end_date = parse_date(args.week_end)
    else:
        base = parse_date(args.date) if args.date else dt.datetime.now(tz).date()
        start_date = base - dt.timedelta(days=base.weekday())
        end_date = start_date + dt.timedelta(days=6)
    start_local = dt.datetime.combine(start_date, dt.time.min, tz)
    end_local = dt.datetime.combine(end_date, dt.time.max.replace(microsecond=0), tz)
    return start_date, end_date, start_local.astimezone(dt.timezone.utc), end_local.astimezone(dt.timezone.utc)


def github_headers(accept: str, token: Optional[str]) -> Dict[str, str]:
    headers = {
        "Accept": accept,
        "User-Agent": "codex-github-star-weekly",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def get_json(url: str, accept: str, token: Optional[str], retries: int = 2) -> Any:
    last: Optional[BaseException] = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=github_headers(accept, token))
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code in {403, 429, 500, 502, 503, 504} and attempt < retries:
                time.sleep(1.5 * (attempt + 1))
                last = exc
                continue
            body = exc.read().decode("utf-8", "replace")[:300]
            raise SystemExit(f"GitHub API error {exc.code} for {url}: {body}")
        except Exception as exc:  # network flakes
            last = exc
            if attempt < retries:
                time.sleep(1.5 * (attempt + 1))
                continue
            raise SystemExit(f"GitHub API request failed for {url}: {last}")
    raise SystemExit(f"GitHub API request failed for {url}: {last}")


def iso_utc(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(dt.timezone.utc)


def repo_url(full_name: str) -> str:
    return f"https://github.com/{full_name}"


def norm_url(url: str) -> str:
    return url.lower().rstrip("/")


def load_cache(path: Path) -> Dict[str, str]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return {str(k): str(v) for k, v in data.items()}
    except Exception:
        return {}
    return {}


def write_cache(path: Path, cache: Dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def cache_lookup(cache: Dict[str, str], url: str) -> Optional[str]:
    key = norm_url(url)
    for cached_url, desc in cache.items():
        if norm_url(cached_url) == key and desc and desc != "__DELETED__" and desc != cached_url:
            return desc
    return None


def trim_cjkish(text: str, limit: int = 34) -> str:
    text = re.sub(r"\s+", " ", text).strip(" .。")
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def describe_repo(repo: Dict[str, Any], cached: Optional[str]) -> str:
    if cached:
        return cached

    name = str(repo.get("name") or repo.get("full_name") or "repo")
    full_name = str(repo.get("full_name") or name)
    desc = str(repo.get("description") or "")
    lang = str(repo.get("language") or "").strip()
    topics = " ".join(str(x) for x in (repo.get("topics") or []))
    hay = f"{name} {full_name} {desc} {topics}".lower()
    cve = CVE_RE.search(f"{name} {desc}")

    if "byovd" in hay or ("edr" in hay and ("killer" in hay or "process" in hay)):
        return "基于BYOVD的EDR进程终止工具"
    if cve and any(x in hay for x in ["exploit", "poc", "rce", "lpe"]):
        return f"{cve.group(0).upper()}漏洞利用PoC"
    if " c2" in f" {hay}" or "c2 " in hay or name.lower().endswith("c2"):
        return f"{lang + '实现的' if lang else ''}开源C2框架"
    if "bof" in hay or "beacon object" in hay or "cobalt strike" in hay:
        return "Cobalt Strike BOF红队工具"
    if "wasm" in hay and any(x in hay for x in ["fuzz", "type-confusion", "type confusion"]):
        return "V8 Wasm类型混淆模糊测试系统"
    if "llvm" in hay and any(x in hay for x in ["lifter", "x86_64", "bindings", "nanobind"]):
        if "nanobind" in hay or "binding" in hay:
            return "基于nanobind的LLVM Python绑定"
        return "x86_64到LLVM IR实验性提升器"
    if "patch tuesday" in hay or "msrc" in hay or "bindiff" in hay:
        return "微软补丁星期二更新差分分析CLI"
    if "network monitor" in hay or "packet" in hay or "netstat" in hay:
        return f"{lang + '开发的' if lang else ''}跨平台进程网络监控TUI"
    if "obfuscat" in hay:
        return f"{lang + '项目' if lang else '项目'}递归混淆命令行工具"
    if "knowledge graph" in hay and any(x in hay for x in ["codex", "claude", "cursor"]):
        return "面向AI编码代理的本地代码知识图谱"
    if "proxy" in hay and any(x in hay for x in ["codex", "claude", "model"]):
        return "本地代理可视化AI编码请求的监控面板"
    if "ios" in hay and "javascript" in hay:
        return "iOS JavaScript安全研究平台"
    if "ios" in hay and any(x in hay for x in ["kernel", "exploit", "darksword", "springboard"]):
        return "iOS用户态与内核漏洞利用研究项目"
    if "tpm" in hay and any(x in hay for x in ["sniff", "bitlocker", "luks"]):
        return "dTPM总线嗅探提取磁盘密钥研究资料"
    if "ssh" in hay and "key" in hay:
        return "Linux SSH密钥窃取漏洞PoC"
    if "vulnerability research" in hay:
        return "漏洞研究文档工具与技巧集合"
    if "security research" in hay:
        return "安全研究资料集合仓库"
    if lang and desc:
        return trim_cjkish(f"{lang}项目：{desc}", 38)
    if desc:
        return trim_cjkish(desc, 38)
    return f"{name} GitHub项目"


def fetch_starred(username: str, start_utc: dt.datetime, end_utc: dt.datetime, token: Optional[str], max_pages: int) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for page in range(1, max_pages + 1):
        q = urllib.parse.urlencode({"sort": "created", "direction": "desc", "per_page": 100, "page": page})
        data = get_json(f"{GITHUB_API}/users/{urllib.parse.quote(username)}/starred?{q}", "application/vnd.github.star+json", token)
        if not data:
            break
        older_seen = False
        for item in data:
            starred_at = iso_utc(item.get("starred_at", "1970-01-01T00:00:00Z"))
            if starred_at > end_utc:
                continue
            if starred_at < start_utc:
                older_seen = True
                continue
            repo = item.get("repo") or item
            repo["_event_at"] = starred_at.isoformat()
            out.append(repo)
        if older_seen:
            break
    return out


def fetch_repo(full_name: str, token: Optional[str]) -> Optional[Dict[str, Any]]:
    try:
        return get_json(f"{GITHUB_API}/repos/{full_name}", "application/vnd.github+json", token)
    except SystemExit as exc:
        print(f"warning: cannot fetch repo {full_name}: {exc}", file=sys.stderr)
        return None


def fetch_forks(username: str, start_utc: dt.datetime, end_utc: dt.datetime, token: Optional[str], max_pages: int) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    seen: set[str] = set()
    for page in range(1, max_pages + 1):
        q = urllib.parse.urlencode({"per_page": 100, "page": page})
        data = get_json(f"{GITHUB_API}/users/{urllib.parse.quote(username)}/events/public?{q}", "application/vnd.github+json", token)
        if not data:
            break
        older_seen = False
        for ev in data:
            created = iso_utc(ev.get("created_at", "1970-01-01T00:00:00Z"))
            if created > end_utc:
                continue
            if created < start_utc:
                older_seen = True
                continue
            if ev.get("type") != "ForkEvent":
                continue
            full_name = ev.get("repo", {}).get("name")
            if not full_name or full_name.lower() in seen:
                continue
            seen.add(full_name.lower())
            repo = fetch_repo(full_name, token)
            if repo:
                repo["_event_at"] = created.isoformat()
                out.append(repo)
        if older_seen:
            break
    return out


def existing_github_urls(text: str) -> set[str]:
    return {norm_url(m.group(0)) for m in URL_RE.finditer(text)}


def rows_for(repos: Iterable[Dict[str, Any]], cache: Dict[str, str], existing: set[str], update_cache: bool) -> List[str]:
    rows: List[str] = []
    for repo in repos:
        full = str(repo.get("full_name") or "")
        if not full:
            continue
        url = repo_url(full)
        key = norm_url(url)
        if key in existing:
            continue
        cached = cache_lookup(cache, url)
        desc = describe_repo(repo, cached)
        name = str(repo.get("name") or full.rsplit("/", 1)[-1])
        rows.append(f"| [{name}]({url}) | {desc} |")
        existing.add(key)
        if update_cache and not cached:
            cache[url] = desc
    return rows


def insert_section(text: str, title: str, rows: List[str]) -> str:
    if not rows:
        return text
    table = ["| 链接 | 描述 |", "|------|------|"]
    lines = text.rstrip("\n").splitlines()
    try:
        idx = lines.index(title)
    except ValueError:
        block = ["", title, "", *table, *rows]
        return text.rstrip("\n") + "\n" + "\n".join(block) + "\n"

    next_idx = len(lines)
    for j in range(idx + 1, len(lines)):
        if lines[j].startswith("## "):
            next_idx = j
            break
    insert_at = next_idx
    if insert_at > idx and lines[insert_at - 1].strip() == "":
        insert_at -= 1
    new_lines = lines[:insert_at] + rows + [""] + lines[insert_at:]
    return "\n".join(new_lines).rstrip("\n") + "\n"


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Generate/update weekly GitHub star report")
    ap.add_argument("username", nargs="?", help="GitHub username, e.g. octocat")
    ap.add_argument("--username", dest="username_option", help="GitHub username; overrides the positional value")
    ap.add_argument("--date", help="Local date inside target week, default today")
    ap.add_argument("--week-start", help="Explicit local week start date YYYY-MM-DD")
    ap.add_argument("--week-end", help="Explicit local week end date YYYY-MM-DD")
    ap.add_argument("--timezone", default="Asia/Taipei", help="Local timezone for week boundaries")
    ap.add_argument("--weekly-dir", default="weekly", help="Weekly output directory")
    ap.add_argument("--cache-file", default="links_cache/descriptions_cache.json", help="Description cache JSON")
    ap.add_argument("--include-forks", action="store_true", help="Also append public fork events for the week")
    ap.add_argument("--update-cache", action="store_true", help="Write generated descriptions into cache file")
    ap.add_argument("--write", action="store_true", help="Write the weekly file; otherwise preview only")
    ap.add_argument("--dry-run", action="store_true", help="Preview only (default; kept for explicit commands)")
    ap.add_argument("--max-pages", type=int, default=5, help="Max GitHub API pages to scan")
    ap.add_argument("--token-env", default="GITHUB_TOKEN", help="Environment variable holding GitHub token")
    args = ap.parse_args(argv)

    username = (args.username_option or args.username or "").strip()
    if not username:
        if sys.stdin.isatty():
            username = input("GitHub username: ").strip()
        else:
            username = sys.stdin.readline().strip()
            if not username:
                raise SystemExit("GitHub username is required. Pass it as positional argument, use --username, type it at the prompt, or pipe it on stdin.")
    if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?", username):
        raise SystemExit(f"Invalid GitHub username: {username!r}")
    args.username = username

    token = os.environ.get(args.token_env) or None
    start_date, end_date, start_utc, end_utc = week_range(args)
    weekly_path = Path(args.weekly_dir) / f"weekly-{start_date}_{end_date}.md"
    cache_path = Path(args.cache_file)
    cache = load_cache(cache_path)

    text = weekly_path.read_text(encoding="utf-8") if weekly_path.exists() else f"# Weekly Report: {start_date} ~ {end_date}\n"
    existing = existing_github_urls(text)

    stars = fetch_starred(args.username, start_utc, end_utc, token, args.max_pages)
    star_rows = rows_for(stars, cache, existing, args.update_cache)
    text2 = insert_section(text, f"## GitHub Stars（{start_date} ~ {end_date}）", star_rows)

    fork_rows: List[str] = []
    if args.include_forks:
        forks = fetch_forks(args.username, start_utc, end_utc, token, args.max_pages)
        fork_rows = rows_for(forks, cache, existing, args.update_cache)
        text2 = insert_section(text2, f"## GitHub Forks（{start_date} ~ {end_date}）", fork_rows)

    print(f"GitHub user: {args.username}")
    print(f"Week: {start_date} ~ {end_date} ({args.timezone})")
    print(f"Target: {weekly_path}")
    print(f"Starred repos in range: {len(stars)}; new rows: {len(star_rows)}")
    if args.include_forks:
        print(f"Fork rows: {len(fork_rows)}")

    if not args.write:
        print("\nDRY RUN: pass --write to update the weekly file.")
        for row in star_rows[:80]:
            print(row)
        for row in fork_rows[:80]:
            print(row)
        return 0

    if text2 != text:
        weekly_path.parent.mkdir(parents=True, exist_ok=True)
        weekly_path.write_text(text2, encoding="utf-8")
        print("Updated weekly file")
    else:
        print("No weekly changes needed")

    if args.update_cache:
        write_cache(cache_path, cache)
        print(f"Updated cache: {cache_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


