# X 安全情报晚报 · 2026-11-07

覆盖窗口：2026-11-06 20:15 至 2026-11-07 约 20:20（America/Santiago，UTC-3），约 24 小时（窗口内最晚收录帖为 20:07）。X 只读读取 **14** 次（search_posts_all 主题检索 ×3、高信号／LWiS 成员 `from:` 抽样 ×3、昨日要点与新 CVE 定向 ×5、get_posts_by_ids ×1、search_news ×1、事件定向 ×1），**0 次 429**；与 state.json seen_ids 去重，过滤广告、空转发与明显诈骗帖（如 Instagram 引流「NEXTSH」所谓全国级 0day 工具帖，未收录）。t.co 已用 `curl -sI` 展开。公开备援：CISA KEV JSON（**2026.11.06，共 1769 条，Δ0**，周六无更新）、NVD API、SecurityWeek、BleepingComputer、Securelist、Infosecurity、watchTowr Labs、samcurry.net 等。IoC 一律 defang。本报告为防御向，不转载利用代码、payload 或复现步骤。

## 今日摘要

- **CISA KEV 今日无更新（2026.11.06／1769／Δ0）**：WordPress Core **CVE-2026-119977** 联邦期限 11-06 已过，转入逾期；下周一 **11-10** 到期 Google（Brotli）CVE-2026-111497、Adobe CVE-2026-48356，11-11 Broadcom CVE-2026-41709，11-13 Ivanti CVE-2026-118527；SonicWall CVE-2026-19868 due 11-20。
- **OpenSSH *sshole（CVE-2026-123158）在野利用面扩大**：watchTowr Intel 确认观测到利用（「目前是僵尸网络和挖矿」）；GreyNoise 传感器数据持续被引用；ProjectDiscovery nuclei 已有检测模板 PR。受影响面不止 Alpine，SecurityWeek 点名 OpenWrt、Buildroot、Yocto 等 musl 无 PAM 系统。仍须 **10.6p2／发行版补丁 + 重启 sshd**，或 `PasswordAuthentication no`。
- **SonicWall CVE-2026-19868 细节**：同一公告共 7 个洞，仅 19868 标注疑似被利用（CVSS 7.1）；另有两个 8.8 管理面洞（跨域策略／会话校验）、三个预认证溢出（DoS）；SecurityWeek 提醒上月被利用的 **CVE-2026-102255** 仍未进 KEV。
- **Barracuda ESG 预认证 root 链（CVE-2026-116606 + CVE-2026-111560）**：watchTowr 公开分析；NVD 描述影响 **9.4.0.030 以前**；社区呼吁把管理界面撤离公网。暂未进 KEV。
- **Microsoft Entra Device Registration CVE-2026-109469（CVSS 10.0）**：授权绕过→网络侧提权；社区帖称微软已在服务端缓解（云服务洞），建议核对设备注册与 Conditional Access 相关日志。
- **Crédit Mutuel Arkéa 经服务商被盗约 1 亿欧元（约 1.33 亿美元）**：攻击者经第三方平台进入，以银行自有账户转出并换为 USDC/USDT；银行称已追回部分。
- **APT／Malware**：Securelist 披露 **Storm-2603** 无文件 SharePoint（ToolShell）入侵与 Warlock 尝试（附 IoC）；ESET **SlippyNunchucks** 经 DNS 劫持滥用搜狗输入法投 DarkVigil；malwrhunterteam 发现 macOS 假安装包下载点。
- **其他**：WP Libre Form CVE-2026-118423 公开 PoC 且无修复（建议停用）；Rails Active Storage CVE-2026-122006；Tenda AC19 CVE-2026-123966／Edimax BR-6208AC CVE-2026-122051／WAVLINK CVE-2026-120198（IoT，公开利用、无补丁）；Sam Curry／Shubham Shah ForgeRock 链远程控车（已修）；Gnosis Pay 卡数据泄露；Keplr／Web3Auth 社交登录钱包被盗（X 新闻摘要）。

## CVE / POC / 漏洞

### 1. OpenSSH *sshole CVE-2026-123158 —— 在野利用确认扩大（续报）
条件不变：musl libc + 无 PAM + `PasswordAuthentication yes` + 存在 shadow 为 `*` 的可登录账户 + 本机另有 `$5$`／`$6$` 哈希账户；257–1024 字符的任意密码即可登录。**今日新增**：watchTowr Intel 称已观测到利用，目前多为僵尸网络与挖矿；SecurityWeek 引 OpenSSH 维护者 Damien Miller：鉴于 AI 代理快速「重新发现」漏洞，此次几乎不设禁运；受影响面含 Alpine（3.16–3.24、edge 均检查到）、OpenWrt、Buildroot、Yocto 等。社区已出 nuclei 检测模板（PR），可用于资产自查。修复：**OpenSSH 10.6p2** 或发行版补丁，**必须重启 sshd**；临时：关闭密码认证。狩猎：本应无密码账户出现 `Accepted password for`；超长密码尝试；`sshd -T | grep -E 'usepam|passwordauthentication'`。
- X 原帖：https://x.com/watchtowrcyber/status/2118636513739317525 （11-06 早间，窗口内被转引）；https://x.com/SecurityWeek/status/2119054511159320975 ；https://x.com/TheMsterDoctor1/status/2118960474276425868 ；https://x.com/UK_Daniel_Card/status/2119108419336479161 ；https://x.com/cipherredacted1/status/2119205191442633133 ；https://x.com/modularciso/status/2119006094856966603 ；https://x.com/PacketReport1/status/2119053354143723924 ；https://x.com/jenistranger/status/2119082457429590450 ；https://x.com/i/trending/2118336300994671088 （X 新闻摘要）
- GitHub·检测模板：https://github.com/projectdiscovery/nuclei-templates/pull/17702/files
- PoC（仅列出处，不转载）：https://gist.github.com/rezigned/31656ac0517869f387b7a91f47de5976 （来源 https://x.com/rezigned/status/2118993409679786465 ）
- 文章：https://www.securityweek.com/openssh-rushes-patches-for-sshole-authentication-bypass/ ；https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html ；https://sshhole.com/
- 厂商／上游：https://www.openssh.org/txt/release-10.6p2 ；https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-123158
- 地址／IoC：未见公开 IoC（无统一利用源 IP 列表；以 GreyNoise 看板与本组织 sshd 日志为准）

### 2. SonicWall SonicOS SSLVPN CVE-2026-19868 —— KEV（due 11-20），公告细节
SecurityWeek（11-07）：SonicWall 11-06 公告共 7 个漏洞，**仅 CVE-2026-19868 标注疑似在野利用**（CVSS 7.1，仅在启用 SAML 登录时暴露；持另一认证方式有效凭据可绕过 SAML 与 SAML 强制 MFA）。影响 Gen7 TZ/NSa/NSsp/NSv **7.3.3-7015 及更早**、Gen8 TZ/NSa/NSv **8.2.2-8015 及更早**；修复 **7.3.4-7013／8.2.3-8015**；无变通。同公告另含：两个 CVSS 8.8 管理接口洞（宽松跨域策略、会话校验，部分条件下未认证可执行未授权操作）、三个 SSLVPN／TACACS+ 预认证缓冲区溢出（应用层 DoS）、一个虚拟设备弱口令哈希。另：上月被利用的 **CVE-2026-102255** 仍未进 KEV。防御：升级；管理面不对公网；复查 SSLVPN 登录与非 SAML 认证源。
- X 原帖：https://x.com/SecurityWeek/status/2119120196267057283 ；https://x.com/SecurityWeek/status/2119011671163203845 ；https://x.com/BadgerSignalHQ/status/2118986471814356992 ；https://x.com/SecWireDaily/status/2119082579013873841 ；https://x.com/yabetchi_iPhone/status/2119201643082436886
- 文章：https://www.securityweek.com/sonicwall-patches-exploited-sonicos-bug-that-weakens-vpn-logins/
- 厂商公告：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014
- CISA KEV／NVD：https://www.cisa.gov/known-exploited-vulnerabilities-catalog ；https://nvd.nist.gov/vuln/detail/CVE-2026-19868
- 地址／IoC：未见公开 IoC

### 3. Barracuda Email Security Gateway CVE-2026-116606 + CVE-2026-111560 —— 预认证 root 链
watchTowr Labs（Sina Kheirkhah）分析：116606 为预认证授权绕过（CVSS 9.3，可调用配置导入恢复伪造备份）、111560 为 OS 命令注入（CVSS 8.6，波及 ESG、Load Balancer ADC、Message Archiver、WAF Control Center、WAF、Web Security Gateway），串联得未认证 root。**版本口径不一**：watchTowr 表列修于 9.4.0.029，NVD 描述「9.4.0.030 以前」受影响，社区帖亦写 9.4.0.030+——建议直接升到 **≥9.4.0.030** 并以厂商公告为准。NVD 引用含 Mandiant 披露 MNDT-2026-0042。暂未进 KEV。狩猎：管理 UI 异常配置导入／备份恢复记录、伪造备份校验和（社区提示）。
- X 原帖：https://x.com/Komodosec/status/2118901150011584729 ；https://x.com/DFIR_Radar/status/2118901732654682147 ；https://x.com/V0iD_0daY/status/2118857862294212737 ；https://x.com/Arcscaler/status/2118859597830045899 ；https://x.com/samilaiho/status/2119041978197479642
- 文章：https://labs.watchtowr.com/barracuda-networks-is-your-new-best-friend-barracuda-email-security-gateway-pre-auth-remote-root-rce-cve-2026-116606-cve-2026-111560/ ；https://thehackernews.com/2026/11/experts-demonstrate-barracuda-email.html
- 厂商公告：https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection
- 披露：https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0042.md
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-116606 ；https://nvd.nist.gov/vuln/detail/CVE-2026-111560
- 地址／IoC：未见公开 IoC

### 4. Microsoft Entra Device Registration CVE-2026-109469（CVSS 10.0）
NVD 11-06 收录：Entra 设备注册「用户可控键」授权绕过，未授权攻击者可经网络提权。日文社区帖称微软说明**已在服务端缓解**（云服务漏洞，通常无需客户打补丁）；部分帖渲染为「流氓设备成为受信企业设备、绕过 Conditional Access」属推测口径。建议：复查近期异常设备注册／加入、Conditional Access 中「合规设备」依赖、Entra 审计日志。
- X 原帖：https://x.com/zukai_ai_news/status/2118848517242503610 ；https://x.com/read__the__diff/status/2118989689126273230 ；https://x.com/pwnwatch_app/status/2118850920520011833 ；https://x.com/ParameterWatch/status/2118857340208505293
- 厂商：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-109469
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-109469
- 地址／IoC：未见公开 IoC

### 5. WordPress：Core 119977 转入逾期；WP Libre Form CVE-2026-118423 公开 PoC 无修复
- **Core CVE-2026-119977**：KEV 期限 11-06 已过；Wordfence 累计拦截 24 万+ 次，攻击者在站点更新窗口守候最长约 14.5 小时。仍是「先对 `/wp-content/upgrade/` 返回 403，再升 7.1.4」。X 新闻摘要：https://x.com/i/trending/2118806656876446001 ；https://x.com/Aegisrecon/status/2118873142441730207 ；Wordfence：https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-core/wordpress-core-470-713-unauthenticated-upgrade-window-staged-installer-remote-code-execution
- **WP Libre Form ≤1.5.0.1 CVE-2026-118423**：表单上传不校验类型→未认证上传 PHP→RCE；公开 PoC 已出，**暂无修复版本**——建议立即停用／移除，并检查上传目录中的 `.php`。X：https://x.com/SecAlertsCo/status/2119061698736754853 ；https://x.com/MarsCareer/status/2119063986620526764 ；https://x.com/Aegisrecon/status/2119054188026151327 ；WPScan：https://wpscan.com/vulnerability/35149a79-aee1-4f13-ba29-583c2224c5da/ ；NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-118423
- 另：Gravity Forms 被列入「有利用报告未进 KEV」，升 **3.1.3+**（来源 Aegisrecon 帖，未见厂商公告链接，待核实）。
- 地址／IoC：未见公开 IoC

### 6. Ruby on Rails Active Storage CVE-2026-122006（CVSS 9.8）
NVD：activestorage 8.1.4.1 之前，在使用 ImageMagick 处理附件时 analyzer 于附件时即运行且无安全策略，可致服务器读写（如读取 `secret_key_base`）。修复 **8.1.4.1／8.0.5.2**，社区提示同时 mini_magick ≥5.1。窗口内仅见「检测工具」帖，未见在野报告。
- X 原帖：https://x.com/exploitgrid/status/2119074901315203144 ；https://x.com/SecWireDaily/status/2119082579944980538
- 厂商：https://github.com/rails/rails/security/advisories/GHSA-f3w6-w445-fwh9 ；https://github.com/rails/rails/releases/tag/v8.1.4.1 ；https://github.com/rails/rails/releases/tag/v8.0.5.2
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-122006
- 地址／IoC：未见公开 IoC

### 7. Zyxel GS1900 CVE-2026-107441（续）
Binarly：从威胁者基础设施回收的利用在 Patch 2（.2 固件）上仍有效，命中独立的 CGI 越界写；Zyxel 描述为相邻网络未认证 OS 命令执行。升 **2.90 Patch 3**（按型号 .3 版本），并轮换 root 凭据。未进 KEV。
- X 原帖：https://x.com/DFIR_Radar/status/2118932236745797700 ；https://x.com/nurhayatdev/status/2118869810360537322 ；https://x.com/ksg93rd/status/2119122642888208675
- 文章：https://www.binarly.io/advisories/brly-2026-057
- 厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-out-of-bounds-write-vulnerability-in-gs1900-series-switches-11-03-2026
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-107441
- 地址／IoC：未见本窗口新 IoC

### 8. IoT 公开利用、无补丁（简报）
- **Tenda AC19 16.03.10.07 CVE-2026-123966**：`saveParentControlInfo` 堆溢出，远程、免登录，利用已公开，未见补丁。X：https://x.com/cvedotnew/status/2119082473984336259 ；https://x.com/TheHackerWire/status/2119103322821214711 ；NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-123966 ；VulDB：https://vuldb.com/vuln/432038
- **Edimax BR-6208AC 1.32 CVE-2026-122051**：`/goform/mp` 命令注入，利用已公开；厂商早先被联系但未回应（NVD 口径）。X：https://x.com/SecAlertsCo/status/2118941793265799647 ；NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-122051
- **WAVLINK WL-WN530BE1-A CVE-2026-120198**：`/protocol.csp` 命令注入，利用公开、无补丁。X：https://x.com/cveintelligence/status/2118942853716201477 ；NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-120198
- 防御：管理面勿对公网；EOL／无补丁设备隔离或更换。
- 地址／IoC：未见公开 IoC

### 9. Sam Curry／Shubham Shah：ForgeRock 链 RCE→两家车企远程控车（已修）
研究博文（11-07）：ForgeRock 路径混淆 + WAF 绕过 + OpenIDM 调度器得到 SSO 服务器代码执行，可为任意客户创建会话，进而定位、开关锁、远程启停车辆；车企未具名，报告后约 2 小时内修复并轮换凭据。同时发布 WARDOGS 托管商 RCE 文。启示：自托管 ForgeRock／OpenIDM 管理端点勿外露、复查 WAF 路径规范化。
- X 原帖：https://x.com/samwcyo/status/2119030320171266117 ；https://x.com/samwcyo/status/2119030321505079440
- 文章：https://samcurry.net/forgerock ；https://samcurry.net/wardogs
- 地址／IoC：未见公开 IoC

### 10. CISA KEV 目录状态与逾期清单
目录仍为 **2026.11.06／1769／Δ0**（周六无新增）。**新近逾期**：WordPress **CVE-2026-119977**（due 11-06）。仍逾期：Ivanti **CVE-2026-111357**（11-02）、GitLab **CVE-2026-97229**／Cisco **CVE-2026-76418**（11-01）、Plex **CVE-2026-96652／96655**、Siemens **CVE-2026-110936**（11-03）、Linux **CVE-2026-46300**（10-31）。即将到期：Google CVE-2026-111497 与 Adobe CVE-2026-48356 **11-10**；Broadcom CVE-2026-41709 **11-11**；Ivanti CVE-2026-118527 **11-13**；Apple CVE-2024-27834 **11-18**；SonicWall CVE-2026-19868 **11-20**。观察（未进 KEV 但有利用报告）：Zyxel 107441、sshole 123158、SonicWall 102255、Barracuda 116606/111560（尚无在野报告）、Gravity Forms。
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog ；JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- 地址／IoC：未见公开 IoC

## 工具与 GitHub 发布

### 1. nuclei 模板：sshole CVE-2026-123158 检测（PR）
社区帖指向 ProjectDiscovery nuclei-templates PR，可用于自有资产暴露面检查（务必只扫授权范围）。
- X 原帖：https://x.com/TheMsterDoctor1/status/2118960474276425868
- GitHub：https://github.com/projectdiscovery/nuclei-templates/pull/17702/files
- 地址／IoC：未见公开 IoC

### 2. Kaspersky：CLRDeserializationExploitFinder 与 VirtualPathProvider Lab（防御工具）
随 Storm-2603 报告发布，用于检测 .NET 反序列化利用（含 ToolShell）与基于 VirtualPathProvider 的无文件 webshell；文中给出 IIS-Configuration ETW 事件 25/47 与 17/18/19/21 的差异检测思路。
- 文章：https://securelist.com/storm-2603-fileless-toolshell-attack/121467/ （工具仓库链接见原文）
- X 原帖：https://x.com/ksg93rd/status/2119122642888208675
- 地址／IoC：见「APT / Malware」Storm-2603 条

### 3. 其他
- **npm AI 代理工具会把 Claude Code 会话提示词外传**（X Article，建议检查 `~/.claude`）：https://x.com/con_golias/status/2119013087806095434 → https://x.com/i/article/2119018334813376512
- **假「安全工具」GitHub 仓库**（Doctor Web：Trojan.Loader.3261、BackDoor.AsyncRAT.115、Trojan.Clipper.688、JS.Stealer.191；2,000+ Windows 主机）续传：https://x.com/Python_s_/status/2118880654368682380 ；https://x.com/mikejt4/status/2118808156440601034 ；https://www.bleepingcomputer.com/news/security/fake-security-tools-on-github-push-backdoors-and-infostealers/
- **MalOps「Operation Hijacked Trust」恶意软件分析练习**（DLL 搜索顺序劫持→反射加载 RAT）：https://x.com/MalGamy12/status/2119016597058724206 ；https://malops.io/chain-challenges/operation-hijacked-trust
- **Init1Security**：恢复 ISO 容器「隐藏文件」能力的训练用工具（红队向，注意 ISO 内隐藏文件的检测）：https://x.com/init1security/status/2118807890987544940 ；https://x.com/dmcxblue/status/2119059506990641641
- **Anthropic Cyber Verification Program**（放宽恶意软件分析／漏洞验证时的分类器拦截）：https://x.com/LuYuHao_Neil/status/2119041528974958886 ；https://x.com/samwcyo/status/2118908015848169891
- 地址／IoC：未见公开 IoC（Doctor Web 样本以原文为准）

## APT / Malware 分析

### 1. Storm-2603：无文件 SharePoint（ToolShell）入侵与 Warlock 尝试（Securelist）
Kaspersky 回溯分析（11-05 发布，事件发生于 2025-12）：12-20 单次 ToolPane 指纹探测（ONYPHE 基础设施）→ 静默 3 天 → **12-24 平安夜**经 SPN 节点打 CVE-2025-53770 链，在 w3wp.exe 内注册 VirtualPathProvider 加载内存 webshell（特定 User-Agent 触发、XOR 自定义协议、suo5 隧道）；EfsPotato 式命名管道提权到 SYSTEM；经 Supabase 存储拉取存在漏洞的 Velociraptor 0.73.4.0（CVE-2025-6264）；部署 Zoho Assist、VS Code 隧道、Cloudflare Tunnel 等多重隧道；投放漏洞驱动 rsndispot.sys 做 EDR 杀手并尝试 Warlock 勒索（被拦截）。归因 Storm-2603（中等置信）。防御：SharePoint 打补丁后仍需轮换 MachineKey；监测 w3wp 异常子进程／外连、未授权 VPP、Velociraptor／远程管理工具意外出现。
- X 原帖：https://x.com/ksg93rd/status/2119122642888208675
- 文章：https://securelist.com/storm-2603-fileless-toolshell-attack/121467/
- 地址／IoC（原文抄录，已 defang）：
  - `45.91.94[.]204`（SPN 节点）；`49.51.132[.]100`（SPN 节点）
  - `91.224.92[.]121`、`204.76.203[.]219`（防弹托管 C2）；`199.232.210[.]172`（C2 流量中继）
  - `hxxps://vdfccjpnedujhrzscjtq[.]supabase[.]co/storage/v1/object/public/image/v4[.]msi`（漏洞版 Velociraptor 包）
  - `hxxps://auth[.]qgtxtebl[.]workers[.]dev/`（Velociraptor 服务器）
  - `hxxps://files[.]catbox[.]moe/8f7vex[.]msi`（被滥用的 Zoho Assist 安装包）
  - `hxxps://github[.]com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64[.]msi`（被滥用的合法隧道工具）
  - 哈希（MD5，原文带 0x 前缀）：`FD91321BF7FF7245DDA9B7B5D791ACE8`（vskp2 webshell）；`3A55D8F8F29716C694671834D8C6CB29`（Velociraptor.exe）；`991EC6E04413F2D4D29341C17A8A54D5`（被滥用 VS Code）；`3D553B9061C03F891CE97D7D2E64DDEE`（VS Code Insiders）；`2C32E44A013CBFC5A323EFB7694701D2`（隧道工具）；`112A86ECA3CB5A0B5E20AB744CC5AF93`（改名 7z.exe）；`A930F81E3FB0A226EC5904D9043A17B8`（ZohoMeeting.7z）；`054a32d6033b1744dca7f49b2e466ea2`（漏洞驱动 rsndispot.sys）；`2d9ebf9c042f596f435865b40edad928`（Warlock AV killer DLL，正文）

### 2. SlippyNunchucks：DNS 劫持滥用搜狗输入法投 DarkVigil（ESET）
中国利益相关组织（ESET 高置信，至少自 2023-09 活动）。2026-07-01 起，搜狗输入法组件以明文 HTTP 拉取推广配置，经 DNS 劫持返回恶意配置，令应用下载 DarkVigil（又名 FDMTP，20+ 插件的 .NET 模块化工具集）并置于搜狗组件会执行的位置获得持久化。受害者在香港、泰国、日本、越南、斯里兰卡、阿曼（含跨国博彩组织、迪拜网吧、丹麦大学生）。腾讯于 **搜狗输入法 16.10**（10 月下旬）改为 HTTPS + 证书锁定；ESET 称下载组件仍不校验文件类型与保存位置；DNS 劫持发生位置未知（路由器／ISP 皆有可能）。防御：升级到 16.10+；监控输入法进程异常下载与落地 .NET 程序集；检查家用／分支路由器 DNS 设置。
- X 原帖：https://x.com/Huntio/status/2119082473988476971
- 文章：https://www.infosecurity-magazine.com/news/slippynunchucks-sogou-dns-hijacking/
- 地址／IoC：本窗口所读材料未列 IoC（以 ESET 原报告为准）

### 3. Crédit Mutuel Arkéa 约 1 亿欧元被盗（经服务商）
BleepingComputer：攻击者经服务商平台直接进入网络，以 Arkéa **自有账户**向其他银行发起转账并换成加密货币（ZachXBT 估约 1.18 亿欧元／1.33 亿美元，以 USDC/USDT 提走；称因未及时公开，11-03 前已洗出约 3,000 万美元）；银行仅确认「数量级」，称客户资产无损、非人为失误，属「复杂攻击」；CNCM 主席称已追回部分。警惕后续借事件的钓鱼。启示：第三方支付／转账平台的特权凭据与交易审批隔离。
- X 原帖：https://x.com/BleepinComputer/status/2119089297642918202 ；https://x.com/f3ssoftware/status/2118845323455943007 ；https://x.com/prisminfoss/status/2119168608018579946 ；https://x.com/modularciso/status/2119136551892648256
- 文章：https://www.bleepingcomputer.com/news/security/hackers-pull-off-133-million-french-bank-heist-via-service-provider/ ；https://information.tv5monde.com/economie/cyberattaque-credit-mutuel-arkea-recupere-une-partie-des-100-millions-deuros-derobes-2844822 ；https://www.halborn.com/blog/post/explained-the-credit-mutuel-arkea-cyberattack-november-2026
- 厂商（银行）公告：https://www.cm-arkea.com/arkea/banque/assurances/pa_38367/fr/credit-mutuel-arkea-annonce-avoir-ete-victime-d-une-attaque ；https://www.cm-arkea.com/arkea/banque/assurances/pa_38386/fr/informations-complementaires-suite-a-l-attaque-dont-le-credit-mutuel-arkea-a-ete-victime
- 地址／IoC：未见公开 IoC（链上地址以 ZachXBT 原帖为准，本窗口未取得）

### 4. macOS 假安装包「SkyLawsInstaller.dmg」（malwrhunterteam）
- X 原帖：https://x.com/malwrhunterteam/status/2119048043223752796
- 地址／IoC（原帖抄录）：`hxxps://apple.eu10hub[.]com/get_file?file=91A2T8Ehs06E`（仿冒 Apple 域名下发 DMG）

### 5. 威胁报告聚合（RST Cloud 摘录，原报告多为 11-05／11-06）
- **ARTEX「Agentic Asbestos」（Censys）**：关联 Storm-0940，工具含 Cobalt Strike、AdaptixC2、Vshell、GodPotato 等。https://x.com/rst_cloud/status/2119111526611132868 ；https://censys.com/blog/artex-agentic-asbestos/
- **Armorsteal（Seqrite）**：Python（PyArmor 混淆）窃密 + XMRig 挖矿套件。https://x.com/rst_cloud/status/2119058461824545242 ；https://www.seqrite.com/blog/armorsteal-unpacked-breaking-down-a-python-malware-kit-that-steals-data-and-mines-crypto/
- **DarkSword 路由器的 iOS 26 路径 C10 已关闭**（ClickFix、加密货币用户）：https://x.com/rst_cloud/status/2119134285382795708 ；https://ohey.ca/research/darksword-router-ios-26-c10/
- **HYFLOCK 勒索（Check Point／Cyberint PDF）**：BYOVD、删除卷影副本，针对政府／医疗／教育／法律。https://x.com/rst_cloud/status/2119073633117081982 ；https://checkpoint.cyberint.com/hubfs/HYFLOCK%20-%20From%20Underground%20Recruitment%20to%20Public%20Extortion.pdf
- **APT29 移动水坑**（Security Affairs 续报，主线见 11-04）：https://x.com/Huntio/status/2119127940537417949 ；https://securityaffairs.com/202473/apt/russian-apt29-targets-mobile-users-with-watering-hole-attacks.html
- 地址／IoC：以各原报告为准（本摘要未逐一抄录）

### 6. SecurityWeek 周报要点（11-06 发布，窗口内推送）
Trezor 提醒自 2026-03 起从 CryptoBilis 购买的设备转移资金（买家称 Safe 5 内有带蜂窝模块的窃取助记词植入，未经 Trezor 证实）；Mandiant LLMJacking 单日账单超 10 万美元、累计达 100 万美元，一例利用 LiteLLM CVE-2026-40217 提权 API key；Onapsis／Recorded Future：SAP 补丁到首次利用／公开 PoC 中位数缩至 1–3 天；Synology 警告 2024-12 已修漏洞（Synology-SA-24:20）被用于 NAS 勒索；Era 披露针对 Flowise（CVE-2024-58351）的「hello」框架 Greeter；Push Security 披露仿 OpenAI／SpaceX 活动邀请的设备码钓鱼（Kali365 PhaaS）。
- X 原帖：https://x.com/SecurityWeek/status/2119064577602150736
- 文章：https://www.securityweek.com/in-other-news-trezor-implant-llmjacking-bills-hit-1m-sap-flaws-weaponized-within-days/
- 地址／IoC：未见公开 IoC

### 7. 泄露／勒索与金融事件简报（多数未证实）
- **Gnosis Pay** 旧消费卡系统 11-03 被入侵：姓名、地址、完整卡号与 CVV、钱包地址外泄；资金无损，强制 3DS。https://x.com/mg_crypto0/status/2119067367095349250 ；https://www.theblock.co/news/defi/2026-11-06-gnosis-pay-data-breach-legacy-debit-card-system-435934 ；https://www.coindesk.com/business/2026/11/07/gnosis-pay-breach-exposes-card-numbers-home-addresses-and-linked-crypto-wallets ；官方帖：https://x.com/gnosispay/status/2118713486616227862
- **Keplr 钱包暂停 Google／Apple 登录**：Web3Auth 问题致社交登录钱包被盗（X 新闻摘要称至少 600 万美元、4.4 万+ 钱包，待核实）。https://x.com/i/trending/2118960935272669668
- **Anthropic 通知企业用户：第三方研究机构未经许可访问业务联系人数据**（X 新闻摘要，待核实；无对话／密码／支付数据）。https://x.com/i/trending/2119107733496447135
- **意大利外长 Tajani 个人数据暗网泄露**（X 新闻摘要）：https://x.com/i/trending/2119056134371738000
- **LBC Express（菲律宾快递）2,090 万条记录被叫卖**（未证实）：https://x.com/TheThreatWire/status/2119149137069523394
- **越南国企 534.3 GB 被叫卖（BlackNet00，未证实）**：https://x.com/VECERTRadar/status/2118896127197979075
- **DarkForums 疑遭 S-ROOT 打击**（未证实）：https://x.com/VECERTRadar/status/2119059240014811338
- **Who Gives A Crap 客户数据经营销供应商外泄**：https://x.com/mikejt4/status/2119176144142447009
- 地址／IoC：未见公开 IoC

## 地址／IoC 汇总

- sshole／SonicWall 19868／Barracuda／Entra 109469／Rails／WP Libre Form／IoT 洞：**未见公开 IoC**（补丁、配置与日志狩猎为主）
- Storm-2603（Securelist）：`45.91.94[.]204`、`49.51.132[.]100`、`91.224.92[.]121`、`204.76.203[.]219`、`199.232.210[.]172`；`vdfccjpnedujhrzscjtq[.]supabase[.]co/.../v4[.]msi`、`auth[.]qgtxtebl[.]workers[.]dev`、`files[.]catbox[.]moe/8f7vex[.]msi`；MD5 见上文 APT 第 1 条
- macOS 假安装包：`hxxps://apple.eu10hub[.]com/get_file?file=91A2T8Ehs06E`
- SlippyNunchucks／Crédit Mutuel Arkéa／ARTEX／Armorsteal／HYFLOCK：以原报告为准，本窗口未抄录到具体 IoC
- 昨日 vx-underground 清盘样本（`81.168.24[.]109`）与 Codex 广告持久化（`zz.aiapi2025[.]top`）：无新刷新，仍以 11-06 晚报为准

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

本日 LWiS 交叉：X 工具无 list timeline 接口，改为对成员随机抽样 25 个 handle（PortSwiggerRes、merlin_c2、elad_shamir、Oddvarmoe、samwcyo、dmcxblue、spaceraccoonsec 等）及高信号账号（vxunderground、cyb3rops、GreyNoiseIO、TheHackersNews、BleepinComputer、SecurityWeek、Malwarebytes、fr0gger_、malwrhunterteam、Huntio、ido_cohen2 等）做 `from:` 检索。命中：samwcyo ForgeRock 控车研究、malwrhunterteam 假 DMG、Huntio SlippyNunchucks／APT29、dmcxblue／Init1Security 工具帖、Oddvarmoe 深度伪造社工演练；周六整体为闲聊居多。LWiS 博客清单命中 samcurry.net、labs.watchtowr.com（已补链）。

## 来源搜索 URL

- https://x.com/search?q=(CVE%20OR%200day%20OR%20exploit%20OR%20POC)%20-is%3Aretweet%20lang%3Aen&src=typed_query&f=live
- https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20implant)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)%20-is%3Aretweet%20lang%3Aen&src=typed_query&f=live
- https://x.com/search?q=(sshole%20OR%20%22CVE-2026-123158%22%20OR%20%22CVE-2026-19868%22%20OR%20Plex2Shell%20OR%20ARTEX%20OR%20%22CVE-2026-83844%22%20OR%20%22CVE-2026-119977%22)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(%22CVE-2026-107441%22%20OR%20%22Gravity%20Forms%22%20OR%20%22CVE-2026-118423%22%20OR%20%22CVE-2026-122006%22%20OR%20%22CVE-2026-122051%22%20OR%20%22CVE-2026-116606%22%20OR%20Barracuda)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(infostealer%20OR%20ransomware%20OR%20backdoor%20OR%20RAT%20OR%20loader)%20(IoC%20OR%20IOCs%20OR%20C2%20OR%20sha256%20OR%20campaign)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(%22Storm-2603%22%20OR%20Arkea%20OR%20%22CVE-2026-109469%22%20OR%20%22CVE-2026-123966%22%20OR%20Web3Auth%20OR%20SlippyNunchucks)%20-is%3Aretweet&src=typed_query&f=live
- LWiS 列表：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD API：https://services.nvd.nist.gov/rest/json/cves/2.0
