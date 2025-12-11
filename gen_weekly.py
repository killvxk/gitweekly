#!/usr/bin/env python3
import subprocess
import re
from datetime import datetime, timedelta
from collections import defaultdict

def get_week_range(date_str):
    """Get Monday-Sunday range for a given date"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    monday = date - timedelta(days=date.weekday())
    sunday = monday + timedelta(days=6)
    return monday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")

def get_commits_by_week():
    """Group commits by week"""
    result = subprocess.run(
        ["git", "log", "--format=%H %ai", "--all", "--reverse"],
        capture_output=True, text=True, cwd="f:/gitweekly", encoding="utf-8", errors="ignore"
    )

    weeks = defaultdict(list)
    for line in result.stdout.strip().split("\n"):
        parts = line.split()
        if len(parts) >= 2:
            commit_hash = parts[0]
            date_str = parts[1]
            week_start, week_end = get_week_range(date_str)
            weeks[(week_start, week_end)].append(commit_hash)

    return dict(sorted(weeks.items()))

def get_diff_for_week(prev_commit, end_commit):
    """Get diff between two commits"""
    result = subprocess.run(
        ["git", "diff", prev_commit, end_commit, "--unified=0"],
        capture_output=True, text=True, cwd="f:/gitweekly", encoding="utf-8", errors="ignore"
    )
    return result.stdout or ""

def extract_links_with_context(diff_text):
    """Extract links with their preceding titles from diff"""
    links_data = []
    current_file = None
    current_title = None
    url_pattern = r'https?://[^\s<>\"\'\)\]\}]+[^\s<>\"\'\)\]\}\.,]'

    lines = diff_text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("+++ b/"):
            current_file = line[6:]
            current_title = None
        elif line.startswith("+") and not line.startswith("+++"):
            content = line[1:].strip()

            # Check if it's a title line
            title_match = re.match(r'^#{1,6}\s+(.+)$', content)
            if title_match:
                current_title = title_match.group(1)
                continue

            # Extract URLs from the line
            urls = re.findall(url_pattern, content)
            for url in urls:
                links_data.append({
                    "url": url,
                    "title": current_title,
                    "file": current_file
                })

    # Remove duplicates while preserving order
    seen = set()
    unique_links = []
    for item in links_data:
        if item["url"] not in seen:
            seen.add(item["url"])
            unique_links.append(item)

    return unique_links

def categorize_links(links_data):
    """Categorize links by file type"""
    categories = {
        "README.md": {"name": "收集的项目", "emoji": "📦", "links": []},
        "tools.md": {"name": "有趣的工具", "emoji": "🛠️", "links": []},
        "BOF.md": {"name": "BOF 工具", "emoji": "🔴", "links": []},
        "skills-ai.md": {"name": "AI 使用技巧", "emoji": "🤖", "links": []},
        "docs.md": {"name": "有趣的文章", "emoji": "📚", "links": []},
        "free_baipiao.md": {"name": "免费资源", "emoji": "🆓", "links": []},
        "other": {"name": "其他", "emoji": "📋", "links": []}
    }

    for item in links_data:
        file_name = item.get("file", "")
        if file_name in categories:
            categories[file_name]["links"].append(item)
        else:
            categories["other"]["links"].append(item)

    return categories

def generate_weekly_md(week_start, week_end, links_data, commit_count):
    """Generate markdown content for a week"""
    categories = categorize_links(links_data)

    lines = [f"# 本周更新 ({week_start} ~ {week_end})\n"]

    for file_key, cat in categories.items():
        if not cat["links"]:
            continue

        lines.append(f"\n## {cat['emoji']} {cat['name']}\n")
        lines.append("| 项目 | 说明 |")
        lines.append("|------|------|")

        for item in cat["links"]:
            url = item["url"]
            title = item.get("title") or ""

            # Extract project name from GitHub URL
            name = url
            github_match = re.match(r'https://github\.com/([^/]+/[^/]+)', url)
            if github_match:
                name = github_match.group(1).split("/")[-1]
            elif "github.io" in url or url.endswith(".md"):
                name = url.split("/")[-1] or url.split("/")[-2]
            else:
                # Try to get domain name
                domain_match = re.match(r'https?://([^/]+)', url)
                if domain_match:
                    name = domain_match.group(1)

            display_name = title if title else name
            lines.append(f"| [{display_name}]({url}) | {title if title else ''} |")

    lines.append(f"\n---\n")
    lines.append(f"**统计：** 本周共 {commit_count} 次提交，新增 {len(links_data)} 个链接。\n")

    return "\n".join(lines)

def main():
    weeks = get_commits_by_week()
    print(f"Found {len(weeks)} weeks of data")

    prev_end_commit = None

    for (week_start, week_end), commits in weeks.items():
        end_commit = commits[-1]

        # Get diff
        if prev_end_commit:
            diff = get_diff_for_week(prev_end_commit, end_commit)
        else:
            # First week - compare with empty tree
            result = subprocess.run(
                ["git", "diff", "4b825dc642cb6eb9a060e54bf8d69288fbee4904", end_commit, "--unified=0"],
                capture_output=True, text=True, cwd="f:/gitweekly", encoding="utf-8", errors="ignore"
            )
            diff = result.stdout or ""

        links_data = extract_links_with_context(diff)

        if links_data:
            # Generate markdown
            md_content = generate_weekly_md(week_start, week_end, links_data, len(commits))

            # Save to file
            filename = f"f:/gitweekly/weekly/weekly-{week_start}_{week_end}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(md_content)

            print(f"Generated: weekly-{week_start}_{week_end}.md ({len(links_data)} links)")
        else:
            print(f"Skipped: {week_start} to {week_end} (no links)")

        prev_end_commit = end_commit

    print("\nDone!")

if __name__ == "__main__":
    main()
