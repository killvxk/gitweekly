# X 安全情报晚报 · 2026-11-19（周四）

> 报告时间：2026-11-19 约 19:56（America/Santiago），即 2026-11-20 约 06:56（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-18 22:55 UTC 到 11-19 23:00 UTC（约 24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-19 22:54:28～22:57:08 UTC（约 3 分钟，CVE／POC／exploit 关键词噪声刷屏），所以加了 relevancy 补搜 25 条（11-19 00:50:36～21:20:21 UTC，约 20.5 小时）、编号 CVE＋补丁／公告关键词 recency 25 条（11-19 22:15:39～22:53:55 UTC，仅约 38 分钟，仍偏短），以及 min_likes:5 高互动补搜 25 条（11-19 00:39:43～22:30:07 UTC，约 21.8 小时）。另一次 advisory relevancy 补搜被噪声刷到仅约 5 分钟，不计入有效覆盖。窗口起点 11-18 22:55 至 11-19 00:39 的约 1.7 小时，主要靠工具组 Latest 与 LWiS List 补上。
> - 工具组 Latest 16 条覆盖 11-18 22:58:03～11-19 22:42:51 UTC（约 23.7 小时，距窗口起点约 3 分钟），未再做 relevancy 补搜。
> - 威胁组 Latest 25 条只覆盖 11-19 19:31:03～22:45:20 UTC（约 3.2 小时），relevancy 补搜 25 条覆盖 11-19 00:05:29～22:08:44 UTC（约 22.0 小时）。
> - LWiS List 共 3 页、拉取 283 条（97＋96＋90），其中窗口内 277 条，覆盖 11-18 22:55 UTC（窗口起点；第 3 页最旧拉到 11-18 22:13:46 UTC，已越过起点）到 11-19 22:59:03 UTC（约 24.1 小时）。
> **其他信源**：SecureFlow 的 all／community／blog 三路接口首次返回 **HTTP 522**，随后用浏览器 UA＋站点 Referer 重试均 **超时**，**本窗口未能拉取新条目**，条数记为失败而非 0。pwn.watch 订阅源仍停在 2026-11-08 20:19 GMT，**本窗口无新条目**。ExploitGrid 上期之后未收录、且 date 落在约 48 小时窗口内的 exploit 共 **78 条**（约 11-18 06:58～20:05 UTC；接口 date 字段时区混用），其中 HIGH／CRITICAL 70 条（去重后约 33 个 CVE）；按规则只对与本窗口交叉、已在 KEV、或对应 CVE 为本窗口新讨论的条目作补丁／公开 exploit 佐证，其余老 CVE 重复 PoC 只计数不展开。AI/TLDR 本窗口 **15 条**（security 类 **0 条**）；发布页在换 UA＋Referer 后仍返回 Cloudflare 403，原文链接以订阅源标题与摘要为准。Agent Use Cases 本窗口 **30 条**（节内精选代表性条目）。本期为周四，不加阮一峰周刊节。
> **CISA KEV**：目录版本仍为 **2026.11.18**（发布 2026-11-18T19:17:41Z），**今日目录未更新、无新增条目**。昨日入目录的 4 条（Synology CVE-2024-10441、LiteLLM CVE-2026-40217、REDCap CVE-2026-90817、Apache Axis CVE-2026-90436）与 11-17 的 Puppet CVE-2026-115731 仍有效。临近期限：**11-20（明日）SonicWall CVE-2026-19868**；**11-21** Synology CVE-2024-10441、REDCap CVE-2026-90817、Apache Axis CVE-2026-90436；11-18 的 Apple CVE-2024-27834 已到期；11-24 Outlook CVE-2026-124194、Chrome CVE-2026-125350、Cisco BroadWorks CVE-2026-20320、Openwave CVE-2026-111793；12-01 Puppet CVE-2026-115731；12-02 LiteLLM CVE-2026-40217。期限以 CISA 官方为准，ExploitGrid 截止日期列表作交叉核对。
> **验收**：采集 ⚠️（X Latest／relevancy／高互动补搜／LWiS List、pwn.watch、ExploitGrid、AUC、AI/TLDR、KEV 均已拉取并写明条数；**SecureFlow 三路 522／超时，未通过「三路都已拉取」这项**）· 核验链接 ✅（见文末核验记录）· 成稿 ✅（十个小节齐全，周四不含周刊节）· 落盘与交付 ✅（box 与本机 /Users/kenny1337/Desktop/_05_项目/X安全情报晚报/ 均已写入）。

## 今日摘要

- **今日主线是 Broadcom／VMware 紧急补丁日（VMSA-2026-0009），且已确认被在野利用。** 最严重的是 vCenter 目录服务认证绕过 **CVE-2026-123890**（CVSS 9.8）：攻击者只要能网络访问 vCenter、无需凭据，即可获得 `administrator@vsphere.local` 会话。Mandiant／Google Threat Intelligence 证实，受疑与中国有关的间谍组织 **ARMORY CASTLE**（原 UNC5221）早在 **2026 年 9 月初** 就用自制 Golang 工具 **BONESAW** 利用该漏洞；初始入口是此前披露的 BeyondTrust Remote Support 0day。同公告还修了 SDDC Manager 三枚缺陷和 Windows 版 VMware Tools 的 SAML 令牌问题。官方无临时缓解、也不能走 Quick Patch，应立即按修复版本升级。
- **Windows 11 26H2 锁屏／BitLocker 绕过 0day（FastUnlock）** 在 X 上引发大量讨论：通过 Narrator 辅助功能绕过锁屏，目前尚无微软补丁；披露者给出的临时缓解是用 AppLocker 或自定义 DACL 限制 Narrator。已有公开 exploit，报告不链 PoC 仓库、不写步骤。
- **Drupal 核心安装器严重缺陷 CVE-2026-132165**（SA-CORE-2026-017）可导致未认证重装站点并远程代码执行，官方与 BleepingComputer 都警告利用可能很快出现；请升到 10.6.22／11.3.22／11.4.13，不能立即升级则阻断 `/core/install.php`。同期还有需管理员权限的 gadget chain CVE-2026-132166。
- **Apache Roller 未认证反序列化 RCE（CVE-2026-129448，与 CVE-2026-82384 为同一问题）已被 Apache 标明「正在被利用」。** 影响 4.0.0 至 6.1.4（以及只写了 6.1.5 的那条 CVE），应升到 **6.1.6 或更高**；仅在管理界面关闭 XML-RPC 不够。
- 其余需关注：GeoNetwork 预认证 RCE 链（CVE-2026-63219＋CVE-2026-58400，已有公开 exploit）；Ubiquiti UniFi Access 公告 073（7 枚，5 枚严重，最重 CVE-2026-132802，修复版 4.3.24）；昨日 nginx2root 今日仍有跟进且公开 exploit 数量继续增加。威胁侧，AetherC2 安卓银行木马正在针对以色列 Yad2 卖家；Inception 声称泄漏 AutoZone 数据；摩根大通、Visa、Mastercard 称第三方供应商遭攻击。
- KEV 目录今日未更新。**明日（11-20）是 SonicWall SonicOS SSLVPN CVE-2026-19868 的联邦修补期限。**

## CVE / POC / 漏洞

### 1. VMware vCenter 认证绕过 CVE-2026-123890（VMSA-2026-0009，已在野利用）
- 说明：2026-11-19 Broadcom 发布 VMSA-2026-0009，共 5 枚漏洞。最严重的 **CVE-2026-123890** 是 vCenter 的 VMware Directory Service 认证绕过（CWE-288；Mandiant 技术描述为通过 DCE/RPC 泄露未认证 SRP-6a 会话密钥），CVSSv3 **9.8**。具备网络访问即可在无凭据情况下建立 `administrator@vsphere.local` 会话，进而通过 vmdird 的 RPC 接口执行命令、取走包含 `data.mdb` 在内的文件。Mandiant 确认 ARMORY CASTLE（原 UNC5221）在 2026 年 9 月初即用 BONESAW 利用此漏洞（详见 APT 节）。该漏洞与今年早些时候 VMSA-2026-0006 中的 CVE-2026-59309 **不是同一问题**，已打过旧补丁的系统仍需这次更新。同公告另外四枚：CVE-2026-123891（SDDC Manager SQL 注入）、CVE-2026-123892（SDDC Manager 认证后命令注入）、CVE-2026-123893（SDDC Manager 本地提权）、CVE-2026-123894（Windows 版 VMware Tools SAML 令牌签名绕过，影响配置了 guest alias mapping 的虚拟机，提权留在客户机内）。官方称无变通办法、不能用 vCenter Quick Patch，属紧急变更。Rapid7 汇总的修复版本：VCF／vSphere Foundation 9.1.x → **9.1.1.0200**，9.0.x → **9.0.2.0200**；vCenter 8.0 → **8.0 U3m**；VCF 5.x → **5.2.5**；vCenter 7.0 需联系 Broadcom 扩展支持；Telco Cloud Platform／Infrastructure 参见 KB463116（走 8.0 U3m）。注意：安装 8.0 U3m 或 9.0.2.0200 会触发「Back-in-Time」限制，阻断升到 VCF 9.1.1，升级路径中的环境需先看官方 FAQ 与互操作矩阵。ESX 宿主机本身不受这五枚漏洞影响。vSphere 6.5／6.7（已停止评估）与通用支持已结束的 7.0 应视为受影响。本期未见该 CVE 被列入 CISA KEV。
- X 原帖：https://x.com/cyb3rops/status/2123471170523513041 · https://x.com/Big_Bad_W0lf_/status/2123417607873204268 · https://x.com/rapid7/status/2123525966060241185 · https://x.com/VMwareSRC/status/2123397146963759137 · https://x.com/Dinosn/status/2123446210010706249
- 厂商公告／问答：https://brcm.tech/vmsa-2026-0009-qna · https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0009/README.md · https://support.broadcom.com/web/ecx/security-advisory
- 文章／PDF：https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-vsphere · https://www.rapid7.com/blog/post/etr-cve-2026-123890-critical-authentication-bypass-vmware-vcenter/ · https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html
- CVE 记录：https://www.cve.org/CVERecord?id=CVE-2026-123890

### 2. Windows 11 26H2 锁屏／BitLocker 绕过 0day（FastUnlock，尚无补丁）
- 说明：@MSNightmare2000 披露 Windows 11 26H2 锁屏可被绕过，并称可导致完整 BitLocker 绕过；后续说明与转发将其归因于 Narrator 辅助功能，目前尚无微软安全更新。披露者给出的临时缓解是通过 AppLocker 或自定义 DACL 限制 Narrator，直到官方补丁发布。该帖互动很高（数千赞）。已有公开 exploit／仓库在流传，本报告只记录这一事实，不链 PoC 仓库、不写利用步骤。防御方应关注物理／近端场景下的锁屏策略，并限制 Narrator 等辅助功能在锁屏界面的可用性。
- X 原帖：https://x.com/MSNightmare2000/status/2123400798365430118 · https://x.com/MSNightmare2000/status/2123438269140451807 · https://x.com/Dinosn/status/2123429464537522465

### 3. Drupal 核心安装器严重缺陷 CVE-2026-132165（SA-CORE-2026-017）
- 说明：Drupal 安全团队发布 SA-CORE-2026-017。CVE-2026-132165 位于核心安装器脚本，未认证攻击者可能借此重装站点并实现远程代码执行。BleepingComputer 援引官方：若 Web 服务器不能写入或改权限 `settings.php`，部分利用路径会被缓解；即使用户已通过其他方式得到保护，仍应升级。受影响版本为低于 **10.6.22**、11.3.x 低于 **11.3.22**、11.4.x 低于 **11.4.13** 的分支。不能立即升级时应在 Web 服务器配置或站点根目录 `.htaccess` 中阻断 `/core/install.php`。同期还修了中等严重的 gadget chain **CVE-2026-132166**（需管理员权限才可导致 RCE）。官方在预告中警告利用「可能在数小时或数天内出现」，且至少一枚可被匿名用户利用。本期未见进入 KEV。
- X 原帖：https://x.com/Dinosn/status/2123411051811397764 · https://x.com/itsMikeKipruto/status/2123431043487412454
- 厂商公告：https://www.drupal.org/sa-core-2026-017 · https://www.drupal.org/docs/administering-a-drupal-site/security-in-drupal/securing-the-installer-installphp
- 文章：https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaw-warns-exploits-may-surface-quickly/

### 4. Apache Roller 未认证反序列化 RCE CVE-2026-129448（与 CVE-2026-82384 为同一问题，已被利用）
- 说明：Apache 在安全公告中写明：Apache Roller 4.0.0 至 6.1.4 的 XML-RPC 端点在认证之前反序列化 vendor extension 类型，未认证远程攻击者可执行任意代码。这与只列出 6.1.5 的 **CVE-2026-82384** 是同一漏洞，且「正在被积极利用」。Apache 尚未公开归因或受害面细节。修复版本为 **Apache Roller 6.1.6 或更高**（关闭扩展类型并在关闭 XML-RPC 后拒绝恶意请求）。不能立即升级的缓解：在 `WEB-INF/web.xml` 将 `enabledForExtensions` 设为 `false`，删除 `/roller-services/xmlrpc` 的 servlet 映射并重启。仅在管理界面关闭 XML-RPC **不够**，因为旧版本会在检查该开关之前就反序列化请求。狩猎时可关注对 `/roller-services/xmlrpc`（或 `/roller/...`）的异常 POST。本期未见进入 KEV。未见 pwn.watch 新条目；ExploitGrid 本窗口未见专门收录该 CVE 的新 exploit 记录。
- X 原帖：https://x.com/superdoccimo/status/2123503107552194910 · https://x.com/ptdbugs/status/2123345131935854696
- 厂商公告：https://lists.apache.org/thread/lnz4s26tv6hdo03wngtdbpfj4hg4gtds · https://roller.apache.org/downloads/downloads.html · https://roller.apache.org/security.html
- 文章：https://www.bleepingcomputer.com/news/security/apache-warns-of-roller-rce-vulnerability-exploited-in-attacks/
- CVE 记录：https://nvd.nist.gov/vuln/detail/CVE-2026-129448 · https://www.cve.org/CVERecord?id=CVE-2026-129448

### 5. GeoNetwork 预认证 RCE 链 CVE-2026-63219＋CVE-2026-58400（已有公开 exploit）
- 说明：@BridgerTalha 称在 GeoNetwork 中发现一条可在无认证情况下拿到 shell 的链：CVE-2026-63219（未授权 formatter 上传）与 CVE-2026-58400（Saxon XSLT 导致 Java 执行）。ExploitGrid 在 11-18 收录了标题为 GeoNetwork-UnauthenticatedRCE 的 CRITICAL 条目（internalId EGE-GH-rIMg4tA），可作「已有公开 exploit」的交叉佐证。本报告不链 PoC 仓库、不写利用步骤。运行 GeoNetwork 的单位应尽快核对厂商／发行版补丁并限制管理接口暴露。
- X 原帖：https://x.com/BridgerTalha/status/2123372779441713582
- 文章：https://exploitgrid.net/exploits/EGE-GH-rIMg4tA · https://exploitgrid.net/vulnerabilities/CVE-2026-63219 · https://exploitgrid.net/vulnerabilities/CVE-2026-58400

### 6. Ubiquiti UniFi Access 安全公告 Bulletin 073（7 枚，5 枚严重）
- 说明：X 上多条帖子汇总 Ubiquiti 安全公告 Bulletin 073：UniFi Access Application（门禁／闸机／电梯控制软件）在 11-19 公开 7 枚缺陷，其中 5 枚为严重级别；最重为 **CVE-2026-132802**（有帖称为 CVSS 9.9，涉及文件处理中的符号链接跟随导致 root 代码执行）。受影响版本为 **4.3.24 之前**，修复版本为 **4.3.24 或更高**。同期提到的编号还有 CVE-2026-132803、CVE-2026-132804、CVE-2026-132807、CVE-2026-132808 等。box 用浏览器 UA 访问社区公告页返回的是前端壳层（HTTP 200，正文由脚本渲染），细节以公告页和 CVE 记录为准。
- X 原帖：https://x.com/SamAiPr/status/2123307521163362409 · https://x.com/2logics/status/2123538409742299362
- 厂商公告：https://community.ui.com/releases/Security-Advisory-Bulletin-073/677d5551-5ad9-4c85-86e9-4cdd9636a1e2
- CVE 记录：https://www.cve.org/CVERecord?id=CVE-2026-132802

### 7. 昨日主线后续：nginx2root（CVE-2026-123007／CVE-2026-123633 等）公开 exploit 继续增加
- 说明：F5／nginx 于 11-18 发布的 1.30.7（稳定）／1.31.9（主线）补丁日（nginx2root）今日仍有政府与发行版跟进，例如马尔代夫数字服务（MDS）安全通告、KUSANAGI 更新 kusanagi-nginx，以及 CERT-EU 安全公告 2026-022。X 上继续强调 CVE-2026-123007（HTTP/2 预认证内存破坏，可导致工作进程权限下的未认证代码执行）与 CVE-2026-123633。ExploitGrid 本窗口新增大量与这两枚 CVE 相关的 HIGH 条目（属重复收录的公开 exploit／检测仓库，只计数不展开）。临时缓解仍是关闭 HTTP/2，但不能覆盖全部缺陷，应升级。官方顾问页：https://nginx.org/en/security_advisories.html。
- X 原帖：https://x.com/mdsgovmv/status/2123461337569218674 · https://x.com/kusanagi_saya/status/2123353183884058899 · https://x.com/0disoft/status/2123340179683573796
- 厂商公告：https://nginx.org/en/security_advisories.html
- 文章／PDF：https://cert.europa.eu/publications/security-advisories/2026-022/pdf · https://kusanagi.tokyo/en/releases/28500/

### 8. 其他需留意的修补期限与公开 exploit
- **明日（11-20）到期**：SonicWall SonicOS SSLVPN CVE-2026-19868。https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-19868
- **11-21**：Synology DSM／BeeStation CVE-2024-10441、REDCap CVE-2026-90817、Apache Axis 1.x CVE-2026-90436。https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2024-10441 · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-90817 · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-90436
- **已到期（11-18）**：Apple 多产品不当认证 CVE-2024-27834。https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2024-27834
- **11-24／12-01／12-02**：Outlook CVE-2026-124194、Chrome CVE-2026-125350、Cisco BroadWorks CVE-2026-20320、Openwave CVE-2026-111793；Puppet Enterprise CVE-2026-115731；LiteLLM CVE-2026-40217（昨日入 KEV，今日仍有「正在被利用、尽快修补」的跟进帖，不重复展开）。
- X 上另有较低信号的公开 exploit 提示，仅记录事实、不展开步骤：ONLYOFFICE Docs 命令注入 CVE-2026-113630；Telerik UI for AJAX CVE-2026-13181（修复目标版本有帖提到 v2026.2.708 之前受影响）。Ruby 侧有人讨论预认证 RCE／「Ruby2Shell」（CVE-2026-132825，称与字符串大写转换堆溢出有关），官方公告细节本期未独立核到，暂不作为已确认条目展开。
- ExploitGrid 本窗口 HIGH／CRITICAL 新条目中，nginx2root 与 Java4Shell（CVE-2026-114938，上期已报道）占大多数，其余多为老 CVE 的重复 PoC，只计数不展开。

## 工具与 GitHub 发布

### 1. NTSleuth：跨架构提取并分析 Windows 系统调用
- 说明：@SEKTOR7net 介绍 @xaitax 的开源工具 NTSleuth，可从 ntdll.dll 与 win32u.dll 自动提取 ARM64／x64／x86 的系统调用，借助 PHNT 数据库解析参数，并导出 JSON 或 C 头文件。可用于授权测试与检测工程中的 syscall 测绘。仓库页 HTTP 200。
- X 原帖：https://x.com/SEKTOR7net/status/2123395112663466305
- GitHub：https://github.com/xaitax/NTSleuth

### 2. Claude-BugHunter：面向缺陷狩猎与外部红队的 Claude Code skill 包
- 说明：X 上有帖介绍 GitHub 仓库 elementalsouls/Claude-BugHunter，称这是一套给 Claude Code 使用的 skill／命令集合，从已公开的漏洞报告中归纳常见缺陷类别，用于授权范围内的缺陷狩猎与红队工作。仓库页 HTTP 200。仅记录发布事实，供授权测试使用；不转载其中的攻击步骤。
- X 原帖：https://x.com/JM688688/status/2123547580760314031
- GitHub：https://github.com/elementalsouls/Claude-BugHunter

### 3. agent-redteam：针对「自己拥有的」LLM agent 做授权测试的 skill
- 说明：@edbrdi 发布 agent-redteam，称可在 Claude Code、Codex 等加载 SKILL.md 的环境中，按范围对自有 agent 做注入、工具滥用与数据泄漏等测试并生成回归包。仅记录发布事实，不复制具体测试用例或攻击步骤。
- X 原帖：https://x.com/edbrdi/status/2123217019277304200
- GitHub：https://github.com/edbrdi/agent-redteam

### 4. 其他
- Objective-See OBTS v9 期间，@0x4D31 分享演讲幻灯「toolchain is the loader」，并提到已开源 Maratus。幻灯页：https://0x4d31.github.io/toolchain-is-the-loader/ （经 @patrickwardle 转发：https://x.com/patrickwardle/status/2123328916261908487）。另有 @justdionysus 的 XNU 利用相关幻灯：https://justdionysus.github.io/slides/2026-obts-v9-blazakis-exploiting-xnu.pdf
- 昨日已报道的 BOFbird（NetBird 的 BOF-PE 移植）在窗口起点附近仍有转发，不重复展开。GitHub：https://github.com/Whispergate/BOFbird

## APT / Malware 分析

### 1. ARMORY CASTLE（原 UNC5221）利用 vCenter 0day 与 BONESAW 深入 vSphere
- 说明：Mandiant／GTIG 在 11-19／11-20 发表的报告（与 VMSA 同日）补充了 ARMORY CASTLE 的后续活动。该组织先利用 BeyondTrust Remote Support 的 0day **CVE-2026-102764**（补丁公告 BT26-05，Mandiant 曾于 10-15 披露）进入，再横向到内部 Linux 设备并提权，随后用 **CVE-2026-123890** 打 vCenter。Mandiant 称取证表明，其在 **2026 年 9 月初** 就使用 Golang 远程利用工具 **BONESAW** 利用该 vCenter 漏洞：泄露 LMDB、劫持 SAML STS、创建 SSO 管理员账户，并部署多套针对目标设备定制的恶意软件。@cyb3rops 强调攻击者还能直接从虚拟机磁盘窃取数据，即使 vCenter 未暴露在互联网上也值得尽快打补丁。防御重点：立即按 VMSA-2026-0009 升级；检查 9 月以来的 vCenter／SSO 异常管理员账户、SAML STS 异常和目录数据库访问；并回溯 BeyondTrust Remote Support 的入侵面。不展开利用步骤。
- X 原帖：https://x.com/cyb3rops/status/2123471170523513041 · https://x.com/Big_Bad_W0lf_/status/2123417607873204268
- 文章：https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-vsphere
- 厂商公告：https://brcm.tech/vmsa-2026-0009-qna

### 2. AetherC2 安卓银行木马：以 Yad2「物流／交付」为诱饵瞄准以色列用户
- 说明：@g0njxa 与 cyberapp.co.il 的分析描述了一场针对以色列 Yad2 卖家的活跃活动。诱饵为伪造的「已找到买家／需要安装交付应用」短信或链接，页面仿冒 Google Play，实际侧载 APK；随后以伪造的「Google Play 服务更新」诱使授予无障碍等权限，再分层释放银行木马 AetherC2。能力包括凭据与银行信息窃取、网页注入覆盖、实时屏幕流、键盘记录、短信／OTP 劫持，控制端笔记为俄语。两则来源给出的 C2 与下载域并不完全相同（可能是同一活动的不同样本或不同时间窗口），下面按来源原样抄录，供狩猎交叉，不尝试合并成单一真相。
- X 原帖：https://x.com/g0njxa/status/2123548207653208174
- 文章：https://cyberapp.co.il/research/aetherc2-yad2-delivery-android-attack-chain
- 地址／IoC：见「地址／IoC 汇总」

### 3. Inception 勒索／敲诈团伙声称泄漏 AutoZone 数据
- 说明：@DailyDarkWeb 称 Inception 敲诈团伙在泄漏站上架美国汽配零售商 AutoZone（田纳西州孟菲斯总部），并在赎金期限过后将数据标记为已泄漏。团伙声称约 22 GB、23,562 个文件，其中包括 827 个 ServiceNow 事件文件夹以及涉及 LDAP 登录、AutoZone Rewards、PayPal 订单失败、Cisco Finesse 联络中心故障等的 IT runbook。此为泄漏站单方面声称，未见 AutoZone 官方确认。防御方若为相关供应链或使用类似 ServiceNow 流程，可关注凭据与 runbook 泄露后的二次利用。
- X 原帖：https://x.com/DailyDarkWeb/status/2123539197885632997

### 4. 摩根大通、Visa、Mastercard：第三方供应商遭网络攻击
- 说明：路透社报道（X 上由 @Dinosn 等转发）摩根大通、Visa、Mastercard 称向其提供服务的第三方供应商遭到网络攻击。另有转发称勒索组织 n0n 在暗网发布所谓摩根大通客户数据，该说法未经官方确认，需与「第三方供应商被攻击」的公司声明区分看待。box 用浏览器 UA 访问路透社原文时遇到验证页（非 404），链接予以保留。
- X 原帖：https://x.com/Dinosn/status/2123486561086149106 · https://x.com/evilsocket/status/2123450566995320951
- 文章：https://www.reuters.com/legal/government/jpmorgan-says-third-party-vendors-targeted-cyberattack-2026-11-19/

## SecureFlow 信息流精选

本日无显著更新。SecureFlow 的 all、community、blog 三路公开接口在首次拉取时返回 HTTP 522（源站不可用）；随后用浏览器 UA 加站点 Referer 重试，三次均超时。未能获取本窗口新条目，不将失败计为 0 条。

## AI/TLDR 动态

今日 AI 圈的重点是产品与资本市场并行：Google 把 Gemini 的电脑操控带到 Mac（后台窗口里操作应用与文件，不抢占当前屏幕），并向开发者开放 Genie 4 世界模型与「按需加载工具描述」的 Tool Retrieval；Anthropic 将 IPO 定价为每股 83 美元、11-19 在纳斯达克开盘；Microsoft 在 Ignite 2026 发布 MAI Realtime 1、Image 2.7 以及面向安全场景的便宜模型 Cyber 2 Flash；Claude Code 更新到 2.1.328。本窗口共 **15** 条（订阅源约 50 条），其中 **security 类 0 条**。发布页 https://ai-tldr.dev/releases/... 在浏览器 UA＋首页 Referer 下仍返回 Cloudflare 403，故未从页面抄出额外原始来源，以下链接以 AI/TLDR 条目为准。video／showcase 类低信号条目只计数或简写。

### 模型与平台
- Google 向开发者开放 Genie 4，可流式生成可玩的 720p 世界：https://ai-tldr.dev/releases/google-genie-4-gemini-api/
- Microsoft MAI 在 Ignite 2026 发布首个语音到语音模型 MAI Realtime 1、图像编辑 Image 2.7，以及廉价安全向模型 Cyber 2 Flash：https://ai-tldr.dev/releases/microsoft-mai-ignite-2026-models/
- RadixArk 开源 DaisyRose-27B（基于 Qwen3.8-27B 的强化学习调优，面向长程 agent 任务）：https://ai-tldr.dev/releases/radixark-daisyrose-27b/
- Apple FastFrames：号称在 50ms 内生成 480p 视频帧：https://ai-tldr.dev/releases/apple-fastframes/

### 工具与开源仓库
- Gemini for Mac 电脑操控：在后台窗口中操作 Mac 应用、文件和网站：https://ai-tldr.dev/releases/google-gemini-mac-computer-use/
- Gemini API Tool Retrieval：agent 可挂上大量工具，只为实际用到的工具支付输入 token：https://ai-tldr.dev/releases/google-gemini-api-tool-retrieval/
- Google Labs Stitch Loop：持续观察已上线产品、提出修复并开 PR 的长时 agent：https://ai-tldr.dev/releases/google-stitch-loop/
- Claude Code 2.1.328：auto mode 扩展到第三方云，`/code-review` 改为只报缺陷：https://ai-tldr.dev/releases/anthropic-claude-code-2-1-328/

### 行业与研究动态
- Anthropic IPO 定价 83 美元／股，11-19 在纳斯达克上市：https://ai-tldr.dev/releases/anthropic-ipo-priced-83/
- OpenAI 第二份内部研究报告称，agent 完成 2–4 小时研究任务的成功率约 46%，自 3 月以来大致翻倍，但增益不均（showcase，简记）：https://ai-tldr.dev/releases/openai-research-acceleration-jagged-frontier/
- 有条目称 OpenAI 模型参与改写 AMD GPU 电路、PPA 最高约提升 14%，部分改动进入实际芯片（showcase，简记）：https://ai-tldr.dev/releases/openai-chip-design-amd-gpu-14-percent/
- 有条目称 Claude agent 完成两项黑洞物理未决计算（showcase，简记）：https://ai-tldr.dev/releases/anthropic-claude-black-hole-physics/

### 视频（只计数）
本窗口 video 类 3 条（AI Explained 谈 Anthropic IPO／GPT-6.2 Astra、Two Minute Papers 谈 AlphaGenome 2、Wes Roth 谈 Google Neon），不展开。

## Agent 用例动态

今天收录的用例仍然高度集中在「写代码、做产品」和「让浏览器／电脑 agent 去填表、比价、下单」两类：Replit Agent 与 Cursor／Claude Code／Codex 被用来从零搭应用、写测试、按分支隔离工作区；Gemini、Perplexity Comet、Meta Muse、Manus 则被用来订机票、报名比赛、比价和下单。安全相关信号不多，但「给每个 coding agent 按 git 分支隔离工作区并分配独立本地 IP」以及「过夜让 agent 逆向 AirPlay、结果用电脑麦克风最大音量自检」值得留意权限与物理副作用。本窗口共 **30** 条（11-19 计 20 条、11-18 计 10 条，按 pubDate），以下精选代表性条目。

### 安全与权限相关
- 有人用 Cursor 与 Claude Code 做了一个 Electron macOS 应用，按 git 分支为每个 coding agent 提供隔离工作区并分配独立本地 IP：https://agentusecases.ai/use-case/build-a-macos-app-isolating-agent-workspaces-per-branch
- 有人让 agent 过夜逆向 AirPlay，agent 试图用最大音量播放并用笔记本麦克风监听来验证结果：https://agentusecases.ai/use-case/reverse-engineer-airplay-overnight
- 有人做了一个可通过 Telegram／WhatsApp／电子邮件触达的个人 agent，用来打补丁、发发票、处理服务商、审合同并起草 GDPR 请求：https://agentusecases.ai/use-case/run-a-personal-agent-for-servers-accounting-contracts-and-re

### 软件工程与多 agent
- 有人放出一群过夜 agent，为模拟器实现带 JIT 的 AArch64 CPU：https://agentusecases.ai/use-case/implement-an-aarch64-cpu-with-jit-using-an-overnight-agent-h
- 有人用 Cursor 搭建包含摄入管道、Neo4j 模式、检索工具和 LangGraph agent 的完整仓库：https://agentusecases.ai/use-case/build-an-ingestion-and-retrieval-agent-repo-in-cursor
- 有人向 Cursor agent 描述 API 端点，生成带断言的 `.http` 测试文件并跑通：https://agentusecases.ai/use-case/generate-api-test-files-from-endpoint-descriptions
- 有人用 Codex 定时从 GitHub Issues 或 Notion 取缺陷列表，在独立 git worktree 里逐项处理：https://agentusecases.ai/use-case/work-through-bug-lists-on-a-schedule-in-git-worktrees
- 开源版 Cursor Projects 的主 agent 会读取云端 PR 聊天上下文、执行并关闭 issue：https://agentusecases.ai/use-case/act-on-cloud-pr-chat-context-and-close-issues
- 多条 Replit Agent 用例：做播客转 chatbot 应用、人力资源市场 MVP、全栈 Web 应用，以及「一天内做完应用后陷入修 A 坏 B 的循环」：https://agentusecases.ai/use-case/build-a-podcast-to-chatbot-app-and-its-marketing-site · https://agentusecases.ai/use-case/build-a-staffing-marketplace-mvp-and-a-browser-game · https://agentusecases.ai/use-case/build-a-full-stack-web-app-with-ai-and-database · https://agentusecases.ai/use-case/build-an-app-in-a-day-then-hit-bug-loops

### 浏览器、出行与个人事务
- 有人用 Perplexity Comet 根据 Excel 为九人填写机票表，并用来购物比价：https://agentusecases.ai/use-case/fill-flight-booking-forms-from-an-excel-sheet
- 有旅行作者让 Gemini agent 搜机票，21 分钟找到报价并填好旅客信息，在下单前停住：https://agentusecases.ai/use-case/search-flights-with-an-ai-agent-stopping-before-booking
- Gemini 电脑操控模型在零售网站比较运动相机并提交联系表单：https://agentusecases.ai/use-case/compare-products-and-submit-web-forms-with-browser-control
- RunSignup 员工用 Meta Muse 搜索赛事并填写报名表，第二次用已存密码和虚拟卡完成：https://agentusecases.ai/use-case/sign-up-for-races-with-a-browser-agent
- 有 agent 每天检查可退票家庭行程是否降价，称已省下 250 美元：https://agentusecases.ai/use-case/watch-refundable-ticket-prices-and-claim-the-drop
- 有人用 Claude Code 从约 120 张收据扫描件抽出供应商、日期、金额和类别到 CSV，并做订阅审计：https://agentusecases.ai/use-case/extract-receipts-into-a-csv-and-audit-subscriptions-with-cla
- 有人用 Gemini 做求职助手（简历、面试、调研），称大约三个月后找到工作：https://agentusecases.ai/use-case/build-a-job-search-helper-agent-for-cv-interviews-and-resear
- 有人用 Manus 在约 10 分钟内列出印度亚马逊 10,000 卢比以下的手机，或追踪 AI 创业公司、生成竞品对比表：https://agentusecases.ai/use-case/list-all-smartphones-under-rs-10-000-on-amazon-india · https://agentusecases.ai/use-case/track-ai-startups-with-an-agent · https://agentusecases.ai/use-case/map-top-autonomous-agents-into-a-comparison-sheet-and-deck

## 地址／IoC 汇总

以下仅抄录已在公开帖子或文章中出现的指标，供狩猎与拦截；不附利用步骤。不同来源对同一活动给出的 C2／域名不完全一致，按来源分列，不擅自合并。

**AetherC2／Yad2 诱饵活动（来源：X @g0njxa，2026-11-19）**
- 样本 SHA-256（TikTokPremium.apk）：`f1bb496bf4c54c487b0760d4c2f40324868018e71024b70f84efc585fa5dc7a6`
- 下载／投放域：`yad2-app-download[.]pro`、`app[.]onlytikpremium[.]pro/install.php`
- C2：`85.155.14.42`；MQTT over 双向 TLS：`ssl://85.155.14.42:443`；面板：`85.155.14.42:45043`
- 称 11-04 至 11-19 有 50 余名活跃受害者；活动标签 `paradigm`、`serj`、`octo`；一处「测试」IP：`31.31.30.79`（摩尔多瓦）
- X 原帖：https://x.com/g0njxa/status/2123548207653208174

**AetherC2／Yad2 诱饵活动（来源：cyberapp.co.il 分析文）**
- 诱饵链接：`https://yad2appl.org/app-download`（文章写作明文 URL）
- MQTT C2：`ssl://194.5.97.27:443`（双向 TLS）
- 文章称被动观察确认 44 名以色列受害者；活动标签 `yad2`
- 文章：https://cyberapp.co.il/research/aetherc2-yad2-delivery-android-attack-chain

未见其他需单独抄录的公开 IoC。vCenter／Drupal／Roller／nginx／KEV 条目为漏洞与补丁情报，不在此重复。AutoZone 与摩根大通相关内容目前是泄漏站或媒体报道，本期未见可核验的 IP／域名／哈希。

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
- 周刊一般每周五北京时间早上发布；报告日期（Santiago）为周六的那期收录 GitHub 项目和有趣文章。去重键：ryf:<周刊链接>。本期为周四，不加周刊节（最新已收录期为第 419 期）。

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

- X Latest CVE／POC／exploit／0day（recency）：窗口 2026-11-18 22:55 UTC 起，25 条仅覆盖约 3 分钟；relevancy 补搜约 20.5 小时；编号 CVE＋补丁关键词 recency 约 38 分钟（偏短）；min_likes:5 高互动补搜约 21.8 小时。
- X Latest url:github.com (C2 OR red team OR nuclei)：16 条，约 23.7 小时。
- X Latest "malware analysis" OR "threat report" OR "threat actor"：Latest 约 3.2 小时，relevancy 约 22.0 小时。
- LWiS List：https://x.com/i/lists/1239330068461244424 （3 页／283 条，窗口内 277 条，约 24.1 小时）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 → **HTTP 522，重试超时**
- SecureFlow community 源列表：https://secureflow.scope-sentry.top/api/rss/category?category=community → **HTTP 522，重试超时**
- SecureFlow blog 源列表：https://secureflow.scope-sentry.top/api/rss/category?category=blog → **HTTP 522，重试超时**
- pwn.watch RSS：https://pwn.watch/feed.xml （50 条；最新仍为 2026-11-08 20:19 GMT，本窗口 0 条）
- ExploitGrid exploits：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （窗口内未见过的 78 条，HIGH／CRITICAL 70 条／约 33 个 CVE；与本窗口交叉展开的主要是 GeoNetwork 与 nginx2root 佐证，其余老 CVE 重复 PoC 只计数）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （10 条活跃期限，与 CISA 交叉：11-20 SonicWall 未出现在该列表中，11-21 的 REDCap／Synology／Axis、12-01 Puppet、12-02 LiteLLM 有出现；期限以 CISA 官方为准）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （目录版本 2026.11.18，今日无新增）
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条；36 小时内新 15 条，security 0 条；releases 页面 403）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条；48 小时内新 30 条）
- 阮一峰周刊：本期为周四，不加此节。
- 核验记录：正文及来源节中的主链接用浏览器 UA 抽查（见 linkcheck.json）。t.co 已从 entities／展开 URL 处理。AI/TLDR 条目页换 UA＋Referer 后仍 403，保留订阅源链接并注明。路透社原文遇验证页（401／验证码壳），保留官方 URL。Ubiquiti 社区公告页与 Drupal SA 页面为前端渲染壳层（HTTP 200 但无完整正文），已同时保留 X 转述的版本号与 BleepingComputer 报道。诱饵域 yad2appl.org 在核验时出现 TLS 意外中断，作为文章中的 IoC 保留并注明。公开 PoC 仓库（FastUnlock、GeoNetwork 等）未写入报告。
- 验收：采集 ⚠️（X Latest／relevancy／高互动／LWiS List 成功；pwn.watch、ExploitGrid、AUC、AI/TLDR、KEV 已拉取并写明条数；**SecureFlow 三路 522／超时未通过**）· 核验链接 ✅（见核验记录）· 成稿 ✅（十个小节齐全，周四不含周刊节，IoC 仅抄录已核对指标，无利用步骤，已按 seen_ids 去重）· 落盘与交付 ✅（box 与本机副本均已写入并读回确认）
