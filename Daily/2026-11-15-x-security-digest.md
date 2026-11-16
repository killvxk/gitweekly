# X 安全情报晚报 · 2026-11-15（周日）

> 报告时间：2026-11-15 约 20:00（America/Santiago），即 2026-11-16 约 07:00（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-14 22:55 UTC 到 11-15 22:55 UTC（24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-15 21:23～22:45 UTC（约 1.4 小时），所以加了 relevancy 补搜 25 条（11-15 01:00～21:56）。
> - 工具组（github.com + C2/红队/nuclei）Latest 只有 **1 条**（且与安全工具无关），工具节主要靠 LWiS List。
> - 威胁组 Latest 25 条（11-15 18:07～22:53）加 relevancy 25 条（11-15 00:30～21:54），以勒索/数据泄露站播报为主。
> - LWiS X List 翻了 2 页共 195 帖，其中 127 帖在窗口内（11-14 22:55～11-15 22:41 UTC），覆盖完整 24 小时。
>
> **其他信源**：SecureFlow all 本窗口 **4 条新条目**（全部是 HackerOne 公开报告，11-15 13:16～22:35 北京时间）；community 7 源、blog 12 源均为 **0 条**。pwn.watch 订阅源仍停在 2026-11-08 20:19 GMT，**本窗口无新条目**。ExploitGrid 数据最新一条是 11-14 19:16 UTC（周末未更新），上期之后未收录的 exploit 共 **54 条**（11-13 22:59～11-14 19:16 UTC），按规则展开 7 条，其余为已报 CVE、老 CVE 重复 PoC 或中低危，只计数。AI/TLDR 本窗口 8 条（security 类 0 条）；Agent Use Cases 本窗口 17 条。
> **CISA KEV**：目录版本 2026.11.13，周末无新增；**今天（11-16 周一）是 Check Point CVE-2026-123039 与 UnrealIRCd CVE-2026-114713 的联邦修补期限**。
> **周末版说明**：本期是周日；阮一峰周刊第 419 期已在周六（11-14）那一期收录，按规则本期不再加周刊节，所以是十个小节。
> **验收**：采集 ✅ · 核验链接 ✅ · 成稿 ✅ · 落盘与交付 ✅（box 与本机 /Users/kenny1337/Desktop/_05_项目/X安全情报晚报/ 均已写入）。

## 今日摘要

- **Cursor 公布安全事件报告**：攻击者先从 AI 基础设施商 Fireworks AI 拿到访问密钥，复制了 Cursor 共享给它的存储桶（内含 2025 年为主的历史 coding-agent 轨迹，部分带未脱敏的 API 凭据），再用这些凭据进入 Cursor 内部系统，10-29 在 Cursor 的 VS Code 扩展市场缓存里放上恶意 Claude Code 扩展 2.1.312／2.1.313（上架约 11 小时，最多约 5000 名开发者受影响，会装持久化 SSH 后门）。
- **Linux 内核 NoisyTCP（CVE-2026-99288）公开**：v4bel 披露 TCP 收包路径的竞争条件，对默认配置的 Nginx/Apache/SSH 等普通 TCP 监听即可远程、免认证触发（至少可致整机内核崩溃，理论上可 UAF）；修复提交 4e2b3ef19e0e（2026-11-03），embargo 已结束。
- **今天是两个 KEV 的修补期限**：Check Point Gaia CVE-2026-123039（与 PHP2Shell 串联）和 UnrealIRCd CVE-2026-114713，X 上仍在密集提醒；ExploitGrid 周末又收录了多份 UnrealIRCd 与 PHP2Shell 相关仓库（含扫描器、YARA）。
- **N-able N-central「4EverAble2Shell」**：公开 exploit 后数小时内即被利用，大多数被攻陷的服务器已装 11-10 的 Hotfix 2；缓解措施是关闭 Legacy API。
- **数据泄露与勒索**：n0n 勒索组声称从 Expedia 偷走近 10 亿旅客记录（Expedia 确认经第三方数据平台被供应链入侵，数字未确认），并在泄露站新挂 Starbucks、Samsung、Gap 等；TSMC 确认员工数据经云服务商泄露；La Poste 子公司 Maileva 泄露 2200 万人姓名地址。
- **ARTEX 后续**：MalwareMustDie 发布 TLP:CLEAR 的 ARTEX 检测签名包（v1.1.3，合并 FBI FLASH 与 Sophos 指标）；爱沙尼亚把 11-14 针对国防企业 Threod Systems 的纵火未遂归因于俄 GRU。

## CVE / POC / 漏洞（每条：说明 + 地址列表；合并 X、KEV、pwn.watch、ExploitGrid 的补丁状态与公开 exploit 情况）

### 1. Linux 内核 NoisyTCP：TCP 免认证远程内存破坏（CVE-2026-99288）
- 说明：研究者 Hyunwoo Kim（@v4bel）公开公告。漏洞在 TCP 收包路径（stale ehash 查找与 request socket 释放/重分配并发），对「普通」TCP 监听即可远程、免认证触发；在多 RX 队列或启用 RPS 的服务器上，至少可导致空指针解引用使整机内核 panic（容器里的服务被打也会拖垮宿主机），另一条路径是较难触发的远程 UAF。作者称这个问题潜伏约 11 年。
- 补丁状态：上游修复提交 **4e2b3ef19e0e（2026-11-03）**，公告里另有临时缓解（防御者应优先打内核补丁，关注发行版内核更新）。KEV：未收录。ExploitGrid：本窗口未见收录。
- 地址：
  - X 原帖：https://x.com/v4bel/status/2122006607378972745
  - 公告（GitHub）：https://github.com/V4bel/NoisyTCP
  - NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-99288

### 2. Check Point Gaia CVE-2026-123039 与 UnrealIRCd CVE-2026-114713：KEV 期限就是今天（11-16）
- 说明：两者都在 11-13 进入 CISA KEV，联邦期限 11-16。Check Point 是 Gaia 本地提权到 root（已与 PHP2Shell 串联用于攻击链），X 上转述的修复版本为 R82.20 T14、R82.10 T52、R82 T132、R81.20 T174（以 Check Point 官方公告为准）；UnrealIRCd 为服务器级命令注入，已被利用。
- 公开 exploit：ExploitGrid 周末新收录 UnrealIRCd CVE-2026-114713 相关仓库 3 份（含 PoC、扫描器）；PHP2Shell（CVE-2026-109618/109619）新增 2 份（调查/实验环境类）。只记录「已有公开 exploit」，不链仓库。
- 地址：
  - X 原帖：https://x.com/qubit0/status/2121946134658584689 、https://x.com/TheExploitHQ/status/2122086366032847026 、https://x.com/ProferoSec/status/2121925176812302427 、https://x.com/0xdarkbear/status/2122079330024947802
  - CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  - ExploitGrid：https://exploitgrid.net/vulnerabilities/CVE-2026-114713 、https://exploitgrid.net/vulnerabilities/CVE-2026-123039 、https://exploitgrid.net/vulnerabilities/CVE-2026-109618

### 3. N-able N-central「4EverAble2Shell」：exploit 公开数小时内被利用
- 说明：漏洞链可让未认证攻击者拿到 N-central 服务器 root；exploit 代码 11-12 公开后数小时内即出现利用，研究者发现的被攻陷服务器多数已装 11-10 发布的 Hotfix 2。只有开启 Legacy API 时可利用；N-able 已限制部分功能、预防性关闭 Intune 集成，并要求本地部署客户确认 Legacy API 已关闭，且称已发现更多 IoC。
- 防御：立刻核查 Legacy API 设置；按 N-able 后续公告排查入侵迹象。
- 地址：
  - X 原帖：https://x.com/kbytech/status/2122088254140821734 、https://x.com/ernesttheaiguy/status/2122078451205116136
  - 文章：https://www.kbytechnologies.com/news-security/n-able-n-central-zero-day-exploited-november-2026

### 4. Android 11 月公告：Framework 严重 RCE（CVE-2026-58868）
- 说明：X 上转述 Google 公告：CVE-2026-58868 影响 Android 14–17，无需额外权限或用户交互；11-05 及以后的补丁级别修复；Pixel 公告另列 IMS 高危 RCE CVE-2026-55335。
- 地址：
  - X 原帖：https://x.com/nurhayatdev/status/2122092315254616481
  - 厂商公告：https://source.android.com/docs/security/bulletin/2026/2026-11-01

### 5. Integra32 门禁安全管理系统 .NET Remoting RCE（CVE-2026-63079，CVSS 9.3，暂无补丁）
- 说明：RBH Access Technologies Integra32 5.1.11 R5.0 及更早版本，TCP 2001 端口暴露已弃用的 .NET Remoting 服务时，未认证攻击者可发送构造的序列化数据以 SYSTEM 执行代码；暂无修复版本，缓解是限制 2001 端口的网络访问。
- 地址：
  - X 原帖：https://x.com/cvedotnow/status/2122093184029262100
  - 文章：https://cve.now/CVE-2026-63079

### 6. 新 CVE 已有公开 exploit（来源：ExploitGrid，11-14 收录，均为 CRITICAL）
- **Directus < 12.1.0（CVE-2026-126539，9.2）**：公开模式 WebSocket 连接下发送失败的认证消息即可绕过权限检查，未认证读/改/删任意集合记录；修复版 12.1.0。
  - 厂商公告：https://github.com/directus/directus/security/advisories/GHSA-97xr-jchp-xm3c
  - ExploitGrid：https://exploitgrid.net/exploits/EGE-GH-rIMBoIx
- **Craft CMS（CVE-2026-115934，9.3）**：使用 craft.search 的站点前台存在未认证 SQL 注入（仅 MySQL/MariaDB），可堆叠查询升到管理员；修复版 5.11.2。
  - 厂商公告：https://github.com/craftcms/cms/security/advisories/GHSA-qcvp-ggx3-97r6
  - ExploitGrid：https://exploitgrid.net/exploits/EGE-GH-p5zqpD4
- **OpenEMR < 8.4.0（CVE-2026-126473，9.3）**：OAuth scope 规范化缺陷，未认证攻击者可拿到未批准的系统级 FHIR 权限读写患者记录；修复版 8.4.0。
  - 厂商公告：https://github.com/openemr/openemr/security/advisories/GHSA-6xh3-fmm5-jjp4
  - ExploitGrid：https://exploitgrid.net/exploits/EGE-GH-Ix3j8my
- **Payload CMS form-builder 插件（CVE-2026-105857，10.0）**：构造的表单提交可在服务器执行代码；修复版 3.90.0 / 4.0.0-canary.34。
  - 厂商公告：https://github.com/payloadcms/payload/security/advisories/GHSA-r488-j9vj-wx3q
  - ExploitGrid：https://exploitgrid.net/exploits/EGE-GH-ARETKFa
- **MongoDB Node.js 驱动（CVE-2026-126837，9.1）**：mongodb+srv:// 的 DNS SRV 主机校验缺陷，可能让驱动连到预期域名之外的主机。
  - 厂商：https://jira.mongodb.org/browse/NODE-7830
  - ExploitGrid：https://exploitgrid.net/exploits/EGE-GH-q05IMqI
- **NocoDB < 2026.08.0（CVE-2026-126274 等 3 个）**：已认证 Creator 可在表/列标题注入存储型 XSS；ExploitGrid 同日收录 CVE-2026-126269／126273／126274 三份。
  - 厂商公告：https://github.com/nocodb/nocodb/security/advisories/GHSA-638g-xw92-xq9x
  - ExploitGrid：https://exploitgrid.net/exploits/EGE-GH-2hrA690
- 其余只计数：GPUStack、OpenMage、jDownloads、AutomatorWP、Apache（CVE-2026-74756／68982）、sipcapture、Ajenti、Tenda HG21 等新 PoC 仓库；Apache mod_http2 CVE-2026-119618（4 份，含扫描器/YARA）、Control Web Panel、Synology、Fortinet 等此前已报 CVE 的重复仓库。

### 7. 周末 X 上的其他提醒（均已收录于 KEV，作复核）
- Microsoft 11 月补丁日 Outlook 零日 CVE-2026-124194（泄露 NTLMv2 哈希，KEV 期限 11-24）：https://x.com/ido_cohen2/status/2121981787144438270 、https://x.com/Lumideezy/status/2122065733274284416
- Chrome 今年第 8 个在野零日 CVE-2026-125350（KEV 期限 11-24）：https://x.com/PaidFreeDroid/status/2121850455646937118 、https://lifeboat.com/blog/2026/11/google-issues-chrome-security-update-for-eighth-actively-exploited-zero-day-of-2026
- SonicWall SSL-VPN SAML MFA 绕过 CVE-2026-19868（KEV 期限 11-20）：https://x.com/HotaSamit/status/2121939404206026979
- Citrix NetScaler 认证绕过被利用（文中编号 CVE-2026-19490）：https://x.com/systemforce/status/2121891035764727826 、https://systemforce.co.uk/blog/2026/11/15/citrix-netscaler-cve-2026-19490-authentication-bypass-attack/
- 回顾分析：Interlock 勒索组 1 月起把 Cisco FMC CVE-2026-20131 当零日利用（KEV 3 月已收录）：https://x.com/Dinosn/status/2121805285237108954 、https://blog.securelayer7.net/cve-2026-20131-cisco-fmc-rce/
- 注：X 上有账号把 SharePoint CVE-2026-50522 当新闻转发，实际 KEV 7 月已收录，非新事件。

## 工具与 GitHub 发布（每条：说明 + 地址列表）

1. **Red Hat prodsec-skills**：Red Hat 产品安全团队发布给 AI 编程助手和 agent 系统用的安全技能集（Dinosn 转发，266 赞）。
   - X 原帖：https://x.com/Dinosn/status/2121967167184752962
   - GitHub：https://github.com/RedHatProductSecurity/prodsec-skills
2. **Suture**：Windows implant 开发框架，用于进攻工程与 C2 研究，基于 Crystal Palace 生成 PIC 加载器＋模块化载荷（85 赞）。
   - X 原帖：https://x.com/ipurple/status/2121885636856827983
   - GitHub：https://github.com/racoten/suture-pic
3. **emp3r0r 新增「自改写」C2 与自主 EDR 规避**：作者借用 ARTEX 的 harness 做循环，持续改写载荷直到高遥测特征消失（154 赞）。防御方应关注 AI 驱动的载荷变形对签名检测的影响。
   - X 原帖：https://x.com/jm33_m0/status/2121951893404704972
   - GitHub：https://github.com/jm33-m0/emp3r0r
4. **M365Pwned**（OtterHacker）：用应用级 OAuth 令牌经 Microsoft Graph 枚举/搜索 M365 邮件与 SharePoint 的红队 GUI 工具。
   - X 原帖：https://x.com/DirectoryRanger/status/2121984058175730003
   - GitHub：https://github.com/OtterHacker/M365Pwned
5. **TokenSmith**（JUMPSEC）：在授权测试中生成 Entra ID access/refresh token。
   - X 原帖：https://x.com/DirectoryRanger/status/2121982266566172754
   - GitHub：https://github.com/JumpsecLabs/TokenSmith
6. **ShareHound**（Podalirius）：用 BloodHound OpenGraph 映射网络共享权限。
   - X 原帖：https://x.com/DirectoryRanger/status/2121982792552833438
   - GitHub：https://github.com/p0dalirius/sharehound
7. **NEBULA**（MHaggis）：交互式 PowerShell TUI，用于测试 Windows 执行技术、COM、WMI 与 LOLBAS（适合检测工程验证）。
   - X 原帖：https://x.com/DirectoryRanger/status/2121982991777833194
   - GitHub：https://github.com/MHaggis/NEBULA
8. **Hayabusa CODE BLUE 版 + Windows 事件日志配置指南**（Yamato Security，防御向 DFIR）。
   - X 原帖：https://x.com/DirectoryRanger/status/2121981291172110495 、https://x.com/DirectoryRanger/status/2121979761232576916
   - GitHub：https://github.com/Yamato-Security/hayabusa 、https://github.com/Yamato-Security/EnableWindowsLogSettings
9. **Swarmerz**（Secorizon）：把多个独立模型组成「蜂群」做源码审计与漏洞研究的终端工具。
   - X 原帖：https://x.com/Teach2Breach/status/2121863941932384398
   - 文章：https://blog.secorizon.com/2026/11/secorizonai-research-swarmerz-release.html
10. **研究文章**：Praetorian 公开 Swarmer（利用强制用户配置文件低权限隐蔽改注册表做持久化）；逆向微软签名 rootkit Netfilter 驱动；Defender for Endpoint 时间线内部机制；Windows 服务失败恢复用于规避检测。
    - X 原帖：https://x.com/DirectoryRanger/status/2121982555952205958 、https://x.com/DirectoryRanger/status/2121980291560751465 、https://x.com/DirectoryRanger/status/2121982618665357529 、https://x.com/DirectoryRanger/status/2121985317565772138
    - 文章：https://www.praetorian.com/blog/corrupting-the-hive-mind-persistence-through-forgotten-windows-internals/ 、https://splintersfury.github.io/mal_blog/post/netfilter_driver/ 、https://kqlquery.com/posts/defender-endpoint-timeline-internals/ 、https://hackers-arise.com/defense-evasion-recoverit-using-windows-service-failure-recovery-to-evade-detection/
11. **Java Unicode 转义把注释变成可执行代码**：代码审查时要注意 \u000a 等转义（供应链/代码审计意义）。
    - X 原帖：https://x.com/Dinosn/status/2122073198846169254
    - 文章：https://octri.dev/blog/java-unicode-escape-comment
12. **IDA Pro 新的恶意软件分析插件**（Hex-Rays 直播演示：识别加壳并辅助脱壳、在全系统 Windows 环境中安全单步）。
    - X 原帖：https://x.com/HexRaysSA/status/2122080310083145872

## APT / Malware 分析（每条：说明 + 地址列表）

1. **Cursor 安全事件：经 Fireworks AI 密钥泄露→内部系统→恶意 Claude Code 扩展（供应链）**
   - 说明：攻击者用 Fireworks AI 上存放的访问密钥复制了 Cursor 的只读共享存储桶（历史 coding-agent 轨迹，来自未开 Privacy Mode 的用户，部分含未脱敏 API 凭据；Cursor 称涉及不到 0.05% 用户，凭据泄露不到 0.01% 客户），继而窃取归档非生产源码仓库、部分客服邮件、客户曾提供给客服的凭据等。10-29 攻击者用窃得凭据把恶意 Claude Code 扩展 2.1.312／2.1.313 放进 Cursor VS Code 扩展市场缓存，约 11 小时后下架；恶意代码会收集系统信息、写入攻击者 SSH 公钥、尝试开启 SSH 并持久化（研究者发现代码错误使其在不少 Windows/macOS 上未生效）。Anthropic 正版扩展与 Open VSX 未受影响。
   - 防御：10-29 期间在 Cursor 里装过/更新过 Claude Code 扩展的，检查 authorized_keys 与 SSH 服务状态、轮换凭据。
   - X 原帖：https://x.com/Dinosn/status/2121805144841187753
   - 厂商公告：https://cursor.com/blog/security-incident-update
   - 文章：https://www.bleepingcomputer.com/news/security/cursor-confirms-security-breach-led-to-malicious-claude-code-extension/ 、https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/
2. **ARTEX 后续：检测签名包与更多研究**
   - 说明：MalwareMustDie 以 TLP:CLEAR 发布 ARTEX 检测签名包（MMD-072-2026，已更新到 v1.1.3，合并 FBI FLASH 与 Sophos X-Ops 指标，附 OpenIOC 与测试脚本）；Microsoft 威胁情报观察到攻击者用 ARTEX 在公开 GitHub 仓库里搜寻泄露凭据（cyb3rops 转推）；有研究者称在 ARTEX、strix 等多款 AI 渗透 agent 上拿到 RCE（maxime_tz 转推）。BleepingComputer 跟进 FBI 警告。
   - X 原帖：https://x.com/ipurple/status/2122046880498532834 、https://x.com/Dinosn/status/2122073124153749951 、https://x.com/cyb3rops/status/2121999008176718101 、https://x.com/maxime_tz/status/2121929139707937074
   - 文章：https://blog.malwaremustdie.org/2026/11/mmd-072-2026-artex-detection-signature.html 、https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/
   - GitHub（检测规则）：https://github.com/unixfreaxjp/malwaremustdie
3. **n0n 勒索/勒索组：Expedia 近 10 亿记录（供应链）＋新挂 Starbucks、Samsung、Gap**
   - 说明：新成立的俄语勒索组 n0n 声称从 Expedia 偷走近 10 亿旅客记录；Expedia 向 Skift 确认是经被入侵的第三方数据平台进入其系统（同一供应链事件还影响多家公司），但未确认数量。周末 n0n 泄露站又挂出 Starbucks、Samsung、Gap 等品牌。
   - X 原帖：https://x.com/Dinosn/status/2121805209932304481 、https://x.com/DailyDarkWeb/status/2122062776915079366 、https://x.com/CTI__Updates/status/2122046985587065213
   - 文章：https://securityaffairs.com/203062/cyber-crime/extortion-group-claims-theft-of-nearly-one-billion-expedia-traveler-records.html
4. **TSMC 员工数据经云服务商泄露**
   - 说明：11-08 有人以「SmithBianl」名义在黑客论坛拍卖 6.9GB 据称来自 TSMC 的数据；TSMC 向 SEC 申报确认数据与其在云服务商系统中的数据一致，影响现任及前员工，未发现自身系统被入侵。
   - X 原帖：https://x.com/Dinosn/status/2121990392836972863
   - 文章：https://www.bleepingcomputer.com/news/security/tsmc-employee-data-breach-linked-to-cloud-provider/
5. **La Poste 子公司 Maileva 泄露 2200 万人姓名与地址**
   - 说明：9 月中旬遭攻击，受影响的是通过 Maileva 寄送文件的收件人（含社会住房租户、医学检验患者），银行信息未泄露，已通报 CNIL。
   - X 原帖：https://x.com/Dinosn/status/2121938299476377837
   - 文章：https://securityaffairs.com/203126/data-breach/data-breach-at-la-poste-subsidiary-maileva-affects-22-million-people-in-france.html
6. **爱沙尼亚：GRU 指使针对国防企业 Threod Systems 的纵火未遂**
   - 说明：11-14 凌晨针对无人机厂商 Threod Systems 的破坏未遂，爱沙尼亚外长与安全警察（KAPO）政治归因于俄罗斯 GRU，拉脱维亚 VDD 协助。
   - X 原帖：https://x.com/SwitHak/status/2122006558032773358 、https://x.com/SwitHak/status/2122003105562644885
7. **勒索泄露站播报（未核实，只记名单）**：PixelLeaks 连续挂出多家印度制造企业（Godrej & Boyce、Connectwell、PlasmaGen）；Qilin 挂美国国防航天制造商 Apex Technology；INC RANSOM 挂印尼 PT Sarimelati Kencana；LockBit 5.0 挂马来西亚 Penang Adventist Hospital；另有声称的 Chaoxing（超星）9200 万记录、哈萨克斯坦最高法院 5.07 亿记录、坎昆市政府 400GB 等数据售卖帖。
   - X 原帖：https://x.com/FalconFeedsio/status/2122067619901845965 、https://x.com/FalconFeedsio/status/2122049471278399838 、https://x.com/FalconFeedsio/status/2121973609195549009 、https://x.com/digvijay_k11/status/2121807229481623693 、https://x.com/MonThreat/status/2121915588855390596 、https://x.com/DailyDarkWeb/status/2122084933657366670 、https://x.com/DailyDarkWeb/status/2122090145692205432
8. **Hunt.io 每日：凭据钓鱼基础设施**：vysecurity 披露一台以「商务合作」为诱饵收集凭据的钓鱼服务器（地址见 IoC 节），对方还泄露了自己的 Gmail SMTP 凭据。
   - X 原帖：https://x.com/vysecurity/status/2122003718757609945
9. **The DFIR Report 引文**：一起入侵中 more_eggs 是主要 C2 流量，后转为 Cobalt Strike，Pyramid C2 仅用过一次。
   - X 原帖：https://x.com/TheDFIRReport/status/2122087644955918401

## SecureFlow 信息流精选（X 上未出现的高信号条目，按 community／blog／BugBounty 分组；每条：来源 + 说明 + 原文链接）

- **community**：本日无显著更新（7 个源 48 小时内 0 条新文章）。
- **blog**：本日无显著更新（12 个源 7 天内无未收录新文章）。
- **BugBounty（HackerOne 公开报告，来自 all 接口）**：
  - [$10000] 通过自定义 JS tracer（Boa 引擎）未认证远程终止 Arc RPC 节点进程，造成持续 DoS：https://hackerone.com/reports/3966160
  - 项目备份导入时角色恢复未过滤导致提权：https://hackerone.com/reports/4081135
  - 通过 X-Forwarded-For 绕过匿名 API 限速：https://hackerone.com/reports/4059744
  - 匿名翻译建议经 Change API 暴露 IP 地址：https://hackerone.com/reports/4117330

## AI/TLDR 动态（来自 ai-tldr.dev：今日概括 + 未合并的安全条目在前 + 按类别分组的条目，每条附链接；写明本窗口条目总数）

今天 AI 圈是周末节奏：DeepSeek 把联网搜索、文件输入和安全检查做进 API；开源侧有可边听边说的 Haru-4B 语音模型和 Chrome DevTools MCP 1.13（给编程 agent 加日志点与网络 mock）；评论文章集中讨论黄仁勋离开对美国开源模型的影响。本窗口共 **8 条**，security 类 0 条。

- **安全**：本窗口无 security 类条目。（AI 相关安全事件见上文 Cursor 供应链事件与 ARTEX。）
- **模型**：
  - Haru-4B：Apache-2.0 的开源语音模型，可以边听边说：https://ai-tldr.dev/releases/higurashi-haru-4b/
- **工具与开源仓库**：
  - DeepSeek App API：把网页搜索、文件输入和安全检查直接做进 API：https://ai-tldr.dev/releases/deepseek-app-capabilities-api/
  - Chrome DevTools MCP 1.13.0：agent 可给运行中的页面加日志点、模拟网络响应：https://ai-tldr.dev/releases/chrome-devtools-mcp-1-13-0/
  - Plannotator：在浏览器里审阅编程 agent 的计划与 diff：https://ai-tldr.dev/releases/plannotator-v0-28-64/
  - deepseek-v3-jax：190 行纯 JAX 复现 DeepSeek V3 核心思路：https://ai-tldr.dev/releases/deepseek-v3-jax-190-lines/
- **论文与研究**：
  - Sebastian Raschka 讲解现代 LLM 的位置编码（RoPE 逐步实现）：https://ai-tldr.dev/releases/sebastian-raschka-positional-embeddings-nov15/
- **行业动态**：
  - Nathan Lambert：黄仁勋离开是美国开源模型的挫折：https://ai-tldr.dev/releases/interconnects-open-source-ai-without-jensen/
  - Jakub T. Jankiewicz：AI 生成的代码都应开源：https://ai-tldr.dev/releases/jankiewicz-ai-generated-code-open-source/

## Agent 用例动态（来自 agentusecases.ai：今日总结 + 按主题分组的条目，每条附链接；写明本窗口条目总数）

今天的用例以「编程 agent 做应用」和「无代码自动化 agent（n8n、Zapier Agents）替代固定流程」为主，另有多 agent 编排一次性造产品、个人生活助理（订餐、比价、膳食计划）和内容生产。值得注意的安全向做法是把运维 agent 关在只读沙箱里、只提出修复计划。本窗口共 **17 条**，全部列出。

- **安全相关（放前面）**：
  - 用一个被 snap 限制、只读的 MCP agent（Maat）诊断 Ubuntu 问题，修复计划经 polkit 由用户确认后才执行：https://agentusecases.ai/use-case/diagnose-ubuntu-problems-with-a-confined-read-only-agent
  - 有人为信息安全、AI 等快速变化的话题各开一个 agent 专门跟踪新闻：https://agentusecases.ai/use-case/track-fast-moving-news-topics-with-dedicated-agents
- **编程与多 agent 编排**：
  - 开发者用 Claude Code、ChatGPT 让主编排 agent 按大规格书把模块分给子编排和 worker，做出网店、SaaS 和 Steam 游戏：https://agentusecases.ai/use-case/orchestrate-parallel-ai-workers-to-build-products-from-a-spe
  - 用 GitHub Copilot 加脚手架 agent 生成带 CRUD 和 20 条种子数据的员工目录应用：https://agentusecases.ai/use-case/build-a-crud-employee-directory-app-with-copilot-handoffs
  - Copilot 先出计划、批准后 Agent 模式自动改代码：https://agentusecases.ai/use-case/plan-then-implement-code-changes-with-copilot-agent-mode
  - 运维 agent 在空闲时自己做了一个基础设施看板：https://agentusecases.ai/use-case/build-an-infrastructure-dashboard-with-an-agent
- **文档与数据处理**：
  - 用 Claude Code／Codex 技能把扫描件重建成带真实文字和矢量图的 PDF：https://agentusecases.ai/use-case/rebuild-scanned-pages-as-vector-pdfs
  - 用 Claude Code 识别扫描乐谱，效果胜过其他 OCR：https://agentusecases.ai/use-case/ocr-scanned-sheet-music-with-claude-code
  - ChatGPT Agent 逐个调研公司并填进 CRM（比 Operator 快）：https://agentusecases.ai/use-case/research-companies-and-fill-a-crm-from-a-lead-list
- **无代码自动化与客服**：
  - 用一个 Zapier Agent 替换 8 个固定 Zap：https://agentusecases.ai/use-case/replace-eight-zaps-with-a-single-ai-agent
  - Zapier Agent 检查当天帖子是否已发、分析文案：https://agentusecases.ai/use-case/automate-daily-post-checks-and-publishing-logic
  - 客服工程师用 n8n 调研工单、起草回复并从已关闭工单学习：https://agentusecases.ai/use-case/draft-support-ticket-responses-from-research
  - 语音 agent 把任务交给 n8n，写每日 AI 简报并改编成推文串和视频脚本：https://agentusecases.ai/use-case/run-newsletter-and-content-repurposing-with-a-voice-agent
- **个人助理与购物**：
  - 用 ChatGPT／Claude 描述披萨订单，确认后由语音 agent 打电话下单：https://agentusecases.ai/use-case/order-pizza-by-voice-agent-from-chatgpt-or-claude
  - 用 Claude 比较同一酒店在多个网站含税费的总价：https://agentusecases.ai/use-case/compare-hotel-total-costs-including-taxes-and-fees
  - 家长用 Zapier Agent 加 Google Sheet 记忆做不重复的幼儿膳食计划：https://agentusecases.ai/use-case/plan-toddler-meals-without-repeats
- **内容创作**：
  - 5 人团队用短剧 agent 在 8 天内把 4 万字剧本做成 60 集短剧：https://agentusecases.ai/use-case/produce-a-60-episode-short-drama-from-a-script

## 地址／IoC 汇总

- 钓鱼/凭据收集服务器（vysecurity / Hunt.io，原样抄录）：`http://195.133.61[.]76`
  - 来源：https://x.com/vysecurity/status/2122003718757609945
- Conviction vault 被盗（pMINT 披露，事件发生于 11-04 07:20 UTC，原样抄录）：
  - Vault：`0x87fA4f1403a01b82cBc8E1d147f3E945679373fb`
  - 攻击者钱包：`0xA4a92da5E434c63B8Eb670A5f46CE4a6Eee3b669`
  - 来源：https://x.com/pMINT_pDAI/status/2122084345795969072
- Cursor 恶意扩展：Claude Code 扩展 **2.1.312、2.1.313**（经 Cursor 扩展市场缓存分发，10-29 约 11 小时），行为是写入攻击者 SSH 公钥并持久化；公开报道未给出公钥/C2 原文，见 https://cursor.com/blog/security-incident-update
- ARTEX：MalwareMustDie 签名包附大量 IP 与 OpenIOC（与 FBI FLASH-20261113-001 指标重合，FLASH 指标已在 11-14 期抄录），完整列表见 https://blog.malwaremustdie.org/2026/11/mmd-072-2026-artex-detection-signature.html
- 泄露站播报中的受害者域名为企业官网（starbucks[.]com、samsung[.]com 等），不是攻击基础设施，不作为 IoC。
- 其他条目：未见公开 IoC。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）：https://x.com/i/lists/1239330068461244424 （本期 2 页 195 帖，窗口内 127 帖；主要信号来自 Dinosn、DirectoryRanger、v4bel、ipurple、jm33_m0、SwitHak、vysecurity、Teach2Breach）
- 博客清单：https://blog.badsectorlabs.com/files/blogs.txt （本地：lwis-sources/blogs.txt；本期用于补链 Praetorian、MalwareMustDie）
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

- X Latest · CVE 组：`(CVE OR POC OR exploit OR 0day OR zero-day) (patch OR vulnerability OR exploited) -is:retweet lang:en` → https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&f=live （25 条，11-15 21:23～22:45 UTC）
- X relevancy 补搜 · CVE：`(CVE OR exploit OR 0day OR "actively exploited") -is:retweet lang:en` （25 条，11-15 01:00～21:56 UTC）
- X Latest · 工具组：`github.com (C2 OR "red team" OR nuclei OR redteam OR "offensive security") -is:retweet` → https://x.com/search?q=github.com%20C2%20OR%20%22red%20team%22%20OR%20nuclei&f=live （1 条，无关）
- X Latest · 威胁组：`("malware analysis" OR "threat report" OR "threat actor") -is:retweet lang:en` → https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live （25 条，11-15 18:07～22:53 UTC）
- X relevancy 补搜 · 威胁（加 ransomware）：25 条，11-15 00:30～21:54 UTC
- LWiS X List：https://x.com/i/lists/1239330068461244424 （195 帖，窗口内 127 帖）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条，覆盖 11-06 14:00～11-15 22:35 北京时间；48 小时内新 4 条）
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community → 先知社区、奇安信攻防社区、Seebug Paper、t00ls、吾爱破解、InfoSec Write-ups、Critical Thinking 逐源拉取 https://secureflow.scope-sentry.top/api/rss/articles/<源id>（48 小时新 0 条）
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog → 微信公众号、samcurry、bombon、moaz、voorivex、projectdiscovery、ZDI-Blog、ZDI-vulnerabilities、dirkjanm、atum、leavesongs.com、brutecat 逐源拉取（7 天新 0 条）
- pwn.watch：https://pwn.watch/feed.xml 、https://pwn.watch/feed.json （lastBuildDate 2026-11-08 20:19 GMT；本窗口无新条目）
- ExploitGrid 最新 exploit：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （100 条，最新 11-14 19:16 UTC；未收录 54 条，展开 7 条）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （CVE-2026-114713、CVE-2026-123039 期限 11-16；CVE-2026-124194 期限 11-24；与 CISA 一致）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （目录版本 2026.11.13，周末无新增）
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条；36 小时内新 8 条，security 0 条）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条；48 小时内新 17 条）
- 阮一峰周刊：本期为周日，第 419 期已于 11-14 期收录，本期不加此节。
- 核验记录：报告共 154 个可核验 URL（不含 X 搜索页与 SecureFlow 模板地址）；53 条 X 原帖均在本期采集数据里核对过帖子 id 与作者；其余 101 个用浏览器 UA 逐个请求，100 个返回 200，唯一例外是 IoC 节里做了去武装处理的钓鱼服务器地址 http://195.133.61[.]76（刻意不访问）。t.co 均已展开；DFIR Report 帖内 t.co 只指向图片，故只列原帖。
- 验收：采集 ✅（X Latest／relevancy／LWiS List 均成功；SecureFlow 三路、pwn.watch、ExploitGrid、AUC、AI/TLDR 均已拉取并写明条数）· 核验链接 ✅（见核验记录）· 成稿 ✅（十个小节齐全（周日不含周刊节），IoC 原样抄录，无利用步骤，已按 seen_ids 去重）· 落盘与交付 ✅（box 与本机副本均已写入并读回确认）
