# X 安全情报晚报 · 2026-09-28

> 搜集窗口：圣地亚哥时间 **2026-09-27 20:00 至 2026-09-28 ~20:35**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周一）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-28.json`（collected_at **2026-09-28T20:25:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-28.json`＋ `/workspace/enrich-extra-2026-09-28.json`＋ `/workspace/enrich-2026-09-28/`。CISA KEV catalogVersion **2026.09.27**／**1728** 条／dateReleased **2026-09-27T21:30:35.5521Z**（相对昨日基线 **2026.09.27／1728**：**count Δ+0**；**今日无 NEW**／无 09-28 Adds 告警）。**due_today** SharePoint **65660**／MikroTik **67279**／WordPress **87902**；**newly_overdue** WSO2 **5430**／Adobe **71362**（昨 due_today 转入）；**仍逾期亮点 16**（昨 14＋上述 2）；**upcoming** 09-30 Citrix **88771／88772**。昨日 CISA「Adds Two」仍为最新 KEV 加目告警：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
> **仍逾期（含 newly_overdue）**：**Check Point CVE-2026-85102／93616**、**Arista VeloCloud CVE-2026-93952**、**F5 BIG-IP APM CVE-2026-94127**、**JFrog Artifactory CVE-2026-42016／42018**、**Zyxel CVE-2026-7273**、**MS CVE-2026-81963／85880**、**Chromium CVE-2026-87491／85046**、**Pixel CVE-2026-58704**、**Cisco ISE CVE-2026-76460**、**Acronis CVE-2026-87886**、**WSO2 CVE-2026-5430**、**Adobe CVE-2026-71362**。**due_today（09-28）**：**SharePoint CVE-2026-65660**／**MikroTik CVE-2026-67279**／**WordPress CVE-2026-87902**。**即将 due 09-30**：**Citrix CVE-2026-88771／88772**。
> X：`/workspace/x-posts-2026-09-28.json`（合并 **41** 条唯一：A8／B8／C17／LWiS8；跨源 ID 重叠 **0**；相对 prior seen_ids 重叠 **4**／**+37** 新 id；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **1h**。Search B 可见约 **72h**（含 Sep 25–28 工具帖，其中 4 条已见 prior）。Search C 约 **1h**。LWiS List 约 **11h**（**交叉校验，不假装为本窗口 24h Latest**；成员 **501**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。抓取备注：Adobe APSB26-92 **403**；Citrix community bulletin **403**；F5 myF5 鉴权墙；Arista curl **406**、WebFetch **200**（含公开 IoC）；Pixel OAuth **302**；Acronis JS 墙；CISA alerts listing／今日 Adds **404**。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露声称一律标 **UNCONFIRMED／未验证**；ImageMagick／KVM 等利用链帖只写「存在公开讨论／需补丁」级防御摘要。

## 今日摘要

- **【主条 · due_today · SharePoint／MikroTik／WordPress】** 联邦 due **2026-09-28**：**CVE-2026-65660**（Microsoft SharePoint 代码注入；forensicTriage=Yes；按 MSRC／BOD 26-04）／**CVE-2026-67279**（MikroTik RouterOS；九月公告语境，公开页未列 67279 ID，见 MikroTrick／86060 族）／**CVE-2026-87902**（WordPress Core 路径遍历→条件 RCE；升 GHSA 补丁版本 7.1.2／7.0.6／6.9.9…）。CISA 加目告警仍为 09-25 对应 Adds。防御：今日到期项优先落地补丁与暴露面核验；BOD 26-04。
  SharePoint MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660
  MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
  WP GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
  CISA Adds One（87902）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog
  CISA Adds Two（65660／67279）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
  X（WP KEV 转述／A）：https://x.com/DailyDarkWeb/status/2104685272399216959

- **【newly_overdue · WSO2 5430／Adobe 71362】** 昨 due_today 转入逾期：**CVE-2026-5430**（WSO2 多产品路径遍历→上传/RCE；按 WSO2-2026-5328 升 Update Level）／**CVE-2026-71362**（Adobe Commerce/Magento 不正确授权；按 APSB26-92，helpx 出口 **403**）。防御：补丁落地核验；BOD 26-04。
  WSO2：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
  APSB26-92：https://helpx.adobe.com/security/products/magento/apsb26-92.html

- **【仍逾期 · Check Point／Arista／F5／JFrog／Zyxel／MS／Chromium／Pixel／ISE／Acronis＋WSO2／Adobe】** 亮点 **16**＝昨 14＋ newly_overdue 2。高信号：**Check Point 85102／93616**（cert_subject 狩猎见 IoC 节）／**Arista 93952**（SA-0183 文件/MD5/IP IoC）／**F5 94127**／**JFrog 42016／42018**／**Zyxel 7273**／MS **81963／85880**／Chromium **87491／85046**／Pixel **58704**／Cisco ISE **76460**／Acronis **87886**。防御：核验补丁与狩猎；BOD 26-04。
  Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
  Arista SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
  F5 K000162605：https://my.f5.com/manage/s/article/K000162605
  JFrog advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories

- **【即将 due 09-30 · Citrix 88771／88772 · X 交叉】** KEV 仍为昨日 NEW（catalog **Δ+0**）；联邦 due **09-30**。X A／LWiS 今日继续交叉：JPCERT/CC 注意提醒、watchTowr 检测工件仓库、citrixInspector 版本识别、NetScaler 利用观测讨论（具体指标未在帖摘要列出）。防御：立即按 CTX 升 ADC/Gateway；按 CTX694799 疑似沦陷取证；BOD 26-04。**不转载利用步骤。**
  CISA Adds Two：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
  CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
  CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
  CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
  JPCERT AT260029：https://www.jpcert.or.jp/at/2026/at260029.html
  watchTowr 仓：https://github.com/watchtowrlabs/watchTowr-vs-Citrix-Netscaler-CVE-2026-88771
  X（foxbook／JPCERT）：https://x.com/foxbook/status/2104690578638172353
  X（DarkWebInformer／watchTowr）：https://x.com/DarkWebInformer/status/2104710347793875293
  X（Maurice_Sec／LWiS）：https://x.com/Maurice_Sec/status/2104541998858240487

- **【X 高信号 · Apple／OpenAI／PeopleSoft】** A（~1h）：**Apple 紧急修复 CVE-2026-86950**（iOS 26／macOS 26／macOS 15；SANS ISC）；**OpenAI macOS 桌面端 26.924.20706 修 CVE-2026-100754**（版本公告转述）；**Oracle PeopleSoft CVE-2026-35273**／UNC6240（ShinyHunters）再大规模利用——**X 转述 UNCONFIRMED**（未附 Mandiant 原文链接，交叉昨日 Mandiant／Oracle）。防御：尽快更新 Apple／ChatGPT 桌面端；PeopleSoft 暴露面与补丁核验。
  SANS ISC：https://isc.sans.edu/diary/33376 · X：https://x.com/sans_isc/status/2104694210649809394
  X（OpenAI）：https://x.com/lyczak/status/2104705169556738394
  X（PeopleSoft 转述）：https://x.com/DailyDarkWeb/status/2104687088163852445
  Mandiant（交叉）：https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft
  Oracle：https://www.oracle.com/security-alerts/alert-cve-2026-35273.html

- **【工具／新闻】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** **无升版**；Risky **新**：**RBNEWS616**（https://risky.biz/RBNEWS616/ · Intel ends paid bug bounties）／**BTN184**（https://risky.biz/BTN184/）；SRB 仍 **SRB184**（https://risky.biz/SRB184a/）；tl;dr 仍 **#347**（https://tldrsec.com/p/tldr-sec-347）。X B：notRDP／Red-Team-Roadmap／Sliver／Mythic／adaptix-graph-c2／MartijnBraam/c2 PR 等（授权评估语境；4 条 prior）。

- **【APT／Malware · 大量 UNCONFIRMED】** C（~1h）：Qilin／cry0／INC RANSOM／Doommageddon 等多起勒索与泄露售卖声称；帮助台未认证上传／Defender 未修利用售卖等——**一律 UNCONFIRMED**。LWiS（~11h）：ImageMagick 7.1.2 RCE 公开讨论（仅写需补丁级摘要）／KVM UAF 逃逸转发（未独立验证）／Entra CAP 绕过文章／AI agent 越界研究／Offensive-Security-AI-Models 仓。

- **【合并统计】** X **41** 唯一（A8／B8／C17／LWiS8；cross **0**；prior **4**；**+37** NEW）；`logged_in=true`／`@seogoogle4`／`blocked=false`；覆盖 A~1h／B~72h／C~1h／LWiS~11h；seen_ids **2111→2148**；报告 `/home/box/workspace/security-watch/reports/2026-09-28-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【due_today】Microsoft SharePoint CVE-2026-65660

联邦 due **2026-09-28**。代码注入；授权攻击者可经网络执行代码；forensicTriage=Yes。防御：按 MSRC 应用缓解／更新；按 BOD 26-04 做 forensic triage；评估互联网暴露。

地址：
- 厂商 MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-65660
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-65660
- CISA Adds Two（09-25）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 2. 【due_today】MikroTik RouterOS CVE-2026-67279

联邦 due **2026-09-28**。行为工作流执行不当语境；公开九月公告页 HTTP 200 但未列 67279 ID（见 MikroTrick／CVE-2026-86060 族）。防御：按 MikroTik 九月安全公告升级；限制管理面；BOD 26-04。

地址：
- 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67279
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-67279
- CISA Adds Two（09-25）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 3. 【due_today】WordPress Core CVE-2026-87902

联邦 due **2026-09-28**。路径遍历→条件 RCE／远程文件包含语境。防御：升至 GHSA 所列补丁版本（示例 **7.1.2／7.0.6／6.9.9…**）；核验暴露面；BOD 26-04。X A 有 KEV 转述帖（未附可审计原始链接——交叉以 CISA／GHSA 为准）。

地址：
- 厂商 GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87902
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87902
- CISA Adds One（09-25）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog
- X（转述）：https://x.com/DailyDarkWeb/status/2104685272399216959
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 4. 【newly_overdue】WSO2 CVE-2026-5430

联邦 due 曾为 **2026-09-27**，今日转入 **newly_overdue**。多产品路径遍历 → 上传/RCE。防御：按 **WSO2-2026-5328** 将受影响产品升至公告 Update Level；BOD 26-04。

地址：
- 厂商：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-5430
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-5430
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 5. 【newly_overdue】Adobe Commerce／Magento CVE-2026-71362

联邦 due 曾为 **2026-09-27**，今日转入 **newly_overdue**。不正确授权。防御：按 **APSB26-92** 应用厂商补丁；BOD 26-04。（helpx box 出口 **403**，仍列已知厂商 URL；NVD 作备援。）

地址：
- 厂商 APSB26-92：https://helpx.adobe.com/security/products/magento/apsb26-92.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-71362
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-71362
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 6. 【即将 due 09-30 · 在野】Citrix NetScaler CVE-2026-88771／CVE-2026-88772

CISA 于 **2026-09-27** 加入 KEV（今日 catalog **Δ+0**，无新加目）；联邦 due **2026-09-30**。88771：不当输入验证 → 未认证命令执行。88772：内存边界限制不当 → RCE/DoS。同公告族覆盖 **CVE-2026-88771–88778**（CTX697096）。KEV 备注称可在 NetScaler 控制台运行厂商 IoC 检查；本轮 enrich／可见厂商页 **未见可抄录具体哈希／IP IoC**（CTX694799 为应急步骤页）。X A＋LWiS 今日交叉：JPCERT AT260029、watchTowr 检测工件仓、citrixInspector、Maurice_Sec 利用观测讨论（帖摘要未列具体指标）。防御：立即按 CTX 升 ADC/Gateway；按 CTX694799 疑似沦陷排查；限制管理面；BOD 26-04。**不转载利用步骤。**

地址：
- CISA Adds Two：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- 厂商 CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
- 厂商 CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
- Community bulletin：https://community.citrix.com/techzone-blogs/110_security-updates/netscaler-adc-and-netscaler-gateway-security-bulletin-for-cve-2026-88771-through-cve-2026-88778
- JPCERT AT260029：https://www.jpcert.or.jp/at/2026/at260029.html
- NVD 88771：https://nvd.nist.gov/vuln/detail/CVE-2026-88771
- NVD 88772：https://nvd.nist.gov/vuln/detail/CVE-2026-88772
- KEV 88771：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88771
- KEV 88772：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88772
- watchTowr 检测仓：https://github.com/watchtowrlabs/watchTowr-vs-Citrix-Netscaler-CVE-2026-88771
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- X（foxbook／JPCERT）：https://x.com/foxbook/status/2104690578638172353
- X（DarkWebInformer／watchTowr）：https://x.com/DarkWebInformer/status/2104710347793875293
- X（DarkWebInformer／citrixInspector）：https://x.com/DarkWebInformer/status/2104707107111276751
- X（securityLab_jp）：https://x.com/securityLab_jp/status/2104708020559376891
- X（Maurice_Sec／LWiS）：https://x.com/Maurice_Sec/status/2104541998858240487

IoC：未见公开 IoC（KEV／CTX 称厂商提供检查，可见抓取未列具体指标；LWiS 帖摘要亦未显示具体值）。

### 7. 【仍逾期 · 在野】Check Point CVE-2026-85102／CVE-2026-93616

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

### 8. 【仍逾期 · 在野】Arista VeloCloud CVE-2026-93952

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

### 9. 【仍逾期 · 在野】F5 BIG-IP APM CVE-2026-94127

KEV due 曾为 **2026-09-25**，继续 overdue。堆溢出 → 未认证数据面 RCE（APM＋OAuth profile 场景）。防御：按 K000162605 先临时 iRule，完成取证后装最终补丁；BOD 26-04。（myF5 鉴权墙，仍列已知厂商 URL。）

地址：
- 厂商 K000162605：https://my.f5.com/manage/s/article/K000162605
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94127
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-94127
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 10. 【仍逾期 · near】JFrog Artifactory CVE-2026-42016／CVE-2026-42018

due 曾为 **2026-09-25**，继续 overdue。42016：令牌授权校验错误提权（修复示例 **≥7.133.11**）。42018：匿名令牌暴露（受影响分支含 <7.111.20；7.117.0–7.117.27；7.125.0–7.125.19；7.133.0–7.133.28；7.146.0–7.146.8）。防御：按 JFrog Security Advisories／Self-Managed Releases 升版；限制管理面。

地址：
- NVD 42016：https://nvd.nist.gov/vuln/detail/CVE-2026-42016
- NVD 42018：https://nvd.nist.gov/vuln/detail/CVE-2026-42018
- KEV 42016：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-42016
- KEV 42018：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-42018
- 厂商 advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- 发行说明：https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases

IoC：未见公开 IoC。

### 11. 【仍逾期】Zyxel／Microsoft／Chromium／Pixel／Cisco ISE／Acronis（合辑）

- **Zyxel GS1900 CVE-2026-7273**（due 曾=09-24）：升 **2.90(*.2)C0**；限制 LAN 管理面。厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273 · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273
- **MS CVE-2026-81963／85880**（due 曾=09-22）：确认九月补丁。MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-81963 · https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880
- **Chromium CVE-2026-87491**（due 曾=09-23）：升 **153.0.8010.36+**。https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- **Chromium CVE-2026-85046**（due 曾=09-18）：尽快升级。https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- **Pixel CVE-2026-58704**（due 曾=09-19）：装 Pixel 2026-09-01 更新（source.android OAuth 环）。https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- **Cisco ISE CVE-2026-76460**（due 曾=09-19）：升 First Fixed（3.1→P12／3.2→P11／3.3→P12／3.4→P7／3.5→P4）。https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  IoC（厂商 SA／昨 enrich 原样）：`admin#show logging application ise-kong/access.log | include dummyuser`；日志路径 `./ise/logs/apigateway/access.log`
- **Acronis CVE-2026-87886**（due 曾=09-19）：按 SEC-10986（JS 墙）。https://security-advisory.acronis.com/advisories/SEC-10986

除 ISE 狩猎示例外，上列多数 **未见公开 IoC**。

### 12. 【X A】Apple 紧急修复 CVE-2026-86950

SANS ISC 汇总 Apple 对 **iOS 26**、**macOS 26／macOS 15** 的紧急修复，涉及 **CVE-2026-86950**。防御：尽快更新受影响 Apple 设备。

地址：
- 文章 SANS ISC：https://isc.sans.edu/diary/33376
- X：https://x.com/sans_isc/status/2104694210649809394
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-86950

IoC：未见公开 IoC。

### 13. 【X A】OpenAI macOS 桌面端 CVE-2026-100754

转述 OpenAI **9/25** macOS 桌面端更新：版本 **26.924.20706** 修复 **CVE-2026-100754**；帖称公告未披露漏洞细节，不能据此推断已遭利用。防御：核对 ChatGPT／Codex 桌面端并更新。

地址：
- X：https://x.com/lyczak/status/2104705169556738394
- NVD（若已收录）：https://nvd.nist.gov/vuln/detail/CVE-2026-100754

IoC：未见公开 IoC。

### 14. 【X A · Mandiant 转述 · UNCONFIRMED】Oracle PeopleSoft CVE-2026-35273

@DailyDarkWeb 转述 Google/Mandiant Threat Intelligence：UNC6240（ShinyHunters）再次大规模利用 **CVE-2026-35273**；帖未附可审计原始报告链接——标 **UNCONFIRMED**，交叉以 Mandiant／Oracle 原文为准（昨日报告已列路径/IP IoC）。防御：PeopleSoft／PSEMHUB 暴露面盘点与补丁；对照 Mandiant 原文狩猎；BOD 26-04／KEV 语境。**不转载利用步骤。**

地址：
- X：https://x.com/DailyDarkWeb/status/2104687088163852445
- Mandiant／GTIG：https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft
- Oracle：https://www.oracle.com/security-alerts/alert-cve-2026-35273.html
- KEV 检索：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-35273

IoC（原样抄录自昨日报告 X 帖列表／交叉用；以 Mandiant 原文为准核验；今日该帖未重列）：
- 路径：`/%50SEMHUB/`
- 文件／名：`x.jsp`／`u.jsp`／`Ple64.exe`／`tunnel.jsp`／`tunnel.jspx`
- IP：`5.199.162.157`／`104.219.234.138`／`162.219.30.165`

### 15. 【LWiS · 公开讨论】ImageMagick 7.1.2 RCE 链

@odinshell（经 @kmkz_security 转发）摘要 ImageMagick **7.1.2** 存在公开利用链讨论（crafted dimensions → integer overflow 等）。**本报不转载利用步骤**；未见 CVE／补丁链接。防御：关注 ImageMagick 官方安全公告与发行版包更新；限制不可信图像处理面；尽快升级受影响版本。

地址：
- X：https://x.com/odinshell/status/2104558360112845075
- ImageMagick 安全入口：https://imagemagick.org/script/security-policy.php

IoC：未见公开 IoC。

### 16. 【LWiS · 未独立验证】KVM use-after-free 逃逸声称

@IntCyberDigest 转发称 AI agent 经 KVM use-after-free 逃逸虚拟机并以大量内存映射冲击宿主；原帖截断，**未在本窗口独立验证**。防御：关注 KVM／内核安全更新与虚拟化加固通告；勿将转发摘要当作已确认漏洞披露。

地址：
- X：https://x.com/IntCyberDigest/status/2104691480178680160

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 核心工具版本（公开 pulse）

- **Sliver** 仍 **v1.7.7**（无升版）：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- **nuclei** 仍 **v3.11.1**（无升版）：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- **nuclei-templates** 仍 **v10.4.9**（无升版）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- Risky **新**：**RBNEWS616** https://risky.biz/RBNEWS616/（Intel ends paid bug bounties）· **BTN184** https://risky.biz/BTN184/（The AI crime machine）· SRB 仍 **SRB184a** https://risky.biz/SRB184a/
- tl;dr sec 仍 **#347**：https://tldrsec.com/p/tldr-sec-347

### X Search B（~72h；授权红队／模拟向；不写利用步骤）

- **Sliver C2 实验室演示**（Authorized testing only）：X：https://x.com/rabixSecurity/status/2104671047169794191
- **notRDP**（Havoc C2 插件；隐式桌面／浏览器查看器——仅授权仿真；**UNCONFIRMED**）：https://github.com/dagowda/notRDP · X：https://x.com/5mukx/status/2104567001083691241
- **MartijnBraam/c2 PR #11**（RPi4 OMT camera streaming）：https://github.com/MartijnBraam/c2/pull/11 · X：https://x.com/FlowingSPDG/status/2104545718321225825
- **Red-Team-Roadmap** Module 17（凭据发现主题；不复述步骤；**UNCONFIRMED／仅授权评估**）：https://github.com/Dev-Chukwuma/Red-Team-Roadmap · X：https://x.com/httpschuks/status/2104514627933532440
- **Sliver CS-Situational-Awareness-BOF**（跨平台 BOF；v1.7.7 语境；**prior_seen**）：https://github.com/sliverarmory/CS-Situational-Awareness-BOF · X：https://x.com/LittleJoeTables/status/2103914959264760196
- **Sliver**（BishopFox；**prior_seen**）：https://github.com/BishopFox/sliver · X：https://x.com/AlAssaf_H/status/2103850433219268943
- **Mythic**（多代理 C2；**prior_seen**）：https://github.com/its-a-feature/Mythic · X：https://x.com/AlAssaf_H/status/2103850054997963011
- **adaptix-graph-c2**（Azure Blob／OneDrive dead-drop；**prior_seen**／**UNCONFIRMED／仅授权评估**）：https://github.com/stillbigjosh/adaptix-graph-c2 · X：https://x.com/stillbigjosh/status/2103455702945796331

### 防御检测／Citrix 相关仓（X A）

- **watchTowr-vs-Citrix-Netscaler-CVE-2026-88771**（检测工件生成器；防御侧核对）：https://github.com/watchtowrlabs/watchTowr-vs-Citrix-Netscaler-CVE-2026-88771 · X：https://x.com/DarkWebInformer/status/2104710347793875293
- **citrixInspector**（被动识别 ADC/Gateway 构建版本与已知漏洞；帖未附独立仓 URL）：X：https://x.com/DarkWebInformer/status/2104707107111276751

### LWiS 交叉工具／研究（~11h）

- **Offensive-Security-AI-Models**（基准仓）：https://github.com/JoasASantos/Offensive-Security-AI-Models · X：https://x.com/C0d3Cr4zy/status/2104316326957449485
- **Entra Conditional Access 绕过讨论**（不受支持设备／Device Platforms）：文章 https://petri.com/bypass-entra-conditional-access-policies/ · X：https://x.com/TechBrandon/status/2104667532867014667
- **dreadnode** AI 安全活动预告：https://x.com/dreadnode/status/2104707704832897352
- **kpolley／Perplexity** AI agent 越界测试声称（引用卡未展开）：https://x.com/kpolley/status/2104603968445784140

IoC：工具帖未见公开 IoC。

## APT / Malware 分析

### 1. 【X C · 未验证】勒索软件事件声称（合辑）

以下均为社交列表报道，**一律 UNCONFIRMED／未验证**；不复述利用步骤：

- **Arnold Center**（美国非营利）据报遭 **Qilin**：https://x.com/FalconFeedsio/status/2104710506422698343 · 站点：https://www.arnoldcenter.org/
- **MinMor Industries**（美国制造）据报遭 **cry0**：https://x.com/FalconFeedsio/status/2104709618769482228 · 站点：https://www.minmor.com/
- **Bake My Day AB**（瑞典）据报遭 **INC RANSOM**：https://x.com/FalconFeedsio/status/2104701138172047781 · 站点：https://www.bakemyday.se/
- **Chem Process Systems**（印度）据报遭 **Doommageddon**：https://x.com/CyberPulse56/status/2104708386600505564
- **Goodrich Shipping & Logistics**（印度）据报遭 **Doommageddon**：https://x.com/CyberPulse56/status/2104707527644512758

IoC：未见公开 IoC。

### 2. 【X C · 未验证】地下泄露／访问／利用售卖声称（合辑）

**一律 UNCONFIRMED／未验证**：

- 企业帮助台未认证文件上传／Explorers 售卖声称：https://x.com/CyberPulse56/status/2104709901545091397
- 危地马拉 SAT 6,000+ 记录泄露声称（rethixx）：https://x.com/CyberPulse56/status/2104709246310855040
- CONALEP Morelos 数据库／SQL 注入入口声称：https://x.com/CyberPulse56/status/2104708705543704887 · https://conalepmorelos.edu.mx/
- Colec.fr 数据库泄露声称（3.36 GB）：https://x.com/CyberPulse56/status/2104706864550195627 · https://colec.fr/
- Hunt.io 暴露目录／俄语 CLAUDE.md「AI 辅助攻击手册」声称：https://x.com/Kostastsale/status/2104706676767236416
- Windows Defender 未修复利用 20,000 美元售卖声称（QatarRat）：https://x.com/CyberPulse56/status/2104705781593485669
- Betibet 数据集声称（Lucasarsenal）：https://x.com/CyberPulse56/status/2104705467863732478
- Lisa Transportation LLC 数据声称：https://x.com/CyberPulse56/status/2104704600032825774
- 巴基斯坦 PVMC／PVMA「TAI」恶意软件／勒索声称：https://x.com/CyberPulse56/status/2104703409961959928 · https://pvmc.gov.pk/ · https://x.com/CyberPulse56/status/2104702300228907367 · https://pvma.pk/
- 叙利亚电信网络服务机构 528 文件声称（Elite Squad）：https://x.com/CyberPulse56/status/2104700314435912064
- 多米尼加 Banco de Semen 数据库声称（cutzinger）：https://x.com/CyberPulse56/status/2104699539168870740

IoC：未见公开 IoC。

### 3. 【LWiS】Steam 恶意软件泛化声称（低置信）

@vxunderground 称收到多人私信但无人提供样本；要求先给出实际 malware——**未证实／低置信**，不能作为已确认事件。

地址：
- X：https://x.com/vxunderground/status/2104682698828927092

IoC：未见公开样本或 IoC。

### 4. ICS

本日公开备援主条以 **due_today 三件套**、**newly_overdue WSO2／Adobe**、**仍逾期网关／编排／APM／VPN／Artifactory** 与 **upcoming Citrix** 为主；**无单独新突出的 2026-09-28 ICS advisory 主条**。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Arista VeloCloud CVE-2026-93952（仍逾期）**：`/usr/local/sbin/.vcnode.js`；`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）；`/etc/systemd/system/vc-sysmon.service`；HTTP 头 `x-vc-opt`；IP `142.93.149.77`／`104.248.126.159`。（来源：今日 enrich-extra／SA-0183）
- **Check Point 85102／93616（仍逾期）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`。（来源：昨日报告／昨日厂商 SK／enrich；今日 enrich-extra 未重抄）
- **Cisco ISE 76460（仍逾期）**：狩猎示例 `admin#show logging application ise-kong/access.log | include dummyuser`；路径 `./ise/logs/apigateway/access.log`。（来源：昨日报告／Cisco SA）
- **PeopleSoft 35273（交叉昨日／Mandiant）**：`/%50SEMHUB/`；`x.jsp`／`u.jsp`／`Ple64.exe`／`tunnel.jsp`／`tunnel.jspx`；IP `5.199.162.157`／`104.219.234.138`／`162.219.30.165`。（以 Mandiant 原文核验；今日 X 转述未重列）
- **Citrix 88771／88772／due_today 三件套／newly_overdue WSO2／Adobe／其余仍逾期／工具仓／C 勒索声称**：未见可抄录公开 IoC（或仅厂商 SK／新闻原文内；Citrix KEV 称有厂商 IoC 检查但可见页未列具体指标；LWiS Maurice_Sec 帖摘要未显示具体值）
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

本窗口 LWiS List 只读采集：扫描约 **15** 条、保留 **8** 条、覆盖约 **11h**（`logged_in=true`／`@seogoogle4`／`blocked=false`；成员页显示 **501**）；跨源 ID 重叠 0（相对 A／B／C）；含 Citrix 交叉、ImageMagick／KVM 讨论、Entra CAP 文章、AI 安全研究仓等；meta：`/workspace/x-lwis-list-meta-2026-09-28.json`。

## 来源搜索 URL

- X Latest A（CVE-2026 精炼）：https://x.com/search?q=%22CVE-2026%22%20-filter%3Areplies%20-from%3ACVEnew%20-from%3AIhhsanMuhammad&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／cobalt）：https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS616：https://risky.biz/RBNEWS616/
- Risky SRB184a：https://risky.biz/SRB184a/
- Risky BTN184：https://risky.biz/BTN184/
- tl;dr sec：https://tldrsec.com/
- tl;dr #347：https://tldrsec.com/p/tldr-sec-347
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 09-27 Adds Two（Citrix 88771／88772）：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 09-27 Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- CISA 09-25 一条 KEV 警报（87902）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-25 两条 KEV 警报（65660＋67279）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
