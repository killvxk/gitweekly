# X 安全情报晚报 · 2026-10-16

> 搜集窗口：圣地亚哥时间 **2026-10-15 20:10 至 2026-10-16 20:15**（America/Santiago／UTC-3，约 **24 小时 5 分**，接昨晚窗口，没有缺口）。ISO／X 搜索参数：`start_time=2026-10-15T23:10:00Z`，`end_time=2026-10-16T23:15:00Z`。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all` + `get_posts_by_ids`，带 entities／note_tweet；t.co 链接一律用 entities.expanded_url／unwound_url 展开）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** A／B／C 三类各跑原始与去噪查询：A 用 `CVE-2026`／安全语境去噪（去刷屏 RT 与自动复述账号）；B 限 `url:github.com` + C2／red team／nuclei／PoC；C 为 malware analysis／threat report／threat actor，排除 ThreatAtlas／FalconFeeds／intels_daily 刷屏。LWiS 用 `from:` + recency：①核心账号批（BleepingComputer／THN／securityaffairs／CISACyber／CrowdStrike／malwrhunterteam／Nulltap_／cybermergemedia／DailyDarkWeb／Python_s_／ThreatWire_）分页；②扩展厂商／媒体（SecurityWeek／Shadowserver／sans_isc／Unit42／Huntress／DFIR_Radar／Dinosn／Talos／TheRecord 等）；③LWiS List 500 成员分 10 段 `from:` 批次全量翻查，外加 Volexity／Mandiant／vxunderground／watchtowr 等研究账号。`from:` 用户名均 ≤15 字符。本轮共 **25 次 X 读取**（search_posts_all 24 次 + get_posts_by_ids 1 次），**未触发限速**（当日额度仍余约 975/1000）。窗口内去重后约 **230+** 条相关帖（多查询重叠），与 seen_ids 比对并剔除广告、空转发、自动复述 KEV 的刷屏账号、闲聊、勒索受害者刷屏后，合并 **162** 条安全相关新帖：**A4／B12／C18／LWiS128**（命中 LWiS／核心信源 `from:` 批次的算 LWiS，其余按 A／B／C 来源）。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON（`/workspace/enrich-2026-10-16/kev.json`）。厂商／研究页存于 `/workspace/enrich-2026-10-16/web/`：CISA 10-16 KEV 警报、Fortinet FG-IR-26-122（CVE-2025-61624）与 FG-IR-26-185（FortiSandbox CVE-2026-107656）、Google/Mandiant GTIG「Ephemeral Supply Chain Tampering（AOMEI/UNC7017）」、THN（PEERSTITCH／AOMEI／UAT-11985／OpenBSD／BeyondTrust）、Security Affairs（PEERSTITCH／NGINX）、Unit 42 PEERSTITCH、BleepingComputer BlockStrap、Sansec 博客、ConnectWise Trust Advisory、SentinelOne APT29 CaptiveCrunch、GuidePoint Silent Ransom Group、Expel QuartzLine、Jamf/OSS GhostAction、Nextron .NET WebSockets Downloader、Volexity Mind the (Patch) Gap Part 3、Avertium PAN-OS CVE-2026-0257、Nulltap（FortiSandbox／Cisco SEG／BeyondTrust）、Amber Wolf（Ivanti 自定义登录页 RCE）、Risky Business／Risky Bulletin、tl;dr sec、估 estore.jp / nikkei.co.jp 泄露公告。GitHub API 查了 nuclei／nuclei-templates／Sliver／emp3r0r／BloodHound／NetExec／Mythic／impacket 的 releases。**BeyondTrust trust-center（BT26-05）对 curl 返回 403，Cisco NX-OS 公告与 AhnLab ASEC（ARTEX）连接超时／TLS 中断**，相关要点取自 Mandiant／GTIG、Nulltap、DFIR_Radar 转述与 X 原帖 entities 展开。
> **CISA KEV：catalogVersion 2026.10.16／1748 条，Δ+2**（对比昨日 2026.10.15／1746；dateReleased 2026-10-16T17:15:48Z＝**10-16 14:15 圣地亚哥**）。**今天新增 2 条**，均 forensicTriage、due **2026-10-19**：**CVE-2026-102764**（BeyondTrust Remote Support 认证绕过/欺骗，在野零日，昨晚报告的未进 KEV 项今日正式入列）与 **CVE-2025-61624**（Fortinet 多产品 CLI 路径遍历，FG-IR-26-122，CVSS 6.0 Medium 但在野、用于投放 PEERSTITCH）。
> **due_today（10-16）：2 条**——Ivanti Connect Secure **CVE-2026-104935**、Windows Shell **CVE-2026-96951**（均 10-13 入列）。**newly_overdue（10-15 到期）：0 条。** Apple CVE-2026-86950（due 10-13）与 AA26-281A 五条（BIND／Struts／Strapi／ONLYOFFICE／ProFTPD，due 10-11）仍逾期。**未来 7 天到期：7 条**：Ahsay 105133／105134、Cisco 76519、PAN-OS 0322 在 **10-17**；Atlassian 21589 在 **10-18**；BeyondTrust 102764、Fortinet 61624 在 **10-19**。下列 CVE **仍未进 KEV**：Magento/Adobe Commerce BlockStrap **103849**、GitLab **97229**、Langflow **105740**、FortiSandbox **107656**、Next.js／librsvg **96889**、Nextcloud/Collabora **110447**、PwnEscape **99999**、WordPress Theme My Login **89079**、Windows WPAD **85884**、Linux「Infinity Core」六条（98260／98256／89754／80775／98385／97941）等。
> 抓取备注：监控的红队工具中 **emp3r0r 今日发 v5.3.0**（2026-10-16 09:07Z＝06:07 圣地亚哥，引入实验性 C agent／tinycbor／标准化 C2 协议）；其余（Sliver v1.7.8／nuclei-templates v10.5.0／nuclei v3.11.1／BloodHound v9.8.0／NetExec v1.5.1／Mythic v3.4.0.5／impacket 0.13.1）均早于本窗口，无新 release。Risky Business 首页突出 RB #855、Risky Bulletin「DataSuckers 俄罗斯被捕」与「Ledger/Trezor 间谍芯片」；tl;dr sec 最新 #350。
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接作狩猎用途。泄露、入侵、勒索类声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【KEV 新增 · 在野零日】BeyondTrust Remote Support CVE-2026-102764**（CWE-290 认证绕过/欺骗，CVSS 4.0 **9.3**，BT26-05）：未认证文件操作 → 主机级 root。Mandiant/GTIG 今日公开归因**疑似 PRC 背景的 ARMORY CASTLE（原 UNC5221，又名 WARP PANDA）**自 **2026-08-29** 起当零日利用，落 SAWFLY webshell、BARECLAW SOCKS5/WebSocket 隧道，抽 vault、改 haproxy、清日志。CISA **10-16** 收进 KEV，due **10-19**，要求 forensic triage。SaaS 已于 10-09 代补；自托管 24.3.1–26.2.3 须打 BT26-05-RS，更旧版本先升级。暴露窗口内设备按已入侵对待。
  X 原帖（Mandiant）：https://x.com/Mandiant/status/2111223164558614561
  X 原帖（THN）：https://x.com/TheHackersNews/status/2110989159330709932
  研究（GTIG/Mandiant）：https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust
  CISA：https://www.cisa.gov/news-events/alerts/2026/10/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
- **【KEV 新增 · 在野】Fortinet 多产品 CVE-2025-61624**（CLI 路径遍历 CWE-22，FG-IR-26-122，CVSS **6.0** Medium）：具 read-write 管理员权限者可经特制 CLI 参数任意写/删文件。虽为中危，但 Unit 42 证实其被用于在 FortiManager（FortiJump CVE-2024-47575）失陷后部署 **PEERSTITCH** 内存级 ARM64 植入体。CISA **10-16** 入列，due **10-19**，forensic triage。升到 FortiOS 7.4.10／7.6.5、FortiProxy 7.4.12／7.6.5、FortiSwitchManager 7.0.7／7.2.8；7.0/7.2/6.4 分支须迁移到固定版本。
  X 原帖（CISA）：https://x.com/CISACyber/status/2111156668570517912
  厂商：https://fortiguard.fortinet.com/psirt/FG-IR-26-122
  研究（Unit 42／THN）：https://thehackernews.com/2026/10/attackers-exploit-fortios-flaw-to.html
- **【APT 植入体】PEERSTITCH（CL-STA-0954）**：Unit 42 披露疑似国家级行动者在失陷电信 MSP 的 FortiManager（FortiJump 2024-47575）后窃取 500+ FortiGate 配置与密钥，再用 CVE-2025-61624 部署无落盘、不开端口、不外联的内存级 ARM64 植入体，hook `/bin/miglogd` 与 `/bin/iked`，对带特定标记（TCP 8550／169.254.0.1）的 VPN 会话绕过安全校验。
  X 原帖（THN）：https://x.com/TheHackersNews/status/2110960344638378030
  研究：https://securityaffairs.com/201077/malware/peerstitch-malware-how-attackers-compromised-500-firewalls-through-fortimanager.html
  下载服务器：`23.240.77[.]233:8085`
- **【KEV 临期提醒】Ivanti 104935 与 Windows 96951 今日（10-16）到期**；Ahsay 105133／105134、Cisco SEG 76519、PAN-OS 0322 明日（10-17）到期；Atlassian 21589 在 10-18。另有 Amber Wolf 披露 Ivanti Connect Secure 自定义登录页 RCE 补丁绕过（25.1.3.0 直接移除功能修复，无 CVE）。
  文章（THN Ivanti 续）：https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html
  X 原帖（Amber Wolf）：https://x.com/buffaloverflow/status/2111114886227120524
- **【供应链 · 短窗篡改】AOMEI Backupper（UNC7017）**：GTIG 披露攻击者在 2026-05~07 间以 **5–10 分钟** 短窗篡改 AOMEI 更新服务器上未签名的 `down_html.ini`／`Notifycfg.ini`，向 11 国落 CROSSROAD 下载器+SHINYROAD 后门（Radmin DLL 侧载），7-20 窗口还加入 WebDAV 1×1 像素弹窗偷 NetNTLMv2。厂商修服务器不清端点。
  X 原帖（THN）：https://x.com/TheHackersNews/status/2111137126469574835
  研究：https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering/
- **【广泛事件 · M365】ConnectWise Cloud Backup（原 SkyKick）**：Huntress 发出 RAPID RESPONSE，未知行动者滥用在 SkyKick 取得的访问向下渗透进客户 Microsoft 365；已见 100+ 受影响租户。ConnectWise 官方确认在查，源 IP `144.172.64[.]128`，UA `Python-urllib/3.12`、`python-requests/2.31`。应立即在 Entra 禁用应用 ID `506e08f9-6e9a-4da4-942b-a099a03644ae`。
  X 原帖（Huntress 串）：https://x.com/HuntressLabs/status/2111170005433815225
  厂商：https://www.connectwise.com/company/trust/advisories
- **【电商 RCE】Magento/Adobe Commerce BlockStrap CVE-2026-103849**（CVSS **10.0**，未进 KEV）：Sansec 披露二次模板引擎指令注入，攻击者在子邮件模板走私 `{{block}}` 被根级签名并再处理 → 未认证 PHP RCE。影响 9 月版至 Magento 2.4.9、Adobe Commerce B2B ≤1.5.3。Adobe 10-13 APSB26-153 修复但需手动打补丁、新装仍脆弱；须保留 9 月 StyleSmuggler 热修。暂未见在野，Sansec 预计很快大规模利用。
  X 原帖（BleepingComputer）：https://x.com/BleepinComputer/status/2111185724036784542
  厂商：https://helpx.adobe.com/security/products/magento/apsb26-153.html
  研究：https://sansec.io/research/blockstrap-magento-rce
- **【内核 · PoC】Linux「Infinity Core」六洞 + OpenBSD root**：@v4bel 披露 Linux 核心子系统 6 枚（Timer 98260／Signal 98256／MM 89754／Futex 80775／Scheduler 98385／SLAB 97941），5 枚有可用 root 利用，可 LPE/容器逃逸，并从普通 App root 三星 Galaxy S26 Ultra；均未进 KEV，须升至发行版固定内核。另 Calif 发布 OpenBSD 7.9 链 37 年老 shmat 整数溢出 + UAF 的 root PoC（9-14/9-30 已补，无 CVE、未见在野）。
  X 原帖（Infinity Core）：https://x.com/v4bel/status/2111125711054688759
  仓库：https://github.com/V4bel/InfinityCore
  文章（OpenBSD）：https://thehackernews.com/2026/10/researchers-demonstrate-openbsd-root.html
- **【统计】** X 合并 **162**（A4／B12／C18／LWiS128）；KEV **2026.10.16／1748／Δ+2**（BeyondTrust 102764、Fortinet 61624，均 due 10-19）；due_today **2**（Ivanti 104935、Windows 96951）；newly_overdue **0**；未来 7 天到期 **7**；红队工具 emp3r0r v5.3.0 新 release。

## CVE / POC / 漏洞

### X-1. 【KEV 新增 · 在野零日】BeyondTrust Remote Support CVE-2026-102764（未认证文件操作 → root）
昨晚（10-15）还是「未进 KEV 的在野零日」，今日 CISA **10-16** 正式收入 KEV，due **2026-10-19**，标 forensicTriage。改进起点仍是 Mandiant/GTIG 博文：CWE-290 improper origin validation，影响 Remote Support ≤26.2.3，未认证即可对设备做任意文件操作。ARMORY CASTLE（原 UNC5221／WARP PANDA）自 **2026-08-29** 起利用，TTP 与昨日一致（SAWFLY `mangoapi.php`、BARECLAW `ingredi_ws`、SUID `dbus-authd`、haproxy 改写、`/uidchanarge` WebSocket、清日志）。
**处置**：SaaS 已于 10-09 代补；自托管 24.3.1–26.2.3 打 BT26-05-RS（更旧先升级），PRA 共享代码亦有预防性补丁。暴露窗口（≥08-29）内互联网可达设备先取证快照→隔离→倾向重建；补丁后再轮换 appliance/API/Vault/SAML 凭据；因本地日志常被清，依赖集中遥测重建。
地址：
- X 原帖（Mandiant）：https://x.com/Mandiant/status/2111223164558614561
- X 原帖（THN）：https://x.com/TheHackersNews/status/2110989159330709932
- X 原帖（BleepingComputer）：https://x.com/BleepinComputer/status/2110978637646152121
- X 原帖（DFIR_Radar 技术串）：https://x.com/DFIR_Radar/status/2111080528627593511
- X 原帖（Nulltap）：https://x.com/Nulltap_/status/2111090754676539615
- X 原帖（watchTowr）：https://x.com/watchtowrcyber/status/2110877295825002979
- 研究（GTIG/Mandiant）：https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust
- 文章（Nulltap）：https://nulltap.sh/p/beyondtrust-armory-castle-root-persistence/
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/10/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 厂商（curl 403，供参考）：https://www.beyondtrust.com/trust-center/security-advisories/bt26-05
IoC（Mandiant 公开文件哈希，原样）：
- SAWFLY `mangoapi.php` SHA-256：`dc14e215269a93fdbc4c1a80b984c23faf7af0911c6dbb85309796a6f2ae95fb`
- BARECLAW `ingredi_ws` SHA-256：`1f19b9a27d79c11bda00a1e8faf74a7fdd683d38ccef1b60df2fd0307e3aa462`
- 路径/线索：`/uidchanarge`、SUID `dbus-authd`、`zz-root-persist`、haproxy backend `webskd3`、`app_84304470%2Ephp`

### X-2. 【KEV 新增 · 在野】Fortinet 多产品 CVE-2025-61624（CLI 路径遍历 → PEERSTITCH）
FG-IR-26-122：FortiOS／FortiPAM／FortiProxy／FortiSwitchManager 的 CLI 存在路径遍历（CWE-22），具管理员 read-write 权限者可经特制参数任意写/删文件。CVSSv3 **6.0 Medium**、Known Exploited **Yes**、2026-04-14 初次公布（已有 FMWP 虚拟补丁 FG-VD-59270.0day）。今日入 KEV（due 10-19）因 Unit 42 确认其用于投放 PEERSTITCH。
**修复版本**：FortiOS 7.6→7.6.5、7.4→7.4.10，7.2/7.0/6.4 迁移固定版；FortiProxy 7.6→7.6.5、7.4→7.4.12；FortiSwitchManager 7.0→7.0.7、7.2→7.2.8；FortiPAM 1.7→1.7.1 等。
地址：
- X 原帖（CISA）：https://x.com/CISACyber/status/2111156668570517912
- X 原帖（Python_s_ KEV 分类）：https://x.com/Python_s_/status/2111148983770845466
- X 原帖（DailyDarkWeb KEV 更新）：https://x.com/DailyDarkWeb/status/2111188020821209095
- 厂商：https://fortiguard.fortinet.com/psirt/FG-IR-26-122
- CISA：https://www.cisa.gov/news-events/alerts/2026/10/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
IoC：PEERSTITCH 侧见 X-7 的 APT/Malware 段（下载器 `23.240.77[.]233:8085`、标记 TCP 8550／169.254.0.1）。

### X-3. 【未进 KEV · CVSS 10】Magento/Adobe Commerce BlockStrap CVE-2026-103849
Sansec 披露二次模板引擎指令注入：子邮件模板中被走私的 `{{block}}` 指令在根级被签名并再处理，导致未认证 PHP RCE。补 StyleSmuggler（VULN-39341）留下的缺口。影响 9 月版至 Magento Open Source 2.4.9、Adobe Commerce ≤2.4.9、B2B ≤1.5.3。Adobe 10-13 APSB26-153 评 priority 2（30 天），Sansec 认为过低：24 小时内即构造出 4 条利用路径，预计很快大规模利用。**须打 2026-oct release 或 Adobe 隔离补丁，并保留 9 月 StyleSmuggler 热修；仅 Composer 安装不够。** 截至今日未见在野。
地址：
- X 原帖（BleepingComputer）：https://x.com/BleepinComputer/status/2111185724036784542
- X 原帖（Sansec 转述）：https://x.com/XavierRiveraX/status/2111186930847158282
- 厂商（Adobe APSB26-153）：https://helpx.adobe.com/security/products/magento/apsb26-153.html
- 研究（Sansec）：https://sansec.io/research/blockstrap-magento-rce
- 文章：https://www.bleepingcomputer.com/news/security/critical-blockstrap-flaw-lets-hackers-run-code-on-magento-servers/
狩猎：`grep -c resolveDeferredDirectives Filter/Template.php`（社区称 0 = 未打补丁，仅作参考，不作权威）。IoC：未见公开网络 IoC。

### X-4. 【未进 KEV · CVSS 10】GitLab CI/CD 正则整数溢出 RCE CVE-2026-97229
Rapid7 发技术分析：GitLab 自管 19.2–19.4.1 的 CI/CD 规则（Onigmo 正则引擎）存在整数溢出，未认证即可以 git OS 账号 RCE。升 GitLab CE/EE 19.4.2/19.3/19.2 补丁线。已有公开 PoC 仓库（仅作狩猎，本报告不转步骤）。
地址：
- X 原帖（Rapid7/2Workly）：https://x.com/2Workly/status/2111212059006583180
- X 原帖（r1cksec PoC）：https://x.com/r1cksec/status/2111071363951890908
- 研究（Rapid7）：https://www.rapid7.com/blog/post/ra-gitlab-ci-cd-regex-integer-overflow-technical-analysis-cve-2026-97229
- PoC 仓库（狩猎用）：https://github.com/jburgess-r7/CVE-2026-97229-PoC
IoC：未见公开 IoC。

### X-5. 【未进 KEV · 在野利用尝试】Langflow 命令注入 CVE-2026-105740 / MCP Stdio RCE（GHSA-7w94-79vh-5mr2）
Langflow 存在命令注入 RCE（CVSS 9.9）：任意已认证用户添加 "Stdio" 传输的 MCP server 即可让用户提供的 command 无校验直接执行（含 `PATH`/`LD_PRELOAD` 环境变量注入）。蜜罐自 10-11 起已见 **1,706** 次利用尝试，持续上升。**升至 1.9.0+（厂商公告修复版）/1.10.3+，设 `LANGFLOW_AUTO_LOGIN=false`，勿暴露公网。** VulnCheck 另报 Langflow CVE-2026-5027／CVE-2026-51886 在野。
地址：
- X 原帖（AiCloudConsult）：https://x.com/AiCloudConsult/status/2111079906226454784
- X 原帖（samilaiho GHSA）：https://x.com/samilaiho/status/2110972024432545846
- GHSA：https://github.com/langflow-ai/langflow/security/advisories/GHSA-7w94-79vh-5mr2
- 文章：https://cyberworldops.eu/en/langflow-command-injection-draws-exploitation-attempts-as-version-190
IoC：未见公开网络 IoC（以 MCP server 异常创建与 `/api/v2/mcp/servers` 调用为狩猎点）。

### X-6. 【未进 KEV · 临期提醒】Ivanti 104935 / Windows 96951（今日到期）+ PAN-OS / Cisco SEG / Ahsay（明日）
两条 due **10-16**：Ivanti Connect Secure CVE-2026-104935（认证绕过，升 22.8R2.5／25.1.3.x 并查失陷，ICT 可能漏检）、Windows Shell MotW 绕过 CVE-2026-96951。明日 due（10-17）：PAN-OS 0322（已认证高权限管理面代码注入，IoC IP `66[.]42[.]72[.]14`、`208[.]83[.]239[.]114`、`149[.]248[.]47[.]234`）、Cisco SEG 76519（附件路径遍历→root，升 AsyncOS 15.5.5-014 或 16.5.0-780）、Ahsay 105133/105134（热修 10.3.4.45／9.15.2.70）。另 Avertium 提示旧 KEV PAN-OS GlobalProtect CVE-2026-0257（已逾期，Qilin/Settra 勒索在野）。Amber Wolf 披露 Ivanti 自定义登录页 RCE 补丁绕过（25.1.3.0 直接移除功能、无 CVE）。
地址：
- X 原帖（THN Ivanti）：https://x.com/TheHackersNews/status/2110832582812369295
- X 原帖（Amber Wolf Ivanti 绕过）：https://x.com/buffaloverflow/status/2111114886227120524
- X 原帖（Avertium PAN-OS 0257）：https://x.com/Avertium/status/2111102364333551992
- 厂商（PAN 0322）：https://security.paloaltonetworks.com/CVE-2026-0322
- 文章（Amber Wolf）：https://blog.amberwolf.com/blog/2026/october/ivanti-custom-signin-page-rce/
- 文章（Avertium）：https://www.avertium.com/flash-notices/palo-alto-networks-globalprotect-authentication-bypass-ransomware-groups-actively-exploiting
IoC（PAN 0322，原样）：`66[.]42[.]72[.]14`、`208[.]83[.]239[.]114`、`149[.]248[.]47[.]234`

### X-7. 【未进 KEV · 多条高危】FortiSandbox 107656 / Cisco NX-OS / NGINX / Theme My Login / Windows WPAD / Plex
- **FortiSandbox GUI 认证绕过 CVE-2026-107656**（FG-IR-26-185，CVSS **9.6 Critical**，Known Exploited **No**）：未认证特制 HTTP 请求绕过登录→执行代码。升 FortiSandbox 5.0.7／4.4.10（PaaS 同），4.4 PaaS 迁移；限 GUI 仅管理网可达，无虚拟补丁。
- **Cisco NX-OS Nexus 3000/9000**：Cisco 发公告（NX-API RCE，cisco-sa-napi-rce-r2shwu2j；本地抓取 TLS 中断，链接作狩猎）。
- **F5 NGINX**：修 11 个问题含 3 枚关键未认证 RCE（CVE-2026-15176、CVE-2026-93479 等）；Juniper 同周 17 条公告 150+ 洞，暂未见在野。
- **WordPress Theme My Login CVE-2026-89079**：多站点+用户自选注册密码场景的未认证账户接管，已有 PoC（狩猎用）。
- **Windows WPAD LPAC CVE-2026-85884**：whesvc 信任 Diagnostics.Lua ETW 事件→以 LocalSystem 跑攻击者 Lua，低权→SYSTEM，有 PoC。
- **Plex 未认证 RCE 链**（$500 赏金，zm_0x 写作+PoC，狩猎用）。
地址：
- X 原帖（FortiSandbox/Nulltap）：https://x.com/Nulltap_/status/2111045352103035337
- X 原帖（Cisco NX-OS/Dinosn）：https://x.com/Dinosn/status/2111162425152094412
- X 原帖（NGINX/securityaffairs）：https://x.com/securityaffairs/status/2111089131195416649
- X 原帖（Theme My Login/DarkWebInformer）：https://x.com/DarkWebInformer/status/2111160588399268175
- X 原帖（WPAD/_MrNiko）：https://x.com/_MrNiko/status/2110924775136919745
- X 原帖（Plex/zm_0x）：https://x.com/zm_0x/status/2111138023543108005
- 厂商（FortiSandbox）：https://fortiguard.fortinet.com/psirt/FG-IR-26-185
- 厂商（Cisco NX-OS）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-napi-rce-r2shwu2j
- 文章（NGINX）：https://securityaffairs.com/201106/security/f5-addressed-critical-rce-flaws-in-nginx.html
- PoC（Theme My Login，狩猎用）：https://github.com/murrez/CVE-2026-89079
- PoC（WPAD，狩猎用）：https://github.com/Beardhammer/CVE-2026-85884
IoC：未见公开网络 IoC。

### X-8. 【PoC 披露】Linux「Infinity Core」六洞 / OpenBSD 7.9 root / Galaxy S26 Ultra
@v4bel（Project Zero 风格）披露 Linux 内核核心子系统 6 枚：Timer **CVE-2026-98260**、Signal **CVE-2026-98256**、MM **CVE-2026-89754**、Futex **CVE-2026-80775**、Scheduler **CVE-2026-98385**、SLAB **CVE-2026-97941**；前五可 LPE/容器逃逸，其一从普通 App root 三星 Galaxy S26 Ultra（Android LPE）。测试于 Ubuntu 26.04 7.0.0-30-generic 与 Arch 7.2.x，均已有上游修复提交；均未进 KEV。另 Calif 发布 OpenBSD 7.9 链 shmat(4) 37 年整数溢出 + 引用计数 UAF 的 root PoC（绕 KARL/SMAP/SMEP，9-14 syspatch/9-30 errata 026 已修，无 CVE、未见在野）。防御向：升发行版固定内核并重启；本报告不转利用步骤。
地址：
- X 原帖（Infinity Core）：https://x.com/v4bel/status/2111125711054688759
- X 原帖（IntCyberDigest 摘要）：https://x.com/IntCyberDigest/status/2111219804585508964
- X 原帖（OpenBSD/Dinosn）：https://x.com/Dinosn/status/2111170480208277690
- 仓库（Infinity Core，狩猎/修复参照）：https://github.com/V4bel/InfinityCore
- 文章（OpenBSD）：https://thehackernews.com/2026/10/researchers-demonstrate-openbsd-root.html
IoC：未见公开网络 IoC（本地/访客侧触发）。

## 工具与 GitHub 发布

- **emp3r0r v5.3.0**（2026-10-16 06:07 圣地亚哥）：本窗口唯一命中的监控红队工具新 release——引入实验性 **C agent**（musl libc、so/PIC 格式、C agent builder）、改用 **tinycbor**、标准化 C2 协议、BOF loader 模块化。仓库：https://github.com/jm33-m0/emp3r0r/releases/tag/v5.3.0
- 其余监控项（**nuclei v3.11.1／nuclei-templates v10.5.0／Sliver v1.7.8／BloodHound v9.8.0／NetExec v1.5.1／Mythic v3.4.0.5／impacket 0.13.1**）：**无新 release**（相对昨日）。
- X 社区分享（防御/实验室向，仅链接，不转利用教程）：
  - **TornadoC2**——拉取式 C2，十种传输、ECDSA 签名任务、Qt/CLI 控制台、RBAC/审计链：https://x.com/ipurple/status/2111212812458750369 ；https://github.com/kamalx06/TornadoC2
  - **Apex C2**——带原生 agentic AI 操作接口（可接 MCP LLM）的 C2 框架：https://x.com/ipurple/status/2111051788145086626 ；https://phantomsec.tools/blog/apex-c2-v04-release
  - **ReflectivePluginLoader**（内存反射加载/模块踩踏）：https://x.com/ipurple/status/2110995566452945329 ；https://github.com/racoten/ReflectivePluginLoader
  - **cuban-eight**（把 PE 打包成伪装 WSL 发行版安装器）：https://x.com/ipurple/status/2111198690320793728 ；https://github.com/shaheeryasirofficial/cuban-eight
  - **docker-cobaltstrike**（CS Teamserver Docker 容器）：https://x.com/ipurple/status/2111158790233981205 ；https://github.com/chryzsh/docker-cobaltstrike
  - **KnockGiga**（Gigabyte 内核驱动 LPE）：https://x.com/Dinosn/status/2111154885492445511 ；https://github.com/mein-0/KnockGiga
  - **Sly**（@layle_ctf 多系统模拟器+调试器，RE/pwn 向，非武器）：https://x.com/layle_ctf/status/2111133651450961988 ；https://github.com/ioncodes/sly
- 防御/审计向 PowerShell（@ipurple 分享）：IDWolf（AD/Entra 卫生审计）、HostBadger（主机加固审计）——仅索引，略。

## APT / Malware 分析

### M-1. ARMORY CASTLE × BeyondTrust（见 X-1）
完整 TTPs／YARA／IoC 见 GTIG 博文与 DFIR_Radar 技术串。Mandiant 评中高置信，与该组此前利用 Citrix NetScaler、Ivanti Connect Secure 边缘设备一致。

### M-2. PEERSTITCH / CL-STA-0954（Fortinet，见 X-2）
Unit 42：失陷电信 MSP 的 FortiManager（FortiJump CVE-2024-47575）后窃 500+ FortiGate 配置/密钥 → 用 CVE-2025-61624 落无落盘内存级 ARM64 植入体，hook `/bin/miglogd`+`/bin/iked`，经进程内存桥通信，对带标记 VPN 会话绕校验；另借 mod_md 开 SSH 反向壳。
地址：
- X 原帖：https://x.com/TheHackersNews/status/2110960344638378030
- 研究：https://securityaffairs.com/201077/malware/peerstitch-malware-how-attackers-compromised-500-firewalls-through-fortimanager.html
IoC（原样）：下载服务器 `23.240.77[.]233:8085`（a.js/index.js、a.wasm/index.wasm、dd/lldprx 等）；内存标记 TCP `8550`、IP `169.254.0.1`。

### M-3. AOMEI Backupper 短窗供应链（UNC7017，见「今日摘要」）
GTIG：三次篡改窗（05-28 10 分、07-16 6 分、07-20 5 分）→ CROSSROAD 下载器写 `RadminComponentRuntime` 计划任务（每 3 小时）→ FamItrfc.exe 侧载 BlkScrDl.dll → SHINYROAD（PocketPy 字节码，beacon 8.218.65[.]184:443）；后续 ADAPTAGENT（Adaptix C2，NitroRuntime，8.210.84[.]56:6800）。07-20 加 WebDAV 像素弹窗偷 NetNTLMv2。CROSSROAD 遇 CN locale 即停。11 国受影响（AU/BR/IN/PK/PT/SG/ZA/ES/CH/TR/US）。
地址：
- X 原帖（THN）：https://x.com/TheHackersNews/status/2111137126469574835
- X 原帖（DFIR_Radar 技术串）：https://x.com/DFIR_Radar/status/2111110629012439547
- 研究：https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering/
- 文章：https://thehackernews.com/2026/10/attackers-tampered-with-aomei.html
IoC（GTIG，原样）：域名 `storage-data[.]com`／`promotion.storage-data[.]com`／`aomei.storage-data[.]com`；IP `8.210.84[.]56`、`8.218.65[.]184`、`47.239.60[.]117`、`96.126.191[.]98`；CROSSROAD `upgrade-now.exe` SHA-256 `9a58e8f49edf5644e5728f74cf36f560d3d486fa51db4db69d927963c7aca450`；Notifycfg.ini SHA-256 `d2f9ef2429312667f0512504b6a19ba4a9cc5514f1b2933923dd42f75a1c5934`；计划任务 `RadminComponentRuntime`／`NitroRuntime`。

### M-4. APT29 CaptiveCrunch（SentinelOne）
SentinelOne：APT29 在受害者同一 L2 网段用本地 LLMNR 投毒（UDP/5355，DnsPoison）+ Windows captive-portal 检查改写→默认浏览器打开攻击页→手动下载 CornFlake（Go RAT）→ ChocoShell（内存 PowerShell 窃取器，偷 Chrome ABE cookie、M365/Entra token，三连 UAC 绕过）。狩猎法：按应答 IP 归并不相关域名所有者数量（该组一个 IP 为 ~128 个不相关机构应答，含 Adobe/Apple/Akamai/AnyDesk/BeyondTrust/Microsoft）。立即用 GPO 禁 LLMNR。
地址：
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2111201397295153245
- 研究：https://www.sentinelone.com/blog/how-sentinelone-blocked-apt29-s-captivecrunch-campaign/

### M-5. UAT-11985（Cisco Talos，台湾目标 AitM）
Chinese-nexus UAT-11985 对台湾研究/政策机构 AI 辅助鱼叉+二维码篡改（quishing），仿 Google 表单登录页，JS 先回传设备指纹（`google_login_start`），提交凭据（`google_login_check`）并经 WebSocket 与 Google 实时中继夺 MFA token；面板仅支持 zh-CN/zh-TW/en。账户接管后须吊销全部会话、审计 OAuth 授权（仅重置密码不够）。
地址：
- X 原帖（THN）：https://x.com/TheHackersNews/status/2111130365557711346
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2111216906292330866
- 文章：https://thehackernews.com/2026/10/uat-11985-uses-fake-event-invites-to.html

### M-6. Silent Ransom Group 泄露内部聊天（GuidePoint GRIT）
GuidePoint 审 5,692 条 Rocket.Chat 记录：Silent Ransom Group（Luna Moth／Chatty Spider／UNC3753）无恶意软件、无漏洞，用电话冒充 IT + 持伪造美国证件物理闯入美国大型律所，经 AnyDesk/Zoho Assist 连接、U 盘外带到 Google Drive/SSH；自称 2026-04 起从 27 家机构收 $206.95M（中位 $600 万）。检测面在流程与物理，非端点。
地址：
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2111170994664779863
- 研究：https://www.guidepointsecurity.com/blog/silent-ransom-group-leaked-chats/
IoC（原样）：Rocket.Chat `aim6umein3kee[.]com`、`slplsskdj2836v2jjsx[.]com`；RDP `45.32.232[.]133:2895`；SSH `199.217.98[.]21`、`216.203.20[.]157`；伪装域 `sokolovsky-law[.]com`、`ominetdata[.]com`、`develevenor[.]com`、`funconnect[.]com`。

### M-7. 其他恶意软件/活动
- **GhostAction 冒名活动（Jamf/OSS Malware）**：GhostAction copycat 把窃取器藏进假 `.woff2` 字体（`fa-solid-400.woff2`），由隐藏 VS Code task（`.vscode/tasks.json`）在打开项目时执行，900+ 仓库，cron 每 5 分钟拉取执行。
- **Nextron .NET WebSockets 后门下载器**：C++ 原版的 C#（.NET 8）变体，同 7 文件、同 NVIDIA 伪装，payload 服务器同为 `153.75.247[.]94`。
- **QuartzLine（Expel）**：可用 PDF 阅读器内藏后门，偷 Chrome 浏览历史并投 Caira RAT。
- **WKLP（ANY.RUN）**：针对美/法政府的 Python 窃取器/RAT，加 Defender 排除项、伪装防火墙规则，C2 `relay[.]wklp-searcher[.]xyz`。
- **假 Active Call Python RAT（@devmihaylov）**：阶段二 `msvci[.]com/files/.ini`、下载服务器 `45[.]61[.]139[.]149`、C2 `g[.]obrn[.]cc`、操作服务器 `64[.]7[.]199[.]7`。
- **malwrhunterteam 开放目录/域名线索**：`158.94.210[.]145`（cloudeliverrs[.]com／debiandelivr[.]com 等十余域）、`154.6.145[.]213`「SKYNET C2」、`191.96.25[.]24`「WHisKEY」面板；FUD 后门伪造 LAPD 证书约 26k。
- **ARTEX（AhnLab ASEC，站点超时）**：中国 AI 辅助渗透框架碎裂为 ScopeWeaver/Tangora/Horda 等 ≥6 分支，一操作者配 Magento CVE-2026-75650 利用+IRC PHP implant。
- **Volexity Mind the (Patch) Gap Part 3**：中国多团伙链 Chrome+Windows 零日投毒；博文展示 Volcano 的 MCP AI 辅助 DFIR，示例恶意域 `cloud.shinewrist[.]net`。
地址：
- https://x.com/JamfThreatLabs/status/2111099159449108776 ；https://opensourcemalware.com/blog/ghostaction-copycats-polinrider-by-hiding-a-stealer-in-a-fake-font-file
- https://x.com/nextronresearch/status/2111148818129383922 ；https://github.com/NextronSystems/iocs
- https://x.com/DailyDarkWeb/status/2111058135582466473 ；https://expel.com/blog/quartzline-a-working-pdf-viewer-with-a-backdoor-inside/
- https://x.com/anyrun_app/status/2111065442093572527
- https://x.com/devmihaylov/status/2111185200369852851
- https://x.com/malwrhunterteam/status/2111017138790056108
- https://x.com/Volexity/status/2111164698091766026 ；https://www.volexity.com/blog/2026/10/16/mind-the-patch-gap-part-3-analysis-with-volexity-volcano-threat-intel-and-mcp/

### M-8. 泄露与事件（部分 UNCONFIRMED）
日本电商/会员泄露今日集中披露（官方确认）：
- E-store Shopserve ≈2335.6 万（7,858 店）：https://estore.jp/press/20261016/
- Nikkei（日本经济新闻社）≈183 万（云开发环境被未授权访问）：https://www.nikkei.co.jp/nikkeiinfo/news/information/1561.html
- Yamato「Kuroneko 延付」≈526 万（+5 万配送/4,100 商户）：https://www.yamato-hd.co.jp/important/info_260929_1.html
- NTT Solmare Comic Seima（含 email+哈希密码）：https://www.nttsolmare.com/press/2026/1016.html
- Beauty Garage 775,725（哈希密码）：https://www.beautygarage.jp/topics/news_unauthorizedaccess2026
- FANCL/ATENEA ≈78.5 万：https://www.fancl.jp/news/pdf/husei.pdf
- WASABI SWITCH（订单数据外泄，已被用于钓鱼）：https://wasabi-inc.biz/help/news/20261016-01/
- Studio.design（客户数据+API 凭据，功能漏洞）：https://studio.design/ja/whats-new/unauthorized-access-2026-10
- 续报：Burger King Japan ≈1118 万、BAE→美国破产法院中断、CenterPoint ≥106 万德州、COPC（俄亥俄）≈140 万（vishing）。
声称类（**UNCONFIRMED**）：SBI（印度）37.5 万 CSV/2,722 PDF、ManoMano ≈17.8 万、Baydöner（土）130 万、Sinaloa（墨）≈100 万、ShinyEquationCartel 众筹零日售卖等。
地址（续报/声称）：
- https://x.com/DailyDarkWeb/status/2111203025855611159 （Shopserve）
- https://x.com/DailyDarkWeb/status/2111148562721493472 （Nikkei）
- https://x.com/BleepinComputer/status/2111065060541903188 （BK Japan）
- https://x.com/DailyDarkWeb/status/2110997062745567663 （COPC vishing）
- https://x.com/sudhakarudumula/status/2111122549031796738 （SBI，UNCONFIRMED）

## 地址／IoC 汇总

| 主题 | IoC／狩猎信号 | 来源 |
|------|----------------|------|
| BeyondTrust／ARMORY CASTLE | SHA256 `dc14e215…ae95fb`（SAWFLY）、`1f19b9a2…3aa462`（BARECLAW）；`/uidchanarge`；SUID `dbus-authd`；`zz-root-persist` | GTIG |
| PEERSTITCH（Fortinet 61624） | 下载器 `23.240.77[.]233:8085`；内存标记 TCP `8550`、IP `169.254.0.1`；hook `/bin/miglogd`、`/bin/iked` | Unit 42 |
| AOMEI／UNC7017 | `storage-data[.]com`、`8.210.84[.]56`、`8.218.65[.]184`、`47.239.60[.]117`、`96.126.191[.]98`；SHA256 `9a58e8f4…aca450`；任务 `RadminComponentRuntime`/`NitroRuntime` | GTIG |
| ConnectWise Cloud Backup（SkyKick） | 源 IP `144.172.64[.]128`；UA `Python-urllib/3.12`、`python-requests/2.31`；禁 Entra 应用 `506e08f9-6e9a-4da4-942b-a099a03644ae` | Huntress/ConnectWise |
| APT29 CaptiveCrunch | 一个 IP 为 ~128 个不相关机构应答；CornFlake/ChocoShell；LLMNR UDP/5355 | SentinelOne |
| Silent Ransom Group | `aim6umein3kee[.]com`、`slplsskdj2836v2jjsx[.]com`、`45.32.232[.]133:2895`、`199.217.98[.]21`、`216.203.20[.]157` | GuidePoint |
| GhostAction copycat | `fa-solid-400.woff2`；`193.32.204[.]199:8080`；标记 `eslint-check`/`DEVBOX`/`#ghc2` | Jamf/OSS |
| Nextron .NET Downloader | SHA256 `7a0ce150…f843c9`、`d1721384…e7f74f`；`153.75.247[.]94`、`www.xionamiconm[.]com` | Nextron |
| QuartzLine | `beatramiro[.]com`、`healskills[.]com`、`motherotters[.]com` 等；SHA256 `069fd1e7…c0527` 等 | Expel |
| WKLP | `relay[.]wklp-searcher[.]xyz` | ANY.RUN |
| 假 Active Call RAT | `msvci[.]com`、`45.61.139[.]149`、`g[.]obrn[.]cc`、`64.7.199[.]7` | @devmihaylov |
| malwrhunterteam | `158.94.210[.]145`、`154.6.145[.]213`、`191.96.25[.]24`、`debiandelivr[.]com` | X |
| PAN-OS 0322 | `66[.]42[.]72[.]14`、`208[.]83[.]239[.]114`、`149[.]248[.]47[.]234` | Palo Alto |
| Volexity | `cloud.shinewrist[.]net` | Volexity |
| Atlassian／BlockStrap／GitLab／Langflow／Infinity Core 等 | 未见公开网络 IoC | — |

其余条目：**未见公开 IoC**。

## LWiS 固定信源（每日交叉，不替代 X Latest）

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

本轮 LWiS 交叉：List 500 成员分 10 段 `from:` 全量翻查，命中高信号条目已并入上文（emp3r0r v5.3.0、Infinity Core/@v4bel、TornadoC2/Apex/ReflectivePluginLoader/@ipurple、Amber Wolf Ivanti 绕过/@buffaloverflow、layle_ctf Sly、Volexity Volcano、watchtowr BeyondTrust、Nulltap FortiSandbox/Cisco/BeyondTrust、cyb3rops/vxunderground 等）。Risky Business 首页：RB #855「ShinyHunters」、Risky Bulletin「DataSuckers 俄被捕」「Ledger/Trezor 间谍芯片」；tl;dr sec 最新 #350。

## 来源搜索 URL

- X A（CVE 去噪）：`https://x.com/search?q=(CVE-2026%20OR%20CVE-2025)%20(exploit%20OR%20PoC%20OR%20RCE%20OR%20KEV%20OR%20zero-day)%20-is%3Aretweet&src=typed_query&f=live`
- X B（GitHub 工具）：`https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20PoC)%20-is%3Aretweet&src=typed_query&f=live`
- X C（威胁分析）：`https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)%20-is%3Aretweet&src=typed_query&f=live`
- X 专题（BeyondTrust/Fortinet KEV）：`https://x.com/search?q=(CVE-2026-102764%20OR%20CVE-2025-61624)&src=typed_query&f=live`
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
