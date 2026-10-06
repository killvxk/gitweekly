# X 安全情报晚报 · 2026-10-03

> 搜集窗口：圣地亚哥时间 **2026-10-02 20:00 至 2026-10-03 ~20:20**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-10-03.json`（collected_at **2026-10-03T20:20:00-03:00**）＋ `/workspace/tools-news-pulse-2026-10-03.json`＋ `/workspace/enrich-2026-10-03/`＋ buckets `/workspace/_kev_buckets_2026-10-03.json`。CISA KEV catalogVersion **2026.10.02**／**1733** 条／dateReleased **2026-10-02T15:19:38.2945Z**（相对昨日基线 **2026.10.02／1733**：**count Δ+0**；raw 与昨字节相同；**今日无 NEW**；CISA `2026/10/03` Adds 索引与常见 Adds 直链均 **404**）。**due_today：Cisco CVE-2026-76504**；**newly_overdue：Apple CVE-2026-86950**（昨 due_today）；**仍逾期亮点 21**（含 Citrix 88771／88772；Apple 今日在 newly 未并入 still）；**upcoming** 10-04 Fortinet **104286**、10-05 Zammad **102489／102490**。
> **仍逾期**：Citrix **88771／88772**、Check Point **85102／93616**、Arista VeloCloud **93952**、F5 BIG-IP APM **94127**、JFrog Artifactory **42016／42018**、Zyxel **7273**、MS **81963／85880**、Chromium **87491／85046**、Pixel **58704**、Cisco ISE **76460**、Acronis **87886**、WSO2 **5430**、Adobe **71362**、SharePoint **65660**、MikroTik **67279**、WordPress **87902**。**newly_overdue：Apple CVE-2026-86950**。**即将 due 10-04：Fortinet CVE-2026-104286**。**即将 due 10-05：Zammad CVE-2026-102489／102490**。
> X：`/workspace/x-posts-2026-10-03.json`（合并 **12** 条：A0／B3／C3／LWiS6；唯一数字 id **0**；跨源 ID 重叠 **0**；相对 prior seen_ids **+0** 新数字 id；全部 **12** 条 `id/status_url=null` **未计入** seen_ids；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 可见约 **22h** 但无合格安全帖（保留 0）。Search B 约 **4–7h**。Search C 约 **12–43 分钟**。LWiS List 约 **19 分钟–1h**（扫描约 **9**／保留 **6**；成员数未显示；**交叉校验，不假装为本窗口 24h Latest**；虚拟列表未暴露 status 链接——报告写作者+摘要+已有文章链接，**不编造 URL**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。抓取备注：首页首次 Loading 后刷新可用；RBNEWS619／620／SRB186／BTN185 **404**；tl;dr #349–351 soft-404；Black Hills 旧路径 404→改用 `blackhillsinfosec.com/bloodhound-data-collection/`；`github.com/echelong/cobal` **404**；Cisco／Apple／Zammad enrich **未见公开威胁 IoC**；Fortinet upcoming 沿用 FG-IR IoC。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露／勒索声称一律标 **UNCONFIRMED／未验证**；仅写谁／打什么／补丁与狩猎级防御摘要。

## 今日摘要

- **【主条 · due_today · Cisco CVE-2026-76504】** CISA 于 **2026-09-30** 入 KEV；联邦 due **2026-10-03＝今日**。Catalyst SD-WAN Manager URI hex 编码绕过 Web／API 认证 → 未认证管理员访问。厂商 SA **200**；有日志狩猎指引（`j_security_check`／`viptela-reserved-`），**未见**公开威胁哈希／攻击者 IP。防御：On-Prem 升固定版本并限制管理面；按 SA 审计日志；BOD 26-04 取证。**不转载利用步骤。**
  厂商 cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76504
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-76504

- **【newly_overdue · Apple CVE-2026-86950】** 昨 due_today（due **2026-10-02**）→ 今日 **newly_overdue**。CoreGraphics 越界写 → 任意代码执行；Apple 称针对性高精攻击。修复：**iOS/iPadOS 26.7.1**／**macOS Tahoe 26.7.1**／**macOS Sequoia 15.8.1**。防御：尽快更新；审慎处理不可信 PDF／字体；BOD 26-04。**未见公开 IoC。**
  Apple：https://support.apple.com/en-us/149226 · https://support.apple.com/en-us/149228 · https://support.apple.com/en-us/149229
  CISA Adds One（09-29）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog

- **【upcoming · Fortinet CVE-2026-104286 due 10-04】** 联邦 due **明天**。路径遍历＋NULL 字节 → 未认证任意文件写入；CVSS **9.8**。有厂商公开 IoC（FG-IR-26-175：7 哈希＋IP）。防御：升 fixed／临时禁 IBE／限管理面；比对哈希与 IP；BOD 26-04。
  厂商 FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175

- **【upcoming · Zammad CVE-2026-102489／102490 due 10-05】** 昨 NEW；due **10-05**。厂商称 102489 仅 ≤6.5 可利用、7.2.0 已加固；102490 细节待 DIVD。**未见公开 IoC。**
  CISA Adds Two（10-02）：https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog
  DIVD-2026-00015：https://csirt.divd.nl/cases/DIVD-2026-00015/

- **【仍逾期亮点 21】** newly_overdue 仅 Apple；still 仍 **21**（含 Citrix）。高信号：Citrix／Check Point／Arista／F5／JFrog／Zyxel／MS／Chromium／Pixel／ISE／Acronis／WSO2／Adobe／SharePoint／MikroTik／WP。防御：补丁落地＋取证；BOD 26-04。
  CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
  CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096

- **【工具／新闻】** **Sliver 升版 v1.7.7→v1.7.8**（发布约 2026-10-03T19:08:40Z）；nuclei **v3.11.1**／nuclei-templates **v10.4.9** **无升版**；Risky 仍 **RBNEWS618**／SRB185／BTN184；tl;dr 仍 **#348**。X B：Red-Team-Roadmap／PentestGPT；LWiS：passkeys.tools／BloodHound 采集指南。
  Sliver v1.7.8：https://github.com/BishopFox/sliver/releases/tag/v1.7.8
  Risky RBNEWS618：https://risky.biz/RBNEWS618/

- **【LWiS／APT 交叉】** Apple Developer 公告 macOS Full Disk Access 变更（@L0Psec）；Insinuator Entra Token Theft／CAE 系列（@DirectoryRanger）；RESIDENT.NGO 摩尔多瓦媒体／公民社会诱饵活动（@rst_cloud；报告提及 Seaborgium 语境——以原文为准）；C 源两条泄露声称——**一律 UNCONFIRMED**。
  Apple Developer：https://developer.apple.com/news/?id=p6zjo
  RESIDENT.NGO：https://resident.ngo/lab/writeups/malware-campaign-impersonates-european-donors-to-target-moldovan-media-and-civil-society/
  Insinuator CAE：https://insinuator.net/2026/09/token-theft-in-microsoft-entra-id-part-2-of-4-continuous-access-evaluation/

- **【合并统计】** X **12**（A0／B3／C3／LWiS6；数字 id **0**；cross **0**；prior **0**；**+0** NEW 数字 id；null_id **12** 未入 seen）；`logged_in=true`／`@seogoogle4`／`blocked=false`；覆盖 A~22h（无保留）／B~4–7h／C~0.7h／LWiS~1h；seen_ids **2326→2326**；报告 `/home/box/workspace/security-watch/reports/2026-10-03-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【due_today · 在野】Cisco Catalyst SD-WAN Manager CVE-2026-76504

CISA 于 **2026-09-30** 加入 KEV；联邦 due **2026-10-03＝今日**。URI hex 编码绕过 Web／API 认证 → 未认证管理员访问。厂商 SA 标题：Cisco Catalyst SD-WAN Manager API Authentication Bypass。防御：On-Prem 升固定版本并限制非受信访问；审计狩猎日志；按 BOD 26-04 取证。**不转载利用／walkthrough 步骤。**

地址：
- CISA Adds One（09-30）：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76504
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-76504
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- enrich IoC JSON：`/workspace/enrich-2026-10-03/cisco-CVE-2026-76504-iocs.json`

IoC（厂商 SA／enrich 狩猎级日志模式原样；**未见**独立恶意文件哈希或攻击者 C2 IP）：
- 日志：`/var/log/nms/containers/service-proxy/serviceproxy-access.log` — 审计含 URI 编码字符的 `j_security_check`（示例含 `%6a_security_check`）来自未知／未授权 IP
- 日志：`/var/log/nms/vmanage-server.log` — 审计 `j_security_check` 且用户名以 `viptela-reserved-` 开头的请求

### 2. 【newly_overdue · 在野】Apple Multiple Products CVE-2026-86950

CISA 于 **2026-09-29** 加入 KEV；联邦 due **2026-10-02** → 今日 **newly_overdue**。CoreGraphics 越界写 → 任意代码执行；Apple 称针对性高精攻击。补丁：**iOS/iPadOS 26.7.1**、**macOS Tahoe 26.7.1**、**macOS Sequoia 15.8.1**。防御：尽快更新；审慎处理不可信 PDF／字体文档；BOD 26-04。**不转载 PoC／payload。**

地址：
- CISA Adds One（09-29）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 Apple 149226：https://support.apple.com/en-us/149226
- 厂商 Apple 149228：https://support.apple.com/en-us/149228
- 厂商 Apple 149229：https://support.apple.com/en-us/149229
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-86950
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-86950
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- enrich IoC JSON：`/workspace/enrich-2026-10-03/apple-CVE-2026-86950-iocs.json`

IoC：未见公开 IoC。

### 3. 【upcoming · due 10-04】Fortinet FortiMail CVE-2026-104286

CISA 于 **2026-10-01** 加入 KEV；联邦 due **2026-10-04**。路径遍历＋ NULL 字节不当处理 → 未认证经 HTTP/HTTPS 任意文件写入；CVSS **9.8**。固定方向：**upcoming 8.0.2+／7.6.7+／7.4.9+**；7.2.x 迁 7.4 分支。临时：按 FG-IR-26-175 禁用 IBE 或限制管理面。防御：升固定版本；比对下列 IoC；审计 remote-ip／archive account／IBE／管理面异常；BOD 26-04。**不转载利用步骤。**

地址：
- CISA Adds One（10-01）：https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-104286
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-104286
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- enrich IoC JSON：`/workspace/enrich-2026-10-03/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`

IoC（厂商 FG-IR-26-175 原样）：
- IP：`79.141.169.187`／`45.129.0.192`
- `/data/lib/liblog.so` ADDED MD5 `64c90a00c7fda4d5c7973ed64c25783a` SHA256 `8015f34dc84922b03688399d7f9fe7a00361789f7e420c7e2a2cdb23e75cef84`
- `/bin/smit` MODIFIED MD5 `5241738a3e9988404239e12243f6d35b` SHA256 `77324ac428bde86d351fc5fc06f6d64a6bfe737dfb2743df1d4c5ac2418a5b6a`
- `/data/bin/webconsole` ADDED MD5 `ae0ea6502d3fa5f0664bceb73189eb54` SHA256 `7a6cea9f5c9e2e9994d4e3c4da73f86cf5acd05ea5d312c066c9d1dafd69ee38`
- `/data/bin/mailservice` ADDED MD5 `f90fa81a5f521d785f2b2f765e3ab897` SHA256 `4000276a150a165d3c2537d1e19fb393c4de8333076a16655e28059cae82157b`
- `/data/etc/httpd.conf` MODIFIED MD5 `61af1c4bce1c2eebc8ff689ca5337791` SHA256 `703e97c64e61e41dc3aaba580d82bb2aa7b6a11b54ee6fb467ed5d5a3bffdef5`
- `/data/etc/ld.so.preload` ADDED MD5 `8eb64f25d2a8e18e05aae058629473cf` SHA256 `8953ec7960b09f544a880b072ad4e6cfda7a8303f486251d3478dcfdfbac23b6`
- `/data/migadmin.tar.gz` MODIFIED MD5 `49a7156a7d043cc8f9f680579db22f86` SHA256 `d6fe51c22b91776f4c961ea58bcac5917f15d560a619d7ce726d3d51795609d3`

### 4. 【upcoming · due 10-05】Zammad CVE-2026-102489／CVE-2026-102490

CISA 于 **2026-10-02** 加入 KEV；联邦 due **2026-10-05**。**102489**：会话固定 → 以 zammad 用户远程代码执行，可与 102490 链式利用；厂商称 **仅 Zammad ≤6.5 可利用**（EOS），7.0+ 实际不可利用，**7.2.0 已加固**。**102490**：不当权限管理 → 本地 zammad→root；厂商称尚未从 DIVD 收到技术细节。DIVD-2026-00015。forensicTriage=Yes；knownRansomwareCampaignUse=Unknown。防御：按厂商 releases／社区声明升级或迁出受影响版本；限制管理与本地提权面；按 BOD 26-04 取证。**未见公开 IoC。不转载利用步骤。**

地址：
- CISA Adds Two（10-02）：https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 厂商 releases：https://zammad.com/en/product/releases/
- 厂商社区声明：https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297
- DIVD case：https://csirt.divd.nl/cases/DIVD-2026-00015/
- DIVD CVE-2026-102489：https://csirt.divd.nl/cves/CVE-2026-102489/
- DIVD CVE-2026-102490：https://csirt.divd.nl/cves/CVE-2026-102490/
- NVD 489：https://nvd.nist.gov/vuln/detail/CVE-2026-102489
- NVD 490：https://nvd.nist.gov/vuln/detail/CVE-2026-102490
- KEV 489：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-102489
- KEV 490：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-102490
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- enrich IoC JSON：`/workspace/enrich-2026-10-03/zammad-CVE-2026-102489-iocs.json` · `/workspace/enrich-2026-10-03/zammad-CVE-2026-102490-iocs.json`

IoC：未见公开 IoC。

### 5. 【仍逾期亮点 · Citrix 等 21】

仍逾期亮点 **21**（与昨相同集合；Apple 在 newly_overdue 未并入 still）。高信号含 Citrix NetScaler **88771／88772**、Check Point、Arista、F5、JFrog、Zyxel、MS、Chromium、Pixel、Cisco ISE、Acronis、WSO2、Adobe、SharePoint、MikroTik、WordPress。防御：按各厂商公告补丁＋BOD 26-04 取证；Citrix 社区页常 403，用 CTX 直链。

地址：
- CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
- CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
- buckets：`/workspace/_kev_buckets_2026-10-03.json`

IoC：见下文「地址／IoC 汇总」中仍逾期条目；无新公开威胁 IoC 则写未见。

### 6. 【KEV NEW】

本日 **无** KEV NEW（catalog 仍 2026.10.02／1733／Δ+0）。

本日无显著更新（就 NEW 而言）。

## 工具与 GitHub 发布

### 1. 【升版】BishopFox Sliver v1.7.8

相对昨 **v1.7.7** 升至 **v1.7.8**（GitHub release published **2026-10-03T19:08:40Z**）。防御／检测工程语境：关注自建 C2 与红队演练资产清单是否需同步标签。**不转载利用步骤。**

地址：
- 仓库 release：https://github.com/BishopFox/sliver/releases/tag/v1.7.8
- 仓库：https://github.com/BishopFox/sliver

IoC：未见公开 IoC。

### 2. 【无升版】nuclei／nuclei-templates

projectdiscovery/nuclei 仍 **v3.11.1**；nuclei-templates 仍 **v10.4.9**。

地址：
- nuclei：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9

IoC：未见公开 IoC。

### 3. 【X B／LWiS 交叉】红队／安全工程仓库与指南

X Search B（~4–7h；无 status_url）：@httpschuks 提 Red-Team-Roadmap（BloodHound／WriteDACL 实验路径——授权评估语境）；@DivyanshT91162 汇总含 PentestGPT；@CobaltHere 提 Claude Marketplace Cobalt 相关仓（卡片链 `github.com/echelong/cobal` 复核 **404**，不编造替代仓）。LWiS：@DirectoryRanger 分享 passkeys.tools（RUB-NDS）与 Black Hills BloodHound 采集指南（旧路径 404，改用现用 URL）。

地址：
- Red-Team-Roadmap：https://github.com/Dev-Chukwuma/Red-Team-Roadmap
- PentestGPT：https://github.com/GreyDGL/PentestGPT
- passkeys.tools（GitHub）：https://github.com/RUB-NDS/passkeys.tools
- Black Hills BloodHound 采集：https://www.blackhillsinfosec.com/bloodhound-data-collection/
- X 原帖：未见公开 status_url（虚拟列表未暴露；不编造）

IoC：未见公开 IoC。

### 4. 【新闻备援】Risky／tl;dr

Risky 仍最新 **RBNEWS618**（Authorities dismantle KillSec group，2026-10-02）；SRB **185**；BTN **184**（619／620／186／185=404）。tl;dr 仍 **#348**（349–351 soft-404）。

地址：
- Risky RBNEWS618：https://risky.biz/RBNEWS618/
- Risky SRB185：https://risky.biz/SRB185/
- Risky BTN184：https://risky.biz/BTN184/
- tl;dr #348：https://tldrsec.com/p/tldr-sec-348
- tools pulse：`/workspace/tools-news-pulse-2026-10-03.json`

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. 【报告】RESIDENT.NGO · 摩尔多瓦媒体／公民社会诱饵活动

X C：@rst_cloud 提及冒充欧洲捐助者的恶意软件活动，针对摩尔多瓦媒体与公民社会；公开报告见 RESIDENT.NGO Threat Lab（2026-09-09 至 09-25 窗口；诱饵含假会议／资助邀请、密码 ZIP／VHDX／LNK 等——仅记狩猎特征，**不转载利用步骤**）。帖文提及 Seaborgium 语境时以报告原文为准，勿自行强归因。

地址：
- 文章：https://resident.ngo/lab/writeups/malware-campaign-impersonates-european-donors-to-target-moldovan-media-and-civil-society/
- X 原帖：未见公开 status_url（@rst_cloud；不编造）

IoC：未见本报另行抄录的公开哈希／C2（以文章原文为准；无独立抄录则写未见公开 IoC）。未见公开 IoC。

### 2. 【LWiS】Entra ID Token Theft／CAE 与 Apple FDA

@DirectoryRanger 分享 Microsoft Entra ID Token Theft 威胁景观与 Continuous Access Evaluation 讨论（Insinuator 系列 Part 2）；@L0Psec 讨论 Apple macOS Full Disk Access 变更（Apple Developer 公告）。防御：启用／评估 CAE 与 Token Protection；审慎授予 FDA；结合条件访问与会话吊销预案。

地址：
- Insinuator CAE：https://insinuator.net/2026/09/token-theft-in-microsoft-entra-id-part-2-of-4-continuous-access-evaluation/
- Microsoft CAE 概念：https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation
- Apple Developer：https://developer.apple.com/news/?id=p6zjo
- X 原帖：未见公开 status_url（不编造）

IoC：未见公开 IoC。

### 3. 【UNCONFIRMED】地下泄露声称（C 源）

@intels_daily：声称 AKM69 提供归因于 Mitsubishi UFJ Financial Group 的约 130 万条记录——**UNCONFIRMED／未验证**。@CyberPulse56：声称威胁行为者「888」上传据称来自 Tata Consultancy Services 的数据——**UNCONFIRMED／未验证**。防御：勿采信未交叉验证的地下市场转述；以受害方／执法／可信 CERT 确认为准。

地址：
- X 原帖：未见公开 status_url（不编造）
- 无独立厂商／执法确认页

IoC：未见公开 IoC。

### 4. 【LWiS 其他】DCOM 横向移动说明／本地图片水印研究

@DirectoryRanger 分享 DCOM 横向移动技术说明（卡片域 `detect.fyi`，无完整文章路径则不编造）与 Microsoft Paint／Photos 本地图片嵌入服务器 GUID 隐形水印研究（卡片 `xusheng.dev`）。防御向阅读；**不转载攻击步骤。**

地址：
- 卡片域名（不完整路径，不编造）：https://detect.fyi · https://xusheng.dev
- X 原帖：未见公开 status_url

IoC：未见公开 IoC。

本日 ICS advisory：无单独新突出的 2026-10-03 ICS advisory 主条。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Fortinet FortiMail CVE-2026-104286（upcoming due 10-04）**：7 文件哈希（`/data/lib/liblog.so`、`/bin/smit`、`/data/bin/webconsole`、`/data/bin/mailservice`、`/data/etc/httpd.conf`、`/data/etc/ld.so.preload`、`/data/migadmin.tar.gz` 之 MD5／SHA256 见 CVE §3）＋ IP `79.141.169.187`／`45.129.0.192`。（来源：FG-IR-26-175／`/workspace/enrich-2026-10-03/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`）
- **Cisco SD-WAN CVE-2026-76504（due_today）**：狩猎日志 `/var/log/nms/containers/service-proxy/serviceproxy-access.log`（编码 `j_security_check`）；`/var/log/nms/vmanage-server.log`（`viptela-reserved-` 用户＋j_security_check）。**未见**独立恶意文件哈希／攻击者 C2 IP。（来源：cisco-sa-sdwan／enrich-2026-10-03）
- **Arista VeloCloud CVE-2026-93952（仍逾期）**：`/usr/local/sbin/.vcnode.js`；`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）；`/etc/systemd/system/vc-sysmon.service`；HTTP 头 `x-vc-opt`；IP `142.93.149.77`／`104.248.126.159`。（来源：SA-0183／既往 enrich）
- **Check Point 85102／93616（仍逾期）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`。（来源：既往报／厂商 SK／enrich）
- **Cisco ISE 76460（仍逾期）**：狩猎示例 `admin#show logging application ise-kong/access.log | include dummyuser`；路径 `./ise/logs/apigateway/access.log`。（来源：既往报／Cisco SA）
- **Citrix still（社交狩猎线索，非厂商正式 IoC）**：超级用户名 `sec_monitor`；WebShell 伪装 CSS——以现场取证为准。
- **Zammad upcoming 102489／102490／Apple newly_overdue 86950／仍逾期其余／工具仓／C 泄露声称**：未见可抄录公开 IoC（或仅厂商原文内；C 帖多为数量转述且 **UNCONFIRMED**）
- 默认无指标条目：写「未见公开 IoC」。

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

本窗口 LWiS List 只读采集：扫描约 **9** 条、保留 **6** 条、覆盖约 **19 分钟–1h**（`logged_in=true`／`@seogoogle4`／`blocked=false`；成员数未显示）；跨源 ID 重叠 0；**6** 条均 `id/status_url=null`（@L0Psec FDA、@DirectoryRanger×5：Entra／passkeys／BloodHound／水印／DCOM）；有文章链的含 Apple Developer、passkeys.tools、Black Hills、detect.fyi、xusheng.dev；meta：`/workspace/x-posts-2026-10-03-lwis-list.json` · `/workspace/x-lwis-list-meta-2026-10-03.json`。

## 来源搜索 URL

- X Latest A（CVE／POC／exploit／0day）：https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／cobalt）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt)&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS618：https://risky.biz/RBNEWS618/
- Risky SRB185：https://risky.biz/SRB185/
- Risky BTN184：https://risky.biz/BTN184/
- tl;dr sec：https://tldrsec.com/
- tl;dr #348：https://tldrsec.com/p/tldr-sec-348
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 10-02 Adds Two（Zammad 102489／102490）：https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 10-01 Adds One（Fortinet 104286）：https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-30 Adds One（Cisco 76504）：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-29 Adds One（Apple 86950）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-27 Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- 厂商 Cisco SD-WAN：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
- 厂商 Fortinet FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- 厂商 Zammad releases：https://zammad.com/en/product/releases/
- 厂商 Zammad 社区：https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297
- DIVD-2026-00015：https://csirt.divd.nl/cases/DIVD-2026-00015/
- Apple 149226／149228／149229：https://support.apple.com/en-us/149226 · https://support.apple.com/en-us/149228 · https://support.apple.com/en-us/149229
- Apple Developer FDA：https://developer.apple.com/news/?id=p6zjo
- RESIDENT.NGO Moldova：https://resident.ngo/lab/writeups/malware-campaign-impersonates-european-donors-to-target-moldovan-media-and-civil-society/
- Insinuator Entra CAE：https://insinuator.net/2026/09/token-theft-in-microsoft-entra-id-part-2-of-4-continuous-access-evaluation/
- Sliver v1.7.8：https://github.com/BishopFox/sliver/releases/tag/v1.7.8
- Red-Team-Roadmap：https://github.com/Dev-Chukwuma/Red-Team-Roadmap
- PentestGPT：https://github.com/GreyDGL/PentestGPT
- passkeys.tools：https://github.com/RUB-NDS/passkeys.tools
- Black Hills BloodHound：https://www.blackhillsinfosec.com/bloodhound-data-collection/
