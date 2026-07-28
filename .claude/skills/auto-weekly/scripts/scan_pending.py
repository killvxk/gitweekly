#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描源文件,提取需要生成描述的 URL(尚未在表格中且无有效缓存)"""
import json
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

URL_RE = re.compile(r'https?://[^\s<>"{}|\\^`\[\]\|）)]+')

FILES = [
    "BOF.md", "C2.md", "docs.md",
    "eBPF安全突破-内核Rootkit致盲可观测性工具.md",
    "Firefox-SpiderMonkey-Wasm一字之差引发的RCE漏洞分析.md",
    "free_baipiao.md", "gsd.md", "Persistence.md", "pico.md",
    "red.md", "sandbox-check.md", "skills-ai.md", "tools.md",
    "使用说明.md",
]

def load_cache():
    with open('links_cache/descriptions_cache.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def norm_url(u):
    return u.rstrip('/').rstrip('。.,;:!?')

def cache_lookup(cache, url):
    """返回 (found, description)"""
    for key in (url, url.rstrip('/'), url + '/'):
        if key in cache:
            v = cache[key]
            if isinstance(v, dict):
                return True, v.get('description', '')
            return True, str(v)
    return False, ''

def desc_meaningful(desc, url):
    if not desc or desc in ('无', '暂无描述', '__DELETED__'):
        return False
    if norm_url(desc) == norm_url(url):
        return False
    return True

def main():
    cache = load_cache()
    # 缓存值统一取出描述
    report = {}
    all_pending = []
    deleted_urls = []

    for fname in FILES:
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            continue

        pending = []   # 需要生成描述
        cached = []    # 缓存已有,但需要转为表格(不在表格行中)
        in_table = 0   # 已在表格中的链接数

        for idx, line in enumerate(lines, 1):
            urls = URL_RE.findall(line)
            if not urls:
                continue
            stripped = line.strip()
            is_table_row = stripped.startswith('|')
            for u in urls:
                u = u.rstrip('。.,;:!?')
                if is_table_row:
                    in_table += 1
                    continue
                found, desc = cache_lookup(cache, u)
                if found and desc == '__DELETED__':
                    deleted_urls.append((fname, idx, u))
                    continue
                if found and desc_meaningful(desc, u):
                    cached.append((idx, u, desc))
                else:
                    pending.append((idx, u))

        report[fname] = {
            'pending': pending,
            'cached_not_table': cached,
            'in_table_count': in_table,
        }
        for idx, u in pending:
            all_pending.append((fname, idx, u))

    print(json.dumps(report, ensure_ascii=False, indent=1))
    print('\n===== 汇总 =====', file=sys.stderr)
    total_pending = sum(len(v['pending']) for v in report.values())
    total_cached = sum(len(v['cached_not_table']) for v in report.values())
    total_table = sum(v['in_table_count'] for v in report.values())
    print(f'待生成描述: {total_pending}', file=sys.stderr)
    print(f'缓存已有(待转表格): {total_cached}', file=sys.stderr)
    print(f'已在表格中: {total_table}', file=sys.stderr)
    print(f'标记删除: {len(deleted_urls)}', file=sys.stderr)
    for f, i, u in deleted_urls:
        print(f'  [DELETED] {f}:{i} {u}', file=sys.stderr)

if __name__ == '__main__':
    main()
