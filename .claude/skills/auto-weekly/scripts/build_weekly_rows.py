#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从缓存提取本周 51 个 URL 的描述,输出 JSON 供组装周报"""
import json
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# (file, name, url) 按提交时间顺序: 07-29 提交在前, 08-01 提交在后
ENTRIES = [
    ("README.md", "CaseStudies", "https://github.com/vschko/CaseStudies"),
    ("README.md", "CVE-2026-42978-PoC-Research", "https://github.com/grizzzer/CVE-2026-42978-PoC-Research"),
    ("README.md", "CVE-2026-50522", "https://github.com/4minx/CVE-2026-50522"),
    ("README.md", "OffsetInspect", "https://github.com/warpedatom/OffsetInspect"),
    ("README.md", "sleepmask-vs", "https://github.com/nickvourd/sleepmask-vs"),
    ("README.md", "WaryasSWHE", "https://github.com/waryas/WaryasSWHE"),
    ("README.md", "CyberMeowfia", "https://github.com/NebuSec/CyberMeowfia"),
    ("README.md", "RTI-Toolkit", "https://github.com/nickvourd/RTI-Toolkit"),
    ("README.md", "CLR-Stomp", "https://github.com/nickvourd/CLR-Stomp"),
    ("README.md", "BOAZ_beta", "https://github.com/thomasxm/BOAZ_beta"),
    ("README.md", "COM-Hunter", "https://github.com/nickvourd/COM-Hunter"),
    ("README.md", "CVE-2026-16232", "https://github.com/sfewer-r7/CVE-2026-16232"),
    ("README.md", "cve-2026-57827", "https://github.com/shinthink/cve-2026-57827"),
    ("README.md", "PPKGPacker", "https://github.com/init1Security/PPKGPacker"),
    ("README.md", "ICH_A12_plus_Ramdisk", "https://github.com/Pa7r0n/ICH_A12_plus_Ramdisk"),
    ("docs.md", "macOS Passwords账户数据泄露(CVE-2025-24169)", "https://joshparnham.com/2026/07/accessing-sensitive-passwords-app-account-data-on-macos-cve-2025-24169/"),
    ("docs.md", "LLM多代理工作流挖掘开源0-day", "https://blog.cykor.kr/2026/02/How-I-Found-Open-Source-0-days-with-an-LLM-Multi-Agent-Workflow"),
    ("docs.md", "当AI让0-day像N-day", "https://starlabs.sg/blog/2026/07-when-ai-makes-0-days-feel-like-n-days/"),
    ("docs.md", "ESC17:Beyond WSUS系列", "https://research.qu35t.pw/en/series/esc17-beyond-wsus/"),
    ("docs.md", "差分规格分析", "https://commaok.xyz/ai/differential-spec/"),
    ("docs.md", "Windows剪贴板数据异常行为", "https://windows-internals.com/random-windows-things-part-2-unexpected-clipboard-data-behavior/"),
    ("docs.md", "绕过Windows认证反射缓解获取SYSTEM(上)", "https://www.synacktiv.com/publications/bypassing-windows-authentication-reflection-mitigations-for-system-shells-part-1"),
    ("docs.md", "clearsword", "https://therealclarity.github.io/blog/clearsword/"),
    ("docs.md", "Static Devirtualization of Tencent VM", "https://back.engineering/blog/31/07/2026/"),
    ("docs.md", "GHSA-jw5r-xhf5-2xcq", "https://github.com/openwrt/openwrt/security/advisories/GHSA-jw5r-xhf5-2xcq"),
    ("docs.md", "SakDriver内核Rootkit逆向", "https://0xsec.gitbook.io/0xsec/malware-analysis/sakdriver-reversing-a-kernel-driver-rootkit"),
    ("docs.md", "Exploiting CVE-2024-5830", "https://faran1512.github.io/posts/Exploiting_CVE-2024-5830/"),
    ("docs.md", "intercepting-ssl-traffic", "https://anadoxin.org/blog/intercepting-ssl-traffic/"),
    ("tools.md", "claude-video", "https://github.com/bradautomates/claude-video"),
    ("tools.md", "credshound", "https://github.com/haxxm0nkey/credshound"),
    ("tools.md", "usernetes", "https://github.com/rootless-containers/usernetes"),
    ("tools.md", "jcode", "https://github.com/1jehuang/jcode"),
    ("tools.md", "Kimi-K3-0.40B", "https://huggingface.co/inference-optimization/Kimi-K3-0.40B"),
    ("tools.md", "bitchat", "https://github.com/permissionlesstech/bitchat"),
    ("tools.md", "ActiveDirectoryTierModel", "https://github.com/microsoft/ActiveDirectoryTierModel"),
    ("tools.md", "Anastasis", "https://github.com/0xazanul/Anastasis"),
    ("tools.md", "Weaponize-CobaltStrike", "https://github.com/nickvourd/Weaponize-CobaltStrike"),
    ("tools.md", "Magic-Atomics", "https://github.com/magicsword-io/Magic-Atomics"),
    ("tools.md", "ai-web3-security", "https://github.com/pashov/ai-web3-security"),
    ("tools.md", "bug-bounties", "https://github.com/lissy93/bug-bounties"),
    ("tools.md", "SquidGate", "https://github.com/SquidSec/SquidGate"),
    ("tools.md", "tldr-code", "https://github.com/parcadei/tldr-code"),
    ("tools.md", "jvm-profiling-toolkit", "https://github.com/krzysztofslusarski/jvm-profiling-toolkit"),
    ("tools.md", "ETWLocksmith", "https://github.com/olafhartong/ETWLocksmith"),
    ("tools.md", "local-openai2anthropic", "https://github.com/dongfangzan/local-openai2anthropic"),
    ("tools.md", "chartr", "https://github.com/rengwu/chartr"),
    ("tools.md", "phalanx", "https://github.com/webxos/phalanx"),
    ("tools.md", "uncensored-ai", "https://github.com/AnkitNayak-dev/uncensored-ai"),
    ("tools.md", "Black-cat", "https://github.com/0rangec3t/Black-cat"),
    ("tools.md", "adhammer", "https://github.com/icedracon/adhammer"),
    ("tools.md", "ephemeral-sandbox", "https://github.com/Ephemeral-AI-Lab/ephemeral-sandbox"),
]

def main():
    with open('links_cache/descriptions_cache.json', 'r', encoding='utf-8') as f:
        cache = json.load(f)

    rows = []
    missing = []
    for fname, name, url in ENTRIES:
        desc = cache.get(url)
        if not desc or desc == '__DELETED__':
            missing.append(url)
            continue
        if '|' in desc:
            print(f'WARN: 描述含管道符 {url}', file=sys.stderr)
        rows.append((fname, name, url, desc))

    if missing:
        print(f'ERROR: {len(missing)} 条缺失', file=sys.stderr)
        sys.exit(1)

    out = {}
    for fname, name, url, desc in rows:
        out.setdefault(fname, []).append(f'| [{name}]({url}) | {desc} |')

    print(json.dumps(out, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
