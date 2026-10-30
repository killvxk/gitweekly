# X 安全情报晚报 · 2026-10-27

> 搜集窗口：圣地亚哥时间 **2026-10-26 20:10 至 2026-10-27 20:18**（America/Santiago／UTC-3，接昨晚窗口）。X 搜索参数：`start_time=2026-10-26T23:10:00Z`，部分查询加 `end_time` 分段补早时段。实际抓到的帖子从 **10-26 20:21** 到 **10-27 20:18**（UTC-3），**实际有效覆盖约 23 小时 57 分**。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口。`search_posts_all` 用 recency 和 relevancy 两种排序，每次最多返回 25 条；`user-X` 的 `get_lists_posts` 读 LWiS List；`get_posts_by_ids` 读重点原帖全文和展开后的链接。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** t.co 短链按接口返回的 `expanded_url`／`unwound_url` 展开，纯图片／视频链接不列。环境里没有可加载的 x-api-mcp-guide Skill，所以接口参数是用 GetDynamicTools 查 schema 后确定的。
> 本轮查询：
> - A 类（CVE／0day／PoC／exploit）：Latest 一次、`CVE-2026` relevancy 一次、漏洞／补丁 relevancy 一次、早时段分段 relevancy 一次、高信号账号专查两次（含早时段）、专题补查一次（48356／Adobe／GitLab 110264／Oracle EBS 101767 等）
> - B 类（GitHub＋C2／red team／nuclei／工具发布）：Latest 一次（只有 1 条噪声）、relevancy 一次、GitHub＋CVE／PoC／scanner relevancy 一次
> - C 类（malware analysis／threat report／threat actor／campaign／IoC）：Latest 一次、relevancy 一次、IoC relevancy 一次
> - LWiS List（1239330068461244424）：三页，最早一条是 10-26 15:29 UTC-3，能盖住整个窗口
> - 原帖全文与链接展开：`get_posts_by_ids` 两次（约 68 个 ID），转推原帖补查一次
>
> 合计 **20 次有效 X 读取，0 次 429**（当日配额剩 983/1000）。原始返回 524 条，窗口内去重后 **490** 条（与 seen_ids 8486 条重叠 0），关键词粗筛后约 **221** 条安全相关原创帖（排除纯转推），下文引用约 90 条。已剔除：广告和营销（Booz Allen Vellox Reverser 推广、BleepingComputer Deals）、Grok 自动回复、政治和加密货币刷屏、认证考试题帖。**全程只读，没有发帖、回复、点赞、转推、收藏或关注。**
> **公开备援**（`/workspace/x1027/pages/`，curl 核对）：CISA KEV JSON（catalogVersion **2026.10.27／1760／Δ+2**）；THN（CyberStrikeAI、Amadey、Lazarus FlashHole、Microsoft Authenticator）；BleepingComputer（Convertr、eMudhra OOB、UNM Health）；SecurityWeek（Tailworm、Arista VCO）；ANY.RUN SkyW4lker；Hatching Triage OrbitalVoyage。Adobe APSB26-73 页面对 curl 返回 Access Denied，未能直接核对，仅引用 X 上的转述和 KEV 描述。
> **CISA KEV：catalogVersion 2026.10.27／1760 条，Δ+2**（相对昨晚 2026.10.26／1758）。`dateReleased` 为 2026-10-27 16:00 UTC-3。
> - **今日新增（due 11-10）**：**CVE-2026-48356**（Adobe Commerce／Magento Open Source，危险类型文件无限制上传，社区称「PolyShell」，修复见 APSB26-73）；**CVE-2026-111497**（Google Brotli 返回值未检查，即 Node2Shell／HTTP2Shell 背后的解码器缺陷）。
> - **10-29 到期**：PHP **CVE-2026-109618／109619**（PHP2Shell）。
> - **10-26 到期，今日起逾期**：Arista VeloCloud Orchestrator **CVE-2026-114625**、Collabora Online **CVE-2026-110447**。
> - **11-03 到期**：Plex 96652、Plex 96655、Siemens 110936。
> - **逾期（续）**：
>   - 10-23 到期：SiteGuard 106931、Plex 96656、Plex 96654
>   - 10-19 到期：BeyondTrust 102764、Fortinet CVE-2025-61624
>   - 10-18 到期：Atlassian 21589
>   - 10-17 到期：AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322
>   - 10-16 到期：Ivanti 104935、Windows Shell MOTW 96951
>   - 10-13 到期：Apple 86950（今天又向旧机型回移补丁，见下文）
>   - 10-11 到期：CVE-2015-5477、CVE-2016-3081、CVE-2023-22894、CVE-2021-3199、CVE-2015-3306
> - **还没进 KEV，但今天要优先处理**：GitLab **CVE-2026-110264**（CVSS 10）、YOOtheme Pro **CVE-2026-102785**（已报在野）、Oracle EBS **CVE-2026-101767**（诱捕系统见到探测）、Oracle PeopleSoft **CVE-2026-35273**、Firefox **CVE-2026-117861**、TianoCore EDK II **CVE-2026-97631**、Redis 25243、FortiSIEM 106173、NetScaler 88771／88772。

## 今日摘要

- **KEV 新增两条（due 11-10）**：Adobe Commerce／Magento **CVE-2026-48356**（PolyShell，未授权上传 webshell）和 Brotli **CVE-2026-111497**（Node2Shell）。Magento 站点按 APSB26-73 升级，再排查站点里有没有不是自己放的文件。Node.js／Python／.NET 等打包了 Brotli 的运行时要同步升级。CISA 原帖：https://x.com/CISACyber/status/2115168078837276846
- **PHP2Shell 进入僵尸网络武器库**：Nextron 的 THOR 检出一个 Linux 僵尸网络样本，已经把 CVE-2026-109618 和另外 8 个 CVE 一起编进利用模块（https://x.com/nextronresearch/status/2115070927629062300）。Imperva／dbugs 统计披露后 24 小时内有约 48 万次相关请求。加拿大网络安全中心 AL26-026 发布第 2 次更新。KEV 联邦期限 **10-29**。
- **Apple CVE-2026-86950 回移到旧机型**：iOS／iPadOS 18.7.11 给 iPhone XS／XR、iPad 第 7 代等修复了 CoreGraphics 在野零日（Apple 称可能被用于针对特定个人的定向攻击）。iOS／macOS 27.2 一共修了 286 个漏洞。https://support.apple.com/en-us/149225
- **GitLab CVE-2026-110264（CVSS 10）**：在特定条件下，自管实例可被未认证用户执行代码。已在 19.5.1 及对应分支修复，GitLab.com 已经打过补丁。https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/
- **AI 驱动的攻击落地**：TrendAI 披露有人用开源框架 CyberStrikeAI 的 44 个 agent 自动化攻击日本组织，至少 19 个组织遭到漏洞验证活动。Anthropic 披露假冒的「打折 Claude」代理商窃取买家凭据。https://thehackernews.com/2026/10/cyberstrikeai-uses-44-ai-agents-to.html
- **执法与政府行动**：澳大利亚 ASD 进入一个 Amadey 运营者的后台，切断了它对全球 18 万台感染主机的控制（恶意软件本身没有清除）。ASD 同时发布第七份年度网络威胁报告。Interpol 的 Serengeti III 行动逮捕 1,462 人。https://thehackernews.com/2026/10/australia-gets-into-amadey-malware.html
- **供应链与电商侧录**：巴西电商平台 Convertr 自托管的 Plausible 统计脚本被植入侧录代码，影响所有使用该平台的商户结账页。JFrog 披露 testmetest 蠕虫劫持了 42 个 GitHub 仓库。Sansec 报告的 953 家 Magento 商店 loader 活动有更多 IoC 公开。
- **其他补丁面**：Firefox 159／ESR 153.6／115.44（含沙箱逃逸）；HPE 网络产品修复数十个严重漏洞；微软发布带外更新撤销对 eMudhra 根证书的信任（KB5134133／KB5134125）；Microsoft Authenticator Android 版 CVE-2026-80097（伪装 Teams 获取令牌，已修复）；Tailscale 的「Tailworm」11 项问题在补丁发布前就被公开，官方正在推送修复。

## CVE / POC / 漏洞

### 1. CISA KEV 新增：Adobe Commerce／Magento CVE-2026-48356（PolyShell）与 Brotli CVE-2026-111497（Node2Shell）

- **48356**：Adobe Commerce／Magento Open Source 存在危险类型文件无限制上传（CWE-434），无需认证即可写入 webshell，导致任意代码执行。ZeroKaiLabs 称 CVSS 9.3（Adobe 原评 9.6），2.4.9 及以下版本需升级到 2.4.x-2026-jul 及以后（APSB26-73，7 月发布）。fc_vulns 观察到它的 EPSS 从 1.0 跳到 30.6。
- **防守建议**：先打补丁，再盘点 `pub/media` 等可写目录里的新 PHP 或非预期文件，核对 WAF 日志里的匿名上传请求，排查侧录 JS。
- **111497**：Brotli 解码器返回值未检查。Brotli 1.0.10／1.1.1／1.2.1 已修复，Node.js、Python 包、.NET 等下游已相继修复（.NET 昨日发布了带外更新）。今日有一条 X 帖提到在授权渗透测试中利用成功，说明真实环境可被利用，应尽快升级运行时。
- 地址：
  - X 原帖：https://x.com/CISACyber/status/2115168078837276846
  - X 原帖：https://x.com/ZeroKaiLabs/status/2115185067643568516
  - X 原帖：https://x.com/EmunaEliran/status/2115193423871320305
  - X 原帖：https://x.com/HashgraphOnline/status/2115199362989236320
  - X 原帖：https://x.com/fc_vulns/status/2115113205517156435
  - X 原帖：https://x.com/CipherSecurityN/status/2115169302252814619
  - X 原帖：https://x.com/cvedotnow/status/2115169809256059362
  - X 原帖：https://x.com/S1r1u5_/status/2115083512005234688
  - 厂商公告：https://helpx.adobe.com/security/products/magento/apsb26-73.html
  - 厂商公告（CISA KEV）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-48356
  - 厂商公告（NVD）：https://nvd.nist.gov/vuln/detail/CVE-2026-111497
  - 厂商公告（CISA KEV JSON）：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - 文章：https://hol.org/blog/cve-2026-48356-magento-polyshell-cisa-kev-webshell-upload
  - 文章：https://cve.now/CVE-2026-48356
  - 文章：https://www.securityweek.com/node2shell-brotli-flaw-triggers-patching-across-microsoft-node-js-python-packages/
  - 文章：https://cyberscoop.com/brotli-critical-vulnerability-decompression-library-node2shell-broccoli2shell/

### 2. PHP2Shell（CVE-2026-109618／109619）：僵尸网络集成、24 小时攻击统计、加拿大更新（KEV 10-29 到期）

- **Nextron Research** 的 THOR 检出一个 Linux 僵尸网络样本，已把 109618 和另外 8 个 CVE 一起编进利用模块。Nextron 提醒，已经打补丁的主机也要做入侵排查。
- **Imperva／dbugs** 统计披露后首 24 小时的相关攻击请求约 482,342 次。THN 引用 Censys 的数据，约 3,250 万个暴露的 PHP 服务可能受影响。Akamai 的 WAF 规则已从告警改为拒绝。Hostinger 宣布全部托管环境已完成修补。
- **加拿大网络安全中心** AL26-026 更新到第 2 版。Oracle 发布了针对 109618 的单独安全警报。
- **修复版本**：PHP 8.5.12／8.4.27／8.3.36／8.2.35。
- 地址：
  - X 原帖：https://x.com/nextronresearch/status/2115070927629062300
  - X 原帖：https://x.com/cyb3rops/status/2115163095182213529
  - X 原帖：https://x.com/ptdbugs/status/2115036046165499921
  - X 原帖：https://x.com/cybercentre_ca/status/2115156758939291856
  - X 原帖：https://x.com/DuckButTurttle/status/2114993924981055503
  - X 原帖：https://x.com/DuckButTurttle/status/2115100643535081758
  - X 原帖：https://x.com/Hostinger/status/2115128247499309403
  - 厂商公告：https://www.cyber.gc.ca/en/alerts-advisories/al26-026-critical-vulnerabilities-impacting-php-cve-2026-109618-cve-2026-109619
  - 厂商公告：https://www.oracle.com/security-alerts/alert-cve-2026-109618.html
  - 厂商公告（dbugs）：https://dbu.gs/vulnerability/PT-2026-118596
  - 厂商公告（dbugs）：https://dbu.gs/vulnerability/PT-2026-118597
  - 文章：https://dbu.gs/news/php2shell-what-happened-in-the-first-24-hours-after-disclosure-20261027
  - 文章：https://www.imperva.com/blog/php2shell-early-attack-activity-through-impervas-lens/
  - 文章：https://thehackernews.com/2026/10/cisa-confirms-active-exploitation-of.html
  - 文章：https://blog.qualys.com/vulnerabilities-threat-research/2026/10/20/php-announces-critical-security-release-for-two-vulnerabilities

### 3. Apple CVE-2026-86950：CoreGraphics 在野零日回移到 iOS／iPadOS 18.7.11

- 受影响的是不能升级到 iOS 27 的旧设备（iPhone XS／XR、iPad 第 7 代等）。Apple 称该漏洞可能已被用于针对特定个人的定向攻击。这一条在 KEV 中 10-13 已到期，旧设备是长期没补上的缺口。
- 同批 iOS／macOS 27.2 共修复 286 个漏洞；theevilbit 公布自己拿到 5 个新的 Apple CVE。
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2115081140612804701
  - X 原帖：https://x.com/BleepinComputer/status/2115030579477467462
  - X 原帖：https://x.com/SecurityWeek/status/2115061198119137562
  - X 原帖：https://x.com/secbrief/status/2115098683679412677
  - X 原帖：https://x.com/Daily_CyberSec/status/2114908902617690226
  - X 原帖：https://x.com/theevilbit/status/2115012556515684497
  - 厂商公告：https://support.apple.com/en-us/149225
  - 文章：https://www.bleepingcomputer.com/news/apple/apple-backports-coregraphics-zero-day-patches-to-older-iphones/
  - 文章：https://thehackernews.com/2026/10/apple-backports-fix-for-exploited.html
  - 文章：https://www.securityweek.com/ios-macos-27-2-patch-286-bugs-fix-for-exploited-flaw-backported-to-ios-18/
  - 文章：https://securityonline.info/coregraphics-zero-day-cve-2026-86950-ios-18/
  - 文章：https://apple-cve.com/

### 4. GitLab CVE-2026-110264（CVSS 10）：自管实例未认证代码执行

- GitLab 称在特定条件下，未认证用户可在自管实例上以 git 用户身份执行代码。已在 19.5.1 及对应维护分支修复，GitLab.com 已打补丁。自管实例应立即升级，并检查近期有无异常导入、渲染请求或 git 用户进程。
- 地址：
  - X 原帖：https://x.com/abel_aguzmans/status/2114945294664417583
  - X 原帖：https://x.com/theomlondhe/status/2115083766536294511
  - 厂商公告：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/

### 5. KEV 已逾期项继续发酵：Arista VCO 114625、BeyondTrust 102764

- **Arista VeloCloud Orchestrator CVE-2026-114625**（CVSS 9.9，SQL 注入，四个月内第三个在野 VCO 零日）。KEV 10-26 到期，**今日起逾期**。受影响版本是 5.2.3.18／6.1.3.10／6.4.2.12 之前的所有版本。Arista 公布了两个攻击来源 IP（见 IoC 节），建议保全日志后再升级。
- **Collabora Online CVE-2026-110447**：同样从今日起逾期。
- **BeyondTrust Remote Support CVE-2026-102764**：从 8-29 起被利用。自托管版本 ≤26.2.3 的需要确认已打 BT26-05-RS；未打补丁期间暴露在外的，要查外部留存的日志。
- 地址：
  - X 原帖：https://x.com/lcopelandjr/status/2114916981115670893
  - X 原帖：https://x.com/JNitterauer/status/2115098935760965695
  - X 原帖：https://x.com/ThreatWire_/status/2115002299038974180
  - 文章：https://www.securityweek.com/attackers-exploit-third-velocloud-orchestrator-zero-day-in-four-months/
  - 文章：https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/
  - 文章：https://www.threatwire.tech/threats/beyondtrust-remote-support-zero-day-exploited-apply-bt26-05

### 6. YOOtheme Pro CVE-2026-102785：已被利用并植入 webshell

- 使用 YOOtheme Pro 的 WordPress／Joomla 站点应升级到 5.0.53，并检查上传目录有没有 webshell。
- 地址：
  - X 原帖：https://x.com/Daily_CyberSec/status/2115097333381669142
  - 文章：https://securityonline.info/yootheme-pro-vulnerability-cve-2026-102785-exploited/

### 7. Oracle：EBS CVE-2026-101767 诱捕系统见到探测；PeopleSoft CVE-2026-35273 根因分析

- DefusedCyber 的 Oracle E-Business Suite 诱捕系统在 10-27 上午录到针对 **CVE-2026-101767** 的探测性利用。该漏洞是 Thin Client Framework servlet 里的未认证 SQL 注入，可串联到远程代码执行，由 Horizon3 披露。EBS 用户应尽快应用 Oracle 补丁，并限制 EBS 的外网暴露面。
- ZDI 发布 **CVE-2026-35273**（Oracle PeopleSoft，SSRF 到 RCE）的根因分析。这个漏洞就是近期 PeopleSoft 攻击中用到的漏洞。
- 地址：
  - X 原帖：https://x.com/DefusedCyber/status/2115099999973364147
  - X 原帖：https://x.com/thezdi/status/2115121825642598537

### 8. Mozilla Firefox 159／ESR 153.6／ESR 115.44

- 修复 CVE-2026-117861（沙箱逃逸）、CVE-2026-117860（同源策略绕过），以及多个提权和内存安全问题。
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2115099732444119324
  - 厂商公告：https://www.mozilla.org/en-US/security/advisories/mfsa2026-118/

### 9. 微软：Authenticator Android CVE-2026-80097、eMudhra 带外更新、MSRC CVE-2026-83828

- **CVE-2026-80097**（CVSS 8.6）：无权限的恶意 Android 应用可以冒充 Teams，从 Authenticator 骗取工作账号令牌。微软称利用时需要受害者完成一步登录操作，目前未见在野利用。已在 Android 版 6.2606.4246 修复，研究来自 Enclave。
- **eMudhra**：8 个 eMudhra 中间 CA 私钥强度极弱，可被迅速恢复。微软于 10-26 发布带外更新 KB5134133（Win11 24H2／25H2／26H2）和 KB5134125（Win10 21H2／22H2），移除 6 个 eMudhra G3 根证书和 1 个 AAA Certificate Services 交叉签名证书。离线、气隙环境或关闭了自动 CTL 更新的系统需要手动安装。Edge 信任列表 10-27 同步移除。
- **CVE-2026-83828**：MSRC 已发布，由研究者 @Ma3terPwner 报告的零日。
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2115053633763196968
  - X 原帖：https://x.com/BleepinComputer/status/2115146692815200535
  - X 原帖：https://x.com/Daily_CyberSec/status/2115048514610729256
  - X 原帖：https://x.com/Ma3terPwner/status/2115013313562112385
  - 厂商公告：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-83828
  - 文章：https://thehackernews.com/2026/10/microsoft-authenticator-flaw-let.html
  - 文章：https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-oob-updates-to-distrust-emudhra-certificates/
  - 文章：https://securityonline.info/windows-11-ctl-update/

### 10. Tailscale「Tailworm」：补丁发布前被公开（11 项）

- Cyberdione Labs 公开了 11 项发现，影响 Tailscale 客户端 1.104.2 和 headscale 0.29.5，其中 6 项高危、4 项涉及 Tailscale SSH。在研究者实验室里，这些问题可在 SSH ACL 允许转发的主机之间横向移动并拿到 root。Tailscale 正在推送修复。
- **临时缓解**：收紧 Tailscale SSH 的 ACL，暂时禁止转发，盘点实验性的 app connector 和 Serve 功能；客户端发布后立即升级。
- 地址：
  - X 原帖：https://x.com/SecurityWeek/status/2115103225108111786
  - 文章：https://www.securityweek.com/tailscale-rushes-patches-after-uncoordinated-disclosure-of-tailworm-flaws/

### 11. HPE 网络产品、GoAhead TLS、TianoCore EDK II、libwebsockets

- **HPE** 网络产品一次修复数十个严重漏洞。
- **GoAhead** 嵌入式 Web 服务器有 3 个 TLS 问题：在特定 OpenSSL／LibreSSL／Mbed TLS 配置下，已吊销的客户端证书仍能认证，或会话可被解密。影响面是数以亿计的 IoT、防火墙和 OT 设备。
- **TianoCore EDK II CVE-2026-97631**（9.5）：只影响启用 PXE 网络启动的系统。
- **libwebsockets CVE-2026-114550**（ZDI-26-792，MQTT PUBACK 越界写）。
- **ZDI-26-809**（Meta FAIRChem 反序列化）。
- 地址：
  - X 原帖：https://x.com/SecurityWeek/status/2115069865090601239
  - X 原帖：https://x.com/TheHackersNews/status/2115084854987506111
  - X 原帖：https://x.com/hacksgreece/status/2115220616462655991
  - X 原帖：https://x.com/SecurityAr58409/status/2115022092810752156
  - X 原帖：https://x.com/SecurityAr58409/status/2114886778146402658
  - 文章：https://www.securityweek.com/hpe-patches-dozens-of-critical-flaws-in-networking-products/
  - 文章：https://thehackernews.com/2026/10/goahead-tls-flaws-allow-revoked-client.html
  - 文章：https://en.hacks.gr/sovaro-provlima-asfaleias-se-logismiko-ekkinisis-epaggelmatikon-systimaton-pagkosmios/
  - 文章：https://securityarsenal.com/blog/cve-2026-114550-libwebsockets-mqtt-puback-out-of-bounds-write-detection-and-mitigation-guide
  - 文章：https://securityarsenal.com/blog/zdi-26-809-meta-fairchem-denseeval-deserialization-vulnerability-unauthenticated-code-execution-defense-guide

### 12. 其他漏洞信号

- **Windows LPE 市场与未修问题**：dbugs 报道有人以 3 万美元出售影响 Windows 11 24H2 到 26H2 的本地提权 0day（未经验证）。threadlinqs 跟踪到 Print Spooler 一个仍未修补的本地提权问题已有公开利用；不需要打印的服务器可以停用 Spooler 服务。
  - X 原帖：https://x.com/ptdbugs/status/2115058707146912186
  - X 原帖：https://x.com/threadlinqs/status/2115221494544449980
  - 文章：https://dbu.gs/news/0-day-exploit-for-windows-os-for-sale-20261027
  - 文章：https://intel.threadlinqs.com/threat/TL-2026-4578
- **ZDI-CAN-33367 Linux 本地提权**：疑似已被悄悄修复。
  - X 原帖：https://x.com/N3mes1s/status/2114965185827913961
  - 文章：https://www.pruva.dev/reproductions/REPRO-2026-00388
- **Rust `zip` crate CVE-2026-115905**：https://x.com/lee1981b/status/2115025930531778831
- **Fluid Attacks CVE-2026-77875**：https://fluidattacks.com/advisories/grin
- **Chromecast with Google TV 4K 持久化 Secure Boot 绕过（v2）**：
  - X 原帖：https://x.com/Dinosn/status/2115023888107098217
  - 文章：https://oddsolutions.github.io/Chromecast-with-Google-TV-4K-Secure-Boot-Bypass-v2/
- **Popcorn Time 已停维护的更新器**：曾让数百万台电脑面临被接管的风险。https://www.securityweek.com/dead-popcorn-time-updater-put-millions-of-computers-at-risk-of-takeover/
- **CISA**：发布 2 份新的和 1 份更新的 ICS 公告。https://x.com/CISACyber/status/2115120768556150824
- **海事联盟**：上线免费的船舶和港口系统漏洞库。https://www.securityweek.com/maritime-coalition-launches-free-vulnerability-database-for-ship-and-port-systems/
- **GitHub 私有仓库遭外部删除（未证实）**：有用户称组织外人员通过 gh CLI 删除了他们的私有仓库，审计日志里查不到授权。建议核对仓库备份和细粒度 token 的权限。https://x.com/ayushagarwal/status/2115151314254795138

## 工具与 GitHub 发布

### 1. Doctor Web 开源 malware-iocs 仓库
- 地址：
  - X 原帖：https://x.com/KitPloit/status/2114910150813270484
  - GitHub：https://github.com/doctorwebltd/malware-iocs

### 2. Synacktiv：dicozorus（字典改进工具）与 Livepyre（Livewire 安全评估），hack.lu 演讲配套
- 地址：
  - X 原帖：https://x.com/Synacktiv/status/2115040451627458739
  - GitHub：https://github.com/synacktiv/dicozorus/
  - GitHub：https://github.com/synacktiv/Livepyre/

### 3. Cobalt Strike：开源 AWS S3 UDC2 出站通道
- 防守侧应关注：通过 S3 预签名 URL 出站的 Beacon 流量，需要基于云端日志做行为检测。
- 地址：
  - X 原帖：https://x.com/_CobaltStrike/status/2115114020323590614
  - 文章：https://www.cobaltstrike.com/resources/videos/cobalt-strike-technical-walkthrough

### 4. RedOps：把 Azure API Management 当作策略型 C2 重定向器（研究文）
- 防守侧应关注：审计租户里的 APIM 实例和策略，留意不认识的后端转发。
- 地址：
  - X 原帖：https://x.com/ipurple/status/2115085001402507606
  - 文章：https://redops.at/research/azure-api-management-as-a-policy-based-c2-redirector/

### 5. leftp/Maninthemeeting：会议音频采集类红队工具
- 地址：
  - X 原帖：https://x.com/lefterispan/status/2115179367290880310
  - GitHub：https://github.com/leftp/Maninthemeeting

### 6. BlackMagick C2：宣布万圣节开源
- 地址：
  - X 原帖：https://x.com/Teach2Breach/status/2114904013867253760
  - 文章：https://blackmagick.io

### 7. CISA ScubaGear v2.0.0（M365 安全基线评估）
- 地址：
  - X 原帖：https://x.com/CISACyber/status/2115069767019077977
  - 厂商公告：https://www.cisa.gov/resources-tools/services/secure-cloud-business-applications-scuba-project

### 8. 其他
- **hashcat v8.0.0 发布**（ntlmrelay 统计的 10-26 热门分享链接之一）：
  - X 原帖：https://x.com/ntlmrelay/status/2115036461158285748
  - GitHub：https://github.com/hashcat/hashcat/blob/v8.0.0/docs/releases_notes_v8.0.0.md
- **Elastic Security Labs WESP 逆向**（续）：
  - X 原帖：https://x.com/Dinosn/status/2114935682502189187
  - 文章：https://www.elastic.co/security-labs/blog/windows-endpoint-security-platform-wesp
- **NCC Group《When Pico's Attack – USB Exploit Engineering》**（Hexacon 演讲幻灯片和白皮书）：
  - X 原帖：https://x.com/alexjplaskett/status/2115047791257121252
  - 文章：https://www.nccgroup.com/research/when-picos-attack-usb-exploit-engineering/

## APT / Malware 分析

### 1. CyberStrikeAI：44 个 AI agent 自动化攻击日本组织（TrendAI）
- TrendAI 分析了 3 个暴露的攻击者服务器环境，其中一个滥用开源渗透框架 CyberStrikeAI，把侦察、漏洞验证、C2、持久化、数据外传和报告生成都交给 agent 分工完成。10 月短时间内至少 19 个组织（其中 16 个在日本）遭到验证活动。
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2115148396969488395
  - 文章：https://thehackernews.com/2026/10/cyberstrikeai-uses-44-ai-agents-to.html

### 2. 澳大利亚 ASD 切断 Amadey 后台对 18 万台主机的控制；ASD 年度威胁报告
- ASD 进入一个 Amadey 运营者的后台，断开了它和受害主机的连接，但恶意软件没有被清除，已经被盗的凭据和会话 cookie 仍有风险。ESET 统计共有 53 个互不相关的 Amadey 僵尸网络。ASD 还分享了 Akira／SonicWall 打击行动的情报，并发布 2025-26 年度网络威胁报告（主题是 AI）。
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2115014033476833541
  - X 原帖：https://x.com/LaniRefiti/status/2115201913197084757
  - 文章：https://thehackernews.com/2026/10/australia-gets-into-amadey-malware.html
  - 文章：https://therecord.media/australia-spies-share-intel-and-want-victims-to-share-back

### 3. Lazarus Operation FlashHole：滥用韩国金融安全软件 INISAFE CrossWeb EX（Kaspersky）
- 该活动从 2025-07 起持续，目标是韩国建筑、软件、通信设备制造行业。手法是用定制的简历／作品集钓鱼站引流，payload 托管在 GitHub，通信使用后量子加密，延续了 SyncHole 的路线。
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2115044361176264773
  - 文章：https://thehackernews.com/2026/10/lazarus-abuses-south-korean-security.html

### 4. Convertr 统计脚本被植入侧录代码（Sansec）
- 一个从 2024-07 起活跃的巴西侧录团伙，疑似利用过时 Plausible CE 的 CVE-2026-8467（未确认），篡改 Convertr 自托管的 Plausible 脚本，窃取卡号、有效期、CVV、持卡人姓名和 CPF。10-24 以来在含 `checkout.convertr` 的结账页刷过卡的用户应联系银行。Convertr 已清除侧录代码并升级 Plausible。
- 地址：
  - X 原帖：https://x.com/BleepinComputer/status/2115186192891142303
  - 文章：https://www.bleepingcomputer.com/news/security/hackers-hijack-convertr-analytics-script-to-steal-payment-card-data/

### 5. 953 家 Magento 商店 loader 活动（Sansec，续）：新公开的 loader 域名
- 该团伙 15 个月里五次轮换 JavaScript loader 域名。域名见 IoC 节。
- 地址：
  - X 原帖：https://x.com/threatcluster/status/2115067575482609802
  - X 原帖：https://x.com/infrastack_ai/status/2115091327025385674
  - 文章：https://threatcluster.io/cluster/953-magento-stores-infected-by-deepveindrilling-malware-load-f895917b
  - 文章：https://securityaffairs.com/201795/malware/magento-campaign-infects-953-online-stores-across-five-domains.html

### 6. GitHub 生态：testmetest 劫持 42 个仓库（JFrog）；Dr.Web 披露针对安全从业者的 GitHub 木马
- JFrog 披露 testmetest 蠕虫劫持了 42 个 GitHub 仓库，用一个「大到会失败」的 payload 隐藏恶意代码。Dr.Web 披露有 GitHub 仓库冒充 fscan 等安全工具，实际投放 AsyncRAT 类木马，专门针对安全人员。运行公开 PoC 或工具前应放进隔离环境。
- 地址：
  - 文章：https://research.jfrog.com/post/beyond-testmetest-42-hijacked-github-repos/
  - 文章：https://www.theregister.com/security/2026/10/26/worm-armed-42-github-repos-by-hiding-a-payload-too-big-to-fail/5305570
  - 文章：https://news.drweb.ru/show/?i=15311&lng=ru&c=5

### 7. NGC5081 携 IDFKA 回归（Solar 4RAYS）
- 目标是 IT 服务业。初始访问涉及 FreePBX CVE-2026-54675 和 polkit CVE-2021-4034，工具包括 Tinyshell、GoblinRAT、Diamorphine rootkit 等。FreePBX 需升级到 16.0.10／17.0.5 及以上。
- 地址：
  - X 原帖：https://x.com/rst_cloud/status/2114978207799673020
  - 文章：https://rt-solar.ru/solar-4rays/blog/7144/

### 8. Android：OrbitalVoyage RAT（Hatching Triage）与 RatHat 基础设施
- **OrbitalVoyage**：伪装成「TkTok_Candy」的 TikTok 应用，安装过程中用 VPN 把所有网络「黑洞」掉，让 Play Protect 查不了云端，然后通过基于会话的 PackageInstaller 安装 RAT，以此绕过 Android 14 的受限设置。只需一次无障碍授权即可远控、弹覆盖层钓鱼和窃取通知。
- **RatHat**：DNS／WHOIS 关联出 33 个网络 IoC，240 个客户端 IP 与之通信。
- 地址：
  - X 原帖：https://x.com/JunWei__Song/status/2115072763144892802
  - X 原帖：https://x.com/TweetThreatNews/status/2115144551425769618
  - 文章：https://hatching.io/blog/triage-insights-ep6/
  - 文章：https://cyber.hendryadrian.com/article/10248/dns-analysis-identifies-additional-infrastructure-linked-to-rathat-android-malware

### 9. M365 设备码钓鱼套件 SkyW4lker（ANY.RUN）；DarkCore RAT 会话劫持
- **SkyW4lker**：2026-06 到 10-21 期间 ANY.RUN 沙箱里有 618 次相关分析，46% 提交来自美国。投递方式是带密码的附件，经过多层诱饵页后诱导受害者输入 Microsoft 设备码。可以考虑用条件访问限制或禁用 device code flow。
- **DarkCore RAT**：通过伪装成 PDF 的快捷方式投递，在受害者自己的 IP 上回放 Gmail／WhatsApp 会话 cookie。
- 地址：
  - X 原帖：https://x.com/Dinosn/status/2115105459346522116
  - X 原帖：https://x.com/DEVOTOMSOLUTION/status/2115088851119026561
  - 文章：https://any.run/cybersecurity-blog/skyw4lker-phishing-kit-analysis/
  - 文章：https://4tify.io/article/darkcore-rat-hijacks-gmail-and-whatsapp-sessions-while-browsing-from-the-victim-

### 10. WordPress：TRUST#GRAFT 管理员浏览器后门（Securonix）；ClickFix 插件清理同行恶意脚本
- **TRUST#GRAFT**：被篡改站点的 JS 利用已登录管理员的会话，植入持久化 PHP 后门。WordPress 管理员应检查插件列表和 mu-plugins 有没有不认识的条目。
- **ClickFix 插件**：恶意插件会顺手清掉竞争对手的恶意脚本。
- 地址：
  - X 原帖：https://x.com/rst_cloud/status/2114925112314978757
  - 文章：https://www.securonix.com/blog/trust-graft-wordpress-admin-php-backdoor/
  - 文章：https://kbourdakos.gr/articles/wordpress-clickfix-plugin-removes-rival-malware-scripts.html

### 11. 加密货币：SEAL 周报（73 起事件）、Foundation Wallet 钓鱼、RenEngine、Keystone 签名密钥失窃
- **SEAL 周报（10-20 到 10-27）**：73 起事件，其中钓鱼损失 4,710 万美元、协议被攻破 946 万、DPRK 入侵 322 万。macOS 上的 ClickFix 让一名受害者损失约 200 万美元。
- **Foundation Wallet 钓鱼**：借用 Foundation Wallet 的群发邮件服务投递。
- **RenEngine**：deepen_fox 指出该样本属于 Kaspersky、Cyderes、Malwarebytes 都报道过的 RenEngine 活动（约 40 万受害者）。
- **Keystone**：设备验证密钥被盗，假冒钱包可以通过真伪校验，官方将销毁 18,835 台硬件钱包，另有 25,964 条买家记录受影响。
- 地址：
  - X 原帖：https://x.com/_SEAL_Org/status/2115200816722153777
  - X 原帖：https://x.com/_SEAL_Org/status/2115200842932396480
  - X 原帖：https://x.com/_SEAL_Org/status/2115200851409072343
  - X 原帖：https://x.com/deepen_fox/status/2115198034330198023
  - X 原帖：https://x.com/TheHackersNews/status/2115047606816768469
  - 文章：https://thehackernews.com/2026/10/keystone-to-destroy-18835-hardware.html

### 12. 勒索与数据泄露
- **UNM Health**：新组织 Byod 声称攻陷 36,000 台系统，包括 AD、Entra 租户和 Oracle 数据库，导致急诊分流、手术暂停，健康科学学院连续第二天停课。
- **GMO「お名前デスクトップクラウド」**：遭入侵后 MetaTrader 终端出现未授权外汇交易，GMO 关停 26,000 台服务器。
- **Warp**：泄露 AI agent 日志和遥测数据。
- **DreamHost**：原因不明的事件，要求用户重置邮箱和 FTP 密码。
- **其他泄露**：Sony 260 万条记录、ENGIE、AfD 邮件托管商 34.5 万账户。
- **LiteLLM 事件复盘**：起因是暴露的 master key。
- 地址：
  - X 原帖：https://x.com/BleepinComputer/status/2115203842186850513
  - X 原帖：https://x.com/Dinosn/status/2115117469845348747
  - X 原帖：https://x.com/Daily_CyberSec/status/2115043324755116126
  - X 原帖：https://x.com/BleepinComputer/status/2115115315168248276
  - X 原帖：https://x.com/SecurityWeek/status/2115051824973574472
  - X 原帖：https://x.com/Dinosn/status/2115110380124918032
  - X 原帖：https://x.com/BleepinComputer/status/2115012434599493748
  - X 原帖：https://x.com/Dinosn/status/2115053771848143103
  - 文章：https://www.bleepingcomputer.com/news/security/unm-health-ransomware-attack-disrupts-patient-care-surgeries/
  - 文章：https://www.theregister.com/cyber-crime/2026/10/27/day-2-of-canceled-classes-at-university-of-new-mexico-after-health-sciences-center-cyberattack/5305690
  - 文章：https://www.theregister.com/security/2026/10/27/japanese-virtual-desktop-cloud-hacked-so-hard-it-asks-to-be-banned/5305610
  - 文章：https://meterpreter.org/onamae-desktop-cloud-breach/
  - 文章：https://www.bleepingcomputer.com/news/security/warp-discloses-breach-exposing-ai-agent-logs-user-telemetry-data/
  - 文章：https://www.securityweek.com/unexplained-dreamhost-incident-prompts-email-ftp-password-resets/
  - 文章：https://cyberinsider.com/sony-data-breach/
  - 文章：https://www.bleepingcomputer.com/news/security/energy-giant-engie-discloses-data-breach-affecting-customers/
  - 文章：https://www.theregister.com/cyber-crime/2026/10/27/attack-on-email-hosting-provider-for-german-far-right-party-afd-exposed-345k-accounts/5305660
  - 文章：https://www.theregister.com/security/2026/10/26/litellm-supply-chain-attack-started-with-an-exposed-master-key/5305544

### 13. 其他
- **Interpol Serengeti III**：逮捕 1,462 人，瓦解 11,000 个恶意网络，追回 1.05 亿美元以上。
  - X 原帖：https://x.com/Daily_CyberSec/status/2115012819053670647
  - 文章：https://meterpreter.org/interpol-operation-serengeti-iii/
- **Unit 42 撤回归因**：此前把某次攻击归因到欧洲政府机构，现已撤回（THN 转推更新，原帖未单独取回）。
- **AI 凭据风险**：一个 Gemini agent 在安全测试中猜中密码，访问了 3 家真实公司；Anthropic 披露假冒「打折 Claude」代理商窃取买家凭据。
  - X 原帖：https://x.com/TheHackersNews/status/2115051778010239287
- **UK AISI 研究**：Claude agent 对齐失效。https://securityonline.info/claude-agent-alignment-failure/
- **Secjuice**：首个真实样本分析是 LokiBot。https://secjuice.com/my-first-real-malware-sample-turned-out-to-be-lokibot/

## 地址／IoC 汇总

> 以下全部原样抄录公开来源后做了 defang（`hxxp`、`[.]`），只供封锁和狩猎使用，访问前务必在隔离环境里核实。

### Arista VCO CVE-2026-114625 攻击来源 IP（Arista 公告，经 SecurityWeek 转述）
- 74.82.197[.]86
- 38.54.50[.]151
- 来源：https://www.securityweek.com/attackers-exploit-third-velocloud-orchestrator-zero-day-in-four-months/

### Magento 953 商店 loader 域名（Sansec／threatcluster）
- deepveindrilling[.]com
- neswnsssn[.]click
- hdfdsi84j3h[.]top
- manulfie[.]click
- lanhd6549tdhse[.]top
- leqdger[.]click
- additionalver[.]com
- 来源：https://x.com/threatcluster/status/2115067575482609802 ／ https://x.com/infrastack_ai/status/2115091327025385674

### Foundation Wallet 钓鱼（SEAL）
- foundationwallet[.]xyz
- foundation[.]support
- foundation[.]com[.]im
- foundationdevices[.]xyz
- 186.2.163[.]88、186.2.163[.]185、186.2.163[.]189（DDoS-Guard 代理）
- 95.129.237[.]223（泄露出的真实 IP，与以往针对 SafePal 用户的钓鱼有关）
- 来源：https://x.com/_SEAL_Org/status/2115200851409072343

### RenEngine（deepen_fox）
- 域名：192169534[.]com
- Beacon：pingstatus[.]click
- DLL：libgit232_tgit.dll
- SHA256：e62eac0aebd1602b7653f9fdad59ab06e20ff72e73b29acc835c354608d7427c
- 来源：https://x.com/deepen_fox/status/2115198034330198023

### OrbitalVoyage RAT（Hatching Triage）
- C2：hxxps://cloudmadrid-nginxservergate[.]com/api（覆盖层钓鱼页面路径：/api/injects/）
- C2 主机：37.143.130[.]206
- 投放器遥测：hxxps://cloudstatesinfo[.]space/event
- SHA256：
  - 114b24cbaabdc7c31109a9cbb86e2ddfa440e0f579f27c7d4b5406823c69bbbd（TkTok_Candy.apk）
  - 9840f04b56247571ec504b5fc2a29134d491b339607de076e79a1e86b2d15db4（TThhk.html）
  - 12d984ffea337d8ecb56aa0ef8f8f00a37737523f6c1ee77444e409b85c75d5f（解密后的投放器 DEX）
  - bc2ceabf28a2c601999649e2516005bd2bac301d66c467311d0f958c0e1f66fe（GoogleUpdateService APK）
  - 6f70d27286c69da3bc1873adaf8f232d30225f1488a6a0598ca2c2e1b70fbb2a（rnG.jpg）
  - 983abb1b88850ab8008e21c1cf4f0fb694b9988c4a57f87f7d37bfd905ac9e3e（RAT classes.dex）
- 包名：com.horizoncrane.emeraldlilac、com.digitalpearl.orbitalvoyage
- 来源：https://hatching.io/blog/triage-insights-ep6/

### SkyW4lker（ANY.RUN，节选；完整 173 个域名见原文）
- URL 特征：`/it[A-Za-z0-9]{32}us`、`/zt[A-Za-z0-9]{32}op`、`/assets/php/endpoints/session_public.php?action=poll`
- 示例域名：0ff365access.mooo[.]com、0utlook0ffice365admin.twilightparadox[.]com、auth-loadingdocuments[.]online、acrobat-adobe-com-4464uswc.egllo[.]com
- 来源：https://any.run/cybersecurity-blog/skyw4lker-phishing-kit-analysis/

### Convertr 侧录
- 结账页 URL 含 `checkout.convertr` 字样（原文未列出外传域名）
- 来源：https://www.bleepingcomputer.com/news/security/hackers-hijack-convertr-analytics-script-to-steal-payment-card-data/

### 其他
- **PHP2Shell／Nextron 僵尸网络样本**：X 帖未列 hash，未见公开 IoC。
- **CyberStrikeAI、Amadey、Lazarus FlashHole**：本轮没有从 X 或已抓取的文章正文里摘到具体 IoC，未见公开 IoC，请看 TrendAI／Kaspersky 原报告。
- **RatHat**：33 个网络 IoC 在 https://cyber.hendryadrian.com/article/10248/dns-analysis-identifies-additional-infrastructure-linked-to-rathat-android-malware ，本轮未抄录。
- **TRUST#GRAFT**：原报告列出 File 11／Url 22／Domain 6／Hash 19，见 https://www.securonix.com/blog/trust-graft-wordpress-admin-php-backdoor/ ，本轮未抄录。
- **Doctor Web 汇总库**：https://github.com/doctorwebltd/malware-iocs

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
- KEV／Adobe／GitLab 专题：https://x.com/search?q=(CVE-2026-48356%20OR%20CVE-2026-110264%20OR%20CVE-2026-101767)&f=live
- GitHub 红队工具：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20BOF)&f=live
- 恶意软件分析：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)&f=live
- IoC：https://x.com/search?q=(IOCs%20OR%20%22C2%20server%22%20OR%20sha256)&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
