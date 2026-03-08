#!/usr/bin/env python3
"""
缓存查询脚本
从 JSON 缓存文件中查询指定 URL 的描述

用法:
    python cache_query.py <url> [--cache-file <path>]

返回值:
    0: 找到缓存，输出描述文本
    1: 未找到缓存
    2: 错误（文件不存在、JSON 解析失败等）
"""
import sys
import json
import argparse
from pathlib import Path


def query_cache(url: str, cache_file: Path) -> tuple[int, str]:
    """
    查询缓存

    Args:
        url: 要查询的 URL
        cache_file: 缓存文件路径

    Returns:
        (exit_code, message)
        - (0, description): 找到缓存
        - (1, "NOT_FOUND"): 未找到缓存
        - (2, error_msg): 错误
    """
    # 检查文件是否存在
    if not cache_file.exists():
        return (1, "NOT_FOUND")

    # 读取并解析 JSON
    try:
        with open(cache_file, 'r', encoding='utf-8') as f:
            cache = json.load(f)
    except json.JSONDecodeError as e:
        return (2, f"JSON 解析失败: {e}")
    except Exception as e:
        return (2, f"读取文件失败: {e}")

    # 查询 URL
    if url in cache:
        description = cache[url]
        # 检查是否为删除标记
        if description == "__DELETED__":
            return (1, "DELETED")
        return (0, description)
    else:
        return (1, "NOT_FOUND")


def main():
    parser = argparse.ArgumentParser(
        description='查询 URL 缓存描述',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    # 查询单个 URL
    python cache_query.py "https://github.com/user/repo"

    # 指定缓存文件路径
    python cache_query.py "https://github.com/user/repo" --cache-file ./my_cache.json

退出码:
    0 - 找到缓存
    1 - 未找到缓存
    2 - 错误
        """
    )

    parser.add_argument('url', help='要查询的 URL')
    parser.add_argument(
        '--cache-file',
        type=Path,
        default=Path('links_cache/descriptions_cache.json'),
        help='缓存文件路径 (默认: links_cache/descriptions_cache.json)'
    )

    args = parser.parse_args()

    exit_code, message = query_cache(args.url, args.cache_file)

    print(message)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
