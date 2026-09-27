# X 安全情报晚报 · 2026-09-25

> 搜集窗口：圣地亚哥时间 **2026-09-24 20:00 至 2026-09-25 ~20:35**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周五）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-25.json`（collected_at **2026-09-25T20:15:09-03:00**）＋ `/workspace/tools-news-pulse-2026-09-25.json`＋ `/workspace/enrich-extra-2026-09-25.json`＋ `/workspace/enrich-2026-09-25/`。CISA KEV catalogVersion **2026.09.25**／**1726** 条／dateReleased **2026-09-25T18:58:16.5029Z**（相对昨日 **2026.09.24／1723**：**count Δ+3 NEW**；dateAdded=2026-09-25：**CVE-2026-65660**（Microsoft SharePoint）、**CVE-2026-67279**（MikroTik RouterOS）、**CVE-2026-87902**（WordPress Core））。CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog （87902）＋ https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog （65660＋67279）。
> **期限今日 09-25**：**Check Point CVE-2026-85102／CVE-2026-93616**、**Arista VeloCloud CVE-2026-93952**、**F5 BIG-IP APM CVE-2026-94127**、**JFrog Artifactory CVE-2026-42016／CVE-2026-42018**。**新起逾期（due 曾=09-24）**：**Zyxel CVE-2026-7273**。**仍逾期 MS**：**CVE-2026-81963**／**CVE-2026-85880**（due 曾=09-22）；**Chromium CVE-2026-87491**（due 曾=09-23）／**CVE-2026-85046**；**Pixel CVE-2026-58704**／**Cisco ISE CVE-2026-76460**／**Acronis CVE-2026-87886**。**即将 due 09-27**：**WSO2 CVE-2026-5430**／**Adobe CVE-2026-71362**。NEW 三条联邦 due **09-28**。
> X：`/workspace/x-posts-2026-09-25.json`（合并 **38** 条唯一：A10／B8／C13／LWiS8；跨源 ID 重叠 **1**＝`2103611079385366941`（A＋C，主源 A）；相对 prior seen_ids 重叠 **3**／**+35** 新 id；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.9h**。Search B 可见约 **48h**（含 Sep 23–25 工具帖，其中 3 条已见 prior）。Search C 约 **2h**。LWiS List 约 **22h**（**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【主条 · KEV +3 NEW】** CISA KEV catalogVersion **2026.09.25**／**1726** 条／dateReleased **2026-09-25T18:58:16.5029Z**（相对昨日 **2026.09.24／1723**：**Δ+3**）。两条 CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog · https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
  - **CVE-2026-65660**（Microsoft SharePoint）：代码注入（CWE-94）→ 授权攻击者可经网络执行代码；联邦 due **2026-09-28**；forensicTriage=Yes。厂商：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660 · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-65660 · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-65660
  - **CVE-2026-67279**（MikroTik RouterOS）：行为工作流执行不当（CWE-841）→ 未认证会话通道／exec 请求，可链式至 CVE-2026-86060；联邦 due **2026-09-28**。厂商九月公告（MikroTrick 族；页面未直接列出本 CVE 号）：https://mikrotik.com/supportsec/september-2026-vulnerability/ · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67279 · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-67279
  - **CVE-2026-87902**（WordPress Core）：远程文件包含（CWE-98）→ 未认证可选本地 `.php` 纳入页面模板解析／条件 RCE；联邦 due **2026-09-28**；forensicTriage=Yes。GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87902 · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87902 · nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-87902.yaml · X A：https://x.com/SecAlertsCo/status/2103618289293238381 · X B：https://x.com/wtf_yodhha/status/2103045866567483772

- **【期限今日 · Check Point／Arista／F5／JFrog】** **CVE-2026-85102／93616**（Check Point）、**93952**（Arista VeloCloud，含厂商 IoC）、**94127**（F5 BIG-IP APM）、**42016／42018**（JFrog）。防御：立即按厂商 SK／SA／K 文／advisories 补丁与临时缓解；BOD 26-04。
  Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
  SK85102：https://support.checkpoint.com/results/sk/sk1000117
  SK93616：https://support.checkpoint.com/results/sk/sk1000171/
  Arista SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
  F5 K000162605：https://my.f5.com/manage/s/article/K000162605
  JFrog advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories

- **【新起逾期 · Zyxel CVE-2026-7273】** GS1900 CGI 栈溢出；due 曾为 **09-24**，今日起 **newly_overdue**。防御：升至列明 **2.90(*.2)C0**；限制 LAN 管理暴露；BOD 26-04。
  厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273

- **【仍逾期 · MS／Chromium／Pixel／ISE／Acronis】** MS **CVE-2026-81963／85880**（due 曾=09-22）；Chromium **87491**（due 曾=09-23）／**85046**；Pixel **58704**／Cisco ISE **76460**／Acronis **87886**。防御：核验补丁落地；BOD 26-04。
  MSRC 81963：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963
  MSRC 85880：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880
  Chrome 87491：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html

- **【即将 due 09-27 · WSO2／Adobe】** **CVE-2026-5430**（WSO2）／**CVE-2026-71362**（Adobe Magento／Commerce APSB26-92）。防御：按 WSO2-2026-5328／APSB26-92 升版；BOD 26-04。（Adobe 页 box 出口曾 **403**，仍列已知厂商 URL。）
  WSO2：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
  APSB26-92：https://helpx.adobe.com/security/products/magento/apsb26-92.html

- **【工具／新闻】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** **无升版**；Risky **RBNEWS614→RBNEWS615（NEW）**（https://risky.biz/RBNEWS615/）；SRB184（https://risky.biz/SRB184a/）；BTN183；tl;dr 仍 **#347**（https://tldrsec.com/p/tldr-sec-347）。X B：Adaptix／BotC2／Stratus／EvilMist／HackMyAgent／Comment2Shell／Red-Team-Roadmap／nuclei 87902 模板等。

- **【X 交叉 · CVE／工具】** A（~0.9h）：sudo **96512** PoC 声称（**UNCONFIRMED**）、eBPF **93127**、Pixel **58704** 定向利用声称（**UNCONFIRMED**）、IBM Guardium **85542／85029**、WP **87902** KEV、PRTG **4637**、Outlook **100208**、pfSense **97730**、Roundcube **48842**（**UNCONFIRMED**，与 C 跨源）、PHP 8.2.34。B（~48h）：Adaptix C2 云通道、Comment2Shell、Stratus、EvilMist、HackMyAgent 等。

- **【X 交叉 · APT／Malware】** C（~2h）：多起地下泄露／勒索宣传（解放军相关文件、Le Matin、HOllOwRansOm、Miraflores、Dynamic Protection Group、印度政府门户、印度国防部、美执法／情报、MEPhI、SriLankan Airlines、Efadah 等）——**一律 UNCONFIRMED**。LWiS（~22h）：PamStealer、Mini Shai-Hulud、ScreenConnect 滥用观测、Gitea **60004**、IDA MCP、MS analytics 入侵声称（**UNCONFIRMED**）、Gmail 求职诈骗观察。

- **【合并统计】** X **38** 唯一（A10／B8／C13／LWiS8；cross **1**；prior **3**；**+35** NEW）；`logged_in=true`／`@seogoogle4`／`blocked=false`；seen_ids **1990→2025**；报告 `/home/box/workspace/security-watch/reports/2026-09-25-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【NEW KEV · due 09-28】Microsoft SharePoint CVE-2026-65660

CISA 于 **2026-09-25** 加入 KEV；联邦 due **2026-09-28**；forensicTriage=Yes。代码注入（CWE-94）→ 授权攻击者可经网络执行代码。防御：按 MSRC 更新指南尽快打补丁；盘点互联网／内网暴露的 SharePoint；BOD 26-04 法医分流。**本报不转载利用细节。**（MSRC 页为 SPA shell，以厂商更新指南为准。）

地址：
- CISA 09-25 警报（两条）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 厂商 MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-65660
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-65660
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-65660
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-65660
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 2. 【NEW KEV · due 09-28】MikroTik RouterOS CVE-2026-67279

CISA 于 **2026-09-25** 加入 KEV；联邦 due **2026-09-28**。行为工作流执行不当（CWE-841）→ 未认证客户端可打开会话通道并发送 exec 请求；可链式利用 CVE-2026-86060。厂商九月「MikroTrick」族公告页面列出姊妹 CVE（67276／67277／86060），**未直接以本 CVE 号列出**——以 KEV／NVD 与厂商升级指引为准。防御：尽快升 RouterOS；检查 Flagged 状态与未知脚本／用户；限制管理面；BOD 26-04。**不转载利用步骤。**

地址：
- CISA 09-25 警报（两条）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67279
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-67279
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-67279
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC（厂商建议检查 Flagged 状态与未知脚本／用户）。

### 3. 【NEW KEV · due 09-28】WordPress Core CVE-2026-87902

CISA 于 **2026-09-25** 加入 KEV；联邦 due **2026-09-28**；forensicTriage=Yes。远程文件包含（CWE-98）→ 未认证攻击者可令页面模板解析纳入主题目录外可读本地 `.php`，可致条件 RCE。X A 称补丁后数小时出现探测——**探测／在野流量声称 UNCONFIRMED**。防御：立即按 GHSA 升至列明补丁版本；盘点公开 WordPress；用 nuclei-templates 做**授权**暴露面核查；BOD 26-04。**不转载利用步骤。**

地址：
- CISA 09-25 警报（一条）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87902
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87902
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-87902
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-87902.yaml
- X 原帖（A）：https://x.com/SecAlertsCo/status/2103618289293238381
- X 原帖（B，prior_seen）：https://x.com/wtf_yodhha/status/2103045866567483772
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 4. 【期限今日 · 在野】Check Point CVE-2026-85102／CVE-2026-93616

CISA 于 **2026-09-22** 加入 KEV；联邦 due **今日 2026-09-25**。85102：VPN 不当证书校验 → 未认证 RCE。93616：管理面路径穿越 → 未认证脚本上传／执行。修复示例见 SK：85102 — **R82.10 Jumbo Take 44+／R82 Take 126+／R81.20 Take 166+**；93616 — **R82.20 Hotfix／R82.10 Take 45+／R82 Take 127+／R81.20 Take 170+** 等。防御：立即按 SK 打 Jumbo／Hotfix；限制管理／VPN 面；证书 subject 狩猎；BOD 26-04。**不转载利用步骤。**

地址：
- 厂商 SK85102：https://support.checkpoint.com/results/sk/sk1000117
- 厂商 SK93616：https://support.checkpoint.com/results/sk/sk1000171/
- Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
- BleepingComputer：https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/
- NVD 85102：https://nvd.nist.gov/vuln/detail/CVE-2026-85102
- NVD 93616：https://nvd.nist.gov/vuln/detail/CVE-2026-93616
- KEV 85102：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85102
- KEV 93616：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-93616

IoC（厂商观测 cert_subject，原样抄录，非穷尽）：
- `CN=vpn,OU=users,O=global`
- `CN=vpn-user,OU=users,O=global`
- `CN=vpnuser,OU=users,O=global`

### 5. 【期限今日 · 在野】Arista VeloCloud CVE-2026-93952

KEV due **今日 2026-09-25**。on-prem VCO 不当输入校验；成功利用可影响编排器机密性／完整性／可用性。修复示例：**VCO 5.2.3.16+／6.4.2.8+**。防御：升 on-prem VCO；将 VCO Web 限制到可信管理网；按 SA-0183 狩猎下列 IoC；BOD 26-04。

地址：
- 厂商 SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-93952
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-93952
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC（厂商 SA-0183／enrich-extra 原样抄录，非穷尽）：
- 文件：`/usr/local/sbin/.vcnode.js`
- 文件：`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）
- 文件：`/etc/systemd/system/vc-sysmon.service`
- HTTP 头：`x-vc-opt`
- IP：`142.93.149.77`
- IP：`104.248.126.159`

### 6. 【期限今日 · 在野】F5 BIG-IP APM CVE-2026-94127

KEV due **今日 2026-09-25**。虚拟服务器配置访问策略＋OAuth profile 时堆溢出 → 未认证数据面 RCE。防御：按 K000162605 盘点 APM＋OAuth VS；先临时 iRule 再 ENG hotfix；BOD 26-04。（myF5 可能需登录，仍列已知厂商 URL。）

地址：
- 厂商 K000162605：https://my.f5.com/manage/s/article/K000162605
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94127
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-94127

IoC：未见公开 IoC。

### 7. 【期限今日 · near】JFrog Artifactory CVE-2026-42016／CVE-2026-42018

公开备援列 due **今日 2026-09-25**。42016：token scope 校验特权提升（修复示例 **≥7.133.11**）。42018：匿名 token 泄露面（匿名访问禁用时仍可能向未认证调用者返回内部匿名用户 token）。防御：按 JFrog Security Advisories／Self-Managed Releases 升版；限制 Artifactory 管理面。

地址：
- NVD 42016：https://nvd.nist.gov/vuln/detail/CVE-2026-42016
- NVD 42018：https://nvd.nist.gov/vuln/detail/CVE-2026-42018
- KEV 42016：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-42016
- KEV 42018：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-42018
- 厂商 advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- 发行说明：https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases

IoC：未见公开 IoC。

### 8. 【新起逾期 · 在野】Zyxel GS1900 CVE-2026-7273

KEV due 曾为 **2026-09-24**，今日起 **newly_overdue**。LAN 向 CGI 栈溢出 → 未认证 OS 命令面。防御：升至列明 **2.90(*.2)C0** 固件；限制 LAN 管理暴露；BOD 26-04。

地址：
- 厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-7273
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 9. 【仍逾期 · 在野】Microsoft CVE-2026-81963／CVE-2026-85880

KEV due 曾为 **2026-09-22**，继续 overdue。81963：Windows Update Stack 链接跟随 → 本地提权至 SYSTEM。85880：Windows 堆溢出。防御：核验 9 月 Windows 安全更新已落地；盘点未补丁主机；BOD 26-04。

地址：
- MSRC 81963：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963
- MSRC 85880：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880
- NVD 81963：https://nvd.nist.gov/vuln/detail/CVE-2026-81963
- NVD 85880：https://nvd.nist.gov/vuln/detail/CVE-2026-85880
- KEV 81963：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-81963
- KEV 85880：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85880

IoC：未见公开 IoC。

### 10. 【仍逾期 · 在野】Chromium 87491／85046／Pixel 58704／Cisco ISE 76460／Acronis 87886

仍逾期重点：Chromium **CVE-2026-87491**（due 09-23；Chrome **153.0.8010.36+**）／**CVE-2026-85046**（due 09-18）；Pixel **CVE-2026-58704**／Cisco ISE **CVE-2026-76460**／Acronis **CVE-2026-87886**（due 09-19）。X A 今日续称 Pixel 58704「定向利用」——**UNCONFIRMED**。防御：按厂商公告补丁；BOD 26-04。

地址：
- Chrome 87491：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- NVD 87491：https://nvd.nist.gov/vuln/detail/CVE-2026-87491
- Chrome 85046：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- NVD 85046：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
- Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- NVD 58704：https://nvd.nist.gov/vuln/detail/CVE-2026-58704
- X（Pixel 声称）：https://x.com/Python_s_/status/2103622304584327491
- Cisco ISE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- NVD 76460：https://nvd.nist.gov/vuln/detail/CVE-2026-76460
- Acronis：https://security-advisory.acronis.com/advisories/SEC-10986
- NVD 87886：https://nvd.nist.gov/vuln/detail/CVE-2026-87886

IoC：未见公开 IoC（或仅厂商 SK／通报内）。

### 11. 【即将 due 09-27 · 在野】WSO2 CVE-2026-5430／Adobe CVE-2026-71362

昨日 NEW KEV；联邦 due **2026-09-27**。5430：路径穿越 → 未受限上传／可致 RCE（厂商顾问 WSO2-2026-5328 叙事侧重 JWT 认证绕过——**两说并存，以厂商 update levels 为准**）。71362：不正确授权（CWE-863）；公告 **APSB26-92**（box 出口曾 **403**，仍列已知 URL）。防御：按顾问／APSB 升版；BOD 26-04。

地址：
- 厂商 WSO2-2026-5328：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
- NVD 5430：https://nvd.nist.gov/vuln/detail/CVE-2026-5430
- KEV 5430：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-5430
- 厂商 APSB26-92：https://helpx.adobe.com/security/products/magento/apsb26-92.html
- NVD 71362：https://nvd.nist.gov/vuln/detail/CVE-2026-71362
- KEV 71362：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-71362
- 社区 PR：https://github.com/wso2/carbon-apimgt/pull/13752 · https://github.com/wso2/product-apim/pull/14167

IoC：未见公开 IoC。

### 12. 【X A · 非 KEV · 声称】sudo CVE-2026-96512／eBPF CVE-2026-93127

- **sudo CVE-2026-96512**：称 NOTBEFORE／NOTAFTER 时间约束存在本地提权／授权绕过（CVSS 声称 7.8）——**PoC／利用声称 UNCONFIRMED**；防御评估受影响 sudo 版本并升级。**不转载 PoC 步骤。** X：https://x.com/ridvanyagli/status/2103623788512661713 · 仓库：https://github.com/abraxas/CVE-2026-96512
- **eBPF CVE-2026-93127**：LinuxSecurity 讨论 verifier 错误与越界路径；强调缺少公开 exploit ≠ 已完成可达性评估——未见主动利用确认。X：https://x.com/lnxsec/status/2103622606133842101 · 可见链（未展开）：https://t.co/Qzy8Ay7O4X

IoC：未见公开 IoC。

### 13. 【X A · 非 KEV】IBM Guardium／Outlook／pfSense／PRTG／PHP

- **IBM Guardium Data Protection 12.2**：CVE-2026-85542（Central Manager 命令注入，CVSS 声称 8.8）／CVE-2026-85029（路径遍历，CVSS 声称 7.5）；帖文给出修复包 **SqlGuard_12.0p233**。防御：按厂商包升级。X：https://x.com/thecircuitry_/status/2103622285445718292 · 可见域：https://thecircuitry.to
- **Microsoft Outlook CVE-2026-100208**：整数溢出、CVSS 声称 7.5，高复杂度、需用户交互。防御：按微软指引评估修补。X：https://x.com/thecircuitry_/status/2103616750138912823 · 可见域：https://thecircuitry.to
- **pfSense CVE-2026-97730**：dashboard widgets 高严重度 LFI（CVSS 声称 8.5）；建议 Plus **26.07+** 或 CE **2.9.0+**。X：https://x.com/ADKCyber/status/2103616477387784248 · NVD（若已收录）：https://nvd.nist.gov/vuln/detail/CVE-2026-97730 · 可见 t.co：https://t.co/9vs9eEIA9Q · https://t.co/9NwSyzScJm
- **Paessler PRTG CVE-2026-4637**：反射型 XSS／明文域凭据披露，称已在 **v26.2.120.1449** 修复；全球暴露实例声称约 73.8k。防御：核查暴露面并升级。X：https://x.com/zoomeyebot/status/2103616810583253173 · 可见链（截断）：https://zoomeye.ai/searchResult?q...
- **PHP 8.2.34**：含 CVE-2026-91768／CVE-2025-1218／CVE-2026-91769 等修复。防御：升级并查看变更日志。X：https://x.com/php_net/status/2103611762473910771 · 可见域：https://php-net.pro

IoC：未见公开 IoC。

### 14. 【X A／C 跨源 · 声称】Roundcube CVE-2026-48842

跨源 ID **2103611079385366941**（A＋C，主源 A）。称未认证 SQL 注入，影响旧版 1.6.x／1.7.x，并称加拿大网络安全机构承认在野利用报告——**主动利用 UNCONFIRMED**；以加拿大官方通告为准。防御：核查版本／补丁与官方通告。**不转载利用步骤。**

地址：
- X 原帖：https://x.com/Python_s_/status/2103611079385366941
- 可见 t.co（C 采集，标签 cyber.gc.ca AV26-503 Update 1，未展开）：https://t.co/X4HkysJA7h

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 核心版本脉冲（公开备援）

Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 相对昨日 **无升版**。Risky Business **RBNEWS614→RBNEWS615（NEW）**——标题摘要：Major vulnerability found in ancient TACACS+ networking protocol；SRB184／BTN183 不变；tl;dr 仍 **#347**。

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

覆盖约 **48h**（含 Sep 23–24；其中 3 条 prior_seen）。仅列防御认知／仓库定位；**不转操作步骤**；能力描述 **UNCONFIRMED**。

- **Adaptix C2 云死信通道**（Azure Blob／OneDrive）：https://github.com/stillbigjosh/adaptix-graph-c2 · 文章：https://stillbigjosh.com/writeup.html?file=writeups/adaptix-graph-c2.md · X：https://x.com/stillbigjosh/status/2103455702945796331
- **Red-Team-Roadmap**（Module 14；训练向）：https://github.com/Dev-Chukwuma/Red-Team-Roadmap · X：https://x.com/httpschuks/status/2103445975100527016
- **Comment2Shell**（含 Nuclei 模板／Docker lab——授权验证暴露面）：https://github.com/DeathShotXD/Comment2Shell · X：https://x.com/XssPayloads/status/2103440816941523278
- **Stratus Red Team**（云对手模拟／检测验证）：https://github.com/DataDog/stratus-red-team · X：https://x.com/rilopezp/status/2103297811676807493
- **BotC2-RAT**（逆向／C2 仿真材料；prior_seen）：https://github.com/ShadowOpCode/BotC2-RAT/blob/main/BotC2_RAT.pdf · X：https://x.com/blackstormsecbr/status/2103220590740140368
- **nuclei-templates WP CVE-2026-87902**（prior_seen）：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-87902.yaml · X：https://x.com/wtf_yodhha/status/2103045866567483772 · Telegram（可见）：https://t.me/brutsecurity/3034
- **EvilMist**（Cloud／Entra ID 红队工具包；仅授权）：https://github.com/Logisek/EvilMist · X：https://x.com/EsGeeks/status/2102910572857614577
- **HackMyAgent**（AI agents／MCP 扫描；prior_seen）：https://github.com/opena2a-org/hackmyagent · X：https://x.com/EsGeeks/status/2102777566515847519

IoC：工具帖未见公开 IoC。

### LWiS 相关研究／工具向交叉

覆盖约 **22h**（**交叉校验，不假装 24h Latest**）。

- **Hex-Rays IDA MCP Server**（官方；隔离分析环境评估 agent 权限）：X：https://x.com/mrexodia/status/2103518007255237079
- **Gitea CVE-2026-60004**（diffpatch 端点 RCE 描述）：文章：https://dbu.gs/news/rce-in-gitea-cve-2026-60004-20260925 · X：https://x.com/ptdbugs/status/2103422337441730671 · 可见 t.co：https://t.co/E5UanVZJku
- **ProjectDiscovery CoT Analysis of Offensive Agents**：https://projectdiscovery.io/research/chain · X：https://x.com/KoyalwarTarun/status/2103588109556625468
- **ScreenConnect 滥用观测**（Huntress 比例转述）：X：https://x.com/Securityinbits/status/2103111424369446935

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. 【LWiS】PamStealer macOS malware

@Dinosn 转述 The Hacker News：PamStealer macOS 恶意软件，标题提及 live C2 payload 解密与多层持久化。防御：检查 macOS 持久化位置、异常出站连接及 EDR 告警。

地址：
- X：https://x.com/Dinosn/status/2103597548971913375
- 可见 t.co（UI 目标 thehackernews.com，完整路径未显示）：https://t.co/Y04nRX8PVD

IoC：未见公开 IoC（详见原文）。

### 2. 【LWiS】Mini Shai-Hulud（GitHub Actions）

@Dinosn 转述 The Hacker News：受影响 GitHub Actions 恢复运行并继续执行 Mini Shai-Hulud。防御：审计 workflow、第三方 action 与 secrets；隔离并重建可疑 runner。

地址：
- X：https://x.com/Dinosn/status/2103597459205427648
- 可见 t.co（UI 目标 thehackernews.com，完整路径未显示）：https://t.co/SFxksMPPNW

IoC：未见公开 IoC（详见原文）。

### 3. 【LWiS】ScreenConnect 滥用观测

@Securityinbits：ScreenConnect 约占 Huntress 观察到的被滥用远程访问工具 **74.5%**；提供 Defender／Elastic hunting notes。防御：审查 RMM 使用基线、签名与进程／网络遥测。

地址：
- X：https://x.com/Securityinbits/status/2103111424369446935

IoC：未见公开 IoC。

### 4. 【LWiS · UNCONFIRMED】Microsoft 内部 analytics 入侵声称

@IntCyberDigest 称 16 岁攻击者经伪造、未签名 login token 进入 Microsoft 内部 analytics 并以管理员身份运行 SQL——**UNCONFIRMED**；勿将该帖当作已证实事件。防御：核查 token 签发／签名验证、服务间信任与最小权限。

地址：
- X：https://x.com/IntCyberDigest/status/2103590183400788402

IoC：未见公开 IoC。

### 5. 【LWiS】Gmail 求职诈骗观察

@Dinosn 观察近期 Gmail 纯文本诈骗绕过过滤器：利用 LinkedIn 资料开启虚构职位对话，最终导向收费服务——**UNCONFIRMED（作者观察）**。防御：加强求职／外部邮件反钓鱼规则与用户核验。

地址：
- X：https://x.com/Dinosn/status/2103599551596867956

IoC：未见公开 IoC。

### 6. 【X C · 未验证】地下勒索／泄露声称（合辑）

以下均为社交列表报道，**一律 UNCONFIRMED／未验证**；不复述利用步骤：

- 解放军相关 AI／量子／反高超音速「文件泄露」声称：https://x.com/intels_daily/status/2103622375740694554
- holl0w33n／摩洛哥 Le Matin 数据库（约 6 万用户）声称：https://x.com/CyberPulse56/status/2103617928096870544
- HollowCrimeCorp／「HOllOwRansOm」勒索宣传：https://x.com/CyberPulse56/status/2103613299774628010
- Frouzen／Cyberagentsss／秘鲁 Miraflores 市政府库声称：https://x.com/CyberPulse56/status/2103612699825570226 · 可见 t.co：https://t.co/XaSlU1FPhW
- ripzx／纽约 Dynamic Protection Group Firebase 售卖声称：https://x.com/intels_daily/status/2103607256851915259
- HSRgroup／印度政府门户 SQLi 数据声称（含 copyright.gov.in）：https://x.com/CyberPulse56/status/2103605689662972392 · 可见 t.co：https://t.co/4zIGfBFvi5
- 「mosad」／印度国防部防务采购文件声称：https://x.com/CyberPulse56/status/2103605308006555765
- MrDarkRoot／美执法情报「千万＋ FBI 案件」声称：https://x.com/CyberPulse56/status/2103598895993630845
- Blacknet00／俄罗斯 MEPhI（OpenVPN／xl2tpd 等标签）声称：https://x.com/intels_daily/status/2103598122429513795
- BLACKNET-00／SriLankan Airlines（PRTG／Log4j 标签）声称：https://x.com/intels_daily/status/2103598076443197652
- 「Roxanne」／沙特 Efadah HR 勒索声称：https://x.com/intels_daily/status/2103592159077122123 · 可见 t.co：https://t.co/uIM8Kf764y

IoC：帖文可见主机名／标签声称（非核验）— `MIRAFLORES.GOB.PE`／`copyright.gov.in`／`efadah.com[.]sa`；其余多数 **未见公开 IoC**。

### 7. 【X C】Malware Anatomy（教育向）

@Anastasis_King 三部分「Malware Anatomy」：PE 结构、运行时行为、持久化／网络／入侵指标——防御／教育性内容；未展示具体恶意操作步骤。

地址：
- X：https://x.com/Anastasis_King/status/2103586144663343312

IoC：未见公开 IoC。

### 8. ICS

本日公开备援 **无单独突出的 2026-09-25 新 ICS advisory 主条**（KEV 主更新为 SharePoint／MikroTik／WordPress）。网关／编排／APM／VPN／Artifactory 类以今日 due 桶为主。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Arista VeloCloud CVE-2026-93952（今日 due）**：`/usr/local/sbin/.vcnode.js`；`/usr/local/sbin/vc-sysmond`（md5 `dc78e206eaeadec59fc5801fe4556bd0`）；`/etc/systemd/system/vc-sysmon.service`；HTTP 头 `x-vc-opt`；IP `142.93.149.77`／`104.248.126.159`。
- **Check Point 85102／93616（今日 due）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`；另见 sk1000171 厂商狩猎节。
- **地下声称可见主机名（UNCONFIRMED）**：`MIRAFLORES.GOB.PE`／`copyright.gov.in`／`efadah.com[.]sa`。
- **NEW KEV SharePoint 65660／MikroTik 67279／WP 87902／Zyxel 7273 新逾期／MS 仍逾期／Chromium／Pixel／ISE／Acronis／WSO2／Adobe／F5／JFrog／X A 非 KEV 项／工具仓／LWiS malware 报道**：未见可抄录公开 IoC（或仅厂商 SK／新闻原文内）。
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

本窗口 LWiS List 只读采集：保留 **8** 条、覆盖约 **22h**（`logged_in=true`／`@seogoogle4`／`blocked=false`）；跨源 ID 重叠 0（相对 A／B／C）；含 PamStealer／Mini Shai-Hulud／ScreenConnect／Gitea 60004／IDA MCP／MS 声称 UNCONFIRMED／Gmail 诈骗观察；meta：`/workspace/x-lwis-list-meta-2026-09-25.json`。

## 来源搜索 URL

- X Latest A（CVE-2026 精炼）：https://x.com/search?q=%22CVE-2026%22%20-filter%3Areplies%20-from%3ACVEnew%20-from%3AIhhsanMuhammad&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%28%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%29%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS615：https://risky.biz/RBNEWS615/
- Risky SRB184a：https://risky.biz/SRB184a/
- tl;dr sec：https://tldrsec.com/
- tl;dr #347：https://tldrsec.com/p/tldr-sec-347
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 今日一条 KEV 警报（87902）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 今日两条 KEV 警报（65660＋67279）：https://www.cisa.gov/news-events/alerts/2026/09/25/cisa-adds-two-known-exploited-vulnerabilities-catalog
