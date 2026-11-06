# X 安全情报晚报 · 2026-11-03

覆盖窗口：2026-11-02 20:15 至 2026-11-03 20:15（America/Santiago，UTC-3），约 24 小时。X 只读读取 9 次（主题检索 4 次、LWiS 成员检索 3 次（覆盖 500 个成员中的前 150 个）、指定帖批量查询 2 次），0 次 429；所收帖子均为本窗口新帖，不与 seen_ids 重复。t.co 均已从卡片展开（只有图片的帖只列原帖）。公开备援：CISA KEV JSON（**2026.11.03，共 1767 条，Δ+1**）、NVD、厂商与研究机构页面。IoC 一律 defang。本报告为防御向，不转载利用代码、payload 或复现步骤。

## 今日摘要

- **KEV 新增 WordPress Core CVE-2026-119977（11-03 加入，due 11-06，要求取证排查）**：4.7.0–7.1.3 在核心升级窗口存在 TOCTOU 竞态，可让未认证者在服务器执行代码；10-28 发布的 **WordPress 7.1.4** 已修复。X 上 cve.now、Enclave Radar 均报在野利用。
- **Zyxel GS1900 交换机：原 KEV 补丁无效**。Binarly 发现被归因到 CVE-2026-7273（9-21 进 KEV）的在野利用其实打的是另一个未修漏洞，Zyxel 已为此发新修复 **CVE-2026-107441**。已经「打过 7273 补丁」的设备仍需再升级。
- **Siemens SIMATIC IoT2050 Advanced（Node-RED）CVE-2026-58115（CVSS 10）在野利用**：VulnCheck 蜜罐自 10-30 起观测到投放 Linux bot 与隐藏后门；修复 V4.3.4.1+，否则移除 Node-RED。未进 KEV。带 C2 IP（见 IoC）。
- **Android 11 月公告**：Framework 零点击 RCE CVE-2026-58868（Critical），补丁级别 2026-11-01 起修复，建议 2026-11-05；未见在野、无公开 PoC。
- **KEV 到期**：今日（11-03）Plex Media Server 96652／96655、Siemens Software Center 110936；11-06 WordPress 119977。Ivanti 111357 自 11-03 起逾期，GitLab 97229／Cisco 76418 继续逾期（X 上称 Shadowserver 仍见 1000+ 台未修 GitLab）。
- **PHP2Shell 狩猎**：DFIR Radar 整理检测要点（内存耗尽报错＋PHP-FPM SIGSEGV 为最早信号、`.user.ini` 的 `auto_prepend_file` 持久化）。
- **APT**：Kimsuky（APT43）点号填充 LNK 钓鱼（Operation GitPower／HTTPSpy）检测分析；携程 4.01 亿条数据暗网叫卖（未证实）。
- **工具**：Noriben v2.1.0 恶意软件沙箱、MalChela v4.5.0 接入 ScanMalware 查询。

## CVE / POC / 漏洞

### 1. WordPress Core CVE-2026-119977：今日进 KEV（due 11-06）
CISA 描述：全量包核心升级时使用可预测、可 Web 访问的暂存路径，导致 TOCTOU 竞态，未认证攻击者可在升级窗口内执行代码（CWE-367）。影响 4.7.0–7.1.3；WordPress 7.1.4（10-28 发布）修复了该升级流程缺陷（报告者 Umut Bayram），同版本还修了多处存储型 XSS。KEV 标注需做取证排查（Forensic Triage: Yes）。处置：确认所有站点已到 7.1.4（自动后台更新的站点通常已升级），检查升级期间的异常 PHP 文件与新增管理员。注意 cve.now 帖写「No patch listed yet」与 WordPress 官方公告不符，以官方 7.1.4 为准。
- X 原帖：https://x.com/cvedotnow/status/2117721119788581350
- X 原帖：https://x.com/EnclaveRadar/status/2117719948806037655
- X 原帖：https://x.com/valtryltd/status/2117723814406565925
- 厂商公告：https://wordpress.org/news/2026/10/wordpress-7-1-4/
- 文章（Wordfence）：https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-core/wordpress-core-470-713-unauthenticated-upgrade-window-staged-installer-remote-code-execution
- 文章：https://cve.now/CVE-2026-119977
- 文章：https://app.enclave.ai/threat-feed/CVE-2026-119977
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-119977
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-119977
- 地址／IoC：未见公开 IoC

### 2. Zyxel GS1900 交换机：在野 0day 绕过 CVE-2026-7273 补丁，新编号 CVE-2026-107441
Binarly 称：针对 GS1900 的在野 RCE 原被关联到 CVE-2026-7273（KEV 9-21 加入，CGI 栈溢出，局域网未认证），但该补丁挡不住实际利用；攻击者用的是另一处未修漏洞，经 Binarly 报告后 Zyxel 发布新修复并分配 CVE-2026-107441（Binarly 编号 BRLY-2026-057）。处置：按 Zyxel 新公告再次升级，管理界面只对可信管理网段开放；不要以「已修 7273」作为安全依据。
- X 原帖：https://x.com/binarly_io/status/2117651602823598202
- 文章（Binarly）：https://www.binarly.io/blog/zyxel-gs1900-rce-cve-2026-107441
- 厂商／研究公告（Binarly）：https://www.binarly.io/advisories/brly-2026-057
- 厂商公告（Zyxel，7273 原公告）：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-107441
- 地址／IoC：未见公开 IoC（帖内未列）

### 3. Siemens SIMATIC IoT2050 Advanced（Node-RED）CVE-2026-58115：在野利用
CVSS 10，Node-RED HTTP 接口缺少认证，未认证者可创建并触发流程以 root 执行代码。VulnCheck 蜜罐至 10-30 记录多次利用：下载 AMD64 Linux 二进制从内存路径执行，部分用两段式下载器 `wget.sh`，另有加入恶意 `/cmd` 端点接 exec 节点的持久化。补丁自 8 月已出：V4.3.4.1 或更高；无法升级则移除 Node-RED 或强制 HTTPS＋强认证。未进 KEV。狩猎：Node-RED 派生的 wget/curl 进程、`/dev/shm/.b`、`/tmp/.kworker`、异常 flow。
- X 原帖：https://x.com/phantmradar/status/2117502019183525937
- X 原帖：https://x.com/BadgerSignalHQ/status/2117571235496521886
- X 原帖：https://x.com/ZeroDayFacts/status/2117571903670092108
- X 原帖：https://x.com/Daily_CyberSec/status/2117410979717996944
- X 原帖：https://x.com/DIYprojects55/status/2117692745372573825
- 文章：https://badgersignal.com/articles/active-exploitation-of-siemens-simatic-iot2050-advanced-nodered-authentication-flaw-cve202658115
- 文章：https://securityonline.info/node-red-rce-vulnerability-cve-2026-58115/
- 文章：https://pbxscience.com/siemens-industrial-gateway-flaw-exploited-in-the-wild-persistent-backdoors-found-after-reboot/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-58115
- 地址／IoC（引自 Badger Signal 转述 VulnCheck）：C2 `85.215.73[.]250`、`45.194.90[.]57:38472`；文件 `/dev/shm/.b`、`/tmp/.kworker`；下载器名 `wget[.]sh`

### 4. Android 11 月安全公告：Framework 零点击 RCE CVE-2026-58868
FrameDecoder.cpp 的 onOutputReceived 处理媒体帧时堆越界写，无需额外权限或用户交互即可远程代码执行。影响 Android 14／15／16／16 QPR2／17。补丁级别 2026-11-01 修复，建议直接到 2026-11-05（含内核与硬件组件修复）。无公开 PoC、未见在野。
- X 原帖：https://x.com/DarkWebInformer/status/2117756247344927078
- 厂商公告：https://source.android.com/docs/security/bulletin/2026/2026-11-01
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-58868
- 地址／IoC：未见公开 IoC

### 5. PHP2Shell（CVE-2026-109618／109619）检测与处置整理
DFIR Radar 基于一份 6 条事件的日志样本整理：最早信号是 PHP「Allowed memory size exhausted」致命错误＋PHP-FPM 子进程 SIGSEGV，随后 php-fpm（www-data）拉起 `/dev/shm/.s` 脚本与反弹 shell，持久化为上传目录下 `uploads/.cache.php`，通过 `.user.ini` 的 `auto_prepend_file` 每次请求加载。修复版本 8.5.12／8.4.27／8.3.36／8.2.35 且必须重启所有 PHP worker；7.4／8.0／8.1 无官方修复。另一个会话上传进度向量 CVE-2026-115560（非 PHP2Shell）临时缓解为 `session.upload_progress.enabled = 0`。疑似先于补丁被打的主机按已失陷处理，保全 `/dev/shm`（重启即清空），轮换 www-data 可读的所有凭据。
- X 原帖：https://x.com/DFIR_Radar/status/2117648671823036780
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-109618
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-109619
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-109618
- 地址／IoC（日志样本中出现，原样 defang）：`198.51.100[.]23:4444`（注意：198.51.100.0/24 是 RFC 5737 文档保留段，多半是脱敏示例，不宜直接当真实 C2 封堵依据）；路径 `/dev/shm/.s`、`uploads/.cache[.]php`、`.user.ini`（`auto_prepend_file`）

### 6. Ivanti／GitLab／Cisco 跟进与「旧闻翻炒」提醒
- Ivanti Connect Secure：Rapid7 ETR 被大量转发；Read the Diff 提醒以「实际运行版本」对照 10-30 更新后的受影响范围，而不是看上次打补丁的日期（需 25.1.1.3／22.8R2.6）。KEV 中 111357 已于 11-02 到期，**今起逾期**；118527 due 11-13。
- GitLab CVE-2026-97229：X 帖称 Shadowserver 仍见 1000+ 台未修（未找到 Shadowserver 原始链接，数字待核实）。
- Morphisec 今日推送的 F5 BIG-IP APM CVE-2026-94127（KEV 9-22 加入）和 UTA0565 Chrome＋ALPC 0day 链（85046／87491／85880，9 月）均为旧事件回顾，不是新进展；BleepingComputer 的 Cisco ASA/FTD DoS 0day 链接也是旧文被重发。
- X 原帖：https://x.com/read__the__diff/status/2117713630074634696
- X 原帖：https://x.com/RoryCrave/status/2117737992857202709
- X 原帖：https://x.com/rst_cloud/status/2117661385194705183
- X 原帖：https://x.com/gilles_ac/status/2117579998865559745
- X 原帖：https://x.com/morphisec/status/2117675699293020313
- X 原帖：https://x.com/morphisec/status/2117692055136751748
- X 原帖：https://x.com/so_sthbryan/status/2117685490207883343
- 文章（Rapid7）：https://www.rapid7.com/blog/post/etr-additional-ivanti-connect-secure-zero-days-exploited-in-the-wild-cve-2026-111357-cve-2026-118527/
- 文章：https://www.bleepingcomputer.com/news/security/cisco-warns-of-firewall-zero-day-exploited-to-crash-ssl-vpn-devices/
- 厂商公告（F5）：https://my.f5.com/manage/s/article/K000162605
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-111357
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-97229
- 地址／IoC：未见公开 IoC

### 7. KEV 状态
目录 2026.11.03（发布 2026-11-03T20:00Z）共 1767 条，Δ+1：WordPress Core CVE-2026-119977（due 11-06）。**今日 11-03 到期**：Plex Media Server CVE-2026-96652／96655、Siemens Software Center CVE-2026-110936。之后：11-06 WordPress 119977；11-10 Magento 48356、Brotli 111497；11-11 VMware ESX 41709；11-13 Ivanti 118527。**逾期**：Ivanti 111357（11-02）、GitLab 97229 与 Cisco ASA/FTD 76418（11-01）、Fragnesia 46300（10-31）、PHP2Shell 109618／109619（10-29）等。ThreatPodium 当日报告称「6 new KEVs」为其统计周期口径，以 KEV JSON 为准。
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- X 原帖：https://x.com/threatpodium/status/2117447240692162612
- 文章：https://threatpodium.com/threat-intelligence-report-2026-11-03/
- 地址／IoC：未见公开 IoC

## 工具与 GitHub 发布

### 1. Noriben v2.1.0：便携恶意软件分析沙箱
Brian Baskin 正式宣布 v2.1.0：ASCII 图形进程树、监控 DLL 加载、JSON 输出等。
- X 原帖：https://x.com/bbaskin/status/2117643920037515573
- GitHub：https://github.com/Rurik/Noriben/
- 地址／IoC：未见公开 IoC

### 2. MalChela v4.5.0：YARA／恶意软件分析工具集接入 ScanMalware
Threat Intel Query 可查询某 URL 在 ScanMalware 的扫描结论，无需 API key，默认关闭，仅发送主机名。
- X 原帖：https://x.com/scanmalware/status/2117705884079923339
- 文章（更新日志）：https://scanmalware.com/changelog
- 地址／IoC：未见公开 IoC

### 3. 其他红队／AI 渗透仓库（低信号）
yogsec 的 Red-Team-Tools 清单、ctf-ai-agent-skills（给 AI agent 的 75 套 CTF 方法）、ARES（「授权红队自动化」框架，帖子涉及募捐，谨慎看待）。ProjectDiscovery 继续宣传 neo（用户用其确认「未认证 SQLi 到命令执行」）以及其「带后门 AI 模型」研究的反响。
- X 原帖：https://x.com/yogsec/status/2117439577292149151
- X 原帖：https://x.com/salmanite/status/2117700705859629402
- X 原帖：https://x.com/makayla_alhamwi/status/2117588464560755169
- X 原帖：https://x.com/pdiscoveryio/status/2117583425469403414
- X 原帖：https://x.com/pdiscoveryio/status/2117661266827489446
- GitHub：https://github.com/yogsec/Red-Team-Tools
- GitHub：https://github.com/Salman0x01/ctf-ai-agent-skills
- GitHub：https://github.com/Mafifrizi/ARES
- 地址／IoC：未见公开 IoC

## APT / Malware 分析

### 1. Kimsuky（APT43）点号填充 LNK 钓鱼：Operation GitPower／HTTPSpy
ThreadLinqs 汇总 SOC Prime 11-03 的分析：伪装成文档、文件名用点号填充的 LNK，隐藏执行 PowerShell／WScript／MSHTA，经服务与登录触发的计划任务持久化，创建隐藏账户并清空 DC 安全审计日志；GitHub raw 与 Pastebin 作 C2／载荷托管。注意 SOC Prime 的样本是 9-21 在受控域控上的**模拟**，其中文件、任务、账户名来自模拟环境，不是真实入侵。lazarusholic 同日转发 JoeSecurity「Operation GitPower」沙箱报告。狩猎：命令行 100+ 空格填充的 LNK、用户可写目录运行 HTA 的 mshta、DC 上 1102 日志清除事件。
- X 原帖：https://x.com/threadlinqs/status/2117719235652972720
- X 原帖：https://x.com/lazarusholic/status/2117582718058045824
- 文章（ThreadLinqs）：https://intel.threadlinqs.com/threat/TL-2026-5175
- 文章（SOC Prime）：https://socprime.com/blog/kimsuky-detection-and-exploitation-analysis/
- 文章（Genians）：https://genians.co.kr/en/blog/threat_intelligence/ai-agent-opencode
- 文章（Fortinet）：https://www.fortinet.com/blog/threat-research/dprk-related-campaigns-with-lnk-and-github-c2
- 沙箱报告（JoeSecurity）：https://www.joesecurity.org/reports/report-7d62e779a769e120ac8f0c5a8bd4e968.html
- 地址／IoC（ThreadLinqs 公开的 3/20 条，其余需付费）：SHA256 `af0309aa38d067373c54b2a7774a32f68ab72cb2dbf5aed74ac784b079830184`；URL `hxxps://pastebin[.]com/raw/gybpx38s`；域名 `raw[.]githubusercontent[.]com`（合法服务被滥用，勿整域封禁）

### 2. 数据泄露与勒索（未经证实，仅攻击方声称）
- 携程（Ctrip/Trip.com）：暗网卖家称有 4.01 亿条用户记录（姓名、电话、地址、预订历史、未来出发日期），要价 1500 美元加密货币；携程未确认，可能含重复或旧数据。若属实，旅行主题钓鱼风险上升。
- FalconFeeds 当日勒索受害者帖：Qilin（Meshbesher & Spence、Arthur Chapman 律所）、Rhysida（Pope County Title）、Akira（Pelham Plastics，30 GB）、FALCON（Buchanan Ingersoll & Rooney，260 GB）、SCARLETTGROUP（Medina Healthcare System）、CHAOS、SETTRA、Payload（德国 Mann Stahlbau）。本窗口未见智利新受害者。
- vx-underground 当日热帖讨论某人在社交媒体上公开自称以雇主名义尝试入侵某组织基础设施（细节未核实，未收录具体指控）。
- X 原帖：https://x.com/DailyDarkWeb/status/2117453930896769430
- X 原帖：https://x.com/FalconFeedsio/status/2117405235656474776
- X 原帖：https://x.com/FalconFeedsio/status/2117659020341461170
- X 原帖：https://x.com/FalconFeedsio/status/2117538195021955232
- X 原帖：https://x.com/FalconFeedsio/status/2117635103983906973
- X 原帖：https://x.com/FalconFeedsio/status/2117707573675901073
- X 原帖：https://x.com/FalconFeedsio/status/2117740228895195343
- X 原帖：https://x.com/FalconFeedsio/status/2117462165615747341
- X 原帖：https://x.com/vxunderground/status/2117650872675045766
- 地址／IoC：未见公开 IoC

### 3. 培训与活动
SANS DFIR 11-04 11:00 ET（智利时间 13:00）网络研讨：Lenny Zeltser 演示在恶意软件分析中隔离并约束 AI agent、核验其结论。
- X 原帖：https://x.com/sansforensics/status/2117649582393839715
- 地址／IoC：未见公开 IoC

## 地址／IoC 汇总

全部已 defang，抄自所引来源：
- Siemens IoT2050 Node-RED CVE-2026-58115（经 Badger Signal 转述 VulnCheck）：C2 `85.215.73[.]250`、`45.194.90[.]57:38472`；文件 `/dev/shm/.b`、`/tmp/.kworker`；下载器 `wget[.]sh`。来源：https://badgersignal.com/articles/active-exploitation-of-siemens-simatic-iot2050-advanced-nodered-authentication-flaw-cve202658115
- Kimsuky Operation GitPower（ThreadLinqs 公开样本）：SHA256 `af0309aa38d067373c54b2a7774a32f68ab72cb2dbf5aed74ac784b079830184`；`hxxps://pastebin[.]com/raw/gybpx38s`；`raw[.]githubusercontent[.]com`（被滥用的合法服务）。来源：https://intel.threadlinqs.com/threat/TL-2026-5175
- PHP2Shell 日志样本（DFIR Radar）：`198.51.100[.]23:4444`（RFC 5737 文档保留段，疑为脱敏示例）；`/dev/shm/.s`、`uploads/.cache[.]php`、`.user.ini` 中的 `auto_prepend_file`
- 其余条目（WordPress 119977、Zyxel 107441、Android 58868、工具类）：未见公开 IoC

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

本日对 LWiS List 前 150 个成员做了 3 次检索（其中一组带链接筛选为 0 条），大多为非技术内容；有用的 ProjectDiscovery（neo、带后门 AI 模型研究）、runZero（EOL 设备与后量子密码迁移：https://www.runzero.com/blog/eol-pqc/ ）、SinSinology（称厂商已分诊其三份漏洞报告：https://x.com/SinSinology/status/2117693903570612659 ）、vx-underground 数条已并入上文。

## 来源搜索 URL

- https://x.com/search?q=CVE%20PoC%20exploit%200day&f=live
- https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- https://x.com/search?q=Kimsuky%20OR%20Lazarus%20OR%20Typhoon%20OR%20CVE-2026-58115&f=live
- https://x.com/i/lists/1239330068461244424
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://nvd.nist.gov/vuln/search
- https://blog.badsectorlabs.com/files/blogs.txt
- https://risky.biz/
- https://tldrsec.com/
