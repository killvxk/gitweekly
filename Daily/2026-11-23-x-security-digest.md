# X 安全情报晚报 · 2026-11-23（周一）

> 报告时间：2026-11-23 约 19:56（America/Santiago），即 2026-11-24 约 06:56（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-22 22:51 UTC 到 11-23 22:56 UTC（约 24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-23 22:53:31～22:55:48 UTC（约 4 分钟，CVE／POC／exploit 关键词噪声刷屏），所以加了 relevancy 补搜 25 条（11-23 05:41:24～21:46:43 UTC，约 16.09 小时），以及编号 CVE-2026／CVE-2025／advisory／CISA KEV 关键词 recency 25 条（11-23 22:36:29～22:54:20 UTC，约 0.3 小时，仍偏短）。另一次针对今日新入 KEV 的 MONAI／MailAssure／known exploited 做 relevancy 补搜 25 条，覆盖 11-22 23:19:15～11-23 22:37:32 UTC（约 23.3 小时）。窗口前段主要靠该条补搜、工具组 Latest 与 LWiS List 补上。
> - 工具组 Latest 13 条覆盖 11-22 23:00:27～11-23 22:41:11 UTC（约 23.68 小时，距窗口起点约 9 分钟）。
> - 威胁组 Latest 25 条只覆盖 11-23 20:01:52～22:48:20 UTC（约 2.77 小时），relevancy 补搜 25 条覆盖 11-22 23:07:10～11-23 21:33:16 UTC（约 22.44 小时）。另一次就 KEPCO／Bell Canada／Unit 42／agentic threat actor 做 relevancy 补搜，用于交叉验证。
> - LWiS List（`list:1239330068461244424` 只读 Latest）首屏 25 条覆盖 11-23 19:23:28～22:48:38 UTC；再翻页至第 9 屏（第 10 屏在 `start_time` 约束下为空），合并去重后 216 条，整体 11-22 22:58:01～11-23 22:48:38 UTC（约 23.84 小时，距窗口起点约 7 分钟）。
> **其他信源**：SecureFlow 的 all／community／blog 三路接口（含站点首页）均返回 **HTTP 522**，用浏览器 UA＋站点 Referer 重试仍为 **522**（Cloudflare 源站错误，与 11-19、11-22 期相同，不是 UA 问题）。community／blog 各源未能逐个拉取，本窗口 SecureFlow 新条目计为 0，并在对应小节与来源节如实写明。pwn.watch 订阅源已拉取（XML／JSON 均为 200；XML 50 条），**本窗口无新条目**（订阅源 `lastBuildDate` 为 2026-11-08 20:19:52 GMT）。ExploitGrid exploits 列表已拉取 100 条，严格 48 小时窗口内新条目 **0**（列表最新 `date` 为 2026-11-20 19:48:48 UTC，早于 48 小时起点 11-21 22:56 UTC）；老 CVE 的重复 PoC 只计数不展开。ExploitGrid KEV 期限接口返回 10 条，**未包含**今日新入目录的 2 条，也未列出明天到期的 4 条，与 CISA 官方不完全一致，期限以 CISA 为准。CISA KEV 目录当前 **1792** 条（`dateReleased` 2026-11-23T19:43:55Z），本窗口新增 **2** 条（11-23 入目录，联邦期限 11-26）。AI/TLDR 订阅源 50 条，本窗口（约 36 小时，且不在 seen_ids）新条目 **14**，其中 security **1**；其 releases 详情页换 UA＋Referer 后仍 **403**，报告保留订阅链接。Agent Use Cases RSS 60 条，本窗口（约 48 小时）新条目 **26**（11-23 计 14，11-22 计 12）。本日为周一（America/Santiago），不加阮一峰周刊节；上期（周日）已收录第 420 期。
> **验收**：采集——SecureFlow 三路失败已如实写明，其余信源已拉取并按窗口筛选；核验链接——主链接已用浏览器 UA 抽查，AI/TLDR releases 页仍 403 已注明，MSRC 顾问页遇到 SSL 中断已改用 CISA／NVD 链接；成稿——每日十节齐全（非周末，无阮一峰节），无利用代码／payload／PoC 步骤；落盘与交付见文末。

## 今日摘要

- **CISA 今天（11-23）把 2 条漏洞列入 KEV**，联邦修补期限均为 **2026-11-26**：Project MONAI Label 路径遍历（CVE-2026-133968，可导致任意文件写入乃至 RCE），以及 N-able MailAssure／SpamExperts 的 LDAP 同步检查 SSRF（CVE-2026-134624）。这两条在上期已作为研究披露／厂商修复出现，今天因「已有活跃利用证据」进入目录。
- **周五入目录的 4 条 KEV 联邦期限就是今天（11-23）**：VMware vCenter 认证绕过（CVE-2026-123890）、Cisco Expressway 预认证 root 命令执行（CVE-2026-76466）、Apache Roller XML-RPC 反序列化（CVE-2026-129448）、SAP NetWeaver Enterprise Portal（CVE-2025-42884）。Cisco 官方顾问今日更新到 1.1 版，仍写明**没有临时缓解措施**；Censys 称观察到约 14,900 台相关暴露主机（并非全部易受影响）。香港时间已到 11-24 清晨，Santiago 报告日仍为 11-23 晚。
- **明天（11-24）到期**的还有 Outlook／Microsoft Office CVE-2026-124194、Chrome／Chromium CVE-2026-125350、Cisco BroadWorks CVE-2026-20320、Openwave CVE-2026-111793。X 上有报道称微软确认 Outlook 该漏洞正被主动利用（描述为 NTLMv2 spoofing）；本期未能打开 MSRC 页面（SSL 中断），利用事实以已在 KEV 为准。
- **韩国电力公社 KEPCO 确认数据泄露，影响超过 150 万人**（11-20 发现，涉及账单平台 KEPCO ON 与采购系统 SRM）。**Bell Canada** 称 11-17 发生「agentic threat actor」入侵，波及 Bell、Aliant、MTS、Virgin Plus、Lucky Mobile 等客户。Unit 42 发布 Com 关联团伙的 vishing／侧载 Chrome 扩展报告。此外，Huntress 记录到已修补的 ConnectWise ScreenConnect 客户端漏洞（CVE-2026-84869）被用来打 MSP 技术员主机；Microsoft Entra Connect Health API 缺陷导致租户元数据被读走，服务端修复已在 11-19 部署。

## CVE / POC / 漏洞

### 1. CISA 今日新增 2 条 KEV（11-23 入目录，期限 11-26）

CISA 于 11 月 23 日发布警报，将 2 条漏洞加入已知被利用目录，依据是活跃利用证据。官方目录由 1790 条增至 **1792** 条。ExploitGrid 的 active-deadlines 尚未列出这两条，期限以 CISA 官方为准。

- CISA 公告：https://www.cisa.gov/news-events/alerts/2026/11/23/cisa-adds-two-known-exploited-vulnerabilities-catalog

#### 1.1 Project MONAI Label 路径遍历 CVE-2026-133968

- 说明：MONAI Label 的路径遍历可让未认证远程攻击者向数据存储目录之外写入任意文件，并可能造成 RCE。这就是上期报道的、Amazon 披露「中国关联行为体用开源自主渗透框架 Cairn 的 AI agent，在约 11 分钟内自己发现并利用」的 0day。官方安全版本仍是 **0.8.6**。今日因已有活跃利用被列入 KEV，联邦期限 **11-26**。X 上有帖复述 PUT `/datastore/image` 目录穿越（CVSS 9.8）。只记补丁与狩猎优先级，不写利用步骤。
- X 原帖：https://x.com/showtechweekly/status/2125000020965413026 · https://x.com/WebsecCL/status/2124971257439363510 · https://x.com/2logics/status/2124983006058471555
- 厂商公告：https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94 · https://github.com/Project-MONAI/MONAILabel/pull/1915
- 厂商公告（KEV／NVD／交叉）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-133968 · https://nvd.nist.gov/vuln/detail/CVE-2026-133968 · https://www.cve.org/CVERecord?id=CVE-2026-133968
- 文章／PDF：https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/

#### 1.2 N-able MailAssure（SpamExperts）SSRF CVE-2026-134624

- 说明：MailAssure／SpamExperts 在 LDAP 同步连接检查中存在 SSRF，已认证的 API 用户可探测内网主机与端口并向内部服务发送请求。上期已作为厂商修复简讯出现（当时称除一台托管服务器外未见利用）；The Hacker News 今日稿指出，该漏洞是在一次入侵调查中发现的。现已进入 KEV，期限 **11-26**。请核对本组织是否使用 MailAssure／SpamExperts，并按厂商顾问升级。
- X 原帖：https://x.com/Dinosn/status/2124859205613965494 · https://x.com/2logics/status/2124983006058471555
- 厂商公告：https://me.n-able.com/s/security-advisory/aArVy0000002mrlKAA/cve2026134624-mailassure-ldap-sync-connection-check-ssrf
- 厂商公告（KEV／NVD／交叉）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-134624 · https://nvd.nist.gov/vuln/detail/CVE-2026-134624
- 文章／PDF：https://thehackernews.com/2026/11/n-able-discloses-critical-mail-assure.html

### 2. 今日到期的 4 条 CISA KEV（11-20 入目录，期限 11-23）

这 4 条已在上期完整收录，今日仍是修补窗口的最后一天（香港时间已进入 11-24，Santiago 仍为 11-23）。KEV JSON 显示 11-20 至今日这 2 条新增之外，没有其他新条目改写这批期限。

- CISA 公告（11-20）：https://www.cisa.gov/news-events/alerts/2026/11/20/cisa-adds-four-known-exploited-vulnerabilities-catalog

#### 2.1 VMware vCenter 认证绕过 CVE-2026-123890

- 说明：仍是今日讨论最密的条目之一。官方顾问 VMSA-2026-0009，**没有临时缓解措施**。X 上继续跟进活跃利用；@Dinosn 称已有公开 PoC（用于在补丁可用后做检测），本期**不链 PoC 仓库、不写步骤**。Code White（@codewhitesec）补充称，同一安全更新还修了另一个更易利用、甚至没有单独 CVE 编号的认证绕过，建议不要只盯这一条编号。怀疑失陷时仍需按厂商指引轮换 STS 签名密钥与证书。
- X 原帖：https://x.com/TheExploitHQ/status/2124891355071603193 · https://x.com/Dinosn/status/2124731581839376584 · https://x.com/codewhitesec/status/2124898645350785089 · https://x.com/socstorm/status/2124767415502569914
- 厂商公告：https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/VMSA-2026-0009--VMware-vCenter--Tools--and-SDDC-Manager-updates-address-multiple-vulnerabilities--CVE-2026-123890--CVE-2026-123891--CVE-2026-123892--CVE-2026-123893--CVE-2026-123894-/39495 · https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0009/README.md
- 厂商公告（KEV／NVD／交叉）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-123890 · https://nvd.nist.gov/vuln/detail/CVE-2026-123890

#### 2.2 Cisco Expressway 预认证 root 命令执行 CVE-2026-76466（CVSS 9.8）

- 说明：硬编码凭据等问题（CWE-798），未认证、有网络访问的攻击者可在集群环境的 Expressway-C／Expressway-E 上以 root 执行命令。Cisco 顾问 cisco-sa-vcs-static-cred-hr7EWZ8t **今天 15:51 GMT 更新到 Version 1.1**，仍写明 **No workarounds available**。X 上有帖称修复目标为 X15.5.20，X14 及更早需迁移。Censys 今日顾问称观察到约 14,900 台相关暴露主机（并非全部脆弱），并记录已有利用报告。BleepingComputer 亦跟进 CISA 将其列为已在攻击中被利用。
- X 原帖：https://x.com/censysio/status/2124961727338926556 · https://x.com/uwillc/status/2124865760862314578 · https://x.com/busenur038/status/2124840027532185917 · https://x.com/Dinosn/status/2124778255056028138
- 厂商公告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t
- 厂商公告（KEV／交叉）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-76466
- 文章／PDF：https://censys.com/advisory/cve-2026-76466/ · https://www.bleepingcomputer.com/news/security/cisa-flags-critical-cisco-expressway-rce-flaw-as-actively-exploited/

#### 2.3 Apache Roller XML-RPC 反序列化 CVE-2026-129448 与 SAP NetWeaver Enterprise Portal CVE-2025-42884

- 说明：Roller 的 XML-RPC 端点在认证前反序列化不可信数据，CVSS 9.8，已在野外被利用；SAP 条目同日到期。今日讨论以 Cisco／vCenter 为主，这两条没有显著的新技术细节，但仍应在期限日完成修补。
- X 原帖：https://x.com/ctiwatchHQ/status/2124925990744834287
- 厂商公告（KEV）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-129448 · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-42884

### 3. 明天（11-24）到期的 KEV：Outlook CVE-2026-124194 等

- 说明：CISA 目录中，11-24 到期的 4 条为：Microsoft Office Outlook CVE-2026-124194、Google Chromium CVE-2026-125350、Cisco BroadWorks CVE-2026-20320、Openwave Messaging Webtop Media Transcoder CVE-2026-111793（均于 11-10 入目录）。X 上有聚合稿称微软已确认 Outlook 该漏洞正被主动利用，并写为 NTLMv2 spoofing；该条本来就在 KEV。本期访问 MSRC 更新指南页时出现 SSL 中断，故不以 MSRC 页面为据，请直接按 CISA／厂商补丁通道处理。后续还有 Puppet Enterprise CVE-2026-115731（期限 12-01）、LiteLLM CVE-2026-40217（12-02）。
- X 原帖：https://x.com/f1tym1/status/2124998833817989217
- 厂商公告（KEV／NVD）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-124194 · https://nvd.nist.gov/vuln/detail/CVE-2026-124194 · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-125350 · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-20320 · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-111793
- 文章／PDF：https://f1tym1.com/2026/11/23/microsoft-confirms-active-exploitation-of-outlook-ntlmv2-spoofing-vulnerability/

### 4. ConnectWise ScreenConnect 客户端漏洞 CVE-2026-84869（CVSS 9.9，已有在野利用）

- 说明：The Hacker News 援引 Huntress／John Hammond：攻击者利用**现已修补**的 ScreenConnect 客户端缺陷，在客人会话中向连入的 MSP 技术员主机投递并执行文件。Huntress 在 11 月 12 日观察到一起个案；相关活动区间约为 10 月 20 日至 11 月 16 日，并记录到大量对 ScreenConnect 服务器的客人「运行文件」请求。载荷会从 `masterdarky.com` 拉取安装包，并拉起指向攻击者中继的 rogue ScreenConnect 客户端。此处只记谁／打什么／补丁与狩猎域名，不写投递或脚本细节。请确认 ScreenConnect 已升到厂商已发布的修复版本，并在技术员工作站上排查异常 ScreenConnect 客户端与该域名访问。
- X 原帖：https://x.com/Dinosn/status/2124859311218201048
- 文章／PDF：https://thehackernews.com/2026/11/hackers-exploit-critical-screenconnect.html

### 5. Ghostscript「Upload2Shell」CVE-2026-125396 跟进

- 说明：上期已展开。今日仍有帖提醒：特制 PDF／PostScript 可逃逸 `-dSAFER` 并执行命令；有公开 PoC，**尚未进入 KEV**；修复版本 10.08.0 或发行版回移。不重复原理，也不链 PoC。
- X 原帖：https://x.com/OstorlabSec/status/2124791744571052332 · https://x.com/busenur038/status/2124926939211382842

### 6. 其他需留意的修补与讨论（信号低于以上条目）

- **simple-git CVE-2026-134815**：@OstorlabSec 称带连字符前缀的值可让 simple-git 在主机上执行攻击者指定的程序（CVSS v4 9.2），修复版本 4.1.0；称尚无公开 PoC、未入 KEV。原帖配图，本期未核验到独立顾问页，暂作待核对简讯。X 原帖：https://x.com/OstorlabSec/status/2124899798461325326
- **WhatsApp 三处修补，其中一处曾被用于诈骗活动**：SC World 11-22 简讯，今日经 LWiS 转发。本期未在正文中抽出 CVE 编号，请以 WhatsApp 官方安全更新为准。X 原帖：https://x.com/Dinosn/status/2124702928552542465 ｜ 文章：https://www.scworld.com/brief/whatsapp-patches-three-security-flaws-including-one-exploited-in-scam-campaign
- **NASA-AMMOS AIT-GUI CVE-2026-77309**：有帖称 ≤2.5.0 在相邻网络下可未认证执行 Python，已在 2.5.1 修复，仓库 11-3 已归档，未见 KEV。GitHub Advisory：https://github.com/advisories/GHSA-jrjx-9jjw-747m ｜ X 原帖：https://x.com/busenur038/status/2124806666726035836
- **Synology DSM**：@pfiatde 提醒有 Synology NAS 的人尽快打补丁（配图）；与此前已到期的 KEV 条目 CVE-2024-10441 相关讨论一致，不重复展开。X 原帖：https://x.com/pfiatde/status/2124949600977186856
- **警惕伪造公告「Bluetooth2Shell」**：@InfiShark 指出今日流传的「CVE-2026-9001、一次配对提示即可在 3 秒内拿到 root、CVSS 10.0、全平台」是讽刺页，页脚写明是 advisory 形式的 satire，**不是真实漏洞**。X 原帖：https://x.com/InfiShark/status/2124913098268291143
- **未作为已确认要闻展开**：X 上有帖列举 NGINX HTTP/2 相关 CVE-2026-123007／CVE-2026-123633 并称 Palo Alto 就 PAN-OS 影响发布了缓解措施，但原帖未给出可核验的 F5／nginx／Palo Alto 公告链接，本期未予确认。HPE Morpheus CVE-2026-95793、Ivanti／VulnCheck 侧的 CVE-2026-121653（有帖称尚未进入 CISA KEV）等证据不足或仅单帖，不展开。

## 工具与 GitHub 发布

### 1. Claude-BugHunter 仍居趋势榜首

- 说明：@trending_repos 统计该仓库 24 小时新增约 2,037 star，总量约 18,821。定位仍是缺陷狩猎与外部红队用的 Claude Code skill 包（仓库页称 82 个 skill、15 条斜杠命令、681 条已披露报告模式等）。仅用于授权测试。上期已出现，今日热度继续升高，作简要跟进。
- X 原帖：https://x.com/trending_repos/status/2124852716942004412 · https://x.com/PedroSFH23/status/2124894400744493321
- GitHub：https://github.com/elementalsouls/Claude-BugHunter

### 2. RedAgent：用 Rust 写的、走 MCP 工具服务器的自主进攻安全 agent

- 说明：@yasindce1998 发布 RedAgent，定位为面向授权测试的自主进攻安全 agent：目标驱动规划、硬范围护栏、操作员审批，以及可验证的哈希链式证据账本。仓库页 HTTP 200。仅限授权环境。
- X 原帖：https://x.com/yasindce1998/status/2124944766823768338
- GitHub：https://github.com/yasindce1998/RedAgent

### 3. NEBULA：交互式 PowerShell 框架，用于测试 WMI、COM、LOLBAS 与持久化

- 说明：@CyberWarship 介绍 MHaggis／NEBULA，供红蓝队在授权测试中演练 WMI、COM、LOLBAS 和持久化技术。仓库页 HTTP 200。
- X 原帖：https://x.com/CyberWarship/status/2124875639513657508
- GitHub：https://github.com/MHaggis/NEBULA

### 4. GraphCLI、SnowCLI、dnsanity（简讯）

- 说明：@EthicalKaizoku 介绍 GraphCLI（经 Microsoft Graph 做 Entra ID／M365／Intune／Azure 的交互式侦察，应用身份认证）和 SnowCLI（面向 ServiceNow 实例的授权测试工具）。@EsGeeks 介绍 nil0x42／dnsanity，用模板校验 DNS 解析器质量，适合赏金与 recon 自动化。上述均只登记仓库与用途，不转载操作细节，且仅限授权测试。
- X 原帖：https://x.com/EthicalKaizoku/status/2124655930239512944 · https://x.com/EthicalKaizoku/status/2124650133870575830 · https://x.com/EsGeeks/status/2124708827396558989
- GitHub：https://github.com/Ethical-Kaizoku/GraphCLI · https://github.com/Ethical-Kaizoku/SnowCLI · https://github.com/nil0x42/dnsanity

### 5. ProjectDiscovery 发布 SecurityContext 2.0

- 说明：@pdiscoveryio 宣布 SecurityContext 2.0，把 CVE、GitHub advisory、修复提交、KEV／EPSS 等与开源仓库／软件包／锁文件或 SBOM 对齐，用来判断「谁真的受影响」。帖中举例可把一条 CVE 追到具体包版本与引入它的仓库。仓库／产品页本期未单独核验，先以 X 原帖为准。
- X 原帖：https://x.com/pdiscoveryio/status/2124932908087706027 · https://x.com/pdiscoveryio/status/2124932910704939473

## APT / Malware 分析

### 1. 韩国电力公社 KEPCO 确认超 150 万人数据泄露

- 说明：BleepingComputer（Bill Toulas，11-23）报道，威胁行为体进入韩国电力公社（KEPCO）内网，访问了含客户、员工与承包商数据的两套系统。公司于 **11 月 20 日**确认：受影响的是电费账单平台 **KEPCO ON** 与电子采购系统 **SRM**，随后阻断外部 IP 并暂停相关服务。公告披露的规模约为：650,487 名 KEPCO ON 客户（含姓名、身份信息、电话、地址，以及银行／卡片与账单信息）、426,827 名企业代表、442,934 名员工（所属、工号、手机、邮箱等），合计超过 150 万。KEPCO 称攻击使用了「AI 等先进技术」，但未说明初始入口。化名 **Noiem** 的账号曾在 11-19 的论坛上宣称持有数据；韩国个人情报保护委员会证实 KEPCO 当天收到声称窃数据的邮件，**对 Noiem 的归因尚未确认**。受影响者面临定向钓鱼与冒充风险。
- X 原帖：https://x.com/TheCyberSecHub/status/2124970434320019704 · https://x.com/jpsharada/status/2124970862050959625 · https://x.com/Sent_Intel/status/2124985264472780808
- 文章／PDF：https://www.bleepingcomputer.com/news/security/south-koreas-power-giant-kepco-confirms-data-breach-impacting-15-million/

### 2. Bell Canada：「agentic threat actor」于 11-17 进入内部系统

- 说明：CBC（11-23）报道，Bell 发言人确认 11 月 17 日有「agentic threat actor」访问部分内部系统，受影响范围包括 Bell、Bell Aliant、Bell MTS、Virgin Plus 与 Lucky Mobile 的客户；公司未公布人数。Bell 称信用卡号、银行信息等「高度敏感」个人数据未被取用。Virgin Plus 通知称可能涉及姓名、邮寄地址、电话、邮箱与账户信息，并已请加拿大皇家骑警网络犯罪部门调查。Winnipeg Free Press（11-22）补充：Bell MTS 近期电邮中断，调查发现与密码重置环节的漏洞有关，并与此次 Bell 事件存在关联。X 上对「agentic」这一表述讨论很多，但公开信息仍只有公司自己的定性，没有可独立核验的攻击链细节。
- X 原帖：https://x.com/osintsmyth/status/2124956621256462697 · https://x.com/99allandufour99/status/2124970080899633304 · https://x.com/warrens_intern/status/2124647964899528719 · https://x.com/Pearcespective/status/2124894485759017184
- 文章／PDF：https://www.cbc.ca/news/canada/bell-cybersecurity-incident-virgin-plus-9.7432273 · https://www.winnipegfreepress.com/breakingnews/2026/11/22/bell-mts-says-cyberattack-behind-recent-email-outage

### 3. Unit 42：Com 关联团伙的 vishing 与侧载 Chrome 扩展

- 说明：Palo Alto Networks Unit 42 报告《Dialing for Data: Inside the Com’s High-Profile Heists》描述近期多波与 Com 关联的 vishing：冒充内部 IT 支持，把员工带到仿冒 SSO 页，窃取会话并登记攻击者自己的 MFA 设备，再在 Teams 上勒索；金融、医疗、法律等数据密集行业是重点，有帖称医疗已成为优先目标。@mgreen27 补充同一活动里出现侧载「Google Chrome」扩展：从 `oskeysetup.com` 以开发者模式安装，利用 `chrome.debugger` 做 C2，并用名称隐藏调试横幅，同时更新了 Velociraptor 检测规则。此处只记手法类别、狩猎域名与防御建议，不写扩展实现细节。
- X 原帖：https://x.com/mgreen27/status/2124815476354068918 · https://x.com/virusbtn/status/2124816583596163073 · https://x.com/pol_md5sum/status/2124827500115357737 · https://x.com/NoctisIntel/status/2124919455226667092
- 文章／PDF：https://unit42.paloaltonetworks.com/com-affiliate-vishing-attacks/
- GitHub（检测规则，非恶意样本）：https://github.com/mgreen27/DetectRaptor/blob/master/vql/ChromiumExtensionPersistence.yaml

### 4. Microsoft Entra Connect Health：API 缺陷导致租户元数据被读取

- 说明：SC World／BleepingComputer／Security Affairs 均有报道。问题出在 Entra Connect Health API（报道称该接口于 2026-07-23 引入）。微软于 **11 月 9 日**发现，**11 月 19 日**部署了服务端修复。未授权方可只读访问租户级元数据，包括管理员邮箱、租户 ID、域名和同步状态；微软称密码、认证令牌和有效加密密钥未被泄露。管理员联系方式暴露后存在定向钓鱼风险。X 上今日经 LWiS 传播。
- X 原帖：https://x.com/Dinosn/status/2124702371624174043 · https://x.com/Dinosn/status/2124881410527822112
- 文章／PDF：https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/ · https://www.scworld.com/brief/microsoft-discloses-data-breach-involving-entra-connect-health-service · https://securityaffairs.com/203820/data-breach/microsoft-entra-connect-health-breach-exposes-tenant-metadata-and-admin-details.html

### 5. 其他入侵与恶意软件简讯

- **GL.iNet 确认云端漏洞导致路由器与 KVM 感染恶意软件**：SC World 简讯，经 LWiS 转发。请关注厂商公告并检查相关云账号／设备固件。X 原帖：https://x.com/Dinosn/status/2124701838666559873 ｜ 文章：https://www.scworld.com/brief/gl-inet-confirms-cloud-vulnerability-led-to-router-and-kvm-malware-infections
- **Azure 缺陷被用来针对挪威能源企业的机密**：SecurityWeek 报道，经 LWiS 转发。BleepingComputer 同期亦有「Azure 缺陷被用来窃取客户 API 凭据」的相关稿。X 原帖：https://x.com/Dinosn/status/2124926974908944837 ｜ 文章：https://www.securityweek.com/azure-flaw-exploited-to-target-secrets-at-norwegian-energy-firms/ · https://www.bleepingcomputer.com/news/security/microsoft-azure-flaw-exploited-to-steal-customers-api-credentials/
- **Cleverbridge 支付卡数据泄露、奥地利外交部网站被入侵、Bulgaria 政府长期窃密被发现、Bromcom 约 35.5 万账号出现在 HIBP**：均为 LWiS 转发的简讯或目录项，证据强度一般，作备查。https://www.scworld.com/brief/cleverbridge-reports-data-breach-involving-payment-card-information · https://www.scworld.com/brief/austrian-foreign-ministry-website-breached-by-hackers · https://securityaffairs.com/203794/intelligence/bulgaria-discovers-massive-government-breach-after-five-years-of-undetected-spying.html · https://haveibeenpwned.com/Breach/Bromcom
- **GitHub 上批量假杀毒／VPN 仓库**：@Dinosn 再次报告多账号以相似模式投放疑似恶意仓库。X 原帖：https://x.com/Dinosn/status/2124717523916698011
- 勒索软件监测号今日点名的 RHYSIDA、Dark Project 等受害者清单，未见第一手确认，不作为独立要闻展开。

## SecureFlow 信息流精选

本日无显著更新。SecureFlow 的 all、community、blog 三路接口及站点首页在多次使用浏览器 UA 与站点 Referer 后仍返回 **HTTP 522**（Cloudflare 源站错误），未能拉取任何条目。

## AI/TLDR 动态

本窗口（约 36 小时、不在 seen_ids）新条目 **14** 条，其中 security **1** 条。订阅源共 50 条。今日 AI 圈的重点是：Anthropic 推出用 agent 审阅、修改并批准 GitHub PR 的 Claude Ship，并为企业 Claude 开放带零数据留存的 Frontier Safeguards 公测；客服 agent 公司 Sierra 完成 17.5 亿美元 F 轮、估值约 300 亿美元；Z.ai 发布带视觉编码能力的 GLM-5.4（Loop Transformer）；OpenCode 2.4.0 增加内置浏览器与定时自动化。安全侧最值得看的是美国俄勒冈州与弗吉尼亚州就 Grok 性深度伪造问题起诉 SpaceX——这是 AI/TLDR 本窗口唯一的 security 类条目。video／showcase 类低信号条目只计数（本窗口新条目中 video 4、showcase 1），不逐条展开。AI/TLDR 的 releases 详情页换 UA＋Referer 后仍 **403**，下面保留订阅条目链接。

### 安全

- **俄勒冈州与弗吉尼亚州就 Grok 深度伪造起诉 SpaceX**：AI/TLDR 称这是两州首次就 Grok 性深度伪造及其安全声明向 SpaceX 提起诉讼。详情页 403，原文来源页本期未单独展开。https://ai-tldr.dev/releases/oregon-virginia-sue-spacex-grok-deepfakes/

### 模型

- **GLM-5.4**：Z.ai 新旗舰，用 Loop Transformer（同一组层跑两遍）并加入面向编码的视觉能力。https://ai-tldr.dev/releases/zai-glm-5-4/

### 工具与开源仓库

- **Claude Ship**：Anthropic 的 agent 可对 GitHub PR 做审阅、修改并给出批准决定。https://ai-tldr.dev/releases/anthropic-claude-ship/
- **OpenCode 2.4.0**：内置浏览器、定时自动化，并可处理视频；agent 能使用已登录的真实浏览器会话。https://ai-tldr.dev/releases/anomalyco-opencode-2-4-0/
- **Google Search Personal Intelligence**：AI Mode 可连接 Wallet 与 Drive，按个人上下文作答。https://ai-tldr.dev/releases/google-search-personal-intelligence-wallet-drive/

### 论文与研究

- **DeepMind Quantum Algorithm Agents**：用 agent 寻找更便宜的量子线路，并由定理证明器（Lean）逐一校验，称成本最高可降约 290 倍。https://ai-tldr.dev/releases/google-deepmind-quantum-algorithms-agents-lean/

### 行业动态

- **Sierra F 轮 17.5 亿美元、估值约 300 亿美元**：客服 agent 公司约半年内估值再翻倍。https://ai-tldr.dev/releases/sierra-series-f-1-75b/
- **Enterprise Frontier Safeguards 公测**：Anthropic 为企业 Claude 增加误用监测，并称零数据留存。https://ai-tldr.dev/releases/anthropic-enterprise-frontier-safeguards-beta/
- 另有若干教程／本地模型入门条目未展开：https://ai-tldr.dev/releases/gpupartner-beginners-guide-local-ai-unsloth/

## Agent 用例动态

本窗口（约 48 小时、不在 seen_ids）新条目 **26** 条（RSS 共 60 条；11-23 计 14，11-22 计 12）。今天人们主要仍在用 Claude Code、Claude in Chrome、ChatGPT Agent、Perplexity Comet、Meta Muse 和 OpenClaw 做事：一边是浏览器／电脑操控（后台路径审计、批量上传、填表、清理 Windows、剪视频），一边是个人助理与生活后勤（保险单据解读、邮件分拣、订机票与披萨、购物车、旅行规划），也有把 agent 直接嵌进客户工单或一人公司的日常开发。与安全／权限更相关的条目放在前面：有人让浏览器 agent 只读走过自己的 Stripe、Cloudflare、Supabase 和 GitHub 后台，也有人给 agent 单独邮箱去完成注册验证——这两类都直接碰到账户权限与凭据边界。

### 安全与权限相关

- 有人用 Claude in Chrome 只读走查 106 条后台路径（Stripe、Cloudflare、Supabase、GitHub），再用 Claude Code 修正文档里过时的 8 条路径。https://agentusecases.ai/use-case/audit-vendor-dashboard-paths-and-correct-stale-docs
- 有人给 Meta Muse 单独配了邮箱，好让 agent 自己完成注册与验证邮件，而不卡在人机验证上。https://agentusecases.ai/use-case/give-an-agent-its-own-email-to-finish-sign-ups
- 有人用 Claude 连到任务管理器，诊断并清理变慢的 Windows 电脑。https://agentusecases.ai/use-case/diagnose-and-clean-up-a-slow-windows-pc
- 有人用 Perplexity Comet 填表、做合规培训并扫描 Facebook Marketplace，但称它最近开始拒绝这类 agent 任务。https://agentusecases.ai/use-case/fill-forms-and-scan-marketplace-with-a-browser-agent

### 编程、办公与多会话

- 有开发者用 Claude Code 回复客户 Jira 并按反馈改代码，客户以为在和本人对话。https://agentusecases.ai/use-case/handle-client-jira-tickets-and-fixes-with-claude
- 有小型代理公司老板用多路长时间 Claude Code 会话，在工作所在的机器上跑几乎全部项目。https://agentusecases.ai/use-case/run-an-agency-s-work-through-many-claude-code-sessions
- 有独立 SaaS 创始人让 Claude Code 写大部分代码，并以短信／电话在需要时向人请示。https://agentusecases.ai/use-case/run-a-solo-saas-with-an-agent-that-texts-you
- 有人用 Claude 做了手机端加 Mac 端的交接应用，以便在多台电脑之间控制 agent 会话。https://agentusecases.ai/use-case/control-agent-sessions-across-computers-from-mobile

### 浏览器、生活后勤与内容

- 有人用 Claude Code 对照 EOB 与保单，约三分钟看清拒赔单其实不用再付钱（未代为提交任何材料）。https://agentusecases.ai/use-case/explain-a-denied-insurance-claim-from-eob-and-policy
- 有人把 Claude Desktop 管文件、Claude in Chrome 负责往网站批量上传文档。https://agentusecases.ai/use-case/bulk-upload-documents-to-a-website-via-browser-agent
- 有人用 Claude 在个人电脑上跑视频剪辑流水线，不另装剪辑软件或 MCP 插件。https://agentusecases.ai/use-case/automate-video-editing-on-a-personal-pc
- 有人用 Claude Code skill 加上 Claude in Chrome，把收藏的食谱做成周菜单并在批准后填入 Whole Foods／Instacart 购物车（不自动结账）。https://agentusecases.ai/use-case/turn-saved-recipes-into-a-weekly-meal-plan-and-carts
- 有人请 ChatGPT Agent 找店并订披萨，agent 在弹窗里转了一圈，没订成。https://agentusecases.ai/use-case/order-a-pizza-to-your-house-with-an-agent
- 有人用 Perplexity Comet 打开 The Verge 首页并把所有 AI 报道在新标签页打开，还提到它处理过邮件、LinkedIn 和 Reddit。https://agentusecases.ai/use-case/open-every-ai-story-from-a-news-homepage-in-tabs
- 有评论用 Claude Code 做家谱研究。https://agentusecases.ai/use-case/research-your-family-tree-with-claude-code
- 有人用 Meta Muse 处理收件箱、起草回复并预订多伦多四人保龄球局；医生门户预约则碰到限制。https://agentusecases.ai/use-case/run-a-personal-assistant-that-handles-email-and-books-group-
- 有人用 Meta Muse 每小时分拣未读邮件，并在周一发送简报。https://agentusecases.ai/use-case/triage-unread-email-hourly-and-send-monday-briefings
- 有人用 Meta Muse 订机票，但邮箱填错，没收到确认。https://agentusecases.ai/use-case/book-flights-with-an-agent-with-a-failed-email-entry
- 有人用 OpenClaw 收集差旅发票、监控信息源并起草内容，或与 Claude Code 一起规划新西兰南岛行程。https://agentusecases.ai/use-case/collect-receipts-for-expense-reimbursements · https://agentusecases.ai/use-case/monitor-feeds-for-story-angles-and-draft-content · https://agentusecases.ai/use-case/plan-and-book-a-new-zealand-south-island-trip

其余未逐条展开的条目包括用 agent 集群冲击 P vs NP、把旧 Gmail 标为已读、用 Claude 写图片元数据脚本、以及安排每周调研摘要等。

## 地址／IoC 汇总

- `oskeysetup.com`：Unit 42 所述 Com 关联 vishing 活动中，用于开发者模式侧载伪装成 Chrome 的扩展、并走 `chrome.debugger` C2 的下载域。来源：https://unit42.paloaltonetworks.com/com-affiliate-vishing-attacks/ · https://x.com/mgreen27/status/2124815476354068918
- `masterdarky.com`：Huntress／The Hacker News 记录的 ScreenConnect 活动中，技术员主机被攻陷后拉取安装包的域名。来源：https://thehackernews.com/2026/11/hackers-exploit-critical-screenconnect.html
- 未见其他在本期高信号条目中被公开、且适合原样抄录的 IP、钱包或样本哈希。KEPCO 事件中论坛宣称者使用化名 Noiem，这是声称而非已确认归因，不作为技术 IoC。

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

## Agent Use Cases（用户 2026-11-05 加入，单独成节）

- 站点：https://agentusecases.ai/ ，持续扫描收录人们实际用 AI agent 做的事。
- RSS：https://agentusecases.ai/feed.xml （约 60 条，覆盖约 3 天，每天约 20 条，pubDate 为 GMT，带浏览器 UA 访问）。
- 去重键：auc:<use-case 链接>。

## 阮一峰《科技爱好者周刊》（用户 2026-11-05 加入，仅周末版）

- 博客：https://www.ruanyifeng.com/blog/index.html ；订阅源：https://www.ruanyifeng.com/blog/atom.xml
- 周刊一般每周五北京时间早上发布；报告日期（Santiago）为周六的那期收录 GitHub 项目和有趣文章。去重键：ryf:<周刊链接>。

## AI/TLDR（每日，ai-tldr.dev）

- 首页：https://ai-tldr.dev/
- Atom 订阅源：https://ai-tldr.dev/feed.xml （约 50 条／6 天；category 含 security、model、tool、repo、paper、article 等）
- security 类条目与 X／SecureFlow 交叉合并；去重键 atl:条目链接

### pwn.watch 与 ExploitGrid（2026-11-12 加入，与 X 交叉）

- pwn.watch 实时安全事件 RSS：https://pwn.watch/feed.xml （JSON：https://pwn.watch/feed.json）
- ExploitGrid 最新公开 exploit：https://api.exploitgrid.net/api/exploits?page=1&limit=100
- ExploitGrid KEV 修补期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines
- 页面：https://exploitgrid.net/vulnerabilities/<CVE> 、https://exploitgrid.net/exploits/<internalId>

## 来源搜索 URL

- X Latest 窗口：2026-11-22 22:51 UTC～2026-11-23 22:56 UTC（约 24 小时）。CVE 组 Latest：约 4 分钟（25 条，噪声刷屏）；CVE relevancy 补搜：约 16.09 小时（25 条）；CVE 编号／advisory recency：约 0.3 小时（25 条）；MONAI／MailAssure／known exploited relevancy：约 23.3 小时（25 条）。工具组 Latest：约 23.68 小时（13 条）。威胁组 Latest：约 2.77 小时（25 条）；威胁 relevancy：约 22.44 小时（25 条）。LWiS List 只读：https://x.com/i/lists/1239330068461244424 ，9 屏合并去重 216 条，约 23.84 小时。
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （**HTTP 522**，重试仍 522；本窗口新条目 0）
- SecureFlow community 源列表：https://secureflow.scope-sentry.top/api/rss/category?category=community （**HTTP 522**，未能逐源拉取）
- SecureFlow blog 源列表：https://secureflow.scope-sentry.top/api/rss/category?category=blog （**HTTP 522**，未能逐源拉取）
- pwn.watch RSS：https://pwn.watch/feed.xml （200，50 条；JSON 200）。本窗口新条目 **0**（`lastBuildDate` 2026-11-08 20:19:52 GMT）。
- ExploitGrid exploits：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （200，100 条）。本窗口（48 小时）新条目 **0**（最新 `date` 2026-11-20 19:48:48 UTC）。
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （200，10 条；与 CISA 官方不完全一致，缺今日新增与 11-24 到期条目，以 CISA 为准）。
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （200，目录 1792 条，`dateReleased` 2026-11-23T19:43:55Z；本窗口新增 2 条）。
- AI/TLDR Atom：https://ai-tldr.dev/feed.xml （200，50 条）。本窗口（约 36 小时、未在 seen_ids）新条目 **14**，其中 security **1**。releases 详情页 **403**。
- Agent Use Cases RSS：https://agentusecases.ai/feed.xml （200，60 条）。本窗口（约 48 小时、未在 seen_ids）新条目 **26**。
- 阮一峰 Atom：https://www.ruanyifeng.com/blog/atom.xml （200，已确认最新周刊第 420 期已在 seen_ids；本日非周末，不收录）。
- CISA 今日警报：https://www.cisa.gov/news-events/alerts/2026/11/23/cisa-adds-two-known-exploited-vulnerabilities-catalog （200）

---

**落盘**：box 路径 `/home/box/workspace/security-watch/reports/2026-11-23-x-security-digest.md`；本机路径 `/Users/kenny1337/Desktop/_05_项目/X安全情报晚报/2026-11-23-x-security-digest.md`。
