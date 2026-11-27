# X 安全情报晚报 · 2026-11-26（周四）

> 报告时间：2026-11-26 约 20:00（America/Santiago），即 2026-11-27 约 07:00（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-25 23:00 UTC 到 11-26 约 23:03 UTC（约 24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-26 22:59:06～23:02:18 UTC（约 3 分钟，CVE／POC／exploit 关键词噪声刷屏），所以加了 relevancy 补搜 25 条（11-26 01:00:02～17:50:00 UTC，约 16.8 小时），以及 SSM Agent／OpenSSL 定向 relevancy 19 条（11-26 00:25:47～23:02:18 UTC，约 22.6 小时）、昨日 KEV 相关（Juniper／Mitel／Xen Orchestra／GeoServer／PAN-OS 等）relevancy 25 条（11-25 23:03:25～11-26 22:04:35 UTC，约 23 小时）。窗口前段主要靠定向补搜、工具组与 LWiS List 补上。
> - 工具组 Latest 11 条覆盖 11-26 05:26:20～19:31:58 UTC（约 14.1 小时；第 2 屏 0 条）。窗口起点到 05:26 UTC 的缺口由 LWiS List 与 relevancy 补搜承担。
> - 威胁组 Latest 24 条只覆盖 11-26 19:59:21～22:58:05 UTC（约 3 小时），relevancy 补搜 25 条覆盖 11-25 23:29:53～11-26 22:50:57 UTC（约 23.35 小时）。
> - LWiS List（list:1239330068461244424 只读 Latest）共翻 9 屏，合并去重后 **178** 条，整体 11-25 23:03:32～11-26 22:55:49 UTC（约 23.87 小时，距窗口起点约 3.5 分钟；最晚一条距出报约 7 分钟）。
> **其他信源**：SecureFlow 的 all／community／blog 三路接口今日均返回 **HTTP 200**。all 拉取 200 条，本窗口（约 48 小时且不在 seen_ids 的 sf:id）新条目 **16**，其中 HackerOne 12 条、Seebug Paper 2 条、奇安信攻防社区 1 条、先知社区 1 条。community 分类 7 个源中「吾爱破解」因 updatedAt 为 2024-09-19 已跳过，其余 6 个源均 200，合计 600 条，本窗口新条目 **3**（与 all 中社区条目对应，按 sfl:原文链接去重后仍为这 3 条）。blog 分类 12 个源中「微信公众号」因 updatedAt 为 2025-02-17 已跳过，其余 11 个源均 200，合计 367 条，7 天窗口新条目 **0**。pwn.watch 订阅源已拉取（XML／JSON 均为 200；XML 50 条），**本窗口无新条目**（订阅源最后更新于 2026-11-10 01:13:32 GMT）。ExploitGrid exploits 与 KEV 期限均为 200：exploits 列表 100 条，48 小时窗口内新条目 **86**（列表最新 date 为 2026-11-26 12:46:16 UTC；其中 CRITICAL／HIGH 38 条），绝大多数是老 CVE 或自动收录的 GitHub PoC，只对与本窗口讨论／KEV 相关的条目展开，其余只计数。ExploitGrid KEV 期限接口返回 10 条，覆盖 11-25 入目录中的 8 条，**仍未包含** Xen Orchestra CVE-2026-133469 与 Danfoss CVE-2025-41450，期限以 CISA 官方为准。CISA KEV 目录当前仍为 **1805** 条（dateReleased 2026-11-25T19:48:12.4344Z），较昨日期无新增，**11-26 无新入目录条目**。nday.land「Just moved」（https://www.nday.land/?since=48h ，默认最低阶段 patch）公开 HTML 已拉取 4 页，均为 200，去重后阶段变化 **209** 条（11-26 有 94 条、11-25 有 105 条、11-24 有 4 条；另有窗口外置顶 6 条只计数）；为本 routine 首次采集，seen_ids 中尚无 ndl: 前缀，窗口内条目均视为新。噪声很大（大量 Drupal 贡献模块中低危 +POC），只展开 KEV／在野、本窗口高信号新 PoC，以及与 X／KEV／ExploitGrid 交叉的条目。AI/TLDR 订阅源 50 条，本窗口（约 36 小时，且不在 seen_ids）新条目 **20**，其中 category 为 security 的 **0** 条。Agent Use Cases RSS 60 条，本窗口（约 48 小时）新条目 **17**。本日为周四（America/Santiago），不加阮一峰周刊节；第 420 期已在 11-22 期收录（seen_ids 中已有）。
> **验收**：采集——X Latest 与 LWiS List 均已尝试，各 HTTP 信源已用浏览器 UA 拉取并按窗口筛选，失败项已如实写明。核验链接——主链接已用浏览器 UA 抽查：AWS 官方速报 2026-197-AWS、瑞士 NCSC／BACS 公告、Tropic Square 官方顾问、OpenSSL 2026-11-24 公告全文、SecurityWeek（Juniper）、SecurityAffairs（瑞士 AI agent）、先知社区文章、Athar 仓库与 GitHub API、CISA KEV 目录页均为 **200**。Drupal 官方 SA-CORE-2026-019／017 与安全列表返回 Cloudflare「Client Challenge」（不是 404，正文未出），保留官方 URL，技术事实以 X 转述、Cybersecurity News 报道与 nday.land 阶段记录为准；NVD／cve.org／MSRC 更新指南仍是前端壳。日文转述页 rocket-boys.co.jp 与 issoh.co.jp 换 UA 后仍 **403**，SSM 条目以已核验的 AWS 官方速报为准。AI/TLDR releases 详情页仍 **403**，报告保留订阅链接。Seebug Paper 条目页返回 **521**，保留原文链接并注明。forum.butian.net（奇安信攻防社区）从 box 出现 TLS／连接失败（不是 403），标注为「box 网络无法连接，浏览器可开」。成稿——每日十节齐全（非周末，无阮一峰节），无利用代码／payload／PoC 步骤；落盘与交付见文末。

## 今日摘要

- **AWS SSM Agent 默认注册密钥问题（CVE-2026-134069）在 X 上今天形成明显传播**。官方安全速报 2026-197-AWS 已于 11 月 23 日发布：2026-09-09 之前的 AWS 官方 Windows Server AMI 上，同一 AMI 启动的实例共享同一把 SSM 实例注册密钥；在 Default Host Management Configuration（DHMC）管理的实例上，本地非管理员用户可能取得该实例的 DHMC 角色凭证。CVSS v3.1 为 7.3（High），v4.0 为 8.2。**就地升级代理不能清除已写入的共享密钥**，官方建议用 9 月 9 日及之后的 AMI 替换实例；删除 Agent Vault 不是受支持的修复，且会破坏 DHMC 管理。@securityLab_jp 的转述帖获得 341 赞／95 转。
- **Drupal 警告新的严重访问绕过 CVE-2026-136716（SA-CORE-2026-019）已遭活跃利用**，可导致站点被接管。nday.land 显示该 CVE 今天进入 PoC 阶段并被置顶。与此同时，已在 11-24 进入 CISA KEV、联邦期限为 **明天（11-27）** 的 Drupal 核心安装器相关漏洞 **CVE-2026-132165** 也在今天出现公开 PoC（置顶，约 7 名研究者讨论）。请尽快按官方公告升级核心，并检查安装器接口是否仍暴露。
- **CISA KEV 今日无新增**（目录仍为 1805 条）。需要盯期限：今天（11-26）到期的有 MONAI Label CVE-2026-133968 与 N-able MailAssure CVE-2026-134624；明天（11-27）有 Optimizely CVE-2026-132224、AntiCsrf／CodePlex CVE-2026-131914，以及上述 Drupal CVE-2026-132165；11-28 则是昨天那批 10 条中的大多数（含 Juniper Session Smart CVE-2026-103406、Xen Orchestra CVE-2026-133469、Mitel／Danfoss 等）。ExploitGrid 今天还能看到 Juniper CVE-2026-103406 的公开 exploit／分析条目（只记「已有公开 exploit」，不链仓库）。
- **Tropic Square 今天发布 TROPIC01 安全顾问**：与 NinjaLab 的内部评估发现电磁侧信道弱点（理论上可提取芯片内 ECC 私钥），官方评分 Medium（CVSS 4.2），需要物理接触芯片、实验室设备并耗时数月；**固件 2.1.0（2026-08-07 已发布）已缓解**，官方称未见在野利用。
- 另外：OpenSSL 在 11-24 发布顾问（修复版计划 **12 月 1 日** 推出，均为低危 DoS／资源类；**官方列表中没有** X／HN 上流传的「CVE-2026-121481、CVSS 9.8、EVP_EncodeBlock 缓冲区溢出」）；@AirbyteHQ 提醒开源用户升级到 2.6.0 以修复 Java4Shell（CVE-2026-114938），并称部分平台版本与 9 个 connector 镜像曾被篡改，需要轮换凭证；瑞士 NCSC 确认境内首次出现有 AI agent 协助的攻击；X 上还在讨论 1Password 员工 GitHub 账号被入侵、PolinRider 向大量 GitHub 仓库投毒，以及 FIFA 遭入侵的报道。

## CVE / POC / 漏洞

### 1. AWS SSM Agent：CVE-2026-134069（默认注册密钥，官方速报 2026-197-AWS）

Amazon SSM Agent 用于通过 Systems Manager 管理 EC2。官方在 11 月 23 日 13:30 PST 发布重要速报：2026-09-09 之前发布的 AWS 官方 Windows Server AMI 中，实例注册组件使用了默认／共享加密密钥（CWE-1394），从同一 AMI 启动的实例共用一把注册密钥。若实例由 DHMC 管理，本地非管理员用户可能获取该实例的 DHMC 角色凭证。受影响版本为这些 AMI 中的 Amazon SSM Agent < 3.3.5226.0；**从受影响 AMI 启动的实例在就地升级代理后仍然受影响**，因为共享密钥不会随升级被替换。官方建议用 2026-09-09 及之后、已包含 3.3.5226.0 或更高版本的 Windows Server AMI 替换实例。删除 Agent Vault 不是受支持的修复方法，会导致 DHMC 管理的实例异常。在无法立即替换时，官方临时建议限制这些实例上非管理员本地用户的访问。致谢 The YOSS Platform。本窗口 X 上以日文安全媒体传播为主，@securityLab_jp 帖为 341 赞／95 转。

- 厂商公告：https://aws.amazon.com/security/security-bulletins/2026-197-aws/
- GitHub 公告编号（官方速报引用）：GHSA-rfpp-9v45-jjv4
- X 原帖：https://x.com/securityLab_jp/status/2125756730953089414 · https://x.com/hanadon_lab/status/2125813367818592394 · https://x.com/jpsharada/status/2125806559808893295 · https://x.com/Liberaliobot/status/2125845515111997465
- 日文转述页（换 UA 后仍 403，仅作交叉，事实以 AWS 速报为准）：https://rocket-boys.co.jp/security-measures-lab/aws-ssm-agent-cve-2026-134069-windows-ami-2026/

### 2. Drupal 核心：CVE-2026-136716 已遭活跃利用；CVE-2026-132165（KEV，期限 11-27）今日出现公开 PoC

Cybersecurity News 与 X 转述称，Drupal 警告高度严重的访问绕过 **CVE-2026-136716**（SA-CORE-2026-019）正在被活跃利用，可用于接管未修复站点。nday.land 将该条标记为 11-26「PoC published」并置顶。同一窗口还提到 SA-CORE-2026-017。已在 11-24 列入 CISA KEV、联邦期限为 **2026-11-27** 的 **CVE-2026-132165**（Drupal 核心安装器相关）今天也被 nday 标为公开 PoC，置顶讨论热度较高（约 7 名研究者）。Drupal 官方公告页用浏览器 UA 访问时返回 Cloudflare 挑战页（不是 404），下面保留官方 URL，细节以交叉来源为准。请尽快升级核心，并确认安装／更新界面未对公网暴露。nday 上同时出现大批 Drupal 贡献模块的中低危 +POC（仅计数，不展开）。

- 厂商公告：https://www.drupal.org/sa-core-2026-019 · https://www.drupal.org/sa-core-2026-017 · https://www.drupal.org/security
- 文章：https://cybersecuritynews.com/drupal-website-takeover-flaw/
- nday.land：https://www.nday.land/vuln/CVE-2026-136716 · https://www.nday.land/vuln/CVE-2026-132165
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- X 原帖：https://x.com/The_Cyber_News/status/2125879902801215847 · https://x.com/yabetchi_iPhone/status/2125747808322101447

### 3. CISA KEV 跟踪：今日无新增；多条期限落在 11-26 至 11-28

CISA 已知被利用目录仍为 **1805** 条，dateReleased 仍为 2026-11-25T19:48:12.4344Z，**11-26 没有新入目录的编号**。nday.land 把昨天那 10 条标记为 11-25「added to KEV」，与官方一致。X 上继续讨论这批漏洞，尤其是 Juniper Session Smart。ExploitGrid 的 active-deadlines 仍列出其中 8 条，未列出 CVE-2026-133469 与 CVE-2025-41450，期限以 CISA 官方为准。

需要优先关注的联邦期限：

- **今天（2026-11-26）**：CVE-2026-133968（Project MONAI／MONAI Label，11-23 入目录）；CVE-2026-134624（N-able MailAssure，11-23 入目录）。
- **明天（2026-11-27）**：CVE-2026-132224（Optimizely Web Experimentation）；CVE-2026-131914（Idunno AntiCsrf／CodePlex AntiCSRF）；CVE-2026-132165（Drupal Core，见上节，今日已有公开 PoC）。
- **2026-11-28**：CVE-2026-103406（HPE／Juniper Session Smart Conductor 与 Router，未认证 root 命令注入，修复版本仍为多方转述的 7.0.5／7.1.7／7.2.3）；CVE-2026-133469（Vates Xen Orchestra）；CVE-2026-133323／133324／133275／133303（Mitel MiCollab）；CVE-2023-25914／CVE-2023-25915（Danfoss AK-SM 800A）。CVE-2026-133311 与 CVE-2025-41450 期限仍为 12-09。

Juniper CVE-2026-103406：X 上继续强调 Juniper 已收到利用报告、已进 KEV；SecurityWeek 有跟进报道。ExploitGrid 在 11-25 收录了该编号的公开 exploit／分析条目，**只记「已有公开 exploit」这一事实，不链 PoC 仓库**。

- CISA 昨日警报：https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 文章：https://www.securityweek.com/critical-juniper-session-smart-conductor-flaw-exploited-in-attacks/ · https://tldrcve.com/juniper-ssr-conductor/
- ExploitGrid（佐证，不链 PoC 仓库）：https://exploitgrid.net/vulnerabilities/CVE-2026-103406
- nday.land：https://www.nday.land/vuln/CVE-2026-103406 · https://www.nday.land/vuln/CVE-2026-133469
- X 原帖：https://x.com/tldrcve/status/2125975155335925825 · https://x.com/threatpodium/status/2125731777498972435 · https://x.com/nietechniczny/status/2125839730575020380 · https://x.com/Dinosn/status/2125891346732908561


### 4. Tropic Square TROPIC01：电磁侧信道弱点（官方顾问，固件 2.1.0 已缓解）

Tropic Square 今天发布顾问：2026 年 4 月与合作实验室 NinjaLab 的内部评估发现 TROPIC01 存在电磁侧信道弱点，理论上可在测量芯片工作时泄漏的信号后提取其中存储的 ECC 私钥。官方评分为 Medium（CVSS 4.2），并写明攻击者需要拿到物理芯片、具备专业能力与实验室设备，估计耗时 3–5 个月。**固件 2.1.0 已于 2026 年 8 月 7 日发布并有效缓解**；官方称已按协调披露提前通知商业伙伴，且没有在野利用证据。完整评估报告计划随后放到其 GitHub。@tropicsquare 与 @NinjaLabFr 均发了原帖。

- 厂商公告：https://www.tropicsquare.com/news-and-events/tropic01-security-advisory-internally-found-electromagnetic-side-channel-weakness-fixed-in-firmware-2-1-0
- X 原帖：https://x.com/tropicsquare/status/2125892399293427921 · https://x.com/NinjaLabFr/status/2125937146242478150

### 5. OpenSSL 11-24 官方顾问（修复版计划 12 月 1 日）；澄清 X／HN 上的 CVE-2026-121481 传闻

OpenSSL 于 2026 年 11 月 24 日发布安全顾问，相关修复已进入公开仓库，**发行版计划于 2026 年 12 月 1 日推出**。顾问列出的均为 **Low** 严重性，主要包括：CVE-2026-84786（非 SMTP DANE 客户端可能空指针解引用导致崩溃）；CVE-2026-107494（QUIC RETIRE_CONNECTION_ID 队列在重传场景下仍可能被打满，是 CVE-2026-84784 修复不完整的后续）；CVE-2026-121482（在启用 CRL 检查时验证恶意构造的 CMS／PKCS#7 SignedData 可能消耗过量 CPU）；CVE-2026-84785（QUIC 流乱序分片重组节点过多导致内存占用上升）。受影响分支因条目而异，常见升级目标为 OpenSSL 4.1.1／4.0.4／3.5.10。

需要澄清：窗口末尾 X 与 Hacker News 上流传「OpenSSL EVP_EncodeBlock() 缓冲区溢出、CVE-2026-121481、CVSS 9.8」。用浏览器 UA 核对官方 secadv 索引、vulnerabilities 页面以及 20261124 公告全文，**均未出现 CVE-2026-121481**，相近编号是低危的 CVE-2026-121482。本期不把该传闻当作已确认的高危漏洞展开。

- 厂商公告：https://www.openssl.org/news/secadv/20261124.txt · https://www.openssl.org/news/vulnerabilities.html
- X 原帖（传闻，未获官方列表支持）：https://x.com/flexdinesh/status/2126089192203800925
- 文章／讨论：https://news.ycombinator.com/item?id=50569226

### 6. Airbyte：升级 2.6.0 修复 Java4Shell（CVE-2026-114938），并轮换被篡改镜像的凭证

@AirbyteHQ 今天发布安全说明：开源用户应升级到 **Airbyte 2.6.0**，其中修复了 Java4Shell（CVE-2026-114938）；同时识别到部分平台版本以及 **9 个 connector 镜像**曾被篡改，若运行过这些版本，应升级对应 connector 并轮换其凭证。这是供应链方向的信号，优先处理暴露在构建／生产环境中的自托管实例。

- X 原帖：https://x.com/AirbyteHQ/status/2125799181709451490
- GitHub 安全公告列表：https://github.com/airbytehq/airbyte/security/advisories
- ExploitGrid（佐证该编号近日出现公开 exploit 条目，不链仓库）：https://exploitgrid.net/vulnerabilities/CVE-2026-114938

### 7. 其他跟进与本窗口公开 PoC（防御向摘要）

- **微软 11 月更新与 NTLM／SSO**：X 上继续发酵「11 月安全更新可能导致部分使用 NTLM 的第三方应用与设备登录失败」。这是昨日已报过的议题，今天 @The_Cyber_News 的跟进帖获得 312 赞／81 转。文章：https://cybersecuritynews.com/november-update-breaks-authentication/ ；X 原帖：https://x.com/The_Cyber_News/status/2125900475891593420
- **Palo Alto PAN-OS 利用链跟进**：@vineetdaniel 的每日简报重申官方已确认攻击者把 PHP2Shell（CVE-2026-109618／109619）与内核本地提权 Fragnesia（CVE-2026-46300）链式利用，目标仍是公网暴露的管理口。X 原帖：https://x.com/vineetdaniel/status/2125780345068912952
- **PHP 一组 UAF／明文暴露今天被 nday 标为公开 PoC**（约 T+7d），ExploitGrid 也出现对应 HIGH／CRITICAL 条目：CVE-2026-129182、CVE-2026-129481、CVE-2026-129291（PHP-FPM epoll 本地提权）、CVE-2026-128064（大小写混用的 HTTPS／FTPS URL 可能导致明文传输）。只记「已有公开 PoC」，不链仓库。nday：https://www.nday.land/vuln/CVE-2026-129182 · https://www.nday.land/vuln/CVE-2026-129291
- **Openfind MailGates／Mail2000 命令注入**（CVE-2026-137389／CVE-2026-137390）在 nday 上为 11-26 新披露且当天出现公开 PoC（T+0d）。来源：nday.land。https://www.nday.land/vuln/CVE-2026-137389 · https://www.nday.land/vuln/CVE-2026-137390
- **OpenBSD SSH「SSHole」CVE-2026-123158**：ExploitGrid 在 11-25／11-26 连续收录多条该编号的公开 exploit 条目，只记「已有公开 exploit」。https://exploitgrid.net/vulnerabilities/CVE-2026-123158
- **Revive Adserver**：nday 今天把一组 T+0d 的 XSS／SQL 注入／访问控制等问题标为公开 PoC（CVE-2026-133202 至 CVE-2026-133211 一带），与 SecureFlow 中一批 HackerOne 公开报告相对应，见「SecureFlow 信息流精选」。
- **其他只计数不展开**：nday 窗口内约 199 条 11-25／11-26 阶段变化里，大量为 Drupal 贡献模块中低危访问绕过 +POC、GitLab 较旧编号的重复 PoC、以及窗口外置顶项（如 11-18 的 NGINX HTTP/2 CVE-2026-123007、11-19 披露的 nfsd 预认证问题 CVE-2026-99362、11-20 的 Cisco Expressway KEV CVE-2026-76466 等）。ExploitGrid 48 小时内 86 条新 exploit 中，老编号（Log4Shell、CVE-2024-4577 等）的重复 PoC 只计数。

## 工具与 GitHub 发布

### 1. Athar：用 YAML 描述服务指纹（@cyb3rops 与 @MalGamy12）

@cyb3rops 今天宣布与 @MalGamy12 发布 Athar，定位为服务指纹标准：把标题、正文、头字段、favicon hash、证书等可观察特征写成一条 YAML 规则，再用于扫描与识别，作者把它比作 Sigma 早期的感觉。仓库 https://github.com/Athar-HQ/Athar 目前约 53 star（GitHub API，创建于 11-24，11-26 仍有推送）。LWiS 与工具检索中均有讨论。

- GitHub：https://github.com/Athar-HQ/Athar
- X 原帖：https://x.com/cyb3rops/status/2125871882297557186

### 2. Claude-BugHunter 仍在 GitHub 趋势（约 23.8k star）

@trending_repos 显示 Claude-BugHunter 继续登上趋势：面向已授权测试的 Claude Code 技能包（85 个技能等），过去 24 小时约 +1600 star，总计约 23,783。昨日已报过，今天只作热度跟进。仓库明确只应用于有书面授权的资产。

- GitHub：https://github.com/elementalsouls/Claude-BugHunter
- X 原帖：https://x.com/trending_repos/status/2125924697183506818

### 3. @theflow0 分享 SAS 会议幻灯（PS5 Linux）

@theflow0 今天放出上个月在巴厘岛 TheSAScon 的幻灯，链接指向其 Presentations 仓库中的 2026-sascon-ps5-linux.pdf，获得 419 赞／38 转。

- GitHub／PDF：https://github.com/TheOfficialFloW/Presentations/blob/master/2026-sascon-ps5-linux.pdf
- X 原帖：https://x.com/theflow0/status/2126008026562011574

## APT / Malware 分析

### 1. 瑞士 NCSC：首次确认有 AI agent 协助的网络攻击

SecurityAffairs 转述、@Dinosn 转发：瑞士国家网络安全中心（NCSC／BACS）称近日首次接到「攻击过程有 AI agent 协助」的报告，受害者包括至少两个行业的关键基础设施运营方；在 NCSC 已知的这类案件中，攻击均成功进入受害 IT 系统。官方将这类工具称为 Agentic Offensive Frameworks，并提醒它们同时被用于授权渗透测试（双用途）。攻击目标仍以弱口令、已知漏洞和互联网暴露系统为主。官方建议尽快修补暴露面。美国 IC3 稍早也有相关 CSA 可作交叉（https://www.ic3.gov/CSA/2026/261113.pdf）。

- 官方公告：https://www.bacs.admin.ch/en/26-ki-agenten-1-en
- 文章：https://securityaffairs.com/204004/hacking/switzerland-confirms-first-ai-agent-cyberattacks-on-local-organisations.html
- X 原帖：https://x.com/Dinosn/status/2125784809603825733

### 2. 1Password：员工 GitHub 账号被入侵后的客户数据与供应链讨论

BleepingComputer 报道、X 上继续讨论：1Password 在一名员工的 GitHub 账号被入侵后出现客户数据被窃。@payloadartist 指出，比起「保险库仍然安全」的表述，更值得看的是攻击者据报获得了源代码与 CI／CD 访问，并向后端推送了恶意代码。@ajrgd 补充，在服务端被入侵的时间窗口里，团队／家庭保险库的邀请、SCIM 与开通流程依赖的是认证与授权，而不是端到端加密。本期未从公开材料中抄到可核验的 IoC。请以厂商官方说明为准，关注会话撤销、凭证轮换和 CI 信任链。

- 文章：https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/
- X 原帖：https://x.com/Dinosn/status/2125784661003583684 · https://x.com/payloadartist/status/2125789442065715490 · https://x.com/ajrgd/status/2126049695856205993

### 3. 朝鲜关联 PolinRider：超 7600 个 GitHub 仓库被投毒

The Hacker News 报道、@Dinosn 转发：与朝鲜有关联的 PolinRider 活动向超过 7600 个 GitHub 仓库投毒以传播恶意软件。请核对自己依赖的 GitHub 来源、钩子和 Action，优先检查异常提交与陌生维护者变更。本期只记录这一公开报道，不转载样本或利用细节。

- 文章：https://thehackernews.com/2026/11/north-korea-linked-polinrider-poisons.html
- X 原帖：https://x.com/Dinosn/status/2126020301607879087

### 4. FIFA 称遭受网络攻击，涉及个人与业务信息

SecurityWeek 报道、@Dinosn 转发：FIFA 表示自己成为网络攻击的受害者，攻击者访问了「个人与业务信息」。未见本窗口的官方技术报告或公开 IoC，细节以后续厂商／执法通报为准。

- 文章：https://www.securityweek.com/fifa-says-it-has-been-victim-of-a-cyberattack-accessing-personal-and-business-information/
- X 原帖：https://x.com/Dinosn/status/2126020223312724130

### 5. 勒索与泄露站通告（均未见官方确认）

威胁组检索中出现多起泄露站／通告类帖，均为「声称」或「据报」，本期不当作已确认事件：美国公用事业 Eversource Energy、人工心脏厂商 SynCardia Systems（The Gentlemen）、食品企业 Sweet Darling Sales、印尼移民总局（HYFLOCK，声称 10–11 天内公布数据）、以及 Air Canada、iTradePro Academy、西班牙临床数据库、PumpTech、New Plymouth School District 等。另有 Webworm 定制 SoftEther VPN 用于隐蔽接入、孟加拉相关团体声称篡改网站等通报，同样未见官方确认。

- X 原帖（HYFLOCK／印尼移民总局通告）：https://x.com/FalconFeedsio/status/2125916205076934847

## SecureFlow 信息流精选

本窗口 SecureFlow 高信号且 X 主检索中未作为独立事件展开的条目如下。community 新 3 条与 all 接口中的社区条目为同一批原文，按链接合并。

### community

- **先知社区**：ELF DT_RELR 压缩重定位导致 objdump 审计盲区分析与绕过（2026-11-25 10:59）。原文：https://xz.aliyun.com/news/93459
- **奇安信攻防社区**：core_pattern 里的命令注入——%e 如何变成提权入口（2026-11-26 09:46）。原文：https://forum.butian.net/share/5215 （从 box 访问出现 TLS／连接失败，不是 403；标注为「box 网络无法连接，浏览器可开」）
- **Seebug Paper**：PseuDRAGON：面向封闭网络金融数据假名化的知识引导本地大语言模型（2026-11-26 16:22）。原文：https://paper.seebug.org/3538 （条目页返回 521，保留链接）
- **Seebug Paper**：MirrorGuard：防御 LiDAR 感知免受被动镜面攻击（2026-11-25 16:32）。原文：https://paper.seebug.org/3537 （条目页返回 521，保留链接）

### blog

本日无显著更新。

### BugBounty

- **Nextcloud Notes**（HackerOne，2026-11-26）：上传文件名允许 Unicode RTLO 字符，导致可执行文件上传与误导性 UI。https://hackerone.com/reports/3490059
- **Revive Adserver 相关一组公开报告**（HackerOne，多条时间为 2026-11-25）：包括基于错误的 SQL 注入、includebanner 数组键 SQL 注入、VAST XML 注入替换播放跟踪、跨广告主跟踪器关联、反射 XSS、公式注入、未认证跨跟踪器变量注入等。可与 nday 上今天标记为公开 PoC 的 Revive Adserver 编号交叉。示例：https://hackerone.com/reports/4216475 · https://hackerone.com/reports/4228805 · https://hackerone.com/reports/4209444 · https://hackerone.com/reports/4195061 · https://hackerone.com/reports/4215622

## AI/TLDR 动态

来自 https://ai-tldr.dev/ 订阅源。本窗口新条目 **20** 条，其中 category 为 security 的 **0** 条（未出现可并入 CVE／工具／APT 节的安全类条目）。AI/TLDR 的 releases 详情页用浏览器 UA 访问仍返回 **403**，下面保留订阅条目链接；原始来源以条目标题中的发布方为准，未强行补未核验的官网路径。video／纯 showcase 类低信号条目（llm.asm、GRH in Lean 等）只在文末计数。

今天 AI 圈的主线有三条：一是数学与复杂性讨论升温——OpenAI 内部模型的预印本声称反驳了多项式 Hirsch 猜想，Scott Aaronson 发文讨论这些结果对 P ≠ NP 的意味；二是产品与工作台继续下沉——Claude 的电脑操控进入 Team／Enterprise 测试，ChatGPT 开始合并 Chat 与 Work 标签、把 Health 和 Space 扩到更多端与档位；三是治理与工作流程——纽约州禁止内置 AI 聊天的玩具，谷歌要求 Workspace 里的 AI agent 改走其 MCP 服务器并调整配额计费，纽约时报要求摄影记者暂时避开 Photoshop 2027 以免误触生成式功能。

### 模型、论文与研究

- OpenAI 预印本讨论多项式 Hirsch 猜想被证伪：https://ai-tldr.dev/releases/openai-math-polynomial-hirsch-disproof/
- Scott Aaronson：「Holy shit」，AI 数学结果指向 P ≠ NP：https://ai-tldr.dev/releases/scott-aaronson-holy-shit-magnitude-nov25/
- go/codegolf 基准：GPT-6.2 Astra 据报首次打破谷歌 2015 年内部竞赛的人类纪录：https://ai-tldr.dev/releases/bjin-go-codegolf-benchmark-gpt-6-2-astra/
- 蚂蚁集团开源 Ling-3.2-air（124B 多模态 MoE，约 5.5B 激活，偏工作流与文档）：https://ai-tldr.dev/releases/inclusionai-ling-3-2-air/

### 工具与产品

- Anthropic：Claude computer use 进入 Team／Enterprise 测试，可在授权范围内看到屏幕并操作桌面应用：https://ai-tldr.dev/releases/anthropic-claude-computer-use-team-enterprise/
- Anthropic：Claude 可向已连接应用收发文件；月度回顾 Reflect 出测试并覆盖 Claude Code 与 Cowork；iOS 端外观更新：https://ai-tldr.dev/releases/anthropic-claude-connector-file-transfers/ · https://ai-tldr.dev/releases/anthropic-claude-monthly-recap-out-of-beta/ · https://ai-tldr.dev/releases/anthropic-claude-mobile-refreshed-look/
- OpenAI：开始向部分 Pro 用户测试把 Work 标签并入普通 Chat；手机端改为 Home／Explore；Health 扩展到 Android 与桌面；Space 向 Plus 放开；Responses API 增加医疗场景配置；并修复 GPT-6.2 用量计费，Astra／Sol 额度会比之前更快用完：https://ai-tldr.dev/releases/openai-chatgpt-combined-chat-work/ · https://ai-tldr.dev/releases/openai-chatgpt-new-mobile-experience/ · https://ai-tldr.dev/releases/openai-chatgpt-health-android-desktop-dots/ · https://ai-tldr.dev/releases/openai-chatgpt-space-plus-rollout/ · https://ai-tldr.dev/releases/openai-responses-api-healthcare-configurations/ · https://ai-tldr.dev/releases/openai-gpt-6-2-usage-billing-fix/
- Command Code 推出 Moat：每月 5 美元的模型路由，号称不加路由费：https://ai-tldr.dev/releases/commandcode-moat/

### 行业动态

- 谷歌 Workspace 附加条款：让 AI agent 改用其 MCP 服务器，并带来新的配额与计费：https://ai-tldr.dev/releases/google-workspace-ai-tools-addendum-mcp/
- 纽约州禁止内置 AI 聊天的玩具（签署后 90 天生效、为期五年），为加州之后第二个出台类似禁令的州：https://ai-tldr.dev/releases/new-york-ai-chatbot-toy-ban/
- 纽约时报要求摄影记者避开 Photoshop 2027，担心新的 AI 功能太容易被误触发：https://ai-tldr.dev/releases/nyt-photographers-avoid-photoshop-2027/

showcase／演示类（llm.asm、GRH in Lean 缩短证明等）2 条，只计数不展开。

## Agent 用例动态

来自 https://agentusecases.ai/ ，本窗口新条目 **17** 条（RSS 共 60 条）。今天人们主要仍在用 coding agent 做工程自动化（PR 评审、补测试、数据研究、把优化假设写成可证伪的循环），同时出现一批「让 agent 去挣钱／运营网站」的实验——结果两极：有人用带分工的子 agent 做成联盟营销站并声称 30 天收入 1422 美元，也有人让自主 agent 连续多日尝试仍是 0 美元甚至账号被封。个人生活向的自动化（早餐流程、扫地、营养数据看板）和销售线索清洗也不少。与安全／权限最相关的一条放在最前：用小型工具门控模型决定 agent 能否执行退款动作。

### 安全与权限（优先）

- 用工具门控模型拦退款动作：作者拿 Strands Decider 2B 做门控，在 16 个退款案例上决定 agent 该不该动手，并用 Nova Pro 当评判。https://agentusecases.ai/use-case/gate-refund-actions-with-a-tool-gate-model

### 工程与研究

- 在 GitHub Actions 里自动跑 PR 评审、分析测试失败、生成 changelog，并把 issue 规格变成实现草稿（Claude Code）。https://agentusecases.ai/use-case/automate-pr-reviews-and-changelogs-with-github-actions
- 给被遗忘的 Node.js 后端补 23 个 vitest，两轮修好 4 个失败，约 15 分钟（Claude Code）。https://agentusecases.ai/use-case/add-unit-tests-to-a-forgotten-node-js-backend
- 用可证伪假设循环做性能优化，据报把 KaHIP 加快 3.9 倍、VieCut 加快 8.9 倍（Claude Code）。https://agentusecases.ai/use-case/optimize-code-through-an-automated-falsifiable-hypothesis-lo
- 用 coding agent 做数据研究项目（Claude Code）。https://agentusecases.ai/use-case/run-data-research-projects-with-a-coding-agent
- 为社会科学学术工作配置 Claude Code。https://agentusecases.ai/use-case/support-academic-social-science-work-with-a-coding-agent-set
- 在 AWS 上搭建多 agent 系统（课程毕业项目）。https://agentusecases.ai/use-case/build-a-multi-agent-system-on-aws

### 经营、销售与内容

- 用带分工的子 agent 搭建并运营联盟营销站，作者称 30 天收入 1422 美元（Grok Bot）。https://agentusecases.ai/use-case/build-and-run-an-affiliate-marketing-site-with-sub-agents
- 让 Claude Code 带着记忆和决策日志连续 31 个会话「经营」生意，五个市场合计收入 0 美元。https://agentusecases.ai/use-case/let-an-agent-run-a-business-autonomously-from-zero
- 自主 agent 尝试挣到第一块美元，12 天后仍是 0 美元，且多次被封号。https://agentusecases.ai/use-case/have-an-autonomous-agent-try-to-earn-its-first-dollar
- 把销售线索找到、补全并推进 HubSpot（Claude + Clay）。https://agentusecases.ai/use-case/find-enrich-and-push-sales-prospects-into-hubspot
- 用 Claude 做内容选题、写稿、生成短视频并定时发 TikTok；或先做成 CSV 再导入 Buffer／Metricool。https://agentusecases.ai/use-case/run-content-marketing-and-tiktok-posting-with-claude · https://agentusecases.ai/use-case/prepare-bulk-social-posts-for-buffer-or-metricool

### 生活与地产

- 为孩子做一键早晨流程，并在猫砂盆工作后调度扫地机（Claude）。https://agentusecases.ai/use-case/build-morning-routine-and-vacuum-automations
- 用 Claude in Chrome 把 Cronometer 与 Fitbit／Google Health 数据汇总到一块看板。https://agentusecases.ai/use-case/pull-nutrition-and-fitness-data-into-one-dashboard
- 从 Redfin 筛选可能的动机卖家、以及用 MCP 做租金与翻修测算（后两条偏教程／厂商示例，不是已核实的成交案例）。https://agentusecases.ai/use-case/source-motivated-seller-real-estate-deals-from-redfin-listin · https://agentusecases.ai/use-case/analyze-a-rental-property-deal-with-comps-and-rehab-costs

## 地址／IoC 汇总

未见公开 IoC。本窗口的勒索／泄露站条目多为受害者名称与通告，没有随帖给出可核验的样本哈希、C2、IP 或钱包地址；1Password、PolinRider、FIFA 与瑞士 AI agent 攻击的公开报道也未在本期采集到可原样抄录的 IoC。若后续厂商或 CERT 公布指标，再行补充。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）: https://x.com/i/lists/1239330068461244424
- 博客清单: https://blog.badsectorlabs.com/files/blogs.txt （本地: lwis-sources/blogs.txt）
- CISA KEV: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD: https://nvd.nist.gov/
- Risky Business: https://risky.biz/
- tl;dr sec: https://tldrsec.com/
- SecureFlow 安全信息流: https://secureflow.scope-sentry.top/all （只读接口: https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200）
- SecureFlow 社区: https://secureflow.scope-sentry.top/community （源列表: https://secureflow.scope-sentry.top/api/rss/category?category=community）
- SecureFlow 博客: https://secureflow.scope-sentry.top/blog （源列表: https://secureflow.scope-sentry.top/api/rss/category?category=blog）

### Agent Use Cases（用户 2026-11-05 加入，单独成节）

- 站点：https://agentusecases.ai/ ，持续扫描收录人们实际用 AI agent 做的事。
- RSS：https://agentusecases.ai/feed.xml （约 60 条，覆盖约 3 天，每天约 20 条，pubDate 为 GMT，带浏览器 UA 访问）。
- 去重键：auc:<use-case 链接>。

### 阮一峰《科技爱好者周刊》（用户 2026-11-05 加入，仅周末版）

- 博客：https://www.ruanyifeng.com/blog/index.html ；订阅源：https://www.ruanyifeng.com/blog/atom.xml
- 周刊一般每周五北京时间早上发布；报告日期（Santiago）为周六的那期收录 GitHub 项目和有趣文章。去重键：ryf:<周刊链接>。

### AI/TLDR（每日，ai-tldr.dev）

- 首页：https://ai-tldr.dev/
- Atom 订阅源：https://ai-tldr.dev/feed.xml （约 50 条／6 天；category 含 security、model、tool、repo、paper、article 等）
- security 类条目与 X／SecureFlow 交叉合并；去重键 atl:条目链接

### pwn.watch 与 ExploitGrid（2026-11-12 加入，与 X 交叉）

- pwn.watch 实时安全事件 RSS：https://pwn.watch/feed.xml （JSON：https://pwn.watch/feed.json）
- ExploitGrid 最新公开 exploit：https://api.exploitgrid.net/api/exploits?page=1&limit=100
- ExploitGrid KEV 修补期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines
- 页面：https://exploitgrid.net/vulnerabilities/<CVE> 、https://exploitgrid.net/exploits/<internalId>

### nday.land（2026-11-27 加入，与 X 交叉，不单独成节）

- 首页「Just moved」：https://www.nday.land/ ；采集用 https://www.nday.land/?since=48h （与 ?since=2d 等价；默认最低阶段 patch）
- 漏洞页：https://www.nday.land/vuln/<CVE> ；信源说明：https://www.nday.land/src ；讨论热度：https://www.nday.land/discussed
- 去重键：ndl:<CVE编号>:<阶段>:<变化日期>（阶段为 KEV／POC／ANA／PAT／ITW／DIS）
- 只用公开 HTML（带浏览器 UA），不登录；官方 API 与 feed.xml 需账户令牌，未提供令牌时不调用。只写阶段变化与「已有公开 PoC」并附 nday 条目页，不链 PoC 仓库。

## 来源搜索 URL

- X Latest CVE／POC／exploit／0day：https://x.com/search?q=(CVE%20OR%20POC%20OR%20PoC%20OR%20exploit%20OR%200day%20OR%20%220-day%22)%20-is%3Aretweet&f=live （25 条，仅约 3 分钟；另做 relevancy 与定向补搜）
- X Latest github.com + C2／red team／nuclei：https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20redteam%20OR%20nuclei%20OR%20implant)%20-is%3Aretweet&f=live （11 条，约 14.1 小时）
- X Latest malware analysis／threat report／threat actor：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)%20-is%3Aretweet&f=live （Latest 约 3 小时；relevancy 补搜约 23.35 小时）
- LWiS List：https://x.com/i/lists/1239330068461244424 （9 屏，178 条，约 23.87 小时）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条，窗口新 16）
- SecureFlow community 源列表：https://secureflow.scope-sentry.top/api/rss/category?category=community （6 个源 600 条，窗口新 3；吾爱破解已跳过）
- SecureFlow blog 源列表：https://secureflow.scope-sentry.top/api/rss/category?category=blog （11 个源 367 条，7 天窗口新 0；微信公众号已跳过）
- pwn.watch RSS：https://pwn.watch/feed.xml （50 条，窗口新 0，最后更新 2026-11-10 01:13:32 GMT）
- ExploitGrid exploits：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （100 条，48 小时新 86，CRITICAL／HIGH 38；只展开交叉项）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （10 条）
- nday.land Just moved：https://www.nday.land/?since=48h （4 页，去重 209 条阶段变化；11-26 有 94 条、11-25 有 105 条）
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （1805 条，11-26 新增 0）
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条，窗口新 20，security 0）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条，窗口新 17）
- 阮一峰周刊订阅源：https://www.ruanyifeng.com/blog/atom.xml （第 420 期已收录，本日非周末不出节）

覆盖区间：X 为 2026-11-25 23:00 UTC 至 11-26 约 23:03 UTC；SecureFlow／ExploitGrid／nday／Agent Use Cases 约 48 小时（blog 分类 7 天）；AI/TLDR 约 36 小时；pwn.watch 订阅源无本窗口新条目。



## 落盘与交付

- Box：/home/box/workspace/security-watch/reports/2026-11-26-x-security-digest.md
- 本机（PRIMARY）：/Users/kenny1337/Desktop/_05_项目/X安全情报晚报/2026-11-26-x-security-digest.md
- state.json 已更新 last_report_date=2026-11-26，并写入本窗口新的 seen_ids（x／sf／sfl／egx／ndl／atl／auc）。
