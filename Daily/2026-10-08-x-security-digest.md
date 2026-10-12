# X 安全情报晚报 · 2026-10-08（补做）

> 搜集窗口：圣地亚哥时间 **2026-10-07 20:30 至 2026-10-09 ~08:40**（America/Santiago / UTC-3，约 36 小时）。**本报为补做版**：10-08 20:09 的定时任务失败、没有产出，于 10-09 上午补跑，窗口延伸到补做时，所以覆盖 10-08 全天加 10-09 清晨。
> **X 采集方式**：使用 Grok Bot 自带的 X 只读公共数据接口（全量搜索与按 id 取帖，含 t.co 展开字段），**未开浏览器，未检查 @seogoogle4 浏览器登录状态**。A／C 组完整窗口（按相关度取前 25）；B 组原查询只返回 1 条，改用 `url:github.com` 查询重跑；另做 1 次针对性查询（CVE-2026-107406／AhsayCBS／Bricksforge／AA26-281A 等）；LWiS List 用 500 名成员备份分 10 批 `from:` 查询（共返回 103 帖）。本轮约 18 次 X 读取。合并 **79** 条新帖（A26／B13／C16／LWiS24），与 seen_ids 无重叠。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON `/workspace/kev-2026-10-08.json`（= `/workspace/enrich-2026-10-08/kev.json`），27 个厂商／研究 RSS（`/workspace/enrich-2026-10-08/*.xml`，摘要 `feeds_out.txt`），文章与 IoC 抽取 `/workspace/enrich-2026-10-08/`（`iocs-2026-10-08.json`、`cisa-aa26-281a-ioc-tables.json`）。
> **CISA KEV：catalogVersion 2026.10.08／1739 条，Δ+5**（dateReleased 2026-10-08T20:09Z = 17:09 UTC-3，结束连续 3 天未更新）。新增 5 条全是旧漏洞，与同日联合通告 AA26-281A（Integrity Tech／Flax Typhoon）的 Affected Products 一一对应，**due 均为 2026-10-11**。
> **due_today（10-08）：无**；**newly_overdue：Citrix CVE-2026-88779**（10-07 到期）；**upcoming 7 天：6 条**（新增 5 条 10-11 到期；Apple CVE-2026-86950 的 due 由 10-02 **改为 10-13**）；**仍逾期高信号 26 条**（+88779，−Apple 86950）。另外 CVE-2022-0995 的 due 被 CISA 从 09-09 改为 08-29（仍逾期）。
> 抓取备注：Adobe 安全公告 RSS 与 APSB 页面 403；GTIG RSS、MSRC blog RSS 返回空；tl;dr sec 原文 403（只能从首页列表确认 #349）；Risky Business 新集 404；LevelBlue THOR 原报告与 Mandiant/eSentire 原文未找到 URL（只引用 X 摘要帖）；Morphisec 帖里提到的「未修补的 Defender 0day」找不到一手来源，**未纳入、未验证**。
> 规则：每条含完整 https URL；分列 X 原帖／GitHub·PoC 仓库／厂商公告／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；泄露／入侵声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【KEV 恢复更新 · +5 · 10-11 到期】** ISC BIND CVE-2015-5477、Apache Struts CVE-2016-3081、Strapi CVE-2023-22894（可与 CVE-2023-22621 串成 RCE）、ONLYOFFICE CVE-2021-3199、ProFTPD CVE-2015-3306。这 5 条都是 AA26-281A 列出的被利用漏洞。
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  厂商／政府：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- **【Citrix 第 4 个 NetScaler 严重漏洞 · CVE-2026-107406（CVSS 9.5）】** SAML IdP／SP 配置下内存溢出，可致 RCE 或 DoS；**10-07 刚为 88779 升级到 14.1-73.41／13.1-64.28 的 SAML IdP 仍受影响**，须再升到 14.1-73.46／13.1-64.29。Citrix 称公告发布时未见利用，无 workaround。
  厂商：https://support.citrix.com/external/article/CTX697191
  X 原帖：https://x.com/_POPPELGAARD/status/2108313405849260428
- **【新在野 · 无补丁 · 有 IoC】AhsayCBS CVE-2026-105133＋105134** 被串用投放 JSP webshell 和 XMRig（SYSTEM 权限），10.3.4 及以下全部受影响，**厂商尚无补丁**（Huntress）。
  厂商：https://www.huntress.com/blog/ahsaycbs-flaws-exploit
  X 原帖：https://x.com/DFIR_Radar/status/2108468167907405868
- **【新在野 · 有补丁】WordPress Bricksforge CVE-2026-85097**（未认证任意文件上传→RCE，9.8/10.0），Patchstack 10-07 18:47（UTC-3）起观测到自动化利用；修复版 3.1.8.10。
  文章：https://wpdeeply.com/bricksforge-3-1-8-9-actively-exploited-file-upload-rce-cve-2026-85097/
- **【中国 · 执法＋联合通告 · 有 IoC】** FBI 查封 Integrity Tech（Flax Typhoon）的 MicroScan／FishHub 7 个域名；CISA／FBI／NSA 等发布 AA26-281A（数百条 IoC）。
  厂商／政府：https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-vulnerability-scanning-and-spear-phishing-tools-operated
  文章：https://www.bleepingcomputer.com/news/security/fbi-disrupts-chinese-hacking-tools-used-to-breach-critical-infrastructure/
- **【Citrix 88771 杀伤链 · 有 IoC】** LevelBlue THOR 公布 88771 的完整利用链（6 个利用源 IP、两段载荷哈希、`sec_monitor` 后门账号、伪装成 CSS 的 PHP webshell）。
  X 原帖：https://x.com/DFIR_Radar/status/2108014958990553481
- **【APT · 有 IoC】** Zscaler：疑似 TraderTraitor 用木马化 Terraform AWS provider 投放 FLATROOF／ROOFDECK；ESET：UAC-0099 MATCHBOIL 演进（另有 TrendAI ASHVEIN RAT）。
  厂商：https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver
  厂商：https://www.welivesecurity.com/en/eset-research/matchboil-new-tricks-same-old-evil-intentions/
- **【供应链】** tensorlake@0.5.144 npm 包被植入 Mini Shai-Hulud 蠕虫（撤销 token 后会触发 `rm -rf ~/`）；FakeGit 回潮，17,610 个恶意 GitHub 仓库。
  文章：https://safedep.io/tensorlake-npm-compromise-mini-shai-hulud
- **【Malware · 有 IoC · 未验证】** vx-underground 分析一个 Linux 样本：链上（智能合约）取配置，最终投放 Garble 混淆的 Sliver。
  X 原帖：https://x.com/vxunderground/status/2108445132685021424
- **【工具】** emp3r0r v4.24.0（10-08 22:20）与 v4.24.1（10-09 05:16）；Cobalt Strike Linux Beacon 预览；CloudPEASS K8s-PEAS；Synacktiv fusetea。Sliver／nuclei／nuclei-templates 无新版。
  GitHub：https://github.com/jm33-m0/emp3r0r/releases/tag/v4.24.1
- **【合并统计】** X **79**（A26／B13／C16／LWiS24）；seen_ids **2423→2502**；Risky 仍 RBNEWS618；tl;dr sec 出 #349（约 10-08）；报告 `/home/box/workspace/security-watch/reports/2026-10-08-x-security-digest.md`

## CVE / POC / 漏洞

### X-1. 【X 交叉 · 新 Critical · 未进 KEV】Citrix NetScaler CVE-2026-107406（SAML 内存溢出 → RCE／DoS，CVSS 9.5）
Citrix 在 10-08 发布 CTX697191：NetScaler ADC／Gateway 配置为 SAML IdP 或 SP 时存在内存溢出，可致 RCE 或 DoS，**无 workaround**。致谢 JPMorgan Chase XOR Team 与 Maxim Suhanov。受影响范围有两块：一是 SAML IdP 的 14.1-73.37～73.41、13.1-64.23～64.28（**即 10-07 为 88779 升级的版本也中招**）；二是 SAML SP 或 IdP 的 14.1-73.37、13.1-64.23 之前版本；FIPS／NDcPP 同理，Secure Private Access Hybrid 也受影响。修复版：14.1-73.46、13.1-64.29、14.1-73.46 FIPS、13.1.37.283（FIPS／NDcPP）。Citrix 称公告时未见利用；Shadowserver 观测约 2.1 万个 NetScaler 指纹 IP。防御：用 `add authentication samlAction`（SP）或 `add authentication samlIdPProfile`（IdP）确认是否配置了 SAML，有则立即再升一次；升级后按 88771／88779 的 IoC 复查。
地址：
- X 原帖（Poppelgaard，附只读检查脚本）：https://x.com/_POPPELGAARD/status/2108313405849260428
- X 原帖（VulniPulse）：https://x.com/vulnipulse/status/2108280392340164860
- X 原帖（Securityblog「连续第三周」）：https://x.com/Securityblog/status/2108304948622696683
- X 原帖（Security Affairs）：https://x.com/securityaffairs/status/2108499451279204832
- X 原帖（Security Arsenal 狩猎指南）：https://x.com/SecurityAr58409/status/2108500056827420735
- 厂商 CTX697191：https://support.citrix.com/external/article/CTX697191
- GitHub（Poppelgaard 只读检查器，非利用）：https://github.com/ThomasPoppelgaard/netscaler-ctx697096-checker
- NVD（按 CVE 构造）：https://nvd.nist.gov/vuln/detail/CVE-2026-107406
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/citrix-warns-admins-to-patch-new-netscaler-rce-flaw-immediately/
- 文章 The Hacker News：https://thehackernews.com/2026/10/citrix-patches-critical-netscaler-flaw.html
- 文章 Security Affairs：https://securityaffairs.com/200670/security/cve-2026-107406-citrix-fixes-critical-netscaler-adc-and-gateway-vulnerability.html
IoC：未见公开 IoC（未见利用）。

### X-2. 【X 交叉 · 在野 · 已逾期】Citrix NetScaler CVE-2026-88771 杀伤链（LevelBlue THOR）＋ 88779 转为逾期
DFIR Radar 摘要 LevelBlue THOR 报告：认证日志的用户名里出现 `pitboss`、`NSPPE`、`unexpectedly died`，同时带有注入命令和 `${IFS}`。第二阶段 `main.py` 改写 `/var/python/bin/customsnmpd` 做反弹 shell；`update_c08937.pl` 只在内存执行，建本地超级用户 `sec_monitor`，打包外传 `/flash/nsconfig` 后自删，把 `/bin/sh` 改为 6555，并在 `/var/netscaler/logon/LogonPoint/.local_journal` 放 PHP webshell（改 `/etc/httpd.conf`，经仿 CSS 的 URL 暴露）。同日另一篇摘要汇总了 watchTowr 根因（NSPPE 崩溃日志处理 Perl 脚本的命令注入）、Mandiant/GTIG 的 `.ico`→`.sig` PHP webshell，以及 eSentire 的 3 个活动簇（其一安装合法的 Platypus 管理代理）。**88779 已于 10-07 到期，今起转入逾期**；Threat Landscape 帖重申 88779 被当作 0day 打 DoS。防御：先查 `sec_monitor` 账号、`/bin/sh` 权限、`.local_journal`、httpd.conf 新增的 Alias／SetHandler；**文件不在不代表干净**（载荷会自删）。
地址：
- X 原帖（LevelBlue 链，IoC 一手摘要）：https://x.com/DFIR_Radar/status/2108014958990553481
- X 原帖（88771 综述）：https://x.com/DFIR_Radar/status/2108347841982656998
- X 原帖（88779 DoS）：https://x.com/LandscapeThreat/status/2108291109642215490
- X 原帖（三连 0day 提醒）：https://x.com/Secureit4uusa/status/2108332770426560964
- 厂商 CTX697174（88779）：https://support.citrix.com/external/article/CTX697174
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88771
- 文章：LevelBlue／Mandiant／eSentire 原文 URL 未取得，不编造
IoC：见汇总「LevelBlue NetScaler 88771」。

### X-3. 【X 交叉 · 新起在野 · 无补丁 · 有 IoC】AhsayCBS CVE-2026-105133＋CVE-2026-105134（Huntress）
MSP 常用的备份管理平台 AhsayCBS：105133（`checkSysPwd` 认证绕过，中危）串 105134（`/rps/api/json/UpdateReceivers.do` 未认证 RCE，严重）。攻击者在应用目录写 JSP webshell，以 SYSTEM 执行。Huntress 首次观测时间为 **10-07 20:20（UTC-3）**。后续由 `cbssvcX64.exe` 派生 curl／certutil，从阿里云 OSS 拉 Taskgmr.ps1、伪装成 Edge 的 XMRig 和 NSSM，建服务 `MicrosoftEdgeUpdateSvc`，并加载 WinRing0x64.sys 提升挖矿性能；Taskgmr.ps1 会在任务管理器打开时暂停挖矿。**10.3.4 及以下全部受影响，无补丁**；未进 KEV。防御：管理接口只对可信 IP／VPN 开放；狩猎 `cbssvcX64.exe` 的异常子进程、%TEMP% 下的 edge.exe／msedge.exe／Taskgmr.ps1；**命中即整机重装**（Huntress 称攻击者留有二级后门）。Huntress 在 threat-intel 仓库发布了 4 条 Sigma 规则。
地址：
- X 原帖：https://x.com/DFIR_Radar/status/2108468167907405868
- 厂商 Huntress：https://www.huntress.com/blog/ahsaycbs-flaws-exploit
- GitHub（Huntress Sigma／IoC 目录）：https://github.com/huntresslabs/threat-intel/tree/main/2026/2026-10
- NVD（按 CVE 构造）：https://nvd.nist.gov/vuln/detail/CVE-2026-105134
IoC：见汇总「Huntress AhsayCBS」。

### X-4. 【X 交叉 · 新起在野 · 有补丁】WordPress Bricksforge CVE-2026-85097（未认证文件上传 → RCE）
Bricksforge Pro Forms 首次上传时检查 MIME，后续表单提交却信任客户端的 `temporaryFileUploads.url`，可把含 PHP 的图片写到可执行路径。只要启用了 Pro Forms 就受影响。Patchstack 10-07 18:47（UTC-3）起观测到协调的自动化利用，主要目标是 `POST /wp-json/bricksforge/v1/form_submit`。修复版 3.1.8.10（4.x 分支也已修）。未进 KEV。防御：立即升级；uploads 目录禁止执行 PHP；更新后检查 webshell（升级不会清除已上传文件）。
地址：
- X 原帖（LoreleiWeb）：https://x.com/LoreleiWeb/status/2108498167503167986
- X 原帖（CVEnew）：https://x.com/CVEnew/status/2108124898640216396
- X 原帖（TheHackerWire）：https://x.com/TheHackerWire/status/2108376908794933252
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85097
- 文章 WPDeeply：https://wpdeeply.com/bricksforge-3-1-8-9-actively-exploited-file-upload-rce-cve-2026-85097/
- 文章 TheHackerWire：https://www.thehackerwire.com/vulnerability/CVE-2026-85097/
IoC（行为特征，WPDeeply 转 Patchstack 原样）：请求 `/wp-json/bricksforge/v1/form_submit` 且含 `temporaryFileUploads`；先调 `bricksforge_regenerate_nonce` 再上传；`/wp-content/uploads/bricksforge/tmp/` 下出现异常 PHP；dated uploads 目录出现 `login_admin_*.php`。未见公开 IP／哈希。

### X-5. 【X 交叉 · 跟踪】Atlassian CVE-2026-21589：VulnCheck 也确认在野，**KEV 仍未收录**
10-08 X 上多个帖子转述 VulnCheck 确认 8 个 Atlassian 产品的 21589 在野利用；watchTowr 原文是 LWiS 网络 10-07 被分享最多的链接（@ntlmrelay 统计，9 人）。CISA KEV 2026.10.08 版**仍未收录**。处置同昨日报告。
地址：
- X 原帖（Security Arsenal 转 VulnCheck）：https://x.com/SecurityAr58409/status/2108244776310972780
- X 原帖（Charland）：https://x.com/NichoCharland/status/2108231799386357959
- X 原帖（@ntlmrelay 分享榜）：https://x.com/ntlmrelay/status/2108137065347260815
- 文章 Security Arsenal：https://securityarsenal.com/blog/critical-rce-in-8-atlassian-products-actively-exploited-in-the-wild-detection-and-remediation-guide-for-jira-and-confluence-defenders
- 厂商：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
IoC：沿用昨日 Previdian 3 个 IP（见 2026-10-07 报告）；本窗口没有新的公开 IoC。

### X-6. 【X · 研究／PoC 公开】（仅记录，不转载利用细节）
- **LibreOffice 6 个漏洞 PoC**（@thomasrinsma 与 @b0n0b0__，含 RCE 和经 GStreamer 的 LFI；CVE 编号帖中未给出）：X https://x.com/thomasrinsma/status/2108307050379772251
- **OpenCTI JsonMapper SafeJS RCE** 的 Metasploit 模块已合并（@egeblc，PR #21884），自建 OpenCTI 的 CTI 团队应尽快升级：X https://x.com/egeblc/status/2108212188489937288 ／ GitHub https://github.com/rapid7/metasploit-framework/pull/21884
- **AnyDesk RCE PoC**（V12，CVE 未给出）：X https://x.com/v12sec/status/2108311107526164868 ／ GitHub https://github.com/v12-security/pocs/tree/main/anydesk
- **Ghostscript CVE-2026-101258**（`-dSAFER` 绕过）PoC：X https://x.com/AlAssaf_H/status/2108060524302758326 ／ GitHub https://github.com/v12-security/pocs/tree/main/ghostscript
- **VMware Workstation／Fusion CVE-2026-59346**（VMXNET3，昨日已报）出现公开崩溃 PoC：X https://x.com/ridvanyagli/status/2108111138713964599 ／ GitHub https://github.com/0xCyberstan/CVE-2026-59346-POC ／ 厂商 https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/security-advisories/0/38288
- **gVisor directfs TOCTOU 沙箱逃逸**（CVE-2026-96812 的后续，无独立 CVE）：X https://x.com/N3mes1s/status/2108514848988397813 ／ 复现 https://www.pruva.dev/reproductions/REPRO-2026-00382
- **NVIDIA DCGM Exporter CVE-2026-47483**（pprof 暴露→DoS，2,000+ 暴露 GPU 服务器）：X https://x.com/Dinosn/status/2108398985060962346 ／ 文章 https://lava.security/research/cve-2026-47483-nvidia-dcgm-exporter-vulnerability ／ https://www.theregister.com/security/2026/10/08/high-severity-nvidia-bug-could-crash-gpu-monitoring-on-exposed-servers/5302077
- **GoBalance（Tor 负载均衡）两个严重漏洞**，曾被用于攻击 Dread／Omega 暗网市场；补丁和 PoC 一起发布：X https://x.com/DarkWebInformer/status/2108214882248061268 ／ GitHub https://github.com/kolmteistov/gobalance-patch ／ 文章 https://thehackernews.com/2026/10/gobalance-flaw-lets-attackers-hijack.html
- **libjxl 32 位整数溢出**（v0.11.2 修复）PoC：X https://x.com/patchhawk_/status/2108009242296758643 ／ GitHub https://github.com/78ResearchLab/PatchHawk-PoC/tree/main/78RL-2026-0009 ／ https://github.com/libjxl/libjxl/releases/tag/v0.11.2
- reveal.js postMessage XSS（已修）：https://x.com/0xAsm0d3us/status/2108153968308486339 ；OWASP Java HTML Sanitizer CVE-2025-66021（旧）：https://x.com/ironfisto/status/2108250593810899278 ／ https://github.com/OWASP/java-html-sanitizer/security/advisories/GHSA-g9gq-3pfx-2gw2
- 微软「17 万亿条记录」漏洞仅获 5k 赏金（@payloadartist 转述，**细节未核对**）：https://x.com/payloadartist/status/2108204266816946215
- **Pwn2Own Ireland 2026 结束**：98 个 0day、奖金 $1,262,000；Pixel 10、Galaxy S26、OpenAI Codex、Oracle Autonomous AI DB 被攻破（厂商修补前不公开细节）：文章 https://www.bleepingcomputer.com/news/security/hackers-earn-1262000-for-98-zero-days-at-pwn2own-ireland/ ／ https://thehackernews.com/2026/10/three-teams-demonstrate-remote-hacks-of.html
IoC：以上均未见公开 IoC。

### X-7. 【X · 跟踪项提醒（旧闻转发，无新信息）】
- FortiMail CVE-2026-104286（KEV，逾期）：X https://x.com/sh3ll_c0d3/status/2108257120680386830 ／ https://x.com/secpoint/status/2108113798284320771 ；厂商 https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- F5 BIG-IP APM CVE-2026-94127（KEV，逾期）：X https://x.com/morphisec/status/2108282596568322191
- Arista VeloCloud VCO CVE-2026-93952（KEV，逾期）：X https://x.com/CisoMarketplace/status/2108119844549734624 ／ 文章 https://secureiotoffice.world/aristas-ai-driven-edge-threat-management-sd-wan-new-option/
- Adobe Commerce CVE-2026-75650「StyleSmuggler」（APSB26-146，9 月 KEV 已收录、已过期）：深度分析 X https://x.com/Dinosn/status/2108198274574274599 ／ 文章 https://blog.securelayer7.net/cve-2026-75650-stylesmuggler-magento-rce/ ／ X https://x.com/wagento/status/2108162180436897916 ／ 厂商（403 未抓取）https://helpx.adobe.com/security/products/magento/apsb26-146.html
- Zammad 102489／102490（KEV，逾期）：Horizon3 10-08 15:51 另发技术详情页 https://horizon3.ai/attack-research/vulnerabilities/cve-2026-102489/ ；本周 0day 汇总 X https://x.com/UjlakiMarci/status/2108483646898205082
- Morphisec 当日简报提到「未修补 Defender 0day、SharePoint RCE、3 个 Linux 内核 CVE 在野」，**无一手来源、未验证**：X https://x.com/morphisec/status/2108282561428435162
IoC：未见新增公开 IoC。

### P-1. 【KEV · 2026.10.08 新增 5 条（due 2026-10-11）· 均与 AA26-281A 对应】
- ISC BIND CVE-2015-5477（TKEY 查询 DoS）：https://nvd.nist.gov/vuln/detail/CVE-2015-5477 ／ 参考 https://web.archive.org/web/20150729014733/https://kb.isc.org/article/AA-01272
- Apache Struts CVE-2016-3081（DMI `method:` 前缀命令注入，forensicTriage=Yes）：https://nvd.nist.gov/vuln/detail/CVE-2016-3081 ／ 厂商 https://cwiki.apache.org/confluence/display/WW/S2-032
- Strapi CVE-2023-22894（管理面板明文存储，可串 CVE-2023-22621 成 RCE；可能 EoL，forensicTriage=Yes）：https://nvd.nist.gov/vuln/detail/CVE-2023-22894 ／ 厂商 https://strapi.io/blog/security-disclosure-of-vulnerabilities-cve ；FOFA 称 16.9 万个结果：X https://x.com/fofabot/status/2108405735990145217
- ONLYOFFICE Docs CVE-2021-3199（JWT 下图片上传路径穿越→RCE，forensicTriage=Yes）：https://nvd.nist.gov/vuln/detail/CVE-2021-3199 ／ 厂商 https://github.com/ONLYOFFICE/DocumentServer/blob/903fe5ab7a275bd69c3c3346af2d21cf87ebeabf/CHANGELOG.md#563
- ProFTPD CVE-2015-3306（mod_copy `site cpfr/cpto` 任意读写，forensicTriage=Yes）：https://nvd.nist.gov/vuln/detail/CVE-2015-3306 ／ 厂商 http://www.proftpd.org/
- 注：AA26-281A 的 Affected Products 还列有 CVE-2014-6278、CVE-2019-11510、CVE-2021-22205（均早已在 KEV）。
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
IoC：KEV 本身不含 IoC；相关 IoC 见 AA26-281A（汇总）。

### P-2. 【厂商 · 其他公告状态】
- Cisco：10-07 批量（见昨日报告）中 NX-API RCE（cisco-sa-napi-rce-r2shwu2j）于 10-08 11:11（UTC-3）修订；BleepingComputer 跟进报道 Nexus 接管风险：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-napi-rce-r2shwu2j ／ https://www.bleepingcomputer.com/news/security/cisco-warns-of-critical-flaws-allowing-nexus-switch-takeover/
- CISA ICS 10-08 新增 3 条：ICSA-26-281-01（Red Lion N-Tron 700）https://www.cisa.gov/news-events/ics-advisories/icsa-26-281-01 ／ ICSA-26-281-02（GPA openPDC／openHistorian）https://www.cisa.gov/news-events/ics-advisories/icsa-26-281-02 ／ ICSA-26-281-03（Satel Netco Design）https://www.cisa.gov/news-events/ics-advisories/icsa-26-281-03
- Fortinet（最新仍 10-01 FG-IR-26-175）、Palo Alto（最新仍 10-02 CVE-2026-0250）、Ivanti（最新 09-08）：无新公告。MSRC：10 月 Patch Tuesday 在 10-13。
IoC：未见公开 IoC。

### P-3. 【仍逾期高信号 26 条】
Citrix 88771／88772／**88779（新转入）**、Check Point 85102／93616、Arista 93952、F5 94127、JFrog 42016／42018、Zyxel 7273、Microsoft 81963／85880／65660、Google 87491／85046／58704、Cisco 76460／76504、Acronis 87886、WSO2 5430、Adobe 71362、MikroTik 67279、WordPress 87902、Fortinet 104286、Zammad 102489／102490。Apple 86950 因 due 改为 10-13 移出逾期，进入 upcoming。
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

## 工具与 GitHub 发布

### 1. emp3r0r v4.24.0／v4.24.1（窗口内两版）
v4.24.0（10-08 22:20，UTC-3）：默认附带 `proxy-ns`，新增用户态 WireGuard；v4.24.1（10-09 05:16）修复 operator 容器缺工具的问题。防御向：用户态 WireGuard 隧道会让 C2 流量更像正常 VPN，需关注主机上的非常规 WireGuard 进程。
- GitHub release：https://github.com/jm33-m0/emp3r0r/releases/tag/v4.24.0 ／ https://github.com/jm33-m0/emp3r0r/releases/tag/v4.24.1
- X 原帖：本窗口 X 未采到发布帖，不编造

### 2. Cobalt Strike：Linux Beacon 首次预览（网络研讨会录像）
- X 原帖：https://x.com/_CobaltStrike/status/2108191601948328209
- 文章：https://www.cobaltstrike.com/resources/videos/cobalt-strike-technical-walkthrough?source=Li

### 3. CloudPEASS：新增 K8s-PEAS（枚举被控主体在 Kubernetes 集群中的权限）
- X 原帖：https://x.com/hacktricks_live/status/2108157346824192327
- GitHub：https://github.com/peass-ng/CloudPEASS

### 4. Synacktiv fusetea（用 HTTP Range 请求从 VM 磁盘快速取文件／机密，T-REX 2026）
- X 原帖：https://x.com/Synacktiv/status/2108477586896474340
- GitHub：https://github.com/synacktiv/fusetea/
- 幻灯片：https://www.synacktiv.com/sites/default/files/2026-10/downloading_a_needle_from_a_haystack.pdf

### 5. ImmoralFiber（Windows Fiber 注入 PoisonFiber／调用栈伪装 PhantomThread，@ipurple 推荐，可用于检测研究）
- X 原帖：https://x.com/ipurple/status/2108515099535401057
- GitHub：https://github.com/JanielDary/ImmoralFiber

### 6. ARTEX 开源仓库热度（CrowdStrike 报告后 9 小时 500 星）
防御向：昨日 CrowdStrike 报告的 AI 渗透框架；关注镜像／英文分支（其中一个 jfreemansh 镜像已 404）。
- X 原帖：https://x.com/Z3nlyte/status/2108213504473723104 ／ https://x.com/wilderko/status/2108289228308091386
- GitHub：https://github.com/mhtsec/ARTEX
- 文章 The Hacker News：https://thehackernews.com/2026/10/artex-ai-pentesting-tool-used-in-data.html

### 7. 其他
- praetorian vespasian（从流量生成 REST／GraphQL／SOAP／WS API 规格）：X https://x.com/EsGeeks/status/2108029583186382897 ／ GitHub https://github.com/praetorian-inc/vespasian
- rea-pentest-playbook-skill（授权渗透工作流 skill）：X https://x.com/Henry_Li87/status/2108408246184943872 ／ GitHub https://github.com/henryli777/rea--pentest-playbook-skill
- Kerberos：针对无 SPN 账号滥用无协议转换的约束委派：X https://x.com/ipurple/status/2108297723258482801 ／ 文章 https://hunio.org/security/abusing-constrained-delegation-without-protocol-transition-against-spn-less-accounts/
- Microsoft Copilot 后渗透面合集（多数已被修，仅一个 LOLBin 仍有效）：X https://x.com/ipurple/status/2108219386704380040 ／ GitHub https://github.com/4n4s4zi/tour-de-mscopilot
- VirusTotal 新增公网 IPv4 扫描以发现 C2：X https://x.com/anzendo/status/2108480613884031409

### 8. 核心工具无新版
Sliver v1.7.8（https://github.com/BishopFox/sliver/releases/tag/v1.7.8）、nuclei v3.11.1（https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1）、nuclei-templates v10.5.0（https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.0；窗口内 main 只有 KEV／EPSS 元数据自动提交，外加 CVE-2022-27925、CVE-2024-51483 模板合并）、Mythic v3.4.0.5、Impacket 0.13.1、NetExec v1.5.1；Havoc 仍无 release。

## APT / Malware 分析

### X-1. 【政府 · 有 IoC】FBI 查封 Integrity Tech（Flax Typhoon）MicroScan／FishHub 域名 ＋ 联合通告 AA26-281A
10-08 美国司法部／FBI 查封 7 个域名：MicroScan 扫描平台（配合 Mirai 僵尸网络扫描；目标包括南卡电力公司、日本和波兰机场、台湾天然气和电力公司、高校，确认两所台湾大学被入侵），以及 FishHub 鱼叉钓鱼／数据窃取平台（服务器上有 20+ 组织的数据）。同日 CISA／FBI／NSA 等发布 AA26-281A：攻击者用自动扫描、XSS、对 Exchange（ECP／EWS）密码喷洒，以 SoftEther VPN 持久化（常伪装成 conhost.exe／dllhost.exe），通过门户把窃取的邮件提供给第三方；行业覆盖政府、关键制造、医疗、IT、执法、教育、宗教组织。FBI 另称相关黑客经门户向第三方出售被盗邮件。美国悬赏 1000 万美元征集 HAFNIUM 相关人员 Zhang Yu 的线索。防御：Exchange 启用 MFA、关闭不用的服务；狩猎 System32 之外运行的 SoftEther（conhost/dllhost 名）；导入 AA26-281A IoC（含 2016 年起的旧指标，封堵前需核实）。
- X 原帖（@Dinosn 转 BleepingComputer）：https://x.com/Dinosn/status/2108398906358829367
- X 原帖（@Dinosn 转 The Register）：https://x.com/Dinosn/status/2108398828571476309
- X 原帖（@Dinosn 转 THN 门户）：https://x.com/Dinosn/status/2108399234663981068
- X 原帖（Cybermerge 狩猎要点）：https://x.com/cybermergemedia/status/2108261261863440746 ／ https://x.com/cybermergemedia/status/2108287737820225865
- 政府 CISA AA26-281A：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- 政府 DOJ：https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-vulnerability-scanning-and-spear-phishing-tools-operated
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/fbi-disrupts-chinese-hacking-tools-used-to-breach-critical-infrastructure/
- 文章 The Hacker News：https://thehackernews.com/2026/10/fbi-seizes-7-domains-disrupts-flax.html ／ https://thehackernews.com/2026/10/fbi-says-china-linked-hackers-ran.html ／ https://thehackernews.com/2026/10/us-offers-up-to-10-million-for-tips-on.html
- 文章 The Register：https://www.theregister.com/security/2026/10/08/us-disrupts-chinese-hacking-tools-as-7-govts-warn-of-prc-spies-stealing-sensitive-data-worldwide/5302107
- IoC：见汇总「Flax Typhoon／AA26-281A」

### X-2. 【Zscaler · 有 IoC】疑似 TraderTraitor：木马化 Terraform AWS provider → FLATROOF（Rust）／ROOFDECK
2026-07 的活动（低置信度归因 TraderTraitor／Pressure Chollima）：伪造 `terraform-provider-awsbeta`，在 Terraform 加载时执行 Bash loader `safari_updater`；载荷藏在 `.woff` 字体的 `@@ENDFONT@@` 标记之后，AES-256-CBC 加密。FLATROOF 支持 Telegram／GitHub API／webhook 三种 C2，带浏览器和钱包窃取器；ROOFDECK 从本地文件、Pastebin 或 Nostr 资料取 C2。目标是加密货币／Web3 开发者和云工程师（含 CI/CD）。防御：只从官方 registry 拉 provider 并锁定哈希；CI 里监控 provider 派生的 `sh -c`。
- X 原帖（RST Cloud 抽取）：https://x.com/rst_cloud/status/2108448388135952585
- 厂商 Zscaler：https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver
- IoC：见汇总「Zscaler TraderTraitor」

### X-3. 【ESET · 有 IoC】UAC-0099 MATCHBOIL 下载器 2024→2026 演进；TrendAI 另报 ASHVEIN RAT
ESET：俄罗斯关联的 UAC-0099 用 C# 下载器 MATCHBOIL（.NET Reactor 混淆、查事件日志反沙箱、Run 键与计划任务持久化）打乌克兰能源、交通、制造业。TrendAI（Earth Sirrush）另报新 .NET RAT「ASHVEIN」：把任务藏在 WordPress 页面的隐形 HTML 里，部分变种以 GitHub 作 dead drop，经 VHD 投递，并对 AI 恶意软件分析工具做提示注入。
- X 原帖（@SwitHak 转 ESET）：https://x.com/SwitHak/status/2108215944665248216
- X 原帖（ASHVEIN）：https://x.com/DEVOTOMSOLUTION/status/2108233661208293725
- 厂商 ESET：https://www.welivesecurity.com/en/eset-research/matchboil-new-tricks-same-old-evil-intentions/
- GitHub（ESET IoC 仓库）：https://github.com/eset/malware-ioc/tree/master/
- 文章 The Hacker News（ASHVEIN）：https://thehackernews.com/2026/10/uac-0099-targets-ukrainian-government.html ／ https://4tify.io/article/uac-0099-unleashes-ashvein-a-new-net-rat-hiding-commands-in-invisible-html
- IoC：MATCHBOIL 见汇总「ESET MATCHBOIL」；ASHVEIN 转载文中未见具体指标，**未见公开 IoC**

### X-4. 【供应链 · 有 IoC】tensorlake@0.5.144 npm 被植入 Mini Shai-Hulud（ChainDrop 家族）
`lib/Math_Symbol.js`（约 856KB）在安装时执行，窃取云、GitHub、npm、SSH、浏览器和钱包凭据（俄语区域跳过）；C2 用硬编码域名、以太坊合约（35 个 RPC）和签名 GitHub commit 作 dead drop；外传到新建公开仓库，描述为「Shai-Hulud: Here We Go Again」；用 npm token 和 trusted publishing 自我传播，并给 Claude Code／VS Code 加 hook。**`gh-token-monitor` 在 token 被撤销（40x）后执行 `rm -rf ~/`**。处置建议：先隔离主机、清除持久化，再撤销 token。与昨日 Unit 42 ChainDrop 交叉。
- X 原帖（RST Cloud）：https://x.com/rst_cloud/status/2108440800652570779 ／ https://x.com/rst_cloud/status/2108364920127430738
- X 原帖（@Dinosn 转 The Register）：https://x.com/Dinosn/status/2108246252882137453
- 文章 SafeDep：https://safedep.io/tensorlake-npm-compromise-mini-shai-hulud
- 文章 The Hacker News：https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html
- 文章 The Register：https://www.theregister.com/security/2026/10/08/shai-hulud-worm-makes-jump-to-ai-infrastructure-with-tensorlake-compromise/5302054
- IoC：见汇总「tensorlake」

### X-5. 【vx-underground · 有 IoC · 未验证】Linux 样本：链上取配置 → Garble 混淆的 Sliver
混淆 bash 脚本先复制自身到 `~/.config/.pipeaudio/.env`，建 systemd 用户服务 `flawless.service`；再经 JSON-RPC 从智能合约取得加密 URL，按 CPU 架构下载约 41MB 的 Go 二进制，作者判断是 Garble 混淆的 SliverC2。**个人分析，未经厂商验证**。
- X 原帖：https://x.com/vxunderground/status/2108445132685021424
- IoC：见汇总「vx-underground Linux Sliver」

### X-6. 【其他研究（RST Cloud 抽取／LWiS 转发，IoC 在原文）】
- Bitdefender「Midnight Mimosa」：廉价 Android 手机（Doogee、Cubot 及山寨机）固件预装恶意软件，做广告欺诈和住宅代理；Play 商店另有 13 个 App：X https://x.com/rst_cloud/status/2108387676365709579 ／ 厂商 https://www.bitdefender.com/en-us/blog/labs/midnight-mimosa-malware ／ 文章 https://www.bleepingcomputer.com/news/security/low-cost-android-phones-ship-with-residential-proxy-malware/ （原文 127 个哈希，未逐条抄录）
- Censys：DarkSword iOS 利用链＋Coruna 钱包窃取平台开放目录（中文运营者，19 个钱包；iOS 26 链 CVE-2026-31001 尚未成型，**不应视为 0day**）：X https://x.com/rst_cloud/status/2108067306446229861 ／ 厂商 https://censys.com/blog/darksword-coruna-open-directory-finding-report/
- Cofense：以「客诉」为饵的邮件打酒店，LNK→Node.js→EtherRAT／TONResolver（区块链 dead drop）：X https://x.com/rst_cloud/status/2108082501629456404 ／ 厂商 https://cofense.com/blog/from-guest-complaints-to-malware-blockchain-abuse-targets-hotels
- Checkmarx MALFEX npm 活动（Overlord RAT 从 Solana memo 取 C2；`function-flag`、`function-color`、`cdn-img-fetch` 仍可安装）：X https://x.com/rst_cloud/status/2108327007431889237 ／ 厂商 https://checkmarx.com/zero-post/malfex-npm-malware-campaign-three-payloads-and-an-adversary-that-signs-their-work/
- Talos UAT-11985：AI 生成的活动邀请＋二维码钓鱼，以实时 Google AitM 攻击台湾研究机构人员：厂商 https://blog.talosintelligence.com/uat-11985/ ／ IoC https://github.com/Cisco-Talos/IOCs/blob/main/2026/10/uat-11985.txt ；Talos 另发 AI 分析规避综述：https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/ ；Warlock 相关观点文：X https://x.com/rst_cloud/status/2108410454330454271 ／ https://blog.talosintelligence.com/making-sure-the-checks-get-printed/
- ThreatHunter.ai「Azure30」：ClickFix→msiexec→Node.js 后门（文内有 IoC／KQL／YARA）：X https://x.com/ThreatHunter_AI/status/2108517333736276298 ／ 文章 https://www.threathunter.ai/blog/azure30-nodejs-backdoor-trojanized-msi-clickfix/
- FakeGit 回潮：17,610 个 GitHub 仓库投放 SmartLoader→StealC（Apiiro）：X https://x.com/Dinosn/status/2108254776618254377 ／ 文章 https://www.bleepingcomputer.com/news/security/fakegit-malware-campaign-returns-with-17-610-malicious-github-repos/
- Flashpoint CastleStealer：X https://x.com/Dinosn/status/2108259703851774134 ／ 文章 https://flashpoint.io/blog/castlestealer-an-emerging-infostealer-growing-more-sophisticated/
- Hunt.io 提前发现 BraZetsu 初始访问经纪商的基础设施：X https://x.com/Dinosn/status/2108399423076151496 ／ 文章 https://securityaffairs.com/200634/cyber-crime/hunt-io-finds-new-brazetsu-infrastructure-months-before-disclosure.html
- PoeLLM 后续解读（Hunt.io、Help Net）：X https://x.com/Huntio/status/2108214625594470772 ／ https://x.com/helpnetsecurity/status/2108143417825820818
- OpenAI 披露并瓦解两起利用 AI 的「假门面」影响力行动（俄、伊）：X https://x.com/SwitHak/status/2108283456618631263 ／ 文章 https://openai.com/index/disrupting-ai-enabled-false-front-operations/
- IoC：除 Talos 外，本节各条在本报中**未逐条抄录**，以原文为准

### X-7. 其他事件（多为声称／报道，标注可信度）
- IDC Frontier（软银子公司）IDCF Cloud「东日本 Region 1」遭勒索，10-07 03:40（日本时间）开始，影响 495 家企业和地方政府，全区域管理控制台暂停：X https://x.com/Dinosn/status/2108399039569916111 ／ 文章 https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/
- 意大利外交部网站遭攻击（官方称已缓解）：X https://x.com/Dinosn/status/2108399073979973936 ／ 文章 https://securityaffairs.com/200650/cyber-warfare-2/italys-foreign-ministry-under-cyberattack-as-embassy-sites-come-under-review.html
- JPCERT/CC：日本网络数据泄露激增，与移动 API 滥用、Metabase SQL 注入被利用有关：X https://x.com/Dinosn/status/2108254803247976614 ／ 文章 https://thehackernews.com/2026/10/japan-sees-sharp-rise-in-web-data-leaks.html
- 「Eternal」声称泄露洪都拉斯选民名册（**UNCONFIRMED**）：X https://x.com/VECERTRadar/status/2108308045713584290
- NightSpire 勒索团伙在泄露站列出受害者，含 Vietnam SuperPort（**UNCONFIRMED／仅泄露站声称**）：X https://x.com/undercode_news/status/2108416511505494258 ／ https://x.com/Npj8448/status/2108412434126123145
- 黑山逮捕俄罗斯「Rybar」网络负责人 Zvinchuk：X https://x.com/SwitHak/status/2108509954436952377 ／ 文章 https://www.vijesti.me/vijesti/crna-hronika/830529/u-akciji-crnogorskih-bezbjednosnih-sluzbi-priveden-zvincuk-sef-ruske-mreze-ribar-i-vise-njegovih-saradnika
- 执法：Empire 暗网市场经营者被判 40 年（https://www.bleepingcomputer.com/news/security/owner-of-empire-cybercrime-market-gets-40-years-in-prison/）；MonsterCloud 老板被控收客户 1900 万美元却暗中付赎金（https://thehackernews.com/2026/10/monstercloud-owner-accused-of-billing.html）；ASOS 称数据泄露源于社工与凭据被盗（https://www.bleepingcomputer.com/news/security/asos-links-data-breach-to-social-engineering-attack-credential-theft/）
- IoC：以上均未见公开 IoC

## 地址／IoC 汇总

**Huntress AhsayCBS（厂商原样）**
- IoC 表 IP（原文表内未标注角色）：`177.4.12[.]11`／`38.60.252[.]110`／`107.191.47[.]199`／`185.220.236[.]49`／`104.234.26[.]10`／`123.202.208[.]37`
- 载荷托管：`hxxp://imagefiles-backup.oss-ap-southeast-7.aliyuncs[.]com/javas/Office/win/`（Taskgmr.ps1／edge.exe／msedge.exe／config.json／WinRing0x64.sys）
- 矿池：`xmr.kryptex[.]network:8029`、`51.195.127[.]124`；矿池用户 `krxYMRN97D/creativejs`
- SHA256：`05f69ae6b2b89c1c4dcf836bff032232f11bf0109f2b498e2345045d06139034`（msedge.exe，改版 NSSM）／`4dcb0202fe8b2d4d7b183764e38184cd6ed50132786cc7e7d1f7f4bce1dd6f3d`（edge.exe，XMRig）／`481728a7c9c4c02be07051d9c1958d902ea6397ebb8952ab83944818e3d25d21`（Taskgmr.ps1）
- 服务 `MicrosoftEdgeUpdateSvc`；利用端点 `/rps/api/json/UpdateReceivers.do`
- 来源：https://www.huntress.com/blog/ahsaycbs-flaws-exploit

**LevelBlue NetScaler 88771（经 DFIR Radar 摘要原样）**
- 利用源 IP：`70.172.58[.]168`／`162.243.36[.]88`／`173.40.135[.]209`／`47.230.224[.]154`／`92.118.204[.]229`／`87.224.84[.]82`
- 载荷：`hxxp://23.27.143[.]20:9000/main.py`（SHA256 `e9fe43968c6c0955300e3bc4d7fb0b05a18570b4733aaf4f5c6f7f09be5a242c`）／`hxxp://64.94.85[.]67:443/update_c08937.pl`（SHA256 `974b69782fdf5d67b97cfd508465939e44ee10798dbcc1e82b92d78776bad938`）
- C2／外传：`45.141.21[.]130:443`、`64.94.85[.]67`
- 主机痕迹：账号 `sec_monitor`；`/bin/sh` 权限 6555；`/var/netscaler/logon/LogonPoint/.local_journal`；`/tmp/update_result_3567cs.tgz`；`/var/python/bin/customsnmpd`；`/var/netscaler/logon/insight-new.js`；`/var/netscaler/logon/LogonPoint/xua.html`；日志串 `pitboss`、`NSPPE`、`unexpectedly died`、`${IFS}`
- 来源：https://x.com/DFIR_Radar/status/2108014958990553481

**Flax Typhoon／AA26-281A（政府原样）**
- FBI 查封域名：`c0cc[.]cc`（MicroScan）／`98aicai[.]com`／`98aicode[.]com`／`outlook3650[.]com`／`youtubecard[.]com`／`linkedinns[.]net`（FishHub 投递）／`98aiblog[.]com`（SoftEther VPN）
- AA26-281A 附录 Table 10–15：域名约 218 条、IP 约 515 条、归因／混淆网络域名 24 条、webshell 约 7 个、工具与脚本约 16 个、可能落地文件约 37 个（含 MD5/SHA-256）。条目太多，本报不逐条抄录，本地已原样存档 `/workspace/enrich-2026-10-08/cisa-aa26-281a-ioc-tables.json`；官方 STIX 在通告页下载。
- 来源：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a ／ https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-vulnerability-scanning-and-spear-phishing-tools-operated

**Zscaler TraderTraitor（厂商原样，MD5）**
- `9d78ece09457907b730d139e4e0c64dd`（terraform-provider-awsbeta_v1.0.0）／`73adaea97f003735335505858c1c6def`（safari_updater）／`116f7189ed7b41f1b339a749d56e63be`（HiraginoSans-Bold.woff）／`be60c52ca8a01fef7dc15c2f0ebb77d8`（HiraginoSans-Regular.woff）／`58fa0d651898446d5f5d2ed8a27a3330`（MalgunGothic-Bold.woff）／`2621753691be9521288664bb551dfba6`（MalgunGothic-Italic.woff）／`ad0b1b6d2c8b9d09d6473a4a299470ab`（NotoSansCJK-Bold.woff）／`4b8509cde757b5428e5f99c8dffe73ca`（NotoSansCJK-ExtraBold.woff）／`3826dc7a9ba8bd5b1c143560c1530d89`（NotoSansCJK-Italic.woff）／`34a52e6a4d803e94fe497bab682abfd3`（NotoSansCJK-Regular.woff）／`2b81aceab0142472d94eb42e500b27b1`（imagent，ROOFDECK macOS）／`9d88b4494c7bc27b10358b68a899ad54`（update.exe，ROOFDECK Windows）
- 网络：`hxxps://diagnose.hashicorp-terraform[.]io/plugins/grpc/v6/schema/metrics/333afe63-c5a2-43f0-b046-7cbaa7797e8a`／`hxxps://supportaru.serveftp[.]com/statics/cache/v11/`／`hxxps://raw.githubusercontent[.]com/bluearuhost/hospitalrun-frontend/refs/heads/main/public/fonts/version1/`／`hxxps://stage-fashion365.vercel[.]app/static/tinymce4.7.5/plugins/fonts/v1104/`／`hxxps://arusupport-region1-webhook[.]online/statics/cache/v11/abicfjej`（FLATROOF C2）／`hxxps://pastebin[.]com/raw/3yptBDhL`（ROOFDECK）／`delay.servehttp[.]com`（ROOFDECK C2）
- AES key（loader）：`PTa3WZPQZAjj55t@`（转自 RST Cloud 抽取）
- 来源：https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver

**ESET MATCHBOIL（厂商原样，SHA-1）**
- `B6569B0050B864C4A0D32326954BC2D3852A3958`（PlannerLibrary.dll）／`A926889BAB31F3C34663D18C05C4E862EF367028`（AnimalUpdater.exe）／`026F892630D0A4FE854A75984695BA99AF0022C4`（bootloader.exe）／`F886B615CB9E23EAD2718FF2A61155ACFB04CE9E`、`1E2C4AAC30EDFF86CD9A30BD08B199BCD3D0CCCE`（PlannerAssistantManager.exe）／`C85D28F7D272CE2BBBFB9DAE71D21BF25B8D00FC`（RegularExpressionExplorer.exe）／`6D72B56B86FD5ED9BD188C8C88CFC69476F836E7`（HelpersLibraries.dll）
- C&C：`virtualdailyplanner[.]pro`、`telemetry-conf[.]com`（Cloudflare 后）／`64.95.10[.]223`（`flycloud-service[.]com`）／`64.95.13[.]210`（`airarticlegenerate[.]com`）
- 来源：https://www.welivesecurity.com/en/eset-research/matchboil-new-tricks-same-old-evil-intentions/

**tensorlake Mini Shai-Hulud（SafeDep 原样）**
- 包 `tensorlake@0.5.144`，文件 `lib/Math_Symbol.js`；域名 `iseekaigogo[.]com`；以太坊合约 `0xb614155Fd88114d40549b259457Bcf921Df091B9`；GitHub 签名账号 `thebeautifulmarchoftime`；外传仓库描述 `Shai-Hulud: Here We Go Again`；组件 `gh-token-monitor`
- 来源：https://safedep.io/tensorlake-npm-compromise-mini-shai-hulud

**vx-underground Linux Sliver（X 帖原样，未验证）**
- C2：`lmfaoxd(.)lol`／`bucket.lmfaoxd(.)lol`／`proxy.lmfaoxd(.)lol`
- 智能合约：`0x0000000000d2dCC83D913bd90653b2ef69340f87`
- SHA256：loader `ed11f431ce9bda16dd98558ec996c53a80841083c0c00deef215c2b0889d1b34`／Sliver（解密）`2c01c232d9d054efd6949695c3c7aeddbeb68fa3a848b7632cd634eb7b59de4d`／Sliver（加密）`2f8e4c5baa78f4d68cc9ac06d4bd33b4420d2d35b8168d195069a0b32c602702`
- 路径：`~/.config/.pipeaudio/.env`、`~/.config/systemd/user/flawless.service`
- 来源：https://x.com/vxunderground/status/2108445132685021424

**Bricksforge CVE-2026-85097**：仅行为特征（见 X-4），未见公开 IP／哈希。

**本地 IoC JSON**：`/workspace/enrich-2026-10-08/iocs-2026-10-08.json`

**其余条目**：Citrix 107406、KEV 新增 5 条、Atlassian（无新增）、LibreOffice／OpenCTI／AnyDesk／Ghostscript／gVisor／DCGM／GoBalance／libjxl、Pwn2Own、ASHVEIN、各工具、IDCF、意大利外交部、UNCONFIRMED 声称——**未见公开 IoC**；Midnight Mimosa／DarkSword／Cofense／MALFEX／Azure30／Talos UAT-11985 的 IoC 在原文，未抄录。

## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/ （仍是 RBNEWS618 https://risky.biz/RBNEWS618/ ／SRB185／RB854／SOAPBOX111；RBNEWS619、SRB186、BTN185 均 404）
- tl;dr sec 通讯：https://tldrsec.com/ （**#349 已出，约 10-08**：「Vulns & Exploits in the AI Era, Package Manager Sandboxing, Testing AI Sandboxes」，原文页 403 未抓取，推定 URL https://tldrsec.com/p/tldr-sec-349）
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form

本日 LWiS List（500 成员分 10 批，窗口约 36h，共 103 帖）另计入 24 条（与 B 组重叠的 @hacktricks_live、@Synacktiv、@ipurple ImmoralFiber 记在 B 组）：@vxunderground 的 Linux Sliver 样本；@thomasrinsma LibreOffice PoC；@egeblc OpenCTI MSF 模块；@N3mes1s gVisor；@SwitHak 的 ESET MATCHBOIL、OpenAI 假门面行动、Rybar 逮捕；@ipurple Kerberos 委派与 Copilot 后渗透；@_CobaltStrike Linux Beacon；@Dinosn 转发的 FBI／Flax、IDCF、意大利外交部、FakeGit、tensorlake、BraZetsu、CastleStealer、JPCERT、NVIDIA DCGM、StyleSmuggler；@0xAsm0d3us reveal.js；@payloadartist 微软赏金；@ntlmrelay 分享榜。博客清单交叉：Huntress、Talos、ESET、Zscaler、Horizon3 当天有新文（已入正文）；watchTowr（最新 10-06）、SentinelLabs、Check Point、Securelist、Proofpoint、DoublePulsar、Trend Micro、Unit 42（最新 10-07）当天没有新文；GTIG、MSRC blog RSS 为空，未判断。

## 来源搜索 URL

- X Search A（Latest）：https://x.com/search?q=(CVE%20OR%20POC%20OR%20exploit%20OR%200day)&f=live
- X Search A′（本轮实际查询）：https://x.com/search?q=(%22CVE-2026%22%20OR%200day%20OR%20%22zero-day%22%20OR%20%22actively%20exploited%22%20OR%20%22exploited%20in%20the%20wild%22)%20-filter%3Areplies&f=live
- X Search B（Latest）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live （本轮另用 `url:github.com (C2 OR "red team" OR pentest OR nuclei OR EDR OR BOF OR exploit OR PoC OR implant OR evasion)`）
- X Search C（Latest）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live （本轮另用 IOCs／SHA256／C2／attribution 组合）
- X 针对性查询：`"CVE-2026-107406" OR "APSB26-146" OR "CVE-2026-75650" OR AhsayCBS OR "Defender zero-day" OR "CVE-2026-85097" OR "AA26-281A"`
- LWiS X List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 通告 RSS：https://www.cisa.gov/cybersecurity-advisories/all.xml
- Cisco PSIRT RSS：https://sec.cloudapps.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml
- Fortinet PSIRT RSS：https://filestore.fortinet.com/fortiguard/rss/ir.xml
- Palo Alto RSS：https://security.paloaltonetworks.com/rss.xml
- Citrix 公告：https://support.citrix.com/external/article/CTX697191
- GitHub releases：https://github.com/BishopFox/sliver/releases ／ https://github.com/projectdiscovery/nuclei/releases ／ https://github.com/projectdiscovery/nuclei-templates/releases ／ https://github.com/jm33-m0/emp3r0r/releases
