# X 安全情报晚报 · 2026-10-19

> 搜集窗口：圣地亚哥时间 **2026-10-18 20:10 至 2026-10-19 20:10**（America/Santiago／UTC-3，**24 小时**，接昨晚窗口，没有缺口）。X 搜索参数：`start_time=2026-10-18T23:10:00Z`，`end_time=2026-10-19T23:10:00Z`。实际抓到的帖子时间从 **10-18 20:30** 到 **10-19 20:09**（UTC-3）。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`，Latest／recency 排序）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** 接口回传了 entities，多数 t.co 直接展开，其余用 HTTP 跳转补展开（如 buff.ly → Joe Sandbox）；纯图片／媒体 t.co 不列。A／B／C 三类各跑原始与去噪查询，A 类另做翻页与两个时段切片（截止 13:00、06:00 UTC-3）；C 类做一个凌晨切片；LWiS List 500 成员分 10 段 `from:` 批次全量翻查；另跑核心媒体／厂商账号两页、IoC 猎人账号两页、专题（SiteGuard／Plex2Shell／KEV 到期项）两页、Coruna／DarkSword 专题一页。共 **28 次有效 X 读取**；另有 **8 次调用被 X 端 429 限流拒绝**（首轮 7 个并发全拒、1 次重试再拒，未消耗读取），等 60 秒后改为 3～4 个一组才恢复。
> **覆盖说明（重要）**：每次查询最多 25 条。宽泛查询只覆盖到窗口最后 1～3 小时：A1 只到 20:04 起、C1 只到 19:07 起（UTC-3）；A 类靠翻页与切片补到 **13:01–20:06、11:55–12:53、05:07–05:53** 三段，中间有空档；C 类凌晨切片覆盖 **00:02–10:24**。**10-18 20:10 至 10-19 约 05:00 这段 A／C 关键词流覆盖偏薄**，主要靠 B 类（23:04 起全窗口）、LWiS 成员批次和核心账号第二页（03:08–11:10）补足。另外 A 类大量被 @vulnipulse 的批量 MSRC CVE 机器人帖子占据（本窗口 63 条），挤掉了不少有效帖。
> 窗口内去重后 **536** 条帖子（与 seen_ids 无重叠），关键词粗筛（剔除纯回复、闲聊、广告、"POC" 指有色人种等歧义噪声）得 **339** 条安全相关新帖：**A128（其中约 60 条为 vulnipulse 机器人）／B34／C50／LWiS23／核心＋IoC 猎人59／专题45**（多查询重叠时按最先命中批次归类）。下文实际引用约 110 条。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON（`/workspace/enrich-2026-10-19/kev.json`）；CISA 网站公告列表（最新一条仍是 10-16，今天没有新的 KEV 警报）；厂商／研究页存于 `/workspace/enrich-2026-10-19/web/`：Unit 42（PAN-OS 0257，10-19 更新）、Siemens ProductCERT、SecurityWeek（Siemens／Fortinet）、BleepingComputer（AOMEI、NGINX）、Google Cloud／ManageEngine（AOMEI）、THN（Plex2Shell、Broadcom WPS、GhostAction、Apex Accelerator）、JPCERT/CC（SiteGuard）、Citizen Lab、The Record（FirstVDS）、NetAskari、Check Point 周报、Risky Business、tl;dr sec；NVD API 核对了 Redis 66373／ColdFusion 105899／curl 92392／Siemens 110936／Agent Mesh 103091 的条目状态。GitHub API 查了 nuclei／nuclei-templates／Sliver／emp3r0r／BloodHound／NetExec／Mythic／impacket／Havoc：**只有 BloodHound 出了新版 v9.9.0-rc1**（见工具段）。
> **CISA KEV：catalogVersion 2026.10.16／1748 条，Δ0**（截至约 20:12 UTC-3 周一仍未更新，连续第三天不变）。**due_today（10-19）：2 条**：BeyondTrust **CVE-2026-102764** 与 Fortinet **CVE-2025-61624**。**newly_overdue（10-18 到期）：1 条**：Atlassian **CVE-2026-21589**。已逾期：AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322（10-17）；Ivanti 104935、Windows 96951（10-16）；Apple 86950（10-13）。**未来 7 天内没有新的到期项。** **仍未进 KEV 的在野漏洞**：Siemens Software Center **CVE-2026-110936**（今日新）、SiteGuard 106931、Plex2Shell 链、Rank Math PRO 111862、Redis 66373（单源声称）等。
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接作狩猎用途。泄露、入侵类声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【在野 · iOS 水坑】Coruna／DarkSword 系 iOS 漏洞利用套件被挂在欧洲、拉美、中东的正常网店上**：@malwrhunterteam 先在意大利化妆品站 estrosa[.]it 发现，随后在西班牙萨克斯风店、智利电脑店、法国 Padirac 溶洞景区网店等陆续确认。路径是拼错的 `/js/analystic/assets/js/group.html`。@0xDanielLopez 统计 40+ 域名（PrestaShop／WordPress），@Darkfibr3 称公开遥测 124 个域名、6 个确认受害站。iOS 18 以下用 Coruna 系链，18 及以上用 DarkSword 系链；完整链路窃取钥匙串、34 个钱包 App、照片、备忘录，只驻留内存。已公开 SHA-256、信标域名、ThreatFox／Bazaar 条目。**受害站是不知情的托管方：封路径，别封商家。**
- **【在野 · 勒索】PAN-OS GlobalProtect CVE-2026-0257 被 Qilin、Inc 勒索团伙用作入口**：Unit 42 今天（10-19）更新简报：Spikey Scorpius（Qilin）与 Tarnished Scorpius（Inc）都在利用，另有公开报道归因 Settra 勒索软件。入侵后用 RMM 侦察、RDP／SMB 横移，**一例直接打到 vCenter，关掉 ESXi `execInstalledOnly`，对域控 VMDK 离线导凭据，绕过来宾机 EDR**；还串了 Veeam CVE-2023-27532。KEV 早在 5-29 收录，标注「已知用于勒索」。
- **【在野 · ICS 厂商软件】Siemens Software Center CVE-2026-110936（DLL 侧加载）被 ClickFix 活动利用**：Siemens ProductCERT 确认，攻击者拿正版签名的 3.5.8.7 配自带 DLL；归入 Forescout 披露的 ROMULUS ClickFix 投递平台。修到 **4.0.9.8**。已公开 C2 IP／域名、MSI 与 DLL 哈希、主机痕迹。未进 KEV。
- **【KEV 到期】** **BeyondTrust 102764 与 Fortinet 61624 今天到期**，Atlassian 21589 今起逾期。Rapid7 确认 BeyondTrust 漏洞在披露前已被利用；SecurityWeek 详述 Fortinet 61624 在电信入侵中被当 0day 用来拿 root 并植入 PeerStitch 内存后门。
- **【供应链】** AOMEI Backupper 更新服务器被 UNC7017 在 5–7 月三次各篡改约 10 分钟，投 CROSSROAD／SHINYROAD／ADAPTAGENT（Google、ManageEngine 发完整报告与 IoC）；Rank Math PRO 3.0.123 后门续报（升级不足以清除）；GhostAction 改用 `my-github[.]com` 钓鱼加 OAuth 设备码授权；Elastic 披露假 Web3 加速器 REF8801 用 npm 包投 Win／Mac 窃密木马。
- **【漏洞补丁】** F5 NGINX 带外补丁（15176／93479／97205，媒体续报）；Adobe ColdFusion **CVE-2026-105899（CVSS 10，未认证上传）**；Redis **CVE-2026-66373** 被单一账号称在野（UNCONFIRMED）；curl 92392、Google Agent Mesh 103091、MariaDB、VS Code、Nix、BioStar 驱动等；Metasploit 排队三个 Cisco SEG 模块；Broadcom Wi-Fi WPS「forever day」续报。
- **【APT／间谍】** Citizen Lab：塞尔维亚贝尔格莱德大学校长 iPhone 被 Pegasus **零点击**感染（选举前 6 天）；Kimsuky（APT-C-55）多路径投递；Plex2Shell 在野续报（`mylovelyminer` 连 `ota.proxystream[.]st`）；JPCERT/CC 就 SiteGuard 106931 发出注意唤起。
- **【入侵／泄露（UNCONFIRMED 为主）】** Ahold Delhaize 美欧多品牌系统下线；Bullhorn 下线；Nikkei 一个月内第三起泄露（180 万条）；俄罗斯主机商 FirstVDS 经 VMmanager 6 漏洞被拷客户数据；日本单日多起（H2O 126 万、Nifty、Furusato Choice、JETRO 743、JFA）；Krebs：执法怀疑某赎金谈判公司高管参与运营 ShinyHunters 勒索站；Qilin 声称打了 GardaWorld。
- **【工具】** BloodHound v9.9.0-rc1；COM 劫持持久化 BOF、Malvex（AI 驱动恶意软件分析框架）、Black Sand Beacon；Cloudflare 开源 security-audit-skill；Datadog 披露对 Jev 的「伪造策略」绕过（检测率 ~83%→~4%）。

## CVE / POC / 漏洞

### 1. PAN-OS GlobalProtect · CVE-2026-0257（认证绕过）· Unit 42 10-19 更新：Qilin／Inc 勒索团伙利用
GlobalProtect 门户／网关认证绕过，可在受影响版本上绕过控制建立 VPN 会话。**只有启用了「认证覆盖 cookie」且证书配置特定时才暴露**；厂商 CVSS 4.0 为 7.8，5-13 发布。Unit 42 简报 **10-19 下午 4 点（PT）更新**：持续看到勒索团伙 **Spikey Scorpius（Qilin）** 与 **Tarnished Scorpius（Inc）** 尝试利用，另有公开报道把利用归到 **Settra** 勒索。入侵后的典型动作：用 RMM 双用途工具做内网侦察，经 RDP／SMB 横移，再部署凭据窃取、外泄和勒索工具。调查从 6 月初持续至今，覆盖教育、金融、医疗、制造、政府、能源、零售等十余个行业。**最值得注意的变化是直接转向虚拟化层**：一例从 VPN 网关进到 vCenter，在 ESXi 上关掉 `execInstalledOnly`，用自制工具直接对域控的 VMDK 做离线凭据导出，绕开来宾机 EDR；也见到与 Veeam **CVE-2023-27532** 串用。KEV：2026-05-29 收录、due 06-01、`knownRansomwareCampaignUse=Known`。
- 修补与缓解：升级到含修复的版本（如 12.1.7／11.2.12／11.1.15／10.2.18-h6 等，按官方表）；或给认证覆盖 cookie 改用专用证书，或关闭认证覆盖。**有成功 `gateway-connected` 事件就按事件响应处理**，并排查 vCenter／ESXi 与备份服务器。
- X 原帖：
  - https://x.com/Python_s_/status/2112319498883666277
  - https://x.com/HuginIntel/status/2112319501324656833
  - https://x.com/_Why_Noot/status/2112319509956563173
- 厂商公告：
  - https://security.paloaltonetworks.com/CVE-2026-0257
  - https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
  - https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 文章：
  - https://www.rapid7.com/blog/post/etr-rapid7-observed-exploitation-of-pan-os-globalprotect-authentication-bypass-vulnerability-cve-2026-0257/
  - https://www.infosecurity-magazine.com/news/palo-alto-vpn-vulnerability-target/
- 地址／IoC（Unit 42，PoC 公开前即 5-29 前的探测源，查 GlobalProtect 日志里的成功登录）：`23.128.228[.]6`、`104.207.144[.]154`、`146.19.216[.]119`、`146.19.216[.]120`、`146.19.216[.]125`、`179.43.172[.]213`、`185.195.232[.]139`、`198.12.106[.]60`、`202.144.192[.]47`。可疑主机 ID／设备名（任何来源 IP 的成功 `gateway-connected` 事件）：`aa:bb:cc:dd:ee:ff`、`00:11:22:33:44:55`、`WINDOWS-LAPTOP-001`、`DESKTOP-GP01`、`GP-CLIENT`。PoC 硬编码客户端值：`endpoint_os_version : Microsoft Windows 10 Pro 64-bit`、`source_user_info.domain : empty`。今天的勒索更新**未附新 IoC**。

### 2. Siemens Software Center · CVE-2026-110936（DLL 侧加载）· 在野（ClickFix），未进 KEV
Siemens ProductCERT 10-19 确认在野利用：攻击者把**正版签名**的 Siemens Software Center（3.5.8.7，会不加校验加载 DLL）和自己的 DLL 打包投递。NVD 描述：4.0.9.8 之前所有版本从不受控路径加载 DLL（10-15 发布，SSA-580366）。SecurityWeek 与 threatcluster 把它关联到 **ROMULUS** ClickFix 多载荷投递平台（Forescout 10-15 报告；rst_cloud 摘要中关联 Silver Fox、LegionLoader、RomulusLoader）。修到 **4.0.9.8**。X 上 @Pick_Analytica 提醒：签名正确不代表安全，按行为猎，别只看哈希。
- X 原帖：
  - https://x.com/Pick_Analytica/status/2112319886437519571
  - https://x.com/EduardKovacs/status/2112246772932227263
  - https://x.com/SecurityWeek/status/2112246911130550306
  - https://x.com/threatcluster/status/2112273632223215823
  - https://x.com/rst_cloud/status/2112135560517083465
- 厂商公告：https://productcert.siemens.com/news/2026/10/19/active-exploitation-of-cve-2026-110936-in-siemens-software-center/
- 文章：
  - https://www.securityweek.com/siemens-software-center-vulnerability-exploited-in-clickfix-malware-attacks/
  - https://threatcluster.io/cluster/siemens-software-center-vulnerability-exploited-in-clickfix--8e99de93
  - https://www.forescout.com/blog/romulus-analysis-of-a-new-multi-payload-clickfix-delivery-platform/
- 地址／IoC（Siemens）：活跃 C2／托管 `96.62.218[.]59`、`wizardexpensive[.]com`；已失活分发 `2.27.248[.]127`；SHA-256 `f4d7c5321bb0d1bda439304a753bcf9b467b98ca53c7e9493b9c2c3451092e4a`（AllMyBasic.msi）、`3fdcc7d7d049a89711fb31fb236940a1c5a09d899143ffd20c3c41fb1f2cf491`（archive.dll）。主机痕迹：`AppData\Local\Programs` 下出现「SM Software Provisioning Service」目录；`SiemensSoftwareCenter.exe` 同目录有 `activate.bak`／`statinfosta.DB`；`AppData\Local\FTSuite\ftc.uml`；`SiemensSoftwareCenter.exe` 由 msiexec 从 `AppData\Local\Programs` 拉起。ROMULUS（rst_cloud 摘要转 Forescout）：面板服务器 `86.109.75.7`，下载 `orbitflownetwork[.]lol/dl/J8QkZUVJgV.7z`，LegionLoader C2 `smashshape[.]com`（`/nfront.php`、`/nback.php`）。

### 3. KEV 到期追踪 · BeyondTrust＋Fortinet 今天到期／Atlassian 今起逾期
- **BeyondTrust Remote Support CVE-2026-102764**（未认证认证绕过／消息来源校验不当，厂商 CVSS 4.0 9.3，BadgerSignal 写 9.8；≤26.2.3）：due **10-19 今天**。Rapid7 确认披露前已在野。BadgerSignal 汇总 Mandiant 结论：8-29 起利用（比 10-15 披露早约 7 周），疑似中国关联的 **ARMORY CASTLE（原 UNC5221）**，投 **SAWFLY** webshell 与 **BARECLAW** 隧道，清掉 6 个日志源，持久化标记 `zz-root-persist`。处置：自建实例打 **BT26-05-RS**（适用 24.3.1～26.2.3，更老版本要先升级；SaaS 已于 10-09 修完）；先留证再清理；猎 SAWFLY／BARECLAW；**轮换盒子里保存的全部凭据与密钥**；日志外送。
- **Fortinet CVE-2025-61624**：due **10-19 今天**。SecurityWeek：**UNC5820／CL-STA-0954** 在 2024 年 9 月一次电信入侵中，先用 FortiJump **CVE-2024-47575** 进 FortiManager，再把 61624 当 0day 拿 FortiGate root，植入 ARM64 内存后门 **PeerStitch**；还用 **CVE-2024-26008** 冒充 FortiManager，导出 500+ 台受管 FortiGate 的配置。
- **Atlassian CVE-2026-21589**（Jira 未认证读 web 根目录文件）：due 10-18，**今起逾期**。
- X 原帖：
  - https://x.com/rapid7/status/2112218844077199436
  - https://x.com/BadgerSignalHQ/status/2112215597123842358
  - https://x.com/ifahimulhssn/status/2112224986312372246
  - https://x.com/2Workly/status/2112276480919216581
  - https://x.com/BursaMatus/status/2112195834611642738
  - https://x.com/SecurityWeek/status/2112141384568197412
  - https://x.com/Midas_pcl/status/2112240342439178470
- 厂商公告：
  - https://www.beyondtrust.com/trust-center/security-advisories/bt26-05
  - https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust
  - https://nvd.nist.gov/vuln/detail/CVE-2026-102764
  - https://nvd.nist.gov/vuln/detail/CVE-2025-61624
  - https://www.cisa.gov/news-events/alerts/2026/10/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 文章：
  - https://www.rapid7.com/blog/post/etr-cve-2026-102764-critical-beyondtrust-remote-support-authentication-bypass-exploited-in-the-wild/
  - https://badgersignal.com/articles/critical-beyondtrust-remote-support-authentication-bypass-cve2026102764-actively-exploited
  - https://www.darkreading.com/endpoint-security/beyondtrust-remote-support-exploited-edge-bugs
  - https://www.securityweek.com/exploited-fortinet-bug-linked-to-stealthy-fortigate-implant-in-telecom-hack/
- 地址／IoC：本窗口未见新的公开 IoC（工具名 SAWFLY／BARECLAW／PeerStitch 与 `zz-root-persist` 标记见上；哈希需看 Mandiant／Unit 42 原文，本轮未抓取）。

### 4. SiteGuard Server Edition · CVE-2026-106931 续：JPCERT/CC 发出注意唤起（未进 KEV）
JPCERT/CC 发布 **JPCERT-AT-2026-0032**：厂商确认已被利用，产品在日本国内广泛使用。受影响：Ver2.20 起，Apache／Nginx／IIS 版 8.00 Update5 之前、FreeBSD Apache／Nginx 版 7.00 Update6 之前；默认开启的统计功能开着即受影响（IIS 3.10～4.00 Update4 不受影响）。对策：升级或用厂商替换统计文件的补丁；回避：关闭统计功能。**再次强调：修补可能抹掉痕迹，先在 Web 管理界面获取「诊断信息」留证。** X 上有人指出 CVSS 4.0 8.5 是按本地、低权限前提打分。攻击者与规模仍未公开。
- X 原帖：
  - https://x.com/MalwareBibleJP/status/2112273336025886977
  - https://x.com/AzmyBlog/status/2112222904431600061
  - https://x.com/vitobotta/status/2112196170944483808
  - https://x.com/lee1981b/status/2112114659864039705
  - https://x.com/sh3ll_c0d3/status/2112214951569809584
- 厂商公告：
  - https://www.jpcert.or.jp/at/2026/at260032.html
  - https://jvn.jp/jp/JVN88474777/
  - https://eg-secure.co.jp/siteguard/news/alert-202610-1
- 地址／IoC：未见公开 IoC。

### 5. Plex2Shell 链续（CVE-2026-96652／96654／96655／96656）· 主流媒体跟进，新增矿池域名
THN、SecurityWeek、Ars Technica、SecurityAffairs 今天集中报道。THN 整理：四漏洞（SSRF → 拿 owner token → 认证后 SSRF 拉载荷 → 写入 Codecs 目录执行）串成未认证 RCE，研究者 Zach Main 7-27 报告，**Plex Media Server 1.43.3.10861（8-3）已修**；10-16 细节公开后第二天即被利用，投矿机与住宅代理 `myawesomeproxy`。新增细节：XMRig 进程名 `mylovelyminer`，矿池指向 `ota.proxystream[.]st`；同域另一子域 `global.relay.proxystream[.]st` 8 月被 Bitsight 关联到 **AISURU** DDoS／代理僵尸网络。Reddit 上多名用户报告中招。暴露面：TCP/32400。
- X 原帖：
  - https://x.com/SOCMinute/status/2112310428810236233
  - https://x.com/gettransilience/status/2112319372664672655
  - https://x.com/2Workly/status/2112310467314262455
  - https://x.com/SecurityWeek/status/2112163287689236563
  - https://x.com/securityaffairs/status/2112254148779417618
- 文章：
  - https://thehackernews.com/2026/10/hackers-exploit-plex2shell-flaws-to.html
  - https://www.securityweek.com/plex2shell-exploit-chain-weaponized-against-plex-servers-hours-after-disclosure/
  - https://arstechnica.com/security/2026/10/recently-fixed-plex-media-vulnerabilities-are-being-exploited-to-install-malware/
  - https://securityaffairs.com/201324/hacking/plex2shell-exploit-used-to-turn-vulnerable-plex-servers-into-crypto-miners.html
  - https://threatnews.transilience.cloud/api/reports/threat/mvf9bya7g1lt/pdf?v=2&save=1
- 地址／IoC（THN 汇总，前三项昨日已列）：下载源 `217.60.194[.]116`；利用来源 `91.92.40[.]202`、`176.65.139[.]228`、`45.194.92[.]222`；**新增**矿池 `ota.proxystream[.]st`；关联 `global.relay.proxystream[.]st`（AISURU）；进程名 `myawesomeproxy`、`mylovelyminer`。

### 6. F5 NGINX 带外补丁续 · CVE-2026-15176／93479／97205（媒体跟进，未在野）
BleepingComputer 今天报道 F5 的带外补丁（F5 通告日期 10-14，前几天的晚报已提到版本号）：三个严重漏洞在 `ngx_http_v3_module`（15176、97205）和 `map` 指令（93479），**都需要非默认配置**，堆溢出／UAF 导致 worker 崩溃，在 ASLR 关闭或可被绕过时可能执行代码；同批还有 95101、97629。修到 **1.31.7／1.30.6**，Plus **37.1.0.1／37.0.5.1**，Ingress Controller、Gateway Fabric、Instance Manager 同步。缓解：15176 不在 location 里用 `alias` 或 `$request_filename`；97205 关 AIO 或 SSI；93479 改用命名捕获。F5 尚未标记在野。
- X 原帖：
  - https://x.com/DailyDarkWeb/status/2112220563720868143
  - https://x.com/connect24h/status/2112319691599618248
  - https://x.com/_pksharma/status/2112288228275634491
  - https://x.com/BleepinComputer/status/2112179759543210105
- 厂商公告：
  - https://my.f5.com/manage/s/article/K000163408
  - https://nginx.org/en/security_advisories.html
- 文章：https://www.bleepingcomputer.com/news/security/f5-releases-out-of-band-patches-for-critical-nginx-vulnerabilities/
- 地址／IoC：未见公开 IoC。

### 7. 新披露／单源声称的漏洞
- **Adobe ColdFusion CVE-2026-105899（CVSS 10）**：未认证、无需交互的危险类型文件上传导致代码执行（NVD 10-13 收录，状态 Undergoing Analysis）。暂无在野报告，有 ColdFusion 的尽快补。
  - X：https://x.com/SecAlertsCo/status/2112302422974484805
  - 文章：https://secalerts.co/vulnerability/CVE-2026-105899?utm_campaign=x
- **Redis CVE-2026-66373**：NVD（7-25 收录）描述为「8.8.0 之前，在攻击者已认证且能执行 `RESTORE` 的少见情况下可 RCE」。@C2HuntersLabs 称在 8.6.4 上「确认在野」，链路为 RCE → 导出缓存凭据 → 转向数据库窃取记录 → 清痕。**单一来源，无报告链接，UNCONFIRMED**；修到 8.6.5／8.8.0，并确认 Redis 没有暴露到公网、ACL 禁 `RESTORE`。
  - X：https://x.com/C2HuntersLabs/status/2112252485230571888
- **curl CVE-2026-92392**（8.23.0 修）：上传时收到服务端 HTTP/2 `RST_STREAM`（`HTTP_1_1_REQUIRED` 或 `REFUSED_STREAM`）导致 `Curl_easy` UAF。
  - X：https://x.com/securityLab_jp/status/2112318172238086464
  - 文章：https://rocket-boys.co.jp/security-measures-lab/curl-cve-2026-92392-http2-upload-rce-8-23-0/
- **Google Agent Mesh CVE-2026-103091（CVSS 9.3）**：任何拿到其 OIDC 提供方 token 的人都会被自动注册，默认策略允许调用每个 MCP 节点上的任意工具；9-7 在 v0.1.0-alpha.9 已修，CVE 今天才公开。
  - X：https://x.com/justelite/status/2112126645792362918
  - 厂商公告：https://github.com/google/agentmesh/security/advisories/GHSA-cgmg-9xf6-rrgw
- **MariaDB CVE-2026-92262／85746／85748**：
  - X：https://x.com/CCBalert/status/2112176111761154532
  - 厂商公告：https://github.com/MariaDB/server/security/advisories/GHSA-65jj-h265-3m7h
- **VS Code CVE-2026-102851**（MSRC）：
  - X：https://x.com/cristian_le0/status/2112253783254176042
  - 厂商公告：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-102851
- **Leantime CVE-2026-85990**：
  - X：https://x.com/alex_cuciureanu/status/2112262516466208980
  - 厂商公告：https://github.com/advisories/GHSA-54mm-6729-r5wp
- **Suprema BioStar 驱动 CVE-2026-94129／94128**：
  - X：https://x.com/HugoValters/status/2112285911149089095
  - 文章：https://www.valtersit.com/cve/CVE-2026-94129/
- **Nix CVE-2026-110449／110450／110451**（Determinate Nix v3.23.2 修）：
  - X：https://x.com/DeterminateSys/status/2112261773310976502
  - 厂商公告：https://github.com/DeterminateSystems/nix-src/releases/tag/v3.23.2
- **FreeBSD 内核共享内存 TOCTOU CVE-2026-58094**（技术分析）：
  - X：https://x.com/sh3ll_c0d3/status/2112318880043368556
  - 文章：https://sh3llc0d3.com/blog/freebsd-kernel-shared-memory-vulnerability-dissecting-toctou-race-conditions-in-vm-fault-mapping-cve-2026-58094/
- **Drupal CVE-2026-108097 续**：SecurityWeek 报道 Drupal 警告「快速被利用」风险（SA-CORE-2026-014，昨日已列）。
  - X：https://x.com/SecurityWeek/status/2112209284998242623
  - 文章：https://www.securityweek.com/drupal-warns-of-fast-exploitation-risk-for-critical-core-rce-flaw/
- 地址／IoC：以上均未见公开 IoC。

### 8. 已在 KEV 的漏洞续报
- **NetScaler CVE-2026-88771＋88779**：据 X 转述 Rapid7 分析，攻击者把 88771（预认证 RCE）和 88779 的 SAML 崩溃循环串起来，**跨重启保持 root**；只打补丁不猎失陷会重演 Citrix Bleed。两条都已在 KEV（09-27、10-04 收录）。
  - X：https://x.com/HETPATELL__/status/2112315791911923942
- **AhsayCBS CVE-2026-105133／105134**（已逾期）：Rescana 分析称链路为认证绕过 → RCE，落 webshell，XMRig 伪装成 `edge.exe`；**10.3.4.0 并没有完全堵住**，要打热修并排查 web 根目录。
  - X：https://x.com/HETPATELL__/status/2112271584798912868 ；https://x.com/rst_cloud/status/2112309857315340747
  - 文章：https://www.rescana.com/post/ahsaycbs-cve-2026-105133-105134-exploited-backup-console-rce
- **Cisco Secure Email Gateway**：@stephenfewer 称 Metasploit 队列中有 3 个新模块，分别对应 76519（AMP 文件写，KEV）、76461（SQLi，KEV）、76443（SQLi）。**公开模块合入后利用门槛会进一步降低**，未修的赶紧修。
  - X：https://x.com/stephenfewer/status/2112176438178947244
  - GitHub：https://github.com/rapid7/metasploit-framework/pulls?q=is%3Apr+%22Cisco+Secure+Email+Gateway%22
- 地址／IoC：未见新的公开 IoC。

### 9. 新公开 PoC／研究（只给链接作狩猎／验证用途）
- **KVM CVE-2026-99999「非破坏性可达性」PoC**：只用合法 csum 元数据，验证来宾控制的 `NEEDS_CSUM` 状态可经 virtio-net 到达宿主机；不做内存破坏。@PaulosYibelo 解释 99999 这个编号是 Linux 维护者因影响面特意给的「奖品」。
  - X：https://x.com/pyxgun/status/2112118944085799042 ；https://x.com/PaulosYibelo/status/2112200668257665149
  - GitHub：https://github.com/shizuku198411/CVE-2026-99999-KVM-checksum-metadata-non-destructive-PoC
- **Broadcom Wi-Fi WPS 漏洞（Quentin Kaiser，Hexacon）续**：THN 今天报道。无需 Wi-Fi 密码、空口即可在 Broadcom 方案路由器上拿 root，比利时 Proximus、Orange Belgium、VOO 网关确认可利用；旧 eCos 芯片（BCM3380／3383／33834）没有可用修复，作者称「forever day」，新的 Linux 芯片（BCM3390／65xx／68xx）换用 hostapd 可修。**无 CVE、无补丁、未见在野**。缓解：关闭 WPS。
  - X：https://x.com/TheHackersNews/status/2112069383287947618 ；https://x.com/P7RIM3/status/2112314012100608017 ；https://x.com/Divinmentis/status/2112212530084921723
  - 文章：https://thehackernews.com/2026/10/unpatched-broadcom-wi-fi-flaw-lets.html
- **PortSwigger XSS 速查表更新**：新增 Safari 下用 `<select>` 绕过六种「吞噬型」标签的向量（研究向，用于测试 WAF／净化器）。
  - X：https://x.com/garethheyes/status/2112174430696722645
  - 文章：https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#byass-noscript-consume-using-select
- **@i0n1c**：用 iPhone 18 Pro（iOS 27.0）内核 coredump 研究沙箱机制，并公开询问厂商不肯分配 CVE 时怎么办。
  - X：https://x.com/i0n1c/status/2112226889712751001 ；https://x.com/i0n1c/status/2112175316923994204
- 地址／IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 1. BloodHound v9.9.0-rc1（SpecterOps）· 本窗口唯一有新 release 的监控框架
GitHub API 显示 10-19 15:28（UTC-3）发布 **v9.9.0-rc1**（候选版）。其余监控框架的最新 release：nuclei v3.11.1（8-8）、nuclei-templates v10.5.0（10-05）、Sliver v1.7.8（10-03）、emp3r0r v5.3.0（10-16，前几天已列）、NetExec v1.5.1（2-23）、Mythic v3.4.0.5、impacket 0.13.1（5-19）；Havoc 仓库没有 release。
- GitHub：https://github.com/SpecterOps/BloodHound/releases/tag/v9.9.0-rc1
- 地址／IoC：未见公开 IoC。

### 2. COM_Hijack_BOF · 用 COM 劫持做 Windows 持久化的 BOF（Cobalt Strike／Mythic）
防守侧可据此补 `HKCU\Software\Classes\CLSID` 下 `InprocServer32`／`LocalServer32` 新建与改写的检测。
- X 原帖：https://x.com/ipurple/status/2112280899652088088
- GitHub：https://github.com/bsdrip/COM_Hijack_BOF
- 地址／IoC：未见公开 IoC。

### 3. Black Sand Beacon · Linux 内存驻留 C2 信标，C 写成，支持原生内存加载 ELF BOF
仿照 Cobalt Strike 的 Windows BOF 模型，没有 Go／Rust 运行时，体积小。防守侧关注 `memfd_create`／匿名可执行映射与无文件 ELF 加载。
- X 原帖：https://x.com/yogsec/status/2112236655998550132
- GitHub：https://github.com/grisuno/blacksandbeacon
- 地址／IoC：未见公开 IoC。

### 4. Malvex · AI 驱动的恶意软件分析框架（集成 30+ 工具、Web REPL 和 MCP 服务器）
- X 原帖：https://x.com/ipurple/status/2112246043396190601
- GitHub：https://github.com/JoasASantos/Malvex
- 地址／IoC：未见公开 IoC。

### 5. 其他工具与防守资源
- **DemonLdr**（Havoc 的 UDRL，用 Crystal Palace 构建，昨日已列，今日再次扩散）：https://x.com/5mukx/status/2112242954568110258 ；GitHub：https://github.com/0xPrimo/DemonLdr
- **PhantomBuffer**（`SendMessage`＋`WM_SETTEXT` 注入绕 EDR，昨日已列）：https://x.com/ipurple/status/2112189540022587608 ；GitHub：https://github.com/TwoSevenOneT/PhantomBuffer
- **Cloudflare security-audit-skill**：开源 AI 安全审计 skill。流程是隔离的猎手找候选，再交给全新的对抗式验证者判定已确认／需验证／驳回，并用覆盖台账追踪没查完的路径。
  - X：https://x.com/AlAssaf_H/status/2112216282024059061
  - GitHub：https://github.com/cloudflare/security-audit-skill
- **NVIDIA skillspector**：扫描 AI agent skill 仓库的工具，可用 `--no-llm` 纯静态扫；依赖检查会把包名和版本发给 OSV 查 CVE。
  - X：https://x.com/KowalPrato4o/status/2112122558724047197
  - GitHub：https://github.com/NVIDIA/skillspector
- **mcp-authscan**（MCP 服务器认证扫描器）：https://x.com/Lhmisme/status/2112265015340196101 ；GitHub：https://github.com/LHMisme420/mcp-authscan
- **xalgorix**（开源的「利用验证式」自动渗透引擎，Apache-2.0）：https://x.com/xalgorix/status/2112154515675992321 ；GitHub：https://github.com/xalgorix/xalgorix
- **Anthropic-Credited-CVEs**：追踪 Anthropic「Project Glasswing」披露与补丁的仓库，帖子引用计数为 CVE 316、无 CVE 的已修 128、撤回 243。
  - X：https://x.com/liran_tal/status/2112172928343138618
  - GitHub：https://github.com/patrickmgarrity/Anthropic-Credited-CVEs
- **Datadog Security Labs：「伪造策略」操纵 Jev 评审**：在他们的测试里，提示注入检测率从约 83% 降到约 4%，同法还绕过了 LangChain 基于 Jev 的实验性工具风险评审。
  - X：https://x.com/Frichette_n/status/2112260736785195388
  - 文章：https://securitylabs.datadoghq.com/articles/jev-as-a-judge-how-counterfeit-policy-steers-jev/
- **MITRE ATT&CK v20**：新增 AI 滥用、MFA 绕过、水务攻击等条目。
  - X：https://x.com/SecurityWeek/status/2112313090029351312
  - 文章：https://www.securityweek.com/mitre-attck-v20-catalogs-ai-abuse-mfa-bypass-water-utility-attacks/
- **DFIR_Radar：BYOVD「EDR killer」应拆成四类分别检测**（单条驱动加载规则只能覆盖其中一类）：https://x.com/DFIR_Radar/status/2112167279970373834
- 地址／IoC：以上均未见公开 IoC。

## APT / Malware 分析

### 1. Coruna／DarkSword 系 iOS 漏洞利用套件挂在被入侵的正常网店上（今日最大事件）
**发现经过**：@malwrhunterteam 先在意大利化妆品站 estrosa[.]it 发现可疑 `group.html`，随后连发确认西班牙马德里萨克斯风专卖店 saxtienda[.]com、智利老牌电脑游戏店 v2[.]cl、法国 Padirac 溶洞景区官方网店 boutique.gouffre-de-padirac[.]com 等都挂着同一套 DarkSword 相关套件，表示「多到处理不过来」。@vxunderground 将样本传到 MalwareBazaar，称「在野的 Coruna EK 很罕见」，推测目标为 iOS 18.1.1、18.6.0～18.6.2（代码里直接写着 `stage1_rce`）；另转述 @AelsMartin 又找到 183 个相关对象（帖子被截断）。
**技术要点（防守视角）**：
- 路径是攻击者**拼错**的 `/js/analystic/assets/js/group.html`（不是 analytics；最早帖写错一个字母，按错的路径会 404）。
- @0xDanielLopez：同一 `group.html` 出现在 **40+ 域名**，受害者为西班牙、法国、意大利、智利、瑞典、阿联酋的 PrestaShop／WordPress 网店。注入脚本在页面加载 1.5 秒后插隐藏 iframe；`group.html` 判断是否为 iPhone／iPad／iPod，并按 iOS 版本挑选利用 JS（引用 18.6.x）；仅对 iOS UA 回传信标，POST `{"k":1,"n":<访问的主机名>}`，其中 `hx` 与 `POST` 字符串做了 XOR 66 编码。
- @Darkfibr3 完整拆解：**不是一套而是两套**，iOS 18 以下走 Coruna 系，iOS 18 及以上走 DarkSword／P7；给 18.6 系列下发的 85 字节模块与 iVerify 公开的 `rce_module_18.6.js` 逐字节相同（SHA-256 一致），模块命名用同一种加盐 SHA-256 方案、只换了盐，属于「带构建器的衍生分支」。链路：WebKit RCE → GPU 进程沙箱逃逸 → mediaplaybackd 用户态提权 → 内核提权 → SpringBoard 植入；窃取钥匙串数据库与 keybag、**34 个钱包 App**、照片、备忘录、App 数据；自定义 XOR 通信；**只驻留内存，本构建无持久化**。iOS 18 以下分支更深：原生 Mach-O dylib，再接 ChaCha20／LZMA2 清单（magic `0xf00dbeef`）和另外 19 个阶段（采到 3 个：通讯录、Safari 书签、诊断信息）。规模：公开遥测 **124 个域名**、**6 个路径确认的受害站**、一个 19 域名的「账户合规」诱饵群。已向 ThreatFox 提交 35 条 IoC、向 MalwareBazaar 提交 33 个样本（25 个已索引）。归因：暂不明。
- @duniel_pls：`PE_BUILD = "20260914-aks40"`，构建较新；目前看到最新的目标是 iPhone17,5（16e）、OS build 22G100（18.6.2），与 iVerify／Google 在 DarkSword 中看到的一致。
- @tmechen_：有仓库称 DarkSword 已加入 iOS 26 能力，不再限于 18.4～18.7（**UNCONFIRMED**；仓库链接仅供核对，不转载内容）。
- 相关基础设施（@malwrhunterteam）：`darksword.msxfweb[.]net/gooll/gooll.html` 页面上有最近（含昨天）的调试类留言，出现「coruna-loot」字样；另有标题为「登录 - iOS漏洞后台」「iOS 安全漏洞研究与管理平台」的面板 `admin.msxf[.]info`。
- 背景：NetAskari 10-14 的「Divine Seagull（神的海鸥）」报告称 Coruna／DarkSword 框架仍在中文圈运营者之间扩散，有人尝试扩展到 iOS 26.1，但 @K_Ichida 摘要认为「尚未到实用阶段」。
**防守建议**：iOS／iPadOS 升到最新（DarkSword 所用漏洞 Apple 已修大部分），高风险人员开锁定模式；Web 代理／DNS 封信标域名，并在网站侧检索 `/js/analystic/` 路径；**电商站运营者**检查 PrestaShop／WordPress 主题与插件里的注入脚本。**受害站是不知情的托管方：封路径，别封商家。**
- X 原帖：
  - https://x.com/malwrhunterteam/status/2112230048518537237
  - https://x.com/malwrhunterteam/status/2112234906248003940
  - https://x.com/malwrhunterteam/status/2112242866064118197
  - https://x.com/malwrhunterteam/status/2112253211167875458
  - https://x.com/malwrhunterteam/status/2112307135849644477
  - https://x.com/malwrhunterteam/status/2112309056203354521
  - https://x.com/vxunderground/status/2112234562805739834
  - https://x.com/vxunderground/status/2112234707144368219
  - https://x.com/vxunderground/status/2112236075557003376
  - https://x.com/vxunderground/status/2112264702357110795
  - https://x.com/vxunderground/status/2112265350075277595
  - https://x.com/0xDanielLopez/status/2112290363540938907
  - https://x.com/Darkfibr3/status/2112285287564861797
  - https://x.com/Darkfibr3/status/2112266692814680572
  - https://x.com/duniel_pls/status/2112286937369190459
  - https://x.com/tmechen_/status/2112312324237271062
  - https://x.com/K_Ichida/status/2112318878860685516
- GitHub（仅供核对）：https://github.com/htimesnine/DarkSword-RCE
- 样本库：https://bazaar.abuse.ch/sample/33d60d42472a83d0d2cf4ee6640c615313c29b18ce1e8ab06e41f4bba558a34b/
- 文章：
  - https://www.iverify.com/blog/darksword-ios-exploit-kit-explained
  - https://netaskari.substack.com/p/divine-seagull-coruna-darksword-expansion
- 地址／IoC：信标 `btrf36[.]cc/hx`、`ypnfeo[.]cc/hx`；路径 `/js/analystic/assets/js/group.html`；运营侧 `darksword.msxfweb[.]net/gooll/gooll.html`、`admin.msxf[.]info`；SHA-256 `b4290d69fbb099f72f0b7ebc5fdb1211db0810f79372b871229746027d23f52c`（group.html）、`2e443833dd58278d094acda2067a43cae1e88cbdf3902d7515776ab42f41b7e8`（b8def7dab9dd9ad8.js，loader）、`df86db89f7f965fc117d4c14b722d3d02f1d1de5c6ec216bb59fcf2736374caa`（8150b44e89f06890.js，worker）、`3196034ef1196c9151395859019674e14e3c06e3fdbf230c7e0d0c5f6211824a`（a13e3e4525e28ff8.js，exploit／offsets）、`d70f5b8ec6359ad5c22acb628a7c7ec81c8d549869afa7f96a377e52879a6642`（a8c3f01e6b47d295.js，beacon）、`33d60d42472a83d0d2cf4ee6640c615313c29b18ce1e8ab06e41f4bba558a34b`（Bazaar 套件样本）；构建标记 `PE_BUILD = "20260914-aks40"`；清单 magic `0xf00dbeef`。被挂马站（不知情的托管方，仅供排查，勿封商家）：estrosa[.]it、saxtienda[.]com、v2[.]cl、boutique.gouffre-de-padirac[.]com。

### 2. AOMEI Backupper 更新服务器被篡改（UNC7017）· Google／ManageEngine 完整报告与 IoC（续 10-16）
Google Threat Intelligence Group（GTIG）／Mandiant 与 ManageEngine 今天发布报告：**UNC7017** 在 4–7 月间篡改 AOMEI 自营更新基础设施上的配置文件（`www2.aomeisoftware.com/download/abpopup/down_html.ini`、`account.aomeitech.com/Notifycfg.ini`）。已知三个窗口，**每次只有约 5～10 分钟**：5-28 05:40–05:50、7-16 08:33–08:39、7-20 10:35–10:40（UTC）。软件按正常流程拉到被改的配置后，执行 **CROSSROAD** 下载器，再落 **SHINYROAD** 后门（侧加载 Radmin）和 **ADAPTAGENT**（Adaptix C2）；还用 WebDAV 弹窗窃取 NTLM。受害国家包括美国、澳大利亚、印度、新加坡、西班牙、瑞士。ManageEngine 6-7 就通知过 AOMEI，AOMEI 起初称「传输途中被篡改」，研究者不同意；AOMEI 现称 CTO 正在牵头调查。**服务器侧修复不会清除已装的后门**：查计划任务、AOMEI 安装目录里多出的可执行文件，以及到下列基础设施的连接。
- X 原帖：
  - https://x.com/BleepinComputer/status/2112267851188801677
  - https://x.com/xbhaveshverma/status/2112234825771827392
  - https://x.com/Dinosn/status/2112192957214285988
- 厂商／研究报告：
  - https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering
  - https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html
- 文章：https://www.bleepingcomputer.com/news/security/hackers-hijack-aomei-update-servers-to-secretly-spread-malware/
- 地址／IoC：`8.210.84[.]56`、`serv.oss-cn-hongkong[.]aliyuncs.com`、`storage-data[.]com` 下的主机名；被篡改的配置文件 `down_html.ini`、`Notifycfg.ini`（URL 见上）。完整哈希见 Google／ManageEngine 原文。

### 3. Rank Math PRO 3.0.123 后门续（报道中的 CVE-2026-111862，CVSS 9.8）
10-15 20:02 UTC 到 10-16 07:12 UTC 约 11 小时内下载的 3.0.123 带后门，会泄露数据库凭据、云密钥和 SSH 密钥；**停用插件不能解决问题，恶意代码会重建后门**；干净版本 3.0.124，但升级本身不清除威胁，装过的站要按已失陷处理。
- X 原帖：
  - https://x.com/DFIR_Radar/status/2112318366048235660
  - https://x.com/TheHackersNews/status/2112219875083186264
  - https://x.com/elgerx/status/2112162823375552796
  - https://x.com/BleepinComputer/status/2112293995149672527
  - https://x.com/SecurityWeek/status/2112202789702991986
- 厂商公告：https://rankmath.com/kb/pro-3-0-123-security-incident/
- 文章：
  - https://www.bleepingcomputer.com/news/security/wordpress-seo-plugin-rank-math-compromised-to-backdoor-websites/
  - https://www.securityweek.com/rank-math-pro-wordpress-plugin-compromised-in-supply-chain-attack/
- 地址／IoC（与 10-17 报告一致）：`rank1cdn[.]com`；文件 `wp-includes/class-wp-cache-util.php`；管理员用户名前缀 `wpsupport_`、邮箱域 `@wp-mail[.]net`；option `_np5pvf754c`；cron 标记 `ms6v46`；XOR 键 `xmmqhn`；样本名 `cache-preloader-fff033 (1).php`。

### 4. GhostAction 新阶段：`my-github[.]com` 钓鱼＋自动完成 GitHub OAuth 设备码授权（THN／OpenSourceMalware）
THN 报道：GhostAction 已在 94 个被控 GitHub 仓库里植入伪装成字体的窃密程序（在 VS Code 打开项目时运行）。新阶段是 10-09 注册 `my-github[.]com`，指向与外泄端相同的 `193.32.204[.]199`，当天就用 `noreply@my-github[.]com` 冒充 GitHub 安全提醒（「莫斯科新登录」）钓开源维护者。钓鱼页做反向代理，截获密码与 2FA，并注入 JS **自动走完 GitHub OAuth 设备码授权**（权限范围 `repo`、`workflow`、`read:org`），受害者不需要输入设备码，也不用确认授权；token 外送到 `my-github[.]com` 的 TCP/8443。`my-gitlab[.]com` 命名相近，但研究者称目前没有证据把它和 GhostAction 直接关联。
- X 原帖：
  - https://x.com/TheHackersNews/status/2112168719850029198
  - https://x.com/Dinosn/status/2112192774586200435
- 文章：https://thehackernews.com/2026/10/ghostaction-attackers-plant-credential.html
- 地址／IoC：`my-github[.]com`、`193.32.204[.]199`（含 TCP/8443）、发件人 `noreply@my-github[.]com`；可疑 OAuth scope 组合 `repo`＋`workflow`＋`read:org`。`my-gitlab[.]com` 仅作 pivot 线索，未确认关联。

### 5. 假 Web3 加速器「Apex Accelerator」（Elastic：REF8801）· npm 包投 Win 窃密木马＋macOS 后门
以投资和免费 AI 额度为诱饵，盯上加密创业者与钱包、行情工具开发者，让他们运行「尽调工具」。npm 包 `@apexacc/cli`、`@apexacc/audit`（声称是 18 个工具的 MCP 服务器），发布者 `apexaccelerator`，GitHub 账号 `apexaccs`。同时篡改一个合法 coding agent，让模型请求走攻击者的服务；审计工具会生成伪造的安全发现。7 月 SafeDep 披露过的同一行动包：`@apexfdn/apex`、`@copilot-mcp/apex`、`@apexfdn/copilot-mcp`（投 AMOS）。代码提交历史里有俄语注释，归因不足。
- X 原帖：
  - https://x.com/TheHackersNews/status/2112123909063491916
  - https://x.com/Dinosn/status/2112166337132818533
- 文章：https://thehackernews.com/2026/10/fake-web3-accelerator-uses-npm-packages.html
- 地址／IoC：npm 包 `@apexacc/cli`、`@apexacc/audit`、`@apexfdn/apex`、`@copilot-mcp/apex`、`@apexfdn/copilot-mcp`；域名 `apexaccs[.]org`、`apexfdn[.]xyz`；macOS 伪装名 `com.apple.system.loader`。

### 6. Citizen Lab：塞尔维亚贝尔格莱德大学校长被 Pegasus 零点击感染（选举前 6 天）
Citizen Lab 与 SHARE Foundation 高置信度确认，校长 Vladan Đokić 的 iPhone 在 2026 年被 NSO Pegasus 感染，**零点击**；他曾拒绝配合政府打压学生，3-31 办公室被搜查。另一人是前有组织犯罪检察署助理检察官 Rade Bajić（「川普大厦」案），收到 Apple 威胁通知。塞尔维亚公开已知的受害公民社会人士增至至少 16 人；10-25 提前举行议会选举。
- X 原帖：
  - https://x.com/jsrailton/status/2112133454238204358
  - https://x.com/TheRecord_Media/status/2112258831971463199
- 文章：
  - https://citizenlab.ca/research/pegasus-spyware-serbian-pro-democracy/
  - https://therecord.media/serbia-spyware-pegasus-elections
- 地址／IoC：未见公开 IoC。

### 7. 其他威胁报告（rst_cloud 摘要等）
- **Kimsuky（APT-C-55）多路径投递**：三条投递路径，主要打韩国金融、科研、软件开发，诱饵有韩、日、越、德、英文：钓鱼邮件带恶意 LNK、伪装快捷方式执行 PowerShell，以及**投毒一个克隆的 Python 仓库（供应链）**；用复制出来的 `certutil.exe`、改名的 `curl.exe` 落地，组件放在公共视频目录。报告列了 IoC 计数（文件 11、URL 2、哈希 6、域名 3、邮箱 14），本轮没有抓原文。
  - X：https://x.com/rst_cloud/status/2112317465774489638
  - 原文：https://mp.weixin.qq.com/s/LkX7gqz6uxyYFPHP9qJgBA
- **Black Hawk Android RAT（STAR Labs）**：9-15 至 10-16 出现 64 个变种，冒充日本税务、银行、积分、电商、通讯、交友、流媒体、投资 App；加壳用 `libsa` XOR 壳或开源 `nmmp` VM；聚类特征：组件 `Wv`／`Bv`／`Ir`／`MainActivity`、`REQUEST_INSTALL_PACKAGES` 权限、自定义 `INSTALL_COMPLETE` 广播。
  - X：https://x.com/rst_cloud/status/2112143145546678717
  - 文章：https://starlabs.sg/blog/2026/10-two-hawks-in-a-pod-one-android-rat-behind-a-flock-of-fake-japanese-brands/
- **Flax Typhoon／自动化＋人工混合入侵（ASD 等联合通告 AA26-281A，10-08）**：rst_cloud 今日摘要。
  - X：https://x.com/rst_cloud/status/2112165898769314063
  - 厂商公告：https://www.cyber.gov.au/advisory/chinese-government-linked-cyber-threat-actors-combine-automated-and-hands-on-hacking-tools-to-steal-sensitive-data
- **Overlord Go RAT 经 VHDX 投递（Joe Sandbox）**：伪装成马来西亚 IRBM／LHDN 认证电子发票，链路为 ZIP → VHDX → 假 PDF 快捷方式（LNK）→ 改名的微软辅助功能程序侧加载 DLL → 取回加密载荷 → 注入 `RuntimeBroker.exe`。C2 交互与数据窃取尚未确认。检测要点：别只扫 ZIP，要检查嵌套 VHDX 与挂载卷上的执行。
  - X：https://x.com/joe4security/status/2112281136667726245
  - 报告：https://www.joesandbox.com/joereverser/analysis/09b38686-f9b1-4f68-8cfd-d44c5a203b55/download?type=reports&report=html
- **TradingView 冒充页 ClickFix（Mac 一行命令，脚本不落盘执行；同站也发 Windows 窃密木马）**：
  - X：https://x.com/MalwareBibleJP/status/2112239109448323336
  - 文章：https://github.com/samuelscheit/malware-analysis/blob/main/ktmfoundation.org/writeup.md
- **「Fort Vpn(Ip filter).zip」假 FortiClient 投放器（韩国，@malwrhunterteam）**：包里有正版 `FortiClientMiniSetup-Windows-x64-Enterprise-7.4.3.exe` 和可疑的 `forti_ipfilter 7.4.2.exe`，后者 PDB 为 `E:\dropper_Cpp\dropper\dropper\x64\Release\dropper.pdb`；@smica83 已上传 ZIP 和下一阶段样本到 Bazaar。
  - X：https://x.com/malwrhunterteam/status/2112280401536233938 ；https://x.com/smica83/status/2112281267362558279 ；https://x.com/malwrhunterteam/status/2112286183208497491
  - 样本库：https://bazaar.abuse.ch/sample/a7588b11762a3adf7ed383a384d2d6921b0081354c4672a1c3bf3b865044845e/
- **WKLP Python 窃密木马（@synfinner）**：两个构建相隔约一周，8.9.1（9-26）用 Discord API＋bot token，9.1.0（10-03）改用专用中继 `relay[.]wklp-searcher[.]xyz`；都由一个 CS2 游戏覆盖层程序投放。
  - X：https://x.com/synfinner/status/2112240996914434252
- **公开暴露的攻击者工具目录（etugen）**：`167[.]88.172.3` 上有约 1 GB 存档，含加密钱包吸取脚本、MCP DBHub RCE 工具、回连 `153[.]75.82.143` 的植入物，以及韩文笔记。
  - X：https://x.com/etugenio/status/2112273864499548582
  - 文章：https://app.etugen.io/trashpile/167.88.172.3
- **macOS 家族**：Symantec GhostProfile 防护公告 https://www.broadcom.com/support/security-center/protection-bulletin/ghostprofile-macos-malware （X：https://x.com/threatintel/status/2112199370330546522 ）；objective-see「Heartbreaker」分析 https://objective-see.org/blog/blog_0x8A.html （X：https://x.com/elcerny/status/2112127663997669793 ）。
- **窃密木马情报**：Threadlinqs 称 GlorySprout 的随机数缺陷导致 RC4 密钥固定，防守方可解密其 C2 流量 https://intel.threadlinqs.com/threat/TL-2026-3862 （X：https://x.com/threadlinqs/status/2112083281374060558 ）；Meduza Stealer 概览 https://intel.threadlinqs.com/threat/TL-2026-3864 （X：https://x.com/threadlinqs/status/2112091580588802092 ）。
- **J4ck3LSyN 恶意软件逆向写作**（含样本、反编译、C2 重放与 IoC）：https://jackalsyn.com/posts/malAnalysisAgeAndYorkshire.html （X：https://x.com/J4ck3LSyN/status/2112305199360483733 ）
- **GMO 网络安全 by Ierae**：在一起针对日本企业的入侵中，确认攻击源基础设施使用了中国工程师开发的 AI 自主渗透测试系统「ARTEX」（X 转述，未附链接）：https://x.com/MalwareBibleJP/status/2112306301711822930
- **vxunderground 的 13 阶段「神秘载荷」**（窗口开头，推测为 TAG-150，未公开细节）：https://x.com/vxunderground/status/2111963222131552719 ；https://x.com/vxunderground/status/2111976944992756153
- 地址／IoC：见各条与下方汇总；Kimsuky、Black Hawk、GhostProfile、Heartbreaker 本轮未抓原文 IoC。

### 8. 零散 IoC 投放（猎人账号，单源，UNCONFIRMED）
- Turla（标签）：`103[.]31[.]250[.]254`：https://x.com/phatomcandle/status/2112197084510101598
- Omega RAT C2：`102.220.163.36:9090`：https://x.com/Fact_Finder03/status/2112225654947406029
- Tripaul C2：`31.56.19.150`：https://x.com/Fact_Finder03/status/2112249926851707381
- Monoxide C2：`191.217.250.30`、`monoxide.vip`：https://x.com/Fact_Finder03/status/2112241115885600798

### 9. 入侵／泄露声称（全部 UNCONFIRMED／未验证，除非注明厂商自述）
- **Ahold Delhaize**（厂商自述）：网络攻击导致美欧多数品牌系统下线：https://therecord.media/ahold-delhaize-cyberattack-grocery （X：https://x.com/TheRecord_Media/status/2112227850162143626 ）
- **Bullhorn**（厂商自述）：招聘平台下线以遏制攻击：https://www.bleepingcomputer.com/news/security/bullhorn-takes-staffing-platform-offline-to-contain-cyberattack/ （X：https://x.com/BleepinComputer/status/2112255325487210775 ）
- **Nikkei**：一个月内第三次泄露，180 万条：https://www.bleepingcomputer.com/news/security/nikkei-discloses-third-data-breach-in-a-month-18m-records-exposed/ （X：https://x.com/BleepinComputer/status/2112300264656871607 ）
- **FirstVDS（俄罗斯主机商）**：攻击者利用 ISPsystem **VMmanager 6** 漏洞，以只读方式挂载客户虚拟机磁盘，拷走密码、云凭据、配置和加密钱包，**虚拟机内不留痕迹**；漏洞还没完全修好，厂商建议在下一批更新前不要恢复管理界面访问：https://therecord.media/russia-cyberattack-firstvds-cloud （X：https://x.com/TheRecord_Media/status/2112154430519029771 ）
- **日本单日多起**（MalwareBibleJP 汇总）：H2O 旗下阪急阪神百貨店约 126 万人、E-Store「ショップサーブ」约 2335.6 万人（https://www.yomiuri.co.jp/national/20261019-GYT1T00368/ ；X：https://x.com/MalwareBibleJP/status/2112246155568701525 ）；Nifty、Furusato Choice、Joshin、足利市（X：https://x.com/MalwareBibleJP/status/2112292460403835321 ）；JETRO 743 条（https://www.jetro.go.jp/ ；X：https://x.com/MalwareBibleJP/status/2112235116085018736 ）；JFA-Passport 部分功能停用（https://www.jfa.jp/news/00036934/ ；X：https://x.com/MalwareBibleJP/status/2112282897273266481 ）；楽待 10-09～11 遭不正登录（https://rakumachi.co.jp/20261019 ；X：https://x.com/MalwareBibleJP/status/2112231811103502358 ）。Trend Micro 称日本 1–9 月公开事件 607 起，已超去年全年（https://www.yomiuri.co.jp/economy/20261019-GYT1T00305/ ）；自民党拟提议设「网络紧急事态」政府本部（https://www.nikkei.com/article/DGXZQOUA194PX0Z11C26A0000000/ ）。
- **Krebs：执法怀疑某美国赎金谈判公司高管参与运营 ShinyHunters 受害者勒索站**；被捕谈判人 Dubrovsky 知道 ShinyHunters 偷了 FBI 数据却没报告：https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/ （X：https://x.com/KimZetter/status/2112233413327343886 ；https://x.com/Dinosn/status/2112191822193721396 ）
- **Qilin 声称**：GardaWorld（https://x.com/ThreatAtlas/status/2112320363157758150 ）、Toyota Canarias（https://x.com/intels_daily/status/2112311267037684047 ）。
- **续报**：OpenCode 控制台泄露（约 1.4% 用户的 OpenAI／Anthropic／Google API key 可能外泄）https://thehackernews.com/2026/10/opencode-console-breach-may-have.html 、https://www.bleepingcomputer.com/news/security/opencode-hack-exposes-api-keys-amid-ai-distillation-attacks/ （X：https://x.com/TheHackersNews/status/2112063372753883284 ）；ConnectWise 暂停云服务 https://www.securityweek.com/connectwise-suspends-cloud-services-in-response-to-cyberattack/ （X：https://x.com/SecurityWeek/status/2112171789422112908 ）；Check Point 10-19 周报（CenterPoint Energy 100 万+、Burger King Japan 1118 万、法国超市冷链控制器被改温、LiteLLM CVE-2026-35029／59823）https://research.checkpoint.com/2026/19th-october-threat-intelligence-report/ （X：https://x.com/Dinosn/status/2112212848122433635 ）。
- 地址／IoC：未见公开 IoC。

## 地址／IoC 汇总

> 全部原样抄录自来源，已去武装（`[.]`）的保持原样；单源条目标 UNCONFIRMED。**只用于检测与封堵。**

| 关联 | 类型 | 指标 | 来源 |
|---|---|---|---|
| Coruna／DarkSword iOS 套件 | 信标 | `btrf36[.]cc/hx`、`ypnfeo[.]cc/hx` | @0xDanielLopez |
| Coruna／DarkSword | 路径 | `/js/analystic/assets/js/group.html` | @0xDanielLopez／@Darkfibr3 |
| Coruna／DarkSword | 运营侧 | `darksword.msxfweb[.]net/gooll/gooll.html`、`admin.msxf[.]info` | @malwrhunterteam |
| Coruna／DarkSword | SHA-256 | `b4290d69fbb099f72f0b7ebc5fdb1211db0810f79372b871229746027d23f52c`（group.html） | @0xDanielLopez |
| Coruna／DarkSword | SHA-256 | `2e443833dd58278d094acda2067a43cae1e88cbdf3902d7515776ab42f41b7e8`（loader） | @0xDanielLopez |
| Coruna／DarkSword | SHA-256 | `df86db89f7f965fc117d4c14b722d3d02f1d1de5c6ec216bb59fcf2736374caa`（worker） | @0xDanielLopez |
| Coruna／DarkSword | SHA-256 | `3196034ef1196c9151395859019674e14e3c06e3fdbf230c7e0d0c5f6211824a`（exploit／offsets） | @0xDanielLopez |
| Coruna／DarkSword | SHA-256 | `d70f5b8ec6359ad5c22acb628a7c7ec81c8d549869afa7f96a377e52879a6642`（beacon） | @0xDanielLopez |
| Coruna／DarkSword | SHA-256 | `33d60d42472a83d0d2cf4ee6640c615313c29b18ce1e8ab06e41f4bba558a34b`（Bazaar） | @vxunderground |
| Coruna／DarkSword | 被挂马站（勿封商家） | estrosa[.]it、saxtienda[.]com、v2[.]cl、boutique.gouffre-de-padirac[.]com | @malwrhunterteam |
| PAN-OS 0257（5-29 前探测） | IP | `23.128.228[.]6`、`104.207.144[.]154`、`146.19.216[.]119`、`146.19.216[.]120`、`146.19.216[.]125`、`179.43.172[.]213`、`185.195.232[.]139`、`198.12.106[.]60`、`202.144.192[.]47` | Unit 42 |
| PAN-OS 0257 | 主机 ID／设备名 | `aa:bb:cc:dd:ee:ff`、`00:11:22:33:44:55`、`WINDOWS-LAPTOP-001`、`DESKTOP-GP01`、`GP-CLIENT` | Unit 42 |
| Siemens 110936／Romulus | C2／托管 | `96.62.218[.]59`、`wizardexpensive[.]com`；失活分发 `2.27.248[.]127` | Siemens ProductCERT |
| Siemens 110936 | SHA-256 | `f4d7c5321bb0d1bda439304a753bcf9b467b98ca53c7e9493b9c2c3451092e4a`（AllMyBasic.msi）、`3fdcc7d7d049a89711fb31fb236940a1c5a09d899143ffd20c3c41fb1f2cf491`（archive.dll） | Siemens ProductCERT |
| ROMULUS | 面板／下载／C2 | `86.109.75.7`；`orbitflownetwork[.]lol/dl/J8QkZUVJgV.7z`；`smashshape[.]com`（`/nfront.php`、`/nback.php`） | Forescout（rst_cloud 摘要） |
| AOMEI／UNC7017 | IP／域名 | `8.210.84[.]56`、`serv.oss-cn-hongkong[.]aliyuncs.com`、`storage-data[.]com` 子域 | Google／ManageEngine（BleepingComputer） |
| Plex2Shell | IP | `217.60.194[.]116`（下载）、`91.92.40[.]202`、`176.65.139[.]228`、`45.194.92[.]222` | THN |
| Plex2Shell | 域名 | `ota.proxystream[.]st`（矿池，新增）、`global.relay.proxystream[.]st`（AISURU 关联） | THN |
| Rank Math PRO 3.0.123 | 域名／痕迹 | `rank1cdn[.]com`、`wp-includes/class-wp-cache-util.php`、`wpsupport_*`、`@wp-mail[.]net`、`_np5pvf754c`、`ms6v46` | Rank Math／BleepingComputer |
| GhostAction | 域名／IP | `my-github[.]com`、`193.32.204[.]199`（TCP/8443）、`noreply@my-github[.]com` | THN／OpenSourceMalware |
| Apex Accelerator（REF8801） | npm／域名 | `@apexacc/cli`、`@apexacc/audit`、`@apexfdn/apex`、`@copilot-mcp/apex`、`@apexfdn/copilot-mcp`；`apexaccs[.]org`、`apexfdn[.]xyz` | Elastic／THN |
| Overlord Go RAT | URL／文件 | `hxxps://lhdn[.]tos-cn-hongkong[.]volces[.]com/e-Invoice_INV91074_IRBM_Validated_Tenaga_Systems_Sdn_Bhd_2026-10-15.zip`；`e-Invoice_INV91074_IRBM_Validated_Tenaga_Systems_Sdn_Bhd_2026-10-15.vhdx` | Joe Sandbox |
| Fort Vpn 投放器 | SHA-256／PDB | `a7588b11762a3adf7ed383a384d2d6921b0081354c4672a1c3bf3b865044845e`（ZIP）；`E:\dropper_Cpp\dropper\dropper\x64\Release\dropper.pdb` | @smica83／@malwrhunterteam |
| WKLP 窃密木马 | C2 | `relay[.]wklp-searcher[.]xyz` | @synfinner |
| etugen 暴露目录 | IP | `167[.]88.172.3`（工具目录）、`153[.]75.82.143`（植入物 C2） | etugen |
| Turla（标签，UNCONFIRMED） | IP | `103[.]31[.]250[.]254` | @phatomcandle |
| Omega RAT（UNCONFIRMED） | IP:端口 | `102.220.163.36:9090` | @Fact_Finder03 |
| Tripaul（UNCONFIRMED） | IP | `31.56.19.150` | @Fact_Finder03 |
| Monoxide（UNCONFIRMED） | IP／域名 | `191.217.250.30`、`monoxide.vip` | @Fact_Finder03 |

其余条目（BeyondTrust 102764、Fortinet 61624、Atlassian 21589、SiteGuard 106931、NGINX、ColdFusion、Redis、curl、Agent Mesh、MariaDB、VS Code、Nix、BioStar、FreeBSD、NetScaler、Ahsay、Cisco SEG、KVM 99999、Broadcom WPS、Pegasus、各工具仓库、泄露类）：**未见公开 IoC**（或 IoC 只在本轮未抓取的原文中）。

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


**今日 LWiS 交叉要点**：List 成员里贡献最多的是 @vxunderground（Coruna EK、13 阶段载荷）、@Dinosn（AOMEI、GhostAction、Krebs、Web3 npm、Check Point 周报）、@ipurple（COM_Hijack_BOF、Malvex、PhantomBuffer）、@garethheyes（XSS 速查表）、@i0n1c（iPhone 18 Pro 内核 coredump）、@Frichette_n（Datadog Jev）、@KimZetter（Krebs／ShinyHunters）、@PaulosYibelo（KVM 99999 编号由来）。blogs.txt 里命中的高信号源：Unit 42（`https://unit42.paloaltonetworks.com/`，今日更新 0257 简报）、Krebs on Security（`https://krebsonsecurity.com/`）、PortSwigger（`https://portswigger.net/daily-swig`）、Elastic Security Research（`https://elastic.github.io/security-research/`，REF8801 的原始研究方）。Risky Business 首页与 tl;dr sec 归档页均可访问；tl;dr sec 最新一期为 **#350「Reverse Engineer Anything, Tracking AI-integrated Malware, Test-driving Jev」**，与今日 Datadog Jev 研究同题。

## 来源搜索 URL

- A（CVE／0day／PoC）：https://x.com/search?q=%28CVE-2026%20OR%200day%20OR%20zero-day%20OR%20%22actively%20exploited%22%20OR%20PoC%29%20-is%3Aretweet&f=live
- A 去噪：https://x.com/search?q=%28CVE-2026%20OR%20CVE-2025%29%20%28exploit%20OR%20exploited%20OR%20PoC%20OR%20RCE%20OR%20patch%20OR%20advisory%20OR%20KEV%29%20-is%3Aretweet&f=live
- A 在野：https://x.com/search?q=%28%22zero-day%22%20OR%200day%20OR%20%22in%20the%20wild%22%20OR%20%22actively%20exploited%22%29%20%28vulnerability%20OR%20exploit%20OR%20CVE%20OR%20patch%29%20-is%3Aretweet%20-is%3Areply&f=live
- B（GitHub 红队／C2）：https://x.com/search?q=url%3Agithub.com%20%28C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20PoC%20OR%20exploit%20OR%20BOF%20OR%20EDR%29%20-is%3Aretweet&f=live
- B 补充：https://x.com/search?q=url%3Agithub.com%20%28%22red%20team%22%20OR%20implant%20OR%20%22post-exploitation%22%20OR%20pentest%20OR%20loader%20OR%20Sliver%20OR%20Havoc%29%20-is%3Aretweet&f=live
- C（威胁报告）：https://x.com/search?q=%28%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20OR%20infostealer%20OR%20backdoor%29%20-is%3Aretweet&f=live
- C IoC：https://x.com/search?q=%28malware%20OR%20infostealer%20OR%20RAT%20OR%20backdoor%20OR%20ransomware%20OR%20loader%29%20%28IOC%20OR%20C2%20OR%20sha256%20OR%20%22threat%20report%22%29%20-is%3Aretweet%20-is%3Areply&f=live
- 专题（KEV 到期项／续报）：https://x.com/search?q=SiteGuard%20OR%20plex2shell%20OR%20%22CVE-2026-102764%22%20OR%20%22CVE-2025-61624%22%20OR%20%22CVE-2026-0257%22%20OR%20%22CVE-2026-110936%22%20OR%20%22CVE-2026-21589%22%20OR%20%22CVE-2026-106931%22%20OR%20%22blender-ai-mcp%22&f=live
- 专题（Coruna／DarkSword）：https://x.com/search?q=%28Coruna%20OR%20DarkSword%20OR%20estrosa%20OR%20%22exploit%20kit%22%29%20%28iOS%20OR%20iPhone%20OR%20malwrhunterteam%20OR%20exploit%29&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
