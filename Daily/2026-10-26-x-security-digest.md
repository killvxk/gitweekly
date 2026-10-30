# X 安全情报晚报 · 2026-10-26

> 搜集窗口：圣地亚哥时间 **2026-10-25 20:10 至 2026-10-26 20:18**（America/Santiago／UTC-3，接昨晚窗口）。X 搜索参数：`start_time=2026-10-25T23:10:00Z`，不设 end_time。实际抓到的帖子从 **10-25 20:10** 到 **10-26 20:18**（UTC-3），**实际有效覆盖约 24 小时**。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all` 用 recency 和 relevancy 两种排序；`user-X` 的 `get_lists_posts` 读 LWiS List；`get_posts_by_ids` 读重点原帖全文）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** t.co 短链按接口返回的 `expanded_url`／`unwound_url` 展开；纯图片／视频链接不列。
> 本轮查询：
> - A 类（CVE／0day／PoC／exploit）：Latest／relevancy 两次、`CVE-2026` has:links 一次、actively exploited／zero-day／advisory 一次、高信号账号专查一次
> - B 类（GitHub＋C2／red team／nuclei／工具发布）：两次
> - C 类（malware analysis／threat report／threat actor／APT／campaign／IoC）：两次
> - LWiS List（1239330068461244424）：三页共 284 条（覆盖约 10-26 01:08–19:34 UTC-3）
> - 原帖全文读取：一次（约 36 个 ID）
>
> 合计 **13 次有效 X 读取，0 次 429**。原始返回约 450 条（含列表），窗口内去重 **412** 条（与 seen_ids 8080 条重叠 6），关键词粗筛 **约 183** 条安全相关新帖（排除纯转推与噪声），下文引用约 80 条。剔除了广告／营销、体育、加密货币刷屏、性骚扰语境的「exploit／poc」、纯勒索软件受害者刷屏（未展开）。**全程只读，没有发帖、回复、点赞、转推、收藏或关注。**
> **公开备援**（`/workspace/x1026/pages/`，curl 核对）：CISA KEV JSON（catalogVersion **2026.10.26／1758／Δ+2**）；CISA PHP 警报更新；Google Cloud／BleepingComputer／THN（Gheist、953 商店、Teams、M365、Wasmtime、AI agent）；Sansec／SecurityWeek；runZero BMC；Horizon3 FortiSIEM；Invaders Redis；Unit 42／Palo Alto Brotli；Oracle PHP 警报；Check Point 10-26 日报。本轮**未**用 GitHub API 核对 nuclei／Sliver 等正式 release。
> **CISA KEV：catalogVersion 2026.10.26／1758 条，Δ+2**（相对昨晚 2026.10.23／1756）。`dateReleased` 为 2026-10-26 19:24 UTC-3。
> - **今日新增入列（due 10-29）**：**CVE-2026-109618**（PHP Memory Corruption／PHP2Shell）、**CVE-2026-109619**（PHP Stale Internal Request-State／PHP2Shell）。联邦机构需在 10-29 前完成缓解并做入侵排查。
> - **今日 10-26 到期**：Arista VeloCloud Orchestrator **CVE-2026-114625**（SQLi）、Collabora Online CODE **CVE-2026-110447**（OS 命令注入）。
> - **11-03 到期**：Plex 96652、Plex 96655、Siemens 110936。
> - **逾期（续）**：
>   - 10-23 到期：SiteGuard 106931、Plex 96656、Plex 96654
>   - 10-19 到期：BeyondTrust 102764、Fortinet CVE-2025-61624
>   - 10-18 到期：Atlassian 21589
>   - 10-17 到期：AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322
>   - 10-16 到期：Ivanti 104935、Windows Shell MOTW 96951
>   - 10-13 到期：Apple 86950
>   - 10-11 到期：CVE-2015-5477、CVE-2016-3081、CVE-2023-22894、CVE-2021-3199、CVE-2015-3306
> - **仍未进 KEV、但今日高优先**：Redis RESTORE **CVE-2026-25243**（加拿大网络安全中心标在野）、FortiSIEM 106173、Citrix NetScaler 88771／88772、Brotli／HTTP2Shell 111497、Wasmtime 115889／115893、Ivanti Connect Secure 104935（暗网售卖 PoC）。

## 今日摘要

- **PHP2Shell 正式进 KEV**：CISA 于 10-26 把 CVE-2026-109618／109619 加入 Known Exploited Vulnerabilities Catalog，联邦 due **10-29**；并更新了 10-21 的 PHP 紧急警报。@CISACyber 原帖：https://x.com/CISACyber/status/2114858762259345731
- **在野 RCE 证据升级**：BleepingComputer／Perplexity Adel Karimi（@0x4D31）蜜罐在 PHP 8.4.26＋Apache mod_php 上录到**可用内存泄露＋后续执行**，不再只是崩溃；0x4D31 提醒「成功利用」指蜜罐场景，勿恐慌放大。LiveOverflow 放出 StealMyBitcoin 解法视频；公开仓库 https://github.com/KillaBoi/StealMyBitcoin-PoC 与 Assetnote 扫描器继续流通。
- **今日到期两条 KEV**：Arista VeloCloud **114625**、Collabora Online **110447**——今天就该关单。
- **Redis CVE-2026-25243**：加拿大网络安全中心更新称 **RESTORE 命令相关缺陷已在野利用**；限制／禁用 RESTORE，尽快打补丁。
- **供应链／云凭证**：Wiz 披露 **Gheist**——用被盗 GitHub token 在私库／Enterprise 种 secret-dumping workflow（已恢复 13,500+ 分支／850+ 账号）；Sansec／SecurityWeek／THN 报道 **953 家网店**（多为 Magento）长期 Magecart 式 loader 活动。
- **新恶意软件／地下生态**：abuse.ch 标出 **MopsStealer** C2；Icarus RAT 在地下广告；SecurityBreak 拆解地下「全能」平台 **Omega AI**；Arctic Wolf 梳理 Microsoft Teams「IT Support」社工投毒；Huntress 披露 M365 **token-replay**（97 账号／79 组织）。
- **其他补丁面**：微软 .NET 带外更新修 Brotli **111497**；Wasmtime／Cranelift 两条 CVSS 9.9 沙箱逃逸；Apache Camel 一批（含 XXE）；runZero 披露 21 个 BMC／OOB 问题；Ivanti Connect Secure **104935** 出现 3000 美元预认证 RCE PoC 售卖帖。

## CVE / POC / 漏洞

### 1. PHP2Shell（CVE-2026-109618／109619）：进 KEV、蜜罐确认 RCE、公开 PoC／扫描器
- **KEV**：CISA 10-26 入列，due 2026-10-29；警报页同步更新。补丁仍是 8.5.12／8.4.27／8.3.36／8.2.35；PHP ≤8.1 无官方修复，需升级运行时。
- **在野证据**：BleepingComputer 引 Adel Karimi 蜜罐——Apache mod_php／PHP 8.4.26 上确认 RCE 链（cookie dump＋后续 payload）；Expel 复核。0x4D31 强调证据针对「单 worker、有利配置」的蜜罐，不是全网成功率统计。
- **公开材料**：StealMyBitcoin 挑战被 @killa 解开后，https://github.com/KillaBoi/StealMyBitcoin-PoC 流传；Assetnote 扫描器 https://github.com/assetnote/php2shell-scanner；社区扫描／补丁脚本 https://github.com/thetowsif/php2shell-scan-patch；LiveOverflow 解法视频 https://www.youtube.com/watch?v=VhNiMWtOutw
- **厂商／云响应**：Google Cloud／Mandiant 指南（含未打补丁的旧 PHP 仍脆弱、取证建议）；Oracle Security Alert；Unit 42 Threat Brief；Palo Alto 产品对 PHP2Shell 的影响说明（HIGH）。
- **注意**：昨日「全版本假 PoC」（0x1c1101）仍是玩笑；今日流通的是挑战解法与扫描器——防御向只做版本盘点、封异常 multipart／`PHP_SESSION_UPLOAD_PROGRESS`、查 webshell，不复现利用步骤。
- 地址：
  - X 原帖：https://x.com/CISACyber/status/2114858762259345731
  - X 原帖：https://x.com/BleepinComputer/status/2114648291929387445
  - X 原帖：https://x.com/0x4D31/status/2114738081492332706
  - X 原帖：https://x.com/LiveOverflow/status/2114793138648986101
  - X 原帖：https://x.com/LiveOverflow/status/2114808281633845359
  - X 原帖：https://x.com/pakar_ai/status/2114508942302961698
  - X 原帖：https://x.com/nariman_orujov/status/2114516886415200710
  - X 原帖：https://x.com/burakaiarchi/status/2114774063461576904
  - X 原帖：https://x.com/Dinosn/status/2114528334927270398
  - X 原帖：https://x.com/GsInfosystems/status/2114853764926783827
  - X 原帖：https://x.com/cu1993/status/2114859117302943937
  - X 原帖：https://x.com/ora_club/status/2114532407940620797
  - X 原帖：https://x.com/sec_alert_chan/status/2114858652943241328
  - X 原帖：https://x.com/S1r1u5_/status/2114774529814007865
  - 厂商公告／KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  - 厂商公告：https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching
  - 厂商公告：https://www.oracle.com/security-alerts/alert-cve-2026-109618.html
  - 文章：https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619
  - 文章：https://www.bleepingcomputer.com/news/security/php2shell-security-flaws-now-sucessfully-exploited-in-the-wild/
  - 文章：https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
  - GitHub（挑战 PoC，勿在生产复现）：https://github.com/KillaBoi/StealMyBitcoin-PoC
  - GitHub（扫描器）：https://github.com/assetnote/php2shell-scanner
  - GitHub（扫描／补丁辅助）：https://github.com/thetowsif/php2shell-scan-patch
  - GitHub（蜜罐证据）：https://github.com/0x4D31/honeypot-data/tree/main/reports/php2shell/2026-10-24-rce-evidence
  - 视频：https://www.youtube.com/watch?v=VhNiMWtOutw

### 2. Arista VeloCloud CVE-2026-114625／Collabora Online CVE-2026-110447：今日 KEV 到期
- 两条均于 10-23 入 KEV，**dueDate=2026-10-26**。Arista 为在野 SQLi（近四个月第三条 VCO 相关 0day 叙事继续在 X 流传）；Collabora 为内置 CODE 服务器 OS 命令注入。
- 地址：
  - X 原帖：https://x.com/aimicyber/status/2114603901085237479
  - X 原帖：https://x.com/lucasverdan/status/2114568705208451095
  - 文章：https://invaders.ie/resources/blog/vulnerability/arista-velocloud-orchestrator-cve-2026-114625-patch-now
  - 厂商／KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

### 3. Redis CVE-2026-25243：加拿大标在野利用
- 加拿大网络安全中心更新：RESTORE 命令相关缺陷**已在野利用**；需已认证且能跑 RESTORE 的用户触发，可导致非法内存访问乃至 RCE。限制外网暴露，禁／限 RESTORE，打厂商补丁。
- 地址：
  - X 原帖：https://x.com/lucasverdan/status/2114642189888508205
  - 文章：https://invaders.ie/resources/blog/vulnerability/redis-restore-cve-2026-25243-exploited-patch-now

### 4. FortiSIEM CVE-2026-106173：PoC／技术分析继续
- Horizon3 深度分析：未认证经 tcp/27918 gRPC `SendQueryResult` 路径穿越写文件，CVSS 9.4；加拿大此前已标在野。升级 7.5.1+ 或先封 27918。
- 地址：
  - X 原帖：https://x.com/ptdbugs/status/2114681148466934104
  - X 原帖：https://x.com/Daily_CyberSec/status/2114517393158369504
  - 文章：https://horizon3.ai/attack-research/cve-2026-106173-deep-dive-fortisiem-grpc-path-traversal-file-write-rce/
  - 文章：https://securityonline.info/fortisiem-cve-2026-106173-exploited-poc/
  - GitHub（PoC 仓库，勿复现）：https://github.com/horizon3ai/CVE-2026-106173

### 5. Brotli／HTTP2Shell CVE-2026-111497：微软 .NET 带外更新；Palo Alto 标 CRITICAL 影响
- 微软发布 .NET／ASP.NET Core 带外安全更新（亦提及 Linux tarball 相关 CVE-2026-114148）；目标版本如 8.0.33／9.0.22（以 MSRC 为准）。Palo Alto 发布产品组合对 111497 的影响说明（Severity: CRITICAL）。日本 Security Lab 亦报道。
- 地址：
  - X 原帖：https://x.com/Daily_CyberSec/status/2114533527551148249
  - X 原帖：https://x.com/securityLab_jp/status/2114858664511332705
  - X 原帖：https://x.com/ripjyr/status/2114795014580535638
  - X 原帖：https://x.com/SecAlertsCo/status/2114859082096284089
  - 文章：https://securityonline.info/dotnet-security-update-brotli-october-2026/
  - 厂商公告：https://security.paloaltonetworks.com/CVE-2026-111497

### 6. Wasmtime／Cranelift CVE-2026-115889／115893（CVSS 9.9）
- 恶意 Wasm 模块可逃逸沙箱；115889 全架构，115893 仅 ARM64。10-19／20 已发修复（如 36.0.19、48.0.7、49.0.4），未见在野利用报道、未进 KEV。
- 地址：
  - X 原帖：https://x.com/ThreatWire_/status/2114707606619169248
  - X 原帖：https://x.com/lee1981b/status/2114659932809187482
  - X 原帖：https://x.com/Dinosn/status/2114736636982657326
  - 文章：https://thehackernews.com/2026/10/two-critical-wasmtime-flaws-could-let.html
  - 文章：https://www.threatwire.tech/news/wasmtime-fixes-two-critical-cranelift-sandbox-escapes-cve-2026-115889-and-cve-2026-115893

### 7. Apache Camel 一批（含 CVE-2026-90885 XXE、CVE-2026-95664 S3 注入等）
- 升级到 4.23.0（以官方公告为准）。
- 地址：
  - X 原帖：https://x.com/Daily_CyberSec/status/2114527549455827311
  - 文章：https://securityonline.info/apache-camel-vulnerabilities-xxe-october-2026/

### 8. Linux 内核 teql qdisc CVE-2026-23074：提权／容器逃逸向公开细节
- 缺陷可追溯至 2005；公开利用细节流传。优先内核更新，限制不可信租户的 qdisc／网络命名空间操作。
- 地址：
  - X 原帖：https://x.com/Daily_CyberSec/status/2114652942770778545
  - 文章：https://meterpreter.org/linux-kernel-teql-cve-2026-23074-exploit/

### 9. Ivanti Connect Secure CVE-2026-104935：暗网售卖预认证 RCE PoC（$3000）
- dbugs／ptdbugs 称卖家宣称无认证 HTTPS、提权至 root 并抽取管理员哈希／LDAP／RADIUS／SAML／Azure 密钥；宣称影响 25.1.x／22.8R2.4 等。该 CVE 已在 KEV 且 due 已过（10-16）。**不要购买或运行来路不明的 exploit**；做版本盘点与入侵排查。
- 地址：
  - X 原帖：https://x.com/ptdbugs/status/2114700039993823515
  - 文章：https://dbu.gs/news/sale-of-a-poc-for-a-vulnerability-in-ivanti-connect-secure-cve-2026-104935-20261026
  - 文章：https://dbu.gs/vulnerability/PT-2026-111656

### 10. runZero：Avocent／Dell iDRAC／Supermicro 共 21 个 BMC／OOB 问题
- 高亮点：Avocent ACS **CVE-2026-65184** 未认证命令注入（CVSS 9.8，WebSocket terminal-bridge）；iDRAC／Supermicro 另有多项（含密码空／内存读写等叙事）。隔离 BMC 管理面，按厂商固件更新。
- 地址：
  - X 原帖：https://x.com/runZeroInc/status/2114726588650516817
  - 文章：https://www.runzero.com/blog/lights-out-exposed/

### 11. 其他漏洞信号
- **SPIP CVE-2026-77647**：未认证 RCE，PoC 仓库出现（升级至 ≥4.4.20）。X：https://x.com/Nxploited/status/2114859056905195795 ；GitHub：https://github.com/Nxploited/CVE-2026-77647
- **比利时 CCB**：eMudhra 相关根证书问题——Java／Python／Go 等需打补丁移除受影响 CA（CVE-2026-114820／115557／111943）。X：https://x.com/CCBalert/status/2114842158217691508 ；公告：https://ccb.belgium.be/advisories/warning-emudhra-certificates-software-vulnerabilities-patch-immediately
- **浏览器沙箱逃逸 CVE-2026-40369**：VoidSec writeup＋GitHub exploit 仓库在 X 流传——防御向跟厂商补丁，不展开步骤。X：https://x.com/DarkWebInformer/status/2114804715716223483 ；文章：https://voidsec.com/cve-2026-40369-browser-sandbox-escape/ ；GitHub：https://github.com/orinimron123/CVE-2026-40369-EXPLOIT
- **Agent 沙箱 RCE 研究**：Instinct／Muse 沙箱代码执行（研究者自报 CVE-2026-99999 占位）。文章：https://amirzak.substack.com/p/achieving-code-execution-inside-instinct ；X：https://x.com/AmirZak6/status/2114720402492526611

## 工具与 GitHub 发布

### 1. google/mantis — AI coding agent 找洞／复现／打补丁工具包
- Google 开源、模块化、栈无关。红蓝都可当辅助，注意沙箱与密钥隔离。
- 地址：
  - X 原帖：https://x.com/CyberWarship/status/2114728763426488817
  - GitHub：https://github.com/google/mantis

### 2. PngLoader — PNG 隐写＋Windows「看图」加载器（红队演示）
- 双层编码（nibble→ASCII＋Fibonacci 像素）藏数据，配套 loader 提取执行。仅授权环境使用。
- 地址：
  - X 原帖：https://x.com/ipurple/status/2114762895233851681
  - GitHub：https://github.com/i014n/PngLoader

### 3. PHP2Shell 相关扫描／PoC 仓库（见 CVE 节）
- Assetnote scanner、thetowsif scan-patch、KillaBoi StealMyBitcoin-PoC、0x4D31 蜜罐数据、horizon3ai FortiSIEM PoC。

### 4. PSSW100AVB — 声称「100% AV bypass」的 PowerShell 反向 shell 仓库
- @TihanyiNorbert 推广；当噪声／高风险工具看待，**不要在未授权环境运行**。
- 地址：
  - X 原帖：https://x.com/TihanyiNorbert/status/2114720827698782527

### 5. Elastic Security Labs：Windows Endpoint Security Platform（WESP）逆向
- 微软推动 EDR 出内核；Elastic 分析 Insider 构建中的 `wesp.sys`／`espclient.dll` 等。
- 地址：
  - X 原帖：https://x.com/elasticseclabs/status/2114771560246489270
  - 文章：https://go.es.io/4zcdL2U

### 6. Osmedeus Docker 镜像重建（nuclei／httpx／amass 等从源码用 Go 1.27 构建）
- 地址：
  - X 原帖：https://x.com/mablanconav/status/2114789772531053034

本日无其它显著正式 C2／nuclei 版本发布。

## APT / Malware 分析

### 1. Gheist：被盗 GitHub token → Actions 日志泄密（无传统 C2）
- Wiz：自 9-15 起，攻击者用被盗 token 在可达仓库新建 `ci-sync-******` 分支、植入把 secrets 打进 Actions 日志的 workflow，再下载并删除 run。公开库有 GitHub 熔断；**私库与 GHES 不覆盖**。已恢复 13,500+ 分支／850+ 账号；部分后续见 AWS Secrets Manager 枚举。轮换所有可读 secret，吊销写权限 token。
- 地址：
  - X 原帖：https://x.com/wiz_io/status/2114661038947803570
  - X 原帖：https://x.com/Dinosn/status/2114654979307044941
  - X 原帖：https://x.com/CSec88/status/2114690652831441147
  - 文章：https://thehackernews.com/2026/10/gheist-uses-stolen-github-tokens-to.html
  - 文章（Wiz／X Articles）：https://x.com/i/article/2114659965629587457

### 2. 953 家网店（多为 Magento）长期恶意 JS loader
- Sansec／SecurityWeek／THN：自 2025-07 起，经 Magento `cms_block` 注入小 loader，C2 先区分「真人购物」与扫描器。关联域名随时间轮换（见 IoC）。查 CMS 块与结账页脚本。
- 地址：
  - X 原帖：https://x.com/SecurityWeek/status/2114700661111550428
  - X 原帖：https://x.com/TheHackersNews/status/2114782671276834984
  - X 原帖：https://x.com/securityaffairs/status/2114820058639675821
  - 文章：https://www.securityweek.com/953-online-stores-infected-in-long-lasting-malware-campaign/
  - 文章：https://thehackernews.com/2026/10/hackers-infect-953-online-stores-with.html

### 3. MopsStealer：abuse.ch 标出活跃 C2
- 荷兰 Podaon SIA 托管；域名／IP／端口见 IoC 节。
- 地址：
  - X 原帖：https://x.com/abuse_ch/status/2114712505029124503
  - 样本浏览：https://bazaar.abuse.ch/browse/signature/MopsStealer/
  - IoC：https://threatfox.abuse.ch/browse/malware/win.mops_stealer/

### 4. Microsoft Teams「IT Support」社工 → 远控／勒索
- Arctic Wolf Labs：重复模式——邮件轰炸后 Teams 外部聊天冒充 IT；大量 `*.onmicrosoft.com` 一次性租户与固定显示名；投递远控工具／恶意域名。
- 地址：
  - X 原帖：https://x.com/Dinosn/status/2114786567525179837
  - 文章：https://thehackernews.com/2026/10/attackers-use-microsoft-teams-it.html

### 5. Microsoft 365 token-replay（Huntress）
- 2026-07-14 至 09-22：AitM 偷会话后重放；约 20 万次失败登录回溯到 `193.26.115.0/24`；497 次成功登录，**97 账号／79 组织**失陷，注册 48 个恶意 Entra 设备。
- 地址：
  - X 原帖：https://x.com/Dinosn/status/2114654766701707430
  - 文章：https://thehackernews.com/2026/10/microsoft-365-token-replay-attacks.html

### 6. Omega AI：地下「全能」AI 平台
- SecurityBreak：聚合未受限模型、jailbreak、进攻工具与恶意软件变现指导，降低入门门槛。
- 地址：
  - X 原帖：https://x.com/fr0gger_/status/2114764603091550620
  - 文章：https://blog.securitybreak.io/inside-omega-ai-the-rise-of-all-in-one-underground-ai-services-e0a0f91199b4

### 7. Icarus RAT（广告阶段）
- 别名 Icarus777 推广原生 x86／x64 RAT：hVNC、会话劫持、凭据窃取、键盘记录、加密货币地址劫持等。
- 地址：
  - X 原帖：https://x.com/TheThreatWire/status/2114545328313831671

### 8. Lazarus／FlashHole 与后量子投递（Kaspersky，文章日期 10-21，今日继续传播）
- 针对韩国组织；LPEClient＋ML-KEM-1024 保护载荷投递；钓鱼页→GitHub→INISAFE／fsquirt→TechHub。防御向：限制非常规 GitHub raw／私库拉取、监控异常加密握手。
- 地址：
  - X 原帖：https://x.com/Root__Void/status/2114801823580045357
  - 文章：https://www.bleepingcomputer.com/news/security/lazarus-hackers-use-post-quantum-cryptography-for-malware-delivery/

### 9. AI coding agent 指令投毒（AGENTS.md → 恶意 npm）
- Forever Security：Downloads 里的 `AGENTS.md` 试图让 Codex 类代理安装已知恶意包 `function-color`（MALFEX 链）。代理默认信任工作区指令文件＋浏览器可静默落盘 Downloads。
- 地址：
  - X 原帖：https://x.com/Dinosn/status/2114641307985662052
  - 文章：https://thehackernews.com/2026/10/malicious-file-in-downloads-folder.html

### 10. Sliver C2 暴露面 IoC（orlof_v／Shodan）
- 地址：
  - X 原帖：https://x.com/orlof_v/status/2114731726119268751
  - GitHub：https://github.com/orlofv/Indicators/blob/main/SliverC2

### 11. 其他
- Check Point 10-26 Threat Intelligence Report：https://research.checkpoint.com/2026/26th-october-threat-intelligence-report/ ；X：https://x.com/Dinosn/status/2114774525946761691
- THN 周回顾（This2Shell／That2Shell）：https://thehackernews.com/2026/10/weekly-recap-this2shell-that2shell.html
- endurasecurity「十月四起供应链攻击」长文：https://x.com/i/article/2114709464016195585 ；X：https://x.com/endurasecurity/status/2114710096479486282
- Ryanair 域名凭据据称暗网兜售（PandaPixel）—待核实：https://x.com/DailyDarkWeb/status/2114756533732966654

## 地址／IoC 汇总

> IoC 已 defang（`[.]`），使用前请还原。

### PHP2Shell／KEV
- CVE-2026-109618、CVE-2026-109619（KEV due 2026-10-29）
- CVE-2026-114625、CVE-2026-110447（KEV due 2026-10-26）

### Magento／网店 loader 相关域名（Sansec／THN 报道，防御封锁）
- manulfie[.]click
- neswnsssn[.]click
- lanhd6549tdhse[.]top
- additionalver[.]com
- deepveindrilling[.]com

### MopsStealer（abuse.ch）
- 域名：mops[.]to
- 45.91.202[.]47:408
- 45.91.202[.]47:1488
- 45.91.202[.]146:408
- 45.91.202[.]146:1488
- https://bazaar.abuse.ch/browse/signature/MopsStealer/
- https://threatfox.abuse.ch/browse/malware/win.mops_stealer/

### M365 token-replay（Huntress／THN）
- 193.26.115[.]0/24（大量失败登录来源）

### Sliver C2（orlof_v，高置信）
- 157.245.246[.]149
- 168.138.207[.]32
- 213.145.86[.]42
- 66.78.40[.]197
- 清单：https://github.com/orlofv/Indicators/blob/main/SliverC2

### Teams IT 社工（Arctic Wolf／THN，示例租户域名模式）
- helpdeskteam365.onmicrosoft[.]com
- itendpoint365.onmicrosoft[.]com
- itcoreportal.onmicrosoft[.]com
- itadmin922.onmicrosoft[.]com
- corporateitservicellc.onmicrosoft[.]com

### Gheist
- 分支名前缀：`ci-sync-`＋6 随机字符
- User-Agent：`gheist`（GitHub API）

### 其他
- AI agent 投毒包名：function-color → function-flag（MALFEX）
- Redis／FortiSIEM／Ivanti／Wasmtime／Brotli／SPIP／内核 teql：见各 CVE 节链接；未见额外公开哈希则写「未见公开 IoC」
- **未见公开 IoC**（本窗口未抄到可用哈希／钱包）：Icarus RAT 广告帖、Omega AI 平台综述、Wasmtime 通告本身

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

## 来源搜索 URL

- CVE／PoC Latest：https://x.com/search?q=(CVE%20OR%20POC%20OR%20exploit%20OR%200day)&f=live
- CVE-2026 热门：https://x.com/search?q=%22CVE-2026%22&f=top
- 在野利用：https://x.com/search?q=(%22actively%20exploited%22%20OR%20%22zero-day%22)&f=live
- 厂商公告：https://x.com/search?q=(NetScaler%20OR%20Fortinet%20OR%20Cisco%20OR%20Ivanti)%20(exploited%20OR%20patch)&f=live
- GitHub 红队工具：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20BOF)&f=live
- 恶意软件分析：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)&f=live
- IoC：https://x.com/search?q=(IOCs%20OR%20%22C2%20server%22%20OR%20sha256)&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
