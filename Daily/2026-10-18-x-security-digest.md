# X 安全情报晚报 · 2026-10-18

> 搜集窗口：圣地亚哥时间 **2026-10-17 20:10 至 2026-10-18 20:10**（America/Santiago／UTC-3，**24 小时**，接昨晚窗口，没有缺口）。X 搜索参数：`start_time=2026-10-17T23:10:00Z`，`end_time=2026-10-18T23:10:00Z`。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`，Latest／recency 排序）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** 本轮接口有回传 entities，多数 t.co 已直接展开，其余用 HTTP 跳转补展开；纯图片／媒体 t.co 不列。A／B／C 三类各跑原始与去噪查询，A 类另做翻页与「凌晨时段」切片查询；LWiS List 500 成员分 10 段 `from:` 批次全量翻查（其中 2 段第一次遇到 X 端 429 限流，重试成功）；另跑核心媒体／厂商账号与 IoC 猎人账号两批、SiteGuard／Plex／EC-CUBE 专题一批。共 **24 次有效 X 读取**（另 2 次 429 未计读）。
> **覆盖说明（重要）**：每次查询最多 25 条。宽泛查询（A／C 原始）只覆盖到窗口最后 1～6 小时；A 类靠翻页和切片补到约 07:20 起，**10-17 20:10 至 10-18 07:20 这段 A／C 关键词流覆盖较薄**，该时段主要靠 LWiS 成员批次、B 类（全窗口 17 条）与核心账号批次补足。今天是周日，安全圈发帖量明显偏低。
> 窗口内去重后 **403** 条帖子（与 seen_ids 无重叠），关键词粗筛（剔除纯回复、闲聊、广告）得 **209** 条安全相关新帖：**A75／B16／C64／LWiS27／核心7／专题20**（多查询重叠时按最先命中批次归类）。下文实际引用约 80 条。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON（`/workspace/enrich-2026-10-18/kev.json`）；厂商／研究页存于 `/workspace/enrich-2026-10-18/web/`：JVN（SiteGuard）、BleepingComputer、boredhackerblog（Plex 在野）、zmain.info（plex2shell）、Zscaler ThreatLabz（NetScaler 88771）、Unit 42（CL-UNK-1211）、nulltap（UAT-6275、FortiSIEM）、rogueauthority（setup.iso）、Bugcrowd（Discord）、CyberWorldOps（CikaBika）、SecurityWeek、zerosalarium、Risky Business、tl;dr sec。**Talos 博客与 drupal.org 对 curl 返回 403／JS 挑战**，相关要点取自 X 原帖与转述页。GitHub API 查了 nuclei／nuclei-templates／Sliver／emp3r0r／BloodHound／NetExec／Mythic／impacket／Havoc 的 releases：**本窗口无新 release**。
> **CISA KEV：catalogVersion 2026.10.16／1748 条，Δ0**（周日无更新，连续第二天不变）。**due_today（10-18）：1 条**——Atlassian **CVE-2026-21589**。**newly_overdue（10-17 到期）：4 条**——AhsayCBS **CVE-2026-105133**、**CVE-2026-105134**，Cisco Secure Email Gateway **CVE-2026-76519**，PAN-OS **CVE-2026-0322**。Ivanti 104935、Windows 96951、Apple 86950 与 AA26-281A 五条仍逾期。**未来 7 天到期：2 条**——BeyondTrust **CVE-2026-102764** 与 Fortinet **CVE-2025-61624**（都是 **10-19 明天**）。**仍未进 KEV 的在野漏洞**：SiteGuard **CVE-2026-106931**（今日新）、Plex2Shell 链（今日确认在野）、Rank Math PRO 111862、Magento BlockStrap 103849、Nextcloud/Collabora 110447 等。
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接作狩猎用途。泄露、入侵类声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【在野 · WAF】SiteGuard Server Edition CVE-2026-106931（OS 命令注入，root／SYSTEM）**：日本主机型 WAF，统计功能默认开启即受影响；JPCERT/CC 与厂商确认已被利用。修到 8.00 Update 5（FreeBSD 为 7.00 Update 6），EOL 版本有替换补丁。**厂商特别提醒：修补会抹掉攻击痕迹，先在管理界面下载「诊断信息」再修。** 未进 KEV。
- **【在野 · 家用／小企业服务器】Plex2Shell 四漏洞链（CVE-2026-96652／96654／96655／96656）10-17 起被实际利用**：蜜罐看到公开 PoC 被用来投 xmrig 挖矿与住宅代理「myawesomeproxy」，攻击 IP 与样本哈希已公开。Plex 9 月已修（1.43.2 及更早受影响）。另有人在 X 预告「加密 C2 版」武器化变种（UNCONFIRMED）。
- **【KEV 到期】** Atlassian 21589 今天到期；Ahsay×2／Cisco SEG 76519／PAN-OS 0322 **今起逾期**；**BeyondTrust 102764 与 Fortinet 61624 明天（10-19）到期**——X 上多位研究者提醒：BeyondTrust 盒子等于「带密码库的跳板机」，修补后要轮换它保存的全部凭据。
- **【供应链 · AI 工具】Blender MCP 插件 `LiCinCan/blender-ai-mcp-addon` 被指为 StealC 投递器**：启用即在后台用自带 Python 拉 `mod-stealc`，连 `193.104.58.41:8443`；仓库抓取时仍在线（约 784 星）。单一研究者分析，UNCONFIRMED，但指标具体，建议先封。
- **【恶意软件】** setup.iso 链完整报告出炉（IronPython → CastleLoader → StealC v2 + NetSupport）；Unit 42 公布 CL-UNK-1211（用 AI 生成脚本打政府 Linux，含 SysGoRAT 与 React2Shell 扫描器）全套 IoC；Talos／Recorded Future 的 UAT-6275 用 WinRAR CVE-2025-8088 投 PickleShell 打独联体政府；Darktrace 报 Rust RAT「CikaBika」走 Discord C2。
- **【漏洞补丁】** Drupal SA-CORE-2026-014（CVE-2026-108097 Field UI，及 108099）官方警告利用可能很快出现；FortiSIEM 7.5.0 CVE-2026-106173（TCP/27918，未在野）；LMCache CVE-2026-105192；VS Code 81376 与 VS/SSMS Copilot 103572 两个开发工具 RCE；Discord 一键 RCE（经 Twitch 嵌入，已修，$5,500）。
- **【工具】** PhantomBuffer（`WM_SETTEXT` 注入绕 EDR 的研究）、DemonLdr（Havoc 的 UDRL 分支）、DidierStevens `onedump.py` 新版；监控的红队框架本窗口无新 release。

## CVE / POC / 漏洞

### 1. SiteGuard Server Edition · CVE-2026-106931（在野，未进 KEV）
EG Secure Solutions 的主机型 WAF（WordPress.org 统计约 50 万站点装有其插件版）。统计功能里的 OS 命令注入，攻击者可用 root／SYSTEM 执行命令。JVN 给 CVSS 4.0 为 8.5（向量为本地、低权限，意味着攻击者多半已在机器上有立足点，有人在 X 上专门指出这一点）。受影响：Apache httpd／Nginx／IIS 2.20 起至 8.00 Update 5 之前；FreeBSD 上至 7.00 Update 6 之前；IIS 3.10～4.00 Update 4 不受影响。厂商 9-29 已私下通知有支持合同的客户。**修补前先在 Web 管理界面下载诊断信息留证**，修补可能抹掉痕迹。攻击者、受害者、规模均未公开。
- X 原帖：
  - https://x.com/V0iD_0daY/status/2111957590485709152
  - https://x.com/Dinosn/status/2111839575920242749
  - https://x.com/MLS_HQ/status/2111955778592448921
  - https://x.com/Pick_Analytica/status/2111864924477821142
  - https://x.com/cybermergemedia/status/2111843123471257604
  - https://x.com/joho_no_todai/status/2111840077563449783
- 厂商公告：
  - https://www.eg-secure.co.jp/siteguard/news/alert-202610-1
  - https://jvn.jp/en/jp/JVN88474777/
- 文章：
  - https://www.bleepingcomputer.com/news/security/hackers-exploit-siteguard-waf-flaw-to-run-commands-as-system-root/
  - https://joho-todai.com/siteguard-vulnerability-cve-2026-106931-root-access/
- 地址／IoC：未见公开 IoC。

### 2. Plex Media Server · Plex2Shell 链（CVE-2026-96652／96654／96655／96656）· 10-17 起在野
研究者 code-zm 10-16 公开四漏洞串联的未认证 RCE 写作与 PoC（Plex 赏金 $500）；Plex 已在 9-1 发安全公告（1.43.2 及更早版本）。boredhackerblog 的蜜罐 10-17 上午起看到真实利用：先 SSRF 回连 sslip.io 域名，再从 `217.60.194.116` 拉 docker 与 UPX 加壳的 `x`（xmrig），第二轮又投住宅代理「myawesomeproxy」（会打印「同意外部使用你的网络流量」字样，作者关联到 proxystream.st）。原作者已在仓库发布检测规则，蜜罐作者另放 pcap。另：@J4ck3LSyN 预告「plex2shell-wz」带 XOR／ChaCha20 加密 C2 配置、memfd 内存执行的变种（**UNCONFIRMED**，无代码链接）。
- X 原帖：
  - https://x.com/Thempra/status/2111953782107955699
  - https://x.com/DarkWebInformer/status/2111849768729100292
  - https://x.com/HOTHEAD01TH/status/2111759231762186480
  - https://x.com/skocherhan/status/2111911750832402707
  - https://x.com/DailyDarkWeb/status/2111945921852592206
  - https://x.com/J4ck3LSyN/status/2111918880134414734
- GitHub／PoC 仓库（仅供狩猎）：
  - https://github.com/code-zm/plex2shell
  - https://github.com/code-zm/plex2shell/tree/main/detection
  - https://github.com/BoredHackerBlog/plex2shell_pcap
- 厂商公告：https://forums.plex.tv/t/important-security-update-for-plex-media-server-v1-43-2-and-earlier/942319
- 文章：
  - https://www.boredhackerblog.info/2026/10/plex-vulnerabilities-being-exploited-in.html
  - https://zmain.info/blog/plex2shell
  - https://www.reddit.com/r/PleX/comments/1x95krg/inthewild_exploitation_of_old_plex_servers/
- 地址／IoC：利用来源 IP `45.194.92.222`、`91.92.40.202`、`176.65.139.228`；下载源 `217.60.194.116`；回连形式 `127.0.0.1.45-194-92-222.sslip.io:8952`；UA `Python-urllib/3.10`；SHA-256 `5712ef510481f15fe8b18fdd10b73026d57cb3d9d151878a692358b99a464441`（docker）、`68938fb428f2bcfef4ede62f7b29cd0f15f37ed59e94462c099f2ca64e36baa7`（x，UPX）、`b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49`（x，脱壳）、`e546b10aee5edc754da4f9b0baace00392257121911f630145078eafad1e6bd9`（myawesomeproxy）、`2d3c618b21a7e2f8bcd735da188e44a7609ff3f204832dd0781cd09e4388c9db`（xmrig）。

### 3. KEV 到期追踪 · Atlassian 21589 今日到期／四条今起逾期／BeyondTrust＋Fortinet 明天到期
- **Atlassian CVE-2026-21589**（Jira 未认证读 web 根目录文件，CVSS 9.3）：due **10-18 今天**。
- **今起逾期（due 10-17）**：AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322（管理界面认证后 RCE，Palo Alto 称利用范围很有限）。
- **BeyondTrust Remote Support CVE-2026-102764**（≤26.2.3，补丁 BT26-05-RS，SaaS 已修）：Mandiant 归因疑似中国关联的 ARMORY CASTLE（原 UNC5221），8-29 起零日利用，SAWFLY webshell。X 上 @mathias_fuchs 强调：别把它当「一台设备被打」，要按跳板机＋密码库失陷来处置，轮换它保存的所有凭据。due **10-19**。
- **Fortinet CVE-2025-61624**（FortiOS 等 CLI 路径穿越）：Unit 42 关联 PEERSTITCH，due **10-19**。
- X 原帖：
  - https://x.com/Reductedrecon/status/2111894318587982246
  - https://x.com/mathias_fuchs/status/2111801382990725608
  - https://x.com/CroutonKron/status/2111878604447682740
  - https://x.com/HoustonIntrove1/status/2111849277903552967
  - https://x.com/ernesttheaiguy/status/2111885028665753639
  - https://x.com/MalwareBibleJP/status/2111813054614872420
  - https://x.com/MLS_HQ/status/2111782308797681997
- 厂商公告：
  - https://www.cisa.gov/news-events/alerts/2026/10/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
  - https://security.paloaltonetworks.com/CVE-2026-0322
  - https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 文章：
  - https://www.securityweek.com/chinese-apt-exploited-beyondtrust-vulnerability-as-zero-day/
  - https://www.anthonybahn.com/news/fortios-cve-2025-61624-peerstitch-implant-exploited/
  - https://cvetodo.com/newsletters/weekly/weekly-cyber-update-2026-week-42
- 地址／IoC：本窗口未见新的公开 IoC（BeyondTrust 的 SAWFLY／BARECLAW 工具名已在前几日报告）。

### 4. Drupal 核心 SA-CORE-2026-014 · CVE-2026-108097（Field UI RCE）＋ CVE-2026-108099（Entity List）
所有受支持版本受影响，修复版 10.6.19／11.3.19／11.4.10。核心本身不直接可利用，但贡献模块或自定义代码会打开路径，其中一种无需登录。尚未报告在野利用，Drupal 警告利用可能在数小时到数天内出现。临时缓解：卸载 `field_ui`。
- X 原帖：
  - https://x.com/NoDramaCyber/status/2111805444297519374
  - https://x.com/modularciso/status/2111858002160394750
  - https://x.com/techaiwire/status/2111880408518512943
- 厂商公告：https://www.drupal.org/sa-core-2026-014
- 文章：https://techaiwire.com/articles/drupal-sa-core-2026-014-field-ui-rce-cve-2026-108097/
- 地址／IoC：未见公开 IoC。

### 5. FortiSIEM 7.5.0 · CVE-2026-106173（FG-IR-26-180，未在野）
`phQueryMaster` gRPC 组件的路径穿越导致任意文件写，特制数据包可未认证执行代码，Fortinet 评 9.4，标注「Known Exploited: No」。升级到 7.5.1；暂时把 TCP/27918 限到真正需要的客户端网段（内网也要限）。
- X 原帖：https://x.com/Nulltap_/status/2111867142761279978
- 厂商公告：https://fortiguard.fortinet.com/psirt/FG-IR-26-180
- 文章：https://nulltap.com/p/fortinet-fortisiem-packet-code-execution/
- 地址／IoC：未见公开 IoC。

### 6. EC-CUBE AmazonPay 插件 · CVE-2026-103671（「在野劫持结账」，UNCONFIRMED）
只有 ZoomEye 机器人帖称 EC-CUBE 4 系列 AmazonPay 插件被在野利用来劫持结账，暴露约 1k 实例。本轮**没找到厂商或 JPCERT 公告链接**，先列为待核实；日本电商运营方可先查插件版本。
- X 原帖：https://x.com/zoomeyebot/status/2111951785397194847
- 厂商公告：本轮未取得。
- 地址／IoC：未见公开 IoC。

### 7. 开发工具与 AI 组件漏洞（均已修）
- **LMCache CVE-2026-105192**：多进程模式在未认证的 ZeroMQ 端口（默认 5555）反序列化 pickle，绑到可路由地址即 RCE；0.3.9～0.5.5 受影响，0.5.6 修复但仍无 RPC 认证，要限源。
- **VS Code CVE-2026-81376**：Workspace Trust 绕过到 RCE（CVSS 9.6，$4,000），升到 1.136.2+。
- **Visual Studio／SSMS Copilot CVE-2026-103572**：Copilot 按文件名保护 `.mcp.json`，但 Windows 会丢掉末尾的点，被注入的 agent 可以写 `.mcp.json.` 加 MCP 服务器执行命令。VS 2022 也要补。
- **Discord 一键 RCE（经 Twitch 嵌入）**：Bugcrowd 10-14 公开，P1、$5,500、已修；链条涉及 V8 RegExp UAF 与 Electron IPC 沙箱逃逸。
- X 原帖：
  - https://x.com/alex_cuciureanu/status/2111895818093388110
  - https://x.com/devmoonpy/status/2111926148225548719
  - https://x.com/DarkWebInformer/status/2111885508930380162
  - https://x.com/swif_ai/status/2111767863002570972
  - https://x.com/vxunderground/status/2111926875626893547
  - https://x.com/vxunderground/status/2111927008414638264
- 厂商公告：
  - https://github.com/LMCache/LMCache/security/advisories/GHSA-w5f2-9q9c-ff4h
- 文章：
  - https://samchen.blog/blog/vscode-nested-form-to-rce
  - https://embracethered.com/blog/posts/2026/visual-studio-copilot-remote-code-execution/
  - https://bugcrowd.com/disclosures/63864b55-10d6-4e82-a619-192b8c0c99ad/1-click-remote-code-execution-via-twitch-embed
- 地址／IoC：未见公开 IoC。

### 8. 新公开 PoC 仓库（只给链接作狩猎／验证用途）
- **Magento／Adobe Commerce BlockStrap CVE-2026-103849 实验环境**（@Dinosn）。日本 CSIRT @connect24h 提醒：仓库 README 承认完整命令执行要靠实验专用 gadget，别把它直接读成「标准安装未认证 RCE 已证实」。
- **V-Secure 精云驱动 ZyArk.sys CVE-2026-19195**：IOCTL 访问控制不当暴露特权注册表操作（BYOVD 类，查驱动加载）。
- **macOS automountd CVE-2026-84568**（及 84570）：LDAP 投毒 automount 后经 `fstype` 路径穿越以 root 执行；Apple 9-14 已修（Sequoia 15.8／Tahoe 26.7）。
- **WooCommerce Medical Prescription Attachment ≤1.2.3 CVE-2025-29009**：未认证任意文件上传（CVSS 10）。
- **Peercoin 区块链漏洞**：官方紧急发布 v0.15.2，细节见论坛帖。
- X 原帖：
  - https://x.com/Dinosn/status/2111735561803190763
  - https://x.com/connect24h/status/2111775262279135735
  - https://x.com/Ciel0Fernandez/status/2111850617446768739
  - https://x.com/0xManan/status/2111769476119347705
  - https://x.com/DarkWebInformer/status/2111619584738410803
  - https://x.com/PeercoinPPC/status/2111801448443035906
- GitHub／PoC 仓库：
  - https://github.com/dinosn/cve-2026-103849-blockstrap-lab
  - https://github.com/patrickt2017/CVE-2026-19195-PoC
  - https://github.com/redinpulse/CVE-2026-84568
  - https://github.com/Nxploited/CVE-2025-29009
  - https://github.com/peercoin/peercoin/releases/tag/v0.15.2ppc
- 文章：https://talk.peercoin.net/t/new-peercoin-exploit-detected-its-not-great-we-have-a-plan/16917
- 地址／IoC：未见公开 IoC。

### 9. 其他回顾与零散条目
- **Citrix NetScaler CVE-2026-88771**：Zscaler ThreatLabz 10-16 发利用分析（访问日志投毒→认证前命令执行→指纹→多个 webshell，另见 FreeBSD x64 植入物），附 28 个来源 IP（见 IoC 汇总）。X 上转的 CyberScoop「三个零日」文章是 **10-05 旧闻**。
- **Amazon Neptune CVE-2026-110812**（Gremlin 导入反序列化 RCE，需认证，1.5.0.0 修复）：仅见 X 帖，未取得 AWS 公告链接。
- **Cisco SD-WAN Manager CVE-2026-20245／76504**、**PwnEscape CVE-2026-99999**、**Nextcloud Collabora 110447**：本窗口只是提醒帖，无新进展。
- X 原帖：
  - https://x.com/samilaiho/status/2111805533321658720
  - https://x.com/johnmcclure00/status/2111882522686566448
  - https://x.com/UpwindMDR/status/2111811971783803081
  - https://x.com/yogsec/status/2111765000859861064
  - https://x.com/thatboringbro/status/2111863608783278373
  - https://x.com/HETPATELL__/status/2111908028148842980
- 文章：
  - https://www.zscaler.com/blogs/security-research/cve-2026-88771-inside-exploitation-critical-netscaler-rce-vulnerability
  - https://cyberscoop.com/citrix-netscaler-third-exploited-zero-day-vulnerability/
  - https://nvd.nist.gov/vuln/detail/CVE-2026-20245
- 地址／IoC：NetScaler 88771 来源 IP 见汇总表；其余未见公开 IoC。

## 工具与 GitHub 发布

### 1. PhantomBuffer（@TwoSevenOneT）· 用 `SendMessage`＋`WM_SETTEXT` 做隐蔽注入绕 EDR 的研究
作者称可绕过高端 EDR。防守侧：关注跨进程向窗口大量发送 `WM_SETTEXT` 后紧接执行的行为。
- X 原帖：
  - https://x.com/TwoSevenOneT/status/2111645120626139344
  - https://x.com/TwoSevenOneT/status/2111645670239248546
- GitHub：https://github.com/TwoSevenOneT/PhantomBuffer （仓库名取自帖文正文「Github: TwoSevenOneT/PhantomBuffer」）
- 文章：https://www.zerosalarium.com/2026/10/PhantomBuffer-Effective-EDR-Evasion-Stealth-Injection.html
- 地址／IoC：未见公开 IoC。

### 2. DemonLdr（@cr4ckeddd）· Havoc 框架支持用户自定义反射加载器（UDRL）的分支，附 Crystal Palace 构建的 UDRL PoC
- X 原帖：https://x.com/cr4ckeddd/status/2111808270025544141
- GitHub：https://github.com/0xPrimo/DemonLdr
- 地址／IoC：未见公开 IoC。

### 3. 其他工具与防守资源
- **FenrirLVX**：离线 WordPress 插件指纹＋CVE 关联。
- **onedump.py 新版**（Didier Stevens，列出 OneNote 内嵌文件，DFIR 用）。
- **CloudKeyVaultEvents**：Azure Key Vault 日志架构与 KQL 狩猎。
- **PowerShell 编码命令参数的各种拼写**：检测规则常漏的变体。
- **cve-intel**：KEV＋EPSS＋NVD＋OSV 合成风险分。
- **eleven**：把 AI 接进 Ghidra／Rizin／jadx 的逆向工作台。
- **orlofv/Indicators**：每日更新的 Sliver／Vidar 等 IoC 列表。
- X 原帖：
  - https://x.com/LeviathanXCDN/status/2111677421330235751
  - https://x.com/DirectoryRanger/status/2111800039156666797
  - https://x.com/DirectoryRanger/status/2111801240027828255
  - https://x.com/DirectoryRanger/status/2111736978903544086
  - https://x.com/Dinosn/status/2111728036924022802
  - https://x.com/EsGeeks/status/2111596357509366062
  - https://x.com/orlof_v/status/2111817425150964152
- GitHub：
  - https://github.com/leviathan-offsec/FenrirLVX
  - https://github.com/DidierStevens/Beta/blob/master/onedump.py
  - https://github.com/Fazmin/cve-intel
  - https://github.com/Zfinix/eleven
  - https://github.com/orlofv/Indicators/blob/main/SliverC2
- 文章：
  - https://kqlquery.com/posts/cloudkeyvaultevents/
  - https://ridgelinecyber.com/blog/encoded-powershell-spellings-your-detection-misses/
- 地址／IoC：未见公开 IoC。

### 4. 监控的红队框架 releases
本窗口无新版本。最新：nuclei v3.11.1（08-08）、nuclei-templates v10.5.0（10-05）、Sliver v1.7.8（10-03）、emp3r0r v5.3.0（10-16，已在前报）、BloodHound v9.8.0（10-07）、NetExec v1.5.1、Mythic v3.4.0.5、impacket 0.13.1；Havoc 仓库无 GitHub release。
- 来源：https://api.github.com/repos/projectdiscovery/nuclei/releases 等（GitHub API）。

## APT / Malware 分析

### 1. 恶意 Blender MCP 插件 `LiCinCan/blender-ai-mcp-addon` 投递 StealC（UNCONFIRMED）
@vibelancer 分析：插件自称「mcp-for-blender-pro」，复制了 ahujasid 真实 blender-mcp 的 3,651 行代码，维护者写成一字之差的「anujasid」。勾选启用即在 `register()` 里静默启动自带的 Python 3.13（缺失时从第二个仓库 `mcp-for-blender-pro-runtime` 下载），执行 `blen.blend` 里藏的脚本，关闭 TLS 校验连 C2 拉 `mod-stealc` 内存执行；用 `%TEMP%` 下的标记文件只跑一次。Box 抓取时仓库仍在线（约 784 星、377 fork）。要做：查 Blender 插件目录、标记文件，轮换粘贴进插件的所有 API key，从干净设备改浏览器密码。
- X 原帖：https://x.com/vibelancer/status/2111924940119126286
- GitHub 仓库（恶意，勿安装）：https://github.com/LiCinCan/blender-ai-mcp-addon
- 地址／IoC：C2 `193.104.58.41:8443`；标记文件 `%TEMP%\hjaksdhk1242kjha.txt`；二阶段名 `mod-stealc`；载体 `blen.blend`、`tools/python-x64`；关联仓库名 `mcp-for-blender-pro-runtime`；伪维护者 `anujasid`。

### 2. setup.iso → IronPython → CastleLoader → StealC v2 ＋ NetSupport（昨日 malwrhunterteam 样本的完整报告）
rogueauthority 发布全链分析：ISO 内 `setup.lnk` 调 `setup.cmd`，用自带 IronPython（`ipyw32.exe`）执行伪装成文本的 `docs\submergibility.txt`；之后五段全在内存，Base64 混入西里尔字母、XOR、RC4，最后是 C++ 加载器 bot，装 StealC v2 与 NetSupport。三个公开沙箱里两个判干净，因为没点快捷方式。@vxunderground 同日吐槽了同一条「8 层 stager」链。@SquiblydooBlog 与 @500mk500 把三个域名分别对应到 CastleLoader／NetSupport／StealC。
- X 原帖：
  - https://x.com/SquiblydooBlog/status/2111859404257849725
  - https://x.com/vxunderground/status/2111873359709704442
  - https://x.com/skocherhan/status/2111867847475659189
  - https://x.com/500mk500/status/2111905477777121597
- GitHub：https://github.com/stamparm/trails/commit/7cfea40ba4ef90bf024433f14e458d3bee0ee50e
- 文章：https://rogueauthority.org/setup-iso-ironpython-stealc-netsupport
- 地址／IoC：见汇总表（域名 3 个、IP 4 个、SHA-256 6 个、互斥量、UA、路径）。

### 3. Unit 42 · CL-UNK-1211：用 AI 生成脚本打政府 Linux 环境（10-15 发布，今日 X 扩散）
2025-10 至 2026-04 活动，归属未定（国家或犯罪团伙）。脚本里残留给操作者看的对话式 AI 注释。手法：`auto_prepend_file` 植 PHP webshell（含 Plesk 路径）、`.bashrc` 里伪造 sudo 别名记密码（日志伪装成 SolarWinds 文件名）、自研 Go 写的跨平台 WebSocket RAT「SysGoRAT」与 React2Shell（CVE-2025-55182）扫描器、PwnKit 提权、GSocket 中继、`xp_cmdshell` 横向、日志清除与时间戳篡改，并用「RedTeamOps2025」「pentest123」伪装成红队演练。
- X 原帖：https://x.com/MalwareBibleJP/status/2111866406442832316
- 文章：https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/
- 地址／IoC：见汇总表（17 个 IP、4 个域名、11 个 SHA-256）；持久化路径 `/etc/systemd/system/sys-update.service`。

### 4. UAT-6275（Cisco Talos × Recorded Future）· WinRAR CVE-2025-8088 投 PickleShell 打独联体政府
2025-06 至 2026-08，九国（哈、吉、塔、土、乌、亚美尼亚、阿塞拜疆、俄、白俄）外交／经济／环境部门，诱饵涉水与能源。四条投递链：宏文档、PS2EXE 下载器＋计划任务、LNK→PowerShell 拉 GitHub 脚本、2026-04 起用 WinRAR 路径穿越把 PickleShell 放进启动文件夹（Talos 称这是该组首次用漏洞投递）。WinRAR 7.13 修复。狩猎：解压后新出现的启动项、异常 PowerShell。
- X 原帖：https://x.com/Nulltap_/status/2111957649822724225
- 文章：
  - https://blog.talosintelligence.com/break-the-silence-kazakhstan-nexus-uat-6275-targets-cis-government-organizations
  - https://nulltap.com/p/uat-6275-winrar-cis-government-shells/
- 地址／IoC：未见公开 IoC（Talos 原文对 Box 返回 403，未能抄录其 IoC 节；需要时请直接打开 Talos 链接）。

### 5. CikaBika Bot（Darktrace，经 SecurityAffairs）· Rust RAT 用 Discord 当 C2
`Proposition_Projet.img` 内伪装 Word 的 LNK 启隐藏 PowerShell，从诱饵 PDF 里解出 Nim 加载器，再把 Rust DLL 以 `dbghelp.dll` 放进 Edge 安装目录做搜索顺序劫持，借 `computerdefaults.exe` 绕 UAC 写受保护目录。每台受害机建一个 Discord 频道，大文件经 Ngrok 外传。Darktrace 未能证实 Edge 真的加载了该 DLL。
- X 原帖：
  - https://x.com/DFIR_Radar/status/2111790004301139992
  - https://x.com/CyberWorldOps/status/2111885225974280365
- 文章：
  - https://securityaffairs.com/201210/security/rust-based-cikabika-bot-turns-discord-into-a-command-center.html
  - https://cyberworldops.eu/en/cikabika-bot-pairs-discord-control-with-an-unconfirmed-edge
- 地址／IoC：文件 `Proposition_Projet.img`；Edge 目录下的 `dbghelp.dll`；滥用 `computerdefaults.exe`；C2 为 Discord、外传走 Ngrok（未见公开 IP／域名／哈希）。

### 6. GuLoader 与 RevStealer 沙箱复盘（@Darkfibr3）
GuLoader 以 `Order-1004552_2026-10-14.bat`（NSIS 自解压）订单诱饵投递，从 `194.116.236.88` 取加密二阶段；RevStealer 把配置死投放在 telegra.ph 页面与 Polygon RPC 调用里，通过 SMTP 外传，计划任务每分钟运行，Defender 检出为 `Trojan:Win32/Qwexlafiba!rfn`。作者已提交 URLhaus／ThreatFox。
- X 原帖：https://x.com/Darkfibr3/status/2111808890643865895
- 文章／记录：
  - https://urlhaus.abuse.ch/url/3951887/
  - https://threatfox.abuse.ch/ioc/1972726/
- 地址／IoC：见汇总表。

### 7. 「Father Miguel／Père Miguel」假捐款广告诈骗（International Cyber Digest 调查）
Meta 广告引流至捐款页，结账页默认勾选 $5 附加费、不写商户或慈善名；Meta 下架了一个版本，其他广告投放到 10-18，捐款站至今在线。
- X 原帖：
  - https://x.com/IntCyberDigest/status/2111890504791228839
  - https://x.com/IntCyberDigest/status/2111890496452767951
  - https://x.com/IntCyberDigest/status/2111890501972672566
- 文章：https://palette.osint.industries/snapshot/01a14f8c-77d1-77e8-abfb-a3451794972b
- 地址／IoC：`peremiguel[.]online`、`smmartwork[.]com`、`pmiguel[.]online`。

### 8. 零散 IoC 投放（猎人账号，单源，UNCONFIRMED）
- SideWinder C2（@phatomcandle）；Sliver C2 与 Vidar 域名（@orlof_v）；BTMOB Android RAT 面板与 NDragon RAT 面板（@Fact_Finder03）；AsyncRAT C2 域名举报（@CYMIT11428，帖中 t.co 展开出两个域名，哪一个是 C2 未逐一核实）；仿 Miro 钓鱼页（@skocherhan）；MODBEACON Rust RAT 用 gRPC 流加密 C2（@blueteamsec1，原文链接未展开）；GreyNoise 披露「Bandit」劫持 IoT 与路由器卖带宽到 Pawns.app。
- X 原帖：
  - https://x.com/phatomcandle/status/2111834695830761940
  - https://x.com/orlof_v/status/2111817425150964152
  - https://x.com/orlof_v/status/2111757703110676824
  - https://x.com/Fact_Finder03/status/2111814806756057553
  - https://x.com/Fact_Finder03/status/2111797694792364391
  - https://x.com/CYMIT11428/status/2111866491008348332
  - https://x.com/CYMIT11428/status/2111843129292992804
  - https://x.com/skocherhan/status/2111875203739336955
  - https://x.com/blueteamsec1/status/2111603671985500464
  - https://x.com/sh3ll_c0d3/status/2111864637486477595
- GitHub：
  - https://github.com/orlofv/Indicators/blob/main/SliverC2
  - https://github.com/orlofv/Indicators/blob/main/Vidar
- 文章：https://sh3llc0d3.com/blog/greynoise-unmasks-bandit-global-proxyjacking-campaign-enrolls-iot-devices-into-pawnsapp/
- 地址／IoC：见汇总表。

### 9. 泄露／入侵声称（全部 UNCONFIRMED／未验证）
ShinyHunters 声称攻击 Vercel（ThreatAtlas 机器人帖，行业字段明显有误）；有人声称拿到 JAMCO Aerospace 全库访问；「Zerrix」兜售 VirusTotal Enterprise API key；HostingPeru 65 万条、Habib Metropolitan Bank 数据兜售；EY／Goldman Sachs 工单泄露复盘；Gîtes de France 117,574 账号入 HIBP（这条有 HIBP 收录）。另 ConnectWise Cloud Backup 事件继续发酵（THN：ConnectWise 暂停 Cloud Backup）。
- X 原帖：
  - https://x.com/ThreatAtlas/status/2111953392738164796
  - https://x.com/MonThreat/status/2111859282085875744
  - https://x.com/DarkWebInformer/status/2111860607368491095
  - https://x.com/intels_daily/status/2111952010903798219
  - https://x.com/intels_daily/status/2111953175913574892
  - https://x.com/Dinosn/status/2111933083511353565
  - https://x.com/Dinosn/status/2111728059233767463
  - https://x.com/Dinosn/status/2111746635579486638
- 文章：
  - https://ponderwall.com/index.php/2026/10/18/ey-data-breach-wall-street-goldman-sachs/
  - https://haveibeenpwned.com/Breach/GitesDeFrance
  - https://thehackernews.com/2026/10/connectwise-suspends-cloud-backup-after.html
- 地址／IoC：未见公开 IoC。

## 地址／IoC 汇总

> 原样抄录，保持去武装格式；仅供检测与封堵，勿直接访问。

| 来源 | 类型 | 指标 |
|---|---|---|
| Plex2Shell 在野（boredhackerblog） | 利用来源 IP | `45.194.92.222`、`91.92.40.202`、`176.65.139.228` |
| Plex2Shell 在野 | 下载源／回连 | `217.60.194.116`；`127.0.0.1.45-194-92-222.sslip.io:8952`；UA `Python-urllib/3.10` |
| Plex2Shell 在野 | SHA-256 | `5712ef510481f15fe8b18fdd10b73026d57cb3d9d151878a692358b99a464441`（docker）、`68938fb428f2bcfef4ede62f7b29cd0f15f37ed59e94462c099f2ca64e36baa7`（x UPX）、`b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49`（x 脱壳）、`e546b10aee5edc754da4f9b0baace00392257121911f630145078eafad1e6bd9`（myawesomeproxy）、`2d3c618b21a7e2f8bcd735da188e44a7609ff3f204832dd0781cd09e4388c9db`（xmrig） |
| Blender MCP 插件（StealC） | C2／文件 | `193.104.58.41:8443`；`%TEMP%\hjaksdhk1242kjha.txt`；`mod-stealc`；`blen.blend` |
| Blender MCP 插件 | 仓库 | `github.com/LiCinCan/blender-ai-mcp-addon`、`mcp-for-blender-pro-runtime` |
| setup.iso 链（rogueauthority） | 域名→IP | `jumalputty[.]com`→`94[.]26[.]0[.]118`（阶段与加载器 C2）；`nizariuserp[.]com`→`195[.]63[.]130[.]47`（NetSupport 包）；`crataga[.]site`→`79[.]132[.]128[.]88`（角色未知）；StealC C2 `85[.]239[.]149[.]151` |
| setup.iso 链 | URL | `hxxps[://]jumalputty[.]com/473070fa-6f82-5c2a-9dee-3db4be57110f/`（doc8、v8、viewer99）；`hxxps[://]jumalputty[.]com/70cadffb-604e-5ebd-845d-79a123ed1f74`（加载器 C2） |
| setup.iso 链 | SHA-256 | `36805ebcc0c295751c9b858fc9bbe75ba46362c672f860eafb73ec67f7ce8a4b`（setup.iso）、`61dac869de65880377d4f398175b6c17d703a29b01483bd52fc3954e5876f9e3`（doc8）、`63e5e40ea1abc1a4df7d5881a86332705f19f51510b9d09e5d6f725fc653dfcc`（v8）、`0d65239438fb18bdd4a80e1a2b071eed3215ac0615d4f62854aeeefde98e69ba`（加载器，仅内存）、`7114bf57f09c0bb24e6d7e895afc33721187b06969c3454db749c1c0e11cfb10`（StealC v2）、`9666964ef36a9a4a5585d10d3337cfa07472b002083df885639812f2178b5676`（StealC App-Bound helper） |
| setup.iso 链 | 主机特征 | 互斥量 `D7lzR4b7W1q6PHS`；UA `hUoJQMMpy5YoPFuQ0Htm`；`%LOCALAPPDATA%\Nets\Netsupport\client32.exe`；`docs\submergibility.txt`、`runtime\ipyw32.exe` |
| CL-UNK-1211（Unit 42） | IP | `45.88.188[.]140`、`198.23.185[.]234`、`138.68.244[.]146`、`185.21.136[.]6`、`72.61.89[.]179`、`104.194.158[.]65`、`109.224.53[.]140`、`162.243.175[.]162`、`154.93.37[.]228`、`141.164.58[.]87`、`88.80.150[.]232`、`88.119.167[.]57`、`173.212.247[.]23`、`104.248.131[.]53`、`147.182.224[.]216`、`93.93.112[.]57`、`192.210.183[.]17` |
| CL-UNK-1211 | 域名 | `magento[.]ink`、`solidmonpe[.]com`、`wibu-bau-bawang[.]online`、`beraskencur[.]site` |
| CL-UNK-1211 | SHA-256 | React2Shell 扫描器 `2bf7992e6260c1a98c709fa98ec766fb9f27692f338b30b43ac821b824fd849e`、`27d799ceadb570bfca890d4c2572314afe57eecf14083d30409da15afdfc4704`、`d73186cea6cf2cf3d48c09139a9d15521365aab675787b4e7a6f81767331c9fd`、`9e45830171eb607cf2c0fc80f5cc9cc3db39bb937032136990383a595f6f151e`；提权后门 `c527b94e3d21824a674face4cd9d862e536b60ccbf54573839e3360f99188343`；GSocket `d94f75a70b5cabaf786ac57177ed841732e62bdcc9a29e06e5b41d9be567bcfa`；PwnKit `44e83f84a5d5219e2f7c3cf1e4f02489cae81361227f46946abe4b8d8245b879`；PHP webshell `1505a3a727f8899b2ad343519f7bf9c438b8b802f8d6b854f5db3b52f857c76a`、`76c58fad4f70cf277a15a499b9a2151ac60e7a6b5c7a9ab684843dcc19f0d0a5`、`b1e82c6b0caea177e8bb71ad826867f509c65f0a43a651b50253e7c726566eac` |
| CL-UNK-1211 | 主机特征 | `/etc/systemd/system/sys-update.service`；`auto_prepend_file` 指向 webshell；伪装字符串 `RedTeamOps2025`、`pentest123` |
| NetScaler CVE-2026-88771（Zscaler） | 来源 IP | `45.153.212[.]101`、`46.233.40[.]20`、`46.236.167[.]143`、`46.33.33[.]95`、`49.150.197[.]119`、`78.190.152[.]64`、`81.10.79[.]197`、`82.167.14[.]7`、`95.105.74[.]172`、`100.38.125[.]66`、`102.213.132[.]123`、`102.222.146[.]45`、`103.181.212[.]245`、`103.197.249[.]161`、`103.83.146[.]100`、`111.92.128[.]89`、`114.145.49[.]215`、`120.244.160[.]182`、`125.62.88[.]26`、`130.12.182[.]7`、`154.183.158[.]198`、`154.241.254[.]9`、`174.60.63[.]37`、`177.52.203[.]23`、`183.63.88[.]227`、`190.117.56[.]56`、`195.62.37[.]119`、`207.48.184[.]10` |
| GuLoader（Darkfibr3） | IP／URL 路径／主机 | `194.116.236.88`、`GET /vDsuzsiIMAiwv69.bin`、`33841-28554.dchost.com` |
| GuLoader | 主机特征 | 注册表 `HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\pianofortist\seedsmen\needleproof`；诱饵 `Order-1004552_2026-10-14.bat` |
| RevStealer | 域名／死投放 | `apollo.hosterbox.com:587`、`mail.spark-trail95.xyz/health`、`api.telegra.ph/getPage/`、`polygon-bor-rpc.publicnode.com`、`polygon.lava.build` |
| RevStealer | 主机特征 | `AppData\Local\Common\Common\Temp\E8204C9F\ProUpdate7dd338.exe`；计划任务 `MaintainHost_058f`（每分钟）；检出名 `Trojan:Win32/Qwexlafiba!rfn` |
| CikaBika Bot | 文件／行为 | `Proposition_Projet.img`；Edge 安装目录下 `dbghelp.dll`；`computerdefaults.exe` 绕 UAC |
| Father Miguel 捐款诈骗 | 域名 | `peremiguel[.]online`、`smmartwork[.]com`、`pmiguel[.]online` |
| SideWinder（phatomcandle） | IP／域名 | `146[.]70[.]41[.]160`、`www[.]flpoised[.]net` |
| Sliver C2（orlof_v） | IP | `130.94.1[.]88`、`167.99.227[.]197` |
| Vidar（orlof_v） | 域名 | `7k.iakmialor.web[.]id` |
| BTMOB Android RAT 面板 | IP／域名 | `47.236.21.193`；`tardipig[.]com`、`btmob[.]my`、`btmob[.]live`、`btmob[.]pw` |
| NDragon RAT 面板 | IP:端口 | `192.252.183.158:8080` |
| AsyncRAT 举报（CYMIT11428，未逐一核实） | 域名 | `9721.cn[.]com`、`bf168-slot[.]com`、`arianpars[.]co`、`qh88vn[.]vip` |
| 仿 Miro 钓鱼（skocherhan） | 域名 | `collaboration-creator[.]info` |

其余条目（SiteGuard 106931、KEV 到期各条、Drupal 108097／108099、FortiSIEM 106173、EC-CUBE 103671、LMCache、VS Code／VS Copilot、Discord、各 PoC 仓库、UAT-6275、泄露声称）：**未见公开 IoC**。

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

本日 LWiS 成员高信号（周日整体偏静）：@TwoSevenOneT（PhantomBuffer）、@cr4ckeddd（DemonLdr）、@vxunderground（setup.iso 多层 stager、Discord 一键 RCE）、@Dinosn（SiteGuard、BlockStrap 实验环境、ConnectWise、OpenCode、cve-intel）、@DirectoryRanger（onedump、Key Vault KQL、PowerShell 编码检测）、@ntlmrelay（10-17 热门链接：Huntress ConnectWise、Microsoft 公告、Anthropic ECDSA 曲线研究、BleepingComputer ConnectWise）、@PaulosYibelo（PwnEscape 后续答疑）。博客清单交叉：Unit 42（https://unit42.paloaltonetworks.com/）与 embracethered（https://embracethered.com/blog/）在清单内，今日条目已引用。tl;dr sec 最新仍为 #350；Risky Business 首页本窗口未见新集数可确认。

## 来源搜索 URL

- A（CVE／0day／PoC）：https://x.com/search?q=%28CVE-2026%20OR%200day%20OR%20zero-day%20OR%20%22actively%20exploited%22%20OR%20PoC%29%20-is%3Aretweet&f=live
- A 去噪：https://x.com/search?q=%28CVE-2026%20OR%20CVE-2025%29%20%28exploit%20OR%20exploited%20OR%20PoC%20OR%20RCE%20OR%20patch%20OR%20advisory%20OR%20KEV%29%20-is%3Aretweet&f=live
- A 在野：https://x.com/search?q=%28%22zero-day%22%20OR%200day%20OR%20%22in%20the%20wild%22%20OR%20%22actively%20exploited%22%29%20%28vulnerability%20OR%20exploit%20OR%20CVE%20OR%20patch%29%20-is%3Aretweet%20-is%3Areply&f=live
- B（GitHub 红队／C2）：https://x.com/search?q=url%3Agithub.com%20%28C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20PoC%20OR%20exploit%20OR%20BOF%20OR%20EDR%29%20-is%3Aretweet&f=live
- B 补充：https://x.com/search?q=url%3Agithub.com%20%28%22red%20team%22%20OR%20implant%20OR%20%22post-exploitation%22%20OR%20pentest%20OR%20loader%20OR%20Sliver%20OR%20Havoc%29%20-is%3Aretweet&f=live
- C（威胁报告）：https://x.com/search?q=%28%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20OR%20infostealer%20OR%20backdoor%29%20-is%3Aretweet&f=live
- C IoC：https://x.com/search?q=%28malware%20OR%20infostealer%20OR%20RAT%20OR%20backdoor%20OR%20ransomware%20OR%20loader%29%20%28IOC%20OR%20C2%20OR%20sha256%20OR%20%22threat%20report%22%29%20-is%3Aretweet%20-is%3Areply&f=live
- 专题：https://x.com/search?q=SiteGuard%20OR%20plex2shell%20OR%20%22EC-CUBE%22%20OR%20%22CVE-2026-106931%22&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
