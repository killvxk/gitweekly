# X 安全情报晚报 · 2026-09-30

> 搜集窗口：圣地亚哥时间 **2026-09-29 20:00 至 2026-09-30 ~20:30**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-30.json`（collected_at **2026-09-30T20:20:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-30.json`＋ `/workspace/enrich-extra-2026-09-30.json`＋ `/workspace/enrich-2026-09-30/`。CISA KEV catalogVersion **2026.09.30**／**1730** 条／dateReleased **2026-09-30T16:59:23.0688Z**（约合当地 13:59 CLST；相对昨日基线 **2026.09.29／1729**：**count Δ+1**；**NEW Cisco CVE-2026-76504**；今日 CISA「Adds One」：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog ）。**due_today** Citrix **CVE-2026-88771／88772**（联邦 due=**2026-09-30＝今日**，**尚未**转入 newly_overdue／overdue）；**newly_overdue 空**；**仍逾期亮点 19**（含昨 newly_overdue 的 SharePoint **65660**／MikroTik **67279**／WordPress **87902**，现归仍逾期）；**upcoming** 10-02 Apple **86950**、10-03 Cisco **76504**。
> **仍逾期**：**Check Point CVE-2026-85102／93616**、**Arista VeloCloud CVE-2026-93952**、**F5 BIG-IP APM CVE-2026-94127**、**JFrog Artifactory CVE-2026-42016／42018**、**Zyxel CVE-2026-7273**、**MS CVE-2026-81963／85880**、**Chromium CVE-2026-87491／85046**、**Pixel CVE-2026-58704**、**Cisco ISE CVE-2026-76460**、**Acronis CVE-2026-87886**、**WSO2 CVE-2026-5430**、**Adobe CVE-2026-71362**、**SharePoint CVE-2026-65660**、**MikroTik CVE-2026-67279**、**WordPress CVE-2026-87902**。**due_today（≠overdue）**：**Citrix CVE-2026-88771／88772**。**即将 due 10-02**：**Apple CVE-2026-86950**。**即将 due 10-03**：**Cisco CVE-2026-76504**。
> X：`/workspace/x-posts-2026-09-30.json`（合并 **53** 条唯一：A25／B3／C11／LWiS14；跨源 ID 重叠 **0**；相对 prior seen_ids 重叠 **0**／**+53** 新 id；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **3h**。Search B 可见约 **11h**。Search C 约 **1h**。LWiS List 约 **24h**（**交叉校验，不假装为本窗口 24h Latest**；成员约 **501**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。抓取备注：Adobe APSB26-92 **403**；Citrix community bulletin **403**/Cloudflare；F5 myF5 鉴权墙；Arista curl **406**、WebFetch **200**（含公开 IoC）；CISA `/news-events/alerts` **404**（今日 Adds One 200）；CTX697096／MSRC SPA；tl;dr #348 软 404；部分 A／C 帖 t.co 未展开（卡片域名已在条目注明）。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露／勒索声称一律标 **UNCONFIRMED／未验证**；仅写谁／打什么／补丁与狩猎级防御摘要。

## 今日摘要

- **【主条 · KEV NEW · Cisco CVE-2026-76504】** CISA 于 **2026-09-30** 将 **CVE-2026-76504** 加入 KEV（catalog **2026.09.30／1730／Δ+1**）；联邦 due **2026-10-03**；forensicTriage=Yes；ransomware 使用 Unknown。Cisco Catalyst SD-WAN Manager：URI hex 编码致 API 认证绕过→admin（CVSS 9.8；Cisco PSIRT 称 2026-09 活跃利用）。固定版本示例：**20.9.10.1／20.12.8.2／20.15.6.1／20.18.4.1／26.1.2.1／26.2.1**；Cloud Managed **20.15.605**（用户侧无动作）。X A／LWiS 交叉（desmondsec2／VELO_ch／AzmyBlog／notCVE／Dinosn／BleepingComputer）。防御：On-Prem 尽快升固定版本并限制非受信访问；按厂商狩猎日志模式（编码 `j_security_check`、`viptela-reserved-` 用户）；BOD 26-04。**不转载利用步骤；未见独立恶意样本哈希／攻击者 C2 IP。**
  CISA Adds One：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
  厂商 cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
  文章（BC）：https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-sd-wan-authentication-bypass-zero-day-exploited-in-attacks/
  X（desmondsec2）：https://x.com/desmondsec2/status/2105436522543505563
  X（Dinosn／LWiS）：https://x.com/Dinosn/status/2105313998140764390

- **【due_today · Citrix 88771／88772 · 尚未 overdue】** KEV 自 09-27；联邦 due **2026-09-30＝今日**（bucket=due_today，**未**转入 newly_overdue）。88771 未认证命令执行；88772 内存边界不当→RCE/DoS；同族 CTX697096 覆盖 **88771–88778**。X A：sui_sys／nike49424。防御：立即按 CTX 升 ADC/Gateway（帖称示例 **14.1-73.37／13.1-64.23**，以厂商为准）；按 CTX694799 疑似沦陷取证；BOD 26-04。**本轮 enrich 未见可抄录具体哈希／IP。**
  CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
  CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
  CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
  X（sui_sys）：https://x.com/sui_sys/status/2105412872855863589
  X（nike49424）：https://x.com/nike49424/status/2105391484555907453

- **【upcoming · Apple CVE-2026-86950 due 10-02】** 昨 NEW 入 KEV；due **2026-10-02**。X A：navydoc001 称 Apple 为 86950 发紧急补丁（iOS/iPadOS **26.7.1**、macOS Tahoe **26.7.1**、Sequoia **15.8.1**）。防御：尽快更新受影响 Apple 设备；BOD 26-04。
  CISA Adds One（09-29）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
  Apple：https://support.apple.com/en-us/149226 · https://support.apple.com/en-us/149228 · https://support.apple.com/en-us/149229
  X（navydoc001）：https://x.com/navydoc001/status/2105437079354097673

- **【仍逾期亮点 19 · newly_overdue 空】** 无 dueDate=09-29 条目转入。昨 SharePoint **65660**／MikroTik **67279**／WP **87902** 继续 overdue。高信号：**Check Point 85102／93616**、**Arista 93952**（SA-0183 IoC）、**F5 94127**、**JFrog 42016／42018**、**Zyxel 7273**、MS／Chromium／Pixel／ISE／Acronis／WSO2／Adobe。防御：补丁落地核验与狩猎；BOD 26-04。
  Arista SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
  Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/

- **【X A 交叉 · Smart Slider／Plesk／K8s／GitLab／Zimbra／Bitget 声称等】** Smart Slider 3 **CVE-2026-14876**（修 **3.5.1.39**）；Plesk 18.0.81 Update 2／18.0.80 Update 9（critical，CVE 待定）；K8s **CVE-2026-2270** OwnerReference／GC；GitLab EE **CVE-2026-87719**（CVSS 9.9 称）；Zimbra **CVE-2026-73570**（KEV／在野转述）；Linux **CVE-2026-72018**；ManageEngine ADSSP **CVE-2026-74849**；Bitget「0-day 伪造热钱包提现」社交声称（**UNCONFIRMED**）。防御：按厂商补丁；勿采信未核验交易所事件细节。

- **【工具／新闻】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** **无升版**；Risky **新 RBNEWS617**（ShinyHunters suspect arrested in the Netherlands，2026-09-30）；SRB 仍 **SRB184a**／BTN 仍 **BTN184**；tl;dr 仍 **#347**（#348 软 404）。X B（~11h）：**Lockjaw** C2／**DeepTeam**／**AdaptixC2 serverless** 插件（授权评估语境）。LWiS：RustHound-CE、WatchGuard Fireware、Entra ID 脚本注入缓解、XProtect 5363、awesome-agent-skills-security 等。

- **【APT／Malware · 大量 UNCONFIRMED】** C（~1h）：Japan Times／Eclipse、CNEH／Kairos、Houston Thyroid／N0n、Software Answers／pear 等勒索声称；ULOS E／aurora／Globe Telecom／Kafiil 等泄露声称——**一律 UNCONFIRMED**。较有信号：LunexStealer BYOVD（AMD PDFWKRNL CVE-2023-20598）研究转述；LWiS C-suite M365 钓鱼＋RMM；Oxygen Forensics 执法供应链报道；DIVD 入侵二手转述。

- **【合并统计】** X **53** 唯一（A25／B3／C11／LWiS14；cross **0**；prior **0**；**+53** NEW）；`logged_in=true`／`@seogoogle4`／`blocked=false`；覆盖 A~3h／B~11h／C~1h／LWiS~24h；seen_ids **2196→2249**；报告 `/home/box/workspace/security-watch/reports/2026-09-30-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【KEV NEW · due 10-03】Cisco Catalyst SD-WAN Manager CVE-2026-76504

CISA 于 **2026-09-30** 加入 KEV；联邦 due **2026-10-03**。URI hex 编码绕过 Web／API 认证规则 → 未认证管理员访问；CVSS **9.8**；forensicTriage=Yes；knownRansomwareCampaignUse=Unknown。Cisco PSIRT 称 **2026-09** 活跃利用。固定版本示例：**20.9.10.1／20.12.8.2／20.15.6.1／20.18.4.1／26.1.2.1／26.2.1**；早于 20.9 需迁固定发行；Cisco Managed Cloud **20.15.605**（用户侧无动作）。防御：On-Prem 尽快升级并限制非受信网络访问；审计下列狩猎日志；BOD 26-04。**不转载利用步骤。**

地址：
- CISA Adds One：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76504
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-76504
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-76504
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/cisco-warns-of-new-sd-wan-authentication-bypass-zero-day-exploited-in-attacks/
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- X（desmondsec2）：https://x.com/desmondsec2/status/2105436522543505563
- X（VELO_ch）：https://x.com/VELO_ch/status/2105430740725055627
- X（AzmyBlog）：https://x.com/AzmyBlog/status/2105413005676892629
- X（notCVE）：https://x.com/notCVE/status/2105392429348049328
- X（Dinosn／LWiS）：https://x.com/Dinosn/status/2105313998140764390

IoC（厂商 SA／今日 enrich 狩猎级日志模式原样；**未见**独立恶意文件哈希或攻击者 C2 IP；示例私网 IP 非威胁情报 IoC）：
- 日志：`/var/log/nms/containers/service-proxy/serviceproxy-access.log` — 审计含 URI 编码字符的 `j_security_check`（例 `POST /%6a_security_check`；任一单字符编码均可）来自未知／未授权 IP
- 日志：`/var/log/nms/vmanage-server.log` — 审计 `j_security_check` 且用户名以 `viptela-reserved-` 开头的请求

### 2. 【due_today · 尚未 overdue · 在野】Citrix NetScaler CVE-2026-88771／CVE-2026-88772

CISA 于 **2026-09-27** 加入 KEV；联邦 due **2026-09-30＝今日**（**due_today**，**尚未**计入 newly_overdue／overdue）。88771：不当输入验证 → 未认证命令执行。88772：内存边界限制不当 → RCE/DoS。同公告族 **CVE-2026-88771–88778**（CTX697096）。社区公告 Cloudflare/**403**；CTX697096 SPA。X A 交叉。防御：立即按 CTX 升 ADC/Gateway；按 CTX694799 疑似沦陷排查；限制管理面；BOD 26-04。**不转载利用步骤。**

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
- X（sui_sys）：https://x.com/sui_sys/status/2105412872855863589
- X（nike49424）：https://x.com/nike49424/status/2105391484555907453

IoC：未见公开 IoC（KEV／CTX 称厂商提供检查，可见抓取未列具体哈希／IP）。

### 3. 【upcoming · due 10-02】Apple Multiple Products CVE-2026-86950

CISA 于 **2026-09-29** 加入 KEV；联邦 due **2026-10-02**。CoreGraphics 越界写 → 任意代码执行。补丁示例：**iOS/iPadOS 26.7.1**、**macOS Tahoe 26.7.1**、**macOS Sequoia 15.8.1**。X A：navydoc001 紧急补丁提醒（正文未展开 Apple 公告外链）。防御：尽快更新；BOD 26-04。

地址：
- CISA Adds One（09-29）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 Apple 149226：https://support.apple.com/en-us/149226
- 厂商 Apple 149228：https://support.apple.com/en-us/149228
- 厂商 Apple 149229：https://support.apple.com/en-us/149229
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-86950
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-86950
- X（navydoc001）：https://x.com/navydoc001/status/2105437079354097673
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 4. 【仍逾期】SharePoint CVE-2026-65660／MikroTik CVE-2026-67279／WordPress CVE-2026-87902

昨 newly_overdue，今日归 **still_overdue**（due 曾=09-28）。**65660**：SharePoint 代码注入；按 MSRC／BOD 26-04。**67279**：MikroTik RouterOS；按九月安全公告。**87902**：WordPress Core 路径遍历→条件 RCE；升 GHSA 补丁版本。防御：补丁落地核验；暴露面与 forensic triage。

地址：
- SharePoint MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660
- MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
- WP GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
- NVD 65660：https://nvd.nist.gov/vuln/detail/CVE-2026-65660
- NVD 67279：https://nvd.nist.gov/vuln/detail/CVE-2026-67279
- NVD 87902：https://nvd.nist.gov/vuln/detail/CVE-2026-87902
- KEV 入口：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 5. 【仍逾期 · 在野】Check Point CVE-2026-85102／CVE-2026-93616

due 曾=09-25，继续 overdue。85102：VPN 不当证书校验。93616：管理面路径穿越。防御：按 SK 打 Jumbo／Hotfix；限制管理／VPN 面；证书 subject 狩猎；BOD 26-04。

地址：
- 厂商 SK85102：https://support.checkpoint.com/results/sk/sk1000117
- 厂商 SK93616：https://support.checkpoint.com/results/sk/sk1000171/
- Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
- NVD 85102：https://nvd.nist.gov/vuln/detail/CVE-2026-85102
- NVD 93616：https://nvd.nist.gov/vuln/detail/CVE-2026-93616
- KEV 85102：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85102
- KEV 93616：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-93616

IoC（厂商 SK／博客观测 cert_subject，原样带自昨日报告／enrich；非穷尽）：
- `CN=vpn,OU=users,O=global`
- `CN=vpn-user,OU=users,O=global`
- `CN=vpnuser,OU=users,O=global`

### 6. 【仍逾期 · 在野】Arista VeloCloud CVE-2026-93952

due 曾=09-25，继续 overdue。on-prem VCO 不当输入校验（在野）。修复示例：**VCO 5.2.3.16+／6.4.2.8+**。防御：升 on-prem VCO；限制 VCO Web 至可信管理网；按 SA-0183 狩猎；BOD 26-04。

地址：
- 厂商 SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-93952
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-93952

IoC（厂商 SA-0183／今日 enrich 原样，非穷尽）：
- 文件：`/usr/local/sbin/.vcnode.js`
- 文件：`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）
- 文件：`/etc/systemd/system/vc-sysmon.service`
- HTTP 头：`x-vc-opt`
- IP：`142.93.149.77`
- IP：`104.248.126.159`

### 7. 【仍逾期 · 合辑】F5／JFrog／Zyxel／MS／Chromium／Pixel／ISE／Acronis／WSO2／Adobe

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
- **Adobe CVE-2026-71362**：按 APSB26-92（helpx **403**）。https://helpx.adobe.com/security/products/magento/apsb26-92.html

除 ISE／Arista／Check Point 外，上列多数 **未见公开 IoC**。

### 8. 【X A】Smart Slider 3 CVE-2026-14876／Plesk 紧急更新

- **Smart Slider 3**（@mgn_jpn）：中危，称影响 80 万+ 站点，CVSS 6.4；修复 **3.5.1.39**；卡片 shindan.m-g-n.me；t.co 未展开。X：https://x.com/mgn_jpn/status/2105435990886121928 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-14876
- **Plesk Panel**（@ridvanyagli）：09-29 发布 **18.0.81 Update 2**、**18.0.80 Update 9**；厂商暂称 critical security issue，CVE 待定；卡片 docs.plesk.com Change Log；t.co 未展开。X：https://x.com/ridvanyagli/status/2105431116219920390 · 厂商变更日志入口：https://docs.plesk.com/

IoC：未见公开 IoC。

### 9. 【X A】Kubernetes CVE-2026-2270／GitLab EE CVE-2026-87719／内核与 Nginx 实验

- **K8s CVE-2026-2270**（@lnxsec）：StatefulSet UID／OwnerReference 可致跨 ns pod 绕过常规 GC 语义。X：https://x.com/lnxsec/status/2105435537385357399 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-2270
- **GitLab EE CVE-2026-87719**（@zoomeyebot）：不安全反序列化，CVSS 9.9 称，critical patch；ZoomEye 暴露面 dork（仅作暴露面情报）。X：https://x.com/zoomeyebot/status/2105428749999394929 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87719
- **Linux CVE-2026-53266**（ARP／分片）：https://x.com/lnxsec/status/2105415672532517033 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-53266
- **Linux CVE-2026-72018**（称 16-byte write→root；容器共享内核非边界）：https://x.com/_skinnyguinea/status/2105412060431692252 · 文章卡片 cybernews.com（t.co 未展开）· NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-72018
- **Nginx Rift CVE-2026-42945**（TryHackMe 实验语境；rewrite module heap overflow 称）：https://x.com/Ogunley68617855/status/2105415620129128850 · 卡片 tryhackme.com（t.co 未展开）· NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-42945

防御：按上游／发行版补丁；K8s 审 OwnerReference 策略；GitLab 打 critical patch。**不转载利用／实验步骤。**

IoC：未见公开 IoC。

### 10. 【X A · KEV 交叉】Zimbra CVE-2026-73570／ManageEngine CVE-2026-74849／其他

- **Zimbra CVE-2026-73570**（@DFIR_Radar／@TweetThreatNews）：称未认证 SMTP→凭据窃取／外传，KEV，CVSS 8.9 称；web shell／Zimclient2／AzCopy 横向移动转述。防御：按 Zimbra／CISA 公告补丁与狩猎；BOD 26-04。X：https://x.com/DFIR_Radar/status/2105403119030898963 · https://x.com/TweetThreatNews/status/2105402443399852198 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-73570 · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-73570
- **ManageEngine ADSelfService Plus CVE-2026-74849**（@HugoValters）：CVSS 9.8 称；建议升 build **7001+**。X：https://x.com/HugoValters/status/2105390726951657895 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-74849
- **CVE-2026-19445**（@ThreatAtlas）：UAF Critical／CVSS 9.2 称，厂商产品未指明——信号弱。X：https://x.com/ThreatAtlas/status/2105402714553504194
- **OpenSSL low**（@eris_dev 自称报告获署名）：https://x.com/eris_dev/status/2105410121136525532
- **Salesforce CVE 组合概览**（@HugoValters；称无 KEV 命中）：https://x.com/HugoValters/status/2105390978810953764
- **Bitget 0-day 热钱包提现声称**（@Alexka09）：**UNCONFIRMED／未验证**。X：https://x.com/Alexka09/status/2105436938333266009
- **GitLab sandbox／Hugging Face agent 供应链讨论**（@stretchcloud）：https://x.com/stretchcloud/status/2105436277512261819

IoC：未见公开 IoC（Zimbra 帖摘要未列可抄录哈希／IP）。

### 11. 【LWiS 交叉】WatchGuard Fireware／Spectre v2 变体／Entra ID

- **WatchGuard Fireware OS 严重代码注入**（厂商已修；帖未显 CVE）：文章 https://www.securityweek.com/watchguard-patches-critical-fireware-os-code-injection-vulnerability/ · X：https://x.com/Dinosn/status/2105313850190905470
- **Spectre v2 新变体**（Intel／AMD／Arm 数据泄漏风险报道；窗口边缘）：https://www.securityweek.com/new-spectre-v2-variant-exposes-intel-amd-arm-cpus-to-data-leaks/ · X：https://x.com/Dinosn/status/2104984875363147999
- **Microsoft 将自 10 月起阻断 Entra ID 脚本注入**：https://www.bleepingcomputer.com/news/security/microsoft-to-block-entra-id-script-injection-attacks-starting-october/ · X：https://x.com/Dinosn/status/2105313779542045182
- **Apple XProtect → 5363**（未披露对应问题）：https://eclecticlight.co/2026/09/30/apple-has-released-another-update-to-xprotect-for-all-macos/ · X：https://x.com/howardnoakley/status/2105177058758312015

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 核心工具版本（公开 pulse）

- **Sliver** 仍 **v1.7.7**（无升版）：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- **nuclei** 仍 **v3.11.1**（无升版）：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- **nuclei-templates** 仍 **v10.4.9**（无升版）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- Risky **新**：**RBNEWS617** https://risky.biz/RBNEWS617/（ShinyHunters suspect arrested in the Netherlands，2026-09-30）· 昨 **RBNEWS616** https://risky.biz/RBNEWS616/ · **BTN184** https://risky.biz/BTN184/ · SRB 仍 **SRB184a** https://risky.biz/SRB184a/
- tl;dr sec 仍 **#347**（无变化；#348 软 404）：https://tldrsec.com/p/tldr-sec-347

### X Search B（~11h；授权红队／模拟向；不写利用步骤）

- **Lockjaw**（Rust based Windows C2 Framework；仅授权评估语境）：https://github.com/g13net/lockjaw · X：https://x.com/ipurple/status/2105406520536027458
- **DeepTeam**（LLM／AI agent 红队框架）：https://github.com/confident-ai/deepteam · X：https://x.com/PythonHub/status/2105391045131309239
- **AdaptixC2 serverless transport plugin**（AWS Lambda＋DynamoDB relay；流量呈出站 HTTPS 至 AWS）：https://github.com/stillbigjosh/adaptix-serverless-c2 · X：https://x.com/ipurple/status/2105265660762763506

### LWiS 交叉工具／研究（~24h）

- **RustHound-CE 2.5.20**（SAMR LocalGroups／BloodHound 图关系）：X：https://x.com/g0h4n_0/status/2105213842112254413
- **awesome-agent-skills-security**（AI agent skill 攻防清单）：https://github.com/LLMSecurity/awesome-agent-skills-security · X：https://x.com/Dinosn/status/2105151005939597542
- **OpenVuln／GLM-5.3**（开源项目漏洞发现声明；数字未独立核验）：https://huggingface.co/spaces/zai-org/OpenVuln · X：https://x.com/ZixuanLi_/status/2105120154329977240
- **WinDbg DbgEng 句柄泄漏**（工程缺陷提示）：X：https://x.com/TwoSevenOneT/status/2105316207696154756
- **HackerOne／Vercel 供应链漏洞讨论**（发帖者描述，无 CVE）：X：https://x.com/S1r1u5_/status/2105322479556386911

IoC：工具帖未见公开 IoC。

## APT / Malware 分析

### 1. 【X A · 研究转述】LunexStealer BYOVD（AMD PDFWKRNL）

@_josehelps 转述 PolySwarm／Ontinue：假 CAPTCHA → AMD **PDFWKRNL.sys**（**CVE-2023-20598**）BYOVD → 清零内核回调 → LunexStealer 与 Native Messaging Host 持久化。防御：关注驱动白名单／BYOVD 狩猎；浏览器扩展／Native Messaging 异常。外链卡片 hubspotemail.net（t.co 未展开）。**不转载操作步骤。**

地址：
- X：https://x.com/_josehelps/status/2105402557611065803
- NVD（历史驱动 CVE）：https://nvd.nist.gov/vuln/detail/CVE-2023-20598

IoC：未见公开 IoC（帖摘要未列哈希／IP）。

### 2. 【LWiS】C-suite M365 钓鱼＋RMM／Oxygen Forensics／车载窃听警告

- **美国高管钓鱼窃取 M365 会话并部署 RMM**（The Hacker News）：https://thehackernews.com/2026/09/us-focused-csuite-phishing-steals.html · X：https://x.com/Dinosn/status/2105313901868941322
- **Oxygen Forensics 据称长期存在于欧洲警察部门**（SecurityAffairs；供应链／执法暴露面线索）：https://securityaffairs.com/200090/intelligence/oxygen-forensics-a-russian-run-forensics-firm-spent-a-decade-inside-european-police-departments.html · X：https://x.com/Dinosn/status/2105313805635088785
- **AIVD 警告车内机密谈话**（现代汽车麦克风可被远程开启等转述）：X：https://x.com/IntCyberDigest/status/2105254099587305521

IoC：未见公开 IoC。

### 3. 【X C · 未验证】勒索软件事件声称（合辑）

以下均为社交列表报道，**一律 UNCONFIRMED／未验证**：

- **The Japan Times** 据报遭 **Eclipse**（FalconFeeds／ThreatAtlas）：https://x.com/FalconFeedsio/status/2105436575127699799 · https://x.com/ThreatAtlas/status/2105420014786339072 · 站点：https://japantimes.co.jp/
- **CNEH**（法国）据报遭 **Kairos**：https://x.com/FalconFeedsio/status/2105434852707492339 · 站点：https://cneh.fr/
- **Houston Thyroid & Endocrine Specialists** 据报遭 **N0n**（帖内日期写 2026-10-01，需核验）：https://x.com/ThreatAtlas/status/2105429107634737247
- **Software Answers（Banyan）** 据报遭 **pear**：https://x.com/ThreatAtlas/status/2105428942010142812

IoC：未见公开 IoC。

### 4. 【X C · 未验证】地下泄露／售卖声称（合辑）

**一律 UNCONFIRMED／未验证**：

- ULOSE／newyjh[.]com 数据库声称：https://x.com/intels_daily/status/2105434296605450445
- aurora／Buford-Thompson ~350 QuickBooks 记录声称：https://x.com/intels_daily/status/2105431336211091668
- 克罗地亚博彩用户资料＋赌场 RCE／面板声称：https://x.com/DailyDarkWeb/status/2105427113679716404
- Porman2344／Globe Telecom＋Converge ICT 声称：https://x.com/intels_daily/status/2105419191482200138
- Kafiil（kafiil[.]com）用户数据声称：https://x.com/DailyDarkWeb/status/2105411754604068886

IoC：未见可核验公开 IoC（仅帖文域名转述，不作确认）。

### 5. 【X C】其他

- **DIVD 基础设施入侵**（二手转述；「Agentic AI」未证实）：https://x.com/xbhaveshverma/status/2105424952639754685

### 6. ICS

本日公开备援主条以 **KEV NEW Cisco 76504**、**due_today Citrix 88771／88772**、**仍逾期网关／编排／APM／VPN** 与 **upcoming Apple／Cisco** 为主；**无单独新突出的 2026-09-30 ICS advisory 主条**。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Cisco SD-WAN CVE-2026-76504（NEW）**：狩猎日志 `/var/log/nms/containers/service-proxy/serviceproxy-access.log`（编码 `j_security_check`，例 `/%6a_security_check`）；`/var/log/nms/vmanage-server.log`（`viptela-reserved-` 用户＋j_security_check）。**未见**独立恶意文件哈希／攻击者 C2 IP。（来源：cisco-sa-sdwan／`/workspace/enrich-2026-09-30/cisco-sa-sdwan-CVE-2026-76504-iocs.json`）
- **Arista VeloCloud CVE-2026-93952（仍逾期）**：`/usr/local/sbin/.vcnode.js`；`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）；`/etc/systemd/system/vc-sysmon.service`；HTTP 头 `x-vc-opt`；IP `142.93.149.77`／`104.248.126.159`。（来源：今日 enrich／SA-0183）
- **Check Point 85102／93616（仍逾期）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`。（来源：昨日报告／厂商 SK／enrich）
- **Cisco ISE 76460（仍逾期）**：狩猎示例 `admin#show logging application ise-kong/access.log | include dummyuser`；路径 `./ise/logs/apigateway/access.log`。（来源：昨日报告／Cisco SA）
- **Citrix due_today／Apple 86950／仍逾期其余／工具仓／C 勒索与泄露声称**：未见可抄录公开 IoC（或仅厂商原文内；C 帖多为域名转述且 **UNCONFIRMED**）
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

本窗口 LWiS List 只读采集：扫描约 **62** 条、保留 **14** 条、覆盖约 **24h**（`logged_in=true`／`@seogoogle4`／`blocked=false`；成员约 **501**）；跨源 ID 重叠 0（相对 A／B／C）；含 Cisco SD-WAN 交叉、C-suite 钓鱼、WatchGuard、Entra ID、XProtect、RustHound-CE、Oxygen Forensics、Spectre 变体等；meta：`/workspace/x-lwis-list-meta-2026-09-30.json`。

## 来源搜索 URL

- X Latest A（CVE／0-day）：https://x.com/search?q=%28CVE%20OR%20%220-day%22%20OR%200day%29%20-filter%3Areplies&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／cobalt／implant／threat hunting）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20%22red-team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt%20OR%20implant%20OR%20%22threat%20hunting%22)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS617：https://risky.biz/RBNEWS617/
- Risky RBNEWS616：https://risky.biz/RBNEWS616/
- Risky SRB184a：https://risky.biz/SRB184a/
- Risky BTN184：https://risky.biz/BTN184/
- tl;dr sec：https://tldrsec.com/
- tl;dr #347：https://tldrsec.com/p/tldr-sec-347
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 09-30 Adds One（Cisco 76504）：https://www.cisa.gov/news-events/alerts/2026/09/30/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-29 Adds One（Apple 86950）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-27 Adds Two（Citrix 88771／88772）：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 09-27 Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- 厂商 Cisco SD-WAN：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
