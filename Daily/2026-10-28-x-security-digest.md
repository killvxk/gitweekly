# X 安全情报晚报 · 2026-10-28

> 搜集窗口：圣地亚哥时间 **2026-10-27 20:18 至 2026-10-28 20:15**（America/Santiago／UTC-3，接昨晚窗口）。X 搜索参数：`start_time=2026-10-27T23:18:00Z`，部分查询加 `end_time` 分段补早时段。实际抓到的帖子从 **10-27 20:22** 到 **10-28 20:12**（UTC-3），**实际有效覆盖约 23 小时 50 分**。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口。`search_posts_all` 用 recency 和 relevancy 两种排序，每次最多返回 25 条；`user-X` 的 `get_lists_posts` 读 LWiS List；`get_posts_by_ids` 读重点原帖全文和展开后的链接。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** t.co 短链按接口返回的 `expanded_url`／`unwound_url` 展开，纯图片／视频链接不列。环境里没有可加载的 x-api-mcp-guide Skill，所以接口参数是用 GetDynamicTools 查 schema 后确定的。
> 本轮查询：
> - A 类（CVE／0day／PoC／exploit）：Latest 一次、`CVE-2026` relevancy 及 `end_time` 分段补查、在野利用／补丁 relevancy、高信号账号专查
> - B 类（GitHub＋C2／red team／nuclei／工具发布）：Latest 一次（几乎全是噪声）、relevancy 一次、`url:github.com`＋安全关键词 relevancy 一次
> - C 类（malware analysis／threat report／threat actor／campaign／IoC）：Latest 一次、relevancy 及分段补查、IoC relevancy
> - LWiS List（1239330068461244424）：三页，最早一条早于窗口起点，能盖住整个窗口
> - 原帖全文与链接展开：`get_posts_by_ids` 一次（100 个 ID）
>
> 合计 **20 次有效 X 读取，0 次 429**（当日配额剩约 980/1000）。原始返回 764 条，去重后 633 条，其中窗口内 **589** 条（与 seen_ids 8976 条重叠 0；窗口外的 44 条 List 旧帖不计入），排除纯转推后 509 条，关键词粗筛后约 **328** 条安全相关帖，下文引用约 100 条。已剔除：广告和营销（Booz Allen Vellox Reverser 推广、安全评估推销帖）、Grok 自动回复、黑客松作品刷屏、体育／政治／加密货币刷屏。**全程只读，没有发帖、回复、点赞、转推、收藏或关注。**
> **公开备援**（`/workspace/x1028/pages/`，curl 核对）：CISA KEV JSON（catalogVersion **2026.10.28／1762／Δ+2**）；Dream Research（PHP2Shell＋Fragnesia）；SecurityWeek（PHP2Shell 防火墙、Oracle EBS 探测）；THN（PHP2Shell、Volt Typhoon、Virtualine）；Lumen Black Lotus Labs（Silent Train）；HOL（ESXi CVE-2026-41709）；BleepingComputer（So-net）；The Register（Cisco 开源工具）；ThreatDown（LodaRAT）；Sansec（deepveindrilling）。
> **CISA KEV：catalogVersion 2026.10.28／1762 条，Δ+2**（相对昨晚 2026.10.27／1760）。`dateReleased` 为 2026-10-28 16:00 UTC-3。
> - **今日新增**：**CVE-2026-46300**（Linux Kernel 变量未初始化，即「Fragnesia」本地提权，**due 10-31**，联邦期限只有 3 天）；**CVE-2026-41709**（Broadcom VMware ESX 日志记录不足，**due 11-11**）。
> - **10-29（明天）到期**：PHP **CVE-2026-109618／109619**（PHP2Shell）。
> - **11-03 到期**：Plex 96652、Plex 96655、Siemens 110936。
> - **11-10 到期**：Adobe Commerce／Magento 48356、Brotli 111497。
> - **逾期（续）**：
>   - 10-26 到期：Arista VeloCloud Orchestrator 114625、Collabora Online 110447
>   - 10-23 到期：SiteGuard 106931、Plex 96656、Plex 96654
>   - 10-19 到期：BeyondTrust 102764、Fortinet CVE-2025-61624
>   - 10-18 到期：Atlassian 21589
>   - 10-17 到期：AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322
>   - 10-16 到期：Ivanti 104935、Windows Shell MOTW 96951
>   - 10-13 到期：Apple 86950
>   - 10-11 到期：CVE-2015-5477、CVE-2016-3081、CVE-2023-22894、CVE-2021-3199、CVE-2015-3306
> - **还没进 KEV，但今天要优先处理**：Oracle EBS **CVE-2026-101767**（开始被探测）、Oracle PeopleSoft **CVE-2026-35273**（三洞串联）、Veeam B&R **CVE-2026-108142**（CVSS 9.1）、WatchGuard Fireware **CVE-2026-112709／112710**、GFI KerioConnect **CVE-2026-112353**（报在野）、gotenberg **CVE-2026-40281**（VulnCheck 见在野）、FortiMail **CVE-2026-104286**、VMware SDDC Manager 9.1.1 node.js RCE（补丁待发）。

## 今日摘要

- **KEV 新增两条**：Linux 内核「Fragnesia」**CVE-2026-46300**（due 10-31）和 VMware ESX 日志绕过 **CVE-2026-41709**（due 11-11）。前者正是 PHP2Shell 实战链里用来拿 root 的提权洞；后者据 HOL 转述被中国关联的 WARP PANDA 当零日用来让命令不进日志。CISA 原帖：https://x.com/CISACyber/status/2115529867412292016
- **PHP2Shell 首次完整实战链曝光**：Dream Research 称疑似中国关联的攻击者把 PHP2Shell（109618／109619）和 Fragnesia 串起来，10-23～24 拿下美、日、台、韩 24 台防火墙和 1 台内部管理服务器，并在一个美国政府关联环境里做 AD 枚举、提取凭据；厂商和版本未公开。KEV 联邦期限 **明天 10-29**。https://x.com/InfraWatchHQ/status/2115281115011277199
- **Volt Typhoon「Silent Train」**：Lumen Black Lotus Labs 披露其多跳中继框架，关联 4 起确认的零日行动（Versa Director、N-able N-central、Cisco Catalyst SD-WAN、Arista VCO），专打端点管理和 SD-WAN 控制面。https://x.com/TheHackersNews/status/2115506858517815431
- **Oracle 两线**：PeopleSoft **CVE-2026-35273** 被证实是 SSRF 起头的三个缺陷串联，ShinyHunters 自 5 月起利用；EBS **CVE-2026-101767**（CVSS 9.8 SQL 注入）已被 Defused 诱捕系统看到探测。https://x.com/TheHackersNews/status/2115324357270729105
- **Node2Shell／Brotli 111497 在野流量**：有传感器记录到针对 Node.js 24.22.0 的真实攻击流量，红队也反映生产环境大量未修；升级 Node 22.23.4／24.22.1／26.12.1、brotli 1.2.1。https://x.com/jorgeliauw/status/2115528035189285334
- **补丁大潮**：Chrome 156（52 个修复，4 个 Critical）、Veeam B&R 13.x（108142 授权绕过 9.1）、WatchGuard Fireware（18 个公告，7 个 Critical）、TeamViewer 15.83、Yamaha NWR100（9.8）。https://x.com/vulnipulse/status/2115282020113002817
- **执法行动**：美国 DOJ 联合私营伙伴拿下防弹主机 Virtualine（AS202412 Omegatech），abuse.ch 统计其上 1 万多个恶意分发站点。https://x.com/abuse_ch/status/2115350081603854801
- **恶意软件**：Group-IB 披露印度 Android 金融欺诈集群 CyberDakait（7 个家族、约 1.8 万设备、760 万条短信）；Kaspersky 的 Lazarus FlashHole 用 ML-KEM-1024 加密 C2；INJ3CTOR3 的 FreePBX 植入物改成每分钟外传凭据。https://x.com/GroupIB_TI/status/2115366036308476197
- **事件与泄露**：日本 GMO「お名前.com デスクトップクラウド」被入侵并遭勒索威胁（悬赏 100 万美元）；Sony 旗下 So-net 约 258 万条会员数据外泄；123 Reg 披露疑似中国关联的「AI 网络攻击」；摩尔多瓦约 75 万个 IDNP 外泄。https://x.com/BleepinComputer/status/2115485248775504339

## CVE / POC / 漏洞

### 1. CISA KEV 新增：Linux「Fragnesia」CVE-2026-46300 与 VMware ESX CVE-2026-41709

- **CVE-2026-46300**（Linux Kernel，Missing Initialization of a Variable，CVSS 7.8）：本地提权，cve.now 摘要称问题在核心网络 sk_buff 处理（TCP 接收合并路径）；Dream 的报告把它描述为 XFRM ESP-in-TCP 相关、可改写页缓存的提权洞。修复版本见各发行版（cve.now 列出 5.10.257、5.15.208 等稳定分支）。**联邦期限 10-31**，比常规短得多。
- **CVE-2026-41709**（Broadcom VMware ESX，Insufficient Logging，CVSS 仅 2.7）：攻击者在 ESXi 上执行的命令可以不进本地日志。HOL 转述称中国关联的 WARP PANDA 把它当零日用。修复：ESXi 8.0 U3j（25429389）、9.0.2.0100（25595025）、9.1.0.0（25370933）、VCF 5.2.4，**没有缓解措施**。CVSS 低但进 KEV，说明它是真实入侵链中「反取证」一环。
- 防守动作：给暴露 PHP 的 Linux 设备／服务器同时排期内核更新；ESXi 打补丁后把日志转发到主机外的 syslog／SIEM，并对窗口期内的 ESXi 主机做离机日志对比。
- 地址：
  - X 原帖：https://x.com/CISACyber/status/2115529867412292016
  - X 原帖：https://x.com/CipherSecurityN/status/2115529528521150590
  - X 原帖：https://x.com/HashgraphOnline/status/2115541625619578957
  - X 原帖：https://x.com/cvedotnow/status/2115523137848643627
  - X 原帖：https://x.com/cvedotnow/status/2115523141732642965
  - 厂商公告（CISA KEV）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  - 厂商公告（Broadcom）：https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
  - 文章：https://hol.org/blog/cve-2026-41709-vmware-esxi-logging-bypass-cisa-kev
  - 文章：https://cve.now/CVE-2026-41709
  - 文章：https://cve.now/CVE-2026-46300
  - 文章：https://pwn.watch/i/linux-fragnesia-lpe-cve-2026-46300-cisa-kev

### 2. PHP2Shell（CVE-2026-109618／109619）＋ Fragnesia：25 台服务器被拿 root，波及美国政府关联环境（KEV 明天 10-29 到期）

- **谁**：Dream Research 判断为疑似中国关联的行动者，带 AI 辅助痕迹（攻击机装有 Claude Code、配置了 DeepSeek／Kimi 的 aiscan 平台、FOFA API 密钥，约 40 个脚本风格高度一致）；Dream 也强调这**不是**全自动的国家级攻击。
- **打什么**：某大厂防火墙的 appweb 管理界面（该防火墙 OS 内置 PHP 8.0.30）。攻击者用 FOFA 找到约 1.9 万个暴露的管理界面，筛到美、日、台、韩约 240 个目标，10-23～24 成功拿下 24 台防火墙和 1 台内部管理服务器，随后在美国政府关联环境里提取 LDAP 服务账号凭据、枚举 AD。利用代码为非公开定制版，**通用 PHP2Shell 签名可能不触发**。厂商与受影响版本未公开，厂商已获通报。
- **补丁与狩猎**：PHP 8.5.12／8.4.27／8.3.36／8.2.35（8.1 及更早无官方修复），升级后重启 PHP-FPM／Web 服务；Palo Alto 已把自家 PAN-OS 管理界面相关公告升为 Critical 并陆续发 hotfix。管理界面不要暴露到公网；排查管理面 Web 目录里的未知 PHP 文件、`/etc/pam.d/` 下文件被改、异常的 `su` 成功记录、来自防火墙的 LDAP 绑定和 AD 枚举。
- 旁证：Cloudflare 办了 PHP2SHELL CTF（LiveOverflow 在打）；runZero 提醒不要乱用未经验证的检测脚本和 PoC。
- 地址：
  - X 原帖：https://x.com/InfraWatchHQ/status/2115281115011277199
  - X 原帖：https://x.com/CipherSecurityN/status/2115427640869839001
  - X 原帖：https://x.com/TheHackersNews/status/2115475223931982303
  - X 原帖：https://x.com/DFIR_Radar/status/2115550199238324401
  - X 原帖：https://x.com/nurhayatdev/status/2115554731510636736
  - X 原帖：https://x.com/h_a_t_a_r_a_k_e/status/2115448863851233320
  - X 原帖：https://x.com/LiveOverflow/status/2115335665671925821
  - X 原帖：https://x.com/runZeroInc/status/2115444534137987566
  - 厂商公告（Palo Alto）：https://security.paloaltonetworks.com/CVE-2026-109618
  - 厂商公告（CISA）：https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching
  - 厂商公告（JVN）：https://jvn.jp/vu/JVNVU99905564/
  - 文章：https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers
  - 文章：https://www.securityweek.com/china-linked-hackers-exploit-php2shell-to-root-firewalls/
  - 文章：https://thehackernews.com/2026/10/php2shell-attack-roots-25-servers.html
  - 文章：https://php-rce.cloudflare.app/

### 3. Node2Shell／Brotli2Shell（CVE-2026-111497，KEV due 11-10）：在野流量与生产环境残留

- 有传感器记录到针对 Node.js 24.22.0（x86-64）的真实攻击流量（来源 IP 见 IoC 小节）。红队 S1r1u5_ 称客户环境里大量未修，而且这类问题在应用层，常规监控抓不到。FelipeDaragon 提醒：PHP 的 Windows 构建也打包了 Brotli，一台 PHP 可能同时受 PHP2Shell 和 Brotli2Shell 影响。
- 补丁：Node.js 22.23.4／24.22.1／26.12.1（20.x 已 EOL 不修），google/brotli 1.2.1；临时措施可在 WAF／反代丢弃入站 `Content-Encoding: br`。
- 地址：
  - X 原帖：https://x.com/jorgeliauw/status/2115528035189285334
  - X 原帖：https://x.com/S1r1u5_/status/2115532048886853672
  - X 原帖：https://x.com/FelipeDaragon/status/2115426192614408222
  - X 原帖：https://x.com/szchan111/status/2115264187102584972
  - 厂商公告（Node.js）：https://nodejs.org/en/blog/vulnerability/october-2026-security-releases
  - GitHub 发布：https://github.com/google/brotli/releases/tag/v1.2.1
  - 厂商公告（JVN）：https://jvn.jp/vu/JVNVU97400824/
  - 文章：https://cybersecuritynews.com/node2shell-vulnerability/

### 4. Oracle：PeopleSoft CVE-2026-35273 是三洞串联；EBS CVE-2026-101767 开始被探测

- **PeopleSoft 35273**：新的技术分析显示，ShinyHunters 自 5 月起利用的「零日」其实是三个缺陷（SSRF 绕过内部访问控制 → 未认证 RCE），Oracle 用一个 CVE 一并修复。确认 PeopleTools 已打 10 月 CPU，并排查 PeopleSoft 服务器上的异常文件写入和对回环地址的内部请求。
- **EBS 101767**（CVSS 9.8，未认证 SQL 注入可致 RCE）：上周 10 月 CPU 已修，Defused 诱捕系统已见探测。尚未进 KEV。
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2115324357270729105
  - X 原帖：https://x.com/SecurityWeek/status/2115508143157342348
  - X 原帖：https://x.com/ksg93rd/status/2115283792252276934
  - 文章：https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html
  - 文章：https://www.zerodayinitiative.com/blog/2026/10/20/cve-2026-35273-ssrf-to-rce-in-oracle-peoplesoft
  - 文章：https://www.securityweek.com/hackers-start-probing-fresh-oracle-ebs-vulnerability/

### 5. Google Chrome 156：52 个修复，4 个 Critical

- 修复版：Windows／Mac 156.0.8078.73/.74，Linux 156.0.8078.73。Critical：**CVE-2026-118306**（FileSystem 内存破坏）、**118331**（FileAPI 输入校验）、**118348**（Skia 输入校验）、**118344**（Layout UAF）。目前没有在野利用的说法。
- 地址：
  - X 原帖：https://x.com/SecureAnago_JP/status/2115226889476608273
  - X 原帖：https://x.com/WorldCyberNewsX/status/2115322677271367880
  - X 原帖：https://x.com/kasegerumatome/status/2115373044940292472
  - 厂商公告（Google）：https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html

### 6. Veeam：B&R CVE-2026-108142（CVSS 9.1）等五个漏洞；VBM365 KB4957

- **108142**：未认证攻击者可绕过 CDP Coordinator Service 授权。另有 105477（Veeam Agent for Linux 本地提权 7.3）、108140／108141（路径穿越任意写 5.9）、107671（Veeam ONE 管理员绕过 MFA 8.5）。受影响 B&R 13.0／13.1，12.x 不受这几项影响。
- 升级：B&R 13.1.2（13.1.2.57）／13.0.3（13.0.3.63）、Agent for Linux 13.1.2.11、Veeam ONE 13.1 P1（13.1.0.7940）。Veeam Backup for Microsoft 365 8.6 另修 106076／106077／106078／CVE-2025-64394。备份系统一直是勒索团伙首要目标，建议优先。
- 地址：
  - X 原帖：https://x.com/DarkWebInformer/status/2115235714581299404
  - X 原帖：https://x.com/CERTpy/status/2115440097248067613
  - X 原帖：https://x.com/autumn_good_35/status/2115486218842726886
  - 厂商公告（Veeam）：https://www.veeam.com/kb4957
  - 厂商公告（CERT-PY）：https://www.cert.gov.py/vulnerabilidades-en-productos-veeam-7/

### 7. WatchGuard Fireware OS：18 个公告，7 个 Critical（CVSS 9.1–9.5）

- 含 AD 认证服务的认证前 RCE（**CVE-2026-112709／112710**）、SIP 代理（**93857**）、WireGuard 配置（**103594**）。防火墙边界设备，建议今晚排期。
- 地址：
  - X 原帖：https://x.com/vulnipulse/status/2115282020113002817
  - 文章：https://vulnipulse.com/vendors/watchguard

### 8. VMware SDDC Manager 9.1.1：node.js 组件 RCE（9.8），补丁待发

- VMware 安全响应称有临时缓解方案、正式补丁尚未发布。SDDC Manager 是 VCF 的管理平面，建议先限制网络可达性并执行官方缓解。
- 地址：
  - X 原帖：https://x.com/PyroTek3/status/2115466373027725772
  - X 原帖（VMware 原帖）：https://twitter.com/VMwareSRC/status/2115297170773655895

### 9. 远程访问与通信软件：TeamViewer 15.83、Telegram rlottie CVE-2026-111105

- **TeamViewer**：**CVE-2026-92372／111585／92374**（最高 CVSS 8.8，提权与代码执行），升级到 15.83（公告 TV-2026-1011）。
- **Telegram CVE-2026-111105**（CVSS 7.0，ZDI 零日公告）：rlottie 动画库越界写。ZDI 最终公告写明需要用户交互，不是「零点击贴纸」；Telegram 称服务器端贴纸校验可缓解，客户端修复版本未公布，也没有在野报告。
- 地址：
  - X 原帖：https://x.com/CCBalert/status/2115432672407269858
  - X 原帖：https://x.com/Daily_CyberSec/status/2115343636736970834
  - X 原帖：https://x.com/DarkWebInformer/status/2115494600018444753
  - 厂商公告（TeamViewer）：https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2026-1011/
  - 文章：https://securityonline.info/teamviewer-vulnerabilities-patched-tv-2026-1011/

### 10. 已报在野、尚未进 KEV：GFI KerioConnect 112353、gotenberg 40281、FortiMail 104286

- **GFI KerioConnect Webmail CVE-2026-112353**：存储型 XSS，打开恶意 SVG 附件即可窃取凭据、会话令牌和邮箱数据，Alan Turing Institute 观测台称已在野利用。
- **gotenberg CVE-2026-40281**：VulnCheck 金丝雀观测到真实利用。
- **FortiMail CVE-2026-104286**：未认证路径穿越任意写，报道称作为零日被利用（只见二手转述，请以 Fortinet PSIRT 为准）。
- 地址：
  - X 原帖：https://x.com/TuringCyberObs/status/2115475371759939755
  - X 原帖：https://x.com/Python_s_/status/2115233652971827492
  - X 原帖：https://x.com/aimicyber/status/2115331814013190597
  - 文章（GitHub 报告）：https://github.com/alan-turing-institute/cyber-threat-observatory/blob/main/reports/2026-10-27/TIER_2_CVE-2026-112353.md
  - 文章：https://vulncheck.com/xdb/22443535b87c

### 11. 日本与网络设备：Yamaha NWR100 CVE-2026-97854（9.8）、BeyondTrust 102764 续

- **Yamaha NWR100**：未认证 OS 命令注入 **97854**（v3.1 9.8／v4 9.3）和配置导出文件未认证读取 **109822**（6.5），Rev.26.00.07 及更早受影响，**Rev.26.00.08** 修复；默认 WAN 侧不开 Web GUI，但做了端口开放或从无线侧仍可被打。
- **BeyondTrust RS CVE-2026-102764**（KEV 已逾期）：Google 称 Armory Castle（原 UNC5221）自 8 月起利用，打完补丁还要回溯补丁前的入侵痕迹。
- 地址：
  - X 原帖：https://x.com/h_a_t_a_r_a_k_e/status/2115448863851233320
  - X 原帖：https://x.com/snypet86/status/2115237547848634385
  - 厂商公告（Yamaha）：https://www.rtpro.yamaha.co.jp/RT/FAQ/Security/JVNVU91027179.html
  - 厂商公告（JVN）：https://jvn.jp/vu/JVNVU91027179/
  - 文章：https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust/

### 12. 其他漏洞信号

- **Microsoft Edge 沙箱纯逻辑洞逃逸**：Orange Tsai 在 Pwn2Own 2026 拿到 17.5 万美元的链公开了技术细节（无内存破坏）。https://x.com/TheHackersNews/status/2115480048002326811 ／ https://thehackernews.com/2026/10/researcher-reveals-how-logic-bugs-alone.html
- **AI 自动串联漏洞**：报道称 Anthropic 未发布模型自主把 Chrome／Safari／Windows／Linux 的零日串成可用利用，其中提到 Linux 内核 CVE-2026-98432（9.8）。https://thehackernews.com/2026/10/anthropics-unreleased-ai-model-chains.html ／ https://x.com/aviatrixtrc/status/2115488220234268708
- **Adobe Campaign Classic**：8 个 Critical（代码执行、安全绕过）。https://x.com/Dinosn/status/2115419939876294979 ／ https://thehackernews.com/2026/10/adobe-fixes-8-critical-campaign-classic.html
- **Roundcube CVE-2026-113386**：修复版 1.6.20／1.7.5（cPanel 版同步）。https://x.com/georgetasioulis/status/2115362763367170202 ／ https://www.cve.org/CVERecord?id=CVE-2026-113386
- **Linux 内核研究**：V4bel「Infinity Core」公开 6 个内核核心子系统 LPE／容器逃逸（98260、98256、89754、80775、98385、97941）；a13xp0p0v 发布 CVE-2026-31695 演讲幻灯片。https://x.com/ksg93rd/status/2115445009222676708 ／ https://github.com/V4bel/InfinityCore ／ https://x.com/a13xp0p0v/status/2115349271251734945 ／ https://a13xp0p0v.tech/img/Alexander_Popov-Dangerous_Device.pdf
- **Microsoft Word 私有 RCE 链在 BreachForums 叫卖**（卖家 xynapse，自称绕过 MOTW／受保护视图，**未经证实**）。https://x.com/TheThreatWire/status/2115439922815631846
- **可疑 PoC 警示**：有人指出一个自称 Splunk CVE-2026-76268 的 GitHub PoC 实为通用 Patroni 脚本改写，大概率无效（仓库地址见 IoC 小节，已 defang，不建议运行）。https://x.com/papa_anniekey/status/2115389263957434436
- **边界设备持续告警**：NetScaler 88771／88772、Ivanti、Check Point 零日仍在被利用（threadlinqs 汇总）；Arista VCO 114625 提醒继续发酵；Supermicro BMC CVE-2026-16521（7.2）。https://x.com/threadlinqs/status/2115455629317833204 ／ https://x.com/starswarm/status/2115428373535088767 ／ https://x.com/yogsec/status/2115256616811704568
- **Apple 86950（KEV 已逾期）**：iOS／iPadOS 18.7.11 向旧机型回移 CoreGraphics 在野零日补丁。https://x.com/ByteCheck101/status/2115389397428564022 ／ https://f1tym1.com/2026/10/28/apple-backports-fix-for-exploited-coregraphics-zero-day-cve-2026-86950-to-older-iphones/
- **XLibre X Server 25.1.10**：修复 CVE-2026-50256～50263。https://x.com/r1w1s1/status/2115272848138711056 ／ https://github.com/X11Libre/xserver/releases/tag/xlibre-xserver-25.1.10
- **InfraTrust 报告**：关键网络基础设施被利用漏洞汇总。https://www.bleepingcomputer.com/news/security/infratrust-report-warns-of-exploited-flaws-in-critical-network-infrastructure/

## 工具与 GitHub 发布

### 1. ac0d3r/machbox v0.2.0：一次性 macOS 虚拟机自动化

- v0.2.0 重写为通用的可丢弃 macOS VM 自动化工作流，样本分析部分移到独立插件，适合在隔离环境里分析可疑 Mach-O 样本。
- 地址：
  - X 原帖：https://x.com/ac0d3r/status/2115398059169648696
  - GitHub 仓库：https://github.com/ac0d3r/machbox
  - GitHub 仓库：https://github.com/ac0d3r/machbox-malware

### 2. Cisco 开源 AI agent 恶意行为检测工具

- 看 agent 动作之间的关系（如读配置文件＋向外部端点发请求组合成外泄），而非单个动作；适合已部署 MCP／agent 的团队评估。
- 地址：
  - X 原帖：https://x.com/Dinosn/status/2115419505161543714
  - 文章：https://www.theregister.com/security/2026/10/28/cisco-open-sources-tool-for-detecting-ai-agents-on-hacking-sprees/5305867

### 3. ProjectDiscovery Neo「Vulnerability Triage」全面开放

- 地址：
  - X 原帖：https://x.com/pdiscoveryio/status/2115427991597752628
  - 文章：https://projectdiscovery.io/blog/introducing-neo-triage

### 4. 检测工程：Elastic 新增 161 条预置规则；ClickFix msiexec 混淆提醒

- Elastic 预置规则一次更新 161 条；Wietze 提醒 ClickFix 样本靠参数混淆躲 msiexec 检测，建议用 ArgFuscator 的 msiexec 变体表核对规则（配合 ThreatHunter.ai 的 Azure30 木马化 MSI 报告）。
- 地址：
  - X 原帖：https://x.com/SBousseaden/status/2115490972310323540
  - X 原帖：https://x.com/Wietze/status/2115476995123417311
  - 文章：https://argfuscator.net/executables/windows/msiexec.html
  - 文章：https://www.threathunter.ai/blog/azure30-nodejs-backdoor-trojanized-msi-clickfix/

### 5. 红队基础设施、逆向与 AI 安全工具（GitHub）

- **m19o/NightAgents**：监控和保护红队基础设施。X 原帖：https://x.com/m19o__/status/2115521153150194095 ／ GitHub 仓库：https://github.com/m19o/NightAgents
- **lupingQAQ/inkblade**：面向 LLM 训练／推理集群的渗透框架（十层攻击面），可当 AI 集群加固检查表。X 原帖：https://x.com/lupingQAQ/status/2115333931533050276 ／ GitHub 仓库：https://github.com/lupingQAQ/inkblade
- **ExpOrx/IDAChef**：嵌入 IDA Pro 9.x 的 CyberChef 式工具箱。X 原帖：https://x.com/blackstormsecbr/status/2115544561997205776 ／ GitHub 仓库：https://github.com/ExpOrx/IDAChef
- **NVIDIA/SkillSpector**：agent skills 安全扫描。X 原帖：https://x.com/Zk3r0x/status/2115282559886348487 ／ GitHub 仓库：https://github.com/NVIDIA/SkillSpector
- **gongchengcheng/Decepticon**：AI 驱动的授权渗透测试环境。X 原帖：https://x.com/HackingTeam77/status/2115322578432635273 ／ GitHub 仓库：https://github.com/gongchengcheng/Decepticon
- **ipreetgs/aegis**：本地索引公开 CVE 情报并映射暴露面。GitHub 仓库：https://github.com/ipreetgs/aegis

### 6. 研究文与演讲

- **chompie1337**：确定性步骤＋AI 混合流水线做 Windows 内核 N-day 研究（演讲视频）。X 原帖：https://x.com/chompie1337/status/2115576088747561222
- **Mitiga**：在野 Entra 条件访问／CAE 绕过狩猎；kmkz 实测令牌重放时 CAE 未告警。X 原帖：https://x.com/kmkz_security/status/2115396225142866344 ／ 文章：https://www.mitiga.io/blog/hunting-conditional-access-policy-bypass-in-the-wild
- **Microsoft 365 Copilot 数据存放在 Exchange 邮箱隐藏文件夹**：邮箱完全访问权即可拿到提示历史，也意味着保留策略和 eDiscovery 适用。X 原帖：https://x.com/PyroTek3/status/2115520723267604986
- **AWS MCP Python 沙箱研究**。文章：https://xplo1t-sec.github.io/posts/breaking-the-aws-mcp-python-sandbox/
- **Kerberos 无协议转换约束委派（无 SPN 账户）**。文章：https://hunio.org/security/abusing-constrained-delegation-without-protocol-transition-against-spn-less-accounts/

## APT / Malware 分析

### 1. Volt Typhoon「Silent Train」：多跳中继框架与多起零日行动（Lumen Black Lotus Labs）

- **打什么**：端点管理、网络管理、带外管理和 SD-WAN 控制面；关联 Versa Director CVE-2024-39717、N-able N-central CVE-2025-8875／8876、Cisco Catalyst SD-WAN CVE-2026-20127、Arista VeloCloud CVE-2026-16812，另有疑似 Quest KACE 零日（30 多个受害者）；能源、水务、航空、铁路受影响。
- **怎么藏**：境外 VPS → 境外被控 SOHO／IoT → 美国境内被控设备出口，绕过地理围栏和 IP 信誉；平均会话约 4 小时，结束后清理 SSH 密钥、临时服务和配置。
- **狩猎**：管理平台／SD-WAN 编排器来自住宅或小型办公 IP 的管理登录、短时间新增又删除的 SSH 密钥与服务。
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2115506858517815431
  - X 原帖：https://x.com/DFIR_Radar/status/2115519945542979787
  - X 原帖：https://x.com/KimZetter/status/2115477415338160562
  - X 原帖：https://x.com/SwitHak/status/2115490931881263369
  - 厂商报告（Lumen）：https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework
  - 文章：https://thehackernews.com/2026/10/volt-typhoon-used-covert-silent-train.html
  - 文章：https://www.zetter-zeroday.com/silent-train-volt-typhoons-sophisticated-infection-chain-into-us-targets-exposed/

### 2. CyberDakait：针对印度银行客户的 Android 欺诈集群（Group-IB）

- 自 2025-07 起冒充 11 家印度银行和 2 个政府项目，诱导安装托管在 GitHub 的 APK；7 个家族（cyb3rx、appkjl、godz、d-passive、d-shine、GhostBat/GhostGrab、tenxen）共享短信拦截、呼叫转移、覆盖层窃卡能力，C2 走 Telegram bot／Firebase／HTTP；约 1.8 万设备、760 万条短信被拦截。
- 地址：
  - X 原帖：https://x.com/GroupIB_TI/status/2115366036308476197
  - X 原帖：https://x.com/DFIR_Radar/status/2115383840898232373
  - 厂商报告（Group-IB）：https://link.group-ib.com/4zYErEw

### 3. Lazarus Operation FlashHole：ML-KEM-1024 加密 C2（Kaspersky，续）

- 针对韩国建筑、软件、通信设备行业，滥用 INISAFE CrossWeb EX，DLL 侧载投放 TechHub、ClientHub、LPEClient，部分阶段只在内存运行，C2 用后量子 ML-KEM-1024 加密。
- 地址：
  - X 原帖：https://x.com/ZeroDayFacts/status/2115288838868476323

### 4. INJ3CTOR3 FreePBX 植入物：每分钟外传凭据

- 新版植入物由 cron 每分钟把 FreePBX／Issabel／Elastix 的 SIP、AMI、数据库、SMTP 中继配置传到暂存主机；运营者已更换 webshell 门禁哈希和主机水印，按 5 月报告做的狩猎会漏报，还会制造访问日志空洞。处置顺序：先彻底清除，再轮换 SIP trunk 等凭据，否则新凭据几分钟内又被偷走。
- 地址：
  - X 原帖：https://x.com/DFIR_Radar/status/2115338669598855584

### 5. Virtualine（AS202412 Omegatech）防弹主机被执法拿下

- DOJ 联合私营伙伴查封域名，上游运营商断开连接；abuse.ch 统计 URLhaus 上 1 万多个恶意分发站点、ThreatFox 2,000 多条 IoC，主要承载 PureRAT、OverlordRAT、恶意 ScreenConnect、ClickFix／ErrTraffic。可把 AS202412 历史网段继续纳入封锁和回溯狩猎。
- 地址：
  - X 原帖：https://x.com/abuse_ch/status/2115350081603854801
  - 厂商公告（DOJ）：https://www.justice.gov/usao-edva/pr/bulletproof-website-domain-seized-international-law-enforcement-operation
  - 文章：https://thehackernews.com/2026/10/fbi-seizes-virtualine-domain-over.html
  - 文章：https://urlhaus.abuse.ch/asn/202412
  - 文章：https://threatfox.abuse.ch/asn/202412/

### 6. macOS：ICMacOS RAT 地下出租；__c5cfg 样本分析；AMOS 持续活跃

- **ICMacOS**：GlowComa（MADHASH 加密货币盗取团伙）在俄语论坛推广，从窃密器演变为带远控能力的 RAT，用 ClickFix 式诱导和假系统密码框窃取登录密码。X 原帖：https://x.com/rst_cloud/status/2115415037909107196 ／ 文章：https://cybersecuritynews.com/icmacos-remote-access-trojan/
- **__c5cfg**：自定义 Mach-O 区段、直接系统调用、疑似内存加载模块的 macOS 样本逆向。X 原帖：https://x.com/c_kant_/status/2115227496534917133 ／ 文章：https://lynk4.github.io/mare/c5-enigma/index.html
- **AMOS** 等样本哈希见 IoC 小节（EmunaEliran 每日清单）。

### 7. 钓鱼与投递

- **LodaRAT 假法院 ADR 钓鱼**（ThreatDown）：冒充美国联邦法院向 10 万多家公司发邮件，加密 ZIP 层层投放 AutoIt 版 LodaRAT。X 原帖：https://x.com/rst_cloud/status/2115392287190487133 ／ 文章：https://www.threatdown.com/blog/fake-court-adr-phishing-lodarat/
- **Cofense：假招标＋受保护文档**钓微软凭据。X 原帖：https://x.com/rst_cloud/status/2115407448315924706 ／ 文章：https://cofense.com/blog/locked-and-loaded-phishing-through-fake-bids-and-protected-documents
- **Kong RAT**：中国背景行动者 SEO 投毒假冒 DeepSeek 下载。X 原帖：https://x.com/Dinosn/status/2115461613914562851 ／ 文章：https://hybrid-analysis.blogspot.com/2026/10/seo-poisoning-campaign-targets-deepseek.html
- **libcef.dll 侧载＋PNG 藏载荷**：马来西亚企业收到 ISO 格式「发票」，检出率低。X 原帖：https://x.com/vxunderground/status/2115247383852318793
- **哥伦比亚税务主题 VBS 下载器**（哈希见 IoC）。X 原帖：https://x.com/DFIR_hanan96/status/2115263434304757838

### 8. AI 相关威胁

- **暴露的 AI 渗透测试面板被反向接管**（Norforge）：两个集群 AIA0009／AIA0010 向暴露的 Cairn 面板塞任务，让 agent 植入 SSH 密钥、运行恶意软件、外泄配置。X 原帖：https://x.com/rst_cloud/status/2115437794344460760 ／ 文章：https://norforge.com/blog/automated-subversion-attempted-takeover
- **冒充 OpenAI／Anthropic／Meta 爬虫扫描凭据**。X 原帖：https://x.com/jbhall56/status/2115473467600519576 ／ 文章：https://www.darkreading.com/cyber-risk/attacker-impersonates-ai-bots-scans-credentials
- **Storm-0940 ARTEX／ConnectWise 供应链**（微软 10-21 文，今日被重提）。X 原帖：https://x.com/TheElderHacker/status/2115451721908678951 ／ 厂商公告（Microsoft）：https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/

### 9. 电商侧录：Sansec deepveindrilling loader（续）

- Sansec 称该域名是攻击 Magento 店铺团伙的最新 loader 地址；malwrhunterteam 在一个与 CMS 无关的可疑样本里也见到该域名，说明基础设施可能被多用途复用。X 原帖：https://x.com/malwrhunterteam/status/2115526020560249143 ／ 文章：https://sansec.io/research/magento-cms-block-loader-deepveindrilling

### 10. 勒索、入侵与数据泄露

- **GMO「お名前.com デスクトップクラウド」**：攻击者入侵后威胁引爆勒索，GMO 让客户关机并悬赏 100 万美元。X 原帖：https://x.com/markovichio/status/2115553133564719512 ／ 文章：https://thehackernews.com/2026/10/japans-gmo-offers-1-million-bounty-to.html ／ 文章：https://www.bleepingcomputer.com/news/security/japans-gmo-urges-customers-to-shut-down-pcs-amid-ransomware-threat/
- **Sony 旗下 So-net**：2,585,481 条会员记录（姓名、电话、邮箱等，无支付信息）。X 原帖：https://x.com/BleepinComputer/status/2115485248775504339 ／ 文章：https://www.bleepingcomputer.com/news/security/sony-isp-subsidiary-data-breach-exposes-25-million-customer-records/
- **123 Reg**：披露「AI 网络攻击」影响客户数据，怀疑中国关联。X 原帖：https://x.com/Dinosn/status/2115419671352459551 ／ 文章：https://www.theregister.com/cyber-crime/2026/10/28/123-reg-discloses-ai-cyberattack-on-customer-data-suspects-china-nexus/5305936
- **摩尔多瓦**：约 75 万个个人识别号（IDNP）泄露、公共服务瘫痪。X 原帖：https://x.com/Dinosn/status/2115441424863056116 ／ 文章：https://www.rfi.fr/ro/republica-moldova/20261028-cel-mai-mare-atac-cibernetic-asupra-republicii-moldova-peste-750-000-de-idnp-uri-compromise-servicii-publice-paralizate-%C8%99i-riscuri-majore-de-fraud%C4%83
- **S2W：hize_hacker（ULOSE）画像**，自建泄露站贩卖韩企数据，可能与 Gunra 有关。X 原帖：https://x.com/S2W_Official/status/2115242140246622222 ／ 厂商报告（S2W）：https://s2w.inc/en/resources/1144
- **Synology NAS「SINUS-NAS」勒索**（VECERT 预警，初始入侵方式未确认）。X 原帖：https://x.com/VECERTRadar/status/2115242734516629778
- **Epic Games GitHub 令牌叫卖**（未证实，自称涉及 56 个仓库）。X 原帖：https://x.com/VECERTRadar/status/2115561367776215179
- **FalconFeeds 勒索告警**：Ryder、Broadstreet HEOR 等被列上泄露站。X 原帖：https://x.com/FalconFeedsio/status/2115225594384601271 ／ X 原帖：https://x.com/FalconFeedsio/status/2115433403223101476
- **Acronis：The Gentlemen RaaS 深度分析**。文章：https://www.acronis.com/en/tru/posts/the-gentlemen-a-closer-look-at-a-not-so-gentle-ransomware-as-a-service-operation/
- **Nefilim／Hive 附属成员获刑 70 个月**。文章：https://www.bleepingcomputer.com/news/security/nefilim-and-hive-ransomware-affiliate-gets-70-months-in-prison/
- **FEC 竞选财务申报遭攻击中断**。文章：https://securityboulevard.com/2026/10/hacking-attempt-disrupts-fec-campaign-finance-filings/
- **Convertr 电商平台供应链攻击（续）**。文章：https://www.scworld.com/brief/supply-chain-attack-compromises-convertr-e-commerce-platform
- **Water Galura**：DefendEdge 称 7 天追踪到 103 次攻击、周环比 +115%（制造、医疗）。X 原帖：https://x.com/DefendEdge/status/2115444511027466517

## 地址／IoC 汇总

以下全部原样抄录公开来源后做了 defang（`hxxp`、`[.]`），只供封锁和狩猎使用，访问前务必在隔离环境里核实。

### Node2Shell（CVE-2026-111497）攻击来源 IP（jorgeliauw 传感器）

- `94.154.43[.]7`
- 来源：https://x.com/jorgeliauw/status/2115528035189285334

### Kimsuky C2（phatomcandle）

- `27.102.137[.]57`
- 来源：https://x.com/phatomcandle/status/2115458571773034886

### INJ3CTOR3 FreePBX 植入物（DFIR_Radar）

- 暂存主机：`45.95.147[.]178`、`160.119.69[.]4`（上传路径 `/hima_data/index.php`）
- JOMANGY webshell 门禁哈希（MD5）：旧 `a2f6863413c4192a4abfa360577b9961` → 新 `8b3a1d970fda0c17a0b785a990fb7b6a`
- 主机水印：`trace_bd42a8a0d23ae16c85dede7d2abaec05`、`trace_7544725ebaaadac217dfaa7ca8e8fe7e`
- 来源：https://x.com/DFIR_Radar/status/2115338669598855584

### EmunaEliran 每日清单（第 1/3 部分，原帖已 defang）

- AMOS（SHA256）：
  - `1be8fa32f3352a7a6ec520ed39328f886f15796ff8290f980e7cc29360990227`
  - `224b29b4a505df4bff072b64d030d6b7a9b5948a0fd3285ecd6e17ea2368bdce`
  - `2632867386186be5e4488386c139db1b7bd6cf4d37ebf188035986e631d2d49b`
  - `42f86033600342d7c20a4604409ac56bb25eaab55610110dce4203c32d270a01`
  - `444ed24e3824df84f4eca0a460d17e1a8307e0a188329781e7b23b62cb958613`
  - `5b655fc81c7688861ef92a2309b2e689f3e486841a07bdc939ce4f01a30785ea`
  - `60cdc213550d1f6a4efdba7d7053b0407310d5343f1fd64b65cd5ab530b0fea6`
  - `655e38419e203ae667a3252c30b9393c7cabefca43b2daa1fffbf17eb03cdc27`
- ClearFake 域名：`5v8ryehz[.]worknernorgram[.]rest`
- VShell IP：`60[.]204[.]226[.]40`、`8[.]140[.]228[.]202`
- Unknown Stealer 域名：`akumaqqq[.]xyz`
- Vidar 域名：`et[.]aeon888link[.]org`
- Hermes URL：`hxxp://216[.]158[.]95[.]183:8700/login`
- Phorpiex URL：`hxxp://85[.]193[.]68[.]206/angel`
- 来源：https://x.com/EmunaEliran/status/2115395182740844899 （第 2、3 部分未抓取）

### 哥伦比亚税务主题 VBS 下载器（DFIR_hanan96，SHA256）

- `Soporte_cred itacion_no8086.zip`：`674a6f72681e395ff3d0da0c88027393dfbd6bd842a03c744413a45932b05f1a`
- `Sustentacion_Fiscal_2025.vbs`：`c69153e9f3bc938a384c5c0c254938a5bc6be1668bc1a8e4fc0f284d8a07841d`
- 来源：https://x.com/DFIR_hanan96/status/2115263434304757838

### LodaRAT 假法院 ADR 钓鱼（ThreatDown）

- 域名：`florida[.]courtadr[.]com`（钓鱼页）、`support[.]courtadr[.]com`、`courtadr[.]com`（发件域）、`us[.]wind0ws[.]net`（载荷下载）、`my[.]thispc[.]net:4000`（C2）
- IP：`207[.]148[.]77[.]235`（C2）、`67[.]217[.]49[.]66`（源站／发件 IP）
- SHA256：
  - `18b7fb1ead8354847b95cdbb7e1fb655dac59c970ab88ff68afc82d37a5e0108`
  - `1cd822b584795da0981798fd11958635deaccc72b50ba2a6c3e9981fa4f94c29`
  - `2b2cf3626f4d79fa2b10001f024b86677c63e2381f0923331924d26b1ee676ba`
  - `377959c943467a6c9e237d83401a07b9b58418670396e194e5ecd4f2d7a07aa5`
  - `8934202a8b2c65b47fe178e97dccfa311ff0542a936e15fc81ff228ddfce2321`
  - `8caaaf8451298f09c38fcf8e51e035bfcf2101b735d76b7bba2dddd4bbf1b9e2`
  - `8d4d6808d9b88683149a8c6e2b33e4ed62587dfcfd32e6a6c60b087206141c88`
- 来源：https://www.threatdown.com/blog/fake-court-adr-phishing-lodarat/ （哈希与文件对应关系见原文）

### Magento loader（Sansec／malwrhunterteam）

- `deepveindrilling[.]com`
- 来源：https://sansec.io/research/magento-cms-block-loader-deepveindrilling ／ https://x.com/malwrhunterteam/status/2115526020560249143

### Virtualine 防弹主机

- ASN：`AS202412`（Omegatech LTD）
- 来源：https://x.com/abuse_ch/status/2115350081603854801 ／ https://urlhaus.abuse.ch/asn/202412 ／ https://threatfox.abuse.ch/asn/202412/

### 可疑「PoC」仓库（不建议运行）

- `hxxps://github[.]com/murrez/CVE-2026-76268`（自称 Splunk PoC，被指为通用脚本改写，大概率无效）
- 来源：https://x.com/papa_anniekey/status/2115389263957434436

### 其他

- **PHP2Shell＋Fragnesia（Dream）**、**Volt Typhoon Silent Train（Lumen）**、**Lazarus FlashHole**、**ESXi CVE-2026-41709**：X 原帖和本轮抓取的报告正文中未见公开 IoC。
- **CyberDakait**：Group-IB 原报告含 IoC，本轮未抄录，见 https://link.group-ib.com/4zYErEw
- **ICMacOS**：原报告含域名／IP／URL／哈希，本轮未抄录，见 https://cybersecuritynews.com/icmacos-remote-access-trojan/
- **Norforge AI 面板接管**：原报告含 IP／域名／哈希，本轮未抄录，见 https://norforge.com/blog/automated-subversion-attempted-takeover

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
- PHP2Shell／Node2Shell／ESXi／Volt Typhoon 专题：https://x.com/search?q=(PHP2Shell%20OR%20Node2Shell%20OR%20CVE-2026-46300%20OR%20CVE-2026-41709%20OR%20%22Volt%20Typhoon%22)&f=live
- GitHub 红队工具：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20BOF)&f=live
- 恶意软件分析：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)&f=live
- IoC：https://x.com/search?q=(IOCs%20OR%20%22C2%20server%22%20OR%20sha256)&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- GitHub 链接＋安全关键词：https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20EDR%20OR%20exploit%20OR%20malware)&f=top
