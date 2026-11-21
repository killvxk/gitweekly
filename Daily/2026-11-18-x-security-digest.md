# X 安全情报晚报 · 2026-11-18（周三）

> 报告时间：2026-11-18 约 19:58（America/Santiago），即 2026-11-19 约 06:58（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-17 22:50 UTC 到 11-18 23:05 UTC（约 24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-18 23:01:27～23:03:51 UTC（约 2 分钟，CVE 关键词噪声刷屏），所以加了 relevancy 补搜 25 条（11-17 23:08～11-18 21:07 UTC，约 22.0 小时），以及一组补丁／公告关键词补搜 25 条（11-17 23:06～11-18 22:18 UTC，约 23.2 小时）。
> - 工具组 Latest 11 条覆盖 11-17 23:44～11-18 23:01 UTC（约 23.3 小时，距窗口起点约 54 分钟；第 2 页为空），未再做 relevancy 补搜。
> - 威胁组 Latest 25 条只覆盖 11-18 21:36～23:03 UTC（约 1.5 小时），relevancy 补搜 25 条覆盖 11-17 23:32～11-18 22:09 UTC（约 22.6 小时）。
> - LWiS List 共 4 页、拉取 381 条，其中窗口内 308 条，覆盖 11-17 22:50:37～11-18 23:01:16 UTC（约 24.2 小时）；第 4 页已越过窗口起点（最旧拉到 11-17 18:28 UTC）。
> **其他信源**：SecureFlow 的 all／community／blog 三路接口在首次拉取及随后多次重试（浏览器 UA + 站点 Referer）中均返回 **HTTP 522**（源站不可用），**本窗口未能拉取新条目**，条数记为失败而非 0。pwn.watch 订阅源仍停在 2026-11-08 20:19 GMT，**本窗口无新条目**。ExploitGrid 上期之后未收录、且 date 落在约 48 小时窗口内的 exploit 共 **19 条**（11-17 07:41～19:16 UTC），其中 HIGH／CRITICAL 13 条；按规则只对与本窗口交叉的条目作补丁／公开 exploit 佐证，其余老 CVE 重复 PoC 只计数不展开。AI/TLDR 本窗口 **19 条**（security 类 **3 条**）；Agent Use Cases 本窗口 **32 条**（节内精选代表性条目）。本期为周三，不加阮一峰周刊节。
> **CISA KEV**：目录版本 **2026.11.18**（发布 2026-11-18T19:17:41Z），今日新增 4 条：CVE-2024-10441（Synology DSM／BeeStation，联邦修补期限 2026-11-21）、CVE-2026-40217（BerriAI LiteLLM，期限 2026-12-02）、CVE-2026-90817（REDCap，期限 2026-11-21）、CVE-2026-90436（Apache Axis 1.x，期限 2026-11-21）。已到期或临近：11-16 Check Point CVE-2026-123039、UnrealIRCd CVE-2026-114713；**11-18（今日）Apple CVE-2024-27834**；11-20 SonicWall CVE-2026-19868；11-24 Outlook CVE-2026-124194、Chrome CVE-2026-125350、Cisco BroadWorks CVE-2026-20320、Openwave CVE-2026-111793；12-01 Puppet CVE-2026-115731。
> **验收**：采集 ⚠️（X Latest／relevancy／LWiS List、pwn.watch、ExploitGrid、AUC、AI/TLDR、KEV 均已拉取并写明条数；**SecureFlow 三路持续 522，未通过「三路都已拉取」这项**）· 核验链接 ✅（见文末核验记录）· 成稿 ✅（十个小节齐全，周三不含周刊节）· 落盘与交付 ✅（box 与本机 /Users/kenny1337/Desktop/_05_项目/X安全情报晚报/ 均已写入）。

## 今日摘要

- **今日主线是 nginx 补丁日（nginx2root）。** F5／nginx 发布 1.31.9（主线）与 1.30.7（稳定版），一次性修复多枚缺陷。Wiz 与 Xint 等团队重点披露其中两枚 **HTTP/2 预认证内存破坏、可导致远程代码执行** 的漏洞：CVE-2026-123007（官方标 major；Wiz CVSS 4.0 为 9.2）和 CVE-2026-123633（官方标 medium，Wiz 同样给 9.2）。官方顾问页上同期还有 HTTP/3、resolver、mail 代理、TLS 1.3 请求体等条目。临时缓解是关闭 HTTP/2，但不能覆盖全部缺陷，仍应升级。Wiz、Xint、Rapid7、Ikotas Labs、Metnir 各自独立发现并与 F5 协调于 11-18 公开。
- **CISA KEV 一次新增 4 条，其中 3 条联邦期限是 11-21（后天）。** Synology DSM／BeeStation 的 CVE-2024-10441（CVSS 9.8，2024 年已有厂商公告，今日确认在野利用）、Vanderbilt REDCap 的 CVE-2026-90817（未认证代码执行，需知道有效公开调查 hash）、以及 **Apache Axis 1.x** 的 CVE-2026-90436（SOAP Fault 反序列化／不安全反射，产品已 EOL）。另外把 LiteLLM 的沙箱逃逸 CVE-2026-40217 列入 KEV，期限 12-02。
- **新加坡 CSA 预警 Apache HTTP Server mod_http2（CVE-2026-119618）已被利用。** 官方评分 CVSS 3.1 为 8.1（High，不是「十分」），影响 2.4.55 至 2.4.70（启用了 mod_http2），**修复版本是 2026-11-11 发布的 2.4.71**。CSA 称据报已有在野利用且存在公开 PoC。发现者包括 Anthropic OSS Scanner 与 Google Cloud 漏洞研究团队。
- Java4Shell（CVE-2026-114938）仍是热门后续：CISA 发警报敦促立即修补，X 上出现公开 PoC／利用链讨论（本期不链 PoC 仓库）；ExploitGrid 也新收录了相关条目。
- 工具侧：BOFbird 把 NetBird 做成可在 C2 进程内运行的 BOF-PE 模块；Claude-BugHunter 技能包在 GitHub 热榜大幅涨星。威胁侧：Hunt.io 写了暴露在荷兰 VPS 上的凭据盗窃战利品库（含美国银行与联邦身份网关登录）。AI 圈：Wiz 用 AI 扫描框架发现 nginx 漏洞；Palo Alto Networks 宣布 45 亿美元收购 Applied Compute；Google 发布面向编程与 agent 的 Gemini 4 Neon。

## CVE / POC / 漏洞

### 1. nginx 1.31.9／1.30.7 修复多枚缺陷，两枚 HTTP/2 预认证问题被评为可 RCE（nginx2root）
- 说明：nginx 于 11-18 发布 1.31.9 与 1.30.7。官方安全页将 **CVE-2026-123007** 记为 HTTP/2 流控中的内存破坏（major，受影响 1.9.5–1.31.8），将 **CVE-2026-123633** 记为 HTTP/2 释放后使用（medium，受影响 1.19.7–1.31.8）。Wiz 把这两枚都评为 CVSS 4.0 **9.2（Critical）**，称在启用 HTTP/2、无需登录的条件下可导致远程代码执行，并用 Wiz Atlas（AI 代码扫描）辅助发现，已与 F5 协调披露。Xint 以「nginx2root」为题，称共发现五枚可导向远程代码执行的缺陷，并称可与内核漏洞链到宿主机 root；其文同时列出 CVE-2026-123007、123633、123634（resolver）、121810（HTTP/3）、113425（mail 代理）。官方顾问页上同日还标了其它 major 项：CVE-2026-118899（TLS 1.3 下读取请求体时的无限循环，1.13.0–1.31.8）、CVE-2026-113425（mail 代理 UAF，0.5.33–1.31.8）。**修复版本：1.31.9+、1.30.7+**（CVE-2026-120993 仅写 1.31.9+）。无法立即升级时，Wiz 建议关闭 HTTP/2（1.25.1+ 可在 server 块设 `http2 off;` 并去掉 listen 上的 http2 参数，重载后确认旧 worker 已退出）；Xint 提醒关闭 HTTP/2 并不能覆盖全部缺陷。The Hacker News 等报道称已有公开 PoC；本期只记录这一事实，不链 PoC 仓库、不写利用步骤。
- X 原帖：https://x.com/brian_pak/status/2123071121553854545 · https://x.com/nirohfeld/status/2123070394227663006 · https://x.com/TheHackersNews/status/2123122388644856164 · https://x.com/Dinosn/status/2123088735189504431
- 厂商公告：https://nginx.org/en/security_advisories.html · F5 公告例 https://my.f5.com/manage/s/article/K000163926 （CVE-2026-123007）· https://my.f5.com/manage/s/article/K000163928 （CVE-2026-123633）
- 文章：https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities · https://xint.io/blog/nginx2root-remote-code-execution · https://nginx2root.com/ · https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html · https://ai-tldr.dev/releases/wiz-nginx-http2-rce/ · https://news.ycombinator.com/item?id=50547374

### 2. CISA 将 CVE-2026-90436 列入 KEV：官方产品是 Apache Axis 1.x（联邦期限 11-21）
- 说明：CISA KEV 目录 2026.11.18 将 CVE-2026-90436 记为 **Apache Axis Unsafe Reflection**，CVSS 3.1 **9.8**，联邦修补期限 **2026-11-21**，并要求取证分流。NVD 描述：Axis 1.x（至 1.4）在解析入站 SOAP Fault 时，可按 Fault 中指定的类名加载并实例化类，发生在服务处理链（含认证 handler）之前，在 classpath 上存在合适类时可导致未认证远程代码执行。Axis 1.x 已 EOL，Apache 建议迁移到 Axis 2／其他 SOAP 引擎，或自行应用补丁提交；不打算再发 1.x 修复版。昨日部分社媒／转述曾把同一 CVE 编号与 Confluence／N-able 的利用报道写在一起，**本期以 CISA／NVD 记载的 Apache Axis 1.x 为准**。X 上今日几乎没有以 Axis 为名的讨论，条目主要来自 KEV。
- 厂商公告：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-90436 · https://nvd.nist.gov/vuln/detail/CVE-2026-90436 · https://lists.apache.org/thread/8slf0j9gz35z56t0glt5h0ncwlbn4bdz · https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd
- 文章：https://www.openwall.com/lists/oss-security/2026/11/06/12 （本期抓取时 TLS 握手失败，链接仍以官方归档为准）

### 3. Synology DSM／BeeStation CVE-2024-10441 进入 KEV（CVSS 9.8，期限 11-21）
- 说明：CISA 今日将 Synology 系统插件守护进程中的输出编码／转义不当漏洞列入 KEV，可导致远程代码执行，**期限 2026-11-21**，取证分流为 Yes。NVD：影响 BeeStation OS（BSM）1.1-65374 之前，以及 DSM 7.2-64570-4、7.2.1-69057-6、7.2.2-72806-1 之前。厂商公告为 Synology_SA_24_20（及相关 SA_24_23）。X 上有账号称今日已出现公开 PoC，并提醒对互联网开放 Web 登录的未修补设备风险高；本期不链 PoC 仓库。
- X 原帖：https://x.com/ZeroKaiLabs/status/2123158167349854554
- 厂商公告：https://www.synology.com/en-global/security/advisory/Synology_SA_24_20 · https://www.synology.com/en-global/security/advisory/Synology_SA_24_23 · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2024-10441 · https://nvd.nist.gov/vuln/detail/CVE-2024-10441

### 4. REDCap 未认证代码执行 CVE-2026-90817 进入 KEV（期限 11-21）
- 说明：CISA 将 Vanderbilt 大学 REDCap 的代码注入漏洞列入 KEV，CVSS 3.1 **9.8**，期限 **2026-11-21**，取证分流为 Yes。攻击者无需登录，但需要知道有效的公开调查 hash，再通过公开调查上下文访问非预期控制器路由，并在数据导入时提供特制文件路径／流参数。本期 X 上未见显著讨论，条目来自 KEV／NVD。厂商社区页与 Securifera 顾问索引见下。
- 厂商公告：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-90817 · https://nvd.nist.gov/vuln/detail/CVE-2026-90817 · https://projectredcap.org/resources/community
- 文章：https://www.securifera.com/advisories/

### 5. LiteLLM 自定义 Guardrail 沙箱逃逸 CVE-2026-40217 进入 KEV（期限 12-02）
- 说明：CISA 将 BerriAI LiteLLM 列入 KEV，称 `/guardrails/test_custom_code` 存在未受保护的替代通道，可通过字节码改写执行任意代码，期限 **2026-12-02**。NVD 给出 CVSS 3.1 **8.8**。项目 GHSA-wxxx-gvqv-xp7p（2026-05-07 发布，标 Moderate／CVSS 4.0 5.9）写明默认配置下到达该接口需要 **proxy-admin 凭据**，默认 Docker 镜像以 root 运行；受影响版本 `>= 1.81.8, < 1.83.10`，**请升级到 1.83.11 或更新**（公告同时提到 patched release v1.83.10-stable）。临时缓解：在反向代理／网关阻断对该 URI 的 POST。X41 顾问 X41-2026-001 将严重性标为 High（CVSS 4.0 8.7），同样描述为需认证的 HTTP API。本期 X 上几乎没有讨论，条目来自 KEV／厂商顾问。
- 厂商公告：https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p · https://github.com/BerriAI/litellm/releases/tag/v1.83.10-stable · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-40217 · https://nvd.nist.gov/vuln/detail/CVE-2026-40217
- 文章：https://www.x41-dsec.de/lab/advisories/x41-2026-001-litellm/

### 6. 新加坡 CSA：Apache HTTP Server mod_http2 CVE-2026-119618 据报已遭利用（修复版 2.4.71）
- 说明：Apache 官方将 CVE-2026-119618 记为 **critical**：`mod_http2` 的 `assign_headers()` 因共享资源并发同步不当，可导致堆损坏与 RCE。影响 Apache HTTP Server **2.4.55 至 2.4.70**（以及 GitHub 上的 mod_h2 2.0.8–2.0.42）。发现者：Anthropic OSS Scanner、Google Cloud 的 Anthony Weems 与 Simon Scannell。修复于 2026-11-11 合入，**2.4.71 已在 11-11 发布**。新加坡 CSA 警报 AL-2026-164（11-17）称 CVSS 3.1 为 **8.1**，仅启用了 mod_http2 的服务器受影响，并写明「据报已被积极利用、且已有公开 PoC」。X 上今日有 dbugs 条目和「在野利用」转述；请以 Apache／CSA 原文为准，不必把个别帖子里的「十分／零日」表述当成官方评级。应尽快升级到 2.4.71 或更新，或临时关闭 mod_http2。
- X 原帖：https://x.com/ptdbugs/status/2123022963645579597 · https://x.com/XBToshi/status/2122973894399394205
- 厂商公告：https://httpd.apache.org/security/vulnerabilities_24.html#CVE-2026-119618 · https://nvd.nist.gov/vuln/detail/CVE-2026-119618
- 文章：https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2026-164/ · https://dbu.gs/vulnerability/PT-2026-145240 · https://access.redhat.com/security/cve/cve-2026-119618

### 7. Java4Shell（CVE-2026-114938）后续：CISA 敦促立即修补，已有公开 PoC
- 说明：昨日已报道 OpenJDK Base64 解码器内存损坏（Java4Shell）。本窗口内 CISA 发警报要求立即修补；Florian Roth 等继续传播技术概述；X 与 ExploitGrid 显示已有公开 PoC／扫描器条目（HIGH）。本期只记录「已有公开 exploit／PoC」这一事实，不链 PoC 仓库。缓解思路仍见昨日与 Calif 原文（如关闭 BASE64 intrinsics 等），以厂商／OpenJDK 更新为准。
- X 原帖：https://x.com/cyb3rops/status/2122945667978907764 · https://x.com/DarkWebInformer/status/2122829650070016336 · https://x.com/evilsocket/status/2122834023105937777 · https://x.com/pyn3rd/status/2122906289860997165
- 厂商公告：https://www.cisa.gov/news-events/alerts/2026/11/17/critical-java-vulnerability-requires-immediate-patching
- 文章：https://calif.io/java4shell
- ExploitGrid（佐证，已有公开 exploit）：https://exploitgrid.net/vulnerabilities/CVE-2026-114938 · https://exploitgrid.net/exploits/EGE-GH-arXAUnM

### 8. Airlock Gateway WAF 预认证 RCE（CVE-2026-19707）公开披露
- 说明：InfoGuard Labs 于 11-18 公开 CVE-2026-19707：Airlock Gateway 在 HTML 响应处理中存在堆溢出，在攻击者能够影响响应 HTML 等内容、且启用了 URL Encryption（特定模式）等配置时可导致预认证 RCE；影响较小时也可造成 worker 崩溃（拒绝服务）。**受影响：8.5.2 及更早；修复版本 8.5.3 与 8.6.1**（厂商 10-01 已发修复，今日公开）。CVSS 4.0 被标为 Critical（向量含较高攻击复杂度）。建议尽快升级；无法立即升级时，顾问给出了降低暴露的配置缓解（见原文，本期不展开利用条件细节）。
- X 原帖：https://x.com/InfoGuard_Labs/status/2123003649412698449
- 文章：https://labs.infoguard.ch/advisories/cve-2026-19707_airlock-gateway_remote-code-execution/
- 厂商公告：https://www.cve.org/CVERecord?id=CVE-2026-19707

### 9. 其他需留意的修补期限与后续
- **今日（11-18）到期**：Apple 多产品不当认证 CVE-2024-27834。https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2024-27834
- **11-20**：SonicWall SonicOS SSLVPN CVE-2026-19868。https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-19868
- **11-24**：Outlook CVE-2026-124194、Chrome CVE-2026-125350（X 上 @_MrNiko 提到公开崩溃 PoC；KEV 已收录）、Cisco BroadWorks CVE-2026-20320、Openwave CVE-2026-111793。Chrome 帖：https://x.com/_MrNiko/status/2123012700628463844 · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-125350
- **Puppet Enterprise CVE-2026-115731**（昨日入 KEV，期限 12-01）今日仍有媒体跟进「已被利用」。https://thehackernews.com/2026/11/hackers-exploiting-critical-puppet-rce.html · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-115731

## 工具与 GitHub 发布

### 1. BOFbird：把 NetBird 网格客户端打成可在 C2 进程内运行的 BOF-PE 模块
- 说明：@ipurple 介绍今日仓库 BOFbird：将 NetBird 客户端包装为一组 BOF-PE 模块，可在 C2 进程内运行（网格隧道、SOCKS5、端口转发等）。防御方可关注异常 named pipe 以及未经授权的 NetBird 连接。仅记录发布事实，供授权测试与检测使用。
- X 原帖：https://x.com/ipurple/status/2122957521300402177
- GitHub：https://github.com/Whispergate/BOFbird

### 2. Claude-BugHunter：面向授权漏洞狩猎／红队的 Claude Code 技能包，热榜暴涨
- 说明：GitHub 仓库 `elementalsouls/Claude-BugHunter` 被多账号列为当日热门，描述为约 80+ 个 skill、15 条 slash 命令，并从数百份已公开漏洞报告中归纳模式，用于授权范围内的漏洞狩猎和外部红队。trending_repos 称 24 小时内星标增幅超过两千。只作工具发布记录，不转载具体打法。
- X 原帖：https://x.com/trending_repos/status/2123025498951324045
- GitHub：https://github.com/elementalsouls/Claude-BugHunter

### 3. agent-redteam：用 skill 测试自己的 AI agent
- 说明：@edbrdi 发布 agent-redteam，用于在别人动手之前先测试自己的 AI agent。
- X 原帖：https://x.com/edbrdi/status/2123119220137562507
- GitHub：https://github.com/edbrdi/agent-redteam

## APT / Malware 分析

### 1. Hunt.io：荷兰 VPS 上暴露的凭据盗窃战利品库（美国银行与联邦身份网关登录）
- 说明：Hunt.io 称在荷兰 VPS（Podaon SIA）上发现一个开放目录，是一套凭据盗窃行动的战利品与任务库。内容包括从受害者本人 Windows 电脑窃取的密码管理器保险库明文、美国银行登录，以及 ID.me、Login.gov、IRS、SSA 等联邦身份相关账户——**报道强调银行或机构本身未必被攻破，而是受害者终端先失陷**。文中称 10-12 至 11-08 约 27 天内观察到 603 台主机回连，流量经 Cloudflare Workers 域名，并并行使用 HavoX、Phantom53、Krint 等 C2；还涉及离线处理 LastPass／1Password／KeePass、Chrome 应用绑定加密数据库，以及多个 AI 开发工具的会话令牌。完整 IOC 表以原文为准，本期只抄录已核对的主机地址与 C2 名称（见「地址／IoC」）。
- X 原帖：https://x.com/Huntio/status/2123091035115160054
- 文章：https://hunt.io/blog/us-bank-irs-ssa-logins-stolen-russian-speaking-operator

### 2. Microsoft agent-framework PyPI 投毒（后续报道，昨日已披露）
- 说明：昨日已报道 `agent-framework` 1.26.1／1.26.2 被植入凭据窃取逻辑。今日 The Hacker News、SecurityWeek 与 AI/TLDR 继续汇总：两个恶意版本会在 Python 进程启动时窃取云凭据与令牌，窗口很短。请核对应使用 1.26.0 或官方重新发布的安全版本，并轮换可能暴露的密钥。不重复展开攻击步骤。
- X 原帖：https://x.com/TheHackersNews/status/2122944680317067366 · https://x.com/Dinosn/status/2123022300333363535
- 文章：https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html · https://www.securityweek.com/microsoft-agent-framework-releases-poisoned-with-credential-stealer/ · https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer · https://ai-tldr.dev/releases/microsoft-agent-framework-pypi-compromise/

### 3. Optimizely 供应链事件后续：Krebs 称攻击者曾用实验平台对头部网站做恶意软件 A/B 测试
- 说明：昨日已报道 Optimizely 脚本被劫持、波及多家媒体与企业站点。今日 KrebsOnSecurity 跟进称攻击者利用该实验平台对头部网站投放的恶意软件做 A/B 测试。防御重点仍是审查第三方标签／实验脚本与厂商审计日志。
- X 原帖：https://x.com/Dinosn/status/2122902520678998306
- 文章：https://krebsonsecurity.com/2026/11/attackers-used-optimizely-to-a-b-test-malware-on-top-websites/

## SecureFlow 信息流精选

本日无显著更新。SecureFlow 的 all、community、blog 三个公开接口在本窗口多次请求均返回 HTTP 522（Cloudflare 源站错误），带浏览器 UA 与首页 Referer 重试后仍失败，因此无法按分类统计新条目。不将失败记为「零条」。

## AI/TLDR 动态

今日 AI 圈与安全交叉最紧的是 **Wiz 用 AI 扫描框架发现 nginx HTTP/2 预认证缺陷**（已与 CVE 节合并）。模型与产品方面，Google 推出面向长程编程与 agent 的中端模型 Gemini 4 Neon，DeepMind 的 Genie 4 进入 Project Genie；微软在 Ignite 周期里让 Word／Excel／PowerPoint 进入 Copilot 正式可用，并发布更快的 Decision-1.1；Anthropic 更新 Claude Code 2.1.327 并推出平台联动计费；OpenAI Codex CLI 0.170.0 加入终端实时语音。行业上，Palo Alto Networks 宣布以约 45 亿美元股票收购 Applied Compute（企业自有开放权重模型的训练与服务）。本窗口共 **19** 条（security 3、model 7、tool 7、article 1、ecosystem 1）。

### 安全（未在他处展开的，以及交叉提示）
- **安全** · Nginx HTTP/2 预认证 RCE，补丁 1.31.9／1.30.7（已与 CVE 节合并）：https://ai-tldr.dev/releases/wiz-nginx-http2-rce/ · 原始来源 https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities · https://nginx.org/en/security_advisories.html
- **安全** · Vals AI 自主作战／目标选择测试：Frontier 模型很少拒绝选择军事目标，把任务说成「游戏」后拒答进一步下降；报道称 Claude Opus 5.5 在 32 次运行中有 22 次选中一所学校。https://ai-tldr.dev/releases/vals-autonomous-warfare-ai-targeting/ · 原文 https://www.vals.ai/blogs/autonomous-warfare · https://techcrunch.com/2026/11/17/ai-models-can-be-tricked-into-identifying-civilians-as-military-targets-by-telling-them-its-a-game/
- **安全** · Microsoft agent-framework 在 PyPI 上的两个版本被植入凭据窃取（昨日已报道，今日 AI/TLDR 收录）：https://ai-tldr.dev/releases/microsoft-agent-framework-pypi-compromise/ · https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer

### 模型
- Gemini 4 Neon：Google 面向长程编程与 agent、成本低于 Carbon 的中端模型。https://ai-tldr.dev/releases/google-gemini-4-neon/ · https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/ · 模型卡 https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf
- Genie 4 进入 Project Genie，可在生成世界里用提示改场景（含声音）。https://ai-tldr.dev/releases/google-genie-4-project-genie/
- Meituan LongCat-Video-Avatar 1.6：开源数字人／对口型长视频模型。https://ai-tldr.dev/releases/meituan-longcat-video-avatar-1-6/
- tiny-voca：约 450 万参数、可在 CPU 上高倍实时运行的开源 TTS。https://ai-tldr.dev/releases/n4ze3m-tiny-voca/
- Qwen3.8-27B 的 Pi agent LoRA、SenseNova-Loop-9B、Microsoft-Decision-1.1（速度约快一倍并支持读图）：https://ai-tldr.dev/releases/harness-hub-qwen3-8-27b-pi-adapted/ · https://ai-tldr.dev/releases/sensenova-loop-9b/ · https://ai-tldr.dev/releases/microsoft-decision-1-1/ · https://commandline.microsoft.com/microsoft-decision-model-ga/

### 工具与开源仓库
- VS Code 1.147：agent 增加 Browser Use、模型路由和延迟发送。https://ai-tldr.dev/releases/microsoft-vscode-1-147/ · https://code.visualstudio.com/updates/v1_147 · https://github.com/microsoft/vscode/releases/tag/1.147.0
- Codex CLI 0.170.0：终端里通过 WebRTC 做实时语音。https://ai-tldr.dev/releases/openai-codex-cli-0-170/ · https://github.com/openai/codex/releases/tag/rust-v0.170.0
- Claude Code 2.1.327：减少把 MCP 令牌放在命令行、工作树更安全。https://ai-tldr.dev/releases/anthropic-claude-code-2-1-327/ · https://github.com/anthropics/claude-code/releases/tag/v2.1.327
- Claude 平台联动计费、ChatGPT for Sales、Gemini 应用登陆低内存 Android Go 手机：https://ai-tldr.dev/releases/anthropic-claude-platform-linked-billing/ · https://claude.com/resources/articles/linked-billing-on-claude-platform · https://ai-tldr.dev/releases/openai-chatgpt-for-sales/ · https://ai-tldr.dev/releases/google-gemini-app-lower-memory-android/

### 论文与研究／行业动态
- 探测显示较新的 Claude 模型能较好预测真实氨基酸顺序，提示可能大规模见过蛋白质序列。https://ai-tldr.dev/releases/xinming-tu-claude-protein-sequences-probe/
- Palo Alto Networks 以约 45 亿美元股票收购 Applied Compute。https://ai-tldr.dev/releases/palo-alto-networks-applied-compute-acquisition/ · 新闻稿 https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000030/ex992pressrelease_november.htm
- Copilot 在 Ignite 2026：Word、Excel、PowerPoint 在 Copilot 中正式可用。https://ai-tldr.dev/releases/microsoft-copilot-ignite-2026-office-ga/ · https://www.microsoft.com/en-us/copilot/blog/2026/11/17/copilot-at-microsoft-ignite-expanding-whats-possible-with-intelligence-built-for-work/

## Agent 用例动态

今天的用例仍然高度集中在 **编程与多 agent 协作**（由一个主导 agent 把审查意见交给实现 agent 循环修改，只在越权或反复失败时叫人）、以及 **电脑／浏览器操控**（Claude computer use、Claude in Chrome、OpenClaw 安装软件、转录、打电话）。个人助理、CRM／销售运营和内容自动化也不少；有一条明确写到用 Grok Bot 做 Reddit 评论和私信，但账号因自动化受限、浏览器额度消耗很快。与安全／权限相关的用法放在前面。本窗口 RSS 新条目 **32** 条，下面按主题精选，不复制提示词。

### 安全与电脑／浏览器操控（需留意权限与账号风险）
- 有人用 Grok Bot 自动在 Reddit 评论并私信做调研，账号被限制、浏览器操作很快耗尽额度：https://agentusecases.ai/use-case/automate-reddit-commenting-and-dms-for-research
- 用 OpenClaw 在 WhatsApp／Telegram 上装转录软件、转写文件并接通电话：https://agentusecases.ai/use-case/install-transcription-software-and-transcribe-files-with-an-
- Claude computer use／Claude in Chrome、以及给 agent 桌面与浏览器控制的用法，继续出现在个人助理和运营流程里（权限面大，建议最小授权）：相关条目见本窗口 RSS，例如 https://agentusecases.ai/feed.xml

### 编程与多 agent 编排
- 用主导 agent 带实现／审查 agent：审查意见由实现 agent 修改并再提交，只有超出范围或多次失败才找人：https://agentusecases.ai/use-case/run-implementing-and-reviewing-agents-with-a-lead-agent
- 多人继续用 Claude Code、Codex、Cursor、OpenClaw 组合做实现与评审（窗口内多条，主题同上）。

### 个人助理与运营
- 有人用 Hermes Agent（Grok 4.6）做研究并代打电话给牙医：https://agentusecases.ai/use-case/use-a-personal-agent-for-research-and-calling-the-dentist
- Meta Muse 被描述为从空置出租管理到签下租约：https://agentusecases.ai/use-case/manage-a-vacant-rental-through-to-a-signed-lease
- 有评论让 Grok Bot 监视由 Claude 更新的 Google Sheet，并登录 CRM 为新客户登记工作：https://agentusecases.ai/use-case/book-crm-jobs-from-a-google-sheet-of-new-customers

其余条目覆盖广告工作流、营销周计划、把跟踪数据接到客户旅程等，完整列表见 https://agentusecases.ai/feed.xml 。

## 地址／IoC 汇总

以下仅抄录已在公开文章中出现、并经本期核对的指标，供狩猎与拦截；不附利用步骤。

- Hunt.io 报道的凭据盗窃战利品库主机：`145.63.138[.]67`（荷兰 VPS，文章称属 Podaon SIA；原文写作 145.63.138[.]67）
- 文中点名的 C2／框架名称：HavoX、Phantom53、Krint bridge；称另有 12 个 Cloudflare Workers 域名，完整域名表见原文，本期未能从页面稳定抽出全部域名，故不臆造。
- 文章：https://hunt.io/blog/us-bank-irs-ssa-logins-stolen-russian-speaking-operator

未见其他需单独抄录的公开 IoC。nginx／Apache／KEV 条目为漏洞与补丁情报，不在此重复。

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

## 来源搜索 URL（含 SecureFlow 三个接口、pwn.watch 订阅源、ExploitGrid 两个数据地址、AI/TLDR 订阅源、Agent Use Cases RSS、周末版的阮一峰周刊、各来源条数与覆盖区间）

- X Latest CVE／POC／exploit／0day（recency）：窗口 2026-11-17 22:50 UTC 起，25 条仅覆盖约 2 分钟；relevancy 补搜约 22.0 小时；公告／补丁关键词补搜约 23.2 小时。
- X Latest url:github.com (C2 OR red team OR nuclei)：11 条，约 23.3 小时。
- X Latest "malware analysis" OR "threat report" OR "threat actor"：Latest 约 1.5 小时，relevancy 约 22.6 小时。
- LWiS List：https://x.com/i/lists/1239330068461244424 （4 页／381 条，窗口内 308 条，约 24.2 小时）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 → **HTTP 522（重试后仍失败）**
- SecureFlow community 源列表：https://secureflow.scope-sentry.top/api/rss/category?category=community → **HTTP 522**
- SecureFlow blog 源列表：https://secureflow.scope-sentry.top/api/rss/category?category=blog → **HTTP 522**
- pwn.watch RSS：https://pwn.watch/feed.xml （50 条；最新仍为 2026-11-08 20:19 GMT，本窗口 0 条）
- ExploitGrid exploits：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （窗口内未见过的 19 条，HIGH／CRITICAL 13 条；与本窗口交叉展开的主要是 CVE-2026-114938，其余老 CVE 重复 PoC 只计数）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （与 CISA 交叉：11-16 的 Check Point／UnrealIRCd 已过；11-24 的 Outlook／Chrome／Cisco／Openwave；Puppet 12-01。今日新入 KEV 的 Synology／REDCap／Axis／LiteLLM 多数尚未出现在该截止日期列表中，期限以 CISA 官方为准。）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （目录版本 2026.11.18，新增 CVE-2024-10441、CVE-2026-40217、CVE-2026-90817、CVE-2026-90436）
- NVD API（CVE 详情核对）：https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-90436 等
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条；36 小时内新 19 条，security 3 条）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条；48 小时内新 32 条）
- 阮一峰周刊：本期为周三，不加此节。
- 核验记录：正文及来源节中的主链接用浏览器 UA 抽查（见 linkcheck.json）。t.co 已从页面 meta refresh／entities 展开（如 BOFbird → https://github.com/Whispergate/BOFbird，Claude-BugHunter → https://github.com/elementalsouls/Claude-BugHunter）。NVD 详情页为前端渲染，核验用官方 REST API（200）并保留 nvd.nist.gov 链接。oss-security 的 Axis 邮件归档本期 TLS 握手失败，保留官方 URL 并注明。F5 顾问页可能需登录，已同时保留 nginx.org 公开顾问页。Java4Shell／部分 KEV 条目的公开 PoC 仓库未写入报告。
- 验收：采集 ⚠️（X Latest／relevancy／LWiS List 成功；pwn.watch、ExploitGrid、AUC、AI/TLDR、KEV 已拉取并写明条数；**SecureFlow 三路 522 未通过**）· 核验链接 ✅（见核验记录）· 成稿 ✅（十个小节齐全，周三不含周刊节，IoC 仅抄录已核对指标，无利用步骤，已按 seen_ids 去重）· 落盘与交付 ✅（box 与本机副本均已写入并读回确认）
