# X 安全情报晚报 · 2026-10-12

> 搜集窗口：圣地亚哥时间 **2026-10-11 20:16 至 2026-10-12 20:14**（America/Santiago／UTC-3，约 24 小时）。ISO／X 搜索：`start_time=2026-10-11T23:16:00Z`，`end_time=2026-10-12T23:14:00Z`。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`，含 entities／note_tweet；t.co 用 entities.expanded_url，缺失的以 curl 读跳转头展开）。**未开浏览器，未检查 @seogoogle4 浏览器登录状态。** A／C／定向用 relevancy；LWiS 分批 `from:` 用 recency（4 批：①chudyPB／vxunderground／Dinosn／L0Psec／_xpn_／watchtowrcyber／DFIR_Radar／rad9800／pdiscoveryio／Synacktiv／jm33_m0／Flangvik／bohops／_RastaMouse／C5pider／TrustedSec；②briankrebs／cyb3rops／daaximus／TheDFIRReport／g0njxa／MsftSecIntel／unit42_intel／HuntressLabs／crowdstrike／Mandiant／Securelist／malware_traffic／bananaben17／Nulltap_／cybermergemedia／nextronresearch／SpiderLabs；③BleepinComputer／TheHackersNews／securityaffairs／campuscodi／GossiTheDog／malwrhunterteam 等新闻／研究扩展源；④SinSinology／mrd0x／harmj0y／SBousseaden／patrickwardle／tiraniddo／itm4n／thegrugq／fr0gger_ 等 List 成员）。本轮 **16 次 X 读取**（未触限）。合并 **93** 条安全相关新帖（**A32／B6／C21／LWiS34**），全部与 seen_ids 去重。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON `/workspace/enrich-2026-10-12/kev.json`（= `/workspace/kev-2026-10-12.json`）；厂商／研究页存于 `/workspace/enrich-2026-10-12/`（Ahsay 公告、Huntress、Previdian 21589、CrowdSec 21589、CISA Citrix Alert、Citrix CTX697191、AA26-281A、Patchstack／THN Bricksforge、Unit 42 C2Agent IoC／Blinder Tunnel、Elastic REF8801、SpiderLabs PhantomPolia、BleepingComputer Danfoss／Ledger／AvisLoader、Cooling Post、Risky／tl;dr 首页、GitHub releases：emp3r0r／Sliver／nuclei／nuclei-templates）。
> **CISA KEV：catalogVersion 2026.10.08／1739 条，Δ+0**（与昨日同版；dateReleased 2026-10-08T20:09Z＝10-08 17:09 圣地亚哥）。**今日无 NEW**，CISA 已连续 4 天无新增。
> **due_today（10-12）：无。** **newly_overdue：5 条（AA26-281A，10-11 到期，今日起逾期）**：CVE-2015-5477（ISC BIND）、CVE-2016-3081（Apache Struts）、CVE-2023-22894（Strapi）、CVE-2021-3199（ONLYOFFICE Docs）、CVE-2015-3306（ProFTPD）。**upcoming 7 天：1 条**——Apple CVE-2026-86950（CoreGraphics 越界写）**明天 2026-10-13 到期**。CVE-2026-107406（Citrix）／21589（Atlassian）／102255（SonicWall）／105133·105134（Ahsay）／85097（Bricksforge）**仍未进 KEV**。
> 抓取备注：Wordfence 页面要求 JS 验证（curl 202 空页、WebFetch 被挡），只用 X 摘要＋原文链接；其余页面 curl 200。tl;dr sec 最新仍 **#349**；Risky Business 首页最新：Risky Bulletin「ShinyHunters suspects arrested in US and Jordan」、Between Two Nerds「The FBI and ShinyHunters are the same」；GitHub API 正常。
> 规则：每条带完整 https URL；X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标就写「未见公开 IoC」；不编造；**不转载利用代码／payload／PoC 步骤**；泄露／入侵／勒索声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【KEV 逾期】AA26-281A 五条从今天起逾期**（BIND／Struts／Strapi／ONLYOFFICE／ProFTPD，Flax Typhoon／Integrity Tech 语境）；KEV 仍是 2026.10.08 版。**Apple CVE-2026-86950 明天（10-13）到期**。
  政府：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
  X 原帖：https://x.com/jfernandogg/status/2109448974755369410
- **【OT／事件 · 新】法国数百家超市的 Danfoss 冷链控制器遭远程操控**：10-11 夜间被强制进入除霜循环，部分柜温被调到 50 °C；Intermarché、Coopérative U、Leclerc 等受影响，报道称 250～500 家门店。Danfoss 称受影响的多为 EOL 设备（AK-SM800／AK-SC355）和固件过旧的 AK-SM800A。巴黎检方已立案。入侵途径**未确认**。
  X 原帖：https://x.com/BleepinComputer/status/2109666378152050910
  文章：https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/
  厂商声明（Cooling Post）：https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/
- **【在野 · 已出修复】AhsayCBS 105133／105134**：Ahsay 10-12 正式推出 hotfix——v10 用 **10.3.4.45**，v7／v8／v9 用 **9.15.2.70**。Huntress 已独立验证 10.3.4.45 能挡住攻击链的初始入口。
  X 原帖：https://x.com/HuntressLabs/status/2109683722052157506
  厂商：https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134
  研究：https://www.huntress.com/blog/ahsaycbs-flaws-exploit
- **【在野 · 规模扩大】WordPress Bricksforge CVE-2026-85097（CVSS 10）**：Patchstack 记录到 63 个源 IP；THN／SecurityWeek 等 10-12 集中报道。修复版 **3.1.8.10**（部分来源写 4.0.1+）。
  X 原帖：https://x.com/averyjparker/status/2109617279910674795
  厂商（Patchstack）：https://patchstack.com/articles/critical-unauthenticated-arbitrary-file-upload-vulnerability-exploited-in-bricksforge-plugin/
- **【在野尝试 · 未进 KEV】Atlassian CVE-2026-21589**：Previdian 已记录 **380 次尝试／58 个 IP／19 个国家**，最后观测 10-12；CrowdSec 记录 89 个独立 IP（其中 66 个是 LeakIX 扫描），公开 PoC 约 10 个。
  X 原帖：https://x.com/Crowd_Security/status/2109638259873616371
  文章：https://www.crowdsec.net/vulntracking-report/cve-2026-21589-atlassian-jira-confluence-flaw-exploited
- **【AI 恶意软件 · 新 IoC】Unit 42 C2Agent**：Go 编写的 Windows 植入体，由 LLM 驱动，自带 MCP 客户端和 skills，会滥用受害者本机的 AI 编码工具；载荷 URL `agent.x90[.]dev/data/copilot.txt` 发帖时仍可访问。
  X 原帖：https://x.com/Unit42_Intel/status/2109744924530737622
  GitHub IoC：https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-09-C2Agent-malware.txt
- **【供应链 · 新 IoC】Elastic REF8801「Apex Accelerator」**：冒充 Web3 加速器，通过 npm 包 `@apexacc/cli`、`@apexacc/audit` 投放 macOS 后门 CloudSyncD 和 Windows 窃密木马；同时给开发者注册攻击者控制的 MCP 服务器，并截获 OpenRouter 流量。
  X 原帖：https://x.com/DFIR_Radar/status/2109691248533454965
  文章：https://www.elastic.co/security-labs/threat-command/apex-accelerator-malicious-npm-packages
- **【统计】** X 合并 **93**（A32／B6／C21／LWiS34）；seen_ids **2725→2818**；KEV **2026.10.08／1739／Δ0**；due_today **0**；newly_overdue **5**；tl;dr #349。

## CVE / POC / 漏洞

### X-1. 【KEV · 今日起逾期】AA26-281A 五条（10-11 到期）＋ Apple 86950 明天到期
KEV 目录仍是 **2026.10.08**（Δ0）。AA26-281A 的五条旧漏洞联邦期限已过（10-11），从今天起算 **newly_overdue**：ProFTPD CVE-2015-3306、ONLYOFFICE CVE-2021-3199、Strapi CVE-2023-22894、Apache Struts CVE-2016-3081、ISC BIND CVE-2015-5477。WoldLabs 指出：目前的初始访问仍在利用十年以上的旧漏洞。**Apple CVE-2026-86950**（CoreGraphics 越界写，定向攻击中在野利用，PDF／零点击链语境）**10-13 到期**——请确认 iOS／macOS 已升到修复版本。
地址：
- X 原帖（KEV 看板）：https://x.com/jfernandogg/status/2109448974755369410
- X 原帖（WoldLabs）：https://x.com/WoldLabs/status/2109669002578690073
- X 原帖（Apple 86950）：https://x.com/johnmcclure00/status/2109643505299583062
- X 原帖（Apple 86950 博文）：https://x.com/sh3ll_c0d3/status/2109529753422065895
- 政府 AA26-281A：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- 文章（Dark Reading · Apple）：https://www.darkreading.com/cyberattacks-data-breaches/apple-zero-day-vulnerability-weaponized-targeted-attacks
- 文章（sh3ll_c0d3 · Apple）：https://sh3llc0d3.com/blog/apple-coregraphics-zero-day-analyzing-cve-2026-86950-and-in-the-wild-exploitation/
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
IoC：AA26-281A 的 IoC 见「地址／IoC 汇总 · AA26-281A／Integrity Tech」；Apple 86950 未见公开 IoC。

### X-2. 【在野 · 新增 hotfix】AhsayCBS CVE-2026-105133（认证绕过）＋105134
Ahsay 10-10 的公告承认 10.3.4.0「未完全修复」。**10-12** Huntress 更新（12:00 ET＝13:00 圣地亚哥）：Ahsay 已发布 hotfix——v10（含 10.3.4.0）打 **10.3.4.45**，v7／v8／v9 打 **9.15.2.70**。Huntress **已独立验证** 10.3.4.45 能阻断攻击链的初始入口（105133 认证绕过，绕过后才能触达 105134）。hotfix 下载需要伙伴门户账号，打完要重启。防御：立即打 hotfix 并重启；管理面只对可信网开放；按既有狩猎点排查（`cbssvcX64.exe` 异常子进程、TEMP 目录下的 `WinRing0x64.sys`／`Taskgmr.ps1`、伪装成 Edge 的挖矿服务）。
地址：
- X 原帖（Huntress）：https://x.com/HuntressLabs/status/2109683722052157506
- X 原帖（DailyDarkWeb 复述）：https://x.com/DailyDarkWeb/status/2109711351979638839
- 厂商公告：https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134
- 厂商 hotfix（需伙伴登录）：https://www.ahsay.com/en/hotfix-v10-partner-only
- 研究 Huntress：https://www.huntress.com/blog/ahsaycbs-flaws-exploit
IoC：沿用既有晚报（见汇总「AhsayCBS」），今日未见新增网络 IoC。

### X-3. 【在野 · 扩散】WordPress Bricksforge CVE-2026-85097（CVSS 10，未认证上传→RCE）
Patchstack：受影响 ≤3.1.8.9，修复 **3.1.8.10**（BadgerSignal、DFIR_Radar 等写 4.0.1+，以插件更新日志为准）；首次观测到利用是 **2026-10-07 21:47 UTC**（18:47 圣地亚哥）。共 **63** 个源 IP，其中一簇 44 个 IP 在几秒内发出相同请求，属自动化批量利用。THN、SecurityWeek 等 10-12 集中报道。防御：立即升级；排查对 `/wp-json/bricksforge/v1/form_submit` 带 `temporaryFileUploads` 参数的请求；检查 `/wp-content/uploads/bricksforge/tmp/` 下是否有 PHP 文件（尤其 `login_admin_*.php`）。**注**：X 上有账号兜售利用链讲解（@Reductedrecon），已作噪声排除，不转载。
地址：
- X 原帖：https://x.com/averyjparker/status/2109617279910674795
- X 原帖：https://x.com/_skinnyguinea/status/2109646039997431818
- X 原帖：https://x.com/BadgerSignalHQ/status/2109615164274467317
- X 原帖：https://x.com/Orion84x/status/2109628706847121723
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2109600629857694126
- 厂商／研究 Patchstack：https://patchstack.com/articles/critical-unauthenticated-arbitrary-file-upload-vulnerability-exploited-in-bricksforge-plugin/
- 文章 THN：https://thehackernews.com/2026/10/attackers-exploit-cvss-100-bricksforge.html
- 文章 SecurityWeek：https://www.securityweek.com/bricksforge-wordpress-plugin-vulnerability-exploited-in-the-wild/
IoC：见汇总「Bricksforge（Patchstack 前 6 个源 IP）」。

### X-4. 【在野尝试升级 · 未进 KEV】Atlassian CVE-2026-21589（未认证任意文件读）
Previdian 10-12 更新：累计 **380** 次尝试、**58** 个源 IP、**19** 国、5 个传感器，最后观测 2026-10-12；日分布 10-06 6、10-07 107、10-08 108、10-09 86、10-10 54、10-11 15、10-12（截至抓取）4，**已明显回落**。CrowdSec：10-07 至 10-12 上午共 **89** 个独立 IP（66 个属 LeakIX 的 DigitalOcean 扫描集群），网络日均约 1,331 条信号，10-09 峰值 2,021；GitHub 公开 PoC 约 10 个，含一个 10-06 发布的批量扫描工具。两家都强调「尝试≠成功入侵」。**仍未进 KEV**。防御：升到固定版本；Jira＋Crowd 集成的环境要轮换 Crowd application 密码并核查 Jira 管理员账号。
地址：
- X 原帖（CrowdSec）：https://x.com/Crowd_Security/status/2109638259873616371
- X 原帖：https://x.com/BursaMatus/status/2109537162425405876
- X 原帖：https://x.com/ita_ipo/status/2109591989222064286
- 厂商公告：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
- 蜜罐 Previdian：https://previdian.com/CVE-2026-21589
- 文章 CrowdSec：https://www.crowdsec.net/vulntracking-report/cve-2026-21589-atlassian-jira-confluence-flaw-exploited
IoC：未见完整公开 IoC 表（CrowdSec／Previdian 的 IP 明细需要账号）；只能按路径穿越特征及 WEB-INF／crowd.properties 的异常读取来狩猎。

### X-5. 【在野尝试 · 未进 KEV】SonicWall SMA1000 CVE-2026-102255（CVSS 10，预认证 SSRF）
多方复述：补丁发布后观测到约 **135** 次利用尝试；加拿大网络安全中心已发 AV26-1017；SonicWall 方面**未确认**成功入侵。受影响 12.4.3-03526 及更早、12.5.0-02952 及更早（6210／7210／8200v）。仍未进 KEV。
地址：
- X 原帖：https://x.com/TweetThreatNews/status/2109705784535708125
- X 原帖：https://x.com/marcantonioglbl/status/2109652882488283597
- X 原帖（版本表）：https://x.com/Python_s_/status/2109599360635806091
- 厂商 SonicWall：https://www.sonicwall.com/support/notices/kA1VN000002QP3G0AW
- 政府 加拿大：https://www.cyber.gc.ca/en/alerts-advisories/sonicwall-security-advisory-av26-1017
- 文章：https://cyber.hendryadrian.com/article/1729/sonicwall-sma-1000-flaw-sees-135-exploitation-attempts-after-patch
IoC：未见公开网络 IoC。

### X-6. 【跟踪 · 有补丁】Citrix NetScaler CVE-2026-107406（SAML 内存溢出）续＋纠错
CTX697191：只有配置为 **SAML SP 或 IdP** 才受影响；已经打了 88779 补丁（14.1-73.41／13.1-64.28）的 IdP 设备**仍受 107406 影响**，需再升到 **14.1-73.46／13.1-64.29**（FIPS／NDcPP 同理）。CISA 告警页仍为 **10-09** 修订版。Shadowserver 语境称约 2.1 万个 NetScaler 指纹 IP 暴露（二手转述）。**纠错**：@emits_ca、@fernandokarl 把 **88779** 写成「新 0day」，实际 88779 早在 10-04 就进了 KEV、已逾期；今天的新动态是 107406。
地址：
- X 原帖：https://x.com/Sunil_kumawat17/status/2109489789947072758
- X 原帖（NCIIPC）：https://x.com/NCIIPC/status/2109507311551307970
- X 原帖：https://x.com/ALLITAustralia/status/2109771401716707597
- X 原帖（暴露面）：https://x.com/sinaowolabi76x/status/2109606581906161779
- X 原帖（误标示例）：https://x.com/emits_ca/status/2109701437026435351
- 厂商 CTX697191：https://support.citrix.com/external/article/CTX697191
- 政府告警：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- 文章：https://allitservices.com.au/netscaler-cve-2026-107406-october-2026/
IoC：107406 未见公开 IoC；88771／88779 的狩猎点沿用既有晚报。

### X-7. 【新 CVE／PoC 披露 · 未见确认在野】
- **GitLab CE/EE CVE-2026-97229**（CVSS 10，CI/CD 正则整数溢出→未认证 RCE；修复 19.2.8／19.3.4／19.4.2）：X https://x.com/Python_s_/status/2109698858469265719 ；厂商 https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/ ；CERT-EU https://www.cert.europa.eu/publications/security-advisories/2026-016/
- **Progress MarkLogic CVE-2026-85947**（CVSS 9.9，可创建持久管理员；修复 11.3.7／12.1.0）：X https://x.com/Python_s_/status/2109739411319443705 ；厂商 https://community.progress.com/s/article/Marklogic-Critical-Security-Alert-Bulletin-October-2026
- **Langflow CVE-2026-105697**（CVSS 9.9，添加 MCP stdio server 即可执行系统命令，默认 auto-login 下无需账号；修复 1.10.3）＋ **CVE-2026-10561**（修复 1.10.1，后续加固到 1.12.3）：X https://x.com/swif_ai/status/2109770816372326706 ；X https://x.com/Python_s_/status/2109641941373579288 ；GitHub https://github.com/langflow-ai/langflow/security/advisories/GHSA-w794-rj3p-xv45 ；GitHub https://github.com/langflow-ai/langflow/security/advisories/GHSA-8qpj-27x8-pwpq
- **Handlebars.js CVE-2026-106446**（CVSS 9.8，106445 的兄弟洞，AST 校验不完整；修复 4.7.10）：X https://x.com/Python_s_/status/2109514825541808206 ；GitHub https://github.com/handlebars-lang/handlebars.js/security/advisories/GHSA-8r5x-fm3f-whwj
- **macOS autofs CVE-2026-84568／84570 PoC 声称**：第三方 GitHub 仓库声称有实验室 PoC，**并非致谢研究者本人发布，ThreatWire 也未验证**——标 **UNCONFIRMED**。X https://x.com/ThreatWire_/status/2109682057710317947 ；文章 https://www.threatwire.tech/news/macos-autofs-path-traversal-is-cve-2026-84568
- **Rill OAuth CVE-2026-108718**（恶意 OAuth 客户端可拿到不过期令牌）：X https://x.com/TuringCyberObs/status/2109564589654548832 ；GitHub https://github.com/alan-turing-institute/cyber-threat-observatory/blob/main/reports/2026-10-11/TIER_2_CVE-2026-108718.md
- **Ghostscript CVE-2026-39919**（CVSS 9.8，JPEG 2000 解码堆溢出；受影响 9.21–10.07.1；Wordfence 称已在开启 -dSAFER 的线上 WordPress 上复现 RCE）：X https://x.com/DFIR_Radar/status/2109736402451943606 ；文章 https://www.wordfence.com/blog/2026/10/wordfence-argus-discovers-critical-vulnerability-in-ghostscript-the-program-that-turns-uploaded-pdfs-into-thumbnails-on-your-server/ （本轮被 JS 验证挡住，修复版本请以 Artifex 公告为准）
- **LMCache CVE-2026-105192**（CVSS 9.8，**仍无补丁**；CERT-UG 建议封 5555 端口）＋当日补丁清单：X https://x.com/CERT_UG/status/2109599976355414203
IoC：以上条目未见公开恶意 IoC。

### X-8. 【跟踪 · FortiMail／PaperCut／GlobalProtect】
- **FortiMail CVE-2026-104286**（在 KEV、已逾期）：原帖称修复 7.4.9／7.6.7／8.0.2（7.2 分支以厂商公告为准），临时缓解是关闭 IBE。X https://x.com/Python_s_/status/2109699133971845500 ；厂商 https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- **PaperCut**：watchTowr 10-09 公开的补丁绕过链今日在 X 上继续发酵，**无新厂商版本**。X https://x.com/DailyDarkWeb/status/2109742291212763468 ；研究 https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/
- **【UNCONFIRMED】Palo Alto GlobalProtect CVE-2026-0257 被 Qilin／Settra 勒索团伙利用**：仅见 Undercode 一源，厂商未确认。X https://x.com/UndercodeUpdate/status/2109518970189758479 ；文章 https://undercodetesting.com/palo-alto-globalprotect-cve-2026-0257-exploited-in-the-wild-by-qilin-and-settra-ransomware-gangs-video/
IoC：未见新增公开网络 IoC。

### X-9. 【噪声过滤】
收购 0day 的广告（@advance_sec0）、「写了 exploit 脚本」类自述（@Python_Papi）、阴谋论帖「一切联网设备都有 0day」、音乐／加密货币撞词帖、ExploitGrid 批量 lab 广告、兜售利用链讲解的帖子：**只作噪声，不采信**。
IoC：无。

### P-1. 【仍逾期高信号】
AA26-281A 五条（**今日新起逾期**）；Citrix **88771／88772／88779**；Fortinet **104286**；Zammad **102489／102490**；Cisco 76460／**76504**；Check Point 85102／93616；Arista 93952；F5 94127；JFrog 42016／42018；Zyxel 7273；Microsoft 81963／85880／65660；Google 87491／85046／58704；Acronis 87886；WSO2 5430；Adobe 71362；MikroTik 67279；WordPress 87902。
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

## 工具与 GitHub 发布

### 1. 【新 · DFIR】Collect-LinuxMemoryDump **v1.0.0**（2026-10-12）
Linux 内存取证采集脚本：集成 AVML／LiME／MAGNET DumpIt for Linux，并同时收集 Volatility 3 所需的内核镜像和映射布局。
- X 原帖：https://x.com/LETHAL_DFIR/status/2109516073725042706
- GitHub：https://github.com/LETHAL-FORENSICS/Collect-LinuxMemoryDump/releases/tag/v1.0.0

### 2. 【Blue Team】Zircolite **v4.5.0**（2026-10-10）
独立运行的 SIGMA 检测工具，可分析 EVTX、Auditd 和 Linux 版 Sysmon 日志。
- X 原帖：https://x.com/ksg93rd/status/2109646425730789754
- GitHub：https://github.com/wagga40/Zircolite/releases/tag/v4.5.0

### 3. 【Red Team 研究环境】Labyrinth（Ludus 上的 MaaS 靶场，@ipurple 分享，LWiS）
提供 CI/CD 驱动的载荷编译、混淆和 EDR 规避测试流水线，**仅供实验室研究**。GitHub API 查不到 release。
- X 原帖：https://x.com/ipurple/status/2109674794325008531
- GitHub：https://github.com/Whispergate/Labyrinth

### 4. 其他安全工具
- **Sara v1.4.0**（MikroTik RouterOS 安全审计工具，改用 RouterOS API，CVE 检索增强）：X https://x.com/ifritnoises/status/2109564038728536384 ；GitHub https://github.com/ifritnoises/sara/releases/tag/v1.4.0
- **Aqua CVE-Half-Day-Watcher**（追踪「已公开但尚未修补」的 CVE）：X https://x.com/gitrepos/status/2109509467192668268 ；GitHub https://github.com/Aqua-Nautilus/CVE-Half-Day-Watcher
- **Anthropic oss-scanner**（开源项目漏洞扫描，仓库里放 `.oss-scanner/` 威胁模型文件）：X https://x.com/ftnext/status/2109562719120810198 ；GitHub https://github.com/anthropics/oss-scanner
- **NVIDIA SkillSpector**（安装 Claude／Codex／MCP skills 前先扫描）：X https://x.com/0xal0ke/status/2109718220202500146 ；GitHub https://github.com/NVIDIA/SkillSpector
- **检测规则周报**（Detections Digest 10-05～10-12：8 个仓库 78 条规则变更，含 KerberLoss、BYOVD、提示词注入）：X https://x.com/DFIR_Radar/status/2109721471077736832 ；文章 https://detections-digest.rulecheck.io/p/detections-digest-20261012
- **AWS GuardDuty Extended Threat Detection** 新增 5 类指标（狩猎提示：EKS 节点上伪装成 kuboard-agent 的 frp）：X https://x.com/DFIR_Radar/status/2109781755230114040 ；厂商 https://aws.amazon.com/blogs/security/guardduty-extended-threat-detection-has-added-five-new-indicators-to-surface-attack-sequences/

### 5. 核心扫描器／C2：本日无显著更新
- emp3r0r 仍为 **v5.2.2**（10-11）：https://github.com/jm33-m0/emp3r0r/releases/tag/v5.2.2
- Sliver **v1.7.8**（10-03）：https://github.com/BishopFox/sliver/releases/tag/v1.7.8
- nuclei **v3.11.1**：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates **v10.5.0**（10-05）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.0

## APT / Malware 分析

### X-1. 【OT 事件 · 新】法国超市 Danfoss 冷链控制器遭远程操控
10-11 夜间，攻击者远程触发 Danfoss 冷链控制器的内置除霜功能，冷柜被迫持续除霜，部分被调到 50 °C 送风，大量生鲜和冷冻食品报废。BleepingComputer 报道 250～350 家门店受影响，Cooling Post 称约 500 家；受害方包括 Intermarché（150～200 家）、Coopérative U（不到 100 家）、Carrefour Market、Monoprix、Leclerc、Super U。Danfoss 声明：受影响的多为 **AK-SM800（2021 年 EOL）**、**AK-SC355（2016 年停产）** 以及固件过旧的 **AK-SM800A**；正协助客户升级固件、加强网络防护、撤掉直接的互联网暴露。Claroty Team82 此前披露过 StoreView 暴露问题和认证绕过 **CVE-2025-41450**（AK-SM 800A 修复 R4.3.1），但**是否就是本次入口尚未确认**。欧盟农业专员已公开谴责；巴黎检方已立案。**归因：未确认。** 防御：盘点暴露在公网的 StoreView／AK-SM 管理页；EOL 设备移出扁平网络；升到 R4.3.1 及以上；限制远程访问并改掉默认口令。
地址：
- X 原帖（BleepingComputer）：https://x.com/BleepinComputer/status/2109666378152050910
- X 原帖（cybermergemedia · 厂商声明）：https://x.com/cybermergemedia/status/2109745695708303867
- X 原帖（cybermergemedia · 设备型号）：https://x.com/cybermergemedia/status/2109741805663338801
- X 原帖（cybermergemedia · 门店规模）：https://x.com/cybermergemedia/status/2109639311620718624
- X 原帖（justabreach）：https://x.com/justabreach/status/2109582018417697125
- X 原帖（SirenesFR）：https://x.com/SirenesFR/status/2109598289192513959
- X 原帖（argevise · Le Figaro）：https://x.com/argevise/status/2109603780178133153
- X 原帖（CVE-2025-41450 语境）：https://x.com/JustACheckbox/status/2109654346770133174
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/
- 厂商声明（Cooling Post）：https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/
- 文章 Le Figaro：https://www.lefigaro.fr/societes/une-cyberattaque-a-touche-les-infrastructures-frigorifiques-de-centaines-de-supermarches-cooperative-u-et-intermarche-20261012
IoC：未见公开 IoC（狩猎方向：在扫描数据中搜 StoreView 页面标题）。

### X-2. 【新 · 有 IoC】Unit 42 · C2Agent（LLM 驱动的 Windows 恶意软件）
Go 编写；从 C2 拿到提示词后调用 LLM 平台执行任务，自身作为 MCP 客户端连接合法 MCP 服务（`mcp.firecrawl[.]dev`），并使用 C2 下发的 skills；会滥用受害者本机的 AI 编码工具（「living-off-the-AI」）。样本最早出现在 2026-09-10，29 天内迭代了 8 个大版本；两阶段投递：Go stager 下载伪装成 `copilot.txt` 的 PE，然后连回 C2 `agent.x90[.]dev`。
地址：
- X 原帖：https://x.com/Unit42_Intel/status/2109744924530737622
- GitHub IoC：https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-09-C2Agent-malware.txt
IoC：见汇总「C2Agent」。

### X-3. 【新 · 有 IoC】Elastic REF8801 · Apex Accelerator／Apex Arena（Web3 创业者定向）
伪装成 Web3 风投加速器，用免费 AI 额度引诱加密初创团队；npm 包 **`@apexacc/cli`**、**`@apexacc/audit`** 从发布起就是恶意的（不是被劫持）。会下载 macOS 后门 **CloudSyncD** 和 Windows 窃密链（Python→Go 加载器→窃密木马，经 Telegram 外传），把攻击者控制的 MCP 服务器持久注册进开发者的 AI 代理，截获 OpenRouter LLM 流量；所谓「安全审计」结果是硬编码伪造的；提交历史里有俄语注释。
地址：
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2109691248533454965
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2109726966509433329
- X 原帖（Nulltap_）：https://x.com/Nulltap_/status/2109748150848409730
- 文章 Elastic：https://www.elastic.co/security-labs/threat-command/apex-accelerator-malicious-npm-packages
IoC：见汇总「REF8801」。

### X-4. 【有 IoC】SectopRAT 两条投递链
- **The DFIR Report**：借 SonicWall、IBM、Blue Iris、ON1 的**合法签名 EXE** 侧加载，最终投放 SectopRAT（ArechClient2）。X https://x.com/TheDFIRReport/status/2109671796068716861
- **MetaDefender**：Bing 赞助广告推送假的 Claude Desktop 安装包，至少 29 个组织中招，投放 SectopRAT。X https://x.com/MetaDefenderCLD/status/2109618215353794910 ；文章 https://metadefender.com/blog/fake-claude-desktop-malware-sectoprat
IoC：DFIR Report 帖子正文未列 IoC（完整报告待发布）；MetaDefender 文章称附有 IoC（本轮抓取页面过大且主要靠脚本渲染，没有提取，请直接看原文）。

### X-5. 【有 IoC】SpiderLabs · PhantomPolia（ClickFix→Donut shellcode→Remus Stealer）
用 ClickFix 诱导用户执行 `update.ps1`，经 Donut shellcode 投放 Remus Stealer；在 Sepolia 测试网合约里藏配置（EtherHiding 语境）。10-10 的晚报只在周回顾里提过一句，今天是 SpiderLabs 完整报告。
地址：
- X 原帖：https://x.com/SpiderLabs/status/2109649861385609321
- 文章：https://www.levelblue.com/blogs/spiderlabs-blog/inside-phantompolia-remus-stealer-delivery-via-donut-shellcode-in-clickfix-campaign
IoC：见汇总「PhantomPolia」。

### X-6. 【有 IoC】AtlasRAT（Silver Fox 语境）＋ AvisLoader（Tox P2P C2）
- **AtlasRAT**：从 2026-03 至今，C2 协议改了三次（明文魔术字节→XOR→TLS），可能与 ValleyRAT 共用基础设施（Silver Fox）。@naumovax 补充了一批 **886 端口** C2。X https://x.com/DFIR_Radar/status/2109661011485839678 ；X https://x.com/naumovax/status/2109688108442955952 ；沙箱 https://tria.ge/260701-jvr59shv5k/
- **AvisLoader**（Varonis，BleepingComputer 赞助稿）：在暴露的 staging 服务器上被发现；用伪装 DocuSign 的 ClickFix 页面（Cloudflare Workers 托管）投递；C2 走 **Tox P2P**，不依赖固定域名，传统域名下架对它无效。X https://x.com/DFIR_Radar/status/2109676283336503583 ；X https://x.com/BleepinComputer/status/2109647777873768895 ；文章 https://www.bleepingcomputer.com/news/security/inside-avisloader-a-windows-malware-loader-built-to-resist-disruption/
- 相关：DocuSign 主题的 workers.dev 域名，Defender XDR TI 检索到约 230 个。X https://x.com/0x534c/status/2109681951208816884
IoC：AtlasRAT 见汇总；AvisLoader 未列网络 IoC，可狩猎 `auto.exe`、`hmn_hook.dll`、VLCAssistant 相关字样、被篡改的桌面／任务栏快捷方式及 .backup 文件、异常 Tox 流量。

### X-7. 【伊朗关联 · 续＋新变种】Blinder Tunnel／DarkBlinders／OilRig DNS
- **Unit 42 Blinder Tunnel**（已于 10-06 收录；今天 Unit 42 再推）：以迪拜机场编程测试为饵（Peaky Blinders 主题），用武器化的 `.csproj` 文件加 GitHub C2 攻击中东航空／电信关键基础设施。X https://x.com/Unit42_Intel/status/2109670686910300661 ；文章 https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/
- **Nextron**：发现新变种，基础设施有变化，GitHub 加载器发布 6 周后 VirusTotal 检出率仍然很低（细节在配图里）。X https://x.com/nextronresearch/status/2109543626552291785
- **DarkBlinders**（Dream Research Labs）：确认有政府云被入侵、基于 GitHub 的后门。X https://x.com/rst_cloud/status/2109613121568444783 ；文章 https://dreamgroup.com/blog/darkblinders-inside-an-active-espionage-campaign
- **OilRig VPN-over-DNS**（DomainTools）：X https://x.com/rst_cloud/status/2109605536396186016 ；文章 https://dti.domaintools.com/securitysnacks/it-always-comes-back-to-dns-iranian-vpn-over-dns-activity-in-the-2026-conflict
IoC：见汇总「Blinder Tunnel」；其余条目请看原文。

### X-8. 【其他 APT／犯罪生态】
- **Kimsuky · Operation GitPower**（针对乌克兰，Genians）：X https://x.com/rst_cloud/status/2109628295264288986 ；文章 https://www.genians.co.kr/blog/threat_intelligence/operation-gitpower
- **GhostAction 钓鱼续**（面向开源开发者，OpenSourceMalware）：X https://x.com/rst_cloud/status/2109620709890609172 ；文章 https://opensourcemalware.com/blog/ghostaction-phishing-campaign
- **Integrity Tech 续**（zerotsec：「攻击者即上市公司」；ThreatCluster IoC）：X https://x.com/zerotsec/status/2109468718552273213 ；文章 https://research.zerot-security.com/the-attacker-as-a-public-company/ ；X https://x.com/threatcluster/status/2109570527400509859
- **Midnight Mimosa 续**（zerotsec 追溯手机供应链；DFIR_Radar 提示狩猎 `com[.]android.system[.]lite` 静默开启无障碍和通知访问）：X https://x.com/zerotsec/status/2109468446849409211 ；文章 https://research.zerot-security.com/the-supply-chain-that-shipped-the-malware/ ；X https://x.com/DFIR_Radar/status/2109766666586411131 ；文章 https://www.helpnetsecurity.com/2026/10/12/midnight-mimosa-malware-cheap-android-phones/
- **Luna Moth／Silent Ransom Group（UNC3753）**：两人配合的电话诈骗（一人安抚受害者，另一人操作远控）。X https://x.com/DFIR_Radar/status/2109706295834030168 ；文章 https://www.infosecurity-magazine.com/news/luna-moth-leaks-ransomware-playbook/
- **Casbaneiro**（只在目标银行网站上才激活主 C2）：X https://x.com/DEVOTOMSOLUTION/status/2109614005916463261 ；文章 https://4tify.io/article/casbaneiro-banking-trojan-hides-its-c2-until-victims-visit-their-bank
- **RenEngine 加载器→Rust 剪贴板劫持**（BSC 智能合约控制）：X https://x.com/sourojit_dhua/status/2109586651802730666 ；X 长文 https://x.com/i/article/2109571337069133824
- **SilkBypass／BTMOB Android RAT 改名**（DuckDNS 经销商面板）：X https://x.com/akaclandestine/status/2109594675111743603
- **AI 代理自主入侵实录**（breachcache 公开 75 份攻击者服务器上的会话记录）：X https://x.com/breachcache/status/2109587441656938737 ；文章 https://breachcache.com/cases/hands-off-the-keyboard/
- **Ledger 硬件钱包被植入间谍芯片（官方确认）**：经东南亚经销商 CryptoBilis 卖出的部分设备被加装硬件植入物，用于盗取钱包资产。X https://x.com/BleepinComputer/status/2109682419095781631 ；文章 https://www.bleepingcomputer.com/news/security/ledger-confirms-hardware-wallet-spy-implant-behind-crypto-thefts/
- **ShinyHunters 第三次逮捕**（一名加拿大勒索谈判人；此前美国、约旦已各有逮捕）：X https://x.com/securityaffairs/status/2109758150031093943 ；文章 https://securityaffairs.com/200847/cyber-crime/shinyhunters-arrest-number-three-a-canadian-ransomware-negotiator.html
- **Talos：恶意软件给 AI 扫描器「留言」**（最强的那类约 35% 的情况下能把判定拉向良性）：X https://x.com/Nulltap_/status/2109665224102232307 ；文章 https://nulltap.sh/p/cisco-talos-malware-prompts-ai-triage/
- **Thelia 2.6 后台模板→服务器代码执行**（需要后台凭据，**尚无补丁**）：X https://x.com/Nulltap_/status/2109708777381650805 ；文章 https://nulltap.sh/p/thelia-back-office-server-code/
- **malwrhunterteam 样本狩猎**（opendir、Discord C2 RAT 的 ps1、「Grape」包源）：X https://x.com/malwrhunterteam/status/2109743567828611484 ；X https://x.com/malwrhunterteam/status/2109698401327624409 ；X https://x.com/malwrhunterteam/status/2109695872741372005
- **Vidar 新增 17 个域名**（Validin）：X https://x.com/orlof_v/status/2109725284287082961 ；GitHub https://raw.githubusercontent.com/orlofv/Adversarial-Infrastructure-IOC/e442ca14a22521fd678e7348b3f160f9bcf26370/Vidar/Indicators
- **【UNCONFIRMED】KPN 470 万客户数据被出售的声称**：X https://x.com/MonThreat/status/2109566486981300690 。另有 ThreatAtlas 刷屏的勒索泄露站批量受害者帖（N0n 多个港口运营方、thegentlemen 自称 KFC／MoneyGram 等）——**一律未验证，未收录逐条**。
- THN 周回顾：X https://x.com/TheHackersNews/status/2109665983187329450
IoC：见汇总相应小节。

## 地址／IoC 汇总

> 以下原样抄自原帖／原文（保留 defang）；不要直接访问。

### C2Agent（Unit 42，原样摘录）
- C2：`agent.x90[.]dev`；载荷：`hxxps[:]//agent.x90[.]dev/data/copilot.txt`
- 被调用的合法 MCP：`hxxps://mcp.firecrawl[.]dev/v2/mcp`
- SHA256（节选，完整 32 个见 GitHub）：
  - `35fc649622dfea297cb2a37ce2b6a9f89733546a22a5d13410c96ff904126e92`（v0, c2agent.exe.bin）
  - `83fe8207e2fc66df527efe0331109625d841e9904bd8b609c21c603777125e38`（v2, served as copilot.txt）
  - `6f4ddcab4cb6007d308a63f371406ea17177d7444696b1fb62e474eed3207b56`（v2, C:\Windows\1cna1b.exe）
  - `074147b2f1687571ba2f0ca51037ab2274381b0d3cd3fa5cc63cafd371eb9a1b`（v2, C:\Windows\r30xxsrlb.exe）
- 路径特征：`C:\Windows\` 下的随机短名 exe（如 `fdgw6.exe`、`tym9z.exe`、`81jqu.exe`）
- 完整清单：https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-09-C2Agent-malware.txt

### REF8801／Apex Accelerator（Elastic，原样摘录）
- npm：`@apexacc/cli`、`@apexacc/audit`
- 域名：`apexaccs[.]org`、`arena.apexaccs[.]org`、`token.apexaccs[.]org`、`vrf.apexaccs[.]org`、`arena.apexfdn[.]xyz`、`verify.apexfdn[.]xyz`、`arenapex[.]cloud`、`fdn4apex[.]com`、`main.router-apex[.]com`、`update.apex-arena-router[.]com`、`0auth-chromium[.]com`、`ccmihr[.]com`、`cloudmain365duo[.]top`、`ehegisnightmare[.]icu`
- SHA256：`985829083f3937df6c82419216f7697afae0caac8efca6257a756066fe2c0abb`（apex-windows-x64.exe）、`5ee7145061f05779f7f6f9b72e216713d17d53e183a92f408bfbbc44f2bfb95d`（apex-audit-windows-x64.exe）、`42a760b15fea7c9af718ee45386c1c3ea1bec9e30c95d16c287bcc8b2efdc72e`（apex-darwin-arm64）、`127ae4cad80b6605157ca2a1feada8a235e16aacc5d2119337a98115a4e13274`（apex-verify-darwin）、`68f5a00eafa8ecebf5d93328e0fec23b24d6f91808c8384db002946a13656c71`（CloudSyncD installer）
- 完整：https://www.elastic.co/security-labs/threat-command/apex-accelerator-malicious-npm-packages

### PhantomPolia（SpiderLabs，原样摘录）
- 域名：`voderlence[.]com`、`nightflamevortex[.]top`、`voidravenstorm[.]top`、`velnoderic[.]com`、`ironphantomcore[.]top`、`stormvenomforge[.]top`、`shadowemberstrike[.]top`
- ClickFix URL：`workeslexamp[.]com/check/update[.]ps1`、`cloudcheckic[.]com/check/update[.]ps1`、`spaceclou[.]com/check/update[.]ps1`、`littworkers[.]com/check/update[.]ps1`、`cokakina[.]com/check/update[.]ps1`、`citywebntw[.]com/Check/Update[.]ps1`、`littnetworks[.]com/check/update[.]ps1`
- SHA256：`05629F35DFE1409EA963C135581C228E3B71869B0707974244F6938AF635A70E`（audio-music.exe）、`8F4903B8B110EC1B9580A5A27BF49C3E4793538A863100559D085B7545FCDA25`（data_work.exe）、`f02e2fefd74c7268e3aced61017173fff92e2a1d0e7eaf7807189f371fbfcc1f`（download-package.exe）、`61def8b242913b520ec110458a416b02a6a38dc8765bc76bd571ee7ae8350aae`（AutoStart_33875e.au3）
- 完整：https://www.levelblue.com/blogs/spiderlabs-blog/inside-phantompolia-remus-stealer-delivery-via-donut-shellcode-in-clickfix-campaign

### AtlasRAT（@naumovax，原样）
- `16.162.200\.130:886`、`38.190.225\.103:886`、`82.23.246\.77:886`、`108.187.6\.27:886`、`124.156.171\.56:886`、`154.12.25\.55:886`（原帖称回复里还有更多）
- X：https://x.com/naumovax/status/2109688108442955952

### Bricksforge CVE-2026-85097（Patchstack 前 6 个源 IP，原样）
- `177.75.57.20`（EXPLORERNET，巴西）、`23.97.62.146`（Microsoft Azure）、`84.247.60.125`（HostRoyale）、`38.154.185.97`（B2 Net Solutions）、`150.109.16.166`（Tencent）、`153.75.90.146`（Cloudzy）
- 路径／文件：`/wp-json/bricksforge/v1/form_submit`（带 `temporaryFileUploads`）、AJAX `bricksforge_regenerate_nonce`、`/wp-content/uploads/bricksforge/tmp/`、`login_admin_*.php`
- 来源：https://patchstack.com/articles/critical-unauthenticated-arbitrary-file-upload-vulnerability-exploited-in-bricksforge-plugin/

### Blinder Tunnel（Unit 42，原样摘录；10-06 已收录，今日复核）
- 文件／SHA256：`DubaiAirport_Carrers_IT_Test.zip` `6e7d9b33f1e72ea1ede71373a604ecdb060dab7d42055179c1eede9ecd1fd239`；`FlightManager.csproj` `f5b12772db6817f7a765a6fe7565fd3d4f87edc28e42fe3ec0244a372a410fc9`；`RuntimeBroker.dll` `53f35e49eb9b271fd8cbcd3daacb525328dbf159a03dbd1c7adebe0363daa402`；`PsProxy.dll` `3fd810a3aa0039993393741b32287c367a9a5037a41e826906440887cdd3ed13`；`Blackwood.dll` `76273382e4252c1f60a2251141e108942494409c759358320735891762c0682e`
- IP：`91.107.156[.]29`、`65.109.214[.]145`、`38.180.136[.]127`、`87.248.129[.]239`
- 域名：`cloud.g-drive[.]cam`、`drivegoogel[.]cam`、`googeldrive[.]cam`、`googelmeet[.]online`、`meetonline[.]cam`、`portal.sharjahairport[.]cloud`、`asdfafadafg[.]online`、`ns1.soroshpasargad[.]com`
- 完整：https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/

### malwrhunterteam（原样）
- opendir：`http://load.tender-confirmation[.]com:8080/file/`、`http://download.tender-confirmation[.]com:8080/file/`
- Discord C2 RAT：`https://dicechecker[.]app/0b05d2aea7.ps1`
- 「Grape」包源：`https://uniways777[.]com/uniw/Grape.zip`、`https://vanclif[.]com/3585194/Grape.zip`、`https://huniways777[.]com/zz6/Grape.zip`、`https://ramcho777[.]com/ram/Grape.zip`
- 可疑域名：`ukembassyparagraph.enn[.]kr`（https://x.com/malwrhunterteam/status/2109702020701573331 ，未计入合并数）

### Vidar（@orlof_v／Validin，原样节选）
- `fh.33pedia[.]org`、`fh.4-win[.]org`、`fh.54toto[.]org`、`gp.4-win[.]org`、`kh.396zk[.]net`、`analytics.5tr[.]org`、`bi.5tr[.]org`、`client.5tr[.]org`
- 完整：https://raw.githubusercontent.com/orlofv/Adversarial-Infrastructure-IOC/e442ca14a22521fd678e7348b3f160f9bcf26370/Vidar/Indicators

### AA26-281A／Integrity Tech（续）
- ThreatCluster 新列：`halloween[.]checkapi[.]cf`、`xassxxdns[.]alitagotest[.]cf`（另有 4 个见原链接）— https://threatcluster.io/cluster/chinese-cyber-actors-exploit-vulnerabilities-via-integrity-t-f9f38bf5
- 既有：`98aiblog[.]com`、`hmbcloud[.]com`、`natcloudservice[.]com`、`149.28.132[.]137` 等（完整以通告和 STIX 为准）：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a

### AhsayCBS（沿用）
- JSP webshell；XMRig 伪装成 `edge.exe`；服务名 `MicrosoftEdgeUpdateSvc`；`cbssvcX64.exe` 异常子进程；TEMP 下 `WinRing0x64.sys`、`Taskgmr.ps1`
- 修复：v10 → **10.3.4.45**；v7／v8／v9 → **9.15.2.70**

### 无公开 IoC 的条目
- Danfoss 超市事件、Atlassian 21589、SonicWall 102255、Citrix 107406、Apple 86950、GitLab 97229、MarkLogic 85947、Langflow、Ledger 植入、ShinyHunters 逮捕：**未见公开 IoC**
- 勒索／泄露批量声称（KPN、ThreatAtlas 列表）：**UNCONFIRMED**，未见可核验的 IoC

## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/ （首页最新：Risky Bulletin「ShinyHunters suspects arrested in US and Jordan」；Risky Business #854）
- tl;dr sec 通讯：https://tldrsec.com/ （最新仍 **#349**，未见 #350）
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form

本窗口 LWiS 交叉要点（List 成员与扩展高价值源的 `from:` 批次）：
- @vxunderground：以色列政府域名缺少 SPF／DMARC，可被冒充且显示「未伪造」——https://x.com/vxunderground/status/2109733246015832082 ；https://x.com/vxunderground/status/2109749718636986390
- @Dinosn：日本卡拉 OK 厂商第一兴商泄露 870 万条记录——https://x.com/Dinosn/status/2109703962618196019 ；文章 https://www.scworld.com/brief/japanese-karaoke-maker-daiichi-kosho-reports-data-breach-affecting-8-7-million-records
- @thegrugq：agentic 黑客找的是「广度优先的配置错误」，而不是内存破坏 0day——https://x.com/thegrugq/status/2109510470663311676
- @fr0gger_：AI 用于逆向的讨论——https://x.com/fr0gger_/status/2109732040929362336
- @ipurple：Labyrinth MaaS 靶场（见工具节）
- @Unit42_Intel C2Agent／Blinder Tunnel；@nextronresearch 新变种；@TheDFIRReport 签名 EXE→SectopRAT；@SpiderLabs PhantomPolia；@HuntressLabs Ahsay hotfix 验证；@DFIR_Radar（AtlasRAT／AvisLoader／Apex／Ghostscript／Bricksforge／Luna Moth／Midnight Mimosa／检测规则周报／GuardDuty）；@Nulltap_（Apex／Thelia／Talos）；@cybermergemedia（Danfoss 三帖）；@BleepinComputer（Danfoss／Ledger／AvisLoader）；@securityaffairs（ShinyHunters）；@malwrhunterteam（opendir／RAT／Grape）
- 其余成员（_xpn_／C5pider／bohops／jm33_m0／rad9800／SinSinology／mrd0x 等）本窗口无显著安全长帖。

## 来源搜索 URL

- X A（relevancy）：`(CVE OR POC OR exploit OR 0day OR "zero-day" OR "zero day") -is:retweet lang:en` + 时间窗；`"CVE-2026" (exploited OR "in the wild" OR PoC OR patch OR advisory OR KEV) -is:retweet -is:reply`
- X B：`(github.com) (C2 OR "red team" OR nuclei OR Cobalt OR Sliver OR Mythic OR Havoc OR BOF OR EDR)`；`github.com ("new tool" OR released …)`；`url:github.com (YARA OR Sigma OR BOF OR EDR OR DFIR …)`
- X C：`("malware analysis" OR "threat report" OR "threat actor" OR ransomware OR APT) -is:retweet lang:en`；`(malware OR stealer OR loader OR backdoor OR botnet OR APT) (analysis OR campaign OR IOCs …) -from:ThreatAtlas`；`(IOC OR IOCs …) (C2 OR sha256 …)`
- X 定向：Citrix／NetScaler／107406／88779／21589／SonicWall／102255；Ahsay／PaperCut／AA26-281A／emp3r0r／86950／GhostAction／DarkSword／Flax Typhoon／FortiMail／104286；Danfoss／Intermarché／Bricksforge／85097／C2Agent／39919／LMCache；ShinyHunters 逮捕／Ledger 植入
- X LWiS：`from:h1 OR from:h2 …`（4 批）+ 时间窗（recency）
- KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA Citrix Alert：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- AA26-281A：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- Citrix CTX697191：https://support.citrix.com/external/article/CTX697191
- Previdian 21589：https://previdian.com/CVE-2026-21589
- Risky：https://risky.biz/
- tl;dr：https://tldrsec.com/
