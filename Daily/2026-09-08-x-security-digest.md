# X 安全情报晚报 · 2026-09-08

> 搜集窗口：圣地亚哥时间 **2026-09-07 20:00 至 2026-09-08 ~20:55**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周二）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-08.json`（collected_at **2026-09-08T20:35:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-08.md`。CISA KEV catalogVersion **2026.09.08**／**1699** 条／dateReleased **2026-09-08T18:00:21.1079Z**（相对昨日 **+4**；新入 Adobe Magento **CVE-2026-75650**、N-able N-central **CVE-2026-86218**、微软 Windows **CVE-2026-81963／CVE-2026-85880**）。
> **期限今日 09-08：无。期限明日 09-09：legacy 四条（Ajax.NET／Libuser／ABRT／Linux Kernel）。** Sep2 五条联邦 BOD（Kestra **CVE-2026-49869**、JFrog **CVE-2026-82329**、Sangoma **CVE-2026-9586**、SonicWall **CVE-2026-83548/83549**）自 **09-05** 起仍 **OVERDUE**。TrueConf **CVE-2026-72530**（due 09-03）／MLflow **CVE-2026-64849**（due 09-02）仍逾期。due_near：JFrog 路径 **CVE-2026-66384**（09-10）；**NEW** Magento／N-able（**09-11**）；PaperCut **81578/82078**（09-14）；LiteLLM／Starlette（09-16）；Chromium **85046**（09-18）；微软两在野（**09-22**）。
> X：`/workspace/x-posts-2026-09-08.json`（合并 **52** 条：A14／B3／C23／LWiS12；其中 **新 52**／已见 0；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.34h**（高流量，**远不足 24h**）。Search B 约 **50.7h**（含窗外续帖）。Search C 约 **3.65h**。LWiS List 约 **26h**（保留 12 条安全相关）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · KEV +4／Patch Tuesday】** CISA 今日将四条入 KEV：Adobe Magento **CVE-2026-75650**（due **09-11**）、N-able N-central **CVE-2026-86218**（due **09-11**，Huntress 记主动利用）、微软 Windows **CVE-2026-81963／CVE-2026-85880**（due **09-22**，在野 LPE）。MSRC 九月更新可用；媒体称本轮约 **974** 洞（Windows 723／Office 222）。联邦 BOD Sep2 五条仍逾期。
  警报：https://www.cisa.gov/news-events/alerts/2026/09/08/cisa-adds-four-known-exploited-vulnerabilities-catalog
  MSRC：https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep
  Krebs：https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/
  SecurityWeek：https://www.securityweek.com/microsoft-patches-record-974-vulnerabilities-including-two-exploited-zero-days/

- **【NEW · Magento／N-able】** Adobe APSB26-146 覆盖 Commerce／Magento 模板引擎相关 **CVE-2026-75650**；N-able 预认证 RCE **CVE-2026-86218**（fix前 **2026.3.1.14**）与 Huntress 主动利用文交叉，联邦 due **09-11**。
  Adobe：https://helpx.adobe.com/security/products/magento/apsb26-146.html
  N-able：https://me.n-able.com/s/security-advisory/aArVy0000002Ld3KAE/cve202686218-preauthentication-remote-code-execution
  Huntress：https://www.huntress.com/blog/n-able-vulnerability-exploitation

- **【X · FortiGate／PivotC2】** 日文转述 SOCRadar：针对 **CVE-2025-25249** 的 FortiGate 利用并部署 PivotC2（Node.js RAT），声称已瞄超 **30,000** IP。按 Fortinet FG-IR-25-084 升级／缓解；**不转写利用链。**
  厂商：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2025-25249
  X：https://x.com/__kokumoto/status/2097464362390966586

- **【NEW · PaperCut Sep8 状态 bump】** 厂商页 **last_updated: September 8, 2026**（原 Sep7）：*No new information to report; work continues towards the official release.* Emergency Patch **R3** 仍最新；KEV **CVE-2026-81578/82078** due **2026-09-14**。
  厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/

- **【ICS NEW】** ICSA-26-251-01 CareCam Pro／**CVE-2026-85083**（CISA：非远程可利用；未见公开利用）。
  https://www.cisa.gov/news-events/ics-advisories/icsa-26-251-01

- **【新闻 · tl;dr #344 NEW】** *VMs won't contain Cyber-capable Agents, AWS AI Security Analyst, Decompilers vs LLMs*。Risky Biz **无新增**（RBNEWS610／BTN182 仍最新）。
  https://tldrsec.com/blog/tldr-sec-344/

- **【工具】** Sliver **仍 v1.7.7**；nuclei-templates **仍 v10.4.8**。NEW：SpecterOps **TATS**；C2PE／Tailcat 隧道 PoC 仓库；GhostSocks 恶意 GitHub 伪装与 IoC。
  TATS：https://specterops.io/blog/2026/09/08/token-analysis-and-tracking-system-tats/
  C2PE：https://github.com/sneakerhax/C2PE/blob/main/Command_and_Control/tailcat_http_exec/README.md

- **【Chrome】** Desktop Stable **153.0.8010.36**／ChromeOS **152.0.7977.113**／Android **153.0.8010.36** 频道帖（帖体 **无 CVE 列表**）；KEV Chromium **CVE-2026-85046** 仍 due **09-18**。

## CVE / POC / 漏洞

### 1. 【KEV NEW】四条入目录（2026-09-08）

CISA 基于在野利用证据将下列四条加入 KEV。按厂商补丁／BOD 26-04 与取证分流要求收敛；**不转写利用细节。**

| CVE | 产品 | due | 简述 |
|-----|------|-----|------|
| CVE-2026-75650 | Adobe Commerce／Magento | **09-11** | 模板引擎特殊元素未正确中和 → 任意代码执行风险 |
| CVE-2026-86218 | N-able N-central | **09-11** | 静态代码注入 → 预认证 RCE（before 2026.3.1.14） |
| CVE-2026-81963 | Microsoft Windows Update Stack | **09-22** | link following → 本地提权至 SYSTEM |
| CVE-2026-85880 | Microsoft Windows ALPC | **09-22** | 堆溢出 → 本地提权 |

地址：
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/08/cisa-adds-four-known-exploited-vulnerabilities-catalog
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- Adobe：https://helpx.adobe.com/security/products/magento/apsb26-146.html
- N-able：https://me.n-able.com/s/security-advisory/aArVy0000002Ld3KAE/cve202686218-preauthentication-remote-code-execution
- Huntress：https://www.huntress.com/blog/n-able-vulnerability-exploitation
- SecurityWeek N-able：https://www.securityweek.com/n-able-patches-critical-zero-day-in-n-central/
- SecurityWeek Adobe：https://www.securityweek.com/adobe-patches-over-170-vulnerabilities-including-commerce-zero-day/
- MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963 https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-75650 https://nvd.nist.gov/vuln/detail/CVE-2026-86218 https://nvd.nist.gov/vuln/detail/CVE-2026-81963 https://nvd.nist.gov/vuln/detail/CVE-2026-85880

IoC：Huntress 文 HTML 中可见示例 SHA256 `839ac630f0ae92cad1b87b1d695f1cd794786146f5140edcde6b96459a929e90` 与 IP `104.30.180.109`（上下文需对照原文）；完整狩猎以 Huntress／N-able 原文为准。

### 2. 【KEV 逾期续】Sep2 五条 BOD ＋ TrueConf／MLflow

JFrog Artifactory **CVE-2026-82329**、Sangoma Switchvox **CVE-2026-9586**、SonicWall SMA1000 **CVE-2026-83548/83549**、Kestra OSS **CVE-2026-49869** 自 09-05 起逾期。TrueConf Server **CVE-2026-72530**（due 09-03）、MLflow **CVE-2026-64849**（due 09-02）仍逾期。近期限：JFrog 路径 **CVE-2026-66384**（09-10）；LiteLLM **CVE-2026-59822**／Starlette **CVE-2026-48710**（09-16）。X 续见 Sangoma KEV 提醒帖。

地址：
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-82329 https://nvd.nist.gov/vuln/detail/CVE-2026-9586 https://nvd.nist.gov/vuln/detail/CVE-2026-83548 https://nvd.nist.gov/vuln/detail/CVE-2026-83549 https://nvd.nist.gov/vuln/detail/CVE-2026-49869 https://nvd.nist.gov/vuln/detail/CVE-2026-72530 https://nvd.nist.gov/vuln/detail/CVE-2026-64849 https://nvd.nist.gov/vuln/detail/CVE-2026-59822 https://nvd.nist.gov/vuln/detail/CVE-2026-48710 https://nvd.nist.gov/vuln/detail/CVE-2026-66384
- SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
- nuclei（JFrog）：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-82329.yaml
- X（Sangoma）：https://x.com/snypet86/status/2097466897461600371

IoC：未见本条新增统一 IoC；逐厂商公告。

### 3. 【X／MSRC】Microsoft 2026-09 Patch Tuesday（两在野 Zero-day）

MSRC 九月安全更新可用；另宣布扩大面向微软分配 CVE 的机器可读 VEX 覆盖。媒体／日文转述强调在野 **CVE-2026-85880**（ALPC）与 **CVE-2026-81963**（Update Stack），并点名关注 Exchange RCE **CVE-2026-55007**、以及 **CVE-2026-80097** 等叙述。按 MSRC 升级；**不转写利用链。**

地址：
- MSRC 发布说明：https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep
- MSRC 更新指南：https://msrc.microsoft.com/update-guide/
- MSRC CVE：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880 https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963
- Krebs：https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/
- SecurityWeek：https://www.securityweek.com/microsoft-patches-record-974-vulnerabilities-including-two-exploited-zero-days/
- SANS diary：https://isc.sans.edu/diary/September%202026%20Microsoft%20Patch%20Tuesday/33320
- X（MSRC）：https://x.com/msftsecresponse/status/2097374775018750265
- X（日文交叉）：https://x.com/__kokumoto/status/2097463864250274107

IoC：未见公开攻击者 C2／样本哈希；行动以补丁部署为主。

### 4. 【PaperCut】CVE-2026-81578／82078（KEV due 09-14）— Sep8 状态 bump

厂商页 **last_updated September 8, 2026, 4:40pm (AEST)**：无新情报，正式版仍在推进。Emergency Patch **R3** 仍为当前紧急补丁。公网暴露未打补丁应假定失陷。

地址：
- 厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-81578 https://nvd.nist.gov/vuln/detail/CVE-2026-82078

IoC：续见厂商页狩猎路径／示例哈希（见下方 IoC 汇总）；本日无新抄录。

### 5. 【X】FortiGate CVE-2025-25249 ＋ PivotC2（SOCRadar 转述）

声称针对 FortiOS／FortiGate 的 **CVE-2025-25249** 在野利用并部署 PivotC2（面向 FortiGate 的 Node.js RAT），超 3 万 IP 被瞄。防御：按 FG-IR-25-084 升级至固定版本／移除接口 fabric 访问等缓解；狩猎异常出站 TLS／配置导出。**不转写 CAPWAP／利用包细节。**

地址：
- 厂商：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- NVD／CVE：https://nvd.nist.gov/vuln/detail/CVE-2025-25249 https://www.cve.org/CVERecord?id=CVE-2025-25249
- Arctic Wolf 背景：https://arcticwolf.com/resources/blog/cve-2025-25249/
- X：https://x.com/__kokumoto/status/2097464362390966586

IoC：未见本报可独立核验的统一 C2 列表；以 SOCRadar／厂商原文为准。

### 6. 【X】OpenPanel CVE-2026-85610（GHSA）

认证项目成员（reader）可借图表公式求值（CWE-94）在 API 进程触发 RCE 并破坏组织隔离；**2.3.0** 已修。按 GHSA 升级。

地址：
- 厂商／GHSA：https://github.com/Openpanel-dev/openpanel/security/advisories/GHSA-7476-c5cc-8999
- X：https://x.com/devyn/status/2097464749550186735

IoC：未见公开 IoC。

### 7. 【X】ZcopyReaper／Linux CVE-2026-43502（公开 PoC 声称）

帖称 Linux RDS zerocopy 相关 **CVE-2026-43502** 已有公开 PoC。内核稳定树已有修复提交。**仅记漏洞存在与打补丁；不转载 PoC／步骤。**

地址：
- 文章：https://securityonline.info/zcopyreaper-linux-vulnerability/?utm_source=twitter&utm_medium=social_share
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-43502
- X：https://x.com/Hack32_/status/2097467639731748875

IoC：未见公开 IoC。

### 8. 【LWiS】Linux SCTP CVE-2026-64564（SCTPhantom）

腾讯安全研究：Linux SCTP use-after-free；上游有修复。按内核更新收敛；**不转写利用。**

地址：
- 文章：https://matrix.tencent.com/en/2026/08/06/sctphantom-CVE-2026-64564
- X：https://x.com/linkersec/status/2097424490539987312

IoC：未见公开 IoC。

### 9. 【X】MikroTik「MikroTrick」连锁漏洞（日文）

NEXSIGHT 称 RouterOS 六件套（认证绕过至配置夺取），SSH 暴露设备优先更新。按厂商／文章路径打补丁。

地址：
- 文章：https://cyber.nexsight.co/articles/2026/09/09/mikrotik-routeros-mikrotrick-cve-2026-67276-2026-09-09/
- SecurityWeek 交叉：https://www.securityweek.com/mikrotik-patches-critical-flaws-chained-to-hack-routers/
- X：https://x.com/NEXSIGHTNEWS/status/2097463712927940848

IoC：未见公开 IoC。

### 10. 【ICS NEW】CareCam Pro ICSA-26-251-01／CVE-2026-85083

CISA ICS：CareCam Pro IP 摄像头；发布 2026-09-08；评估为**非远程可利用**且**无已知公开利用**。按公告缓解／厂商指导。

地址：
- CISA：https://www.cisa.gov/news-events/ics-advisories/icsa-26-251-01
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85083

IoC：未见公开 IoC。

### 11. 【Chrome／ChromeOS】频道更新 ＋ KEV CVE-2026-85046（due 09-18）

KEV **CVE-2026-85046**（dateAdded 2026-09-04，due **2026-09-18**）仍对应先前 Desktop Stable 安全通道。今日 **NEW** Desktop **153.0.8010.36**、ChromeOS **152.0.7977.113**、Android **153.0.8010.36** 频道帖，帖体 **未见 CVE-2026-*** 枚举。生产优先按 KEV／安全通道收敛。

地址：
- Desktop Stable（09-08）：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- ChromeOS（09-08）：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-chromeos_0586661566.html
- Android（09-08）：https://chromereleases.googleblog.com/2026/09/chrome-for-android-update_01729269728.html
- 先前安全 Stable：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- CISA 09-04：https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog
- NVD／KEV：https://nvd.nist.gov/vuln/detail/CVE-2026-85046 https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85046

IoC：未见公开攻击者 C2／样本哈希；行动以浏览器升级为主。

### 12. 【X】BambuStudio「CutInfo」（无 CVE）

帖称 3D 打印切片相关「CutInfo」已在最新二进制后三天有提交修复，但无 CVE／无正式公告。按上游 commit 更新客户端。

地址：
- 提交：https://github.com/bambulab/BambuStudio/commit/5829aa45f
- X：https://x.com/d0tslash/status/2097464417147347043

IoC：未见公开 IoC。

### 13. 【LWiS】DLL Sideloading 研究（vmware-vmx／libcrypto）

InfoSecHarry：围绕 `vmware-vmx.exe` 与 `libcrypto-3-x64.dll` 的 DLL 侧载研究，并贡献 HijackLibs。**仅记防御检测参考；不转写加载步骤。**

地址：
- 文章：https://www.infosecharry.co.uk/blog/dll-sideloading
- X：https://x.com/InfoSecHarry/status/2097412119331291360

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 1. Sliver／nuclei-templates（公开备援）

Sliver **仍 v1.7.7**（2026-09-03）；nuclei-templates **仍 v10.4.8**（2026-08-24）。本窗未见二者新 release。

地址：
- https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

IoC：不适用。

### 2. 【NEW · LWiS】SpecterOps TATS（Token Analysis and Tracking System）

Hope Walker 宣布 TATS 公开发布，用于身份／令牌分析与追踪，欢迎反馈。

地址：
- 文章：https://specterops.io/blog/2026/09/08/token-analysis-and-tracking-system-tats/
- X：https://x.com/Icemoonhsv/status/2097384948449874388

IoC：未见公开 IoC。

### 3. 【NEW · Search B】C2PE／Tailcat HTTP 隧道 PoC

sneakerhax／C2PE 仓库文档：用 Tailcat 隧道化 C2 流量的示例。**仅记仓库存在；不转写隧道配置／利用步骤。**

地址：
- 仓库：https://github.com/sneakerhax/C2PE/blob/main/Command_and_Control/tailcat_http_exec/README.md
- X：https://x.com/sneakerhax/status/2097368670645428389

IoC：未见公开 IoC。

### 4. 【Search B】Sliver／Cobalt Strike 资源汇总帖

资源向帖列出 Sliver 入口、Cobalt Strike UDC2 BOF、Linux Beacon 仓库及 White Knight Labs 文章。作红队工具交叉；**不展开利用。**

地址：
- https://offsec.tools/tool/sliver https://sliver.sh/
- https://github.com/Cobalt-Strike/udc2-vs/tree/main/udc2-bof-vs
- https://github.com/EricEsquivel/CobaltStrike-Linux-Beacon
- https://whiteknightlabs.com/2026/01/06/the-new-chapter-of-egress-communication-with-cobalt-strike-user-defined-c2/
- X：https://x.com/J4ck3LSyN/status/2097441332692488313

IoC：未见公开 IoC。

### 5. 【tl;dr 提及】gendigitalinc/sage

tl;dr #344 提及 ADR 框架 sage。

地址：
- https://github.com/gendigitalinc/sage
- https://tldrsec.com/blog/tldr-sec-344/

IoC：不适用。

## APT / Malware 分析

### 1. 【X】GhostSocks／恶意 GitHub「GLM-5.3」伪装

威胁情报帖：GhostSocks C2 相关 IP／端口，以及伪装为「GLM-5.3」模型的恶意 GitHub 仓库（哈希 `b490a223f931af6efe4be92dfdef4622`）。防御：封锁下列 IP、审 GitHub 组织／仓库可信度。**不转写样本投放步骤。**

地址：
- 仓库（可疑）：https://github.com/GLM-5.3-app/GLM-5.3
- X：https://x.com/PurpleCondors/status/2097278996463448388

IoC：
- `147.45.197.92:443`
- `194.28.225.230:443`（帖写 `194.28.225.230.443`，按常见格式记为 host:443）
- `94.228.161.88:443`
- `b490a223f931af6efe4be92dfdef4622`

### 2. 【X】Needle 组件（威胁演员 Lupin，Telegram 声称）

OSINT 帖：演员 Lupin 分件出售 Windows／macOS「Needle」项目，含可乘合法站点换页的浏览器扩展叙事。**未核实；仅记威胁情报交叉。**

地址：
- X：https://x.com/osint_barbie/status/2097455949908717872

IoC：未见公开 IoC。

### 3. 【X】亚洲威胁情报周报（9 月第 1 周）

Team_D4rkn3ttz 转述 2026-08-31～09-06 亚洲 CTI 周报（作者 @wntidled／@abotulum）。搜索结果截断，未见完整文章 URL。

地址：
- X：https://x.com/Team_D4rkn3ttz/status/2097446082330632207

IoC：未见公开 IoC。

### 4. 【X】AWS Org 接管路径防御警告（Skyhawk）

AI 赋能威胁演员通过合法配置链实现 AWS Organization 接管的防御叙事警告。

地址：
- X：https://x.com/SkyhawkCloudSec/status/2097437373999026617

IoC：未见公开 IoC。

### 5. 【X】A10 × OpenAI Trusted Access for Cyber

A10 加入 OpenAI 可信访问计划，用于恶意软件分析／DDoS／AI 红队并回馈攻击模式。

地址：
- 文章：https://www.a10networks.com/blog/a10-openai-trusted-access-cyber/
- 短链（已展开）：https://bit.ly/4eSMXNm
- X：https://x.com/A10Networks/status/2097415703116587290

IoC：不适用。

### 6. 【LWiS】LG TV 待机扫描／录制隐私研究

The Verge 报道 Gamers Nexus 等研究：LG 电视在待机／离线时扫描本地设备并采集数据的隐私风险。

地址：
- 文章：https://www.theverge.com/tech/991190/lg-tv-spying-standby-recording-wi-fi-scanning-gamers-nexus
- X：https://x.com/verge/status/2097287239659344093

IoC：不适用。

### 7. 【新闻备援】tl;dr sec #344（NEW）／Risky Biz 无新增

**NEW** #344（2026-09-08）。Risky Biz 探测 RBNEWS611／RB852／SRB183／BTN183／FEATURES39 → 404；昨日 RBNEWS610／BTN182 仍最新。

地址：
- https://tldrsec.com/blog/tldr-sec-344/
- https://tldrsec.com/blog/tldr-sec-343/
- https://risky.biz/RBNEWS610/
- https://risky.biz/BTN182/

IoC：以原文为准。

### 8. 【X】勒索／数据泄露声称（均未独立核实）

窗内多起暗网／勒索站点声称，仅作威胁情报交叉，**标签：未核实**：

| 声称 | X 原帖 |
|------|--------|
| 巴西 IME Events ~502K | https://x.com/DarkWebInformer/status/2097469164394811652 |
| 法国 Solimut Mutuelle ~1M+ | https://x.com/DailyDarkWeb/status/2097452349899821302 |
| GirlsChase TV 2026 DB | https://x.com/DailyDarkWeb/status/2097450840545989088 |
| 印度 Setu Bridge Solutions ~6600+ | https://x.com/DailyDarkWeb/status/2097449937923461307 |
| 意大利 EcommerceGuru.it | https://x.com/DailyDarkWeb/status/2097448987439616236 |
| 土耳其 alfred.com.tr ~300K+ | https://x.com/DailyDarkWeb/status/2097448069898146243 |
| 美国社交市场 ~2.7M（平台未具名） | https://x.com/DarkWebInformer/status/2097446140102713377 |
| 西班牙电力 CUPS ~40M+（SIPS 关联声称） | https://x.com/SaidTangier1980/status/2097442172895162746 |
| Transfast／Mastercard ~11M+ | https://x.com/DailyDarkWeb/status/2097440339434831943 |
| Telegram 相关 ~120M（**非**证实 Telegram 本身被入侵） | https://x.com/ICPLEGEND1966/status/2097434547516219657 |
| play → GT Distributors（US） | https://x.com/ThreatAtlas/status/2097427357598367984 |
| play → Red Star Oil（RS） | https://x.com/ThreatAtlas/status/2097427238719459342 |
| 巴基斯坦 PAEC／PMAD／IB DB 出售声称 | https://x.com/intels_daily/status/2097421971600326841 |
| F6：2025–H1'26 追踪 1.64 亿级／164 次泄露叙事 | https://x.com/blackwired32799/status/2097414673822011479 |
| safepay → hbpro.pt（PT） | https://x.com/ThreatAtlas/status/2097414483568193934 |
| safepay → gsngestion.es（ES） | https://x.com/ThreatAtlas/status/2097414363925647546 |
| safepay → gayafores.es（ES） | https://x.com/ThreatAtlas/status/2097414031468577130 |

关联站点（帖内，**非确认 IoC**）：https://setubridgesolutions.co.in https://www.ecommerceguru.it/ https://alfred.com.tr/tr/ https://hbpro.pt/ https://gsngestion.es/ https://gayafores.es/

Telegram 声称帖附带字符串 `1e672d038cebc619d93186418fa98f6499dbdb9cfdfac54f366c61a4a4ee4362`（上下文不明，可能为哈希／地址；**未核实**）。

IoC：未见本报可核验统一样本哈希；不转载广告包或凭证内容。

### 9. 【周边／低价值】

- HTB Academy 恶意软件分析模块结业：https://x.com/0xkhaled___/status/2097459096546849025
- LiveOverflow 猜测 Hugging Face 是否被入侵（无确认）：https://x.com/LiveOverflow/status/2097461720578920813
- DeFi／链上 exploit 叙事（Balancer／Hemi／Cronos／Notional）：https://x.com/nikonchain/status/2097465216573538469 https://x.com/nikonchain/status/2097464998192918969 https://x.com/ZeroDayDevApp/status/2097464879821050096 https://x.com/NotionalFinance/status/2097463462062408152 — Balancer 关联钱包 `0x11246c5b75b3a88b05f0238ced6cd9b8afc7e0ae`
- GPT-6／agent 赛博能力讨论：https://x.com/moooodit/status/2097464836376723725
- Passkey／二手设备／Black Hat 议题周边：https://x.com/NathanMcNulty/status/2097426305868558473 https://x.com/SwiftOnSecurity/status/2097430266683768956 https://x.com/_EthicalChaos_/status/2097429388648132976

## 地址／IoC 汇总

- **KEV 新入（09-08）**：Magento **75650**／N-able **86218**（due **09-11**）；微软 **81963／85880**（due **09-22**）。Huntress 示例：SHA256 `839ac630f0ae92cad1b87b1d695f1cd794786146f5140edcde6b96459a929e90`；IP `104.30.180.109`。
- **KEV 逾期（自 09-05）**：Kestra 49869／JFrog 82329／Sangoma 9586／SonicWall 83548+83549；TrueConf 72530／MLflow 64849。
- **Chromium CVE-2026-85046**：due 09-18；关注 Desktop／ChromeOS／Android 09-08 频道构建。
- **PaperCut（厂商续抄，due 09-14；Sep8 仍无新情报）**：
  - 狩猎：Application Server 上可疑后利用；`C:\ProgramData\ace.exe`；SimpleHelp 路径 `C:\ProgramData\JWrapper-Remote Access\JWAppsSharedConfig\restricted\SimpleService.exe`（服务名 “Remote Access Service”）；AnyDesk 落盘 `C:\ProgramData\AnyDesk.exe`。
  - 投放 URL（去活化）：`hxxps://sendit[.]sh/Gg7Rp/ace[.]exe`；`hxxps://download[.]anydesk[.]com/AnyDesk.exe`（后者为合法下载域被滥用场景，需结合上下文）。
  - Emergency Patch R3 示例 SHA256（Windows v26 Build 76531）：`9375a9c3cf84140a1d8e21b72d3d2c57d85d4de09ea9ae1dc021b64732427da7`（完整多版本校验和见厂商页）。
- **GhostSocks／恶意 GitHub**：`147.45.197.92:443`；`194.28.225.230:443`；`94.228.161.88:443`；`b490a223f931af6efe4be92dfdef4622`；仓库 https://github.com/GLM-5.3-app/GLM-5.3
- **FortiGate／PivotC2**：未见本报新增可核验统一 C2；以 SOCRadar／FG-IR-25-084 为准。
- **链上钱包（帖内）**：`0x11246c5b75b3a88b05f0238ced6cd9b8afc7e0ae`（Balancer 叙事）。
- **Telegram 声称附带字符串（未核实）**：`1e672d038cebc619d93186418fa98f6499dbdb9cfdfac54f366c61a4a4ee4362`
- **关联域名（帖内，非确认 IoC）**：setubridgesolutions.co.in、ecommerceguru.it、alfred.com.tr、hbpro.pt、gsngestion.es、gayafores.es。
- **其余条目**：写「未见公开 IoC」者以上各节为准。

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
- X Latest B（GitHub 工具／C2）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt%20OR%20implant%20OR%20c2)&src=typed_query&f=live
- X Latest B 备援：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&src=typed_query&f=live
- X Latest C（malware／threat）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS610：https://risky.biz/RBNEWS610/
- Risky BTN182：https://risky.biz/BTN182/
- tl;dr sec：https://tldrsec.com/
- tl;dr #344：https://tldrsec.com/blog/tldr-sec-344/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 09-08 四条警报：https://www.cisa.gov/news-events/alerts/2026/09/08/cisa-adds-four-known-exploited-vulnerabilities-catalog
- CISA 09-02 七条警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- CISA 09-04 Chromium 警报：https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog
- ICS CareCam：https://www.cisa.gov/news-events/ics-advisories/icsa-26-251-01
- MSRC 2026-Sep：https://msrc.microsoft.com/update-guide/releaseNote/2026-Sep
- Adobe APSB26-146：https://helpx.adobe.com/security/products/magento/apsb26-146.html
- N-able CVE-2026-86218：https://me.n-able.com/s/security-advisory/aArVy0000002Ld3KAE/cve202686218-preauthentication-remote-code-execution
- Huntress N-able：https://www.huntress.com/blog/n-able-vulnerability-exploitation
- Fortinet FG-IR-25-084：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- SonicWall SNWLID-2026-0016：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
- Chrome Desktop 09-08：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- Krebs MS Patch Tuesday：https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/
- SecurityWeek MS：https://www.securityweek.com/microsoft-patches-record-974-vulnerabilities-including-two-exploited-zero-days/
- SpecterOps TATS：https://specterops.io/blog/2026/09/08/token-analysis-and-tracking-system-tats/
