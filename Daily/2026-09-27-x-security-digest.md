# X 安全情报晚报 · 2026-09-27

> 搜集窗口：圣地亚哥时间 **2026-09-26 20:00 至 2026-09-27 ~20:35**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周日）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-27.json`（collected_at **2026-09-27T20:16:50-03:00**）＋ `/workspace/tools-news-pulse-2026-09-27.json`＋ `/workspace/enrich-extra-2026-09-27.json`＋ `/workspace/enrich-2026-09-27/`。CISA KEV catalogVersion **2026.09.27**／**1728** 条／dateReleased **2026-09-27T21:30:35.5521Z**（相对昨日 **2026.09.25／1726**：**count Δ+2**；**NEW** Citrix **CVE-2026-88771／88772** dateAdded=2026-09-27；**due_today** WSO2 **5430**／Adobe **71362**；**newly_overdue 无**；**仍逾期 14**；**upcoming** 09-28 SharePoint／MikroTik／WP，09-30 Citrix 两枚 NEW）。今日 CISA「Adds Two」：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
> **仍逾期（含昨日转入）**：**Check Point CVE-2026-85102／93616**、**Arista VeloCloud CVE-2026-93952**、**F5 BIG-IP APM CVE-2026-94127**、**JFrog Artifactory CVE-2026-42016／42018**、**Zyxel CVE-2026-7273**、**MS CVE-2026-81963／85880**、**Chromium CVE-2026-87491／85046**、**Pixel CVE-2026-58704**、**Cisco ISE CVE-2026-76460**、**Acronis CVE-2026-87886**。**due_today（09-27）**：**WSO2 CVE-2026-5430**／**Adobe CVE-2026-71362**。**即将 due 09-28**：**SharePoint CVE-2026-65660**／**MikroTik CVE-2026-67279**／**WordPress CVE-2026-87902**。
> X：`/workspace/x-posts-2026-09-27.json`（合并 **34** 条唯一：A12／B10／C9／LWiS3；跨源 ID 重叠 **0**；相对 prior seen_ids 重叠 **4**／**+30** 新 id；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **1h**。Search B 可见约 **48h**（含 Sep 25–27 工具帖，其中 4 条已见 prior）。Search C 约 **6h**。LWiS List 约 **15h**（**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。抓取备注：Adobe APSB26-92 box 出口 **403**；Citrix community bulletin **403**；F5 myF5 鉴权墙；Arista SA-0183 curl/urllib **406**、WebFetch **200**（含公开 IoC）；Pixel OAuth **302**；Acronis JS 墙。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【主条 · KEV Δ+2 · NEW Citrix 88771／88772】** CISA KEV 升至 catalogVersion **2026.09.27**／**1728** 条／dateReleased **2026-09-27T21:30:35.5521Z**（相对昨日 **2026.09.25／1726**：**Δ+2**）。**NEW**：**CVE-2026-88771**（NetScaler 不当输入验证→未认证命令执行）／**CVE-2026-88772**（内存边界限制不当→RCE/DoS）；联邦 due **2026-09-30**；CISA 今日「Adds Two」。厂商：CTX697096／CTX694799／community bulletin（88771–88778）。X 交叉：A 多帖确认在野＋LWiS @TheHackersNews／@cyb3rops。防御：立即按 CTX 升版；按 CTX694799 疑似沦陷取证；BOD 26-04。
  CISA Adds Two：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
  CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
  CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
  Community bulletin：https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778
  X（THN／LWiS）：https://x.com/TheHackersNews/status/2104245184041234553
  X（cyb3rops／LWiS）：https://x.com/cyb3rops/status/2104348877776380316
  X（Deyda checklist）：https://x.com/Deyda84/status/2104345850059391201
  BC 转述：https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/

- **【due_today · WSO2 5430／Adobe 71362】** 联邦 due **2026-09-27**：**CVE-2026-5430**（WSO2 多产品路径遍历→上传/RCE；按 WSO2-2026-5328 升 Update Level）／**CVE-2026-71362**（Adobe Commerce/Magento 不正确授权；按 APSB26-92，helpx 出口 **403**）。防御：今日到期项优先落地补丁；BOD 26-04。
  WSO2：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
  APSB26-92：https://helpx.adobe.com/security/products/magento/apsb26-92.html

- **【仍逾期 · Check Point／Arista／F5／JFrog／Zyxel／MS／Chromium／Pixel／ISE／Acronis】** **newly_overdue 今日为 0**（昨日新逾期 6 条转入仍逾期）。仍逾期高信号：**Check Point 85102／93616**（cert_subject IoC 见昨日厂商/enrich，今日 enrich-extra 未重抄）、**Arista 93952**（SA-0183 含文件/MD5/IP IoC）、**F5 94127**、**JFrog 42016／42018**、**Zyxel 7273**、MS **81963／85880**、Chromium **87491／85046**、Pixel **58704**、Cisco ISE **76460**、Acronis **87886**。防御：核验补丁落地与狩猎；BOD 26-04。
  Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
  Arista SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
  F5 K000162605：https://my.f5.com/manage/s/article/K000162605
  JFrog advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories

- **【即将 due 09-28 · SharePoint／MikroTik／WP】** **CVE-2026-65660**／**67279**／**87902** 联邦 due **09-28**。防御：按 MSRC／MikroTik 九月公告／WP GHSA 升版；BOD 26-04。
  SharePoint MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660
  MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
  WP GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp

- **【X 高信号 · Elementor／PHP SOAP／ServiceNow／PeopleSoft／Magento】** A（~1h）：**Elementor CSRF CVE-2026-62062**（升 4.3.2；Patchstack）；**PHP SOAP CVE-2026-91765**（8.2.34／8.3.35／8.4.26／8.5.11）；**ServiceNow AI Platform** 五漏洞含 **13016／86860**；**Oracle PeopleSoft CVE-2026-35273**（Mandiant／GTIG／UNC6240 转述，帖列路径/IP IoC）；**Magento StyleSmuggler CVE-2026-75650** 店主自述事件——**UNCONFIRMED**；另有 Obot Docker **CVE-2026-101065**。

- **【工具／新闻】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** **无升版**；Risky 仍 **RBNEWS615**（https://risky.biz/RBNEWS615/）／SRB184（https://risky.biz/SRB184a/）／BTN183；tl;dr 仍 **#347**（https://tldrsec.com/p/tldr-sec-347）。X B：Red-Team-Roadmap／GOAD Lab／notRDP／ai-blackteam／Sockpuppets／Sliver BOF／Mythic／Adaptix Graph C2／**Comment2Shell**（PoC 仓——**UNCONFIRMED／仅授权评估**）等。

- **【APT／Malware】** C（~6h）：Anthropic 九月威胁报告（俄关联 AI 工作流间谍／多智能体滥用案例）X 转述；多起地下泄露／访问售卖（Kiassure、Bangladesh Army／MikroTik、US LE/IC、Ronis、Scorenco、ITESHU phpMyAdmin）——**一律 UNCONFIRMED**。LWiS（~15h）：Citrix 交叉＋@dinodaizovi AI/安全工程讨论。

- **【合并统计】** X **34** 唯一（A12／B10／C9／LWiS3；cross **0**；prior **4**；**+30** NEW）；`logged_in=true`／`@seogoogle4`／`blocked=false`；覆盖 A~1h／B~48h／C~6h／LWiS~15h；seen_ids **2081→2111**；报告 `/home/box/workspace/security-watch/reports/2026-09-27-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【NEW · KEV · 在野】Citrix NetScaler CVE-2026-88771／CVE-2026-88772

CISA 于 **2026-09-27** 将两枚加入 KEV（catalogVersion **2026.09.27**／count **1728**／Δ+2）；联邦 due **2026-09-30**。88771：不当输入验证 → 未认证命令执行。88772：内存边界限制不当 → RCE/DoS。同公告族覆盖 **CVE-2026-88771–88778**（CTX697096）。KEV 备注称可在 NetScaler 控制台运行厂商提供的 IoC 检查，并要求按 BOD 26-04 做 forensic triage；本轮 enrich／厂商页可见内容 **未见可抄录具体哈希／IP IoC**（CTX694799 为应急步骤页）。X A＋LWiS 今日密集交叉（THN／cyb3rops／Deyda／CISA Adds Two 链接等）。防御：立即按 CTX 升 ADC/Gateway；按 CTX694799 疑似沦陷排查；限制管理面；BOD 26-04。**不转载利用步骤。**

地址：
- CISA Adds Two：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 厂商 CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
- 厂商 CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
- Community bulletin：https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778
- NVD 88771：https://nvd.nist.gov/vuln/detail/CVE-2026-88771
- NVD 88772：https://nvd.nist.gov/vuln/detail/CVE-2026-88772
- KEV 88771：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88771
- KEV 88772：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88772
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- X（THN／LWiS）：https://x.com/TheHackersNews/status/2104245184041234553
- X（cyb3rops／LWiS）：https://x.com/cyb3rops/status/2104348877776380316
- X（Deyda）：https://x.com/Deyda84/status/2104345850059391201 · 文章：https://www.deyda.net/index.php/de/2026/08/28/netscaler-cve-checkliste-updates-sicherheitspruefung-und-incident-response/
- X（yousukezan）：https://x.com/yousukezan/status/2104345432310890661 · https://securityonline.info/citrix-netscaler-zero-day-rce/
- X（theNovacyberqfs）：https://x.com/theNovacyberqfs/status/2104344325396291718
- X（taku888infinity）：https://x.com/taku888infinity/status/2104344053764772114 · BC：https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/
- X（HashgraphOnline）：https://x.com/HashgraphOnline/status/2104342575616573730 · https://hol.org/blog/cve-2026-88771-netscaler-unauthenticated-rce
- X（__kokumoto／CISA Adds Two）：https://x.com/__kokumoto/status/2104340752415555968

IoC：未见公开 IoC（KEV／CTX 称厂商提供检查，可见抓取未列具体指标）。

### 2. 【due_today】WSO2 CVE-2026-5430

联邦 due **2026-09-27**。多产品路径遍历 → 上传/RCE。防御：按 **WSO2-2026-5328** 将受影响产品升至公告 Update Level（例：API Control Plane 4.6.0→UL22；API Manager 4.6.0→UL21 等）；BOD 26-04。

地址：
- 厂商：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-5430
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-5430
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 3. 【due_today】Adobe Commerce／Magento CVE-2026-71362

联邦 due **2026-09-27**。不正确授权。防御：按 **APSB26-92** 应用厂商补丁；BOD 26-04。（helpx box 出口 **403**，仍列已知厂商 URL；NVD 作备援。）

地址：
- 厂商 APSB26-92：https://helpx.adobe.com/security/products/magento/apsb26-92.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-71362
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-71362
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 4. 【仍逾期 · 在野】Check Point CVE-2026-85102／CVE-2026-93616

CISA 于 **2026-09-22** 加入 KEV；联邦 due 曾为 **2026-09-25**，继续 **still_overdue**。85102：VPN 不当证书校验 → 未认证 RCE。93616：管理面路径穿越 → 未认证脚本上传／执行。今日 enrich-extra 对应条目写「未见公开 IoC」；**cert_subject 狩猎指标原样带自昨日报告／昨日厂商 SK／enrich**（注明来源）。防御：立即按 SK 打 Jumbo／Hotfix；限制管理／VPN 面；证书 subject 狩猎；BOD 26-04。**不转载利用步骤。**

地址：
- 厂商 SK85102：https://support.checkpoint.com/results/sk/sk1000117
- 厂商 SK93616：https://support.checkpoint.com/results/sk/sk1000171/
- Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
- NVD 85102：https://nvd.nist.gov/vuln/detail/CVE-2026-85102
- NVD 93616：https://nvd.nist.gov/vuln/detail/CVE-2026-93616
- KEV 85102：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85102
- KEV 93616：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-93616
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC（厂商 SK／博客观测 cert_subject，原样抄录自昨日报告／昨日 enrich vendor，非穷尽；今日 enrich-extra 未重抄）：
- `CN=vpn,OU=users,O=global`
- `CN=vpn-user,OU=users,O=global`
- `CN=vpnuser,OU=users,O=global`

### 5. 【仍逾期 · 在野】Arista VeloCloud CVE-2026-93952

KEV due 曾为 **2026-09-25**，继续 overdue。on-prem VCO 不当输入校验（CVSS 10，在野）。修复示例：**VCO 5.2.3.16+／6.4.2.8+**。防御：升 on-prem VCO；将 VCO Web 限制到可信管理网；按 SA-0183 狩猎下列 IoC；BOD 26-04。（抓取：curl/urllib **406**，WebFetch **200**。）

地址：
- 厂商 SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-93952
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-93952
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC（厂商 SA-0183／今日 enrich-extra 原样抄录，非穷尽）：
- 文件：`/usr/local/sbin/.vcnode.js`
- 文件：`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）
- 文件：`/etc/systemd/system/vc-sysmon.service`
- HTTP 头：`x-vc-opt`
- IP：`142.93.149.77`
- IP：`104.248.126.159`

### 6. 【仍逾期 · 在野】F5 BIG-IP APM CVE-2026-94127

KEV due 曾为 **2026-09-25**，继续 overdue。堆溢出 → 未认证数据面 RCE（APM＋OAuth profile 场景）。防御：按 K000162605 先临时 iRule，完成取证后装最终补丁；BOD 26-04。（myF5 鉴权墙，仍列已知厂商 URL。）

地址：
- 厂商 K000162605：https://my.f5.com/manage/s/article/K000162605
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94127
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-94127
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 7. 【仍逾期 · near】JFrog Artifactory CVE-2026-42016／CVE-2026-42018

due 曾为 **2026-09-25**，继续 overdue。42016：令牌授权校验错误提权（修复示例 **≥7.133.11**）。42018：匿名令牌暴露（受影响分支含 <7.111.20；7.117.0–7.117.27；7.125.0–7.125.19；7.133.0–7.133.28；7.146.0–7.146.8）。防御：按 JFrog Security Advisories／Self-Managed Releases 升版；限制管理面。

地址：
- NVD 42016：https://nvd.nist.gov/vuln/detail/CVE-2026-42016
- NVD 42018：https://nvd.nist.gov/vuln/detail/CVE-2026-42018
- KEV 42016：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-42016
- KEV 42018：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-42018
- 厂商 advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- 发行说明：https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases

IoC：未见公开 IoC。

### 8. 【仍逾期】Zyxel／Microsoft／Chromium／Pixel／Cisco ISE／Acronis（合辑）

- **Zyxel GS1900 CVE-2026-7273**（due 曾=09-24）：升 **2.90(*.2)C0**；限制 LAN 管理面。厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273 · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273
- **MS CVE-2026-81963／85880**（due 曾=09-22）：确认九月补丁。MSRC：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963 · https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880
- **Chromium CVE-2026-87491**（due 曾=09-23）：升 **153.0.8010.36+**。https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- **Chromium CVE-2026-85046**（due 曾=09-18）：尽快升级。https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- **Pixel CVE-2026-58704**（due 曾=09-19）：装 Pixel 2026-09-01 更新（source.android OAuth 环）。https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- **Cisco ISE CVE-2026-76460**（due 曾=09-19）：升 First Fixed（3.1→P12／3.2→P11／3.3→P12／3.4→P7／3.5→P4）。https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  IoC（厂商 SA／enrich 原样）：`admin#show logging application ise-kong/access.log | include dummyuser`；日志路径 `./ise/logs/apigateway/access.log`
- **Acronis CVE-2026-87886**（due 曾=09-19）：按 SEC-10986（JS 墙）。https://security-advisory.acronis.com/advisories/SEC-10986

除 ISE 狩猎示例外，上列多数 **未见公开 IoC**。

### 9. 【即将 due 09-28】SharePoint／MikroTik／WordPress

- **CVE-2026-65660** Microsoft SharePoint 代码注入；due **09-28**；forensicTriage=Yes。MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660 · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-65660
- **CVE-2026-67279** MikroTik RouterOS；due **09-28**；可与 MikroTrick／CVE-2026-86060 链式语境。https://mikrotik.com/supportsec/september-2026-vulnerability/ · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-67279
- **CVE-2026-87902** WordPress Core 远程文件包含／条件 RCE；due **09-28**；升 GHSA 所列补丁版本（如 7.1.2／7.0.6／6.9.9…）。https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87902

IoC：未见公开 IoC。

### 10. 【X A】Elementor CSRF CVE-2026-62062

WordPress Elementor 插件 CSRF；帖称影响 4.3.0／4.3.1，补丁 **4.3.2**；Patchstack 文章。防御：升 Elementor≥4.3.2；审查已登录用户点击风险。

地址：
- X：https://x.com/MalwareBibleJP/status/2104341821904339173
- Patchstack：https://patchstack.com/articles/cross-site-request-forgery-in-elementor-plugin-affecting-2-million-sites/
- NVD（若已收录）：https://nvd.nist.gov/vuln/detail/CVE-2026-62062

IoC：未见公开 IoC。

### 11. 【X A】PHP SOAP CVE-2026-91765

PHP 安全发布 **8.2.34／8.3.35／8.4.26／8.5.11**；帖称 SOAP **CVE-2026-91765** CVSS 7.5。防御：升至对应安全版本。

地址：
- X：https://x.com/securityLab_jp/status/2104338088629854237
- 文章：https://rocket-boys.co.jp/security-measures-lab/php-security-release-8-2-34-8-3-35-8-4-26-8-5-11/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-91765

IoC：未见公开 IoC。

### 12. 【X A】ServiceNow AI Platform（含 CVE-2026-13016／86860 等）

帖称 ServiceNow AI Platform 九月五漏洞（含 **CVE-2026-13016**、**CVE-2026-86860** 等；标签含未认证 SQLi／critical）。防御：按厂商／转述文章盘点补丁窗口；限制暴露面。

地址：
- X：https://x.com/securityLab_jp/status/2104345645738078302
- 文章：https://rocket-boys.co.jp/security-measures-lab/servicenow-ai-platform-september-2026-five-vulnerabilities-cve-2026-13016/

IoC：未见公开 IoC。

### 13. 【X A · Mandiant 转述】Oracle PeopleSoft CVE-2026-35273

@Python_s_ 转述 Mandiant／GTIG：UNC6240（ShinyHunters）对 **CVE-2026-35273** 续作大规模利用，并称 WAF 旁路路径 `/%50SEMHUB/` 等。防御：PeopleSoft／PSEMHUB 暴露面盘点与补丁；对照 Mandiant 原文狩猎 web shell／后门；BOD 26-04／KEV 语境。**不转载利用步骤。**（采集 tags 含 UNCONFIRMED；Mandiant 主文为权威交叉。）

地址：
- X：https://x.com/Python_s_/status/2104338288664268801
- Mandiant／GTIG：https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft
- Oracle：https://www.oracle.com/security-alerts/alert-cve-2026-35273.html
- KEV 检索：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-35273

IoC（原样抄录自该 X 帖列表，供狩猎；以 Mandiant 原文为准核验）：
- 路径：`/%50SEMHUB/`
- 文件／名：`x.jsp`／`u.jsp`／`Ple64.exe`／`tunnel.jsp`／`tunnel.jspx`
- IP：`5.199.162.157`／`104.219.234.138`／`162.219.30.165`

### 14. 【X A · UNCONFIRMED】Magento StyleSmuggler CVE-2026-75650

@darkkingii 自述 Magento 2.4.8 店于 09-20–22 遭 **CVE-2026-75650**（StyleSmuggler／CVSS 10）攻击并清 webshell——**事件细节 UNCONFIRMED**（第一人称社媒声称）。防御：关注 Adobe 相关安全公告与 Magento 上传面加固；勿照抄攻击步骤。

地址：
- X：https://x.com/darkkingii/status/2104331253583409606
- Adobe security 入口：https://helpx.adobe.com/security.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-75650

IoC（帖列路径／特征，**UNCONFIRMED**）：`pub/media/custom_options/quote/`；`/customer/address_file/upload`；`/rest/V1/guest-carts`；`template_styles`；`*.php`；`@nx.invalid`

### 15. 【X A】Obot Docker CVE-2026-101065

希腊语短帖：Obot 关键漏洞致 Docker 失控语境。防御：关注 SecNews 原文与厂商修复。

地址：
- X：https://x.com/SecNews_GR/status/2104336060826226873
- 文章：https://www.secnews.gr/736328/cve-2026-101065-obot-docker/?fsp_sid=15197

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 核心工具版本（公开 pulse）

- **Sliver** 仍 **v1.7.7**（无升版）：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- **nuclei** 仍 **v3.11.1**（无升版）：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- **nuclei-templates** 仍 **v10.4.9**（无升版）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- Risky：**RBNEWS615** https://risky.biz/RBNEWS615/ · **SRB184a** https://risky.biz/SRB184a/ · **BTN183** https://risky.biz/BTN183/（均未变）
- tl;dr sec 仍 **#347**：https://tldrsec.com/p/tldr-sec-347

### X Search B（~48h；授权红队／模拟向；不写利用步骤）

- **Red-Team-Roadmap**（教育路径；Windows PE 模块笔记）：https://github.com/Dev-Chukwuma/Red-Team-Roadmap · X：https://x.com/httpschuks/status/2104297168995852611
- **Red-Team-GOAD-Lab-Proxmox**（GOAD／Proxmox／pfSense 家用实验室指南）：https://github.com/pho5nix/Red-Team-GOAD-Lab-Proxmox · X：https://x.com/ipurple/status/2104241939923263695
- **notRDP**（Havoc C2 插件；隐式桌面／浏览器查看器——仅授权仿真）：https://github.com/dagowda/notRDP · X：https://x.com/ipurple/status/2104161092469448967
- **ai-blackteam／ai-evals**（LLM 红队评估工具宣传）：https://github.com/BILLKISHORE/ai-evals · https://ai-blackteam.ai-evals.workers.dev/ · X：https://x.com/Spark82804016/status/2104099697539568086
- **Sockpuppets**（开源 C2 声称；仅授权对手模拟）：https://github.com/ajm4n/sockpuppets · X：https://x.com/AJHammond/status/2104031639651450915
- **Sliver CS-Situational-Awareness-BOF**（跨平台 BOF；当前 release v1.7.7 语境）：https://github.com/sliverarmory/CS-Situational-Awareness-BOF · 文档：https://sliver.sh/docs/?name=Cross-platform+BOFs · X：https://x.com/LittleJoeTables/status/2103914959264760196
- **Sliver**（BishopFox；prior_seen）：https://github.com/BishopFox/sliver · X：https://x.com/AlAssaf_H/status/2103850433219268943
- **Mythic**（多代理 C2；prior_seen）：https://github.com/its-a-feature/Mythic · X：https://x.com/AlAssaf_H/status/2103850054997963011
- **adaptix-graph-c2**（Azure Blob／OneDrive dead-drop 信道；prior_seen）：https://github.com/stillbigjosh/adaptix-graph-c2 · 文章：https://stillbigjosh.com/writeup.html?file=writeups/adaptix-graph-c2.md · X：https://x.com/stillbigjosh/status/2103455702945796331
- **Comment2Shell**（WP 预认证 XSS→RCE 链 PoC／Nuclei／Docker lab——**UNCONFIRMED／仅授权评估**；prior_seen）：https://github.com/DeathShotXD/Comment2Shell · X：https://x.com/XssPayloads/status/2103440816941523278

IoC：工具帖未见公开 IoC（Comment2Shell 仓含 PoC 材料——不转载步骤）。

### LWiS 交叉（~15h；不假装 24h Latest）

- **Citrix NetScaler 告警**（@cyb3rops／@TheHackersNews）：见 CVE 节第 1 条。
- **@dinodaizovi** AI／安全工程可利用性讨论（OpenSSH／Firecracker／seL4 语境）：https://x.com/dinodaizovi/status/2104115286647472518

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. 【X C】Anthropic 九月威胁报告（转述）

@AIRiskNetwork／@zenjin_ai 讨论 Anthropic September threat report：俄关联间谍行动使用 AI 工作流针对 20+ 组织（含政府部门）；安全工具检出恶意软件后 AI 重建再部署；以及多智能体、少人工逐步介入的滥用案例。**帖未附文章 URL**。防御：关注 Anthropic 原文案例对 AI 工作流治理与检测的启示；勿将社媒摘要当作完整报告。

地址：
- X：https://x.com/AIRiskNetwork/status/2104266838716694651
- X：https://x.com/zenjin_ai/status/2104300043444396540

IoC：未见公开 IoC。

### 2. 【X C】Assemblyline 4 恶意软件分析框架（加拿大 Cyber Centre）

开源文件 triage／API／Docker/K8s——蓝队向。

地址：
- X：https://x.com/EsGeeks/status/2104288017913393650
- 帖文提及（截断）：`github.com/CybercentreCan…`（未给出可核验完整仓库 URL；不编造完整路径）

IoC：未见公开 IoC。

### 3. 【X C · 未验证】地下勒索／泄露／访问声称（合辑）

以下均为社交列表报道，**一律 UNCONFIRMED／未验证**；不复述利用步骤：

- **Kiassure**（法国 insurtech）数据库售卖声称：https://x.com/DailyDarkWeb/status/2104350882095939600
- **Bangladesh Army／Qadirabad** 全网沦陷声称（MikroTik CCR1036／RouterOS 6.49.18／CVE-2018-14847 语境）：https://x.com/MonThreat/status/2104265206838726895
- **US Law Enforcement／Intelligence databases** 大规模泄露声称（可能虚假信息标签）：https://x.com/MonThreat/status/2104264075714625779 · 帖链：https://mrhex.sbs
- **Ronis**（澳大利亚）~34500 客户记录泄露声称：https://x.com/intels_daily/status/2104301835041300844
- **Scorenco[.]com**（法国体育）22962 条泄露声称：https://x.com/intels_daily/status/2104277379816276121
- **ITESHU** phpMyAdmin 凭据免费访问售卖声称（墨西哥）：https://x.com/intels_daily/status/2104271653169496446

IoC（Bangladesh 帖可见指标，**一律 UNCONFIRMED**）：IP `27.147.148.184`；RouterOS `6.49.18`；CVE-2018-14847；文件名 `autosupout.rif`／`15123_1812358-20260513-2247.backup`；VLAN 标签 `vlan2402-GGC`／`vlan2403-FNA`；弱口令示例 `123321`。其余多数 **未见公开 IoC**。

### 4. ICS

本日公开备援主条以 **Citrix NEW KEV** 与既有 overdue／upcoming 网关／编排／APM／VPN／Artifactory 类为主；**无单独新突出的 2026-09-27 ICS advisory 主条**。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Arista VeloCloud CVE-2026-93952（仍逾期）**：`/usr/local/sbin/.vcnode.js`；`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）；`/etc/systemd/system/vc-sysmon.service`；HTTP 头 `x-vc-opt`；IP `142.93.149.77`／`104.248.126.159`。（来源：今日 enrich-extra／SA-0183）
- **Check Point 85102／93616（仍逾期）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`。（来源：昨日报告／昨日厂商 SK／enrich；今日 enrich-extra 未重抄）
- **Cisco ISE 76460（仍逾期）**：狩猎示例 `admin#show logging application ise-kong/access.log | include dummyuser`；路径 `./ise/logs/apigateway/access.log`。（来源：今日 enrich-extra／Cisco SA）
- **PeopleSoft 35273（X 转述）**：`/%50SEMHUB/`；`x.jsp`／`u.jsp`／`Ple64.exe`／`tunnel.jsp`／`tunnel.jspx`；IP `5.199.162.157`／`104.219.234.138`／`162.219.30.165`。（来源：X 帖列表；以 Mandiant 原文核验）
- **Magento 75650 事件声称（UNCONFIRMED）**：`pub/media/custom_options/quote/`；`/customer/address_file/upload`；`/rest/V1/guest-carts`；`template_styles`；`*.php`；`@nx.invalid`
- **Bangladesh Army 声称（UNCONFIRMED）**：`27.147.148.184`；RouterOS `6.49.18`；`autosupout.rif` 等（见 APT 节）
- **Citrix NEW 88771／88772／due_today WSO2／Adobe／upcoming 09-28 三件套／其余仍逾期／工具仓**：未见可抄录公开 IoC（或仅厂商 SK／新闻原文内；Citrix KEV 称有厂商 IoC 检查但可见页未列具体指标）
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

本窗口 LWiS List 只读采集：扫描约 **11** 条、保留 **3** 条、覆盖约 **15h**（`logged_in=true`／`@seogoogle4`／`blocked=false`）；跨源 ID 重叠 0（相对 A／B／C）；含 Citrix NetScaler 交叉（THN／cyb3rops）与 AI／安全工程讨论；meta：`/workspace/x-lwis-list-meta-2026-09-27.json`。

## 来源搜索 URL

- X Latest A（CVE-2026 精炼）：https://x.com/search?q=%22CVE-2026%22%20-filter%3Areplies%20-from%3ACVEnew%20-from%3AIhhsanMuhammad&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／cobalt）：https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS615：https://risky.biz/RBNEWS615/
- Risky SRB184a：https://risky.biz/SRB184a/
- Risky BTN183：https://risky.biz/BTN183/
- tl;dr sec：https://tldrsec.com/
- tl;dr #347：https://tldrsec.com/p/tldr-sec-347
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 09-27 Adds Two（Citrix 88771／88772）：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 09-25 一条 KEV 警报（87902）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-25 两条 KEV 警报（65660＋67279）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
