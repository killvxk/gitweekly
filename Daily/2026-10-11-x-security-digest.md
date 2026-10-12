# X 安全情报晚报 · 2026-10-11

> 搜集窗口：圣地亚哥时间 **2026-10-10 20:16 至 2026-10-11 20:10**（America/Santiago / UTC-3，约 24 小时）。ISO／X 搜索：`start_time=2026-10-10T23:16:00Z`，`end_time≈2026-10-11T23:00:00Z`（接口将 end 微调到至少 10 秒前）。
> **X 采集方式**：使用 Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`，含 t.co 展开／entities／note_tweet 字段），**未开浏览器，未检查 @seogoogle4 浏览器登录状态**。A／定向用 relevancy；B／C 各 relevancy；另做 Citrix／Atlassian／SonicWall／Ahsay·PaperCut·AA26·emp3r0r／GhostAction·DarkSword·Dire Wolf·GoBalance·Flax／Flax Typhoon 定向；LWiS List 分批 `from:`（本轮约 4 批高价值：chudyPB／vxunderground／Dinosn／L0Psec／_xpn_／watchtowrcyber／DFIR_Radar／rad9800／pdiscoveryio／Synacktiv／jm33_m0／Flangvik／bohops／_RastaMouse／C5pider／TrustedSec／briankrebs／cyb3rops／daaximus／TheDFIRReport／g0njxa／MsftSecIntel／unit42_intel／HuntressLabs／crowdstrike／Mandiant／Securelist／malware_traffic／bananaben17／nulltap_／cybermergemedia）。本轮约 **20** 次 X 读取（含共享侧短暂 429 重试；未触日限）。合并 **55** 条安全相关新帖（A20／B2／C14／LWiS19），与 seen_ids 去重。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON `/workspace/kev-2026-10-11.json`（= `/workspace/enrich-2026-10-11/kev.json`）；厂商／研究页于 `/workspace/enrich-2026-10-11/`（AA26-281A、CISA Citrix Alert、Atlassian CVE-2026-21589、Previdian 21589、Risky／tl;dr 首页、GitHub releases：emp3r0r／Sliver／nuclei／nuclei-templates）。
> **CISA KEV：catalogVersion 2026.10.08／1739 条，Δ+0**（相对昨日同一版本；dateReleased 仍 2026-10-08T20:09Z）。**今日无 NEW**。
> **due_today（10-11）＝5 条（AA26-281A）**：CVE-2015-5477（ISC BIND）、CVE-2016-3081（Apache Struts）、CVE-2023-22894（Strapi）、CVE-2021-3199（ONLYOFFICE Docs）、CVE-2015-3306（ProFTPD）。**newly_overdue：无**（相对昨日 due=10-10 为空；Citrix 88771／88772／88779、FortiMail 104286、Zammad 102489／102490、Cisco 76504 等仍逾期）；**upcoming 7 天：1 条**（Apple CVE-2026-86950 due **2026-10-13**）。CVE-2026-107406／CVE-2026-21589／CVE-2026-102255／Ahsay 105133／105134 **仍未进 KEV**。
> 抓取备注：部分 CISA HTML／Risky 深链 curl 曾 403，改用 WebFetch 成功；BleepingComputer 相关页常 Cloudflare／403；tl;dr sec 首页可抓，最新仍 **#349**；Risky Business 首页未见明确新 RBNEWS 编号（上一窗口语境仍 RBNEWS618）；GitHub API 正常。
> 规则：每条含完整 https URL；分列 X 原帖／GitHub·PoC 仓库／厂商公告／文章；没有指标就写「未见公开 IoC」；不编造；**不转载利用代码／payload／PoC 步骤**；泄露／入侵／勒索声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【KEV 到期日】AA26-281A 五条 today due 2026-10-11**：ProFTPD CVE-2015-3306、ONLYOFFICE CVE-2021-3199、Strapi CVE-2023-22894、Apache Struts CVE-2016-3081、ISC BIND CVE-2015-5477（Flax Typhoon／Integrity Tech 语境）；联邦 FCEB 今日截止。
  政府：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
  X 原帖：https://x.com/Dinosn/status/2109223733927764403
- **【在野尝试升级 · 未进 KEV】Atlassian CVE-2026-21589**：Previdian 蜜罐累计约 **376** 次尝试／**56** 源 IP（截至 10-11；昨日语境约 321／49）；仍未进 KEV。
  厂商：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
  蜜罐：https://previdian.com/CVE-2026-21589
- **【补丁争议续】AhsayCBS CVE-2026-105133／105134**：多源称厂商 10-09 称 10.3.4.0 已修、10-10 改口「未完全修复」、hotfix **10.3.4.45** 伙伴门户（待公开页交叉）。
  X 原帖：https://x.com/jfernandogg/status/2109343274297115126
  文章：https://nulltap.sh/p/ahsaycbs-webshell-miner/
- **【工具 · 新】emp3r0r v5.2.0→v5.2.2（今日）**：v5.2.0 新增 **QUIC C2 transport**；随后两则 operator 相关 bugfix。
  GitHub：https://github.com/jm33-m0/emp3r0r/releases/tag/v5.2.0
- **【边界设备续】Citrix NetScaler**：107406／88779 窗口内持续催补丁；CISA 告警页仍为 10-09 修订版（纳入 107406）。
  政府：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
  厂商 CTX697191：https://support.citrix.com/external/article/CTX697191
- **【DFIR · 新 IoC】Midnight Mimosa**（Bitdefender）：廉价 MediaTek 预装 Android 恶意软件；狩猎 `com.android.system.lite`／`libeasy.so`、出站 TCP **6000**。
  X 原帖：https://x.com/DFIR_Radar/status/2109313710191702111
  文章：https://securityaffairs.com/200759/malware/bitdefender-finds-preinstalled-android-malware-you-cant-uninstall-seen-in-150-countries.html
- **【DFIR · 新 IoC】The DFIR Report · Proxyjacking／Pawns.app**：暴露 Linux 被装合法带宽代理；IoC 含 `144.172.86.173` 等。
  X 原帖：https://x.com/TheDFIRReport/status/2109388761943417181
- **【合并统计】** X **55**（A20／B2／C14／LWiS19）；seen_ids **2660→2725**；KEV **2026.10.08／1739／Δ0**；due_today **5**；tl;dr #349。

## CVE / POC / 漏洞

### X-1. 【KEV · 今日到期】AA26-281A 五条 due **2026-10-11**（Flax Typhoon／Integrity Tech）
CISA KEV **catalogVersion 2026.10.08** 无更新（Δ0）。联邦 FCEB **今日**到期条目即 AA26-281A 五条老旧但在野：
- **CVE-2015-3306** ProFTPD（不当访问控制／文件读写语境）
- **CVE-2015-5477** ISC BIND（数据处理错误→DoS 语境）
- **CVE-2016-3081** Apache Struts（命令注入）
- **CVE-2021-3199** ONLYOFFICE Docs（路径穿越）
- **CVE-2023-22894** Strapi（敏感信息明文存储）
联合通告将活动与中国关联 Integrity Technology Group 启用工具链（MicroScan／FishHub 等）及 Flax Typhoon 等公开命名交叉；FBI／DOJ 已扣押相关域名（见 APT 节）。防御：盘点暴露的 FTP／BIND／Struts／ONLYOFFICE／Strapi；不可打补丁则隔离；按 AA26-281A 狩猎 SoftEther 伪装、EBurst／office-cli、邮件外传异常。
地址：
- X 原帖（Dinosn）：https://x.com/Dinosn/status/2109223733927764403
- X 原帖（Security Affairs）：https://x.com/securityaffairs/status/2109212450146886100
- X 原帖（到期提醒）：https://x.com/_skinnyguinea/status/2109388619630702901
- 政府 AA26-281A：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- 文章 nulltap（ProFTPD）：https://nulltap.sh/p/proftpd-file-copy-exploitation/
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
IoC：通告含大量域名／IP／哈希（STIX 可下载）；本报摘录见「地址／IoC 汇总 · AA26-281A／Flax」。

### X-2. 【在野尝试升级 · 未进 KEV】Atlassian CVE-2026-21589（任意文件读）
Previdian 公开页更新：自首观至 **2026-10-11** 累计约 **376** 次尝试、**56** 个源 IP、18 国——明确为传感器／蜜罐尝试，**不等于生产端成功入侵已证实**。**仍未进 KEV**。厂商固定版本表未变（Bitbucket 9.4.26／10.2.8／10.5.1；Confluence 9.2.26／10.2.19 等）。防御：优先升固定版；临时 WAF／RewriteValve／urlrewrite 正则阻断 `..` 紧邻 `/` `\` `::`（含编码）；Crowd 集成环境轮换可能泄露的 application 凭据。
地址：
- X 原帖：https://x.com/_skinnyguinea/status/2109367300981670248
- X 原帖：https://x.com/ita_ipo/status/2109230827351515345
- X 原帖：https://x.com/UktusNas/status/2109244881340108959
- 厂商公告：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
- 蜜罐 Previdian：https://previdian.com/CVE-2026-21589
- 研究 watchTowr（既有）：https://labs.watchtowr.com/you-wont-hear-about-these-even-in-myths-atlassian-jira-confluence-and-more-pre-auth-arbitrary-file-read-cve-2026-21589/
IoC：未见统一公开 C2／哈希表；狩猎路径穿越与 WEB-INF／crowd.properties 异常读取。

### X-3. 【在野 · 补丁争议续】AhsayCBS CVE-2026-105133＋105134
窗口内多源复述：10-09 厂商称 **10.3.4.0** 已覆盖；10-10 改口「未完全修复」，hotfix **10.3.4.45** 仅伙伴门户（**未见本轮可核验的独立厂商公开安全公告页**）。nulltap 续写 webshell／假 Edge 挖矿狩猎。防御：管理面仅可信网；打 hotfix／最新构建并重启；狩猎 `cbssvcX64.exe` 异常子进程、TEMP `WinRing0x64.sys`／`Taskgmr.ps1`、伪装 Edge 服务。
地址：
- X 原帖：https://x.com/jfernandogg/status/2109343274297115126
- X 原帖：https://x.com/_pksharma/status/2109280459418915055
- X 原帖：https://x.com/Nulltap_/status/2109232067800436980
- 文章 nulltap：https://nulltap.sh/p/ahsaycbs-webshell-miner/
- 文章 Huntress（既有）：https://www.huntress.com/blog/ahsaycbs-flaws-exploit
IoC：见汇总「AhsayCBS」。

### X-4. 【跟踪 · 有补丁 · 未进 KEV】Citrix NetScaler CVE-2026-107406／88779 续
窗口内持续催促升 **14.1-73.46／13.1-64.29**（及 FIPS／NDcPP 对应）；CISA 告警页 **Last Revised October 09, 2026**（纳入 107406）。Citrix 语境称 107406 公告时未见未缓解利用；88779 仍在 KEV 且已逾期。防御：确认 SAML SP／IdP；打补丁前保全证；对 88771／88772／88779 一并复查。
地址：
- X 原帖：https://x.com/ralbuque/status/2109377972603965868
- X 原帖：https://x.com/_skinnyguinea/status/2109388613347651603
- X 原帖：https://x.com/MalwareBibleJP/status/2109128613476106644
- 政府告警：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- 厂商 CTX697191：https://support.citrix.com/external/article/CTX697191
IoC：未见厂商完整公开网络 IoC；88771 狩猎关键词见既有晚报（pitboss／NSPPE 等，**非利用步骤**）。

### X-5. 【研究／PoC 披露 · 未见确认大规模在野】
- **Handlebars.js CVE-2026-106445**（CVSS 语境 9.2）：受影响 4.0.0–4.7.9，修 **4.7.10+**。X https://x.com/ridvanyagli/status/2109089223009558767 ；GitHub https://github.com/murrez/CVE-2026-106445
- **nginx-ui CVE-2026-107806**（认证后 RCE，修 **2.5.0**）：X https://x.com/ridvanyagli/status/2109087777782468640 ；GitHub https://github.com/murrez/CVE-2026-107806
- **OpenSpug Spug CVE-2026-108540**（CVSS 9.9，公开 PoC、厂商沉默语境）：X https://x.com/ThreatAft/status/2109233619386700051 ；文章 https://threataft.com/articles/openspug-spug-cve-2026-108540-file-transfer-rce
- **miniOrange OTP Verification CVE-2026-106610**（≤5.5.7，修 5.5.8）：X https://x.com/Python_s_/status/2109222539855585776 ；Patchstack https://patchstack.com/database/wordpress/plugin/miniorange-otp-verification/vulnerability/wordpress-miniorange-otp-verification-plugin-5-5-7-privilege-escalation-vulnerability?_s_id=cve
- **Cisco NX-OS／Nexus 多条**（含内存破坏 CVE-2026-76459 及 nulltap 写的 MPLS OAM／NGOAM／NX-API 根执行语境）：X https://x.com/Python_s_/status/2109381257217950197 ；Cisco https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR ；nulltap https://nulltap.sh/p/cisco-nexus-mpls-echo-root-code/ ／ https://nulltap.sh/p/cisco-nexus-ngoam-root-code/ ／ https://nulltap.sh/p/cisco-nx-api-root-execution/
- **【UNCONFIRMED 研究声称】Signal Messaging Server「0day」**（未认证管理端点／指标／日志级别）：研究者 @abraxas_null — **标 UNCONFIRMED／研究 lab 语境，非厂商确认在野**。X https://x.com/abraxas_null/status/2109340167748337907 ；GitHub https://github.com/abraxas/signal-server-dropwizard-admin ；文章 https://abraxaslabs.tech/research/signal-server-dropwizard-admin
IoC：以上条目本窗口未见统一公开恶意 C2 表（Signal 条目为研究披露）。

### X-6. 【跟踪 · PaperCut／SonicWall】
PaperCut ≥26.0.5、SonicWall SMA1000 CVE-2026-102255：本窗口定向检索多为二次转发／噪声；**无显著新厂商版本或新在野确认**。防御同昨日。
- PaperCut watchTowr（既有）：https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/
- SonicWall CyberMerge（既有）：https://cybermerge.com/stories/sonicwall-sma1000-cve-2026-102255-exploited
IoC：未见新增公开网络 IoC。

### X-7. 【其他噪声过滤】
ExploitGrid 批量旧 CVE lab 广告、WordPress「wp2shell」空转发、公寓／slang、非安全「Dire Wolf」游戏／生物帖：**仅作噪声，不采信为新在野事件**。
IoC：无。

### P-1. 【仍逾期高信号】
Citrix **88771／88772／88779**、Check Point 85102／93616、Arista 93952、F5 94127、JFrog 42016／42018、Zyxel 7273、Microsoft 81963／85880／65660、Google 87491／85046／58704、Cisco 76460／**76504**、Acronis 87886、WSO2 5430、Adobe 71362、MikroTik 67279、WordPress 87902、Fortinet **104286**、Zammad **102489／102490**。
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

## 工具与 GitHub 发布

### 1. 【新】emp3r0r **v5.2.0／v5.2.1／v5.2.2**（均 2026-10-11）
相对昨日 v5.1.0：
- **v5.2.0**（03:05Z）：**C2 增加 QUIC transport**
- **v5.2.1**（10:42Z）：operator 本地模式勿清空 C2 workspace
- **v5.2.2**（12:34Z）：operator cleanupConfig 相关再修
防御／监测侧留意 C2 可能更多使用 QUIC／ECH 封装（叠昨日 ECH 叙述）。
- GitHub v5.2.0：https://github.com/jm33-m0/emp3r0r/releases/tag/v5.2.0
- GitHub v5.2.2：https://github.com/jm33-m0/emp3r0r/releases/tag/v5.2.2

### 2. 核心扫描器／C2：其余无新版
- Sliver **v1.7.8**（2026-10-03）：https://github.com/BishopFox/sliver/releases/tag/v1.7.8
- nuclei **v3.11.1**：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates **v10.5.0**（2026-10-05）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.0

### 3. 其他
- Group B「github.com + C2／nuclei…」本窗口几乎全是非安全撞名噪声（有效工具帖极少）。
- vxunderground：再上传大量恶意样本语料（研究向，**勿直接执行**）：https://x.com/vxunderground/status/2109363803930382530

## APT / Malware 分析

### X-1. 【政府／执法 · 今日到期交叉】Flax Typhoon／Integrity Tech · AA26-281A
窗口内持续复述：FBI／DOJ 扣押 Microscan／FishHub 相关 **7 域名**；多国联合通告 AA26-281A；KEV 五条老旧 CVE **今日**联邦到期。ThreatCluster 等二次列举部分域名 IoC（见汇总）。
地址：
- X 原帖：https://x.com/threatcluster/status/2109208970866938027
- X 原帖：https://x.com/DecryptionDigst/status/2109246326105899386
- X 原帖：https://x.com/NTDNews/status/2109268125212442820
- 政府：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- 文章 Help Net（既有）：https://www.helpnetsecurity.com/2026/10/09/fbi-flax-typhoon-microscan-fishhub-domains/
IoC：见汇总「AA26-281A／Flax」；完整表以 STIX／通告原文为准。

### X-2. 【新 · 有狩猎 IoC】Midnight Mimosa（预装 Android）
Bitdefender：廉价 MediaTek 机预装、难卸载；广告欺诈＋代理流量。DFIR Radar：狩猎包名／库与出站 **TCP 6000**。
地址：
- X 原帖：https://x.com/DFIR_Radar/status/2109313710191702111
- X 原帖（Dinosn）：https://x.com/Dinosn/status/2109326445701181882
- 文章：https://securityaffairs.com/200759/malware/bitdefender-finds-preinstalled-android-malware-you-cant-uninstall-seen-in-150-countries.html
IoC：见汇总「Midnight Mimosa」。

### X-3. 【新 · 有 IoC】Proxyjacking via Pawns.app（The DFIR Report）
暴露 Linux 被装合法「卖带宽」代理（Pawns），目标用受害者 IP 赚钱；JSP webshell＋隐藏 `.p` 副本＋`@reboot` cron。
地址：
- X 原帖：https://x.com/TheDFIRReport/status/2109388761943417181
IoC：见汇总「Pawns／Proxyjacking」。

### X-4. 【其他／续】
- Dire Wolf／GhostAction／P7 DarkSword／PoeLLM／GoBalance／Warlock：**本日无显著新公开技术细节**（定向检索「Dire Wolf」被游戏／生物噪声淹没）。沿用昨日晚报。
- JPCERT-AT-2026-0030（国内相次非法访问）：反编译公开 App 抽 API／密钥语境 — X https://x.com/cybermergemedia/status/2109316007940837856 ；政府 https://www.jpcert.or.jp/at/2026/at260030.html
- Plug&Pwn 实用指南（SCRT）：https://blog.scrt.ch/2026/10/06/a-practical-guide-to-plugpwn-for-pentesters-and-defenders/ ／ X https://x.com/Dinosn/status/2109214278133936574
IoC：续报类见原汇总；JPCERT 条目以通告为准。

## 地址／IoC 汇总

### AA26-281A／Flax Typhoon（摘录；完整以通告／STIX 为准）
- 通告：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- STIX JSON：通告页「AA26-281A STIX JSON」下载链
- SoftEther 宿主域名语境（通告正文）：`98aiblog[.]com`、`hmbcloud[.]com`、`hmbcloud[.]net`、`hmbiplc-01[.]com`、`javacheck.ooguy[.]com`、`javaupdate.giize[.]com`、`sexytube0[.]com`、`twimg.co[.]uk` 等
- 基础设施语境：`dns.studiocloud[.]xyz`、`natcloudservice[.]com`、`upl.natcloudservice[.]com`；IP 例 `149.28.132[.]137`
- 二次消息域名摘录（ThreatCluster）：`c0cc[.]cc`、`youtubecard[.]com`、`98aicode[.]com`、`98aicai[.]com`、`linkedinns[.]net`、`outlook3650[.]com`
- 样本／工具哈希：见通告 Appendix（webshell／扫描器／SoftEther 伪装等表）——**本报不整表复述，请直接读 PDF／STIX**

### Midnight Mimosa（DFIR Radar／Bitdefender 摘要，原样）
- 包名语境：`com.android.system.lite`
- 库：`libeasy.so`
- 网络：出站 TCP **6000**
- 文章：https://securityaffairs.com/200759/malware/bitdefender-finds-preinstalled-android-malware-you-cant-uninstall-seen-in-150-countries.html

### Pawns／Proxyjacking（The DFIR Report，原样）
- 基础设施 IP：`144.172.86.173`、`209.99.190.80`（原文写作 144[.]172[.]86[.]173 等）
- 账户：`skynox7@proton.me`
- 文件路径：`/tmp/.p`、`/var/tmp/.p`、`/opt/.p`、`/home/.p`、`/tmp/gotoschool`
- 状态文件：`/var/tmp/.config/pawns-cli/pawns-consent.log`
- 狩猎：web 服务进程拉起 wget／curl；proxyware 启动参数；与 Pawns／Honeygain／EarnApp／PacketStream 通信
- X：https://x.com/TheDFIRReport/status/2109388761943417181

### AhsayCBS（沿用＋今日续）
- 投放：JSP webshell；XMRig 伪装 `edge.exe`；服务名语境 `MicrosoftEdgeUpdateSvc`
- 狩猎：`cbssvcX64.exe` 异常子进程（curl／certutil）；TEMP 中 `WinRing0x64.sys`、`Taskgmr.ps1`
- 补丁语境：10.3.4.0 争议；hotfix **10.3.4.45**（伙伴门户，待厂商公开页）

### Dire Wolf／GhostAction／P7 DarkSword／PoeLLM／Longlegs（沿用昨日）
- Dire Wolf：`Global\\direwolfAppMutex`；`C:\\runfinish.exe`；`HowToRecoveryFiles.txt`；`.direwolf-encrypted`
- GhostAction C2：`193.32.204.199`；工作流名 `security-audit.yml`／`github_actions_security.yml`
- DarkSword IP／域名：见昨日晚报
- PoeLLM：https://github.com/blacklotuslabs/IOCs/blob/main/PoeLLM_IOCs.txt
- Warlock SHA256：见昨日晚报

### SonicWall SMA1000／Atlassian 21589／PaperCut／Citrix 107406
- 未见厂商发布的完整公开网络 IoC 清单；以补丁版本与日志狩猎为主。

### 其他
- Apple CVE-2026-86950 due **2026-10-13**
- 勒索／入侵批量声称：一律 **UNCONFIRMED**，未见可核验公开 IoC

## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/ （本窗口首页未明确新编号；上一窗口语境 RBNEWS618）
- tl;dr sec 通讯：https://tldrsec.com/ （最新仍 **#349** — Vulns & Exploits in the AI Era…；未见 #350）
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form

本窗口 LWiS 交叉要点：@Dinosn AA26／KEV 五条／Midnight Mimosa／Plug&Pwn／密码学工作量估算站；@DFIR_Radar Midnight Mimosa；@TheDFIRReport Pawns proxyjacking；@Nulltap_ ProFTPD／Ahsay／Cisco Nexus 系列；@vxunderground 样本库与「goop」教学长帖；@_xpn_／@rad9800／@C5pider／@bohops／@jm33_m0 互动（emp3r0r 发布见 GitHub，非本批长文）；@cybermergemedia JPCERT 国内泄露波。

## 来源搜索 URL

- X A（relevancy）：`CVE OR POC OR exploit OR 0day` + `CVE POC` + 时间窗
- X B：`github.com (C2 OR "red team" OR nuclei OR Sliver OR Cobalt)` + 时间窗
- X C：`("malware analysis" OR "threat report" OR "threat actor")` + 时间窗
- X 定向：Citrix／NetScaler／107406／88779；Atlassian／21589；SonicWall／102255／SMA1000；Ahsay／105133／PaperCut／AA26-281A／emp3r0r／ProFTPD／Strapi／ONLYOFFICE；GhostAction／DarkSword／PoeLLM／Dire Wolf／GoBalance／Flax；Flax Typhoon／Integrity／MicroScan／FishHub
- X LWiS：`from:h1 OR from:h2 …`（约 4 批高价值）+ 时间窗（recency）
- KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA Citrix Alert：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- AA26-281A：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- Risky：https://risky.biz/
- tl;dr：https://tldrsec.com/
