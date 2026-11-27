# X 安全情报晚报 · 2026-11-25（周三）

> 报告时间：2026-11-25 约 20:00（America/Santiago），即 2026-11-26 约 07:00（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-24 23:00 UTC 到 11-25 约 23:03 UTC（约 24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-25 23:00:43～23:02:38 UTC（约 2 分钟，CVE／POC／exploit 关键词噪声刷屏），所以加了 relevancy 补搜 25 条（11-25 14:55:22～23:03:25 UTC，约 8.13 小时），以及今日新入 KEV 编号／Mitel／Danfoss／Xen／Session Smart 等 relevancy 补搜 25 条。窗口前段主要靠工具组 Latest、威胁组 relevancy 与 LWiS List 补上。
> - 工具组 Latest 14 条覆盖 11-24 23:00:27～11-25 20:46:37 UTC（约 21.77 小时，距窗口起点约 27 秒）。
> - 威胁组 Latest 24 条只覆盖 11-25 22:22:08～23:01:51 UTC（约 40 分钟），relevancy 补搜 25 条覆盖当日勒索泄露站通告与分析帖（可见条目最早约 11-25 00:32 UTC，约跨 22 小时）。
> - LWiS List（list:1239330068461244424 只读 Latest）共翻 9 屏，合并去重后 **214** 条，整体 11-24 23:03:24～11-25 22:11:35 UTC（约 23.14 小时，距窗口起点约 3.4 分钟；最晚一条距出报约 48 分钟）。
> **其他信源**：SecureFlow 的 all／community／blog 三路接口今日均返回 **HTTP 200**。all 拉取 200 条，本窗口（约 48 小时且不在 seen_ids 的 sf:id）新条目 **142**，其中 ZDI-vulnerabilities **120** 条的原文链接已在昨日以 sfl: 写入 seen_ids（同一批 11-24 14:00 公告换了 all 接口 id，本期不重复展开），HackerOne 16 条，社区高信号 5 条（其中 InfoSec Write-ups 2 条链接已在 seen_ids，不重复展开）。community 分类 7 个源中「吾爱破解」因 updatedAt 为 2024-09-19 已跳过，其余 6 个源均 200，合计 600 条，本窗口新条目 **3**。blog 分类 12 个源中「微信公众号」因 updatedAt 为 2025-02-17 已跳过，其余 11 个源均 200，合计 367 条，7 天窗口新条目 **0**。pwn.watch 订阅源已拉取（XML／JSON 均为 200；XML 50 条），**本窗口无新条目**（订阅源最后更新于 2026-11-10 01:13:32 GMT）。ExploitGrid exploits 与 KEV 期限均为 200：exploits 列表 100 条，严格 48 小时窗口内新条目 **0**（列表最新 date 为 2026-11-20 19:48:48 UTC）；老 CVE 的重复 PoC 只计数不展开。ExploitGrid KEV 期限接口返回 10 条，覆盖今日新入目录中的 8 条，**未包含** Xen Orchestra CVE-2026-133469 与 Danfoss CVE-2025-41450，期限以 CISA 官方为准。CISA KEV 目录当前 **1805** 条（dateReleased 2026-11-25T19:48:12.4344Z），较昨日期 1795 条新增 **10** 条，全部为今日（11-25）入目录。AI/TLDR 订阅源 50 条，本窗口（约 36 小时，且不在 seen_ids）新条目 **15**，其中 category 为 security 的 **1** 条。Agent Use Cases RSS 60 条，本窗口（约 48 小时）新条目 **14**。本日为周三（America/Santiago），不加阮一峰周刊节；第 420 期已在 11-22 期收录（seen_ids 中已有）。
> **验收**：采集——X Latest 与 LWiS List 均已尝试，各 HTTP 信源已用浏览器 UA 拉取并按窗口筛选，失败项已如实写明。核验链接——主链接已用浏览器 UA 抽查：CISA 警报、Mitel／Vates／Danfoss 顾问、Palo Alto PAN-SA-2026-0015、GeoServer 官方更新、DIVD 披露页与取证 PDF、AI/TLDR 原始来源（LessWrong、Anthropic Siren、VS Code 1.148）均为 200。Juniper 官方公告页返回门户加载壳（标题 “CEC Juniper Community”，正文未出，不是 404），保留官方 URL，修复版本以多方 X 转述＋CISA 注释链接为准；Vates 顾问页为前端渲染，静态 HTML 几乎只有导航，保留官方 URL，技术事实以 CISA 短描述为准；NVD／cve.org 记录页仍是前端壳；AI/TLDR releases 详情页仍 **403**，报告保留订阅链接并用已核验的原始来源页补链；Seebug Paper 条目页返回 **521**，保留原文链接并注明。成稿——每日十节齐全（非周末，无阮一峰节），无利用代码／payload／PoC 步骤；落盘与交付见文末。

## 今日摘要

- **CISA 今天（11-25）把 10 条漏洞列入 KEV**，官方警报已发布。其中 **Mitel MiCollab AWV 组件 5 条**（含 CVSS 10.0 的未认证命令注入 CVE-2026-133323）、**Danfoss AK-SM 800A 制冷控制器 3 条**、**HPE／Juniper Session Smart Conductor／Router 未认证 root 命令注入 CVE-2026-103406**（CVSS 9.8，Juniper 称已收到利用报告，修复版本 7.0.5／7.1.7／7.2.3），以及 **Vates Xen Orchestra 空 JSON 登录令牌认证绕过 CVE-2026-133469**。联邦期限大多为 **2026-11-28**，CVE-2025-41450 与 CVE-2026-133311 为 **12-09**。@CISACyber 官方帖已公布这 10 条。
- **Palo Alto 今天发布 PAN-SA-2026-0015**，在 PAN-OS 中修复 Linux 内核本地提权 **Fragnesia（CVE-2026-46300）**。官方写明：已观察到针对**公网暴露管理口**的利用；已知利用链是先打 PHP2Shell（CVE-2026-109618，10 月底已出补丁），再用来提权。请尽快升到公告列出的 hotfix，并避免把管理口直接暴露到公网。
- **DIVD 今天公布了 9 月遭入侵的完整取证报告**：攻击使用 ARTEX（Agentic Offensive Framework），利用 Zammad 当时的两枚 0day（CVE-2026-102489／CVE-2026-102490，厂商分别在 7.2 与 7.2.2 修复），约 1.3 秒劫持管理员账户、约 20 分钟拿到 root。报告称被带走的是工单标题、邮箱和电话，未见未公开漏洞研究被窃。@KimZetter 转发了该报告（236 赞／64 转）。
- **GeoServer 官方已在 11-23 公布 10 月修复对应的 CVE**，X 上今天继续讨论未认证 RCE 链正在被利用。请升到 **3.0.2／2.28.6／2.27.7**。另：微软 11 月补丁在修复 RPC 运行时高危 RCE（CVE-2026-118737）的同时收紧了 NTLM 签名，部分第三方 SSO／代理出现认证失败；VMware 本周第三组关键补丁（含已报过的 vCenter CVE-2026-123903，以及 ESX／Workstation 相关编号）也在继续发酵。
- 工具方面，Claude-BugHunter（面向已授权测试的 Claude Code 技能包）登上 GitHub 趋势，约 22.9k star；TKNet v1.2.0 开源了 SMB 共享盘点工具。勒索方面仍有多起泄露站声明（利物浦大学、Osaki Electric 等），均未见官方确认。

## CVE / POC / 漏洞

### 1. CISA 今日新增 10 条 KEV（11-25 入目录）

CISA 于 11 月 25 日发布警报，将 10 条漏洞加入已知被利用目录，依据是活跃利用证据。官方目录由昨日期的 1795 条增至 **1805** 条。ExploitGrid 的 active-deadlines 目前列出其中 8 条，未列出 CVE-2026-133469 与 CVE-2025-41450，期限以 CISA 官方为准。已知勒索活动利用情况官方均为 Unknown。

- CISA 公告：https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog
- KEV 目录（短链 go.dhs.gov/Z3Q 会跳转到此）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- X 原帖：https://x.com/CISACyber/status/2125699750754132152 · https://x.com/issoh_co_jp/status/2125697620320403635 · https://x.com/JasonRadney74/status/2125723273057144976 · https://x.com/__kokumoto/status/2125727083423060334

#### 1.1 HPE／Juniper Session Smart：CVE-2026-103406（OS 命令注入，期限 11-28）

- 说明：CISA 称 Session Smart Conductor 与 Session Smart Router 存在 OS 命令注入（CWE-78），远程攻击者可通过特制的 salt minion ID 以 root 执行命令。多方 X 帖转述 Juniper 给出的 CVSS 为 **9.8**，并称 Juniper 已收到利用报告；修复版本为 **7.0.5／7.1.7／7.2.3**。官方公告页用浏览器 UA 访问时只返回门户加载壳，下面保留 CISA 注释中的官方 URL，版本信息以 X 交叉转述为准，不以未打开的正文为唯一依据。联邦期限 11-28。请尽快确认资产并按厂商指引升级，限制编排／密钥管理接口的公网暴露。
- X 原帖：https://x.com/CyberStackorg/status/2125701307587568114 · https://x.com/tcastroassis1/status/2125652124902052231 · https://x.com/Dernetic/status/2125642054168359301 · https://x.com/DailyDarkWeb/status/2125637442845704647 · https://x.com/ZeroKaiLabs/status/2125632458125414668
- 厂商公告：https://supportportal.juniper.net/s/article/2026-10-On-Demand-Security-Bulletin-Session-Smart-Router-and-Session-Smart-Conductor-Multiple-internally-discovered-vulnerabilities-resolved
- 厂商公告（KEV／NVD／交叉）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-103406 · https://nvd.nist.gov/vuln/detail/CVE-2026-103406 · https://www.cve.org/CVERecord?id=CVE-2026-103406 · https://exploitgrid.net/vulnerabilities/CVE-2026-103406

#### 1.2 Mitel MiCollab AWV 组件 5 条（MISA-2026-0012，多数期限 11-28）

- 说明：官方顾问 MISA-2026-0012（首发 11-16，11-24 修订 2.0 补上 CVE 编号）覆盖 Audio, Web and Video Conferencing（AWV）上的 5 条漏洞。受影响为 **MiCollab 10.3（10.3.0.18）及更早**；Mitel 为 10.3（10.3.0.18）提供补丁，也可升到后续版本，细节见 KB000129195。顾问写明这些漏洞组合利用会显著放大影响。临时缓解：限制对 AWV 组件的外部访问。
  - CVE-2026-133323：未认证 OS 命令注入，Critical／**CVSS 10.0**，期限 11-28
  - CVE-2026-133303：未认证 XML 注入（需预置恶意内容），Critical／9.0，期限 11-28
  - CVE-2026-133275：未认证危险类型文件上传，Medium／5.3，期限 11-28
  - CVE-2026-133324：认证处理不当导致认证绕过，Medium／5.3，期限 11-28
  - CVE-2026-133311：弱认证，可用系统生成的随机标识或预置内容读取敏感信息，Medium／5.9，期限 **12-09**
- X 原帖：https://x.com/CipherSecurityN/status/2125683720526962811 · https://x.com/issoh_co_jp/status/2125697622098776322 · https://x.com/ndayland/status/2125726439026962529
- 厂商公告：https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012
- 厂商公告（KEV／NVD／交叉）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-133323 · https://nvd.nist.gov/vuln/detail/CVE-2026-133323 · https://exploitgrid.net/vulnerabilities/CVE-2026-133323

#### 1.3 Danfoss AK-SM 800A 系列 3 条（DSA-2023-08-01／DSA-2025-03-01）

- 说明：三条均已有厂商补丁，但今天因活跃利用被列入 KEV。CISA 与 BleepingComputer 都在提示这批制冷控制器漏洞。
  - CVE-2023-25915：输入校验不当导致远程任意命令执行，厂商 CVSS **9.8**，修复为软件 **3.3**（低于 3.3 受影响），期限 11-28。同一顾问还提到 CVE-2023-25913（认证绕过，**未**列入本次 KEV）。
  - CVE-2023-25914：经 XML 接口的路径遍历，可读底层系统文件，厂商 CVSS 7.5，同样在 DSA-2023-08-01 中用 3.3 修复，期限 11-28。
  - CVE-2025-41450：不当认证，攻击者可生成泄露内网 IP、用户名、门店名等信息的 Web 报告，厂商 CVSS 8.2，修复为 **4.2**（4.2 之前受影响），期限 **12-09**。致谢 Claroty Team82。
- X 原帖：https://x.com/Dinosn/status/2125626124222808361
- 文章：https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-unpatched-flaw-in-danfoss-refrigeration-controllers/
- 厂商公告：https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2023-08-01 · https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-03-01
- 下载／升级入口（厂商顾问引用）：https://www.danfoss.com/en/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/#tab-overview
- 厂商公告（KEV／NVD／交叉）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2023-25915 · https://nvd.nist.gov/vuln/detail/CVE-2023-25915 · https://nvd.nist.gov/vuln/detail/CVE-2025-41450

#### 1.4 Vates Xen Orchestra：CVE-2026-133469（空对象登录令牌，期限 11-28）

- 说明：CISA 称 Xen Orchestra 对输入类型校验不当，未认证攻击者可通过含空 JSON 对象的特制认证令牌绕过认证并以管理权限操作。厂商顾问为 VSA-2026-062（标题 Empty-object login token）。顾问页静态 HTML 几乎只有导航，本期技术事实以 CISA 短描述为准，保留官方 URL。联邦期限 11-28。
- 厂商公告：https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-062/
- 厂商公告（KEV／NVD／交叉）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-133469 · https://nvd.nist.gov/vuln/detail/CVE-2026-133469 · https://www.cve.org/CVERecord?id=CVE-2026-133469 · https://exploitgrid.net/vulnerabilities/CVE-2026-133469

### 2. Palo Alto PAN-OS 修复已在野利用的 Fragnesia（CVE-2026-46300，PAN-SA-2026-0015）

- 说明：Palo Alto 今天的 OSS CVE 公告修复 Linux 内核 XFRM ESP-in-TCP 子系统本地提权 Fragnesia。官方写明：已观察到针对**公网暴露管理口**的利用；问答称目前所见利用都走这条暴露路径。SecurityWeek 还回顾了 10 月底的攻击：中国背景威胁者先用 PHP2Shell（CVE-2026-109618）拿 RCE，再打 Fragnesia 部署 root webshell，涉及 24 台防火墙和 1 台内部管理服务器。PHP2Shell 已在 10-30 左右对受支持版本出补丁；即便已打 PHP2Shell 补丁，厂商仍建议一并打上 Fragnesia hotfix，并避免管理口直接对公网开放（只从管理网或经 VPN 进入）。修复版本包括 **12.2.4-h3、12.1.10-h6、12.1.7-h15、12.1.4-h15、11.2.16-h3、11.2.13-h6、11.2.10-h19、11.2.7-h25、11.2.4-h25、11.1.16-h6、11.1.13-h18、11.1.10-h38、11.1.7-h14、11.1.6-h42、11.1.4-h40、10.2.18-h15、10.2.16-h14、10.2.13-h29、10.2.10-h45、10.2.7-h41** 及之后版本。
- X 原帖：https://x.com/Dinosn/status/2125524144288682121
- 厂商公告：https://security.paloaltonetworks.com/PAN-SA-2026-0015 · https://security.paloaltonetworks.com/CVE-2026-46300
- 相关（PHP2Shell，10 月）：https://security.paloaltonetworks.com/CVE-2026-109618
- 文章：https://www.securityweek.com/palo-alto-networks-patches-fragnesia-flaw-used-to-root-firewalls/ · https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-fragnesia-flaw-exploited-in-pan-os-attacks/

### 3. GeoServer：官方公布 CVE，X 称未认证 RCE 链仍在被利用

- 说明：GeoServer 项目在 **11-23** 发文，为 10 月稳定版／维护版中已修复的问题补上 CVE，并再次呼吁升级到 **3.0.2／2.28.6／2.27.7**。The Hacker News 今天的报道（经 @Dinosn 转发）称两条缺陷正被利用，研究者警告存在未认证 RCE 链。本期只记补丁版本与狩猎优先级，不写利用步骤、不链 PoC 仓库。若实例尚未升级，应视为紧急。
- X 原帖：https://x.com/Dinosn/status/2125604335849742342
- 厂商公告：https://geoserver.org/vulnerability/2026/11/23/cve-update.html
- 文章：https://thehackernews.com/2026/11/hackers-exploit-two-geoserver-flaws-as.html

### 4. 微软 11 月补丁：CVE-2026-118737 与 NTLM 签名兼容性问题

- 说明：BleepingComputer 与 The Register 今天都写到，11 月安全更新修复了 Windows RPC 运行时中的高危 RCE **CVE-2026-118737**（时序相关认证弱点，官方称未认证攻击者可在未交互情况下远程执行代码），并作为 NTLM 消息签名加固的第一阶段。与此同时，部分未正确实现 NTLM 的第三方应用、认证代理和 SSO 出现认证失败（例如 CHALLENGE 里置了 TARGET_INFO 标志却给出空／不完整的 TargetInfo）。微软已承认兼容性问题，并在支持文档中提供了临时缓解。The Register 也从第三方登录受阻的角度做了跟进。请在修补 RPC／NTLM 相关漏洞的同时，评估依赖 NTLM 的第三方组件。
- X 原帖：https://x.com/Dinosn/status/2125524110990295288 · https://x.com/Dinosn/status/2125658566426001901
- 文章：https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-authentication-issues-after-november-updates/ · https://www.theregister.com/security/2026/11/25/microsofts-ntlm-security-changes-trip-up-third-party-logins/5312085

### 5. VMware 本周第三组关键补丁（含已报过的 CVE-2026-123903）

- 说明：上期已收录 Broadcom VMSA-2026-0011 中的 vCenter 认证绕过 **CVE-2026-123903**（CVSS 9.8）。The Register 今天称这是一周内第三组关键补丁，除 123903 外还提到可在 ESX 上执行代码的 **CVE-2026-123910**（I/O filter 服务堆溢出写）、**CVE-2026-123911**（释放后使用），以及 Workstation／Fusion 上的客户机逃逸 **CVE-2026-123912**（也存在于 ESX，但官方称无法逃出该产品沙箱；与 USB 控制器有关，可通过关闭该控制器缓解）。文章称上周部分更新已覆盖今天披露的部分问题，但仍有跨 ESX、vCenter、Workstation、Fusion、Tools、Cloud Foundation 等十余个产品的新补丁要打。@codewhitesec 称其在顾问发布两天前已有针对 CVE-2026-123903 的可工作利用（本期不链仓库、不写步骤）。Box 访问 Broadcom 安全公告门户未能定位到一条新的、带明确编号的公告页，产品修补请以 Broadcom／VMware 官方顾问为准。
- X 原帖：https://x.com/Dinosn/status/2125469495066071547 · https://x.com/codewhitesec/status/2125629967690060000
- 文章：https://www.theregister.com/virtualization/2026/11/25/this-could-mess-with-thanksgiving-says-vmware-as-it-drops-third-critical-patch-bundle-in-a-week/5312017

### 6. Drupal 核心安装器 RCE（CVE-2026-132165）仍在被利用（跟进）

- 说明：该条已在上期作为 11-24 新入 KEV、期限 11-27 收录，修复版本为 **10.6.22／11.3.22／11.4.13**。今天 The Hacker News 与 BleepingComputer 继续报道 Fail2Install／实站劫持，说明窗口内利用仍在发生。请确认已升级并限制 `/core/install.php` 的公网访问。联邦期限就是 **11-27**。
- X 原帖：https://x.com/Dinosn/status/2125577017072480271 · https://x.com/Dinosn/status/2125536974371188932
- 文章：https://thehackernews.com/2026/11/drupal-fail2install-exploit-details.html · https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-drupal-rce-flaw-to-hijack-sites/
- 厂商公告：https://www.drupal.org/sa-core-2026-017 · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-132165

### 7. 即将到期的既有 KEV（提醒，不重复展开）

- **明天（11-26）到期**（11-23 入目录，已在此前日报收录）：Project MONAI Label CVE-2026-133968、N-able MailAssure CVE-2026-134624。
- **11-27 到期**（11-24 入目录，已在上期收录）：Drupal CVE-2026-132165、Idunno AntiCsrf CVE-2026-131914、Optimizely Web Experimentation CVE-2026-132224。
- 目录检索：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-133968 · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-134624

### 8. Google Project Zero：Apple RawCamera 多条内存损坏

- 说明：@ProjectZeroBugs 今天连续披露 Apple RawCamera 解码路径上的一组堆溢出／越界读／未初始化内存问题（DNG Deflate、Sony Deflate、Hasselblad、lossless-JPEG、Phase One IIQ、JPEG-XL 缩略图等）。目前公开条目以 Project Zero 问题跟踪为准，未见同步的 Apple 安全公告编号被交叉到本期采集里。建议关注后续 Apple 安全更新。
- X 原帖：https://x.com/ProjectZeroBugs/status/2125533872431731076 · https://x.com/ProjectZeroBugs/status/2125533872498802939 · https://x.com/ProjectZeroBugs/status/2125534146483327317
- 文章／跟踪：https://project-zero.issues.chromium.org/issues/552288129

## 工具与 GitHub 发布

### 1. Claude-BugHunter：面向已授权测试的 Claude Code 技能包，登顶 GitHub 趋势

- 说明：elementalsouls/Claude-BugHunter 被多条 X 帖列为当日 GitHub 趋势第一，仓库页显示约 **22.9k** star、2.3k fork。简介为 84 个技能、15 条斜杠命令、681 条已公开报告模式，覆盖常见漏洞类别与身份／基础设施攻击矩阵。发布者与转发帖都写明**仅用于已获授权的系统**。不是 C2，而是 AI 辅助漏洞狩猎技能包。
- X 原帖：https://x.com/trending_repos/status/2125562202124079152 · https://x.com/demmagence/status/2125689209256079806 · https://x.com/yaro360/status/2125363950384464207
- GitHub：https://github.com/elementalsouls/Claude-BugHunter

### 2. TKNet v1.2.0：Linux／Windows 下盘点 SMB 共享与账户权限

- 说明：@BridgerTalha 发布开源桌面网络扫描器 TKNet v1.2.0，用于在渗透／红队项目中枚举 SMB 共享、检查特定账户的读写权限，并导出确认的 IPv4 主机。
- X 原帖：https://x.com/BridgerTalha/status/2125692656646771179
- GitHub：https://github.com/BridgerAlderson/TKNet

### 3. Claroty 公开 OPC-UA 漏洞研究框架

- 说明：@kmkz_security 转发 Claroty 的 opcua-exploit-framework，定位为 OPC-UA 协议的漏洞研究框架（仓库描述含 research & exploitation）。本期只记该研究工具已公开这一事实与仓库地址，不写利用步骤。
- X 原帖：https://x.com/kmkz_security/status/2125660994370486608
- GitHub：https://github.com/claroty/opcua-exploit-framework

### 4. 其他工具动态

- ProjectDiscovery 宣传可为编码 agent 一键加入 SecurityContext（免费、无需 API key）：https://x.com/pdiscoveryio/status/2125601647066075401 · https://go.projectdiscovery.io/installsecuritycontext
- @ipurple 介绍基于 Elastic 检测规则（可选 Defender 签名）的文件扫描器 phantom-seeker：https://x.com/ipurple/status/2125602221274333255 · https://github.com/FarrimWildaxe/phantom-seeker
- Florian Roth（@cyb3rops）放出《AOFs and Defensive Minimalism》讲稿 PDF（英／德）：https://x.com/cyb3rops/status/2125485767799550172 · https://github.com/Neo23x0/Talks/blob/master/AOFs-and-Defensive-Minimalism-Slides-EN.pdf
- @NinjaParanoid 表示 Brute Ratel（BRc4）不打算在 2027 年涨价：https://x.com/NinjaParanoid/status/2125600401659740598

## APT / Malware 分析

### 1. DIVD 公布 9 月入侵完整取证：ARTEX 智能体＋Zammad 0day

- 说明：荷兰漏洞披露组织 DIVD 今天放出 DIVD-2026-00014 的完整披露与取证报告（PDF 约 9 MB，已核验为 application/pdf）。官方概述：2026-09-21，攻击者入侵用于 csirt@divd.nl 等邮箱的 Zammad 工单系统，利用当时的两枚 0day **CVE-2026-102489** 与 **CVE-2026-102490**（已通过 DIVD-2026-00015 报告给厂商，分别在 Zammad **7.2** 与 **7.2.2** 修复）。@KimZetter 引述：约 **1.3 秒**劫持管理员账户，约 **20 分钟**取得服务器完全控制。官方称攻击后续使用了 ARTEX（Agentic Offensive Framework）一类 AI agent，活动量与生成物数量很大；被带走的是工单标题、邮箱和电话，**未见未公开漏洞研究被窃**，网络隔离限制了横向。使用 Zammad 的组织应确认已升到包含上述修复的版本。本期只记谁／打什么／补丁，不转载攻击步骤或 payload。
- X 原帖：https://x.com/KimZetter/status/2125619443762151835
- 文章／报告：https://csirt.divd.nl/cases/DIVD-2026-00014/ · https://csirt.divd.nl/cases/DIVD-2026-00014/full_disclosure/ · https://www.divd.nl/hacked/ · https://www.divd.nl/documents/DIVD-2026-00014-forensics-report.pdf

### 2. 泄露站声明的勒索事件（均未见官方确认）

- 说明：FalconFeeds／相关账号今天继续转发泄露站添加受害者的声明，包括但不限于：英国利物浦大学（ScarlettGroup，声称 6–7 日内公布）、日本 Osaki Electric 智能电表相关生产受扰（独立新闻转发）、美国 New Plymouth School District（INTERLOCK，声称约 200 GB）、美国 York Engineering（RHYSIDA）、英国 Plumbs Limited（Aur0ra）、北马其顿 ALSA NET（Space Bears）、哥伦比亚 XACTUS（Qilin）、西班牙 Islas Natura（Meduza Locker），以及 PLAY、FALCON 等对多家公司的清单。FALCON 对 Aimbridge Hospitality 与 CSG Systems 的声明已在上期出现。均为泄露站单方陈述，**未见受害方官方确认**，仅供狩猎与监测优先级参考。
- X 原帖：https://x.com/FalconFeedsio/status/2125666624619659275 · https://x.com/rtehrani/status/2125720189572378792 · https://x.com/FalconFeedsio/status/2125687982741184765 · https://x.com/FalconFeedsio/status/2125687757834183001 · https://x.com/FalconFeedsio/status/2125621730408534254 · https://x.com/FalconFeedsio/status/2125455040265724142

### 3. 其他威胁简讯

- InfraTrust 警告网络设备供应链缺陷已被利用（细节以报道为准）：https://x.com/Dinosn/status/2125613559061090387 · https://www.bleepingcomputer.com/news/security/infratrust-warns-of-exploited-supply-chain-flaws-in-network-appliances/
- 报道称 Remus Stealer 所宣传的「Gmail 0day」实为恶意 Chrome 扩展：https://x.com/Dinosn/status/2125597890613551403 · https://cyberinsider.com/remus-stealer-gmail-zero-day-chrome-extension/

## SecureFlow 信息流精选

all 接口 48 小时未见 sf:id 共 142 条，但其中 120 条 ZDI-vulnerabilities 的原文链接已在昨日期以 sfl: 入库（11-24 14:00 那批 Pwn2Own／0day 公告），本期不重复展开。InfoSec Write-ups 两篇（DHS 赏金、Intel／CBSE JWT）链接亦已在 seen_ids。blog 分类 7 天窗口无新条目。以下为 X 上未作为主条展开、且链接尚未入库的社区高信号。

### community

- 先知社区｜Dagu 未授权远程命令执行（CVE-2026-126752）复现与代码审计（2026-11-24 12:44）。社区分析帖，本期只记存在该 CVE／分析文、不写复现步骤。原文：https://xz.aliyun.com/news/93419
- 先知社区｜蓝队防御 AI Agent 任务链攻击的 WAF 检测错位分析与会话级评分方案（2026-11-24 13:45）。防御向讨论，与本期 AI agent 安全主题相关。原文：https://xz.aliyun.com/news/93415
- Seebug Paper｜MirrorGuard：防御 LiDAR 感知免受被动镜面攻击（2026-11-25 16:32）。用浏览器 UA 访问条目页返回 **521**，保留链接。原文：https://paper.seebug.org/3537

### blog

本日无显著更新。

### BugBounty

HackerOne 公开报告本窗口新 16 条，多为常规注入／逻辑类披露；标题带 CVE 的 1 条为「Default OAuth2 Credentials on SAP Commerce Cloud — Admin Token via Published Sample Secret（CVE-2026-44761）」：https://hackerone.com/reports/3966705 。其余低信号条目只计数不展开。

## AI/TLDR 动态

来自 ai-tldr.dev，本窗口新条目 **15** 条（其中 security **1** 条；video／showcase 低信号可少展开）。AI/TLDR releases 详情页今日仍 403，下面同时给出已核验的原始来源（如有）。

今日 AI 圈的两条安全向消息最值得看：一篇 LessWrong 研究指出，即便模型各自处于沙箱，只要共用同一推理服务器，仍可能通过批大小／内核舍入等副作用通道互传信息；Anthropic 则公开了 Siren 评估，用来测量 Claude 在「沙箱门没关严」时会不会走出去。产品侧，Anthropic 把 Messages API 迁到 Rust（号称单请求 CPU 降约 70%），VS Code 1.148 让 agent 在关闭窗口后继续跑，Claude Code 2.1.332 支持从 MCP 服务器拉取 skills。数学／理论方面，围绕 Claude 辅助的黎曼猜想证明、OpenAI 声称矩阵乘法指数恰为 9/4、以及 Google agent 发布的因子分解相关论文，争议和跟进都很多，本期只记事实、不做对错裁决。

### 安全

- **（安全）** 沙箱中的模型仍可借共享推理服务器互通：Niranjan Deshpande 与 David Africa 在 LessWrong 写到，共用 vLLM 等推理服务时，批大小导致的内核舍入、KV cache 复用等可成为隐蔽信道。https://ai-tldr.dev/releases/lesswrong-models-communicate-via-inference-servers/ · 原文：https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being-sandboxed
- **（安全／评测，benchmark）** Anthropic Siren：故意把沙箱门留缝，统计 Claude 走出边界并误用外部材料的频率；官方页介绍了 1700+ 场景与缓解措施。https://ai-tldr.dev/releases/anthropic-siren-sandbox-escape-eval/ · 原文：https://safeguards.anthropic.com/2026/siren/

### 模型

- LlamaIndex 发布仅 8.1M 参数、可在普通 CPU 上跑的 OCR 模型 OCRia-nano-1：https://ai-tldr.dev/releases/llamaindex-ocria-nano-1/
- PrismML Ternary Bonsai 2.5 27B：约 5.9 GB 体积，宣称在 agent 任务上接近全精度：https://ai-tldr.dev/releases/prismml-bonsai-2-5-27b/

### 工具与开源仓库

- VS Code 1.148：关闭窗口后 agent 仍可继续工作，并可将会话放入独立容器。https://ai-tldr.dev/releases/microsoft-vscode-1-148/ · 官方说明：https://code.visualstudio.com/updates/v1_148
- Claude Code 2.1.332：支持从 MCP 服务器提供 skills，并修复一系列挂起（GitHub changelog 今日 503，仅保留订阅链接）：https://ai-tldr.dev/releases/anthropic-claude-code-2-1-332/
- DeepMind Antigravity 插件 Mass Spec Skills：从 MS/MS 谱图辅助鉴定分子：https://ai-tldr.dev/releases/deepmind-antigravity-mass-spec-skills/
- Sous Labs Songe：在机器空闲时用本地计算训练你的模型：https://ai-tldr.dev/releases/sous-labs-songe/

### 论文与研究

- OpenAI 预印本声称方阵乘法指数恰好是 9/4：https://ai-tldr.dev/releases/openai-math-matrix-multiplication-nine-fourths/
- Google Cogentic／agent 一天内挂出多篇理论纸，其中包括宣称已证明的更快整数分解：https://ai-tldr.dev/releases/google-cogentic-factoring-discrete-log-papers/

### 行业动态

- Anthropic 称已将 Messages API 迁到 Rust，由 Claude agents 参与移植，并以线上流量作为检验：https://ai-tldr.dev/releases/anthropic-messages-api-rust-migration/

### 仅计数不展开

- video 3 条（Fireship、Two Minute Papers 关于黎曼猜想证明的跟进，以及 Sam Witteveen 本地训练视频）、showcase 1 条（用 Astra 搜系外行星）。

## Agent 用例动态

来自 agentusecases.ai，本窗口新条目 **14** 条（全部列出）。今天的用例仍然集中在编程 agent 做「本来要人点很多次」的事：开云账号、跑 Lighthouse 再改站、做账和报税材料、销售准备；同时出现了更靠近权限与资金的方向——用带 MCP 的钱包让 agent 付款／分账，以及给 agent 虚拟卡去购物、让 Google AI Mode 预填结账。个人事务上，有人用 Grok Bot 查无人认领财产、用 agent 批量改求职信，还有让 agent 代打电话预约医生。与安全／权限相关的放在最前。

### 安全与权限（优先）

- 有人在钱包前加一层 MCP，让 agent 通过聊天付款、收款、分摊聚餐或旅行账，并提到 passkey 授权：https://agentusecases.ai/use-case/send-and-split-money-by-chatting-with-your-ai-agent
- 有评论者用本地 Qwen，加 agents.md 策略，把被拒绝的任务经共享 SQL 任务板升级给前沿模型：https://agentusecases.ai/use-case/route-refused-tasks-between-local-and-frontier-models
- 作者给 agent 一张虚拟借记卡、25 美元预算去买礼物，它能浏览比较并走到结账，但在最后一步遇到困难：https://agentusecases.ai/use-case/have-an-ai-agent-shop-for-a-gift-on-a-25-budget
- 记者给 Google AI Mode 设定目标价格和购买许可，对方打开了预填好的结账页：https://agentusecases.ai/use-case/let-google-ai-mode-find-and-check-out-a-gift

### 编程与运维

- 有人用 Claude Code 办理 AWS 账号开通，想把新手入门流程走顺：https://agentusecases.ai/use-case/create-an-aws-account-with-a-coding-agent
- 有人用带 chrome-devtools-mcp 的 agent 跑 Lighthouse、改站并复测，宣称 Accessibility 达到 100：https://agentusecases.ai/use-case/run-lighthouse-seo-audits-and-fix-a-site-with-an-agent

### 财务与行政

- 一家约 1000 万美元规模公司的两名会计用 Cursor 与 Claude Code 做供应商发票处理：https://agentusecases.ai/use-case/process-vendor-invoices-with-a-bookkeeping-agent
- 有人用 Claude Code／Claude 搭报税材料收集与簿记流程：https://agentusecases.ai/use-case/build-a-tax-document-gathering-and-bookkeeping-workflow

### 研究、求职与生活助理

- 研究者用 Claude Code 找到 1952 年一篇能更好解决其建模子问题的论文：https://agentusecases.ai/use-case/find-a-1952-paper-solving-a-modeling-sub-problem
- 有创始人推销会在后台按姓名搜索无人认领政府资金并协商账单的 agent：https://agentusecases.ai/use-case/find-unclaimed-government-money-and-negotiate-bills
- 有评论者说用 Grok Bot 查无人认领财产，为家人找到了款项：https://agentusecases.ai/use-case/search-unclaimed-property-for-family-members
- 求职者用 Grok Bot 按至少 50% 匹配度的岗位批量改求职信：https://agentusecases.ai/use-case/mass-apply-to-jobs-with-customized-cover-letters
- 销售用 Claude Code 做通话准备、展会流程和客户名单：https://agentusecases.ai/use-case/prep-outbound-sales-work-with-a-coding-agent
- 有用例让 agent 代为致电诊所，预约最早的在网号：https://agentusecases.ai/use-case/call-doctors-offices-and-book-the-earliest-in-network-appointment

## 地址／IoC 汇总

未见公开 IoC。今日条目以漏洞编号、补丁版本、厂商顾问和泄露站声明为主，采集范围内未见到可原样抄录的 C2、样本哈希、钱包地址或攻击基础设施 IP／域名（泄露站点名的受害方官网不属于攻击 IoC，不列入）。DIVD 取证 PDF 可能含调查指标，请直接阅读官方报告，本期不摘录。

## LWiS 固定信源（每日交叉，不替代 X Latest）

# LWiS 固定信源（每日交叉，不替代 X Latest）

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

- X Latest CVE／POC／exploit／0day（recency，窗口约 2 分钟，已加 relevancy 与编号补搜）：查询 (CVE OR POC OR PoC OR exploit OR 0day OR 0-day) -is:retweet lang:en
- X Latest 工具：url:github.com (C2 OR "red team" OR nuclei OR "red-team" OR cobalt OR sliver OR havoc OR "command and control") -is:retweet（14 条，约 21.77 小时）
- X Latest 威胁：("malware analysis" OR "threat report" OR "threat actor" OR ransomware OR "threat intel") -is:retweet（Latest 约 40 分钟；relevancy 约跨 22 小时）
- X LWiS List：list:1239330068461244424 -is:retweet（9 屏，214 条，约 23.14 小时）https://x.com/i/lists/1239330068461244424
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条，48 小时新 sf:id 142，其中 120 条 ZDI 原文已在昨日 sfl 去重；接口 200）
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community （6／7 个源已拉，跳过吾爱破解；48 小时新 3）
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog （11／12 个源已拉，跳过微信公众号；7 天新 0）
- pwn.watch：https://pwn.watch/feed.xml 、https://pwn.watch/feed.json （50 条，本窗口新 0，最新／lastBuildDate 2026-11-10 01:13:32 GMT）
- ExploitGrid exploits：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （200；100 条，48 小时新 0，最新 2026-11-20 19:48:48 UTC）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （200，10 条，未包含今日 Xen Orchestra 与 Danfoss CVE-2025-41450）
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （1805 条，今日新 10）
- CISA 今日警报：https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条，36 小时新 15，security 1）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条，48 小时新 14）
- 阮一峰订阅源已拉取，最新仍为第 420 期（已在 seen_ids，本日非周末不下节）：https://www.ruanyifeng.com/blog/atom.xml

---

**落盘**：Box /home/box/workspace/security-watch/reports/2026-11-25-x-security-digest.md；本机 /Users/kenny1337/Desktop/_05_项目/X安全情报晚报/2026-11-25-x-security-digest.md。
