# X 安全情报晚报 · 2026-09-20

> 搜集窗口：圣地亚哥时间 **2026-09-19 20:00 至 2026-09-20 ~20:20**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周日）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-20.json`（collected_at **2026-09-20T20:02:30-03:00**）＋ `/workspace/tools-news-pulse-2026-09-20.json`＋ `/workspace/enrich-extra-2026-09-20.json`＋ `/workspace/enrich-2026-09-20/`。CISA KEV catalogVersion **2026.09.18**／**1716** 条／dateReleased **2026-09-18T19:00:05.0974Z**（相对昨日 **+0**，无 NEW）。
> **期限今日 09-20**：无。**新起逾期（due 曾为 09-19）**：**Pixel CVE-2026-58704**／**Cisco ISE CVE-2026-76460**（在野）／**Acronis CVE-2026-87886**。**明日 due 09-21**：Linux Kernel **CVE-2025-39682**／**CVE-2025-39964**／**CVE-2026-53266**。仍逾期示例：**Chromium V8 CVE-2026-85046**／Cisco ESA **76461**／LiteLLM **59822**／Starlette **48710**／ScreenConnect **84869**／GitLab **85706**／PaperCut **81578／82078**／MikroTik **67277／86060**／Citrix **19490**／Fortinet **25249**／Cisco FMC **20079**／Magento **75650**／N-able **86218**。
> X：`/workspace/x-posts-2026-09-20.json`（合并 **34** 条唯一：A5／B8／C10／LWiS11；**0** 跨源 ID 重叠；**34** 条均未见 prior seen_ids；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **1h**。Search B 约 **24h kept**（可见约 30h，已过滤更早）。Search C 约 **1h**。LWiS List 约 **20h**（另有 Sep 19 date-only；**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · 新起逾期 · Cisco ISE 76460 · 在野】** 联邦 due 曾为 **09-19**，今日起标逾期：**CVE-2026-76460**（ISE／ISE-PIC 特权 API 误用 → 未认证 Web 管理绕过）。Cisco PSIRT 确认 **active exploitation**；无正式 workaround。固定：**3.1P12／3.2P11／3.3P12／3.4P7／3.5P4**。防御：紧急补丁；iACL 仅临时降低暴露；狩猎 `access.log`。
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76460
  文章：https://note.com/note_suke/n/na2f35974648d?sub_rt=share_pb
  X 原帖：https://x.com/oyusuke0603/status/2101807806726955258

- **【新起逾期 · Pixel／Acronis】** **CVE-2026-58704**（Pixel Modem 不当授权／提权；补丁级别 ≥ **2026-09-05**；有限定向）／**CVE-2026-87886**（Acronis Backup 扩展默认权限；cPanel ≥1.9.3.1021／Plesk ≥1.8.11.638／DirectAdmin ≥1.2.3.238；有限定向）。
  Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
  Acronis：https://security-advisory.acronis.com/advisories/SEC-10986
  X 原帖：https://x.com/MalwareBibleJP/status/2101806364922413552

- **【X · Check Point CVE-2026-85102／85103 · CVSS 9.8】** Quantum Security Gateway／VPN；Jumbo **R81.20 Take166+／R82 Take126+／R82.10 Take44+**（另 R81.10 Take190+；Spark 另见 SK）。荷兰 NCSC 高紧迫，但 **未确认已在野**；厂商称尚无滥用迹象。
  SK85102：https://support.checkpoint.com/results/sk/sk1000117
  SK85103：https://support.checkpoint.com/results/sk/sk1000118
  NCSC：https://advisories.ncsc.nl/2026/ncsc-2026-0365.html
  X 原帖：https://x.com/ngsk_ciso/status/2101804087562170795

- **【X · IBM MCP Context Forge CVE-2026-53710】** Critical；RestrictedPython 沙箱问题；修 **≥1.0.2**；GHSA-xm98-3vcf-fph7；**非 KEV**；未见在野声明。
  GHSA：https://github.com/IBM/mcp-context-forge/security/advisories/GHSA-xm98-3vcf-fph7
  发布：https://github.com/IBM/mcp-context-forge/releases/tag/v1.0.2
  X 原帖：https://x.com/SecAlertsCo/status/2101806011036135852

- **【X · partial · CodeAstro QR Attendance CVE-2026-94048】** Medium；公开文章称 public exploit（**本报不复述步骤**）；未见官方修复版本；非 KEV。
  文章：https://www.secnews.gr/734580/codeastro-qr-code-attendance-cve-2026-94048/
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94048
  X 原帖：https://x.com/SecNews_GR/status/2101803634514178103

- **【明日 due 09-21 · Linux×3】** **CVE-2025-39682**／**CVE-2025-39964**／**CVE-2026-53266** 仍在 KEV；本地 `knownRansomwareCampaignUse=Unknown`。
  CISA +2：https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-two-known-exploited-vulnerabilities-catalog
  CISA +1：https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-one-known-exploited-vulnerability-catalog

- **【仍逾期 · Chromium 85046 等】** **CVE-2026-85046**（V8 类型混淆，在野）及 Cisco ESA／LiteLLM／Starlette 等仍逾期（见头注）。
  厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html

- **【威胁 · 地下声称 · 均未验证】** RedClinica 智利 120GB 患者库声称（undercode／DailyDarkWeb／Splint3r7／VECERTRadar）；厄瓜多尔医疗 6.68M／阿尔及利亚国防约 36k／阿根廷 TRANSENER 高压图纸（UNCONFIRMED）；Crypto RAT ~$235k（无变种）；DBHunter 多目标。LWiS：ShinyHunters／Clop、Docker escape Accomplish、TraderTraitor SentinelOne。
  RedClinica 文章：https://undercodenews.com/dark-web-alert-threat-actor-claims-120gb-redclinica-patient-database-leak-in-chile-video/
  ShinyHunters：https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/

- **【工具 · 核心无升版 · X／LWiS 交叉】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 均无升版。Risky 仍 **RBNEWS612**／**SRB183**；tl;dr 仍 **#346**。BotC2 RAT 研究报告、CnaEmulator、OneDrive-UDC2、nuclei-templates PR#17240、DeepTeam、mubix ai-ctf／IOXIDResolver、stratomarco ai-training-ml-security。
  BotC2：https://github.com/ShadowOpCode/BotC2-RAT/blob/main/BotC2_RAT.pdf
  CnaEmulator：https://github.com/iterat0r/CnaEmulator
  OneDrive-UDC2：https://github.com/nmht3t/OneDrive-UDC2

## CVE / POC / 漏洞

### 1. 【新起逾期 · 在野】Cisco ISE／ISE-PIC CVE-2026-76460

CISA due 曾为 **2026-09-19**，今日起标逾期（added 2026-09-16）。特权 API 误用 → 未认证可绕过 Web 管理；Cisco 确认 **active exploitation**。无正式 workaround。固定版本：**3.1 Patch 12／3.2 Patch 11／3.3 Patch 12／3.4 Patch 7／3.5 Patch 4**（ISE 3.0 需迁移）。防御：紧急升级；临时 iACL 限制管理面；狩猎异常 `access.log` 与外联；遵循 **BOD 26-04**。X 日文分析交叉（oyusuke0603／note.com）。**本报不转载利用细节。**

地址：
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76460
- CISA 入目警报（09-16）：https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 文章：https://note.com/note_suke/n/na2f35974648d?sub_rt=share_pb
- X 原帖：https://x.com/oyusuke0603/status/2101807806726955258

IoC：未见公开 IoC。

### 2. 【新起逾期】Google Pixel CVE-2026-58704

KEV due 曾为 **2026-09-19**，今日起标逾期。蜂窝 Modem 不当授权／权限绕过 → 邻接提权；Google 称可能有限定向在野。防御：安装 Pixel **2026-09** 更新，安全补丁级别 ≥ **2026-09-05**。

地址：
- 厂商：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-58704
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC。

### 3. 【新起逾期】Acronis Backup 扩展 CVE-2026-87886（SEC-10986）

KEV due 曾为 **2026-09-19**，今日起标逾期。cPanel／WHM／Plesk／DirectAdmin 备份扩展默认权限不当 → 本地提权；厂商称有限定向在野。防御：cPanel 插件 ≥**1.9.3.1021**；Plesk ≥**1.8.11.638**；DirectAdmin ≥**1.2.3.238**；排查受影响托管主机。

地址：
- 厂商：https://security-advisory.acronis.com/advisories/SEC-10986
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87886
- X 原帖：https://x.com/MalwareBibleJP/status/2101806364922413552

IoC：未见公开 IoC。

### 4. 【X · 非 KEV】Check Point Quantum CVE-2026-85102／CVE-2026-85103（CVSS 9.8）

厂商 SK1000117／SK1000118 与荷兰 NCSC-2026-0365 确认两条 Critical（CVSS 9.8）。Jumbo 修复基线：**R81.20 Take 166+**／**R82 Take 126+**／**R82.10 Take 44+**／**R81.10 Take 190+**；Spark：**R82.00.10 Build 2325+**／**R81.10.17 Build 4968+**；**R82.20 不受影响**。LivePatch：SK1000117 列 Take 26（85102 特定离线情形）；SK1000118 列 Take 24（85103）。NVD SSVC exploitation=none；NCSC 评估近期大规模利用概率高，但 **未称已确认在野**；厂商称尚无滥用迹象。防御：按分支立即升级；无法立即升级时仅按官方临时缓解收紧 VPN 访问并尽快升级；**85103 含 Security Management Server**。

地址：
- 厂商 SK85102：https://support.checkpoint.com/results/sk/sk1000117
- 厂商 SK85103：https://support.checkpoint.com/results/sk/sk1000118
- NVD 85102：https://nvd.nist.gov/vuln/detail/CVE-2026-85102
- NVD 85103：https://nvd.nist.gov/vuln/detail/CVE-2026-85103
- NCSC advisory：https://advisories.ncsc.nl/2026/ncsc-2026-0365.html
- NCSC 警报：https://www.ncsc.nl/alerts/kritieke-kwetsbaarheden-in-check-point-vpn-producten-met-actief-misbruik-verwacht-update-nu
- X 原帖：https://x.com/ngsk_ciso/status/2101804087562170795

IoC：未见公开 IoC。

### 5. 【X · 非 KEV】IBM MCP Context Forge CVE-2026-53710

IBM GitHub advisory **GHSA-xm98-3vcf-fph7**／NVD／CVE.org 确认 Critical。受影响：`mcp-contextforge-gateway <= 1.0.1`；修复：**≥1.0.2**。未列入本地 KEV；NVD SSVC exploitation=none；未见厂商称已在野。防御：核对是否部署 `python_sandbox_server`；升级至 1.0.2+；复核 HTTP／SSE 暴露、认证与最小权限。

地址：
- GHSA：https://github.com/IBM/mcp-context-forge/security/advisories/GHSA-xm98-3vcf-fph7
- 修复发布：https://github.com/IBM/mcp-context-forge/releases/tag/v1.0.2
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-53710
- 文章（聚合）：https://secalerts.co/vulnerability/CVE-2026-53710
- X 原帖：https://x.com/SecAlertsCo/status/2101806011036135852

IoC：未见公开 IoC。

### 6. 【X · partial】CodeAstro QR Code Attendance CVE-2026-94048

CVE.org（VulDB CNA）与 NVD 有正式记录；受影响版本 **1.0**；严重度 Medium（NVD v3.1；v4 口径或为 Low）。公开文章／CVE 描述称存在 public exploit——**本报不复述任何利用内容**。未见 CodeAstro 官方修复公告或修复版本；非 KEV；不能将 public exploit 说法升级为已确认在野。防御：盘点并升级／替换 1.0；无厂商修复前避免管理面公网暴露；访问控制、日志审查与隔离。

地址：
- 文章：https://www.secnews.gr/734580/codeastro-qr-code-attendance-cve-2026-94048/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94048
- 厂商站点（无 CVE 修复公告）：https://codeastro.com/
- X 原帖：https://x.com/SecNews_GR/status/2101803634514178103

IoC：未见公开 IoC。

### 7. 【明日 due 09-21】Linux Kernel CVE-2025-39682／CVE-2025-39964／CVE-2026-53266

昨日入 KEV；联邦 due **2026-09-21**。本日 catalog **无新增**。本地 KEV 对勒索软件使用均为 **Unknown**。防御：按发行版内核更新；BOD 26-04 triage；盘点高暴露 Linux 宿主／容器。

地址：
- CISA +2：https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA +1：https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-one-known-exploited-vulnerability-catalog
- NVD 39682：https://nvd.nist.gov/vuln/detail/CVE-2025-39682
- NVD 39964：https://nvd.nist.gov/vuln/detail/CVE-2025-39964
- NVD 53266：https://nvd.nist.gov/vuln/detail/CVE-2026-53266
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 8. 【仍逾期】Chromium V8 CVE-2026-85046 及其他

联邦 due 曾为 **2026-09-18**，仍逾期。V8 类型混淆 → 沙箱内 RCE；Google 称 **exploitation in the wild**。修复示例：**152.0.7977.82/.83**。另仍逾期：Cisco ESA **CVE-2026-76461**、LiteLLM **59822**、Starlette **48710**、ScreenConnect **84869**、GitLab **85706**、PaperCut **81578／82078**、MikroTik **67277／86060**、Citrix **19490**、Fortinet **25249**、Cisco FMC **20079**、Magento **75650**、N-able **86218** 等（见公开备援）。

地址：
- Chromium 厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- NVD 85046：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
- Cisco ESA：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX
- NVD 76461：https://nvd.nist.gov/vuln/detail/CVE-2026-76461
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 1. 核心工具版本 pulse（无升版）

Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 相对昨日均无变化。Risky Business 仍 **RBNEWS612**／**SRB183**（613／184=404）；tl;dr sec 仍 **#346**（#347 未确认新刊）。

地址：
- Sliver：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- nuclei：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- RBNEWS612：https://risky.biz/RBNEWS612/
- SRB183：https://risky.biz/SRB183/
- tl;dr #346：https://tldrsec.com/p/tldr-sec-346

IoC：未见公开 IoC。

### 2. 【X】BotC2 RAT 逆向研究报告

@ShadowOpCode：BotC2 RAT 原生 x64 逆向／C2 仿真研究 PDF（防御研究语境）。防御：对照报告中的行为特征完善 EDR／网络狩猎；勿将研究仿真器部署到生产。

地址：
- 仓库／报告：https://github.com/ShadowOpCode/BotC2-RAT/blob/main/BotC2_RAT.pdf
- X 原帖：https://x.com/ShadowOpCode/status/2101786509653254376

IoC：未见公开 IoC。

### 3. 【X】CnaEmulator（Cobalt Strike Aggressor 仿真）

@Dinosn／@ipurple：iterat0r/CnaEmulator — 独立的 `.cna` 开发／仿真／测试 harness。防御：限制未授权渗透工具安装；审计工程机上的 CNA／Beacon 相关工件。

地址：
- 仓库：https://github.com/iterat0r/CnaEmulator
- X 原帖：https://x.com/Dinosn/status/2101725772461359372
- X 原帖：https://x.com/ipurple/status/2101716549572645020

IoC：未见公开 IoC。

### 4. 【X】OneDrive-UDC2（Cobalt Strike 用户自定义 C2）

@Dinosn／@ipurple：nmht3t/OneDrive-UDC2 — 以 OneDrive 为传输层的 CS UDC2。防御：监控异常 Graph／OneDrive API 轮询与非交互上传；审计 Entra 应用权限与非常规出站。

地址：
- 仓库：https://github.com/nmht3t/OneDrive-UDC2
- X 原帖：https://x.com/Dinosn/status/2101598125785833743
- X 原帖：https://x.com/ipurple/status/2101557103324176807

IoC：未见公开 IoC。

### 5. 【X】nuclei-templates matcher 修复（CVE-2026-31807）

@shaivarth：projectdiscovery/nuclei-templates **PR #17240** — 修正 CVE-2026-31807 模板 matcher，降低误报。防御：更新 nuclei-templates 至含该修复的版本／跟踪 PR 合并状态。

地址：
- PR：https://github.com/projectdiscovery/nuclei-templates/pull/17240
- X 原帖：https://x.com/shaivarth/status/2101604871736795360

IoC：未见公开 IoC。

### 6. 【X】DeepTeam（LLM／Agent 红队框架）

@shushant_l 合辑含 confident-ai/deepteam（LLM／AI agent 红队）。防御：仅在授权评测环境使用；对生产 LLM 端点做访问控制与异常提示注入监测。

地址：
- 仓库：https://github.com/confident-ai/deepteam
- X 原帖：https://x.com/shushant_l/status/2101628457180692968

IoC：未见公开 IoC。

### 7. 【LWiS】mubix ai-ctf／IOXIDResolver；stratomarco AI 训练仓

@mubix：更新 **ai-ctf**（prompt injection 教学，答案在仓内）与 **IOXIDResolver**。@stratomarco（经 @mubix 转）：ai-training-ml-security。防御：安全培训用途；对照 AI 应用威胁模型做内部演练。

地址：
- ai-ctf：https://github.com/mubix/ai-ctf
- IOXIDResolver：https://github.com/mubix/IOXIDResolver
- ai-training-ml-security：https://github.com/stratomarco/ai-training-ml-security
- X 原帖：https://x.com/mubix/status/2101788742193147930
- X 原帖：https://x.com/mubix/status/2101787732263538874
- X 原帖：https://x.com/stratomarco/status/2101809592757883000

IoC：未见公开 IoC。

### 8. 【可选 · 较低优先级】Red-Team-Roadmap

@httpschuks：Dev-Chukwuma/Red-Team-Roadmap（自学／实验语境，OpenSSH 版本与 CVE 对照叙事）。

地址：
- 仓库：https://github.com/Dev-Chukwuma/Red-Team-Roadmap
- X 原帖：https://x.com/httpschuks/status/2101597110474813464

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. 【X · 未验证】RedClinica（智利）120GB 患者数据库声称

多源交叉（@undercode_news／@DailyDarkWeb／@Splint3r7／@VECERTRadar）称威胁行为者声称泄露 RedClinica 约 **120GB** 患者数据。VECERTRadar 明确标 **UNCONFIRMED**；undercode 帖带事实核查投票。**均未独立核实。**

地址：
- 文章：https://undercodenews.com/dark-web-alert-threat-actor-claims-120gb-redclinica-patient-database-leak-in-chile-video/
- X 原帖：https://x.com/undercode_news/status/2101809845590454767
- X 原帖：https://x.com/DailyDarkWeb/status/2101804464478822860
- X 原帖：https://x.com/Splint3r7/status/2101789247674147085
- X 原帖：https://x.com/VECERTRadar/status/2101785749477576727

IoC：未见公开 IoC。

### 2. 【X · 未验证】厄瓜多尔医疗／阿尔及利亚国防／阿根廷 TRANSENER

- @Splint3r7：厄瓜多尔公共卫生系统声称约 **6.68M** 患者记录。
- @Splint3r7：阿尔及利亚国防（DCSA）约 **36,000** 军官记录声称。
- @VECERTRadar：阿根廷 **TRANSENER** 高压／技术图纸出售声称 — 明确 **UNCONFIRMED**。

地址：
- 厄瓜多尔声称：https://x.com/Splint3r7/status/2101798985145225702
- 阿尔及利亚声称：https://x.com/Splint3r7/status/2101794158080032959
- TRANSENER 预警：https://x.com/VECERTRadar/status/2101787150882664869

IoC：未见公开 IoC。

### 3. 【X · 未验证】Crypto RAT 约 $235k 声称

@coinbureau／@GWNavigator：远程访问木马劫持加密货币会话，声称约 **$235,000**／数百受害者；**无变种名、无样本哈希**。视为未核实线索。

地址：
- X 原帖：https://x.com/coinbureau/status/2101771234879123651
- X 引用评述：https://x.com/GWNavigator/status/2101803893373993388

IoC：未见公开 IoC（无变种／样本）。

### 4. 【X · 未验证】DBHunter 多目标数据库声称

@intels_daily：威胁行为者 **DBHunter** 声称关联多目标库（含 Prince of Songkla University、Delacombe Primary School、Saint Lucia Inland Revenue 等叙事）。**未独立核实。**

地址：
- X 原帖：https://x.com/intels_daily/status/2101795315774857445

IoC：未见公开 IoC。

### 5. 【LWiS】新闻合辑 · ShinyHunters／Clop、Docker escape、TraderTraitor

@ntlmrelay（Sep 19 网络分享 Top）：BleepingComputer 称 **ShinyHunters** 入侵 Clop 泄露站并威胁勒索该团伙；Accomplish **Docker 逃逸** 文；SentinelOne **TraderTraitor** API 后门复现分析。属公开报道交叉，非本报独立确认战役归因。

地址：
- ShinyHunters／Clop：https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/
- Docker escape：https://www.accomplish.ai/blog/escaping-dockers-hypervisor/
- TraderTraitor：https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/#cq=i1
- X 原帖：https://x.com/ntlmrelay/status/2101627580184993856

IoC：未见本报可抄录公开 IoC（详见各原文）。

### 6. 【LWiS】OpenAI 披露／负责任披露辩论

@S1r1u5_／@TalBeerySec／@LiveOverflow（@evilsocket 转）：围绕 OpenAI 披露边界、CFAA／RD vs 横向移动、VDP 流程拥堵的讨论。**无 IoC、无利用步骤。**

地址：
- https://x.com/S1r1u5_/status/2101779800096645593
- https://x.com/S1r1u5_/status/2101769672333066673
- https://x.com/S1r1u5_/status/2101619967913521431
- https://x.com/TalBeerySec/status/2101560506242761097
- https://x.com/LiveOverflow/status/2101252729326739932

IoC：未见公开 IoC。

### 7. ICS

本日窗口 **无 2026-09-20 新 ICS advisory 显著条目**（公开备援未检出当日新刊）。TRANSENER 高压图纸仅为地下论坛 **UNCONFIRMED** 声称（见上）。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **新起逾期 KEV 主条（ISE 76460／Pixel 58704／Acronis 87886）及明日 due Linux×3／仍逾期 Chromium 85046 等**：未见可抄录公开 IoC IP／样本哈希列表。
- **Check Point 85102／85103／IBM 53710／CodeAstro 94048**：未见公开 IoC。
- **地下声称（RedClinica／厄瓜多尔／阿尔及利亚／TRANSENER／DBHunter／Crypto RAT）**：未见可核验公开 IoC；一律视为未验证。
- **工具仓（BotC2／CnaEmulator／OneDrive-UDC2／DeepTeam／ai-ctf／IOXIDResolver 等）**：仓库 URL 见上；无攻击 IoC。
- **其余条目**：未见公开 IoC。

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

- X Latest A（CVE／POC／exploit／0day／vulnerability）：https://x.com/search?q=(CVE%20OR%20POC%20OR%20exploit%20OR%200day%20OR%20%220-day%22%20OR%20vulnerability)%20-filter%3Areplies&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／havoc／cobalt／implant）：https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20redteam%20OR%20nuclei%20OR%20sliver%20OR%20havoc%20OR%20cobalt%20OR%20%22command%20and%20control%22%20OR%20implant)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor／ransomware／threat intel）：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20OR%20ransomware%20OR%20%22threat%20intel%22)%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
