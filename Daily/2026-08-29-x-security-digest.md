# X 安全情报晚报 · 2026-08-29

> 搜集窗口：圣地亚哥时间 **2026-08-28 20:00 至 2026-08-29 20:15**（America/Santiago / UTC-4）。**本报为官方 20:00 cron 晚报（周六）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-08-29.json`（collected_at **2026-08-29T20:05:00-04:00**）。CISA KEV catalogVersion **仍为 2026.08.27**／**1685** 条／dateReleased **2026-08-27T17:00:36.6632Z**。**2026-08-28／08-29 dateAdded：无新 CVE**；无 08-28／08-29 新 CISA Alert；无新 ICSA。**期限今日**是 Citrix **CVE-2026-8452** 与 MS SQL **CVE-2019-1068**。PaperCut **CVE-2026-82078／81578 仍未入 KEV**，厂商页 Last updated **August 29, 2026**。
> X：文件 `/workspace/x-posts-2026-08-29.json`（**30** 条，cve 17／tool 5／apt 8；collected_at **2026-08-29T20:15:00-04:00**；**logged_in=true**／**blocked=false**／账号 **@seogoogle4**）。搜索1 Latest 最旧可见约 **2026-08-29T21:21:39Z**（约 **2.7 小时**，高流量，**不可当作完整 24h**）。搜索2 量少可覆盖 24h+（最旧可见至 **8/22**）。搜索3 最旧可见约 **2026-08-29T23:08:23Z**（约 **1 小时**）。Search C 末尾出现一次 “Something went wrong” 横幅，非硬性限流。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉引用，且 A／C 窗口偏短。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造 CVE、URL、哈希、日期、推文或 IoC。无 URL 不写叙事。
> 说明：防御向晚报。只记谁／打什么／补丁与狩猎。不转载利用代码、payload、请求样例或 PoC。

## 今日摘要

- **期限今日 · Citrix NetScaler CVE-2026-8452 ＋ Microsoft SQL Server CVE-2019-1068（KEV due 2026-08-29）**：dateAdded 均为 **2026-08-26**；ransomwareCampaignUse **Unknown**。Citrix 补丁构建：**14.1-72.61+**／**13.1-63.18+**／**14.1-72.61 FIPS+**／**13.1-37.272 FIPS/NDcPP+**；前置条件为 Gateway（VPN／ICA／CVPN／RDP Proxy）**或** AAA vserver。SQL Server 按 MSRC 打补丁。本轮 KEV 无增量。IoC：厂商页未见 C2／IP／域名；公开报道曾提 `/var/vpn/theme/` 下 `x.php`／`z.php` 作为狩猎线索（非本轮新发现）。
  厂商：https://support.citrix.com/external/article/CTX696604/netscaler-adc-and-netscaler-gateway-secu.html https://msrc.microsoft.com/update-guide/vulnerability/CVE-2019-1068
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-8452 https://nvd.nist.gov/vuln/detail/CVE-2019-1068
  CISA：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  文章：https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploiting-citrix-netscaler-rce-flaw-in-attacks/

- **紧急延续 · PaperCut NG／MF CVE-2026-82078／CVE-2026-81578（尚未入 KEV）**：Emergency Patch **Release 2** 仍须安装（即使已打第一轮）。厂商页 **Last updated August 29, 2026**。本窗口 **AEST 新增**：FAQ（10:53／20:48）＋ **Card/ID lookup 与 SAML 打补丁后问题正在调查**（16:35）。NVD Last Modified **2026-08-29**（NIST CVSS 仍 N/A）。受影响至 **24.1.10／25.0.13／26.0.5** 之前。公网 Application Server 仍须立刻把 Web 管理面限制到受信 IP。**不转写利用细节。** IoC：厂商狩猎字符串＋Huntress 观察＋Release 2 SHA256 见地址／IoC 汇总。
  厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-82078 https://nvd.nist.gov/vuln/detail/CVE-2026-81578
  文章：https://www.huntress.com/blog/papercut-actively-exploited https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/ https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/

- **期限明日 · ownCloud CVE-2023-49105 ＋ Linux Kernel CVE-2026-53362（due 2026-08-30）**：延续 08-27 三连加的前两项。JFrog Artifactory **CVE-2026-66384** due **09-10**。Gitea **CVE-2026-60004** 联邦期限已于 **昨日 08-28** 到期。IoC：未见公开 IoC。
  CISA：https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2023-49105 https://nvd.nist.gov/vuln/detail/CVE-2026-53362 https://nvd.nist.gov/vuln/detail/CVE-2026-66384 https://nvd.nist.gov/vuln/detail/CVE-2026-60004

- **本窗口 X 交叉 · WordPress Forminator CVE-2026-15748（NVD 发布 2026-08-18，非本日新披露；X 今日转载）**：未认证任意文件上传，Wordfence CVSS 3.1 **9.8**。受影响 **≤1.56.1**。本轮 Wordfence 博文被 WAF 挡住，补丁号以插件更新通道／Wordfence 文为准，**不编造已修版本号**。**尚未入 KEV。不转写绕过细节。** IoC：未见公开 IoC。
  厂商／NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-15748
  文章：https://www.wordfence.com/blog/2026/08/600000-wordpress-sites-affected-by-arbitrary-file-upload-vulnerability-in-forminator-forms-wordpress-plugin/ https://www.wordfence.com/threat-intel/vulnerabilities/id/263ac05d-f1ca-46e3-a43e-3b45eb8066d4?source=cve
  X：https://x.com/MalwareBibleJP/status/2093822507170328609

- **本窗口交叉 · IBM ARE for i CVE-2026-18527（NVD 发布／修改 2026-08-28；厂商公告初版 08-21）**：CWE-384；IBM CVSS 3.1 **9.9**。另有信息泄露 **CVE-2026-17203**（7.5）。受影响 **V1R1M0**；PTF **SJ11185**（打完后旧 GUI 不可用）。**尚未入 KEV。** IoC：未见公开 IoC。
  厂商：https://www.ibm.com/support/pages/node/7284580
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-18527
  X：https://x.com/ADKCyber/status/2093820052352995370

- **X 声称／需标注 · Nvidia「GreenSection」用户态内存破坏（尚无 CVE、无厂商公告）**：研究员公开仓库。本报只记 URL，**不转写、不复现**。公开备援未独立核验。IoC：未见公开 IoC。
  仓库：https://github.com/MSNightmare/GreenSection
  X：https://x.com/MSNightmare2000/status/2093835397172216238 https://x.com/_MrNiko/status/2093842412871504139

- **X 旧 KEV 回放（非今日新加）**：Progress LoadMaster **CVE-2026-8037**（KEV dateAdded **2026-08-07**／due **08-10**）；Zimbra **CVE-2026-73570**（dateAdded **2026-08-21**／due **08-24**，补丁 **10.1.20**）；Microsoft WinSock **CVE-2026-68820**（dateAdded **2026-08-11**／due **08-25**）。X 称 LoadMaster 仍在被扫。IoC：未见公开 IoC。

- **工具**：Sliver **仍为 v1.7.6**；nuclei-templates **仍为 v10.4.8**。X 新提及 **Whispergate/InfraGuard**（C2 重定向器）。tailcat 为昨日已见交叉。IoC：未见公开 IoC。
  仓库：https://github.com/BishopFox/sliver/releases/tag/v1.7.6 https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8 https://github.com/Whispergate/InfraGuard

- **勒索／声称（X 窗口，公开备援未独立核验）**：ShinyHunters → Neogen Corporation（美农业食品）；Qilin → LAPoco Architects；m3rx 声称 Lindner Group **4.6 TB／2,638,995 文件**；佐治亚州 Norcross 市遭勒索（未点名家族）；柏林州网络勒索 **30 BTC**／逾 10 万文件（延续昨日 Rhysida 语境）。IoC：未见公开 IoC。

- **ICS／Alert**：无 08-28／08-29 新 ICSA、无新 CISA Alert。KEV 目录本身未更新。

## CVE / POC / 漏洞

### 1. 【KEV 期限今日】Citrix NetScaler CVE-2026-8452（dateAdded 2026-08-26；联邦期限 2026-08-29）

内存边界操作限制不当，CISA 短描述可导致拒绝服务。已知在野（KEV）。补丁（CTX696604）：**14.1-72.61+**、**13.1-63.18+**、**14.1-72.61 FIPS+**、**13.1-37.272 FIPS/NDcPP+**。前置：Gateway（VPN／ICA／CVPN／RDP Proxy）或 AAA vserver。BOD 26-04：曾暴露主机取证分诊。**不转写利用细节。**

狩猎：立刻按构建号核对；公网 Gateway／AAA 优先；备份配置后升级。

地址：
- 厂商 CTX696604：https://support.citrix.com/external/article/CTX696604/netscaler-adc-and-netscaler-gateway-secu.html
- 厂商（KEV notes 备用路径）：https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696604
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-8452
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- KEV 字段页：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-8452
- CISA 08-26 六连加警报：https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog
- 文章（较早，作上下文）：https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploiting-citrix-netscaler-rce-flaw-in-attacks/
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-on-risk

IoC：CTX696604 本轮未见 C2／IP／域名。公开报道曾提 web shell 路径 `/var/vpn/theme/x.php`、`/var/vpn/theme/z.php` 作为狩猎线索（非本轮新 IoC，当 hunt lead）。

### 2. 【KEV 期限今日】Microsoft SQL Server CVE-2019-1068（dateAdded 2026-08-26；联邦期限 2026-08-29）

远程代码执行。ransomwareCampaignUse **Unknown**。按 MSRC 更新指南打补丁。续报，无今日 KEV 增量。

地址：
- MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2019-1068
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2019-1068
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 08-26 警报：https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC。

### 3. 【紧急／在野／尚未入 KEV】PaperCut NG／MF CVE-2026-82078＋CVE-2026-81578 · 厂商页更新 2026-08-29

相对昨日晚报：KEV **仍未收录**；NVD Last Modified **2026-08-29**（NIST CVSS 仍 N/A）；厂商页新增 FAQ 与 **Card/ID lookup + SAML 打补丁后问题调查中**（AEST 29 Aug 04:35pm）。Release 2 要求不变。Huntress／Rapid7／THN 报道仍有效。**本报不转写根因、请求样例或利用步骤。**

| CVE | 名称 | CWE | 分数 | NVD |
|---|---|---|---|---|
| CVE-2026-82078 | Unsafe Dynamic Class Loading in Database Connector | CWE-470 | 厂商 CVSS 4.0 **9.4**（昨日晚报）；NIST 本轮 N/A | Last Modified 2026-08-29 |
| CVE-2026-81578 | Authentication Bypass | CWE-306 | 厂商 CVSS 4.0 **8.8**（昨日晚报）；NIST 本轮 N/A | Last Modified 2026-08-29 |

受影响（NVD／PaperCut semver）：MF／NG 在 **24.1.10、25.0.13、26.0.5** 之前。Release 2 覆盖 v24／v25／v26（Win／Linux／macOS）。v23 及更早：升级到最新。公网 Application Server：**立刻**限制 Web 管理面到受信 IP。

狩猎信号与 Release 2 SHA256：**见地址／IoC 汇总**。厂商强调：缺失这些 IoC ≠ 未中招。

地址：
- 厂商紧急公告：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- NVD CVE-2026-82078：https://nvd.nist.gov/vuln/detail/CVE-2026-82078
- NVD CVE-2026-81578：https://nvd.nist.gov/vuln/detail/CVE-2026-81578
- Huntress：https://www.huntress.com/blog/papercut-actively-exploited
- Rapid7：https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/
- BC（Release 2）：https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/
- THN（链利用，昨日）：https://thehackernews.com/2026/08/attackers-chain-two-papercut-flaws-to.html

IoC：厂商狩猎字符串＋Huntress 观察＋全部 Release 2 SHA256 见「地址／IoC 汇总」。未见独立公开的攻击者 C2 IP／域名／样本哈希清单。

### 4. 【期限明日】ownCloud CVE-2023-49105 ＋ Linux Kernel CVE-2026-53362（due 2026-08-30）

延续 08-27 KEV 三连加。ownCloud：未认证 WebDAV 预签名 URL 绕过；补丁 ≥10.13.1（厂商后催 ≥10.13.3）。Kernel：IPv6 相关（昨日晚报）。无今日 KEV 增量。

地址：
- CISA 08-27 警报：https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
- 厂商 ownCloud：https://owncloud.com/security-advisories/webdav-api-authentication-bypass-using-pre-signed-urls/
- NVD ownCloud：https://nvd.nist.gov/vuln/detail/CVE-2023-49105
- NVD Kernel：https://nvd.nist.gov/vuln/detail/CVE-2026-53362
- NVD JFrog CVE-2026-66384（due 09-10）：https://nvd.nist.gov/vuln/detail/CVE-2026-66384
- JFrog 公告索引：https://docs.jfrog.com/releases/docs/jfrog-security-advisories

IoC：未见公开 IoC。

### 5. 【X 转载／NVD 已有】Forminator Forms CVE-2026-15748（NVD 发布 2026-08-18；Last Modified 2026-08-20；尚未入 KEV）

WordPress 表单插件未认证任意文件上传，Wordfence CVSS 3.1 **9.8**（AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H）。受影响 **≤1.56.1**。X 卡片称约 60 万站点。本轮 Wordfence 博文抓取被 CloudFront challenge 挡住，**不编造补丁版本号**——以 WordPress 插件更新通道及 Wordfence 原文为准。**不转写 MIME／字段伪造等利用细节。** 非本日新披露，仅因 X 窗口出现而交叉。

地址：
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-15748
- Wordfence 博文（X 卡片）：https://www.wordfence.com/blog/2026/08/600000-wordpress-sites-affected-by-arbitrary-file-upload-vulnerability-in-forminator-forms-wordpress-plugin/
- Wordfence intel：https://www.wordfence.com/threat-intel/vulnerabilities/id/263ac05d-f1ca-46e3-a43e-3b45eb8066d4?source=cve
- X：https://x.com/MalwareBibleJP/status/2093822507170328609

IoC：未见公开 IoC。

### 6. 【本窗口交叉】IBM Administration Runtime Expert for i CVE-2026-18527（NVD 2026-08-28；厂商初版 2026-08-21）

CWE-384 Session Fixation。IBM CVSS 3.1 **9.9**（AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H）。同公告 **CVE-2026-17203**（CWE-287，7.5，敏感信息）。受影响 **V1R1M0**。修复：PTF **SJ11185**（https://www.ibm.com/mysupport/s/fix-information?legacy=SJ11185）；打完后 legacy ARE GUI 不可用。无缓解措施。**尚未入 KEV。不转写利用细节。**

地址：
- 厂商公告：https://www.ibm.com/support/pages/node/7284580
- PTF：https://www.ibm.com/mysupport/s/fix-information?legacy=SJ11185
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-18527
- X：https://x.com/ADKCyber/status/2093820052352995370

IoC：未见公开 IoC。

### 7. 【X 声称／无 CVE／无厂商】Nvidia 用户态「GreenSection」内存破坏

X：研究员 @MSNightmare2000 公开仓库，描述为 Nvidia 用户态 DLL／全局节相关内存破坏，可能跨用户边界。本轮 GitHub API 限流，未拉取仓库元数据。公开备援（KEV／NVD／厂商）**无对应 CVE、无 Nvidia 公告**。**只记 URL，不转写、不复现、不评估可利用性。**

地址：
- 仓库：https://github.com/MSNightmare/GreenSection
- X 作者：https://x.com/MSNightmare2000/status/2093835397172216238
- X 转发：https://x.com/_MrNiko/status/2093842412871504139

IoC：未见公开 IoC。

### 8. 【旧 KEV 回放／X 称仍在扫描】Progress LoadMaster CVE-2026-8037（KEV dateAdded 2026-08-07；due 2026-08-10）

未认证命令注入。NVD NIST CVSS 3.1 **9.8**。补丁：LoadMaster **≥7.2.63.2**／**≥7.2.54.18**（分支不同）；相关 ECS／Object Scale Connection Manager、MOVEit WAF 同系列。X 称入 KEV 前已有 792 次利用尝试、现仍被打。**非今日新加 KEV。不转写利用细节。**

地址：
- 厂商：https://community.progress.com/s/article/LoadMaster-Critical-Security-Bulletin-June-2026-CVE-2026-8037-CVE-2026-33691
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-8037
- CISA KEV 字段：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-8037
- watchTowr（第三方，不抄利用）：https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/
- eSentire：https://www.esentire.com/security-advisories/progress-kemp-loadmaster-vulnerability-targeted-cve-2026-8037
- X：https://x.com/D0xedDevi0/status/2093843835059368227

IoC：未见公开 IoC。

### 9. 【旧 KEV 回放】Zimbra Collaboration CVE-2026-73570（dateAdded 2026-08-21；due 2026-08-24 已过）

OS 命令注入。补丁 **10.1.20**（NVD：10.1.20 之前受影响）。MITRE CVSS 3.1 **8.9**。可选 **zimbra-snmp** 且启用 SNMP 通知为触发条件（NVD 描述，防御向）。X 今日日文帖复述「已入 KEV、升 10.1.20」——属旧条目回放，**本轮 KEV 无 08-28／08-29 新加**。**不转写 SMTP／SNMP 请求样例。**

地址：
- 厂商 advisories：https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories
- 厂商 Security Center：https://wiki.zimbra.com/wiki/Security_Center
- 厂商 10.1.20：https://blog.zimbra.com/2026/07/patch-release-update-zimbra-10-1-20/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-73570
- CISA KEV 字段：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-73570
- CERT.PL：https://moje.cert.pl/komunikaty/2026/145/aktywnie-wykorzystywana-podatnosc-w-zimbra-collaboration-suite/
- X：https://x.com/Teeeda_worker/status/2093821093744439766 https://x.com/oyusuke0603/status/2093845179803512882

IoC：未见公开 IoC。

### 10. 【延续】ServiceNow CVE-2026-18885／18886／74820（X 今日复述昨日满分三项）

昨日晚报已报。厂商称这三项＋CVE-2026-6876 未见恶意利用。云侧已打；自管须打热修。X 今日补了 CVE 号交叉。**尚未入 KEV。**

地址：
- BC：https://www.bleepingcomputer.com/news/security/servicenow-warns-of-three-max-severity-security-vulnerabilities/
- THN：https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html
- X：https://x.com/McM1Alex/status/2093838938012000628

IoC：未见公开 IoC。

### 11. 【X 仅见／公开备援未核验】其他短项

- **WooCommerce CVE-2026-15369**：希腊文帖称可获管理员权限。本轮 NVD 详情页未完整渲染。不作确认在野。
  文章：https://www.secnews.gr/729086/cve-2026-15369-woocommerce-eupatheia/
  X：https://x.com/SecNews_GR/status/2093826562596524538
  IoC：未见公开 IoC。
- **Linux Foundation Magma 1.9.0 CVE-2026-82549**：仅 VulDB 条目。
  文章：https://vuldb.com/vuln/397065
  X：https://x.com/vuldb/status/2093826354898997451
  IoC：未见公开 IoC。
- **CVE-2026-60644「未认证远程接管」**：仅 integsec 博文，推文未点名产品。公开备援未核验。
  文章：https://integsec.com/blog/cve-2026-60644-unauthenticated-remote-takeover-bug-what-it-means-for-your-business-and-how-to-respond
  X：https://x.com/integ_sec/status/2093817218756759842
  IoC：未见公开 IoC。
- **Microsoft CVE-2026-68820**（WinSock Ancillary Function Driver UAF）：**已在 KEV**（dateAdded 2026-08-11，due **2026-08-25 已过**）。X 日文帖复述。
  MSRC：https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2026-68820
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-68820
  X：https://x.com/oyusuke0603/status/2093843027685195801
  IoC：未见公开 IoC。
- **Gitea CVE-2026-60004**：联邦期限 **昨日 08-28** 已过。补丁 **1.27.1**。
  GHSA：https://github.com/go-gitea/gitea/security/advisories/GHSA-rcr6-4jqh-j84m
  发布：https://github.com/go-gitea/gitea/releases/tag/v1.27.1
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-60004
  IoC：未见公开 IoC。
- **Chrome 151 CVE-2026-76034／76036、Tomcat CVE-2026-65182、ASUS 待分配 CVE**：X 链接文章日期为 08-20／08-25／08-26 或无 CVE，视为过期转载，不单列新事件。
  Chrome 文：https://www.cybernote.click/2026/08/20/google-chrome-151-cve-2026-76034-76036-update/
  ASUS 公告页：https://www.asus.com/security-advisory/

## 工具与 GitHub 发布

### 1. BishopFox/sliver · 仍为 v1.7.6（无更新）

昨日晚报已记 **v1.7.6**（2026-08-28T18:37:03Z）。本轮 GitHub API 最近发布仍为此版。nuclei-templates **仍为 v10.4.8**（2026-08-24T13:01:50Z）。

地址：
- https://github.com/BishopFox/sliver/releases/tag/v1.7.6
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

IoC：未见公开 IoC。

### 2. 【X 本窗口】Whispergate/InfraGuard（C2 重定向／管理）

X：红队向「支持主流 C2 的重定向代理与管理器」。本轮 GitHub API 限流，未拉元数据。防御向记录：环境中出现该仓库／同名二进制时当 C2 基建狩猎线索，不提供使用说明。

地址：
- 仓库：https://github.com/Whispergate/InfraGuard
- X：https://x.com/hunterinosec/status/2093649215633195110

IoC：未见公开 IoC。

### 3. 【X 交叉／昨日已见】tailscale/tailcat

X 再贴「like netcat, but over Tailscale's data plane」。昨日晚报已作交叉。非新发行版标签。

地址：
- 仓库：https://github.com/tailscale/tailcat
- X：https://x.com/0xjams/status/2093540911007289686

IoC：未见公开 IoC。

### 4. 【X】CyberStrike（LLM 驱动自动化渗透框架）

X 指向 GitHub 仓库。公开备援未核发版。仅作工具出现记录。

地址：
- 仓库：https://github.com/CyberStrikeus/CyberStrike
- X：https://x.com/Pethuraj/status/2093754216108167212

IoC：未见公开 IoC。

其余 X 工具帖（Objective-See 工具清单、SOFA OSINT harness）无新 C2／nuclei／sliver 发布，不单列。

## APT / Malware 分析

### 1. 【X 声称】ShinyHunters → Neogen Corporation（美国农业／食品）

两条监测帖称将该公司列为受害者。公开备援（BC／THN／CISA）本轮**无独立报道**。昨日 McKesson／ShinyHunters 为另一事件。**未核验，当声称。**

地址：
- X：https://x.com/TMRansomMon/status/2093841638732755410
- X：https://x.com/sec_news_com/status/2093845484326854884
- X 分析串：https://x.com/sec_news_com/status/2093845486021333282
- 监测页：https://recon.sec-lav.com/#ransomware

IoC：未见公开 IoC。

### 2. 【X 声称】Qilin → LAPoco Architects（美国）

地址：
- 文章：https://www.hendryadrian.com/ransom-lapoco-architects-aug-2026/
- X：https://x.com/TweetThreatNews/status/2093851278346539203

IoC：未见公开 IoC。

### 3. 【X 声称】m3rx → Lindner Group（奥地利制造；声称 4.6 TB／2,638,995 文件）

地址：
- 文章：https://www.hendryadrian.com/ransom-lindner-group-com-aug-2026/
- X：https://x.com/TweetThreatNews/status/2093847495117807677

IoC：未见公开 IoC。

### 4. 【X】佐治亚州 Norcross 市遭勒索（未点名家族）

地址：
- X：https://x.com/MichaelSavaged/status/2093846484181454931

IoC：未见公开 IoC。

### 5. 【延续】柏林州网络勒索（X 提 30 BTC／逾 10 万文件）

昨日晚报已报柏林拒付／Rhysida 语境。今日德语帖复述勒索 30 BTC。公开备援无 08-29 新官方稿。

地址：
- 昨日 THN：https://thehackernews.com/2026/08/berlin-refuses-to-pay-hackers-who-stole.html
- X：https://x.com/trickbetrug/status/2093851291323674912

IoC：未见公开 IoC。

### 6. 本日无显著更新（已核实的 APT 报告）

APT28／HOOKEDGE、McKesson／ShinyHunters 详细取证、19 个钱包窃取扩展：昨日已报，本轮公开备援无新 IoC／新报告。

## 地址／IoC 汇总

### PaperCut（厂商原文＋Huntress 观察；缺失 ≠ 未中招）

- `pc-app.exe` 相关异常／IDS·EDR 告警；`pc-app.exe`／Java 拉起 shell 或发现类工具
- PaperCut `server.log` 缺失、截断或删除
- `ERROR No suitable driver found for jdbc:no:x`
- `ERROR DatabaseUtils - Database error looking up cardID: VALUES CAST`
- 意外 `.class` 位于 `server/lib`（观察到 `Udydn.class`、`Moo97.class`，名称可能变化）
- 对应 `.cmd`／`.out` 位于 `server/data/content`（如 `Udydn.out`、`Udydn.cmd`）
- 日志：`DB URL: jdbc:derby:memory:pwn`
- `derby.log` 启动不规则库名含 `pwn`
- 日志中 Base64：`d2hvYW1pICYgdmVy`（`whoami & ver`）；`d2hvYW1pICYgdmVyICYgdGFza2xpc3Q=`（`whoami & ver & tasklist`）

**Emergency Patch Release 2 SHA-256（厂商表）**

PaperCut MF：
- v26 Win `5c63ef18c523c85d5e73efc7fbb2bd2edacf0b03bcf80fe4d7e4c1a7c8bcbcf4`／Linux `6117b53dd0610052c53aeafced91cd3d0ad80ed1dcc578e873291a8b697b802a`／macOS `7dea84473f8d00d4608b7e797b633f130139e23bf5bba02848a1df0a7e2cc7c6`
- v25 Win `b296de7da020152a83291378ab4ca5c461d76510648347fd6e69f3fb2cd5e9c9`／Linux `296498ef5ec1ac8927dc1ccae9a9aa3c04036da6d2768813e6df818049b3f4a1`／macOS `3e5509f0514228031967934d32e4a40512bd6fb5857bfde3002866bc3ede3f9a`
- v24 Win `75aba456d6629848c89513371c44037f2bdddbc1e39bdadc16d1fed8b59766eb`／Linux `7ac8f002fb602d1f54665d8a18a25fc57cf41239ae0c03b18591ee220b57d419`／macOS `40581392cc11a1f46b90ab5c2607fdacade77aca0de6629c1d78a2a71548fc9c`

PaperCut NG：
- v26 Win `c9a2b356910b5fef3c114d48cb7c508414d1d35ddac74c530d1e8923d357e7d4`／Linux `3261356ced056fd5ab0962a07178701e80c6ebbce30d7158d20ed3c57b1dcf59`／macOS `bdd54d5cb9f20924b059986a44f849df499f7de7cb5cd0a60290d2b2610850e7`
- v25 Win `b155cf19cdab1b7fc92c2dd030d1c0cd439397d83d7749042f65e2364ca03589`／Linux `282be7404a25c12317a2079eed59e8794f0c9d7bd257dee60c39b529da18a46a`／macOS `276ee64a7bb4d4e242fe7ddaecf3cd279eee91e83fbd1e6f44050db2f90bda6d`
- v24 Win `f58a3fe4e9d7543c38a3f01e53f4a9ad34884289a71df25f734af9d977c06319`／Linux `a7ea1e2cdb22a4349ae854491b10b89a52d075e9106ec68f838f12d5f2a15f51`／macOS `1e70dd6510d0b9618035a3db462b78ece06cd70f41bcccca8196c015c46a480b`

### Citrix 狩猎线索（非本轮新；当 hunt lead）

- `/var/vpn/theme/x.php`
- `/var/vpn/theme/z.php`

### 其他条目

其余 CVE／工具／勒索声称：**未见公开 IoC**（无 C2、下载 URL、IP、域名、钱包、样本哈希）。

### 全部 URL（便于复制）

- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/cybersecurity-advisories
- https://www.cisa.gov/news-events/ics-advisories
- https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-on-risk
- https://support.citrix.com/external/article/CTX696604/netscaler-adc-and-netscaler-gateway-secu.html
- https://nvd.nist.gov/vuln/detail/CVE-2026-8452
- https://nvd.nist.gov/vuln/detail/CVE-2019-1068
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2019-1068
- https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- https://nvd.nist.gov/vuln/detail/CVE-2026-82078
- https://nvd.nist.gov/vuln/detail/CVE-2026-81578
- https://www.huntress.com/blog/papercut-actively-exploited
- https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/
- https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/
- https://nvd.nist.gov/vuln/detail/CVE-2023-49105
- https://nvd.nist.gov/vuln/detail/CVE-2026-53362
- https://nvd.nist.gov/vuln/detail/CVE-2026-66384
- https://nvd.nist.gov/vuln/detail/CVE-2026-60004
- https://owncloud.com/security-advisories/webdav-api-authentication-bypass-using-pre-signed-urls/
- https://github.com/go-gitea/gitea/security/advisories/GHSA-rcr6-4jqh-j84m
- https://nvd.nist.gov/vuln/detail/CVE-2026-15748
- https://www.wordfence.com/blog/2026/08/600000-wordpress-sites-affected-by-arbitrary-file-upload-vulnerability-in-forminator-forms-wordpress-plugin/
- https://www.wordfence.com/threat-intel/vulnerabilities/id/263ac05d-f1ca-46e3-a43e-3b45eb8066d4?source=cve
- https://www.ibm.com/support/pages/node/7284580
- https://nvd.nist.gov/vuln/detail/CVE-2026-18527
- https://github.com/MSNightmare/GreenSection
- https://nvd.nist.gov/vuln/detail/CVE-2026-8037
- https://community.progress.com/s/article/LoadMaster-Critical-Security-Bulletin-June-2026-CVE-2026-8037-CVE-2026-33691
- https://nvd.nist.gov/vuln/detail/CVE-2026-73570
- https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories
- https://blog.zimbra.com/2026/07/patch-release-update-zimbra-10-1-20/
- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2026-68820
- https://www.bleepingcomputer.com/news/security/servicenow-warns-of-three-max-severity-security-vulnerabilities/
- https://github.com/BishopFox/sliver/releases/tag/v1.7.6
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8
- https://github.com/Whispergate/InfraGuard
- https://github.com/tailscale/tailcat
- https://github.com/CyberStrikeus/CyberStrike
- https://x.com/MalwareBibleJP/status/2093822507170328609
- https://x.com/ADKCyber/status/2093820052352995370
- https://x.com/MSNightmare2000/status/2093835397172216238
- https://x.com/D0xedDevi0/status/2093843835059368227
- https://x.com/hunterinosec/status/2093649215633195110
- https://x.com/TMRansomMon/status/2093841638732755410
- https://x.com/TweetThreatNews/status/2093847495117807677

## 来源搜索 URL

- https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/cybersecurity-advisories
- https://www.cisa.gov/news-events/ics-advisories
- https://nvd.nist.gov/vuln/detail/CVE-2026-8452
- https://nvd.nist.gov/vuln/detail/CVE-2026-82078
- https://github.com/BishopFox/sliver/releases/tag/v1.7.6
- https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day%20OR%20%220-day%22&src=typed_query&f=live
- https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20havoc%20OR%20cobalt)&src=typed_query&f=live
- https://x.com/search?q=(APT%20OR%20%22malware%20analysis%22%20OR%20ransomware%20OR%20%22threat%20report%22%20OR%20KEV)&src=typed_query&f=live
