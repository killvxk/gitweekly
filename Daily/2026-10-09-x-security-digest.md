# X 安全情报晚报 · 2026-10-09

> 搜集窗口：圣地亚哥时间 **2026-10-08 20:30 至 2026-10-09 20:15**（America/Santiago / UTC-3，约 24 小时）。ISO／X 搜索：`start_time=2026-10-08T23:30:00Z`，`end_time≈2026-10-09T23:15:00Z`（接口将 end 微调到至少 10 秒前）。
> **X 采集方式**：使用 Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`／`get_posts_by_id(s)`，含 t.co 展开字段），**未开浏览器，未检查 @seogoogle4 浏览器登录状态**。A 组先 recency 试跑噪声过大，改用 relevancy＋`CVE-2026` 定向；B／C 各 relevancy；另做 PaperCut／Longlegs／DarkSword／GhostAction 定向查询；LWiS List 500 handle 分批 `from:`（本轮完成约 12 批高价值批次，含 chudyPB／vxunderground／Dinosn／L0Psec／_xpn_ 等）。本轮约 **20** 次 X 读取（未触日限／分钟限）。合并 **54** 条安全相关新帖（A22／B2／C14／LWiS16），与 seen_ids 去重。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON `/workspace/kev-2026-10-09.json`（= `/workspace/enrich-2026-10-09/kev.json`）；厂商／研究页抓取于 `/workspace/enrich-2026-10-09/`（Citrix CTX697191、CrowdStrike ARTEX、Lumen PoeLLM IoC、watchTowr PaperCut、THN AnyDesk／GhostAction／DarkSword／Ahsay／Flax、PolySwarm Warlock、iVerify P7、Risky／tl;dr 首页、GitHub releases）。
> **CISA KEV：catalogVersion 2026.10.08／1739 条，Δ+0**（相对昨日同一版本；dateReleased 仍 2026-10-08T20:09Z）。**今日无 NEW**。
> **due_today（10-09）：无**；**newly_overdue：无**（昨日起逾期的 Citrix CVE-2026-88779 继续逾期）；**upcoming 7 天：6 条**（AA26-281A 五条 due **2026-10-11**；Apple CVE-2026-86950 due **2026-10-13**）；**仍逾期高信号 26 条**（含 Citrix 88771／88772／88779、FortiMail 104286、Zammad 102489／102490、Cisco 76504 等）。CVE-2026-107406 **仍未进 KEV**。
> 抓取备注：BleepingComputer 首页 403；PaperCut 厂商 security 页返回异常／404；Adobe／部分厂商页未再抓；Risky Business 首页仍见 RBNEWS618（未见更新集）；tl;dr sec 最新仍为 **#349**（未见 #350）；LWiS 未跑满全部 20 批（覆盖关键研究者批次，剩余批次窗口内多为闲聊／RT）。
> 规则：每条含完整 https URL；分列 X 原帖／GitHub·PoC 仓库／厂商公告／文章；没有指标就写「未见公开 IoC」；不编造；**不转载利用代码／payload／PoC 步骤**；泄露／入侵声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【新 · 在野 · 补丁绕过链】PaperCut NG／MF 预认证 RCE 连环绕过（watchTowr，10-09）** 原链 CVE-2026-81578＋82078 打 26.0.3；后续补丁多次被绕，现公开 WT-2026-0143（无 CVE）＋CVE-2026-82077，可打至 26.0.4-PO；**修复版 26.0.5**。
  文章：https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/
  X 原帖：https://x.com/watchtowrcyber/status/2108622632740704672
- **【PoC 公开 · 有补丁】AnyDesk Linux AnyPwn**（8.0.2 预认证堆溢出→root；**8.0.3 已修**，changelog 仅写 crash；**无 CVE／未进 KEV／未见在野**）。
  文章：https://www.threatwire.tech/research/anydesk-linux-anypwn-exploit-targets-fixed-pre-auth-bug
  GitHub：https://github.com/v12-security/pocs/tree/main/anydesk
- **【APT · 有 IoC】Longlegs（Storm-2603）经 SharePoint ToolShell 投 Warlock**，用水务／电信／政府目标；经 SYSVOL／dfsrs 域内扩散；Symantec／PolySwarm。
  文章：https://blog.polyswarm.io/china-linked-warlock-ransomware-campaign-targets-critical-infrastructure
  X 原帖：https://x.com/DFIR_Radar/status/2108589184227352643
- **【供应链 · 有 IoC】GhostAction**：恶意 GitHub Actions「security audit」工作流，波及数万仓库；C2 `193.32.204.199`。
  文章：https://thehackernews.com/2026/10/credential-stealing-github-actions.html
  X 原帖：https://x.com/DFIR_Radar/status/2108664624669454775
- **【iOS · 有 IoC】P7 DarkSword**（iVerify／Censys）：Keychain／钱包窃取＋双向 C2；修 **iOS 18.4.1+**。
  文章：https://www.iverify.com/blog/darksword-variant-threat-research
  文章：https://thehackernews.com/2026/10/p7-darksword-ios-exploit-kit-adds.html
- **【跟踪】Citrix CVE-2026-107406** 继续发酵（仍未见利用、未进 KEV）；**AhsayCBS 105133／105134** 仍无补丁且 PoC 流传；**AA26-281A 五条 KEV due 10-11**。
  厂商：https://support.citrix.com/external/article/CTX697191
  政府：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- **【Malware · 有 IoC】PoeLLM**（Lumen Black Lotus，AI 服务器挖矿／利用机器人）；**macOS Element 仿冒**（L0Psec，proxy08.com）。
  文章：https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware
  X 原帖：https://x.com/L0Psec/status/2108663107824345098
- **【工具】** emp3r0r 仍 v4.24.1；Sliver v1.7.8；nuclei v3.11.1；nuclei-templates v10.5.0 — **本日核心工具无新版**。ai-llm-red-team-handbook 热度上升；rad9800 Diaspore。
  GitHub：https://github.com/jm33-m0/emp3r0r/releases/tag/v4.24.1
- **【合并统计】** X **54**（A22／B2／C14／LWiS16）；seen_ids **2502→2572**；KEV **2026.10.08／1739／Δ0**；Risky RBNEWS618；tl;dr #349；报告本路径。

## CVE / POC / 漏洞

### X-1. 【X 交叉 · 新公开 · 在野 · 有补丁】PaperCut NG／MF 预认证 RCE 与多次补丁绕过（CVE-2026-81578／82078／82077＋WT-2026-0143）
watchTowr（Piotr Bazydło @chudyPB）10-09 发文梳理自 8-27 起的 PaperCut「在野利用→无补丁公告→多次补丁绕过」时间线。最初在野链针对 **26.0.3**：CVE-2026-81578（认证绕过）＋CVE-2026-82078（认证后 RCE）。后续 26.0.4／26.0.4-PO 补丁不完整；现公开 **WT-2026-0143**（认证绕过，**未单独分配 CVE**）与 **CVE-2026-82077／WT-2026-0144**（Scan to Fax 相关路径问题，认证后 RCE）。完整链可打到 **26.0.4-PO build 76508**。**PaperCut 于 9-10 发布 26.0.5**，修 WT-2026-0143 与 82077。防御：立即升到 **≥26.0.5**；在代理／Web 日志狩猎 `POST /app` 且含 `service=direct/1/Home/Setup`、以及 `scanActionType=FAX` 且 `faxProviderModel` 含异常路径特征；审查 Config Editor 对 `system.scan.fax.send.command-args` 的改动；可用 watchTowr DAG **只测暴露、不执行完整链**。未进 KEV（本日）。
地址：
- X 原帖（watchTowr）：https://x.com/watchtowrcyber/status/2108622632740704672
- X 原帖（DFIR Radar 摘要）：https://x.com/DFIR_Radar/status/2108619526317527122
- X 原帖（/r/netsec）：https://x.com/_r_netsec/status/2108626889481007162
- X 原帖（CveTodo）：https://x.com/CveTodo/status/2108664462286709038
- X 原帖（作者 RT）：https://x.com/chudyPB/status/2108627408957940061
- 文章 watchTowr Labs：https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/
- GitHub（DAG，非利用步骤）：https://github.com/watchtowrlabs/watchTowr-vs-PaperCut-WT-2026-0143/
- NVD（按 CVE 构造）：https://nvd.nist.gov/vuln/detail/CVE-2026-82077
IoC：未见公开 C2／哈希；狩猎特征见上（行为／日志）。

### X-2. 【X 交叉 · PoC 公开 · 有补丁 · 未见在野】AnyDesk Linux AnyPwn（8.0.2 → root；修于 8.0.3）
V12 Security 公开 AnyPwn：AnyDesk Linux **8.0.2** 会话协议堆溢出，研究者称可在连接被接受前以 root 执行命令。厂商 **2026-06-23** 发 **8.0.3**，changelog 仅「Fixed a bug that could lead to a crash」；**截至 10-09 无 CVE、无安全公告、未进 KEV、未见在野利用**。防御：Linux AnyDesk 升到 **≥8.0.3**；限制管理端口暴露；勿在未打补丁主机上对不可信端点开放。
地址：
- X 原帖（ThreatWire）：https://x.com/ThreatWire_/status/2108577298936893771
- X 原帖（spinidg）：https://x.com/spinidg/status/2108583975987900600
- X 原帖（Python_s_／NØØT）：https://x.com/Python_s_/status/2108697150225793472
- 文章 ThreatWire：https://www.threatwire.tech/research/anydesk-linux-anypwn-exploit-targets-fixed-pre-auth-bug
- 文章 The Hacker News：https://thehackernews.com/2026/10/researchers-publish-working-exploit-for.html
- GitHub（PoC 仓库，**不转载步骤**）：https://github.com/v12-security/pocs/tree/main/anydesk
- 厂商 changelog：https://anydesk.com/en/changelog/linux
IoC：未见公开 IoC。

### X-3. 【跟踪 · 未进 KEV】Citrix NetScaler CVE-2026-107406（SAML 内存溢出，CVSS 9.5）
窗口内持续跟进：须确认是否配置 SAML SP／IdP，并升到 **14.1-73.46／13.1-64.29**（及对应 FIPS／NDcPP）。Citrix 称公告时未见利用。与已逾期的 88771／88779 一并复查。
地址：
- X 原帖（morphisec）：https://x.com/morphisec/status/2108592093299949772
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2108461775205310923
- X 原帖（Python_s_）：https://x.com/Python_s_/status/2108591070149787694
- X 原帖（The_Cyber_News）：https://x.com/The_Cyber_News/status/2108376428060549213
- 厂商 CTX697191：https://support.citrix.com/external/article/CTX697191
- 文章 THN：https://thehackernews.com/2026/10/citrix-patches-critical-netscaler-flaw.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-107406
IoC：未见公开 IoC（未见利用）。

### X-4. 【跟踪 · 在野 · 无补丁】AhsayCBS CVE-2026-105133＋105134
Huntress 链仍有效；DFIR Radar 称 **PoC 已流传**（10-07 起）。**10.3.4 及以下受影响，厂商尚无补丁**。防御同昨日：管理面只对可信网络开放；狩猎 `cbssvcX64.exe` 异常子进程与假 Edge 挖矿服务；命中倾向整机重建。
地址：
- X 原帖：https://x.com/DFIR_Radar/status/2108649723099767198
- 厂商 Huntress：https://www.huntress.com/blog/ahsaycbs-flaws-exploit
- 文章 THN：https://thehackernews.com/2026/10/attackers-exploit-ahsaycbs-flaws-to.html
- GitHub（Huntress 规则／目录）：https://github.com/huntresslabs/threat-intel/tree/main/2026/2026-10
IoC：见昨日晚报「Huntress AhsayCBS」；本窗口无新公开哈希表。

### X-5. 【KEV 状态 · Δ0】catalogVersion 2026.10.08／1739；AA26-281A 五条 due 10-11
本日 KEV **无更新**。即将到期：
- 2026-10-11：CVE-2015-5477（ISC BIND）、CVE-2016-3081（Apache Struts）、CVE-2023-22894（Strapi）、CVE-2021-3199（ONLYOFFICE）、CVE-2015-3306（ProFTPD）
- 2026-10-13：CVE-2026-86950（Apple）
联合通告与处置：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
IoC：见 AA26-281A／昨日汇总。

### X-6. 【其他提及／研究】
- Cisco NX-API RCE（cisco-sa-napi-rce-r2shwu2j／CVE-2026-76471 等，延续 10-07 批量）：X https://x.com/Python_s_/status/2108606807706882121 ／ 厂商 https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-napi-rce-r2shwu2j
- GTIG「AI 时代漏洞披露与利用趋势」：X https://x.com/ptdbugs/status/2108595325069930748 ／ 文章 https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era/
- ThaiCERT：Rejetto HFS Session 伪造告警：https://x.com/ThaiCERTByNCSA/status/2108377551269965918
- DFIR_Lab 提及 CVE-2026-69461（Windows NTFS，CVSS 8.8）— **未独立核实一手公告，仅作跟踪**：https://x.com/DFIR_Lab/status/2108353064289624241
- Atlassian CVE-2026-21589：**KEV 仍未收录**（延续）。
IoC：以上未见新增公开 IoC。

### P-1. 【仍逾期高信号 26 条】
Citrix 88771／88772／**88779**、Check Point 85102／93616、Arista 93952、F5 94127、JFrog 42016／42018、Zyxel 7273、Microsoft 81963／85880／65660、Google 87491／85046／58704、Cisco 76460／76504、Acronis 87886、WSO2 5430、Adobe 71362、MikroTik 67279、WordPress 87902、Fortinet 104286、Zammad 102489／102490。
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

## 工具与 GitHub 发布

### 1. 核心 C2／扫描器：本日无新版
- emp3r0r **v4.24.1**（10-09 08:16Z，昨日晚报已覆盖）：https://github.com/jm33-m0/emp3r0r/releases/tag/v4.24.1
- Sliver **v1.7.8**：https://github.com/BishopFox/sliver/releases/tag/v1.7.8
- nuclei **v3.11.1**：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates **v10.5.0**：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.0

### 2. AI／LLM 红队手册热度
- X：https://x.com/gitrepos/status/2108633795922444375
- GitHub：https://github.com/Shiva108/ai-llm-red-team-handbook

### 3. Diaspore（rad9800）：可移植 Python 子集／沙箱运行时
- X：https://x.com/rad9800/status/2108691674138583483
- GitHub：https://github.com/radkawar/diaspore
- 文档：https://radkawar.github.io/diaspore/

### 4. 其他
- OSINT Cheat sheet：https://x.com/7h3h4ckv157/status/2108612646010519835 ／ https://github.com/Jieyab89/OSINT-Cheat-sheet
- ProjectDiscovery 文章「How abliterated models can get you pwned」：https://x.com/pdiscoveryio/status/2108550060980277626
- Synacktiv fusetea（**昨日已报，seen**）：https://x.com/Synacktiv/status/2108477586896474340

## APT / Malware 分析

### X-1. 【Symantec／PolySwarm · 有 IoC】Longlegs（Storm-2603）→ Warlock
经本地 SharePoint **ToolShell** 链初始访问，LAYOUTS webshell、窃取 machine key；LotL（msiexec←Catbox／Wasabi、NetExec、VS Code Insiders 隧道、DLL 侧载）；部分入侵滥用 K7RKScan 驱动（CVE-2025-1055，BYOVD）杀软；**经 SYSVOL＋dfsrs.exe 域内分发 Warlock**。样本哈希见下方汇总。
地址：
- X 原帖（DFIR Radar）：https://x.com/DFIR_Radar/status/2108589184227352643
- X 原帖（PolySwarm）：https://x.com/PolySwarm/status/2108626885856919775
- 文章 PolySwarm：https://blog.polyswarm.io/china-linked-warlock-ransomware-campaign-targets-critical-infrastructure
IoC：见汇总「Longlegs／Warlock」。

### X-2. 【供应链 · 有 IoC】GhostAction 恶意 GitHub Actions
攻击者盗用维护者身份写入 `security-audit.yml`／`github_actions_security.yml`，扫仓库与 git 历史中的密钥，经 HTTP 外泄到 **193.32.204.199**。防御：全库搜上述工作流文件名（约 8-31 起）；命中即轮换全部 Actions／历史密钥、删工作流并审计 fork。
地址：
- X 原帖：https://x.com/DFIR_Radar/status/2108664624669454775
- 文章 THN：https://thehackernews.com/2026/10/credential-stealing-github-actions.html
IoC：见汇总「GhostAction」。

### X-3. 【iOS · 有 IoC】P7 DarkSword／Coruna
iVerify／Censys：链 CVE-2025-24201＋CVE-2025-31200，注入 SpringBoard，双向 C2，Keychain／Notes／钱包（含 imToken／BitKeep）。须更新到 **iOS 18.4.1+**。基础设施 IP／域名见汇总。
地址：
- X 原帖：https://x.com/DFIR_Radar/status/2108634561802321920
- X 原帖（续）：https://x.com/DFIR_Radar/status/2108694540232139043
- X 原帖：https://x.com/siliconsandshq/status/2108500551692390450
- 文章 iVerify：https://www.iverify.com/blog/darksword-variant-threat-research
- 文章 Censys：https://censys.com/blog/darksword-coruna-open-directory-finding-report/
- 文章 THN：https://thehackernews.com/2026/10/p7-darksword-ios-exploit-kit-adds.html
IoC：见汇总「P7 DarkSword」。

### X-4. 【Lumen · 有 IoC】PoeLLM（Canto Incognito）
针对 LiteLLM／Ollama／Gotenberg 等 AI 相关服务的恶意软件，挖矿与利用机器人化。IoC 文件由 Black Lotus Labs 发布。
地址：
- X 原帖：https://x.com/Python_s_/status/2108639832360505592
- 文章：https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware
- GitHub IoC：https://github.com/blacklotuslabs/IOCs/blob/main/PoeLLM_IOCs.txt
IoC：见汇总「PoeLLM」。

### X-5. 【LWiS · 有 IoC】macOS「Element」仿冒加载器
L0Psec／malwrhunterteam：样本与 `element.proxy08.com`／`proxy08.com` 通信，DMG＋AppleScript→curl|zsh→嵌入 Mach-O（CCCrypt）。
地址：
- X 原帖（主帖）：https://x.com/L0Psec/status/2108663107824345098
- X 原帖（哈希／域名）：https://x.com/L0Psec/status/2108663131367244071
IoC：见汇总「macOS Element／proxy08」。

### X-6. 【跟踪／UNCONFIRMED】
- CrowdStrike ARTEX 针对韩国金融（续报）：https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/ ／ X https://x.com/catnap707/status/2108695772279849165
- Tensorlake／Shai-Hulud npm（昨日已报）：https://socket.dev/blog/tensorlake-compromise
- FBI 再捕 ShinyHunters 相关嫌疑人：https://thehackernews.com/2026/10/fbi-arrests-another-shinyhunters.html
- 多条勒索／库售卖帖（Quick France、China Mobile 8.5 亿条、Gate Crypto 等）一律 **UNCONFIRMED**：例如 https://x.com/intels_daily/status/2108695785080520984
- _xpn_「Bye Deno, our malware barely knew thee…」：https://x.com/_xpn_/status/2108650463339892801 （上下文为讨论向，未见附 IoC）
IoC：ARTEX／Tensorlake 沿用既有报告；勒索声称未见公开可核验 IoC。

## 地址／IoC 汇总

### Longlegs／Warlock（DFIR Radar 转 Symantec／PolySwarm 摘要，原样）
- 样本 SHA256：`206f27ae820783b7755bca89f83a0fe096dbb510018dd65b63fc80bd20c03261`
- 样本 SHA256：`ae9f7fce57c7b928e659dccf0e00fa79cd9cd61a106f18d4e03f92dc3a03c295`
- 行为狩猎：SharePoint `w3wp.exe` 异常子进程；LAYOUTS 新 webshell；msiexec 访问 Catbox／Wasabi；`code-insiders.exe` 作服务／隧道；**dfsrs.exe 作为非标准可执行父进程**；勒索说明 `how to restore your files.txt`；run.exe／rune.exe
- 文章：https://blog.polyswarm.io/china-linked-warlock-ransomware-campaign-targets-critical-infrastructure

### GhostAction（DFIR Radar／THN 摘要，原样）
- C2 IP：`193.32.204.199`
- 工作流文件名：`security-audit.yml`、`github_actions_security.yml`
- 文章：https://thehackernews.com/2026/10/credential-stealing-github-actions.html

### P7 DarkSword（DFIR Radar／iVerify／Censys 摘要，原样，部分已去混淆写法）
- 基础设施 IP：`43.134.165.205`、`166.88.95.90`、`23.148.212.237`、`47.102.192.23`、`156.239.230.120`
- 域名：`66ds.lol`、`agdx53.cc`、`cdn.gotoiphone.com`、`mzpo30.cam`
- 本机路径线索：`/private/var/tmp/keychain_c2_dump.json`、`keychain_c2_dump.done`、`p7_debug.log`、`c2_wallet_debug.log`
- 文章：https://www.iverify.com/blog/darksword-variant-threat-research ／ https://censys.com/blog/darksword-coruna-open-directory-finding-report/

### PoeLLM（Black Lotus Labs 文件原样）
- C2 IP（仍活跃／曾活跃）：`92.119.164.50`、`103.249.201.108`、`178.128.14.204`、`136.148.69.233`、`185.132.53.158`、`120.224.114.212`、`5.78.73.122`、`15.204.178.28`、`92.119.165.74`、`45.133.73.28`、`89.39.253.46`、`191.37.28.160`
- SHA256：`6fab94577364beec314afae3b082dd680933f08a8349b9f35b92667e8231b501`、`350a99830b80b5600d3a2757fa996155579ef9d0c53de95f0299f64d280b9bb1`、`f706aba0d150db2d8f385cbbbb6a6d4fe590a5d184f29e5b1b05fcc4c2cd0932`
- 来源：https://github.com/blacklotuslabs/IOCs/blob/main/PoeLLM_IOCs.txt

### macOS Element／proxy08（L0Psec 原样）
- SHA256：`29fc5399903e47f7aa13f932ed88ea8770456e2ec860898f2b207d53db075355`（st_helper611b_arm64）
- SHA256：`79433c988f7cbb90b5356b53719a3d4601a35819e9fd0e00ede15591d8152d29`
- SHA256：`bd093cce8b2c7afb507b8452dc51098ab91e65be549470f293d0bd0a3d9786ee`
- 域名：`proxy08.com`、`element.proxy08.com`
- X：https://x.com/L0Psec/status/2108663131367244071

### 其他
- PaperCut／AnyDesk／Citrix 107406：未见公开网络 IoC
- AA26-281A／AhsayCBS／Tensorlake：见既有晚报与厂商原文

## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/ （首页仍见 **RBNEWS618**，本窗口未见更新集）
- tl;dr sec 通讯：https://tldrsec.com/ （最新仍 **#349** — Vulns & Exploits in the AI Era…；未见 #350）
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form

本窗口 LWiS 交叉要点：@watchtowrcyber／@chudyPB PaperCut；@L0Psec macOS 样本；@Dinosn 转发／摘录 Citrix、ARTEX、Flax、固件预装恶意软件等；@rad9800 Diaspore；@_xpn_ Deno／模型政策讨论。

## 来源搜索 URL

- X A（relevancy）：query≈`(CVE OR "proof of concept" OR 0day OR RCE) …` + 时间窗
- X A CVE：`(CVE-2026 OR CVE-2025 OR …)` + 时间窗
- X B：`url:github.com (C2 OR "red team" OR nuclei OR cobalt OR sliver OR havoc)` + 时间窗
- X C：`("malware analysis" OR "threat report" OR "threat actor") …` + 时间窗
- X 定向：PaperCut／watchTowr；Longlegs／DarkSword／GhostAction／PoeLLM
- X LWiS：`from:h1 OR from:h2 …`（约 12 批×25 handle）+ 时间窗
- KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- Risky：https://risky.biz/
- tl;dr：https://tldrsec.com/
