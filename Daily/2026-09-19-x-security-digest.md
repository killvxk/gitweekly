# X 安全情报晚报 · 2026-09-19

> 搜集窗口：圣地亚哥时间 **2026-09-18 20:00 至 2026-09-19 ~20:20**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周六）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-19.json`（collected_at **2026-09-19T20:09:36-03:00**）＋ `/workspace/tools-news-pulse-2026-09-19.json`＋ `/workspace/enrich-extra-2026-09-19.json`＋ `/workspace/enrich-2026-09-19/`。CISA KEV catalogVersion **2026.09.18**／**1716** 条／dateReleased **2026-09-18T19:00:05.0974Z**（相对昨日 **+0**，无 NEW）。
> **期限今日 09-19**：**Pixel CVE-2026-58704**／**Cisco ISE CVE-2026-76460**（在野）／**Acronis CVE-2026-87886**。**新起逾期（due 曾为 09-18）**：**Chromium V8 CVE-2026-85046**（在野）。**明日 due**：无。仍 due **09-21**：Linux Kernel **CVE-2025-39964**／**CVE-2026-53266**／**CVE-2025-39682**。仍逾期：Cisco ESA **76461**／LiteLLM **59822**／Starlette **48710**／ScreenConnect **84869**／GitLab **85706**／PaperCut **81578／82078**／MikroTik **67277／86060**／Citrix **19490**／Fortinet **25249**／Cisco FMC **20079**／Magento **75650**／N-able **86218**。
> X：`/workspace/x-posts-2026-09-19.json`（合并 **18** 条唯一：A6／B2／C3／LWiS7；**0** 跨源 ID 重叠；**18** 条均未见 prior seen_ids；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **1h**。Search B 约 **6h**。Search C 约 **1h**。LWiS List 约 **22h**（另有 Sep 18 date-only；**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · 今日 due · Cisco ISE 76460 · 在野】** 联邦 due **今日 09-19**：**CVE-2026-76460**（ISE／ISE-PIC 特权 API 误用 → 未认证 Web 管理绕过，可至 root）。Cisco PSIRT 确认 **active exploitation**；无正式 workaround。固定：**3.1P12／3.2P11／3.3P12／3.4P7／3.5P4**。防御：紧急补丁；iACL 限制管理面；狩猎 `ise-kong/access.log`。
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76460
  X 原帖：https://x.com/techhelpcanada/status/2101438071874974001

- **【今日 due · Pixel／Acronis】** **CVE-2026-58704**（Pixel Modem 不当授权／提权；补丁级别 ≥ **2026-09-05**；有限在野）／**CVE-2026-87886**（Acronis Backup 扩展默认权限；cPanel ≥1.9.3.1021／Plesk ≥1.8.11.638／DirectAdmin ≥1.2.3.238）。
  Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
  Acronis：https://security-advisory.acronis.com/advisories/SEC-10986

- **【新起逾期 · Chromium V8 85046 · 在野】** due 曾为 **09-18**，今日起标逾期。V8 类型混淆 → 沙箱内 RCE；稳定通道 **152.0.7977.82/.83**。
  厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85046

- **【X · Azure AI Foundry CVE-2026-85889 · CVSS 10】** 缺少认证 → 提权；**MSRC 已在服务侧缓解**，客户无需本地补丁；未见在野。
  MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85889
  文章：https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html
  原帖：https://x.com/aruntikaram/status/2101439343998968180

- **【X · SolarWinds ARM CVE-2026-28326】** 硬编码密钥 → 未认证 RCE（邻接）；修 **ARM 2026.2.1+**；未见公开在野声明。
  厂商：https://www.solarwinds.com/trust-center/security-advisories/CVE-2026-28326
  文章：https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html
  原帖：https://x.com/connect24h/status/2101437358017220723

- **【X · Docker Sandboxes CVE-2026-77179】** macOS virtio-fs 符号链接 → 主机 FS 逃逸；修 **Sandboxes ≥0.42.0**；GHSA 已核实（非仅传言）。
  GHSA：https://github.com/advisories/GHSA-4x2g-7mfh-8rx6
  发布：https://github.com/docker/sbx-releases/releases/tag/v0.42.0
  原帖：https://x.com/_MrNiko/status/2101442475747684424

- **【X · Plugin4Shell 续】** Automater 舰队盘点文；地板仍 **Claude Code ≥2.1.179／Codex ≥0.146.0**。
  主披露：https://www.air.security/blog-posts/plugin4shell
  Automater：https://automater.ai/intel/plugin4shell-pin-verify-fleet-patch/
  原帖：https://x.com/automater_ai/status/2101444615131836578

- **【威胁 · 勒索／地下声称】** ThreatMon：**unsafe** → **voltgames.io**；DailyDarkWeb：德国托管面板拍卖（~2600 用户）／多国电信基础设施泄露——**均未验证**。
  voltgames 声明帖：https://x.com/TMRansomMon/status/2101444234897141801
  电信声称：https://x.com/DailyDarkWeb/status/2101434424466493779

- **【工具 · 核心无升版 · X 交叉】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 均无升版。Risky 仍 **RBNEWS612**／**SRB183**；tl;dr 仍 **#346**。X／LWiS：Mythic Teams C2 profile、NullAI HexStrike、ntlmscout、KernelSight、AD Attack Map；ACLPWN BOF（X 宣称、未见公开仓库）。
  msteams：https://github.com/Whispergate/msteams
  ntlmscout：https://github.com/boydhacks/ntlmscout
  KernelSight：https://github.com/splintersfury/KernelSight

## CVE / POC / 漏洞

### 1. 【今日 due · 在野】Cisco ISE／ISE-PIC CVE-2026-76460

CISA due **2026-09-19**（added 2026-09-16）。特权 API 误用 → 未认证可绕过 Web 管理；Cisco 确认 **active exploitation**。无正式 workaround。固定版本：**3.1 Patch 12／3.2 Patch 11／3.3 Patch 12／3.4 Patch 7／3.5 Patch 4**（ISE 3.0 需迁移）。防御：紧急升级；临时 iACL 限制管理面；狩猎 `ise-kong/access.log` 与外联异常；遵循 **BOD 26-04**。X 多帖交叉（techhelpcanada／QubbleOfficial）。**本报不转载利用细节。**

地址：
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76460
- CISA 入目警报（09-16）：https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 文章：https://techhelp.ca/cisco-ise-cvss-10-zero-day-active-exploitation/?utm_source=twitter&utm_medium=social&utm_campaign=SocialWarfare
- X 原帖：https://x.com/techhelpcanada/status/2101438071874974001
- X 原帖：https://x.com/QubbleOfficial/status/2101437521372606635

IoC：未见公开 IoC。

### 2. 【今日 due】Google Pixel CVE-2026-58704

KEV due **2026-09-19**。蜂窝 Modem 不当授权／权限绕过 → 邻接提权；Google 称有限定向在野。防御：安装 Pixel **2026-09** 更新，安全补丁级别 ≥ **2026-09-05**。

地址：
- 厂商：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-58704
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC。

### 3. 【今日 due】Acronis Backup 扩展 CVE-2026-87886

KEV due **2026-09-19**（SEC-10986）。cPanel／WHM／Plesk／DirectAdmin 备份扩展默认权限不当 → 本地提权；厂商称有限在野。防御：cPanel 插件 ≥**1.9.3.1021**；Plesk ≥**1.8.11.638**；DirectAdmin ≥**1.2.3.238**；排查受影响托管主机。

地址：
- 厂商：https://security-advisory.acronis.com/advisories/SEC-10986
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87886

IoC：未见公开 IoC。

### 4. 【新起逾期 · 在野】Chromium V8 CVE-2026-85046

联邦 due 曾为 **2026-09-18**，今日起标逾期。V8 类型混淆 → 沙箱内 RCE；Google 称 **exploitation in the wild**。修复：**152.0.7977.82/.83**（Win／Mac）／**152.0.7977.82**（Linux）。防御：全舰队验证 Chrome／Edge／Chromium 浏览器版本并强制重启。

地址：
- 厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC。

### 5. 【X · 非 KEV】Azure AI Foundry CVE-2026-85889（CVSS 10）

关键关键函数缺少认证（CWE-306）→ 提权。MSRC／THN：厂商已在**服务侧缓解**，客户无需安装补丁或改配置；未见在野。防御：审计 Foundry／AI 应用身份与异常 API／角色提升遥测。

地址：
- MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85889
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-85889
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85889
- 文章：https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html
- X 原帖：https://x.com/aruntikaram/status/2101439343998968180

IoC：未见公开 IoC。

### 6. 【X · 非 KEV】SolarWinds ARM CVE-2026-28326

硬编码静态密钥（CWE-321）→ 未认证 RCE；影响 ARM **2026.2 及更早**；CVSS 8.8（邻接）。修复：**ARM 2026.2.1+**（厂商公告约 09-17）。防御：升级；限制 ARM 管理面可达性；按 hardening 指南加固。

地址：
- 厂商：https://www.solarwinds.com/trust-center/security-advisories/CVE-2026-28326
- 发行说明：https://documentation.solarwinds.com/en/success_center/arm/content/release_notes/arm_2026-2-1_release_notes.htm
- 加固：https://documentation.solarwinds.com/en/success_center/arm/content/secure-your-arm-deployment.htm
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-28326
- 文章：https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html
- X 原帖：https://x.com/connect24h/status/2101437358017220723

IoC：未见公开 IoC。

### 7. 【X · 非 KEV】Docker Sandboxes CVE-2026-77179（GHSA-4x2g-7mfh-8rx6）

macOS virtio-fs 主机服务对已 unlink 路径不当跟随符号链接 → guest 可读写共享区外主机文件（VMM 用户权限）。影响 Sandboxes **0.28.0–<0.42.0**；修复 **≥0.42.0**。防御：升级；临时 clone 模式并避免额外主机挂载；审计沙箱 Agent 对主机路径的异常访问。**已核实 GHSA／NVD，非仅 X 传言。**

地址：
- GHSA：https://github.com/advisories/GHSA-4x2g-7mfh-8rx6
- 修复发布：https://github.com/docker/sbx-releases/releases/tag/v0.42.0
- Docker 文档：https://docs.docker.com/ai/sandboxes/
- 隔离说明：https://docs.docker.com/ai/sandboxes/security/isolation/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-77179
- 文章：https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html
- 文章：https://accomplish.ai/blog/escaping-dockers-hypervisor/
- X 原帖：https://x.com/_MrNiko/status/2101442475747684424

IoC：未见公开 IoC。

### 8. 【续 · due 09-21】Linux Kernel CVE-2025-39964／CVE-2026-53266／CVE-2025-39682

昨日 KEV +3；联邦 due **2026-09-21**。本日 catalog **无新增**。防御：按发行版内核更新；BOD 26-04 triage。

地址：
- CISA +2：https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA +1：https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-one-known-exploited-vulnerability-catalog
- NVD 39964：https://nvd.nist.gov/vuln/detail/CVE-2025-39964
- NVD 53266：https://nvd.nist.gov/vuln/detail/CVE-2026-53266
- NVD 39682：https://nvd.nist.gov/vuln/detail/CVE-2025-39682
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 9. 【仍逾期】Cisco ESA CVE-2026-76461 及其他

Cisco Secure Email Gateway 未认证 SQLi → OS root；due 曾为 09-17。修复示例：**15.5.5-014／16.0.4-302／16.5.0-780**。另仍逾期 LiteLLM／Starlette 等（见头注）。

地址：
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76461

IoC：未见公开 IoC。

### 10. 【X · 供应链续】Plugin4Shell

Air Security 披露 AI coding 插件 SHA-pin 未校验 HEAD；Automater（今日）强调舰队盘点与 post-checkout HEAD 断言。地板：**Claude Code ≥2.1.179**／**Codex ≥0.146.0**；Copilot／Gemini 风险面见原文。无 CVE。

地址：
- 主披露：https://www.air.security/blog-posts/plugin4shell
- Automater：https://automater.ai/intel/plugin4shell-pin-verify-fleet-patch/
- THN：https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html
- The Register：https://www.theregister.com/security/2026/09/17/ai_coding_agents_0_click_rce_flaw_could_hand_attackers_keys_to_the_kingdom/5297335
- Claude Code：https://github.com/anthropics/claude-code
- Codex：https://github.com/openai/codex
- X 原帖：https://x.com/automater_ai/status/2101444615131836578

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 1. 核心工具版本 pulse（无升版）

Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 相对昨日均无变化。Risky Business 仍 **RBNEWS612**／**SRB183**（613／184=404）；tl;dr sec 仍 **#346**（#347=404）。

地址：
- Sliver：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- nuclei：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- RBNEWS612：https://risky.biz/RBNEWS612/
- SRB183：https://risky.biz/SRB183/
- tl;dr #346：https://tldrsec.com/p/tldr-sec-346

IoC：未见公开 IoC。

### 2. 【X】Mythic C2 · Microsoft Teams／Graph profile

@r1cksec：Whispergate/msteams — 经 Graph API 与 Teams 频道通信的 Mythic C2 Profile。防御：监控异常 Entra 应用对 Graph／Teams 频道的高频读写；审计 bot／应用权限；告警非常规 Teams 出站与短间隔轮询。

地址：
- 仓库：https://github.com/Whispergate/msteams
- X 原帖：https://x.com/r1cksec/status/2101357404239667692

IoC：未见公开 IoC。

### 3. 【X】NullAI HexStrike AI Terminal

@NealFrazierTech：NullAITech/NullAI-HexStrike-AI-Terminal（AI 红队工作站叙事）。防御：EDR／资产基线；限制未授权渗透工具安装。

地址：
- 仓库：https://github.com/NullAITech/NullAI-HexStrike-AI-Terminal
- X 原帖：https://x.com/NealFrazierTech/status/2101403657103094119

IoC：未见公开 IoC。

### 4. 【LWiS】ntlmscout

@ipurple：boydhacks/ntlmscout — 未认证 NTLM Type-1／Type-2 侦察（NetBIOS／DNS／森林／OS build 等）。防御：收敛对外 NTLM；强制 SMB／LDAP 签名与 EPA；监控异常协商洪泛。

地址：
- 仓库：https://github.com/boydhacks/ntlmscout
- X 原帖：https://x.com/ipurple/status/2101299241993855064

IoC：未见公开 IoC。

### 5. 【LWiS】KernelSight

@5mukx：Windows 内核驱动漏洞知识库（约 156–157 案例／64 驱动）。防御：对照 LOLDrivers／厂商补丁盘点脆弱驱动；强化 HVCI／驱动阻止列表。

地址：
- 仓库：https://github.com/splintersfury/KernelSight
- 站点：https://splintersfury.github.io/KernelSight/
- LOLDrivers：https://www.loldrivers.io/
- X 原帖：https://x.com/5mukx/status/2101192645309501511

IoC：未见公开 IoC。

### 6. 【LWiS · 时间不确定】AD Attack Architecture Map／ACLPWN BOF

- @xxByte：AD 攻击架构参考图（含蓝队 Event ID／加固清单）— date-only Sep 18。
- @init1security：宣称 ACLPWN BOF（训练报名叙事）— **未见可验证公开 GitHub**；相关但不同：fox-it/aclpwn.py、0xM4L/acl-abuse-havoc。

地址：
- AD Map：https://kypvas.github.io/ad_attack_architecture/
- AD Map 原帖：https://x.com/xxByte/status/2100913237885636617
- ACLPWN 原帖：https://x.com/init1security/status/2100996188795461785
- 相关非同：https://github.com/fox-it/aclpwn.py
- 相关非同：https://github.com/0xM4L/acl-abuse-havoc

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. 【X】ThreatMon · unsafe 勒索声称 voltgames.io

@TMRansomMon：团伙 **unsafe** 将 **voltgames.io** 列为受害者（时间戳叙事 2026-09-20 UTC+3）。视为监控声明，非独立确认。

地址：
- X 原帖：https://x.com/TMRansomMon/status/2101444234897141801
- 声称相关域名：https://voltgames.io/

IoC：域名 `voltgames.io`（来自帖文／卡片；**未独立核实为被攻陷确认**）。

### 2. 【X】DailyDarkWeb · 未验证地下声称

- 德国托管管理面板访问权拍卖声称（约 2600 用户／phpMyAdmin）— 帖文自标未验证。
- 多国电信基础设施泄露声称（TV Zamora／TELGUA／Liberty／Fiber X／TELMEX／FIBERTEL 等）— 帖文自标未验证。

地址：
- 德国托管声称：https://x.com/DailyDarkWeb/status/2101434530288799768
- 电信声称：https://x.com/DailyDarkWeb/status/2101434424466493779

IoC：未见可核验公开 IoC（仅叙事）。

### 3. 【LWiS】披露争议／恶意软件视频语境

@gergely_kalman／@jachiam0：围绕 Hacktron／OpenAI CISO 披露争议讨论（关联昨报 libheif／Discourse 语境）。@vxunderground：恶意软件分析视频筹备（内存二阶段讨论；无步骤）。

地址：
- https://x.com/gergely_kalman/status/2101398681198948843
- https://x.com/jachiam0/status/2101366246440931521
- https://x.com/vxunderground/status/2101404667213234643
- 昨报相关研究员文：https://www.hacktron.ai/blog/hacking-openai

IoC：未见公开 IoC。

### 4. ICS

本日窗口 **无 2026-09-19 新 ICS advisory 显著条目**（公开备援未检出当日新刊）。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **今日 KEV 主条（ISE 76460／Pixel 58704／Acronis 87886／Chromium 85046 新逾期／Linux×3 仍 due 09-21）**：未见可抄录公开 IoC IP／样本哈希列表。
- **Azure 85889／SolarWinds 28326／Docker 77179／Plugin4Shell**：未见公开 IoC。
- **ThreatMon unsafe／voltgames.io**：帖文域名 `voltgames.io`（声称级，未独立确认）。
- **DailyDarkWeb 地下声称**：未见可核验公开 IoC。
- **工具仓（msteams／HexStrike／ntlmscout／KernelSight）**：仓库 URL 见上；无攻击 IoC。
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
