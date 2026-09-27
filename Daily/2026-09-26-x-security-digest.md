# X 安全情报晚报 · 2026-09-26

> 搜集窗口：圣地亚哥时间 **2026-09-25 20:00 至 2026-09-26 ~20:35**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周六）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-26.json`（collected_at **2026-09-26T20:23:21-03:00**）＋ `/workspace/tools-news-pulse-2026-09-26.json`＋ `/workspace/enrich-extra-2026-09-26.json`＋ `/workspace/enrich-2026-09-26/`。CISA KEV catalogVersion **2026.09.25**／**1726** 条／dateReleased **2026-09-25T18:58:16.5029Z**（相对昨日 **2026.09.25／1726**：**count Δ0**；**无 NEW** dateAdded=2026-09-26；**无 due_today**）。昨日 CISA 警报仍适用交叉：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog ＋ https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog 。
> **新起逾期（due 曾=09-25）**：**Check Point CVE-2026-85102／CVE-2026-93616**、**Arista VeloCloud CVE-2026-93952**、**F5 BIG-IP APM CVE-2026-94127**、**JFrog Artifactory CVE-2026-42016／CVE-2026-42018**。**仍逾期**：**Zyxel CVE-2026-7273**；**MS CVE-2026-81963／CVE-2026-85880**（due 曾=09-22）；**Chromium CVE-2026-87491／CVE-2026-85046**；**Pixel CVE-2026-58704**／**Cisco ISE CVE-2026-76460**／**Acronis CVE-2026-87886**。**即将 due 09-27**：**WSO2 CVE-2026-5430**／**Adobe CVE-2026-71362**。**即将 due 09-28**：**SharePoint CVE-2026-65660**／**MikroTik CVE-2026-67279**／**WordPress CVE-2026-87902**。
> X：`/workspace/x-posts-2026-09-26.json`（合并 **67** 条唯一：A24／B17／C14／LWiS12；跨源 ID 重叠 **0**；相对 prior seen_ids 重叠 **11**／**+56** 新 id；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **8h**。Search B 可见约 **48h**（含 Sep 23–25 工具帖，其中 11 条已见 prior）。Search C 约 **7h**。LWiS List 约 **20h**（**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。抓取备注：Adobe APSB26-92 box 出口 **403**；F5 myF5 鉴权墙；Arista SA-0183 curl 初 **406**、urllib 后 **200**。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【主条 · KEV Δ0 · 无 NEW／无 due_today】** CISA KEV 仍为 catalogVersion **2026.09.25**／**1726** 条／dateReleased **2026-09-25T18:58:16.5029Z**（相对昨日 **Δ0**；CVE 集合相同）。今日 **无** dateAdded=2026-09-26 NEW、**无** dueDate=2026-09-26。昨日两条 CISA 警报仍作交叉：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog · https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog

- **【新起逾期 · Check Point／Arista／F5／JFrog】** due 曾为 **09-25**，今日起 **newly_overdue**：**CVE-2026-85102／93616**（Check Point）、**93952**（Arista VeloCloud，厂商 SA-0183 含 IoC）、**94127**（F5 BIG-IP APM）、**42016／42018**（JFrog）。防御：立即按厂商 SK／SA／K 文／advisories 补丁与临时缓解；BOD 26-04。
  Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
  SK85102：https://support.checkpoint.com/results/sk/sk1000117
  SK93616：https://support.checkpoint.com/results/sk/sk1000171/
  Arista SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
  F5 K000162605：https://my.f5.com/manage/s/article/K000162605
  JFrog advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories

- **【仍逾期 · Zyxel／MS／Chromium／Pixel／ISE／Acronis】** **Zyxel CVE-2026-7273**（due 曾=09-24）；MS **81963／85880**（due 曾=09-22）；Chromium **87491／85046**；Pixel **58704**／Cisco ISE **76460**／Acronis **87886**。防御：核验补丁落地；BOD 26-04。
  Zyxel：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
  MSRC 81963：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963
  MSRC 85880：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880

- **【即将 due 09-27 · WSO2／Adobe】** **CVE-2026-5430**（WSO2）／**CVE-2026-71362**（Adobe Magento／Commerce APSB26-92）。防御：按 WSO2-2026-5328／APSB26-92 升版；BOD 26-04。（Adobe 页 box 出口仍 **403**，仍列已知厂商 URL。）
  WSO2：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
  APSB26-92：https://helpx.adobe.com/security/products/magento/apsb26-92.html

- **【即将 due 09-28 · SharePoint／MikroTik／WordPress】** 昨日 NEW KEV 三件套联邦 due **09-28**：**CVE-2026-65660**／**67279**／**87902**。X 今日续有 SharePoint／MikroTik／WP／MicroTrick 讨论。
  SharePoint MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660
  MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
  WP GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp

- **【X 高信号 · PeopleSoft／Cisco 声称／CMS／插件】** Mandiant／GTIG：**Oracle PeopleSoft CVE-2026-35273** 被 UNC6240（ShinyHunters）大规模利用（Mandiant：https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/ · THN：https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html）。Cisco Secure Firewall FMC **20079／20316**「Sandworm 串联」声称——**UNCONFIRMED**。另有 Drupal **96362**、Kyverno **100706**、Joomla UP **97160–97163**、Grav **42608**、Capsule **61795**、Bookly **93399**、OpenClaw **100599**、Check Point **93616** 等交叉。

- **【工具／新闻】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** **无升版**；Risky 仍 **RBNEWS615**（https://risky.biz/RBNEWS615/）／SRB184（https://risky.biz/SRB184a/）／BTN183；tl;dr 仍 **#347**（https://tldrsec.com/p/tldr-sec-347）。X B：Sliver／Mythic／Adaptix／Red-Team-Roadmap／Comment2Shell／Stratus／EvilMist／HackMyAgent／deepteam／dpapi-toolkit／nuclei 87902 等。

- **【X 交叉 · APT／Malware】** C（~7h）：多起地下泄露／勒索宣传（Interpol NCB 印尼、Blue Locker 画像、罗马尼亚 RouterOS 访问售卖、BARRACUDA／e-icc、TheGentlemen／FTAPI、西班牙 CN-CERT、FiveWest、韩政府邮箱、BLACKLOCKS／ARCA、khazna.app、约旦电力、印度酒店 PMS、Data.com／Salesforce、山东健康记录等）——**一律 UNCONFIRMED**。LWiS（~20h）：HEIF Heist／IDA MCP／ADCS ESC_CES／Omarchy LPE／Electrovolt／链接汇总等。

- **【合并统计】** X **67** 唯一（A24／B17／C14／LWiS12；cross **0**；prior **11**；**+56** NEW）；`logged_in=true`／`@seogoogle4`／`blocked=false`；seen_ids **2025→2081**；报告 `/home/box/workspace/security-watch/reports/2026-09-26-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【新起逾期 · 在野】Check Point CVE-2026-85102／CVE-2026-93616

CISA 于 **2026-09-22** 加入 KEV；联邦 due 曾为 **2026-09-25**，今日起 **newly_overdue**。85102：VPN 不当证书校验 → 未认证 RCE。93616：管理面路径穿越 → 未认证脚本上传／执行。修复示例见 SK：85102 — **R82.10 Jumbo Take 44+／R82 Take 126+／R81.20 Take 166+**；93616 — **R82.20 Hotfix／R82.10 Take 45+／R82 Take 127+／R81.20 Take 170+** 等。X A 今日续标 93616 在野：https://x.com/gettransilience/status/2103862544783888846 。防御：立即按 SK 打 Jumbo／Hotfix；限制管理／VPN 面；证书 subject 狩猎；BOD 26-04。**不转载利用步骤。**

地址：
- 厂商 SK85102：https://support.checkpoint.com/results/sk/sk1000117
- 厂商 SK93616：https://support.checkpoint.com/results/sk/sk1000171/
- Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
- NVD 85102：https://nvd.nist.gov/vuln/detail/CVE-2026-85102
- NVD 93616：https://nvd.nist.gov/vuln/detail/CVE-2026-93616
- KEV 85102：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85102
- KEV 93616：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-93616
- X（93616）：https://x.com/gettransilience/status/2103862544783888846
- 可见文章：https://threatnews.transilience.cloud/report/cve/cve-2026-93616
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC（厂商 SK／博客观测 cert_subject，原样抄录自 enrich vendor，非穷尽）：
- `CN=vpn,OU=users,O=global`
- `CN=vpn-user,OU=users,O=global`
- `CN=vpnuser,OU=users,O=global`

### 2. 【新起逾期 · 在野】Arista VeloCloud CVE-2026-93952

KEV due 曾为 **2026-09-25**，今日起 **newly_overdue**。on-prem VCO 不当输入校验；成功利用可影响编排器机密性／完整性／可用性。修复示例：**VCO 5.2.3.16+／6.4.2.8+**。防御：升 on-prem VCO；将 VCO Web 限制到可信管理网；按 SA-0183 狩猎下列 IoC；BOD 26-04。（抓取：curl 初 **406**，urllib 后 **200**。）

地址：
- 厂商 SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-93952
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-93952
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC（厂商 SA-0183／enrich vendor 原样抄录，非穷尽）：
- 文件：`/usr/local/sbin/.vcnode.js`
- 文件：`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）
- 文件：`/etc/systemd/system/vc-sysmon.service`
- HTTP 头：`x-vc-opt`
- IP：`142.93.149.77`
- IP：`104.248.126.159`

### 3. 【新起逾期 · 在野】F5 BIG-IP APM CVE-2026-94127

KEV due 曾为 **2026-09-25**，今日起 **newly_overdue**。虚拟服务器配置访问策略＋OAuth profile 时堆溢出 → 未认证数据面 RCE。X A 称可在 `/var/log/ltm` 检索 APM+OAuth 访问痕迹；另有地下论坛 RCE 声称——**论坛声明 UNCONFIRMED**。防御：按 K000162605 盘点 APM＋OAuth VS；先临时 iRule 再 ENG hotfix；BOD 26-04。（myF5 鉴权墙，仍列已知厂商 URL。）

地址：
- 厂商 K000162605：https://my.f5.com/manage/s/article/K000162605
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94127
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-94127
- X：https://x.com/imranahmed005/status/2103923049519325661
- X（论坛声称）：https://x.com/MonThreat/status/2103922092617929140

IoC：未见公开 IoC。

### 4. 【新起逾期 · near】JFrog Artifactory CVE-2026-42016／CVE-2026-42018

公开备援列 due 曾为 **2026-09-25**，今日起 **newly_overdue**。42016：token scope 校验特权提升（修复示例 **≥7.133.11**）。42018：匿名 token 泄露面（匿名访问禁用时仍可能向未认证调用者返回内部匿名用户 token）。防御：按 JFrog Security Advisories／Self-Managed Releases 升版；限制 Artifactory 管理面。

地址：
- NVD 42016：https://nvd.nist.gov/vuln/detail/CVE-2026-42016
- NVD 42018：https://nvd.nist.gov/vuln/detail/CVE-2026-42018
- KEV 42016：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-42016
- KEV 42018：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-42018
- 厂商 advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- 发行说明：https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases

IoC：未见公开 IoC。

### 5. 【仍逾期 · 在野】Zyxel GS1900 CVE-2026-7273

KEV due 曾为 **2026-09-24**，继续 overdue。LAN 向 CGI 栈溢出 → 未认证 OS 命令面。防御：升至列明 **2.90(*.2)C0** 固件；限制 LAN 管理暴露；BOD 26-04。

地址：
- 厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 6. 【仍逾期 · 在野】Microsoft CVE-2026-81963／CVE-2026-85880

KEV due 曾为 **2026-09-22**，继续 overdue。81963：Windows Update Stack 链接跟随 → 本地提权至 SYSTEM。85880：Windows 堆溢出。防御：核验 9 月 Windows 安全更新已落地；盘点未补丁主机；BOD 26-04。

地址：
- MSRC 81963：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963
- MSRC 85880：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880
- NVD 81963：https://nvd.nist.gov/vuln/detail/CVE-2026-81963
- NVD 85880：https://nvd.nist.gov/vuln/detail/CVE-2026-85880
- KEV 81963：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-81963
- KEV 85880：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85880

IoC：未见公开 IoC。

### 7. 【仍逾期 · 在野】Chromium 87491／85046／Pixel 58704／Cisco ISE 76460／Acronis 87886

仍逾期重点：Chromium **CVE-2026-87491**（due 09-23；Chrome **153.0.8010.36+**）／**CVE-2026-85046**（due 09-18）；Pixel **CVE-2026-58704**／Cisco ISE **CVE-2026-76460**／Acronis **CVE-2026-87886**（due 09-19）。防御：按厂商公告补丁；BOD 26-04。

地址：
- Chrome 87491：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- NVD 87491：https://nvd.nist.gov/vuln/detail/CVE-2026-87491
- Chrome 85046：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- NVD 85046：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
- Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- NVD 58704：https://nvd.nist.gov/vuln/detail/CVE-2026-58704
- Cisco ISE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- NVD 76460：https://nvd.nist.gov/vuln/detail/CVE-2026-76460
- Acronis：https://security-advisory.acronis.com/advisories/SEC-10986
- NVD 87886：https://nvd.nist.gov/vuln/detail/CVE-2026-87886

IoC：未见公开 IoC（或仅厂商 SK／通报内）。

### 8. 【即将 due 09-27 · 在野】WSO2 CVE-2026-5430／Adobe CVE-2026-71362

联邦 due **2026-09-27**（明日）。5430：路径穿越 → 未受限上传／可致 RCE（厂商顾问 WSO2-2026-5328）。71362：不正确授权（CWE-863）；公告 **APSB26-92**（box 出口曾 **403**，仍列已知 URL）。X A 今日讨论 WSO2／Adobe／SharePoint KEV 修补优先级：https://x.com/intels_daily/status/2103924358682964184 。防御：按顾问／APSB 升版；BOD 26-04。

地址：
- 厂商 WSO2-2026-5328：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
- NVD 5430：https://nvd.nist.gov/vuln/detail/CVE-2026-5430
- KEV 5430：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-5430
- 厂商 APSB26-92：https://helpx.adobe.com/security/products/magento/apsb26-92.html
- NVD 71362：https://nvd.nist.gov/vuln/detail/CVE-2026-71362
- KEV 71362：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-71362
- X：https://x.com/intels_daily/status/2103924358682964184

IoC：未见公开 IoC。

### 9. 【即将 due 09-28 · 在野】Microsoft SharePoint CVE-2026-65660

CISA 于 **2026-09-25** 加入 KEV；联邦 due **2026-09-28**；forensicTriage=Yes。代码注入（CWE-94）→ 授权攻击者可经网络执行代码。X 今日续有讨论：https://x.com/SecNews_GR/status/2103886626728358272 。防御：按 MSRC 更新指南尽快打补丁；盘点互联网／内网暴露的 SharePoint；BOD 26-04 法医分流。**本报不转载利用细节。**

地址：
- CISA 09-25 警报（两条）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 厂商 MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-65660
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-65660
- X：https://x.com/SecNews_GR/status/2103886626728358272
- 文章：https://www.secnews.gr/736205/cve-2026-65660-sharepoint-mikrotik/?fsp_sid=15073
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 10. 【即将 due 09-28 · 在野】MikroTik RouterOS CVE-2026-67279（＋链 86060／MicroTrick）

CISA 于 **2026-09-25** 加入 KEV；联邦 due **2026-09-28**。行为工作流执行不当（CWE-841）→ 未认证会话通道／exec 请求；可链式至 CVE-2026-86060。X 称 MicroTrick 仓库描述链式无认证管理员权限——**仅防御认知／仓库定位，不转载 PoC 步骤**。防御：尽快升 RouterOS；检查 Flagged 状态与未知脚本／用户；限制管理面；BOD 26-04。

地址：
- CISA 09-25 警报（两条）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67279
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-67279
- MicroTrick 仓库（防御提及）：https://github.com/digiprosec/MicroTrick
- X（MicroTrick）：https://x.com/ridvanyagli/status/2103888375463788597
- X（西语串联）：https://x.com/jfernandogg/status/2103922554591396052
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC（厂商建议检查 Flagged 状态与未知脚本／用户）。

### 11. 【即将 due 09-28 · 在野】WordPress Core CVE-2026-87902

CISA 于 **2026-09-25** 加入 KEV；联邦 due **2026-09-28**；forensicTriage=Yes。远程文件包含（CWE-98）→ 未认证可选本地 `.php` 纳入页面模板解析／条件 RCE。X 称补丁后数小时出现利用尝试——**探测／在野流量声称 UNCONFIRMED**；建议 **4.7.0–7.1.1** 升至 **7.1.2+**。防御：立即按 GHSA 升至列明补丁版本；盘点公开 WordPress；用 nuclei-templates 做**授权**暴露面核查；BOD 26-04。**不转载利用步骤。**

地址：
- CISA 09-25 警报（一条）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87902
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87902
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-87902.yaml
- X：https://x.com/technobezz/status/2103919422935064815
- X B（prior_seen）：https://x.com/DhiyaneshDK/status/2102720074809544970
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 12. 【X A · 高信号】Oracle PeopleSoft CVE-2026-35273（Mandiant／ShinyHunters）

Mandiant／Google GTIG 报告：UNC6240（ShinyHunters）对 Oracle PeopleSoft 发起新一轮大规模利用，称可绕过 WAF；建议立即按 Oracle／Mandiant 指引修复并排查 web shell／持久化。多帖交叉（含西语／阿语转述）。**FBI 事件与 PeopleSoft 关联在个别帖中明确称尚未确认**——勿自行串联。防御：盘点 PeopleSoft 暴露面；按厂商补丁；狩猎异常 POST／web shell；BOD 风格优先级。**不转载利用步骤。**

地址：
- Mandiant／GTIG：https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/
- The Hacker News：https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html
- X（Mandiant 转发）：https://x.com/SnoopyLinkin/status/2103880495733805386
- X：https://x.com/rafael_a_rosado/status/2103971668481769507
- X：https://x.com/alawbathani/status/2103970682325401873
- X：https://x.com/BotBauR/status/2103958153461215651
- X：https://x.com/DiarioBitcoin/status/2103889366787489919

IoC：未见公开 IoC（详见 Mandiant 原文）。

### 13. 【X A · UNCONFIRMED】Cisco Secure Firewall FMC CVE-2026-20079／20316「Sandworm」声称

日文技术解说称 Cisco Secure Firewall Management Center 的 **CVE-2026-20079** 与 **CVE-2026-20316** 被 Sandworm 串联利用，并提到改良版 Cyclops——**UNCONFIRMED**；勿当作已证实归因。防御：核查边界设备型号／补丁状态；对照 Cisco 官方公告。

地址：
- X：https://x.com/iss_kk_official/status/2103987769240695126

IoC：未见公开 IoC。

### 14. 【X A · 非 KEV】Drupal／Kyverno／Joomla UP／Grav／Capsule／Bookly／OpenClaw／Citrix 澄清

- **Drupal CVE-2026-96362**：ZoomEye 称可致代码执行／提权／XSS；防御盘点暴露实例并修补——**利用细节 UNCONFIRMED**。X：https://x.com/zoomeyebot/status/2103979200449552796
- **Kyverno CVE-2026-100706**：称租户权限可升级为集群管理员；属分析／PoC 线索，需核验影响版本。**不转载 PoC。** X：https://x.com/xhackio/status/2103970693386002862
- **Joomla UP 插件 CVE-2026-97160–97163**：称无登录可读 `configuration.php`；UP **6.1.0** 修复。X：https://x.com/mysitesguru/status/2103967101304103093 · 文章：https://mysites.guru/blog/up-plugin
- **Grav CMS CVE-2026-42608**：FormFlash 未认证路径遍历；公开修复称仅列 **2.0.0-beta.2**。X：https://x.com/_pksharma/status/2103924512102211909
- **Capsule CVE-2026-61795**：Kubernetes tenant webhook 旧正则允许畸形 AllowedHostnames.Regex；CVSS 声称 6.8、帖称未修复。X：https://x.com/HugoValters/status/2103923307942920444
- **Bookly WP 插件 CVE-2026-93399**：未认证 IDOR（CVSS 声称 9.1）；称 PoC 已公开——**不转载 PoC**。X：https://x.com/PadhiyarRushi/status/2103893520293736719
- **OpenClaw ＜2026.7.1**：称新增高危 CVE，含 **CVE-2026-100599**（Google Meet node approval 绕过／节点执行）。X：https://x.com/ridvanyagli/status/2103885569889534373
- **OpenCTI CVE-2026-76822**：Case Creation 授权缺陷；核对官方公告。X：https://x.com/zoomeyebot/status/2103888603432771611
- **Citrix NetScaler**：有帖质疑「新零日」；评论澄清对应已披露修复的 **CVE-2026-19490**（认证绕过）——**勿把未经证实零日说法当事实**。X：https://x.com/jeredbare/status/2103919745775129086 · https://x.com/blondecapitalvc/status/2103889685957513386

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 核心版本脉冲（公开备援）

Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 相对昨日 **无升版**。Risky Business 仍 **RBNEWS615**（标题摘要：Major vulnerability found in ancient TACACS+ networking protocol）；SRB184／BTN183 不变；tl;dr 仍 **#347**。

地址：
- Sliver：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- nuclei：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- RBNEWS615：https://risky.biz/RBNEWS615/
- SRB184a：https://risky.biz/SRB184a/
- BTN183：https://risky.biz/BTN183/
- tl;dr #347：https://tldrsec.com/p/tldr-sec-347

IoC：未见公开 IoC。

### X Search B／相关工具仓（防御认知）

覆盖约 **48h**（含 Sep 23–25；其中 **11** 条 prior_seen）。仅列防御认知／仓库定位；**不转操作步骤**；能力描述 **UNCONFIRMED**。

- **Sliver**（BishopFox；授权对手模拟）：https://github.com/BishopFox/sliver · X：https://x.com/AlAssaf_H/status/2103850433219268943
- **Mythic**（模块化多代理 C2／协作红队；防御检测验证）：https://github.com/its-a-feature/Mythic · X：https://x.com/AlAssaf_H/status/2103850054997963011
- **Red-Team-Roadmap** Module 11–15（训练向／Linux 提权误配置／DVWA／Web 枚举／密码喷洒风险）：https://github.com/Dev-Chukwuma/Red-Team-Roadmap · X：https://x.com/httpschuks/status/2103745239282303457 · https://x.com/httpschuks/status/2103445975100527016 · https://x.com/httpschuks/status/2103445525643092228 · https://x.com/httpschuks/status/2103434817228406932 · https://x.com/httpschuks/status/2103026922074653122
- **Adaptix 云死信 C2**（Azure Blob／OneDrive；prior_seen）：https://github.com/stillbigjosh/adaptix-graph-c2 · 文章：https://stillbigjosh.github.io/writeup.html?file=writeups/adaptix-graph-c2.md · X：https://x.com/stillbigjosh/status/2103455702945796331
- **Comment2Shell**（Nuclei 模板／Docker lab——授权验证暴露面；prior_seen）：https://github.com/DeathShotXD/Comment2Shell · X：https://x.com/XssPayloads/status/2103440816941523278
- **Stratus Red Team**（云对手模拟／检测验证；prior_seen）：https://github.com/DataDog/stratus-red-team · X：https://x.com/rilopezp/status/2103297811676807493
- **BotC2-RAT**（逆向／C2 仿真材料；prior_seen）：https://github.com/ShadowOpCode/BotC2-RAT/blob/main/BotC2_RAT.pdf · X：https://x.com/blackstormsecbr/status/2103220590740140368
- **EvilMist**（Cloud／Entra ID；仅授权；prior_seen）：https://github.com/Logisek/EvilMist · X：https://x.com/EsGeeks/status/2102910572857614577
- **HackMyAgent**（AI agents／MCP 扫描；prior_seen）：https://github.com/opena2a-org/hackmyagent · X：https://x.com/EsGeeks/status/2102777566515847519
- **deepteam**（LLM／AI agent red-team；prior_seen）：https://github.com/confident-ai/deepteam · X：https://x.com/ChrisShort/status/2102773315643334713
- **dpapi-toolkit**（Windows DPAPI 工件识别；prior_seen）：https://github.com/crypt0p3g/dpapi-toolkit · X：https://x.com/cryptopeg/status/2102753493123752365
- **nuclei-templates WP CVE-2026-87902**（prior_seen）：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-87902.yaml · X：https://x.com/DhiyaneshDK/status/2102720074809544970
- **PROJECT-LION／Dialers_splitter.yaml**（检测规则片段；帖未给可核验仓库）：X：https://x.com/lexs17/status/2103723194095956075

IoC：工具帖未见公开 IoC。

### LWiS 相关研究／工具向交叉

覆盖约 **20h**（**交叉校验，不假装 24h Latest**）。

- **Hex-Rays 官方 IDA MCP Server**（免费开源；隔离分析环境评估 agent 权限）：文章：https://hex-rays.com/blog/hex-rays-ida-mcp-server · X：https://x.com/HexRaysSA/status/2103896696027807843
- **HEIF Heist**（HacktronAI／图像解析器静默修复讨论；无 CVE／发行版补丁语境）：X：https://x.com/S1r1u5_/status/2103990017291145447 · https://x.com/dinodaizovi/status/2103584561586385072
- **ADCS ESC_CES**（NTLM relay 至 AD CS 高权限路径）：文章：https://adhdmurky.github.io/posts/post4/ · X：https://x.com/ipurple/status/2103799345535664358
- **Omarchy LPE《Haptics Havoc》**：文章：https://www.piratemoo.com/haptics-havoc-an-omarchy-lpe/ · X：https://x.com/apiratemoo/status/2103681252184539297
- **Electrovolt／Electron＋V8**（DEF CON 研究；Speaker Deck）：https://speakerdeck.com/s1r1us/electrovolt-pwning-popular-desktop-apps-while-uncovering-new-attack-surface-on-electron?slide=2 · X：https://x.com/S1r1u5_/status/2103796315423416553
- **Sep 25 高分享链接汇总**（MS 记录暴露／Kiteworks／EDR 规避／CF 容器跨租户／Google Agentic Hacks）：X：https://x.com/ntlmrelay/status/2103802438109073541 · https://blog.faav.net/how-i-couldve-accessed-17-trillion-microsoft-records · https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html · https://www.scworld.com/brief/new-edr-evasion-technique-proves-difficult-to-detect · https://blog.cloudflare.com/containers-cross-tenant-vulnerability/ · https://blog.google/security/agentic-hacks-real-proofs-inside-googles-pagebreak-project/

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. 【Mandiant】UNC6240／ShinyHunters → Oracle PeopleSoft

见上文 CVE 节第 12 条。Mandiant／GTIG 主报告与 THN 转述；X 多帖交叉。防御：PeopleSoft 暴露面盘点、补丁、web shell／后门狩猎。

地址：
- Mandiant：https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/
- THN：https://thehackernews.com/2026/09/attackers-bypass-wafs-to-exploit-oracle.html
- X：https://x.com/SnoopyLinkin/status/2103880495733805386

IoC：未见公开 IoC（详见 Mandiant 原文）。

### 2. 【X C】Blue Locker Ransomware 威胁画像（SOC Radar）

@rst_cloud 指向 SOC Radar 威胁行为者画像：Blue Locker，并列出 Proton／Limba／Zola／Shinra／Loki／Blackbit／Fonix／Memecryptor／Conti 等相关标签——属威胁情报转述。防御：对照 SOC Radar 原文更新检测与勒索响应手册。

地址：
- X：https://x.com/rst_cloud/status/2103984474937573823
- 文章：https://socradar.io/blog/dark-web-profile-blue-locker-ransomware/

IoC：未见公开 IoC（详见原文）。

### 3. 【X C · 未验证】地下勒索／泄露声称（合辑）

以下均为社交列表报道，**一律 UNCONFIRMED／未验证**；不复述利用步骤：

- YUKA／印尼 Interpol NCB「管理后台 SQLi」声称：https://x.com/intels_daily/status/2103984749417005265
- 罗马尼亚中小企业网络「RouterOS 完全管理权限」初始访问售卖：https://x.com/DarkWebInformer/status/2103942020909732295
- BARRACUDA／美国 International Chemical Company（e-icc.com）勒索声称：https://x.com/FalconFeedsio/status/2103932255681089633 · https://e-icc.com/
- TheGentlemen／德国 FTAPI Software 受害者声称：https://x.com/DailyDarkWeb/status/2103931917141946383 · https://www.ftapi.com/
- CUTZINGER／西班牙 CN-CERT／CNI 入侵威胁声称（帖自标 UNCONFIRMED）：https://x.com/VECERTRadar/status/2103919713034060144
- BLACKNET-00／南非 FiveWest 文件／证件／密钥声称：https://x.com/Splint3r7/status/2103916658557321527
- 韩国政府邮箱「500+ 官方文件」声称（帖称发生于 2025）：https://x.com/Splint3r7/status/2103916585165389952
- BLACKLOCKS／南非 ARCA Unlimited Architects：https://x.com/FalconFeedsio/status/2103911797942321523 · https://arcaunlimited.com/
- milo9477／khazna[.]app（MySQL／GCP Cloud SQL／Magento）售卖声称：https://x.com/intels_daily/status/2103909254524457430
- Elite Squad／约旦电力／JEPCO「约 8 GB」声称：https://x.com/CyberPulse56/status/2103889984487084088
- DDEEAALLEERR／印度酒店 PMS「约 5 万预订」声称：https://x.com/CyberPulse56/status/2103888967062217002
- CuteGhost666／Data.com／Salesforce「最高 15 亿条」声称：https://x.com/CyberPulse56/status/2103886860527518161
- 中国山东省「183 万健康记录」售卖声称：https://x.com/intels_daily/status/2103879048812224770

IoC：帖文可见受害方域名声称（非核验）— `e-icc.com`／`ftapi.com`／`arcaunlimited.com`／`khazna[.]app`；其余多数 **未见公开 IoC**。

### 4. 【LWiS】HEIF Heist／AI 辅助利用链讨论

@S1r1u5_／@dinodaizovi／@LiveOverflow 讨论 HacktronAI HEIF Heist：上游静默修复的图像解析器漏洞、模型构造 oracle／堆读写原语、复杂利用链与自动化改变攻击经济学——属研究／讨论向；**不转载利用步骤**。防御：关注图像编解码器补丁与沙箱策略；评估 AI 辅助利用对补丁 SLA 的影响。

地址：
- X：https://x.com/S1r1u5_/status/2103990017291145447
- X：https://x.com/dinodaizovi/status/2103584561586385072
- X：https://x.com/LiveOverflow/status/2103800907733368861
- X：https://x.com/LiveOverflow/status/2103798894400581831

IoC：未见公开 IoC。

### 5. 【LWiS】ADCS／Omarchy LPE／Electron 研究

- ADCS ESC_CES：https://x.com/ipurple/status/2103799345535664358 · https://adhdmurky.github.io/posts/post4/
- Omarchy LPE：https://x.com/apiratemoo/status/2103681252184539297 · https://www.piratemoo.com/haptics-havoc-an-omarchy-lpe/
- Electrovolt：https://x.com/S1r1u5_/status/2103796315423416553 · https://speakerdeck.com/s1r1us/electrovolt-pwning-popular-desktop-apps-while-uncovering-new-attack-surface-on-electron?slide=2
- n-day／V8 sandbox 讨论：https://x.com/S1r1u5_/status/2103799470588858878
- DNS 工具沙箱绕过时序追问：https://x.com/vikhyatk/status/2103736063802110318

IoC：未见公开 IoC。

### 6. ICS

本日公开备援 **无单独突出的 2026-09-26 新 ICS advisory 主条**（KEV catalog Δ0）。网关／编排／APM／VPN／Artifactory 类以 **newly_overdue** 桶为主。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Arista VeloCloud CVE-2026-93952（新起逾期）**：`/usr/local/sbin/.vcnode.js`；`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）；`/etc/systemd/system/vc-sysmon.service`；HTTP 头 `x-vc-opt`；IP `142.93.149.77`／`104.248.126.159`。（来源：enrich vendor SA-0183）
- **Check Point 85102／93616（新起逾期）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`；另见 sk1000171 厂商狩猎节。（来源：enrich vendor SK／博客）
- **地下声称可见域名（UNCONFIRMED）**：`e-icc.com`／`ftapi.com`／`arcaunlimited.com`／`khazna[.]app`。
- **SharePoint 65660／MikroTik 67279／WP 87902／Zyxel 7273／MS 仍逾期／Chromium／Pixel／ISE／Acronis／WSO2／Adobe／F5／JFrog／PeopleSoft／X A 非 KEV 项／工具仓／LWiS 研究**：未见可抄录公开 IoC（或仅厂商 SK／新闻原文内；enrich-extra 对应条目亦写「未见公开 IoC」）。
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

本窗口 LWiS List 只读采集：扫描约 **20** 条、保留 **12** 条、覆盖约 **20h**（`logged_in=true`／`@seogoogle4`／`blocked=false`）；跨源 ID 重叠 0（相对 A／B／C）；含 HEIF Heist／IDA MCP／ADCS ESC_CES／Omarchy LPE／Electrovolt／Sep 25 链接汇总／AI 利用链讨论；meta：`/workspace/x-lwis-list-meta-2026-09-26.json`。

## 来源搜索 URL

- X Latest A（CVE-2026 精炼）：https://x.com/search?q=%22CVE-2026%22%20-filter%3Areplies%20-from%3ACVEnew%20-from%3AIhhsanMuhammad&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei）：https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%28%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%29%20-filter%3Areplies&src=typed_query&f=live
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
- CISA 09-25 一条 KEV 警报（87902）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-25 两条 KEV 警报（65660＋67279）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

