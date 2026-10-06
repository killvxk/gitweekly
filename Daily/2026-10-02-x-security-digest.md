# X 安全情报晚报 · 2026-10-02

> 搜集窗口：圣地亚哥时间 **2026-10-01 20:00 至 2026-10-02 ~20:35**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-10-02.json`（collected_at **2026-10-02T20:20:00-03:00**）＋ `/workspace/tools-news-pulse-2026-10-02.json`＋ `/workspace/enrich-2026-10-02/`＋ buckets `/workspace/_kev_buckets_2026-10-02.json`。CISA KEV catalogVersion **2026.10.02**／**1733** 条／dateReleased **2026-10-02T15:19:38.2945Z**（约合当地 12:19 CLST；相对昨日基线 **2026.10.01／1731**：**count Δ+2**；**NEW Zammad CVE-2026-102489／CVE-2026-102490**；今日 CISA「Adds Two」：https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog ）。**due_today：Apple CVE-2026-86950**；**newly_overdue 空**（Citrix 88771／88772 昨 newly_overdue → **今日并入 still**）；**仍逾期亮点 21**（昨 19＋Citrix 2）；**upcoming** 10-03 Cisco **76504**、10-04 Fortinet **104286**、10-05 Zammad **102489／102490**。
> **仍逾期**：**Citrix CVE-2026-88771／88772**（昨 newly_overdue 并入）、**Check Point CVE-2026-85102／93616**、**Arista VeloCloud CVE-2026-93952**、**F5 BIG-IP APM CVE-2026-94127**、**JFrog Artifactory CVE-2026-42016／42018**、**Zyxel CVE-2026-7273**、**MS CVE-2026-81963／85880**、**Chromium CVE-2026-87491／85046**、**Pixel CVE-2026-58704**、**Cisco ISE CVE-2026-76460**、**Acronis CVE-2026-87886**、**WSO2 CVE-2026-5430**、**Adobe CVE-2026-71362**、**SharePoint CVE-2026-65660**、**MikroTik CVE-2026-67279**、**WordPress CVE-2026-87902**。**newly_overdue：空**。**即将 due 10-03**：**Cisco CVE-2026-76504**。**即将 due 10-04**：**Fortinet CVE-2026-104286**。**即将 due 10-05**：**Zammad CVE-2026-102489／102490**。
> X：`/workspace/x-posts-2026-10-02.json`（合并 **27** 条：A8／B3／C4／LWiS12；唯一数字 id **18**；跨源 ID 重叠 **0**；相对 prior seen_ids 重叠 **0**／**+18** 新 id；LWiS **9** 条 `id/status_url=null` **未计入** seen_ids；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.5h**。Search B 可见约 **13h**。Search C 约 **1h**。LWiS List 约 **24h**（扫描约 **63**／保留 **12**；成员约 **501**；**交叉校验，不假装为本窗口 24h Latest**；虚拟列表未暴露部分帖 status 链接——报告写作者+摘要+已有文章链接，**不编造 URL**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。抓取备注：Citrix 社区公告常 **403**（用 CTX 直链）；CISA `/news-events/alerts` 索引常 **404**（今日 Adds Two 直链 200）；RBNEWS619／SRB186／BTN185 **404**；tl;dr #349／#350 软 404；Zammad／Apple／DIVD enrich **未见公开 IoC**；Fortinet upcoming 沿用昨 FG-IR IoC。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露／勒索声称一律标 **UNCONFIRMED／未验证**；仅写谁／打什么／补丁与狩猎级防御摘要。

## 今日摘要

- **【主条 · KEV NEW · Zammad CVE-2026-102489／102490】** CISA 于 **2026-10-02** 将两 CVE 加入 KEV（catalog **2026.10.02／1733／Δ+2**）；联邦 due **2026-10-05**；forensicTriage=Yes；ransomware 使用 Unknown。**102489**：会话固定（CWE-384）→可致以 zammad 用户 RCE，可与 102490 链式利用。**102490**：不当权限管理（CWE-269）→本地 zammad→root 提权。厂商社区声明：102489 **仅 ≤6.5 可利用**（EOS），7.0+ 实际不可利用，**7.2.0 已加固**；102490 称尚未从 DIVD 获技术细节、暂无法核实范围。DIVD-2026-00015。防御：按厂商 releases／社区指引升级或迁出版本；限制管理面；BOD 26-04 取证。**未见公开 IoC。不转载利用步骤。**
  CISA Adds Two：https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog
  厂商 releases：https://zammad.com/en/product/releases/
  厂商社区：https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297
  DIVD case：https://csirt.divd.nl/cases/DIVD-2026-00015/
  DIVD CVE 489：https://csirt.divd.nl/cves/CVE-2026-102489/
  DIVD CVE 490：https://csirt.divd.nl/cves/CVE-2026-102490/

- **【due_today · Apple CVE-2026-86950】** KEV 自 09-29；due **2026-10-02＝今日**。CoreGraphics 越界写 → 任意代码执行；Apple 称针对性高精攻击。修复：**iOS/iPadOS 26.7.1**／**macOS Tahoe 26.7.1**／**macOS Sequoia 15.8.1**。防御：尽快更新受影响设备；审慎处理不可信 PDF／字体；BOD 26-04。**未见公开 IoC。不转载 PoC。**
  CISA Adds One（09-29）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
  Apple：https://support.apple.com/en-us/149226 · https://support.apple.com/en-us/149228 · https://support.apple.com/en-us/149229

- **【upcoming · Cisco CVE-2026-76504 due 10-03】** 联邦 due **明天**。X A：@jfernandogg／@LandscapeThreat 提醒积极利用与认证绕过、无 workaround。防御：On-Prem 升固定版本并限制管理面；狩猎编码 `j_security_check`／`viptela-reserved-`；BOD 26-04。
  厂商 cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
  X（jfernandogg）：https://x.com/jfernandogg/status/2106157280945443035
  X（LandscapeThreat）：https://x.com/LandscapeThreat/status/2106154768636805356

- **【upcoming · Fortinet CVE-2026-104286 due 10-04】** 昨 NEW 入 KEV；X A：@SOCMinute 提醒无凭据写文件风险。有厂商公开 IoC（FG-IR-26-175：7 哈希＋IP）。防御：升 fixed／临时禁 IBE／限管理面；比对哈希与 IP；BOD 26-04。
  厂商 FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
  X（SOCMinute）：https://x.com/SOCMinute/status/2106160928437719048

- **【仍逾期亮点 21】** newly_overdue 空；Citrix 88771／88772 **并入 still**（昨 19＋2＝21）。高信号：Citrix／Check Point／Arista／F5／JFrog／Zyxel／MS／Chromium／Pixel／ISE／Acronis／WSO2／Adobe／SharePoint／MikroTik／WP。LWiS：@CISAgov 更新 Citrix 活跃利用告警并新增 SIGMA（无 status_url，见文章／go.dhs 短链）；@POPPLEGAARD 报告持久化工具迹象。防御：补丁落地＋取证；BOD 26-04。
  CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
  CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
  CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html

- **【X A 交叉 · WP Statistics 97652／SharePoint 缓解脚本／geopy ReDoS】** @mgn_jpn：WP Statistics **CVE-2026-97652**（CVSS 6.1；修正 **14.16.15**）；@ubitquity_io：SharePoint Warlock／Storm-2603 防御缓解脚本（提及 BYOVD CVE-2025-1055——仅缓解语境）；@dailycve：geopy ReDoS 提示。防御：升插件；按厂商／环境评估部署缓解；**不转载利用步骤**。
  X（mgn_jpn）：https://x.com/mgn_jpn/status/2106160799290913107
  文章：https://shindan.m-g-n.me
  X（ubitquity_io）：https://x.com/ubitquity_io/status/2106160397866737842

- **【工具／新闻】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** **无升版**；Risky **新 RBNEWS618**（Authorities dismantle KillSec group，2026-10-02）；SRB 仍 **185**／BTN 仍 **184**；tl;dr 仍 **#348**。X B（~13h）：AI-FILE、LazyOwn、Red-Team-Roadmap（授权评估／检测工程语境）。
  Risky RBNEWS618：https://risky.biz/RBNEWS618/
  AI-FILE：https://github.com/kyle41111/AI-FILE
  LazyOwn：https://github.com/grisuno/LazyOwn
  Red-Team-Roadmap：https://github.com/Dev-Chukwuma/Red-Team-Roadmap

- **【LWiS／APT 交叉】** Apple 收紧 macOS Full Disk Access（TechCrunch／Bloomberg；关联 ChatGPT **CVE-2026-100754** 研究）；apple-cve.com 公告索引；Better Auth CVSS 9.1 授权绕过（1.7.7 已修，无 status_url）；C 源四条泄露声称——**一律 UNCONFIRMED**。
  TechCrunch：https://techcrunch.com/2026/10/02/apple-tightens-mac-data-controls/
  Bloomberg：https://www.bloomberg.com/news/articles/2026-10-02/apple-to-tighten-mac-data-controls
  apple-cve.com：https://apple-cve.com
  X（objective_see）：https://x.com/objective_see/status/2106160270603100238

- **【合并统计】** X **27**（A8／B3／C4／LWiS12；数字 id **18**；cross **0**；prior **0**；**+18** NEW；LWiS null_id **9** 未入 seen）；`logged_in=true`／`@seogoogle4`／`blocked=false`；覆盖 A~0.5h／B~13h／C~1h／LWiS~24h；seen_ids **2308→2326**；报告 `/home/box/workspace/security-watch/reports/2026-10-02-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【KEV NEW · due 10-05】Zammad CVE-2026-102489／CVE-2026-102490

CISA 于 **2026-10-02** 加入 KEV；联邦 due **2026-10-05**。**102489**：会话固定 → 以 zammad 用户远程代码执行，可与 102490 链式利用；厂商称 **仅 Zammad ≤6.5 可利用**（EOS），7.0+ 实际不可利用，**7.2.0 已加固**。**102490**：不当权限管理 → 本地 zammad→root；厂商称尚未从 DIVD 收到技术细节、暂无法核实范围；第三方称活跃利用。DIVD-2026-00015。forensicTriage=Yes；knownRansomwareCampaignUse=Unknown。防御：按厂商 releases／社区声明升级或迁出受影响版本；限制管理与本地提权面；按 BOD 26-04 取证。**未见公开 IoC。不转载利用步骤。**

地址：
- CISA Adds Two：https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog
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
- enrich IoC JSON：`/workspace/enrich-2026-10-02/zammad-CVE-2026-102489-iocs.json` · `/workspace/enrich-2026-10-02/zammad-CVE-2026-102490-iocs.json`

IoC：未见公开 IoC。

### 2. 【due_today · 在野】Apple Multiple Products CVE-2026-86950

CISA 于 **2026-09-29** 加入 KEV；联邦 due **2026-10-02＝今日**。CoreGraphics 越界写 → 任意代码执行；Apple 称针对性高精攻击。补丁：**iOS/iPadOS 26.7.1**、**macOS Tahoe 26.7.1**、**macOS Sequoia 15.8.1**。防御：尽快更新；审慎处理不可信 PDF／字体文档；BOD 26-04。**不转载 PoC／payload。**

地址：
- CISA Adds One（09-29）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 Apple 149226：https://support.apple.com/en-us/149226
- 厂商 Apple 149228：https://support.apple.com/en-us/149228
- 厂商 Apple 149229：https://support.apple.com/en-us/149229
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-86950
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-86950
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- enrich IoC JSON：`/workspace/enrich-2026-10-02/apple-CVE-2026-86950-iocs.json`

IoC：未见公开 IoC。

### 3. 【upcoming · due 10-03】Cisco Catalyst SD-WAN Manager CVE-2026-76504

CISA 于 **2026-09-30** 加入 KEV；联邦 due **2026-10-03**。URI hex 编码绕过 Web／API 认证 → 未认证管理员访问。X A：@jfernandogg 提醒 due 临近且无 workaround；@LandscapeThreat 称积极利用可致认证绕过。防御：On-Prem 升固定版本并限制非受信访问；审计狩猎日志；BOD 26-04。**不转载利用／walkthrough 步骤。**

地址：
- CISA Adds One（09-30）：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76504
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-76504
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- X（jfernandogg）：https://x.com/jfernandogg/status/2106157280945443035
- X（LandscapeThreat）：https://x.com/LandscapeThreat/status/2106154768636805356

IoC（厂商 SA／昨 enrich 狩猎级日志模式原样；**未见**独立恶意文件哈希或攻击者 C2 IP）：
- 日志：`/var/log/nms/containers/service-proxy/serviceproxy-access.log` — 审计含 URI 编码字符的 `j_security_check` 来自未知／未授权 IP
- 日志：`/var/log/nms/vmanage-server.log` — 审计 `j_security_check` 且用户名以 `viptela-reserved-` 开头的请求

### 4. 【upcoming · due 10-04】Fortinet FortiMail CVE-2026-104286

CISA 于 **2026-10-01** 加入 KEV；联邦 due **2026-10-04**。路径遍历＋ NULL 字节不当处理 → 未认证经 HTTP/HTTPS 任意文件写入；CVSS **9.8**。固定方向：**upcoming 8.0.2+／7.6.7+／7.4.9+**；7.2.x 迁 7.4 分支。临时：按 FG-IR-26-175 禁用 IBE 或限制管理面。X A：@SOCMinute。防御：升固定版本；比对下列 IoC；审计 remote-ip／archive account／IBE／管理面异常；BOD 26-04。**不转载利用步骤。**

地址：
- CISA Adds One（10-01）：https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-104286
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-104286
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- enrich IoC JSON（昨，仍适用）：`/workspace/enrich-2026-10-01/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`
- X（SOCMinute）：https://x.com/SOCMinute/status/2106160928437719048

IoC（厂商 FG-IR-26-175／昨 enrich **原样抄录**，非穷尽）：
- 文件：`/data/lib/liblog.so` — MD5 `64c90a00c7fda4d5c7973ed64c25783a` · SHA256 `8015f34dc84922b03688399d7f9fe7a00361789f7e420c7e2a2cdb23e75cef84`（ADDED）
- 文件：`/bin/smit` — MD5 `5241738a3e9988404239e12243f6d35b` · SHA256 `77324ac428bde86d351fc5fc06f6d64a6bfe737dfb2743df1d4c5ac2418a5b6a`（MODIFIED）
- 文件：`/data/bin/webconsole` — MD5 `ae0ea6502d3fa5f0664bceb73189eb54` · SHA256 `7a6cea9f5c9e2e9994d4e3c4da73f86cf5acd05ea5d312c066c9d1dafd69ee38`（ADDED）
- 文件：`/data/bin/mailservice` — MD5 `f90fa81a5f521d785f2b2f765e3ab897` · SHA256 `4000276a150a165d3c2537d1e19fb393c4de8333076a16655e28059cae82157b`（ADDED）
- 文件：`/data/etc/httpd.conf` — MD5 `61af1c4bce1c2eebc8ff689ca5337791` · SHA256 `703e97c64e61e41dc3aaba580d82bb2aa7b6a11b54ee6fb467ed5d5a3bffdef5`（MODIFIED）
- 文件：`/data/etc/ld.so.preload` — MD5 `8eb64f25d2a8e18e05aae058629473cf` · SHA256 `8953ec7960b09f544a880b072ad4e6cfda7a8303f486251d3478dcfdfbac23b6`（ADDED）
- 文件：`/data/migadmin.tar.gz` — MD5 `49a7156a7d043cc8f9f680579db22f86` · SHA256 `d6fe51c22b91776f4c961ea58bcac5917f15d560a619d7ce726d3d51795609d3`（MODIFIED）
- IP：`79.141.169.187`
- IP：`45.129.0.192`

### 5. 【仍逾期 · 昨 newly_overdue 并入】Citrix NetScaler CVE-2026-88771／CVE-2026-88772

CISA 于 **2026-09-27** 加入 KEV；联邦 due **2026-09-30**；昨 newly_overdue，**今日并入 still_overdue_highlights（21）**。88771：未认证命令执行。88772：内存边界不当 → RCE/DoS。同族 CTX697096 覆盖 **88771–88778**。LWiS：@CISAgov 更新活跃利用告警并新增 SIGMA 检测规则（**无 status_url**，有 go.dhs 短链）；@POPPLEGAARD 报告持久化攻击工具与环境迹象（**无 status_url**，有 GitHub 组织链）。防御：立即按 CTX 升 ADC/Gateway；按 CTX694799 疑似沦陷排查；狩猎异常超级用户与伪装静态资源；BOD 26-04。

地址：
- CISA Adds Two（09-27）：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- 厂商 CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
- 厂商 CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
- Community bulletin：https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778
- NVD 88771：https://nvd.nist.gov/vuln/detail/CVE-2026-88771
- NVD 88772：https://nvd.nist.gov/vuln/detail/CVE-2026-88772
- KEV 88771：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88771
- KEV 88772：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88772
- LWiS 文章短链（@CISAgov，无 status_url）：https://go.dhs.gov/5aH
- LWiS 仓库组织（@POPPLEGAARD，无 status_url）：https://github.com/ThomasPopplegaard
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开哈希／C2 IP（社交狩猎线索如超级用户名 `sec_monitor`、WebShell 伪装 CSS——以现场取证为准，非厂商正式 IoC 清单）。

### 6. 【仍逾期 · 在野】Check Point CVE-2026-85102／CVE-2026-93616

due 曾=09-25，继续 overdue。85102：VPN 不当证书校验。93616：管理面路径穿越。防御：按 SK 打 Jumbo／Hotfix；限制管理／VPN 面；证书 subject 狩猎；BOD 26-04。

地址：
- 厂商 SK85102：https://support.checkpoint.com/results/sk/sk1000117
- 厂商 SK93616：https://support.checkpoint.com/results/sk/sk1000171/
- Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
- NVD 85102：https://nvd.nist.gov/vuln/detail/CVE-2026-85102
- NVD 93616：https://nvd.nist.gov/vuln/detail/CVE-2026-93616
- KEV 85102：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85102
- KEV 93616：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-93616

IoC（厂商 SK／博客观测 cert_subject，原样带自昨报／enrich；非穷尽）：
- `CN=vpn,OU=users,O=global`
- `CN=vpn-user,OU=users,O=global`
- `CN=vpnuser,OU=users,O=global`

### 7. 【仍逾期 · 在野】Arista VeloCloud CVE-2026-93952

due 曾=09-25，继续 overdue。on-prem VCO 不当输入校验（在野）。修复示例：**VCO 5.2.3.16+／6.4.2.8+**。防御：升 on-prem VCO；限制 VCO Web 至可信管理网；按 SA-0183 狩猎；BOD 26-04。

地址：
- 厂商 SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-93952
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-93952

IoC（厂商 SA-0183／昨 enrich 原样，非穷尽）：
- 文件：`/usr/local/sbin/.vcnode.js`
- 文件：`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）
- 文件：`/etc/systemd/system/vc-sysmon.service`
- HTTP 头：`x-vc-opt`
- IP：`142.93.149.77`
- IP：`104.248.126.159`

### 8. 【仍逾期 · 合辑】F5／JFrog／Zyxel／MS／Chromium／Pixel／ISE／Acronis／WSO2／Adobe／SharePoint／MikroTik／WP

- **F5 BIG-IP APM CVE-2026-94127**（due 曾=09-25）：按 K000162605。https://my.f5.com/manage/s/article/K000162605 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94127
- **JFrog Artifactory CVE-2026-42016／42018**（due 曾=09-25）：按厂商 advisories。https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- **Zyxel GS1900 CVE-2026-7273**（due 曾=09-24）：升固件并限制 LAN 管理面。https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
- **MS CVE-2026-81963／85880**（due 曾=09-22）：确认九月补丁。https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963 · https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880
- **Chromium CVE-2026-87491／85046**：升 Chromium 系。https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html · https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- **Pixel CVE-2026-58704**：装 Pixel 安全更新。https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- **Cisco ISE CVE-2026-76460**：升 First Fixed。https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- **Acronis CVE-2026-87886**：按 SEC-10986。https://security-advisory.acronis.com/advisories/SEC-10986
- **WSO2 CVE-2026-5430**：按 WSO2-2026-5328。https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
- **Adobe CVE-2026-71362**：按 APSB26-92（helpx 常 **403**）。https://helpx.adobe.com/security/products/magento/apsb26-92.html
- **SharePoint CVE-2026-65660**：MSRC。https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660 · X A 交叉缓解脚本：https://x.com/ubitquity_io/status/2106160397866737842
- **MikroTik CVE-2026-67279**：https://mikrotik.com/supportsec/september-2026-vulnerability/
- **WordPress Core CVE-2026-87902**：GHSA。https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87902

除 ISE／Arista／Check Point／Fortinet upcoming 外，上列多数 **未见公开 IoC**。

### 9. 【X A】WP Statistics CVE-2026-97652／geopy ReDoS／Intel Downfall 回顾／CVE 趋势

- **WP Statistics CVE-2026-97652**（@mgn_jpn）：CVSS 6.1；项目已发 **14.16.15** 修正版，建议升级。X：https://x.com/mgn_jpn/status/2106160799290913107 · 文章：https://shindan.m-g-n.me
- **geopy ReDoS**（@dailycve）：页面未提供 CVE 编号；关注上游修复／升级。X：https://x.com/dailycve/status/2106161508665176274 · 站点：https://dailycve.com
- **Intel Downfall CVE-2022-40982**（@MariaNoble5408）：第六至十一代 Core 信息泄露回顾；防御：Intel 微码／平台补丁。X：https://x.com/MariaNoble5408/status/2106158251679285622
- **CVE 数量／评分／Debian 13 内核修复趋势**（@securethebits）：补丁优先级与资产盘点。X：https://x.com/securethebits/status/2106157695728566595

防御：升 WP Statistics 至修正版；评估 geopy 依赖；历史微码／平台补丁核验。**不转载利用步骤。**

IoC：未见公开 IoC。

### 10. 【LWiS】Better Auth／Apple FDA 收紧／ChatGPT CVE-2026-100754

- **Better Auth**（@v12sec，**无 status_url／id**）：认证库 CVSS **9.1** 授权绕过；**1.7.7** 已修复。防御：依赖方尽快升 **1.7.7+**。
- **Apple 收紧 macOS Full Disk Access**（@objective_see）：关联 ChatGPT **CVE-2026-100754** 研究，提示 AI 代理数据访问风险。X：https://x.com/objective_see/status/2106160270603100238 · TechCrunch：https://techcrunch.com/2026/10/02/apple-tightens-mac-data-controls/
- **Apple FDA／MDM／PPPC 影响**（@ClassicII_MrMac）：X：https://x.com/ClassicII_MrMac/status/2106141231004942412
- **Bloomberg 同题**（@SwiftOnSecurity 转发，**无 status_url**）：https://www.bloomberg.com/news/articles/2026-10-02/apple-to-tighten-mac-data-controls
- **apple-cve.com 公告索引**（@theevilbit）：https://apple-cve.com · X：https://x.com/theevilbit/status/2105978027842671096

防御：关注 macOS FDA／MDM 策略变更对安全工具与 AI 代理的影响；升 Better Auth。

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 核心工具版本（公开 pulse）

- **Sliver** 仍 **v1.7.7**（无升版）：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- **nuclei** 仍 **v3.11.1**（无升版）：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- **nuclei-templates** 仍 **v10.4.9**（无升版）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- Risky **新**：**RBNEWS618** https://risky.biz/RBNEWS618/（Authorities dismantle KillSec group，2026-10-02）· **SRB185** https://risky.biz/SRB185/ · **BTN184** https://risky.biz/BTN184/ · RBNEWS619／SRB186／BTN185＝**404**
- tl;dr sec 仍 **#348** https://tldrsec.com/p/tldr-sec-348（#349／#350 软 404；首页仍列 #348 为最新）

### X Search B（~13h；授权红队／模拟／检测工程向；不写利用步骤）

- **AI-FILE**（Mythic C2 listener profile；经 OpenAI Files API 交换 implant 消息；授权评估／检测工程）：https://github.com/kyle41111/AI-FILE · X：https://x.com/ipurple/status/2106072255931498924
- **LazyOwn**（RedTeam／APT Framework；AI agents／Linux BOF beacon／YARA+Nuclei marketplace）：https://github.com/grisuno/LazyOwn · X：https://x.com/zapstiko/status/2105988015780966707
- **Red-Team-Roadmap**（Kerberos 基础／授权实验室学习路线）：https://github.com/Dev-Chukwuma/Red-Team-Roadmap · X：https://x.com/httpschuks/status/2105956476749488548

### LWiS 交叉工具／研究（~24h）

- **Rust 安全审查／性能／调试**（@evilsocket，**无 status_url**）：工程实践推荐（无独立仓库链）。
- **安全研究训练思路**（@LiveOverflow，**无 status_url**）：动手分析。
- **List 时间线交叉样本**（@badsectorlabs，**无 status_url**）。
- **CISA 网络基础设施安全更新**（@CISAgov，**无 status_url**）：https://www.cisa.gov

IoC：工具帖未见公开 IoC。

## APT / Malware 分析

### 1. 【Risky】KillSec 团伙瓦解报道

Risky Business **RBNEWS618**（2026-10-02）：当局瓦解 KillSec 团伙。防御：关注相关 TTPs 基线与历史受害者通报交叉核验。

地址：
- Risky RBNEWS618：https://risky.biz/RBNEWS618/

IoC：未见公开 IoC（播客／新闻摘要级）。

### 2. 【X C · 未验证】地下泄露／售卖声称（合辑）

以下均为社交列表报道，**一律 UNCONFIRMED／未验证**：

- **AntichatNews／Pentagon ~300 万条记录**声称：https://x.com/intels_daily/status/2106159080439992486
- **Nameless511／摩洛哥住房部门 ~26,452 条**售卖声称：https://x.com/CyberPulse56/status/2106155642100879370
- **Ballalaika／Instagram API 抓取 ~1,700 万行**数据集声称：https://x.com/CyberPulse56/status/2106154660587569420
- **Ballalaika／法国 Urssaf Pajemploi** 数据库声称：https://x.com/CyberPulse56/status/2106154077923205499

IoC：未见可核验公开 IoC（仅帖文数量／部门转述，不作确认）。

### 3. ICS

本日公开备援主条以 **KEV NEW Zammad**、**due_today Apple**、**仍逾期网关／编排／APM／VPN（含 Citrix 并入）** 与 **upcoming Cisco／Fortinet／Zammad** 为主；**无单独新突出的 2026-10-02 ICS advisory 主条**。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Fortinet FortiMail CVE-2026-104286（upcoming due 10-04）**：7 文件哈希（`/data/lib/liblog.so`、`/bin/smit`、`/data/bin/webconsole`、`/data/bin/mailservice`、`/data/etc/httpd.conf`、`/data/etc/ld.so.preload`、`/data/migadmin.tar.gz` 之 MD5／SHA256 见 CVE §4）＋ IP `79.141.169.187`／`45.129.0.192`。（来源：FG-IR-26-175／`/workspace/enrich-2026-10-01/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`）
- **Cisco SD-WAN CVE-2026-76504（upcoming due 10-03）**：狩猎日志 `/var/log/nms/containers/service-proxy/serviceproxy-access.log`（编码 `j_security_check`）；`/var/log/nms/vmanage-server.log`（`viptela-reserved-` 用户＋j_security_check）。**未见**独立恶意文件哈希／攻击者 C2 IP。（来源：cisco-sa-sdwan／昨 enrich）
- **Arista VeloCloud CVE-2026-93952（仍逾期）**：`/usr/local/sbin/.vcnode.js`；`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）；`/etc/systemd/system/vc-sysmon.service`；HTTP 头 `x-vc-opt`；IP `142.93.149.77`／`104.248.126.159`。（来源：SA-0183／昨 enrich）
- **Check Point 85102／93616（仍逾期）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`。（来源：昨报／厂商 SK／enrich）
- **Cisco ISE 76460（仍逾期）**：狩猎示例 `admin#show logging application ise-kong/access.log | include dummyuser`；路径 `./ise/logs/apigateway/access.log`。（来源：昨报／Cisco SA）
- **Citrix still（社交狩猎线索，非厂商正式 IoC）**：超级用户名 `sec_monitor`；WebShell 伪装 CSS——以现场取证为准。
- **Zammad NEW 102489／102490／Apple due_today 86950／仍逾期其余／工具仓／C 泄露声称**：未见可抄录公开 IoC（或仅厂商原文内；C 帖多为数量转述且 **UNCONFIRMED**）
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

本窗口 LWiS List 只读采集：扫描约 **63** 条、保留 **12** 条、覆盖约 **24h**（`logged_in=true`／`@seogoogle4`／`blocked=false`；成员约 **501**）；跨源 ID 重叠 0（相对 A／B／C）；**9** 条 `id/status_url=null`（@v12sec Better Auth、@CISAgov Citrix SIGMA／基建更新、@POPPLEGAARD 持久化工具、@SwiftOnSecurity Bloomberg、@evilsocket Rust、@LiveOverflow、@theevilbit 交叉、@badsectorlabs）；有 id 的含 @theevilbit apple-cve.com、@objective_see Apple FDA／ChatGPT CVE-2026-100754、@ClassicII_MrMac FDA／MDM；meta：`/workspace/x-posts-2026-10-02-lwis-list.json`。

## 来源搜索 URL

- X Latest A（CVE／0-day）：https://x.com/search?q=%28CVE%20OR%20%220-day%22%20OR%200day%29%20-filter%3Areplies&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／cobalt／implant／threat hunting）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20%22red-team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt%20OR%20implant%20OR%20%22threat%20hunting%22)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS618：https://risky.biz/RBNEWS618/
- Risky SRB185：https://risky.biz/SRB185/
- Risky BTN184：https://risky.biz/BTN184/
- Risky RBNEWS617：https://risky.biz/RBNEWS617/
- tl;dr sec：https://tldrsec.com/
- tl;dr #348：https://tldrsec.com/p/tldr-sec-348
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 10-02 Adds Two（Zammad 102489／102490）：https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 10-01 Adds One（Fortinet 104286）：https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-30 Adds One（Cisco 76504）：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-29 Adds One（Apple 86950）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-27 Adds Two（Citrix 88771／88772）：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 09-27 Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- 厂商 Zammad releases：https://zammad.com/en/product/releases/
- 厂商 Zammad 社区：https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297
- DIVD-2026-00015：https://csirt.divd.nl/cases/DIVD-2026-00015/
- 厂商 Fortinet FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- 厂商 Cisco SD-WAN：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
- Apple 149226／149228／149229：https://support.apple.com/en-us/149226 · https://support.apple.com/en-us/149228 · https://support.apple.com/en-us/149229
- TechCrunch Apple FDA：https://techcrunch.com/2026/10/02/apple-tightens-mac-data-controls/
- Bloomberg Apple FDA：https://www.bloomberg.com/news/articles/2026-10-02/apple-to-tighten-mac-data-controls
- apple-cve.com：https://apple-cve.com
- AI-FILE：https://github.com/kyle41111/AI-FILE
- LazyOwn：https://github.com/grisuno/LazyOwn
- Red-Team-Roadmap：https://github.com/Dev-Chukwuma/Red-Team-Roadmap
