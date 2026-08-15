#!/usr/bin/env python3
"""
Daily 情报扫描脚本（模式 3 辅助）

扫描 Daily/ 目录下文件名以本周日期开头的 md 摘要文件，提取 URL，
按目标分类文件全量去重后，输出按启发式类别分组的候选清单。
guess 仅为建议，最终分类由会话结合 Daily 正文上下文判断。

用法:
    python scan_daily.py [--week-start YYYY-MM-DD] [--daily-dir Daily] [--json <path>]

退出码:
    0: 正常输出（可能为空）
    2: Daily 目录不存在
"""
import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse

URL_RE = re.compile(r'https?://[^\s<>"{}|\\^`\[\]，。）)]+')
CVE_RE = re.compile(r'CVE-\d{4}-\d+', re.IGNORECASE)
FILE_DATE_RE = re.compile(r'^(\d{4}-\d{2}-\d{2})[^0-9]')

# 全局排除域名：X 来源帖 / 搜索 API / 漏洞库条目 / 厂商补丁公告 / 政府通告 / 新闻通稿
EXCLUDE_HOSTS = (
    'x.com', 'twitter.com', 't.co',
    'api.github.com',
    'nvd.nist.gov', 'cve.org', 'cve.report', 'opencve.io', 'tenable.com',
    'msrc.microsoft.com', 'helpx.adobe.com',
    'me.sap.com', 'support.sap.com', 'url.sap.com',
    'sec.cloudapps.cisco.com', 'support.broadcom.com', 'support.citrix.com',
    'security.paloaltonetworks.com', 'wordpress.org', 'blog.jetbrains.com',
    'cisa.gov', 'cert.gov.ua',
    'thehackernews.com', 'bleepingcomputer.com', 'securityweek.com',
    'csoonline.com', 'techtimes.com', 'helpnetsecurity.com',
    'darkreading.com', 'securityaffairs.com', 'neowin.net', 'arstechnica.com',
    'dataminr.com', 'fieldeffect.com',
)

C2_KW = ('c2', 'c&c', 'implant', 'beacon', 'botnet', 'rootkit', '-rat', 'rat-')
BOF_KW = ('bof', 'coff')

TARGET_FILES = ('C2.md', 'README.md', 'docs.md', 'BOF.md', 'tools.md')


def norm(url: str) -> str:
    """URL 归一化：去尾部斜杠、统一小写，用于去重比较。"""
    return url.rstrip('/').lower()


def host_excluded(host: str) -> bool:
    host = host.lower().removeprefix('www.')
    for ex in EXCLUDE_HOSTS:
        ex = ex.removeprefix('www.')
        if host == ex or host.endswith('.' + ex):
            return True
    return False


def classify(url: str, section: str) -> str:
    """启发式分类：cve / c2 / bof / tools / article（仅建议，需会话复核）。"""
    p = urlparse(url)
    host = p.netloc.lower()
    repo = p.path.rstrip('/').split('/')[-1] if p.path.strip('/') else ''
    blob = f"{repo} {section}"

    if 'gist.github.com' in host:
        return 'cve'  # gist PoC 默认归 CVE 类，需复核
    if 'github.com' in host:
        if CVE_RE.search(blob) or 'poc' in repo.lower() or 'exploit' in repo.lower():
            return 'cve'
        if any(k in repo.lower() for k in BOF_KW):
            return 'bof'
        if any(k in repo.lower() for k in C2_KW):
            return 'c2'
        return 'tools'
    return 'article'


def week_bounds(today: date) -> tuple[date, date]:
    start = today - timedelta(days=today.weekday())
    return start, start + timedelta(days=6)


def collect_daily(daily_dir: Path, start: date, end: date) -> dict:
    """提取本周 Daily 文件中的 URL，带章节上下文。"""
    cands: dict[str, dict] = {}
    for f in sorted(daily_dir.glob('*.md')):
        m = FILE_DATE_RE.match(f.name)
        if not m:
            continue
        d = datetime.strptime(m.group(1), '%Y-%m-%d').date()
        if not (start <= d <= end):
            continue
        section = ''
        for line in f.read_text(encoding='utf-8', errors='ignore').splitlines():
            stripped = line.strip()
            heading = re.match(r'^#{2,4}\s+(.*)$', stripped)
            if heading:
                section = heading.group(1)
                continue
            if '搜尋' in section or '搜索' in section:  # 「來源搜尋 URL」节跳过
                continue
            for u in URL_RE.findall(line):
                u = u.rstrip(').,;')
                pu = urlparse(u)
                host = pu.netloc
                if not host or host_excluded(host):
                    continue
                # 裸域名(IoC)、恶意载荷/样本文件、raw 内容文件排除
                if pu.path in ('', '/') or pu.path.lower().endswith(('.log', '.dll', '.exe', '.bin', '.iwq')):
                    continue
                if 'raw.githubusercontent.com' in host:
                    continue
                ent = cands.setdefault(norm(u), {'url': u, 'sections': set(), 'files': set()})
                ent['sections'].add(section)
                ent['files'].add(f.name)
    return cands


def existing_urls(root: Path) -> set:
    """目标分类文件（表格 + raw 区）中已存在的全部 URL，归一化。"""
    found: set = set()
    for name in TARGET_FILES:
        p = root / name
        if not p.exists():
            continue
        for u in URL_RE.findall(p.read_text(encoding='utf-8', errors='ignore')):
            found.add(norm(u.rstrip(').,;')))
    return found


def main():
    ap = argparse.ArgumentParser(description='Daily 情报扫描（模式 3 辅助）')
    ap.add_argument('--week-start', help='覆盖周一起始日期 YYYY-MM-DD（默认取本周）')
    ap.add_argument('--daily-dir', default='Daily', help='Daily 目录（默认: Daily）')
    ap.add_argument('--root', default='.', help='分类文件所在根目录（默认: .）')
    ap.add_argument('--json', dest='json_out', help='同时输出 JSON 到指定路径')
    args = ap.parse_args()

    daily_dir = Path(args.daily_dir)
    root = Path(args.root)
    if not daily_dir.is_dir():
        print(f'错误: Daily 目录不存在: {daily_dir}', file=sys.stderr)
        sys.exit(2)

    if args.week_start:
        start = datetime.strptime(args.week_start, '%Y-%m-%d').date()
    else:
        start = date.today()
    start, end = week_bounds(start)

    cands = collect_daily(daily_dir, start, end)
    have = existing_urls(root)

    result = {'week': f'{start} ~ {end}', 'files': sorted({f for c in cands.values() for f in c['files']}),
              'candidates': {}, 'deduped': []}
    for key, ent in sorted(cands.items()):
        if key in have:
            result['deduped'].append(ent['url'])
            continue
        guess = classify(ent['url'], ' / '.join(ent['sections']))
        result['candidates'].setdefault(guess, []).append(
            {'url': ent['url'], 'sections': sorted(ent['sections']), 'files': sorted(ent['files'])})

    print(f"📅 周期: {start} ~ {end}")
    print(f"📄 Daily 文件: {', '.join(result['files']) or '无'}")
    for grp in ('cve', 'c2', 'bof', 'tools', 'article'):
        items = result['candidates'].get(grp, [])
        if not items:
            continue
        print(f"\n== {grp} ({len(items)}) ==")
        for it in items:
            print(f"  [{','.join(it['sections'])[:40]:40s}] {it['url']}")
    print(f"\n去重跳过: {len(result['deduped'])}")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    sys.exit(0)


if __name__ == '__main__':
    main()
