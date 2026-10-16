# X 安全情报晚报 · 2026-10-13

> 搜集窗口：圣地亚哥时间 **2026-10-12 20:14 至 2026-10-13 20:13**（America/Santiago／UTC-3，约 24 小时，与昨晚窗口无缝衔接）。ISO／X 搜索：`start_time=2026-10-12T23:14:00Z`，`end_time=2026-10-13T23:13:00Z`。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all` + `get_posts_by_ids`，含 entities／note_tweet；t.co 一律用 entities.expanded_url / unwound_url 展开，本轮无需 curl 兜底）。**未开浏览器，未检查 @seogoogle4 浏览器登录状态。** A／B／C／定向检索用 relevancy；LWiS 用 `from:` recency：①优先批（chudyPB／vxunderground／Dinosn／watchtowrcyber／DFIR_Radar／TheDFIRReport／MsftSecIntel／Unit42_Intel／HuntressLabs／Synacktiv／nextronresearch／SpiderLabs／ipurple／thegrugq／fr0gger_ 等 39 个 List 成员 + BleepinComputer／TheHackersNews／securityaffairs／malwrhunterteam／Nulltap_／cybermergemedia／Volexity 等 10 个扩展源，按 4 个时段分段 + 翻页，覆盖全窗口）；②其余 **475 个 List 成员分 9 批全量覆盖**。本轮 **33 次 X 读取**（29 次搜索 + 4 次按 ID 取全文；未触限）。合并 **104** 条安全相关新帖（**A26／B2／C10／LWiS66**），全部与 seen_ids 去重（0 条重复）。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON `/workspace/enrich-2026-10-13/kev.json`；厂商／研究页存于 `/workspace/enrich-2026-10-13/`（Volexity 博文＋GitHub IoC、Rapid7／THN／BleepingComputer Ivanti、MSRC CVE-2026-96951 API、SANS ISC 10 月 PT、BleepingComputer PT、Unit 42 PuTTY／REDCap IoC、Threatray IoC、Rapid7 GitLab、THN SAP／LG／Docker／npm／Danfoss、BleepingComputer Ghostscript／TFG、Check Point LiteLLM、Zetter Trezor、SecurityWeek Ledger／Meta、DOJ OpenAI、CERT-FR CERTFR-2026-ALE-012、ASEC Funhouse、Risky／tl;dr 首页、GitHub releases：emp3r0r／Sliver／nuclei／nuclei-templates）。
> **CISA KEV：catalogVersion 2026.10.13／1741 条，Δ+2**（相对昨日 2026.10.08／1739；dateReleased 2026-10-13T19:10Z＝**10-13 16:10 圣地亚哥**）。**NEW：CVE-2026-104935（Ivanti Connect Secure）、CVE-2026-96951（Windows Shell）**——两条都只给 **3 天**期限（**due 2026-10-16**），且都标 `forensicTriage: Yes`（打补丁之外还要求按 BOD 26-04 做取证排查）。CISA 连续 4 天无新增后今日恢复。
> **due_today（10-13）：1 条**——Apple CVE-2026-86950（CoreGraphics 越界写，iOS／iPadOS／macOS）。**newly_overdue（10-12 到期）：0 条。** 仍逾期：AA26-281A 五条（10-11 到期，BIND／Struts／Strapi／ONLYOFFICE／ProFTPD）等。**upcoming 7 天：2 条**——即今日新增的 104935 与 96951（10-16）。CVE-2026-107406（Citrix）／21589（Atlassian）／102255（SonicWall）／105133·105134（Ahsay）／85097（Bricksforge）／97229（GitLab）**仍未进 KEV**。
> 抓取备注：BleepingComputer 个别页对 curl 返回 403（Adception 稿），改引 Push Security 原文；MSRC releaseNote 页为前端渲染，改用 MSRC API JSON 核对 96951；Ivanti hub 页为前端渲染，版本号以 Rapid7／THN 转述的厂商表为准。tl;dr sec 最新仍 **#349**；Risky Business 首页可见：Risky Bulletin「Authorities dismantle KillSec group, arrest members across Europe」「ShinyHunters suspects arrested in US and Jordan」、Between Two Nerds「The FBI and ShinyHunters are the same」；GitHub API 正常。
> 规则：每条带完整 https URL；X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标就写「未见公开 IoC」；不编造；**不转载利用代码／payload／PoC 步骤**（下文 Ivanti 只保留检测用的请求特征）；泄露／入侵／勒索声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【KEV 新增 · 紧急】Ivanti Connect Secure CVE-2026-104935**（认证绕过＋RCE，CVSS 8.6）：Volexity 披露未知团伙 **UTA0576** 自 **10-03** 起对当时全补丁设备（22.8R2.4）做三洞链（第三洞提权补丁仍在路上），无 webshell，再触发利用跑命令并清日志；ICT 完整性检查**看不到**内存补丁。今日进 KEV，联邦期限 **10-16**。
  X 原帖：https://x.com/Volexity/status/2110034602672709712
  研究：https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/
  厂商：https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935
- **【KEV 新增 · Patch Tuesday】Windows Shell CVE-2026-96951**（MotW 绕过／命令注入，CVSS 8.8，**exploited=Yes**）：10 月补丁日创纪录约 **1,411** 条；另有公开披露的 .NET／WDAC CVE-2026-108398（Project Zero）与 MessagePack-CSharp DoS CVE-2026-92707。KEV 期限同为 **10-16**。
  X 原帖：https://x.com/BleepinComputer/status/2110098145262899231
  MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-96951
  文章：https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2026-patch-tuesday-fixes-1-411-flaws-3-zero-days/
- **【KEV 到期今天】Apple CVE-2026-86950**（CoreGraphics）：联邦 BOD 期限就是今天，请确认已升到修复版本。
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **【OT／续】法国超市 Danfoss 冷链**：THN／CERT-FR 更新；CERTFR-2026-ALE-012 覆盖 AK-SM／AK-SC 及 Copeland／Dixell xweb；Synacktiv 重推 2023 年 SM800／SC355 认证绕过报告作为可能入口语境（**入口仍未官方确认**）。
  X 原帖：https://x.com/Synacktiv/status/2110035129565401214
  政府：https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/
- **【供应链／硬件】Ledger 植入续＋Trezor 争议**：Ledger 确认经授权经销商设备可经 eSIM／LTE 外传助记词；Joe Grand 称 8 月已向 Trezor 报过两台植入，与 Trezor「无证据」声明冲突。
  文章：https://www.securityweek.com/86-million-crypto-heist-linked-to-ledger-signer-hardware-implant/
  文章：https://www.zetter-zeroday.com/trezor-wallets-also-compromised-with-implants/
- **【恶意软件 · 新 IoC】Unit 42 假 PuTTY MSI（EtherHiding）**＋ **REDCap CVE-2026-90817→XMRig**；Threatray 本周 6 个新家族；SOCRadar **ICMacOS**；Push **Adception** 假 Claude ClickFix。
  GitHub IoC：https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-12-MSI-impersonating-PuTTY-delivers-malware.txt
- **【事件】OpenAI 工程师被捕**：沙特籍工程师 Abdulrahman Alfozan 被控在旧金山办公室内植入录音设备。
  政府：https://www.justice.gov/opa/pr/saudi-national-arrested-installing-surreptitious-audio-recording-device-openai
- **【统计】** X 合并 **104**（A26／B2／C10／LWiS66）；seen_ids **2818→2960**（本次写入 142 个见过／采纳 ID，含正文引用与同主题支撑帖）；KEV **2026.10.13／1741／Δ+2**；due_today **1**；newly_overdue **0**；upcoming **2**（10-16）；tl;dr #349。

## CVE / POC / 漏洞

### X-1. 【KEV 新进 · 紧急】Ivanti Connect Secure CVE-2026-104935（认证绕过＋RCE）＋未编号提权洞
Volexity（10-13）披露：未知团伙 **UTA0576** 自 **2026-10-03** 起对**当时全补丁**设备（22.8R2.4 Build 19097）使用三洞链——`welcome.cgi` 认证绕过（用 `X-DSCGI-PATH` 把头路由到受保护 CGI）、`wu.cgi` 竞态写文件→以 cgi-server 执行、再经 dsinvoked／内存补丁 `libdsplibs.so` 提权到 root。**认证绕过＋RCE 合编为 CVE-2026-104935（CVSS 8.6）**；提权洞**尚无 CVE／补丁「未来几周」**。攻击者**不落 webshell**：每条命令重跑整条链，经 HTTPS 回传结果；清 `/home/runtime/dlogs/debuglog` 与 `audit.log` 时间窗；ICT **检测不到**（只改内存）。后渗透重点：LDAP／LAPS／BitLocker 恢复密钥、Kerberoast 测试、密码喷洒、`/data/.icscap/` 下伪装成 `dsstatmond` 的抓包。CISA **同日**进 KEV，联邦期限 **2026-10-16**，并要求 forensic triage。修复版本（Rapid7 转述厂商表）：**22.8R2.5**；**25.1.1.2**（针对 25.1.1.1 及更早）；**25.1.3.0／25.1.3.1**（针对 25.1.2.x）；22.7.x 及以下不受影响。防御：紧急打补丁；**不要只看 ICT 绿勾**；查 `/tmp/` 下 `ml.py`／`rq5.py`／`mk.py`／`rr.py`／`sp_run.py`／`h.py` 及 `/data/.icscap/`；网络侧监控大量 `/dana-na/auth/url_default/welcome.cgi` 且 `X-DSCGI-PATH` 与 URL 不一致的请求；有内存镜像优先做内存取证。
地址：
- X 原帖（Volexity）：https://x.com/Volexity/status/2110034602672709712
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2110068357949247657
- X 原帖（watchTowr）：https://x.com/watchtowrcyber/status/2110039791416811785
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2110040542620909953
- X 原帖（BleepingComputer）：https://x.com/BleepinComputer/status/2110034348581753341
- X 原帖（THN）：https://x.com/TheHackersNews/status/2110063755329691674
- X 原帖（cybermergemedia）：https://x.com/cybermergemedia/status/2110044307839385912
- X 原帖（securityaffairs）：https://x.com/securityaffairs/status/2110071922520408151
- X 原帖（Dinosn／Rapid7）：https://x.com/Dinosn/status/2110067952728891668
- 研究 Volexity：https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/
- GitHub IoC（Volexity）：https://github.com/volexity/threat-intel/tree/main/2026/2026-10-13%20Ivanti
- 厂商公告：https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935
- Rapid7：https://www.rapid7.com/blog/post/etr-ivanti-connect-secure-zero-day-exploited-in-the-wild-cve-2026-104935/
- THN：https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html
- BleepingComputer：https://www.bleepingcomputer.com/news/security/ivanti-warns-of-connect-secure-zero-day-exploited-in-attacks/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-104935
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
IoC：见汇总「UTA0576／Ivanti」。

### X-2. 【KEV 新进 · Patch Tuesday】Windows Shell CVE-2026-96951（MotW 绕过）＋ 10 月约 1,411 条
微软 10 月补丁日发布约 **1,411** 条（BleepingComputer；部分二次源写 1,413／1,419，以 MSRC 发布说明为准），含 **70 Critical**；**1 条在野利用零日**＝**CVE-2026-96951**（Windows Shell 命令注入→绕过 Mark of the Web，CVSS 8.8，`exploited=Yes`，用户打开特制文件／附件即可）；**2 条公开披露零日**：CVE-2026-108398（.NET Framework，可绕 WDAC／受保护进程加载，Project Zero James Forshaw）、CVE-2026-92707（MessagePack-CSharp DoS）。CISA 把 96951 列入 KEV，期限 **10-16**。同日 Win11 24H2 Home／Pro 结束支持；微软开始为全部自有 CVE 发布 VEX。SANS ISC 还点名 CVE-2026-70571（Exchange RCE，攻击复杂度高）。防御：优先打含 96951 的累计更新并强制重启；邮件／IM 投递的文件强化 SmartScreen／Protected View；Exchange／.NET／WDAC 策略单独排期。
地址：
- X 原帖（BleepingComputer）：https://x.com/BleepinComputer/status/2110098145262899231
- X 原帖（MsftSecIntel）：https://x.com/MsftSecIntel/status/2110063798929273018
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2110121394742943851
- X 原帖（ai4cybersec 分诊）：https://x.com/ai4cybersec/status/2110138343816392830
- MSRC（96951）：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-96951
- MSRC 发布说明：https://msrc.microsoft.com/update-guide/releaseNote/2026-Oct
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2026-patch-tuesday-fixes-1-411-flaws-3-zero-days/
- SANS ISC：https://isc.sans.edu/diary/rss/33422
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-96951
IoC：未见公开恶意样本／网络 IoC（利用细节未公开）。

### X-3. 【KEV · 今日到期】Apple CVE-2026-86950
联邦 BOD 期限为 **2026-10-13**。CoreGraphics 越界写，定向攻击语境（PDF／零点击链相关）。请确认 iOS／iPadOS／macOS 已到 Apple 公告修复版本。
地址：
- Apple：https://support.apple.com/en-us/149226
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
IoC：未见公开 IoC。

### X-4. 【独立复现 · 未进 KEV】GitLab CVE-2026-97229（CVSS 10，CI/CD 正则整数溢出→未认证 RCE）
Rapid7 10-13 在官方未打补丁的 GitLab CE 19.4.1 镜像上独立复现任意代码执行（以 git 用户跑）；修复 **19.2.8／19.3.5／19.4.2**。前提：能向公开项目提交恶意 `.gitlab-ci.yml` 与 UTF-8 仓库路径——开放自注册的自建实例风险更高。**仍未进 KEV**；未见确认在野利用。防御：立即升级；临时限制匿名访问与不可信用户建／写公开项目。
地址：
- X 原帖：https://x.com/DailyDarkWeb/status/2110024862366580816
- X 原帖：https://x.com/TheHackersNews/status/2109928573540929895
- X 原帖：https://x.com/securityaffairs/status/2110005971556671870
- Rapid7：https://www.rapid7.com/blog/post/etr-cve-2026-97229-critical-unauthenticated-remote-code-execution-in-gitlab/
- 厂商：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/
- THN：https://thehackernews.com/2026/10/gitlab-patches-cvss-100-flaw-that-could.html
IoC：未见公开恶意 IoC。

### X-5. 【新披露 · 未见确认在野】SAP Cloud SDK for Python CVE-2026-89111（CVSS 10，OAuth2 SSRF 凭据窃取）
多租户场景下若攻击者控制租户子域名，可把 OAuth2 客户端凭据拐到攻击者服务器。Advisory 以 **0.45.2** 为修复；THN 复核称 **0.53.0～0.55.0** 在 Destination 模块路径上复现缺口，**0.55.1+** 已补。请升到 **≥0.55.1**（当日最新 0.58.4）。
地址：
- X 原帖：https://x.com/TheHackersNews/status/2110063119427108933
- X 原帖：https://x.com/BleepinComputer/status/2110005466772250885
- 文章 THN：https://thehackernews.com/2026/10/sap-discloses-critical-cvss-10-flaw-in.html
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-oauth2-ssrf-security-flaw/
IoC：未见公开恶意 IoC。

### X-6. 【新 · 有 IoC】Unit 42 · REDCap CVE-2026-90817→内存链 XMRig
未认证 POST 滥用公开 survey 端点，经临时 Blade webshell 与伪装 JPEG 的内存 cradle 投放 XMRig；矿池钱包可见至少 4 个活跃 worker。请 REDCap 管理员升到不受影响版本。
地址：
- X 原帖：https://x.com/Unit42_Intel/status/2109811397617992120
- GitHub IoC：https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-07-XMRig-campaign-through-CVE-2026-90817.txt
IoC：见汇总「REDCap／90817」。

### X-7. 【跟踪 · Ghostscript CVE-2026-39919】
Wordfence／BleepingComputer：JPEG 2000 解码堆溢出，受影响 **9.21–10.07.1**，修复 **10.08.0**（Artifex 9-08）；WordPress 开启 -dSAFER 的缩略图场景可被武器化。DEVOTOMSOLUTION 称**尚未见确认在野**。防御：升 Ghostscript／重建容器；临时禁 PDF 上传或关掉 ImageMagick PDF 渲染。
地址：
- X 原帖：https://x.com/BleepinComputer/status/2110122465477243354
- 文章：https://www.bleepingcomputer.com/news/security/ghostscript-flaw-lets-hackers-hijack-servers-via-pdf-uploads/
IoC：未见公开恶意 IoC。

### X-8. 【新披露 · 未见确认在野】LiteLLM CVE-2026-35029（CVSS 8.7）＋ HAProxy Data Plane API CVE-2026-109575（CVSS 9.8）
- **LiteLLM**：低权限账号可绕过 `/config/update` 管控，最终加载远程 Python 模块 RCE；升 **≥1.83.9**。Check Point 报告。X https://x.com/Python_s_/status/2110091306727043427 ；研究 https://research.checkpoint.com/2026/when-llm-gateways-go-wrong-findings-from-litellm/ ；GitHub https://github.com/BerriAI/litellm/security/advisories/GHSA-53mr-6c8q-9789
- **HAProxy Data Plane API**：特定 mTLS／监听器配置下认证可被绕过，拿到明文配置或整表替换；修到 **2.9.29／3.0.25／3.2.17／3.3.9／3.4.4**。X https://x.com/Python_s_/status/2109936842191536161 ；GitHub https://github.com/haproxytech/dataplaneapi/releases/tag/v3.4.4
IoC：以上未见公开恶意 IoC。

### X-9. 【其他高信号】
- **LG webOS 三洞本地网根接管**（无 CVE，TyphoonPWN 演示，未见在野）：X https://x.com/TheHackersNews/status/2109965012953678137 ；文章 https://thehackernews.com/2026/10/lg-smart-tvs-vulnerable-to-pre-auth.html
- **Docker Hub「GhostPat」**（账户转组织时 PAT 所有权错绑，已修，Docker 称未见利用）：X https://x.com/TheHackersNews/status/2110070030193041496 ；文章 https://thehackernews.com/2026/10/docker-fixes-critical-two-year-old-hub.html
- **npm Trusted Publishing**：未验证绑定现 **48h** 过期；Bloom 称曾可劫持 1,500+ 包／约 1,000 万下载。X https://x.com/TheHackersNews/status/2110044433936941556 ；文章 https://thehackernews.com/2026/10/github-tightens-npm-publishing-after.html
- **Adobe Acrobat／Reader CVE-2026-81983**（整数溢出→OOB 写，AI fuzz 发现）：X https://x.com/_r_netsec/status/2110016042802237443 ；文章 https://remedio.io/blog/cve-2026-81983-integer-overflow-vulnerability-enables-out-of-bounds-write-in-adobe-acrobat/
- **Project Zero · Samsung** 字幕／JPEG／DNG 三件 OOB：X https://x.com/ProjectZeroBugs/status/2109984193505808768 ；https://x.com/ProjectZeroBugs/status/2109984193501692235 ；https://x.com/ProjectZeroBugs/status/2109984193501602177
- **Akaunting CVE-2026-19198**（Fluid Attacks）：X https://x.com/fluidattacks/status/2110134233003913655 ；https://fluidattacks.com/advisories/badbo
- **Google DevSite Flask session pickle RCE**（已修，研究员 Simon Köck，$90k 赏金）：X https://x.com/Python_s_/status/2109887510230732920 ；https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce
- **Credential Guard／SFAPE CVE-2026-83498**（9 月补丁复盘，DFIR_Radar）：X https://x.com/DFIR_Radar/status/2109932966126440740
- **MyReport Updater** 未认证 gRPC→SYSTEM／RCE（Quarkslab，修程约 10-13）：X https://x.com/DFIR_Radar/status/2110071075262406860
- **Open VSX 扫描 fail-open**（已于 2 月修，今日复述）：X https://x.com/DFIR_Radar/status/2109842188473421912
- **OCI Identity Domain 权限绕过**（User Manager→管理员 API key，6 月补丁复盘）：X https://x.com/DFIR_Radar/status/2110114423495123310
- **Shopware HTML 媒体窃管理员 token**：X https://x.com/Nulltap_/status/2110102959237599470 ；https://nulltap.sh/p/shopware-media-upload-admin-token/
- **跟踪**：Citrix／NetScaler（含 88778 语境暴露面）、SonicWall 102255、Atlassian 21589、N-able N-central 86218（LOLRMM）、Bricksforge 85097——无本质新补丁，仅二次传播。

### X-10. 【噪声过滤】
音乐／加密货币撞词「zero-day」、ExploitGrid 分数广告、ThreatAtlas 批量勒索受害者刷屏、未验证的「GitLab 已在野」单源（aviatrixtrc）：**只作噪声，不采信**。
IoC：无。

### P-1. 【仍逾期高信号】
AA26-281A 五条；Citrix **88771／88772／88779**；Fortinet **104286**；Zammad **102489／102490**；Cisco 76460／**76504**；Check Point 85102／93616；Arista 93952；F5 94127；JFrog 42016／42018；Zyxel 7273；Microsoft 81963／85880／65660；Google 87491／85046／58704；Acronis 87886；WSO2 5430；Adobe 71362；MikroTik 67279；WordPress 87902；N-able **86218**。今日新增待 10-16：Ivanti **104935**、Windows **96951**。
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
## 工具与 GitHub 发布

### 1. 【新 · Red Team／研究】PentestAssistant（Amadeus IT Group）
面向授权白盒 Web 渗透的 LLM harness：静态分析＋动态利用＋可审计执行链。
- X 原帖：https://x.com/max2cbx/status/2109992549502873786
- GitHub：https://github.com/AmadeusITGroup/PentestAssistant

### 2. 【新 · 钓鱼演练】Psychopath Console
开源钓鱼模拟框架，声明仅用于授权红队与安全研究。
- X 原帖：https://x.com/Chadi0x/status/2110088921350631614
- GitHub：https://github.com/chadi0x/Psychopath

### 3. 【新 · 数据集】Cobalt Strike beacon corpus（56,843 条）
原始 beacon 与解析配置公开于 Hugging Face。
- X 原帖：https://x.com/ipurple/status/2110136408275075336
- 数据集：https://huggingface.co/datasets/fox-srt/cobaltstrike-beacon-corpus

### 4. 【新 · DFIR／蓝队】其他
- **Overlord RAT 逆向分析**（Go／HTTP2＋WebSocket C2／反射 DLL／IoC）：X https://x.com/ipurple/status/2110104550644359639 ；GitHub https://github.com/kaandemir993/Overlord-RAT-Reverse-Engineering-a-Go-Based-RAT-Injection-Keylogging-C2-Exfiltration-Analysis
- **AD Purple Team 实验室**（Kerberoasting／BloodHound／Wazuh 规则）：X https://x.com/ipurple/status/2110097909005828321 ；GitHub https://github.com/M-med/Active-Directory-Simulation-Attack-
- **Strands Box**（AI agent 沙箱＋Dogwood 语义策略）：X https://x.com/ipurple/status/2110089559119937734 ；GitHub https://github.com/strands-agents/box
- **aten**（AI 编码代理 intent＋action 遥测，@Antonlovesdnb）：X https://x.com/ipurple/status/2110043660570198460 ；GitHub https://github.com/Antonlovesdnb/aten
- **ADE Framework**（Detection Logic Bugs 形式化）：X https://x.com/ipurple/status/2110005133085913583 ；https://adeframework.org/
- **VirusTotal macOS Mirage** 沙箱（原生 Apple Silicon＋Sigma）：X https://x.com/DFIR_Radar/status/2109978698036240851
- **N-able N-central 入 LOLRMM**（服务器侧 CVE-2026-86218 已在 KEV）：X https://x.com/_josehelps/status/2109787952654197000 ；https://lolrmm.io/tools/n-able-n-central/
- **Apple XProtect 更新**（全 macOS）：X https://x.com/howardnoakley/status/2110114185749364787 ；http://eclecticlight.co/2026/10/13/apple-has-just-released-an-update-to-xprotect-for-all-macos-23/

### 5. 核心扫描器／C2：本日无显著更新
- emp3r0r 仍为 **v5.2.2**（10-11）：https://github.com/jm33-m0/emp3r0r/releases/tag/v5.2.2
- Sliver **v1.7.8**（10-03）：https://github.com/BishopFox/sliver/releases/tag/v1.7.8
- nuclei **v3.11.1**：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates **v10.5.0**（10-05）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.0
## APT / Malware 分析

### X-1. 【OT／续】法国超市 Danfoss 冷链＋CERT-FR＋Synacktiv 旧洞语境
10-11～12 夜间攻击者远程把数百家法国超市冷柜打进除霜循环（部分到 50 °C）；CERT-FR 发 **CERTFR-2026-ALE-012**（10-12 首版、10-13 修订），覆盖 **Danfoss AK-SM／AK-SC** 以及 **Copeland xweb／Dixell xweb**，要求断网或严格过滤。Synacktiv 重推 2023 年对 SM800／SC255／SC355 的认证绕过与 SM800A 多洞报告，称「可能与本次有关」——**官方仍未确认入口**。DFIR_Radar 汇总：Les Mousquetaires 称损失数千万欧元；SOCRadar 称法国 StoreView Shodan／Censys 暴露面分别约 2,898／881。防御：按 CERT-FR 处置；EOL 设备隔离；AK-SM 800A 升到最新 5.3.x；审计承包商远程通道；加装独立温感。
地址：
- X 原帖（Synacktiv）：https://x.com/Synacktiv/status/2110035129565401214
- X 原帖（THN）：https://x.com/TheHackersNews/status/2109939702371672284
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2110009747839807641
- X 原帖（securityaffairs）：https://x.com/securityaffairs/status/2109914750067097797
- 政府 CERT-FR：https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/
- 文章 THN：https://thehackernews.com/2026/10/attackers-heat-french-supermarket.html
- Synacktiv PDF（SM800／SC355）：https://www.synacktiv.com/sites/default/files/2023-10/synacktiv-danfoss-sm800-sc255-sc355-auth-bypass.pdf
- Synacktiv PDF（SM800A）：https://www.synacktiv.com/sites/default/files/2023-10/synacktiv-danfoss-sm800a-multiple-vulnerabilities.pdf
IoC：未见公开网络 IoC（狩猎：公网 StoreView／AK-SM 管理页）。

### X-2. 【新 · 有 IoC】Unit 42 · SEO 假 PuTTY MSI（EtherHiding C2）
针对搜「putty」的技术人员：SEO／广告导向 `puty[.]ink`，下载 Backblaze 上的恶意 MSI；落地合法签名 PuTTY 0.85 作诱饵，同时跑混淆 Node.js 加载器；C2 经以太坊主网合约 EtherHiding 解析，每 500ms 伪装静态资源轮询，可下发任意 JS（含近实时屏幕流）。
地址：
- X 原帖：https://x.com/Unit42_Intel/status/2110107318444499172
- GitHub IoC：https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-12-MSI-impersonating-PuTTY-delivers-malware.txt
IoC：见汇总「假 PuTTY／EtherHiding」。

### X-3. 【新 · 有 IoC】ICMacOS（Icarus macOS）· GlowComa MaaS
SOCRadar：9 月起销售的 macOS 窃密木马，数周内进化为带 LaunchAgent＋WebSocket 的持久 RAT；ClickFix 终端诱饵；CIS 地理锁定；订阅 $699／周起。狩猎 `com.apple.systemupdater.plist`、`escapeai[.]live`。
地址：
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2109917825972257270
- 文章 SOCRadar：https://socradar.io/blog/icmacos-infostealer-rat/
IoC：见汇总「ICMacOS」。

### X-4. 【新 · 有 IoC】Push Security「Adception」· 假 Claude ClickFix（macOS）
Google Ads 把落地写成 Bing，经 `bing.com/ck/a`＋南美被入侵零售站跳到 `claude-desk-code[.]com`；页面显示合法 `claude.ai/install.sh`，Copy 按钮却写入解码后拉 `lake-90[.]com` 并 `| zsh` 的命令。工具链内部称 **AcSig**；最终载荷未确认。
地址：
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2110027528911962222
- 研究 Push：https://pushsecurity.com/blog/adception-malvertising-another-search-engines-search-results
IoC：见汇总「Adception／假 Claude」。

### X-5. 【有 IoC】ThreatrayTuesday · 6 个新家族（IronRAT／DPPBotRAT／TakerStealer／NoobSaibotRAT／YamiStealer／AudaxStealer）
HTTP 轮询 C++ RAT（Chromium ABE 窃密＋WMI 持久）等；完整 SHA256／C2 见 GitHub。
地址：
- X 原帖：https://x.com/ThreatrayLabs/status/2109978253418991708
- GitHub IoC：https://github.com/threatray/threat-research/blob/main/ThreatrayTuesday/iocs-2026-10-13.md
IoC：见汇总「Threatray 2026-10-13」。

### X-6. 【有 IoC】malwrhunterteam／vxunderground · POS 假更新＋Azure C2＋欧洲油气 Rust 样本（细节有限）
- 假「Aloha／POS Terminal Maintenance」站：`alohapos-update[.]com` 等；vxunderground 指 ToastPOS 相关团伙改版。
- 微软证书签名样本，C2 走 Azure：`asiioasdjasiojasodijasa.eastus.cloudapp.azure.com`，UA 伪装 CrowdStrike CsAgent。
- vxunderground：针对欧洲 **Oil & Gas** 的高强度反仿真 Rust 样本，公开细节极少、检出近零——**无完整公开 IoC 表**。
- 另：假交易平台 zip（密码 `github`）→信息窃密，C2 `91.99.119.25`，Steam／Telegram 外联。
地址：
- X 原帖：https://x.com/malwrhunterteam/status/2110094925232537816
- X 原帖：https://x.com/vxunderground/status/2110122224975859943
- X 原帖：https://x.com/malwrhunterteam/status/2110054829842219012
- X 原帖：https://x.com/vxunderground/status/2109915310203511280
- X 原帖：https://x.com/vxunderground/status/2110040350966292574
- X 原帖：https://x.com/vxunderground/status/2109829651715477681
IoC：见汇总「POS／Azure C2／交易平台窃密」。

### X-7. 【有 IoC】其他恶意软件／活动
- **ClingSTUN**（FortiGuard／PolySwarm 语境，IoT 代理后门，滥用公共 STUN）：X https://x.com/DFIR_Radar/status/2110100118217031736
- **假期主题钓鱼→ConnectWise ScreenConnect**：域名 `theinvitationestateco[.]vu`；X https://x.com/DFIR_Radar/status/2110055081831764285
- **Edge 翻译扩展（ID ifbamokmfkcnhbpeokkochdpecopfccd）劫持**：`clicktranslator[.]com` 过期被接管，87k 安装／99 天外传 URL＋联盟劫持——以 DFIR_Radar 长帖为准（未找到独立厂商博文，标为 X 一手）。X https://x.com/DFIR_Radar/status/2110095467040194649
- **DarkBlinders／StarkMeet**（政府云，GitHub C2，UNC5795／Dust Specter 重叠语境）：X https://x.com/LandscapeThreat/status/2109939957804482713
- **Kimsuky · Funhouse 勒索**（恶意 HWP 简历→Quasar）：X https://x.com/rst_cloud/status/2109937991892324655 ；ASEC https://asec.ahnlab.com/ko/95774/
- **Donot C2**：`45.61.137.107`／`sacksolution.info`；X https://x.com/phatomcandle/status/2110022765004603787
- **PoeLLM／Canto Incognito**（Lumen，>3,400 台 AI 相关暴露面；C2 藏在 GitHub 诗里）：X https://x.com/Python_s_/status/2110052117071188216 ；https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware ；https://github.com/blacklotuslabs/IOCs/blob/main/PoeLLM_IOCs.txt
- **Talos · 台湾研究活动假邀请→Google 登录中继**：X https://x.com/Nulltap_/status/2109789559282450627 ；https://nulltap.sh/p/taiwan-event-google-phishing/
- **Coruna／DarkSword iOS 利用套件**面向企业机队、源码泄露：X https://x.com/DFIR_Radar/status/2110129421709427046
- **Windows Fibers** 被 Earth Ammit／Kurma 用于 CoffeeLoader／ACR Stealer：X https://x.com/ipurple/status/2109980515071651885

### X-8. 【事件／供应链／物理】
- **OpenAI 录音设备案**：沙特籍工程师 Abdulrahman Alfozan（2025-07 入职）被控 9-28 前后在高管会议室电视 USB 口植入加密录音器，10-09 被捕。X https://x.com/KimZetter/status/2110118573729616155 ；DOJ https://www.justice.gov/opa/pr/saudi-national-arrested-installing-surreptitious-audio-recording-device-openai ；BleepingComputer https://x.com/BleepinComputer/status/2110136831106760874
- **Ledger 硬件植入续**：eSIM／LTE 读取设置屏 24 词；Genuine Check 可能漏检；与约 $86M 盗窃关联报道。X https://x.com/TheHackersNews/status/2110077713956622765 ；https://thehackernews.com/2026/10/ledger-finds-unauthorized-hardware.html ；https://www.securityweek.com/86-million-crypto-heist-linked-to-ledger-signer-hardware-implant/
- **Trezor**：CCO 称「无证据被植入」但缩减授权经销商；Kim Zetter／Joe Grand 称 8 月已报两台 One／Model T 植入（非授权渠道）。X https://x.com/KimZetter/status/2110107981832708465 ；https://www.zetter-zeroday.com/trezor-wallets-also-compromised-with-implants/
- **Meta GitHub**：约 1,500 人（多为员工）个人数据因员工凭据失窃被访问；非 Meta 产品洞。X https://x.com/Dinosn/status/2110058224162685096 ；https://www.securityweek.com/meta-says-hackers-took-code-personal-data-of-1500-in-github-breach/
- **TFG London**：社工窃员工凭据，影响 Hobbs／Whistles／Phase Eight；客户数据暴露未确认。X https://x.com/BleepinComputer/status/2110049073830998482 ；https://www.bleepingcomputer.com/news/security/tfg-london-cyberattack-disrupts-systems-at-hobbs-and-whistles-retailers/
- **Blueberry Pediatrics**：经 Metabase 洞窃健康数据。X https://x.com/Dinosn/status/2109989635115917434 ；https://cyberinsider.com/blueberry-pediatrics-discloses-health-data-theft-through-metabase-flaw/
- **UK Housing Ombudsman**「安全事件」调查中。X https://x.com/BleepinComputer/status/2110073099274031124
- **Anthropic**：小模型数月内或可在 IoT 自复制实验警告（非已发生的事件）。X https://x.com/TheHackersNews/status/2110074668854263959
IoC：硬件／企业内部案多见「未见公开网络 IoC」；恶意软件见对应汇总。
## 地址／IoC 汇总

> 以下原样抄自原帖／原文（保留 defang）；不要直接访问。

### UTA0576／Ivanti Connect Secure（Volexity，原样）
- IP：`108.165.147[.]64`（Evoxt VPS；OpenVPN 观测 9-30～10-07）
- 狩猎路径／文件：`/tmp/ml.py`、`/tmp/rq5.py`、`/tmp/mk.py`、`/tmp/rr.py`、`/tmp/sp_run.py`、`/tmp/h.py`（亦见 `/data/.icscap/h.py`）；`/data/.icscap/dsstatmond`；`/data/.icscap/cap*`；`/home/runtime/tmp/ics-root-run-inband-*.pl`
- 请求特征：大量 `POST/GET /dana-na/auth/url_default/welcome.cgi`，且请求头 `X-DSCGI-PATH` 指向 `/home/webserver/htdocs/dana/fb/smb/wu.cgi` 或 `/home/runtime/tmp/<MD5>`（与 URL 路径不一致）
- CSV：https://github.com/volexity/threat-intel/blob/main/2026/2026-10-13%20Ivanti/iocs.csv
- 完整分析：https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/

### 假 PuTTY／EtherHiding（Unit 42，原样摘录）
- 域名：`puty[.]ink`、`presanis[.]com`、`putredirhelps[.]online`；Backblaze `*.s3.us-east-005.backblazeb2[.]com`
- 合约：`0x89F5664d6fD8d990FA04F53253Be4855ed481A74`；selector `0x7d434425`；campaign arg `0x4e7b6e29ab5f4c01e3b9f86a3558a2d99ae0cbaf`；build ID `1835187f-121a-4103-832f-24649a461cac`
- SHA256：`b59d9c911f11ddbe5ac0cd7e2e6e311093a44ac31453b5cab801c31f6a170750`（MSI）、`71049ac72adad0c0c4c7a0763a4a9c806ba0687e7146237174d6252b45fb39db`（cmd）、`d5197f58b4c2d760f61f7cf0ff9e2a78fcaade12a05057d6e33e8e84c3be084d`（js）、`cbc1f7909cb2460e4fb371f3159ea00a167eb4feefea2011f1f6eae3a3449ec6`（ini）
- 路径：`%LOCALAPPDATA%\idejDHjFnNXb\`、`...\vXA8Jj\node.exe`
- 完整：https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-12-MSI-impersonating-PuTTY-delivers-malware.txt

### REDCap CVE-2026-90817／XMRig（Unit 42，原样）
- IP：`202.61.130[.]221`
- SHA256：`39a435123dc1fffd499aa2acf11ef46e3ee2e805bf137811af0c2c5b12546920`
- 路径：`/var/www/html/redcap/temp/cache/d3f11fc8ee9c2d986425eff26ecace5b4004eb8e.bladec`；`/var/tmp/.syslog-a224be51/xmrig.tar.gz`
- 钱包：`87maYgt7bMvgDxQsBavYNVDr6BQgJNaaRKXg2yBh8A3GLVoizCq9eeycBT7v6kdnm8f41Vfz84x6XLeEUJDRqvYbSrhvzTw`
- 矿池：`auto.c3pool[.]org`
- 完整：https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-07-XMRig-campaign-through-CVE-2026-90817.txt

### ICMacOS（SOCRadar／DFIR_Radar，原样）
- 域名：`escapeai[.]live`、`mikoblico[.]xyz`
- IP：`85.137.253[.]61`、`45.13.186[.]247`
- URL：`hxxps[://]escapeai[.]live/icmacos_run_v2[.]command`、`.../ICMacOs?arch={arm64|amd64}`、`.../payload[.]py`、`.../upload`；`wss[://]escapeai[.]live/ws?...`
- 持久化：`~/Library/LaunchAgents/com.apple.systemupdater.plist`；日志 `/tmp/.update-helper.log`
- 文章：https://socradar.io/blog/icmacos-infostealer-rat/

### Adception／假 Claude（Push／DFIR_Radar，原样）
- 域名：`claude-desk-code[.]com`、`lake-90[.]com`、`homeopatiaalemana[.]com`（跳板）
- 文章：https://pushsecurity.com/blog/adception-malvertising-another-search-engines-search-results

### Threatray 2026-10-13（原样）
- IronRAT：`47a9e572…6beb30` → `rat[.]ironrat.de5.net`
- DPPBotRAT：`a31fdd57…60576a` → Discord webhook（见原文）
- TakerStealer：`61f41806…21b5c5` → Discord webhook
- NoobSaibotRAT：`63a9dd2e…c5d27e` → `192[.]52.242.79`
- YamiStealer：`bf282293…8fa9d8` → `hxxps://txrouteuifbfewfubewfbhgrabbing[.]xyz/api/log`
- AudaxStealer：`0e146631…711fc2b`
- 完整表：https://github.com/threatray/threat-research/blob/main/ThreatrayTuesday/iocs-2026-10-13.md

### POS／Azure C2／交易平台窃密（malwrhunterteam／vxunderground，原样）
- POS：`alohapos-update[.]com`、`instantposupdate[.]com`、`posupdate[.]zip`
- Azure C2：`asiioasdjasiojasodijasa.eastus.cloudapp[.]azure.com`（UA 伪装 `CsAgent/7.04.18110.0`）
- 面板：`http://176.123.11[.]84:3000/`（「AVM PRO」）
- C2 域名：`dont-lose-ur-shit.whitelist[.]run`
- 交易平台窃密：`91.99.119[.]25`；`steamcommunity[.]com/profiles/76561198622044578`；`t[.]me/scii0n`

### ScreenConnect 假期钓鱼（DFIR_Radar，原样）
- 域名：`theinvitationestateco[.]vu`
- IP：`104.21.73[.]121`、`172.67.162[.]73`
- SHA256：`f3aab811ae8163e09db40db201facc7e189d1a1b161be265202ca54b39b5e6cc`（ScreenConnect.ClientSetup.exe）；MD5 `739a54032b89432bb4c9c33969f6b383`

### 翻译扩展 clicktranslator（DFIR_Radar，原样）
- Edge ID：`ifbamokmfkcnhbpeokkochdpecopfccd`（v0.4.2）
- 域名：`clicktranslator[.]com`、`api.clicktranslator[.]com`、`advertisingshubb[.]com`、`meetlookup[.]com`、`provenpixel[.]com`、`848trk[.]com`；CDN `1752680588.rsc.cdn77[.]org`
- SHA256：`d4a2d0404a9197d2491b7412d2872e647a06e7c6ed482ba064be8c64df9f10fc`（background.js）
- Analytics：`G-C2X1K7ZKNP`；`yk_tag=444`

### PoeLLM（Lumen／Black Lotus，原样节选）
- C2 IP（截至 10-07）：`92.119.164[.]50`、`103.249.201[.]108`、`178.128.14[.]204`
- SHA256：`6fab94577364beec314afae3b082dd680933f08a8349b9f35b92667e8231b501`
- 完整：https://github.com/blacklotuslabs/IOCs/blob/main/PoeLLM_IOCs.txt

### Donot（原样）
- `45[.]61[.]137[.]107`；`sacksolution[.]info`

### Mirage 示例窃密样本（DFIR_Radar／VT，原样节选）
- SHA256：`be77bca22f078d57058535ddcf26a39a752a8df030392cb45ba6a60e06651878`；二阶段 `f7dcdc4167ec267aef007f9d5f98e9e0314185e5355effd3e304b6fa686ea84c`
- C2：`109.238.87[.]111`、`193.178.159[.]129`

### AA26-281A／Ahsay／Bricksforge（续，无本质新增）
- 沿用 10-12 晚报；Ahsay 修复仍为 **10.3.4.45／9.15.2.70**

### 无公开 IoC 的条目
- Patch Tuesday 96951／108398／92707、GitLab 97229、SAP 89111、Ghostscript 39919、LiteLLM／HAProxy、LG webOS、Docker GhostPat、npm Trusted Publishing、Apple 86950、OpenAI 录音案、Meta GitHub、TFG London、Ledger／Trezor 硬件案（无网络 IoC）、vxunderground 欧洲油气 Rust 样本（无公开哈希）、Danfoss 超市事件：**未见公开网络 IoC** 或仅有厂商／研究页内指标
## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/ （首页可见：Risky Bulletin「Authorities dismantle KillSec group, arrest members across Europe」「ShinyHunters suspects arrested in US and Jordan」；Between Two Nerds「The FBI and ShinyHunters are the same」；Soap Box：HD Moore 谈 OT）
- tl;dr sec 通讯：https://tldrsec.com/ （最新仍 **#349**，未见 #350）
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form

本窗口 LWiS 交叉要点（优先批分段＋其余 9 批 List 成员）：
- @Volexity／@watchtowrcyber／@DFIR_Radar／@cybermergemedia／@BleepinComputer／@TheHackersNews／@MsftSecIntel：Ivanti 104935＋Patch Tuesday（见 CVE 节）
- @Unit42_Intel：假 PuTTY EtherHiding；REDCap 90817
- @Synacktiv：Danfoss 2023 认证绕过 PDF 重推
- @vxunderground：欧洲油气反仿真样本；ToastPOS／假交易平台窃密
- @malwrhunterteam：POS 假更新、Azure C2、AVM PRO 面板
- @ThreatrayLabs：六家族 IoC
- @KimZetter：OpenAI 录音案、Ledger／Trezor 植入
- @ipurple：Pentest／Overlord／AD lab／Strands／aten／Fibers／beacon corpus
- @thegrugq：挪威门禁码梗（中国车存演习影像语境）
- @Nulltap_：Shopware、Talos 台湾钓鱼、PQC 证书测试床
- @howardnoakley：XProtect 更新；@ProjectZeroBugs：Samsung 三洞；@max2cbx：PentestAssistant
- 其余多数成员本窗口无显著安全长帖（大量为回复／活动／非安全内容，已过滤）。
## 来源搜索 URL

- X A（relevancy）：`(CVE OR POC OR exploit OR 0day OR "zero-day" OR "zero day") -is:retweet lang:en` + 时间窗；`"CVE-2026" (exploited OR "in the wild" OR PoC OR patch OR advisory OR KEV) -is:retweet -is:reply`
- X B：`github.com (C2 OR "red team" OR nuclei OR Sliver OR Mythic OR Havoc OR BOF OR EDR OR YARA OR Sigma OR DFIR)`；`url:github.com ("new tool" OR released OR release OR open-source OR PoC …)`
- X C：`("malware analysis" OR "threat report" OR "threat actor") -is:retweet lang:en`；`(malware OR stealer OR loader OR backdoor OR botnet OR ransomware) (analysis OR campaign OR IOCs …) -from:ThreatAtlas`；`(IOC OR IOCs) (C2 OR sha256 …)`
- X 定向：Ivanti／Volexity／UTA0576／104935；Patch Tuesday／96951／108398；Citrix／21589／SonicWall／GitLab／97229／Ghostscript／39919；Danfoss／Trezor／Ledger／Ahsay／Bricksforge
- X LWiS：优先批 `from:`（4 时段分段＋翻页）＋其余成员 9 批 `from:` + 时间窗（recency）
- KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- Volexity Ivanti：https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/
- Ivanti 公告：https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935
- MSRC 96951：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-96951
- CERT-FR ALE-012：https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/
- AA26-281A：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- Risky：https://risky.biz/
- tl;dr：https://tldrsec.com/
