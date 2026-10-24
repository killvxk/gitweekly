# X 安全情报晚报 · 2026-10-20

> 搜集窗口：圣地亚哥时间 **2026-10-19 20:10 至 2026-10-20 20:10**（America/Santiago／UTC-3，名义 24 小时，接昨晚窗口）。X 搜索参数：`start_time=2026-10-19T23:10:00Z`，`end_time=2026-10-20T23:10:00Z`。实际抓到的帖子时间从 **10-19 22:04** 到 **10-20 20:09**（UTC-3），**实际有效覆盖约 22 小时**：**10-19 20:10–22:04 这约 2 小时没有抓到任何帖子**（宽泛查询被更晚的帖子占满 25 条上限，夜间切片最早只到 22:04／01:17）。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`，Latest／recency 排序）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** 本轮接口**没有回传 entities**，t.co 一律用 curl 跟随 HTTP 跳转展开（373 个短链全部展开；纯图片／视频 t.co 不列）。A 类（CVE／0day）跑了原始、翻页、在野三种查询并做 **4 个时段切片**；B 类（GitHub 红队／C2）原始＋去噪两次；C 类（威胁报告）原始、IoC、两个时段切片共 4 次；LWiS List 500 成员分 10 段 `from:` 批次全量查；核心媒体／厂商账号两页、IoC 猎人账号两页；专题 3 次（Coruna／DarkSword／GhostAction／OVHcloud；PAN-OS／Plex2Shell／SiteGuard；Cisco SEG／Zimbra／SafePay／eMudhra／Oracle EBS／FortiSIEM／HOOKEDGE）。共 **30 次有效 X 读取，0 次 429**。
> **覆盖说明（重要）**：每次查询最多 25 条。宽泛查询只覆盖窗口最后 1～3 小时（A1 到 19:03 起、C1 到 17:07 起，UTC-3），靠切片补到 **01:17–04:58、06:30–11:29、11:31–15:55、17:24–20:02** 等段，中间仍有空档。**10-19 20:10–22:04 无覆盖；22:04–01:17 只靠 LWiS 批次覆盖，关键词流偏薄。** 专题「Coruna／DarkSword」查询被西班牙城市 A Coruña 与「Bloodhound Gang」等噪声淹没（T1 基本作废），延续线索主要从其它批次与公开备援补。
> 窗口内去重后 **632** 条帖子（与 seen_ids 4713 条**零重叠**），关键词粗筛（剔除纯回复、闲聊、广告、营销号重复帖、"backdoor" 政治隐喻等噪声）得 **370** 条安全相关新帖：**A152／B25／C78／LWiS25／核心＋IoC 猎人45／专题45**（多查询重叠按最先命中批次归类）。下文实际引用约 120 条。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON（`/workspace/enrich-2026-10-20/kev.json`）；CISA 公告「Adds Six KEV」与 **#StopRansomware: SafePay（AA26-293A）**；php.net 新闻归档；watchTowr FAQ、BleepingComputer（PHP／OVHcloud）；THN（eMudhra、OVHcloud、FortiSIEM、Cairn AI 代理）；Symantec（security.com）Swallowtail／APT28；Horizon3（Oracle EBS 101767、FortiSIEM 106173）；Censys（Plex2Shell）；Rapid7（NetScaler 链）；OVHcloud GitHub 公告 GHSA-862f-55f5-vmvw；The Record（SafePay）；Cisco PSIRT（SEG 76519）；CERT Polska／Microsoft（Zimbra 73570，核对确认为 8 月旧闻）；Nikkei／ITmedia／Security NEXT（NEC）；BlockBeats（SlowMist DarkSword 报告摘要，SlowMist 原文被 Cloudflare 拦截）。GitHub API 查了 nuclei／nuclei-templates／Sliver／emp3r0r／BloodHound／NetExec／Mythic／impacket／Havoc：**本窗口没有任何新 release**（BloodHound v9.9.0-rc1 是昨天 15:28 发的，昨日已列）。
> **CISA KEV：catalogVersion 2026.10.20／1754 条，Δ+6**（`dateReleased` 2026-10-20 16:00 UTC-3，**连续三天不变后今天更新**）。新增：Plex **CVE-2026-96652／96654／96655/96656**（Plex2Shell 链）、SiteGuard **CVE-2026-106931**、Siemens Software Center **CVE-2026-110936**——**昨天列为「在野但未进 KEV」的三条线索今天全部入列**。**due_today（10-20）：0 条。newly_overdue（10-19 到期）：2 条**：BeyondTrust **CVE-2026-102764**、Fortinet **CVE-2025-61624**。已逾期：Atlassian 21589（10-18）；AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322（10-17）；Ivanti 104935、Windows 96951（10-16）；Apple 86950（10-13）。**upcoming：10-23** SiteGuard 106931、Plex 96656、Plex 96654；**11-03** Plex 96652、Plex 96655、Siemens 110936。**仍未进 KEV、值得盯的**：PHP 109618／109619（未修、未见在野）、Rank Math PRO 111862、Redis 25243（加拿大网络中心称已被利用）、Oracle EBS 101767／101809、FortiSIEM 106173。
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接作狩猎用途。泄露、入侵类声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【未修 · 全网级】PHP 核心两个严重漏洞 CVE-2026-109618／109619 提前泄露，官方 10-21 14:00 UTC（11:00 UTC-3）发紧急安全版**：php.net 官方只说「两个严重漏洞，CVSS v4.0 各 9.2，细节与受影响版本随补丁公布」，并保留「细节公开或出现在野就提前发」的权利。watchTowr 确认「是真的」、评 CVSS 10、称两者都是 RCE 且影响 PHP 5／6／7／8，并称已复现 109618 但在补丁前不公开细节；**目前未见在野**。@k_firsov 有个叫 php2shell 的工具声称能打 WordPress／MediaWiki／phpBB／Magento／Laravel 等（UNCONFIRMED，不转载）。全球约三分之一 PHP 站仍跑 5／7，补丁窗口会很紧张。
- **【在野 · 勒索/供应链主题日】CISA KEV 一次加 6 条，昨天三条「在野未进 KEV」线索今天全入列**：Plex2Shell 四件（Plex<1.43.3.10861，SSRF→盗 owner token→写 Codecs 目录执行，公开 PoC 次日即被用来投 XMRig＋住宅代理，Censys 见约 32.4 万台暴露、约 30% 仍脆弱、3 天内补丁率 <2%）、SiteGuard 106931（OS 命令注入）、Siemens Software Center 110936（DLL 侧加载，ClickFix/ROMULUS 投 RAT）。
- **【在野 · 供应链】OVHcloud 官方 CLI 的 GitHub 发行物被挂马（v0.11.0–v0.15.0）**：开发者 GitHub 账号被盗（半年前装了恶意 VS Code 插件 `color-picker-universal 2.8.91`，关联 GlassWorm），10-19 12:47–14:21 UTC 替换了 5 个版本的 mac/Linux/Windows 二进制与 checksums，约 94 分钟、约 250 次下载。恶意 go 构建会偷 VS Code/Cursor/Claude/AWS/GCP/Azure/K8s/SSH/Terraform 等密钥，经 Solana RPC 外带、上传到 `45.32.148[.]174`。源码与 CI/CD 未受影响；干净版 v0.16.0。装过的按已泄露处理、换机轮换全部密钥。
- **【在野 · APT】Symantec：APT28／Swallowtail（GRU）用 HOOKEDGE 后门打两个北约成员国的海军造船厂、军用航发厂、执法机关**：恶意 Word 宏→用隐藏单像素 Edge 窗口当 HTTP 客户端从 webhook.site 取任务→推 SSH 私钥建持久反向隧道（C2 `185.82.218[.]119`）、PowerShell 环回抓 NTLM、新反射加载器 `ld.exe`（运行时才给密钥解密）。造船厂潜伏至少两个月。
- **【在野 · 勒索】FBI/CISA/德英联合 #StopRansomware: SafePay（AA26-293A）**：自 2024-08 起 600+ 受害者，靠暴破/钓鱼/边缘设备漏洞（CVE-2020-3259、2023-20269、2023-27532、2024-40711、2024-40766）入场，LOLBins 横移、电话施压。附完整 IoC（IP、文件、哈希）。
- **【信任链】eMudhra 8 个中间 CA 私钥被攻破**：研究者 10-17 报告，Mozilla/Chrome 数小时内拦截；私钥熵极低（有的值 <256，甚至「4」），可伪造任意站点证书。Chrome（CRLSet，按公钥、含 Sectigo 交叉签名副本）、Firefox 158.0.1（OneCRL，CVE-2026-113470）、Go 1.27.3/1.26.10（CVE-2026-111943）、NSS、certifi、Homebrew 已处置；浏览器用户风险低，自管信任库/IoT/Go 程序需手动更新。
- **【在野 · 续报】PAN-OS GlobalProtect CVE-2026-0257 被 Qilin/INC 勒索利用**（Unit 42，10-19 更新：从 VPN 转打 vCenter/ESXi、离线导域控凭据，昨日已列）；**NetScaler CVE-2026-88771＋88779 链**（Rapid7 10-20 更新完整 IoC：WHIPSHOT/SLAPSHOT、.slap 框架、跨重启 root、vCenter 侦察）。
- **【新披露 · 高危】Oracle 10 月 CPU**：Horizon3 的 **Oracle EBS CVE-2026-101767**（未认证 SQLi→RCE，TCF servlet，CVSS 9.8，附 IoC）、**CVE-2026-101809（CVSS 10）**；**Fortinet FortiSIEM CVE-2026-106173**（未认证 gRPC 路径穿越→任意写→RCE，CVSS 9.4，Horizon3 PoC 公开，未进 KEV）。
- **【AI 攻防】** THN/NorForge：中文圈犯罪者用开源 AI 代理框架 **Cairn** 自主攻击 1200+ 站、打下 100+ 公司（Deere/SharkNinja/Cummins），单次约 $5、约 10% 成功率、平均 23 小时拿下；暴露的面板还泄露受害者密钥。日本：NEC 委托先 9 月下旬遭攻击、正规账号被盗用加密顾客服务器并泄露 3 家顾客数据；官房长官称「是否用 AI、是否外国主体介入仍待查」。
- **【工具/研究】** 本窗口监控的 C2/红队框架**无新 release**；X 上流传的有 ipurple「从零写 BOF」、Sentinel（Windows 用户态 EDR）、OpenBSD 37 年老内核洞利用（califio）、EAC_rollback（驱动回滚 PoC）、FortiSIEM/Dokploy/Laravel/Windows Defender 等 PoC（仅链接作狩猎）。

## CVE / POC / 漏洞

### 1. PHP 核心 · CVE-2026-109618／109619（RCE）· 提前泄露，10-21 14:00 UTC 发补丁（未修 / 未见在野）
PHP 安全团队 10-20 预告：10-21 14:00 UTC（11:00 UTC-3）发安全版，修两个严重漏洞，**官方评 CVSS v4.0 各 9.2**，不提前披露细节/受影响版本/修复版本，并保留「细节公开或出现在野就提前发」的权利。消息源于一条已删的 Hacker News 帖（petecooper），随后 watchTowr 公开确认：两者为 RCE、**按其评估 CVSS 10、影响 PHP 5/6/7/8**，已复现 109618 但补丁前不公开细节，**未观察到在野**。cyb3rops 提醒约三分之一 PHP 站仍跑 PHP 5/7，迁移压力大，并发布 process-watcher 帮助在补丁前监控 PHP 子进程。防御：清点所有生产 PHP，备好快速升级流程，补丁一出立即升级；不要听信未验证的 php2shell 演示。
- X 原帖：
  - https://x.com/cyb3rops/status/2112616479061667936
  - https://x.com/watchtowrcyber/status/2112611507749982605
  - https://x.com/BleepinComputer/status/2112650802703827190
  - https://x.com/Frichette_n/status/2112660164541100417
  - https://x.com/he_malware/status/2112661667972780337
  - https://x.com/watchtowrcyber/status/2112679565705314585
- 厂商公告：https://www.php.net/archive/2026.php#2026-10-20-1
- 文章：
  - https://watchtowr.com/intelligence/php-cve-2026-109618-faq/
  - https://www.bleepingcomputer.com/news/security/php-warns-admins-of-two-critical-flaws-emergency-patches-coming-tomorrow/
- 地址／IoC：未见公开 IoC（未修、未见在野）。

### 2. Plex Media Server · Plex2Shell 链 CVE-2026-96652/96654/96655/96656 · 今日入 KEV、在野
四个漏洞串成未认证 RCE：未认证 `/player/timeline` 触发 SSRF → `searchOne` 强制走环回拿到 owner 管理 token → 用 token 设 x264 转码选项，转码一段构造视频把 .so 写进 Plex `Codecs` 目录并被无签名校验加载。单独评分不高（96656=7.2、96654=6.5、96652/96655=4.3），串起来是未认证 RCE。研究者 code-zm 10-16 公开 Plex2Shell write-up，**次日（10-17）蜜罐即中招**，投 XMRig 与住宅代理。**Plex 1.43.3.10861（8-4）已修**；CISA 今日列入 KEV（96656/96654 due 10-23，96652/96655 due 11-03）。Censys：约 32.4 万台暴露、约 30% 仍脆弱、公开 PoC 后 3 天内补丁率 <2%。暴露的按失陷处理：净重装、清 `Codecs`、查 `Preferences.xml` 异常转码选项、登出所有设备、改密码。
- X 原帖：
  - https://x.com/censysio/status/2112553312515940528
  - https://x.com/BigVikDada/status/2112666193316172007
  - https://x.com/phantmradar/status/2112641203368042522
  - https://x.com/HashgraphOnline/status/2112642520018719020
  - https://x.com/Boluyung/status/2112671302020649263
- 厂商公告：
  - https://forums.plex.tv/t/important-security-update-for-plex-media-server-v1-43-2-and-earlier/942319
  - https://www.cisa.gov/news-events/alerts/2026/10/20/cisa-adds-six-known-exploited-vulnerabilities-catalog
- 文章：
  - https://censys.com/advisory/cve-2026-96652-cve-2026-96654-cve-2026-96655-cve-2026-96656/
  - https://thehackernews.com/2026/10/hackers-exploit-plex2shell-flaws-to.html
- 地址／IoC：进程名 `mylovelyminer`／`myawesomeproxy`、矿池 `ota.proxystream[.]st`（10-19 已列）；本轮无新 IoC。

### 3. SiteGuard Server Edition · CVE-2026-106931（OS 命令注入）· 今日入 KEV、在野
EG Secure 的 WAF 产品，默认开启的统计功能导致 OS 命令注入；影响 Ver8.00 Update5 之前（续 10-18/10-19 JPCERT 注意唤起）。CISA 今日列入 KEV，**due 10-23**。CVSS 厂商按本地/低权限前提打 8.5。修补或关闭统计功能，**修补前先在 Web 管理界面取「诊断信息」留证**。
- X 原帖：
  - https://x.com/thecircuitry_/status/2112641225538814232
  - https://x.com/notCVE/status/2112639780219494572
  - https://x.com/ADKCyber/status/2112673937309987101
  - https://x.com/issoh_co_jp/status/2112646231839109523
- 厂商公告：
  - https://www.eg-secure.co.jp/siteguard/news/alert-202610-1
  - https://www.cisa.gov/news-events/alerts/2026/10/20/cisa-adds-six-known-exploited-vulnerabilities-catalog
- 地址／IoC：未见公开 IoC。

### 4. Siemens Software Center · CVE-2026-110936（DLL 侧加载）· 今日入 KEV、在野（ClickFix/ROMULUS）
正版签名 Software Center 配恶意 DLL，经 ClickFix（含冒充 ChatGPT Custom GPT 的话术）诱导运行，侧加载后投 RAT、回连攻击者 C2（续 10-19）。修到 **4.0.9.8**。CISA 今日列入 KEV，**due 11-03**。aviatrixtrc 补充：ROMULUS 是 MaaS 平台，Legion Loader 回连取模块化载荷。
- X 原帖：
  - https://x.com/vuln_tracker/status/2112535290925453369
  - https://x.com/drerdalozkaya/status/2112542273544093707
  - https://x.com/aviatrixtrc/status/2112596637293883558
  - https://x.com/aviatrixtrc/status/2112598120919966138
  - https://x.com/TheHackersNews/status/2112442133579964651
- 厂商公告：
  - https://productcert.siemens.com/productcert/html/ssa-580366.html
  - https://www.cisa.gov/news-events/alerts/2026/10/20/cisa-adds-six-known-exploited-vulnerabilities-catalog
- 文章：https://www.securityweek.com/siemens-software-center-vulnerability-exploited-in-clickfix-malware-attacks/
- 地址／IoC（Siemens，10-19 已列）：`96.62.218[.]59`、`wizardexpensive[.]com`；SHA-256 `f4d7c5321bb0d1bda439304a753bcf9b467b98ca53c7e9493b9c2c3451092e4a`（AllMyBasic.msi）、`3fdcc7d7d049a89711fb31fb236940a1c5a09d899143ffd20c3c41fb1f2cf491`（archive.dll）。本轮无新 IoC。

### 5. Oracle 10 月 CPU · EBS CVE-2026-101767（未认证 SQLi→RCE，CVSS 9.8）＋CVE-2026-101809（CVSS 10）
Horizon3 公开 **CVE-2026-101767**：Oracle E-Business Suite 的 TCF servlet（`/OA_HTML/AppsTCFServer`，`oracle.apps.fnd.tcf.SocketServer`，默认 EBS URL 防火墙放行）存在未认证 SQL 注入，可以 APPS 库用户执行 SQL、进而以 EBS 应用账号执行系统命令；影响 12.2.3–12.2.15，10-20 的 10 月 CPU 已修。另有 SecAlerts 标出 **CVE-2026-101809（CVSS 10，未认证 RCE）**。缓解：从 URL 防火墙白名单移除 `/OA_HTML/AppsTCFServer`，限制 Web 层网络可达，监控库活动。
- X 原帖：
  - https://x.com/Horizon3Attack/status/2112651247362658611
  - https://x.com/Horizon3ai/status/2112657110404100454
  - https://x.com/SecAlertsCo/status/2112666199284687302
- 厂商/文章：
  - https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/
  - https://secalerts.co/vulnerability/CVE-2026-101809?utm_campaign=x
- 地址／IoC（Horizon3，狩猎用）：对 `/OA_HTML/AppsTCFServer` 实例化 `oracle.apps.jtf.gantt.server.GanttDataServer` 的未认证 POST、随后库侧活动；`$APPLPTMP` 异常文件；`oracle` 账号经 Concurrent Manager 派生 `/bin/sh`。

### 6. Fortinet FortiSIEM · CVE-2026-106173（未认证 gRPC 路径穿越→任意写→RCE，CVSS 9.4，未进 KEV）
phQueryMaster gRPC 服务（端口 27918）无需登录/证书即可连接；Horizon3 在 query-id 头塞空字节截断服务端文件名，覆写 cron 每 60 秒跑的 redis 健康检查脚本达成 RCE。Fortinet 10-13 发公告，Horizon3 已公开 PoC 与深度分析；在野状态未知，**未进 KEV**。尽快升级 FortiSIEM。
- X 原帖：
  - https://x.com/TheHackersNews/status/2112569443423486115
  - https://x.com/Horizon3Attack/status/2112527399778750836
  - https://x.com/_skinnyguinea/status/2112550274325746090
  - https://x.com/SecAlertsCo/status/2112543512910585883
  - https://x.com/hongzh0/status/2112588945569783987
- 文章：
  - https://horizon3.ai/attack-research/cve-2026-106173-deep-dive-fortisiem-grpc-path-traversal-file-write-rce/
  - https://thehackernews.com/2026/10/critical-fortisiem-flaw-gets-public.html
- 地址／IoC：未见公开 IoC（PoC 覆写 redis 健康检查脚本，可据此猎异常写入）。

### 7. Cisco Secure Email Gateway · CVE-2026-76519（AMP 任意写→root，CVSS 9.8，KEV 已逾期）
续报：AMP 文件信誉服务开启且 Content Scanner Tools <25.3.0.5525 时，未认证攻击者发带构造附件的邮件即可任意写文件、以 root 执行命令（10-14 公告、已在 KEV，due 10-17 已逾期）。修复：`contentscannerupdate` 升 CST 到 25.3.0.5525+（无需重启/升级），AsyncOS 升 15.5.5-014 或 16.5.0-780；用 `grep "System Security" system_logs` 查痕。
- X 原帖：
  - https://x.com/ThreatHunter_AI/status/2112680661525868806
  - https://x.com/RedDotSecNews/status/2112574742016196828
  - https://x.com/KaitanSecurity/status/2112514177591906514
- 厂商公告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp
- 地址／IoC（Cisco）：`grep "System Security" system_logs` 出现「Suspected compromise」类告警即需排查；无网络 IoC 公布。

### 8. 其它新披露／单源声称的漏洞
- **Drupal 核心 CVE-2026-108097／108099（Field UI/Entity List RCE）**：FORTBRIDGE 公开 108097 完整 PoC，至少一条利用路径无需登录；升 11.4.10／11.3.19／10.6.19（续报）。
  - X：https://x.com/ifahimulhssn/status/2112405776405086231 ；https://x.com/2Workly/status/2112431301240447148
  - 文章：https://www.securityweek.com/drupal-warns-of-fast-exploitation-risk-for-critical-core-rce-flaw/
- **Redis CVE-2026-25243（RESTORE，需认证，CVSSv4 7.7）**：加拿大网络中心（Cyber Centre）称已在野利用、有公开 exploit；修补或 ACL 禁 RESTORE。（注：与 10-19 报告里单源声称的 Redis 66373 为不同编号，这条有官方来源。）
  - X：https://x.com/DuckButTurttle/status/2112443060588257423 ；https://x.com/moton/status/2112424871108255861
  - 厂商公告：https://www.cyber.gc.ca/en/alerts-advisories/redis-security-advisory-av26-423
- **Apache Answer CVE-2026-90910（CVSS 9.8，未认证绕过）**、**Apache Camel CVE-2026-78162（CVSS 10，反序列化）**：无在野证据，升级即可。
  - X：https://x.com/SecAlertsCo/status/2112422443981693173 ；https://x.com/PrecursorUK/status/2112546245365682519
  - 厂商/文章：https://www.precursorintelligence.com/what-is/CVE-2026-78162
- **Microsoft 10 月补丁日**：1,411 修复、含一个在野利用的 Shell/Mark-of-the-Web 绕过 **CVE-2026-96951**（今年第 3 个被利用的 Shell 洞，KEV due 10-16 已逾期）。
  - X：https://x.com/EllerionS/status/2112545235838370101 ；https://x.com/blackbeltsecure/status/2112555740158177680
- **GNU inetutils-telnetd CVE-2026-24061（未认证 root 绕过，NEW_ENVIRON 注入）**：研究博客公开（sh3ll_c0d3）。
  - X：https://x.com/sh3ll_c0d3/status/2112604920239014155
  - 文章：https://sh3llc0d3.com/blog/gnu-inetutils-telnetd-remote-authentication-bypass-zero-day-unauthenticated-root-access-via-new_environ-and-crlf-injection/
- **Netcore NBR200V2 多个命令注入/溢出（CVE-2026-94095/94096/94101，CVSS 9.9，公开 exploit、厂商无响应）**、**OrdaSoft Joomla Gallery CVE-2026-88855（认证 SQLi）**、**TP-Link Tapo C320WS CVE-2026-105810（认证 RCE，首发 CVE）**。
  - X：https://x.com/HugoValters/status/2112451502337884637 ；https://x.com/m0ud4/status/2112594551387173047
- **DFIR_Radar 全盘未修 IoT/企业软件（无 CVE/无补丁）**：Parasoft CTP 10.7.5 未认证 RCE 链（CVSS 9.8）、Edimax BR-6478AC、TRENDnet TV-IP302PI 命令注入——均 seclists Full Disclosure。
  - X：https://x.com/DFIR_Radar/status/2112635452972789862 ；https://x.com/DFIR_Radar/status/2112665769360175159
  - 文章：https://seclists.org/fulldisclosure/2026/Oct/31
- 地址／IoC：以上均未见公开 IoC（PoC 仓库仅作狩猎）。

### 9. 已在 KEV 的在野漏洞续报
- **PAN-OS GlobalProtect CVE-2026-0257**（KEV，5-29 收录）：Qilin/INC 勒索继续利用、转打 vCenter/ESXi 离线导域控凭据（Unit 42 10-19 更新，昨日已详列）。
  - X：https://x.com/TheHackersNews/status/2112567982727840054 ；https://x.com/Dinosn/status/2112604255156625811
  - 文章：https://www.theregister.com/cyber-crime/2026/10/20/palo-altos-firewall-os-has-been-under-attack-from-multiple-ransomware-groups-since-june/
- **BeyondTrust Remote Support CVE-2026-102764**（KEV，10-19 到期今起逾期）：Mandiant/Google 归因中国关联 ARMORY CASTLE（原 UNC5221），8-29 起利用、投 SAWFLY webshell 与 BARECLAW 隧道（昨日已详列）。
  - X：https://x.com/CyberScoopNews/status/2112590924790342048 ；https://x.com/xbhaveshverma/status/2112657612080902253
  - 文章：https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust/
- **Citrix NetScaler CVE-2026-88771＋88779**（均在 KEV）：Rapid7 10-20 更新完整 IoC——WHIPSHOT/SLAPSHOT，log-poisoning＋SAML 崩溃链，经崩溃处理器跨重启以 root 执行，`chmod 6555 /bin/sh`，`.slap` 框架、Perl/Python 隧道、FreeBSD Go 侦察器扫 vCenter/LDAP，导出 ns.conf 与密钥。见地址表。
  - X：https://x.com/rst_cloud/status/2112544951451988322 ；https://x.com/TachyonSecurit/status/2112644372567388389
  - 文章：https://www.rapid7.com/blog/post/ra-netscaler-intrusions-chaining-cve-2026-88771-and-cve-2026-88779
- 地址／IoC：见地址表（NetScaler 条目）。

## 工具与 GitHub 发布

> **本窗口监控的 C2/红队框架均无新 release**（GitHub API 核对：nuclei v3.11.1[8-8]、nuclei-templates v10.5.0[10-5]、Sliver v1.7.8[10-3]、emp3r0r v5.3.0[10-16]、BloodHound v9.9.0-rc1[昨天 10-19 15:28]、NetExec v1.5.1[2-23]、Mythic v3.4.0.5、impacket 0.13.1[5-19]；Havoc 无 release）。以下为 X 上流传的工具/研究，多为文章或既有仓库。

- **ipurple「从零用 C 写 Beacon Object File（BOF）」技术文**：防守侧可据以理解 BOF 行为特征。
  - X：https://x.com/ipurple/status/2112639616780226774
  - 文章：https://by7e.dev/blog/bof-from-scratch-in-c
- **Sentinel · Windows 用户态 EDR（ETW 遥测、行为关联、MITRE ATT&CK）**：
  - X：https://x.com/ptlegion/status/2112553775374139618
  - GitHub：https://github.com/psihijatrija/Sentinel
- **Skarvel（twelvesec）· 单条 IoC 驱动的跨仓库猎取工具**：从一个 IoC 找遍公开仓库的分支/PR，挖确认载荷里的新 IoC 并持续追踪。
  - X：https://x.com/ipurple/status/2112574665009082854
  - GitHub：https://github.com/twelvesec/Skarvel
- **califio「Big Fish：利用 OpenBSD 37 年老内核漏洞」**（研究/PoC，仅链接）：
  - X：https://x.com/ksg93rd/status/2112554450284126620
  - GitHub：https://github.com/califio/publications/tree/main/MADBugs/openbsd
- **EAC_rollback（驱动回滚 PoC）**：区分「验证谁签了驱动」与「验证特权服务该加载哪个驱动」。
  - X：https://x.com/AzizWho/status/2112678220055163324
  - GitHub：https://github.com/oh-az/EAC_rollback
- **ProjectDiscovery neo**（subfinder/httpx/nuclei/katana/naabu/dnsx/interactsh/cvemap/neo 的自动化编排，宣传向）：
  - X：https://x.com/pdiscoveryio/status/2112627777811988630
- **Forrest Orr 免费归档上线**（Windows 内存破坏/恶意软件内存痕迹写作、工具、shellcode/PoC 实验，含 DoubleStar Darkhotel 利用链再现）：
  - X：https://x.com/PumpkinSecurity/status/2112644042299527348 ；https://x.com/cr3ghost/status/2112654526255878500
  - GitHub：https://github.com/forrest-orr/ExploitDev ；https://github.com/forrest-orr/DoubleStar
- **AI 攻防/安全审计（扩散向，仅链接）**：AlAssaf_H「10 个 AI 驱动攻击安全 GitHub 仓库」（含 Strix 多代理渗透）、PortSwigger/其它。
  - X：https://x.com/AlAssaf_H/status/2112601571854819582
  - GitHub：https://github.com/usestrix/strix
- 地址／IoC：以上均未见公开 IoC。

## APT / Malware 分析

### 1. APT28／Swallowtail（GRU）用 HOOKEDGE 打两个北约国的防务目标（Symantec，今日最大 APT 事件）
Symantec（security.com）确认 Swallowtail（APT28/Fancy Bear/Forest Blizzard）攻击两个北约成员国的**执法机关、军用航发制造商、海军造船厂**。造船厂一案潜伏至少两个月、有明显 hands-on-keyboard：7-24 恶意 Word 宏（从 Outlook 附件缓存直接打开）落下 HOOKEDGE 链（VBS 启动器＋自动提交隐藏表单的 HTML/XHTML 对＋批处理）；批处理**杀掉 Edge 后，用单像素、屏外的隐藏 Edge 窗口加载 base64 JS，把浏览器当 HTTP 客户端**从 `webhook.site` 取任务并回传结果。7-27 起改从专用 IP `185.82.218[.]119:443` 取任务。TTP：推 SSH 私钥（落 `C:\ProgramData\Adobe\id_rsa`）即用它 `-R` 建后台反向隧道给出进内网的路由；PowerShell 起环回 HTTP 监听、`net use` 强迫本机对自己 SMB 认证以抓 NTLMv2；新反射加载器 **ld.exe**（参数给密钥和加密文件路径，内存解密后调 `ExecuteLoader`，解密内容头 `ADSA`/0x41534441）。基础设施到 9-24 仍活跃。
- X 原帖：
  - https://x.com/SwitHak/status/2112676418026918192
  - https://x.com/Pick_Analytica/status/2112682760850878792
  - https://x.com/CroutonKron/status/2112645134064206322
  - https://x.com/BadgerSignalHQ/status/2112560729480167440
  - https://x.com/rst_cloud/status/2112582885823647946
- 文章：
  - https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets
  - https://github.com/NextronSystems/iocs/tree/master/reports/Hunting%20APT28:%20How%20We%20Caught%20Covenant%20Grunt%20Hiding%20in%20Office%20Documents
- 地址／IoC（Symantec）：C2 `185.82.218[.]119`；`webhook[.]site/890efd8d-6e9e-428a-bcf9-987745d71000`、`/53379b62-8020-41cf-af57-effa6e1e8506`、`/5b73dc69-d765-4440-a4d2-e9eb33283eb9`、`/d828b9fc-5435-4b1c-881f-d6350c11d0b6`、`/ca3c058e-3c88-449b-8299-822cd5d5e17c`；侦察里探测到硬编码 `23.220.75[.]245`；ld.exe SHA-256 `f1cc91e7427a22027f65d31bbee19c54b602d08d7d93e4745b9cea59fa8132ff`（另有 18 个 HOOKEDGE dropper/VBS 哈希见原文）；落点 `C:\ProgramData\Adobe\id_rsa`、`C:\ProgramData\ld.exe`、`Events.dat`。

### 2. OVHcloud 官方 CLI 的 GitHub 发行物被挂马（v0.11.0–v0.15.0，GlassWorm 关联）
OVHcloud 官方公告（GHSA-862f-55f5-vmvw）：某开发者 GitHub 账号被盗（根因是 2025-10-20 在个人 Mac 装了恶意 VS Code 插件 `color-picker-universal 2.8.91`，用 GlassWorm 钱包 `BjVeAjPrSKFiingBn4vZvghsGj9KCE8AJVtbc9S8o8SC` 做 Solana RPC，装了持久 NodeJS 服务回连 `162.33.177[.]177`），被用其窃取的密钥在 **10-19 12:47–14:21 UTC** 替换了 v0.11.0–v0.15.0 的 mac(x86_64/arm64)、Linux(x86_64/arm64)、Windows(x86_64) 二进制和 checksums.txt（约 94 分钟、约 250 次下载）。恶意 go 构建（stripped，envchecker 模块）偷 VS Code/Cursor/Continue/Cody/OpenCode/Hermes/Claude/AWS/GCP/Azure/Docker/K8s/NPM/doctl/SSH/Terraform/.netrc/.gitconfig 等，打包后经 Solana RPC（钱包 `BHaDaVbdCYFNaKZGn7yLXFneWoJHZgLiBYkHxVrjyALF`）取指令、上传到 `hxxps://45.32.148[.]174/upload`。**源码/标签/CI-CD 未动**；干净版 v0.16.0（已启用不可变发行）。装过（窗口内下载并运行）的按密钥全泄露处理，换机轮换云/容器/K8s/Terraform/SSH/Git/npm/AI 工具密钥；可查临时目录是否有 `envchecker-[0-9]{9,10}`。
- X 原帖：
  - https://x.com/BursaMatus/status/2112559108981215743
  - https://x.com/TweetThreatNews/status/2112668256066519177
  - https://x.com/theharold_news/status/2112647256822231350
  - https://x.com/BreachHistoryBH/status/2112669815269990680
- 厂商/文章：
  - https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw
  - https://www.bleepingcomputer.com/news/security/ovhcloud-cli-releases-backdoored-on-github-to-steal-developer-secrets/
  - https://thehackernews.com/2026/10/hackers-hijack-five-ovhcloud-cli.html
  - https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool
- 地址／IoC（OVHcloud）：外带 `45.32.148[.]174:443`；Solana 钱包 `BHaDaVbdCYFNaKZGn7yLXFneWoJHZgLiBYkHxVrjyALF`（stealer）、`BjVeAjPrSKFiingBn4vZvghsGj9KCE8AJVtbc9S8o8SC`（GlassWorm/插件）；回连 `162.33.177[.]177`；恶意二进制 MD5 `6f2f086239f3d88eb2750e871901927d`(Darwin_arm64)、`347e65eb7f2d78d1c6872690272a6cc3`(Darwin_x86_64)、`01f57206d37c28cf711677f612052913`(Linux_arm64)、`301bff0b51980b9e76c93633e7cfd3bd`(Linux_x86_64)、`6a3cf153338c416169cda2fe704c8848`(Windows)；工作目录 `envchecker-[0-9]{9,10}`。

### 3. FBI/CISA/德英联合 #StopRansomware: SafePay（AA26-293A）
SafePay 自 2024-08 起对北美/南美/欧洲/澳洲 600+ 企业与关基下手，2026 年「最活跃勒索团伙之一」。入场靠暴破/猜密码、钓鱼、边缘设备漏洞（CVE-2020-3259、2023-20269、2023-27532、2024-40711、2024-40766）与自动化脚本；入内后建/接管账号、用 LOLBins（PowerShell/PsExec/WinRM/nltest/ShareFinder.ps1）横移、NetExec/netscan 侦察、RClone/FileZilla/WinRAR/b2.exe(Backblaze) 外带，电话施压；代码部分像 LockBit。曾打 Conduent、Microlise 等。
- X 原帖：
  - https://x.com/CISACyber/status/2112619252247114226
  - https://x.com/DailyDarkWeb/status/2112653585255383392
  - https://x.com/arnavsharma/status/2112677233009578333
- 厂商/文章：
  - https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a
  - https://therecord.media/fbi-says-safepay-ransomware-gang-among-most-active-600-victims
- 地址／IoC（CISA，2024-11~2026-08）：IP `104.26.2[.]223`、`140.82.114[.]4`、`185.199.108[.]133`、`77.37.49[.]40`、`173.194.194[.]94`、`167.235.225[.]149`、`5.255.11[.]134`、`88.119.167[.]239`(soc.dll C2)、`37.10.71[.]188`；SHA-256 `921df888aaabcd828a3723f4c9f5fe8b8379c6b7067d16b2ea10152300417eae`(soc.dll)、`327b8b61eb446cc4f710771e44484f62b804ae3d262b57a56575053e2df67917`／`a0dc80a37eb7e2716c02a94adc8df9baedec192a77bde31669faed228d9ff526`(locker.dll)、`e79608cf1d6b51324c14bef8883054c1238ed5f080222cc464810e6e14adc346`(Injected PE)、`BBDD3620A67AEDEC4B9A68B2C9CC880B6631215E129816AEA19902A6F4BC6F41`(SharpShares.exe)；文件 locker.dll／soc.dll／nxc.exe／b2.exe／ShareFinder.ps1／Socks.exe／Socks_werfault.exe；主机名 `WIN-SBOE3CPNAL`、`WIN-3IUUOFVTQAR`、`WIN-DK18BI83M0S`、`WIN-I1HRRJHCEIV`。

### 4. eMudhra 8 个中间 CA 私钥被攻破（信任链事件）
Mozilla/Chrome 10-20 确认：印度 CA eMudhra（emSign 品牌）8 个中间 CA 的私钥被攻破，私钥熵极低（部分私钥值 <256，甚至「4」），任何持有者可为任意站点签发浏览器会接受的伪造证书。研究者「Wayne」10-17 用 8 把密钥各签「We have a problem here」报告根程序。6 个是 TLS（DV/OV/EV，chain 到 emSign ECC Root CA - G3），2 个代码签名；每个还有 Sectigo 交叉签名副本。Chrome（CRLSet，18:05Z 收报→19:45Z 拦截，按公钥匹配含交叉副本）、Firefox（OneCRL；158.0.1/ESR 带静态块，CVE-2026-113470）、Go 1.27.3/1.26.10（拒绝含这 8 把密钥的链，CVE-2026-111943，URGENT 轨道）、NSS 3.131.1、Python certifi、Rust webpki-roots、Homebrew 已处置；Node.js/Composer 待定。浏览器用户风险低（无 CT 日志记录可被默认信任）；Go 程序/certifi/IoT/自管信任库需手动更新。Chrome 将在 root store v43 移除该根并复查 eMudhra 另一根。
- X 原帖：
  - https://x.com/TheHackersNews/status/2112592553749176652
  - https://x.com/championswimmer/status/2112676637191885168
  - https://x.com/itsJaimeMedina/status/2112682526355644664
  - https://x.com/yamasinsapporo/status/2112678926959124880
  - https://x.com/sandeepssrin/status/2112678215714255318
- 文章：
  - https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html
  - https://bugzilla.mozilla.org/show_bug.cgi?id=2083449
  - https://www.firefox.com/en-US/firefox/158.0.1/releasenotes/
- 地址／IoC：无传统 IoC；受影响中间 CA：EM DV/OV/EV TLS CA - G3B 与 G3C、EM OV CS CA - G3B 与 G3C；根 emSign ECC Root CA - G3。

### 5. AI 驱动的自主入侵：Cairn 代理攻击 1200+ 站（NorForge/THN）
中文圈犯罪者用开源 AI 代理框架 **Cairn** 自主攻击 1200+ 站、触及 100+ 公司（Deere、SharkNinja、Cummins 等）。研究者 Snorre Fagerland（NorForge）从 10-2 起发现约两打暴露在公网的 Cairn 面板（常在 8000 端口），可实时读到攻击者作业：最活跃的中文集群 AIA0001 关联 1100+ 攻击项目，目标美日澳，典型任务是「在店铺跑代码并种 webshell 上传器」；平均 23 小时拿下、约 10% 成功率、单次约 $5（整场约 $5000 token）、worker 名 `claudecode_deepseek-v4.1-flash`。暴露面板还泄露受害者密钥（Trufflehog 扫出数百个、11% 仍有效）。一个 worker 目录里有 Magento StyleSmuggler（CVE-2026-75650）的 PoC 与测试台（无证据用于这些入侵）。
- X 原帖：
  - https://x.com/Dinosn/status/2112564850656202984
  - https://x.com/DarkReading/status/2112596463247098186
  - https://x.com/SansLimit3/status/2112523777833587162
- 文章：
  - https://thehackernews.com/2026/10/hackers-use-autonomous-ai-agents-to.html
  - https://www.darkreading.com/cyberattacks-data-breaches/hackers-abuse-ai-pen-test-tool-cairn
- 地址／IoC：未见公开网络 IoC（狩猎点：公网 8000 端口无登录的代理面板、隐藏目录里的异常上传表单；Magento 2.4.4–2.4.9 打 Adobe 热修）。

### 6. DarkSword-PROV2 iOS 利用套件续：SlowMist 深度分析
SlowMist（10-19，经 BlockBeats 摘要，SlowMist 原文被 Cloudflare 拦截未直接读到）：相关利用代码 2026-03 公开后，**DarkSword-PROV2** 7 月上 GitHub、9 月下旬基础设施上线。全自动流水线整合漏洞投递、设备/数据采集、外带、钱包资金归集；盗 Keychain/文件/消息，并专门解密钱包数据、归集资金（针对 imToken/TokenPocket/TronLink）。虽号称支持 iOS 13+，**实际有效利用窗口集中在 iOS 18.6–18.7.2 与 26.0–26.1**。WebKit JSCore RCE→dyld PAC 绕过→GPU/mediaplaybackd 沙箱逃逸→内核读写→注入 SpringBoard/securityd/键盘输入采集。建议升级 iOS、别点不明链接；曾访问可疑落地页的设备把助记词/私钥按已泄露处理，用干净设备新建钱包转移资产并撤销授权。（续 10-19 Coruna/DarkSword 条目。）
- X 原帖：https://x.com/RomanChainOps/status/2112518665845317794 ；https://x.com/JeffreyReitman/status/2112677038003978632
- 文章：
  - https://en.theblockbeats.news/flash/372583
  - https://github.com/adoemwanmei/DarkSword-PROV2 （仅供核对，不转载内容）
- 地址／IoC：SlowMist 原文被 Cloudflare 拦截未取到具体 IoC；参见 10-19 报告已列的 `btrf36[.]cc`、`ypnfeo[.]cc`、`/js/analystic/`、`darksword.msxfweb[.]net`、`admin.msxf[.]info` 等。

### 7. 其它威胁报告（rst_cloud 摘要等）
- **BRONZE SANDCASTLE（中国关联）**：改版 Meterpreter 植入物经 Sandboxie DLL 侧加载，打亚非，2025.8–2026.8。X：https://x.com/DFIR_Radar/status/2112605366781407422
- **INC/The Gentlemen 勒索的 AI 编排入侵生态（Prodaft/SansLimit3）**：7 台暴露的对手服务器藏 AI 会话、46 个预置加密器、62 个点名受害者与自主攻击框架 Phantom 源码。X：https://x.com/SansLimit3/status/2112523777833587162 ；https://x.com/DFIR_Radar/status/2112514715389735077
- **TRIPAUL3（模块化 Windows x64 RAT，C++）**：配置与 6 个加密插件藏在 PE overlay。X：https://x.com/CryptoInsane/status/2112679820869898242
- **synfinner 拆 C++ 双载荷窃密器**：AES-256-GCM 配置（头 `UMRBLCFG`），运行时解密 Discord webhook 与 mutex（`Local\{3F2504E0-4F89-11D3-9A0C-0305E82C3301}`）。X：https://x.com/synfinner/status/2112647138274328625
- **ROMULUS/ClickFix（冒充 ChatGPT Custom GPT）→ Legion Loader**：X：https://x.com/aviatrixtrc/status/2112598120919966138
- **PyPI 'saeka' 刷卡自动化犯罪软件**、**ConnectWise Cloud Backup 供应链（Truesec）**：X：https://x.com/rst_cloud/status/2112598059456528560 ；https://x.com/rst_cloud/status/2112590471184748735 （文章 https://www.truesec.com/hub/blog/supply-chain-attack-on-connectwise-cloud-backup ）
- **objective-see 公开 HeartBreaker macOS 样本与变形框架**（研究库，pw: infect3d）：X：https://x.com/objective_see/status/2112528919299764457
- 地址／IoC：见各条与地址表；多为摘要，具体哈希见各原文。

### 8. 零散 IoC 投放（猎人账号，单源，UNCONFIRMED）
- LAFS RAT/Panel：`paybtmob[.]store`、`45.158.8[.]87`；SHA-256 `b4ee9ccd3db4836ccce2bfd5822d65c541a488ddf84fa9569070fa724c172296`、`dad182e472136e1ce4e4ad4aa92f84d23b85bf289f5f9d6d3a96146c25c219ab`（@Fact_Finder03）：https://x.com/Fact_Finder03/status/2112568660963610876
- SilentLynx/Lynx（标签）：`172[.]86[.]86[.]60`（@phatomcandle）：https://x.com/phatomcandle/status/2112559475689476360
- Mythic C2：`2[.]27.63.244`，回连 `cdn-staticfiles[.]com`、`wiredrum[.]llc`（@etugenio）：https://x.com/etugenio/status/2112628745077133499
- Cobalt Strike（中国，开放目录）：`218.244.142[.]4:80`（@0xb1lal）：https://x.com/0xb1lal/status/2112636594993709162
- SliverC2（Shodan，@orlof_v）：`106.12.190[.]248`、`193.70.100[.]109`、`38.87.116[.]68`、`43.160.211[.]117`：https://x.com/orlof_v/status/2112542490683183523
- 可疑样本（@smica83，abuse.ch）：`35da31b12e2c66f2954b9edb93189d9aefb500deb22d879a0623fc6b0729d0cd`（'Windows Defender smart host security.exe'，拉脱维亚）、`2f9b740d5d686506ac9c3f222c0a8c79d2a7fb880a85edda30d8b48ce3c7e217`（'RuntimeBroker.exe'，沙特）：https://x.com/smica83/status/2112600765139218500
- macOS 诱饵（@malwrhunterteam）：`watts-macos.github[.]io/Watts_3.1.2.dmg`：https://x.com/malwrhunterteam/status/2112607806964535613

### 9. 入侵／泄露声称（除注明厂商/官方自述外一律 UNCONFIRMED）
- **NEC（厂商自述）**：系统开发/保守委托先 9 月下旬遭攻击，正规账号认证信息被盗用、从委托先终端登入顾客系统加密服务器致停摆；关系者共享的云存储文件外泄，3 家顾客中 2 家确认个人信息泄露（续日本持续被攻击潮）。
  - X：https://x.com/MalwareBibleJP/status/2112664915999961224 ；https://x.com/DailyDarkWeb/status/2112668752877859236
  - 文章：https://www.itmedia.co.jp/news/article/2610/20/2000002433/ ；https://www.security-next.com/191694
- **日本其它（MalwareBibleJP 汇总）**：アルカディア（防災アプリ）不正アクセス 105 小时攻防、关东4县警察 约3.66万人个资可能外泄；Ymirlink「Cuenote FC」约900万条；リンクステーション GETTIIS 会员ID 约31.8万；富士急ハイランド/CLUB-フジQ、フジテレビ番宣系统（约730件）、津市図書館、燦HD子会社等。木原官房长官：「是否用 AI、是否外国主体介入仍待查」（GMO 旗下安全公司称部分攻击用了中国系 AI 代理）。
  - X：https://x.com/MalwareBibleJP/status/2112666928183710056 ；https://x.com/MalwareBibleJP/status/2112674981440274860
- **California（官方自述）**：州教育测评承包商泄露，涉数百万学生姓名/住址/残障状态/测评结果。X：https://x.com/TheRecord_Media/status/2112626326750531940
- **Nikkei**：180 万条（续报，securityaffairs）。X：https://x.com/securityaffairs/status/2112604980301402312
- **Zeabur**：两月内第二次泄露后关停。X：https://x.com/BleepinComputer/status/2112628242309919010
- **Qilin/其它团伙声称**：ThreatAtlas/intels_daily/CyberThreatLine 等列出 SilentRansomGroup、payload、HollowedOps（声称 Binance/OKX/Bitget 相关加密欺诈）、GLOBAL SECRET GROUP、MIMORI（声称 OpenText/AVEVA）等多条 **UNCONFIRMED** 声称。X：https://x.com/intels_daily/status/2112682047399432553 ；https://x.com/Darkwebintell/status/2112550314335457708
- 地址／IoC：未见公开 IoC。

### 10. 本轮核对的「旧闻/误报」提醒
- **Zimbra CVE-2026-73570**（X 上 BadgerSignal 等今日热传为「zero-click RCE 活跃利用」）：经核对，这是 **2026-08 的旧事件**（7-20 修于 10.1.20，CERT Polska 8-17 报在野，CISA 8 月入 KEV，Microsoft 9-30 跟进）。今日没有新进展，仅为再次扩散，**非今日新在野**。
  - X：https://x.com/BadgerSignalHQ/status/2112560229745586380
  - 文章：https://www.helpnetsecurity.com/2026/08/25/zimbra-cve-2026-73570-compromised/

## 地址／IoC 汇总

> 全部原样抄录自来源，已去武装（`[.]`）的保持原样；单源条目标 UNCONFIRMED。**只用于检测与封堵。**

| 关联 | 类型 | 指标 | 来源 |
|---|---|---|---|
| APT28/Swallowtail HOOKEDGE | C2/IP | `185.82.218[.]119`；硬编码探测 `23.220.75[.]245` | Symantec |
| APT28/Swallowtail | webhook.site | `/890efd8d-6e9e-428a-bcf9-987745d71000`、`/53379b62-8020-41cf-af57-effa6e1e8506`、`/5b73dc69-d765-4440-a4d2-e9eb33283eb9`、`/d828b9fc-5435-4b1c-881f-d6350c11d0b6`、`/ca3c058e-3c88-449b-8299-822cd5d5e17c` | Symantec |
| APT28/Swallowtail | SHA-256 | `f1cc91e7427a22027f65d31bbee19c54b602d08d7d93e4745b9cea59fa8132ff`（ld.exe，另 18 个 HOOKEDGE 哈希见原文） | Symantec |
| APT28/Swallowtail | 落点 | `C:\ProgramData\Adobe\id_rsa`、`C:\ProgramData\ld.exe`、`Events.dat` | Symantec |
| OVHcloud CLI/GlassWorm | 外带/回连 | `45.32.148[.]174:443`；`162.33.177[.]177` | OVHcloud |
| OVHcloud CLI/GlassWorm | Solana 钱包 | `BHaDaVbdCYFNaKZGn7yLXFneWoJHZgLiBYkHxVrjyALF`、`BjVeAjPrSKFiingBn4vZvghsGj9KCE8AJVtbc9S8o8SC` | OVHcloud |
| OVHcloud CLI | MD5 | `6f2f086239f3d88eb2750e871901927d`、`347e65eb7f2d78d1c6872690272a6cc3`、`01f57206d37c28cf711677f612052913`、`301bff0b51980b9e76c93633e7cfd3bd`、`6a3cf153338c416169cda2fe704c8848` | OVHcloud |
| OVHcloud CLI | 主机痕迹 | 临时目录 `envchecker-[0-9]{9,10}` | OVHcloud |
| SafePay 勒索 | IP | `104.26.2[.]223`、`140.82.114[.]4`、`185.199.108[.]133`、`77.37.49[.]40`、`173.194.194[.]94`、`167.235.225[.]149`、`5.255.11[.]134`、`88.119.167[.]239`、`37.10.71[.]188` | CISA AA26-293A |
| SafePay | SHA-256 | `921df888...417eae`(soc.dll)、`327b8b61...df67917`／`a0dc80a3...8d9ff526`(locker.dll)、`e79608cf...14adc346`(Injected PE)、`BBDD3620...F4BC6F41`(SharpShares.exe) | CISA AA26-293A |
| SafePay | 文件/主机名 | locker.dll／soc.dll／nxc.exe／b2.exe／ShareFinder.ps1／Socks.exe；`WIN-SBOE3CPNAL`/`WIN-3IUUOFVTQAR`/`WIN-DK18BI83M0S`/`WIN-I1HRRJHCEIV` | CISA AA26-293A |
| NetScaler 88771+88779 | C2/IP | `v5v.in`、`209.74.64[.]192`、`192.159.99[.]139`、`213.209.159[.]55`、`179.60.146[.]241`、`45.92.1[.]17:30444`、`62.133.62[.]80`、`46.151.182[.]18`、`132.243.166[.]140`、`199.233.217[.]13`、`31.56.197[.]72`、`64.94.85[.]67`、`130.94.20[.]222`、`173.231.39[.]244` | Rapid7 |
| NetScaler | SHA-256 | `6774bfed...6f0a03c44`(1.sh)、`a0ba4e1a...80535556`(17447d.sh)、`56a892d8...1b4a6fb186`(2.sh/r.sh)、`8e8b9532...d19b51a4d`(scanner-freebsd-amd64)、`eaf00862...fd3a31cdde`(vc)、`ffe052fc...d9c0b138`(nsvmd) | Rapid7 |
| NetScaler | 路径 | `/nsconfig/.slap/`、`/flash/.nsvm/nsvmd`、`/var/tmp/.ux/slapshot.py`、setuid `/bin/sh`、`.slap.receiver`/`.ctxs.receiver`/`receiver.deb` webshell | Rapid7 |
| Oracle EBS 101767 | 狩猎 | 未认证 POST `/OA_HTML/AppsTCFServer` 实例化 `GanttDataServer`；`$APPLPTMP` 异常文件；`oracle` 经 Concurrent Manager 派生 `/bin/sh` | Horizon3 |
| Siemens 110936（10-19） | C2/哈希 | `96.62.218[.]59`、`wizardexpensive[.]com`；`f4d7c53...1092e4a`(AllMyBasic.msi)、`3fdcc7d7...1f2cf491`(archive.dll) | Siemens ProductCERT |
| LAFS RAT（UNCONFIRMED） | 域名/IP/哈希 | `paybtmob[.]store`、`45.158.8[.]87`；`b4ee9ccd...c172296`、`dad182e4...25c219ab` | @Fact_Finder03 |
| SilentLynx/Lynx（UNCONFIRMED） | IP | `172[.]86[.]86[.]60` | @phatomcandle |
| Mythic C2（UNCONFIRMED） | IP/域名 | `2[.]27.63.244`、`cdn-staticfiles[.]com`、`wiredrum[.]llc` | @etugenio |
| Cobalt Strike（UNCONFIRMED） | IP | `218.244.142[.]4:80` | @0xb1lal |
| SliverC2（UNCONFIRMED） | IP | `106.12.190[.]248`、`193.70.100[.]109`、`38.87.116[.]68`、`43.160.211[.]117` | @orlof_v |
| 可疑样本（abuse.ch） | SHA-256 | `35da31b1...729d0cd`('Windows Defender smart host security.exe')、`2f9b740d...e3c7e217`('RuntimeBroker.exe') | @smica83 |
| macOS 诱饵 | URL | `watts-macos.github[.]io/Watts_3.1.2.dmg` | @malwrhunterteam |
| synfinner 窃密器 | 主机痕迹 | mutex `Local\{3F2504E0-4F89-11D3-9A0C-0305E82C3301}`、配置头 `UMRBLCFG` | @synfinner |

其余条目（PHP 109618/109619、Plex2Shell、SiteGuard 106931、FortiSIEM 106173、Cisco SEG 76519、Drupal、Redis 25243、Apache Answer/Camel、Netcore、eMudhra、Cairn、PAN-OS 0257、BeyondTrust 102764、各工具仓库、泄露类）：**未见公开 IoC**（或 IoC 只在本轮未抓取的原文中）。

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

**今日 LWiS 交叉要点**：List 成员本轮贡献最多的是 @vxunderground（goop/恶意样本串、PHP 段子）、@cyb3rops（PHP RCE 准备、process-watcher）、@Dinosn（PAN-OS、Cairn AI、Pegasus、Signal/Meta 快讯）、@ipurple（从零写 BOF、Skarvel、PhantomBuffer 测评）、@LiveOverflow 与 @Frichette_n（PHP 0day 视频/预警）、@SwitHak 与 @Pick_Analytica（APT28/Swallowtail）、@objective_see（HeartBreaker macOS 样本）、@noperator（pocpocalypse）。blogs.txt 命中的高信号源：Unit 42（`https://unit42.paloaltonetworks.com/`，PAN-OS 0257 续）、Rapid7（NetScaler 链）、Horizon3（`https://www.horizon3.ai/red-team-blog/`，EBS 101767/FortiSIEM 106173）、watchTowr labs（`https://labs.watchtowr.com/`，PHP FAQ）、Krebs/Elastic/security.googleblog。Risky Business 首页与 tl;dr sec 归档可访问；tl;dr sec 最新仍是 **#350「Reverse Engineer Anything, Tracking AI-integrated Malware, Test-driving Jev」(10-15)**，无新一期。

## 来源搜索 URL

- A（CVE／0day／PoC）：https://x.com/search?q=%28CVE-2026%20OR%20CVE-2025%29%20%28exploit%20OR%20exploited%20OR%20PoC%20OR%20RCE%20OR%20patch%20OR%20advisory%20OR%20KEV%20OR%200day%20OR%20zero-day%29%20-is%3Aretweet%20-from%3Avulnipulse&f=live
- A 在野：https://x.com/search?q=%28%22zero-day%22%20OR%200day%20OR%20%22in%20the%20wild%22%20OR%20%22actively%20exploited%22%29%20%28vulnerability%20OR%20exploit%20OR%20CVE%20OR%20patch%29%20-is%3Aretweet%20-is%3Areply&f=live
- B（GitHub 红队／C2）：https://x.com/search?q=url%3Agithub.com%20%28C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20PoC%20OR%20exploit%20OR%20BOF%20OR%20EDR%20OR%20implant%20OR%20loader%29%20-is%3Aretweet&f=live
- C（威胁报告）：https://x.com/search?q=%28%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%29%20-is%3Aretweet%20-is%3Areply&f=live
- C IoC：https://x.com/search?q=%28malware%20OR%20infostealer%20OR%20RAT%20OR%20backdoor%20OR%20ransomware%20OR%20loader%29%20%28IOC%20OR%20C2%20OR%20sha256%20OR%20%22threat%20report%22%29%20-is%3Aretweet%20-is%3Areply&f=live
- 专题（PHP／KEV 新增／供应链）：https://x.com/search?q=%28CVE-2026-109618%20OR%20CVE-2026-109619%20OR%20plex2shell%20OR%20SiteGuard%20OR%20%22CVE-2026-110936%22%20OR%20OVHcloud%20OR%20eMudhra%20OR%20FortiSIEM%29&f=live
- 专题（APT/勒索）：https://x.com/search?q=%28Swallowtail%20OR%20HOOKEDGE%20OR%20APT28%20OR%20SafePay%20OR%20NetScaler%20OR%20%22Armory%20Castle%22%29%20-is%3Aretweet&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
