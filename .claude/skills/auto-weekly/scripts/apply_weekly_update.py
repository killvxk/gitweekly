#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量写入 16 条描述到缓存,并将 docs.md / tools.md 顶部裸 URL 转为表格行"""
import json
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

CACHE = 'links_cache/descriptions_cache.json'

# url -> (链接标题, 描述)
DATA = {
    # docs.md — 文章
    "https://joshparnham.com/2026/07/accessing-sensitive-passwords-app-account-data-on-macos-cve-2025-24169/":
        ("macOS Passwords账户数据泄露(CVE-2025-24169)", "CVE-2025-24169:浏览器扩展宿主泄露已存账户数据"),
    "https://blog.cykor.kr/2026/02/How-I-Found-Open-Source-0-days-with-an-LLM-Multi-Agent-Workflow":
        ("LLM多代理工作流挖掘开源0-day", "用LLM多代理工作流发现开源软件0-day的实践"),
    "https://starlabs.sg/blog/2026/07-when-ai-makes-0-days-feel-like-n-days/":
        ("当AI让0-day像N-day", "AI辅助挖掘Linux内核net/sched竞态0-day"),
    "https://research.qu35t.pw/en/series/esc17-beyond-wsus/":
        ("ESC17:Beyond WSUS系列", "ESC17研究系列:ADCS证书信任问题攻击面剖析"),
    "https://commaok.xyz/ai/differential-spec/":
        ("差分规格分析", "差分技术与AI编码代理结合精炼软件规格"),
    "https://windows-internals.com/random-windows-things-part-2-unexpected-clipboard-data-behavior/":
        ("Windows剪贴板数据异常行为", "Windows剪贴板:任意进程可监听读取复制内容"),
    "https://www.synacktiv.com/publications/bypassing-windows-authentication-reflection-mitigations-for-system-shells-part-1":
        ("绕过Windows认证反射缓解获取SYSTEM(上)", "绕过Windows认证反射缓解措施获取SYSTEM shell"),
    # tools.md — 工具
    "https://github.com/bradautomates/claude-video":
        ("claude-video", "赋予Claude观看任意视频能力的Agent技能插件"),
    "https://github.com/haxxm0nkey/credshound":
        ("credshound", "类Nuclei本机凭据面扫描器,集成BloodHound(Go)"),
    "https://github.com/rootless-containers/usernetes":
        ("usernetes", "无root权限部署运行的Kubernetes方案"),
    "https://github.com/1jehuang/jcode":
        ("jcode", "主打低内存占用的AI编码代理CLI(Rust)"),
    "https://huggingface.co/inference-optimization/Kimi-K3-0.40B":
        ("Kimi-K3-0.40B", "Kimi-K3微调的0.40B特征提取模型"),
    "https://github.com/permissionlesstech/bitchat":
        ("bitchat", "蓝牙Mesh端到端加密聊天应用,IRC风格(Swift)"),
    "https://github.com/microsoft/ActiveDirectoryTierModel":
        ("ActiveDirectoryTierModel", "微软AD分层管理模型(Tier 0/1/2)部署脚本"),
    "https://github.com/0xazanul/Anastasis":
        ("Anastasis", "面向漏洞赏金的JS端点发现工具(TypeScript)"),
    "https://github.com/nickvourd/Weaponize-CobaltStrike":
        ("Weaponize-CobaltStrike", "自动下载编译CobaltStrike实用BOF的脚本"),
}

FILES = ["docs.md", "tools.md"]
URL_RE = re.compile(r'^https?://\S+$')


def write_cache():
    with open(CACHE, 'r', encoding='utf-8') as f:
        cache = json.load(f)
    added = updated = 0
    for url, (_, desc) in DATA.items():
        if url in cache and cache[url] == desc:
            continue
        if url in cache:
            updated += 1
        else:
            added += 1
        cache[url] = desc
    with open(CACHE, 'w', encoding='utf-8', newline='') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    print(f'缓存: 新增 {added}, 更新 {updated}, 总条目 {len(cache)}')


def transform(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 找表头分隔行 |---|---|
    sep_idx = None
    for i, ln in enumerate(lines):
        if re.match(r'^\|[\s:-]+\|[\s:-]+\|?\s*$', ln.strip()):
            sep_idx = i
            break
    if sep_idx is None:
        print(f'{fname}: 未找到表格,跳过')
        return

    # 收集表头之前的裸 URL 行(仅处理在 DATA 中的)
    rows = []
    remove = set()
    for i in range(sep_idx):
        s = lines[i].strip()
        if URL_RE.match(s) and s in DATA:
            title, desc = DATA[s]
            rows.append(f'| [{title}]({s}) | {desc} |\n')
            remove.add(i)

    if not rows:
        print(f'{fname}: 无待转换裸 URL')
        return

    # 删除裸 URL 行,压缩表头前的连续空行
    kept = [ln for i, ln in enumerate(lines) if i not in remove]
    # 重新定位分隔行
    sep_idx = next(i for i, ln in enumerate(kept)
                   if re.match(r'^\|[\s:-]+\|[\s:-]+\|?\s*$', ln.strip()))
    # 压缩分隔行之前的连续空行为一个
    out = []
    blank_run = 0
    for i, ln in enumerate(kept):
        if i < sep_idx and not ln.strip():
            blank_run += 1
            if blank_run > 1:
                continue
        elif ln.strip():
            blank_run = 0
        out.append(ln)
    sep_idx = next(i for i, ln in enumerate(out)
                   if re.match(r'^\|[\s:-]+\|[\s:-]+\|?\s*$', ln.strip()))
    # 在分隔行后插入新行
    out[sep_idx + 1:sep_idx + 1] = rows

    with open(fname, 'w', encoding='utf-8') as f:
        f.writelines(out)
    print(f'{fname}: 转换 {len(rows)} 行为表格')


if __name__ == '__main__':
    write_cache()
    for fn in FILES:
        transform(fn)
