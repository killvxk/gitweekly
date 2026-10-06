# X 安全情报晚报 · 2026-10-04

> 搜集窗口：圣地亚哥时间 **2026-10-03 20:00 至 2026-10-04 ~20:20**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-10-04.json`（collected_at **2026-10-04T20:20:00-03:00**）＋ `/workspace/tools-news-pulse-2026-10-04.json`＋ `/workspace/enrich-2026-10-04/`＋ buckets `/workspace/_kev_buckets_2026-10-04.json`。CISA KEV catalogVersion **2026.10.04**／**1734** 条／dateReleased **2026-10-04T18:52:56Z（＝15:52 UTC-3）**（相对昨日基线 **2026.10.02／1733**：**count Δ+1**；无 removed；既有条目无字段变化）。**NEW：Citrix CVE-2026-88779**（due **10-07**；CISA 2026/10/04 Adds One 页 200）。**due_today：Fortinet CVE-2026-104286**；**newly_overdue：Cisco CVE-2026-76504**（昨 due_today）；**仍逾期亮点 22**（昨 21＋Apple 86950；含 Citrix 88771／88772；全库逾期≈1729）；**upcoming** 10-05 Zammad **102489／102490**（明天）、10-07 Citrix **88779**。
> **仍逾期**：Citrix **88771／88772**、Apple **86950**、Check Point **85102／93616**、Arista VeloCloud **93952**、F5 BIG-IP APM **94127**、JFrog Artifactory **42016／42018**、Zyxel **7273**、MS **81963／85880**、Chromium **87491／85046**、Pixel **58704**、Cisco ISE **76460**、Acronis **87886**、WSO2 **5430**、Adobe **71362**、SharePoint **65660**、MikroTik **67279**、WordPress **87902**。**newly_overdue：Cisco CVE-2026-76504**。**今日 due：Fortinet CVE-2026-104286**。**即将 due 10-05：Zammad CVE-2026-102489／102490**。**即将 due 10-07：Citrix CVE-2026-88779**。
> X：`/workspace/x-posts-2026-10-04.json`（合并 **6** 条：A1／B0／C0／LWiS5；唯一数字 id **6**（全部有 `id`／`status_url`）；跨源 ID 重叠 **0**；相对 prior seen_ids **+6** 新数字 id；**logged_in=true**／**@seogoogle4**；**blocked=true**）。**B、C 两路 Latest 搜索（含重试及新标签页）持续停在「Loading timeline」，0 条——本报 B／C 无 X 内容，不假装有**。Search A Latest 覆盖约 **0.1h**（扫描约 **28**／保留 **1**；大量被 POC 普通语义污染，未接近 24h 边界）。LWiS List 覆盖约 **23h**（扫描约 **30**／保留 **5**；之后为 10-03 或更旧内容）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。全程只读，未发帖／回复／点赞／转推／收藏／追踪。抓取备注：CISA `/news-events/alerts` 与 `/alerts/2026/10/04/` 索引 **404**（改用 `/news-events/cybersecurity-advisories` 200）；Citrix community 博客 **403**（Cloudflare）；CTX697174 kbsearch 为 JS 壳→改用 `/external/article/CTX697174` 200；Cisco SA box curl TLS 失败、WebFetch 200；Cisco RSS WebFetch 500；Risky RBNEWS619／620／SRB186／BTN185 **404**；tl;dr #349／#350 soft-404；BleepingComputer box curl 403（链接沿用 X 帖展开 URL）；proftpd.org box curl 超时、WebFetch 200。
> 规则：每条含完整 https URL；分列 X 原帖／GitHub·PoC 仓库／厂商公告（CISA KEV／NVD／厂商）／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露／勒索声称／未证实传闻一律标 **UNCONFIRMED／未验证**；仅写谁／打什么／补丁与狩猎级防御摘要。

## 今日摘要

- **【主条 · KEV NEW · Citrix CVE-2026-88779】** CISA 于 **2026-10-04** 入 KEV（due **2026-10-07**）。NetScaler ADC／Gateway **SAML** 内存缓冲区越界 → 拒绝服务（CVSS4 **8.7**，CWE-119）；前提：配置为 SAML SP 或 SAML IdP。Citrix 称已观察到针对未缓解部署的定向攻击；**88771／88772 之后第三个遭利用的 NetScaler 漏洞**。**9/27 已打补丁但启用 SAML 者须再升级**至 14.1-73.41／13.1-64.28（FIPS 14.1-73.41 FIPS；13.1-FIPS／NDcPP 13.1-37.282）。厂商**未见公开 IoC**；Beazley BSL-A1216 有**战役级第三方 IoC（主要对应 88771／88772 活动）**，并称观察到攻击者用 88779 强制重启以触发 88771 日志注入。
  厂商 CTX697174：https://support.citrix.com/external/article/CTX697174
  CISA Adds One（10-04）：https://www.cisa.gov/news-events/alerts/2026/10/04/cisa-adds-one-known-exploited-vulnerability-catalog
  Beazley BSL-A1216：https://labs.beazley.security/advisories/BSL-A1216

- **【due_today · Fortinet CVE-2026-104286】** FortiMail 路径遍历＋NULL 字节 → 未认证任意文件写入（CVSS3 **9.8**）；联邦 due **今日 10-04**。修复 **8.0.2／7.6.7／7.4.9 厂商仍标 upcoming**；临时禁用 IBE／限制管理面与 webmail 暴露。有厂商公开 IoC（FG-IR-26-175：7 哈希＋2 IP）。
  厂商 FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-104286

- **【newly_overdue · Cisco CVE-2026-76504】** 昨 due_today（due **10-03**）→ 今日 **newly_overdue**。Catalyst SD-WAN Manager URI 编码认证绕过 → admin。SA **rev 1.1（10-02）** 新增 Live Protect shield（仅临时部分防护）；Snort **67179**；修复 20.9.10.1／20.12.8.2／20.15.6.1／20.18.4.1／26.1.2.1／26.2.1（Cloud 20.15.605）。**未见公开 IoC**（仅日志狩猎指引）。
  厂商 cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU

- **【upcoming · Zammad CVE-2026-102489／102490 due 10-05＝明天】** 厂商称 102489 仅 ≤6.5 可利用、7.2.0 已加固；102490 细节待 DIVD。**未见公开 IoC。**
  厂商社区声明：https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297

- **【X A／LWiS · ProFTPD CVE-2026-42167 PoC 再流传】** @0xManan 转 ZeroPathAI PoC 仓库。NVD：mod_sql SQL 注入（CWE-89，CVSS3.1 **8.1**），在以 `%U` 等扩展记录 USER 请求且 SQL 后端允许命令执行时可致 RCE；官方 NEWS 将修复（Issue 2052）列于 **1.3.9a（2026-04-27）**，1.3.10rc1 亦含；当前 1.3.9 分支最新 **1.3.9d（2026-08-14）**。**非 KEV**；CISA SSVC exploitation=poc。仅防御摘要，**不转载利用步骤**。
  X 原帖：https://x.com/0xManan/status/2106305536459149612
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-42167

- **【仍逾期亮点 22】** Apple 86950 今日并入 still；高信号：Citrix 88771／88772（与今日 88779 同一战役语境）、Check Point、Arista、F5、JFrog、Zyxel、MS、Chromium、Pixel、ISE、Acronis、WSO2、Adobe、SharePoint、MikroTik、WP。防御：补丁落地＋BOD 26-04 取证。
  CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway

- **【工具／新闻】** Sliver 仍 **v1.7.8**、nuclei **v3.11.1**、nuclei-templates **v10.4.9**——**均无升版**；Risky 仍 **RBNEWS618**／SRB185／BTN184；tl;dr 仍 **#348**。LWiS X：Harden-Windows-Security「device usage intents」（@CyberCakeX）、module stomping 防御检测文章（@felixm_pw）。
  Harden-Windows-Security：https://github.com/HotCakeX/Harden-Windows-Security/wiki/Protect#device-usage-intents
  module stomping：https://combat.theater/blog/module-stomping/

- **【APT／新闻 · UNCONFIRMED】** ShinyHunters 成员据报在约旦被拘并协助 FBI（@Dinosn 转 BleepingComputer，**UNCONFIRMED／未验证**）；@SwiftOnSecurity 讽刺转引 Ken Dilanian 关于 FBI 大规模入侵的报道（**UNCONFIRMED／未验证**，原帖无链接）；@n4glov 回复中提到未公开 zero-day（**UNCONFIRMED**）。
  BleepingComputer：https://www.bleepingcomputer.com/news/security/shinyhunters-hacker-reportedly-detained-in-jordan-aiding-fbi/

- **【合并统计】** X **6**（A1／B0／C0／LWiS5；数字 id **6**；cross **0**；prior **0**；**+6** NEW 数字 id；null_id **0**）；`logged_in=true`／`@seogoogle4`／`blocked=true`（B／C Loading timeline）；覆盖 A~0.1h／B 0／C 0／LWiS~23h；seen_ids **2326→2332**；报告 `/home/box/workspace/security-watch/reports/2026-10-04-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【KEV NEW · 在野】Citrix NetScaler ADC／Gateway CVE-2026-88779（SAML DoS）

CISA 于 **2026-10-04** 加入 KEV；联邦 due **2026-10-07**；forensicTriage=Yes；knownRansomwareCampaignUse=Unknown。漏洞：NetScaler ADC／Gateway 内存缓冲区操作越界（CWE-119）→ 拒绝服务；CVSS4 **8.7**（`CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N`）。**前提**：设备配置为 SAML SP（`add authentication samlAction`）或 SAML IdP（`add authentication samlIdPProfile`）。受影响：14.1 < 14.1-73.41；13.1 < 13.1-64.28；14.1-FIPS < 14.1-73.41 FIPS；13.1-FIPS／NDcPP < 13.1-37.282；Secure Private Access Hybrid 部署中的 NetScaler 实例同样受影响。修复：**14.1-73.41／13.1-64.28／14.1-73.41 FIPS／13.1-37.282** 及更高。厂商变更：2026-10-03（PST）初版，同日加 NetScaler 博客链接；致谢 Bishop Fox 与 watchTowr。NVD 状态 Received（尚未分析）。BleepingComputer（10-04）：Citrix 称已观察到针对未缓解部署的定向攻击，研究者仍在调查是否可致 RCE。Beazley（BSL-A1216，Update 6，10-04）：观察到攻击者用 88779 **强制重启以触发 88771 日志注入**；已打 9/27 补丁的设备未见执行注入命令、未见代码执行。防御：确认是否启用 SAML SP／IdP 与版本；**已于 9/27 修补 88771／88772 但启用 SAML 者须再次升级**；狩猎 nsaaad 反复崩溃／pitboss 重启、`ns.log` 中 “unexpectedly died”；按 BOD 26-04 取证。**不转载利用步骤。**

地址：
- X 原帖：本窗口 X 未采到相关帖（B／C 受阻），不编造
- GitHub／PoC 仓库：未见公开 PoC 仓库（不编造）
- 厂商 CTX697174（静态页）：https://support.citrix.com/external/article/CTX697174
- 厂商 CTX697174（kbsearch）：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174
- 厂商博客（box 403，链接取自 KEV notes）：https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/
- CISA Adds One（10-04）：https://www.cisa.gov/news-events/alerts/2026/10/04/cisa-adds-one-known-exploited-vulnerability-catalog
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88779
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-88779
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- Forensics Triage Requirements：https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk
- 文章 Beazley BSL-A1216：https://labs.beazley.security/advisories/BSL-A1216
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/citrix-patches-netscaler-saml-zero-day-exploited-in-attacks/
- 文章 SecurityOnline：https://securityonline.info/citrix-netscaler-cve-2026-88779-exploited/
- 文章 ZeroHunt：https://zerohunt.ai/blog/netscaler-cve-2026-88779-saml-dos/
- enrich IoC JSON：`/workspace/enrich-2026-10-04/citrix-CVE-2026-88779-iocs.json`

IoC：**厂商未见公开 IoC**。第三方 Beazley BSL-A1216 战役级 IoC（**主要对应 88771／88772 活动**，非厂商 IoC，defang 原样保留）见下文「地址／IoC 汇总」。

### 2. 【due_today · 在野】Fortinet FortiMail CVE-2026-104286

CISA 于 **2026-10-01** 加入 KEV；联邦 due **2026-10-04＝今日**；forensicTriage=Yes。路径遍历（CWE-22）＋ NULL 字节不当处理（CWE-158）→ 未认证经 HTTP/HTTPS 任意文件写入；CVSS3 **9.8**。修复：**FortiMail 8.0.2／7.6.7／7.4.9（厂商仍标 upcoming）**；7.2 迁移至 7.4+。FG-IR-26-175 时间线仍仅 10-01 初版；Fortinet PSIRT RSS 近 24h **无新公告**。临时：按 FG-IR-26-175 禁用 IBE 或限制 webmail／管理面暴露。防御：比对下列 IoC；审计 IBE／管理面异常与文件变更；BOD 26-04 取证。**不转载利用步骤。**

地址：
- X 原帖：本窗口 X 未采到相关帖，不编造
- GitHub／PoC 仓库：未见公开 PoC 仓库（不编造）
- 厂商 FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- 厂商 PSIRT RSS：https://filestore.fortinet.com/fortiguard/rss/ir.xml
- CISA Adds One（10-01）：https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-104286
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-104286
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- enrich IoC JSON：`/workspace/enrich-2026-10-04/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`

IoC（厂商 FG-IR-26-175 原样）：
- IP：`79.141.169.187`／`45.129.0.192`
- `/data/lib/liblog.so` ADDED MD5 `64c90a00c7fda4d5c7973ed64c25783a` SHA256 `8015f34dc84922b03688399d7f9fe7a00361789f7e420c7e2a2cdb23e75cef84`
- `/bin/smit` MODIFIED MD5 `5241738a3e9988404239e12243f6d35b` SHA256 `77324ac428bde86d351fc5fc06f6d64a6bfe737dfb2743df1d4c5ac2418a5b6a`
- `/data/bin/webconsole` ADDED MD5 `ae0ea6502d3fa5f0664bceb73189eb54` SHA256 `7a6cea9f5c9e2e9994d4e3c4da73f86cf5acd05ea5d312c066c9d1dafd69ee38`
- `/data/bin/mailservice` ADDED MD5 `f90fa81a5f521d785f2b2f765e3ab897` SHA256 `4000276a150a165d3c2537d1e19fb393c4de8333076a16655e28059cae82157b`
- `/data/etc/httpd.conf` MODIFIED MD5 `61af1c4bce1c2eebc8ff689ca5337791` SHA256 `703e97c64e61e41dc3aaba580d82bb2aa7b6a11b54ee6fb467ed5d5a3bffdef5`
- `/data/etc/ld.so.preload` ADDED MD5 `8eb64f25d2a8e18e05aae058629473cf` SHA256 `8953ec7960b09f544a880b072ad4e6cfda7a8303f486251d3478dcfdfbac23b6`
- `/data/migadmin.tar.gz` MODIFIED MD5 `49a7156a7d043cc8f9f680579db22f86` SHA256 `d6fe51c22b91776f4c961ea58bcac5917f15d560a619d7ce726d3d51795609d3`

### 3. 【newly_overdue · 在野】Cisco Catalyst SD-WAN Manager CVE-2026-76504

CISA 于 **2026-09-30** 加入 KEV；联邦 due **2026-10-03** → 今日 **newly_overdue**。URI hex 编码处理不当（CWE-177）→ 未认证远程以 admin 权限访问；CVSS3 **9.8**。厂商 SA 标题：Cisco Catalyst SD-WAN Manager API Authentication Bypass Vulnerability；**rev 1.1（2026-10-02）新增 Live Protect shield**（仅临时部分防护；副作用：含 URI 编码的合法用户可能无法登录）；Snort Rule **67179**。修复：<20.9 迁移；20.9→**20.9.10.1**；20.12→**20.12.8.2**；20.15→**20.15.6.1**；20.18→**20.18.4.1**；26.1→**26.1.2.1**；26.2→**26.2.1**；SD-WAN Cloud（Cisco Managed）**20.15.605**（无需用户操作）。近 24h 新 Cisco SA：RSS 抓取失败，**未能确认**。防御：升固定版本并限制管理面；按日志狩猎指引审计；BOD 26-04 取证。**不转载利用／walkthrough 步骤。**

地址：
- X 原帖：本窗口 X 未采到相关帖，不编造
- GitHub／PoC 仓库：未见（不编造）
- 厂商 cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
- CISA Adds One（09-30）：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-76504
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76504
- 文章 Horizon3（10-01 研究，LWiS 抽查）：https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76504/
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- enrich IoC JSON：`/workspace/enrich-2026-10-04/cisco-CVE-2026-76504-iocs.json`

IoC：未见公开 IoC（厂商 IoC 节仅为日志狩猎示例，示例 IP 为内网示意，勿当威胁情报）。狩猎模式原样：
- 日志：`/var/log/nms/containers/service-proxy/serviceproxy-access.log` — 审计 `j_security_check`／URI 单字符编码（如 `%6a_security_check`）
- 日志：`/var/log/nms/vmanage-server.log` — 审计 `viptela-reserved-` 开头用户名的调用

### 4. 【upcoming · due 10-05＝明天】Zammad CVE-2026-102489／CVE-2026-102490

CISA 于 **2026-10-02** 加入 KEV；联邦 due **2026-10-05**。**102489**：会话固定 → 以 zammad 用户远程代码执行，可与 102490 链式利用；厂商称 **仅 Zammad ≤6.5 可利用**（EOS），7.0+ 实际不可利用，**7.2.0 已加固**。**102490**：不当权限管理 → 本地 zammad→root；厂商称尚未从 DIVD 收到技术细节。DIVD-2026-00015。防御：升级或迁出受影响版本；限制管理与本地提权面；按 BOD 26-04 取证。**未见公开 IoC。不转载利用步骤。**

地址：
- X 原帖：本窗口 X 未采到相关帖，不编造
- GitHub／PoC 仓库：未见（不编造）
- 厂商 releases：https://zammad.com/en/product/releases/
- 厂商社区声明：https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297
- CISA Adds Two（10-02）：https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog
- KEV 489：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-102489
- KEV 490：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-102490
- NVD 489：https://nvd.nist.gov/vuln/detail/CVE-2026-102489
- NVD 490：https://nvd.nist.gov/vuln/detail/CVE-2026-102490
- 文章 DIVD case：https://csirt.divd.nl/cases/DIVD-2026-00015/
- enrich IoC JSON：`/workspace/enrich-2026-10-04/zammad-CVE-2026-102489-iocs.json` · `/workspace/enrich-2026-10-04/zammad-CVE-2026-102490-iocs.json`

IoC：未见公开 IoC。

### 5. 【X · PoC 流传】ProFTPD mod_sql CVE-2026-42167（非 KEV）

X（LWiS List，约 21h 前）：@0xManan 转 ZeroPathAI 的 CVE-2026-42167 PoC 仓库（CVSS 8.1）。**防御摘要**：NVD（Analyzed）描述为 mod_sql SQL 注入（CWE-89；CVSS3.1 **8.1**，AC:H），在**以 `%U` 等扩展记录 USER 请求**（如 SQLLog／SQLNamedQuery 场景）且 **SQL 后端允许执行命令**（NVD 举例 COPY TO PROGRAM）时可致远程代码执行。**受影响版本**：NVD 描述为「before 1.3.9a」（affected 区段 1.3.7b ≤ v < 1.3.9a；但 NVD CPE 配置写 ≤1.3.9b，两者不一致，以厂商为准）。**修补**：ProFTPD 1.3.9 分支 NEWS 将「Issue 2052 – SQL injection possible via mod_sql because of is_escaped_text() logic error (CVE-2026-42167)」列于 **1.3.9a（Released 27-Apr-2026）**；1.3.10rc1 Release Notes 亦列「Fix for SQL injection (CVE-2026-42167)」；当前 1.3.9 分支最新为 **1.3.9d（2026-08-14）**。CISA SSVC：exploitation=poc、automatable=no、technicalImpact=total；**未入 KEV**，本报未见在野利用证据。**检测／缓解**：盘点启用 mod_sql 的 ProFTPD 实例与版本，升至 1.3.9a+（建议 1.3.9d）或 1.3.10 分支；检查 SQLLog／SQLNamedQuery 是否在失败登录路径记录 `%U`，临时移除该类记录；SQL 账号最小权限（不授超级用户／服务器端程序执行权限）；在 FTP 日志中排查 USER 名含 SQL 元字符（引号、分号等）的失败登录及数据库异常子进程。**不转载利用步骤／payload。**

地址：
- X 原帖：https://x.com/0xManan/status/2106305536459149612（t.co `https://t.co/oP63X5AKKz` → 下列仓库）
- GitHub／PoC 仓库：https://github.com/ZeroPathAI/proftpd-CVE-2026-42167-poc
- 厂商 issue（修复）：https://github.com/proftpd/proftpd/issues/2052
- 厂商 Release Notes 1.3.10rc1：http://www.proftpd.org/docs/RELEASE_NOTES-1.3.10rc1（厂商仅提供 http 链接，按原样记录）
- 厂商 NEWS（1.3.9 分支）：https://github.com/proftpd/proftpd/blob/1.3.9/NEWS
- 厂商 release v1.3.9a：https://github.com/proftpd/proftpd/releases/tag/v1.3.9a
- 厂商 release v1.3.9d：https://github.com/proftpd/proftpd/releases/tag/v1.3.9d
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-42167
- 文章 ZeroPath：https://zeropath.com/blog/proftpd-cve-2026-42167-auth-bypass-privesc-rce
- 文章 oss-security：https://www.openwall.com/lists/oss-security/2026/05/01/4
- enrich NVD JSON：`/workspace/enrich-2026-10-04/nvd-api-CVE-2026-42167.json`

IoC：未见公开 IoC。

### 6. 【X · UNCONFIRMED】@n4glov 回复中的未公开 zero-day 传闻

X Search A（约 4 分钟前）：@n4glov 在回复中提到由 gazine 发现的一个 zero-day，以及由 theflow 发现的另一个 exploit，称后者可能与前者不同、公开时间尚不确定。**无产品名、无 CVE、无链接——UNCONFIRMED／未验证**，仅作线索观察，勿据此行动。

地址：
- X 原帖：https://x.com/n4glov/status/2106884298351800327
- GitHub／PoC 仓库：无
- 厂商公告：无
- 文章：无

IoC：未见公开 IoC。

### 7. 【仍逾期亮点 22 · Citrix 等】

仍逾期亮点 **22**（昨 21 ＋ Apple 86950 今日并入）；全库 dueDate<2026-10-04 共 1730，扣除 newly_overdue 1 ≈ still **1729**。高信号含 Citrix NetScaler **88771／88772**（与今日 NEW 88779 同一战役语境，见 Beazley）、Apple **86950**（修复 iOS/iPadOS 26.7.1／macOS Tahoe 26.7.1／macOS Sequoia 15.8.1）、Check Point、Arista、F5、JFrog、Zyxel、MS、Chromium、Pixel、Cisco ISE、Acronis、WSO2、Adobe、SharePoint、MikroTik、WordPress。防御：按各厂商公告补丁＋BOD 26-04 取证。

地址：
- CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
- CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
- 文章 Unit 42（09-30）：https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
- 文章 watchTowr（09-29，88772）：https://labs.watchtowr.com/here-we-go-again-citrix-netscaler-dtls-preauth-memory-overflow-cve-2026-88772/
- Apple 149226：https://support.apple.com/en-us/149226
- KEV Apple 86950：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-86950
- buckets：`/workspace/_kev_buckets_2026-10-04.json`

IoC：见下文「地址／IoC 汇总」中仍逾期条目（Citrix 战役 IoC 见 Beazley；Apple 未见公开 IoC）。

### 8. 【厂商动态】MSRC／CISA 列表

MSRC CVRF API 近 24h 仅见既有月度文档修订时间戳（2026-Feb、2026-Sep、2025-Mar、2024-Dec；本地 10-03 22:49–23:14），**未逐 CVE 比对修订内容**；无新月度文档、无带外公告迹象。CISA cybersecurity-advisories 列表 10-03 无条目，10-04 仅 Adds One（Citrix 88779）。ICS advisory：本窗口无单独突出主条。

地址：
- MSRC CVRF updates：https://api.msrc.microsoft.com/cvrf/v3.0/updates
- MSRC Update Guide：https://msrc.microsoft.com/update-guide/
- CISA 列表：https://www.cisa.gov/news-events/cybersecurity-advisories
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 1. 【LWiS X】Harden-Windows-Security · device usage intents

@CyberCakeX（约 17h 前）介绍 Harden-Windows-Security 的 **device usage intents**：按设备用途（游戏、业务、学校、开发、高权限等）自动调节安全加固措施，并提到可用 MCP server。防御向：适合按资产角色分层制定 Windows 加固基线；上线前在测试环境评估兼容性。

地址：
- X 原帖：https://x.com/CyberCakeX/status/2106624424653062555（t.co `https://t.co/rBzMkwTqYV` → 下列 wiki）
- GitHub 仓库（wiki）：https://github.com/HotCakeX/Harden-Windows-Security/wiki/Protect#device-usage-intents
- GitHub 仓库：https://github.com/HotCakeX/Harden-Windows-Security
- 厂商公告：无
- 文章：无（以仓库 wiki 为准）

IoC：未见公开 IoC。

### 2. 【LWiS X】module stomping 技术解析（C2 注入技术的防御检测）

@felixm_pw（约 23h 前）分享 module stomping 解析：现代 C2 implant／stager 常用的注入技术，文章涵盖工作原理、商业 C2 框架用法及**防御检测**。本报仅记检测方向：关注合法 DLL 映像内存区与磁盘文件不一致、可执行页被改写、异常模块加载后立即写入等遥测（以原文为准）。**不转载实现步骤。**

地址：
- X 原帖：https://x.com/felixm_pw/status/2106536344587489506（t.co `https://t.co/KVhntNjwWn` → 下列文章）
- GitHub 仓库：无
- 厂商公告：无
- 文章：https://combat.theater/blog/module-stomping/

IoC：未见公开 IoC。

### 3. 【无升版】BishopFox Sliver／nuclei／nuclei-templates

Sliver 仍 **v1.7.8**（昨日升版；published 2026-10-03T19:08:40Z＝16:08 UTC-3），今日无新 release。projectdiscovery/nuclei 仍 **v3.11.1**；nuclei-templates 仍 **v10.4.9**。注：Beazley 报 Citrix 战役中出现硬编码 Sliver C2 域名与 Sliver implant 哈希（见 IoC 汇总），可用于检测工程。

地址：
- X 原帖：B 路 Latest 受阻，0 条（不编造）
- Sliver v1.7.8：https://github.com/BishopFox/sliver/releases/tag/v1.7.8
- nuclei v3.11.1：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates v10.4.9：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- tools pulse：`/workspace/tools-news-pulse-2026-10-04.json`

IoC：未见公开 IoC。

### 4. 【新闻备援】Risky／tl;dr

本日无显著更新：Risky 仍最新 **RBNEWS618**（Authorities dismantle KillSec group，2026-10-02）；SRB **185**；BTN **184**（RBNEWS619／620、SRB186、BTN185 均 404）。tl;dr 仍 **#348**（#349／#350 soft-404）。

地址：
- Risky RBNEWS618：https://risky.biz/RBNEWS618/
- Risky SRB185：https://risky.biz/SRB185/
- Risky BTN184：https://risky.biz/BTN184/
- tl;dr #348：https://tldrsec.com/p/tldr-sec-348

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. 【战役】Citrix NetScaler 88771／88772／88779 持续利用（Beazley BSL-A1216）

Beazley Security 战役页（10-04 Update 6）汇总 88771／88772／88779：攻击者用 88779 强制重启以触发 88771 日志注入；载荷投递含 **Sliver** 下载脚本与 implant、PHP webshell；Mandiant/GTIG 指标涉及 **WHIPSHOT** 传输头与 **SLAPSHOT** 代理残留；多来源（GreyNoise、Lupovis、Mandiant/GTIG、CERT-EU、watchTowr）。LWiS 抽查：Unit 42（09-30）与 watchTowr（09-29）仍为最近相关文。防御：对照 IoC 汇总狩猎 webshell 路径、httpd.conf 变更与异常 Cookie／HTTP 头；可疑设备按 CTX694799 处置并取证。

地址：
- X 原帖：本窗口 X 未采到（C 路受阻），不编造
- GitHub 仓库：无
- 厂商 CTX697174：https://support.citrix.com/external/article/CTX697174
- CISA Adds One（10-04）：https://www.cisa.gov/news-events/alerts/2026/10/04/cisa-adds-one-known-exploited-vulnerability-catalog
- 文章 Beazley：https://labs.beazley.security/advisories/BSL-A1216
- 文章 Unit 42：https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/citrix-patches-netscaler-saml-zero-day-exploited-in-attacks/

IoC：有（第三方战役级，主要对应 88771／88772 活动），原样见「地址／IoC 汇总」。

### 2. 【UNCONFIRMED／未验证】ShinyHunters 成员据报在约旦被拘并协助 FBI

@Dinosn（约 21h 前）转发 BleepingComputer 报道：ShinyHunters 黑客据报在约旦被拘留并协助 FBI。属媒体「据报」，**UNCONFIRMED／未验证**；以后续执法／官方信息为准。

地址：
- X 原帖：https://x.com/Dinosn/status/2106564615207280861（t.co `https://t.co/WlZ5pZB1AR` → 下列文章）
- GitHub 仓库：无
- 厂商／执法公告：未见
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/shinyhunters-hacker-reportedly-detained-in-jordan-aiding-fbi/

IoC：未见公开 IoC。

### 3. 【UNCONFIRMED／未验证】@SwiftOnSecurity 转引「FBI 大规模入侵」报道

@SwiftOnSecurity（约 4 分钟前）以讽刺口吻转引 Ken Dilanian 关于「FBI 大规模入侵影响多数员工并延伸至地方官员」的报道；原帖非技术帖、**未附链接**，本报未取得原始报道 URL（不编造）——**UNCONFIRMED／未验证**。

地址：
- X 原帖：https://x.com/SwiftOnSecurity/status/2106885398894932263
- GitHub 仓库：无
- 厂商／官方公告：未见
- 文章：未取得（不编造）

IoC：未见公开 IoC。

### 4. 【LWiS 博客抽查】

抽查 11 个高信号源（watchTowr、Bishop Fox、Unit 42、Horizon3、SentinelLabs、Fortinet Threat Research、SpecterOps、TrustedSec、dfir.ch、Assetnote、MSRC blog），**近 24h 均无新威胁报告／工具发布**——本日无显著更新。最近条目参考：dfir.ch 10-01 LSASS dump 重建、TrustedSec 10-01 HashcatRosetta、Bishop Fox 10-01 Check Point 93616 研究。

地址：
- dfir.ch：https://dfir.ch/posts/field_notes_trickdump/
- TrustedSec：https://trustedsec.com/blog/hashcatrosetta-reading-the-rosetta-stone-of-password-cracking
- Bishop Fox：https://bishopfox.com/blog/weaponizing-check-point-management-cve-2026-93616
- SpecterOps：https://specterops.io/blog/2026/09/30/introducing-adversary-intelligence-llm-tradecraft/

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Citrix NetScaler 战役（Beazley BSL-A1216；页面标题涵盖 88771／88772／88779；IoC 主要对应 88771／88772 活动；非厂商 IoC；defang 原样）**（来源：https://labs.beazley.security/advisories/BSL-A1216 ／`/workspace/enrich-2026-10-04/citrix-CVE-2026-88779-iocs.json`）
  - 网络：
    - `213.209.159[.]55` IPv4 — Exploit and payload delivery（Publicly reported）
    - `51.158.203[.]95` IPv4 — Exploit delivery（Publicly reported）
    - `185.244.213[.]112` IPv4 — Exploit delivery（Beazley Security）
    - `104.207.47[.]54` IPv4 — Exploit delivery（Beazley Security）
    - `104.207.46[.]202` IPv4 — Exploit delivery（Beazley Security）
    - `104.207.32[.]77` IPv4 — Exploit delivery（Beazley Security）
    - `158.94.211[.]205:8080` IPv4 — Exfil receiver（Beazley Security）
    - `149.104.78[.]141` IPv4 — Exploitation attempts, beginning September 24（GreyNoise）
    - `138.28.234[.]38` IPv4 — Exploitation with attempted DNS exfiltration（Lupovis）
    - `82.167.14[.]7` IPv4 — Exploitation check (writes a test marker)（Lupovis）
    - `85.203.46[.]191` IPv4 — Reconnaissance（Lupovis）
    - `154.217.251[.]226` IPv4 — CVE-2026-88772 scanning（Lupovis）
    - `143.198.7[.]94` IPv4 — CVE-2026-88772 scanning and staging（Mandiant/GTIG）
    - `157.254.167[.]12` IPv4 — CVE-2026-88772 exploitation with backdoor installation（Mandiant/GTIG）
    - `httpworkbench[.]com` Domain — Out-of-band callback for exfiltrated output（Lupovis）
    - `www.pyrlnk[.]cc` Domain — Hardcoded sliver C2（Analysis）
    - `pyrlnk[.]cc` Domain — Payload delivery second wave（Publicly Reported）
    - `f.pylrk[.]cc` Domain — Payload delivery second wave（Publicly Reported）
    - `213.209.159[.]55:443/t/*` Domain — Payload delivery（Publicly Reported）
    - `webhook[.]site` Domain — Out-of-band callback（Publicly Reported）
    - `*.dnshook[.]site` Domain — Out-of-band callback（Publicly Reported）
  - 主机 SHA-256：
    - `c2f5532f3209dce0bd30ead47a2616a74ce8170324ef68dfd59acac3f5f1da34` — Sliver download script（Analysis）
    - `0188b0eba4b01c4fb838df9d1d76c76d7f1dc22897e25161975b606c134c1027` — Sliver C2 implant（Analysis）
    - `6f5a2a452a7901323abd21879c6cecccb47c06aeeaccb1b467212f3b11e4b1e7` — PHP webshell（GreyNoise）
  - 主机路径：
    - `/var/netscaler/logon/LogonPoint/custom/.ctxs.receiver` (Webshell location, GreyNoise)
    - `/vpn/media/nsgclient.ico` / `/vpn/media/*.ico` (Masquaerading icon request URI routed to .sig webshell, Mandiant/GTIG)
    - `/vpn/scripts/linux/nsginstaller*.deb` / `/vpn/scripts/linux/nsgclient*.deb` / `/vpn/scripts/linux/*.php` (Staging path for malicious PHP web shells, Mandiant/GTIG)
    - `/tmp/.uxdport` or `/tmp/.uxdlock` (SLAPSHOT proxy artifact, Mandiant/GTIG)
  - 其他：
    - httpd.conf: `Alias /logon/LogonPoint/custom/receiver.min.css` or `AliasMatch ^/logon/LogonPoint/custom/receiver\.min\.[0-9a-f]+\.css$` (Webshell routing, GreyNoise)
    - httpd.conf: `php_flag engine on` (changed from off) + SetHandler block for webshell (GreyNoise; CERT-EU)
    - Cookies `CsrfToken` and `NSC_TASS` (Webshell access, GreyNoise)
    - `HTTP_X_UX` / `HTTP_X_UX_[0-9]+` (Transport headers used by WHIPSHOT, Mandiant/GTIG)
    - ns.log: “missed too many heartbeats” or “unexpectedly died” in authentication log lines (watchTowr, CERT-EU)
    - `SSL_HANDSHAKE_FAILURE` where ClientVersion is DTLSv1.0 `/var/core` (Mandiant/GTIG)
    - 日志模式：pitboss “PPE unexpectedly died” 后紧随 NSPPE 注入串（Beazley；命令载荷内容按规则不转载）
  - 厂商 CTX697174：未见公开 IoC。
- **Fortinet FortiMail CVE-2026-104286（due_today）**：IP `79.141.169.187`／`45.129.0.192`；7 文件哈希（`/data/lib/liblog.so`、`/bin/smit`、`/data/bin/webconsole`、`/data/bin/mailservice`、`/data/etc/httpd.conf`、`/data/etc/ld.so.preload`、`/data/migadmin.tar.gz` 之 MD5／SHA256 原样见 CVE §2）。（来源：https://fortiguard.fortinet.com/psirt/FG-IR-26-175 ／`/workspace/enrich-2026-10-04/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`）
- **Cisco SD-WAN CVE-2026-76504（newly_overdue）**：未见公开 IoC；狩猎日志 `/var/log/nms/containers/service-proxy/serviceproxy-access.log`（编码 `j_security_check`）；`/var/log/nms/vmanage-server.log`（`viptela-reserved-` 用户）。（来源：cisco-sa-sdwan-webauth／enrich-2026-10-04）
- **Arista VeloCloud CVE-2026-93952（仍逾期）**：`/usr/local/sbin/.vcnode.js`；`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）；`/etc/systemd/system/vc-sysmon.service`；HTTP 头 `x-vc-opt`；IP `142.93.149.77`／`104.248.126.159`。（来源：SA-0183／既往 enrich，沿用昨报）
- **Check Point 85102／93616（仍逾期）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`。（来源：既往报／厂商 SK，沿用昨报）
- **Cisco ISE 76460（仍逾期）**：狩猎示例 `admin#show logging application ise-kong/access.log | include dummyuser`；路径 `./ise/logs/apigateway/access.log`。（来源：既往报／Cisco SA，沿用昨报）
- **Zammad 102489／102490（upcoming）／Apple 86950（still）／ProFTPD 42167／@n4glov 传闻／Harden-Windows-Security／module stomping／ShinyHunters／SwiftOnSecurity 转引**：未见公开 IoC。
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


本窗口 LWiS List 只读采集：扫描约 **30** 条、保留 **5** 条、覆盖约 **23h**（`logged_in=true`／`@seogoogle4`；之后为 10-03 或更旧内容，停止）；**5** 条均有数字 id 与 status_url（@SwiftOnSecurity、@CyberCakeX、@felixm_pw、@0xManan、@Dinosn）；跨源 ID 重叠 0。LWiS 博客 RSS 抽查 11 源近 24h 无新文（见 `/workspace/enrich-2026-10-04/lwis/`）。

## 来源搜索 URL

- X Latest A（CVE／POC／exploit／0day）：https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&f=live
- X Latest B（github.com + C2／red team／nuclei；**本轮 Loading timeline 受阻，0 条**）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- X Latest C（malware analysis／threat report／threat actor；**本轮 Loading timeline 受阻，0 条**）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 公告列表：https://www.cisa.gov/news-events/cybersecurity-advisories
- CISA 10-04 Adds One（Citrix 88779）：https://www.cisa.gov/news-events/alerts/2026/10/04/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 10-02 Adds Two（Zammad 102489／102490）：https://www.cisa.gov/news-events/alerts/2026/10/02/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 10-01 Adds One（Fortinet 104286）：https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-30 Adds One（Cisco 76504）：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-27 Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- NVD API（CVE 2.0）：https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-88779
- NVD 88779／104286／76504／42167：https://nvd.nist.gov/vuln/detail/CVE-2026-88779 · https://nvd.nist.gov/vuln/detail/CVE-2026-104286 · https://nvd.nist.gov/vuln/detail/CVE-2026-76504 · https://nvd.nist.gov/vuln/detail/CVE-2026-42167
- 厂商 Citrix CTX697174：https://support.citrix.com/external/article/CTX697174
- 厂商 Fortinet FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- 厂商 Fortinet PSIRT RSS：https://filestore.fortinet.com/fortiguard/rss/ir.xml
- 厂商 Cisco SD-WAN：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
- 厂商 Zammad 社区：https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297
- 厂商 ProFTPD issue 2052：https://github.com/proftpd/proftpd/issues/2052
- 厂商 ProFTPD NEWS：https://github.com/proftpd/proftpd/blob/1.3.9/NEWS
- MSRC CVRF：https://api.msrc.microsoft.com/cvrf/v3.0/updates
- Beazley BSL-A1216：https://labs.beazley.security/advisories/BSL-A1216
- BleepingComputer Citrix 88779：https://www.bleepingcomputer.com/news/security/citrix-patches-netscaler-saml-zero-day-exploited-in-attacks/
- BleepingComputer ShinyHunters：https://www.bleepingcomputer.com/news/security/shinyhunters-hacker-reportedly-detained-in-jordan-aiding-fbi/
- ZeroPathAI PoC 仓库：https://github.com/ZeroPathAI/proftpd-CVE-2026-42167-poc
- Harden-Windows-Security：https://github.com/HotCakeX/Harden-Windows-Security/wiki/Protect#device-usage-intents
- module stomping：https://combat.theater/blog/module-stomping/
- Risky Business：https://risky.biz/ · https://risky.biz/RBNEWS618/
- tl;dr sec：https://tldrsec.com/ · https://tldrsec.com/p/tldr-sec-348
- Sliver v1.7.8：https://github.com/BishopFox/sliver/releases/tag/v1.7.8
