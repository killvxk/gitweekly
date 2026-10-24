# X 安全情报晚报 · 2026-10-22

> 搜集窗口：圣地亚哥时间 **2026-10-21 20:15 至 2026-10-22 20:15**（America/Santiago／UTC-3，名义 24 小时，接昨晚窗口）。X 搜索参数：`start_time=2026-10-21T23:15:00Z`，`end_time=2026-10-22T23:15:00Z`。实际抓到的帖子时间从 **10-21 20:15** 到 **10-22 20:14**（UTC-3），**实际有效覆盖约 24 小时**。A 类加了深夜／午间／傍晚三个时间切片，核心媒体分三段抓（20:15–08:15／08:14–15:07／08:15–20:15），**没有明显的大块空白**。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`，用 Latest／recency 和 relevancy 两种排序）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** 接口多数批次没回传 entities，t.co 一律用 curl 跟随 HTTP 跳转展开：粗筛帖中共 **340** 个短链，**340** 个都展开到了非 t.co 目标；纯图片／视频链接不列。
> 本轮各类查询次数：
> - A 类（CVE／0day）：原始、去噪、在野各一次，另加三个时间切片
> - B 类（GitHub 红队／C2）：两次
> - C 类（威胁报告／IoC）：三次
> - LWiS List：500 名成员分 10 段做 `from:` 批次
> - 核心媒体／厂商账号：三段
> - IoC 猎人账号：两页
> - 专题（Arista／PHP2Shell／LiteLLM·GitLab·Storm-0940·Railway／QUIC·BIND·Langflow／Mirai·Zeabur·MythicRatatoskr）：四次
>
> 合计 **30 次有效 X 读取，0 次 429**。
> **覆盖说明**：每次查询最多返回 25 条。宽泛的 A/C 查询会被 PHP2Shell 热帖占满，所以 A 类切片时排除了 `php2shell`，再靠专题补回来。剔除了广告／营销、空转发、「Black October」类清单复读、`Python_s_`／`lyrie_ai` 类自动刷屏，以及 Grok 自动回复。
> 窗口内去重后 **605** 条帖子（与 seen_ids 6072 条**零重叠**）。关键词粗筛得 **394** 条安全相关新帖，按最先命中的批次归类：**A115／B28／C63／LWiS46／核心＋IoC 猎人73／专题69**。下文实际引用约 90 条。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**（`/workspace/enrich-2026-10-22/`）：
> - CISA KEV JSON
> - Arista Security Advisory 0199（官网直连返回空页，内容以 BleepingComputer／THN 转述为准）
> - AWS Security Blog（MadPot）
> - cowrAI 蜜罐（GODOFTHUNDER）
> - SOCRadar
> - Zscaler（Armorsteal）
> - Wiz（Storm-0940）
> - ESET WeLiveSecurity 与 eset/malware-ioc（MythicRatatoskr）
> - ISC KB（BIND CVE-2026-94300）
> - THN（KSMBD／QPACK／OpenCode）
> - BleepingComputer（LiteLLM／Railway／Capcom／GitLab）
> - SecurityWeek（Cisco 34 洞）
> - 4tify（k0t）
> - Talos（eMudhra）
> - CVETodo（Langflow）
>
> GitHub API 核对了 nuclei／nuclei-templates／Sliver／BloodHound／NetExec／Mythic／impacket／Havoc／emp3r0r／httpx：窗口内只有 **BloodHound v9.9.0-rc3**（10-21 20:31 UTC-3，昨晚报告已提及），其余没有新的正式 release。Huntress 博客被 Cloudflare 拦截，tldrsec.com 返回 Cloudflare 质询页，这两处只给链接、不转述细节。
> **CISA KEV：catalogVersion 2026.10.21／1754 条，Δ+0**（相对昨天的 2026.10.21／1754）。本日抓取时（约 20:20 UTC-3）`dateReleased` 仍是 2026-10-21 11:04 UTC-3，**今天 KEV 没有更新、没有新增 CVE**，加了 no-cache 参数复核结果一样。
> - **due_today（10-22）：0 条。**
> - **newly_overdue（续）**：
>   - 10-19 到期：BeyondTrust **CVE-2026-102764**、Fortinet **CVE-2025-61624**
>   - 10-18 到期：Atlassian **CVE-2026-21589**
>   - 10-17 到期：AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322
>   - 10-16 到期：Ivanti 104935、Windows 96951
>   - 10-13 到期：Apple 86950
> - **明日 10-23 到期**：**SiteGuard Server Edition CVE-2026-106931**、**Plex CVE-2026-96656**、**Plex CVE-2026-96654**。
> - **11-03 到期**：Plex 96652、Plex 96655、Siemens 110936。
> - **仍未进 KEV、但今日高优先**：
>   - **Arista VeloCloud CVE-2026-114625**：厂商确认在野
>   - **PHP2Shell 109618／109619**：AWS 见 10-17 起尝试，cowrAI 和 Sophos 转述有成功投放 Mirai 的个案
>   - Langflow CVE-2026-105740：单源称在野
>   - GitLab 110264：未见在野
>   - Linux KSMBD 两个未修 RCE：无 CVE、无主线补丁
>   - BIND 94300
>   - Cisco Expressway 76466：未见在野
>
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接，供狩猎用。泄露、入侵类声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【新 0day · 已在野】Arista VeloCloud Orchestrator（VCO）On-Prem CVE-2026-114625（CVSS 9.9，SQL 注入）**：任何已登录用户，哪怕只是「Enterprise Read Only」，都能伪装成本地「superuser operator」。Arista 确认已遭利用，托管版 VCO 已修复；本地部署请升级到 **5.2.3.18／6.1.3.10／6.4.2.12**。厂商点名的攻击 IP 是 `74[.]82.197.86`、`38[.]54.50.151`。这是今年 Arista 第四个被利用的 0day，有帖称「VCO 自 7 月以来第三次」。ZoomEye 统计 VeloCloud 标题暴露约 **520** 个。
- **【PHP2Shell 续 · 利用已落地】**
  - AWS MadPot 在 **10-17**（禁运期内、披露前四天）就记录到一次利用尝试，10-21 02:00–08:00 UTC 又有多次，AWS 公开了 6 个 IP。AWS 说明这些是共享匿名网络 IP，**应排查、不宜直接封**。
  - cowrAI 蜜罐抓到完整链条：PHP-RCE → 加载器 → Mirai 系 DDoS bot「GODOFTHUNDER」，C2 为 `134.199.154.64:50792`。InfraWatchHQ 转述 Sophos 确认有一起成功投放 Mirai 的案例（单源）。
  - Hunt.io 称有一个自 5 月起追踪的僵尸网络在补丁发布约 20 分钟后就加上了 php2shell UA。
  - SOCRadar 在暴露的攻击者服务器上发现针对 8.4.26 mod_php 的武器化脚本，以及对约 20 个站点的条件筛查。
  - Censys 上线了全球修补进度仪表板。
  - 仍未进 KEV。唯一完整修复是升级到 **8.5.12／8.4.27／8.3.36／8.2.35** 并重启所有 worker，排查起点建议从 **10-17** 算。
- **【供应链 · AI】LiteLLM 1.107.0 事后复盘**：
  - PyPI 七个 wheel 在 11:39:51–13:23 UTC 在线；Docker Hub 被污染的镜像索引 `sha256:1bbcb144…c339e` 在 11:46:56–14:20 UTC 在线。
  - 植入方式是 `cook.pth`／`cook.py`／`sitecustomize.py`，每次 Python 启动都会执行，连运行 pip 排查也会触发。数据外带到 `litellm[.]dev/healthcheck`。
  - THN 报道攻击者随后测试了被盗的 AWS 凭据，LiteLLM 怀疑 GitHub OAuth 令牌是从暴露的内部部署日志里泄露的。
- **【PaaS 密钥泄露】Railway**：存放客户环境变量的系统被未授权访问，部分变量可能已被解密。所有部署已暂停，Pro／Enterprise 先恢复构建。官方要求所有用户轮换密钥（含私有镜像仓库凭据）。Railway 称这是针对 AI 推理服务商的一系列攻击的一环。Zeabur 二次被入侵后宣布关停（多帖同报）。
- **【APT · 破坏】ESET：MythicRatatoskr**：一个 Go 后门，把 C&C 藏在 **Yggdrasil** 去中心化 IPv6 网状网络里。UAC-0099 于 2025-07 钓鱼入侵一家乌克兰粮食物流公司，再交接给 **Sandworm**，后者在 2025-09-17 通过 GPO 下发 SDelete 擦除数据。IoC 已公开在 GitHub。
- **【APT · AI 智能体】Storm-0940／ARTEX 续**：Wiz 称其目标扩大到 IT 与软件厂商，用 AI 智能体对 Okta／Entra／Cognito 做密码喷洒等攻击，并公开了 IP 与 UA。CyberScoop 引述 Microsoft 称其「最早 2026 年 9 月」就开始使用 ARTEX。
- **【Linux 内核 · 未修】KSMBD 两个 CVSS 9.0 RCE 在公开邮件列表提前曝光**：ZDI-CAN-33774 无需认证即可在 445 端口触发；ZDI-CAN-33549 需要 SMB Direct／RDMA。目前**都没有 CVE，也没有主线修复**。检查 `ksmbd` 模块是否加载，未修期间请禁用或隔离。
- **【协议 DoS】HTTP/3 QPACK 内存放大**（FoxIO，PoC 已公开，10 个协议栈中 7 个受影响）：quic-go（Caddy／Traefik／cloudflared）、quiche、lsquic、Wireshark 已修；**Bun、aioquic、h3 仍未修**。Bun 实测放大约 4000 倍，可卡死在 100% CPU。
- **【其他高危补丁】**
  - BIND 9 **CVE-2026-94300**：GSS-TSIG 重放导致内存破坏，可能 RCE；修复版 9.20.30／9.21.27，9.18 没有修复。
  - Cisco 一次修 34 个洞，其中 Expressway **CVE-2026-76466**（9.8，集群部署未认证 root RCE，修复版 X15.5.20）。
  - OpenCode 1.0.137–1.18.32 存在恶意 MCP 服务器在 Windows／WSL 登录时执行代码的问题，**没有 CVE**，1.18.33 已修。
  - Laravel token guard 认证绕过 CVE-2026-114509：单源称 PoC 已公开。
- **【恶意软件】**
  - Zscaler：**Armorsteal**（SEO 投毒，仿冒 Chocolatey／MAS 网站，Python 窃密）
  - Zscaler：Citrix **CVE-2026-88771** 被利用投放 FreeBSD Rust 植入 **TimeSmuggler**，与 Sansec 报的 StyleSmuggler 0day 活动重叠
  - Group-IB：**k0t** 大规模打 FortiGate／FortiWeb／GlobalProtect 窃取凭据
  - **SiriusQT** RAT 以 MaaS 形式出售
  - StealC 卖家改名推出 **Stadia** RAT
  - Huntress：「美食」域名 ClickFix 活动
- **【泄露／执法】**
  - Capcom 确认 CAPCOM ID **1170 万**账户泄露（邮箱、IP 等；密码与信用卡未泄露）
  - eMudhra 宣布退出全球 SSL/TLS 发证业务
  - INTERPOL「Serengeti III」逮捕 1462 人
  - Everest 声称窃取 PwC 590GB 数据（**UNCONFIRMED**）

## CVE / POC / 漏洞

### 1. Arista VeloCloud Orchestrator On-Prem · CVE-2026-114625（CVSS 9.9，SQLi→提权为 superuser operator）· **在野 0day**
Arista Security Advisory 0199 于 10-22 发布。攻击者只要有一个普通的已认证会话（包括只读角色），就能通过低复杂度 SQL 注入访问仅供内部使用的功能，以本地「superuser operator」身份操作，进而影响 VCO 主机与它管理的全部 SD-WAN 边缘设备。厂商确认已有攻击。托管 VCO 已修复；本地部署修复版为 **5.2.3.18／6.1.3.10／6.4.2.12**。
修复前的建议：
- 把 VCO Web 界面限制在管理网段，监控来自已知恶意 IP 的连接，复查近期管理员变更。
- 检查 Web 访问日志里异常的类 URL 路径组件、编码字符、指向本地／内部服务的引用，以及高请求速率。
- 怀疑已失陷时，先保全 Web、后端、系统、数据库日志和文件时间戳，再联系 TAC。

MSP 常把 VCO 登录发给客户和承包商，暴露面比看上去大。今年 Arista 已修过三个被利用的 0day（EOS 与 VCO）。ZoomEye 用 `title="VeloCloud"` 统计暴露约 520 个（暴露不等于脆弱）。
- X 原帖：
  - https://x.com/TheHackersNews/status/2113346318953545907 （16:06 UTC-3）
  - https://x.com/BleepinComputer/status/2113319125166542937 （14:18 UTC-3）
  - https://x.com/DarkWebInformer/status/2113292650828726321 （12:33 UTC-3）
  - https://x.com/tsnmediahub/status/2113343389848506879 （15:55 UTC-3，抄录了封禁 IP）
  - https://x.com/phishtimeapp/status/2113372318785474639 （17:50 UTC-3，附厂商公告链接）
  - https://x.com/zoomeyebot/status/2113401342756819214 （19:45 UTC-3，暴露 520）
  - https://x.com/Dinosn/status/2113330112016073143 （LWiS，15:02 UTC-3）
  - https://x.com/cybermergemedia/status/2113336052786323637 （「自 7 月以来第三次」）
- 厂商公告：https://www.arista.com/en/support/advisories-notices/security-advisory/24838-security-advisory-0199
- 文章：
  - https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/
  - https://thehackernews.com/2026/10/arista-warns-of-critical-velocloud-sql.html
  - https://securityonline.info/velocloud-orchestrator-cve-2026-114625-exploited/
  - https://zerohunt.ai/blog/arista-velocloud-cve-2026-114625-sqli-operator-escalation/
- 地址／IoC（厂商公告，经 BleepingComputer 转述）：`74[.]82.197.86`、`38[.]54.50.151`

### 2. PHP 核心 · PHP2Shell CVE-2026-109618／109619 · 后续：**披露前已有利用尝试，有 Mirai 投放个案**
- **AWS（MadPot）**：最早一次尝试在 **2026-10-17**，来自商业匿名网络 IP。PoC 最早约在 10-21 02:00 UTC 出现，02:00–08:00 UTC 又有多次尝试。禁运原定 10-21 14:00 UTC 解除，补丁发布后几小时内 PoC 激增，且几乎立刻被用来打传感器。AWS 建议：
  - 排查从 10-17 算起；
  - 无法立即修补的，可考虑阻断 multipart 上传（先评估业务影响）；
  - 在日志里查表单上传中带 `PHP_SESSION_UPLOAD_PROGRESS` 字符串的 POST；
  - 查异常进程和文件修改。

  另据 @read__the__diff 帖，AWS 还为 Lambda／Elastic Beanstalk 的 PHP runtime 发布了公告，**帖中称尚未公布修复版本**（未独立核实）。
- **cowrAI 蜜罐「GODOFTHUNDER」**：同一行为者躲在商业 VPN／代理后面向多个传感器喷洒未认证 PHP-RCE。触发 bailout 后下发一行命令，拉取 69 字节加载器，再拉取 175KB 的 ELF。这是 Mirai 系 DDoS bot，回连 C2 后对乌克兰第三方主机发起持续洪泛。（报告里有完整命令，本文**不转载**。）
- **Sophos（经 InfraWatchHQ 转述，单源）**：确认一起成功利用并投放 Mirai 变种的案例，受害者未具名，未见勒索或窃数据关联。
- **Hunt.io**：扫描器在网络和指纹上关联到一个自 5 月起追踪的僵尸网络，补丁发布约 20 分钟后首次打到其蜜罐，只是在原有工具上加了 php2shell UA。
- **SOCRadar**：攻击者服务器的目录列表对外暴露，里面有针对 PHP 8.4.26 + Apache mod_php 的「one-click」利用脚本和筛查脚本。筛查的约 20 个站点都不满足前置条件，没有拿到 shell。这条链依赖调试类配置（upload_progress 开、strict mode 关、极低 memory_limit、单 worker），硬化过的生产配置能挡住，但只有升级才能彻底消除风险。
- **Censys** 上线了全球 PHP2Shell 暴露与修补进度仪表板；Rapid7、Aikido 做了直播简报。
- **检测**：
  - Nextron 的 THOR／Sigma／YARA 覆盖
  - Sysdig 的检测文章
  - nuclei 模板（ProjectDiscovery，仅用于资产核查）
  - CyberThreatNet 的 KQL／Splunk／Sigma 查询
  - zin-lay/php2shell-detector
- **噪声提醒**：TensorustAI 称 GitHub 上刷屏的「exploit」多为假仓库；JeskoRiot 称该漏洞 2024 年已被开发者发现（单源，未核实）。请勿运行来路不明的 PoC。
- X 原帖：
  - https://x.com/TheHackersNews/status/2113157293315637466 （03:35 UTC-3，Amazon 10-17）
  - https://x.com/BleepinComputer/status/2113256430006387190 （10:09 UTC-3）
  - https://x.com/SecurityWeek/status/2113206546410926419 （06:51 UTC-3）
  - https://x.com/DuckButTurttle/status/2113165638424506783
  - https://x.com/xxdesmus/status/2113320252876738883 （14:23 UTC-3，Mirai 链）
  - https://x.com/InfraWatchHQ/status/2113348312271311257 （16:14 UTC-3，Sophos 转述）
  - https://x.com/Huntio/status/2113331676818424127 （15:08 UTC-3）
  - https://x.com/DFIR_Radar/status/2113300378343321797 （SOCRadar 来源）
  - https://x.com/DFIR_Radar/status/2113345785932779538 （Nextron）
  - https://x.com/DFIR_Radar/status/2113330701437403585 （Sysdig）
  - https://x.com/censysio/status/2113357354720743914 （16:50 UTC-3，仪表板）
  - https://x.com/rapid7/status/2113331401668075982
  - https://x.com/DhiyaneshDK/status/2113228690293416438 （nuclei 模板）
  - https://x.com/pdiscoveryio/status/2113110871820136726 （LWiS，资产盘点指南）
  - https://x.com/offsectraining/status/2113357985883803664 （LWiS，实验环境）
  - https://x.com/read__the__diff/status/2113400376066011187 （AWS Lambda／EB runtime）
  - https://x.com/TensorustAI/status/2113114427075551285 （假 PoC 提醒）
  - https://x.com/JeskoRiot/status/2113263491612065937 （2024 年已知说，单源）
  - https://x.com/muzuk0/status/2113385618390781967 （取证实验）
  - https://x.com/AviPilcer/status/2113402529547501737 （OpenAI「Patch the Planet」与 CISA 警报）
  - https://x.com/CyberThreatNet/status/2113373864705077268 （狩猎查询）
  - https://x.com/z1nk57/status/2113163905895919988 （检测器）
- 厂商公告：
  - https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/
  - https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching
  - https://censys.com/advisory/cve-2026-109618-cve-2026-109619/
- 文章：
  - https://cowrai.com/research/php2shell-godofthunder/
  - https://socradar.io/blog/php2shell-exploit-tooling-attacker-server/
  - https://www.nextron-systems.com/2026/10/22/php2shell-detection-coverage-in-thor/
  - https://webflow.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core
  - https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html
  - https://www.bleepingcomputer.com/news/security/amazon-says-php2shell-exploitation-began-4-days-before-patches/
  - https://www.securityweek.com/php2shell-exploitation-started-days-before-patches/
  - https://www.securityweek.com/tech-and-security-companies-respond-to-php2shell-vulnerabilities/
  - https://php2shell.censys.com
- GitHub·PoC／检测仓库（只给链接，供核查和狩猎）：
  - https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-109618.yaml
  - https://github.com/CyberThreatNet/hunt-lab
  - https://github.com/zin-lay/php2shell-detector
  - 研究型 PoC：https://github.com/9bie/php2shell-bypass-aslr-exp （由 @muzuk0 引用，**勿在生产环境运行**）
- 地址／IoC：
  - AWS MadPot：`103.216.220.92`（10-17）、`31.223.184.166`、`37.19.200.5`、`134.209.159.64`、`103.114.163.188`、`95.217.98.37`（以上 5 个为 10-21）。AWS 原注：属共享匿名基础设施，建议排查而非直接封禁。
  - cowrAI：
    - 投递源：`85.11.167.243`、`217.60.242.76`、`45.198.224.169`
    - 加载器／载荷托管：`92.118.112.100`
    - C2：`thunder.godofthunder[.]st`，引爆时解析到 `134.199.154.64:50792`
    - 其他关联：`45.88.138.0`、`45.88.138.44`
    - SHA256：加载器 `4d02f14d109458cb0d696b65456918fcd724ca385aa30c688f08554c8899938c`；bot `0c5486f06620e26e316f4b33f318b0d646d5e1133789331aa2fed012360d1486`
  - SOCRadar 攻击者服务器：`206.188.197[.]105`（端口 9999／8899／8888）
  - 日志特征：表单上传中带 `PHP_SESSION_UPLOAD_PROGRESS` 的 POST（AWS）

### 3. GitLab · CVE-2026-110264（CVSS 10.0）· 后续
没有新的在野报告，也未进 KEV。比利时 CCB 发警报要求立即修补；BleepingComputer 跟进称这是 10 天内第二个满分正则漏洞（前一个是 97229）。修复版：**19.5.1／19.4.3／19.3.6／19.2.9／19.1.9／19.0.10／18.11.13**；GitLab Dedicated 19.3.5-internal0 和 19.4.2-internal0 以上已包含修复。
- X 原帖：
  - https://x.com/BleepinComputer/status/2113234434203722162 （08:42 UTC-3）
  - https://x.com/CCBalert/status/2113295089480933626
  - https://x.com/Joshua_WD/status/2113228374327820645
- 厂商／CERT 公告：https://ccb.belgium.be/advisories/warning-critical-unauthenticated-remote-code-execution-gitlab-patch-immediately
- 文章：https://www.bleepingcomputer.com/news/security/gitlab-warns-of-new-max-severity-code-execution-vulnerability/
- 地址／IoC：未见公开 IoC

### 4. Linux 内核 KSMBD · ZDI-CAN-33774／ZDI-CAN-33549（各 CVSS 9.0，RCE）· **无补丁、无 CVE**
- **33774**：任何在 445 端口跑 KSMBD 的服务器都受影响，无需认证。成因是 SMB1／SMB2 处理表分配的竞态，导致越界读，拿到共享访问后还有越界写路径。
- **33549**：需要 SMB Direct 和支持 RDMA 的网卡，是整数下溢。

两份报告由 ZDI 抄送到公开邮件列表，没附补丁，Greg KH 公开批评。截至 10-22，主线内核没有确定的修复；RHEL 默认不带 KSMBD。处置：用 `systemctl status ksmbd`／`lsmod | grep ksmbd` 确认是否启用，未修期间禁用或隔离 445。
- X 原帖：https://x.com/TheHackersNews/status/2113315655512731872 （14:04 UTC-3）
- 文章：https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html
- 地址／IoC：未见公开 IoC

### 5. HTTP/3 QPACK 内存放大 DoS（FoxIO，PoC 已公开）
一条连接就能让服务器 OOM；Bun 因计数器溢出会卡死在 100% CPU。各实现状态：

| 状态 | 实现 |
|---|---|
| 已修 | quic-go（CVE-2025-64702）、Cloudflare quiche（CVE-2026-12523）、lsquic、Wireshark |
| 未修 | Bun、aioquic、h3（Rust） |
| 不受影响 | IIS、Envoy、ngtcp2/nghttp3、Google quiche |

临时措施：Bun 不要对外暴露 HTTP/3；h3 设置 `max_field_section_size`；mitmproxy 关闭 http3。
- X 原帖：
  - https://x.com/TheHackersNews/status/2113162336110604645 （03:55 UTC-3）
  - https://x.com/2Workly/status/2113269368809574442
- 文章：https://thehackernews.com/2026/10/new-qpack-flaws-can-crash-http3-servers.html
- 地址／IoC：未见公开 IoC

### 6. ISC BIND 9 · CVE-2026-94300（GSS-TSIG 重放 → 内存破坏，可能 RCE）
攻击者截获一条已签名的 GSS-TSIG UDP 报文，在 TSIG 密钥有效期内重放，同时向自己控制的区发送特制查询，就可能触发内存破坏，甚至 RCE。CVSS 向量为 AV:N/AC:H/PR:N。修复版 **9.20.30／9.21.27**，**9.18 没有修复**。GSS-TSIG 是 AD 客户端做安全动态更新的路径。ISC 致谢 OpenAI 的 Dave Aitel 独立报告。
- X 原帖：
  - https://x.com/PumpkinSecurity/status/2113405677909782789 （20:02 UTC-3）
  - https://x.com/i0n1c/status/2113299665588556246 （LWiS，13:01 UTC-3）
- 厂商公告：https://kb.isc.org/docs/cve-2026-94300
- 地址／IoC：未见公开 IoC

### 7. Cisco 10-21 批量补丁（34 个洞）· Expressway CVE-2026-76466（9.8，未认证 root RCE）
Expressway 的集群部署因持久 cookie 和客户端证书校验不足，攻击者可以连上数据库服务并调用 RPC，以 root 执行命令。修复版 **X15.5.20**。同批还有：
- UC 产品三个严重 CVE：76473／76474／76475
- Snort 3 的 20236／20043（修复版 3.12.4.0）
- IOS XR 76505、Secure Client 76462

Cisco 称**未见在野利用**。
- X 原帖：
  - https://x.com/CCBalert/status/2113297145398788428 （12:51 UTC-3）
  - https://x.com/SecurityWeek/status/2113210321926246837 （07:06 UTC-3）
- 厂商公告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t
- 文章：https://www.securityweek.com/cisco-patches-34-vulnerabilities-across-multiple-products/
- 地址／IoC：未见公开 IoC

### 8. Langflow · CVE-2026-105740（CVSS 9.9，需认证的 RCE）· 单源称在野
CVETodo 引用 Previdian 的数据：到 10-19 仍有利用尝试。版本 1.9.0 之前，用 Stdio 传输添加 MCP 服务器时，命令字段会被直接执行。1.9.0 修了第一处，但相关注入还需要 **1.10.3** 才补全。**不在 KEV 中。** 注意：昨晚线索里的「CVE-2026-0770」应以本条为准。
- X 原帖：https://x.com/CveTodo/status/2113314810284683643 （14:01 UTC-3）
- 文章：https://cvetodo.com/news/critical-langflow-rce-flaw-cve-2026-105740-under-active-exploitation-after-patches-released
- 地址／IoC：未见公开 IoC

### 9. OpenCode · 恶意 MCP 服务器登录时执行代码（Windows／WSL，**无 CVE**）
受影响版本 1.0.137–1.18.32，已在 1.18.33 修复（9-28 发布）。开发者执行 `opencode mcp auth` 时，服务器提供的 OAuth 授权端点 URL 会被拼进 PowerShell 命令，且没有转义。报告方给出的建议分为 9.8。没有 CVE，扫描器不会报出受影响版本。另外 vxunderground 的当日汇总提到「OpenCode leaking API keys」，细节未核实。
- X 原帖：
  - https://x.com/TheHackersNews/status/2113219984365359340 （07:44 UTC-3）
  - https://x.com/vxunderground/status/2113086117927178490 （LWiS，当日事件汇总）
- 文章：https://thehackernews.com/2026/10/opencode-flaw-lets-malicious-mcp.html
- 地址／IoC：未见公开 IoC

### 10. 其他漏洞线索（简列）
- **Node.js CVE-2026-111497（Brotli 越界写）**：修复版 22.23.4／24.22.1／26.12.1，**20.x 已 EOL 没有补丁**。帖称尚无在野利用，并提及 PoC（细节见原帖）。
  - X：https://x.com/TheHackersNews/status/2113176153666326609 、https://x.com/BlueFairyDevs/status/2113247304375271841
  - 文章：https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html
  - GitHub：https://github.com/google/brotli/commit/0ed4268a4401abcb44720963 （来自 @N3mes1s https://x.com/N3mes1s/status/2113384217576886476 ）
  - 地址／IoC：未见公开 IoC
- **Laravel token guard 认证绕过 CVE-2026-114509（9.2）**：据 CSIRT Toscana 已有公开 PoC，只影响 MySQL/MariaDB 上的 `'driver' => 'token'` guard，Sanctum／Passport 不在公告范围（单源，未核实）。
  - X：https://x.com/catcowbug/status/2113369194150412352 （17:37 UTC-3）
  - 地址／IoC：未见公开 IoC
- **Juniper J-Web CVE-2026-101954**：可未认证接管；未进 KEV，厂商称未见利用；修复版 25.2R2-S2 等。
  - X：https://x.com/snypet86/status/2113087039880962150 （10-21 22:56 UTC-3）
  - 厂商：https://supportportal.juniper.net/s/article/2026-10-Security-Bulletin-Junos-OS-and-Junos-OS-Evolved-Multiple-vulnerabilities-resolved
- **Check Point CVE-2026-85102 续**：自 9-12 起被利用，9-22 入 KEV，10-7 出现公开 PoC，约 11849 个网关可能暴露。
  - X：https://x.com/leonov_av/status/2113338499156111616
  - 文章：https://avleonov.com/2026/10/12/i177-about-remote-code-execution-check-point-quantum-security-gateway-cve202685102-vulnerability/
- **SMB 签名绕过新技术**：@_dirkjan 转介，称近期 Windows 版本似已修补。
  - X：https://x.com/_dirkjan/status/2113345594676691065 （LWiS）→ https://x.com/aas_s3curity/status/2113054299001373025
- **Adobe Acrobat CVE-2026-81983**：745 字节的 PDF 就能触发整数溢出和越界写（Remedio 披露）。
  - X：https://x.com/ProximusLabs/status/2113323388538364335
- **KEV 明日 10-23 到期的三条**（SiteGuard 106931、Plex 96656／96654）有多帖提醒：
  - https://x.com/ZeroKaiLabs/status/2113225429196931446
  - https://x.com/BrotherZero777/status/2113314797601329371
  - https://x.com/BrotherZero777/status/2113358589263827332
  - 厂商：https://www.eg-secure.co.jp/siteguard/news/alert-202610-1
- **已逾期 KEV 的后续报道**：
  - BeyondTrust 102764：中国关联团伙利用了数周，链条为 webshell → root → vault dump → 隧道。https://x.com/threatroundup/status/2113286399067660701 ；文章 https://threatroundup.com/news/armory-castle-beyondtrust-exploitation/
  - Atlassian 21589：有探测。https://x.com/packetninjas/status/2113363908845039656
- **Splunk／SolarWinds 安全更新**：https://www.securityweek.com/splunk-solarwinds-release-fresh-security-updates/ （X：https://x.com/SecurityWeek/status/2113220783250067593 ）
- **Oracle 10 月 CPU（1200+ 漏洞）**：https://www.securityweek.com/oracle-patches-over-1200-vulnerabilities-with-october-2026-cpu/ （X：https://x.com/SecurityWeek/status/2113173582838956500 ）
- **Signal 漏洞：恶意来电方可阻止对方挂断**：https://www.securityweek.com/signal-vulnerability-lets-malicious-callers-block-hang-ups/
- **CISA 发布 19 个新增、1 个更新的 ICS 公告**：https://x.com/CISACyber/status/2113343865058918848 → https://go.dhs.gov/iEv
- **疑似机器人账号**：`lyrie_ai` 等账号批量发「0day Intel」帖（SharePoint 50522、49176、50454 等），**疑似自动生成，未采信**。

## 工具与 GitHub 发布

- **LiteLLM v1.107.0「PrivCollect」应急工具包**（IoC、YARA、离线扫描器、响应指引；作者自述借助 AI 编写，使用前请自行审阅）：
  - X：https://x.com/PeterDaveHello/status/2113264022489604359 （10:39 UTC-3）
  - GitHub：https://github.com/PeterDaveHello/litellm-privcollect-toolkit
- **PHP2Shell 检测／狩猎**：
  - nuclei-templates CVE-2026-109618：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-109618.yaml
  - CyberThreatNet hunt-lab（KQL／Splunk／Sigma）：https://github.com/CyberThreatNet/hunt-lab
  - zin-lay/php2shell-detector：https://github.com/zin-lay/php2shell-detector
  - ProjectDiscovery 的 securetheweb.org：https://securetheweb.org/
  - Censys 仪表板：https://php2shell.censys.com
- **DLLParty**（演示「DLL party」进程注入技术，红蓝双方均可参考检测）：
  - X：https://x.com/CyberWarship/status/2113200948378058857
  - GitHub：https://github.com/epersic/DLLParty/
- **llm-redteam-harness**：离线运行 AgentDojo 注入套件。工具白名单把 travel 场景 ASR 从 82.9% 降到 3.6%，banking 场景只从 97.9% 降到 31.9%，说明白名单不是完整防御。
  - X：https://x.com/eyemotors/status/2113121874804945359
  - GitHub：https://github.com/globe-teck/llm-redteam-harness
- **orlofv/Indicators**（Shodan 抓到的 SliverC2 服务器列表，持续更新）：https://github.com/orlofv/Indicators/blob/main/SliverC2 （X：https://x.com/orlof_v/status/2113267309032698298 ）
- **ESET malware-ioc**（MythicRatatoskr）：https://github.com/eset/malware-ioc/tree/master/mythicratatoskr
- **Corelight：用 Zeek 检测被盗 eMudhra 证书**：https://corelight.com/blog/detect-compromised-emudhra-certificates-zeek （X：https://x.com/DFIR_Radar/status/2113391109049340264 ）
- **Hackvertor UI 更新**（@garethheyes，LWiS）：https://hackvertor.co.uk/
- **框架 release 核对**：窗口内只有 BloodHound v9.9.0-rc3（https://github.com/SpecterOps/BloodHound/releases/tag/v9.9.0-rc3 ，10-21 20:31 UTC-3，昨晚报告已列）。nuclei（v3.11.1）、Sliver（v1.7.8）、NetExec、Mythic、impacket、emp3r0r（v5.3.0，10-16）、httpx 均无新版。
- **其余**：B 类 GitHub 批次里多为 AI 工具或论文代码（如 Easydict、GhostSwitch），以及「10 个侦察仓库」类营销清单，和安全无关或不是新发布，**本日无其他显著更新**。

## APT / Malware 分析

### 1. ESET · MythicRatatoskr（Go 后门，C&C 藏在 Yggdrasil 网状网络）· UAC-0099 → Sandworm 交接，最终擦除数据
时间线：
- 2025-07-16：UAC-0099 用鱼叉邮件入侵一家乌克兰粮食物流公司，执行链落地 MATCHBOIL → MATCHWOK 后门。
- 次日：部署全新后门 MythicRatatoskr，以 Windows 服务持久化，配置 AES 加密，C&C 通过 Yggdrasil 内的 HTTPS 通信，另部署 SOCKS5 代理。
- 2025-09-17：Sandworm 经 AD 组策略下发 SDelete，全网擦除数据。

ESET 以高置信度判断 UAC-0099 把访问权移交给了 Sandworm。ESET 指出 Yggdrasil 本身不提供匿名性，可以尝试定位网络中的节点，并据此追查了 C&C。注意：样本内置的 Yggdrasil peer 列表多为公共 peer，**不宜直接当 IoC 封禁**。
- X 原帖：
  - https://x.com/ESETresearch/status/2113193995400630579 （06:01 UTC-3，1/6）
  - https://x.com/ESETresearch/status/2113194002103103516 （IoC 6/6）
- 文章：https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/
- GitHub：https://github.com/eset/malware-ioc/tree/master/mythicratatoskr
- 地址／IoC：
  - MATCHWOK C&C：`hxxps://uztickets[.]com`；投递 URL：`hxxps://egyptanimals[.]com/animals/photoalbum`
  - Yggdrasil C&C：`b479:2771:8df4:b5eb:d007:63b0[:]2838`
  - SHA-1（MythicRatatoskr）：`D5F9288DAEBF87AE4579945F8DC6CF235B093CFD`（Act64.exe）、`B69EF0E45B401440C0FDE22046775D0C57E87415`（ie.exe）、`4E3E6577866E4CE2ED73CA089700AE04230E768F`、`69969EEB7E0A3D84C4E70193636FCF934C6AA388`、`8CEB5F8BCDF4995B7164996F1429D682613BB17B`（ieupdate.exe）、`01855153CA7A33AD5FF36451DE5612DFBA0DD2CA`（krbtman.exe）、`E29AF83A07FB32EB47C28733A9382E766D53F704`（OneDriveLiveUpdater.exe）、`028CA11F3F0D8396043AF7BF756231FC2F50F829`、`9085896989947C0919A660352F75F6B233FC645B`（windowsdefendersvc.exe）、`D7E6A5A46C6ED3510997E91B11E51BE0250FD2A2`（updater.exe）
  - SHA-1（SOCKS5）：`131A371A1E4EE78EC3B2863607C99290EC3B58A6`（krbtman.exe）、`09C816697C0C2AFF9B4FF58681558CA30D04C9CD`（nbtresolver.exe）

### 2. Storm-0940／ARTEX · Wiz：目标扩大到 IT 与软件厂商
Wiz 追踪到这个使用 ARTEX 智能体框架的中国关联行为者，正把 ConnectWise 事件后的攻击扩展到更多 IT／软件厂商，用 AI 智能体对 Okta、Entra、Cognito 做密码喷洒和批量访问，日志里会留下「大量 Access Denied」这类可检测模式。CyberScoop 引述 Microsoft 称其「最早于 2026 年 9 月」开始使用 ARTEX。
- X 原帖：
  - https://x.com/wiz_io/status/2113284193975255255 （11:59 UTC-3）
  - https://x.com/TheHackersNews/status/2113123818302812408 （01:22 UTC-3）
  - https://x.com/CyberScoopNews/status/2113372900010938667
  - https://x.com/rst_cloud/status/2113350049258238308
- 厂商：https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
- 文章：
  - https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors
  - https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html
- 地址／IoC（Wiz）：
  - IP：`104.194.150.21`、`144.172.64.60`、`144.172.64.99`、`144.172.64.128`（后三个 Microsoft 归因 Storm-0940）、`167.88.172.97`
  - UA（Wiz 注明噪声大，不宜单独狩猎）：`curl/7.88.1`、`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36`

### 3. LiteLLM 1.107.0 供应链（第二次）· 复盘细节
- **受影响制品**：
  - PyPI 七个 wheel：11:39:51–13:23 UTC
  - Docker Hub 的 v1.107.0／latest／main-latest／main-stable 指向被污染的索引：11:46:56–14:20 UTC
  - GHCR：13:51 UTC 前下线
- **植入**：只改了安装包，没动应用代码。植入 `cook.pth`、`cook.py`、`sitecustomize.py`，每次启动 Python 都会执行。
- **窃取范围**：云凭据、AI 工具凭据、Git／npm／PyPI／CI 凭据、SSH／GPG／TLS 密钥、浏览器数据。数据用 AES-256-CBC 加密（密钥再用 RSA-4096 加密）后外带。
- **后续**：THN 称攻击者随后测试了被盗的 AWS 凭据。
- **处置**：按 digest 固定到 **1.106.2**；凡在上述时段拉取过的环境都按已失陷处理，轮换全部凭据。
- X 原帖：
  - https://x.com/BleepinComputer/status/2113347944132784601 （16:13 UTC-3）
  - https://x.com/TheHackersNews/status/2113187202020814927 （05:34 UTC-3）
  - https://x.com/DFIR_Radar/status/2113209876344197210
  - https://x.com/DFIR_Radar/status/2113406149441585493
  - https://x.com/theomlondhe/status/2113270522087624831
- 文章：https://www.bleepingcomputer.com/news/security/litellm-release-pipeline-hacked-to-distribute-info-stealer-malware/
- GitHub：https://github.com/PeterDaveHello/litellm-privcollect-toolkit
- 地址／IoC：Docker 镜像索引 `sha256:1bbcb1443bc962e45f5aad53fe3d2c30600e0379715fb6c664cdd3ac126c339e`；外带端点 `litellm[.]dev/healthcheck`；文件名 `cook.pth`、`cook.py`、`sitecustomize.py`

### 4. Zscaler · Armorsteal（Python 窃密，SEO 投毒仿冒 Chocolatey／MAS）
搜索结果被投毒，把受害者引到仿冒的 Chocolatey 和 Massgrave（MAS）网站。投放的 install.ps1 会同时运行真正的 Chocolatey 安装器作掩护，再装三个模块：远控（HTTPS，4 个硬编码 C2 域名，带 RSA-2048 任务签名）、监控（截屏加密）、窃密（Chromium 无头浏览器）。基础设施在 2026 年 9 月和 10 月两次轮换。
- X 原帖：
  - https://x.com/DFIR_Radar/status/2113314984922862048 （14:02 UTC-3）
  - https://x.com/DFIR_Radar/status/2113314988282581353
- 文章：https://www.zscaler.com/blogs/security-research/seo-poisoning-campaign-delivers-new-armorsteal-malware
- 地址／IoC（Zscaler）：
  - 域名：`choclatey[.]org`（含 `community[.]choclatey[.]org`，仿冒 Chocolatey）、`massgravel[.]net`（仿冒 MAS）
  - C2：`workerstats[.]net`、`pymons[.]is`、`datamons[.]org`（先待机后启用）；待机 C2：`niceer[.]net`、`supertrap[.]net`
  - 文中出现的 IP：`82.153.135[.]80`、`186.2.175[.]183`、`186.2.163[.]185`、`190.115.31[.]69`、`209.99.186[.]187`、`104.21.87[.]146`（后者是 Cloudflare 段，慎封）
  - SHA256：
    - install.ps1：MAS 诱饵 `f3846ec2a6ff0a27d9ef2b9bf7908743b81d295ef29344acfb96ff83fff994f9`；Chocolatey 诱饵 `fb1181160e9f10ce1eb5e5dc9bc23e1498a39110ee9ea361fd150454cb01b292`
    - 远控模块：Update.zip `3e3b62a9836697d978cbb620dc8af8f6eefdf8cb73fc30d16bb394d1c58f4c97`；SysMon.py `0ea99fbbe29af6f797e3866ed5f822c7a5d3e9cdb990a8c382a715069f156499`
    - 监控模块：nig20084.zip `237ba698d7dc8936c43e0e78e7644002375e51e8baf9b3a7d4e18683f871ee31`；basrq.py `8fb7aaf2b9270b8b75f6844aaefd5242b4f926fb89cba10fff3d9b908a769788`
    - 窃密模块：getthem20084.zip `be0329d0795dd62ae587faf97e704bb36413e5c98ddd8fe575f5077db3c84e5f`；got.py `5410c2f239c3649928383c4478dea182f90b21f5b258081fec07e9d297ae4b1c`
    - 旧版：nig20083.zip `04d2828155ed2a276cfd3c97d4f966d328391dd818e04e773212cd601e49fa74`；getthem20083.zip `56f05c4fb1c25c04e0dde60e2e5e41ac164a6dc53688d0f9eb52a55f82106389`

### 5. Zscaler ThreatLabz · Citrix CVE-2026-88771 → FreeBSD Rust 植入「TimeSmuggler」
ThreatLabz 观察到攻击者利用 Citrix CVE-2026-88771 投放一个基于 FreeBSD、用 Rust 写的后门 TimeSmuggler。Sansec 在 StyleSmuggler（Magento）0day 活动中也看到同一恶意软件被分发。完整分析请看原帖链接（窗口内没抓到附带 IoC）。
- X 原帖：https://x.com/Threatlabz/status/2113308058629853206 （13:34 UTC-3）
- 相关：BleepingComputer「Magento StyleSmuggler zero-day exploited to deploy Linux backdoor」（BleepingComputer 站内相关文章标题，正文未单独抓取）
- 地址／IoC：未见公开 IoC（窗口内帖文未附）

### 6. Group-IB／NyxLab · k0t 大规模攻击 FortiGate／FortiWeb／GlobalProtect 窃取凭据
k0t 利用 **CVE-2025-64446**（FortiWeb 路径穿越）、**CVE-2026-0257**（GlobalProtect）和弱口令／默认口令，从设备配置里导出 LDAP/AD 服务账号等凭据（帖称涉及 7 万多条），之后部署 MeshCentral 等 RMM 并用 Rclone 外传。处置：打补丁；管理面不要暴露在公网；轮换设备中存储的所有凭据；FortiGate 启用组织自控密钥的私有数据加密；排查非自建的 MeshCentral／Atera 和 Rclone。
- X 原帖：
  - https://x.com/LandscapeThreat/status/2113361051857076360 （17:05 UTC-3，含 IoC）
  - https://x.com/DEVOTOMSOLUTION/status/2113285337975796084
  - https://x.com/BrotherlyTechHQ/status/2113265139059429783
- 文章：https://4tify.io/article/k0t-campaign-hits-fortigate-fortiweb-and-globalprotect-to-harvest-credentials
- 地址／IoC（转自 @LandscapeThreat）：`mesh[.]buttruyen[.]com`、`62[.]60[.]131[.]43`、`Meshcentral[.]girydsfsggvb[.]com`、`62[.]60[.]135[.]64`

### 7. 其他恶意软件与活动
- **SiriusQT**：Windows RAT 加窃密，自 2026-04 起以 MaaS 出售，至少 30 个付费买家、146 个许可令牌，在英、德、法、西、意、荷都有活动。
  - X：https://x.com/DFIR_Radar/status/2113179237926797667 （05:02 UTC-3）
  - 地址／IoC：未见公开 IoC（帖文未附）
- **Stadia RAT**：StealC 卖家在 Operation Endgame（2026-06）四个月后改名回归。Stadia 带 HVNC、远程 shell、内存加载，StealC 作为六个模块之一。
  - X：https://x.com/DFIR_Radar/status/2113284875448938709
  - 地址／IoC：未见公开 IoC
- **Huntress：「美食」域名 ClickFix**：从 Google 搜索「Amazon business」开始，诱导到 grillmasterspro、EmbersAndBites 等域名。博客对本机被 Cloudflare 拦截，未核对细节。
  - X：https://x.com/HuntressLabs/status/2113285290164892085 （12:04 UTC-3）
  - 文章：https://www.huntress.com/blog/amazon-clickfix-finger
  - 地址／IoC：帖文只给出域名名称片段 grillmasterspro、EmbersAndBites，没有完整 TLD，未作 IoC 收录
- **Unit 42**：用 AI 建站工具搭钓鱼页，配合聊天应用收集凭据。另一篇报告分析行为者借助 AI 规划多类网络犯罪，涉及 Hermes、Ncat，受害者在印度。
  - X：https://x.com/Unit42_Intel/status/2113398262094831991 、https://x.com/rst_cloud/status/2113327296241156488
  - 文章：https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/
  - 地址／IoC：未见公开 IoC
- **Forescout：法国 700 多家超市的 Danfoss AK-SM／AK-SC 冷链控制系统被入侵**，温度和除霜被篡改。
  - X：https://x.com/DFIR_Radar/status/2113361268035797082
  - 文章：https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/
  - 地址／IoC：未见公开 IoC
- **Zimperium：Android Intrusion Logging 还原了 RatHat 完整杀伤链**（从 ADB 自配对到 C2 外连）。
  - X：https://x.com/DFIR_Radar/status/2113376087228993720
  - 文章：https://zimperium.com/blog/beyond-the-sandbox-leveraging-android-intrusion-logs-to-expose-advanced-threats
  - 地址／IoC：未见公开 IoC
- **SliverC2 服务器（@orlof_v，Shodan，高置信）**：
  - X：https://x.com/orlof_v/status/2113267309032698298 （10:52 UTC-3）
  - GitHub：https://github.com/orlofv/Indicators/blob/main/SliverC2
  - 地址／IoC：`130.94.20[.]71`、`141.11.32[.]132`、`2.27.248[.]209`、`67.207.95[.]101`，另 2 个见仓库链接
- **IoC 猎人当日样本（abuse.ch／MalwareBazaar）**：
  - @smica83 'DEW_protected.exe'（黎巴嫩）：`67c10a4f7db7fe55953b9b57492d4e6aa9cf0e20f492d193328def2662840c97`，经 `api.telegram(.)org` 通信。https://x.com/smica83/status/2113375121545236514
  - @smica83 'Invitation to an Important Banquet – October 23rd – FF.rar'（柬埔寨）：`914adfba2837c786986bb16577f630e3355bb1984fc82e6d642657e790e6dbf8`；`104.143.42(.)209:22`；`wwppodd6688(.)com`。https://x.com/smica83/status/2113374095416905793
  - @smica83 柬埔寨电费主题 rar：`b199422fe5f11a4c532f05fbca85446edd426c70fb4f330bb7f78e566f5bd66a`；`ababy9(.)com`。https://x.com/smica83/status/2113351070315642931
  - @smica83 'Forecaster.msi'（丹麦、哈萨克斯坦）：`09af553a032ac6591b9f1271ade103549946640a82136dc2cee4b1da6a488552`；`smaluf(.)net:3857`；`77.220.212(.)113:2084`。https://x.com/smica83/status/2113348751532118078
  - @smica83 'NARCOTICS NETWORK AND POLICE FACILITATION.doc'（巴基斯坦）：`e6eca876f1e4423eadde8298c879774118f094d0b714a9dd202883b50ddc02dc`。https://x.com/smica83/status/2113350145672884651 （关联 @malwrhunterteam https://x.com/malwrhunterteam/status/2113348453837181349 ，域名 `helensolution[.]info`）
  - @smica83 'Reader_en_install.iso'：`5f4bf788c53ba55b9ed13ac1d71e636ed6d378c7d04ff1bd9d2ec52015cf36df`，来源 `hxxps://pixeldrain(.)com/api/file/LEfVj7fg?download`。https://x.com/smica83/status/2113342928957415879 （关联 @malwrhunterteam `172.82.64[.]48` https://x.com/malwrhunterteam/status/2113341322392133833 ）
  - @smica83 FUD 'Client_Matter_Document zip'（韩国）：`6930ec46d217c854d7e5731e5efad4757eeb344e28386742586a33f455d8b401`。https://x.com/smica83/status/2113373037047246960
  - @malwrhunterteam：`104.194.141[.]56`、`sunmerksin[.]com`、`placewingarage[.]com`。https://x.com/malwrhunterteam/status/2113378811026825565
  - @malwrhunterteam 面板「ARVION — Login」：`arvion[.]network`。https://x.com/malwrhunterteam/status/2113314922159599908
  - @skocherhan：`193.143.1[.]142`（AS198953 Proton66，关联 @TheGentlemen26）。https://x.com/skocherhan/status/2113334198782288175 ；`gist[.]github[.]com/HenrySmith202`。https://x.com/skocherhan/status/2113373688724926523
  - @500mk500 privatestress 系列域名：`privatestress.com／.icu／.pw／.ru／.st`。https://x.com/500mk500/status/2113331085819941375

### 8. 泄露／入侵／执法（**UNCONFIRMED 的已标注**）
- **Capcom 确认 CAPCOM ID 泄露**：1170 万邮箱，另有创建时间、最后登录时间和 IP。43 个账户还泄露了生日等信息；196 个账户的密码被攻击者改掉，已重置。密码和信用卡未泄露。10-19 发现，10-21 报警。
  - X：https://x.com/BleepinComputer/status/2113365529255707120 （17:23 UTC-3）
  - 文章：https://www.bleepingcomputer.com/news/security/capcom-confirms-data-breach-affecting-117-million-accounts/ 、https://cyberinsider.com/capcom-data-breach-affecting-11-7-million-accounts-worldwide/
- **Railway 环境变量泄露**（官方确认存在未授权访问）：
  - X：https://x.com/BleepinComputer/status/2113381316959871278 、https://x.com/TheHackersNews/status/2113229957040336907
  - 文章：https://www.bleepingcomputer.com/news/security/railway-warns-devs-to-rotate-secrets-after-potential-breach/
- **eMudhra 退出全球 SSL/TLS 发证业务**：起因是 8 把中间 CA 私钥可被猜出；Chrome／Firefox 撤销对其 ECC 根的信任，约 3 万张证书需要更换。Talos 和 Corelight 发布了检测方法。
  - X：https://x.com/TheHackersNews/status/2113333814894412268 、https://x.com/TalosSecurity/status/2113254607065346255
  - 文章：https://blog.talosintelligence.com/compromised-intermediate-certificates/ 、https://www.theregister.com/security/2026/10/22/disgraced-indian-cert-issuer-leaves-the-cert-issuing-business/5304848
- **INTERPOL「Serengeti III」**：21 国参与，逮捕 1462 人，瓦解 10909 个恶意网络，追回 1.05 亿美元以上。
  - X：https://x.com/TheHackersNews/status/2113264290878886147 、https://x.com/BleepinComputer/status/2113185455193698512
  - 文章：https://thehackernews.com/2026/10/interpol-arrests-1462-suspects-disrupts.html
- **UNCONFIRMED／未验证**：
  - Everest 声称窃取 PwC 590GB 数据，已启动倒计时：https://x.com/DailyDarkWeb/status/2113406674224750645
  - Kirkland & Ellis 被列上「leakeddata」泄露站：https://x.com/DailyDarkWeb/status/2113304072082313320
  - Qilin 声称攻击 SEPIVER（墨西哥）和 United Restaurant Supply（美国）：https://x.com/FalconFeedsio/status/2113389024853537249 、https://x.com/FalconFeedsio/status/2113326574355484890
  - SoftBank、EsSalud、SoundCloud S3、Kinguin 等泄露声称（DailyDarkWeb 系列）均未核实。

## 地址／IoC 汇总

> 全部原样抄录自所引原帖或厂商／研究文章，防御用途。共享匿名网络、Cloudflare 段和公共 Yggdrasil peer 请先排查再决定是否封禁。

| 类型 | 指标 | 关联 | 来源 |
|---|---|---|---|
| IP | `74[.]82.197.86`、`38[.]54.50.151` | Arista VCO CVE-2026-114625 攻击 IP | https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/ |
| IP | `103.216.220.92`（10-17）、`31.223.184.166`、`37.19.200.5`、`134.209.159.64`、`103.114.163.188`、`95.217.98.37` | PHP2Shell 早期尝试（匿名网络，建议排查不封） | https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/ |
| IP | `85.11.167.243`、`217.60.242.76`、`45.198.224.169`（投递）；`92.118.112.100`（载荷）；`134.199.154.64:50792`（C2）；`45.88.138.0`、`45.88.138.44` | PHP2Shell → GODOFTHUNDER Mirai | https://cowrai.com/research/php2shell-godofthunder/ |
| 域名 | `thunder.godofthunder[.]st` | GODOFTHUNDER C2 | 同上 |
| SHA256 | `4d02f14d109458cb0d696b65456918fcd724ca385aa30c688f08554c8899938c`（加载器）、`0c5486f06620e26e316f4b33f318b0d646d5e1133789331aa2fed012360d1486`（bot） | GODOFTHUNDER | 同上 |
| IP | `206.188.197[.]105`（:9999／:8899／:8888） | PHP2Shell 攻击者工具服务器 | https://socradar.io/blog/php2shell-exploit-tooling-attacker-server/ |
| 字符串 | `PHP_SESSION_UPLOAD_PROGRESS`（POST 表单） | PHP2Shell 日志狩猎 | AWS 同上 |
| SHA256 | `1bbcb1443bc962e45f5aad53fe3d2c30600e0379715fb6c664cdd3ac126c339e` | LiteLLM 被污染的 Docker 镜像索引 | https://www.bleepingcomputer.com/news/security/litellm-release-pipeline-hacked-to-distribute-info-stealer-malware/ |
| 域名／文件 | `litellm[.]dev/healthcheck`；`cook.pth`、`cook.py`、`sitecustomize.py` | LiteLLM 外带端点与植入文件 | 同上 |
| IP | `104.194.150.21`、`144.172.64.60`、`144.172.64.99`、`144.172.64.128`、`167.88.172.97` | Storm-0940／ARTEX | https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors |
| 域名 | `uztickets[.]com`（C&C）、`egyptanimals[.]com/animals/photoalbum`（投递） | UAC-0099 MATCHWOK | https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/ |
| IPv6 | `b479:2771:8df4:b5eb:d007:63b0[:]2838` | MythicRatatoskr Yggdrasil C&C | https://github.com/eset/malware-ioc/tree/master/mythicratatoskr |
| SHA-1 | `D5F9288DAEBF87AE4579945F8DC6CF235B093CFD`、`B69EF0E45B401440C0FDE22046775D0C57E87415`、`4E3E6577866E4CE2ED73CA089700AE04230E768F`、`69969EEB7E0A3D84C4E70193636FCF934C6AA388`、`01855153CA7A33AD5FF36451DE5612DFBA0DD2CA`、`E29AF83A07FB32EB47C28733A9382E766D53F704`、`028CA11F3F0D8396043AF7BF756231FC2F50F829`、`9085896989947C0919A660352F75F6B233FC645B`、`D7E6A5A46C6ED3510997E91B11E51BE0250FD2A2`、`8CEB5F8BCDF4995B7164996F1429D682613BB17B`、`131A371A1E4EE78EC3B2863607C99290EC3B58A6`、`09C816697C0C2AFF9B4FF58681558CA30D04C9CD` | MythicRatatoskr／SOCKS5 | 同上 |
| 域名 | `choclatey[.]org`、`community[.]choclatey[.]org`、`massgravel[.]net`、`workerstats[.]net`、`pymons[.]is`、`datamons[.]org`、`niceer[.]net`、`supertrap[.]net` | Armorsteal 诱饵／C2 | https://www.zscaler.com/blogs/security-research/seo-poisoning-campaign-delivers-new-armorsteal-malware |
| IP | `82.153.135[.]80`、`186.2.175[.]183`、`186.2.163[.]185`、`190.115.31[.]69`、`209.99.186[.]187`、`104.21.87[.]146`（Cloudflare，慎封） | Armorsteal 基础设施 | 同上 |
| SHA256 | `f3846ec2a6ff0a27d9ef2b9bf7908743b81d295ef29344acfb96ff83fff994f9`、`fb1181160e9f10ce1eb5e5dc9bc23e1498a39110ee9ea361fd150454cb01b292`、`3e3b62a9836697d978cbb620dc8af8f6eefdf8cb73fc30d16bb394d1c58f4c97`、`237ba698d7dc8936c43e0e78e7644002375e51e8baf9b3a7d4e18683f871ee31`、`be0329d0795dd62ae587faf97e704bb36413e5c98ddd8fe575f5077db3c84e5f`、`04d2828155ed2a276cfd3c97d4f966d328391dd818e04e773212cd601e49fa74`、`56f05c4fb1c25c04e0dde60e2e5e41ac164a6dc53688d0f9eb52a55f82106389`、`0ea99fbbe29af6f797e3866ed5f822c7a5d3e9cdb990a8c382a715069f156499`、`8fb7aaf2b9270b8b75f6844aaefd5242b4f926fb89cba10fff3d9b908a769788`、`5410c2f239c3649928383c4478dea182f90b21f5b258081fec07e9d297ae4b1c` | Armorsteal 各模块 | 同上 |
| 域名／IP | `mesh[.]buttruyen[.]com`、`62[.]60[.]131[.]43`、`Meshcentral[.]girydsfsggvb[.]com`、`62[.]60[.]135[.]64` | k0t（Forti／GlobalProtect） | https://x.com/LandscapeThreat/status/2113361051857076360 |
| IP | `130.94.20[.]71`、`141.11.32[.]132`、`2.27.248[.]209`、`67.207.95[.]101`（另 2 个见仓库） | SliverC2 | https://x.com/orlof_v/status/2113267309032698298 |
| SHA256 | `67c10a4f7db7fe55953b9b57492d4e6aa9cf0e20f492d193328def2662840c97`（经 `api.telegram(.)org`） | DEW_protected.exe | https://x.com/smica83/status/2113375121545236514 |
| SHA256／IP／域名 | `914adfba2837c786986bb16577f630e3355bb1984fc82e6d642657e790e6dbf8`；`104.143.42(.)209:22`；`wwppodd6688(.)com` | 柬埔寨「宴会邀请」rar | https://x.com/smica83/status/2113374095416905793 |
| SHA256／域名 | `b199422fe5f11a4c532f05fbca85446edd426c70fb4f330bb7f78e566f5bd66a`；`ababy9(.)com` | 柬埔寨电费 rar | https://x.com/smica83/status/2113351070315642931 |
| SHA256／域名／IP | `09af553a032ac6591b9f1271ade103549946640a82136dc2cee4b1da6a488552`；`smaluf(.)net:3857`；`77.220.212(.)113:2084` | Forecaster.msi | https://x.com/smica83/status/2113348751532118078 |
| SHA256／域名 | `e6eca876f1e4423eadde8298c879774118f094d0b714a9dd202883b50ddc02dc`；`helensolution[.]info` | 巴基斯坦 doc 诱饵 | https://x.com/smica83/status/2113350145672884651 |
| SHA256／URL／IP | `5f4bf788c53ba55b9ed13ac1d71e636ed6d378c7d04ff1bd9d2ec52015cf36df`；`hxxps://pixeldrain(.)com/api/file/LEfVj7fg?download`；`172.82.64[.]48` | Reader_en_install.iso | https://x.com/smica83/status/2113342928957415879 |
| SHA256 | `6930ec46d217c854d7e5731e5efad4757eeb344e28386742586a33f455d8b401` | Client_Matter_Document zip（韩国） | https://x.com/smica83/status/2113373037047246960 |
| IP／域名 | `104.194.141[.]56`、`sunmerksin[.]com`、`placewingarage[.]com`；`arvion[.]network` | malwrhunterteam 线索 | https://x.com/malwrhunterteam/status/2113378811026825565 |
| IP | `193.143.1[.]142`（AS198953 Proton66） | skocherhan 线索 | https://x.com/skocherhan/status/2113334198782288175 |
| 域名 | `privatestress.com`、`.icu`、`.pw`、`.ru`、`.st` | 500mk500 线索 | https://x.com/500mk500/status/2113331085819941375 |

未见公开 IoC 的条目：GitLab 110264、KSMBD、QPACK、BIND 94300、Cisco 76466、Langflow 105740、OpenCode、Node 111497、TimeSmuggler（窗口内帖文未附）、SiriusQT、Stadia、Danfoss 冷链、RatHat、Capcom、Railway、eMudhra。

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

**本日交叉情况**：
- **LWiS List**：10 段 `from:` 批次在窗口内共返回 165 条，粗筛 46 条。
- **活跃成员与对应条目**：
  - @Dinosn：Arista
  - @vxunderground：当日事件汇总
  - @pdiscoveryio：PHP 资产盘点
  - @i0n1c：BIND
  - @N3mes1s：Brotli commit
  - @_dirkjan：SMB 签名绕过
  - @offsectraining：PHP2Shell 实验
  - @garethheyes：Hackvertor
  - @KimZetter、@TwoSevenOneT：eMudhra
  - @LloydLabs：批评扫描数据口径
- **Risky Business**：RSS 最新一期仍是 **#856「8-bit encryption, PHP megabugs and more」**（10-21 01:43 UTC-3 发布，早于本窗口），本日没有新一期：https://risky.biz/
- **tl;dr sec**：tldrsec.com／feed 对本机返回 Cloudflare 质询页，**本日无法核对**是否有新一期：https://tldrsec.com/
- **blogs.txt 中的博客**：ESET WeLiveSecurity、Zscaler、Wiz、Talos、Unit 42、Huntress、Nextron、Sysdig 当日的相关文章已在上文交叉引用。

## 来源搜索 URL

- X 只读接口查询（下列为等价的 X 网页搜索 URL，便于人工复核；实际用接口 `search_posts_all` 执行）：
  - A 类：https://x.com/search?q=(CVE-2026%20OR%20CVE-2025)%20(exploit%20OR%20exploited%20OR%20PoC%20OR%20RCE%20OR%20patch%20OR%20advisory%20OR%20KEV%20OR%200day%20OR%20zero-day)%20-is%3Aretweet&f=live
  - B 类：https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20redteam%20OR%20BOF%20OR%20EDR%20OR%20implant%20OR%20nuclei)%20-is%3Aretweet&f=live
  - C 类：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)%20-is%3Aretweet&f=live
  - LWiS List：https://x.com/i/lists/1239330068461244424
  - 专题 Arista：https://x.com/search?q=CVE-2026-114625&f=live
  - 专题 PHP2Shell：https://x.com/search?q=php2shell%20(exploited%20OR%20Mirai%20OR%20honeypot%20OR%20IOC)&f=live
  - 专题 LiteLLM／Railway／Storm-0940：https://x.com/search?q=(LiteLLM%20OR%20Railway%20OR%20Storm-0940)%20-is%3Aretweet&f=live
  - 专题 BIND／QPACK／Langflow：https://x.com/search?q=(CVE-2026-94300%20OR%20QPACK%20OR%20Langflow)&f=live
- 公开备援：
  - CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - CISA KEV 页：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  - CISA 网络安全公告：https://www.cisa.gov/news-events/cybersecurity-advisories
  - NVD：https://nvd.nist.gov/vuln/search
  - Arista 公告：https://www.arista.com/en/support/advisories-notices/security-advisory/24838-security-advisory-0199
  - ISC BIND：https://kb.isc.org/docs/cve-2026-94300
  - Cisco 公告页：https://sec.cloudapps.cisco.com/security/center/publicationListing.x
  - LWiS blogs.txt：https://blog.badsectorlabs.com/files/blogs.txt
  - Risky Business：https://risky.biz/
  - tl;dr sec：https://tldrsec.com/
