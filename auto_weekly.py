#!/usr/bin/env python3
"""
完全自动化的周报生成工具
1. 从git历史生成周报文件（基于gen_weekly.py）
2. 自动获取GitHub内容
3. 使用AI生成中文描述
4. 更新周报文件
"""
import re
import os
import json
import time
import subprocess
import requests
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from collections import defaultdict

# ============ 配置区域 ============
# AI接口配置 - 支持两种认证方式
# 1. ANTHROPIC_API_KEY: 传统API Key认证 (x-api-key header)
# 2. ANTHROPIC_AUTH_TOKEN: OAuth Token认证 (Authorization: Bearer header)
_BASE_URL = os.getenv("ANTHROPIC_BASE_URL", "https://api.anthropic.com")
# 自动处理URL：如果不以/messages结尾，则追加 /v1/messages 或 /messages
if _BASE_URL.endswith("/messages"):
    AI_API_URL = _BASE_URL
elif _BASE_URL.endswith("/v1"):
    AI_API_URL = _BASE_URL.rstrip("/") + "/messages"
else:
    AI_API_URL = _BASE_URL.rstrip("/") + "/v1/messages"
AI_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
AI_AUTH_TOKEN = os.getenv("ANTHROPIC_AUTH_TOKEN", "")  # OAuth token模式
AI_MODEL = os.getenv("AI_MODEL", "claude-sonnet-4-5-20250929")  # Claude Sonnet 4.5

# Git仓库配置
GIT_REPO_PATH = "f:/gitweekly"
WEEKLY_DIR = Path(GIT_REPO_PATH) / "weekly"
CACHE_DIR = Path(GIT_REPO_PATH) / "links_cache"
# ================================


class WeeklyGenerator:
    """周报生成器 - 从git历史生成周报文件"""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.weekly_dir = self.repo_path / "weekly"
        self.weekly_dir.mkdir(exist_ok=True)

        # 文件类型到分类的映射
        self.category_map = {
            'README.md': '📦 收集的项目',
            'tools.md': '🔧 收集的工具',
            'BOF.md': '🎯 BOF工具',
            'skills-ai.md': '🤖 AI使用技巧',
            'docs.md': '📚 收集的文章',
            'free.md': '🎁 免费资源'
        }

    def get_week_range(self, date_str: str) -> Tuple[str, str]:
        """获取日期所在周的周一到周日"""
        date = datetime.strptime(date_str, "%Y-%m-%d")
        monday = date - timedelta(days=date.weekday())
        sunday = monday + timedelta(days=6)
        return monday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")

    def get_git_log(self, since_date: str = None) -> List[Dict]:
        """获取git提交日志"""
        cmd = [
            'git', '-C', str(self.repo_path),
            'log', '--pretty=format:%H|%ad|%s',
            '--date=format:%Y-%m-%d'
        ]

        if since_date:
            cmd.extend(['--since', since_date])

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        commits = []
        for line in result.stdout.strip().split('\n'):
            if not line:
                continue
            parts = line.split('|', 2)
            if len(parts) == 3:
                commits.append({
                    'hash': parts[0],
                    'date': parts[1],
                    'message': parts[2]
                })

        return commits

    def extract_links_from_diff(self, commit_hash: str) -> Dict[str, List[Dict]]:
        """从提交diff中提取链接，按文件分类（排除weekly目录）

        处理逻辑：
        - GitHub链接：desc留空，后续用AI生成
        - 非GitHub链接：使用标题行作为desc
        """
        cmd = [
            'git', '-C', str(self.repo_path),
            'show', commit_hash, '--format=', '--unified=0'
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        links_by_file = defaultdict(list)
        current_file = None
        last_title = ""  # 保存上一行的标题（用于非GitHub链接）

        for line in result.stdout.split('\n'):
            # 检测文件名
            if line.startswith('diff --git'):
                match = re.search(r'b/(.+)$', line)
                if match:
                    current_file = match.group(1)
                    last_title = ""
                continue

            # 只处理新增的行
            if not line.startswith('+') or line.startswith('+++'):
                continue

            # 去掉开头的+号
            content = line[1:]

            # 排除weekly目录下的文件
            if not current_file or current_file not in self.category_map:
                continue
            if current_file.startswith('weekly/'):
                continue

            # 检测标题行 (#### 标题 或 ### 标题 等)
            title_match = re.match(r'^#{1,6}\s+(.+)$', content)
            if title_match:
                last_title = title_match.group(1).strip()
                continue

            # 1. 匹配markdown链接格式: [text](https://...)
            markdown_pattern = r'\[([^\]]+)\]\((https?://[^\)]+)\)'
            markdown_matches = re.findall(markdown_pattern, content)
            for text, url in markdown_matches:
                if 'github.com' in url:
                    # GitHub链接：desc留空，后续用AI生成
                    links_by_file[current_file].append({'url': url, 'desc': ''})
                else:
                    # 非GitHub链接：使用markdown中的text作为desc
                    links_by_file[current_file].append({'url': url, 'desc': text})

            # 2. 匹配纯URL格式: https://...
            markdown_urls = [m[1] for m in markdown_matches]
            url_pattern = r'https?://[^\s\)\]>]+'
            url_matches = re.findall(url_pattern, content)
            for url in url_matches:
                if url not in markdown_urls:
                    if 'github.com' in url:
                        # GitHub链接：desc留空，后续用AI生成
                        links_by_file[current_file].append({'url': url, 'desc': ''})
                    else:
                        # 非GitHub链接：使用上一行的标题作为desc
                        links_by_file[current_file].append({'url': url, 'desc': last_title})
                    last_title = ""  # 使用后清空

            # 如果这行不是标题也不是链接，清空last_title
            if not title_match and not url_matches and not markdown_matches:
                if content.strip():  # 非空行
                    last_title = ""

        return dict(links_by_file)

    def get_weekly_commits(self, week_start: str, week_end: str) -> Dict:
        """获取指定周的提交记录"""
        cmd = [
            'git', '-C', str(self.repo_path),
            'log', '--pretty=format:%H|%ad|%s',
            '--date=format:%Y-%m-%d',
            f'--since={week_start}',
            f'--until={week_end} 23:59:59'
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        commits = []
        for line in result.stdout.strip().split('\n'):
            if not line:
                continue
            parts = line.split('|', 2)
            if len(parts) == 3:
                commits.append({
                    'hash': parts[0],
                    'date': parts[1],
                    'message': parts[2]
                })

        return {'commits': commits}

    def extract_links_from_diffs(self, commits: List[Dict]) -> Dict[str, List[Dict]]:
        """从多个提交的diff中提取链接（排除weekly目录）"""
        all_links = defaultdict(list)

        for commit in commits:
            links_by_file = self.extract_links_from_diff(commit['hash'])
            for file, links in links_by_file.items():
                all_links[file].extend(links)

        return dict(all_links)

    def generate_markdown(self, week_start: str, week_end: str, weekly_data: Dict, links_by_file: Dict[str, List[Dict]]) -> str:
        """生成周报的markdown内容"""
        content = f"# 本周更新 ({week_start} ~ {week_end})\n\n"

        # 去重并按分类组织链接
        unique_links = {}
        for file, links in links_by_file.items():
            category = self.category_map.get(file, '📦 其他')
            if category not in unique_links:
                unique_links[category] = {}
            # 使用url作为key去重，保留desc
            for link in links:
                url = link['url']
                desc = link['desc']
                if url not in unique_links[category]:
                    unique_links[category][url] = desc
                elif not unique_links[category][url] and desc:
                    # 如果已有url但没有desc，更新desc
                    unique_links[category][url] = desc

        # 按分类输出
        for category in sorted(unique_links.keys()):
            links_dict = unique_links[category]
            if links_dict:
                content += f"\n## {category}\n\n"
                content += "| 项目 | 说明 |\n"
                content += "|------|------|\n"

                for url, desc in links_dict.items():
                    # 从URL提取项目名
                    name = url.rstrip('/').split('/')[-1]
                    # 如果desc是项目名本身，清空它让AI生成
                    if desc and desc.lower() != name.lower():
                        content += f"| [{name}]({url}) | {desc} |\n"
                    else:
                        content += f"| [{name}]({url}) |  |\n"

        # 统计信息
        total_commits = len(weekly_data['commits'])
        total_links = sum(len(links) for links in unique_links.values())

        content += f"\n---\n\n"
        content += f"**统计：** 本周共 {total_commits} 次提交，新增 {total_links} 个链接。\n"

        return content

    def generate_weekly_files(self, start_date: str = "2025-07-21") -> List[str]:
        """生成所有周报文件"""
        print("\n" + "="*60)
        print("📅 第一步：从Git历史生成周报文件")
        print("="*60)

        # 获取提交记录
        commits = self.get_git_log(start_date)

        if not commits:
            print("⚠️  未找到提交记录")
            return []

        # 按周分组
        weeks = defaultdict(lambda: {'commits': [], 'links': defaultdict(list)})

        for commit in commits:
            monday, sunday = self.get_week_range(commit['date'])
            week_key = f"{monday}_{sunday}"

            weeks[week_key]['commits'].append(commit)

            # 提取该提交的链接
            links_by_file = self.extract_links_from_diff(commit['hash'])
            for file, links in links_by_file.items():
                weeks[week_key]['links'][file].extend(links)

        # 生成周报文件
        generated_files = []

        for week_key in sorted(weeks.keys()):
            week_data = weeks[week_key]
            monday, sunday = week_key.split('_')
            filename = f"weekly-{week_key}.md"
            filepath = self.weekly_dir / filename

            # 检查文件是否已存在
            if filepath.exists():
                print(f"⏭️  跳过已存在: {filename}")
                generated_files.append(filename)
                continue

            # 生成内容
            content = f"# 本周更新 ({monday} ~ {sunday})\n\n"

            # 去重链接（使用字典，url为key，desc为value）
            unique_links = {}
            for file, links in week_data['links'].items():
                category = self.category_map.get(file, '📦 其他')
                if category not in unique_links:
                    unique_links[category] = {}
                for link in links:
                    url = link['url']
                    desc = link['desc']
                    if url not in unique_links[category]:
                        unique_links[category][url] = desc
                    elif not unique_links[category][url] and desc:
                        unique_links[category][url] = desc

            # 按分类输出
            for category in sorted(unique_links.keys()):
                links_dict = unique_links[category]
                if links_dict:
                    content += f"\n## {category}\n\n"
                    content += "| 项目 | 说明 |\n"
                    content += "|------|------|\n"

                    for url, desc in links_dict.items():
                        name = url.rstrip('/').split('/')[-1]
                        if desc and desc.lower() != name.lower():
                            content += f"| [{name}]({url}) | {desc} |\n"
                        else:
                            content += f"| [{name}]({url}) |  |\n"

            # 统计信息
            total_commits = len(week_data['commits'])
            total_links = sum(len(links) for links in unique_links.values())

            content += f"\n---\n\n"
            content += f"**统计：** 本周共 {total_commits} 次提交，新增 {total_links} 个链接。\n"

            # 写入文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"✅ 生成: {filename} ({total_links} 个链接)")
            generated_files.append(filename)

        print(f"\n📊 共生成 {len(generated_files)} 个周报文件")
        return generated_files


class DescriptionGenerator:
    """描述生成器 - 使用AI生成项目描述"""

    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(exist_ok=True)
        self.cache_file = self.cache_dir / 'descriptions_cache.json'
        self.cache = self.load_cache()
        self.dirty = False  # 标记缓存是否被修改

    def load_cache(self) -> Dict:
        if self.cache_file.exists():
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_cache(self):
        """保存缓存（只在有修改时才写入文件）"""
        if not self.dirty:
            return  # 没有修改，跳过写入
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)
        self.dirty = False

    def fetch_github_content(self, url: str) -> Optional[str]:
        """获取GitHub仓库的README内容（使用raw.githubusercontent.com，无API限制）"""
        try:
            if 'github.com' not in url:
                return None

            parts = url.replace('https://github.com/', '').split('/')
            if len(parts) < 2:
                return None

            owner, repo = parts[0], parts[1]

            headers = {
                'User-Agent': 'Mozilla/5.0'
            }

            # 1. 尝试获取仓库主页（用于提取描述）
            repo_page_url = f"https://github.com/{owner}/{repo}"
            try:
                page_response = requests.get(repo_page_url, headers=headers, timeout=5)
                description = ""
                if page_response.status_code == 200:
                    # 简单提取描述（在<meta property="og:description"中）
                    import re
                    desc_match = re.search(r'<meta property="og:description" content="([^"]*)"', page_response.text)
                    if desc_match:
                        description = desc_match.group(1)
            except:
                description = ""

            # 2. 直接从raw.githubusercontent.com获取README（无API限制）
            readme_content = ""

            # 尝试常见的README文件名
            readme_files = ['README.md', 'readme.md', 'README.MD', 'README', 'README.txt']

            for readme_name in readme_files:
                raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{readme_name}"
                try:
                    readme_response = requests.get(raw_url, headers=headers, timeout=10)
                    if readme_response.status_code == 200:
                        readme_content = readme_response.text[:3000]
                        break
                except:
                    pass

                # 如果main分支失败，尝试master分支
                if not readme_content:
                    raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/master/{readme_name}"
                    try:
                        readme_response = requests.get(raw_url, headers=headers, timeout=10)
                        if readme_response.status_code == 200:
                            readme_content = readme_response.text[:3000]
                            break
                    except:
                        pass

            # 组合内容
            if readme_content or description:
                content = f"Repository: {owner}/{repo}\n"
                if description:
                    content += f"Description: {description}\n"
                if readme_content:
                    content += f"\nREADME (excerpt):\n{readme_content}"
                return content

            return None

        except Exception as e:
            return None

    def call_ai_for_summary(self, url: str, content: str) -> Optional[str]:
        """调用AI接口生成中文摘要"""
        try:
            prompt = f"""请为以下GitHub项目生成一个简洁的中文描述（15-30个汉字）。
要求：
1. 突出项目的核心功能
2. 使用专业技术术语
3. 简洁明了，便于快速理解

项目链接: {url}

项目信息:
{content}

请只返回中文描述，不要包含其他内容。"""

            headers = {"Content-Type": "application/json"}

            # 判断API类型：检查URL是否包含/v1/messages（Anthropic格式）
            is_anthropic_format = "/v1/messages" in AI_API_URL.lower() or "anthropic.com" in AI_API_URL.lower()

            # 根据不同的AI接口格式调整请求
            if is_anthropic_format:
                payload = {
                    "model": AI_MODEL,
                    "max_tokens": 100,
                    "messages": [{"role": "user", "content": prompt}]
                }
                headers["anthropic-version"] = "2023-06-01"

                # 优先使用 AUTH_TOKEN (OAuth)，否则使用 API_KEY
                if AI_AUTH_TOKEN:
                    headers["Authorization"] = f"Bearer {AI_AUTH_TOKEN}"
                elif AI_API_KEY:
                    headers["x-api-key"] = AI_API_KEY

            elif "ollama" in AI_API_URL.lower():
                payload = {
                    "model": AI_MODEL,
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False
                }
            else:
                payload = {
                    "model": AI_MODEL,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7,
                    "max_tokens": 100
                }
                if AI_API_KEY:
                    headers["Authorization"] = f"Bearer {AI_API_KEY}"

            response = requests.post(AI_API_URL, json=payload, headers=headers, timeout=30)

            if response.status_code == 200:
                result = response.json()

                if is_anthropic_format:
                    description = result.get('content', [{}])[0].get('text', '').strip()
                elif "ollama" in AI_API_URL.lower():
                    description = result.get('message', {}).get('content', '').strip()
                else:
                    description = result.get('choices', [{}])[0].get('message', {}).get('content', '').strip()

                description = description.strip('"\'').strip()
                return description
            else:
                print(f"    ✗ AI API 错误: HTTP {response.status_code}")
                print(f"    ✗ 响应内容: {response.text[:200]}")
                return None

        except Exception as e:
            print(f"    ✗ AI API 异常: {e}")
            return None

    def is_cached(self, url: str) -> bool:
        """检查URL是否已缓存"""
        return url in self.cache

    def get_cached(self, url: str) -> Optional[str]:
        """获取缓存的描述"""
        return self.cache.get(url)

    def generate_description(self, url: str) -> Optional[str]:
        """生成单个URL的描述（带缓存）

        返回值:
        - 字符串: 正常描述
        - "__DELETED__": 链接404/不可用，应从周报中删除
        - None: 生成失败但可以重试
        """
        # 检查缓存
        if url in self.cache:
            return self.cache[url]

        # 获取内容
        content = self.fetch_github_content(url)
        if not content:
            # 缓存标记为已删除，避免重复请求404链接
            self.cache[url] = "__DELETED__"
            self.dirty = True
            return "__DELETED__"

        # 调用AI生成描述
        description = self.call_ai_for_summary(url, content)

        if description and len(description) > 5:
            self.cache[url] = description
            self.dirty = True  # 标记缓存已修改
            return description

        return None


class WeeklyUpdater:
    """周报更新器 - 更新周报文件中的描述"""

    def __init__(self, weekly_dir: Path):
        self.weekly_dir = weekly_dir

    def extract_links_needing_descriptions(self, file_path: Path) -> List[str]:
        """提取需要描述的链接"""
        links = []
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'\| \[([^\]]+)\]\((https://[^\)]+)\) \| ([^\|]*) \|'
        matches = re.findall(pattern, content)

        for _, url, desc in matches:
            if not desc.strip() or '收集的项目地址' in desc:
                links.append(url)

        return links

    def update_weekly_file(self, file_path: Path, descriptions: Dict[str, str]) -> Tuple[int, int]:
        """更新周报文件

        返回: (更新数量, 删除数量)
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        update_count = 0
        delete_count = 0
        new_lines = []
        pattern = r'\| \[([^\]]+)\]\((https://[^\)]+)\) \| ([^\|]*) \|'

        for line in lines:
            match = re.search(pattern, line)
            if match:
                _, url, desc = match.groups()

                # 检查是否需要删除（404链接）
                if url in descriptions and descriptions[url] == "__DELETED__":
                    delete_count += 1
                    continue  # 跳过此行，不写入新文件

                # 检查是否需要更新描述
                if (not desc.strip() or '收集的项目地址' in desc) and url in descriptions:
                    if descriptions[url] != "__DELETED__":
                        update_count += 1
                        name = url.split('/')[-1]
                        line = f'| [{name}]({url}) | {descriptions[url]} |\n'

            new_lines.append(line)

        if update_count > 0 or delete_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)

        return update_count, delete_count


class AutoWeeklyProcessor:
    """完全自动化的周报处理器"""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.generator = WeeklyGenerator(repo_path)
        self.desc_gen = DescriptionGenerator(CACHE_DIR)
        self.updater = WeeklyUpdater(WEEKLY_DIR)

    def process_existing_weeklies(self, max_links_per_week: int = 50):
        """仅为已有周报生成描述（非交互模式）"""
        print("\n" + "="*60)
        print("📝 为所有已存在的周报文件生成描述")
        print("="*60)
        print(f"📊 每周最多处理: {max_links_per_week} 个链接\n")

        weekly_files = sorted([
            f for f in os.listdir(str(WEEKLY_DIR))
            if f.startswith('weekly-') and f.endswith('.md')
        ])

        print(f"发现 {len(weekly_files)} 个周报文件\n")

        for i, filename in enumerate(weekly_files, 1):
            file_path = WEEKLY_DIR / filename
            print(f"\n{'='*60}")
            print(f"[{i}/{len(weekly_files)}] 处理: {filename}")
            print('='*60)

            links = self.updater.extract_links_needing_descriptions(file_path)
            if not links:
                print("  ✓ 已完成")
                continue

            print(f"📊 发现 {len(links)} 个需要描述的链接")

            if len(links) > max_links_per_week:
                print(f"⚠️  本次只处理前 {max_links_per_week} 个链接")
                links = links[:max_links_per_week]

            descriptions = {}

            for j, url in enumerate(links, 1):
                print(f"\n  [{j}/{len(links)}] 处理: {url}")

                # 先检查缓存
                if self.desc_gen.is_cached(url):
                    desc = self.desc_gen.get_cached(url)
                    if desc == "__DELETED__":
                        print(f"    ⊘ 跳过 (链接不可用)")
                        descriptions[url] = desc  # 传递删除标记
                    else:
                        print(f"    ✓ 缓存命中: {desc}")
                        descriptions[url] = desc
                    continue

                # 没有缓存，需要网络请求
                print(f"    → 获取GitHub内容...")
                desc = self.desc_gen.generate_description(url)

                if desc == "__DELETED__":
                    print(f"    ⊘ 链接不可用 (404)")
                    descriptions[url] = desc  # 传递删除标记
                elif desc:
                    print(f"    ✓ 生成: {desc}")
                    descriptions[url] = desc

                    # 每5个保存一次
                    if j % 5 == 0:
                        self.desc_gen.save_cache()
                        print(f"    💾 已保存缓存 ({j}/{len(links)})")
                else:
                    print(f"    ✗ 生成失败")

                time.sleep(1)  # 只在网络请求后才sleep

            self.desc_gen.save_cache()

            if descriptions:
                print(f"\n📝 更新周报文件...")
                updated, deleted = self.updater.update_weekly_file(file_path, descriptions)
                if updated > 0:
                    print(f"✅ 成功更新 {updated} 个描述到 {filename}")
                if deleted > 0:
                    print(f"🗑️  删除 {deleted} 个无效链接")
            else:
                print(f"\n⚠️  没有成功生成任何描述")

        print("\n" + "="*60)
        print("🎉 所有周报处理完成！")
        print("="*60)

    def process_current_week(self, max_links: int = 50):
        """生成当前周的周报（含AI描述）"""
        print("\n" + "="*60)
        print("📅 生成当前周的周报")
        print("="*60)

        # 获取当前周的日期范围
        today = datetime.now()
        # 计算本周一（周一是0）
        days_since_monday = today.weekday()
        monday = today - timedelta(days=days_since_monday)
        sunday = monday + timedelta(days=6)

        week_start = monday.strftime('%Y-%m-%d')
        week_end = sunday.strftime('%Y-%m-%d')

        print(f"📊 当前周期: {week_start} ~ {week_end}")
        print(f"📊 最多处理: {max_links} 个链接\n")

        # 生成本周的周报文件
        filename = f"weekly-{week_start}_{week_end}.md"
        file_path = WEEKLY_DIR / filename

        print(f"📝 生成周报文件: {filename}")

        # 获取本周的Git提交
        weekly_data = self.generator.get_weekly_commits(week_start, week_end)

        if not weekly_data['commits']:
            print(f"⚠️  本周 ({week_start} ~ {week_end}) 没有提交记录")
            return

        print(f"✓ 发现 {len(weekly_data['commits'])} 个提交")

        # 提取所有链接
        links_by_file = self.generator.extract_links_from_diffs(weekly_data['commits'])

        # 统计总链接数
        total_links = sum(len(links) for links in links_by_file.values())
        print(f"✓ 提取 {total_links} 个链接")

        if total_links == 0:
            print("⚠️  本周没有新增链接")
            return

        # 生成markdown内容
        content = self.generator.generate_markdown(week_start, week_end, weekly_data, links_by_file)

        # 保存文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ 周报文件已生成: {file_path}")

        # 为链接生成描述
        print(f"\n{'='*60}")
        print("🤖 开始为链接生成AI描述...")
        print('='*60)

        links = self.updater.extract_links_needing_descriptions(file_path)

        if not links:
            print("✅ 所有链接都已有描述")
            return

        print(f"📊 发现 {len(links)} 个需要描述的链接")

        if len(links) > max_links:
            print(f"⚠️  链接较多，本次只处理前 {max_links} 个")
            links = links[:max_links]

        descriptions = {}

        for j, url in enumerate(links, 1):
            print(f"\n  [{j}/{len(links)}] {url}")

            # 先检查缓存
            if self.desc_gen.is_cached(url):
                desc = self.desc_gen.get_cached(url)
                if desc == "__DELETED__":
                    print(f"    ⊘ 跳过 (链接不可用)")
                    descriptions[url] = desc
                else:
                    print(f"    ✓ 缓存命中: {desc}")
                    descriptions[url] = desc
                continue

            # 没有缓存，需要网络请求
            print(f"    → 获取GitHub内容...")
            desc = self.desc_gen.generate_description(url)

            if desc == "__DELETED__":
                print(f"    ⊘ 链接不可用 (404)")
                descriptions[url] = desc
            elif desc:
                print(f"    ✓ 生成: {desc}")
                descriptions[url] = desc

                # 每5个保存一次
                if j % 5 == 0:
                    self.desc_gen.save_cache()
                    print(f"    💾 已保存缓存 ({j}/{len(links)})")
            else:
                print(f"    ✗ 生成失败")

            time.sleep(1)  # 只在网络请求后才sleep

        # 保存缓存
        self.desc_gen.save_cache()

        # 更新文件
        if descriptions:
            updated, deleted = self.updater.update_weekly_file(file_path, descriptions)
            if updated > 0:
                print(f"\n✅ 成功更新 {updated} 个描述")
            if deleted > 0:
                print(f"🗑️  删除 {deleted} 个无效链接")
        else:
            print(f"\n⚠️  没有成功生成任何描述")

        print("\n" + "="*60)
        print(f"🎉 当前周周报生成完成！")
        print(f"📄 文件位置: {file_path}")
        print("="*60)

    def process_all(self, start_date: str = "2025-07-21", max_links_per_week: int = 50):
        """完全自动化处理"""
        print("\n" + "="*60)
        print("🚀 启动完全自动化周报生成流程")
        print("="*60)
        print(f"📍 仓库路径: {self.repo_path}")
        print(f"🤖 AI模型: {AI_MODEL}")
        print(f"📊 每周最多处理: {max_links_per_week} 个链接\n")

        # 步骤1: 生成周报文件
        generated_files = self.generator.generate_weekly_files(start_date)

        if not generated_files:
            print("\n⚠️  没有可处理的周报文件")
            return

        # 步骤2: 为每个周报生成描述
        print("\n" + "="*60)
        print("📝 第二步：生成项目描述并更新周报")
        print("="*60)

        for i, filename in enumerate(generated_files, 1):
            file_path = WEEKLY_DIR / filename

            print(f"\n{'#'*60}")
            print(f"# [{i}/{len(generated_files)}] 处理: {filename}")
            print(f"{'#'*60}")

            # 提取需要描述的链接
            links = self.updater.extract_links_needing_descriptions(file_path)

            if not links:
                print("✅ 所有链接都已有描述")
                continue

            print(f"📊 发现 {len(links)} 个需要描述的链接")

            # 限制处理数量
            if len(links) > max_links_per_week:
                print(f"⚠️  链接较多，本次只处理前 {max_links_per_week} 个")
                links = links[:max_links_per_week]

            descriptions = {}

            # 处理每个链接
            for j, url in enumerate(links, 1):
                print(f"\n  [{j}/{len(links)}] {url}")

                # 先检查缓存
                if self.desc_gen.is_cached(url):
                    desc = self.desc_gen.get_cached(url)
                    print(f"    ✓ 缓存命中: {desc}")
                    descriptions[url] = desc
                    continue

                # 没有缓存，需要网络请求
                print(f"    → 获取GitHub内容...")
                description = self.desc_gen.generate_description(url)

                if description:
                    print(f"    ✓ 生成: {description}")
                    descriptions[url] = description

                    # 每5个保存一次
                    if j % 5 == 0:
                        self.desc_gen.save_cache()
                        print(f"    💾 已保存缓存 ({j}/{len(links)})")
                else:
                    print(f"    ✗ 生成失败")

                # 避免请求过快（只在网络请求后才sleep）
                time.sleep(1)

            # 保存缓存
            self.desc_gen.save_cache()

            # 更新文件
            if descriptions:
                updated, deleted = self.updater.update_weekly_file(file_path, descriptions)
                if updated > 0:
                    print(f"\n✅ 成功更新 {updated} 个描述")
                if deleted > 0:
                    print(f"🗑️  删除 {deleted} 个无效链接")
            else:
                print(f"\n⚠️  没有成功生成任何描述")

        print("\n" + "="*60)
        print("🎉 所有周报处理完成！")
        print("="*60)


def format_duration(seconds: float) -> str:
    """格式化时间为可读字符串"""
    if seconds < 60:
        return f"{seconds:.1f}秒"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}分{secs:.1f}秒"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        return f"{hours}小时{minutes}分{secs:.1f}秒"


def main():
    # 记录开始时间
    script_start_time = time.time()

    # 设置控制台编码
    import sys
    if sys.platform == 'win32':
        try:
            import codecs
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'ignore')
        except:
            pass

    print("""
╔════════════════════════════════════════════════════════════╗
║         完全自动化周报生成工具                              ║
║   Git历史 → 周报生成 → AI描述 → 自动更新                   ║
╚════════════════════════════════════════════════════════════╝
""")

    # 检查认证配置（支持两种方式）
    if not AI_API_KEY and not AI_AUTH_TOKEN:
        print("❌ 错误：未设置认证信息")
        print("\n请设置以下任一环境变量：")
        print("  方式1 - API Key:")
        print("    Windows: $env:ANTHROPIC_API_KEY='your-key'")
        print("    Linux:   export ANTHROPIC_API_KEY='your-key'")
        print("\n  方式2 - OAuth Token:")
        print("    Windows: $env:ANTHROPIC_AUTH_TOKEN='your-token'")
        print("    Linux:   export ANTHROPIC_AUTH_TOKEN='your-token'")
        return

    # 显示当前认证方式
    if AI_AUTH_TOKEN:
        print(f"🔐 认证方式: OAuth Token (ANTHROPIC_AUTH_TOKEN)")
    else:
        print(f"🔐 认证方式: API Key (ANTHROPIC_API_KEY)")

    # 选择模式
    print("\n请选择运行模式：")
    print("1. 完全自动化（生成周报 + AI描述）")
    print("2. 仅生成周报文件（不生成描述）")
    print("3. 仅为已有周报生成描述")
    print("4. 生成当前周的周报（含AI描述）")

    choice = input("\n请输入选项 (1/2/3/4): ").strip()

    processor = AutoWeeklyProcessor(GIT_REPO_PATH)

    if choice == "1":
        # 完全自动化
        start_date = input("起始日期 (默认: 2025-07-21): ").strip() or "2025-07-21"
        max_links = int(input("每周最多处理链接数 (默认: 50): ").strip() or "50")
        processor.process_all(start_date, max_links)

    elif choice == "2":
        # 仅生成周报
        start_date = input("起始日期 (默认: 2025-07-21): ").strip() or "2025-07-21"
        processor.generator.generate_weekly_files(start_date)

    elif choice == "3":
        # 仅生成描述
        print("\n此模式将为所有已存在的周报文件生成描述")
        max_links = int(input("每周最多处理链接数 (默认: 50): ").strip() or "50")

        weekly_files = sorted([
            f for f in os.listdir(WEEKLY_DIR)
            if f.startswith('weekly-') and f.endswith('.md')
        ])

        for i, filename in enumerate(weekly_files, 1):
            file_path = WEEKLY_DIR / filename
            print(f"\n{'='*60}")
            print(f"[{i}/{len(weekly_files)}] 处理: {filename}")
            print('='*60)

            links = processor.updater.extract_links_needing_descriptions(file_path)
            if not links:
                print("✓ 该文件所有链接都已有描述\n")
                continue

            print(f"📊 发现 {len(links)} 个需要描述的链接")

            if len(links) > max_links:
                print(f"⚠️  本次只处理前 {max_links} 个链接")
                links = links[:max_links]

            descriptions = {}

            for j, url in enumerate(links, 1):
                print(f"\n  [{j}/{len(links)}] 处理: {url}")

                # 先检查缓存
                if processor.desc_gen.is_cached(url):
                    desc = processor.desc_gen.get_cached(url)
                    print(f"    ✓ 缓存命中: {desc}")
                    descriptions[url] = desc
                    continue

                # 没有缓存，需要网络请求
                print(f"    → 获取GitHub内容...")
                desc = processor.desc_gen.generate_description(url)

                if desc:
                    print(f"    ✓ 生成: {desc}")
                    descriptions[url] = desc

                    # 每5个保存一次
                    if j % 5 == 0:
                        processor.desc_gen.save_cache()
                        print(f"    💾 已保存缓存 ({j}/{len(links)})")
                else:
                    print(f"    ✗ 生成失败")

                time.sleep(1)  # 只在网络请求后才sleep

            processor.desc_gen.save_cache()

            if descriptions:
                print(f"\n📝 更新周报文件...")
                updated, deleted = processor.updater.update_weekly_file(file_path, descriptions)
                if updated > 0:
                    print(f"✅ 成功更新 {updated} 个描述")
                if deleted > 0:
                    print(f"🗑️  删除 {deleted} 个无效链接")
                print()
            else:
                print(f"\n⚠️  没有成功生成任何描述\n")

    elif choice == "4":
        # 生成当前周的周报
        max_links = int(input("最多处理链接数 (默认: 50): ").strip() or "50")
        processor.process_current_week(max_links)

    else:
        print("❌ 无效的选项")

    # 打印总运行时间
    total_time = time.time() - script_start_time
    print(f"\n⏱️  总运行时间: {format_duration(total_time)}")


if __name__ == "__main__":
    main()
