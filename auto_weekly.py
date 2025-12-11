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
# AI接口配置 - 默认使用Anthropic Claude API
AI_API_URL = os.getenv("AI_API_URL", "https://api.anthropic.com/v1/messages")
AI_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "claude-sonnet-4-5")  # 使用Claude Sonnet 4.5（最新最强）

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

    def extract_links_from_diff(self, commit_hash: str) -> Dict[str, List[str]]:
        """从提交diff中提取链接，按文件分类"""
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

        for line in result.stdout.split('\n'):
            # 检测文件名
            if line.startswith('diff --git'):
                match = re.search(r'b/(.+)$', line)
                if match:
                    current_file = match.group(1)

            # 提取新增的链接
            if line.startswith('+') and not line.startswith('+++'):
                # 匹配markdown链接
                pattern = r'\[([^\]]+)\]\((https://github\.com/[^\)]+)\)'
                matches = re.findall(pattern, line)

                for text, url in matches:
                    if current_file and current_file in self.category_map:
                        links_by_file[current_file].append(url)

        return dict(links_by_file)

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

            # 去重链接
            unique_links = {}
            for file, links in week_data['links'].items():
                category = self.category_map.get(file, '📦 其他')
                if category not in unique_links:
                    unique_links[category] = []
                unique_links[category].extend(list(set(links)))

            # 按分类输出
            for category in sorted(unique_links.keys()):
                links = list(set(unique_links[category]))
                if links:
                    content += f"\n## {category}\n\n"
                    content += "| 项目 | 说明 |\n"
                    content += "|------|------|\n"

                    for url in links:
                        name = url.split('/')[-1]
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

    def load_cache(self) -> Dict:
        if self.cache_file.exists():
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_cache(self):
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)

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

            # 根据不同的AI接口格式调整请求
            if "anthropic.com" in AI_API_URL.lower():
                payload = {
                    "model": AI_MODEL,
                    "max_tokens": 100,
                    "messages": [{"role": "user", "content": prompt}]
                }
                if AI_API_KEY:
                    headers["x-api-key"] = AI_API_KEY
                    headers["anthropic-version"] = "2023-06-01"

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

                if "anthropic.com" in AI_API_URL.lower():
                    description = result.get('content', [{}])[0].get('text', '').strip()
                elif "ollama" in AI_API_URL.lower():
                    description = result.get('message', {}).get('content', '').strip()
                else:
                    description = result.get('choices', [{}])[0].get('message', {}).get('content', '').strip()

                description = description.strip('"\'').strip()
                return description
            else:
                return None

        except Exception as e:
            return None

    def generate_description(self, url: str) -> Optional[str]:
        """生成单个URL的描述（带缓存）"""
        # 检查缓存
        if url in self.cache:
            return self.cache[url]

        # 获取内容
        content = self.fetch_github_content(url)
        if not content:
            return None

        # 调用AI生成描述
        description = self.call_ai_for_summary(url, content)

        if description and len(description) > 5:
            self.cache[url] = description
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

    def update_weekly_file(self, file_path: Path, descriptions: Dict[str, str]) -> int:
        """更新周报文件"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        update_count = 0
        pattern = r'\| \[([^\]]+)\]\((https://[^\)]+)\) \| ([^\|]*) \|'

        def replacer(match):
            nonlocal update_count
            _, url, desc = match.groups()

            if (not desc.strip() or '收集的项目地址' in desc) and url in descriptions:
                update_count += 1
                name = url.split('/')[-1]
                return f'| [{name}]({url}) | {descriptions[url]} |'

            return match.group(0)

        updated_content = re.sub(pattern, replacer, content)

        if update_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

        return update_count


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
                print(f"    → 获取GitHub内容...")

                desc = self.desc_gen.generate_description(url)

                if desc:
                    print(f"    ✓ 生成: {desc}")
                    descriptions[url] = desc

                    # 每5个保存一次
                    if j % 5 == 0:
                        self.desc_gen.save_cache()
                        print(f"    💾 已保存缓存 ({j}/{len(links)})")
                else:
                    print(f"    ✗ 生成失败")

                time.sleep(1)

            self.desc_gen.save_cache()

            if descriptions:
                print(f"\n📝 更新周报文件...")
                count = self.updater.update_weekly_file(file_path, descriptions)
                print(f"✅ 成功更新 {count} 个描述到 {filename}")
            else:
                print(f"\n⚠️  没有成功生成任何描述")

        print("\n" + "="*60)
        print("🎉 所有周报处理完成！")
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

                # 避免请求过快
                time.sleep(1)

            # 保存缓存
            self.desc_gen.save_cache()

            # 更新文件
            if descriptions:
                count = self.updater.update_weekly_file(file_path, descriptions)
                print(f"\n✅ 成功更新 {count} 个描述")
            else:
                print(f"\n⚠️  没有成功生成任何描述")

        print("\n" + "="*60)
        print("🎉 所有周报处理完成！")
        print("="*60)


def main():
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

    # 检查API Key
    if not AI_API_KEY:
        print("❌ 错误：未设置 ANTHROPIC_API_KEY 环境变量")
        print("\n快速设置：")
        print("  Windows: $env:ANTHROPIC_API_KEY='your-key'")
        print("  Linux:   export ANTHROPIC_API_KEY='your-key'")
        return

    # 选择模式
    print("\n请选择运行模式：")
    print("1. 完全自动化（生成周报 + AI描述）")
    print("2. 仅生成周报文件（不生成描述）")
    print("3. 仅为已有周报生成描述")

    choice = input("\n请输入选项 (1/2/3): ").strip()

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

                time.sleep(1)

            processor.desc_gen.save_cache()

            if descriptions:
                print(f"\n📝 更新周报文件...")
                count = processor.updater.update_weekly_file(file_path, descriptions)
                print(f"✅ 成功更新 {count} 个描述\n")
            else:
                print(f"\n⚠️  没有成功生成任何描述\n")

    else:
        print("❌ 无效的选项")


if __name__ == "__main__":
    main()
