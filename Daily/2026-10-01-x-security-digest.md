# X 安全情报晚报 · 2026-10-01

> 搜集窗口：圣地亚哥时间 **2026-09-30 20:00 至 2026-10-01 ~20:40**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-10-01.json`（collected_at **2026-10-01T20:18:00-03:00**）＋ `/workspace/tools-news-pulse-2026-10-01.json`＋ `/workspace/enrich-2026-10-01/`。CISA KEV catalogVersion **2026.10.01**／**1731** 条／dateReleased **2026-10-01T19:54:04.9308Z**（约合当地 16:54 CLST；相对昨日基线 **2026.09.30／1730**：**count Δ+1**；**NEW Fortinet CVE-2026-104286**；今日 CISA「Adds One」：https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog ）。**due_today 空**；**newly_overdue Citrix CVE-2026-88771／88772**（昨 due_today，due=**2026-09-30**，今日转入逾期）；**仍逾期亮点 19**（昨延续；Citrix **不并入** 19 以免重复计数）；**upcoming** 10-02 Apple **86950**、10-03 Cisco **76504**、10-04 Fortinet **104286**。
> **仍逾期**：**Check Point CVE-2026-85102／93616**、**Arista VeloCloud CVE-2026-93952**、**F5 BIG-IP APM CVE-2026-94127**、**JFrog Artifactory CVE-2026-42016／42018**、**Zyxel CVE-2026-7273**、**MS CVE-2026-81963／85880**、**Chromium CVE-2026-87491／85046**、**Pixel CVE-2026-58704**、**Cisco ISE CVE-2026-76460**、**Acronis CVE-2026-87886**、**WSO2 CVE-2026-5430**、**Adobe CVE-2026-71362**、**SharePoint CVE-2026-65660**、**MikroTik CVE-2026-67279**、**WordPress CVE-2026-87902**。**newly_overdue**：**Citrix CVE-2026-88771／88772**。**即将 due 10-02**：**Apple CVE-2026-86950**。**即将 due 10-03**：**Cisco CVE-2026-76504**。**即将 due 10-04**：**Fortinet CVE-2026-104286**。
> X：`/workspace/x-posts-2026-10-01.json`（合并 **62** 条唯一：A22／B12／C14／LWiS14；跨源 ID 重叠 **0**；相对 prior seen_ids 重叠 **3**／**+59** 新 id；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.87h**。Search B 可见约 **24h**。Search C 约 **2h**。LWiS List 约 **23h**（扫描约 **66**／保留 **14**；成员约 **501**；**交叉校验，不假装为本窗口 24h Latest**）。**首次 home Loading 后重试成功 logged_in=true**。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。抓取备注：Citrix 社区公告 Cloudflare/**403**；CISA `/news-events/alerts` 索引常 **404**（今日 Adds One 直链 200）；RBNEWS618／BTN185 **404**；BC 搜索页 **403**（BC FortiMail 文章直链可用）；部分帖 t.co 已展开为完整 https。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露／勒索声称一律标 **UNCONFIRMED／未验证**；仅写谁／打什么／补丁与狩猎级防御摘要。

## 今日摘要

- **【主条 · KEV NEW · Fortinet CVE-2026-104286】** CISA 于 **2026-10-01** 将 **CVE-2026-104286** 加入 KEV（catalog **2026.10.01／1731／Δ+1**）；联邦 due **2026-10-04**；forensicTriage=Yes；ransomware 使用 Unknown。Fortinet FortiMail：路径遍历（CWE-22）＋ NULL 字节不当处理（CWE-158）→未认证经 HTTP/HTTPS 任意文件写入（CVSS **9.8**；活跃利用）。固定方向：**upcoming 8.0.2+／7.6.7+／7.4.9+**；7.2.x 迁 **7.4** 分支。临时缓解：按 FG-IR-26-175 禁用 IBE 或限制管理面仅受信私网。X A 交叉（sec_news_com／alawbathani／NEXSIGHTNEWS／MyDooM15＋BleepingComputer）。防御：比对厂商公开 IoC 文件哈希与 IP；审计 archive account／IBE／管理面异常；BOD 26-04。**不转载利用步骤。**
  CISA Adds One：https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog
  厂商 FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
  文章（BC）：https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortimail-flaw-exploited-in-zero-day-attacks/
  X（sec_news_com）：https://x.com/sec_news_com/status/2105798843317235825
  X（MyDooM15／BC）：https://x.com/MyDooM15/status/2105791726375846176

- **【newly_overdue · Citrix 88771／88772】** 昨 due_today（due=**2026-09-30**）**今日转入 newly_overdue**。88771 未认证命令执行；88772 内存边界不当→RCE/DoS；同族 CTX697096 覆盖 **88771–88778**。X A：@AzmyBlog 转述入侵后痕迹——攻击者添加 **sec_monitor** 超级用户、WebShell **伪装成 CSS**（**仅狩猎级；不写利用步骤**）。防御：立即按 CTX 升 ADC/Gateway；按 CTX694799 疑似沦陷取证；狩猎异常超级用户名与伪装静态资源；BOD 26-04。**厂商侧本轮未见可抄录具体哈希／IP。**
  CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
  CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
  CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
  X（AzmyBlog）：https://x.com/AzmyBlog/status/2105790468101415192

- **【upcoming · Apple CVE-2026-86950 due 10-02 · PoC 出现报道】** KEV 自 09-29；due **2026-10-02＝明天**。X A：@VELO_ch 称公开 PoC 出现（关联恶意 PDF／字体路径报道）；LWiS：@justdionysus／Calif「Great Glyph Grift」研究交叉。防御：尽快更新受影响 Apple 设备（示例 iOS/iPadOS **26.7.1**、macOS Tahoe **26.7.1**、Sequoia **15.8.1**）；审慎处理不可信 PDF／字体；BOD 26-04。**不转载／不展开 PoC。**
  CISA Adds One（09-29）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
  Apple：https://support.apple.com/en-us/149226 · https://support.apple.com/en-us/149228 · https://support.apple.com/en-us/149229
  文章（THN／VELO）：https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
  X（VELO_ch）：https://x.com/VELO_ch/status/2105788850337689927
  X（justdionysus／LWiS）：https://x.com/justdionysus/status/2105652850453832093

- **【upcoming · Cisco CVE-2026-76504 due 10-03】** 昨 NEW 入 KEV；due **2026-10-03**。X A：@c0desec／@boss_sec_labo；LWiS：@catc0n／VulnCheck 根因分析（**不转载 exploit walkthrough**）。防御：On-Prem 升固定版本并限制非受信访问；狩猎编码 `j_security_check`／`viptela-reserved-`；BOD 26-04。
  厂商 cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
  VulnCheck：https://www.vulncheck.com/blog/revenge-of-the-sd-wan-cve-2026-76504
  X（c0desec）：https://x.com/c0desec/status/2105793102573126013
  X（catc0n／LWiS）：https://x.com/catc0n/status/2105766997833421026

- **【仍逾期亮点 19】** 无 dueDate=10-01 条目；Citrix 记在 newly_overdue。高信号：**Check Point 85102／93616**、**Arista 93952**（SA-0183 IoC）、**F5 94127**、**JFrog 42016／42018**、**Zyxel 7273**、MS／Chromium／Pixel／ISE／Acronis／WSO2／Adobe、SharePoint **65660**／MikroTik **67279**／WP **87902**。防御：补丁落地核验与狩猎；BOD 26-04。
  Arista SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
  Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/

- **【X A 交叉 · Zimbra／WP 多插件／MikroTik 84411／Monta／Ghost 等】** Microsoft 跟踪 Zimbra **CVE-2026-73570**（升 **10.1.20+**、查 WebShell／可疑登录）；WP：**87902**（KEV 仍逾期）＋ LatePoint／Iptanus／Authorizer／Super Forms／Redux／Autoptimize 等；MikroTik **CVE-2026-84411**（升 **7.24+** 或 **7.23.7 LTS**、撤 WAN 暴露）；Monta EV WebSocket 四 CVE；Ghost CMS **103268**；Next.js／Satori **94545**（暴露面情报，不写 RCE 步骤）。防御：按厂商补丁；限制管理面。

- **【工具／新闻】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** **无升版**；Risky **新 SRB185**（“Rogue AI” isn’t going anywhere，2026-10-01）；RBNEWS 仍 **617**／BTN 仍 **184**；tl;dr **新 #348**（昨软 404，今已上线）。X B（~24h）：llm-redkit、dotnet-memshell、RedTeamSimmer、dissect.cobaltstrike **v1.3.0**、voidsyscall、redStackPRO 等（**授权评估语境**）。LWiS：HashcatRosetta、LOLBAS、IDA 9.5 Beta、better-auth **1.7.7**、blackmagick、MCP design 等。

- **【APT／Malware · 大量 UNCONFIRMED】** C（~2h）：Hospital Hermilio Valdizán／RansomHouse、EURODITEL／krybit、瑞士大学 RDWeb、Tata／HELLSKEY、土耳其 IYS、Karamtech、drizly、危地马拉公用事业等——**一律 UNCONFIRMED**。较有信号：DPRK playbook 档案转述（ForIntOrg）；LWiS GrayKey／iPhone 自动重启绕过报道（执法工具语境）。

- **【合并统计】** X **62** 唯一（A22／B12／C14／LWiS14；cross **0**；prior **3**；**+59** NEW）；`logged_in=true`／`@seogoogle4`／`blocked=false`；覆盖 A~0.87h／B~24h／C~2h／LWiS~23h；seen_ids **2249→2308**；报告 `/home/box/workspace/security-watch/reports/2026-10-01-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【KEV NEW · due 10-04】Fortinet FortiMail CVE-2026-104286

CISA 于 **2026-10-01** 加入 KEV；联邦 due **2026-10-04**。路径遍历＋ NULL 字节不当处理 → 未认证经 HTTP/HTTPS 任意文件写入；CVSS **9.8**；forensicTriage=Yes；knownRansomwareCampaignUse=Unknown。受影响示例：FortiMail **8.0.0–8.0.1**／**7.6.0–7.6.6**／**7.4.0–7.4.8**／**7.2.0–7.2.9**。固定方向：**upcoming 8.0.2+／7.6.7+／7.4.9+**；7.2.x 迁 7.4 分支。临时：按 FG-IR-26-175 禁用 IBE 或限制管理面。X A／BC 交叉。防御：升固定版本；比对下列 IoC；审计 remote-ip／archive account／IBE DecrypterMediaIn BufferException／管理面异常 logout；BOD 26-04。**不转载利用步骤。**

地址：
- CISA Adds One：https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-104286
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-104286
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortimail-flaw-exploited-in-zero-day-attacks/
- 文章 NEXSIGHT：https://cyber.nexsight.co/articles/2026/10/02/fortimail-cve-2026-104286-zero-day-kev-2026-10-02/
- recon.sec-lav：https://recon.sec-lav.com/articles/kev-alert-2026-10-01
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- enrich IoC JSON：`/workspace/enrich-2026-10-01/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`
- X（sec_news_com）：https://x.com/sec_news_com/status/2105798843317235825
- X（alawbathani）：https://x.com/alawbathani/status/2105798169841836066
- X（NEXSIGHTNEWS）：https://x.com/NEXSIGHTNEWS/status/2105800784608641182
- X（MyDooM15）：https://x.com/MyDooM15/status/2105791726375846176

IoC（厂商 FG-IR-26-175／今日 enrich **原样抄录**，非穷尽）：
- 文件：`/data/lib/liblog.so` — MD5 `64c90a00c7fda4d5c7973ed64c25783a` · SHA256 `8015f34dc84922b03688399d7f9fe7a00361789f7e420c7e2a2cdb23e75cef84`（ADDED）
- 文件：`/bin/smit` — MD5 `5241738a3e9988404239e12243f6d35b` · SHA256 `77324ac428bde86d351fc5fc06f6d64a6bfe737dfb2743df1d4c5ac2418a5b6a`（MODIFIED）
- 文件：`/data/bin/webconsole` — MD5 `ae0ea6502d3fa5f0664bceb73189eb54` · SHA256 `7a6cea9f5c9e2e9994d4e3c4da73f86cf5acd05ea5d312c066c9d1dafd69ee38`（ADDED）
- 文件：`/data/bin/mailservice` — MD5 `f90fa81a5f521d785f2b2f765e3ab897` · SHA256 `4000276a150a165d3c2537d1e19fb393c4de8333076a16655e28059cae82157b`（ADDED）
- 文件：`/data/etc/httpd.conf` — MD5 `61af1c4bce1c2eebc8ff689ca5337791` · SHA256 `703e97c64e61e41dc3aaba580d82bb2aa7b6a11b54ee6fb467ed5d5a3bffdef5`（MODIFIED）
- 文件：`/data/etc/ld.so.preload` — MD5 `8eb64f25d2a8e18e05aae058629473cf` · SHA256 `8953ec7960b09f544a880b072ad4e6cfda7a8303f486251d3478dcfdfbac23b6`（ADDED）
- 文件：`/data/migadmin.tar.gz` — MD5 `49a7156a7d043cc8f9f680579db22f86` · SHA256 `d6fe51c22b91776f4c961ea58bcac5917f15d560a619d7ce726d3d51795609d3`（MODIFIED）
- IP：`79.141.169.187`
- IP：`45.129.0.192`

### 2. 【newly_overdue · 在野】Citrix NetScaler CVE-2026-88771／CVE-2026-88772

CISA 于 **2026-09-27** 加入 KEV；联邦 due **2026-09-30**，**今日转入 newly_overdue**。88771：不当输入验证 → 未认证命令执行。88772：内存边界限制不当 → RCE/DoS。同公告族 **CVE-2026-88771–88778**（CTX697096）。社区公告 Cloudflare/**403**。X A：@AzmyBlog 称入侵后痕迹含 **sec_monitor** 超级用户、WebShell **伪装成 CSS**（狩猎线索；**不写利用／落盘步骤**）。防御：立即按 CTX 升 ADC/Gateway；按 CTX694799 疑似沦陷排查；狩猎异常超级用户与伪装静态资源；限制管理面；BOD 26-04。

地址：
- CISA Adds Two：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- 厂商 CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
- 厂商 CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
- Community bulletin：https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778
- NVD 88771：https://nvd.nist.gov/vuln/detail/CVE-2026-88771
- NVD 88772：https://nvd.nist.gov/vuln/detail/CVE-2026-88772
- KEV 88771：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88771
- KEV 88772：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88772
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- X（AzmyBlog）：https://x.com/AzmyBlog/status/2105790468101415192

IoC：未见公开哈希／C2 IP（社交转述狩猎线索：超级用户名 `sec_monitor`；WebShell 伪装 CSS——以现场取证为准，非厂商正式 IoC 清单）。

### 3. 【upcoming · due 10-02】Apple Multiple Products CVE-2026-86950（PoC 出现报道）

CISA 于 **2026-09-29** 加入 KEV；联邦 due **2026-10-02**。CoreGraphics 越界写 → 任意代码执行。补丁示例：**iOS/iPadOS 26.7.1**、**macOS Tahoe 26.7.1**、**macOS Sequoia 15.8.1**。X A：@VELO_ch 称公开 PoC 出现（THN 报道，关联恶意 PDF／字体）；LWiS：@justdionysus 引用 Calif「Great Glyph Grift」。另 @deepdig19 YouTube 简述（信息简略）。防御：尽快更新；审慎处理不可信 PDF／字体文档；BOD 26-04。**不转载 PoC／payload。**

地址：
- CISA Adds One（09-29）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 Apple 149226：https://support.apple.com/en-us/149226
- 厂商 Apple 149228：https://support.apple.com/en-us/149228
- 厂商 Apple 149229：https://support.apple.com/en-us/149229
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-86950
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-86950
- 文章 The Hacker News：https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- X（VELO_ch）：https://x.com/VELO_ch/status/2105788850337689927
- X（justdionysus／LWiS）：https://x.com/justdionysus/status/2105652850453832093
- X（calif_io 引用）：https://x.com/calif_io/status/2105382144495517950
- X（deepdig19）：https://x.com/deepdig19/status/2105799371438575873

IoC：未见公开 IoC。

### 4. 【upcoming · due 10-03】Cisco Catalyst SD-WAN Manager CVE-2026-76504

CISA 于 **2026-09-30** 加入 KEV；联邦 due **2026-10-03**。URI hex 编码绕过 Web／API 认证 → 未认证管理员访问；CVSS **9.8**。固定版本示例：**20.9.10.1／20.12.8.2／20.15.6.1／20.18.4.1／26.1.2.1／26.2.1**；Cloud Managed **20.15.605**（用户侧无动作）。X A／LWiS／VulnCheck 交叉。防御：On-Prem 尽快升级并限制非受信网络访问；审计狩猎日志；BOD 26-04。**不转载利用／walkthrough 步骤。**

地址：
- CISA Adds One（09-30）：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76504
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-76504
- VulnCheck：https://www.vulncheck.com/blog/revenge-of-the-sd-wan-cve-2026-76504
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- X（c0desec）：https://x.com/c0desec/status/2105793102573126013
- X（boss_sec_labo）：https://x.com/boss_sec_labo/status/2105788012055671175
- X（catc0n／LWiS）：https://x.com/catc0n/status/2105766997833421026

IoC（厂商 SA／昨 enrich 狩猎级日志模式原样；**未见**独立恶意文件哈希或攻击者 C2 IP）：
- 日志：`/var/log/nms/containers/service-proxy/serviceproxy-access.log` — 审计含 URI 编码字符的 `j_security_check`（例 `POST /%6a_security_check`；任一单字符编码均可）来自未知／未授权 IP
- 日志：`/var/log/nms/vmanage-server.log` — 审计 `j_security_check` 且用户名以 `viptela-reserved-` 开头的请求

### 5. 【仍逾期 · KEV 交叉】Zimbra CVE-2026-73570／WordPress CVE-2026-87902／SharePoint／MikroTik 67279

- **Zimbra CVE-2026-73570**（@VELO_ch）：Microsoft 跟踪未认证命令注入／在野；建议升 **10.1.20+** 并检查 WebShell、可疑登录与邮件／凭据访问痕迹。文章：https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/ · X：https://x.com/VELO_ch/status/2105800678220406928 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-73570 · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-73570
- **WordPress Core CVE-2026-87902**（@sitedock_jp）：仍 overdue（due 曾=09-28）；称修复后数小时即见攻击并入 KEV。X：https://x.com/sitedock_jp/status/2105788603368681775 · GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87902
- **SharePoint CVE-2026-65660**／**MikroTik CVE-2026-67279**：仍 overdue。MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660 · MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/

防御：补丁落地核验；暴露面与 forensic triage；BOD 26-04。

IoC：未见公开 IoC（Zimbra／WP 帖摘要未列可抄录哈希／IP）。

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

### 8. 【仍逾期 · 合辑】F5／JFrog／Zyxel／MS／Chromium／Pixel／ISE／Acronis／WSO2／Adobe

- **F5 BIG-IP APM CVE-2026-94127**（due 曾=09-25）：按 K000162605。https://my.f5.com/manage/s/article/K000162605 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94127
- **JFrog Artifactory CVE-2026-42016／42018**（due 曾=09-25）：按厂商 advisories。https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- **Zyxel GS1900 CVE-2026-7273**（due 曾=09-24）：升固件并限制 LAN 管理面。https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
- **MS CVE-2026-81963／85880**（due 曾=09-22）：确认九月补丁。https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963 · https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880
- **Chromium CVE-2026-87491／85046**：升 Chromium 系。https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html · https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- **Pixel CVE-2026-58704**：装 Pixel 安全更新。https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- **Cisco ISE CVE-2026-76460**：升 First Fixed。https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  IoC（厂商／昨 enrich）：`admin#show logging application ise-kong/access.log | include dummyuser`；`./ise/logs/apigateway/access.log`
- **Acronis CVE-2026-87886**：按 SEC-10986。https://security-advisory.acronis.com/advisories/SEC-10986
- **WSO2 CVE-2026-5430**：按 WSO2-2026-5328。https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
- **Adobe CVE-2026-71362**：按 APSB26-92（helpx 常 **403**）。https://helpx.adobe.com/security/products/magento/apsb26-92.html

除 ISE／Arista／Check Point／Fortinet NEW 外，上列多数 **未见公开 IoC**。

### 9. 【X A】WordPress 插件多 CVE／Redux／Autoptimize

- **LatePoint Appointment Booking CVE-2026-92966**（@ridvanyagli）：未认证任意 Shortcode 执行。X：https://x.com/ridvanyagli/status/2105792431874875866 · 插件：https://wordpress.org/plugins/latepoint/
- **Iptanus File Upload CVE-2026-62071**（@ridvanyagli）：未认证 SQLi，CVSS 9.3 称。X：https://x.com/ridvanyagli/status/2105791625494450282 · 插件：https://wordpress.org/plugins/wp-file-upload/
- **Authorizer CVE-2026-103752**（@ridvanyagli）：CVSS 9.8 称，未认证权限提升。X：https://x.com/ridvanyagli/status/2105790531871691117
- **Super Forms CVE-2026-15989**（@ridvanyagli）：未认证权限提升（role=administrator 注入称）。X：https://x.com/ridvanyagli/status/2105789448763916353
- **Redux Framework CVE-2026-90992**（@mgn_jpn）：CVSS 6.4；修正 **4.5.15**。X：https://x.com/mgn_jpn/status/2105798379489943715 · 文章：https://shindan.m-g-n.me/alerts/cve-2026-90992/
- **Autoptimize CVE-2026-14995**（@mgn_jpn）：CVSS 7.2；修正 **3.1.16**。X：https://x.com/mgn_jpn/status/2105800897125077252 · 文章：https://shindan.m-g-n.me/alerts/cve-2026-14995/

防御：升级受影响插件至厂商修正版；审查管理员角色异常创建。**不转载利用步骤。**

IoC：未见公开 IoC。

### 10. 【X A】MikroTik CVE-2026-84411／Monta／Ghost／Zimbra 93647／Next.js 94545

- **MikroTik RouterOS CVE-2026-84411**（@fredmdl）：Web 管理 underflow，称可未登录 root RCE；建议升 **7.24+** 或 **7.23.7 LTS** 并移除 WAN 暴露。X：https://x.com/fredmdl/status/2105789867892568240 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-84411
- **Monta EV charging**（@NewsTongueX）：WebSocket 认证相关 **CVE-2026-95102／97363／97212／93474**。X：https://x.com/NewsTongueX/status/2105800867253203088 · 站点：https://monta.com/
- **Ghost CMS CVE-2026-103268**（@ridvanyagli）：CVSS 8.8 称；停用 staff 可经自助密码重置恢复权限。X：https://x.com/ridvanyagli/status/2105794550182691233 · 仓库：https://github.com/TryGhost/Ghost
- **Zimbra Collaboration Suite CVE-2026-93647**（@ridvanyagli）：Stored XSS，CVSS 9.3 称（疑似无需认证）。X：https://x.com/ridvanyagli/status/2105798855669219537 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-93647
- **Next.js next/og 与 Satori CVE-2026-94545**（@zoomeyebot）：称图像请求路径 RCE；ZoomEye 暴露面 dork（仅作暴露面情报）。X：https://x.com/zoomeyebot/status/2105791140293398973 · ZoomEye：https://www.zoomeye.ai/searchResult?q=YXBwPSJOZXh0LmpzIg%3D%3D · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94545

防御：按厂商／发行版补丁；MikroTik 撤公网管理面；Ghost／Zimbra 审账号与 XSS 面。**不转载利用／RCE 步骤。**

IoC：未见公开 IoC。

### 11. 【LWiS】better-auth 严重认证绕过／GrayKey iPhone 重启绕过报道

- **better-auth**（@v12sec／@rdjgr 转发）：关键认证绕过，CVSS **9.1** 称；库已在 **Better Auth 1.7.7** 修复（帖称附 PoC——**不转载**）。X：https://x.com/v12sec/status/2105653897226551716
- **iPhone 自动重启绕过**（@josephfcox／@SwiftOnSecurity 转发）：404 Media 报道 GrayKey 相关，执法／取证语境延长锁定设备访问窗口。文章：https://www.404media.co/cops-can-bypass-iphone-automatic-inactivity-reboot-graykey/ · X：https://x.com/josephfcox/status/2105645793700884739

防御：依赖 better-auth 的应用尽快升 **1.7.7+**；移动设备安全策略关注重启／锁定窗口。

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 核心工具版本（公开 pulse）

- **Sliver** 仍 **v1.7.7**（无升版）：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- **nuclei** 仍 **v3.11.1**（无升版）：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- **nuclei-templates** 仍 **v10.4.9**（无升版）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- Risky **新**：**SRB185** https://risky.biz/SRB185/（Srsly Risky Biz: “Rogue AI” isn’t going anywhere，2026-10-01）· **RBNEWS617** https://risky.biz/RBNEWS617/ · **BTN184** https://risky.biz/BTN184/ · RBNEWS618／BTN185＝**404**
- tl;dr sec **新**：**#348** https://tldrsec.com/p/tldr-sec-348（Google's PageBreak Scanner, Perplexity's Agent Security Tool, Defending Agentically；昨软 404，今已上线）· **#347** https://tldrsec.com/p/tldr-sec-347

### X Search B（~24h；授权红队／模拟／检测工程向；不写利用步骤）

- **llm-redkit**（agentic red-team harness；Promptfoo／Garak／PyRIT）：https://github.com/Bn09/llm-redkit · X：https://x.com/belkacem_niati/status/2105730189825380545
- **dotnet-memshell**（.NET 进程插入点研究／检测实验室）：https://github.com/lupingQAQ/dotnet-memshell · X：https://x.com/lupingQAQ/status/2105670169343517032
- **RedTeamSimmer**（Atomic Red Team 可视化模拟）：https://github.com/breachsimrange/redteamsimmer · X：https://x.com/Jayson_security/status/2105645052227657864
- **Red-Team-Roadmap**（AD 枚举／基础模块）：https://github.com/Dev-Chukwuma/Red-Team-Roadmap · X：https://x.com/httpschuks/status/2105626646375977239 · https://x.com/httpschuks/status/2105624677095797177
- **dissect.cobaltstrike v1.3.0**（解析 CS 4.11 transform-obfuscate beacon；检测／取证）：https://github.com/fox-it/dissect.cobaltstrike/releases/tag/v1.3.0 · X：https://x.com/YunZhengHu/status/2105601259831251194
- **redStackPRO**（红队基础设施／cyber range 拓扑画布）：https://github.com/devZero-Security/redStackPRO · X：https://x.com/ipurple/status/2105574689141596330
- **voidsyscall**（跨平台 syscall implant／C2；仅授权评估语境）：https://github.com/VoidSecSoftwares/voidsyscall · X：https://x.com/r1cksec/status/2105567586629132702
- **Lockjaw**（Rust Windows C2；prior overlap／授权评估语境）：https://github.com/g13net/lockjaw · X：https://x.com/ipurple/status/2105406520536027458
- **DeepTeam**（LLM／AI agent 红队框架；prior）：https://github.com/confident-ai/deepteam · X：https://x.com/PythonHub/status/2105391045131309239
- **AdaptixC2 serverless transport**（AWS Lambda＋DynamoDB；prior）：https://github.com/stillbigjosh/adaptix-serverless-c2 · X：https://x.com/ipurple/status/2105265660762763506
- **恶意 GitHub 邀请／Brisova 构建期载荷分析**（@negtivspace；明确勿运行该仓库）：X：https://x.com/negtivspace/status/2105290747436269797

### LWiS 交叉工具／研究（~23h）

- **VulnCheck Cisco SD-WAN 根因**（见 CVE 节；不转载 exploit）：https://www.vulncheck.com/blog/revenge-of-the-sd-wan-cve-2026-76504 · X：https://x.com/catc0n/status/2105766997833421026
- **HashcatRosetta**（Hashcat rule 翻译／优化）：https://trustedsec.com/blog/hashcatrosetta-reading-the-rosetta-stone-of-password-cracking?utm_content=386785309&utm_medium=social&utm_source=twitter&hss_channel=tw-403811306 · X：https://x.com/TrustedSec/status/2105675642838655329
- **IDA 9.5 Beta**（IDA MCP／Assist、多架构反编译、Malware Analysis 插件）：X（fr0gger_）：https://x.com/fr0gger_/status/2105765382288244751 · Hex-Rays：https://x.com/HexRaysSA/status/2105698662932443469
- **LOLBAS 更新**（applocker bypass／proxy execution／任意 DLL／下载／阻断 Defender 更新等条目）：https://lolbas-project.github.io/ · X：https://x.com/Wietze/status/2105629601082855458
- **Outflank MCP design**（agent 找不到工具／忽略约束／上下文截断）：https://www.outflank.nl/blog/2026/09/30/mcp-design/ · X：https://x.com/OutflankNL/status/2105658403691393450
- **blackmagick sleep techniques**（研究／检测；引用 Pulse／Nighthawk Evanesco）：https://blackmagick.io/ · https://www.nighthawkc2.io/evanesco/ · X：https://x.com/Teach2Breach/status/2105730541345820977
- **TEB 取得技巧 gist**（逆向工程笔记）：https://gist.github.com/winterknife/2a8dd60ab593589843de93b04cecac2c · X：https://x.com/_winterknife_/status/2105767907007304095
- **CISO 弱口令＋漏补丁**（The Register）：https://www.theregister.com/security/2026/10/01/ciso-thought-he-had-a-r3lg00dpw0rd-but-forgot-to-patch/5300314 · X：https://x.com/Dinosn/status/2105660599908831331
- **NVIDIA OpenShell 限制 agent**（@_xpn_）：X：https://x.com/_xpn_/status/2105657406344843567
- **车企 app VIN／位置外传研究**（@IntCyberDigest）：X：https://x.com/IntCyberDigest/status/2105442820379091255
- **Bug Bounty 低质量提交观察**（@yeahbutnahbut）：X：https://x.com/yeahbutnahbut/status/2105772978700943639

IoC：工具帖未见公开 IoC。

## APT / Malware 分析

### 1. 【X C】DPRK threat-actor playbook 转述

@ForIntOrg 称 Foreign Interference 档案涵盖 9 月约 **130** 起事件（playbook 级汇总；细节以站点为准）。防御：关注 DPRK 典型供应链／加密货币／社会工程 TTPs 基线狩猎。

地址：
- X：https://x.com/ForIntOrg/status/2105798850514723184
- 站点：https://www.foreigninterference.org/

IoC：未见公开 IoC。

### 2. 【LWiS】GrayKey／iPhone 自动重启绕过报道

404 Media：执法工具语境下绕过 iPhone 自动 inactivity reboot，可能延长锁定设备访问窗口。防御：移动设备丢失／扣押场景的锁定与重启策略评估（非漏洞利用教程）。

地址：
- 文章：https://www.404media.co/cops-can-bypass-iphone-automatic-inactivity-reboot-graykey/
- X：https://x.com/josephfcox/status/2105645793700884739

IoC：未见公开 IoC。

### 3. 【X C · 未验证】勒索软件事件声称（合辑）

以下均为社交列表报道，**一律 UNCONFIRMED／未验证**：

- **Hospital Hermilio Valdizán（秘鲁）** 据报遭 **RansomHouse**（FalconFeeds／ThreatAtlas 交叉）：https://x.com/FalconFeedsio/status/2105801142601142582 · https://x.com/ThreatAtlas/status/2105767042234118284 · 站点：https://hhv.gob.pe/
- **EURODITEL／RESOTELECOM** 据报遭 **krybit**：https://x.com/ThreatAtlas/status/2105774687733129395

IoC：未见公开 IoC。

### 4. 【X C · 未验证】地下泄露／初始访问／售卖声称（合辑）

**一律 UNCONFIRMED／未验证**：

- HELLSKEY_BREACH／Tata Supermarkets 管理访问声称：https://x.com/VECERTRadar/status/2105800715213971882
- 土耳其 IYS ~30.2 万条数据声称：https://x.com/DailyDarkWeb/status/2105798708969542049
- Lvn4t1k0／教育研究机构 183 条记录声称：https://x.com/intels_daily/status/2105796683753791729
- 瑞士某大学 RDWeb 初始访问（约 2,500 主机／Local Admin）广告：https://x.com/DarkWebInformer/status/2105785597918912785
- Sensitive2025／Paraguay Educational Management Portal 声称：https://x.com/intels_daily/status/2105781590316007820
- Fakturownia 遭漏洞入侵、可能暴露哈希／银行信息／令牌声称：https://x.com/IntCyberDigest/status/2105778349867991168
- apt73／IFMIS 受害者数据声称：https://x.com/intels_daily/status/2105774628132061206
- Nameless511／Karamtech ~200 万条（Odoo／WooCommerce／PostgreSQL）声称：https://x.com/intels_daily/status/2105774287940473075
- apt73／drizly[.]com ~250 万条（原帖 Unverified）：https://x.com/intels_daily/status/2105774216649875963
- RETHIXX／危地马拉公用事业账单声称（原帖未获官方验证）：https://x.com/VECERTRadar/status/2105772329078772178

IoC：未见可核验公开 IoC（仅帖文域名／数量转述，不作确认）。

### 5. ICS

本日公开备援主条以 **KEV NEW Fortinet 104286**、**newly_overdue Citrix 88771／88772**、**仍逾期网关／编排／APM／VPN** 与 **upcoming Apple／Cisco／Fortinet** 为主；**无单独新突出的 2026-10-01 ICS advisory 主条**。Monta EV WebSocket 四 CVE 见 CVE 节（充电平台 Web，非传统 ICS advisory）。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Fortinet FortiMail CVE-2026-104286（NEW）**：7 文件哈希（`/data/lib/liblog.so`、`/bin/smit`、`/data/bin/webconsole`、`/data/bin/mailservice`、`/data/etc/httpd.conf`、`/data/etc/ld.so.preload`、`/data/migadmin.tar.gz` 之 MD5／SHA256 见 CVE §1）＋ IP `79.141.169.187`／`45.129.0.192`。（来源：FG-IR-26-175／`/workspace/enrich-2026-10-01/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`）
- **Cisco SD-WAN CVE-2026-76504（upcoming）**：狩猎日志 `/var/log/nms/containers/service-proxy/serviceproxy-access.log`（编码 `j_security_check`）；`/var/log/nms/vmanage-server.log`（`viptela-reserved-` 用户＋j_security_check）。**未见**独立恶意文件哈希／攻击者 C2 IP。（来源：cisco-sa-sdwan／昨 enrich）
- **Arista VeloCloud CVE-2026-93952（仍逾期）**：`/usr/local/sbin/.vcnode.js`；`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）；`/etc/systemd/system/vc-sysmon.service`；HTTP 头 `x-vc-opt`；IP `142.93.149.77`／`104.248.126.159`。（来源：SA-0183／昨 enrich）
- **Check Point 85102／93616（仍逾期）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`。（来源：昨报／厂商 SK／enrich）
- **Cisco ISE 76460（仍逾期）**：狩猎示例 `admin#show logging application ise-kong/access.log | include dummyuser`；路径 `./ise/logs/apigateway/access.log`。（来源：昨报／Cisco SA）
- **Citrix newly_overdue（社交狩猎线索，非厂商正式 IoC）**：超级用户名 `sec_monitor`；WebShell 伪装 CSS——以现场取证为准。
- **Apple 86950／仍逾期其余／工具仓／C 勒索与泄露声称**：未见可抄录公开 IoC（或仅厂商原文内；C 帖多为域名转述且 **UNCONFIRMED**）
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

本窗口 LWiS List 只读采集：扫描约 **66** 条、保留 **14** 条、覆盖约 **23h**（`logged_in=true`／`@seogoogle4`／`blocked=false`；成员约 **501**）；跨源 ID 重叠 0（相对 A／B／C）；含 VulnCheck Cisco SD-WAN、HashcatRosetta、LOLBAS、IDA 9.5、better-auth、blackmagick、Apple glyph、MCP design、GrayKey 等；meta：`/workspace/x-lwis-list-meta-2026-10-01.json`。

## 来源搜索 URL

- X Latest A（CVE／0-day）：https://x.com/search?q=%28CVE%20OR%20%220-day%22%20OR%200day%29%20-filter%3Areplies&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／cobalt／implant／threat hunting）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20%22red-team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt%20OR%20implant%20OR%20%22threat%20hunting%22)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky SRB185：https://risky.biz/SRB185/
- Risky RBNEWS617：https://risky.biz/RBNEWS617/
- Risky BTN184：https://risky.biz/BTN184/
- tl;dr sec：https://tldrsec.com/
- tl;dr #348：https://tldrsec.com/p/tldr-sec-348
- tl;dr #347：https://tldrsec.com/p/tldr-sec-347
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 10-01 Adds One（Fortinet 104286）：https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-30 Adds One（Cisco 76504）：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-29 Adds One（Apple 86950）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-27 Adds Two（Citrix 88771／88772）：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 09-27 Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- 厂商 Fortinet FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- 厂商 Cisco SD-WAN：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
- 文章 BC FortiMail：https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-fortimail-flaw-exploited-in-zero-day-attacks/
