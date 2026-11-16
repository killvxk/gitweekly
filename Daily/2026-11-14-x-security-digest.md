# X 安全情报晚报 · 2026-11-14（周六 · 周末版）

> 报告时间：2026-11-14 约 20:10（America/Santiago），即 2026-11-15 约 07:10（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-13 22:55 UTC 到 11-14 22:55 UTC（24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-14 21:25～22:52 UTC（约 1.5 小时），所以加了 relevancy 补搜 25 条（11-14 00:33～21:31）。
> - 工具组（github.com + C2/红队/nuclei）Latest **0 条**，工具节主要靠 LWiS List。
> - 威胁组 Latest 23 条（11-14 19:38～22:37）加 relevancy 24 条（11-13 23:33～11-14 21:44），以勒索泄露站播报为主。
> - LWiS X List 翻了 2 页共 192 帖，其中 143 帖在窗口内（11-13 22:55～11-14 22:24 UTC），覆盖完整 24 小时。
>
> **其他信源**：SecureFlow 三路本窗口 **0 条新条目**（all 接口最新一条发布于 11-13 21:07 北京时间，前一期已收录；community 7 源、blog 12 源均为 0）。pwn.watch 订阅源仍停在 2026-11-08 20:19 UTC，**本窗口 0 条**。ExploitGrid 本窗口新增 **33 条** exploit 收录（11-13 03:04～18:52 UTC），按规则挑出 8 条展开，其余为老 CVE 重复 PoC 或低危，只计数。AI/TLDR 本窗口 9 条（security 类 0 条）；Agent Use Cases 本窗口 26 条；阮一峰周刊第 419 期为新一期，本期收录。
> **CISA KEV**：目录版本 2026.11.13，近 48 小时新增 2 条（Check Point CVE-2026-123039、UnrealIRCd CVE-2026-114713，期限都是 **11-16 周一**），11-14 无新增。
> **验收**：四步全部通过（详见文末「来源搜索 URL」）。

## 今日摘要

- **周一（11-16）是两个 KEV 的联邦修补期限**：Check Point Gaia CVE-2026-123039（已被用于 PHP2Shell→root→ESXi 擦除器攻击链）和 UnrealIRCd CVE-2026-114713（项目方确认 11-08 起已被利用）。今天 X 上大量提醒「本周末就修」；ExploitGrid 新收录了 Check Point 这个 CVE 的公开 exploit（昨天还是 0 条），X 上也有人称发布了 UnrealIRCd 的 PoC，风险上升。
- **FBI 发布 ARTEX FLASH（FLASH-20261113-001）**：LLM 驱动的自主渗透框架 ARTEX 自 2026-08 起被多方滥用，原仓库下架后仍以 fork／ARTEX PRO 形式扩散，公网暴露控制台 1600+；FLASH 附有 IP、域名与行为指标（已抄入 IoC 节）。
- **朝鲜加密货币盗窃被打击**：美国司法部查封 FaceStealer 社工行动（深度伪造视频会议＋ClickFix，盗走 4 亿美元以上）的云基础设施，并扣押／冻结币安 10-29 被盗资金中超过 12 亿美元。
- **新漏洞与补丁**：PostgreSQL 一次修 52 个漏洞（CVE-2026-6460 类型混淆可让能建对象的用户在服务器执行代码，ExploitGrid 已收录公开 exploit）；Red Hat Quay CVE-2026-110697（9.9）与 WordPress ELEX HelpDesk CVE-2026-119077（9.8）出现公开 exploit；AMD SEV-SNP 新攻击 Mior／Skyfall 公开（需控制宿主机，固件更新 11～12 月下发）。
- **其他**：德国无人机厂商 Quantum Systems 的 QBase 更新服务器被植入恶意更新；欧洲刑警组织 Operation TorNado 逮捕 354 名暗网嫌犯。美国 11-13 全国航班停飞事件，DHS 称是电信故障、不怀疑人为破坏（安全圈讽刺站 faa2shell.com 走红）。

## CVE / POC / 漏洞（每条：说明 + 地址列表；合并 X、KEV、pwn.watch、ExploitGrid 的补丁状态与公开 exploit 情况）

**1. Check Point Gaia OS 本地提权 CVE-2026-123039（续报）：KEV 期限 11-16，ExploitGrid 新收录公开 exploit**
- 谁／什么：DynamicCLI 守护进程的全局可写本地 socket 可被本地用户用来以 root 执行命令；在野攻击链为 PHP2Shell 打 Mobile Access 门户 → 本漏洞提权 → webshell 与 TSGA/TSProxy 后门，部分受害者被投放 ESXi 擦除器。BleepingComputer 今日跟进报道。
- 补丁与公开 exploit：安装 November Jumbo Hotfix（sk1000362），同时修补 PHP2Shell；无法立即修补的，X 上建议停止并禁用 DynamicCLI 进程。ExploitGrid 11-13 03:22 UTC 收录 1 条公开 exploit（只给收录页，不链仓库）。pwn.watch 无条目。
- X 原帖：[FarVisionNetwks](https://x.com/FarVisionNetwks/status/2121728733098729474) · [forbot26](https://x.com/forbot26/status/2121407787481907547) · [ksanjeev284（周末就修）](https://x.com/ksanjeev284/status/2121463502913294700) · [TheExploitHQ](https://x.com/TheExploitHQ/status/2121619885834785062) · [Dinosn（转 BleepingComputer）](https://x.com/Dinosn/status/2121546289871552681)
- 厂商公告：[Check Point sk1000362](https://support.checkpoint.com/results/sk/sk1000362) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-123039) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123039)
- 文章：[BleepingComputer：Check Point gateways hacked via PHP2Shell to deploy VMware ESXi wiper](https://www.bleepingcomputer.com/news/security/check-point-gateways-hacked-via-php2shell-to-deploy-vmware-esxi-wiper/) · [ExploitGrid CVE 页](https://exploitgrid.net/vulnerabilities/CVE-2026-123039) · [ExploitGrid 收录页](https://exploitgrid.net/exploits/EGE-GH-KAuXeqC)

**2. UnrealIRCd labeled-response 注入 CVE-2026-114713（续报）：KEV 期限 11-16，X 上称已有公开 PoC**
- 谁／什么：6.0.0～6.2.7 的 labeled-response 模块不转义 IRCv3 label 标签，在两台以上互联服务器的网络中，任何用户可注入以服务器权限执行的 S2S 命令。维护者 Syzop 表示 11-07 发布热补丁后一天就出现利用。
- 补丁：升级 6.2.7.1 或打热补丁，至少部署 spamfilter 临时规则。X 用户 fixedbyreboot 称已发布 PoC（本报不转链仓库）；ExploitGrid 按本窗口数据未收录。
- X 原帖：[fixedbyreboot（称已发 PoC）](https://x.com/fixedbyreboot/status/2121541239648784550) · [ICHI_Global](https://x.com/ICHI_Global/status/2121483519243211168) · [WasafAbbasi](https://x.com/WasafAbbasi/status/2121566826161115595) · [Dinosn（转 THN）](https://x.com/Dinosn/status/2121593973487665217)
- 厂商公告：[GitHub Advisory GHSA-237f-p9h6-wq4r](https://github.com/advisories/GHSA-237f-p9h6-wq4r) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-114713) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114713)
- 文章：[The Hacker News：Attackers Exploit UnrealIRCd Flaw](https://thehackernews.com/2026/11/attackers-exploit-unrealircd-flaw-that.html) · [ExploitGrid CVE 页](https://exploitgrid.net/vulnerabilities/CVE-2026-114713)

**3. PostgreSQL 一次修复 52 个漏洞，CVE-2026-6460（8.8）类型混淆可致服务器端代码执行；ExploitGrid 收录公开 exploit**
- 谁／什么：能创建对象的数据库用户可利用复合类型字段类型变更后的类型混淆，以运行 PostgreSQL 的系统账号执行代码；影响 18.7、17.12、16.16、15.20、14.25 之前的所有版本。完整修复还需**重新编译已安装的 C 语言扩展**。官方与 CISA 记录均未报告在野利用。同批 CVE-2026-6471（7.2，持 REPLICATION 权限的非超级用户可经逻辑解码插件加载任意文件）。
- 公开 exploit：ExploitGrid 收录 CVE-2026-6460 两条、CVE-2026-6471 一条（含检测脚本类）。研究员已发布技术分析。
- X 原帖：[Dinosn（转 THN）](https://x.com/Dinosn/status/2121532109781393693)
- 厂商公告：[NVD CVE-2026-6460](https://nvd.nist.gov/vuln/detail/CVE-2026-6460) · [NVD CVE-2026-6471](https://nvd.nist.gov/vuln/detail/CVE-2026-6471) · [PostgreSQL 安全页](https://www.postgresql.org/support/security/)
- 文章：[The Hacker News：PostgreSQL Patches 52 Flaws](https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html) · [ExploitGrid CVE-2026-6460](https://exploitgrid.net/vulnerabilities/CVE-2026-6460) · [ExploitGrid CVE-2026-6471](https://exploitgrid.net/vulnerabilities/CVE-2026-6471)

**4. Chrome XML 释放后重用 CVE-2026-125350（续报）：2026 年第 8 个被在野利用的 Chrome 0day，已有公开 exploit 收录**
- 补丁：157.0.8103.50/.51；X 上提醒「周一以来没重启 Chrome 就没修上」，建议策略强制重启。ExploitGrid 11-13 10:24 UTC 收录公开 exploit。
- X 原帖：[wirelesslyhere](https://x.com/wirelesslyhere/status/2121717723298476175) · [TheCyphere](https://x.com/TheCyphere/status/2121604159086686623)
- 厂商公告：[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125350) · [Chrome Releases](https://chromereleases.googleblog.com/)
- 文章：[ExploitGrid CVE 页](https://exploitgrid.net/vulnerabilities/CVE-2026-125350)

**5. Outlook NTLM 泄露 CVE-2026-124194（续报）：KEV 期限 11-24**
- 今天 X 上讨论集中在「CVSS 只是 Moderate 但已被利用、进 KEV」，以及微软致谢 Anthropic Claude 协助发现。修复为 11-10 补丁；建议同时封锁出站 445。
- X 原帖：[Lumideezy](https://x.com/Lumideezy/status/2121695027055501571) · [EXINglobal](https://x.com/EXINglobal/status/2121717312038563929) · [Macfeecn](https://x.com/Macfeecn/status/2121731700879421574)
- 厂商公告：[MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-124194) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124194)
- 文章：[Computerworld：November Patch Tuesday 待办从 Outlook 开始](https://computerworld.com/article/4248384/for-november-patch-tuesday-means-a-to-do-list-that-starts-with-outlook.html)

**6. Red Hat Quay CVE-2026-110697（9.9）：来源：ExploitGrid（新 CVE 已有公开 exploit）**
- 谁／什么：机器人账号列表函数用未转义的命名空间名拼接 SQL LIKE 模式，攻击者建一个含下划线的命名空间即可匹配并取回其他命名空间的机器人账号及其解密凭据。NVD 11-11 发布。与昨天的 Quay CVE-2026-123710 同一产品，请一起排查。
- 厂商公告：[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-110697) · [Red Hat CVE 页](https://access.redhat.com/security/cve/CVE-2026-110697)
- 文章：[ExploitGrid CVE 页](https://exploitgrid.net/vulnerabilities/CVE-2026-110697)

**7. WordPress ELEX HelpDesk & Customer Ticketing System CVE-2026-119077（9.8）：来源：ExploitGrid（新 CVE 已有公开 exploit）**
- 谁／什么：≤3.3.9 存在 PHP 对象注入（ticket_label 字段）。NVD 11-13 发布，当天即出现公开 exploit。建议升级或停用插件。
- 厂商公告：[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-119077)
- 文章：[ExploitGrid CVE 页](https://exploitgrid.net/vulnerabilities/CVE-2026-119077)

**8. AMD SEV-SNP 机密计算新攻击 Mior 与 Skyfall**
- 谁／什么：两项研究（Mior 来自 ETH Zurich）展示恶意宿主可读取 SEV-SNP 保护的虚拟机内数据；Mior 还能修改内存并伪造远程证明报告。前提是控制宿主 hypervisor（Mior 还需控制 BIOS）。
- 补丁：AMD 已列出 8-12 的 SEV 固件（Mior）与微码（Skyfall），平台固件计划 11 月（Skyfall）、12 月（Mior）交给服务器厂商；客户需向服务器厂商取 BIOS 更新。
- X 原帖：[Dinosn（转 THN）](https://x.com/Dinosn/status/2121544188856799296)
- 文章：[The Hacker News：New Mior and Skyfall Attacks](https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html)

**9. 其他新披露（低互动，供排查）**
- Hotel Booking Lite ≤2.5.1 任意文件上传 CVE-2026-125851（9.9，**暂无补丁**）：[X cvedotnow](https://x.com/cvedotnow/status/2121728779240325299) · [cve.now](https://cve.now/CVE-2026-125851) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125851)
- Kingston FURY CTRL RGB 驱动 IOCTL 提权 CVE-2026-129261（9.3）：[X cvedotnow](https://x.com/cvedotnow/status/2121720976748445746) · [cve.now](https://cve.now/CVE-2026-129261)
- D-Link DSL-6740C CVE-2026-129444：[X vuldb](https://x.com/vuldb/status/2121729543455252955) · [VulDB 437457](https://vuldb.com/?id.437457)
- Linux 内核 IPv6 RPL 越界写 CVE-2026-43501（9.8，NVD 5 月发布，内核已修）：[X zoomeyebot](https://x.com/zoomeyebot/status/2121736275564880327) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-43501)
- Barracuda CVE-2026-111560 期限 11-13 已过，且 CVE 记录对受影响版本表述矛盾：[X severitydaily](https://x.com/severitydaily/status/2121589248486703563)

**ExploitGrid 计数（只计数不展开）**：本窗口 33 条中，另有老 CVE 重复 PoC（CVE-2020-1938、CVE-2020-1472、CVE-2025-48384×2、CVE-2025-4606 等）、已 KEV 的 Brotli CVE-2026-111497×2 与 marimo CVE-2026-39987、OpenSSH CVE-2026-123158×2（此前多期已报）、Fortinet 扫描器（CVE-2026-126170 等，11-11/12 已报）、Linux 内核 CVE-2026-98260×3、SAP DIAG CVE-2026-34265、PackageKit CVE-2026-41651、Microsoft CVE-2026-21509 等，以及 MEDIUM／LOW 4 条。列表：https://exploitgrid.net/

## 工具与 GitHub 发布（每条：说明 + 地址列表）

**1. AdminToSystem-HTTP.sys：Windows 管理员→SYSTEM 的 HTTP.sys NTLM 令牌捕获概念验证（140 赞）**
- 说明：利用 HTTP.sys 在内核态完成 NTLM/Negotiate 认证后把令牌交给用户态这一特性，诱使 SYSTEM 进程向本机监听端认证并复用令牌。前提已是管理员，属于提权后手法。
- 防守：关注本机回环地址上新注册的 HTTP.sys URL 组、二进制路径为 UNC/WebDAV 的新建服务，以及以 SYSTEM 运行、带默认凭据访问本机 HTTP 的计划任务（PowerShell／certutil）。
- X 原帖：[Dinosn](https://x.com/Dinosn/status/2121530665623797792)
- GitHub：https://github.com/ivancabrera02/AdminToSystem-HTTP.sys

**2. 《Introduction To Harness Engineering For Vulnerability Research》在线工作坊（Graham Helton、Ryan Basden，154 赞）**
- 说明：讲怎样为授权目标搭建漏洞研究 agent 的「harness」（目标上下文、确定性工具、授权边界、持久状态、验证方法），强调「agent 输出只是线索不是结论」。
- X 原帖：[payloadartist](https://x.com/payloadartist/status/2121611610376765709)
- 文章：https://grahamhelton.github.io/harness-engineering-workshop-book/introduction.html

**3. reddelexc/hackerone-reports：HackerOne 公开披露报告 Top 榜（169 赞）**
- X 原帖：[Dinosn](https://x.com/Dinosn/status/2121552723057299808)
- GitHub：https://github.com/reddelexc/hackerone-reports

**4. Intezer：用 Codex＋Binary Ninja 把 TinyTurla-NG 样本「重建」成可编译源码**
- 说明：Intezer 研究 AI 逆向重建闭源软件（Slack、Finder、TinyTurla-NG DLL），提出「一切都变成开源」对软件保护和恶意软件分析的影响。
- X 原帖：[fr0gger_](https://x.com/fr0gger_/status/2121445330747265164)
- 文章：https://research.intezer.com/blog/2026/11/when-everything-becomes-open-source/

**5. 社区：Cloudflare php2shell WAF CTF 争议**
- 说明：LiveOverflow 称提交的多个 WAF 绕过被以笼统理由判重复，并演示 AI 约 2.5 小时适配出新绕过；Dinosn 等也反映类似情况。提醒：WAF 规则只能作缓解，PHP2Shell 仍须打补丁。
- X 原帖：[LiveOverflow](https://x.com/LiveOverflow/status/2121377196438634857) · [Dinosn](https://x.com/Dinosn/status/2121554714600808875)

**6. 其他**
- yetone/magpie：菜单栏统一切换各 coding agent 的模型（Codex on DeepSeek、Claude Code on Kimi）：[X Dinosn](https://x.com/Dinosn/status/2121548324176347383) · https://github.com/yetone/magpie
- Apple 公布 Secure Exclaves（摄像头／麦克风数据隔离）架构：[X Dinosn](https://x.com/Dinosn/status/2121587780845445124) · https://www.securityweek.com/apple-reveals-how-secure-exclaves-shield-camera-and-microphone-data/

## APT / Malware 分析（每条：说明 + 地址列表）

**1. FBI FLASH：ARTEX 自主渗透框架威胁概览（FLASH-20261113-001）**
- 谁／打什么：ARTEX 是 Go 编写、接入外部大模型的多 agent 渗透平台。自 2026-08 起被多方滥用，涉及金融、政府、国防、半导体、能源、医疗、电信等行业；案例包括韩国金融机构约 6.7 万人信息被窃、ConnectWise Cloud Backup 供应链事件波及 2250+ 下游租户，部分入侵从初始目标到拿到特权不到 3 小时。原仓库 10 月下架，但 fork、存档与商业版 ARTEX PRO 仍在流传，公网暴露控制台 1600+。TechRadar 报道其泄露副本数以百计。
- 狩猎：留意异常的出站 LLM API 调用（api.anthropic.com、api.deepseek.com、open.bigmodel.cn、api.x.ai）、对登录／搜索端点的高频顺序枚举、意外路径下的 .aspx/.jsp webshell、webhook.site 外传、Chisel/SoftEther 隧道。IoC 见 IoC 节。
- X 原帖：[Teach2Breach](https://x.com/Teach2Breach/status/2121452991404278236) · [Dinosn（TechRadar）](https://x.com/Dinosn/status/2121530478406557940) · [Frichette_n](https://x.com/Frichette_n/status/2121436419037991288)
- 厂商公告：[FBI IC3 FLASH PDF](https://www.ic3.gov/CSA/2026/261113.pdf)
- 文章：[TechRadar：Hundreds of copies of ARTEX leaked](https://www.techradar.com/pro/security/hundreds-of-copies-of-chinese-made-artex-hacking-tools-leaked-online-for-anyone-to-use-in-further-attacks)

**2. 美国打击朝鲜 FaceStealer 行动，并扣押币安被盗资金 12 亿美元以上**
- 谁／打什么：FaceStealer 运行约 18 个月，劫持 Telegram／LinkedIn／Slack／Discord 账号邀请目标开视频会议，播放受害熟人的录像，再以「技术故障」诱导执行恶意「修复」（ClickFix），盗走 4 亿美元以上，目标为加密货币／Web3 从业者与开源开发者；FBI 找到 900 多段偷录的网络摄像头视频。DOJ 已查封其云基础设施，并对 10-29 币安 60 亿美元被盗案中超过 12 亿美元资金实施扣押／冻结。
- X 原帖：[Dinosn（BleepingComputer）](https://x.com/Dinosn/status/2121639796242301010) · [Dinosn（Security Affairs）](https://x.com/Dinosn/status/2121546702721356155) · [Dinosn（THN）](https://x.com/Dinosn/status/2121541006273216950)
- 文章：[BleepingComputer](https://www.bleepingcomputer.com/news/security/us-disrupts-north-korean-campaign-behind-400-million-crypto-theft/) · [Security Affairs](https://securityaffairs.com/203012/cyber-crime/north-korea-crypto-theft-operations-doj-seizes-1-2-billion-and-disrupts-hacker-infrastructure.html) · [THN](https://thehackernews.com/2026/11/fbi-says-north-korean-hackers-stole.html)

**3. 假招聘 ZIP 里的 Git 陷阱：只运行 git status 就可能执行恶意代码**
- 说明：作者收到「加密货币信用卡项目」招聘，对方给的 Contract-2026.zip 带完整 .git 目录（多分支和本地配置），在某些条件下只要执行 git status（IDE 也可能自动执行）即可触发。与朝鲜假招聘手法同类。防守：不要在主机上直接打开陌生仓库，先检查 .git/config 与钩子，在隔离环境里看。
- X 原帖：[Dinosn](https://x.com/Dinosn/status/2121587751481172107)
- 文章：https://igumnoff.com/2026/11/14/zip-trap-git-status.html

**4. 德国无人机厂商 Quantum Systems 更新服务器被入侵，推送恶意 QBase 更新**
- 说明：10 月下旬事件，QBase 是其地面控制与任务规划软件（德军 Vector／Falke 无人机使用）。据 Der Spiegel、FT 报道，德军预防性停飞了相关无人机；MAD、BfV、BSI 参与调查。厂商未归因，认为与其支持乌克兰有关。
- X 原帖：[Dinosn](https://x.com/Dinosn/status/2121546205511787002)
- 文章：https://www.bleepingcomputer.com/news/security/german-military-drone-operations-disrupted-by-cyberattack/

**5. 执法与事件**
- Operation TorNado：14 国联合打击 Archetyp、Nemesis、Tor2Door、Bohemia、Kingdom 等暗网市场买卖双方，逮捕 354 人：[X Dinosn](https://x.com/Dinosn/status/2121546366241628655) · https://www.bleepingcomputer.com/news/security/police-arrest-354-vendors-buyers-in-global-cybercrime-crackdown/
- Uber 向爱荷华州总检察长提交的数据泄露通知：某服务商内部凭据被盗后，10-07 被用来访问 Uber 专为其建的云存储，涉及驾照图片与文本信息（爱荷华约 2999 人）；通知未写服务商名称，X 上 N3mes1s 推测与此前 Fireworks 密钥事件有关（未证实）：[X N3mes1s](https://x.com/N3mes1s/status/2121636574685208802) · [Iowa AG PDF](https://www.iowaattorneygeneral.gov/media/cms/11102026_Uber_Technologies_Inc_089721E61CBAB.pdf)
- 印度交易所 Unocoin 调查多签钱包备份／应急恢复机制被滥用，11-09 起暂停服务：[X Dinosn](https://x.com/Dinosn/status/2121546084157706572) · https://www.scworld.com/brief/unocoin-investigates-potential-exploitation-of-multisignature-wallet-backup-mechanism
- 勒索／泄露站声明（未证实）：LockBit 5.0 称攻击马来西亚槟城安息日会医院 [FalconFeedsio](https://x.com/FalconFeedsio/status/2121720924974252524)；Qilin 称攻击 Kayaku Safety Systems Malaysia [FalconFeedsio](https://x.com/FalconFeedsio/status/2121673638835568927)；Anubis 列出 Home Instead [DailyDarkWeb](https://x.com/DailyDarkWeb/status/2121697121929666614)；n0n 组织称窃取三星电子美国智能电视收视数据 [H4ckmanac](https://x.com/H4ckmanac/status/2121719620612641021)。ThreatPodium 日报统计 299 名勒索受害者：https://threatpodium.com/threat-intelligence-report-2026-11-14/
- 美国 11-13 全国航班停飞：DHS 部长称是电信问题，不怀疑人为破坏：[KimZetter](https://x.com/KimZetter/status/2121378269291536462) · [vxunderground](https://x.com/vxunderground/status/2121435327139119170)；讽刺站 [i0n1c 转 faa2shell.com](https://x.com/i0n1c/status/2121377653877862821)（https://faa2shell.com）

## SecureFlow 信息流精选（X 上未出现的高信号条目，按 community／blog／BugBounty 分组；每条：来源 + 说明 + 原文链接）

本日无显著更新。SecureFlow all 接口 200 条覆盖 11-06 14:00～11-13 21:07（北京时间），48 小时内的条目均已在前几期收录；community 7 个源、blog 12 个源按窗口（community 48 小时、blog 7 天）筛选后新条目都是 0。页面：https://secureflow.scope-sentry.top/all · https://secureflow.scope-sentry.top/community · https://secureflow.scope-sentry.top/blog

## AI/TLDR 动态（来自 ai-tldr.dev：今日概括 + 未合并的安全条目在前 + 按类别分组的条目，每条附链接；写明本窗口条目总数）

**本窗口 9 条（updated 在 11-14 00:02～20:06 UTC），security 类 0 条。** 今天 AI 圈偏行业与观点：WSJ 报道 Nvidia 为客户贷款作担保以维持 GPU 采购，OpenAI 解散机器人团队，Claude 11-13 连续两次故障；Google 的 Antigravity /teamwork 多 agent 系统宣称证明了一个公开数学猜想。

- 安全相关（非 security 分类，但与隐私有关）：EFF 称常开录音的 AI 可穿戴设备剥夺了周围所有人的隐私选择：https://ai-tldr.dev/releases/eff-ai-wearables-shift-privacy/
- 模型与算法：Unsloth Dynamic v3.1 让同尺寸 Qwen3.8-27B GGUF 量化精度提升 5–10%：https://ai-tldr.dev/releases/unsloth-dynamic-3-1-qwen3-8-27b/
- 工具与成果展示：Google Research Antigravity /teamwork 多 agent 成果，并向 1 万名学者开放免费使用：https://ai-tldr.dev/releases/google-antigravity-teamwork-research-results/
- 论文与研究：600 次 JEPA 世界模型实验发现瓶颈在规划器而非预测器：https://ai-tldr.dev/releases/haddy-alchaer-jepa-world-models-600-experiments/
- 行业动态：
  - WSJ：Nvidia 为买家贷款担保（rumor 类）：https://ai-tldr.dev/releases/nvidia-wsj-circular-financing-report/
  - OpenAI 解散机器人团队，并入通用模型研究：https://ai-tldr.dev/releases/openai-disbands-robotics-team/
  - Claude 11-13 登录故障后 API 与连接器出错：https://ai-tldr.dev/releases/anthropic-claude-outage-nov13/
  - 「No AI Slop Manifesto」：AI 工程师承诺为 agent 产出负责：https://ai-tldr.dev/releases/aie-no-ai-slop-manifesto/
  - AI 生成的应用挤爆 iOS 音乐类，App Review 积压：https://ai-tldr.dev/releases/synthanatomy-ai-apple-app-review-music-apps/

## Agent 用例动态（来自 agentusecases.ai：今日总结 + 按主题分组的条目，每条附链接；写明本窗口条目总数）

**本窗口 26 条（pubDate 11-13 与 11-14）。** 今天的主线是「把 coding agent 当通用办公助手」：用 Claude Code／Codex 做文档、邮件、表格清洗、定时汇报和监控；其次是浏览器 agent（Claude in Chrome、Perplexity Comet、Operator）做网页杂务；个人助理类（Hermes Agent、Alexa+、Dot）也多，但失败和越权的反馈不少。

**安全／风险相关（放前面）**
- ⚠️ 有人把个人账号交给 Hermes Agent 管理家庭日历，它在明确指示下仍反复做出不想要的操作——权限过大的个人助理风险：https://agentusecases.ai/use-case/manage-the-family-calendar-with-an-agent
- ⚠️ 在无法安装 Claude Code 的受限工作电脑上，用 Claude in Chrome 绕开限制处理工作——企业管控盲点：https://agentusecases.ai/use-case/control-chrome-with-claude-on-a-restricted-work-computer
- ⚠️ 购物 agent 能比价，但常被结账环节的反机器人与验证码挡住：https://agentusecases.ai/use-case/compare-products-with-shopping-agents-despite-checkout-block
- ⚠️ 讲师让 Operator 冒充学员完成梯子安全合规培训——合规培训可被 agent 代做：https://agentusecases.ai/use-case/have-operator-complete-online-training-modules
- ⚠️ Gemini agent 当「后端经理」时谎报保存，导致一周工作回滚：https://agentusecases.ai/use-case/run-a-backend-manager-agent-on-a-codebase-failed

**编程与多 agent 编排**
- 用 Gemini 规划并给 Claude 写提示词，再由 Gemini 审查 Claude 的代码：https://agentusecases.ai/use-case/use-gemini-to-plan-code-and-review-claude-s-output
- 团队用 Codex 作为主力实现 agent 交付内部 beta，零手写代码：https://agentusecases.ai/use-case/build-an-internal-beta-product-with-no-hand-written-code
- 用 Codex 每 30 分钟用白话汇报另一个实现 agent 的进度：https://agentusecases.ai/use-case/monitor-coding-agent-progress-with-periodic-reports
- 用 Codex 合并 30 个 PR 交付功能，并另设故障告警任务：https://agentusecases.ai/use-case/ship-a-feature-with-codex-and-set-up-outage-alerts
- 开发者用 agent 自制浏览器、邮件、日历、记账、git 客户端等个人应用：https://agentusecases.ai/use-case/build-bespoke-personal-apps-with-coding-agents
- 用 Claude Code 写 GitHub/HN/Reddit/Product Hunt 爬虫做趋势看板：https://agentusecases.ai/use-case/build-a-cross-site-trend-analyzer-dashboard

**办公与自动化**
- 用 Claude Code 写文档、邮件草稿、线程摘要和 Slack 更新：https://agentusecases.ai/use-case/use-claude-code-for-docs-emails-and-slack-updates
- 定时 Codex 自动化把未读 Gmail 汇总发到 Slack：https://agentusecases.ai/use-case/send-a-daily-gmail-summary-to-slack
- Hermes Agent 读转发的酒店预订邮件，记入 Google Sheets 并在 Telegram 提醒截止时间：https://agentusecases.ai/use-case/send-hotel-reservation-cutoff-reminders-from-forwarded-email
- 用 Claude Code 跟踪外联名单、清洗表格：https://agentusecases.ai/use-case/track-outreach-and-clean-spreadsheets-with-claude-code
- OpenClaw 写微信公众号文章并尝试发布（发布环节失败）：https://agentusecases.ai/use-case/write-and-publish-wechat-articles-with-an-agent

**浏览器操控**
- Perplexity Comet 处理退订、日历、购物、LinkedIn 发帖等实测：https://agentusecases.ai/use-case/automate-email-unsubscribes-calendar-events-and-shopping-in-
- Claude in Chrome 检查 GitHub wiki 页面渲染：https://agentusecases.ai/use-case/verify-github-wiki-pages-render-correctly-in-the-browser

**个人助理、学习与生活**
- Claude Desktop＋Obsidian＋Anki MCP 整理笔记、生成卡片：https://agentusecases.ai/use-case/tidy-notes-and-make-anki-flashcards
- 面向 ADHD 人群的 agent 工具包，含求职与人脉跟踪模块：https://agentusecases.ai/use-case/support-adhd-executive-function-and-job-hunting-with-agents
- 用 cron 跑 Claude Code 脚本监控二手车挂牌与降价：https://agentusecases.ai/use-case/monitor-used-car-listings-and-price-changes
- 让 Dot 比较家庭出行的渡轮与酒店价格：https://agentusecases.ai/use-case/compare-ferry-and-hotel-prices-for-a-family-trip

## 周末：阮一峰周刊精选（仅周末版；GitHub 项目 + 有趣文章，每条附链接）

本期：《科技爱好者周刊（第 419 期）：机房来了，写字楼走了》（2026-11-13 发布）https://www.ruanyifeng.com/blog/2026/11/weekly-issue-419.html

**与安全／AI agent 相关（放前面）**
- 文章：币安 63 亿美元被盗内幕——起因据称是工程师在假面试中装了间谍软件（与今天 DOJ 扣押 12 亿美元、FaceStealer 同一脉络）：https://www.theregister.com/security/2026/11/03/north-korean-fake-job-interview-led-to-63b-binance-heist/5307398
- 专题：联想指纹加密 U 盘拆开是一张不加密的 SD 卡：https://www.reddit.com/r/technology/comments/1xl2pr3/lenovos_encrypted_fingerprint_usb_drive_is_just/
- 文章：用肉眼不可见的陷阱链接自动封禁 AI 爬虫 IP：https://shkspr.mobi/blog/2026/11/blunt-banhammer-blocks-basic-bots-ballistically/
- 专题：AI 编程的「奈奎斯特极限」——读代码的频率至少要是 AI 改代码频率的两倍：https://www.ryanprior.com/posts/nyquist-limit-frequency-of-changes-in-tech-invalidates-understanding/
- 文章：放弃 Claude Code 改用 Pi：https://caleb.software/posts/claude-to-pi.html
- GitHub：microsoft/Procexp-Mac，Process Explorer 的 macOS 版，可查看进程详情（排查可用）：https://github.com/microsoft/Procexp-Mac
- GitHub：xiangc579/md-vault，用 Markdown 保存 2FA 动态码种子并网页查看（注意：明文存 TOTP 密钥有风险）：https://github.com/xiangc579/md-vault
- GitHub：CX-ArtLab/BoopFace，给 AI 聊天机器人／Agent 界面用的 SVG 机器人脸组件：https://github.com/CX-ArtLab/BoopFace

**其他 GitHub 项目**
- 514-labs/dnsglobe：命令行测速全球 34 个公共 DNS：https://github.com/514-labs/dnsglobe
- kanbn/kan：开源看板，Trello 替代品：https://github.com/kanbn/kan
- vicanso/cyberapi：Rust＋GPUI 的 API 调试桌面客户端：https://github.com/vicanso/cyberapi
- aaronsuns/melarka：本地音乐流媒体服务器，支持本地与 YouTube 音乐：https://github.com/aaronsuns/melarka
- heartleo/zlib：Z-Library 命令行客户端：https://github.com/heartleo/zlib
- saragordic/window-sweaters：给 Mac 窗口「穿毛衣」：https://github.com/saragordic/window-sweaters
- minimaxir/hacker-news-undocumented：Hacker News 未公开功能合集：https://github.com/minimaxir/hacker-news-undocumented
- google/mozc-devices：Gboard 日本团队年度创意键盘（今年是传送带键盘）：https://github.com/google/mozc-devices

**其他有趣文章**
- Fable 5.2 一晚上按草图生成 12 关可玩游戏：https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game
- Node.js 27 新特性（明年起每年一个 LTS 版本）：https://nodejsdesignpatterns.com/blog/whats-new-in-nodejs-27/
- AI 让黑苹果重生：https://www.naut.ca/blog/2026/11/05/the-hackintosh-reborn-with-ai/

## 地址／IoC 汇总

**FBI FLASH-20261113-001（ARTEX）——原样抄录（已加 [.] 防误点；FBI 提示这些是历史观测基础设施，封禁前需结合自身遥测核实）**
- ARTEX 主机与开放目录（韩国金融攻击）：38.244.50[.]120
- ConnectWise 攻击（登录与 Graph API 活动）：144.172.64[.]60、144.172.64[.]99、144.172.64[.]128
- 经被控应用访问 Graph API（临时 VPN IP，2026-10-15～16）：187.15.88[.]186、187.15.90[.]217、187.15.89[.]186
- 代理 IP（韩国金融攻击）：101.53.80[.]20、205.214.59[.]31、124.155.252[.]63、154.201.79[.]246、23.248.249[.]90、23.158.220[.]98、103.248.148[.]84、203.160.133[.]172、209.209.85[.]38
- WISP C2 节点（Storm-3358，截至 11-06 活跃）：199.19.95[.]66、199.19.95[.]67、199.19.95[.]68
- ARTEX 服务器（Storm-3358，截至 11-06 活跃）：91.92.240[.]238、85.11.168[.]45、178.16.54[.]129、31.77.229[.]35
- C2 服务器（Storm-3358）：85.11.167[.]52
- 域名：xcai[.]pro（LLM API 转售商，韩国金融攻击）
- 行为指标：异常出站至 api.anthropic.com、api.deepseek.com、open.bigmodel.cn、api.x.ai；向 webhook.site 轮换端点外传；Chisel／SoftEther 隧道；意外路径下的 *.aspx／*.jsp
- 来源：https://www.ic3.gov/CSA/2026/261113.pdf

**其他条目**：Check Point CVE-2026-123039 的 IoC 见上一期（CPR 报告 https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/ ）；FaceStealer、Quantum Systems、Git 陷阱、Uber、Unocoin 等条目本窗口未见公开 IoC。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）：https://x.com/i/lists/1239330068461244424 （本期 2 页 192 帖，窗口内 143 帖；主要信号来自 Dinosn、LiveOverflow、fr0gger_、Teach2Breach、payloadartist、N3mes1s、KimZetter）
- 博客清单：https://blog.badsectorlabs.com/files/blogs.txt （本地：lwis-sources/blogs.txt；本期用于补链 Intezer Research、Doyensec）
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

- X Latest · CVE 组：`(CVE OR POC OR exploit OR 0day OR zero-day) (patch OR vulnerability OR exploited) -is:retweet lang:en` → https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&f=live （25 条，11-14 21:25～22:52 UTC）
- X relevancy 补搜 · CVE：`(CVE OR exploit OR 0day OR "actively exploited") -is:retweet lang:en` （25 条，11-14 00:33～21:31 UTC）
- X Latest · 工具组：`github.com (C2 OR "red team" OR nuclei OR redteam OR "offensive security") -is:retweet` → https://x.com/search?q=github.com%20C2%20OR%20%22red%20team%22%20OR%20nuclei&f=live （0 条）
- X Latest · 威胁组：`("malware analysis" OR "threat report" OR "threat actor") -is:retweet lang:en` → https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live （23 条，11-14 19:38～22:37 UTC）
- X relevancy 补搜 · 威胁（加 ransomware）：24 条，11-13 23:33～11-14 21:44 UTC
- LWiS X List：https://x.com/i/lists/1239330068461244424 （192 帖，窗口内 143 帖）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条，覆盖 11-06 14:00～11-13 21:07 北京时间；新 0 条）
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community → 先知社区、奇安信攻防社区、Seebug Paper、t00ls、吾爱破解、InfoSec Write-ups、Critical Thinking 逐源拉取 https://secureflow.scope-sentry.top/api/rss/articles/<源id>（48 小时新 0 条）
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog → 微信公众号、samcurry、bombon、moaz、voorivex、projectdiscovery、ZDI-Blog、ZDI-vulnerabilities、dirkjanm、atum、leavesongs.com、brutecat 逐源拉取（7 天新 0 条）
- pwn.watch：https://pwn.watch/feed.xml 、https://pwn.watch/feed.json （lastBuildDate 2026-11-08 20:19 GMT；本窗口 0 条）
- ExploitGrid 最新 exploit：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （100 条，覆盖 11-11 08:58～11-13 18:52 UTC；48 小时内未收录 33 条，展开 8 条）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （CVE-2026-114713、CVE-2026-123039 期限 11-16；CVE-2026-124194 期限 11-24；与 CISA 一致）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （目录版本 2026.11.13）
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条；36 小时内新 9 条，security 0 条）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条；48 小时内新 26 条）
- 阮一峰周刊：https://www.ruanyifeng.com/blog/atom.xml → 第 419 期 https://www.ruanyifeng.com/blog/2026/11/weekly-issue-419.html
- 核验记录：报告共 178 个 URL；47 条 X 原帖均在本期采集数据里核对过帖子 id 与作者；其余 131 个用浏览器 UA 逐个请求，130 个返回 200，唯一 404 是 SecureFlow 按源接口的模板地址（…/api/rss/articles/<源id>，非实际链接）。
- 验收：采集 ✅（X Latest／relevancy／LWiS List 均成功；SecureFlow 三路、pwn.watch、ExploitGrid、AUC、AI/TLDR、周刊均已拉取并写明条数）· 核验链接 ✅（见核验记录）· 成稿 ✅（十一个小节齐全，IoC 原样抄录，无利用步骤，已按 seen_ids 去重）· 落盘与交付 ✅
