# X 安全情报晚报 · 2026-09-29

> 搜集窗口：圣地亚哥时间 **2026-09-28 20:00 至 2026-09-29 ~20:15**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-29.json`（collected_at **2026-09-29T20:15:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-29.json`＋ `/workspace/enrich-extra-2026-09-29.json`＋ `/workspace/enrich-2026-09-29/`。CISA KEV catalogVersion **2026.09.29**／**1729** 条／dateReleased **2026-09-29T13:51:33.3852Z**（相对昨日基线 **2026.09.27／1728**：**count Δ+1**；**NEW Apple CVE-2026-86950**；今日 CISA「Adds One」：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog ）。**due_today 无**；**newly_overdue** SharePoint **65660**／MikroTik **67279**／WordPress **87902**（昨 due_today 转入）；**仍逾期亮点 19**（昨 16＋上述 3）；**upcoming** 09-30 Citrix **88771／88772**、10-02 Apple **86950**。
> **仍逾期（含 newly_overdue）**：**Check Point CVE-2026-85102／93616**、**Arista VeloCloud CVE-2026-93952**、**F5 BIG-IP APM CVE-2026-94127**、**JFrog Artifactory CVE-2026-42016／42018**、**Zyxel CVE-2026-7273**、**MS CVE-2026-81963／85880**、**Chromium CVE-2026-87491／85046**、**Pixel CVE-2026-58704**、**Cisco ISE CVE-2026-76460**、**Acronis CVE-2026-87886**、**WSO2 CVE-2026-5430**、**Adobe CVE-2026-71362**、**SharePoint CVE-2026-65660**、**MikroTik CVE-2026-67279**、**WordPress CVE-2026-87902**。**即将 due 09-30**：**Citrix CVE-2026-88771／88772**。**即将 due 10-02**：**Apple CVE-2026-86950**。
> X：`/workspace/x-posts-2026-09-29.json`（合并 **48** 条唯一：A17／B10／C15／LWiS6；跨源 ID 重叠 **0**；相对 prior seen_ids 重叠 **0**／**+48** 新 id；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.83h**。Search B 可见约 **19h**。Search C 约 **1.75h**。LWiS List 约 **11h**（**交叉校验，不假装为本窗口 24h Latest**；成员 **502**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。抓取备注：Adobe APSB26-92 **403**；Citrix community bulletin **403**/Cloudflare；F5 myF5 鉴权墙；Arista curl **406**、WebFetch **200**（含公开 IoC）；Pixel OAuth 标记；Acronis JS 墙；MSRC SPA；CISA `/news-events/alerts` **404**（advisories 列表 200／今日 Adds One 200）；risky.biz 根 **403**（www 200）。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露声称一律标 **UNCONFIRMED／未验证**；仅写谁／打什么／补丁与狩猎级防御摘要。

## 今日摘要

- **【主条 · KEV NEW · Apple CVE-2026-86950】** CISA 于 **2026-09-29** 将 **CVE-2026-86950** 加入 KEV（catalog **2026.09.29／1729／Δ+1**）；联邦 due **2026-10-02**；forensicTriage=Yes；ransomware 使用 Unknown。Apple 多产品 CoreGraphics 越界写；补丁示例 **iOS/iPadOS 26.7.1**、**macOS Tahoe 26.7.1**、**Sequoia 15.8.1**（报告称针对 iOS 的有限高度针对性攻击；致谢 Meta Product Security）。X A 交叉。防御：尽快更新受影响 Apple 设备；按 BOD 26-04 做暴露面与取证排查。
  CISA Adds One：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
  Apple：https://support.apple.com/en-us/149226 · https://support.apple.com/en-us/149228 · https://support.apple.com/en-us/149229
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-86950
  X（kokumoto）：https://x.com/__kokumoto/status/2105067358494879943

- **【newly_overdue · SharePoint／MikroTik／WordPress】** 昨 due_today 转入逾期：**CVE-2026-65660**（Microsoft SharePoint 代码注入；forensicTriage=Yes；按 MSRC／BOD 26-04）／**CVE-2026-67279**（MikroTik RouterOS；公开九月页未列 67279 ID，见 MikroTrick／86060 族）／**CVE-2026-87902**（WordPress Core 路径遍历→条件 RCE；升 GHSA 补丁版本 7.1.2／7.0.6／6.9.9…）。X A：CrowdSec 称约 30,813 独特 IP 在五日窗口打 WP 87902（转述，交叉以厂商／CISA 为准）。防御：补丁落地核验；BOD 26-04。
  SharePoint MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660
  MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
  WP GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
  X（WP／CrowdSec 转述）：https://x.com/jfernandogg/status/2105062567739888088

- **【即将 due 09-30 · Citrix 88771／88772 · X 交叉】** KEV 自 09-27；联邦 due **09-30**（明日）。X A 今日高信号：恶用确认／PitScaler／Mandiant web shells・tunneling（WHIPSHOT／SLAPSHOT）转述、BleepingComputer 卡片提及、日语 CB／多家重复报道。防御：立即按 CTX 升 ADC/Gateway；按 CTX694799 疑似沦陷取证；BOD 26-04。**不转载利用步骤；本轮 enrich 未见可抄录具体哈希／IP。**
  CISA Adds Two：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
  CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
  CTX697096：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096
  CTX694799：https://support.citrix.com/external/article/CTX694799/steps-to-take-if-netscaler-adc-is-suspec.html
  X（jp_cb_security）：https://x.com/jp_cb_security/status/2105072845256876156
  X（fredmdl／PitScaler）：https://x.com/fredmdl/status/2105065352443093460
  X（kokumoto／BC 卡）：https://x.com/__kokumoto/status/2105065585654808972

- **【仍逾期 · Check Point／Arista／F5／JFrog／Zyxel／MS／Chromium／Pixel／ISE／Acronis＋WSO2／Adobe＋newly_overdue 三件】** 亮点 **19**＝昨 16＋ newly_overdue 3。高信号：**Check Point 85102／93616**（cert_subject 狩猎见 IoC 节）／**Arista 93952**（SA-0183 文件/MD5/IP IoC）／**F5 94127**／**JFrog 42016／42018**／**Zyxel 7273**／MS **81963／85880**／Chromium **87491／85046**／Pixel **58704**／Cisco ISE **76460**／Acronis **87886**／WSO2 **5430**／Adobe **71362**。防御：核验补丁与狩猎；BOD 26-04。
  Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
  Arista SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
  F5 K000162605：https://my.f5.com/manage/s/article/K000162605
  JFrog advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories

- **【X A 高信号 · Chrome 102331／Spectre BTR／ExploitBench】** Chrome **154** 安全更新（作者称修 33 件，含 Critical **CVE-2026-102331** ANGLE 缓冲溢出 CVSS 9.6，恶用未确认）；Spectre v2 新亚种 **Branch Target Reuse (BTR)**（**CVE-2026-64507／64508**，称内核已修）；开源权重模型 ExploitBench 讨论（仅作研究情报，不转载利用）。防御：尽快升 Chrome／Chromium 系；关注内核补丁。
  X（Chrome 154）：https://x.com/__kokumoto/status/2105072446617629158
  X（Spectre BTR）：https://x.com/__kokumoto/status/2105069290038915075
  X（ExploitBench）：https://x.com/pchees/status/2105074333324640336

- **【工具／新闻】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** **无升版**；Risky 仍 **RBNEWS616**／**SRB184**／**BTN184**（无变化）；tl;dr 仍 **#347**（无变化）。X B（~19h）：BounceBack／MEMEXEC／red-team-skill-tree／Nuclei v4 讨论／StrikeAgent／Red-Team-Roadmap／devZero 等（授权评估语境）。LWiS：OpenClaw／auth coercion／ProjectDiscovery Neo／Tern／DNS 红队／WSL Containers。

- **【APT／Malware · 大量 UNCONFIRMED】** C（~1.75h）：Allianz Indonesia／ServiceLlama／Adecco／KEL GROUP／印度政府实体／以色列空军等泄露售卖声称；INTENSE Group（m3rx）／Unique Repair（Kairos）勒索声称；Chromium/Android RCE 销售声称——**一律 UNCONFIRMED**。较有信号：DFIR Radar MSP360/ScreenConnect 钓鱼；Storm-3068（Microsoft DART 转述）／JadePuffer／Storm-3168（Microsoft Azure 破坏活动转述）。

- **【合并统计】** X **48** 唯一（A17／B10／C15／LWiS6；cross **0**；prior **0**；**+48** NEW）；`logged_in=true`／`@seogoogle4`／`blocked=false`；覆盖 A~0.83h／B~19h／C~1.75h／LWiS~11h；seen_ids **2148→2196**；报告 `/home/box/workspace/security-watch/reports/2026-09-29-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【KEV NEW · due 10-02】Apple Multiple Products CVE-2026-86950

CISA 于 **2026-09-29** 加入 KEV；联邦 due **2026-10-02**。CoreGraphics 越界写 → 任意代码执行；forensicTriage=Yes；knownRansomwareCampaignUse=Unknown。厂商补丁示例：**iOS/iPadOS 26.7.1**、**macOS Tahoe 26.7.1**、**macOS Sequoia 15.8.1**（2026-09-28）。报告称针对 iOS（iOS 27 前）的有限高度针对性攻击；致谢 Meta Product Security。防御：尽快更新受影响设备；按 BOD 26-04 做暴露面评估与 forensic triage。

地址：
- CISA Adds One：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 Apple 149226：https://support.apple.com/en-us/149226
- 厂商 Apple 149228：https://support.apple.com/en-us/149228
- 厂商 Apple 149229：https://support.apple.com/en-us/149229
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-86950
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-86950
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-86950
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- X（kokumoto）：https://x.com/__kokumoto/status/2105067358494879943

IoC：未见公开 IoC。

### 2. 【newly_overdue】Microsoft SharePoint CVE-2026-65660

联邦 due 曾为 **2026-09-28**，今日转入 **newly_overdue**。代码注入；授权攻击者可经网络执行代码；forensicTriage=Yes。防御：按 MSRC 应用缓解／更新；按 BOD 26-04 做 forensic triage；评估互联网暴露。（MSRC SPA。）

地址：
- 厂商 MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-65660
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-65660
- CISA Adds Two（09-25）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 3. 【newly_overdue】MikroTik RouterOS CVE-2026-67279

联邦 due 曾为 **2026-09-28**，今日转入 **newly_overdue**。行为工作流执行不当语境；公开九月公告页 HTTP 200 但未列 67279 ID（见 MikroTrick／CVE-2026-86060 族）。防御：按 MikroTik 九月安全公告升级；限制管理面；BOD 26-04。

地址：
- 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67279
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-67279
- CISA Adds Two（09-25）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 4. 【newly_overdue · 在野扫描】WordPress Core CVE-2026-87902

联邦 due 曾为 **2026-09-28**，今日转入 **newly_overdue**。路径遍历→条件 RCE／远程文件包含语境。X A：@jfernandogg 转述 CrowdSec 约 **30,813** 独特 IP／五日窗口信号（交叉以 CISA／GHSA 为准）。防御：升至 GHSA 所列补丁版本（示例 **7.1.2／7.0.6／6.9.9…**）；核验暴露面；BOD 26-04。

地址：
- 厂商 GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87902
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87902
- CISA Adds One（09-25）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog
- X（CrowdSec 转述）：https://x.com/jfernandogg/status/2105062567739888088
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 5. 【即将 due 09-30 · 在野】Citrix NetScaler CVE-2026-88771／CVE-2026-88772

CISA 于 **2026-09-27** 加入 KEV；联邦 due **2026-09-30**。88771：不当输入验证 → 未认证命令执行。88772：内存边界限制不当 → RCE/DoS。同公告族覆盖 **CVE-2026-88771–88778**（CTX697096）。KEV 备注称可在 NetScaler 控制台运行厂商 IoC 检查；本轮 enrich／可见厂商页 **未见可抄录具体哈希／IP IoC**（CTX694799 为应急步骤页；community bulletin Cloudflare/403）。X A 交叉：日语 CB 恶用确认、PitScaler／Mandiant web shells・tunneling（WHIPSHOT／SLAPSHOT）转述、BleepingComputer 卡片、多家 KEV 重复报道。防御：立即按 CTX 升 ADC/Gateway；按 CTX694799 疑似沦陷排查；限制管理面；BOD 26-04。**不转载利用步骤。**

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
- X（jp_cb_security）：https://x.com/jp_cb_security/status/2105072845256876156
- X（fredmdl／PitScaler）：https://x.com/fredmdl/status/2105065352443093460
- X（desmondsec2）：https://x.com/desmondsec2/status/2105065308608512248
- X（kokumoto／BC）：https://x.com/__kokumoto/status/2105065585654808972

IoC：未见公开 IoC（KEV／CTX 称厂商提供检查，可见抓取未列具体指标）。

### 6. 【仍逾期】WSO2 CVE-2026-5430／Adobe CVE-2026-71362

均自昨 newly_overdue 继续 overdue。**5430**：WSO2 多产品路径遍历 → 上传/RCE；按 **WSO2-2026-5328**。**71362**：Adobe Commerce/Magento 不正确授权；按 **APSB26-92**（helpx 出口 **403**）。防御：补丁落地核验；BOD 26-04。

地址：
- WSO2：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
- NVD 5430：https://nvd.nist.gov/vuln/detail/CVE-2026-5430
- KEV 5430：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-5430
- APSB26-92：https://helpx.adobe.com/security/products/magento/apsb26-92.html
- NVD 71362：https://nvd.nist.gov/vuln/detail/CVE-2026-71362
- KEV 71362：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-71362
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

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

KEV due 曾为 **2026-09-25**，继续 overdue。on-prem VCO 不当输入校验（CVSS 10，在野）。修复示例：**VCO 5.2.3.16+／6.4.2.8+**。防御：升 on-prem VCO；将 VCO Web 限制到可信管理网；按 SA-0183 狩猎下列 IoC；BOD 26-04。（抓取：curl **406**，WebFetch **200**。）

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

due 曾为 **2026-09-25**，继续 overdue。42016：令牌授权校验错误提权（修复示例 **≥7.133.11**）。42018：匿名令牌暴露。防御：按 JFrog Security Advisories／Self-Managed Releases 升版；限制管理面。

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
- **Pixel CVE-2026-58704**（due 曾=09-19）：装 Pixel 2026-09-01 更新。https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- **Cisco ISE CVE-2026-76460**（due 曾=09-19）：升 First Fixed（3.1→P12／3.2→P11／3.3→P12／3.4→P7／3.5→P4）。https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  IoC（厂商 SA／昨 enrich 原样）：`admin#show logging application ise-kong/access.log | include dummyuser`；日志路径 `./ise/logs/apigateway/access.log`
- **Acronis CVE-2026-87886**（due 曾=09-19）：按 SEC-10986（JS 墙）。https://security-advisory.acronis.com/advisories/SEC-10986

除 ISE 狩猎示例外，上列多数 **未见公开 IoC**。

### 12. 【X A】Chrome 154／CVE-2026-102331（ANGLE）

@__kokumoto 称 Chrome **154** 安全更新修 **33** 件漏洞，含 Critical **CVE-2026-102331**（ANGLE 缓冲溢出，CVSS 9.6）；作者称恶用未确认。防御：尽快升级 Chrome／Chromium 系浏览器至含修复构建。**不转载利用步骤。**

地址：
- X：https://x.com/__kokumoto/status/2105072446617629158
- NVD（若已收录）：https://nvd.nist.gov/vuln/detail/CVE-2026-102331
- Chrome Releases（交叉检索）：https://chromereleases.googleblog.com/

IoC：未见公开 IoC。

### 13. 【X A】Spectre v2 Branch Target Reuse（CVE-2026-64507／64508）

@__kokumoto 称 Spectre v2 新亚种 **Branch Target Reuse (BTR)** 可在数分钟内泄露 Linux root 密码哈希；涉及 **CVE-2026-64507／CVE-2026-64508**；正文称内核已修复。防御：关注发行版内核安全更新并尽快打补丁。**不转载攻击步骤。**

地址：
- X：https://x.com/__kokumoto/status/2105069290038915075
- NVD 64507：https://nvd.nist.gov/vuln/detail/CVE-2026-64507
- NVD 64508：https://nvd.nist.gov/vuln/detail/CVE-2026-64508

IoC：未见公开 IoC。

### 14. 【X A · 研究讨论】ExploitBench／开源权重模型

@pchees 讨论开源权重模型在 ExploitBench 上生成端到端 V8 exploit 的研究对比（正文时间线截断）。**仅作研究情报记录**；本报不转载任何利用代码或步骤。防御：关注 AI 辅助漏洞利用研究对沙箱与补丁优先级的影响。

地址：
- X：https://x.com/pchees/status/2105074333324640336

IoC：未见公开 IoC。

### 15. 【X A · DailyCVE 合辑】Undici／OpenTelemetry／Electron／Laravel 等

@dailycve 短帖列表（时间线多未展开外链）：**CVE-2026-18540**（Undici HTTP Response Splitting, Low）／**CVE-2026-81872**（OpenTelemetry-Go, Medium）／**CVE-2026-85008**（undici Caching/Replay, Low）／**CVE-2026-102674**（Electron Sandbox Escape, High）／**CVE-2026-102673**（Electron HTML Sandbox Bypass, High）／**CVE-2026-81869**（OpenTelemetry AttributeValueLengthLimit Bypass, Moderate）／**CVE-2026-102279**（Laravel XSS Debug Page, Low）／**CVE-2026-85152**（Undici Cache Poisoning, High）。防御：按依赖清单核对应组件版本与上游公告。

地址：
- X 示例：https://x.com/dailycve/status/2105067752603996580
- X：https://x.com/dailycve/status/2105064611221561819
- X：https://x.com/dailycve/status/2105061812576161815
- NVD 检索入口：https://nvd.nist.gov/vuln/search

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 核心工具版本（公开 pulse）

- **Sliver** 仍 **v1.7.7**（无升版）：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- **nuclei** 仍 **v3.11.1**（无升版）：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- **nuclei-templates** 仍 **v10.4.9**（无升版）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- Risky **无变化**：**RBNEWS616** https://risky.biz/RBNEWS616/（Intel ends paid bug bounties）· **BTN184** https://risky.biz/BTN184/（The AI crime machine）· SRB 仍 **SRB184a** https://risky.biz/SRB184a/
- tl;dr sec 仍 **#347**（无变化）：https://tldrsec.com/p/tldr-sec-347

### X Search B（~19h；授权红队／模拟向；不写利用步骤）

- **BounceBack**（红队行动安全隐蔽重定向器）：https://github.com/D00Movenok/BounceBack · X：https://x.com/DarkWebInformer/status/2105035388867719634
- **MEMEXEC**（Cobalt Strike BOF；内存运行 Windows EXE——仅授权仿真）：https://github.com/WeedHashPeddler/Mem-Exec · X：https://x.com/WeedPeddler/status/2105029407786340709
- **red-team-skill-tree**（全栈红队参考／教育）：https://github.com/lupingQAQ/red-team-skill-tree · X：https://x.com/lupingQAQ/status/2104923856272322987
- **Nuclei v4 能力讨论**（非版本发布；指向 projectdiscovery/nuclei）：https://github.com/projectdiscovery/nuclei · X：https://x.com/hackerkrd/status/2104895371285553496
- **StrikeAgent_AtkBrain-Flash**（渗透／红队／SRC／CTF AI Agent 平台介绍）：https://github.com/Yean-Sec/StrikeAgent_AtkBrain-Flash · X：https://x.com/Dinosn/status/2104865271030616563
- **Red-Team-Roadmap** Module 19／20（后渗透／侧移主题；教育路线图；不复述命令）：https://github.com/Dev-Chukwuma/Red-Team-Roadmap · X：https://x.com/httpschuks/status/2104861760918315117 · https://x.com/httpschuks/status/2104861728337023150
- **「无审查」LLM 项目介绍**（Offensive Security／红队研究语境；仅作情报记录；t.co 未展开）：X：https://x.com/JR_kneda/status/2104821680602542219
- **imputnet/cobalt＋yt-dlp**（名称歧义：视频工具非 Cobalt Strike；低相关误命中）：https://github.com/imputnet/cobalt · https://github.com/yt-dlp/yt-dlp · X：https://x.com/XiaoxiVVa/status/2104786205263147258
- **devZero**（红队基础设施／cyber range 拓扑画布；可导出 Terraform/Ansible）：https://github.com/devZero-Securi · X：https://x.com/5mukx/status/2104783066762023404

### LWiS 交叉工具／研究（~11h）

- **OpenClaw**（扫描状态公告；lolskills.io）：X：https://x.com/M_haggis/status/2104968373742473350
- **auth coercion／LoadLibraryA**（@_dirkjan 短评；未展开步骤）：X：https://x.com/_dirkjan/status/2104897081986945387
- **ProjectDiscovery Neo**（长期安全任务／agent 上下文；厂商公告；日期边界不确定）：X：https://x.com/pdiscoveryio/status/2104559779490521510
- **Tern**（feature complete／计划 beta；QUIC／Tailscale／Iroh 等）：X：https://x.com/_can1357/status/2105052776288137367
- **企业红队 DNS 通信演变**（@HackingLZ；引用 Kalshi「OpenAI pauses training…」声称标 **UNCONFIRMED**）：X：https://x.com/HackingLZ/status/2105031919515979948
- **WSL Containers GA**（Windows Developer／企业管理 Intune/Defender）：X：https://x.com/sinclairinat0r/status/2104992094964130201 · 厂商交叉：https://blogs.windows.com/

IoC：工具帖未见公开 IoC。

## APT / Malware 分析

### 1. 【X C】DFIR Radar · MSP360／ScreenConnect 钓鱼

@DFIR_Radar：2026-07 观察到的钓鱼活动滥用 **MSP360 RMM** 与 **ConnectWise ScreenConnect** 建立冗余远程访问通道，并投放凭证窃取和降低可见性的工具。防御：审核 RMM／远程访问工具授权与异常会话；钓鱼面加固。**不转载操作步骤。**

地址：
- X：https://x.com/DFIR_Radar/status/2105070597982347772

IoC：未见公开 IoC（帖摘要未列哈希／IP）。

### 2. 【X C · Microsoft 转述】Storm-3068／JadePuffer（Storm-3168）Azure

- **Storm-3068**（@BigVikDada 转述 Microsoft DART）：经成功自助密码重置、注册自身认证方法并保留身份，随后使用 Azure DevOps 管理工具和脚本。X：https://x.com/BigVikDada/status/2105066502147731666
- **JadePuffer／Storm-3168**（@Python_s_ 转述 Microsoft）：使用被攻陷 service principals 与高速自动化进行破坏性 Azure 活动；引用 Microsoft telemetry／Security Blog。X：https://x.com/Python_s_/status/2105037465849389496

防御：强化 SSPR／MFA 注册管控；审计 service principal／Azure DevOps 异常；对照 Microsoft 原文狩猎。交叉以微软官方博客为准（本窗口帖仅暴露 t.co）。

IoC：未见公开 IoC（帖摘要未列具体指标）。

### 3. 【X C · 未验证】勒索软件事件声称（合辑）

以下均为社交列表报道，**一律 UNCONFIRMED／未验证**；不复述利用步骤：

- **INTENSE Group**（波兰软件／IT；intense.pl）据报遭 **M3RX／m3rx**：https://x.com/FalconFeedsio/status/2105050616389308586 · https://x.com/ThreatAtlas/status/2105035034524848162 · 站点：https://intense.pl/
- **Unique Repair Services, Inc.**（美国；uniquerepair.com）据报遭 **Kairos**：https://x.com/FalconFeedsio/status/2105032675123945859 · 站点：https://uniquerepair.com/

IoC：未见公开 IoC。

### 4. 【X C · 未验证】地下泄露／售卖声称（合辑）

**一律 UNCONFIRMED／未验证**：

- Allianz Indonesia ~300k 记录声称：https://x.com/intels_daily/status/2105071905677943061 · 域名转述：`agencyconnect.allianz.co[.]id`
- ServiceLlama.com ~1.1M／247 MB 声称：https://x.com/DailyDarkWeb/status/2105070549760454682
- Adecco 8.6M PII/IBAN 声称：https://x.com/MonThreat/status/2105047904821956948
- Chromium／Android WebView Android 14–16 RCE exploit chain 销售声称（**不转载细节**）：https://x.com/MonThreat/status/2105047460469186797
- ChimeraZ／KEL GROUP（Orisha）~1.3M／110 GB 声称：https://x.com/intels_daily/status/2105041714909999167
- Broward University 虚拟网络材料声称：https://x.com/DailyDarkWeb/status/2105039370961248509
- ByteToBreach／印度多政府实体数据售卖声称：https://x.com/intels_daily/status/2105032729062428767
- CuteGhost666／以色列空军 ~80k 人声称：https://x.com/intels_daily/status/2105032179767976168

IoC：未见可核验公开 IoC（仅帖文域名转述，不作确认）。

### 5. 【X C】其他

- GPON 接入网威胁检测混合 malware analysis framework（进行中项目）：https://x.com/the__tomiwa/status/2105040531143479633

### 6. ICS

本日公开备援主条以 **KEV NEW Apple 86950**、**newly_overdue SharePoint／MikroTik／WordPress**、**仍逾期网关／编排／APM／VPN／Artifactory** 与 **upcoming Citrix／Apple** 为主；**无单独新突出的 2026-09-29 ICS advisory 主条**。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Arista VeloCloud CVE-2026-93952（仍逾期）**：`/usr/local/sbin/.vcnode.js`；`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）；`/etc/systemd/system/vc-sysmon.service`；HTTP 头 `x-vc-opt`；IP `142.93.149.77`／`104.248.126.159`。（来源：今日 enrich-extra／SA-0183／`/workspace/enrich-2026-09-29/arista-0183-iocs-from-webfetch.txt`）
- **Check Point 85102／93616（仍逾期）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`。（来源：昨日报告／昨日厂商 SK／enrich；今日 enrich-extra 未重抄）
- **Cisco ISE 76460（仍逾期）**：狩猎示例 `admin#show logging application ise-kong/access.log | include dummyuser`；路径 `./ise/logs/apigateway/access.log`。（来源：昨日报告／Cisco SA）
- **Citrix 88771／88772／newly_overdue 三件套／Apple 86950／其余仍逾期／工具仓／C 勒索与泄露声称**：未见可抄录公开 IoC（或仅厂商 SK／新闻原文内；Citrix KEV 称有厂商 IoC 检查但可见页未列具体指标；C 帖多为域名转述且 **UNCONFIRMED**）
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

本窗口 LWiS List 只读采集：扫描约 **17** 条、保留 **6** 条、覆盖约 **11h**（`logged_in=true`／`@seogoogle4`／`blocked=false`；成员页显示 **502**）；跨源 ID 重叠 0（相对 A／B／C）；含 OpenClaw、auth coercion、ProjectDiscovery Neo、Tern、DNS 红队、WSL Containers 等；meta：`/workspace/x-lwis-list-meta-2026-09-29.json`。

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
- CISA 09-29 Adds One（Apple 86950）：https://www.cisa.gov/news-events/alerts/2026/09/29/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-27 Adds Two（Citrix 88771／88772）：https://www.cisa.gov/news-events/alerts/2026/09/27/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 09-27 Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- CISA 09-25 一条 KEV 警报（87902）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-25 两条 KEV 警报（65660＋67279）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
