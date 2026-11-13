# X 安全情报晚报 · 2026-11-12（周四）

> 报告时间：2026-11-12 约 20:10（America/Santiago）＝ 2026-11-13 约 07:10（香港时间）。
> **覆盖时长**：X 只读搜索窗口 2026-11-11 23:00 UTC～11-12 22:59 UTC（24 小时）。CVE 组 Latest 一页 25 条只覆盖 11-12 22:23～22:58 UTC（约 35 分钟），所以用 relevancy 补搜（25 条，覆盖 11-12 01:30～22:54），另补「在野利用」组 25 条（11-11 23:28～11-12 18:48）和定向组 25 条（11-11 23:04～11-12 21:09）。工具组（github.com + C2/红队等）Latest 和 relevancy 都只有 4 条，且与安全无关，所以工具节主要靠 LWiS List。威胁报告组 Latest 25 条（11-12 18:25～22:46）＋relevancy 25 条（11-12 00:00～22:46）＋恶意软件补搜 25 条（11-11 23:04～11-12 19:19）。LWiS X List 翻两页共 197 帖，覆盖 11-11 22:58～11-12 22:55 UTC（整 24 小时）。SecureFlow 取近 48 小时（blog 放宽到 7 天）；AI/TLDR 取 36 小时；Agent Use Cases 取 48 小时。
> **新信源说明**：pwn.watch 订阅源最后生成于 2026-11-08 20:19 UTC，本窗口内 **0 条新事件**，只把 2 个已有事件页（SonicWall、FreeSWITCH）当佐证。ExploitGrid 最新 exploit 列表最新一条是 11-11 20:12 UTC，本窗口（11-11 23:00 起）**0 条新增**；但上期截止后（11-10 19:33～11-11 20:12）新收录了 50 多条，其中 Outlook、FortiClient、MongoDB 等已并入下文，并按 CVE 做了 8 次查询交叉核对。
> **CISA KEV**：目录版本仍是 2026.11.10，11-11、11-12 都没有新增。**11-13（香港时间今天）是 Barracuda 两条和 Ivanti Connect Secure CVE-2026-118527 的联邦修补期限**；SonicWall CVE-2026-19868 期限为 11-20。
> 本期为工作日版（十个小节），不加阮一峰周刊节；已检查 11-07（周六）那期，已收录周刊第 418 期，不需要补。

## 今日摘要

- **Apache httpd mod_http2 严重 RCE CVE-2026-119618**：11-11 发布 2.4.71 修复，影响 2.4.55～2.4.70（仅启用 HTTP/2 的服务器），未认证即可触发堆破坏。由 Anthropic OSS Scanner 和 Google 云漏洞研究团队分别独立发现。Wiz 称 64% 的云环境有受影响资源；GitHub 已出现可复现崩溃的代码，但还没有确认在野利用。
- **N-able N-central 新 0day「4EverAble2Shell」已被在野利用**：PoC 公开后约 5 小时就被利用，至少 21 台生产服务器被装上 XMRig，其中 19 台已打了 11-10 的 HF2。先关闭 Legacy API，并把服务器从公网撤下。
- **ScreenConnect「SCKit」蠕虫式攻击 MSP**：滥用第三方扩展 RMM+ 的空白默认访问密钥，向 48 个组织的 288 台终端推送恶意 ScreenConnect 客户端；ConnectWise 已禁用 5 个第三方扩展。
- **Xen Orchestra VSA-2026-062 跟进**：已被利用，并与 VSA-2026-063（低权限导入恶意 VM，尚无修复）串联使用。PostgreSQL 修复了一个 22 年前就存在的类型混淆 RCE CVE-2026-6460；FortiClient CVE-2026-121529 在 ExploitGrid 上出现 4 条公开 exploit 收录。
- **执法与 APT**：Europol「Operation Endgame」新一轮行动打掉 Gootloader、CastleRAT、StealC，查获 235 台服务器和 257 个域名，追回 640 万条受害数据；Check Point 披露 CopperDragon（Sparrow 框架的供货方）支持多个中国关联间谍团伙；CloudSEK 发现 Silent Lynx 暴露的服务器里有 AI agent 作战痕迹；4,837 个被盗 GitHub 账号向 1,806+ 个仓库植入 CI 密钥窃取器。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

**1. Apache HTTP Server mod_http2 堆破坏／RCE CVE-2026-119618（严重，2.4.71 已修复）**
- 谁／什么：mod_http2 的 assign_headers() 存在并发竞争，多线程写共享内存时没有正确加锁，导致堆破坏，可能进一步实现 RCE，不需要认证。影响 2.4.55～2.4.70，以及独立 mod_h2 2.0.8～2.0.42；Red Hat 评分 9.8。同版本还修复了 mod_md 崩溃（important）和 mod_vhost_alias 单字节栈覆写（low）。
- 利用状态：Red Hat 称「公开研究已展示可靠利用」，但没有给出出处；Wiz、Nomios 称尚无可用 exploit、没有在野利用，GitHub 上的公开代码只能让子进程崩溃。ExploitGrid 按 CVE 查询为 0 条；不在 KEV。
- 处置：升级 2.4.71 或发行版修复包（RHEL 9 RHSA-2026:98981、Debian sid 2.4.71-1 等），升级后要完整重启而不是 graceful reload；暂时无法升级的，在每个虚拟主机的 Protocols 中去掉 h2/h2c。前面有 CDN/LB 终结 HTTP/2 的，也要检查回源是否走 h2c。
- X 原帖：[JurajCekan](https://x.com/JurajCekan/status/2121009632454103139) · [NetSPI](https://x.com/NetSPI/status/2121014117867639181) · [SANS ISC Stormcast](https://x.com/sans_isc/status/2120698304568967603) · [EnclaveRadar（声称有公开 exploit，存在争议）](https://x.com/EnclaveRadar/status/2120673128846086355)
- 厂商公告：[Apache httpd 2.4 漏洞页](https://httpd.apache.org/security/vulnerabilities_24.html)
- 文章：[Wiz](https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability) · [The Hacker News](https://thehackernews.com/2026/11/critical-apache-http2-flaw-could-let.html) · [Nomios（暴露面判断）](https://www.nomios.co.uk/news-blog/nomios-threat-intelligence-update-apache-http-2-flaw/)

**2. N-able N-central「4EverAble2Shell」0day 已被在野利用（HF2 不能防住）**
- 谁／什么：研究者 Sean Bales 在 11-12 公开 4EverAble2Shell（Apache Axis CVE-2026-90436 加上本地提权，未认证拿 root，前提是启用 Legacy API）和 Agent2Shell（10 多个 0day 组合，在受管 Windows agent 上拿 SYSTEM，需要知道 appliance ID）。Huntback 观测到 PoC 发布约 5 小时后开始利用，至少 21 台生产服务器被装 XMRig，其中 19 台运行 11-10 的 2026.4 HF2（build 2026.4.1.26）。
- ExploitGrid：CVE-2026-90436 **已有公开 exploit**（[ExploitGrid 页面](https://exploitgrid.net/exploits/EGE-GH-9UoEns8)）。
- 处置：立即关闭 Legacy API，服务器不要暴露公网；从 11-11 起排查异常；确认被入侵的按完全失陷处理（这台服务器管理着客户终端）。持续关注 N-able 后续 hotfix。
- X 原帖：[DFIR_Radar](https://x.com/DFIR_Radar/status/2120970397193564225) · [SANS ISC（N-central HF2）](https://x.com/sans_isc/status/2120698304568967603)
- 厂商公告：[N-able：HF2 与后续安全响应](https://www.n-able.com/blog/update-on-n-central-2026-4-hf2-and-ongoing-security-response)
- 文章：[BleepingComputer](https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/) · [Huntback（含主机／网络 IoC）](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers) · [The Hacker News](https://thehackernews.com/2026/11/new-n-central-exploits-work-against.html)

**3. ConnectWise ScreenConnect「SCKit」攻击 MSP（第三方扩展 RMM+ 认证绕过）**
- 谁／什么：11-11 17:47 UTC 起，攻击者借云托管 ScreenConnect 面板的 Run Command，在 48 个组织的至少 288 台终端上安装恶意 ScreenConnect 客户端和 SCKit（持久化，并可中继技术员会话 cookie）。Huntress 把入口归因于 RMM+ 扩展 1.0.31/1.0.32 的空白默认访问密钥；ConnectWise 称不是 ScreenConnect 本身的漏洞，已在约 400 个装有相关扩展的伙伴环境中禁用 5 个第三方扩展。
- 处置：禁用 RMM+ 等第三方扩展；隔离受影响主机，排查时用带外工具，不要用 ScreenConnect 本身；检查是否有多出来的 ScreenConnect 客户端实例，并轮换技术员会话。
- X 原帖：[TheHackersNews](https://x.com/TheHackersNews/status/2120738768806404225) · [0x534c](https://x.com/0x534c/status/2120769820652441825) · [Dinosn 转 SecurityWeek](https://x.com/Dinosn/status/2120833742847762572) · [infrastack_ai](https://x.com/infrastack_ai/status/2120659872878670169)
- 厂商公告：[ConnectWise 伙伴指引](https://www.connectwise.com/blog/screenconnect-security-update-guidance-for-partners)
- 文章：[Huntress](https://www.huntress.com/blog/sckit-worm-rogue-screenconnect)（box 直连 403，经抓取服务读到全文，含 SCKit 各组件哈希）· [The Hacker News](https://thehackernews.com/2026/11/screenconnect-attacks-target-at-least.html) · [SecurityWeek](https://www.securityweek.com/hackers-deploy-malware-in-fresh-screenconnect-campaign/)

**4. Xen Orchestra VSA-2026-062 在野利用跟进（无 CVE，所以不进 KEV）**
- 新进展：Vates 另发 VSA-2026-063，说明攻击者把认证绕过与「低权限用户通过特制参数导入恶意 XVA 虚拟机」串联，可接管 XCP-ng 主机；063 截至目前**尚无修复**。认证绕过本身已在 Xen Orchestra 6.9.2（stable）/6.10.1（latest）修复（xo-server 5.211.2/5.213.1）。
- 处置：升级；XO 管理界面不要暴露公网；按 Vates 公告在代理日志中匹配特征 cookie，并检查名为 pivot2 的 VM、使用「hvm_serial: file」的 VM、/etc/cron.d/zz-ustar* 等文件；确认被入侵的建议重装。
- X 原帖：[V0iD_0daY](https://x.com/V0iD_0daY/status/2120896788366250475) · [pwnsydotcom](https://x.com/pwnsydotcom/status/2120767785580277801)
- 厂商公告：[Vates VSA-2026-062](https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-062/)
- 文章：[The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-critical-xen-orchestra.html) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-xen-orchestra-auth-bypass-flaw-exploited-to-hijack-vm-servers/)

**5. Outlook 在野 0day CVE-2026-124194 跟进（KEV，期限 11-24）**
- 新进展：ExploitGrid 在 11-11 收录了 2 个相关仓库，**已有公开 exploit**（上期查询时为 0 条）：[ExploitGrid CVE 页](https://exploitgrid.net/vulnerabilities/CVE-2026-124194)。X 上对成因的技术细节讨论增多：特制消息文件内嵌 UNC 路径，打开后 Outlook 不弹外部内容警告，直接连接攻击者的 SMB 服务器并泄露 NTLMv2 哈希。修复走的是 Office 更新，不是 Windows Update。
- 另外，11-12 Microsoft 365（Outlook、Teams 等）大面积故障，X 上有人把它和这个 0day 联系起来；微软的解释是服务器健康检查失败导致容量下降，**没有证据表明两者有关**。
- 处置：装 Office/M365 11 月更新；边界封出站 TCP 445；把高权限账号加入 Protected Users 组。
- X 原帖：[0xManan（技术细节，41 赞）](https://x.com/0xManan/status/2120782557075984747) · [okaibedi](https://x.com/okaibedi/status/2121014870145417272) · [Lumideezy（81 赞）](https://x.com/Lumideezy/status/2120891258692657182)
- 文章：[BBC：Microsoft 365 故障](https://www.bbc.com/news/articles/c5gm3g9ldz8xo)

**6. FortiClient 本地 API 来源校验缺陷 CVE-2026-121529（FG-IR-26-194，CVSS 9.1，需用户交互）**
- 谁／什么：FortiClient Windows/Mac/Windows PAM 的本地 API 端点没有正确校验请求来源，未认证的远程攻击者在受害者配合交互后可执行代码或命令。影响 7.4.0～7.4.7、Windows/PAM 7.2.0～7.2.14；8.0 和 Mac 7.2 不受影响。厂商标注未被利用、不在 KEV。
- ExploitGrid：11-11 一天就收录了 4 个仓库，**已有公开 exploit**（[ExploitGrid 页面](https://exploitgrid.net/exploits/EGE-GH-86BgMrn)）；同批还有 FortiManager CVE-2026-126170 的公开 exploit 收录（[ExploitGrid 页面](https://exploitgrid.net/exploits/EGE-GH-LKN5edF)，上期报道的 11 月 PSIRT 批次之一）。
- 处置：用 EMS/RMM 盘点版本，升级到 7.4.8+ 或 7.2.15+；没有临时缓解办法。
- 厂商公告：[FortiGuard FG-IR-26-194](https://fortiguard.fortinet.com/psirt/FG-IR-26-194)
- 文章：[Cybaverse 分析](https://www.cybaverse.co.uk/threats/fortinet-forticlient-cve-2026-121529)

**7. PostgreSQL 22 年前就存在的类型混淆 RCE CVE-2026-6460（11-12 已修复）**
- 谁／什么：Mehmet Ince（mdisec）发现，利用预编译语句准备好以后、再用 ALTER ... SET DATA TYPE 修改复合类型属性，导致数据类型陈旧、内存破坏并可执行代码；需要能执行 SQL 的数据库账号。修复版本 18.7/17.12/16.16/15.20/14.25。这是 mdisec 关于托管 PostgreSQL 风险的六篇系列文章之一。ExploitGrid 按 CVE 查询为 0 条。
- 处置：尽快升级小版本；托管数据库关注云厂商的更新节奏；收紧应用账号的 DDL 权限。
- X 原帖：[kmkz_security 转 mdisec](https://x.com/kmkz_security/status/2120940794676658411)
- 厂商公告：[PostgreSQL CVE-2026-6460](https://www.postgresql.org/support/security/CVE-2026-6460/)
- 文章：[mdisec 分析第 3/6 篇](https://mehmetince.net/part-3-6-how-i-ended-up-turning-a-22-year-old-postgresql-type-confusion-primitive-into-rce-cve-2026-6460/)

**8. MongoDB 预认证 UAF CVE-2026-118383（CVSS 4.0 9.5）／Zoom Workplace 严重提权**
- MongoDB：未认证发送两个请求即可让副本集成员在之后被选为主节点时崩溃（前提是它数据落后）；开启认证也挡不住，单机 mongod 不受影响。厂商自查发现、未被利用；Datadog 已复现。ExploitGrid 有 1 条收录（[ExploitGrid 页面](https://exploitgrid.net/exploits/EGE-GH-bnUXbNK)）。按各分支修复版本升级。[Dinosn](https://x.com/Dinosn/status/2120833768986689572) · [The Hacker News](https://thehackernews.com/2026/11/critical-pre-auth-mongodb-flaw-cve-2026.html)
- Zoom Workplace for Windows：CVE-2026-108187（7.1.5 之前，严重）与 CVE-2026-108186（7.1.0～7.1.8 之前），远程未认证提权，未被利用。升级到 7.1.8+。[Dinosn](https://x.com/Dinosn/status/2120833839656505356) · [The Hacker News](https://thehackernews.com/2026/11/critical-zoom-workplace-flaw-could.html)

**9. KEV 期限提醒（CISA KEV＋ExploitGrid KEV 期限接口交叉核对）**
- **11-13 到期（香港时间今天）**：Barracuda CVE-2026-116606／CVE-2026-111560（串联可未认证拿 root）、Ivanti Connect Secure CVE-2026-118527（可预测标识符）。**11-20**：SonicWall SonicOS SSLVPN CVE-2026-19868（走其他认证方式即可绕过 SAML 和 MFA），ExploitGrid 已收录 2 条（扫描器等），**已有公开 exploit**（[ExploitGrid CVE 页](https://exploitgrid.net/vulnerabilities/CVE-2026-19868)），pwn.watch 状态 patched（[事件页](https://pwn.watch/i/sonicwall-sonicos-sslvpn-saml-bypass-cve-2026-19868)）。**11-24**：Outlook、Chrome、Cisco BroadWorks、Openwave 四条。
- 11-12 到期的 FreeSWITCH CVE-2026-116779 在 X 上继续有人提醒（修复版 1.11.3，[pwn.watch](https://pwn.watch/i/freeswitch-api-chat-rce-cve-2026-116779)）；GPUStack CVE-2026-102895 在野利用的报道继续传播。
- Ivanti 另有 EPM 严重 SQL 注入 CVE-2026-121653（未认证 RCE，2024 SU8 修复，未被利用）：[NHS England Digital CC-4890](https://digital.nhs.uk/cyber-alerts/2026/cc-4890)（box 直连 403，经抓取服务读到全文）· [SecurityWeek](https://www.securityweek.com/citrix-ivanti-patch-critical-and-high-severity-vulnerabilities/)
- X 原帖：[FarVisionNetwks（Barracuda 明天到期）](https://x.com/FarVisionNetwks/status/2121009521716072648) · [D0xedDevi0（SonicWall）](https://x.com/D0xedDevi0/status/2120661382744158232) · [ksg93rd（FreeSWITCH）](https://x.com/ksg93rd/status/2120873181997068451) · [undercode_news（GPUStack）](https://x.com/undercode_news/status/2120859752062161403)
- 来源：[ExploitGrid KEV 期限 API](https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines) · [CISA KEV 目录](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

**10. 其他值得关注**
- Windows CLFS「SignDrop」跟进：THN 报道代码已公开，仍无 CVE、无补丁（257 赞）。[TheHackersNews](https://x.com/TheHackersNews/status/2120938288148316633)
- Google Cloud 提醒 AMD Turin（Zen 5）三个 TSA 侧信道（含新的 CVE-2026-0004「TSA-Fill」），C4D/N4D/H4D/Z4D/G4 系列需打客户机 OS 补丁并停机再启动。[Dinosn](https://x.com/Dinosn/status/2120923248649183542) · [The Hacker News](https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html)
- Synology DSM 严重漏洞 CVE-2026-76954（Synology_SA_26_19，升级 DSM 7.4.1-90080-1／7.3.2-86009-5 等）。[kiddo_pwn 转研究者](https://x.com/kiddo_pwn/status/2120744422564667711) · [Synology 公告](https://www.synology.com/en-global/security/advisory/Synology_SA_26_19)
- Project Zero 公开 Windows .NET PEImageLayout::Map 安全功能绕过。[ProjectZeroBugs](https://x.com/ProjectZeroBugs/status/2120863935549337690) · [问题页](https://project-zero.issues.chromium.org/issues/569822336)
- Chrome 修 83 个、Firefox 修 99 个、Thunderbird 160 修 103 个漏洞，厂商未说明是否在野利用。[TweetThreatNews](https://x.com/TweetThreatNews/status/2120951802900124092)
- Windows 本地管理员到 SYSTEM（通过 HTTP.sys 捕获 NTLM token）**已有公开 PoC**，见 [ipurple 帖](https://x.com/ipurple/status/2120808723606020421)（87 赞，未见厂商回应）。

## 工具与 GitHub 发布（每条：说明 + 地址列表）

**1. 检测／防守向**
- MaldocTrace：不执行宏、靠模拟来分析恶意 Office 宏。[文章](https://debugactiveprocess.medium.com/maldoctrace-emulating-malicious-office-macros-without-running-them-fcd98245a087)（Medium 对 box 返回 403，经抓取服务读到全文；Apache-2.0 单文件 Go 工具）（[@ipurple](https://x.com/ipurple/status/2120848771408179315)）
- LuLu（Objective-See 免费开源 macOS 防火墙）新版本：新功能、界面刷新。（[@patrickwardle](https://x.com/patrickwardle/status/2120881789497483771)，159 赞）
- Threatray v2.3：给 AI 逆向加上已知恶意代码／无害代码上下文。（[@threatray](https://x.com/threatray/status/2120898495720665361)）
- Microsoft FORGE Lab「MDASH」用 AI 扫 Linux 内核：26,502 条原始发现，最终 59 份上游报告、33 个 CVE、8 个可提权到 root。[微软安全博客](https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/)（[@_wmliang_ 转](https://x.com/_wmliang_/status/2120745723222229373)）
- KRBTGT 账号重置时内部到底发生了什么（AD 运维必读）。[文章](https://jorgequestforknowledge.wordpress.com/2026/11/12/what-happens-under-the-hood-when-resetting-the-password-of-a-krbtgt-account/)（[@DirectoryRanger](https://x.com/DirectoryRanger/status/2121011640799813742)）

**2. 红队／测试工具（防守方据此补检测）**
- NetExec 新增 --klist／--klist-dump：用微软签名的 klist.exe 导出 Kerberos TGT。防守方应关注 klist 的异常调用（239 赞）。（[@Defte_](https://x.com/Defte_/status/2120890870887047436) · [@stuk0v_ 转作者](https://x.com/stuk0v_/status/2120897775244111975)）
- NetExec-mcp v1.0.9：可通过 pipx 安装的 NetExec MCP 服务。[GitHub Release](https://github.com/mpgn/NetExec-mcp/releases/tag/v1.0.9)（[@maxime_tz 转](https://x.com/maxime_tz/status/2120990819477754213)）
- s1l3nc3r：利用 Linux 版 MDE 暴露的 BPF map 让指定系统调用不产生遥测。使用 MDE for Linux 的团队应监控对该 BPF map 的写入。[GitHub](https://github.com/unicornofhunt/s1l3nc3r)（[@ipurple](https://x.com/ipurple/status/2120922384374902959)）
- BBOT 3.1：DNS 全部改走 BlastDNS，子域名枚举快约 40%。[发布说明](https://blog.blacklanternsecurity.com/p/4e60982f-ced1-4c72-9754-91499995fb4d)（[@BlackLanternLLC](https://x.com/BlackLanternLLC/status/2120906986825134454)）
- Doyensec ProtoSpector：用于测试 Protobuf/gRPC 流量的 Burp 扩展（[@garethheyes 转](https://x.com/garethheyes/status/2120981549713879485)）；Frag 新增盲注模式（[@garethheyes](https://x.com/garethheyes/status/2120956053630443705)）。
- idasql 0.0.20 支持 IDA 9.5，可让 agent 同时操作多个打开的 IDA 实例（[@Steph3nSims 转](https://x.com/Steph3nSims/status/2120774144891768916)）；Hex-Rays 博客介绍 0xdea 的漏洞研究工具 rhabdomancer/haruspex/augur（[@0xdea 转](https://x.com/0xdea/status/2120992376751530013)）。
- OpenAI Codex Security 0.10.0（开源漏洞扫描器）：支持断点续扫、成本上限。[AI/TLDR](https://ai-tldr.dev/releases/openai-codex-security-0-10-0/)

## APT / Malware 分析（每条：说明 + 地址列表）

**1. CopperDragon：给多个中国关联间谍团伙提供 Sparrow 框架的「数字军需官」（Check Point）**
- 一年期调查，把 SilentDelivery（欧亚水坑攻击，用伪装成证书修复工具的 MSI 投放 SquadC）、OceanGate（亚洲，先打 Linux 边界再横向到 Windows，SparrowDoor/SparrowShell，与 Melofee 有关联）、DarkWire（拉美电信／政府，CopperDoor/CopperDNS）三个集群关联起来，涉及 21 个国家；FamousSparrow、Earth Estries、TropicTrooper、UAT-9244 等都在使用。
- [Check Point Research 报告](https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/) · [@nextronresearch](https://x.com/nextronresearch/status/2120806656229458099) · [@cyb3rops（9 月已共享 CopperLoader 样本）](https://x.com/cyb3rops/status/2120814365486297138)

**2. Operation Endgame 新一轮：Gootloader、CastleRAT、StealC 基础设施被端（Europol，11-12）**
- 9 国参与，查获 235 台服务器、257 个域名（Gootloader 14 台服务器／218 个域名、CastleRAT 120 台／39 个、StealC 102 台），追回 640 万条受害者凭据数据集。
- [Europol 通报](https://www.europol.europa.eu/media-press/newsroom/news/64-million-victim-datasets-secured-in-international-operation-against-malware-networks) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/police-dismantles-gootloader-castlerat-stealc-malware-infrastructure/) · [@Dinosn](https://x.com/Dinosn/status/2120922737409749145) · [@_pksharma（核对服务器数）](https://x.com/_pksharma/status/2120950559167422635)

**3. 4,837 个被盗 GitHub 账号向 1,806+ 个仓库植入 CI 密钥窃取器「wfx」**
- 先用标题为「docs: dependency audit notes」、分支名为 wfx-docs 的 PR 测试写权限（共 61,764 个仓库收到），再把窃取器塞进 workflow 或 npm postinstall 钩子，几分钟后回滚并删掉运行日志。SafeDep 统计有 8,093 个仓库收到恶意提交。
- 处置：搜索组织内有无上述 PR 标题或分支名；窃取器跑过的仓库，所有 Actions 密钥和云角色一律视为泄露，立即轮换。
- [The Hacker News](https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html) · [@Dinosn](https://x.com/Dinosn/status/2120833809910505826) · [@infrastack_ai](https://x.com/infrastack_ai/status/2120772082405609960)

**4. Silent Lynx 服务器暴露：AI agent 参与中亚间谍行动（CloudSEK）**
- 一台无认证暴露的 VPS 上有完整的钓鱼链（伪装成 PDF 的 LNK 加 PowerShell 反弹 shell）、窃取的政府数据，以及一个基于 DeepSeek、负责运营的 AI agent；目标包括塔吉克斯坦铁路和政府网络，操作者疑似哈萨克斯坦背景。
- [CloudSEK](https://www.cloudsek.com/blog/off-the-rails-inside-an-exposed-silent-lynx-server) · [@IdaNotPro](https://x.com/IdaNotPro/status/2120863249352769629) · [@infrastack_ai](https://x.com/infrastack_ai/status/2120893950307553651)

**5. 用 Claude Code agent 攻击 Solana 验证节点与 MEV 机器人服务器窃取私钥**
- 名为 MevBotResearch 的项目定义了两个自定义 agent（侦察、利用），扫描暴露的 ClickHouse、Redis、SSH 服务，提权后窃取私钥并转走钱包余额。
- [@fr0gger_](https://x.com/fr0gger_/status/2120682376078753921)（IoC 见[续帖](https://x.com/fr0gger_/status/2120682378360426757)）· [TLDR 摘要](https://tldr.tech/story/2854db08-cbfd-4ed8-b909-e195545d6043)

**6. Linux 挖矿与持久化**
- Elastic REF3364「SANSAR」：通过暴露的 Ray 作业 agent 进入 3 台 GPU 主机，部署能让 nvidia-smi 显示 0% 占用的挖矿木马；附 YARA 规则和 IoC。[Elastic Security Labs](https://www.elastic.co/security-labs/threat-command/sansar-linux-cryptomining-malware) · [@elasticseclabs](https://x.com/elasticseclabs/status/2120909485711487294)
- 多个团伙滥用开源 GSocket 中继做持久化（双方都向外连接，不需要入站监听），MDE 遥测显示 3～8 月相关检测增长 356%。[BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-plant-gsocket-on-linux-servers-for-persistent-access/) · [@Dinosn](https://x.com/Dinosn/status/2120825535479902606)
- Go 写的扫描器爆破公网 MSSQL，再用 T-SQL 投放 Monero 挖矿程序和 Gh0st RAT 变种（FortiGuard）。[@DFIR_Radar](https://x.com/DFIR_Radar/status/2120910202589331705)

**7. macOS 与终端侧**
- 伪装 MicrosoftTeamsSetup.dmg 诱导用户在脚本编辑器里运行 AppleScript；Moonlock 分析了用 plist 以 headless＋调试参数启动 Chrome 读取文件的手法。[@L0Psec（含哈希）](https://x.com/L0Psec/status/2120903905613902080) · [@L0Psec 转 Moonlock](https://x.com/L0Psec/status/2121000331718910216)
- Blind Eagle（APT-C-36）用 SVG/XHTML 走私、司法主题诱饵投放 AsyncRAT 和 DCRat。[sh3llc0d3 博客](https://sh3llc0d3.com/blog/blind-eagle-apt-c-36-weaponizes-judicial-svg-smuggling-to-deploy-asyncrat-across-latin-america/) · [@sh3ll_c0d3](https://x.com/sh3ll_c0d3/status/2120828202947915872)
- 假 VS Code 安装器（vscode-bootstrap.cmd）滥用 Node.js 投放类 Akira 的 Go 恶意软件（[@joe4security](https://x.com/joe4security/status/2120828707296145426)）；Ky9Agent：.NET 一体化 RAT，可经 LAN/USB 传播，并捆绑改过的 r77 rootkit（[@ThreatrayLabs](https://x.com/ThreatrayLabs/status/2120871740024684884)）；NIKKE 游戏启动器服务端下发的任务通道被用来推送 Lua 窃密程序 k2f-agent（[@DFIR_Radar](https://x.com/DFIR_Radar/status/2120834501890674689)）。

**8. 归因与事件**
- Krebs：Qilin 勒索管理员「Haise」被关联到圣彼得堡一名男子。Qilin 近三个月声称受害者 365 家，是目前最活跃的 RaaS。[KrebsOnSecurity](https://krebsonsecurity.com/2026/11/who-runs-the-ransomware-group-qilin/) · [@Dinosn](https://x.com/Dinosn/status/2120697963165180087)
- 波兰国家电子政务平台 ePUAP 遭攻击后下线（攻击已阻断）。[Security Affairs](https://securityaffairs.com/202895/security/poland-takes-its-national-e-government-platform-offline-after-a-cyberattack.html) · [@Dinosn](https://x.com/Dinosn/status/2120837058923233597)
- Fireworks AI 10 月两次被入侵，导致不到 1% 的 Notion 工作区聊天记录外泄。[SecurityWeek](https://www.securityweek.com/notion-customer-data-compromised-in-fireworks-ai-hack/) · [@Dinosn](https://x.com/Dinosn/status/2120917449990435228)
- 未经证实的声称：Panzer 勒索团伙称攻陷马来西亚卫生部（无样本）（[@DailyDarkWeb](https://x.com/DailyDarkWeb/status/2120945039496950247)）；有人声称盗取 1.11 亿条 Notion 用户数据（[@MonThreat](https://x.com/MonThreat/status/2120862234884587611)），均以官方说法为准。
- 业界：前微软安全专家 Jessica Payne（@jepayneMSFT）离世，多位业内人士悼念她在 Windows 防火墙和 4624 事件分析方面的贡献。[@bohops 转 HackingDave](https://x.com/bohops/status/2120942565050740842)

## SecureFlow 信息流精选（X 上未出现的高信号条目，按 community／blog／BugBounty 分组）

**community（48 小时新条目 9 条：先知 8、Seebug 1）**
- 先知「CVE-2026-118660：happy-dom 服务端 SSRF 全链路分析」：服务端渲染用 happy-dom 的项目需关注。[xz.aliyun.com/news/93265](https://xz.aliyun.com/news/93265)
- 先知「基于默认配置的 Dify 沙箱 RCE 利用链分析与加固探讨」：自建 Dify 的团队可对照文中加固建议。[xz.aliyun.com/news/93260](https://xz.aliyun.com/news/93260)
- 先知「云上攻防 Azure 容器之 ACR-ACI 攻击链」：[xz.aliyun.com/news/93258](https://xz.aliyun.com/news/93258)
- 先知「Gohttpserver Zip Slip 漏洞：从黑盒复现到白盒审计」：[xz.aliyun.com/news/93262](https://xz.aliyun.com/news/93262)
- 先知「CVE-2026-100229 GStreamer H.266 DCI 越界写复现分析」：[xz.aliyun.com/news/93251](https://xz.aliyun.com/news/93251)
- 先知另有 GPT Academic 软链接任意文件读取（CVE-2025-25185）、跨链桥假充值赏金复盘、对抗样本可迁移性综述：[93253](https://xz.aliyun.com/news/93253) · [93255](https://xz.aliyun.com/news/93255) · [93225](https://xz.aliyun.com/news/93225)
- Seebug Paper「先取证还是先处置？面向信息物理系统时限性事件响应的信念级反事实标签」：[paper.seebug.org/3533](https://paper.seebug.org/3533)（核验时 Seebug 源站返回 521，链接取自 SecureFlow 原始数据）
- 奇安信攻防社区、t00ls、InfoSec Write-ups、Critical Thinking：48 小时窗口内没有未收录的新条目；吾爱破解从 2024-09 起未更新。

**blog（12 个源，7 天窗口内首次出现 0 条）**
- ZDI-Blog、ZDI-vulnerabilities、projectdiscovery、samcurry、dirkjanm、leavesongs、brutecat 等：都没有首次出现的新文章（ZDI 上期一次公开的 47 条 Meta AI 库 0Day 已报过）；「微信公众号」源从 2025-02 起未更新。

**BugBounty（HackerOne 公开报告，SecureFlow all 共 4 条）**
- HTTP/2 流拆除时可能把已释放的响应内存发给对端：[HackerOne #4110110](https://hackerone.com/reports/4110110)
- HTTPS Agent 在不同 secureContext 策略之间复用 TLS 认证状态：[HackerOne #3908163](https://hackerone.com/reports/3908163)
- 密码保护的开发店铺可未认证访问 UCP/MCP 商品目录：[HackerOne #4062639](https://hackerone.com/reports/4062639)
- 公开看板页面带 Cache-Control: public 却没有 Vary: Cookie，登录用户的内容可能被缓存给他人：[HackerOne #4151790](https://hackerone.com/reports/4151790)

## AI/TLDR 动态（来自 ai-tldr.dev；本窗口 36 小时内新条目 16 条，其中 security 类 1 条）

今天 AI 圈以 Google 为主：Gemini 4 Hydrogen（便宜、快速的 agent 模型）、A2UI 1.0 生成式 UI 协议定稿、Gemini 智能眼镜开放预订；VS Code 1.146 宣布三个月后移除 Local agent harness。行业大事是 Nvidia CEO 黄仁勋离任，CFO 暂代。安全相关：OpenAI 开源扫描器 Codex Security 0.10.0 支持续扫和成本上限；唯一的 security 类条目是电压毛刺把矿卡解锁成完整的 A100-80G（硬件安全）；另外 United Airlines 禁止第三方 AI agent 代订机票。

**安全**
- 【security】电压毛刺解锁 A100：GA100 矿卡解锁出 80 GB 显存和完整算力。[链接](https://ai-tldr.dev/releases/kate-land-a100-voltage-glitch-unlock/)
- 【tool·安全相关】Codex Security 0.10.0：断点续扫、成本预算、补丁失败提示更清楚。[链接](https://ai-tldr.dev/releases/openai-codex-security-0-10-0/)
- 【ecosystem·agent 管控】United Airlines 禁止第三方 AI agent 订票。[链接](https://ai-tldr.dev/releases/united-airlines-ai-agent-booking-ban/)

**模型**
- Gemini 4 Hydrogen：面向编码 agent 的低价快速模型。[链接](https://ai-tldr.dev/releases/google-gemini-4-hydrogen/)
- ERNIE 5.5 Flash Preview：百度 280B MoE（14B 激活），面向长程 agent 编码。[链接](https://ai-tldr.dev/releases/baidu-ernie-5-5-flash-preview/)
- MiniMax H3-Image：开放权重，约 10 秒生成或编辑 4K 图像。[链接](https://ai-tldr.dev/releases/minimax-h3-image/)

**工具与仓库**
- VS Code 1.146：Local agent harness 进入三个月下线倒计时，Copilot harness 保留。[链接](https://ai-tldr.dev/releases/microsoft-vscode-1-146/)
- A2UI 1.0：agent 只描述界面，由 React/Flutter/SwiftUI/Compose 用自己的组件渲染。[链接](https://ai-tldr.dev/releases/google-a2ui-1-0/)
- agent-browser 0.42（Vercel）：录制并回放浏览器流程。[链接](https://ai-tldr.dev/releases/vercel-labs-agent-browser-0-42/)
- ha-mcp 9.2.0：Home Assistant MCP 服务器（让 AI 改写或回滚自动化，权限需谨慎）。[链接](https://ai-tldr.dev/releases/homeassistant-ai-ha-mcp-9-2-0/)
- Yogurt：本地运行的开源会议纪要工具。[链接](https://ai-tldr.dev/releases/frigadehq-yogurt/)
- MACaQ（华为）：统一的 4-bit 量化方案。[链接](https://ai-tldr.dev/releases/huawei-csl-macaq/)

**其他**
- 黄仁勋离任 Nvidia CEO。[链接](https://ai-tldr.dev/releases/nvidia-board-oust-jensen-huang-report/)
- Google Intelligent Eyewear 开放预订（$395 起）。[链接](https://ai-tldr.dev/releases/google-intelligent-eyewear-preorder/)
- 用线性规划做权重空间编辑，比 AI 反复试错少 8 倍编辑量。[链接](https://ai-tldr.dev/releases/nathan-barry-weight-space-lp/)
- Two Minute Papers：DeepMind AI 证明 Signal 加密代码的正确性。[链接](https://ai-tldr.dev/releases/two-minute-papers-alphaproof-code-nov12/)

## Agent 用例动态（来自 agentusecases.ai；48 小时内新条目 24 条，全部列出）

今天的用例集中在「钱」：让 agent 炒币、炒股、读联动账户做理财决策，其中一例 OpenClaw 做了 47 笔加密期货交易，有 4 笔被人工推翻（包括一笔失控的 ETH 多单），最后被收回执行权限。小生意场景有 Claude Code 读邮件后自动开发票并发送、从 CSV 发票里找供应商涨价、帮招聘方夜间约面试。编程侧有 Claude Code 与 Codex 混编的 agent 集群、在每个 PR 上跑 LLM 评审。家居方面有语音管家、蓝牙控制跑步机等。

**安全与可靠性（置顶）**
- 【权限】OpenClaw 在交易员规则下做加密期货，出现失控单后被收回执行权限。[用例](https://agentusecases.ai/use-case/run-crypto-futures-trades-with-an-agent-under-trader-set-rul)
- 【权限】Claude 通过 Plaid 接入金融账户，辅助理财和投资决策。[用例](https://agentusecases.ai/use-case/use-claude-on-linked-accounts-for-finance-and-investing-deci)
- 【外发动作】Claude Code 读邮件后直接起草并**发送**发票。[用例](https://agentusecases.ai/use-case/draft-and-send-invoices-from-email-details)
- 【可靠性】Perplexity Comet 订宠物友好酒店失败，连不上订房网站。[用例](https://agentusecases.ai/use-case/book-a-pet-friendly-hotel-with-a-browser-agent)
- 【外发动作】给线索打分后自动发冷启动邮件。[用例](https://agentusecases.ai/use-case/score-enriched-leads-and-send-cold-emails)

**编程与工程**
- Claude Code + Codex 多 agent 集群编排。[用例](https://agentusecases.ai/use-case/orchestrate-a-swarm-of-coding-agents-across-claude-code-and-)
- 每个 PR 跑 LLM 评审与 QA，合并量翻三倍。[用例](https://agentusecases.ai/use-case/run-llm-code-review-and-qa-on-every-pull-request)
- 用 Claude Code 写 45 页医学影像综述（113 篇引用）。[用例](https://agentusecases.ai/use-case/write-a-45-page-medical-imaging-literature-review)

**工作与小生意**
- 夜间重新联系未回复的求职者并约面试。[用例](https://agentusecases.ai/use-case/re-engage-unanswered-applicants-and-schedule-screening-calls)
- 从杂货发票里找供应商悄悄涨价。[用例](https://agentusecases.ai/use-case/spot-vendor-price-creep-in-grocery-invoices)
- 把工单、报价、发票登记到表格（有人工复核）。[用例](https://agentusecases.ai/use-case/log-jobs-quotes-and-invoices-into-spreadsheets)
- 工作邮件分拣并起草通话跟进。[用例](https://agentusecases.ai/use-case/triage-work-email-and-draft-call-follow-ups)
- 扫 Zillow 找 25 万美元以下的翻新房源。[用例](https://agentusecases.ai/use-case/scan-zillow-for-fix-and-flip-deals-under-250k)
- 用 ChatGPT 打赢小额诉讼（约 $400）。[用例](https://agentusecases.ai/use-case/win-a-small-claims-case-against-a-landlord)

**投资**
- 让多家 AI 模型交易股票和 ETF（473 天）。[用例](https://agentusecases.ai/use-case/let-ai-models-trade-stocks-and-etfs)
- 用 Claude skills 研究个股。[用例](https://agentusecases.ai/use-case/research-stocks-with-claude-skills)
- 记录交易历史并指出前后矛盾的决策。[用例](https://agentusecases.ai/use-case/track-trade-history-and-flag-contradictory-decisions)

**生活与娱乐**
- 语音管家：购物清单、菜单、家务、灯光、扫地机器人。[用例](https://agentusecases.ai/use-case/run-household-lists-meals-chores-and-smart-home-by-voice)
- 蓝牙控制家用跑步机。[用例](https://agentusecases.ai/use-case/control-a-home-treadmill-over-bluetooth)
- 盘点并重新同步 Hue 与 Apple Home 设备。[用例](https://agentusecases.ai/use-case/inventory-and-resync-hue-and-apple-home-devices)
- agent 借数据湖仓控制花园。[用例](https://agentusecases.ai/use-case/let-an-agent-control-a-garden-using-a-lakehouse)
- Claude 通过 Spotify MCP 点歌、建歌单。[用例](https://agentusecases.ai/use-case/let-claude-queue-songs-and-build-playlists-in-spotify)
- agent-browser 经 CDP 控制桌面音乐播放器点歌。[用例](https://agentusecases.ai/use-case/have-an-agent-request-songs-in-a-desktop-music-player)
- Claude computer use 刷《崩坏：星穹铁道》日常。[用例](https://agentusecases.ai/use-case/clear-daily-game-tasks-in-honkai-star-rail-by-computer-use)

## 地址／IoC 汇总

以下原样抄录自公开帖子／报告，已做防误点处理（[.]），仅用于检测与狩猎：

- N-able N-central 4EverAble2Shell 利用源（来源：[Huntback](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers)、[THN](https://thehackernews.com/2026/11/new-n-central-exploits-work-against.html)）
  - IP：`157.20.241[.]16`（探测、利用链与挖矿脚本下载）
  - 矿机命名特征：`nc_` 加受害 IP
- Xen Orchestra VSA-2026-062（来源：[Vates 公告](https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-062/)、[THN](https://thehackernews.com/2026/11/hackers-exploit-critical-xen-orchestra.html)）
  - IP：`91.211.251[.]112`（端口 8001）、`193.148.56[.]72`、`37.221.208[.]216`、`45.66.35[.]11`、`64.65.0[.]120`、`64.65.62[.]160`、`89.47.51[.]90`、`92.60.37[.]247`
  - Tor：`ustar3rqxgnskzgnwkgpofgtvxevm6cx3lxdbwt4mndtveqyaohid[.]onion`（端口 3333）
  - 主机痕迹：VM 名 `pivot2`；文件 `/etc/cron.d/zz-ustar`、`/etc/cron.d/zz-ustar2`、`/.ustar5`、`/.ustar6`
- Silent Lynx 暴露服务器（来源：[CloudSEK](https://www.cloudsek.com/blog/off-the-rails-inside-an-exposed-silent-lynx-server)）
  - IP：`89.125.213[.]123`（端口 8088，开放目录）
- Claude Code agent 加密货币窃取活动（来源：[@fr0gger_](https://x.com/fr0gger_/status/2120682378360426757)）
  - IP：`91.92.40[.]140`、`46.166.162[.]7`
  - Solana 地址：`GUgzfFJVNweA7uHe5u3CkXRwBS1FG4TvwMpVBMLgNcL`
  - EVM 地址：`0xB596F1E1122cfd5503977C2666407a0256fcAe35`
- macOS 伪装 Teams 安装包（来源：[@L0Psec](https://x.com/L0Psec/status/2120903905613902080)）
  - SHA256（MicrosoftTeamsSetup.dmg）：`380df7164ce9d69ab91a4f1ebf07df097160283be767c398e93c5efa7a6724ae`
- SideCopy（来源：[@phatomcandle](https://x.com/phatomcandle/status/2120900927733256399)，个人狩猎帖，未经厂商确认）
  - 域名：`store2[.]shop`；IP：`213.176.93[.]17`
  - SHA256：`55c94013769e3eb809ff76bdb35482c1971d1e3442dd6d81865da8cca13c8b46`
- GitHub CI 窃取器「wfx」狩猎特征（来源：[THN](https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html)）
  - PR 标题 `docs: dependency audit notes`；分支名 `wfx-docs`
- 其余条目（Apache mod_http2、ScreenConnect SCKit、CopperDragon、Elastic SANSAR、Operation Endgame 等）的 IoC 在厂商报告原文中（Huntress、Check Point、Elastic 均附 IoC 列表），本窗口读到的帖子和摘要里没有可直接抄录的条目，请以原文为准。

## 来源搜索 URL

**X 只读搜索（search_posts_all，起点 2026-11-11T23:00Z，终点 11-12T22:59Z）**
- `(CVE OR 0day OR "zero-day" OR exploit OR PoC) (patch OR exploited OR advisory OR KEV) -is:retweet lang:en`：Latest 25 条（11-12 22:23～22:58 UTC）＋relevancy 25 条（11-12 01:30～22:54）。[x.com 搜索](https://x.com/search?q=CVE%20exploited%20patch&f=live)
- `("actively exploited" OR "exploited in the wild" OR "in-the-wild" OR "zero-day") -is:retweet -is:reply lang:en`：relevancy 25 条（11-11 23:28～11-12 18:48）
- `github.com (C2 OR "red team" OR redteam OR nuclei OR "offensive security" OR BOF OR EDR OR pentest OR "security tool") -is:retweet`：Latest 4 条、relevancy 4 条（同一批 4 条，均与安全工具无关）
- `("malware analysis" OR "threat report" OR "threat actor" OR APT OR ransomware) (research OR report OR campaign) -is:retweet lang:en`：Latest 25 条（11-12 18:25～22:46）＋relevancy 25 条（11-12 00:00～22:46）
- 补搜 `(malware OR backdoor OR stealer OR loader OR APT) ("new research" OR analysis OR blog OR IOCs OR IoC) -is:retweet`：relevancy 25 条（11-11 23:04～11-12 19:19）
- 定向 `("mod_http2" OR "CVE-2026-119618" OR ScreenConnect OR "N-central" OR 4EverAble2Shell OR "Operation Endgame" OR "CVE-2026-121529" OR FortiClient OR "Xen Orchestra" OR SignDrop) -is:retweet`：relevancy 25 条（11-11 23:04～11-12 21:09）
- LWiS X List：[x.com/i/lists/1239330068461244424](https://x.com/i/lists/1239330068461244424)（2 页 197 帖，11-11 22:58～11-12 22:55 UTC）
- X 合计：11 次只读调用共 380 帖，去重后 366 个帖子 ID（含 List）。

**其他信源**
- pwn.watch：https://pwn.watch/feed.xml （50 条，最新 11-08 20:19 UTC；本窗口新事件 0 条；佐证引用 2 个事件页：SonicWall CVE-2026-19868、FreeSWITCH CVE-2026-116779）
- ExploitGrid 最新 exploit：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （100 条，覆盖 11-10 04:14～11-11 20:12 UTC；本窗口新增 0 条，上期截止后到本窗口开始前新增 50 多条；按 CVE 查询 8 次：CVE-2026-121529 4 条、CVE-2026-124194 2 条、CVE-2026-19868 2 条、CVE-2026-90436 1 条、CVE-2026-118383 1 条；CVE-2026-119618、CVE-2026-6460、CVE-2026-121653 为 0 条）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （共 17 条，两页全取；11-13 到期 3 条、11-20 到期 1 条、11-24 到期 4 条）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条，覆盖 2026-11-02 14:00～11-13 03:58 北京时间；48 小时内未收录 13 条：先知 8、HackerOne 4、Seebug 1）
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community （7 个源全部拉取；48 小时新条目 9 条：先知 8、Seebug 1，其余 5 个源 0 条）
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog （12 个源全部拉取；7 天内首次出现 0 条）
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条；36 小时内新条目 16 条，security 类 1 条）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条；48 小时内新条目 24 条）
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （catalogVersion 2026.11.10，共 1,779 条；11-11、11-12 无新增）
- 阮一峰周刊：工作日版不加（11-07 周六版已收录第 418 期）。

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

1. 采集：通过。X 三组只读搜索（Latest＋relevancy 补搜）＋在野利用、恶意软件、定向三组补搜，以及 LWiS List 两页都已完成（11 次只读调用，380 帖，去重 366 个 ID），覆盖时长写在报告头；SecureFlow all（13 条）、community 7 个源（9 条）、blog 12 个源（0 条）全部拉取并按窗口筛选；Agent Use Cases 24 条；AI/TLDR 16 条（security 类 1 条）；pwn.watch、ExploitGrid、CISA KEV 均已拉取并交叉核对；工作日版不加周刊节（已确认 11-07 周六版收录过第 418 期）。说明：① 「github.com + C2/红队」这组 Latest 和 relevancy 都只有 4 条且与安全工具无关，工具节主要靠 LWiS List；② **pwn.watch 订阅源仍停在 11-08 20:19 UTC，ExploitGrid 列表最新一条是 11-11 20:12 UTC，本窗口两者都是 0 条新增**，只作为佐证使用（pwn.watch 2 个事件页；ExploitGrid 7 个 exploit/CVE 页，以及 KEV 期限 17 条）；③ CISA KEV 目录 11-11、11-12 都没有更新。
2. 核验链接：通过。全文 196 个唯一 URL 全部用浏览器 UA 检查过：67 个 X 帖链接的 ID 与作者名都和 X 接口返回的数据对得上；其余 129 个里有 125 个直接返回 200。Huntress、NHS CC-4890、Medium（MaldocTrace）对 box 返回 403，经抓取服务读到全文，已在正文标注；Seebug paper/3533 核验时源站返回 521，链接取自 SecureFlow 原始数据，已标注。正文没有 t.co 短链。
3. 成稿：通过。十个小节齐全、无空节；IoC 节有原样抄录的 IP、域名、哈希和钱包地址；没有利用代码、payload 或利用步骤（公开 exploit 只写「已有公开 exploit」并附 ExploitGrid 或 X 帖链接，不直链 exploit 仓库；Xen Orchestra 的特征 cookie 值只指向厂商公告，不抄录）；已按 state.json 的 seen_ids 去重，67 个引用帖均为首次出现，Outlook、Xen Orchestra、SignDrop、FortiOS 等已报内容只写新进展。
4. 落盘与交付：通过。box 文件已写入（约 47 KB），state.json 已更新（last_report_date=2026-11-12）；已拷到本机 /Users/kenny1337/Desktop/_05_项目/X安全情报晚报/ 并读回确认（字节数与 SHA-256 均与 box 一致）。
