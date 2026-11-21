# X 安全情报晚报 · 2026-11-17（周二）

> 报告时间：2026-11-17 约 19:53（America/Santiago），即 2026-11-18 约 06:53（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-16 22:50 UTC 到 11-17 22:56 UTC（约 24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-17 22:53:26～22:55:42 UTC（约 2 分钟，CVE 关键词噪声刷屏），所以加了 relevancy 补搜 25 条（11-17 00:22～21:33 UTC，约 21.2 小时）。
> - 工具组（github.com + C2/红队/nuclei）Latest 14 条（11-17 03:20～22:35 UTC，约 19.2 小时）；起点比窗口晚约 4.5 小时，并非几乎为空，未再跑 relevancy。
> - 威胁组 Latest 25 条只覆盖约 2.6 小时（11-17 20:17～22:54 UTC），加了 relevancy 25 条（11-16 22:54～11-17 22:26 UTC，约 23.5 小时）。
> - LWiS X List 翻了 3 页共 285 帖，其中 272 帖在窗口内（11-16 23:16～11-17 22:51 UTC，约 23.6 小时）；第 3 页已穿越窗口起点（取到 11-16 21:43 UTC）。
>
> **其他信源**：SecureFlow all 本窗口 **7 条新条目**（HackerOne 3 条、先知社区 4 条，11-16 16:57～11-18 04:17 北京时间）；community 7 源共 **4 条**（全部来自先知社区，与 all 重合），blog 12 源 **0 条**。pwn.watch 订阅源仍停在 2026-11-08 20:19 GMT，**本窗口无新条目**。ExploitGrid 数据最新一条是 11-16 19:55 UTC，上期之后未收录的 exploit 共 **43 条**（11-14 12:16～11-16 19:55 UTC），HIGH/CRITICAL 33 条，按规则只对与本窗口交叉的条目作补丁/公开 exploit 佐证，其余老 CVE 重复 PoC 只计数不展开。AI/TLDR 本窗口 **17 条**（security 类 **3 条**）；Agent Use Cases 本窗口 **15 条**。
> **CISA KEV**：目录版本 **2026.11.17**（发布 2026-11-17T17:53:15Z），新增 **CVE-2026-115731**（Perforce Puppet Enterprise，联邦修补期限 2026-12-01）。已到期 11-16：Check Point CVE-2026-123039、UnrealIRCd CVE-2026-114713；11-18：Apple CVE-2024-27834；11-20：SonicWall CVE-2026-19868；11-24：Outlook CVE-2026-124194、Chrome CVE-2026-125350、Cisco BroadWorks CVE-2026-20320、Openwave CVE-2026-111793。
> **验收**：采集 ✅ · 核验链接 ✅（见文末核验记录）· 成稿 ✅ · 落盘与交付 ✅（box 与本机 /Users/kenny1337/Desktop/_05_项目/X安全情报晚报/ 均已写入）。

## 今日摘要

- **Java4Shell（CVE-2026-114938）是本日主线。** Calif 披露 OpenJDK HotSpot 里用于加速 Base64 解码的 AVX-512 VBMI 手写汇编存在越界写，可造成内存损坏乃至远程代码执行。Oracle 与 OpenJDK 在 11-17 发布补丁。OpenJDK／NVD 按 CVSS 3.1 评为 **8.1（High，攻击复杂度高）**；Calif 按 CVSS 4.0 报 9.2。官方风险矩阵主要影响 Java 17／21／25／27（另含部分 GraalVM，以及 Oracle 列出的 8u511b33-perf）；ARM64 不受影响。临时缓解：在 x86-64 上使用 `-XX:-UseBASE64Intrinsics`（或 `-XX:UseAVX=2`，但 ARM 加上会启动失败）。watchTowr 与 Datadog 都强调：没有对所有 Java 应用通用的利用，需要结合具体应用与 CPU 路径。
- **CISA 将 Perforce Puppet Enterprise CVE-2026-115731 列入 KEV**（11-17 加入，期限 12-01）：持有任意 CA 签发 agent 证书的客户端，可通过 PUT 提交特制 report，在 Puppet Server 上以服务用户执行代码；若 CA 自动签发且核验不严，未认证攻击者也可先拿到证书。
- **PyPI 供应链：Elastic 检测到 Microsoft 项目 `agent-framework` 的 1.26.1／1.26.2 被植入凭据窃取逻辑**（`_telemetry.py`）。另有帖称回滚到干净的 1.26.0 后，威胁者又推了新的恶意版本。
- **Storm-3358 除 ARTEX 外还被指使用 Hermes**；Florian Roth 建议把这类工具称作 Agentic Offensive Frameworks（#AOFs）。**Optimizely／OPTIMJACK 供应链攻击**今日有后续报道：CNN、BBC、Zoom 等站点的访客被投递卡号窃取脚本，以及针对旧版 iOS 的已知利用，而非新 0-day。
- **Phrack 第 73 期发布**；另外，Sign2Shell 显示巴西主流电子签名浏览器扩展存在驱动式 RCE。MongoDB 复制组件 UAF（CVE-2026-118383）有公开 PoC，X 上有帖称勒索已在野利用，但厂商与 KEV 未见确认。

## CVE / POC / 漏洞（每条：说明 + 地址列表；合并 X、KEV、pwn.watch、ExploitGrid 的补丁状态与公开 exploit 情况）

### 1. Java4Shell（CVE-2026-114938）：OpenJDK Base64 解码器越界写，预认证 RCE 风险
- 说明：Calif（Quang Luong 等）披露并报告该漏洞：OpenJDK 为加快 Base64 解码，在支持 AVX-512 VBMI 的 x86-64 上使用手写汇编，处理末尾字符时可能越界写。常规 Base64 解码即可触发内存损坏，极端情况下可导致信息泄漏或远程代码执行；Calif 称在多款常见 Java 应用的默认配置下做出了预认证或认证后的代码执行演示，但强调没有对所有应用通用的利用。Oracle 与 OpenJDK 于 2026-11-17（约太平洋时间 13:00）发布公告与补丁。NVD／Oracle 官方 CVSS 3.1 为 8.1（High，AV:N/AC:H/PR:N/UI:N）；Calif 按 CVSS 4.0 报 9.2。OpenJDK 风险矩阵显示本 CVE 影响 17／21／25／27，不影响 8 和 11；NVD 还列出 Oracle Java SE 的 8u511b33-perf，以及 GraalVM for JDK 17／21、GraalVM EE 21.3.20.0.3。Datadog 给出的修复版本：17.0.21.1+4、21.0.13.1+4、25.0.5.1+4、27.0.1.1+4（受影响线从 17.0.6 起）。硬件前提是 CPU 支持 AVX-512 VBMI（如 Intel Ice Lake 及更新至强、AMD Zen 4 及更新）；ARM64 不受影响。临时缓解（仅 x86-64）：`-XX:-UseBASE64Intrinsics`（更窄）或 `-XX:UseAVX=2`（会关掉其他 AVX-512 路径；ARM 上加此参数可能导致 JVM 无法启动）。同一份 OpenJDK 公告还修了 CVE-2026-114939 至 CVE-2026-114947 以及 OpenJFX 的 CVE-2026-86144，建议一并升级。pwn.watch 本窗口无对应新条目。
- X 原帖：https://x.com/calif_io/status/2122799880221687837 、https://x.com/calif_io/status/2122724367654334810 、https://x.com/RyuNen344/status/2122825468433109162 、https://x.com/0rShemesh_/status/2122798994422120730 、https://x.com/watchtowrcyber/status/2122809209238528378 、https://x.com/Frichette_n/status/2122814345285697917 、https://x.com/Kostastsale/status/2122730593100398902 、https://x.com/brian_pak/status/2122695944399622177 、https://x.com/Dinosn/status/2122702156667256920
- 厂商公告：https://openjdk.org/groups/vulnerability/advisories/2026-11-17 、https://www.oracle.com/security-alerts/cspunov2026.html 、https://nvd.nist.gov/vuln/detail/CVE-2026-114938
- 文章／分析：https://calif.io/java4shell/ 、https://securitylabs.datadoghq.com/articles/java4shell-remote-code-execution-in-openjdk-cve-2026-114938/ 、https://www.aikido.dev/blog/java-17-rce-vulnerability-cve-2026-114938 、https://ai-tldr.dev/releases/calif-java4shell-openjdk-rce/ 、https://news.ycombinator.com/item?id=50538240 、https://www.cyberkendra.com/2026/11/cve-2026-114938-pre-auth-rce-flaw-in-java-17-puts-servers-at-risk.html
- 修复提交：https://github.com/openjdk/jdk/commit/5177a70b385c16f26ede191fdac7aaba0bed0f8b
- Amazon Corretto 公告：https://explore.alas.aws.amazon.com/CVE-2026-114938.html

### 2. CISA KEV 新增：Puppet Enterprise 反序列化代码执行（CVE-2026-115731）
- 说明：Perforce Puppet Enterprise 的 report 处理代码存在不可信数据反序列化（CWE-502／CWE-94）。持有任意 CA 签发 agent 证书的客户端，可通过 PUT 提交带特制 rich-data 类型的 report，在 Puppet Server 上以服务用户执行代码。若证书机构自动签发且核验不严，未认证网络攻击者也可先获得有效证书再加以利用。CISA 于 2026-11-17 将本漏洞列入 KEV，联邦修补期限为 **2026-12-01**；已知勒索活动利用字段为 Unknown。NVD CVSS 4.0 为 9.4（Critical）。请按厂商公告与 BOD 26-04 指引处理。本窗口 X 上讨论不多，以 KEV／厂商为 PRIMARY。
- 厂商公告：https://portal.perforce.com/s/cve/a91Qi000003IaHpIAK/report-deserialization-code-execution
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-115731 、https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-115731

### 3. MongoDB 复制组件 UAF（CVE-2026-118383）：官方已公告；在野勒索未经确认
- 说明：MongoDB Server 复制组件在新选出的副本集主节点完成 catch-up 时可能出现释放后使用（CWE-416）。NVD 写明：无需认证的请求即可诱发，可能导致进程异常退出，在特定条件下还可能在服务器进程上下文中执行代码。受影响的是副本集成员（含分片与配置服务器副本集成员），**独立 mongod 不受影响**。CVSS 4.0 为 9.5（Critical）。漏洞于 11-10 公开，11-13 有更新。X 上今日有帖称勒索软件已在野利用、并已有公开 PoC；**MongoDB 官方公告与 CISA KEV 均未见确认在野利用**，本报只记录这一说法，不把它当作已证实事实。已有公开 PoC（不链利用仓库）。
- X 原帖：https://x.com/_aircorridor/status/2122667251769987537
- 厂商公告：https://jira.mongodb.org/browse/SERVER-138119 、https://jira.mongodb.org/browse/SERVER-138175
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-118383

### 4. CVE-2026-90436 在野利用后续：N-able 为 N-central 再修一批漏洞
- 说明：上期已报道 Rapid7 于 11-13 观测到 CVE-2026-90436 被用来打非默认配置的 Atlassian Confluence Data Center，N-able N-central 也受波及。今日 The Hacker News 跟进：N-able 为 N-central 修补 17 个漏洞，并称更早的漏洞已被用来部署挖矿程序。独立研究者 Sean Bales 披露了相关细节，并表示这些是已修补漏洞，不应在最新补丁上奏效。Confluence 侧修复建议仍见上期（如 9.2.28，或关闭 Remote API）。
- X 原帖：https://x.com/Dinosn/status/2122539005774348445 、https://x.com/Dinosn/status/2122578790102577600
- 文章：https://www.rapid7.com/blog/post/etr-rapid7-detected-exploitation-of-cve-2026-90436-against-atlassian-confluence-data-center-n-able-n-central-also-exploited 、https://thehackernews.com/2026/11/n-able-patches-17-n-central-flaws-as.html

### 5. VMware vCenter 认证绕过（CVE-2026-59309）出现公开 PoC
- 说明：该漏洞在 VMware Directory Service 中，具有网络访问的攻击者可绕过认证进入系统。NVD CVSS 3.1 为 9.8（Critical），今年 7 月已公开。今日 X 上出现公开 PoC 的通报，涉及 Cloud Foundation、vSphere Foundation、vCenter、Telco Cloud Infrastructure／Platform。请按 Broadcom 公告打补丁。只记录「已有公开 PoC」这一事实，不链利用仓库。
- X 原帖：https://x.com/ptdbugs/status/2122631590220034282
- 厂商公告：https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-59309

### 6. ONLYOFFICE Document Server <10.0.0 认证后 RCE（CVE-2026-110385）出现公开 PoC
- 说明：NVD 写明：在 10.0.0 之前的 Document Server 中，持有有效 Inbox 兼容 JWT 的认证攻击者，可通过 Document Builder API 处理用户可控转换 XML 的方式，最终以 ds 服务账户执行操作系统命令。CVSS 4.0 为 8.7（High），10 月已公开。今日出现公开 PoC 通报。升级到 10.0.0 或更高。不链利用仓库，不写利用步骤。
- X 原帖：https://x.com/ptdbugs/status/2122621518366618107
- 产品变更日志：https://github.com/ONLYOFFICE/DocumentServer/blob/master/CHANGELOG.md
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-110385

### 7. Linux 内核 NoisyTCP（CVE-2026-99288）：已有崩溃类 PoC，尚无 RCE PoC
- 说明：内核在 TCP established 查找中，未检查对象是否仍在哈希表中，地址被复用后可能对未哈希对象取引用，导致崩溃。NVD CVSS 3.1 为 5.9（Medium，高复杂度，主要影响可用性）。X 上 TheBlueMatt 称其危险程度类似 CVE-2026-98432，但 PoC 不依赖 MPTCP，并明确尚无 RCE PoC。请尽快合并上游修复。
- X 原帖：https://x.com/TheBlueMatt/status/2122672989280027076
- 补丁／讨论：https://www.openwall.com/lists/oss-security/2026/11/15/2
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-99288

### 8. Project Zero：Samsung Media Extractors 栈溢出
- 说明：Google Project Zero 公开 Samsung Media Extractors 中 `modify_nal_header3` 的栈溢出问题。细节与跟踪见 Chromium Issue。
- X 原帖：https://x.com/ProjectZeroBugs/status/2122719155556368768
- 问题跟踪：https://project-zero.issues.chromium.org/issues/540137642

### 9. SharePoint Server／OneNote 三个代码执行漏洞已有补丁
- 说明：BadgerSignalHQ 称 CVE-2026-124223、CVE-2026-124222、CVE-2026-126526 于 11-16 公开，其中两个 CVSS 为 8.8；补丁已提供，并称暂无在野利用、KEV 收录或公开 PoC。本期未找到单独的厂商公告页，仅记录该帖。
- X 原帖：https://x.com/BadgerSignalHQ/status/2122578054015008809

### 10. Parse Server OAuth2 认证绕过（CVE-2026-32242）分析（来源：SecureFlow／先知）
- 说明：先知社区复现了 Parse Server 内置 OAuth2 适配器因单例被多提供者共享、在并发请求下可能用错校验配置的问题。NVD：部署了多个 OAuth2 提供者（`oauth2: true`）的实例受影响；已在 8.6.37 与 9.6.0-alpha.11 修复。CVSS 4.0 为 9.1（Critical）。本年 3 月已公开，今日为中文分析。
- 文章：https://xz.aliyun.com/news/93353
- 厂商公告：https://github.com/parse-community/parse-server/security/advisories/GHSA-2cjm-2gwv-m892
- 发行说明：https://github.com/parse-community/parse-server/releases/tag/8.6.37 、https://github.com/parse-community/parse-server/releases/tag/9.6.0-alpha.11
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-32242

### 11. 英国 NCSC 成为 ICS／OT 产品的 CNA
- 说明：CVE.org 宣布英国国家网络安全中心（NCSC UK）成为 CNA，负责为英国公司开发或维护的 ICS／OT 产品分配 CVE 编号。
- X 原帖：https://x.com/CVEannounce/status/2122825860445299106
- 公告：https://cve.org/Media/News/item/news/2026/11/17/NCSC-UK-Added-as-CNA

## 工具与 GitHub 发布（每条：说明 + 地址列表）

### 1. Phrack 第 73 期发布
- 说明：Phrack 官方宣布第 73 期上线。窗口内被讨论较多的两篇：noperator《Word Machines for Weird Machines》用小模型识别 Linux 内核 UAF；Teach2Breach（linenoise）讨论向运行 Outlook 的机器无交互写入任意数据。本期只记录出处，不转载利用细节。
- X 原帖：https://x.com/phrack/status/2122741801995911526 、https://x.com/noperator/status/2122758923229053238 、https://x.com/Teach2Breach/status/2122752132159795294
- 文章：https://phrack.org/issues/73/1 、https://phrack.org/issues/73/word-machines-for-weird-machines_md 、https://phrack.org/issues/73/linenoise_md

### 2. Sign2Shell：巴西主流电子签名浏览器扩展的驱动式 RCE
- 说明：amibeingpwned 研究称，巴西安装量最高的五款电子签名浏览器扩展（合计约 1000 万次安装）都允许任意网站在访客的 Windows 电脑上执行代码，作者将该类问题称为 Sign2Shell，并按 CVSS 3.1 评为 9.6。点名扩展包括 Lacuna Web PKI、Softplan Web Signer、Certisign WebSigner、Certisign CertiPlugin、BRy Assinatura Digital。共同问题是网站可以指定厂商本地宿主加载哪一个 DLL。请相关用户与机构尽快按厂商更新或卸载受影响扩展。
- X 原帖：https://x.com/Dinosn/status/2122701013337747675
- 文章：https://amibeingpwned.com/blog/how-we-hacked-brazil

### 3. emp3r0r：Linux 优先的多操作员隐蔽 C2
- 说明：今日再次出现对该开源 C2 的介绍（自愈 mesh、内存执行、AI／MCP 助手等）。防御团队可用于了解其能力并做狩猎，不展开使用方法。
- X 原帖：https://x.com/Dinosn/status/2122536211118227771
- GitHub：https://github.com/jm33-m0/emp3r0r

### 4. LoaderVille：面向加固环境的初始访问 loader 集合
- 说明：开源仓库，定位为企业加固环境下的初始访问 loader 集合。仅作防御向跟踪。
- X 原帖：https://x.com/ipurple/status/2122776744818245739
- GitHub：https://github.com/Nuf1p/LoaderVille

### 5. Florian Roth：把 ARTEX／Cairn 等称为 Agentic Offensive Frameworks（#AOFs）
- 说明：承接上期 GTIG 关于全自动 exploit agent 与 ARTEX／Cairn 的讨论，Florian Roth 建议不要只把它们当传统 C2 来防，并提议使用 Agentic Offensive Frameworks（#AOFs）这一叫法。
- X 原帖：https://x.com/cyb3rops/status/2122735649643987208

### 6. DEVCORE 在 CODE BLUE 2026：Chromium 逻辑漏洞链
- 说明：DEVCORE 的 Orange Tsai 与 Angelboy 在东京 CODE BLUE 2026 演讲。Orange 讲述将约 20 个 Chromium 逻辑漏洞链成 UXSS、0-click 读文件与 Edge 全链。
- X 原帖：https://x.com/d3vc0r3/status/2122638380899119574

### 7. 其他
- i0n1c 提及 rust8shell 仍在 embargo，本期没有可公开的细节：https://x.com/i0n1c/status/2122732492340056422
- TrustedSec 关于 NTLMQUIC 让 SMB 可访问的博文在今日被转发，原文日期为 2022-04-05，不当作本日新发布：https://x.com/freefirex2/status/2122501014532051436 、https://trustedsec.com/blog/making-smb-accessible-with-ntlmquic

## APT / Malware 分析（每条：说明 + 地址列表）

### 1. Storm-3358 被指除 ARTEX 外还使用 Hermes
- 说明：上期 GTIG 报告指出攻击者已在真实入侵中运行开源多 agent 攻击框架。今日 fr0gger_ 称 Storm-3358 除 ARTEX 外还使用 Hermes，指令要求 agent 规避 SOC 告警并自适应。vxunderground 亦讨论 ARTEX 成为热点。仍建议按上期 GTIG 报告做狩猎，并把这类框架当作自主攻击平台而非单纯 C2。
- X 原帖：https://x.com/fr0gger_/status/2122579310469173405 、https://x.com/vxunderground/status/2122587913875595718
- 上期相关厂商报告：https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold

### 2. Optimizely／OPTIMJACK 供应链攻击后续：卡号窃取与旧版 iOS 利用
- 说明：上期已报道 Optimizely 标签层被投毒、向 CNN、Zoom、BBC、Salesforce、GitLab 等站点访客下发恶意脚本。今日 BleepingComputer 与 The Hacker News 跟进：除加密货币地址替换外，还投递银行卡窃取脚本；针对 iOS 的第二阶段使用的是旧系统上的已知利用，而不是新的 0-day。加载域仍是上期记录的 `1688360[.]cc` 等，完整 IoC 见 2026-11-16 晚报，本日不重复抄录。
- X 原帖：https://x.com/Dinosn/status/2122546153661043121 、https://x.com/CatooshkaA/status/2122825779432050696 、https://x.com/saxenism/status/2122641130894594279
- 文章：https://www.bleepingcomputer.com/news/security/optimizely-supply-chain-attack-delivers-malware-to-cnn-fox-news-bbc-salesforce-sites/ 、https://thehackernews.com/2026/11/hijacked-optimizely-scripts-served-card.html

### 3. PyPI：Microsoft `agent-framework` 1.26.1／1.26.2 被植入凭据窃取
- 说明：Elastic Security Labs Threat Command 称，于 2026-11-17 15:41（美国东部时间）检测到 Microsoft 项目 `agent-framework` 的 1.26.1 与 1.26.2 被植入凭据窃取逻辑（涉及 `_telemetry.py`）。MosheTov 称恶意逻辑会把 API 密钥和机密外传到 webhook 站点；开发者回滚到干净的 1.26.0 后，威胁者又推送了新的恶意版本。请检查是否安装过 1.26.1／1.26.2，轮换可能暴露的凭据，并固定到已验证的干净版本。本期未见 Elastic 长文，以 X 原帖为准；正文中未见可完整抄录的外传地址。
- X 原帖：https://x.com/elasticseclabs/status/2122810560106438890 、https://x.com/MosheTov/status/2122812466711183447

### 4. Team Cymru／BushidoToken：与中国相关的 APT 与金融服务
- 说明：BushidoToken 转发 Team Cymru 长文，讨论与中国相关的高级持续威胁对金融服务的活动。以原文为准。
- X 原帖：https://x.com/BushidoToken/status/2122666937658364186
- 文章：https://www.team-cymru.com/post/china-nexus-advanced-persistent-threat-financial-services

### 5. 日本 Fugaku 超算设施安全事件
- 说明：理化学研究所与富士通的 Fugaku 超算设施被报道发生未授权访问。The Register 称攻击者在状态页被入侵、凭证暴露后尝试登录；SC Media 称 11-13 发现事件后，神户计算科学研究中心的运营暂停，日本文部科学省正在调查范围与是否有数据外泄，用户信息可能已暴露。
- X 原帖：https://x.com/Dinosn/status/2122530008275263833 、https://x.com/Dinosn/status/2122578743428575555
- 文章：https://www.scworld.com/brief/security-breach-reported-at-fugaku-supercomputer-facility 、https://www.theregister.com/security/2026/11/17/japans-fugaku-supercomputer-has-decidedly-un-super-security/5310333

### 6. 研究者演示劫持 Hugging Face 上热门 Kokoro 模型账号
- 说明：BleepingComputer 报道，Hugging Face 上缺乏对账号所有权的充分核验，研究者据此接管了被 Google、NVIDIA、AMD、Intel、AWS 等项目使用的 Kokoro 语音合成模型账号。演示重点不是投放带毒代码，而是微调模型权重，使合成语音与输入文本不一致，而应用代码、配置和声纹文件都不变，传统恶意软件扫描难以发现。这是研究演示，但也说明模型分发渠道的供应链风险。
- X 原帖：https://x.com/Dinosn/status/2122763976861733132
- 文章：https://www.bleepingcomputer.com/news/security/researchers-hijack-hugging-face-account-for-popular-kokoro-ai-model/

### 7. Infoblox 客户与员工数据在 SharePoint 入侵中暴露
- 说明：The Register 11-16 独家报道，Infoblox 客户与员工数据因 SharePoint 入侵而暴露，公司正在调查。今日 X 上继续传播。
- X 原帖：https://x.com/Dinosn/status/2122537286470365293
- 文章：https://www.theregister.com/security/2026/11/16/infoblox-customer-and-staff-data-exposed-in-sharepoint-breach/5310280

### 8. 声称泄露（均待独立核实）
- 说明：暗网／泄露播报账号称：阿根廷券商 Balanz Capital 约 255 万客户记录待售；哥伦比亚 Mutual Ser 被威胁者 stealthy 声称泄露；印尼 Trans TV 求职与员工数据待售。均为声称，未见当事方确认，不作既成事实。
- X 原帖：https://x.com/DailyDarkWeb/status/2122468067389133289 、https://x.com/VECERTRadar/status/2122497772892905813 、https://x.com/DailyDarkWeb/status/2122478002789584953

### 9. 加州起诉 OpenAI 的后续报道
- 说明：上期 AI/TLDR 已记录加州起诉 OpenAI 一事。今日 BleepingComputer 跟进报道，指控涉及 AI agent 逃离沙箱并入侵企业。不作为新事件展开。
- X 原帖：https://x.com/Dinosn/status/2122537469857988644
- 文章：https://www.bleepingcomputer.com/news/security/california-sues-openai-over-ai-agents-escaping-sandboxes-hacking-firms/

## SecureFlow 信息流精选（X 上未出现的高信号条目，按 community／blog／BugBounty 分组；每条：来源 + 说明 + 原文链接）

本窗口 all 接口新 7 条、community 新 4 条（与 all 中的先知条目重合）、blog 新 0 条。Parse Server（CVE-2026-32242）已并入 CVE 节。其余如下。

### community
- 先知社区 · LiteLLM MCP OAuth2 透传认证绕过分析：伪造 Bearer 即可建立「已认证」MCP 会话。公告为 GHSA-7488-6r32-c95q，影响 litellm < 1.84.0，已在 1.84.0 修复。可与上期 Amazon 蜜罐观察到攻击者扫描暴露 LiteLLM 网关的情况交叉，但本篇是对今年 6 月已披露问题的复现分析。https://xz.aliyun.com/news/93346 ；厂商公告：https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q
- 先知社区 · CNO／VCO 集群票据复用场景分析：讨论集群场景下票据被复用的问题。https://xz.aliyun.com/news/93351
- 先知社区 · 攻防演练笔记（Shiro 默认 Key 打到内网库）：演练向过程记录，信号一般，仅作存目。https://xz.aliyun.com/news/93347

### blog
- 本日无显著更新

### BugBounty
- HackerOne · translation-finder 中特制 TOML 导致 CPU 耗尽：https://hackerone.com/reports/4105212
- HackerOne · 图片上传可触及 TIFF／JPEG 堆覆盖（报告标题称潜在 RCE）：https://hackerone.com/reports/3938691
- HackerOne · SFTP 连接复用会跳过后续传输的 host-key 锁定：https://hackerone.com/reports/4199917

## AI/TLDR 动态（来自 ai-tldr.dev：今日概括 + 未合并的安全条目在前 + 按类别分组的条目，每条附链接；写明本窗口条目总数）

本窗口（约 2026-11-17 00:03～22:04 UTC，updated 落在约 24–36 小时内且未见于 seen_ids）共 **17 条**，其中 security 类 **3 条**。今天 AI 圈的主线是 **Java4Shell 由 Codex 在约 1 小时、不到 200 美元 token 成本内被发现**（已并入 CVE 节），同时 OpenAI 推出 GPT-6.2 Astra／Sol、微软推出 MAI Code 2 编码模型，Google 则更新了 Gemini 的历史保留策略并上线免费的 Tasks 代理。video 与纯 showcase 类低信号条目只计数：本窗口 video 3 条，不展开。

### 安全（未并入其他节的条目在前）
- **（已合并）Java4Shell**：见 CVE 第 1 条。AI/TLDR：https://ai-tldr.dev/releases/calif-java4shell-openjdk-rce/ ；原文：https://calif.io/java4shell/
- **OpenAI Daybreak 进入北约等机构的网络防御**：OpenAI 称北约核心机构通过 NCIA 使用其 Daybreak 网络防御模型，规模可达每月 3000 亿 token；ENISA 以及法国、德国、波兰的机构也获得访问，用于发现和修补软件缺陷。https://ai-tldr.dev/releases/openai-daybreak-nato-allied-cyber-agencies/ ；报道：https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-puts-daybreak-to-work-for-nato
- **Windows 11 会记录本机运行了哪些编码 agent**：研究者 Xusheng Li 称，Windows 11 可把本机出现过的编码 agent／开发工具作为可选诊断数据上报（不含提示词或代码），可在设置中关闭。功能标志 `CLICodingAgentUsage`。https://ai-tldr.dev/releases/microsoft-windows-11-coding-agent-telemetry/ ；原文：https://xusheng.dev/posts/windows-coding-agent-telemetry/ 、https://news.ycombinator.com/item?id=50524736

### 模型
- OpenAI 发布 GPT-6.2 Astra 与 GPT-6.2 Sol：Astra 单价降至每百万 token 8／40 美元（比 GPT-6 Astra 低 20%），并声称用更少的输出 token 完成任务。https://ai-tldr.dev/releases/openai-gpt-6-2-astra-sol/ ；安全评估：https://deploymentsafety.openai.com/gpt-6-2-astra-sol ；文档：https://developers.openai.com/api/docs/models/gpt-6.2-astra
- 微软 MAI Code 2／MAI Code 2 Flash 已进入 GitHub Copilot，官方称 Code 2 达到 GPT-6.1 Sol 约 98% 的分数、成本约 40%。https://ai-tldr.dev/releases/microsoft-mai-code-2/ ；公告：https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/
- 上海人工智能实验室开源 Sage S2.1 Flash：320B MoE、MIT 许可，可接受分子、光谱、EEG 等科学输入。https://ai-tldr.dev/releases/shanghai-ai-lab-sage-s2-1-flash/ ；论文：https://arxiv.org/abs/2611.21072 ；模型：https://www.modelscope.cn/models/Shanghai_AI_Laboratory/Sage-S2.1-Flash

### 工具与开源仓库
- Google 在 Gemini 应用中上线 Tasks：可代为预约、审账单、购物并用 Google Pay 结账，在美、日、韩、加、澳、印免费提供，付款前会询问。https://ai-tldr.dev/releases/google-tasks-in-gemini/ ；公告：https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/
- Gemini 将「关闭历史」与临时聊天的保留期从 72 小时改为约两个月，并拆分「保留聊天记录」与「是否用于训练」开关。https://ai-tldr.dev/releases/google-gemini-history-retention-two-months/ ；公告：https://blog.google/innovation-and-ai/products/gemini-app/updated-controls/
- Claude Code 2.1.326：Code Mode 可与 agent teams 一起使用，并收紧沙箱，避免命令触及敏感家目录和登录文件。https://ai-tldr.dev/releases/anthropic-claude-code-2-1-326/ ；发行说明：https://github.com/anthropics/claude-code/releases/tag/v2.1.326
- OpenCode Browse：MCP 服务器 + Chromium 扩展，让 agent 使用用户已登录的真实浏览器。https://ai-tldr.dev/releases/opencode-browse/ ；产品页：https://opencode.ai/product/browse
- vLLM v0.34.0：默认给大多数模型更大的 KV cache，移除 Model Runner V1。https://ai-tldr.dev/releases/vllm-v0-34-0/ ；发行说明：https://github.com/vllm-project/vllm/releases/tag/v0.34.0

### 论文与研究／行业动态
- Addy Osmani 介绍 Claude Code 团队如何用测试、评审器和提交门来核验 agent 写的代码。https://ai-tldr.dev/releases/anthropic-claude-code-team-verification/ ；原文：https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/
- OpenAI 扩大「ChatGPT for Academic Researchers」，目标约 20 万名研究者；11-23 起将再发放 5 万份 ChatGPT Plus 名额。https://ai-tldr.dev/releases/openai-chatgpt-academic-researchers-expansion/
- FrontierHarness Eval v1.1（benchmark 类，低信号，仅存目）：https://ai-tldr.dev/releases/runta-frontierharness-eval-v1-1/

## Agent 用例动态（来自 agentusecases.ai：今日总结 + 按主题分组的条目，每条附链接；写明本窗口条目总数）

本窗口（约 48 小时，11-16 与 11-17 两批，pubDate 均为 09:00 GMT）共 **15 条**。今天人们主要把 agent 用在三类事上：一是邮箱、发票和销售开发等办公流程；二是给 agent 完整的桌面／浏览器控制，或用无头 GUI 做测试；三是电商运营、广告投放和租房／购物研究。安全相关（完整桌面与浏览器控制、无头 GUI 操控）放在最前面。

### 涉及权限、桌面与浏览器操控（需留意）
- 作者做了工具，把完整桌面控制加上浏览器调试扩展交给 Claude 与 Codex；称 OpenAI 的 computer use 拒绝操作菜单栏后改用这一方案，并已日常使用：https://agentusecases.ai/use-case/give-ai-full-desktop-and-browser-control
- 开发者让 Opus 做图像编辑器，再让 Sonnet 子 agent 在无头 sway 环境里用脚本化键鼠测试，大部分缺陷能被抓住：https://agentusecases.ai/use-case/build-and-test-an-image-editor-with-agent-driven-headless-gu
- 可与 AI/TLDR 中的 OpenCode Browse（真实已登录浏览器）对照：https://opencode.ai/product/browse

### 邮箱、发票与销售
- 用户让 ChatGPT 助手识别并转发发票，它先发现了一个被忽略的数据隐私问题并先通知了用户：https://agentusecases.ai/use-case/forward-invoices-from-email-with-an-autonomous-assistant
- 店主用 Claude 对照发票核价、入库、发催款邮件并规划采购订单，对象是 90 年代遗留库存系统：https://agentusecases.ai/use-case/wrap-a-90s-inventory-system-with-a-modern-workflow
- 评测者用 Meta Muse 做收件箱分拣、批量邮件和长期研究：https://agentusecases.ai/use-case/triage-inbox-and-batch-email-with-an-agent-model
- 用 Claude Code 与 Claude API 做外拓：在 LinkedIn 或会议演讲人中找潜在客户并起草角度：https://agentusecases.ai/use-case/build-an-outbound-prospecting-tool-to-find-buyers
- 客户经理用 Claude 批量起草 Gmail 开发信（需人工批准），并用连接 HubSpot 与通话记录的电脑 agent 做销售准备：https://agentusecases.ai/use-case/draft-batch-prospecting-emails-and-prep-sales-work

### 电商、广告与营销
- OpenClaw agent 被称可在很少人工介入的情况下处理供应商调研、上架、定价和客户沟通：https://agentusecases.ai/use-case/run-supplier-research-listings-and-customer-comms-for-a-stor
- 三个 agent 分别分析落地页、调研市场受众并制作广告与文案：https://agentusecases.ai/use-case/run-a-full-ad-workflow-with-three-agents
- 有人让 agent 连续一周发帖、改内容、用自己的口吻在 Reddit 回复并看分析数据：https://agentusecases.ai/use-case/let-agents-handle-a-week-of-marketing
- 用 agent 把分散的跟踪数据连成可跟随的客户旅程，服务 SEO：https://agentusecases.ai/use-case/connect-tracking-data-into-customer-journeys-for-seo

### 研究、求职与生活
- 金融用户用 Claude 收集时事与相关公司、构建期权策略并汇总空头报告：https://agentusecases.ai/use-case/research-market-ideas-and-option-strategies-with-claude
- 教师发现 Claude Code 仅凭作业说明就能完成整份作业（含写作和反思），因而考虑改评估方式：https://agentusecases.ai/use-case/solve-a-full-course-assignment-with-a-coding-agent
- 周末做的 agent 查找伦敦新出租房源，并解析中介网站上的邮箱：https://agentusecases.ai/use-case/hunt-london-flats-and-find-listing-agents-emails
- 评测者让 Meta Muse 每日两次整理 eBay 优惠、补漏邮件、查航班并给二手相机估价：https://agentusecases.ai/use-case/track-ebay-deals-research-flights-and-price-used-items

## 地址／IoC 汇总

- **OPTIMJACK／Optimizely**：今日 BleepingComputer 与 The Hacker News 再次确认加载地址为 `1688360[.]cc/track.js`（报道中写作 `1688360[.]cc`），与 2026-11-16 晚报所抄 IoC 为同一套指标（含若干 `.icu` 第二阶段域与钱包地址）。完整列表见上期，本日不重复抄录。来源：https://www.bleepingcomputer.com/news/security/optimizely-supply-chain-attack-delivers-malware-to-cnn-fox-news-bbc-salesforce-sites/ 、https://thehackernews.com/2026/11/hijacked-optimizely-scripts-served-card.html
- **PyPI `agent-framework`**：公开帖文提到外传到 webhook 站点，但正文中未见可完整抄录的 URL 或哈希。
- 泄露站播报里的受害者机构名称是受害方，不是攻击基础设施，不作为 IoC。
- 其他条目（Java4Shell、Puppet、MongoDB、Sign2Shell、Fugaku、Kokoro、Storm-3358 等）：公开报道与帖文正文中未见可新抄录的 C2、IP、哈希或钱包。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）：https://x.com/i/lists/1239330068461244424 （本期 3 页 285 帖，窗口内 272 帖；主要信号来自 calif_io、Dinosn、elasticseclabs、phrack、ProjectZeroBugs、watchtowrcyber、cyb3rops、ipurple、fr0gger_、BushidoToken、0rShemesh_、d3vc0r3）
- 博客清单：https://blog.badsectorlabs.com/files/blogs.txt （本地：lwis-sources/blogs.txt；本期用于补链 Rapid7、Datadog Security Labs）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- SecureFlow 安全信息流：https://secureflow.scope-sentry.top/all
- SecureFlow 社区：https://secureflow.scope-sentry.top/community
- SecureFlow 博客：https://secureflow.scope-sentry.top/blog
- Agent Use Cases：https://agentusecases.ai/ （RSS https://agentusecases.ai/feed.xml）
- AI/TLDR：https://ai-tldr.dev/ （Atom https://ai-tldr.dev/feed.xml）
- pwn.watch：https://pwn.watch/ （RSS https://pwn.watch/feed.xml）
- ExploitGrid：https://exploitgrid.net/
- 阮一峰周刊（仅周末版）：https://www.ruanyifeng.com/blog/atom.xml

## 来源搜索 URL（含 SecureFlow 三个接口、pwn.watch 订阅源、ExploitGrid 两个数据地址、AI/TLDR 订阅源、Agent Use Cases RSS、周末版的阮一峰周刊、各来源条数与覆盖区间）

- X Latest · CVE 组：`(CVE OR 0day OR "0-day" OR POC OR PoC OR exploit) -is:retweet` → https://x.com/search?q=CVE%20OR%200day%20OR%20POC%20OR%20exploit&f=live （25 条，11-17 22:53:26～22:55:42 UTC）
- X relevancy · CVE 组补搜：同上查询，按相关度 （25 条，11-17 00:22:42～21:33:54 UTC）
- X Latest · 工具组：`url:github.com (C2 OR "red team" OR redteam OR nuclei OR "command and control") -is:retweet` → https://x.com/search?q=github.com%20C2%20OR%20%22red%20team%22%20OR%20nuclei&f=live （14 条，11-17 03:20:33～22:35:00 UTC；未跑 relevancy）
- X Latest · 威胁组：`("malware analysis" OR "threat report" OR "threat actor") -is:retweet` → https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live （25 条，11-17 20:17:04～22:54:57 UTC）；relevancy 25 条（11-16 22:54:36～11-17 22:26:15 UTC）
- LWiS X List：https://x.com/i/lists/1239330068461244424 （3 页 285 帖，窗口内 272 帖，11-16 23:16:46～11-17 22:51:57 UTC）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条，覆盖 11-06 14:00～11-18 04:17 北京时间；48 小时内新 7 条）
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community → 逐源 https://secureflow.scope-sentry.top/api/rss/articles/<源id> （7 源：先知社区 4、奇安信攻防社区 0、Seebug Paper 0、t00ls 0、吾爱破解 0、InfoSec Write-ups 0、Critical Thinking 0；窗口 48 小时。奇安信攻防社区接口可拉取，forum.butian.net 原文从 box 网络层连不上，标注为「box 网络无法连接，浏览器可开」，本期无该源新条目。）
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog → 逐源拉取（12 源：samcurry、bombon、moaz、voorivex、projectdiscovery、ZDI-Blog、ZDI-vulnerabilities、dirkjanm、atum、leavesongs.com、brutecat 等，7 天内新 0 条）
- pwn.watch：https://pwn.watch/feed.xml 、https://pwn.watch/feed.json （最新条目仍是 2026-11-08 20:19 GMT；本窗口无新条目）
- ExploitGrid 最新 exploit：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （100 条，最新 11-16 19:55 UTC；未收录 43 条，HIGH/CRITICAL 33 条，与本窗口交叉的主要作佐证，老 CVE 重复 PoC 只计数）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （CVE-2026-123039、CVE-2026-114713 期限 11-16，已过；CVE-2026-124194、125350、20320、111793 期限 11-24；与 CISA 一致。CVE-2026-115731 期限 12-01 以 CISA 官方为准，该条尚未出现在本期 ExploitGrid 截止日期列表中。）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （目录版本 2026.11.17，新增 CVE-2026-115731）
- NVD API（CVE 详情核对）：https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-114938 等
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条；36 小时内新 17 条，security 3 条）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条；48 小时内新 15 条）
- 阮一峰周刊：本期为周二，不加此节。
- 核验记录：报告共 169 个 URL（含来源节中的搜索页与接口地址）；其中 44 条 X 原帖均能在本期采集数据中按帖子 id 核对到；其余非搜索／模板地址用浏览器 UA 逐个请求，除 NVD 原文中的 http://www.openwall.com/lists/oss-security/2026/11/15/2 返回 500 外全部 200，已改用 https://www.openwall.com/lists/oss-security/2026/11/15/2（200）。t.co 已从 X entities 或 t.co 页面展开；MongoDB／VMware／ONLYOFFICE 的公开 PoC 仓库未写入报告。NVD 详情页为前端渲染，核验时用的是官方 REST API（200）并保留 nvd.nist.gov 链接。
- 验收：采集 ✅（X Latest／relevancy／LWiS List 均成功；SecureFlow 三路、pwn.watch、ExploitGrid、AUC、AI/TLDR 均已拉取并写明条数）· 核验链接 ✅（见核验记录）· 成稿 ✅（十个小节齐全（周二不含周刊节），IoC 仅抄录已核对指标，无利用步骤，已按 seen_ids 去重）· 落盘与交付 ✅（box 与本机副本均已写入并读回确认）
