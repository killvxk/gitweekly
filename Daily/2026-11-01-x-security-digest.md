# X 安全情报晚报 · 2026-11-01

覆盖窗口：2026-10-31 20:15 至 2026-11-01 20:15（America/Santiago，UTC-3），约 24 小时。X 只读读取 14 次（主题检索 10 次、指定帖批量查询 1 次、LWiS 成员时间线检索 3 次），0 次 429；共取回 246 条唯一帖，与 seen_ids 重复 0 条；t.co 均已展开（无展开结果的帖只列原帖）。公开备援：CISA KEV 2026.10.30（共 1766 条，周日无更新，Δ0）、NVD API、厂商页面。IoC 一律 defang。本报告为防御向，不转载利用代码、payload 或复现步骤。

## 今日摘要

- **Linux 内核 TCP UAF CVE-2026-98432（CVSS 9.8）成为全天最热话题**：Anthropic Frontier Red Team 披露其内部模型利用此漏洞实现远程 root（利用未公开）；上游 10-15 已修复，NVD 9.8。X 上多方指出 Ubuntu 与部分 RHEL 版本补丁滞后，RHEL 8 已出 RHSA-2026:93415。暴露面是开启 MPTCP 监听的服务器；临时缓解为 `net.mptcp.enabled=0`。未进 KEV，未见在野。
- **KEV 到期**：GitLab CVE-2026-97229、Cisco ASA/FTD CVE-2026-76418 今日 11-01 到期；Ivanti Connect Secure CVE-2026-111357 明日 11-02 到期；Plex 96652/96655、Siemens 110936 11-03 到期。
- **BeyondTrust Remote Support CVE-2026-102764**：Previdian 蜜罐首次观测到探测（单一香港 IP），疑似进入批量扫描阶段（KEV 中已逾期，原截止 10-19）。
- **macOS CVE-2026-112487（revisiond/Storage 本地提权）公开 PoC**：已在 Golden Gate 27.2／Tahoe 26.7.2／Sequoia 15.8.2 修复；未进 KEV，未见在野。
- **FreeSWITCH CVE-2026-116779（CVSS 9.8）**：维护者称已在野利用，修复版 1.11.3；Beam Cloud Beta9 三个 9.9 级跨租户漏洞（JFrog 披露）。
- **VAPOR PANDA / ARTEX 后续**：CyberScoop 引 CrowdStrike 报告，11 天内攻陷约 140 个敏感目标（200+ 机构、14+ 国家）。
- **工具**：0rcruxe 放出 Pass-ta-key PoC 仓库（Google 密码管理器 passkey 研究的配套工具）；AgentSec Inspector（AI 红队）；Trawler（Windows 持久化排查）；Android「SMS of Death」调制解调器远程 DoS 研究。

## CVE / POC / 漏洞

### 1. Linux 内核 IPv4 TCP UAF CVE-2026-98432（CVSS 9.8，未进 KEV）
`tcp_v4_syn_recv_sock()` 与重传 SYN 并发处理产生的竞争条件 UAF（NVD 描述：ipv4: free inet_opt and ireq_opt after an RCU grace period），未认证即可远程触发。Anthropic 10-27 研究文称内部模型约 48 分钟泄露内核指针、再约 5 分钟拿到 shell，利用未公开。X 帖称：Debian、SUSE、Oracle UEK、Amazon Linux 已有补丁；Ubuntu 与 RHEL 部分版本截至 10-31 尚无修复包（RHEL 8 已于 11-01 出 RHSA-2026:93415）。暴露条件：存在 MPTCP 监听（Go 1.24+ 默认开启），可用 `ss -Mlnp` 检查。X 上有人称 GitHub 有「PoC」仓库，但均未经验证，切勿运行。
- X 原帖：https://x.com/RoundtableSpace/status/2117032688867852466
- X 原帖：https://x.com/elchefo/status/2117000123691696367
- X 原帖：https://x.com/TheHour2359/status/2116746050287575363
- X 原帖：https://x.com/hacker_infra/status/2116999722506612757
- X 原帖：https://x.com/32bitsret/status/2117017465544929666
- X 原帖：https://x.com/betterhn300/status/2116737494377017507
- 厂商公告：https://access.redhat.com/errata/RHSA-2026:93415
- 厂商公告：https://ubuntu.com/security/CVE-2026-98432
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-98432
- CVE：https://www.cve.org/CVERecord?id=CVE-2026-98432
- 文章：https://www.anthropic.com/research/discovering-vulnerabilities-with-claude
- 文章：https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf
- 文章：https://pbxscience.com/critical-linux-kernel-flaw-cve-2026-98432-remote-root-exploit-shown-but-ubuntu-and-rhel-still-have-no-fix/
- 讨论：https://news.ycombinator.com/item?id=50319143
- 地址／IoC：未见公开 IoC

### 2. KEV 到期提醒（无新增）
KEV 目录仍为 2026.10.30／1766 条（周日无更新）。**今日 11-01 到期**：GitLab CE/EE CVE-2026-97229（CVSS 10，修复 19.4.2／19.3.5／19.2.8）、Cisco ASA/FTD CVE-2026-76418。**11-02**：Ivanti Connect Secure CVE-2026-111357。**11-03**：Plex Media Server CVE-2026-96652／96655、Siemens Software Center CVE-2026-110936。之后：11-10 Magento 48356、Brotli 111497；11-11 VMware ESX 41709；11-13 Ivanti 118527。已逾期：Fragnesia 46300（10-31）、PHP2Shell 109618/109619（10-29）等。
- X 原帖（GitLab）：https://x.com/h3xivall/status/2116847216664932637
- X 原帖（GitLab）：https://x.com/White_Hunters/status/2116938145228820856
- X 原帖（GitLab）：https://x.com/Real_Willsec/status/2116980543602475116
- X 原帖（Ivanti）：https://x.com/helixml/status/2116720518829101299
- X 原帖（Ivanti）：https://x.com/sh3ll_c0d3/status/2116922213236457664
- X 原帖（Ivanti）：https://x.com/ido_cohen2/status/2116908380346306946
- X 原帖（Cisco）：https://x.com/ThreatRadarAR/status/2116985979860893785
- X 原帖（汇总）：https://x.com/starswarm/status/2116893028740948292
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-97229
- CISA KEV 公告：https://www.cisa.gov/news-events/alerts/2026/10/30/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- 文章：https://thehackernews.com/2026/10/attackers-chain-three-ivanti-connect.html
- 文章：https://helix.ml/threat-watch/i/ivanti-connect-secure-cve-2026-118527
- 文章：https://sh3llc0d3.com/blog/ivanti-connect-secure-zero-day-exploit-chain-missing-authentication-and-predictable-file-staging-chained-to-root-privilege-escalation-cve-2026-111357-and-cve-2026-118527/
- 地址／IoC：未见公开 IoC

### 3. BeyondTrust Remote Support CVE-2026-102764：疑似进入批量扫描
Previdian 称其美国、欧洲两处 BeyondTrust 蜜罐在 11-01 收到探测，来源为同一香港 IP（帖中未公开该 IP），流量与审核中的 Metasploit 模块相近；未观测到成功利用。背景：Mandiant 10-15 报告 ARMORY CASTLE 8 月底把它当 0day 利用；KEV 截止 10-19 已过。处置：打 BT26-05-RS 补丁（受影响 26.2.3 及更早），并排查历史失陷。
- X 原帖：https://x.com/PrevidianCyber/status/2116851059012301188
- X 原帖：https://x.com/Brainix_07/status/2116989365906030981
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-102764
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- 地址／IoC：帖文仅写「单一香港来源 IP」，未给出具体地址，故未抄录

### 4. macOS CVE-2026-112487（revisiond / Storage 本地提权）公开 PoC
路径处理缺陷，本机已有的 App 可借此提权到 root。研究员 @Lyutoon_ 获致谢（称由自动化工具发现并利用），10-31 出现公开利用代码。已修复：macOS Golden Gate 27.2、Tahoe 26.7.2、Sequoia 15.8.2（10-26）。NVD 状态 Awaiting Analysis；未进 KEV，未见在野。
- X 原帖：https://x.com/ThreatWire_/status/2116933790194909488
- X 原帖：https://x.com/ptdbugs/status/2116796575297008083
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-112487
- 文章：https://www.threatwire.tech/news/update-macos-now-public-exploit-code-turns-storage-flaw-cve-2026-112487-into-root
- 文章：https://dbu.gs/vulnerability/PT-2026-125183
- 地址／IoC：未见公开 IoC

### 5. FreeSWITCH CVE-2026-116779（CVSS 9.8，维护者称在野）
入站 SIP MESSAGE（默认开启）可选中 api chat 协议，以 FreeSWITCH 进程权限执行系统命令。受影响 ≤1.11.2，修复 1.11.3；未修补前可在不需要 SIP chat 的 profile 上设 `enable-chat=false`。未进 KEV；NVD 暂无记录。
- X 原帖：https://x.com/Python_s_/status/2116775093804175580
- GitHub·厂商公告：https://github.com/signalwire/freeswitch/security/advisories/GHSA-mg63-h38w-8p9p
- GitHub 发布：https://github.com/signalwire/freeswitch/releases/tag/v1.11.3
- 地址／IoC：未见公开 IoC

### 6. Beam Cloud Beta9 三个 9.9 级跨租户漏洞（JFrog CNA）
CVE-2026-120306（Buildah chroot 隔离）、CVE-2026-120307（沙箱文件 API 路径穿越／符号链接）、CVE-2026-120308（Volume 路径穿越）。修复版 Worker 0.1.756（9-15 发布）；JFrog 的只读验证可取到 worker pod 的 K8s service-account token。未见在野。
- X 原帖：https://x.com/Python_s_/status/2117012012064555509
- X 原帖：https://x.com/Python_s_/status/2117010017287086307
- X 原帖：https://x.com/Python_s_/status/2117012101239857497
- GitHub 发布：https://github.com/beam-cloud/beta9/releases/tag/worker-0.1.756
- GitHub 修复 PR：https://github.com/beam-cloud/beta9/pull/1897
- CVE 记录：https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/120xxx/CVE-2026-120307.json
- 地址／IoC：未见公开 IoC

### 7. 其他（信号较低／待核实）
- Drupal Commerce CVE-2026-118539 后续（仍未进 KEV）：X 原帖 https://x.com/sh3ll_c0d3/status/2116903088212635670 、https://x.com/EvergreenCS117/status/2116675554724450779 ；文章 https://sh3llc0d3.com/blog/drupal-commerce-core-unauthenticated-authorization-bypass-forceful-browsing-exploited-in-the-wild-cve-2026-118539-and-sa-contrib-2026-254/ ；厂商公告 https://www.drupal.org/sa-contrib-2026-254
- TeamViewer 三个高危漏洞（最高 CVE-2026-111585，8.8），修复 15.83，厂商称暂无在野：X 原帖 https://x.com/HomeLabCipher/status/2116938975436836922 ；厂商公告 https://www.teamviewer.com/en/resources/trust-center/security-bulletins/
- LightSAML PHP 库签名校验缺陷 CVE-2026-63182（称已有 PoC）：X 原帖 https://x.com/TuringCyberObs/status/2116925246338904499 ；分析 https://github.com/alan-turing-institute/cyber-threat-observatory/blob/main/reports/2026-10-30/TIER_2_CVE-2026-63182.md
- Windows 11 本地提权研究 TrustedHive（作者称可能与已修复的 CVE-2026-81963 重复，请先确认补丁）：X 原帖 https://x.com/dis0rder_0x00/status/2116969638978286076 ；GitHub https://github.com/dis0rder0x00/TrustedHive
- Eclair v0.14.6 安全版本（闪电网络节点）：X 原帖 https://x.com/BitcoinRevNews/status/2116893478810533962 ；GitHub https://github.com/ACINQ/eclair/releases/tag/v0.14.6
- exploitgrid 收录 Zoho CVE-2026-6516、GitLab 110264/97229 扫描器（未核实）：X 原帖 https://x.com/exploitgrid/status/2116937350140117489 、https://x.com/exploitgrid/status/2116937354330116186 ；页面 https://exploitgrid.net/exploits/6611ec4a-a149-4a0f-a270-06ba008ea995 、https://exploitgrid.net/exploits/fba00e88-ff95-4e1f-a446-0080899ae485
- 地下论坛兜售所谓 AD 0day 提权服务（无 CVE、无演示，未核实）：X 原帖 https://x.com/TheThreatWire/status/2116821438011257021
- 地址／IoC：未见公开 IoC

## 工具与 GitHub 发布

### 1. Pass-ta-key PoC（0rcruxe）
前日 Google 密码管理器／passkey 研究的配套 PoC 仓库，针对 Chrome 进程内存中的 GPM Security Domain Secret。防御：监控非浏览器进程读取 Chrome 进程内存，并保护终端凭据存储。
- X 原帖：https://x.com/ipurple/status/2116947982146732368
- GitHub：https://github.com/0rcruxe/pass-ta-key
- 地址／IoC：未见公开 IoC

### 2. AgentSec Inspector（AI 红队桌面工具）
开源，支持 Windows/Linux，覆盖提示注入／越狱、MCP 与 RAG 审计、多轮黑盒测试。
- X 原帖：https://x.com/St0rnPentest/status/2116850362963358011
- GitHub：https://github.com/St0rn/agentsec-inspector
- 地址／IoC：未见公开 IoC

### 3. Trawler（Windows 持久化排查，蓝队）
PowerShell 脚本，覆盖大多数 MITRE 与 Atomic Red Team 持久化技术，导出带风险评分的 CSV，支持 allow-list 降噪。
- X 原帖：https://x.com/EsGeeks/status/2117002875624882555
- GitHub：https://github.com/joeavanzato/Trawler
- 地址／IoC：未见公开 IoC

### 4. SMS of Death（Android 调制解调器远程 DoS 研究）
作者称通过 WAP Push 可让 Android 12–17 手机的基带崩溃；仅 Android 14–17 有更新。
- X 原帖：https://x.com/ksg93rd/status/2116919342013264356
- GitHub：https://github.com/MarkBlah/smsofdeath
- 文章：https://smsofdeath.com
- 地址／IoC：未见公开 IoC

### 5. 其他
- REA（软件逆向／重建路线图，热度高但偏营销）：X 原帖 https://x.com/N01ennn/status/2116886032763257278 ；GitHub https://github.com/morluto/rea
- 地址／IoC：未见公开 IoC

## APT / Malware 分析

### 1. VAPOR PANDA 使用 ARTEX 代理式 AI 渗透框架（CrowdStrike，后续报道）
CyberScoop：中国国家背景组织 VAPOR PANDA 自 10-17 起针对 14+ 国家的 200+ 机构，11 天内攻陷约 140 个敏感目标，包括外交部、某欧洲国家总统府与总理府、国防情报机构、19 家美国制药／半导体／国防／核能／金融机构，以及美国、比利时、菲律宾的电信商。另有帖文称 AI 代理每小时执行 1500+ 条命令（人工约 40 条）。
- X 原帖：https://x.com/CyberScoopNews/status/2116997707269046603
- X 原帖：https://x.com/ng_hoaiphu/status/2116866030509379726
- X 原帖：https://x.com/cybermergemedia/status/2117002578630250675
- X 原帖：https://x.com/econographs/status/2116726986341322896
- 文章：https://cyberscoop.com/china-vapor-panda-agentic-ai-artex-campaign-crowdstrike/
- 文章（意大利文）：https://ianews24.com/articoli/cina-agenti-ia-vapor-panda-artex-gerardo-costabile
- 地址／IoC：主机侧狩猎线索见下方汇总（cybermergemedia 转述，未与 CrowdStrike 原文核对）

### 2. Cisco Talos：UAT-11473 / KeyDrift 打 Catalyst SD-WAN（10-28 披露，X 复述）
利用 CVE-2026-20127（CVSS 10，2 月已修复、早已进 KEV），植入 KeyDrift 框架（PolyFlame 命令执行、LittleFilch 窃取密钥材料）。目标为卫星运营商、航天、国防与智库；基础设施与 Volt Typhoon「Silent Train」重叠，但未认定为同一组织。本窗口仅见 X 复述，未取到 Talos 原文链接。
- X 原帖：https://x.com/ApollonVisual/status/2116855619730735250
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-20127
- 地址／IoC：未见公开 IoC

### 3. 恶意软件分析教学与工具
- cocomelonc「Malware analysis part 12」，用纯 C 计算节区熵、检测加壳：X 原帖 https://x.com/CyberWarship/status/2116900072508015103 ；文章 https://cocomelonc.github.io/malware/2026/09/23/malware-analysis-12.html
- Booz Allen Vellox Reverser（代理式恶意软件逆向，厂商宣传）：X 原帖 https://x.com/BAHSOURCE1/status/2116958981449281661 ；文章 https://www.boozallen.com/expertise/products/vellox-reverser.html
- @0x4D31 征集 macOS 恶意软件静态分析工具的试用者（尚未发布）：X 原帖 https://x.com/0x4D31/status/2116945701028745447
- 地址／IoC：未见公开 IoC

### 4. 泄露／勒索声称（未经核实）
SHIBA 勒索声称德国 TEMA Haus- und Wärmetechnik；Qilin 声称 Danser；Forexing 声称持有归属 SoftBank 的 5500 万条记录；GoreTerminal 声称持有 SquareTrade/QuillBot 4100 万条；法国 Waffle Factory 数据库、墨西哥格雷罗州 SICECO、印度 ICMR 相关 Aadhaar 数据库出售等。
- X 原帖：https://x.com/FalconFeedsio/status/2117010026401607991
- X 原帖：https://x.com/intels_daily/status/2117030706417213580
- X 原帖：https://x.com/intels_daily/status/2117015602569081011
- X 原帖：https://x.com/intels_daily/status/2117000525241573556
- X 原帖：https://x.com/DailyDarkWeb/status/2117007056620355731
- X 原帖：https://x.com/DailyDarkWeb/status/2116991943121289429
- X 原帖：https://x.com/DailyDarkWeb/status/2116914463672816025
- 地址／IoC：未见公开 IoC（仅受害方名称）

## 地址／IoC 汇总

本窗口未见公开的网络 IoC（无 C2、IP、域名、钱包或样本哈希可抄录）。仅有一条主机侧狩猎线索，原样记录如下：

| 来源 | 类型 | 内容 | 备注 |
|---|---|---|---|
| https://x.com/cybermergemedia/status/2117002578630250675 | 主机路径／关键字 | `C:\ProgramData\artx5v\`；命令行含 `artx` 或 `artex`；`artx` 前缀的云角色 | VAPOR PANDA／ARTEX 狩猎线索，二手转述，未与 CrowdStrike 原文核对 |

BeyondTrust 探测的来源 IP 原帖未公开，故未抄录。

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

本日 LWiS 成员时间线：随机抽 100 个 handle，分 3 批检索，取回 38 条帖。安全相关的仅有：@LiveOverflow 关于「漏洞研究在防御行业被边缘化」的讨论（https://x.com/LiveOverflow/status/2116929507471061252 ）；@stvemillertime 宣布加入 GreyNoise（https://x.com/stvemillertime/status/2116920066985844783 ）；@dmcxblue 转引 init1security 发布（https://x.com/dmcxblue/status/2116995077369200906 ）。其余多为周日闲聊，本日无显著技术更新。

## 来源搜索 URL

- X Latest（CVE/POC）：https://x.com/search?q=CVE%20OR%20PoC%20OR%20exploit%20OR%200day&f=live
- X Latest（GitHub 工具）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- X Latest（威胁报告）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- X Latest（Linux TCP）：https://x.com/search?q=CVE-2026-98432&f=live
- X Latest（macOS）：https://x.com/search?q=CVE-2026-112487&f=live
- X Latest（ARTEX）：https://x.com/search?q=ARTEX%20CrowdStrike&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/ ；tl;dr sec：https://tldrsec.com/

说明：本次 X 采集走 Grok Bot 公共 X 只读接口（search_posts_all，与 Latest 等价的检索，单次上限 25 条），LWiS List 以成员备份中 100 个 handle 的 from: 检索代替；全程无发帖、点赞、追踪、转推或回复。
