#!/usr/bin/env python3
"""
缓存写入脚本
向 JSON 缓存文件写入或更新 URL 描述

用法:
    python cache_write.py <url> <description> [--cache-file <path>]

返回值:
    0: 写入成功
    1: 写入失败
"""
import sys
import json
import argparse
import time
from pathlib import Path


def write_cache(url: str, description: str, cache_file: Path) -> tuple[int, str]:
    """
    写入缓存

    Args:
        url: URL
        description: 描述文本
        cache_file: 缓存文件路径

    Returns:
        (exit_code, message)
        - (0, success_msg): 写入成功
        - (1, error_msg): 写入失败
    """
    # 确保目录存在
    cache_file.parent.mkdir(parents=True, exist_ok=True)

    # 读取现有缓存
    cache = {}
    if cache_file.exists():
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                cache = json.load(f)
        except json.JSONDecodeError as e:
            # JSON 损坏，备份并重新开始
            backup = cache_file.with_suffix(f".corrupt.{int(time.time())}.json")
            try:
                cache_file.rename(backup)
                return (1, f"缓存文件损坏，已备份到 {backup.name}，请检查")
            except Exception as e:
                return (1, f"缓存文件损坏且无法备份: {e}")
        except Exception as e:
            return (1, f"读取缓存失败: {e}")

    # 更新缓存
    is_new = url not in cache
    cache[url] = description

    # 写入文件
    try:
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
    except Exception as e:
        return (1, f"写入文件失败: {e}")

    action = "新增" if is_new else "更新"
    return (0, f"{action}成功: {url}")


def main():
    parser = argparse.ArgumentParser(
        description='写入 URL 缓存描述',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    # 写入新的 URL 描述
    python cache_write.py "https://github.com/user/repo" "这是一个很棒的项目"

    # 指定缓存文件路径
    python cache_write.py "https://github.com/user/repo" "描述" --cache-file ./my_cache.json

退出码:
    0 - 写入成功
    1 - 写入失败
        """
    )

    parser.add_argument('url', help='URL')
    parser.add_argument('description', help='描述文本')
    parser.add_argument(
        '--cache-file',
        type=Path,
        default=Path('links_cache/descriptions_cache.json'),
        help='缓存文件路径 (默认: links_cache/descriptions_cache.json)'
    )

    args = parser.parse_args()

    exit_code, message = write_cache(args.url, args.description, args.cache_file)

    print(message)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
