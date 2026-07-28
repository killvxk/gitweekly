#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量抓取 URL 关键信息(GitHub API / HuggingFace API / 网页 title+meta),供生成描述用"""
import concurrent.futures as cf
import json
import re
import subprocess
import sys
import io
import html as htmllib

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

URLS = [
    "https://joshparnham.com/2026/07/accessing-sensitive-passwords-app-account-data-on-macos-cve-2025-24169/",
    "https://blog.cykor.kr/2026/02/How-I-Found-Open-Source-0-days-with-an-LLM-Multi-Agent-Workflow",
    "https://starlabs.sg/blog/2026/07-when-ai-makes-0-days-feel-like-n-days/",
    "https://research.qu35t.pw/en/series/esc17-beyond-wsus/",
    "https://commaok.xyz/ai/differential-spec/",
    "https://windows-internals.com/random-windows-things-part-2-unexpected-clipboard-data-behavior/",
    "https://www.synacktiv.com/publications/bypassing-windows-authentication-reflection-mitigations-for-system-shells-part-1",
    "https://github.com/bradautomates/claude-video",
    "https://github.com/haxxm0nkey/credshound",
    "https://github.com/rootless-containers/usernetes",
    "https://github.com/1jehuang/jcode",
    "https://huggingface.co/inference-optimization/Kimi-K3-0.40B",
    "https://github.com/permissionlesstech/bitchat",
    "https://github.com/microsoft/ActiveDirectoryTierModel",
    "https://github.com/0xazanul/Anastasis",
    "https://github.com/nickvourd/Weaponize-CobaltStrike",
]

def curl(url, timeout=25, accept=None):
    cmd = ['curl', '-sL', '--max-time', str(timeout), '-A', UA]
    if accept:
        cmd += ['-H', f'Accept: {accept}']
    cmd.append(url)
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=timeout + 5)
        return r.stdout.decode('utf-8', errors='replace'), r.returncode
    except subprocess.TimeoutExpired:
        return '', -1

def strip_html(text):
    text = re.sub(r'<script[\s\S]*?</script>', ' ', text, flags=re.I)
    text = re.sub(r'<style[\s\S]*?</style>', ' ', text, flags=re.I)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = htmllib.unescape(text)
    return re.sub(r'\s+', ' ', text).strip()

def fetch_github(url):
    m = re.match(r'https?://github\.com/([^/]+)/([^/?#\s]+)', url)
    if not m:
        return {'error': 'not a repo url'}
    owner, repo = m.group(1), m.group(2).replace('.git', '')
    body, rc = curl(f'https://api.github.com/repos/{owner}/{repo}')
    info = {'api_rc': rc}
    try:
        meta = json.loads(body)
        if meta.get('message') == 'Not Found':
            return {'error': '404 Not Found'}
        info.update({
            'full_name': meta.get('full_name'),
            'description': meta.get('description'),
            'topics': meta.get('topics'),
            'language': meta.get('language'),
            'stars': meta.get('stargazers_count'),
            'homepage': meta.get('homepage'),
        })
    except json.JSONDecodeError:
        info['api_body_head'] = body[:200]
    # 无描述或描述过短时补抓 README
    if not info.get('description') or len(info['description']) < 20:
        rd, _ = curl(f'https://api.github.com/repos/{owner}/{repo}/readme',
                     accept='application/vnd.github.raw')
        if rd and not rd.startswith('{'):
            info['readme_head'] = strip_html(rd)[:600]
    return info

def fetch_huggingface(url):
    m = re.match(r'https?://huggingface\.co/([^/]+/[^/?#\s]+)', url)
    if not m:
        return {'error': 'not a model url'}
    body, rc = curl(f'https://huggingface.co/api/models/{m.group(1)}')
    try:
        meta = json.loads(body)
        card = meta.get('cardData') or {}
        return {
            'id': meta.get('id'),
            'pipeline_tag': meta.get('pipeline_tag'),
            'tags': (meta.get('tags') or [])[:15],
            'downloads': meta.get('downloads'),
            'card_summary': str(card.get('license', '')) and None,
            'library': meta.get('library_name'),
        }
    except json.JSONDecodeError:
        return {'error': f'api parse fail rc={rc}', 'head': body[:200]}

def fetch_webpage(url):
    body, rc = curl(url)
    if rc != 0 or not body:
        return {'error': f'curl rc={rc}'}
    info = {}
    t = re.search(r'<title[^>]*>([\s\S]*?)</title>', body, re.I)
    if t:
        info['title'] = htmllib.unescape(t.group(1)).strip()
    for pat, key in [
        (r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\']([^"\']+)', 'og_desc'),
        (r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)', 'meta_desc'),
        (r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:description["\']', 'og_desc2'),
    ]:
        m = re.search(pat, body, re.I)
        if m:
            info[key] = htmllib.unescape(m.group(1)).strip()
    # 正文前 1500 字
    info['text_head'] = strip_html(body)[:1500]
    return info

def fetch_one(url):
    try:
        if 'github.com/' in url:
            return url, fetch_github(url)
        if 'huggingface.co/' in url:
            return url, fetch_huggingface(url)
        return url, fetch_webpage(url)
    except Exception as e:
        return url, {'error': str(e)}

def main():
    results = {}
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for url, info in ex.map(fetch_one, URLS):
            results[url] = info
            print(f'[done] {url}', file=sys.stderr)
    print(json.dumps(results, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
