# X 安全情报晚报 · 2026-09-17

> 搜集窗口：圣地亚哥时间 **2026-09-16 20:00 至 2026-09-17 ~20:30**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周四）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-17.json`（collected_at **2026-09-17T20:16:20-03:00**）＋ `/workspace/tools-news-pulse-2026-09-17.json`＋ `/workspace/enrich-extra-2026-09-17.json`＋ `/workspace/enrich-2026-09-17/`。CISA KEV catalogVersion **2026.09.16**／**1713** 条／dateReleased **2026-09-16T18:47:50.6796Z**（相对昨日 **+0**，无新入库）。
> **期限今日 09-17**：**Cisco ESA CVE-2026-76461**。**新起逾期（due 曾为 09-16）**：**LiteLLM CVE-2026-59822**／**Starlette CVE-2026-48710**。**期限明日 09-18**：**Chromium V8 CVE-2026-85046**（在野利用）。**昨日 NEW 仍开放（due 09-19）**：**Pixel CVE-2026-58704**／**Cisco ISE CVE-2026-76460**／**Acronis CVE-2026-87886**。仍逾期：ScreenConnect **84869**／GitLab **85706**／PaperCut **81578／82078**／MikroTik **67277／86060**／Citrix **19490**／Fortinet **25249**／Cisco FMC **20079**／Magento **75650**／N-able **86218**。
> **NEW ICS**：ICSA-26-260-**01..07**（Bransys ELD／Mitsubishi GX Works3／Hitachi Energy FCP／Schneider Modicon M340／NetBotz／ABB Edgenius／PowerChute）＋ **ICSA-26-211-07 Update A**（Mitsubishi CC-Link IE TSN）。
> X：`/workspace/x-posts-2026-09-17.json`（合并 **36** 条唯一：A5／B13／C9／LWiS9；**0** 跨源重叠；其中 B 约 **4** 条已见于 prior seen_ids，仍记高信号但标「先前已见」；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.12h**。Search B 约 **33.22h**。Search C 约 **1.19h**。LWiS List 保留约 **31.5h**／扫描约 **32.3h**（**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。本轮 **未再浏览 X**（沿用已落盘采集）。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · 今日 due · Cisco ESA 76461】** 联邦 due **今日 09-17**：**CVE-2026-76461**（Secure Email Gateway／AsyncOS 未认证 SQLi → 底层 OS **root** 命令执行）。修复示例：`15.5.5-014`／`16.0.4-302`／`16.5.0-780`。防御：尽快按厂商 advisory 升级、限制网关暴露、按 advisory 在 `mail_logs` 做异常狩猎（防御向，不展开攻击步骤）。
  CISA：https://www.cisa.gov/news-events/alerts/2026/09/14/cisa-adds-one-known-exploited-vulnerability-catalog
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76461

- **【新起逾期 · LiteLLM／Starlette】** due 曾为 **09-16**，今日起标逾期：**CVE-2026-59822**（MCP Streamable HTTP 不当认证）／**CVE-2026-48710**（Host 头未校验 → 路径类认证绕过风险）。防御：升级 LiteLLM **≥1.84.0**／Starlette **≥1.0.1**，限制 MCP／ASGI 对外暴露。
  LiteLLM：https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q
  Starlette：https://github.com/Kludex/starlette/security/advisories/GHSA-86qp-5c8j-p5mr
  OSTIF BadHost：https://ostif.org/disclosing-the-badhost-vulnerability-in-starlette

- **【明日 due · Chromium V8 85046 · 在野】** **CVE-2026-85046** 联邦 due **明日 09-18**；Google 称 **exploitation in the wild**。稳定通道修复：**152.0.7977.82/.83**（Win／Mac）／**152.0.7977.82**（Linux）。防御：全舰队尽快验证 Chrome／Edge／基于 Chromium 的浏览器版本覆盖。
  厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85046

- **【昨日 NEW 仍开放 · due 09-19】** **CVE-2026-58704** Pixel／**CVE-2026-76460** Cisco ISE／**CVE-2026-87886** Acronis Backup — KEV catalog 本窗口 **+0**，三条仍开放。KEV 仍 **2026.09.16／1713**。
  Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
  Cisco ISE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  Acronis：https://security-advisory.acronis.com/advisories/SEC-10986

- **【X NEW · Tutor LMS 78175】** Wordfence：**CVE-2026-78175**，Tutor LMS **≤4.0.7** → **4.0.8**；订阅者级 PHP 对象注入／RCE 风险（开放注册＋变现场景更暴露）。X：@__kokumoto／@averyjparker。
  文章：https://www.wordfence.com/blog/2026/09/100000-wordpress-sites-exposed-to-remote-code-execution-via-php-object-injection-vulnerability-found-by-wordfence-argus-in-tutor-lms/
  原帖：https://x.com/__kokumoto/status/2100724391386783755 · https://x.com/averyjparker/status/2100724283735462305

- **【X NEW · Sentry Seer PhantomFix 90999】** **CVE-2026-90999**（agyn.io）；CERT／公开笔记称 **尚无厂商补丁信息**。防御：暂停 Seer 自动修复／交接、强制人工确认、收紧包安装与仓库凭据。X：@labelmake。
  文章：https://agyn.io/blog/sentry-seer-autofix-vulnerability
  原帖：https://x.com/labelmake/status/2100724069230596216

- **【X NEW · AWS IoT Python SDK 92943】** **CVE-2026-92943**：证书主机名校验不当；**1.5.3–1.6.0** → **1.6.1**（默认 mTLS 8883／WebSocket SigV4 443 受影响；ALPN 443 不受影响）。X：@XavierRiveraX。
  厂商：https://aws.amazon.com/security/security-bulletins/2026-114-aws/
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-92943
  原帖：https://x.com/XavierRiveraX/status/2100723858021966229

- **【NEW ICS · 260-01..07】** CISA 今日新增七份 ICS advisory＋一份 Update A。详见 CVE 节。
  列表入口：https://www.cisa.gov/news-events/ics-advisories

- **【威胁 · Settra／Team Cymru／BC 头条／tl;dr #346】** Huntress：**Settra** MeshAgent 勒索剧本（含公开 IoC）；Team Cymru 勒索基础设施分析；BC：Brevo 供应链 ClickFix／RatHat Android／SparroWocky／NightmareStresser 查封等；tl;dr sec **#346 NEW**（Anthropic TI 等）。
  Huntress：https://www.huntress.com/blog/new-settra-ransomware-variant
  Team Cymru：https://www.team-cymru.com/post/ransomware-infrastructure-analysis
  tl;dr #346：https://tldrsec.com/p/tldr-sec-346

- **【工具 · 核心无升版 · Havoc Pro 0.8／ARES 等】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 均无升版。LWiS：@C5pider **Havoc Professional 0.8 Leviathan**（防御向仅记存在）。Search B：ARES／Mythic Telegram profile／ReflectivePluginLoader／flightsim／Red-Team-Roadmap／dsh-redteam-model／nuclei #7749（部分先前已见）。
  nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
  Havoc 原帖：https://x.com/C5pider/status/2100598546021953653

## CVE / POC / 漏洞

### 1. 【今日 due】Cisco Secure Email Gateway CVE-2026-76461

CISA **2026-09-14** 入目；联邦 due **今日 2026-09-17**。未认证 SQL 注入（经特制邮件）可在底层 OS 以 **root** 执行任意命令。防御：升级至厂商修复版本（示例 **15.5.5-014／16.0.4-302／16.5.0-780**）、限制网关暴露、按 advisory 在 `mail_logs` 狩猎相关异常（防御向）。

地址：
- CISA：https://www.cisa.gov/news-events/alerts/2026/09/14/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76461

IoC：未见公开 IoC IP／样本哈希列表。

### 2. 【新起逾期】LiteLLM CVE-2026-59822／Starlette CVE-2026-48710

联邦 due 曾为 **2026-09-16**，今日起标逾期。LiteLLM：MCP Streamable HTTP 不当认证，伪造 Bearer 可触及 MCP tooling。Starlette：Host 头未校验，`request.url.path` 可与路由路径偏离（路径类认证绕过风险）。防御：对照 GHSA 升级、限制对外暴露的 MCP／ASGI 入口。

地址：
- LiteLLM GHSA：https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q
- LiteLLM NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-59822
- Starlette GHSA：https://github.com/Kludex/starlette/security/advisories/GHSA-86qp-5c8j-p5mr
- Starlette NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-48710
- OSTIF：https://ostif.org/disclosing-the-badhost-vulnerability-in-starlette

IoC：未见公开 IoC。

### 3. 【明日 due · 在野】Google Chromium V8 CVE-2026-85046

CISA due **2026-09-18**（added 2026-09-04）。V8 类型混淆 → 沙箱内 RCE（特制 HTML）；影响 Chrome／Edge／Opera 等。Google 公告称 **exploitation is in the wild**。修复：**152.0.7977.82/.83**（Windows／Mac）、**152.0.7977.82**（Linux）。

地址：
- 厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC。

### 4. 【昨日 NEW 仍开放 · due 09-19】Pixel 58704／Cisco ISE 76460／Acronis 87886

KEV catalog 本窗口 **无变更（+0）**；三条仍 due **2026-09-19**。简要续报：
- **CVE-2026-58704** Google Pixel 蜂窝基带不当授权／权限绕过 → 提权；补丁级别叙事 **2026-09-05+**。
- **CVE-2026-76460** Cisco ISE／ISE-PIC 特权 API 误用 → 未认证可绕过 Web 管理；修方向含 ISE 3.1P12／3.2P11／3.3P12／3.4P7／3.5P4。
- **CVE-2026-87886** Acronis Backup cPanel／WHM 插件与 Plesk 扩展默认权限不当 → 本地提权；厂商称有限在野。

地址：
- CISA +1：https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA +2：https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
- Pixel 厂商：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- Pixel BC：https://www.bleepingcomputer.com/news/security/google-fixes-actively-exploited-android-zero-day-on-pixel-devices/
- Cisco ISE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- Cisco ISE BC：https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/
- Acronis：https://security-advisory.acronis.com/advisories/SEC-10986
- Acronis BC：https://www.bleepingcomputer.com/news/security/acronis-warns-of-actively-exploited-flaw-in-its-cpanel-backup-plugin/

IoC：未见公开 IoC。

### 5. 【X NEW】WordPress Tutor LMS CVE-2026-78175

Wordfence Argus 披露；约 **10 万**站点叙事暴露面。受影响 **≤4.0.7**，修复 **4.0.8**。订阅者级 PHP 对象注入 → RCE 风险；开放注册／变现场景门槛更低。防御：立即升级、审查低权限账户与注册／变现暴露面。**本报不转载 PoC／利用步骤。**

地址：
- 文章（Wordfence）：https://www.wordfence.com/blog/2026/09/100000-wordpress-sites-exposed-to-remote-code-execution-via-php-object-injection-vulnerability-found-by-wordfence-argus-in-tutor-lms/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-78175
- X 原帖：https://x.com/__kokumoto/status/2100724391386783755
- X 原帖：https://x.com/averyjparker/status/2100724283735462305

IoC：未见公开 IoC。

### 6. 【X NEW】Sentry Seer PhantomFix CVE-2026-90999

Agyn（2026-09-14）描述：伪造事件／输入可劫持 Seer 自动修复代理（PhantomFix）。公开笔记／CERT 侧称 **尚无厂商补丁版本**。防御：暂停自主修复／交接、强制人工确认、限制包安装与仓库凭据，直至有官方修复。**不转载触发／复现细节。**

地址：
- 文章：https://agyn.io/blog/sentry-seer-autofix-vulnerability
- NVD（记录可能不完整／受限）：https://nvd.nist.gov/vuln/detail/CVE-2026-90999
- X 原帖：https://x.com/labelmake/status/2100724069230596216

IoC：未见公开 IP／域名／哈希（公开 DSN 为输入面叙事，无具体 DSN 公布）。

### 7. 【X NEW】AWS IoT Device SDK for Python CVE-2026-92943

证书与主机名不匹配时未正确校验；受影响 **AWSIoTPythonSDK 1.5.3–1.6.0**（Python 3.7+），升级 **1.6.1**。AWS：默认 X.509／mTLS **8883** 与 WebSocket SigV4 **443** 路径受影响；**ALPN 443** 不受影响；无变通办法，分叉代码需自行合入修复。

地址：
- 厂商公告：https://aws.amazon.com/security/security-bulletins/2026-114-aws/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-92943
- X 原帖：https://x.com/XavierRiveraX/status/2100723858021966229

IoC：未见公开 IoC。

### 8. 【LWiS】Cleo Harmony CVE-2026-84114（SAML 绕过 → RCE 叙事）

@ArmadinSecurity（经 @AndrewOliveau 转发）：称经 Okta 自注册链路，结合 SAML XML Signature Wrapping（XSW）与跨存储身份混淆，可达 Cleo Harmony 生产环境 OS 命令执行；关联 **CVE-2026-84114**。**本窗口仅见 X 卡片／截断文案，未见独立厂商 advisory 链接落盘** → 防御向仅记公开披露存在，待厂商／CVE 详情页交叉；**不转载利用链步骤。**

地址：
- X 原帖：https://x.com/ArmadinSecurity/status/2100712449821294744
- （厂商／NVD 独立链接：本采集未见可抄录 URL）

IoC：未见公开 IoC。

### 9. 【NEW ICS】ICSA-26-260-01..07 ＋ ICSA-26-211-07 Update A

相对昨日 258 批次，今日新增：
- **260-01** Bransys ELD（CVE-2026-77960／86520／86689）
- **260-02** Mitsubishi Electric GX Works3 and Motion Control Settings（CVE-2026-15688）
- **260-03** Hitachi Energy FACTS Control Platform（CVE-2024-3980／3982／4872／7940／7941）
- **260-04** Schneider Electric Modicon M340 Controller and Communication Modules（CVE-2025-6625）
- **260-05** Schneider Electric NetBotz 5 750／755（CVE-2026-13336／13337）
- **260-06** ABB Ability Edgenius（CVE-2026-31431）
- **260-07** Schneider Electric PowerChute Serial Shutdown（CVE-2026-13348）
- **211-07 Update A** Mitsubishi Electric CC-Link IE TSN Communication Protocol（CVE-2026-13584）

地址：
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-260-01
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-260-02
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-260-03
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-260-04
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-260-05
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-260-06
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-260-07
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-211-07
- 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC（见各 ICS advisory 缓解措施）。

### 10. 【仍逾期】ScreenConnect／GitLab／PaperCut／MikroTik／Citrix／Fortinet／FMC／Magento／N-able

重点续报（due 自 09-11～09-14 起逾期）：
- **CVE-2026-84869** ConnectWise ScreenConnect（BC 活跃利用续报）
- **CVE-2026-85706** GitLab CE／EE 任意文件读
- **CVE-2026-81578／82078** PaperCut NG／MF
- **CVE-2026-67277／86060** MikroTik RouterOS（CERT.pl IoC IP 仍见）
- **CVE-2026-19490** Citrix NetScaler／**CVE-2025-25249** Fortinet／**CVE-2026-20079** Cisco FMC／**CVE-2026-75650** Magento／**CVE-2026-86218** N-able

地址：
- ScreenConnect 厂商：https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin
- ScreenConnect BC：https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-critical-screenconnect-flaw/
- GitLab：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- Citrix：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- Fortinet：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- Cisco FMC：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- Talos IoC raw：https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/09/ongoing-fmc-exploitation.txt
- Magento：https://helpx.adobe.com/security/products/magento/apsb26-146.html
- N-able：https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/

IoC：MikroTik CERT.pl IP `82.192.72.4` · `103.102.31.18`；FMC 见 Talos raw；其余多数未见本窗口新公开 IoC。

### 11. 【边缘／教育】CORS 利用与缓解视频（Undercode）

@UndercodeUpdate 分享 CORS exploitation and mitigation 教育向视频／文章。**标注 Educational；本报不转载利用步骤。**

地址：
- 文章：https://undercodetesting.com/cross-origin-resource-sharing-cors-exploitation-and-mitigation-analyzing-vulnerability-disclosure-workflows-video/
- 原帖：https://x.com/UndercodeUpdate/status/2100724146120351828

IoC：不适用。

## 工具与 GitHub 发布

### 1. Sliver／nuclei／nuclei-templates — 无升版

| 项目 | 标签 | 较昨 | URL |
|------|------|------|-----|
| BishopFox/sliver | v1.7.7 | unchanged | https://github.com/BishopFox/sliver/releases/tag/v1.7.7 |
| projectdiscovery/nuclei | v3.11.1 | unchanged | https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1 |
| projectdiscovery/nuclei-templates | v10.4.9 | unchanged（昨 NEW） | https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9 |

另：httpx v1.12.0／katana v1.7.0 非近 2 日新发，仅作感知。
- httpx：https://github.com/projectdiscovery/httpx/releases/tag/v1.12.0
- katana：https://github.com/projectdiscovery/katana/releases/tag/v1.7.0

### 2. Havoc Professional 0.8 Leviathan（LWiS · 防御向仅记存在）

@C5pider 宣布 **Havoc Professional 0.8: Leviathan**（Kaine User-Defined C2、Linux post-ex、端口转发／sleep masking、.NET／PowerSafe、内存 PE／BOF-PE、HTTPS SNI spoofing、许可与 UI 等）。**本报仅记公开发布存在，不提供使用步骤／配置／规避指南。** 本采集未见独立下载 URL 落盘（仅 X 原帖）。

地址：
- X 原帖：https://x.com/C5pider/status/2100598546021953653

IoC：不适用（工具发布）。

### 3. Search B 工具／研究仓（防御向列表）

覆盖约 **33.22h**；其中 **4** 条先前已见（nuclei #7749／Phantom Loader 笔记／calc 补丁玩笑／dsh-redteam-model），仍列但标注：
- **ARES**（Mafifrizi）— 授权交战自动化相关仓。**仅记存在。**
- **Mythic Telegram profile**（DavidCarliez）— Telegram bot-to-bot 作为 Athena 传输。
- **ReflectivePluginLoader**（racoten）— 反射插件加载器（扩展 beacon 叙事）。
- **flightsim**（AlphaSOC）— 合成 C2 流量以评估检测覆盖（蓝队检测测试向）。
- **Red-Team-Roadmap**（Dev-Chukwuma）— 被动侦察／OSINT／攻击面课程笔记。
- **dsh-redteam-model**（SeaOf0）— 【先前已见】十类安全研究模式拆为 persona／playbook／skills。
- **nuclei #7749** — 【先前已见】zstd 解码器未关闭 → goroutine／内存泄漏议题。
- **Phantom Loader LetsDefend 笔记** — 【先前已见】Ghidra 分析笔记。
- calc patcher 玩笑链 — 【先前已见】低信号，不升格。

地址：
- ARES：https://github.com/Mafifrizi/ARES · https://x.com/FieryBagels/status/2100689353919877312
- Mythic Telegram：https://github.com/DavidCarliez/mythic_telegram_profile · https://x.com/ipurple/status/2100671558729499058
- ReflectivePluginLoader：https://github.com/racoten/ReflectivePluginLoader · https://x.com/racotennn/status/2100416170809753863
- flightsim：https://github.com/alphasoc/flightsim · https://x.com/alphasoc/status/2100601138760360207
- Red-Team-Roadmap：https://github.com/Dev-Chukwuma/Red-Team-Roadmap · https://x.com/httpschuks/status/2100663048885117280
- dsh-redteam-model：https://github.com/SeaOf0/dsh-redteam-model · https://x.com/vintcessun/status/2100187703518405055
- nuclei #7749：https://github.com/projectdiscovery/nuclei/issues/7749 · https://x.com/geeknik/status/2100346854370070985
- Phantom Loader 笔记：https://github.com/0xAshvin/Soc-investigation/tree/main/letsdefend · https://x.com/0xAshvin/status/2100204724314419380

IoC：不适用。

### 4. Microsoft Graph PowerShell — 放弃 Windows PowerShell 5.1 支持（LWiS）

@SamErde（经 @PyroTek3 转发）：Microsoft 宣布未来 Graph PowerShell 模块将放弃对 Windows PowerShell **5.1** 的支持；作者视为对模块可靠性的正向投入。防御／运维：规划迁移至 PowerShell 7+ 与官方推荐运行时。

地址：
- 文章：https://devblogs.microsoft.com/microsoft365dev/investing-in-a-more-reliable-microsoft-graph-powershell-experience/
- 原帖：https://x.com/SamErde/status/2100578588621697406

IoC：不适用。

### 5. Constrained Language Mode 绕过笔记（LWiS · 防御感知）

@enigma0x3（经 @PyroTek3 转发）指向一份 gist，讨论在 App Control for Business 环境下与 Constrained Language Mode 相关的行为（称已报告且「by design」）。**本报仅作防御感知：审查相关控制面与应用控制策略；不转载绕过步骤。**

地址：
- Gist：https://gist.github.com/enigma0x3/22d6fc84956f154faf338966cd6d9bb0
- 原帖：https://x.com/enigma0x3/status/2100628652664787319

IoC：不适用。

### 6. 其他 LWiS 工具／产品短讯

- @dmcxblue：课程／评估工具链更新叙事（含 Havoc standIn BOF／Rubeus 更新引用）— **仅记存在，不展开**。https://x.com/dmcxblue/status/2100711906306912268
- @Dr_Machinavelli＠LABScon：开源权重模型进攻能力演示叙事 — 边缘。https://x.com/Dr_Machinavelli/status/2100694051725217846
- @C2IRIS：Apple 拟在 iOS 引入内核级 EDR／EndpointSecuritySE 监控叙事（链接落盘异常为 `https://com.apple`，信息有限）。https://x.com/C2IRIS/status/2100692307250938322
- @howardnoakley：macOS XProtect 5360 与版本更新节奏讨论。https://x.com/howardnoakley/status/2100698133411803222

IoC：不适用或未见。

## APT / Malware 分析

### 1. tl;dr sec #346 NEW（Anthropic TI 等）

published **2026-09-17**。头条：PortSwigger HTTP Terminator／AI 安全研究；Anthropic September 2026 Threat Intel；Cloudflare Codex 工程标准。通讯提及 CVE-2026-39987／42016／42018／82329 等（细节以原文为准）。Risky 仍 **RBNEWS612**／**SRB183**（613／184 仍 404）。

地址：
- tl;dr #346：https://tldrsec.com/p/tldr-sec-346
- Risky：https://risky.biz/RBNEWS612/ · https://risky.biz/SRB183/
- Anthropic 官方：https://www.anthropic.com/threat-intelligence-report-september-2026
- Anthropic PDF：https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf

IoC：未见公开 IP／域名／哈希（以 newsletter／官方 PDF 附录为准）。

### 2. Huntress — Settra MeshAgent 勒索剧本（含 IoC）

Huntress **2026-09-17**：Settra 变种使用 MeshAgent RMM 持久化、恢复抑制、清日志，并见 BYOVD 个例。X／聚合亦见 TMCnet 转载。防御：狩猎 MeshAgent 持久化与下列指标、限制／监控 RMM 部署、保护恢复控制与日志、排查暴露 VPN／凭据。

地址：
- Huntress：https://www.huntress.com/blog/new-settra-ransomware-variant
- TMCnet 转载：https://insight.tmcnet.com/insight/huntress-exposes-settra-s-repeatable-meshagent-ransomware-playbook-mu61kwqf
- X：https://x.com/tmcnet/status/2100712570902474754

IoC（Huntress 公开，原样抄录）：
- IP：`45.13.122[.]7` · `193.5.65[.]114`
- 主机名：`WIN-LIVFRVQFMKO`
- 文件／工件：`mvtcs.exe` · `gdrv.sys` · `RESTORE_FILES.txt` · 扩展名 `.locked`／`.locked_wip`

### 3. Team Cymru — 勒索基础设施分析

Team Cymru（2026-09-15）：跨 20+ 调查的共性趋势 — 滥用暴露 RDP／SSH／VPN、合法 RMM、Rclone／FileZilla、VPS／代理／Tor，以及主机名 `kali` 等标签。**未公开发布客户级具体 IoC。** 防御：优先 MFA、移除互联网暴露 RDP、行为／出站流量狩猎，而非仅靠静态 IP／ASN 封锁。

地址：
- 文章：https://www.team-cymru.com/post/ransomware-infrastructure-analysis
- X：https://x.com/DylanOwendylan/status/2100726085826519100

IoC：未见客户级公开 IoC 列表（文中明确未分享具体调查 IoC）。

### 4. Trickbot 创始人嫌疑／Kovalev（Meduza）

Meduza：德国警方指认 Vitaly Kovalev 为 Trickbot 相关团伙创始人嫌疑；俄罗斯「新人」党曾将其列入选举候选人名单（医院勒索叙事续传）。新闻向。

地址：
- Meduza：https://meduza.io/en/news/2026/09/18/germany-suspects-vitaly-kovalev-of-founding-the-hacking-group-behind-trickbot-whose-ransomware-hit-u-s-hospitals-now-the-new-people-party-has-made-him-a-candidate-for-russia-s-parliament
- X：https://x.com/meduza_en/status/2100721801659584740 · https://x.com/giovannidalloli/status/2100713715255464031

IoC：不适用（人物／司法新闻）。

### 5. BC 头条：Brevo ClickFix／RatHat／SparroWocky／NightmareStresser／CHOSEN BRICK 续报

公开备援首页 spot-check：
- **Brevo** 供应链向客户站点注入 ClickFix 脚本。
- **RatHat** Android 恶意软件（AI 自动化设备控制叙事）。
- **SparroWocky** — 中国相关政府间谍活动叙事。
- **NightmareStresser** DDoS-for-hire 平台遭美方查封。
- **CHOSEN BRICK** 伊朗相关 Windows 间谍恶意软件 — 昨主条，今日仍列于 BC 首页。
- 另：OpenAI 详述 AI agent 未授权行动更多案例（边缘）。

地址：
- Brevo：https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/
- RatHat：https://www.bleepingcomputer.com/news/security/new-rathat-android-malware-uses-ai-to-automate-device-control/
- SparroWocky：https://www.bleepingcomputer.com/news/security/chinese-hackers-use-sparrowocky-malware-in-govt-espionage-attacks/
- NightmareStresser：https://www.bleepingcomputer.com/news/security/fbi-seizes-nightmarestresser-service-linked-to-thousands-of-ddos-attacks/
- CHOSEN BRICK：https://www.bleepingcomputer.com/news/security/iranian-hackers-use-chosen-brick-windows-malware-to-spy-on-targets/
- OpenAI agents：https://www.bleepingcomputer.com/news/security/openai-details-more-cases-of-ai-agents-taking-unauthorized-actions/

IoC：本备援未抄录各文完整 IoC → 以原文附录为准；摘要写 **未见本报可抄录新公开 IoC**（或见原文）。

### 6. ForIntOrg — 俄罗斯干扰剧本档案叙事（低信号）

@ForIntOrg 长帖统计其档案中俄罗斯相关干扰事件规模／方法分布，并指向 foreigninterference.org。属档案／叙事汇总，**信号偏低**，作简要记录。

地址：
- 站点：https://www.foreigninterference.org/
- 原帖：https://x.com/ForIntOrg/status/2100725403598082369

IoC：未见可操作公开 IoC 列表。

### 7. Qilin／Vigatec 智利受害者声称（FalconFeeds · 噪声）

@FalconFeedsio 称智利 Vigatec 遭 Qilin 勒索、拟 9–10 日内泄数据。**未验证受害者监控噪声**，附 caveat，不升格为主条。

地址：
- 原帖：https://x.com/FalconFeedsio/status/2100710791112794356
- 受害者站点（声称关联）：https://www.vigatec.com/

IoC：未见可靠公开 IoC。

### 8. Anthropic TI 续传／其他短讯

- @ReadOmniscient／LWiS @endingwithali：Anthropic Sep 2026 TI 续读（「sophistication 不再是可靠归因信号」等摘要 — **以官方页／PDF 为准**）。
- @cyberhawkintel：Cisco 第二起活跃利用告警短讯（本帖无外链；交叉见 ISE／ESA 条目）。
- Clay County 住房机构勒索本地新闻（低信号事件报道）。

地址：
- Anthropic 官方：https://www.anthropic.com/threat-intelligence-report-september-2026
- X ReadOmniscient：https://x.com/ReadOmniscient/status/2100712560748282188
- X endingwithali：https://x.com/endingwithali/status/2100237380695347605
- X cyberhawkintel：https://x.com/cyberhawkintel/status/2100713632598225066
- Clay County：https://www.inforum.com/news/moorhead/clay-county-housing-agency-subject-of-ransomware-attack · https://x.com/WDAYnews/status/2100722692458533239

IoC：以各原文为准；本窗口未见新独立可抄录列表 → **未见公开 IoC**（或见原文）。

## 地址／IoC 汇总

- **Cisco ESA 76461（今日 due）／LiteLLM／Starlette（新起逾期）／Chromium 85046（明日 due）／Pixel／ISE／Acronis（due 09-19）**：未见公开 IoC。
- **Tutor LMS 78175／Sentry Seer 90999／AWS IoT 92943／Cleo 84114**：未见公开 IoC。
- **NEW ICS 260-01..07／211-07 Update A**：未见公开 IoC。
- **Huntress Settra**：IP `45.13.122[.]7` · `193.5.65[.]114`；主机 `WIN-LIVFRVQFMKO`；`mvtcs.exe` · `gdrv.sys` · `RESTORE_FILES.txt` · `.locked`／`.locked_wip`。
- **MikroTik（CERT.pl，续报）**：`82.192.72.4` · `103.102.31.18`。
- **Cisco FMC Talos**：https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/09/ongoing-fmc-exploitation.txt
- **Team Cymru 勒索基础设施**：未见客户级公开 IoC（文中明确未分享）。
- **Brevo／RatHat／SparroWocky／NightmareStresser／CHOSEN BRICK／ForIntOrg／Qilin 声称／Anthropic**：本报未见可抄录新独立 IoC 列表（或以各原文附录为准）→ **未见公开 IoC**（或见原文）。
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
