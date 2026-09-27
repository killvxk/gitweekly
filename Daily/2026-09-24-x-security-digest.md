# X 安全情报晚报 · 2026-09-24

> 搜集窗口：圣地亚哥时间 **2026-09-23 20:00 至 2026-09-24 ~20:33**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周四）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-24.json`（collected_at **2026-09-24T20:15:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-24.json`＋ `/workspace/enrich-extra-2026-09-24.json`＋ `/workspace/enrich-2026-09-24/`。CISA KEV catalogVersion **2026.09.24**／**1723** 条／dateReleased **2026-09-24T19:00:55.0481Z**（相对昨日 **2026.09.23／1721**：**count Δ+2 NEW**；dateAdded=2026-09-24：**CVE-2026-5430**（WSO2）、**CVE-2026-71362**（Adobe Magento／Commerce APSB26-92））。CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/24/cisa-adds-two-known-exploited-vulnerabilities-catalog
> **期限今日 09-24**：**Zyxel CVE-2026-7273**（GS1900 CGI 栈溢出；补丁 **2.90(*.2)C0**）。**新起逾期（due 曾=09-23）**：Google Chromium V8 **CVE-2026-87491**。**仍逾期 MS**：**CVE-2026-81963**／**CVE-2026-85880**（due 曾=09-22）。**明日 due 09-25**：Check Point **CVE-2026-85102／CVE-2026-93616**、Arista VeloCloud **CVE-2026-93952**、F5 BIG-IP APM **CVE-2026-94127**、JFrog Artifactory **CVE-2026-42016／CVE-2026-42018**。仍逾期重点：**Chromium CVE-2026-85046**／**Pixel CVE-2026-58704**／**Cisco ISE CVE-2026-76460**／**Acronis CVE-2026-87886** 等。NEW 两条联邦 due **09-27**。
> X：`/workspace/x-posts-2026-09-24.json`（合并 **42** 条唯一：A8／B11／C15／LWiS8；跨源 ID 重叠 **0**；相对 prior seen_ids 重叠 **11**／**+31** 新 id；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **5.0h**。Search B 可见约 **72h**（含 Sep 21–24 工具帖，其中多条已见 prior）。Search C 约 **24h**。LWiS List 约 **84h**（**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【主条 · KEV +2 NEW】** CISA KEV catalogVersion **2026.09.24**／**1723** 条／dateReleased **2026-09-24T19:00:55.0481Z**（相对昨日 **2026.09.23／1721**：**Δ+2**）。CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/24/cisa-adds-two-known-exploited-vulnerabilities-catalog
  - **CVE-2026-5430**（WSO2 Multiple Products）：KEV shortDescription 为路径穿越 → 未受限上传／RCE；厂商顾问 **WSO2-2026-5328** 叙事侧重 JWT 认证绕过／账户接管——**两说并存，以厂商 update levels 为补丁源**；联邦 due **2026-09-27**；forensicTriage=Yes。厂商：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/ · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-5430 · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-5430 · 社区 PR：https://github.com/wso2/carbon-apimgt/pull/13752 · https://github.com/wso2/product-apim/pull/14167
  - **CVE-2026-71362**（Adobe Commerce／Magento）：不正确授权（CWE-863）→ 无用户交互即可提升访问；公告 **APSB26-92**；联邦 due **2026-09-27**。厂商：https://helpx.adobe.com/security/products/magento/apsb26-92.html · NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-71362 · KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-71362 · X A：https://x.com/XavierRiveraX/status/2103259511850987561 · 文章卡：https://thecircuitry.to/article/cisa-kev-entry-for-adobe-commerce-cve-2026-71362-mufycg9y

- **【期限今日 · Zyxel CVE-2026-7273】** GS1900 CGI 栈溢出；LAN 未认证 OS 命令面；联邦 due **今日 09-24**。防御：升至列明 **2.90(*.2)C0**；限制 LAN 管理暴露；BOD 26-04。
  厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273

- **【新起逾期 · Chromium CVE-2026-87491】** Google Chromium V8 越界写；due 曾为 **09-23**，今日起 **newly_overdue**。防御：立即升至 Chrome **153.0.8010.36+**（及 Edge-Chromium 等）；BOD 26-04 triage。
  Chrome：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87491
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87491

- **【仍逾期 · MS CVE-2026-81963／85880】** due 曾为 **09-22**，继续 overdue。防御：核验 9 月 Windows 更新；BOD 26-04。另仍逾期重点：Chromium **85046**／Pixel **58704**／Cisco ISE **76460**／Acronis **87886** 等。
  MSRC 81963：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963
  MSRC 85880：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880

- **【明日 due 09-25 · Check Point／Arista／F5／JFrog】** **CVE-2026-85102／93616**（Check Point）、**93952**（Arista VeloCloud）、**94127**（F5 BIG-IP APM）、**42016／42018**（JFrog）。X A 交叉：Check Point 在野声称（**UNCONFIRMED**）、Picus／F5 94127、Adobe KEV 帖。
  Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
  SK85102：https://support.checkpoint.com/results/sk/sk1000117
  SK93616：https://support.checkpoint.com/results/sk/sk1000171/
  Arista SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
  F5 K000162605：https://my.f5.com/manage/s/article/K000162605
  JFrog advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
  X（Check Point 声称）：https://x.com/sh3ll_c0d3/status/2103258183925907630
  X（Picus F5）：https://x.com/PicusSecurity/status/2103194029131280859
  X（LWiS BleepingComputer，prior）：https://x.com/BleepinComputer/status/2102849013829541920

- **【工具／新闻】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** **无升版**；Risky **SRB183→SRB184**（https://risky.biz/SRB184a/）；RBNEWS 仍 **614**（https://risky.biz/RBNEWS614/）；tl;dr **#346→#347**（https://tldrsec.com/p/tldr-sec-347）。X B：BotC2-RAT／KaliGPT／ARES／OneDrive-UDC2／nuclei WP **87902**／Strapi 27886 等（多条 prior-window）。

- **【X 交叉】** A：Adobe KEV 71362、Check Point 93616 声称、Roundcube **48842** 在野声称（**UNCONFIRMED**）、SharePoint **69282**（加国 AL26-023）、Rejetto HFS **97359**、F5 **94127**。C：Anthropic 9 月威胁报告、Iran playbook、多起勒索／库泄露声称（**一律 UNCONFIRMED**）。LWiS：PG **15742** 日志狩猎提示、Check Point 交叉、Warden stealer、SnafflePy、SpecterOps AI 攻防研究、netexec-MCP 等——**交叉校验，不替代 Latest**。

## CVE / POC / 漏洞

### 1. 【NEW KEV · due 09-27】WSO2 CVE-2026-5430

CISA 于 **2026-09-24** 加入 KEV；联邦 due **2026-09-27**；forensicTriage=Yes。KEV shortDescription：API Control Plane／API Manager／Traffic Manager／Universal Gateway **路径穿越** → 未受限文件上传／可导致 RCE。厂商顾问 **WSO2-2026-5328** 公开概述侧重 **JWT 认证绕过／账户接管**——**叙事不完全一致；补丁以厂商 update levels／社区 PR 为准**。修复示例：API Manager **4.6.0 UL21+／4.5.0 UL57+** 等（见顾问表）。防御：按 WSO2-2026-5328 升 Update Levels；盘点互联网暴露的 WSO2 网关／APIM；BOD 26-04。**本报不转载利用细节。**

地址：
- CISA 09-24 警报：https://www.cisa.gov/news-events/alerts/2026/09/24/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 厂商 WSO2-2026-5328：https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-5328/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-5430
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-5430
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-5430
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- 社区 PR：https://github.com/wso2/carbon-apimgt/pull/13752
- 社区 PR：https://github.com/wso2/product-apim/pull/14167

IoC：未见公开 IoC。

### 2. 【NEW KEV · due 09-27】Adobe Commerce／Magento CVE-2026-71362（APSB26-92）

CISA 于 **2026-09-24** 加入 KEV；联邦 due **2026-09-27**；forensicTriage=Yes。不正确授权（CWE-863）→ 无用户交互即可提升对敏感资源的访问。修复：按 **APSB26-92** 升 Adobe Commerce／Magento Open Source **2.4.x-2026-aug**（及 B2B 对应线）。X A／The Circuitry 今日转述 KEV 入库。防御：立即套用 APSB26-92；盘点互联网 Magento／Commerce；BOD 26-04。**不转载利用步骤。**

地址：
- CISA 09-24 警报：https://www.cisa.gov/news-events/alerts/2026/09/24/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 厂商 APSB26-92：https://helpx.adobe.com/security/products/magento/apsb26-92.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-71362
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-71362
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-71362
- 文章：https://thecircuitry.to/article/cisa-kev-entry-for-adobe-commerce-cve-2026-71362-mufycg9y
- X 原帖：https://x.com/XavierRiveraX/status/2103259511850987561

IoC：未见公开 IoC。

### 3. 【期限今日 · 在野】Zyxel GS1900 CVE-2026-7273

KEV due **2026-09-24（今日）**。LAN 向 CGI 栈溢出 → 未认证 OS 命令面。防御：升至列明 **2.90(*.2)C0** 固件（示例：GS1900-8 2.90(AAHH.2)C0 等）；限制 LAN 管理暴露；BOD 26-04。

地址：
- 厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-7273
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 4. 【新起逾期 · 在野】Chromium V8 CVE-2026-87491

KEV due 曾为 **2026-09-23**，今日起 **newly_overdue**。V8 越界写；Google 已知在野利用。修复示例：Chrome **153.0.8010.36+**。仍逾期姊妹 **CVE-2026-85046**（due 09-18）。防御：立即全量升浏览器（含托管 Edge-Chromium）；BOD 26-04。

地址：
- Chrome：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87491
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87491
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 5. 【仍逾期 · 在野】Microsoft CVE-2026-81963／CVE-2026-85880

KEV due 曾为 **2026-09-22**，继续 overdue。81963：Windows Update Stack 链接跟随 → 本地提权至 SYSTEM。85880：Windows 堆溢出。防御：核验 9 月 Windows 安全更新已落地；盘点未补丁主机；BOD 26-04。

地址：
- MSRC 81963：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963
- MSRC 85880：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880
- NVD 81963：https://nvd.nist.gov/vuln/detail/CVE-2026-81963
- NVD 85880：https://nvd.nist.gov/vuln/detail/CVE-2026-85880
- KEV 81963：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-81963
- KEV 85880：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85880

IoC：未见公开 IoC。

### 6. 【明日 due 09-25 · 在野】Check Point CVE-2026-85102／CVE-2026-93616

CISA 于 **2026-09-22** 加入 KEV；联邦 due **2026-09-25**。85102：VPN 不当证书校验 → 未认证 RCE。93616：管理面路径穿越 → 未认证脚本执行。X A 今日续称 93616「在野」（**UNCONFIRMED**；不转载步骤）。LWiS／BleepingComputer 交叉（prior_seen）。修复示例见 SK：85102 — **R82.10 Jumbo Take 44+／R82 Take 126+／R81.20 Take 166+**；93616 — **R82.20 Hotfix／R82.10 Take 45+／R82 Take 127+／R81.20 Take 170+** 等。防御：立即按 SK 打 Jumbo／Hotfix；限制管理／VPN 面；证书 subject 狩猎；BOD 26-04。

地址：
- 厂商 SK85102：https://support.checkpoint.com/results/sk/sk1000117
- 厂商 SK93616：https://support.checkpoint.com/results/sk/sk1000171/
- Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
- BleepingComputer：https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/
- NVD 85102：https://nvd.nist.gov/vuln/detail/CVE-2026-85102
- NVD 93616：https://nvd.nist.gov/vuln/detail/CVE-2026-93616
- X 原帖：https://x.com/sh3ll_c0d3/status/2103258183925907630
- X（LWiS／prior）：https://x.com/BleepinComputer/status/2102849013829541920

IoC（厂商观测 cert_subject，原样抄录，非穷尽）：
- `CN=vpn,OU=users,O=global`
- `CN=vpn-user,OU=users,O=global`
- `CN=vpnuser,OU=users,O=global`

### 7. 【明日 due 09-25 · 在野】F5 BIG-IP APM CVE-2026-94127

KEV due **2026-09-25**。虚拟服务器配置访问策略＋OAuth profile 时堆溢出 → 未认证数据面 RCE。X A：Picus Labs 称已纳入 Threat Library（分析链——**不转载利用细节**）。防御：按 K000162605 盘点 APM＋OAuth VS；先临时 iRule 再 ENG hotfix；BOD 26-04。

地址：
- 厂商 K000162605：https://my.f5.com/manage/s/article/K000162605
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94127
- X 原帖：https://x.com/PicusSecurity/status/2103194029131280859
- Picus 卡链：https://hubs.li/Q04ygfmW0

IoC：未见公开 IoC。

### 8. 【明日 due 09-25 · 在野】Arista VeloCloud CVE-2026-93952

KEV due **2026-09-25**。on-prem VCO 不当输入校验。修复示例：**VCO 5.2.3.16+／6.4.2.8+**。防御：升 on-prem VCO；将 VCO Web 限制到可信管理网；BOD 26-04。

地址：
- 厂商 SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-93952

IoC：未见公开 IoC。

### 9. 【明日 due 09-25 · near】JFrog Artifactory CVE-2026-42016／CVE-2026-42018

公开备援列 due **2026-09-25**。42016：token scope 校验特权提升（修复示例 **≥7.133.11**）。42018：匿名 token 泄露面。防御：按 JFrog Security Advisories／Self-Managed Releases 升版；限制 Artifactory 管理面。

地址：
- NVD 42016：https://nvd.nist.gov/vuln/detail/CVE-2026-42016
- NVD 42018：https://nvd.nist.gov/vuln/detail/CVE-2026-42018
- 厂商 advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- 发行说明：https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases

IoC：未见公开 IoC。

### 10. 【仍逾期 · 在野】Chromium 85046／Pixel 58704／Cisco ISE 76460／Acronis 87886

仍逾期重点（非今日 NEW）：Chromium **CVE-2026-85046**（due 09-18）；Pixel **CVE-2026-58704**／Cisco ISE **CVE-2026-76460**／Acronis **CVE-2026-87886**（due 09-19）。防御：按厂商公告补丁；BOD 26-04。

地址：
- Chrome 85046：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- NVD 85046：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
- Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- NVD 58704：https://nvd.nist.gov/vuln/detail/CVE-2026-58704
- Cisco ISE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- NVD 76460：https://nvd.nist.gov/vuln/detail/CVE-2026-76460
- Acronis：https://security-advisory.acronis.com/advisories/SEC-10986
- NVD 87886：https://nvd.nist.gov/vuln/detail/CVE-2026-87886

IoC：未见公开 IoC（或仅厂商 SK／通报内）。

### 11. 【X A · 非 KEV】SharePoint CVE-2026-69282（加国 AL26-023）

@windowsforum／@cybercentre_ca：称 SharePoint 新 RCE 可将低权限列表访问升级为服务器级风险；建议安装 **KB5002908** 并最小权限。**今晚非 NEW KEV**。防御：按微软／加国警报尽快打补丁；限制 SharePoint 暴露面。**不转载利用步骤。**

地址：
- X 原帖：https://x.com/windowsforum/status/2103250909178335465
- X 原帖：https://x.com/cybercentre_ca/status/2103190307584004583
- NVD（若已收录）：https://nvd.nist.gov/vuln/detail/CVE-2026-69282

IoC：未见公开 IoC。

### 12. 【X A · 非 KEV · 声称】Roundcube CVE-2026-48842／Rejetto CVE-2026-97359／TeamCity CVE-2026-63077

- **Roundcube CVE-2026-48842**：ZoomEye／日文摘要称 pre-auth SQLi「在野」及政府警告——**一律 UNCONFIRMED**；不转载利用。X：https://x.com/zoomeyebot/status/2103254422856020072 · https://x.com/boss_sec_labo/status/2103251597589700852
- **Rejetto HFS2 CVE-2026-97359**：称 multipart 文件名模板注入未认证 RCE（CVSS 声称 10.0）——防御升版；**不转载步骤**。X：https://x.com/SecAlertsCo/status/2103256175902925067
- **TeamCity CVE-2026-63077**：日文摘要称勒索关联利用——**UNCONFIRMED**。X：https://x.com/boss_sec_labo/status/2103251597589700852

IoC：未见公开 IoC。

### 13. 【X B／LWiS · 非 KEV】WordPress CVE-2026-87902／PostgreSQL CVE-2026-15742

- **WP CVE-2026-87902**：未认证页面模板路径穿越 → 条件性 RCE；GHSA 已发；nuclei-templates yaml 在 Search B 被引用。**非今晚 NEW KEV**。利用／流量上升声称 **UNCONFIRMED**。
- **PG CVE-2026-15742**：LWiS @N3mes1s 给出防御向日志检测提示（大整数 levenshtein 参数）并建议打补丁——**仅记录狩猎线索；PoC／RCE 声称仍 UNCONFIRMED；不转载利用步骤**。

地址：
- GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-87902.yaml
- X（B）：https://x.com/Zerodaylabowner/status/2103051662944321555
- X（B）：https://x.com/wtf_yodhha/status/2103045866567483772
- X（LWiS PG 狩猎）：https://x.com/N3mes1s/status/2103112330812833953
- NVD PG：https://nvd.nist.gov/vuln/detail/CVE-2026-15742

IoC（PG 帖文可见狩猎模式，原样抄录，非确认 IoC）：
- `/var/log/postgresql/*.log`
- `levenshtein.*[0-9]{9,}`
其余：未见公开 IoC。

## 工具与 GitHub 发布

### 核心版本脉冲（公开备援）

Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 相对昨日 **无升版**。Risky Business **SRB183→SRB184（NEW 2026-09-24，SRB184a）**；RBNEWS 仍 **614**；BTN183 不变；tl;dr **#346→#347（NEW）**。

地址：
- Sliver：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- nuclei：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- SRB184a：https://risky.biz/SRB184a/
- RBNEWS614：https://risky.biz/RBNEWS614/
- BTN183：https://risky.biz/BTN183/
- tl;dr #347：https://tldrsec.com/p/tldr-sec-347

IoC：未见公开 IoC。

### X Search B／相关工具仓（防御认知）

多条覆盖约 **72h**（含 Sep 21–22 prior_seen）。仅列防御认知／仓库定位；**不转操作步骤**。

- **BotC2-RAT**（NEW）：https://github.com/ShadowOpCode/BotC2-RAT · PDF https://github.com/ShadowOpCode/BotC2-RAT/blob/main/BotC2_RAT.pdf · X https://x.com/blackstormsecbr/status/2103220590740140368
- **nuclei-templates WP CVE-2026-87902**：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-87902.yaml · X https://x.com/Zerodaylabowner/status/2103051662944321555 · https://x.com/wtf_yodhha/status/2103045866567483772
- **Red-Team-Roadmap**（训练向）：https://github.com/Dev-Chukwuma/Red-Team-Roadmap · X https://x.com/httpschuks/status/2103026922074653122 · https://x.com/httpschuks/status/2102475014926684457 · https://x.com/httpschuks/status/2102105619515969974（后者 prior）
- **adk-demo-target**（prior）：https://github.com/rbrus/adk-demo-target · X https://x.com/sixi4ai/status/2102618219882438705
- **KaliGPT**（prior）：https://github.com/SudoHopeX/KaliGPT · X https://x.com/r0psx_ninja/status/2102598052397932552
- **nuclei-templates Strapi CVE-2026-27886 PR**（prior）：https://github.com/projectdiscovery/nuclei-templates/pull/16304/commits/7247bac3eb5eb27cba9bc613a91abb8c9c697853 · X https://x.com/zeroc00i/status/2102580743075463229
- **OneDrive-UDC2**（prior；Cobalt Strike 传输面——防御认知）：https://github.com/nmht3t/OneDrive-UDC2 · X https://x.com/r1cksec/status/2102348916935012788
- **ARES**（prior；授权交战编排）：https://github.com/Mafifrizi/ARES · X https://x.com/EsGeeks/status/2102243918272168438

IoC：工具帖未见公开 IoC。

### LWiS 相关研究／工具向交叉

覆盖约 **84h**（含 Sep 21–22 材料；**交叉校验，不假装 24h Latest**）。

- **SnafflePy**（Snaffler Linux／HTML 报告）：https://github.com/S3cur3Th1sSh1t/SnafflePy/tree/main · X https://x.com/ShitSecure/status/2103121947626201286
- **netexec-mcp**：https://mpgn.fr/building-a-mcp-for-netexec/ · X https://x.com/mpgn_x64/status/2103210484011086269
- **SpecterOps · AI for Offensive Security**：https://specterops.io/blog/2026/09/24/ai-for-offensive-security/#h-vulnerability-nbsp-discovery-and-nbsp-validation-nbsp · X https://x.com/SpecterOps/status/2103228031691051146
- **PHP UAF 修复／macOS sandbox 研究**：https://therealcoiffeur.com/c111001.html · X https://x.com/Coiffeur0x90/status/2102419040706712025
- **Agent Blast Radius（K8s 提权建模）**：https://vishalmurugan.substack.com/p/from-a-sandbox-pod-to-cluster-admin?r=94s84p&utm_campaign=post&utm_medium=web&utm_source=x · X https://x.com/Dinosn/status/2102297989826134373

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. Anthropic September threat report

@AnthropicAI 发布／转述 9 月威胁报告（Search C）。防御：关注 AI 辅助入侵与滥用趋势条目；对照自身暴露面与检测覆盖。

地址：
- X：https://x.com/AnthropicAI/status/2103209439520034969

IoC：未见公开 IoC（详见原文／报告页）。

### 2. Iran Threat Actor Playbook（ForIntOrg）

称伊朗相关行动者分工覆盖网络入侵、监控、侨民、洪水／虚假信息与伪造内容——**观察向综述；归因与细节未独立核验**。防御：按行业通告强化身份／邮件／对外暴露面监控。

地址：
- X：https://x.com/ForIntOrg/status/2103262142363472010

IoC：未见公开 IoC。

### 3. 【LWiS】Warden Windows infostealer

@g0njxa 访谈／报道称 Warden 为新兴 Windows 信息窃取木马、使用面上升。防御：加强终端／浏览器凭据防护与 EDR 狩猎；关注 stealer 分发链。

地址：
- 文章：https://g0njxa.medium.com/approaching-stealers-devs-a-brief-interview-with-warden-a978d5ae1147
- X：https://x.com/g0njxa/status/2102063297382015139

IoC：未见公开 IoC（详见原文）。

### 4. 【X · 未验证】地下勒索／泄露声称（合辑）

以下均为社交／论坛列表报道，**一律 UNCONFIRMED／未验证**：

- GlobalAdmissions／China-Admissions 库泄露声称：https://x.com/intels_daily/status/2103259977926291548 · https://x.com/intels_daily/status/2102882497222615522（后者 prior）
- Paraguay 选举司法数据／Zumarius：https://x.com/intels_daily/status/2102873202997289176 · https://x.com/Splint3r7/status/2102861920575328716
- 西班牙约 5 万条 IBAN／PII 售卖：https://x.com/DailyDarkWeb/status/2102872661307077025（prior）
- ShinchanReal／Pobeda 乘客记录：https://x.com/intels_daily/status/2102867386361634946（prior）
- Emperador／OnTrac 勒索声称：https://x.com/ThreatAtlas/status/2102864741190242526 · https://x.com/FalconFeedsio/status/2102863904582041673
- 其他 C 保留监控帖（无实质公开 IoC）：https://x.com/iZOOlogic/status/2103258535123366329 · https://x.com/FalconFeedsio/status/2103251468740706790 · https://x.com/ThreatAtlas/status/2103250831260987633 · https://x.com/XQOPTRX/status/2103247568146763928 · https://x.com/kernelstub/status/2103219906863063056

IoC：帖文可见主机名声称（非核验）— `GlobalAdmissions[.]com`／`China-Admissions[.]com`／`flypobeda[.]ru`／`ontrac.com`；其余多数 **未见公开 IoC**。

### 5. ICS

本日公开备援 **无单独突出的 2026-09-24 新 ICS advisory 主条**（KEV 主更新为 WSO2／Adobe）。网关／编排／APM／VPN 类仍以明日 due 桶为主。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Check Point 85102／93616（明日 due 09-25）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`；另见 sk1000171 厂商狩猎节。
- **PostgreSQL 15742 狩猎模式（LWiS，非确认 IoC）**：`/var/log/postgresql/*.log`；`levenshtein.*[0-9]{9,}`。
- **地下声称可见主机名（UNCONFIRMED）**：`GlobalAdmissions[.]com`／`China-Admissions[.]com`／`flypobeda[.]ru`／`ontrac.com`。
- **NEW KEV WSO2 5430／Adobe 71362／Zyxel 7273（今日 due）／Chromium 87491 新逾期／MS 仍逾期／Arista 93952／F5 94127／JFrog／仍逾期 ISE／Pixel／Acronis／WP 87902／工具仓**：未见可抄录公开 IoC（或仅厂商 SK 内）。
- **Anthropic／Iran playbook／Warden／SpecterOps 等**：未见公开 IoC 或详见原文。
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

本窗口 LWiS List 只读采集：保留 **8** 条、覆盖约 **84h**（`logged_in=true`／`@seogoogle4`／`blocked=false`）；跨源 ID 重叠 0；含 1 条 prior_seen（BleepingComputer Check Point）；meta：`/workspace/x-lwis-list-meta-2026-09-24.json`。

## 来源搜索 URL

- X Latest A（CVE-2026 精炼）：https://x.com/search?q=%22CVE-2026%22%20-filter%3Areplies%20-from%3ACVEnew%20-from%3AIhhsanMuhammad&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／cobalt）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky SRB184a：https://risky.biz/SRB184a/
- Risky RBNEWS614：https://risky.biz/RBNEWS614/
- tl;dr sec：https://tldrsec.com/
- tl;dr #347：https://tldrsec.com/p/tldr-sec-347
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 今日两条 KEV 警报：https://www.cisa.gov/news-events/alerts/2026/09/24/cisa-adds-two-known-exploited-vulnerabilities-catalog
