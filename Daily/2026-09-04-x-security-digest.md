# X 安全情报晚报 · 2026-09-04

> 搜集窗口：圣地亚哥时间 **2026-09-03 20:00 至 2026-09-04 ~20:20**（America/Santiago / UTC-4）。**本报为官方 20:00 cron 晚报（周五）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-04.json`（collected_at **2026-09-04T20:14:29-04:00**）＋ `/workspace/tools-news-pulse-2026-09-04.md`。CISA KEV catalogVersion **2026.09.04**／**1695** 条／dateReleased **2026-09-04T16:47:03.5197Z**（相对昨日 **+1**：新增 **CVE-2026-85046** Chromium V8）。
> **期限今日 09-04：无。** **期限明日 09-05（5 条紧急）**：Kestra **CVE-2026-49869**、JFrog **CVE-2026-82329**、Sangoma **CVE-2026-9586**、SonicWall **CVE-2026-83548/83549**。PaperCut due **2026-09-14**；LiteLLM／Starlette due **09-16**；Chromium 85046 due **09-18**。TrueConf **CVE-2026-72530** 已过 due（09-03）。
> X：`/workspace/x-posts-2026-09-04.json`（合并 **60** 条：A 8／B 8／C 39／LWiS 5；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.38h**（高流量，**远不足 24h**）。Search B 约 **18.25h**。Search C 约 **9.54h**。LWiS List 约 **12.8h**。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · KEV 新入】Google Chromium V8 CVE-2026-85046**（类型混淆；远程经恶意 HTML 在沙箱内执行；影响 Chromium 系浏览器）。Google 称**在野利用已存在**。Stable **152.0.7977.82/.83**（Win/Mac）／**152.0.7977.82**（Linux）。联邦 BOD 26-04 期限 **2026-09-18**。立即升级 Chrome／Edge／Opera 等，**不转写利用细节**。
  厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
  CISA：https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85046
  文章：https://aviatrix.ai/threat-research-center/chrome-zero-day-cve-2026-85046-v8-type-confusion-september-2026/
  X：https://x.com/aviatrixtrc/status/2096027275590352999

- **【期限倒计时 09-05】** 五条仍 due **明日**：Kestra／JFrog／Sangoma／SonicWall SMA1000（83548/83549，SNWLID-2026-0016）。LiteLLM／Starlette due 09-16。
  警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
  SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

- **【PaperCut 续】** NG／MF **CVE-2026-81578/82078** 仍 KEV（due 09-14）。**R3** 仍为紧急补丁；09-04 仅状态更新（2:48pm AEST，无新情报，正式版仍在推进）。公网未打补丁应假定失陷。
  厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/

- **【X 交叉 · Citrix NetScaler 线索】CVE-2026-19490** 认证绕过／活跃利用讨论（Undercode／Aviatrix TRC）；**未入本报 KEV**。另有旧 **CVE-2023-4966** 横向移动叙述。核对 Citrix 官方补丁通道后再行动；**不转写利用链**。
  文章：https://aviatrix.ai/threat-research-center/critical-citrix-netscaler-auth-bypass-cve-2026-19490-attacks https://undercodetesting.com/citrix-netscaler-cve-2026-19490-critical-authentication-bypass-under-active-exploitation-patch-immediately-video/
  X：https://x.com/UndercodeUpdate/status/2096028308479582609 https://x.com/aviatrixtrc/status/2096024806940348536

- **【LWiS · ClickFix／Exodus RAT】** 篡改版 Citrix Diagnostics Hub v28 安装器经 ClickFix 传播；Huntress／VT 样本与 C2。
  文章：https://www.huntress.com/blog/exodus-crypto-wallet-installer-rat
  VT：https://www.virustotal.com/gui/file/4e57b380eb734992865209eac4cea5d078d7b8841884c47225f20f2df7f682bf/behavior
  X：https://x.com/Shammahwoods/status/2096006009722716361

- **【工具】** Sliver **仍 v1.7.7**；nuclei-templates **仍 v10.4.8**。X 窗：Mythic Ornn、Erebus、Agentseal、FalconFlank、edrEvasionWorkshop、OsintGodseye。
  仓库：https://github.com/BishopFox/sliver/releases/tag/v1.7.7 https://github.com/n0qword/mythic_ornn https://github.com/Whispergate/Erebus https://github.com/getagentseal/agentseal

- **【APT／威胁报告】** Sygnia **Fire Ant**（中国关联、针对受信基础设施）；Google GTIG AI 工具使用；Unit 42 AI 加速攻击（续传）；Recorded Future 自动化签名；暗网／勒索声称大量（未独立核实）。
  https://www.sygnia.co/press-release/sygnia-reveals-new-activity-by-china-nexus-threat-actor-fire-ant-targeting-trusted-infrastructure/
  https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools
  https://unit42.paloaltonetworks.com/ai-assisted-cyber-attack-inside-a-unit-42-investigation/
  https://thehackernews.com/2026/01/experts-detect-pakistan-linked-cyber.html

- **【新闻备援】** Risky Biz **新 RBNEWS609**／**RBFEATURES38**；另 SRB182／RB851／RBNEWS608／BTN181；tl;dr sec 仍 **#343**。ICS **无新发**（仍 ICSA-26-246-*）。
  https://risky.biz/RBNEWS609/ https://risky.biz/RBFEATURES38/ https://tldrsec.com/p/tldr-sec-343

## CVE / POC / 漏洞

### 1. 【KEV 新入】Google Chromium V8 CVE-2026-85046

V8 类型混淆（CWE-843）；恶意 HTML 可在沙箱内任意代码执行；可影响 Chrome／Edge／Opera 等 Chromium 浏览器。Google Stable 09-03 发布 **152.0.7977.82/.83**，并写明 **CVE-2026-85046 在野利用已存在**。CISA 09-04 入 KEV，due **2026-09-18**。升级浏览器；按 BOD 26-04 评估暴露面。**不转写 PoC。**

地址：
- 厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- CISA：https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85046
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- 文章：https://aviatrix.ai/threat-research-center/chrome-zero-day-cve-2026-85046-v8-type-confusion-september-2026/
- X：https://x.com/aviatrixtrc/status/2096027275590352999

IoC：未见本报统一公开样本哈希；狩猎侧重未升级 Chromium 终端与异常浏览器进程／沙箱逃逸相关告警。

### 2. 【KEV 续／due 09-05】五条紧急

JFrog Artifactory **CVE-2026-82329**、Sangoma Switchvox **CVE-2026-9586**、SonicWall SMA1000 **CVE-2026-83548/83549**、Kestra OSS **CVE-2026-49869** 仍 due **2026-09-05**。LiteLLM **CVE-2026-59822**／Starlette **CVE-2026-48710** due 09-16。

地址：
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-82329 https://nvd.nist.gov/vuln/detail/CVE-2026-9586 https://nvd.nist.gov/vuln/detail/CVE-2026-83548 https://nvd.nist.gov/vuln/detail/CVE-2026-83549 https://nvd.nist.gov/vuln/detail/CVE-2026-49869 https://nvd.nist.gov/vuln/detail/CVE-2026-59822 https://nvd.nist.gov/vuln/detail/CVE-2026-48710
- SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
- nuclei（JFrog）：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-82329.yaml

IoC：未见本条新增统一 IoC；逐厂商公告。

### 3. 【KEV 续】PaperCut NG／MF CVE-2026-81578 ＋ CVE-2026-82078（due 2026-09-14）

Emergency Patch Release 3 仍为累积紧急补丁。09-04 厂商仅发状态更新（无新情报）。公网 Application Server 未打补丁应假定失陷并对照厂商 IoC 狩猎。

地址：
- 厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- KEV／NVD：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-81578 https://nvd.nist.gov/vuln/detail/CVE-2026-81578 https://nvd.nist.gov/vuln/detail/CVE-2026-82078
- 文章：https://www.helpnetsecurity.com/2026/08/31/papercut-attack-remote-access-tools/ https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/

IoC：见「地址／IoC 汇总」。

### 4. 【X 交叉】Citrix NetScaler CVE-2026-19490（未入 KEV）

X／第三方文章称认证绕过并活跃利用；另有 Aviatrix 对旧 **CVE-2023-4966** 横向移动／持久 C2 叙述。**本报未在 KEV 见 19490**；行动前核对 Citrix 官方安全公告编号与补丁。**不转写绕过步骤。**

地址：
- 文章：https://aviatrix.ai/threat-research-center/critical-citrix-netscaler-auth-bypass-cve-2026-19490-attacks https://undercodetesting.com/citrix-netscaler-cve-2026-19490-critical-authentication-bypass-under-active-exploitation-patch-immediately-video/
- X：https://x.com/UndercodeUpdate/status/2096028308479582609 https://x.com/aviatrixtrc/status/2096024806940348536
- CVE 记录页（待核）：https://www.cve.org/CVERecord?id=CVE-2026-19490

IoC：帖内未见具体 C2 域名／IP；未见公开哈希。

### 5. 【X 交叉】Rails／BMP CVE-2026-66066 线索

X 称畸形 BMP 处理可致任意文件读／RCE，并称有公开 GitHub PoC；**本报不转载 PoC，不链接利用仓库**。以发行版／上游补丁通道为准核验。

地址：
- X：https://x.com/SecureChap/status/2096025787337953604
- CVE：https://www.cve.org/CVERecord?id=CVE-2026-66066

IoC：未见公开攻击者 C2／样本哈希。

### 6. 【X】Canva Android CVE-2026-85094

特权 WebView 对外部 origin 返回 headers 限制不足。升级官方应用；未见 KEV。

地址：
- CVE：https://www.cve.org/CVERecord?id=CVE-2026-85094
- X：https://x.com/CVEnew/status/2095921771266597176

IoC：未见公开 IoC。

### 7. 【过期提醒】TrueConf CVE-2026-72530（due 已过 09-03）

仍在 KEV；未补丁环境继续按厂商修复版本与 4307/TCP 暴露面处理。

地址：
- 厂商：https://trueconf.com/blog/news/security-fixes-updates-and-advisories
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-72530
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-72530

IoC：关注 4307/TCP 异常。

### 8. ICS

本日 **无显著新发**（仍为昨日 ICSA-26-246-01..08 等）。例：https://www.cisa.gov/news-events/ics-advisories/icsa-26-246-06

## 工具与 GitHub 发布

### 1. Sliver v1.7.7（续／无新版本）

相对昨日无版本 bump；X 仍传播发布说明（Sleep／Aggressor 脚本、端口转发／SOCKS5 等）。nuclei-templates **仍 v10.4.8**。

地址：
- 仓库：https://github.com/BishopFox/sliver/releases/tag/v1.7.7 https://github.com/BishopFox/sliver
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8
- X：https://x.com/LittleJoeTables/status/2095674373533544895 https://x.com/SagarXploit/status/2095898081170702368

IoC：不适用（合法红队框架发布）。

### 2. Mythic Ornn／Erebus／Agentseal／FalconFlank 等

LLM 辅助 Mythic 开发（Ornn）；Mythic 初始访问封装 Erebus；AI agent 安全工具包 Agentseal；CrowdStrike Falcon 相关特权项目 FalconFlank；EDR 规避工坊材料；OSINT Godseye。

地址：
- https://github.com/n0qword/mythic_ornn
- https://github.com/Whispergate/Erebus
- https://github.com/getagentseal/agentseal
- https://github.com/MSNightmare/FalconFlank
- https://github.com/tyeurada/edrEvasionWorkshop
- https://github.com/jollncoelho/OsintGodseye
- 文章：https://outflank.nl/blog/2026/09/02/red-team-ai-skills/ https://synthesis.to/presentations/recon26_agentic_deobfuscation.pdf
- X：https://x.com/noqword/status/2095918985522942336 https://x.com/cr0nym/status/2095817256202633322 https://x.com/bountywriteups/status/2095792843239690696 https://x.com/ntlmrelay/status/2095830403349192862 https://x.com/r1cksec/status/2095794818039320755 https://x.com/zhetikal77/status/2095949936013500708

IoC：未见公开攻击者 IoC。

### 3. Malware Bible（学习资源）

地址：
- https://github.com/Perkins-Fund/Malware-Bible
- X：https://x.com/the_cyber_bite/status/2095901796812419082

IoC：不适用。

## APT / Malware 分析

### 1. 【LWiS】ClickFix → 篡改 Citrix Diagnostics Hub／Exodus 钱包 RAT

篡改版 Citrix Diagnostics Hub v28 安装器；Huntress 分析关联 Exodus 加密钱包窃取／RAT。样本与 C2 见 IoC。

地址：
- 文章：https://www.huntress.com/blog/exodus-crypto-wallet-installer-rat
- VT：https://www.virustotal.com/gui/file/4e57b380eb734992865209eac4cea5d078d7b8841884c47225f20f2df7f682bf/behavior
- X：https://x.com/Shammahwoods/status/2096006009722716361

IoC：`granoco[.]com`；`85[.]239[.]149[.]120`；SHA256 `4e57b380eb734992865209eac4cea5d078d7b8841884c47225f20f2df7f682bf`

### 2. Sygnia Fire Ant（中国关联）

针对受信基础设施的新活动披露。

地址：
- https://www.sygnia.co/press-release/sygnia-reveals-new-activity-by-china-nexus-threat-actor-fire-ant-targeting-trusted-infrastructure/
- X：https://x.com/RoryCrave/status/2095905092851413460

IoC：未见本帖附带完整公开哈希列表；以 Sygnia 原文为准。

### 3. Google GTIG／Unit 42／Recorded Future（AI 与威胁）

GTIG：威胁行为者使用 AI 工具；Unit 42：复杂攻击 tradecraft 压缩；Recorded Future：自动化签名／漏洞优先级（经 Aviatrix 转述）。

地址：
- https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools
- https://unit42.paloaltonetworks.com/ai-assisted-cyber-attack-inside-a-unit-42-investigation/
- https://aviatrix.ai/threat-research-center/recorded-future-automated-signature-creation-vulnerability-prioritization-2025/
- X：https://x.com/thrialectics/status/2095895307422753259 https://x.com/PaloAltoNtwks/status/2095890933485023252 https://x.com/aviatrixtrc/status/2096002200791044379

IoC：未见公开统一哈希。

### 4. 边缘设备入口／Gopher Strike 等

SentinelOne／Tenable 边缘设备利用遥测；THN 巴基斯坦关联 Gopher Strike／Sheet A（文章日期较早，今日 X 仍在传）。

地址：
- https://www.sentinelone.com/blog/what-two-independent-datasets-reveal-about-whos-exploiting-your-perimeter/
- https://thehackernews.com/2026/01/experts-detect-pakistan-linked-cyber.html
- X：https://x.com/ptdbugs/status/2095947558673621349 https://x.com/pedri77/status/2095985388414181454

IoC：未见本帖附带新哈希。

### 5. Passkey 攻击面研究／以太坊合约 C2 线索／AI agent 事故

Aviatrix 称 39 种 passkey 妥协方法；vxunderground 称恶意软件用以太坊智能合约解析 C2（无具体合约地址）；另有 AI agent 云资源误删／权限讨论。

地址：
- https://aviatrix.ai/threat-research-center/passkey-authentication-bypass-methods-2026/
- X：https://x.com/aviatrixtrc/status/2096026385571598370 https://x.com/vxunderground/status/2095970217029492982 https://x.com/rad9800/status/2095976004204535996 https://x.com/nrehiew_/status/2095964409680281695

IoC：未见公开合约地址／哈希。

### 6. 勒索／数据泄露声称（未独立核实）

窗内大量暗网监测帖（Dire Wolf／Wolfram、LockBit5、Akira、Qilin、ShinyHunters、Space Bears、DYSPH0R1A、SilentRansomGroup 等）及政府／医疗／金融数据出售声称。**一律按声称记录，非事实确认。**

示例地址：
- https://x.com/FalconFeedsio/status/2095957580585799935
- https://breachnews.com/breaches/b-stock-database-leak-claim-allegedly-exposes-42000-user-accounts/
- https://x.com/BreachNewsHQ/status/2095960786103324898

IoC：上述声称帖多数未见公开哈希；不转载凭证内容。

## 地址／IoC 汇总

- **Chromium CVE-2026-85046**：未见统一公开样本哈希；升级至 **152.0.7977.82+**；Google 确认在野利用。
- **ClickFix／Exodus RAT（Huntress）**：
  - 域名（去活化）：`granoco[.]com`
  - IP（去活化）：`85[.]239[.]149[.]120`
  - SHA256：`4e57b380eb734992865209eac4cea5d078d7b8841884c47225f20f2df7f682bf`
- **PaperCut（厂商续抄，due 09-14）**：
  - 狩猎：Application Server 上可疑后利用；`C:\ProgramData\ace.exe`；SimpleHelp 路径 `C:\ProgramData\JWrapper-Remote Access\JWAppsSharedConfig\restricted\SimpleService.exe`（服务名 “Remote Access Service”）；AnyDesk 落盘 `C:\ProgramData\AnyDesk.exe`。
  - 投放 URL（去活化）：`hxxps://sendit[.]sh/Gg7Rp/ace[.]exe`；`hxxps://download[.]anydesk[.]com/AnyDesk.exe`（后者为合法下载域被滥用场景，需结合上下文）。
  - Emergency Patch R3 示例 SHA256（Windows v26 Build 76531）：`9375a9c3cf84140a1d8e21b72d3d2c57d85d4de09ea9ae1dc021b64732427da7`（完整多版本校验和见厂商页 Checksums 节）。
- **其余条目**：未见额外可核验公开 IoC，或仅见于原文附件——写「未见公开 IoC」者以上各节为准。

## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/
- tl;dr sec 通讯：https://tldrsec.com/
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form


## 来源搜索 URL

- X Latest A（CVE/POC）：https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- X Latest B（GitHub 工具／C2）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt%20OR%20mythic)&src=typed_query&f=live
- X Latest C（malware／threat）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 09-04 警报：https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog
- Chrome Stable：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
