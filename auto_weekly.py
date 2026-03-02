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
import sys
import json
import time
import logging
import subprocess
import requests
import functools
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from json import JSONDecodeError
from typing import Dict, List, Optional, Tuple, Callable, Any
from urllib.parse import urlparse
from collections import defaultdict

# ============ 日志配置 ============
def setup_logging(log_file: Optional[str] = None, level: int = logging.INFO):
    """配置日志系统"""
    handlers = []

    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_format = logging.Formatter('%(message)s')
    console_handler.setFormatter(console_format)
    handlers.append(console_handler)

    # 文件处理器（可选）
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)
        handlers.append(file_handler)

    logging.basicConfig(level=level, handlers=handlers)
    return logging.getLogger(__name__)

logger = setup_logging()

# ============ 重试装饰器 ============
def retry(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0,
          exceptions: tuple = (requests.RequestException,)):
    """
    重试装饰器

    Args:
        max_attempts: 最大重试次数
        delay: 初始延迟（秒）
        backoff: 延迟倍数（每次重试后延迟乘以此值）
        exceptions: 需要重试的异常类型
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts:
                        logger.warning(f"    ⚠️ 第 {attempt} 次尝试失败: {e}")
                        logger.info(f"    ⏳ {current_delay:.1f}秒后重试...")
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(f"    ✗ 已重试 {max_attempts} 次，放弃")

            raise last_exception
        return wrapper
    return decorator

# ============ 配置管理 ============
@dataclass
class Config:
    """配置类"""
    # AI接口配置
    ai_base_url: str = "https://api.anthropic.com"
    ai_api_key: str = ""
    ai_auth_token: str = ""
    ai_model: str = "claude-sonnet-4-5-20250929"

    # 路径配置
    repo_path: Path = field(default_factory=Path.cwd)
    weekly_dir: Path = field(default=None)
    cache_dir: Path = field(default=None)

    # 处理配置
    max_links_per_week: int = 50
    request_delay: float = 1.0
    cache_save_interval: int = 5

    # 重试配置
    retry_max_attempts: int = 3
    retry_delay: float = 1.0
    retry_backoff: float = 2.0

    def __post_init__(self):
        """初始化后处理"""
        if self.weekly_dir is None:
            self.weekly_dir = self.repo_path / "weekly"
        if self.cache_dir is None:
            self.cache_dir = self.repo_path / "links_cache"

    @property
    def ai_api_url(self) -> str:
        """获取完整的AI API URL"""
        base = self.ai_base_url.rstrip("/")
        if base.endswith("/messages"):
            return base
        elif base.endswith("/v1"):
            return base + "/messages"
        else:
            return base + "/v1/messages"

    @classmethod
    def from_env(cls, repo_path: Optional[Path] = None) -> "Config":
        """从环境变量加载配置"""
        if repo_path is None:
            repo_path = Path.cwd()

        return cls(
            ai_base_url=os.getenv("ANTHROPIC_BASE_URL", "https://api.anthropic.com"),
            ai_api_key=os.getenv("ANTHROPIC_API_KEY", ""),
            ai_auth_token=os.getenv("ANTHROPIC_AUTH_TOKEN", ""),
            ai_model=os.getenv("AI_MODEL", "claude-sonnet-4-5-20250929"),
            repo_path=repo_path,
            max_links_per_week=int(os.getenv("MAX_LINKS_PER_WEEK", "50")),
            request_delay=float(os.getenv("REQUEST_DELAY", "1.0")),
        )

    @classmethod
    def from_file(cls, config_file: Path, repo_path: Optional[Path] = None) -> "Config":
        """从配置文件加载配置"""
        if repo_path is None:
            repo_path = Path.cwd()

        config_data = {}
        if config_file.exists():
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    if config_file.suffix in ('.yaml', '.yml'):
                        try:
                            import yaml
                            config_data = yaml.safe_load(f) or {}
                        except ImportError:
                            logger.warning("未安装 PyYAML，使用环境变量配置")
                    elif config_file.suffix == '.json':
                        config_data = json.load(f)
            except Exception as e:
                logger.warning(f"读取配置文件失败: {e}，使用默认配置")

        # 合并环境变量（环境变量优先级更高）
        return cls(
            ai_base_url=os.getenv("ANTHROPIC_BASE_URL", config_data.get("ai_base_url", "https://api.anthropic.com")),
            ai_api_key=os.getenv("ANTHROPIC_API_KEY", config_data.get("ai_api_key", "")),
            ai_auth_token=os.getenv("ANTHROPIC_AUTH_TOKEN", config_data.get("ai_auth_token", "")),
            ai_model=os.getenv("AI_MODEL", config_data.get("ai_model", "claude-sonnet-4-5-20250929")),
            repo_path=repo_path,
            max_links_per_week=int(os.getenv("MAX_LINKS_PER_WEEK", config_data.get("max_links_per_week", 50))),
            request_delay=float(os.getenv("REQUEST_DELAY", config_data.get("request_delay", 1.0))),
            retry_max_attempts=config_data.get("retry_max_attempts", 3),
            retry_delay=config_data.get("retry_delay", 1.0),
            retry_backoff=config_data.get("retry_backoff", 2.0),
        )

# 全局配置（延迟初始化）
_config: Optional[Config] = None

def get_config() -> Config:
    """获取全局配置"""
    global _config
    if _config is None:
        repo_path = Path.cwd()
        config_file = repo_path / "config.yaml"
        if config_file.exists():
            _config = Config.from_file(config_file, repo_path)
        else:
            _config = Config.from_env(repo_path)
    return _config

def set_config(config: Config):
    """设置全局配置"""
    global _config
    _config = config

# ============ 进度显示 ============
class ProgressBar:
    """简单的进度条显示"""

    def __init__(self, total: int, desc: str = "", width: int = 40):
        self.total = total
        self.current = 0
        self.desc = desc
        self.width = width
        self.start_time = time.time()

    def update(self, n: int = 1):
        """更新进度"""
        self.current += n
        self._display()

    def set(self, n: int):
        """设置当前进度"""
        self.current = n
        self._display()

    def _display(self):
        """显示进度条"""
        if self.total == 0:
            return

        percent = self.current / self.total
        filled = int(self.width * percent)
        bar = '█' * filled + '░' * (self.width - filled)

        elapsed = time.time() - self.start_time
        if self.current > 0:
            eta = elapsed / self.current * (self.total - self.current)
            eta_str = format_duration(eta)
        else:
            eta_str = "--"

        # 使用 \r 回到行首，覆盖之前的输出
        sys.stdout.write(f'\r{self.desc} |{bar}| {self.current}/{self.total} ({percent:.0%}) ETA: {eta_str}')
        sys.stdout.flush()

    def finish(self):
        """完成进度条"""
        self.current = self.total
        self._display()
        print()  # 换行


def format_duration(seconds: float) -> str:
    """格式化时间为可读字符串"""
    if seconds < 60:
        return f"{seconds:.1f}秒"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}分{secs:.0f}秒"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        return f"{hours}小时{minutes}分"
# ================================


def is_meaningful_description(desc: str, url: str) -> bool:
    """
    判断描述是否有意义（不仅仅是URL路径名）

    无意义的描述包括：
    - 空字符串
    - URL路径名（如 weaponized-in-china-deployed-in-india）
    - URL的一部分
    - 太短的文本（少于5个字符）
    - 文件名后缀（如 .html）
    - 纯数字（如 3453）
    """
    if not desc:
        return False

    desc_lower = desc.lower().strip()

    # 从URL提取路径名
    url_name = url.rstrip('/').split('/')[-1]
    url_name_lower = url_name.lower()

    # 如果描述就是URL路径名，不算有效描述
    if desc_lower == url_name_lower:
        return False

    # 移除常见后缀后再比较
    for suffix in ['.html', '.htm', '.md', '.php', '.asp', '.aspx']:
        if url_name_lower.endswith(suffix):
            url_name_no_ext = url_name_lower[:-len(suffix)]
            if desc_lower == url_name_no_ext:
                return False

    # 如果描述是URL路径的变体（将-替换为空格等）
    url_name_normalized = url_name_lower.replace('-', ' ').replace('_', ' ')
    desc_normalized = desc_lower.replace('-', ' ').replace('_', ' ')
    if desc_normalized == url_name_normalized:
        return False

    # 如果描述是纯数字（如 seebug 的 3453）
    if desc.strip().isdigit():
        return False

    # 如果描述太短（少于5个字符），不算有效描述
    if len(desc.strip()) < 5:
        return False

    # 如果描述只是URL的路径部分
    try:
        parsed = urlparse(url)
        path_parts = [p for p in parsed.path.split('/') if p]
        for part in path_parts:
            part_lower = part.lower()
            if desc_lower == part_lower:
                return False
            # 移除后缀后比较
            for suffix in ['.html', '.htm', '.md']:
                if part_lower.endswith(suffix):
                    if desc_lower == part_lower[:-len(suffix)]:
                        return False
    except Exception:
        pass

    return True


def _run_git(repo_path: Path, args: List[str], *, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ['git', '-C', str(repo_path), *args],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='ignore',
        check=check,
    )


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
            'free.md': '🎁 免费资源',
            'pico.md': '🔌 PICO工具',
            'C2.md': '🎮 C2框架'
        }

    def get_week_range(self, date_str: str) -> Tuple[str, str]:
        """获取日期所在周的周一到周日"""
        date = datetime.strptime(date_str, "%Y-%m-%d")
        monday = date - timedelta(days=date.weekday())
        sunday = monday + timedelta(days=6)
        return monday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")

    def get_git_log(self, since_date: str = None) -> List[Dict]:
        """获取git提交日志"""
        args = ['log', '--pretty=format:%H|%ad|%s', '--date=format:%Y-%m-%d']
        if since_date:
            args.extend(['--since', since_date])

        try:
            result = _run_git(self.repo_path, args, check=True)
        except subprocess.CalledProcessError as e:
            print(f"? git log ??: {e}")
            if e.stderr:
                print(f"   stderr: {e.stderr.strip()[:200]}")
            return []

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
        try:
            result = _run_git(self.repo_path, ['show', commit_hash, '--format=', '--unified=0'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"? git show ??: {commit_hash}: {e}")
            if e.stderr:
                print(f"   stderr: {e.stderr.strip()[:200]}")
            return {}

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
        args = [
            'log',
            '--pretty=format:%H|%ad|%s',
            '--date=format:%Y-%m-%d',
            f'--since={week_start}',
            f'--until={week_end} 23:59:59',
        ]

        try:
            result = _run_git(self.repo_path, args, check=True)
        except subprocess.CalledProcessError as e:
            print(f"? git log ??: {e}")
            if e.stderr:
                print(f"   stderr: {e.stderr.strip()[:200]}")
            return {'commits': []}

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

    @dataclass(frozen=True)
    class GithubFetchResult:
        status: str  # ok | not_found | error | invalid
        content: Optional[str] = None
        http_status: Optional[int] = None
        error: Optional[str] = None

    @dataclass(frozen=True)
    class WebFetchResult:
        status: str  # ok | not_found | error
        content: Optional[str] = None
        http_status: Optional[int] = None
        error: Optional[str] = None

    def __init__(self, cache_dir: Path, config: Optional[Config] = None):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(exist_ok=True)
        self.cache_file = self.cache_dir / 'descriptions_cache.json'
        self.cache = self.load_cache()
        self.dirty = False  # 标记缓存是否被修改
        self.config = config or get_config()

    def load_cache(self) -> Dict:
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except JSONDecodeError:
                backup = self.cache_file.with_suffix(f".corrupt.{int(time.time())}.json")
                try:
                    self.cache_file.rename(backup)
                except OSError:
                    pass
                logger.warning(f"缓存文件 JSON 解析失败，已备份: {backup.name}")
        return {}

    def save_cache(self):
        """保存缓存（只在有修改时才写入文件）"""
        if not self.dirty:
            return  # 没有修改，跳过写入
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)
        self.dirty = False

    @staticmethod
    def _parse_github_repo(url: str) -> Optional[Tuple[str, str]]:
        try:
            parsed = urlparse(url)
        except Exception:
            return None

        if parsed.scheme.lower() != 'https':
            return None

        netloc = (parsed.netloc or '').lower()
        if netloc != 'github.com':
            return None

        parts = [p for p in (parsed.path or '').split('/') if p]
        if len(parts) < 2:
            return None

        owner = parts[0].strip()
        repo = parts[1].strip()
        if repo.endswith('.git'):
            repo = repo[:-4]

        if not owner or not repo:
            return None

        return owner, repo

    def is_github_url(self, url: str) -> bool:
        """判断是否为GitHub URL"""
        try:
            parsed = urlparse(url)
            return parsed.netloc.lower() == 'github.com'
        except Exception:
            return False

    def _fetch_with_retry(self, url: str, headers: dict, timeout: int = 10) -> requests.Response:
        """带重试的HTTP请求"""
        config = self.config
        current_delay = config.retry_delay

        for attempt in range(1, config.retry_max_attempts + 1):
            try:
                response = requests.get(url, headers=headers, timeout=timeout)
                return response
            except requests.RequestException as e:
                if attempt < config.retry_max_attempts:
                    logger.warning(f"    ⚠️ 请求失败 (第{attempt}次): {e}")
                    logger.info(f"    ⏳ {current_delay:.1f}秒后重试...")
                    time.sleep(current_delay)
                    current_delay *= config.retry_backoff
                else:
                    raise

    def fetch_github_content(self, url: str) -> "DescriptionGenerator.GithubFetchResult":
        """获取GitHub仓库的README内容（使用raw.githubusercontent.com，无API限制）"""
        repo_info = self._parse_github_repo(url)
        if not repo_info:
            return self.GithubFetchResult(status="invalid")

        owner, repo = repo_info

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        repo_page_url = f"https://github.com/{owner}/{repo}"
        try:
            page_response = self._fetch_with_retry(repo_page_url, headers, timeout=10)
        except requests.RequestException as e:
            return self.GithubFetchResult(status="error", error=str(e))

        if page_response.status_code == 404:
            return self.GithubFetchResult(status="not_found", http_status=404)

        description = ""
        if page_response.status_code == 200:
            desc_match = re.search(
                r'<meta\s+property="og:description"\s+content="([^"]*)"\s*/?>',
                page_response.text,
                flags=re.IGNORECASE,
            )
            if desc_match:
                description = desc_match.group(1)

        readme_content = ""
        readme_files = ['README.md', 'readme.md', 'README.MD', 'README', 'README.txt']
        for branch in ("main", "master"):
            for readme_name in readme_files:
                raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{readme_name}"
                try:
                    readme_response = self._fetch_with_retry(raw_url, headers, timeout=15)
                except requests.RequestException:
                    continue

                if readme_response.status_code == 200:
                    readme_content = readme_response.text[:3000]
                    break
            if readme_content:
                break

        if readme_content or description:
            content = f"Repository: {owner}/{repo}\n"
            if description:
                content += f"Description: {description}\n"
            if readme_content:
                content += f"\nREADME (excerpt):\n{readme_content}"
            return self.GithubFetchResult(status="ok", content=content, http_status=page_response.status_code)

        if page_response.status_code >= 400:
            return self.GithubFetchResult(
                status="error",
                http_status=page_response.status_code,
                error=(page_response.text or "")[:200],
            )

        return self.GithubFetchResult(status="error", http_status=page_response.status_code, error="No description/README found")

    def fetch_web_content(self, url: str) -> "DescriptionGenerator.WebFetchResult":
        """获取非GitHub网页内容"""
        fetcher = WebContentFetcher(self.config)
        result = fetcher.fetch_web_content(url)
        return self.WebFetchResult(
            status=result.status,
            content=result.content,
            http_status=result.http_status,
            error=result.error
        )

    def _call_ai_with_retry(self, payload: dict, headers: dict) -> requests.Response:
        """带重试的AI API请求"""
        config = self.config
        current_delay = config.retry_delay

        for attempt in range(1, config.retry_max_attempts + 1):
            try:
                response = requests.post(
                    config.ai_api_url,
                    json=payload,
                    headers=headers,
                    timeout=30
                )
                # 如果是速率限制错误，也需要重试
                if response.status_code == 429:
                    raise requests.RequestException(f"Rate limited: {response.status_code}")
                return response
            except requests.RequestException as e:
                if attempt < config.retry_max_attempts:
                    logger.warning(f"    ⚠️ AI请求失败 (第{attempt}次): {e}")
                    logger.info(f"    ⏳ {current_delay:.1f}秒后重试...")
                    time.sleep(current_delay)
                    current_delay *= config.retry_backoff
                else:
                    raise

    def call_ai_for_summary(self, url: str, content: str) -> Optional[str]:
        """调用AI接口生成中文摘要"""
        config = self.config

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

            headers = {
                "Content-Type": "application/json",
                "User-Agent": "claude-cli/2.1.20"
            }

            parsed = urlparse(config.ai_api_url)
            path = (parsed.path or "").lower().rstrip("/")
            is_anthropic_format = path.endswith("/v1/messages") or path.endswith("/messages")

            # 根据不同的AI接口格式调整请求
            if is_anthropic_format:
                payload = {
                    "model": config.ai_model,
                    "max_tokens": 100,
                    "messages": [{"role": "user", "content": prompt}]
                }
                headers["anthropic-version"] = "2023-06-01"

                # 优先使用 AUTH_TOKEN (OAuth)，否则使用 API_KEY
                if config.ai_auth_token:
                    headers["Authorization"] = f"Bearer {config.ai_auth_token}"
                elif config.ai_api_key:
                    headers["x-api-key"] = config.ai_api_key

            elif "ollama" in config.ai_api_url.lower():
                payload = {
                    "model": config.ai_model,
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False
                }
            else:
                payload = {
                    "model": config.ai_model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7,
                    "max_tokens": 100
                }
                if config.ai_auth_token:
                    headers["Authorization"] = f"Bearer {config.ai_auth_token}"
                elif config.ai_api_key:
                    headers["Authorization"] = f"Bearer {config.ai_api_key}"

            response = self._call_ai_with_retry(payload, headers)

            if response.status_code == 200:
                result = response.json()

                if is_anthropic_format:
                    description = result.get('content', [{}])[0].get('text', '').strip()
                elif "ollama" in config.ai_api_url.lower():
                    description = result.get('message', {}).get('content', '').strip()
                else:
                    description = result.get('choices', [{}])[0].get('message', {}).get('content', '').strip()

                description = description.strip('"\'').strip()
                return description
            else:
                logger.error(f"    ✗ AI API 错误: HTTP {response.status_code}")
                logger.debug(f"    ✗ 响应内容: {response.text[:200]}")
                return None

        except Exception as e:
            logger.error(f"    ✗ AI API 异常: {e}")
            return None

    def is_cached(self, url: str) -> bool:
        """检查URL是否已缓存"""
        return url in self.cache

    def get_cached(self, url: str) -> Optional[str]:
        """获取缓存的描述"""
        return self.cache.get(url)

    def generate_description(self, url: str) -> Optional[str]:
        """生成单个URL的描述（带缓存）- 支持GitHub和普通网页

        返回值:
        - 字符串: 正常描述
        - "__DELETED__": 链接404/不可用，应从文件中删除
        - None: 生成失败但可以重试
        """
        # 检查缓存
        if url in self.cache:
            return self.cache[url]

        # 根据URL类型选择抓取方式
        if self.is_github_url(url):
            fetch_result = self.fetch_github_content(url)
        else:
            fetch_result = self.fetch_web_content(url)

        if fetch_result.status == "not_found":
            self.cache[url] = "__DELETED__"
            self.dirty = True
            return "__DELETED__"

        if fetch_result.status != "ok" or not fetch_result.content:
            return None

        # 调用AI生成描述
        description = self.call_ai_for_summary(url, fetch_result.content)

        if description and len(description) > 5:
            self.cache[url] = description
            self.dirty = True  # 标记缓存已修改
            return description

        return None


class WebContentFetcher:
    """网页内容抓取器 - 智能提取非GitHub网页的正文内容"""

    @dataclass(frozen=True)
    class FetchResult:
        status: str  # ok | not_found | error
        content: Optional[str] = None
        http_status: Optional[int] = None
        error: Optional[str] = None

    def __init__(self, config: Optional[Config] = None):
        self.config = config or get_config()
        # 需要移除的标签
        self._remove_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside', 'noscript', 'iframe'}
        # 正文容器优先级
        self._content_selectors = ['article', 'main', '.post-content', '.article-content', '.entry-content', '#content']

    def _extract_title(self, html: str) -> str:
        """提取页面标题"""
        import re
        # 尝试 <title>
        match = re.search(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        # 尝试 <h1>
        match = re.search(r'<h1[^>]*>([^<]+)</h1>', html, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return ""

    def _extract_meta_description(self, html: str) -> str:
        """提取 meta description"""
        import re
        match = re.search(
            r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']',
            html, re.IGNORECASE
        )
        if match:
            return match.group(1).strip()
        # 尝试另一种顺序
        match = re.search(
            r'<meta\s+content=["\']([^"\']+)["\']\s+name=["\']description["\']',
            html, re.IGNORECASE
        )
        if match:
            return match.group(1).strip()
        return ""

    def _extract_og_description(self, html: str) -> str:
        """提取 Open Graph description"""
        import re
        match = re.search(
            r'<meta\s+property=["\']og:description["\']\s+content=["\']([^"\']+)["\']',
            html, re.IGNORECASE
        )
        if match:
            return match.group(1).strip()
        match = re.search(
            r'<meta\s+content=["\']([^"\']+)["\']\s+property=["\']og:description["\']',
            html, re.IGNORECASE
        )
        if match:
            return match.group(1).strip()
        return ""

    def _remove_unwanted_tags(self, html: str) -> str:
        """移除不需要的标签及其内容"""
        import re
        for tag in self._remove_tags:
            html = re.sub(
                rf'<{tag}[^>]*>.*?</{tag}>',
                '', html, flags=re.IGNORECASE | re.DOTALL
            )
            # 自闭合标签
            html = re.sub(rf'<{tag}[^>]*/>', '', html, flags=re.IGNORECASE)
        return html

    def _extract_text_from_html(self, html: str) -> str:
        """从HTML中提取纯文本"""
        import re
        # 移除所有标签
        text = re.sub(r'<[^>]+>', ' ', html)
        # 处理HTML实体
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&amp;', '&')
        text = text.replace('&quot;', '"')
        # 合并多个空白字符
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def _extract_main_content(self, html: str) -> str:
        """智能提取正文内容"""
        import re

        # 先移除干扰标签
        cleaned_html = self._remove_unwanted_tags(html)

        # 尝试找到正文容器
        content = ""

        # 1. 尝试 <article>
        match = re.search(r'<article[^>]*>(.*?)</article>', cleaned_html, re.IGNORECASE | re.DOTALL)
        if match:
            content = match.group(1)

        # 2. 尝试 <main>
        if not content:
            match = re.search(r'<main[^>]*>(.*?)</main>', cleaned_html, re.IGNORECASE | re.DOTALL)
            if match:
                content = match.group(1)

        # 3. 尝试带有 content/post/article 类名的 div
        if not content:
            match = re.search(
                r'<div[^>]*class=["\'][^"\']*(?:content|post|article|entry)[^"\']*["\'][^>]*>(.*?)</div>',
                cleaned_html, re.IGNORECASE | re.DOTALL
            )
            if match:
                content = match.group(1)

        # 4. 回退到 body
        if not content:
            match = re.search(r'<body[^>]*>(.*?)</body>', cleaned_html, re.IGNORECASE | re.DOTALL)
            if match:
                content = match.group(1)
            else:
                content = cleaned_html

        # 提取纯文本
        text = self._extract_text_from_html(content)
        return text

    def fetch_web_content(self, url: str) -> "WebContentFetcher.FetchResult":
        """抓取网页内容并智能提取正文"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5,zh-CN;q=0.3',
        }

        try:
            response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)

            if response.status_code == 404:
                return self.FetchResult(status="not_found", http_status=404)

            if response.status_code >= 400:
                return self.FetchResult(
                    status="error",
                    http_status=response.status_code,
                    error=f"HTTP {response.status_code}"
                )

            html = response.text

            # 提取各部分内容
            title = self._extract_title(html)
            meta_desc = self._extract_meta_description(html)
            og_desc = self._extract_og_description(html)
            main_content = self._extract_main_content(html)

            # 组合内容
            content_parts = []
            if title:
                content_parts.append(f"Title: {title}")
            if meta_desc:
                content_parts.append(f"Meta Description: {meta_desc}")
            elif og_desc:
                content_parts.append(f"Description: {og_desc}")
            if main_content:
                # 限制正文长度（增加到5000字符以获取更多上下文）
                truncated = main_content[:5000]
                content_parts.append(f"\nContent:\n{truncated}")

            if not content_parts:
                return self.FetchResult(
                    status="error",
                    http_status=response.status_code,
                    error="No extractable content"
                )

            return self.FetchResult(
                status="ok",
                content="\n".join(content_parts),
                http_status=response.status_code
            )

        except requests.Timeout:
            return self.FetchResult(status="error", error="Request timeout")
        except requests.RequestException as e:
            return self.FetchResult(status="error", error=str(e))


class WeeklyUpdater:
    """周报更新器 - 更新周报文件中的描述"""

    def __init__(self, weekly_dir: Path):
        self.weekly_dir = weekly_dir

    def extract_links_needing_descriptions(self, file_path: Path) -> List[str]:
        """提取需要描述的链接（空描述或无意义描述）"""
        links = []
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'\| \[([^\]]+)\]\((https://[^\)]+)\) \| ([^\|]*) \|'
        matches = re.findall(pattern, content)

        for _, url, desc in matches:
            desc = desc.strip()
            # 使用 is_meaningful_description 判断是否需要生成AI描述
            if not is_meaningful_description(desc, url) or '收集的项目地址' in desc:
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


class SourceFileUpdater:
    """源文件更新器 - 更新 docs.md/README.md 等源文件为表格格式"""

    # 需要处理的源文件列表
    SOURCE_FILES = ['docs.md', 'README.md', 'tools.md', 'BOF.md', 'skills-ai.md', 'pico.md', 'C2.md', 'free.md']

    def __init__(self):
        pass

    def extract_urls(self, file_path: Path) -> List[str]:
        """从文件中提取所有URL"""
        urls = []
        content = file_path.read_text(encoding='utf-8')

        # 匹配独立行的URL
        url_pattern = r'^(https?://[^\s]+)$'
        for match in re.finditer(url_pattern, content, re.MULTILINE):
            urls.append(match.group(1).strip())

        # 匹配markdown链接格式
        md_pattern = r'\[([^\]]+)\]\((https?://[^\)]+)\)'
        for match in re.finditer(md_pattern, content):
            url = match.group(2).strip()
            if url not in urls:
                urls.append(url)

        return urls

    def _extract_title_from_context(self, content: str, url: str) -> str:
        """从URL上下文提取标题"""
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if url in line:
                # 向上查找最近的标题行
                for j in range(i - 1, max(0, i - 5), -1):
                    title_match = re.match(r'^#{1,6}\s+(.+)$', lines[j].strip())
                    if title_match:
                        return title_match.group(1).strip()
                break
        # 从URL提取名称作为回退
        return url.rstrip('/').split('/')[-1]

    def _group_urls_by_section(self, file_path: Path) -> Dict[str, List[Tuple[str, str, str]]]:
        """按章节分组URL，返回 {section_title: [(url, original_title, existing_desc), ...]}

        支持两种格式:
        1. 原始格式: #### 标题 + URL单独一行
        2. 表格格式: | [标题](URL) | 描述 |
        """
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')

        sections = {}
        current_section = "默认"
        current_title = ""

        for line in lines:
            stripped = line.strip()

            # 检测一级或二级标题作为章节
            section_match = re.match(r'^(#{1,2})\s+(.+)$', stripped)
            if section_match:
                current_section = section_match.group(2).strip()
                continue

            # 检测三级及以下标题作为条目标题
            title_match = re.match(r'^#{3,6}\s+(.+)$', stripped)
            if title_match:
                current_title = title_match.group(1).strip()
                continue

            # 检测表格行格式: | [标题](URL) | 描述 |
            table_match = re.match(r'^\|\s*\[([^\]]+)\]\((https?://[^\)]+)\)\s*\|\s*(.*?)\s*\|$', stripped)
            if table_match:
                title = table_match.group(1).strip()
                url = table_match.group(2).strip()
                existing_desc = table_match.group(3).strip()
                if current_section not in sections:
                    sections[current_section] = []
                sections[current_section].append((url, title, existing_desc))
                continue

            # 检测URL（原始格式）
            url_match = re.match(r'^(https?://[^\s]+)$', stripped)
            if url_match:
                url = url_match.group(1)
                if current_section not in sections:
                    sections[current_section] = []
                sections[current_section].append((url, current_title or url.split('/')[-1], ""))
                current_title = ""  # 重置标题

        return sections

    def update_source_file(self, file_path: Path, descriptions: Dict[str, str]) -> Tuple[int, int]:
        """更新源文件为表格格式

        返回: (更新数量, 删除数量)
        """
        sections = self._group_urls_by_section(file_path)

        if not sections:
            return 0, 0

        # 读取原始文件获取主标题
        original_content = file_path.read_text(encoding='utf-8')
        main_title_match = re.match(r'^#\s+(.+)$', original_content, re.MULTILINE)
        main_title = main_title_match.group(1) if main_title_match else file_path.stem

        # 创建备份文件
        backup_path = file_path.with_suffix(file_path.suffix + '.bak')
        backup_path.write_text(original_content, encoding='utf-8')
        logger.info(f"  📦 已创建备份: {backup_path.name}")

        # 构建新内容
        new_lines = [f"# {main_title}\n"]
        updated = 0
        deleted = 0

        for section, url_tuples in sections.items():
            # 先统计本章节有效的URL数量
            valid_rows = []
            section_deleted = 0

            for url, title, existing_desc in url_tuples:
                # 优先使用新生成的描述，否则保留已有描述
                desc = descriptions.get(url, "")

                if desc == "__DELETED__":
                    section_deleted += 1
                    continue

                if desc:
                    updated += 1
                elif existing_desc:
                    # 保留已有描述（表格格式中已有的）
                    desc = existing_desc
                else:
                    desc = ""  # 保留空描述

                # 使用URL最后一段作为显示名称
                display_name = title or url.rstrip('/').split('/')[-1]
                valid_rows.append(f"| [{display_name}]({url}) | {desc} |\n")

            deleted += section_deleted

            # 跳过空章节（所有URL都被删除的情况）
            if not valid_rows:
                continue

            # 添加章节标题
            if section != main_title and section != "默认":
                new_lines.append(f"\n## {section}\n")

            # 添加表格
            new_lines.append("\n| 文章 | 简介 |")
            new_lines.append("\n|------|------|\n")
            new_lines.extend(valid_rows)

        # 写入文件
        file_path.write_text(''.join(new_lines), encoding='utf-8')

        return updated, deleted

    def get_source_files(self, repo_path: Path) -> List[Path]:
        """获取需要处理的源文件列表"""
        files = []
        for filename in self.SOURCE_FILES:
            file_path = repo_path / filename
            if file_path.exists():
                files.append(file_path)
        return files


class AutoWeeklyProcessor:
    """完全自动化的周报处理器"""

    def __init__(self, repo_path: Optional[str] = None, config: Optional[Config] = None):
        self.config = config or get_config()
        self.repo_path = Path(repo_path) if repo_path else self.config.repo_path
        self.generator = WeeklyGenerator(str(self.repo_path))
        self.desc_gen = DescriptionGenerator(self.config.cache_dir, self.config)
        self.updater = WeeklyUpdater(self.config.weekly_dir)
        self.source_updater = SourceFileUpdater()

    def _process_links(self, links: List[str], max_links: int, show_progress: bool = True) -> Dict[str, str]:
        """
        处理链接列表，生成描述（公共方法，消除代码重复）

        Args:
            links: 需要处理的链接列表
            max_links: 最大处理数量
            show_progress: 是否显示进度条

        Returns:
            Dict[str, str]: URL -> 描述的映射
        """
        if len(links) > max_links:
            logger.info(f"⚠️  链接较多，本次只处理前 {max_links} 个")
            links = links[:max_links]

        descriptions = {}
        config = self.config

        # 初始化进度条
        progress = ProgressBar(len(links), desc="处理链接") if show_progress else None

        for j, url in enumerate(links, 1):
            if not show_progress:
                logger.info(f"\n  [{j}/{len(links)}] {url}")

            # 先检查缓存
            if self.desc_gen.is_cached(url):
                desc = self.desc_gen.get_cached(url)
                if desc == "__DELETED__":
                    if not show_progress:
                        logger.info(f"    ⊘ 跳过 (链接不可用)")
                else:
                    if not show_progress:
                        logger.info(f"    ✓ 缓存命中: {desc}")
                descriptions[url] = desc
                if progress:
                    progress.update()
                continue

            # 没有缓存，需要网络请求
            if not show_progress:
                logger.info(f"    → 获取GitHub内容...")

            desc = self.desc_gen.generate_description(url)

            if desc == "__DELETED__":
                if not show_progress:
                    logger.info(f"    ⊘ 链接不可用 (404)")
                descriptions[url] = desc
            elif desc:
                if not show_progress:
                    logger.info(f"    ✓ 生成: {desc}")
                descriptions[url] = desc

                # 定期保存缓存
                if j % config.cache_save_interval == 0:
                    self.desc_gen.save_cache()
                    if not show_progress:
                        logger.info(f"    💾 已保存缓存 ({j}/{len(links)})")
            else:
                if not show_progress:
                    logger.info(f"    ✗ 生成失败")

            if progress:
                progress.update()

            # 只在网络请求后才sleep
            time.sleep(config.request_delay)

        if progress:
            progress.finish()

        # 最终保存缓存
        self.desc_gen.save_cache()

        return descriptions

    def _process_weekly_file(self, file_path: Path, max_links: int, file_index: int = 0,
                              total_files: int = 0, show_progress: bool = True) -> Tuple[int, int]:
        """
        处理单个周报文件（公共方法，消除代码重复）

        Args:
            file_path: 周报文件路径
            max_links: 最大处理链接数
            file_index: 当前文件索引（用于显示进度）
            total_files: 总文件数（用于显示进度）
            show_progress: 是否显示进度条

        Returns:
            Tuple[int, int]: (更新数量, 删除数量)
        """
        filename = file_path.name

        if file_index > 0 and total_files > 0:
            logger.info(f"\n{'='*60}")
            logger.info(f"[{file_index}/{total_files}] 处理: {filename}")
            logger.info('='*60)
        else:
            logger.info(f"\n处理: {filename}")

        links = self.updater.extract_links_needing_descriptions(file_path)

        if not links:
            logger.info("  ✓ 所有链接都已有描述")
            return 0, 0

        logger.info(f"📊 发现 {len(links)} 个需要描述的链接")

        # 处理链接
        descriptions = self._process_links(links, max_links, show_progress)

        # 更新文件
        if descriptions:
            logger.info(f"\n📝 更新周报文件...")
            updated, deleted = self.updater.update_weekly_file(file_path, descriptions)
            if updated > 0:
                logger.info(f"✅ 成功更新 {updated} 个描述到 {filename}")
            if deleted > 0:
                logger.info(f"🗑️  删除 {deleted} 个无效链接")
            return updated, deleted
        else:
            logger.info(f"\n⚠️  没有成功生成任何描述")
            return 0, 0

    def process_existing_weeklies(self, max_links_per_week: int = None):
        """仅为已有周报生成描述（非交互模式）"""
        if max_links_per_week is None:
            max_links_per_week = self.config.max_links_per_week

        logger.info("\n" + "="*60)
        logger.info("📝 为所有已存在的周报文件生成描述")
        logger.info("="*60)
        logger.info(f"📊 每周最多处理: {max_links_per_week} 个链接\n")

        weekly_dir = self.config.weekly_dir
        weekly_files = sorted([
            f for f in os.listdir(str(weekly_dir))
            if f.startswith('weekly-') and f.endswith('.md')
        ])

        logger.info(f"发现 {len(weekly_files)} 个周报文件\n")

        total_updated = 0
        total_deleted = 0

        for i, filename in enumerate(weekly_files, 1):
            file_path = weekly_dir / filename
            updated, deleted = self._process_weekly_file(
                file_path, max_links_per_week,
                file_index=i, total_files=len(weekly_files),
                show_progress=False
            )
            total_updated += updated
            total_deleted += deleted

        logger.info("\n" + "="*60)
        logger.info("🎉 所有周报处理完成！")
        logger.info(f"📊 总计更新: {total_updated} 个描述，删除: {total_deleted} 个无效链接")
        logger.info("="*60)

    def process_current_week(self, max_links: int = None):
        """生成当前周的周报（含AI描述）"""
        if max_links is None:
            max_links = self.config.max_links_per_week

        logger.info("\n" + "="*60)
        logger.info("📅 生成当前周的周报")
        logger.info("="*60)

        # 获取当前周的日期范围
        today = datetime.now()
        days_since_monday = today.weekday()
        monday = today - timedelta(days=days_since_monday)
        sunday = monday + timedelta(days=6)

        week_start = monday.strftime('%Y-%m-%d')
        week_end = sunday.strftime('%Y-%m-%d')

        logger.info(f"📊 当前周期: {week_start} ~ {week_end}")
        logger.info(f"📊 最多处理: {max_links} 个链接\n")

        # 生成本周的周报文件
        weekly_dir = self.config.weekly_dir
        filename = f"weekly-{week_start}_{week_end}.md"
        file_path = weekly_dir / filename

        logger.info(f"📝 生成周报文件: {filename}")

        # 获取本周的Git提交
        weekly_data = self.generator.get_weekly_commits(week_start, week_end)

        if not weekly_data['commits']:
            logger.warning(f"⚠️  本周 ({week_start} ~ {week_end}) 没有提交记录")
            return

        logger.info(f"✓ 发现 {len(weekly_data['commits'])} 个提交")

        # 提取所有链接
        links_by_file = self.generator.extract_links_from_diffs(weekly_data['commits'])
        total_links = sum(len(links) for links in links_by_file.values())
        logger.info(f"✓ 提取 {total_links} 个链接")

        if total_links == 0:
            logger.warning("⚠️  本周没有新增链接")
            return

        # 生成markdown内容
        content = self.generator.generate_markdown(week_start, week_end, weekly_data, links_by_file)

        # 保存文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        logger.info(f"✓ 周报文件已生成: {file_path}")

        # 为链接生成描述
        logger.info(f"\n{'='*60}")
        logger.info("🤖 开始为链接生成AI描述...")
        logger.info('='*60)

        updated, deleted = self._process_weekly_file(file_path, max_links, show_progress=False)

        logger.info("\n" + "="*60)
        logger.info(f"🎉 当前周周报生成完成！")
        logger.info(f"📄 文件位置: {file_path}")
        logger.info("="*60)

    def process_all(self, start_date: str = "2025-07-21", max_links_per_week: int = None):
        """完全自动化处理"""
        if max_links_per_week is None:
            max_links_per_week = self.config.max_links_per_week

        config = self.config

        logger.info("\n" + "="*60)
        logger.info("🚀 启动完全自动化周报生成流程")
        logger.info("="*60)
        logger.info(f"📍 仓库路径: {self.repo_path}")
        logger.info(f"🤖 AI模型: {config.ai_model}")
        logger.info(f"📊 每周最多处理: {max_links_per_week} 个链接\n")

        # 步骤1: 生成周报文件
        generated_files = self.generator.generate_weekly_files(start_date)

        if not generated_files:
            logger.warning("\n⚠️  没有可处理的周报文件")
            return

        # 步骤2: 为每个周报生成描述
        logger.info("\n" + "="*60)
        logger.info("📝 第二步：生成项目描述并更新周报")
        logger.info("="*60)

        weekly_dir = self.config.weekly_dir
        total_updated = 0
        total_deleted = 0

        for i, filename in enumerate(generated_files, 1):
            file_path = weekly_dir / filename

            logger.info(f"\n{'#'*60}")
            logger.info(f"# [{i}/{len(generated_files)}] 处理: {filename}")
            logger.info(f"{'#'*60}")

            updated, deleted = self._process_weekly_file(
                file_path, max_links_per_week,
                show_progress=False
            )
            total_updated += updated
            total_deleted += deleted

        logger.info("\n" + "="*60)
        logger.info("🎉 所有周报处理完成！")
        logger.info(f"📊 总计更新: {total_updated} 个描述，删除: {total_deleted} 个无效链接")
        logger.info("="*60)

    def process_source_files(self, max_links: int = None):
        """处理源文件（docs.md, README.md 等）- 生成描述并转换为表格格式"""
        if max_links is None:
            max_links = self.config.max_links_per_week

        logger.info("\n" + "="*60)
        logger.info("📄 处理源文件（生成描述并转换为表格格式）")
        logger.info("="*60)

        # 获取源文件列表
        source_files = self.source_updater.get_source_files(self.repo_path)

        if not source_files:
            logger.warning("⚠️  未找到需要处理的源文件")
            return

        logger.info(f"📊 发现 {len(source_files)} 个源文件")
        for f in source_files:
            logger.info(f"   - {f.name}")
        logger.info("")

        total_updated = 0
        total_deleted = 0

        for i, file_path in enumerate(source_files, 1):
            logger.info(f"\n{'='*60}")
            logger.info(f"[{i}/{len(source_files)}] 处理: {file_path.name}")
            logger.info('='*60)

            # 提取URL
            urls = self.source_updater.extract_urls(file_path)

            if not urls:
                logger.info("  ✓ 没有需要处理的URL")
                continue

            logger.info(f"📊 发现 {len(urls)} 个URL")

            # 限制处理数量
            if len(urls) > max_links:
                logger.info(f"⚠️  链接较多，本次只处理前 {max_links} 个")
                urls = urls[:max_links]

            # 生成描述
            descriptions = {}
            progress = ProgressBar(len(urls), desc="处理URL")

            for url in urls:
                # 检查缓存
                if self.desc_gen.is_cached(url):
                    desc = self.desc_gen.get_cached(url)
                else:
                    desc = self.desc_gen.generate_description(url)
                    time.sleep(self.config.request_delay)

                if desc:
                    descriptions[url] = desc

                progress.update()

            progress.finish()

            # 保存缓存
            self.desc_gen.save_cache()

            # 更新源文件
            if descriptions:
                logger.info(f"\n📝 更新源文件为表格格式...")
                updated, deleted = self.source_updater.update_source_file(file_path, descriptions)
                logger.info(f"✅ 更新 {updated} 个描述，删除 {deleted} 个无效链接")
                total_updated += updated
                total_deleted += deleted

        logger.info("\n" + "="*60)
        logger.info("🎉 源文件处理完成！")
        logger.info(f"📊 总计更新: {total_updated} 个描述，删除: {total_deleted} 个无效链接")
        logger.info("="*60)

    def commit_changes(self):
        """提交周报文件和缓存的变更"""
        logger.info("\n" + "="*60)
        logger.info("提交周报变更")
        logger.info("="*60)

        try:
            # 检查变更
            logger.info("1. 检查 'git status'...")
            status_result = subprocess.run(
                ['git', '-C', str(self.repo_path), 'status', '--short'],
                capture_output=True, text=True, encoding='utf-8', errors='ignore'
            )
            if not status_result.stdout.strip():
                logger.info("✅ 没有检测到任何变更，无需提交。")
                return

            logger.info("检测到以下变更:")
            logger.info(status_result.stdout)

            # 添加周报文件
            logger.info("2. 添加变更到暂存区...")
            subprocess.run(
                ['git', '-C', str(self.repo_path), 'add', 'weekly/*.md'],
                check=True
            )
            subprocess.run(
                ['git', '-C', str(self.repo_path), 'add', '-f', 'links_cache/descriptions_cache.json'],
                check=True
            )
            logger.info("  ✓ 'weekly/' 目录下的 .md 文件")
            logger.info("  ✓ 'links_cache/descriptions_cache.json'")

            # 提交变更
            commit_message = f"docs: weekly update {datetime.now().strftime('%Y-%m-%d')}"
            logger.info(f"3. 提交变更，提交信息: '{commit_message}'...")
            subprocess.run(
                ['git', '-C', str(self.repo_path), 'commit', '-m', commit_message],
                check=True,
                capture_output=True, text=True, encoding='utf-8', errors='ignore'
            )
            logger.info("✅ 变更已成功提交！")

        except subprocess.CalledProcessError as e:
            logger.error(f"❌ 提交过程中发生错误: {e}")
            logger.error(f"  → Stderr: {e.stderr}")
        except Exception as e:
            logger.error(f"❌ 发生未知错误: {e}")

    # ==================== 新增：全自动模式 ====================

    def run_auto_mode(self, max_links: int = None):
        """
        全自动模式：从Git diff提取本周新增URL → 生成AI描述 → 生成周报 → Git提交

        这是功能1-5的合并版本，一键完成所有操作。
        """
        if max_links is None:
            max_links = self.config.max_links_per_week

        logger.info("\n" + "="*60)
        logger.info("🚀 全自动周报生成模式")
        logger.info("="*60)

        # Step 1: 计算当前周范围
        week_start, week_end = self._get_current_week_range()
        logger.info(f"📅 周期: {week_start} ~ {week_end}")

        # Step 2: 获取本周的Git提交
        weekly_data = self.generator.get_weekly_commits(week_start, week_end)

        if not weekly_data['commits']:
            logger.info("\n⚠️  本周没有提交记录，无需生成周报")
            return

        logger.info(f"\n📝 发现 {len(weekly_data['commits'])} 个提交")

        # Step 3: 从Git diff中提取本周新增的链接（核心修复点）
        links_by_file = self.generator.extract_links_from_diffs(weekly_data['commits'])

        if not links_by_file:
            logger.info("\n⚠️  本周没有新增链接")
            return

        # Step 4: 转换为按分类组织的格式
        urls_by_category = self._convert_links_to_category_format(links_by_file)

        total_urls = sum(len(urls) for urls in urls_by_category.values())
        logger.info(f"\n🔗 本周新增 {total_urls} 个链接，分布在 {len(urls_by_category)} 个分类")

        # Step 5: 筛选需要生成描述的URL（空描述或无意义描述的）
        urls_needing_desc = []
        for category, url_list in urls_by_category.items():
            for url, title, existing_desc in url_list:
                # 使用 _is_meaningful_description 判断是否需要生成AI描述
                if not self._is_meaningful_description(existing_desc, url):
                    urls_needing_desc.append(url)

        logger.info(f"📊 其中 {len(urls_needing_desc)} 个需要生成AI描述")

        # Step 5: 生成AI描述
        descriptions = {}
        if urls_needing_desc:
            logger.info("\n" + "-"*40)
            logger.info("🤖 生成AI描述...")
            logger.info("-"*40)
            descriptions = self._process_links(urls_needing_desc, max_links, show_progress=True)

        # Step 6: 生成周报文件
        logger.info("\n" + "-"*40)
        logger.info("📝 生成周报文件...")
        logger.info("-"*40)

        weekly_file = self._generate_weekly_file(week_start, week_end, urls_by_category, descriptions)
        logger.info(f"✅ 周报已生成: {weekly_file.name}")

        # Step 7: 统计
        updated_count = len([d for d in descriptions.values() if d and d != "__DELETED__"])
        deleted_count = len([d for d in descriptions.values() if d == "__DELETED__"])

        # Step 8: Git提交
        logger.info("\n" + "-"*40)
        logger.info("📤 提交变更...")
        logger.info("-"*40)
        self.commit_changes()

        # 完成
        logger.info("\n" + "="*60)
        logger.info("🎉 全自动模式完成！")
        logger.info(f"📄 周报文件: {weekly_file}")
        logger.info(f"📊 新增描述: {updated_count}，删除无效链接: {deleted_count}")
        logger.info("="*60)

    def _get_current_week_range(self) -> Tuple[str, str]:
        """获取当前周一到周日的日期范围"""
        today = datetime.now()
        days_since_monday = today.weekday()
        monday = today - timedelta(days=days_since_monday)
        sunday = monday + timedelta(days=6)
        return monday.strftime('%Y-%m-%d'), sunday.strftime('%Y-%m-%d')

    def _is_meaningful_description(self, desc: str, url: str) -> bool:
        """判断描述是否有意义（包装全局函数）"""
        return is_meaningful_description(desc, url)

    def _convert_links_to_category_format(self, links_by_file: Dict[str, List[Dict]]) -> Dict[str, List[Tuple[str, str, str]]]:
        """
        将 WeeklyGenerator 返回的格式转换为 _generate_weekly_file 期望的格式

        输入格式: {filename: [{'url': url, 'desc': desc}, ...]}
        输出格式: {category: [(url, title, existing_desc), ...]}
        """
        # 文件到分类的映射
        category_map = {
            'README.md': '📦 收集的项目',
            'tools.md': '🔧 收集的工具',
            'BOF.md': '🎯 BOF工具',
            'skills-ai.md': '🤖 AI使用技巧',
            'docs.md': '📚 收集的文章',
            'free.md': '🎁 免费资源',
            'pico.md': '🔌 PICO工具',
            'C2.md': '🎮 C2框架'
        }

        urls_by_category = {}

        for filename, links in links_by_file.items():
            category = category_map.get(filename, f'📁 {filename}')

            if category not in urls_by_category:
                urls_by_category[category] = []

            for link in links:
                url = link['url']
                desc = link.get('desc', '')
                # 从URL提取标题
                title = url.rstrip('/').split('/')[-1]
                # 转换为 (url, title, existing_desc) 格式
                # 去重检查
                existing_urls = [u[0] for u in urls_by_category[category]]
                if url not in existing_urls:
                    urls_by_category[category].append((url, title, desc))

        return urls_by_category

    def _get_changed_source_files(self, week_start: str, week_end: str) -> List[Path]:
        """
        检测本周变更的源文件（仅SOURCE_FILES范围内）

        使用git log检测指定时间范围内有变更的文件
        """
        source_files = set(self.source_updater.SOURCE_FILES)
        changed_files = []
        changed_set = set()

        try:
            # 使用git log获取时间范围内有变更的文件
            result = subprocess.run(
                ['git', '-C', str(self.repo_path), 'log',
                 f'--since={week_start}', f'--until={week_end}',
                 '--pretty=format:', '--name-only'],
                capture_output=True, text=True, encoding='utf-8', errors='ignore',
                check=True
            )

            # 解析变更的文件列表
            stdout_content = result.stdout.strip()
            if stdout_content:
                for line in stdout_content.split('\n'):
                    filename = line.strip()
                    if filename and filename in source_files:
                        changed_set.add(filename)

            # 转换为Path对象
            for filename in changed_set:
                file_path = self.repo_path / filename
                if file_path.exists():
                    changed_files.append(file_path)

        except subprocess.CalledProcessError as e:
            logger.warning(f"⚠️  Git命令执行失败: {e}")
            # 回退方案：检查所有源文件
            logger.info("📌 使用回退方案：处理所有存在的源文件")
            changed_files = self.source_updater.get_source_files(self.repo_path)

        return sorted(changed_files, key=lambda p: p.name)

    def _collect_urls_from_sources(self, source_files: List[Path]) -> Dict[str, List[Tuple[str, str, str]]]:
        """
        从源文件提取URL并按分类组织

        返回: {category_name: [(url, title, existing_desc), ...]}
        """
        # 分类映射
        category_map = {
            'README.md': '📦 收集的项目',
            'tools.md': '🔧 收集的工具',
            'BOF.md': '🎯 BOF工具',
            'skills-ai.md': '🤖 AI使用技巧',
            'docs.md': '📚 收集的文章',
            'free.md': '🎁 免费资源',
            'pico.md': '🔌 PICO工具',
            'C2.md': '🎮 C2框架'
        }

        urls_by_category = {}

        for file_path in source_files:
            filename = file_path.name
            category = category_map.get(filename, f'📁 {filename}')

            # 使用SourceFileUpdater的方法提取URL
            sections = self.source_updater._group_urls_by_section(file_path)

            # 将所有section的URL合并到对应分类
            for section, url_tuples in sections.items():
                if category not in urls_by_category:
                    urls_by_category[category] = []

                # url_tuples是 [(url, title, existing_desc), ...]
                for url_tuple in url_tuples:
                    # 去重：检查URL是否已存在
                    existing_urls = [u[0] for u in urls_by_category[category]]
                    if url_tuple[0] not in existing_urls:
                        urls_by_category[category].append(url_tuple)

        return urls_by_category

    def _generate_weekly_file(self, week_start: str, week_end: str,
                               urls_by_category: Dict[str, List[Tuple[str, str, str]]],
                               new_descriptions: Dict[str, str]) -> Path:
        """
        生成周报Markdown文件

        Args:
            week_start: 周开始日期
            week_end: 周结束日期
            urls_by_category: {category: [(url, title, existing_desc), ...]}
            new_descriptions: {url: new_description} 新生成的描述

        Returns:
            生成的周报文件路径
        """
        weekly_dir = self.config.weekly_dir
        filename = f"weekly-{week_start}_{week_end}.md"
        file_path = weekly_dir / filename

        # 构建内容
        lines = [f"# 本周更新 ({week_start} ~ {week_end})\n"]

        total_links = 0
        deleted_count = 0

        for category in sorted(urls_by_category.keys()):
            url_list = urls_by_category[category]

            if not url_list:
                continue

            # 过滤掉被删除的URL
            valid_rows = []
            for url, title, existing_desc in url_list:
                # 检查新描述
                new_desc = new_descriptions.get(url, "")

                if new_desc == "__DELETED__":
                    deleted_count += 1
                    continue

                # 优先使用新描述
                if new_desc:
                    desc = new_desc
                # 检查已有描述是否有意义（不仅仅是URL路径名）
                elif self._is_meaningful_description(existing_desc, url):
                    desc = existing_desc
                else:
                    # 无意义的描述，显示为空
                    desc = ""

                # 使用title或从URL提取名称
                display_name = title if title else url.rstrip('/').split('/')[-1]
                valid_rows.append((display_name, url, desc))

            if not valid_rows:
                continue

            # 添加分类标题和表格
            lines.append(f"\n## {category}\n")
            lines.append("\n| 项目 | 说明 |")
            lines.append("\n|------|------|\n")

            for name, url, desc in valid_rows:
                lines.append(f"| [{name}]({url}) | {desc} |\n")
                total_links += 1

        # 添加统计信息
        lines.append(f"\n---\n\n")
        lines.append(f"**统计：** 本周新增 {total_links} 个链接。\n")

        # 写入文件
        file_path.write_text(''.join(lines), encoding='utf-8')

        return file_path


def main():
    """主函数"""
    # 记录开始时间
    script_start_time = time.time()

    # 设置控制台编码 (Windows)
    if sys.platform == 'win32':
        try:
            import codecs
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'ignore')
        except:
            pass

    logger.info("""
╔════════════════════════════════════════════════════════════╗
║         自动化周报生成工具 v2.0                             ║
║   Git变更检测 → 提取URL → AI描述 → 生成周报 → 自动提交     ║
╚════════════════════════════════════════════════════════════╝
""")

    # 初始化配置
    config = get_config()

    # 检查认证配置（支持两种方式）
    if not config.ai_api_key and not config.ai_auth_token:
        logger.error("❌ 错误：未设置认证信息")
        logger.info("\n请设置以下任一环境变量：")
        logger.info("  方式1 - API Key:")
        logger.info("    Windows: $env:ANTHROPIC_API_KEY='your-key'")
        logger.info("    Linux:   export ANTHROPIC_API_KEY='your-key'")
        logger.info("\n  方式2 - OAuth Token:")
        logger.info("    Windows: $env:ANTHROPIC_AUTH_TOKEN='your-token'")
        logger.info("    Linux:   export ANTHROPIC_AUTH_TOKEN='your-token'")
        return

    # 显示当前配置
    if config.ai_auth_token:
        logger.info(f"🔐 认证方式: OAuth Token (ANTHROPIC_AUTH_TOKEN)")
    else:
        logger.info(f"🔐 认证方式: API Key (ANTHROPIC_API_KEY)")

    logger.info(f"📍 仓库路径: {config.repo_path}")
    logger.info(f"🤖 AI模型: {config.ai_model}")

    # 选择模式（简化为2个选项）
    logger.info("\n请选择运行模式：")
    logger.info("1. 全自动生成周报（检测本周变更 → AI描述 → 生成周报 → 自动提交）")
    logger.info("2. 处理源文件（docs.md等转表格 + AI描述）")

    choice = input("\n请输入选项 (1/2): ").strip()

    processor = AutoWeeklyProcessor(config=config)

    if choice == "1":
        # 全自动模式（合并原功能1-5）
        logger.info("\n此模式将自动完成：检测本周变更 → 生成AI描述 → 生成周报 → 自动提交")
        max_links = int(input(f"\n最多处理链接数 (默认: {config.max_links_per_week}): ").strip() or str(config.max_links_per_week))
        processor.run_auto_mode(max_links=max_links)

    elif choice == "2":
        # 处理源文件（保留原功能6）
        logger.info("\n此模式将处理 docs.md、README.md 等源文件")
        logger.info("  - 提取所有URL（GitHub + 普通网页）")
        logger.info("  - 使用AI生成中文简介")
        logger.info("  - 转换为表格格式")
        max_links = int(input(f"\n最多处理链接数 (默认: {config.max_links_per_week}): ").strip() or str(config.max_links_per_week))
        processor.process_source_files(max_links)

    else:
        logger.error("❌ 无效的选项")

    # 打印总运行时间
    total_time = time.time() - script_start_time
    logger.info(f"\n⏱️  总运行时间: {format_duration(total_time)}")


if __name__ == "__main__":
    main()
