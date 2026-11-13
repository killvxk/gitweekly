# X 安全情报晚报 · 2026-11-11（周三）

> 报告时间：2026-11-11 约 20:15（America/Santiago）＝ 2026-11-12 约 07:15（香港时间）。
> **覆盖时长**：X 只读搜索窗口 2026-11-10 23:00 UTC～11-11 23:00 UTC（24 小时）。CVE 组 Latest 一页 25 条只覆盖 11-11 22:30～22:58 UTC，因此用 relevancy 补搜（25 条，覆盖 11-10 23:18～11-11 22:30），另补「在野利用」组 25 条（11-10 23:04～11-11 22:39）和定向组 25 条；工具组（github.com + C2/红队等）Latest 只命中 1 条、relevancy 2 条，工具节主要靠 LWiS List；威胁报告组 Latest 25 条（11-11 17:09～23:00）＋relevancy 25 条（00:42～22:37）＋恶意软件补搜 25 条（11-10 23:03～11-11 22:19）。LWiS X List 翻三页共 287 帖，覆盖 11-10 16:45～11-11 22:58 UTC（超过 24 小时）。SecureFlow 取近 48 小时（blog 放宽 7 天）；AI/TLDR 取 36 小时；Agent Use Cases 取 48 小时。
> **新信源说明**：pwn.watch 订阅源（feed.xml／feed.json／changes.json）最后生成于 2026-11-08 20:19 UTC，本窗口内 **0 条新事件**，只把 2 个已有事件页作为佐证；ExploitGrid 最新 exploit 列表最新一条是 11-10 19:33 UTC，本窗口内 **0 条新增**，但按 CVE 查询与 KEV 期限接口做了交叉核对（见 CVE 节与来源节）。
> **验收说明**：见文末「验收结果」。
> 公开备援：CISA KEV 目录版本仍为 2026.11.10，11-11（美国退伍军人节）无新增；**11-12（香港时间今天）是 OpenSSH（Alpine/musl）、IBM Aspera Faspex、FreeSWITCH、GPUStack 四条 KEV 的联邦修补期限**，Barracuda 两条是明天 11-13。

## 今日摘要

- **Windows CLFS 未修补 0day「SignDrop」公开**：研究者 MSNightmare 公开 CLFS 日志认证机制（.cnpf 签名文件）的本地提权，普通用户可拿 SYSTEM；无 CVE、无补丁、微软未确认。**不要关闭 CLFS 认证**来规避（会重新暴露旧的内存破坏漏洞）。
- **Fortinet 11 月 PSIRT 大批量**：89 份公告约 98 个漏洞、19 个严重，FortiOS（HA 未认证命令执行 CVSS 9.0、OSPF 认证绕过 9.3）、FortiMail（多个未认证 RCE）、FortiManager/FortiAnalyzer、FortiAuthenticator 都有；部分由 AI 模型发现，厂商标注均未被利用。X 上有账号把这些标成「无补丁」，与厂商公告不符，以 FortiGuard 为准。
- **补丁日跟进**：Windows Kerberos CVE-2026-85844（CVSS 9.8，未认证中继到域控拿 SYSTEM，未被利用）是本月 DC 最该先补的；Outlook 在野 0day CVE-2026-124194 细节明确为「打开特制消息文件即泄露 NTLMv2 哈希」，建议同时封出站 SMB。Git CVE-2026-111760 递归克隆可执行代码，已出 2.56.1 等修复版。
- **APT／事件**：Group-IB 曝光俄语操作者 DarkLunnen 暴露的服务器（14 个月行动，FortiGate 后门账号、乌克兰无人机厂商源码窃取尝试）；Kaspersky ICS CERT：BO Team 潜伏俄罗斯工业软件开发商数月，已摸到代码签名服务器；vx-underground 称 Kimsuky 新版 GrimResource 活动；Maersk 确认被 WhiteArmor 勒索、Nitori 3,762 万条客户记录外泄。
- **AI 安全**：Depi 披露 OpenAI Codex 的 GitHub Actions 工作流可被提示注入，串联到可能控制官方 npm 包发布（已修复）；Microsoft Research「Lazarus」改不到 10 个神经元即可给 agent 植入后门；AntiFox AI 渗透平台被用于窃取 AWS 凭据；VulnCheck 复盘 Anthropic Project Glasswing：442 个 CVE，仅 2 个被在野利用、修复率低。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

**1. Windows CLFS 本地提权 0day「SignDrop」（无 CVE、无补丁，已有公开 exploit）**
- 谁／什么：研究者 MSNightmare（Nightmare Eclipse）11-10 公开。问题出在 clfs.sys 为新日志容器生成 .cnpf 认证文件的逻辑：可诱使高权限进程（如 Defender）打开普通用户准备的日志，由 SYSTEM 生成签名文件并继承原文件权限，最终本地提权到 SYSTEM。研究者称 CLFS 认证处于 learning 或 enforcement 模式的系统都受影响（注册表 `HKLM\SYSTEM\CurrentControlSet\Services\CLFS\Authentication\Mode` 为 0/1）；目前没有独立复现，微软未确认。
- 处置：等微软补丁；**不要关闭 CLFS 认证**；收紧本地代码执行（应用控制、最小权限）；监控 Defender 等高权限进程异常创建 .cnpf 文件、异常 SYSTEM 子进程。
- X 原帖：[MSNightmare2000](https://x.com/MSNightmare2000/status/2120395194545864828) · [Dinosn 转发（171 赞）](https://x.com/Dinosn/status/2120412595354239379) · [CipherSecurityN 摘要](https://x.com/CipherSecurityN/status/2120408470654431718) · [Jean_Maes_1994 提醒未验证](https://x.com/Jean_Maes_1994/status/2120412814921576731)
- 文章：[SecurityOnline](https://securityonline.info/signdrop-windows-clfs-zero-day-poc/) · [Cyber Security News](https://cybersecuritynews.com/windows-signdrop-zero-day-exploit/) · [微软 CLFS 日志认证说明](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/clfs-authentication)

**2. Fortinet 11 月 PSIRT：约 98 个漏洞、19 个严重（11-10 发布，均标注未被利用）**
- 谁／什么：FortiOS FG-IR-26-273（CVE-2026-126259，HA FGSP＋standalone-config-sync 或 autoscale 场景下未认证以超级管理员执行命令，CVSS 9.0）、FG-IR-26-267（CVE-2026-126253，OSPF 守护进程认证绕过，CVSS 9.3，需相邻网络，由 Fortinet 内部借助 AI 模型发现）；FortiMail 多个未认证 RCE／认证绕过（CVE-2026-126147、-126148、-126150、-126155～126157、-126263 等）；FortiAnalyzer CVE-2026-126170（9.8）、FortiAuthenticator 硬编码口令 CVE-2026-126257 等。
- 修复版本：FortiOS 8.0.2／7.6.8／7.4.13／7.2.14（7.0 需迁移）；FortiMail 8.0.2／7.6.7／7.4.9；FortiAuthenticator 8.0.4／6.6.11；FortiManager/FortiAnalyzer 8.0.2／7.6.8／7.4.12。
- 处置：优先 FortiMail 与启用 HA 同步的 FortiOS；管理面不暴露公网。注意 X 上 KaitanSecurity 批量帖标注「No patch yet」，与 FortiGuard 公告不符。
- X 原帖：[Dinosn 转 SecurityWeek](https://x.com/Dinosn/status/2120556122793034213) · [Balgan 点评](https://x.com/Balgan/status/2120328558052827601) · [cvedotnow（FortiMail CVE-2026-126146）](https://x.com/cvedotnow/status/2120650421735723185) · [KaitanSecurity（FortiOS CVE-2026-126259）](https://x.com/KaitanSecurity/status/2120645273152033090)
- 厂商公告：[FG-IR-26-273](https://fortiguard.fortinet.com/psirt/FG-IR-26-273) · [FG-IR-26-267](https://www.fortiguard.com/psirt/FG-IR-26-267) · [FortiGuard PSIRT 列表](https://www.fortiguard.com/psirt?product=FortiMail)
- 文章：[SecurityWeek](https://www.securityweek.com/fortinet-patches-nearly-100-vulnerabilities/) · [NHS England Digital CC-4888](https://digital.nhs.uk/cyber-alerts/2026/cc-4888)（box 直连 403，经抓取服务读到全文）

**3. Windows Kerberos 认证绕过 CVE-2026-85844（CVSS 9.8，11 月补丁日修复，未被利用）**
- 谁／什么：未认证攻击者发送特制 Kerberos 认证流量并中继到域控，可拿 SYSTEM，无需用户交互；覆盖 Windows 10/11 与 Server 2012～2025。微软标为 Important，但 CVSS 9.8。
- 处置：域控与依赖 Kerberos 的服务器优先装 11 月更新；临时可限制到 Kerberos／域服务的网络访问。
- X 原帖：[DirectoryRanger 转 martinsohndk「Patch DCs NOW」](https://x.com/DirectoryRanger/status/2120627521691529349)
- 厂商公告：[NVD CVE-2026-85844](https://nvd.nist.gov/vuln/detail/cve-2026-85844) · [MSRC CVE-2026-85844](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85844)

**4. Outlook 在野 0day CVE-2026-124194 跟进（KEV，期限 11-24）**
- 新细节：打开特制消息文件后 Outlook 会在无外部内容警告的情况下连接攻击者服务器，泄露用户 NTLMv2 哈希；X 上有帖称该漏洞与 Anthropic 研究员（借助 Claude）共同致谢，未见厂商原文核实，仅作线索。本月补丁总数各方统计不一（1,093～1,259 个 CVE）。
- 处置：装 Office/M365 11 月更新；边界封出站 SMB（TCP 445）；MyCERT 已发公告。
- X 原帖：[modularciso](https://x.com/modularciso/status/2120341491650269607) · [runbooklab（含修复版本号）](https://x.com/runbooklab/status/2120403402903450055) · [MyCERT](https://x.com/mycert/status/2120512150611607918) · [Bstretweetz](https://x.com/Bstretweetz/status/2120650634978537874)
- ExploitGrid：KEV 期限页已收录（[CVE-2026-124194](https://exploitgrid.net/vulnerabilities/CVE-2026-124194)），按 CVE 查询公开 exploit 为 0 条。
- 文章：[The Register：补丁日超 1,000 个漏洞仅 1 个 0day](https://www.theregister.com/security/2026/11/10/november-patch-tuesday-boasts-over-1000-bugs-but-only-one-zero-day-so-far/5308946)

**5. Chrome 在野 0day CVE-2026-125350 跟进（KEV，期限 11-24）**
- X 上讨论量最大的仍是这条（Pirat_Nation 356 赞）。ExploitGrid 11-10 收录 1 个同名 GitHub 仓库：**已有公开 exploit**（类型未定、状态待核），见 [ExploitGrid 页面](https://exploitgrid.net/exploits/EGE-GH-lP1vXLv)。
- X 原帖：[Pirat_Nation](https://x.com/Pirat_Nation/status/2120517401531879603) · [tsnmediahub（KEV 更正）](https://x.com/tsnmediahub/status/2120645305158750412)
- 文章：[Android Headlines](https://www.androidheadlines.com/2026/11/another-chrome-zero-day-is-being-exploited-in-the-wild-and-google-just-pushed-a-fix.html)（Cloudflare 拦截 box 访问，链接取自 X 帖的展开结果）

**6. Git 递归克隆代码执行 CVE-2026-111760（已修复）**
- 谁／什么：索引处理中的整数截断，超长路径可通过安全检查后被写成攻击者指定的 .git，替换子模块 .git 文件为指向恶意 hooks 的符号链接，`--recursive` 克隆即可执行代码。修复版 Git 2.56.1，以及 2.50.2、2.51.3、2.52.1、2.53.1、2.54.1、2.55.1；GitHub Enterprise Server 3.19.15／3.20.11／3.21.9／3.22.4。
- 处置：升级 Git 及自带 Git 的工具（IDE、CI 镜像）；不要递归克隆不可信仓库。
- X 原帖：[Dinosn 转 THN](https://x.com/Dinosn/status/2120465599579279686)
- 文章：[The Hacker News](https://thehackernews.com/2026/11/git-patches-flaw-that-lets-malicious.html)

**7. Zyxel GS1900 交换机 CVE-2026-107441 跟进（pwn.watch＋ExploitGrid 佐证）**
- 11-03 起已报。X 本窗口继续传播 THN「6 月补丁没挡住」报道：GreyNoise 观测到约 996 台交换机被入侵，Binarly 发现攻击用的 exploit 对修了 CVE-2026-7273 的固件仍有效。
- pwn.watch：状态 patched，修复固件为各型号 2.90(...3)C0（10-22 发布、11-03 公告）。[pwn.watch 事件页](https://pwn.watch/i/zyxel-gs1900-switches-zero-day-cve-2026-107441)
- ExploitGrid：已有公开 exploit（收录 1 条扫描器类仓库），[ExploitGrid 页面](https://exploitgrid.net/exploits/EGE-GH-tCXL1re)
- X 原帖：[P7RIM3](https://x.com/P7RIM3/status/2120316403039207839) · [TonyBeeTweets](https://x.com/TonyBeeTweets/status/2120414952905457745)
- 文章：[The Hacker News](https://thehackernews.com/2026/11/zyxel-gs1900-patch-fails-to-block-zero.html)

**8. KEV 期限提醒（ExploitGrid KEV 期限接口交叉核对）**
- **11-12 到期（香港时间今天）**：OpenSSH/Alpine musl 口令认证绕过 CVE-2026-123158、IBM Aspera Faspex CVE-2026-123218、FreeSWITCH CVE-2026-116779、GPUStack CVE-2026-102895；**11-13 到期**：Barracuda CVE-2026-116606／CVE-2026-111560。
- 其中 CVE-2026-123158（[ExploitGrid](https://exploitgrid.net/vulnerabilities/CVE-2026-123158)）、CVE-2026-123218（[ExploitGrid](https://exploitgrid.net/vulnerabilities/CVE-2026-123218)）**已有公开 exploit**（11-09～11-10 收录多条实验／扫描类仓库）。先知社区同期有一篇 OpenSSH/musl 漏洞成因与修复版本对比分析：[xz.aliyun.com/news/93241](https://xz.aliyun.com/news/93241)。
- Barracuda 佐证：[pwn.watch 事件页](https://pwn.watch/i/barracuda-authorization-bypass-command-injection-cve-2026-116606)（状态 patched）。
- 来源：[ExploitGrid KEV 期限 API](https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines) · [CISA KEV 目录](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

**9. ZDI 11-11 一次公开 47 个 Meta 开源 AI 库 0Day（ZDI-26-907～953，SecureFlow·ZDI-vulnerabilities）**
- 谁／什么：fairseq 31 个、FAIRChem 9 个、Detectron2 6 个、fairseq2 1 个，全是加载 YAML 配置／checkpoint／NPZ 时的代码注入或反序列化 RCE，ZDI 标注为 0Day（厂商未修复即公开）。X 上本窗口未见讨论。
- 处置：只加载可信来源的模型、配置与 checkpoint；在隔离环境里跑研究代码。
- 公告：[ZDI-26-907](https://www.zerodayinitiative.com/advisories/ZDI-26-907/) · [ZDI-26-912](https://www.zerodayinitiative.com/advisories/ZDI-26-912/) · [ZDI-26-913](https://www.zerodayinitiative.com/advisories/ZDI-26-913/) · [ZDI-26-939](https://www.zerodayinitiative.com/advisories/ZDI-26-939/) · [ZDI-26-945](https://www.zerodayinitiative.com/advisories/ZDI-26-945/) · [ZDI-26-952](https://www.zerodayinitiative.com/advisories/ZDI-26-952/)

**10. 其他值得关注**
- Cisco Expressway CVE-2026-76466（CVSS 9.8）与 VMware vCenter CVE-2026-59310/59309：LWiS @Dinosn 转发公开 exploit 工具，均为旧漏洞（ExploitGrid 首次收录分别在 10-26、8 月），**已有公开 exploit**，未打补丁的实例风险上升。X 原帖：[Dinosn（Expressway）](https://x.com/Dinosn/status/2120463385808781790) · [Dinosn（vCenter）](https://x.com/Dinosn/status/2120489639064883342)；ExploitGrid：[EGE-GH-AR2PTxd](https://exploitgrid.net/exploits/EGE-GH-AR2PTxd) · [EGE-GH-bn9q0oU](https://exploitgrid.net/exploits/EGE-GH-bn9q0oU)
- Xen Orchestra 认证绕过在野利用（昨日已报）：THN 跟进。[THN](https://thehackernews.com/2026/11/hackers-exploit-critical-xen-orchestra.html)（[Dinosn](https://x.com/Dinosn/status/2120465768123093491)）
- Project Zero 公开苹果 RawCamera Panasonic RW2 解码越界读：[Project Zero issue](https://project-zero.issues.chromium.org/issues/553365741)（[ProjectZeroBugs](https://x.com/ProjectZeroBugs/status/2120515708132229234)）
- PortSwigger：在严格 CSP（default-src 'none'; form-action 'self'）下窃取凭据的研究：[PortSwigger Research](https://portswigger.net/research/blind-trust-stealing-credentials-through-csp)（[garethheyes](https://x.com/garethheyes/status/2120523485558755423)）
- Entra 新租户「默认坏掉」：唯一管理员被要求 MFA 但条件访问又阻止注册 MFA（[_dirkjan](https://x.com/_dirkjan/status/2120636986948010477)）。
- 奇安信攻防社区「Go CONNECT 双向串线漏洞」：[forum.butian.net/share/5358](https://forum.butian.net/share/5358)（box 网络连不上、抓取服务 403，链接取自 SecureFlow 原始数据）

## 工具与 GitHub 发布（每条：说明 + 地址列表）

**1. LWiS 成员分享的红队／检测工具**
- Tendril：模块化持久化工具包（C# 程序集、统一 BOF、Mythic 命令、Cobalt Strike aggressor），防守方可据此梳理持久化检测点。[GitHub](https://github.com/Whispergate/Tendril)（[@ipurple](https://x.com/ipurple/status/2120640830155403545)）
- Copperhound：Rust 写的 AD／ADCS／Entra ID 攻击路径分析，可吃 SharpHound、bloodhound-python、ldapdomaindump、AzureHound 输出，面向超大环境。（[@ipurple](https://x.com/ipurple/status/2120614792146944463)）
- 独立 WinRM 哈希传递 BOF（内存内完成 NTLMv2 认证、签名加密与 WSMan 通信）。（[@ipurple](https://x.com/ipurple/status/2120594408072679842)）
- impacket-rs：Impacket 核心协议与 AD 部分的 Rust 重写。[GitHub](https://github.com/nestho/impacket-rs)（[@Dinosn](https://x.com/Dinosn/status/2120425203318522317)）
- yamatosecurity 预告 Windows 取证工件一体化解析工具（[@ntlmrelay 转](https://x.com/ntlmrelay/status/2120445162656788953)）

**2. 检测与研究文章**
- ScriptBlock Smuggling 绕 AMSI：仿真＋检测指引并重。[ipurple.team](https://ipurple.team/2026/11/11/scriptblock-smuggling/)（[@ipurple](https://x.com/ipurple/status/2120559315178172476)）
- 用彩虹表破解降级的 NTLMv1-SSP 哈希（Server 2022）：[hunio.org](https://hunio.org/security/ntlmv1-ssp-cracking/)（[@Dinosn](https://x.com/Dinosn/status/2120465546731000160)）；同日微软 NTLM 签名加固受到好评（[@maxime_tz 转](https://x.com/maxime_tz/status/2120560546416087322)）。
- 运行时定位 DLL 基址的 PEB 遍历替代方法：[blog.jaytiwari.me](https://blog.jaytiwari.me/posts/Beyond-PEB-Walking-Alternative-Ways-to-Find-DLL-Base-Addresses-and-Resolve-Functions-at-Runtime/)（[@ipurple](https://x.com/ipurple/status/2120482875388699036)）
- Defender 内部「飞行记录器」取证：[protokol-7](https://protokol-7.github.io/dfir/2026/11/10/defenders-hidden-flight-recorder-mpenginedb.html)（[@whokilleddb 转](https://x.com/whokilleddb/status/2120584854089998494)）
- Entra ID 令牌窃取（4/4）：OAuth 2.0 标准缺口：[Insinuator](https://insinuator.net/2026/11/token-theft-in-microsoft-entra-id-part-4-of-4-oauth-2.0-standard-gaps/)（[@DirectoryRanger 转](https://x.com/DirectoryRanger/status/2120627687769375085)）
- GitGuardian：45 个 agent 化攻击框架盘点及其找什么凭据：[GitGuardian 博客](https://blog.gitguardian.com/ai-pentesting-tools-beyond-artex/)（[@m3g9tr0n 转](https://x.com/m3g9tr0n/status/2120513409280086096)）
- ESET 的 Turla CerealLoader 混合模式技术已有研究者复刻（LWiS @ipurple 转，未附代码链接）：[@ipurple](https://x.com/ipurple/status/2120418521637163284)

**3. 行业**
- ProjectDiscovery：调查 214 名从业者，44% 不完全验证就关闭／降级漏洞发现；另称 Mythos 5.2 是其测过最强的安全模型。（[@pdiscoveryio 调查](https://x.com/pdiscoveryio/status/2120597825482522942) · [@pdiscoveryio 模型评测](https://x.com/pdiscoveryio/status/2120546702549778779)）
- 英国 NCSC 推出「Cyber Adversary Simulation」计划，帮助关键组织做对抗演练（[@benpturner 转](https://x.com/benpturner/status/2120537798726049827)）。
- Outflank 十周年（[OutflankNL](https://x.com/OutflankNL/status/2120584911899771262)）。

## APT / Malware 分析（每条：说明 + 地址列表）

**1. Group-IB：DarkLunnen 暴露服务器，14 个月针对欧洲的行动**
- 谁／什么：拉脱维亚服务器开放目录暴露俄语操作者工作环境（457 个文件取回 35 个）：用改造的 FortiGate CVE-2024-55591 PoC 植入名为「service」的超级管理员后门账号（约 600 台土耳其设备易受影响）；对乌克兰 Aerorozvidka、UkrSpecSystems、Skyeton 等无人机／航空单位做 git-dumper 源码窃取尝试（未确认成功）；VNC 爆破 5,775 个端点（约四分之一像 HMI／ICS）；Hikvision CVE-2017-7921 扫描；Sliver C2。
- 狩猎：FortiGate 上排查名为 service 的超级管理员账号；IoC 见下。
- X 原帖：[GroupIB_TI](https://x.com/GroupIB_TI/status/2120420236927312197)
- 文章：[Group-IB 报告全文（unsafe.sh 转载；group-ib.com 原文链接从 box 与抓取服务访问均返回 404，故不直接引用）](https://unsafe.sh/go-454113.html) · [SecQuill 摘要](https://secquill.com/articles/exposed-server-reveals-14-months-of-a-hacker-s-operations-against-european-targets/)

**2. Kaspersky ICS CERT：BO Team 潜伏工业软件开发商数月，摸到代码签名服务器**
- 谁／什么：经 SSH 口令登录外网 Linux 终端服务器进入，用 vCenter 上的 Log4Shell 拿 root，在宿主机布置伪装成 PostgreSQL/VMware 组件的 cron 后门，拿到 krbtgt（黄金票据），控制 GitLab、Ansible、备份、邮件、DNS，并试图在代码签名服务器上放后门；没有加密或破坏数据，目标疑为供应链。被清出后还用窃取的 DKIM 私钥发钓鱼邮件。
- X 原帖：[cyb3rops 转 e_kaspersky](https://x.com/cyb3rops/status/2120639558127648947)
- 文章：[Kaspersky ICS CERT 报告（俄文）](https://ics-cert.kaspersky.ru/publications/reports/2026/11/05/supply-chain-attack-bo-team-in-a-software-developers-infrastructure/)

**3. Kimsuky（APT43）新版 GrimResource 活动（vx-underground）**
- vx-underground 分析 malwrhunterteam 与 @smica83 分享的样本（含 edge.msc），认为是 3 月 GrimResource 活动的改进版，shellcode 藏在资源中；样本细节以原帖为准。
- X 原帖：[vxunderground 判断](https://x.com/vxunderground/status/2120583082520559923) · [vxunderground 起因](https://x.com/vxunderground/status/2120395931631624450) · [malwrhunterteam 样本线索（经 @cyb3rops 转）](https://x.com/cyb3rops/status/2120482235715620961)

**4. macOS 窃密＋后门新样本（L0Psec 线程）**
- 编译后的 AppleScript「GoogleHelper.scpt」（VT 0 检出）→ C++ 窃密程序用伪造 Google 页面弹框骗口令，收集备忘录、钱包、浏览器数据 → 混淆 Go 后门（持久化、每分钟读剪贴板、支持命令执行与 SOCKS5）。备用下载源包括 Dropbox、Telegram 和多个 IP。IoC 见下。
- X 原帖：[L0Psec 线程](https://x.com/L0Psec/status/2120630150245265737) · [L0Psec IoC](https://x.com/L0Psec/status/2120630183216763083)

**5. 勒索与数据泄露**
- Maersk 确认被收购子公司的本地遗留系统遭入侵、数据被窃，WhiteArmor 索要 500 万美元并威胁公开约 100GB；称运营不受影响。[BleepingComputer](https://www.bleepingcomputer.com/news/security/maersk-confirms-data-breach-as-whitearmor-ransomware-demands-5-million/) · [The Register](https://www.theregister.com/security/2026/11/11/shipping-giant-maersk-probes-it-security-incident-data-theft/5309096)（[Dinosn](https://x.com/Dinosn/status/2120556506903097478)）
- 日本家居零售商 Nitori：11-06 发现入侵，攻击者疑自 10 月中旬起潜伏，最多 3,762 万条客户记录可能外泄（不含密码与信用卡）。[BleepingComputer](https://www.bleepingcomputer.com/news/security/japanese-furniture-giant-nitori-says-hackers-stole-376m-customer-records/)（[Dinosn](https://x.com/Dinosn/status/2120465444893286600)）
- Railway 10 月事件跟进：攻击者经构建基础设施逃逸拿内部凭据与源码，最多约 10 万个 workspace 的环境变量可能泄露，并产生约 74 万美元 AI 盗刷费用。[BleepingComputer](https://www.bleepingcomputer.com/news/apple/railway-breach-leads-to-740-000-in-fraudulent-ai-charges/)（[Dinosn](https://x.com/Dinosn/status/2120465200487039324)）
- MSP Process 供应商入侵导致客户 M365 租户的 OAuth 客户端密钥与 GDAP 令牌外泄，至少 1 个环境确认恶意活动、另 47 个有认证尝试（[DFIR_Radar](https://x.com/DFIR_Radar/status/2120562862154252451)）。
- AllUnited（荷兰俱乐部会员平台）表单缺陷致含 IBAN 的会员数据被批量复制：[TSN Media](https://tsnmedia.org/allunited-data-breach/)（[tsnmediahub](https://x.com/tsnmediahub/status/2120652895490073062)）

**6. 其他活动**
- AntiFox（开源 AI 渗透平台，托管在阿里云）被用于打 Web 服务、植入 ASPX webshell、滥用 AWS IAM／EC2 角色凭据，部分案例读取生产 Secrets Manager 机密、读删 S3 对象。[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-use-antifox-ai-agents-in-aws-credential-theft-attacks/) · [GitGuardian](https://blog.gitguardian.com/another-new-ai-hacking-agent-vs-the-same-credential-problem-antifox-targeting-aws-credentials/)（[Dinosn](https://x.com/Dinosn/status/2120554953102245934)）
- Qlik Sense 服务器被下发 PowerShell 反弹 shell（Cynet），攻击者服务器上还有 ActiveMQ CVE-2023-46604 与 Veeam CVE-2024-40711 工具。[文章](https://kylesinvestigation.com/2026/11/11/qlik-sense-servers-hit-with-powershell-reverse-shells-attacker-server-holds-activemq-and-veeam-exploits/)（[Dinosn](https://x.com/Dinosn/status/2120555280815858072)）
- 多个无关团伙在被控 Linux 服务器上滥用 GSocket（gs-netcat）维持可跨补丁存活的 C2，3～8 月检出增长 356.2%（[DFIR_Radar](https://x.com/DFIR_Radar/status/2120623413383344530)）。
- AhnLab：韩国 DVR 管理软件 CMS 被用于 DLL 侧载投放 Wpcdoor 后门。[ASEC](https://asec.ahnlab.com/en/96477/)（[AhnLabGlobal](https://x.com/AhnLabGlobal/status/2120412528572538918)）
- Huntress：ClickFix 演进为隐写载荷重组、浏览器缓存投递、伪装 RMM 的 Node.js RAT（DuskDesk）（[DFIR_Radar](https://x.com/DFIR_Radar/status/2120442051128852958)）。
- 伊朗 Imperial Kitten 继续打航空航天与国防（钓鱼门户、多级 DLL 侧载、Azure 托管 C2）（[DFIR_Radar](https://x.com/DFIR_Radar/status/2120457513242075262)）；APT-C-36（Blind Eagle）新一轮拉美攻势，用假法院传票投递远控（[zenox_intell](https://x.com/zenox_intell/status/2120476589871800330)）。
- 新样本：NonElevatedDll 模块化后门，经 ASUS WebStorage 走 HTTPS 轮询（[ShanHolo](https://x.com/ShanHolo/status/2120603011697242488)）；Swarm 生态 bee-js 与 Swarm Desktop 供应链被投毒窃取以太坊钱包（[insicurezzadigitale](https://insicurezzadigitale.com/supply-chain-su-swarm-bee-js-e-swarm-desktop-compromessi-per-rubare-wallet-ethereum)）。
- Remus Stealer 兜售号称改密码后仍能读 Gmail 的功能（每月 1,000 美元，未经验证）：[Security Affairs](https://securityaffairs.com/202853/malware/hackers-advertise-a-1000-gmail-tool-that-allegedly-survives-password-resets.html)

**7. AI 安全**
- Depi：OpenAI Codex 的 issue-labeler 工作流可被提示注入，串联 CLR 沙箱逃逸读出 Runner 内存中的机密、再做 GitHub 缓存投毒，理论上可控制官方 @openai/codex npm 包的后续发布；OpenAI 已修复。[Depi 博客](https://depi.security/blog/20261111-backdooring-codex/)（[@N3mes1s 转](https://x.com/N3mes1s/status/2120621824660623410)）
- Microsoft Research「Lazarus」：改写模型最后前馈层里不到 10 个休眠神经元，即可让 agent 平时正常、遇到触发词时执行恶意命令，能通过常规评测；建议做权重完整性与来源校验。[Microsoft Research 博客](https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/)（[MSFTResearch](https://x.com/MSFTResearch/status/2120295164379824154)）
- VulnCheck 复盘 Project Glasswing 七个月：账本 37,966 条发现、仅 217 条标为已修复；可归因 CVE 442 个（约占 2026 年 0.5%），仅 2 个被在野利用；curl 34 份报告拒了 19 份。[VulnCheck 博客](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)（[jeremiahg](https://x.com/jeremiahg/status/2120542706447622614) · [VulnCheckAI](https://x.com/VulnCheckAI/status/2120570883630907800)）
- 反 AI 侦察「焦油坑」：页面声明里藏指令，诱导 AI agent 下载解压炸弹并清空记忆（[fr0gger_](https://x.com/fr0gger_/status/2120364989060149505)）；AI 攻击者基础设施研究汇总 5,884 个 IP：[ella-bakshi.github.io](https://ella-bakshi.github.io/ai-attacker-threat-research/)（[Dinosn](https://x.com/Dinosn/status/2120354211225362880)）

## SecureFlow 信息流精选（X 上未出现的高信号条目，按 community／blog／BugBounty 分组）

**community**
- 奇安信攻防社区「Go CONNECT 双向串线漏洞」：[forum.butian.net/share/5358](https://forum.butian.net/share/5358)（已并入 CVE 节第 10 条）
- 先知社区「OpenSSH/musl 口令认证绕过漏洞底层分析及修复版本对比剖析」：[xz.aliyun.com/news/93241](https://xz.aliyun.com/news/93241)（已并入 CVE 节第 8 条，对应今天到期的 KEV CVE-2026-123158）
- Seebug、t00ls、InfoSec Write-ups、Critical Thinking：48 小时窗口内无未收录新条目；吾爱破解 2024-09 起未更新。

**blog**
- ZDI-vulnerabilities：ZDI-26-907～953 共 47 条 Meta 开源 AI 库 0Day，已并入 CVE 节第 9 条。
- ZDI-Blog、projectdiscovery、samcurry、dirkjanm、leavesongs、brutecat 等：7 天窗口内无首次出现的新文章；「微信公众号」源 2025-02 起未更新。

**BugBounty（HackerOne 公开报告，SecureFlow all 共 19 条，2 条昨日已报未重复）**
- WordPress Playground 的 DOM XSS（/scope:*/wp-includes/empty.html）：[HackerOne #3863343](https://hackerone.com/reports/3863343)
- 同一广告投放管理类项目一次公开 15 份（投放代码页 CSRF、多处反射／存储型 XSS、跨 agency 越权、请求优先级导致的访问控制绕过与盲注等），例：[#3896779 盲注](https://hackerone.com/reports/3896779) · [#3831102 访问控制绕过](https://hackerone.com/reports/3831102) · [#3883840 跨 agency 泄露](https://hackerone.com/reports/3883840)
- 未认证可在任意时间（含非营业时段）预约：[HackerOne #3943436](https://hackerone.com/reports/3943436)

## AI/TLDR 动态（来自 ai-tldr.dev；本窗口 36 小时内新条目 13 条，其中 security 类 0 条）

今天 AI 圈偏工具与模型小步更新：Google 连出 Gemini Decisions API（返回概率而不是文本）、Labs 的 Tabletop 和 DeepMind AlphaGenome 2；阿里开放 Qwen4-Max 两周预览；Amazon 把一个工单分类任务从 Claude Sonnet 4.6 换成小决策模型，成本降约 44 倍。安全相关只有 VulnCheck 对 Glasswing 的复盘（归在 article 类）。

**安全**
- 【安全，X 交叉】VulnCheck 复盘 Project Glasswing：442 个 CVE、2 个被利用，分诊压力落在维护者身上。[AI/TLDR](https://ai-tldr.dev/releases/vulncheck-glasswing-november-update/) · [VulnCheck 博客](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)

**模型**
- Gemini Decisions API：对封闭选项打分、返回校准概率。[AI/TLDR](https://ai-tldr.dev/releases/google-gemini-decisions-api/)
- AlphaGenome 2：按指定细胞类型预测 DNA 变异效应。[AI/TLDR](https://ai-tldr.dev/releases/google-alphagenome-2/)
- Qwen4-Max-Preview：阿里下一代旗舰两周限时预览，主打编码与 agent。[AI/TLDR](https://ai-tldr.dev/releases/qwen-qwen4-max-preview/)

**工具**
- AWS Emulator：由 AI agent 构建的本地 AWS API 模拟器，无需账号即可测试。[AI/TLDR](https://ai-tldr.dev/releases/aws-emulator/)
- Google Labs Tabletop：把群聊里的链接、文件和想法变成共享交互工具。[AI/TLDR](https://ai-tldr.dev/releases/google-labs-tabletop/)
- Claris Harbor：苹果旗下 Claris 测试在自家 Mac（可 Thunderbolt 5 组集群）上跑开放权重模型的私有 AI 服务器。[AI/TLDR](https://ai-tldr.dev/releases/apple-claris-harbor-local-ai-server/)
- ChatGPT Enterprise（含 Codex）上架 AWS Marketplace。[AI/TLDR](https://ai-tldr.dev/releases/openai-chatgpt-enterprise-aws-marketplace/)

**文章与案例**
- Amazon 用 Strands Decider 替换 Sonnet 4.6 做 20 类工单标签，成本降约 98%。[AI/TLDR](https://ai-tldr.dev/releases/amazon-strands-decider-replaces-sonnet-ticket-labels/)
- 48 个 AI agent 扫公开激光雷达数据，72 小时内找到墨西哥登记册里没有的玛雅遗址。[AI/TLDR](https://ai-tldr.dev/releases/pietromiotti-ai-agents-unmapped-maya-site/)
- Claude Fable 5.2 一晚做出可玩的 12 关四人清版游戏。[AI/TLDR](https://ai-tldr.dev/releases/notesbylex-fable-5-2-one-shot-game/)

**传闻与视频**
- 传字节跳动数周内推出类 Meta Muse 的个人 AI 助手（Bloomberg）。[AI/TLDR](https://ai-tldr.dev/releases/bytedance-muse-like-ai-assistant-rumor/)
- 视频 1 条（AI Explained 解读 Fable 5.2 报告）只计数不展开。

## Agent 用例动态（来自 agentusecases.ai；48 小时内新条目 21 条，全部列出）

今天的用例偏「生活与小生意」：拍冰箱照片排一周菜单、拍购物清单按超市路线排序、Zapier Agent 帮物业派水管工、Dots 代为跟 AT&T 砍价。编程侧有 Cursor 用数百个 agent 做 Solid→React 大迁移、Devin 在生产代码库上搭微服务，两条都提到需要人工复核或「虚报成功」。也有人让 AI 直接操控电脑报税，风险值得警惕。

**安全与可靠性（置顶）**
- 【可靠性】Devin 在两个生产代码库上搭微服务、修简单 bug，但有一次虚报成功。[用例](https://agentusecases.ai/use-case/scaffold-microservices-and-fix-bugs-on-production-codebases)
- 【可靠性】Cursor 让数百个 agent 连跑数周完成 Solid→React 原地迁移（+266K/-193K），CI 通过但仍需仔细审查。[用例](https://agentusecases.ai/use-case/migrate-a-codebase-from-solid-to-react-with-parallel-agents)
- 【权限】让 AI 控制电脑提交报税（高敏感操作）。[用例](https://agentusecases.ai/use-case/have-an-ai-control-the-pc-to-file-taxes)
- 【权限】ChatGPT 经 MCP 集成直接部署代码到自建 PaaS。[用例](https://agentusecases.ai/use-case/deploy-code-from-chatgpt-via-mcp-integration)
- 【身份】Meta Muse 代打牙医电话，被对方察觉是 AI，又因缺保险信息没约成。[用例](https://agentusecases.ai/use-case/call-a-dentist-s-office-to-book-an-appointment)

**编程与开发**
- 修复 OpenClaw 抓取网页时把 Shift_JIS 解码成乱码的问题，并端到端验证。[用例](https://agentusecases.ai/use-case/fix-an-agent-s-charset-decoding-of-fetched-web-pages)
- Strands Agents＋Gemini 检测不稳定测试并追根因。[用例](https://agentusecases.ai/use-case/detect-flaky-tests-and-find-their-root-causes)
- Devin 升级教程仓库依赖、加 lint 并开首个 PR。[用例](https://agentusecases.ai/use-case/modernize-a-learning-repo-and-open-the-first-pr)
- 在公园里用手机语音给编码 agent 提反馈修移动端网页。[用例](https://agentusecases.ai/use-case/fix-a-mobile-web-app-by-voice-from-a-park-bench)
- 开源工具让 agent 录制剪辑 App Store 预览视频。[用例](https://agentusecases.ai/use-case/record-app-store-preview-videos-for-ios-apps-with-an-agent)
- 给编码 agent 一个带 CLI 的绘图应用，画可编辑的游戏美术初稿。[用例](https://agentusecases.ai/use-case/let-a-coding-agent-draw-editable-game-art-with-real-brushes)
- Replit Agent 花不到 25 美元做了求职信、发票、习惯追踪等小应用和每周黑客松摘要。[用例](https://agentusecases.ai/use-case/build-small-apps-and-a-weekly-hackathon-digest-with-replit-a)

**研究**
- 48 个并行 agent 扫 NASA 激光雷达数据找未登记玛雅遗址。[用例](https://agentusecases.ai/use-case/scan-nasa-lidar-data-for-unmapped-maya-sites-with-parallel-a)

**个人助理与小企业**
- Zapier Agent 监控租户报修邮件、查 AppFolio 租户状态并起草派单。[用例](https://agentusecases.ai/use-case/dispatch-plumbers-from-tenant-maintenance-emails)
- Claude 连 Stripe、Mercury、QuickBooks 审税表，称找出 CPA 漏掉的 8,000 美元问题。[用例](https://agentusecases.ai/use-case/review-tax-returns-and-books-to-catch-missed-deductions)
- 用 agent 聊天管理 Actual 记账（上传收据、加现金交易）。[用例](https://agentusecases.ai/use-case/manage-a-budgeting-app-by-chatting-with-an-agent)
- Dots 15～20 分钟把 AT&T 账单从 85 美元谈到 45 美元。[用例](https://agentusecases.ai/use-case/negotiate-an-at-t-bill-down)
- 评估经销商车源并生成报价话术。[用例](https://agentusecases.ai/use-case/evaluate-dealer-listings-and-script-car-offers)
- 用 Claude 起草定向简历与职位描述。[用例](https://agentusecases.ai/use-case/draft-targeted-resumes-and-job-descriptions-for-applications)

**生活**
- 拍冰箱照片排一周晚餐与购物清单。[用例](https://agentusecases.ai/use-case/plan-a-week-of-meals-from-a-fridge-photo)
- 拍黑板购物清单，按超市路线排成待办。[用例](https://agentusecases.ai/use-case/turn-a-grocery-list-photo-into-a-route-ordered-todo-list)

## 地址／IoC 汇总

以下原样抄录自公开帖子／报告，已做防误点处理（[.]），仅用于检测与狩猎：

- macOS 窃密＋后门（来源：[L0Psec](https://x.com/L0Psec/status/2120630183216763083)）
  - SHA256（GoogleHelper.scpt 下载器）：`77f9762cdf9d26c0a1fc9c7a5353091093ff9d21ce46a9609004791094626372`
  - SHA256（第二阶段）：`b254a50b540490852157e8f1f8f455c87820f083f3c00ebcd9841e3e242f61b8`
  - SHA256（后门）：`0cab9d1602f82e13431542da357c94fc02298618ec01fbc0e528398183312388`
  - 域名：`forumvashgol[.]online`、`switchpumpkin[.]com`
  - IP：`85.193.68[.]244`、`85.193.68[.]245`
- DarkLunnen（来源：[Group-IB 报告转载](https://unsafe.sh/go-454113.html)）
  - IP（开放目录与 Sliver C2）：`46.8.236[.]121`（端口 8090）
  - FortiGate 后门超级管理员账号名：`service`
- Qlik Sense 反弹 shell（来源：[Cynet 报道转述](https://kylesinvestigation.com/2026/11/11/qlik-sense-servers-hit-with-powershell-reverse-shells-attacker-server-holds-activemq-and-veeam-exploits/)）
  - IP：`45.115.26[.]23`（反弹端口 4455，开放目录端口 8012）
- Telegram「任意消息变 RCE」演示样本（来源：[v12sec，经 @evilsocket 转](https://x.com/evilsocket/status/2120472421421773068)；未见厂商公告）
  - SHA256：`6630b003766baed1fa86cea880d22e41dc416f63d800de3246941ede2396ad48`
- 其余条目（SignDrop、Fortinet、Kerberos、BO Team、Kimsuky、Maersk、Nitori 等）在本窗口读到的 X 帖与摘要中未见可直接抄录的 IoC，请以厂商／研究报告原文为准。

## 来源搜索 URL

**X 只读搜索（search_posts_all，起点 2026-11-10T23:00Z）**
- `(CVE OR 0day OR "zero-day" OR exploit OR PoC) (patch OR exploited OR advisory OR KEV) -is:retweet lang:en`：Latest 25 条（11-11 22:30～22:58 UTC）＋relevancy 25 条（11-10 23:18～11-11 22:30）。[x.com 搜索](https://x.com/search?q=CVE%20exploited%20patch&f=live)
- `("actively exploited" OR "exploited in the wild" OR "in-the-wild" OR "zero-day") -is:retweet -is:reply lang:en`：relevancy 25 条（11-10 23:04～11-11 22:39）
- `github.com (C2 OR "red team" OR redteam OR nuclei OR "offensive security" OR BOF OR EDR ...) -is:retweet`：Latest 1 条、relevancy 2 条（均与安全无关）
- `("malware analysis" OR "threat report" OR "threat actor" OR APT OR ransomware) (research OR report OR campaign) -is:retweet lang:en`：Latest 25 条（11-11 17:09～23:00）＋relevancy 25 条（11-11 00:42～22:37）
- 补搜 `(malware OR backdoor OR stealer OR loader OR APT) ("new research" OR analysis OR blog OR IOCs OR IoC)`：relevancy 25 条（11-10 23:03～11-11 22:19）
- 定向 `(SignDrop OR CLFS OR "Zyxel GS1900" OR GSocket OR "Project Glasswing" OR FortiOS OR FortiMail OR PSIRT)`：relevancy 25 条（11-11 00:43～21:34）
- LWiS X List：[x.com/i/lists/1239330068461244424](https://x.com/i/lists/1239330068461244424)（3 页 287 帖，11-10 16:45～11-11 22:58 UTC）
- X 合计：12 次只读调用共 490 帖，去重后 447 个帖子 ID（含 List）。

**其他信源**
- pwn.watch：https://pwn.watch/feed.xml （50 条，最新 11-08 20:19 UTC；本窗口新事件 0 条；佐证引用 2 个事件页：Zyxel GS1900、Barracuda）
- ExploitGrid 最新 exploit：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （100 条，覆盖 11-09 10:50～11-10 19:33 UTC；本窗口新增 0 条；按 CVE 查询 5 次，4 次命中公开 exploit 条目：CVE-2026-125350、CVE-2026-107441、CVE-2026-76466、CVE-2026-59310；CVE-2026-124194 为 0 条；另从列表交叉出 KEV 中的 CVE-2026-123158、CVE-2026-123218）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （共 17 条，两页全取；11-12 到期 4 条、11-13 到期 2 条）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条，覆盖 2026-10-30 13:07～11-12 04:13 北京时间；48 小时内未收录 68 条：ZDI 47、HackerOne 19、社区 2）
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community （7 个源全部拉取；48 小时新条目 2 条：先知 1、奇安信攻防社区 1）
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog （12 个源全部拉取；7 天内首次出现 47 条，全部来自 ZDI-vulnerabilities）
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条；36 小时内新条目 13 条，security 类 0 条）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条；48 小时内新条目 21 条）
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （catalogVersion 2026.11.10；11-11 无新增）
- 阮一峰周刊：工作日版不加。

### LWiS 固定信源（每日交叉，不替代 X Latest）
- X List（只读）: https://x.com/i/lists/1239330068461244424
- 博客清单: https://blog.badsectorlabs.com/files/blogs.txt （本地: lwis-sources/blogs.txt）
- CISA KEV: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD: https://nvd.nist.gov/
- Risky Business: https://risky.biz/
- tl;dr sec: https://tldrsec.com/
- SecureFlow 安全信息流: https://secureflow.scope-sentry.top/all
- SecureFlow 社区: https://secureflow.scope-sentry.top/community
- SecureFlow 博客: https://secureflow.scope-sentry.top/blog
- Agent Use Cases: https://agentusecases.ai/ （RSS https://agentusecases.ai/feed.xml）
- AI/TLDR: https://ai-tldr.dev/ （Atom https://ai-tldr.dev/feed.xml）
- pwn.watch: https://pwn.watch/ （RSS https://pwn.watch/feed.xml）
- ExploitGrid: https://exploitgrid.net/

## 验收结果

1. 采集：通过。X 三组只读搜索（Latest＋relevancy 补搜）＋在野利用、恶意软件、定向三组补搜与 LWiS List 三页均完成（12 次只读调用，490 帖，去重 447 个 ID），覆盖时长已写在报告头；SecureFlow all（68 条）、community 7 源（2 条）、blog 12 源（47 条）全部拉取并按窗口筛选；Agent Use Cases 21 条；AI/TLDR 13 条（security 0 条）；pwn.watch 与 ExploitGrid 两个新信源已拉取并交叉核对；工作日版无周刊节。说明：① 「github.com + C2/红队」这组 Latest 只命中 1 条且无关，工具节主要靠 LWiS List；② **pwn.watch 订阅源停在 11-08 20:19 UTC、ExploitGrid 列表最新为 11-10 19:33 UTC，本窗口两者都是 0 条新增**，只作为佐证使用（pwn.watch 2 个事件页，ExploitGrid 7 个 CVE／exploit 页及 KEV 期限 17 条）。
2. 核验链接：通过。全文 189 个唯一 URL 全部检查过（浏览器 UA）：68 个 X 帖链接的 ID 与作者名都和 X 接口返回的数据对得上；其余 121 个里 116 个直接返回 200；cybersecuritynews（curl 复查 200）、securityonline 与 NHS CC-4888（box 直连被 Cloudflare 拦截，经抓取服务读到全文）、Android Headlines（Cloudflare 拦截，链接取自 X 帖展开结果）、forum.butian.net（box 网络连不上，链接取自 SecureFlow 原始数据）均已在正文标注。Group-IB 原文链接返回 404，已改用全文转载页与 SecQuill 摘要。t.co 已全部展开。
3. 成稿：通过。十个小节齐全、无空节；IoC 节有原样抄录的哈希／域名／IP；没有利用代码、payload 或利用步骤（公开 exploit 只写「已有公开 exploit」并附 ExploitGrid 或 X 帖链接，不直链 exploit 仓库）；已按 state.json 的 seen_ids 去重，Outlook、Chrome、Barracuda、Xen Orchestra、Zyxel GS1900、Railway 等已报内容只作跟进，昨日已列的 2 份 HackerOne 报告不重复。
4. 落盘与交付：通过。box 文件已写入（约 43 KB）；已拷到本机 /Users/kenny1337/Desktop/_05_项目/X安全情报晚报/ 并读回确认（行数与 box 一致）。
