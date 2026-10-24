# X 安全情报晚报 · 2026-10-23

> 搜集窗口：圣地亚哥时间 **2026-10-22 20:15 至 2026-10-23 20:14**（America/Santiago／UTC-3，名义 24 小时，接昨晚窗口）。X 搜索参数：`start_time=2026-10-22T23:15:00Z`，`end_time=2026-10-23T23:14:00Z`（最后一个专题查询放宽到 23:20Z）。实际抓到的帖子从 **10-22 20:34** 到 **10-23 20:14**（UTC-3），**实际有效覆盖约 23 小时 40 分**；开头约 19 分钟没有抓到帖子，其余时段没有明显空白。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`，Latest／recency 和 relevancy 两种排序；`get_posts_by_ids` 读重要原帖全文）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** t.co 用 curl 跟随 HTTP 跳转展开：粗筛帖中共 **286** 个短链，**286** 个都展开到非 t.co 目标；纯图片／视频链接不列。
> 本轮各类查询：
> - A 类（CVE／0day／PoC）：recency、relevancy、在野、午间切片，共四次
> - B 类（GitHub 红队／C2／nuclei）：两次
> - C 类（malware analysis／threat report／threat actor、IoC）：三次
> - LWiS List：500 名成员分 10 段做 `from:` 批次
> - 核心媒体／厂商账号：两段；IoC 猎人账号：一次
> - 专题（Collabora／Brotli·HTTP2Shell／FortiSIEM·Arista／PHP2Shell／PHP CVE-2026-115560·BlackX）：五次
> - 原帖全文读取：一次（14 个 ID）
>
> 合计 **28 次有效 X 读取，0 次 429**（当日配额剩余约 972/1000）。
> **覆盖说明**：每次查询最多返回 25 条。PHP2Shell／Brotli 热帖会占满宽泛查询，所以用专题查询补齐。剔除了广告／营销、空转发、「Black October」类复读、`lyrie_ai` 类自动刷屏、Grok 自动回复，以及 `$HTTP2SHELL` 代币炒作帖（SolTokenScan、JohnCryptopeow 等）。
> 窗口内去重后 **503** 条帖子（与 seen_ids 6683 条**零重叠**）。关键词粗筛得 **352** 条安全相关新帖，按最先命中的批次归类：**A90／B23／C49／LWiS48／核心＋IoC 猎人47／专题95**。下文实际引用约 100 条。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**（`/workspace/enrich-2026-10-23/`）：CISA KEV JSON 和 CISA 新增公告；SecurityWeek（Arista VCO、Storm-0940／Artex、Atlassian）；BleepingComputer（Arista、Popcorn Time）；THN（Node2Shell、SOCRadar Phantom、BlackX、Pillow、Ruby Onigmo、PHP2Shell／Mirai、PHP CVE-2026-115560、k0t）；Unit 42 PHP 简报（10-23 更新）；Microsoft Security Blog（LiteLLM 1.107.0）；patchtheplanet.org/brotli；securityonline（FortiSIEM）；Group-IB（SiriusQT）；pwn.watch（Collabora）。NSA 公告页对本机只返回空壳，内容以 @NSACyber 原帖为准。
> GitHub API 核对了 nuclei／nuclei-templates／Sliver／BloodHound／NetExec／Mythic／impacket／Havoc／AdaptixC2／httpx：窗口内只有 **nuclei-templates v10.5.1**（10-23 08:19 UTC-3，含 PHP2Shell 主动崩溃检测模板），其余没有新的正式 release。
> **CISA KEV：catalogVersion 2026.10.23／1756 条，Δ+2**（相对昨天的 2026.10.21／1754）。`dateReleased` 为 2026-10-23 16:30 UTC-3。
> - **新增（均 10-23 入列，10-26 到期，勒索用途 Unknown）**：
>   - **Arista VeloCloud Orchestrator CVE-2026-114625**（SQL 注入；昨晚还在「未进 KEV」观察名单）
>   - **Collabora Online Built-in CODE Server CVE-2026-110447**（OS 命令注入）
> - **今日 10-23 到期**：**SiteGuard Server Edition CVE-2026-106931**、**Plex CVE-2026-96656**、**Plex CVE-2026-96654**（明天起转为逾期）。
> - **逾期（续）**：
>   - 10-19 到期：BeyondTrust Remote Support **CVE-2026-102764**、Fortinet **CVE-2025-61624**
>   - 10-18 到期：Atlassian **CVE-2026-21589**
>   - 10-17 到期：AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322
>   - 10-16 到期：Ivanti Connect Secure 104935、Windows 96951
>   - 10-13 到期：Apple 86950
> - **11-03 到期**：Plex 96652、Plex 96655、Siemens 110936。
> - **仍未进 KEV、但今日高优先**：
>   - **PHP2Shell 109618／109619**：Unit 42 见欧洲政府机构被攻破后 2 小时内拿到 MFA 密钥；NSA 联合多国机构再次催补
>   - **PHP CVE-2026-115560**（新，未修，只有缓解措施）
>   - **Brotli CVE-2026-111497**（Node2Shell → HTTP2Shell；尚无在野报告）
>   - **FortiSIEM CVE-2026-106173**（Horizon3 已公开 PoC；尚无在野确认）
>   - GitLab 110264、BIND 94300、Cisco Expressway 76466、Langflow 105740：今日没有新的在野证据
>
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接，供狩猎用。泄露、入侵类声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

1. **KEV Δ+2：Arista VCO 114625 和 Collabora CODE 110447 入列，10-26 到期。** Collabora 自 9 月起已被用来给 Nextcloud 植入 webshell 和挖矿程序。
2. **PHP2Shell 进入「后渗透」阶段**：Unit 42 10-23 更新称，攻击者用 agentic AI 平台做后渗透，2 小时内拿到密码哈希和 MFA 密钥；NSA 联合 CISA、NCSC、ASD、CERT-EU 发公告催补；THN／Sophos 报告数百万次尝试投放 Mirai 变种。
3. **PHP 又报 CVE-2026-115560（未修）**：只影响运行时改 `session.serialize_handler` 的少见配置；缓解是保持 `session.upload_progress.enabled=0`，修复要等下一次常规版本。
4. **Brotli CVE-2026-111497 从 Node2Shell 扩大成「HTTP2Shell」**：由 OpenAI 红队发现，Imperva 在官方 Node 24.22.0 arm64 镜像上实现 RCE。修复版为 Brotli 1.2.1、Node 22.23.4／24.22.1／26.12.1；Aikido 警告不是所有下游都已出修复。
5. **FortiSIEM CVE-2026-106173**：Horizon3 公开分析和 PoC，未认证 gRPC（TCP 27918）路径穿越可导致 RCE；10-13 已出补丁。
6. **SOCRadar「Phantom」**：俄语勒索 affiliates 用 AI 执行入侵，打了 62 个组织，受益方为 INC／The Gentlemen；暴露目录 45.227.254[.]43。
7. **k0t 初始访问经纪人**（Group-IB／NyxLab）：攻破 Fortinet／PAN-OS 边界设备，泄露 7 万多条凭据，给 Qilin／The Gentlemen 供货。
8. **BlackX UEFI bootkit**（Kaspersky，疑 APT41）：在没把「Windows Production PCA 2011」证书加进 DBX 的已打补丁系统上，仍可绕过 Secure Boot；目标是中亚外交机构。
9. **供应链**：Microsoft 发 LiteLLM 1.107.0 深度分析（Python 启动钩子，**不要在可疑环境里运行 python/pip**），附 IoC。
10. **其他补丁**：Pillow 13.0.0、Ruby 4.0.9／3.4.12／3.3.13（Onigmo → GitLab 4 个 RCE）、Atlassian 75 个第三方漏洞、Popcorn Time 分支更新器 CVE-2026-30612。

## CVE / POC / 漏洞

### 1. Collabora Online Built-in CODE Server CVE-2026-110447 —— 新入 KEV，在野
- **谁／打什么**：攻击 Nextcloud 的「Collabora Online – Built-in CODE Server」（richdocumentscode）应用里的 OS 命令注入。据多帖和 pwn.watch，**9 月起**就被用来植入 webshell。日本用户 @ukokq 报告服务器被植入挖矿程序，经 SSH 登录钩子触发（**单源，UNCONFIRMED**）。
- **补丁／缓解**：把 richdocumentscode 升到 **26.4.303**，或删除该应用（据 @Rachidmarcil 和 pwn.watch）。CISA 10-26 到期。
- **狩猎**：检查 Nextcloud 数据和应用目录有没有新的 PHP 文件；看 CODE 进程有没有派生出异常子进程；看 `~/.ssh`、PAM 和 profile 类登录钩子有没有被篡改，以及有没有挖矿进程或外连。
- 地址：
  - X 原帖：https://x.com/CISACyber/status/2113721352498635260 ｜ https://x.com/ZeroKaiLabs/status/2113770467240878121 ｜ https://x.com/pwnwatch_app/status/2113722377351958843 ｜ https://x.com/Rachidmarcil/status/2113729533832462505 ｜ https://x.com/notCVE/status/2113730698154533146 ｜ https://x.com/ukokq/status/2113548296321159271
  - 厂商／CISA：https://www.cisa.gov/news-events/alerts/2026/10/23/cisa-adds-one-known-exploited-vulnerability-catalog-0 ｜ https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  - 文章：https://pwn.watch/i/nextcloud-collabora-built-in-code-server-cve-2026-110447 ｜ https://notcve.org/cve/CVE-2026-110447
  - IoC：未见公开 IoC

### 2. Arista VeloCloud Orchestrator CVE-2026-114625 —— 新入 KEV（CVSS 9.9），在野
- **谁／打什么**：on-prem VCO 的 SQL 注入。任何已认证用户（最低租户角色、只读即可）都能拿到 operator 权限，冒充本地「superuser operator」。Arista 自己发现并确认在野利用；这是 **4 个月内 VCO 第三个被利用的 0day**。ZoomEye 统计约 **529** 个暴露实例。
- **补丁**：升级到 **5.2.3.18／6.1.3.10／6.4.2.12**；托管版已由 Arista 修好。厂商称「没有任何配置能避免暴露」。CISA 10-26 到期。
- **狩猎**：封禁并回查两个攻击源 IP；看高请求率、带编码字符或类 URL 路径片段的请求、引用本地／内部服务的请求；查 webshell 和后门守护进程。修复前先保全 VCO web、应用、系统、数据库日志和文件时间戳。
- 地址：
  - X 原帖：https://x.com/CISACyber/status/2113697295258583459 ｜ https://x.com/socradar/status/2113561869076070813 ｜ https://x.com/zoomeyebot/status/2113612751629402135 ｜ https://x.com/_pksharma/status/2113590643758911564 ｜ https://x.com/ZeroKaiLabs/status/2113588791021842880 ｜ https://x.com/modularciso/status/2113753582608540085
  - 厂商：https://www.arista.com/en/support/advisories-notices/security-advisory/24838-security-advisory-0199 （昨晚记录的公告页；官网直连常返回空页）｜ https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  - 文章：https://www.securityweek.com/attackers-exploit-third-velocloud-orchestrator-zero-day-in-four-months/ ｜ https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/ ｜ https://thehackernews.com/2026/10/arista-warns-of-critical-velocloud-sql.html ｜ SOCRadar：https://hubs.la/Q04C6xBC0
  - IoC：74.82.197[.]86、38.54.50[.]151（Arista／SOCRadar 公布的攻击源）

### 3. PHP2Shell CVE-2026-109618／109619 —— 续：AI 后渗透、NSA 联合公告、Mirai
- **谁／打什么**：
  - **Unit 42（10-23 更新）**：欧洲某政府机构被攻破后，攻击者用 agentic AI 攻击平台做后渗透，**2 小时内**拿到密码哈希和 MFA 密钥，建了 NTLM relay 隧道进 AD，并尝试提权到 Domain Admin。特征是命令批次用分节分隔符包裹（便于 AI 解析）、任务短小密集、失败后快速换路。另据 Unit 42，至少一个欧洲政府已把网站下线以防万一。
  - **NSA**：联合 CISA、NCSC、ASD、CERT-EU 发公告，要求立即评估暴露面并修补。
  - **THN／Sophos**：数百万次利用尝试，投放 Mirai 变种「Potassium」，**暂未确认成功入侵**；也有研究指出武器化比预想的难。SecurityWeek 称已出现 ASLR 绕过利用。
  - **社区争论**：有人认为热度被高估（domchell、LiveOverflow）。
- **补丁**：升级到 **8.5.12／8.4.27／8.3.36／8.2.35** 并重启全部 worker；`session.upload_progress.enabled=0` 继续保留（也是 115560 的缓解）。PAN-OS 管理口也受影响，见 securityonline。
- **狩猎**：
  - Unit 42 简报附有狩猎查询。
  - Talos 已出 Snort 规则；krNeoTra 发了 Snort/Suricata 规则帖。
  - nuclei-templates v10.5.1 加了「Active Crash Detection」模板。
  - Assetnote 发了扫描器。
  - 看 PHP-FPM 有没有异常崩溃或重启、web 进程有没有派生 shell、有没有 NTLM relay 迹象。
- 地址：
  - X 原帖：https://x.com/Unit42_Intel/status/2113729718713209172 ｜ https://x.com/NSACyber/status/2113740408056689005 ｜ https://x.com/2Workly/status/2113552458605892030 ｜ https://x.com/bluetouff/status/2113604738478702949 ｜ https://x.com/BlackLanternLLC/status/2113646984057987519 ｜ https://x.com/krNeoTra/status/2113456607313240573 ｜ https://x.com/theomlondhe/status/2113512450662281512 ｜ https://x.com/domchell/status/2113712993145934232 ｜ https://x.com/LiveOverflow/status/2113651743691293040
  - GitHub／检测：https://github.com/assetnote/php2shell-scanner ｜ https://github.com/blacklanternsecurity/PoCs ｜ https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.1
  - 厂商／政府：https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4630238/nsa-advisory-critical-patches-recommended-for-php-vulnerabilities/ ｜ Unit 42：https://bit.ly/4z7Txr2 ｜ Talos：https://blog.talosintelligence.com/two-critical-rces-in-php-core/
  - 文章：https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html ｜ https://www.securityweek.com/php2shell-exploitation-started-days-before-patches/ ｜ https://watchtowr.com/php2shell-threat-briefing-october-2026/ ｜ https://securityonline.info/pan-os-php2shell-cve-2026-109618/ ｜ https://www.sequretek.com/resources/threat-advisories/Critical%20PHP%20Vulnerabilities%20Under%20Exploitation
  - IoC：Potassium（Mirai 变种）C2 134.199.154[.]64（Sophos，经 THN）

### 4. PHP CVE-2026-115560 —— 新披露，未修
- **是什么**：PHP 10-23 发短公告。应用同时满足以下条件时可能 RCE：把 `session.serialize_handler` 设为 `php_binary` 或 `php_serialize`；运行时在 `session_start()` 前用 `ini_set()` 改成 `php`；session upload progress 处于开启状态。PHP 认为这种配置不常见，**不发紧急补丁**，修复跟随下一次常规版本。**10-21 的 PHP2Shell 修复版不包含此修复。**
- **缓解**：`session.upload_progress.enabled=0`（与 10-21 的缓解相同，已设置的无需再动）。未见在野报告。
- 地址：
  - X 原帖：https://x.com/thephpf/status/2113580383875019242 ｜ https://x.com/SitelemetryApp/status/2113768089284386910 ｜ https://x.com/dboedger/status/2113757042955395582 ｜ https://x.com/elhackernet/status/2113748355457200545 ｜ https://x.com/catnap707/status/2113753119784046658
  - 厂商：https://www.php.net/archive/2026.php#2026-10-23-1 ｜ https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp
  - 文章：https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html ｜ https://mytech-blog.com/cve-2026-109618-php/
  - IoC：未见公开 IoC

### 5. Brotli CVE-2026-111497 —— Node2Shell → 「HTTP2Shell」（CVSS 9.2）
- **是什么**：Brotli 解码器在一种不可能出现的块切换状态下继续解码，导致越界写。OpenAI 称是在前沿模型红队演练中发现的。根因早在 2 月已在源码里修掉，但当时没意识到是安全问题，也没发新版。服务端会解压客户端数据时会被恶意客户端拿下；客户端接受压缩响应时（如 `curl --compressed`）会被恶意服务器拿下。
- **验证情况**：Imperva 在官方 Node.js 24.22.0 linux-arm64 镜像上实现 RCE（需多次尝试），经 Express 5.x 和 body-parser 2.x 的请求体路径及 fetch() 响应路径均复现；其他架构和 22.x／26.x 未测试。**THN 称截至 10-22 未见在野利用。** Aikido 把影响面扩大为「HTTP2Shell」：大量 HTTP 库和应用可能被未认证 RCE，**并非所有下游都已有修复**。
- **补丁**：Brotli **1.0.10／1.1.1／1.2.1**；Node **22.23.4／24.22.1／26.12.1**；Python Brotli **1.2.1**。容器镜像和自带 Node 二进制的产物要单独盘点；20.x 及更早的 EOL 线拿不到修复。Microsoft 给出 Azure WAF 防护规则。
- 地址：
  - X 原帖：https://x.com/OpenAI/status/2113766354386084338 ｜ https://x.com/AikidoSecurity/status/2113759110625906950 ｜ https://x.com/TheHackersNews/status/2113538808126038500 ｜ https://x.com/choblin29/status/2113769614727614632 ｜ https://x.com/strapijs/status/2113661832304931190 ｜ https://x.com/dimasma__/status/2113593375907799131
  - GitHub／PoC（仅供核对，不转述内容）：https://github.com/dimasma0305/CVE-2026-111497-POC
  - 厂商：https://patchtheplanet.org/brotli ｜ https://www.cve.org/CVERecord?id=CVE-2026-111497 ｜ https://techcommunity.microsoft.com/blog/AzureNetworkSecurityBlog/protect-against-brotli-cve-2026-111497-with-azure-web-application-firewall-waf/4567288
  - 文章：https://www.aikido.dev/blog/node2shell-nodejs-brotli-rce-cve-2026-111497 ｜ https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html
  - IoC：未见公开 IoC（`$HTTP2SHELL` 代币帖是炒作，不采信）

### 6. Fortinet FortiSIEM CVE-2026-106173 —— 公开 PoC
- **是什么**：gRPC 服务（TCP **27918**）不校验客户端证书，用攻击者提供的值拼接文件路径，导致路径穿越写文件。覆盖一个每 60 秒执行一次的定时脚本后，可以 admin 用户身份执行代码。Horizon3 已发深度分析和 PoC。CVSS 写法不一（securityonline 写 9.4，部分帖写 9.8）。Fortinet 10-13 已修；CISA 富化标注「poc／automatable」；**未见在野确认**。受影响分支含 7.0–7.5。
- **狩猎**：限制 27918 只对受信任采集器开放；查定时脚本完整性，看 admin 上下文有没有异常子进程。
- 地址：
  - X 原帖：https://x.com/Daily_CyberSec/status/2113429240666345549 ｜ https://x.com/ifahimulhssn/status/2113432634412142628 ｜ https://x.com/nodoware_news/status/2113766300766130178
  - 厂商：https://fortiguard.fortinet.com/psirt （Fortinet PSIRT 总页；具体 FG-IR 编号本次未核到，不编造）
  - 文章：https://securityonline.info/fortisiem-vulnerability-cve-2026-106173-poc/
  - IoC：未见公开 IoC

### 7. Pillow 13.0.0 —— CVE-2026-112900 等
- **是什么**：Pillow 打开 EPS 时把文件名直接交给 Ghostscript，攻击者能控制文件名时可执行命令（GitHub CNA 评 9.2，维护方评 moderate；影响 2.6.0–12.3.0，前提是装了 gs）。13.0.0 是大型安全版本，含两个维护方评 critical 的问题：模式切换后复用陈旧数据，以及 JPEG 解码溢出；另有一个在装了 olefile 时可经 Image.open() 触发命令执行的问题。**均未见在野利用。**
- **补丁**：升级 Pillow 13.0.0；上传接口不要用用户输入拼存储文件名。
- 地址：
  - 文章：https://thehackernews.com/2026/10/critical-flaw-in-pythons-popular-pillow.html
  - 厂商：https://github.com/python-pillow/Pillow/releases
  - IoC：未见公开 IoC

### 8. Ruby Onigmo 正则引擎三个 bug → GitLab 四个 critical RCE
- **是什么**：Ruby 发布 **4.0.9／3.4.12／3.3.13**（4.0.8 漏了其中一个修复）。只有把攻击者可控字符串编译成正则的应用受影响（Regexp.new／union／compile 或 `/#{input}/`）。Ruby 3.2 及更早不再修。这与过去一个月 GitLab 的满分正则漏洞（含 110264）同源。
- 地址：
  - X 原帖：https://x.com/TweetThreatNews/status/2113501750166442435
  - 厂商：https://www.ruby-lang.org/en/news/
  - 文章：https://thehackernews.com/2026/10/ruby-fixes-three-regex-engine-bugs.html ｜ https://cyber.hendryadrian.com/article/7641/gitlab-patches-cvss-10-0-rce-flaw-affecting-self-managed-ce-and-ee
  - IoC：未见公开 IoC

### 9. 其他漏洞与补丁（简列）
- **Popcorn Time 分支 Time4Popcorn CVE-2026-30612**：更新器走明文 HTTP，且不验证签名。Eye Security 注册了被弃用的更新域 popcorntimeupd[.]xyz，观察到约 300 万 Windows、35 万 macOS 客户端连接，并已远程禁用更新器。https://www.bleepingcomputer.com/news/security/abandoned-popcorn-time-app-exposed-millions-of-device-to-rce-attacks/
- **Atlassian** Data Center／Server 修了 75 个第三方漏洞：https://www.securityweek.com/atlassian-patches-75-third-party-flaws-in-data-center-and-server-products/
- **Splunk／SolarWinds** 新一轮更新：https://www.securityweek.com/splunk-solarwinds-release-fresh-security-updates/
- **Signal** 恶意来电者可阻止对方挂断：https://www.securityweek.com/signal-vulnerability-lets-malicious-callers-block-hang-ups/
- **x402 SDK** 严重漏洞：https://x.com/TheHackersNews/status/2113550887901675675 ｜ https://thehackernews.com/2026/10/critical-x402-sdk-flaw-could-let.html
- **Keycloak** CVE 讨论：https://x.com/catcowbug/status/2113484562902712499
- **Windows ALPC CVE-2026-85880** 提权（10 月补丁日）：https://avleonov.com/2026/10/18/i182-about-elevation-of-privilege-windows-advanced-local-procedure-call-alpc-cve202685880-vulnerability/
- **Linux KSMBD 两个 ZDI RCE**（ZDI-CAN-33774／33549，仍无主线补丁）：https://securityarsenal.com/blog/ksmbd-zero-day-rce-flaws-zdi-can-33774-and-zdi-can-33549-defending-linux-smb-servers-before-the-patch-lands ｜ https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html
- **nuclei-templates v10.5.1** 同批新增检测：Avada Builder CVE-2026-6279、WordPress OttoKit CVE-2026-110372、Loom for AWS CVE-2026-103956、Langflow CVE-2026-93674 等：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.1
- **KEV 逾期跟进**：BeyondTrust 102764 已逾期 4 天，相关活动关联 UNC5221 一类：https://2workly.com/insights/beyondtrust-remote-support-cve-2026-102764-exploitation-hunt
- **今日到期**的 SiteGuard 106931、Plex 96656／96654：本日 X 上没有新的利用细节，按 KEV 处理：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

## 工具与 GitHub 发布

> 防御视角：只记录工具是什么、可以怎么检测，不转述用法。

- **whokilleddb/TTs**：滥用 Visual Studio 的 TextTransform.exe 执行 `.tt` 模板里的 C#，可作为 MSBuild 的替代 LOLBin。
  - X：https://x.com/whokilleddb/status/2113584321881887197
  - GitHub：https://github.com/whokilleddb/TTs
  - 防御参考：https://github.com/bohops/UltimateWDACBypassList#texttransformexe ｜ ipurple 的 Text Template 检测文章：https://x.com/ipurple/status/2113680687761129822
  - 狩猎：TextTransform.exe 在开发机以外运行，或加载陌生 `.tt` 文件。
- **Whispergate/Signet**：Mythic payload 签名相关工具。https://github.com/Whispergate/Signet ｜ X：https://x.com/ipurple/status/2113537175891648653 ｜ https://x.com/Dinosn/status/2113582987292131773
- **xen-i0/jinxed-agent**：AdaptixC2 的 Linux agent。https://github.com/xen-i0/jinxed-agent ｜ X：https://x.com/xen_i0/status/2113704151406223655 （AdaptixC2 也出现在 k0t 案中，见下文）
- **dagowda/ConfluenceC2**：把 Confluence 当 C2 通道。https://github.com/dagowda/ConfluenceC2 ｜ X：https://x.com/elgerx/status/2113693074643972591 。狩猎：非人类节奏的 Confluence API 页面读写。
- **jakehildreth/Locksmith2**：AD CS 配置审计和修复（防守向）。https://github.com/jakehildreth/Locksmith2 ｜ X：https://x.com/elgerx/status/2113693034613494055
- **0xPrimo/DemonLdr**：Havoc Demon 的 UDRL 加载器。https://github.com/0xPrimo/DemonLdr ｜ X：https://x.com/r1cksec/status/2113553225878278269
- **ipurple「Protecting C2 Traffic in Nim」**：https://x.com/ipurple/status/2113663651320356982
- **mrgretzky（evilginx 作者）扩展 BITB 钓鱼技术**：https://x.com/mrgretzky/status/2113665151027097626 。防御上应推 FIDO2／passkey。
- **AI 红队／越狱集合**：
  - SnailSploit/Claude-Red：https://github.com/SnailSploit/Claude-Red （X：https://x.com/UrzPhaneendra/status/2113726376805380179 ）
  - confident-ai/deepteam（LLM 红队评测）：https://github.com/confident-ai/deepteam （X：https://x.com/gitrepos/status/2113601633913340401 ）
  - Alejandros17487/ai-jailbreaks：https://github.com/Alejandros17487/ai-jailbreaks （X：https://x.com/Dinosn/status/2113490142581100629 ）
- **PHP2Shell 检测／扫描**：
  - https://github.com/assetnote/php2shell-scanner （X：https://x.com/bluetouff/status/2113604738478702949 ｜ https://x.com/ntlmrelay/status/2113586534272389380 ）
  - 社区仓库 https://github.com/vm32/php2shell （X：https://x.com/vm_32/status/2113628651300499669 ）和 https://github.com/murrez/php2shell （X：https://x.com/murrezsec/status/2113630538003104134 ）未经审计，**慎用**。
- **其他小工具**（低信号，仅列链接）：
  - https://github.com/morluto/rea （X：https://x.com/sammy_capital/status/2113733817596834151 ）
  - https://github.com/PrismorSec/prismor （X：https://x.com/_ar9av/status/2113586849273029110 ）
  - https://github.com/26zl/cybersec-toolkit （X：https://x.com/EsGeeks/status/2113763229130490087 ）
  - https://github.com/hassan-algo/open-sesame
  - https://github.com/Rickert155/VoidSec （0.1.20）
- **正式 release**：nuclei-templates **v10.5.1**（10-23 08:19 UTC-3，新增 68 个模板、54 个 CVE），https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.1 。Sliver、BloodHound、NetExec、Mythic、impacket、Havoc、AdaptixC2、httpx、nuclei 本窗口内**没有新的正式 release**。
- **其他**：Layle 的 Wii 漏洞研究「Haxx Bearers」https://x.com/layle_ctf/status/2113664451698205163

## APT / Malware 分析

### SOCRadar「Phantom」：俄语勒索 affiliates 用 AI 执行入侵（受益方 INC／The Gentlemen）
- **谁／打什么**：「AI 执行、人工审批」模式：人给出受害者提示词并批准每一步，执行交给 OpenCode 和 OpenRouter 托管的商用模型。日志里有 8,257 条消息、133 个会话，目标 62 个组织（美国占一半以上，工业、制造、能源最多），其中 4 个已上 INC／The Gentlemen 泄露站。
- **用到的漏洞**：
  - SimpleHelp CVE-2024-57727
  - FortiClient EMS CVE-2026-35616
  - cPanel/WHM CVE-2026-41940
  - SonicWall SMA1000 CVE-2026-15409：已列为目标，但未确认得手
- **工具**：Phantom（18 个技能模块）、WormGPT-MCP、Ghost C2、QuickLine（Cloudflare 前置的 Mythic agent）、RevSocks、rks3／BackupAgent；用 Zemana 驱动 zam64.sys 做 BYOVD 杀 EDR。
- **狩猎**：查 FortiClient EMS、SimpleHelp、cPanel 的利用记录；查非预期进程加载 zam64.sys；查反向 SOCKS；查同一凭据短时间内先后登录 VPN、RMM、备份平台。
- 地址：
  - X：https://x.com/DFIR_Radar/status/2113768704622358776 ｜ https://x.com/Dinosn/status/2113698925337039245
  - 文章：https://thehackernews.com/2026/10/exposed-infrastructure-reveals-how.html
  - IoC：45.227.254[.]43（暴露目录）；文件 zam64.sys

### k0t 初始访问经纪人（Group-IB／NyxLab）
- **谁／打什么**：k0t（别名 CryptoFeel／Member19／QazWsxShop），2025-10-22 起活跃，2026 年 2–6 月最密集。用 FOFA／ZoomEye 批量找目标，打 FortiGate（CVE-2025-64446）和 PAN-OS GlobalProtect（CVE-2026-0257）；经 OpenConnect VPN 进入，部署 MeshCentral／Atera／AnyDesk 和 AdaptixC2；导出 AD LDAP；用 Rclone 外传到 Wasabi S3／MEGA。共泄露 7 万多条凭据，给 Qilin／The Gentlemen 供货。受害者分布：亚太 38%、拉美 31.9%。
- **防御**：关闭边界设备的外部管理口；修补上述 CVE；VPN 强制 FIDO2；拦截未批准的 Rclone 远端。
- 地址：
  - X：https://x.com/_pksharma/status/2113680430671053022
  - 文章：https://thehackernews.com/2026/10/hackers-breach-enterprise-firewalls-and.html ｜ https://www.pk-sharma.com/briefing/k0t-enterprise-firewall-vpn-breach-70000-credentials-qilin ｜ https://cybersecurity88.com/news/hackers-breach-enterprise-firewalls-and-vpns-exposing-over-70000-credentials/
  - IoC：工具文件名 fortnew[.]py、exploit_2026_0257.py（文件名，非网络指标）；未见公开网络 IoC

### BlackX UEFI bootkit（Kaspersky，疑 APT41）
- **谁／打什么**：2026 年初针对塔吉克斯坦、乌兹别克斯坦、土库曼斯坦的外交机构。BlackX 仿照 BlackLotus 利用 Baton Drop（CVE-2022-21894），通过安装 MOK 加载任意 EFI。只打补丁不够，还要手动把「Windows Production PCA 2011」证书加入 DBX；该证书 10-19 已过期，但没进黑名单就仍能加载。部署前提是已有管理员权限。
- **狩猎**：盘点 DBX 吊销状态；查 EFI 分区里的异常文件和 MOK 列表；查 `C:\ProgramData\Intel\inst.exe` 及同目录的加密 blob。
- 地址：
  - X：https://x.com/TheHackersNews/status/2113704852148924776 ｜ https://x.com/omvapt/status/2113770951535988839
  - 文章：https://thehackernews.com/2026/10/blackx-uefi-bootkit-bypasses-secure.html
  - 厂商参考：https://support.microsoft.com/topic/kb5025885-how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023-24932-41a975df-beb2-40c1-99a3-b3ff139f832d
  - IoC：路径 C:\ProgramData\Intel\inst.exe；加密文件名 PVMDIJGKAX2（THN 转述 Kaspersky）

### Storm-0940 + Artex → ConnectWise（Microsoft）
- 中国关联的 Storm-0940 用开源 AI 渗透框架 Artex，自动化攻击 ConnectWise 客户：对 8 个组织 300 多个账户做密码喷洒，速度超过每分钟 2,900 次；用被盗的 ConnectWise 应用凭据尝试登录 2,250 多个租户；失败登录 15.1 万次以上；部分环境里进一步通过 Graph 篡改应用凭据做持久化。
- 地址：
  - X：https://x.com/CyberScoopNews/status/2113693187868971065
  - 文章：https://www.securityweek.com/china-apt-uses-ai-pentest-tool-artex-in-connectwise-attacks/
  - IoC：未见公开 IoC（Microsoft 原文见 SecurityWeek 引用）

### LiteLLM 1.107.0 供应链（Microsoft 深度分析）
- 10-21 被投毒的 PyPI 包和官方容器镜像，通过 `.pth`／`sitecustomize.py` 在 Python 解释器启动时执行，**不需要 import litellm**。窃取开发工具、AI、云、浏览器、基础设施的凭据，并读取 LiteLLM proxy 数据库。**不要在可疑环境里运行 python 或 pip 来检查**；删除包不足以恢复，要重建环境并轮换凭据。
- 地址：
  - X：https://x.com/MsftSecIntel/status/2113696457123311635
  - 厂商：https://msft.it/6012axjt8 （Microsoft Security Blog）｜ Wiz：https://www.wiz.io/blog/litellm-compromised-steals-credentials
  - 文章：https://www.securityweek.com/litellm-compromised-in-fresh-supply-chain-attack/
  - IoC：见 IoC 汇总（www[.]litellm[.]dev、dead-drop URL、6 个 SHA-256、2 个锁文件）

### 其他威胁报告（简列）
- **Railway 更新**：针对 AI API 密钥的「蒸馏」类滥用，最多约 10 万个 workspace 受影响。https://x.com/TheHackersNews/status/2113712529646203369
- **Huntress：CastleLoader → shellcode loader → Lumma**：index.js 是 CastleLoader，stage-2 用 AES-256-GCM 解密。https://x.com/HuntressLabs/status/2113711882427113844 。IoC：未见公开 IoC。
- **Group-IB SiriusQT RAT**（RAT＋HVNC＋窃密，在 cracked[.]to／crax[.]pro 分发）：https://www.group-ib.com/blog/siriusqt-rat-hvnc-stealer/ 。IoC 见汇总。
- **Semperis「Prince of Persia」**（伊朗关联组织）：https://www.semperis.com/blog/prince-of-persia-threat-group-hiding-in-plain-sight/
- **Sandworm MythicRatatoskr**（续）：https://x.com/DFIR_Radar/status/2113556607070277732
- **Unit 42 CL-UNK-1211 SysGoRAT**：https://x.com/DFIR_Radar/status/2113738585413161055
- **Aokigahara**：https://x.com/DFIR_Radar/status/2113647071119229261 ｜ **Bronze Sandcastle**：https://x.com/DFIR_Radar/status/2113466372613193796 ｜ **Beast 勒索**：https://x.com/DFIR_Radar/status/2113722661192794269
- **SilentNET**（malwation）：https://x.com/malwation/status/2113640932952150322
- **EtherRAT**（伪 Advanced IP Scanner，经 Intune 导入）：https://cyberveille.ch/posts/2026-10-19-etherrat-distribue-via-un-faux-installeur-advanced-ip-scanner-importe-dans-microsoft-intune/ ｜ https://bluecyber.hashnode.dev/etherrat-malware-bootcamp2026
- **OVHcloud CLI GlassWorm**（续）：https://cyberveille.ch/posts/2026-10-21-compromission-de-la-chaine-d-approvisionnement-ovhcloud-cli-par-le-groupe-glassworm/
- **Zimperium：用 Android 入侵日志揭露高级威胁**：https://zimperium.com/blog/beyond-the-sandbox-leveraging-android-intrusion-logs-to-expose-advanced-threats
- **n0n 勒索**（单源，UNCONFIRMED）：https://provendata.com/blog/n0n-ransomware
- **事件**：
  - Initia Chain 被恶意铸造约 260 万美元代币（UNCONFIRMED）：https://x.com/Dinosn/status/2113680506826928289
  - Capcom 数据泄露 1100 万人：https://www.securityweek.com/11-million-impacted-by-capcom-data-breach/
  - Quest Diagnostics：https://www.securityweek.com/quest-diagnostics-reports-cyber-breach-affecting-certain-patient-records/
  - FCC 封禁华为海思监控芯片设备：https://therecord.media/fcc-bans-devices-huawei-surveillance-chips
- **IoC 猎人日常**（NetSupport／Telegram 仿冒／DiddyBot 等）：见下方汇总；出处是 @skocherhan、@malwrhunterteam、@smica83。

## 地址／IoC 汇总

> 全部原样抄录并去武装化（hxxp／[.]）。只用于封禁和狩猎；共享基础设施（workers.dev、pages.dev、raw.githubusercontent.com）只按完整 URL 匹配，不整域封禁。

| 类型 | 指标 | 关联 | 来源 |
|---|---|---|---|
| IP | 74.82.197[.]86 | Arista VCO CVE-2026-114625 攻击源 | https://x.com/socradar/status/2113561869076070813 ｜ https://www.securityweek.com/attackers-exploit-third-velocloud-orchestrator-zero-day-in-four-months/ |
| IP | 38.54.50[.]151 | Arista VCO CVE-2026-114625 攻击源 | 同上 |
| IP | 134.199.154[.]64 | PHP2Shell → Mirai 变种 Potassium C2（Sophos） | https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html |
| IP | 45.227.254[.]43 | SOCRadar「Phantom」勒索 affiliates 暴露目录 | https://x.com/DFIR_Radar/status/2113768704622358776 ｜ https://thehackernews.com/2026/10/exposed-infrastructure-reveals-how.html |
| 文件 | zam64.sys（Zemana 驱动，BYOVD） | Phantom 杀 EDR | 同上 |
| 文件名 | fortnew[.]py、exploit_2026_0257.py | k0t 利用脚本 | https://x.com/_pksharma/status/2113680430671053022 |
| 路径 | C:\ProgramData\Intel\inst.exe；加密文件 PVMDIJGKAX2 | BlackX bootkit 安装器 | https://thehackernews.com/2026/10/blackx-uefi-bootkit-bypasses-secure.html |
| 域名 | www[.]litellm[.]dev | LiteLLM 1.107.0 外传域 | https://msft.it/6012axjt8 |
| URL | hxxp://www[.]litellm[.]dev/healthcheck | LiteLLM 外传 URL | 同上 |
| URL | hxxps://raw[.]githubusercontent[.]com/letters9813/pythonclient-test/main/domain.txt | LiteLLM C2 dead-drop | 同上 |
| SHA256 | 9dd0a3926f96a37eb86cf1ee2310d9be93139cc4ebef3ef9e2efe9531390be25 | LiteLLM cook.py 变体 | 同上 |
| SHA256 | 03ac2a8b752605d1d7710979c17ff18b03dd978203ba23ba97fd8ce3d6f897ea | LiteLLM cook.py（Windows wheel） | 同上 |
| SHA256 | 34bef04fe88ac9d0aae0475630b1738681d15b94f233ac8aa46eacf5968305fa | LiteLLM sitecustomize.py 变体 | 同上 |
| SHA256 | b6122440d0d9cb1eb1ade9933f49214da8c31288de7710c076c2680dfa528465 | LiteLLM sitecustomize.py（Windows wheel） | 同上 |
| SHA256 | 7f191632e7320705d154b85204f1ae546b543acbd7e8861229b76f5042b92bdb | LiteLLM cook.pth | 同上 |
| SHA256 | 84dc8c82c0a4a4a62552ef826b49fcc86d1a5c4a5d0f2c06665723f93d129d7d | LiteLLM cook.pth 变体 | 同上 |
| 文件 | /tmp/remote_code_loader.lock；/tmp/.pc_once_72129118c59f5636c0bb | LiteLLM 加载器锁文件／外传标记 | 同上 |
| 域名:端口 | server[.]activeworkshops[.]com:16614、server[.]activeworkshops[.]com:31166 | SiriusQT RAT C2 | https://www.group-ib.com/blog/siriusqt-rat-hvnc-stealer/ |
| IP:端口 | 2[.]27[.]62[.]140:4449 | SiriusQT RAT C2 | 同上 |
| 域名 | www[.]nairawaterfall[.]com、cdn[.]nairawaterfall[.]com、downloads[.]nairawaterfall[.]com、nairawaterfall[.]com | NetSupport | https://x.com/skocherhan/status/2113753472726434072 |
| IP | 194[.]180[.]191[.]245（AS39798 MivoCloud SRL） | NetSupport（nairawaterfall） | 同上 |
| 域名 | download[.]sakenlogistics[.]com、cdn[.]sakenlogistics[.]com、sakenlogistics[.]com、youlovemybiba[.]com、www[.]youlovemybiba[.]com、download[.]youlovemybiba[.]com、cdn[.]youlovemybiba[.]com | NetSupport | https://x.com/skocherhan/status/2113751077426249995 |
| IP | 150[.]241[.]66[.]223（AS210457 Kyonix Networks Limited） | NetSupport（sakenlogistics／youlovemybiba） | 同上 |
| 域名 | digitalbuys[.]net、armzeso[.]top | NetSupport | https://x.com/skocherhan/status/2113749556450250904 |
| 域名／URL | download[.]transunionbiba[.]lat（opendir）；hxxps://download[.]transunionbiba[.]lat/stage2.js | 开放目录／二阶段脚本 | https://x.com/skocherhan/status/2113748689944490457 ｜ https://x.com/malwrhunterteam/status/2113749305068753356 |
| IP／URL | 141.98.10[.]25；hxxp://141.98.10[.]25/diddysbot-amd64 | 「DiddyBot dropper」 | https://x.com/malwrhunterteam/status/2113743302193230261 ｜ https://x.com/malwrhunterteam/status/2113743909134229940 |
| IP | 2.27.63[.]78 | malwrhunterteam 标注（用途未说明） | https://x.com/malwrhunterteam/status/2113747624935473579 |
| URL | hxxp://89.124.99[.]187:6001/（「Вход — FileHost」面板）；hxxp://146.103.100[.]148:7777/login（「Вход」面板） | 可疑面板 | https://x.com/malwrhunterteam/status/2113730389688963196 |
| SHA256 | 48db2ddcc81839bbd26c206696a47dc772fb7892603616da09657cd976533f69 | 与上条面板相关的样本 | https://x.com/smica83/status/2113731735645048876 ｜ https://bazaar.abuse.ch/sample/48db2ddcc81839bbd26c206696a47dc772fb7892603616da09657cd976533f69/ |
| 域名 | coreservicejcp[.]com | malwrhunterteam 标注 | https://x.com/malwrhunterteam/status/2113728290196463630 |
| SHA256 | d2d95c5534efcea6c63843cde59b617ac5b97e057d908298191468d5e3b7635a（AzureCobalt57-77b11081.msi） | 与 coreservicejcp 相关的样本 | https://x.com/smica83/status/2113729879229317627 ｜ https://bazaar.abuse.ch/sample/d2d95c5534efcea6c63843cde59b617ac5b97e057d908298191468d5e3b7635a/ |
| MD5 | d53128ca7057a8bcc362f2c8ea30fcce | skocherhan 标注样本 | https://x.com/skocherhan/status/2113723160214270452 |
| 域名／主机 | cfclear[.]devdesk[.]workers[.]dev、desktop-telergram[.]org、eqvpn[.]space:2083、hello-world-fancy-mud-57ff[.]2111857176[.]workers[.]dev、linksub-4u1[.]pages[.]dev、llsbsnls[.]suplayer810[.]workers[.]dev、proxy-tg-huafei080[.]papag8593[.]workers[.]dev、t-me[.]nproxy[.]org | Telegram 仿冒／代理类基础设施 | https://x.com/skocherhan/status/2113733954490470752 |
| 域名 | popcorntimeupd[.]xyz | Time4Popcorn 被弃用更新域（已被 Eye Security 接管，属研究方控制） | https://www.bleepingcomputer.com/news/security/abandoned-popcorn-time-app-exposed-millions-of-device-to-rce-attacks/ |

**以下各条未见公开 IoC**：Collabora 110447、PHP 115560、Brotli 111497、FortiSIEM 106173、Pillow、Ruby／GitLab、Storm-0940／Artex（本次未取得 Microsoft 原文指标）、Railway、CastleLoader→Lumma（Huntress 帖只有截图）。

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


### 本日交叉情况
- **LWiS X List**：500 名成员分 10 段做 `from:` 查询（10 次读取，其中第 5 段只返回 2 条，属正常）。去重后最先命中 LWiS 批次的安全相关帖有 **48** 条，主要是：
  - PHP2Shell 争论（domchell、LiveOverflow）
  - TextTransform 工具（whokilleddb）
  - ipurple 的 Signet／Nim C2／Text Template 检测
  - mrgretzky 的 BITB
  - layle_ctf 的 Wii 研究
  - Huntress 的 CastleLoader→Lumma
  - malwrhunterteam、smica83 的 IoC
  
  闲聊和招聘帖已剔除（如 Frichette_n 2113642127695745196）。
- **blogs.txt 高信号源**：Unit 42（PHP 简报 10-23 更新）、Microsoft Security Blog（LiteLLM）、Talos（PHP Snort 规则）、Group-IB（SiriusQT）、Semperis（Prince of Persia）、Zimperium、watchTowr（PHP2Shell 简报）当日的相关文章已在上文交叉引用。Kaspersky 的 BlackX 原报告本次没有直接抓取，以 THN 转述为准。
- **Risky Business**：RSS 最新一期仍是 **#856「8-bit encryption, PHP megabugs and more」**（10-21 01:43 UTC-3 发布，早于本窗口），本日没有新一期：https://risky.biz/
- **tl;dr sec**：首页可以访问，但抓到的 `/p/` 链接都是旧文章，**无法确认**本窗口内有没有新一期：https://tldrsec.com/
- **结论**：今天所有重点（KEV Δ+2、PHP2Shell／115560、Brotli、FortiSIEM、Phantom、k0t、BlackX、LiteLLM）**都先在 X Latest 上出现**，公开信源只用来核对版本号、IP 和日期。

## 来源搜索 URL

- X 只读接口查询（下列为等价的 X 网页搜索 URL，便于人工复核；实际用接口 `search_posts_all` 执行）：
  - A 类：https://x.com/search?q=(CVE-2026%20OR%20CVE-2025)%20(exploit%20OR%20exploited%20OR%20PoC%20OR%20RCE%20OR%20patch%20OR%20advisory%20OR%20KEV%20OR%200day%20OR%20zero-day)%20-is%3Aretweet&f=live
  - B 类：https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20redteam%20OR%20BOF%20OR%20EDR%20OR%20implant%20OR%20nuclei)%20-is%3Aretweet&f=live
  - C 类：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)%20-is%3Aretweet&f=live
  - LWiS List：https://x.com/i/lists/1239330068461244424
  - 专题 Collabora：https://x.com/search?q=CVE-2026-110447&f=live
  - 专题 Brotli／HTTP2Shell：https://x.com/search?q=(CVE-2026-111497%20OR%20HTTP2Shell%20OR%20Node2Shell)&f=live
  - 专题 FortiSIEM／Arista：https://x.com/search?q=(CVE-2026-106173%20OR%20CVE-2026-114625)&f=live
  - 专题 PHP2Shell：https://x.com/search?q=php2shell%20-is%3Aretweet&f=live
  - 专题 PHP 115560／BlackX：https://x.com/search?q=(%22CVE-2026-115560%22%20OR%20upload_progress%20OR%20FortiSIEM%20OR%20BlackX)%20-is%3Aretweet&f=live
- 公开备援：
  - CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - CISA KEV 页：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  - CISA 10-23 新增公告：https://www.cisa.gov/news-events/alerts/2026/10/23/cisa-adds-one-known-exploited-vulnerability-catalog-0
  - NVD：https://nvd.nist.gov/vuln/search
  - PHP 公告：https://www.php.net/archive/2026.php#2026-10-23-1
  - Brotli：https://patchtheplanet.org/brotli
  - Unit 42 PHP 简报：https://bit.ly/4z7Txr2
  - NSA PHP 公告：https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4630238/nsa-advisory-critical-patches-recommended-for-php-vulnerabilities/
  - nuclei-templates v10.5.1：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.1
  - LWiS blogs.txt：https://blog.badsectorlabs.com/files/blogs.txt
  - Risky Business：https://risky.biz/
  - tl;dr sec：https://tldrsec.com/
