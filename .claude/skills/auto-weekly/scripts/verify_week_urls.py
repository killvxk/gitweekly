#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""验证本周提交涉及的 52 个 URL 是否都在缓存中有有效描述"""
import json
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

URLS = {
    "README.md": [
        "https://github.com/vschko/CaseStudies",
        "https://github.com/grizzzer/CVE-2026-42978-PoC-Research",
        "https://github.com/4minx/CVE-2026-50522",
        "https://github.com/warpedatom/OffsetInspect",
        "https://github.com/nickvourd/sleepmask-vs",
        "https://github.com/waryas/WaryasSWHE",
        "https://github.com/NebuSec/CyberMeowfia",
        "https://github.com/nickvourd/RTI-Toolkit",
        "https://github.com/nickvourd/CLR-Stomp",
        "https://github.com/thomasxm/BOAZ_beta",
        "https://github.com/nickvourd/COM-Hunter",
        "https://github.com/sfewer-r7/CVE-2026-16232",
        "https://github.com/shinthink/cve-2026-57827",
        "https://github.com/init1Security/PPKGPacker",
        "https://github.com/Pa7r0n/ICH_A12_plus_Ramdisk",
    ],
    "docs.md": [
        "https://joshparnham.com/2026/07/accessing-sensitive-passwords-app-account-data-on-macos-cve-2025-24169/",
        "https://blog.cykor.kr/2026/02/How-I-Found-Open-Source-0-days-with-an-LLM-Multi-Agent-Workflow",
        "https://starlabs.sg/blog/2026/07-when-ai-makes-0-days-feel-like-n-days/",
        "https://research.qu35t.pw/en/series/esc17-beyond-wsus/",
        "https://commaok.xyz/ai/differential-spec/",
        "https://windows-internals.com/random-windows-things-part-2-unexpected-clipboard-data-behavior/",
        "https://www.synacktiv.com/publications/bypassing-windows-authentication-reflection-mitigations-for-system-shells-part-1",
        "https://therealclarity.github.io/blog/clearsword/",
        "https://back.engineering/blog/31/07/2026/",
        "https://github.com/openwrt/openwrt/security/advisories/GHSA-jw5r-xhf5-2xcq",
        "https://0xsec.gitbook.io/0xsec/malware-analysis/sakdriver-reversing-a-kernel-driver-rootkit",
        "https://faran1512.github.io/posts/Exploiting_CVE-2024-5830/",
        "https://anadoxin.org/blog/intercepting-ssl-traffic/",
    ],
    "tools.md": [
        "https://github.com/bradautomates/claude-video",
        "https://github.com/haxxm0nkey/credshound",
        "https://github.com/rootless-containers/usernetes",
        "https://github.com/1jehuang/jcode",
        "https://huggingface.co/inference-optimization/Kimi-K3-0.40B",
        "https://github.com/permissionlesstech/bitchat",
        "https://github.com/microsoft/ActiveDirectoryTierModel",
        "https://github.com/0xazanul/Anastasis",
        "https://github.com/nickvourd/Weaponize-CobaltStrike",
        "https://github.com/magicsword-io/Magic-Atomics",
        "https://github.com/pashov/ai-web3-security",
        "https://github.com/lissy93/bug-bounties",
        "https://github.com/SquidSec/SquidGate",
        "https://github.com/parcadei/tldr-code",
        "https://github.com/krzysztofslusarski/jvm-profiling-toolkit",
        "https://github.com/olafhartong/ETWLocksmith",
        "https://github.com/dongfangzan/local-openai2anthropic",
        "https://github.com/rengwu/chartr",
        "https://github.com/webxos/phalanx",
        "https://github.com/AnkitNayak-dev/uncensored-ai",
        "https://github.com/0rangec3t/Black-cat",
        "https://github.com/icedracon/adhammer",
        "https://github.com/Ephemeral-AI-Lab/ephemeral-sandbox",
    ],
}

def main():
    with open('links_cache/descriptions_cache.json', 'r', encoding='utf-8') as f:
        cache = json.load(f)

    total = hit = deleted = 0
    missing = []
    for fname, urls in URLS.items():
        for u in urls:
            total += 1
            desc = cache.get(u)
            if desc is None:
                missing.append((fname, u, 'MISSING'))
            elif desc == '__DELETED__':
                deleted += 1
                missing.append((fname, u, 'DELETED'))
            elif not desc.strip() or desc.strip() == u:
                missing.append((fname, u, f'EMPTY/SELF: {desc!r}'))
            else:
                hit += 1

    print(f'总URL数: {total}')
    print(f'缓存命中(有效描述): {hit}')
    print(f'标记删除: {deleted}')
    print(f'缺失/无效: {len(missing)}')
    for f, u, why in missing:
        print(f'  [{why}] {f} :: {u}')

if __name__ == '__main__':
    main()
