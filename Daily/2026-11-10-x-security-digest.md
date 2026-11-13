# X 安全情报晚报 · 2026-11-10（周二）

> 报告时间：2026-11-10 约 20:15（America/Santiago）＝ 2026-11-11 约 07:15（香港时间）。
> **覆盖时长**：X 只读搜索窗口 2026-11-09 23:00 UTC～11-10 22:00 UTC（约 23 小时）；CVE 组用 relevancy 排序补满（25 条覆盖 11-10 00:20～21:31 UTC），工具组（github.com + C2/red team/nuclei）按 Latest 只命中 2 条，威胁报告组 25 条覆盖 11-09 23:24～11-10 21:51 UTC。LWiS X List 翻三页共 241 帖，覆盖 11-09 19:33～11-10 22:47 UTC（超过 24 小时）。SecureFlow 取近 48 小时（blog 放宽 7 天）；AI/TLDR 取 36 小时；Agent Use Cases 取 48 小时。
> **验收说明**：见文末「验收结果」。
> 公开备援：CISA KEV 11-10 新增 6 条（Outlook、Chrome、Cisco BroadWorks、Barracuda ×2、Openwave），其中 Barracuda 两条联邦期限 11-13，其余 11-24。今天是微软／Adobe 11 月补丁日。

## 今日摘要

- **11 月补丁日**：微软约 1,090 个 CVE，只有 1 个在野利用：Outlook 欺骗类 0day CVE-2026-124194（CVSS 6.5，已入 KEV）；Adobe 9 份公告 110 个 CVE，Connect（最高 CVSS 10.0）和 AEM（9.9）最要紧，均未见在野利用；Exchange 11 月 SU 同步发布。
- **Chrome 今年第 8 个在野 0day**：CVE-2026-125350，XML 组件 UAF，修复版 157.0.8103.50/.51，已入 KEV。
- **Barracuda ESG 链式漏洞入 KEV**：CVE-2026-116606（认证绕过）+ CVE-2026-111560（命令注入）可拿 root，厂商称「少数组织」已遭利用，联邦期限只有 3 天（11-13）。
- **APT**：ESET 披露 Turla 的新 .NET 工具集 Cereal，把 Exchange 服务器变成长期收集点；Check Point 跟踪一年的 CopperDragon「Sparrow Framework」（中国关联，水坑＋被动后门，打电信）；朝鲜 Contagious Interview 新一轮木马化 macOS 安装包（IoC 见下）。
- **其他在野利用**：Xen Orchestra 认证绕过 VSA-2026-062 被利用（可接管 XCP-ng 宿主）；watchTowr 蜜罐观测到针对 N-able N-central「Able2Shell」的利用尝试；Calif 展示 Brotli 解压缺陷在 iOS/macOS（含 MTE 设备）上的 WebKit.Networking 代码执行，苹果 27.2.1 已修。
- **AI 安全**：Notion 确认受 Fireworks AI 入侵波及（AI 聊天记录外泄，已停用 Fireworks）；Google 说明消费版 Gemini 拉进对话的 Gmail/Drive 片段可能被人工审核员看到。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

**1. Microsoft Outlook 欺骗 0day CVE-2026-124194（11 月补丁日修复，已在野利用，KEV 11-10，期限 11-24）**
- 谁／什么：「对潜在不安全操作缺少用户交互」类欺骗漏洞，CVSS 6.5／Moderate，影响 Microsoft 365 Apps for Enterprise、Office LTSC 2021 等。本月微软约 1,090 个 CVE 中唯一在野利用的。
- 处置：优先推送 Office/M365 Apps 11 月更新；关注 Outlook 异常外联与预览触发的认证请求。
- X 原帖：[cytexsmb](https://x.com/cytexsmb/status/2120263996875915714) · [GsInfosystems](https://x.com/GsInfosystems/status/2120268110439891058)
- 厂商公告：[MSRC CVE-2026-124194](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-124194) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124194) · [CISA KEV 目录](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- 文章（SecureFlow·ZDI-Blog）：[ZDI 11 月补丁综述](https://www.thezdi.com/blog/2026/11/10/the-november-2026-security-update-review)（含 Adobe 9 份公告 110 CVE：Connect APSB26-191 最高 CVSS 10.0、AEM APSB26-189 9.9）
- 相关：[Exchange Server 2026 年 11 月 SU](https://techcommunity.microsoft.com/blog/exchange/released-november-2026-exchange-server-security-updates/4570368)（LWiS @PyroTek3 转 [原帖](https://x.com/PyroTek3/status/2120242233261609407)）

**2. Google Chrome 在野 0day CVE-2026-125350（XML 组件 UAF，KEV 11-10，期限 11-24）**
- 谁／什么：远程攻击者借特制网页在沙箱内执行代码；Google 确认已有在野利用，是 2026 年第 8 个被利用的 Chrome 0day。修复版 157.0.8103.50/.51；其他 Chromium 内核浏览器需跟进。
- 处置：更新后务必重启浏览器；用 EDR／资产清单核对实际运行版本。
- X 原帖：[Digital_Warfare](https://x.com/Digital_Warfare/status/2120103823863902510) · [AGTPinsights](https://x.com/AGTPinsights/status/2120071067863560490) · [BadgerSignalHQ](https://x.com/BadgerSignalHQ/status/2120059720816050593)
- 厂商公告：[Chrome Releases 稳定版更新](https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-125350)

**3. Barracuda ESG 认证绕过 CVE-2026-116606 + 命令注入 CVE-2026-111560（KEV 11-10，期限 11-13）**
- 谁／什么：116606 让未认证攻击者调用配置导入功能恢复特制备份；111560 是 ESG、负载均衡、ADC、BMA、WAF、WSG 等多产品的 OS 命令注入。两者串联可在 ESG 上拿 root，Barracuda 公告（11-09 更新）称「少数组织」已遭利用；漏洞由 Mandiant 披露。
- 处置：确认已装 BNSF-40425／BNSF-40430；管理界面只对内网开放；排查异常配置导入记录。
- X 原帖：[runbooklab](https://x.com/runbooklab/status/2120243634209456273) · [DailyDarkWeb（KEV 6 条）](https://x.com/DailyDarkWeb/status/2120257398900142167)
- 厂商公告：[Barracuda Trust Center](https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection) · [NVD CVE-2026-116606](https://nvd.nist.gov/vuln/detail/CVE-2026-116606) · [NVD CVE-2026-111560](https://nvd.nist.gov/vuln/detail/CVE-2026-111560)
- GitHub（披露文档，非利用代码）：[Mandiant MNDT-2026-0041](https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0041.md) · [Mandiant MNDT-2026-0042](https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0042.md)

**4. KEV 11-10 其余两条：Cisco BroadWorks XXE CVE-2026-20320、Openwave Webtop Media Transcoder CVE-2026-111793（期限 11-24）**
- BroadWorks：未认证远程读取敏感配置；Openwave：已认证用户可绕过 Webmail 转换非预期文档类型。
- 厂商公告：[Cisco cisco-sa-bworks-xxe-uwUd7CEt](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bworks-xxe-uwUd7CEt) · [Openwave CAN-2026-2032674](https://github.com/GISOpenwave/security-advisories-public/blob/main/CAN-2026-2032674.md) · [JVN JVNVU93403064](https://jvn.jp/en/vu/JVNVU93403064/) · [NVD CVE-2026-20320](https://nvd.nist.gov/vuln/detail/CVE-2026-20320)

**5. Xen Orchestra 认证绕过 VSA-2026-062（在野利用）**
- 谁／什么：Xen Orchestra 处理 REST API 认证时存在缺陷，未认证攻击者可拿到管理员会话，进而完全控制 XCP-ng 虚拟化宿主；Vates 称「已被威胁行为者积极利用」。
- 处置：立即升级 Xen Orchestra；管理面不暴露公网；审计近期新会话、API token 和 VM 操作。
- X 原帖：[DFIR_Radar](https://x.com/DFIR_Radar/status/2120215676526702770) · [tsnmediahub](https://x.com/tsnmediahub/status/2120244106412585246)
- 文章：[TSN Media 报道](https://tsnmedia.org/xen-orchestra-auth-bypass/)

**6. N-able N-central「Able2Shell」跟进：watchTowr 蜜罐已见利用尝试**
- 跟进（首报见 11-09 期）：watchTowr Intel 称 0day 公开后一夜之间就在 N-central 蜜罐上看到利用尝试；建议排查入侵迹象、收紧访问并按厂商指引缓解。
- X 原帖：[watchTowr（经 @SinSinology 转）](https://x.com/watchtowrcyber/status/2120096657366827381) · [BadgerSignalHQ](https://x.com/BadgerSignalHQ/status/2120059291684028688)

**7. Brotli 解压缺陷 → iOS/macOS WebKit.Networking 代码执行（苹果 27.2.1 已修）**
- 谁／什么：Calif 展示 Brotli 缺陷在 iPhone 18 Pro、iPad M5、MacBook M5（均带 MTE）上实现 WebKit.Networking 代码执行，再配合沙箱逃逸；@i0n1c 指出该 bug 数月前已修但没被标为安全问题，其他内嵌旧版 Brotli 的软件可能仍受影响。
- 处置：苹果设备升级到 27.2.1；排查自研／第三方软件里的 Brotli 版本。
- X 原帖：[calif_io](https://x.com/calif_io/status/2120225274877100091) · [i0n1c](https://x.com/i0n1c/status/2120230223979672037) · [i0n1c 补充](https://x.com/i0n1c/status/2120247291478954377)

**8. 公开 PoC 与利用代码动态（只记录存在，不转载步骤）**
- Windows Update Stack 本地提权 CVE-2026-81963（9 月补丁）出现公开利用代码：共享的 Windows 11／Server 2025 主机优先补。X 原帖：[infrastack_ai](https://x.com/infrastack_ai/status/2120164693247758650)
- VulnCheck Initial Access 社区仓库新增 Atlassian Data Center 未授权凭据泄露 CVE-2026-21589、GitLab 未授权 RCE CVE-2026-97229、被勒索使用的 Collabora Online RCE CVE-2026-110447，附检测与查询。X 原帖：[catc0n（经 @kmkz_security 转）](https://x.com/catc0n/status/2119987069712024015)；GitHub：[vulncheck-oss/initial-access-community](https://github.com/vulncheck-oss/initial-access-community)
- @v12sec 发布 VirtualBox 逃逸演示视频与样本哈希（见 IoC 节），未见厂商公告。X 原帖：[v12sec](https://x.com/v12sec/status/2120157058414842253)
- Eclipse Mosquitto 预认证 RCE 打 Home Assistant Green 的研究文章：[born0monday 博客](https://born0monday.me/posts/ha-green-mosquitto-rce/)（LWiS @Dinosn [原帖](https://x.com/Dinosn/status/2119948589531357607)）

**9. ZDI 11-10 批量公告：X.Org Server 6 个、Wireshark 3 个、NVIDIA Megatron-LM 1 个（SecureFlow·ZDI-vulnerabilities）**
- X.Org／libX11／libXrender 多个堆溢出与整数溢出（RCE 或提权），Wireshark LBMC／LoRaWAN／SMB 解析器 RCE，Megatron-LM checkpoint 反序列化 RCE。X 上本窗口未见讨论。
- 文章／公告：[ZDI-26-898](https://www.zerodayinitiative.com/advisories/ZDI-26-898/) · [ZDI-26-899](https://www.zerodayinitiative.com/advisories/ZDI-26-899/) · [ZDI-26-900](https://www.zerodayinitiative.com/advisories/ZDI-26-900/) · [ZDI-26-901](https://www.zerodayinitiative.com/advisories/ZDI-26-901/) · [ZDI-26-902](https://www.zerodayinitiative.com/advisories/ZDI-26-902/) · [ZDI-26-903](https://www.zerodayinitiative.com/advisories/ZDI-26-903/) · [ZDI-26-904](https://www.zerodayinitiative.com/advisories/ZDI-26-904/) · [ZDI-26-905](https://www.zerodayinitiative.com/advisories/ZDI-26-905/) · [ZDI-26-906](https://www.zerodayinitiative.com/advisories/ZDI-26-906/)

## 工具与 GitHub 发布（每条：说明 + 地址列表）

**1. SpecterOps「Sage」：内置在 Mythic C2 的开源 AI 助手，面向假定已入侵演练**
- 说出目标，Sage 生成命令并在受监督模式下等操作员批准。防守方可关注 Mythic 流量特征是否变化。
- X 原帖：[SpecterOps（经 @_logangoins 转）](https://x.com/SpecterOps/status/2120235296184750337)
- 文章：[SpecterOps 博客](https://specterops.io/blog/2026/11/10/sage-ai-for-assumed-breach-operations-built-into-mythic/)

**2. Cobalt Strike 基础设施变更：11-13 前更新 TLS 证书**
- 之后需重新下载最新 updater（20261109）才能更新；4.13 用户无需操作。
- X 原帖：[_CobaltStrike](https://x.com/_CobaltStrike/status/2120228842086224226)
- 厂商公告：[Cobalt Strike 博客](https://www.cobaltstrike.com/blog/cobalt-strike-infrastructure-changes-november-2026)（box 换 UA＋Referer 后仍 403，浏览器可开）

**3. LWiS 成员分享的红队／检测工具**
- nukerat，后渗透框架：[GitHub](https://github.com/nukeratframework/nukerat)（[@ipurple 原帖](https://x.com/ipurple/status/2120074908684439729)）
- Silverseal，Rust 写的 Linux UEFI bootkit／rootkit 框架（适合检测研究）：[GitHub](https://github.com/Idov31/Silverseal)（[@ipurple 原帖](https://x.com/ipurple/status/2120046982777405440)）
- Lure，投放假凭据并在被使用时告警的蜜标工具：[GitHub](https://github.com/SilentMesh-Systems/Lure)（[@ipurple 原帖](https://x.com/ipurple/status/2120062402200772930)）
- ClickOnce 部署被滥用于初始访问的研究文章：[akchhat gitbook](https://akchhat.gitbook.io/dev/initial-access/two-clicks-to-a-beacon-abusing-clickonce-deployments-for-initial-access)（[@ipurple 原帖](https://x.com/ipurple/status/2120254940895387857)）
- etw-rs：Rust 的 ETW 解析性能改进并回移到 krabsetw：[Origin HQ 研究](https://www.originhq.com/research/introducing-etw-rs)（[@_winterknife_ 转](https://x.com/_winterknife_/status/2120092860213076052)）
- linux-live：从 Windows 11 NTFS 上单文件启动的 Linux（签名 shim/GRUB，不改 BitLocker），对 Secure Boot 信任链检测有参考价值：[GitHub](https://github.com/wesmar/linux-live)（[@zux0x3a 原帖](https://x.com/zux0x3a/status/2120262473760604494)）
- 微软发布 Autoruns for Linux 1.0.0，社区已有 Velociraptor artifact（[@maxime_tz 转 @mgreen27](https://x.com/maxime_tz/status/2120096915865882798)）

**4. ProjectDiscovery 博客「Probably Not Exploitable」（SecureFlow·blog）**
- 讨论漏洞「大概不可利用」判断的可靠性与扫描器研判。文章：[projectdiscovery.io](https://projectdiscovery.io/blog/probably-not-exploitable)

## APT / Malware 分析（每条：说明 + 地址列表）

**1. Turla 新工具集 Cereal：把 Exchange 变成长期收集点（ESET）**
- 谁／打什么：俄罗斯关联的 Turla 使用此前未公开的模块化 .NET 工具集 Cereal；组件 CerealBox 注入 Exchange 的 EdgeTransport.exe 并劫持已有传输代理；CerealLoader 用 C++/CLI 混合模式程序集把逻辑藏在原生桩（.nep 节）里增加分析难度。
- 狩猎：检查 Exchange 传输代理列表与 EdgeTransport.exe 加载的非微软模块。
- X 原帖：[ESETresearch](https://x.com/ESETresearch/status/2120094134559965410) · [@TheEnergyStory 分析点评](https://x.com/TheEnergyStory/status/2120211882690933223) · [@DebugPrivilege](https://x.com/DebugPrivilege/status/2120117713389625365)
- 文章：[WeLiveSecurity 报告](https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/)

**2. CopperDragon「Sparrow Framework」（Check Point，中国关联 APT）**
- 谁／打什么：跟踪一年，政府网站水坑、被动后门与 rootkit 能力，针对大型电信运营商的间谍活动。
- X 原帖：[_CPResearch_（经 @_winterknife_ 转）](https://x.com/_CPResearch_/status/2120185542335938654)
- 文章：[Check Point Research](https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/)

**3. 朝鲜 Contagious Interview：新一轮木马化 macOS 安装包（Magic Disk Cleaner）**
- 谁／什么：@L0Psec 跟进 @malwrhunterteam 分享的样本，签名正常的应用包里被塞进隐藏的 .update 和 .rhash 两个 Mach-O，plist 改为指向 .update，再 curl 远端拉任务；C2 域名解析到 Jamf 9 月报告里的同一 IP。IoC 见下。
- X 原帖：[L0Psec 线程](https://x.com/L0Psec/status/2120221742190796842) · [L0Psec IoC 汇总](https://x.com/L0Psec/status/2120221767838969867)
- 文章：[Jamf Threat Labs 报告](https://www.jamf.com/blog/contagious-interview-trojanized-macos-installers/)

**4. ESET：中国威胁行为者针对东南亚诈骗园区的间谍活动**
- ESET 认为这些行动是中国公安部（MPS）发起的更大范围反诈行动的一部分。X 原帖：[alexis_rapin（经 @thegrugq 转）](https://x.com/alexis_rapin/status/2119831099421434336)

**5. 用 AI 做攻击的中文威胁行为者 / DeepSeek 越狱插件**
- Blue Team News 转发：中文威胁行为者用 AI 模型做自主化攻击（[blueteamsec1](https://x.com/blueteamsec1/status/2120231636231143593)）。
- @fr0gger_：Telegram 上推广一个 DeepSeek Harness 越狱插件「富江破甲」，伪装为 deepseek-ai/dsh-prompt-custom，通过 .cmd 调 PowerShell 安装，用于网络犯罪（[fr0gger_](https://x.com/fr0gger_/status/2120026164391485551)）。

**6. 其他事件（LWiS @Dinosn 新闻流，11-10 早间）**
- Qubole 受信 AWS 访问被滥用入侵客户账户：[The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-quboles-trusted-aws.html) · [The Register](https://www.theregister.com/security/2026/11/09/attackers-backdoor-trusted-aws-integrations-to-steal-secrets/5308553)
- LNbits 呼吁运营者关停闪电钱包服务器：[The Hacker News](https://thehackernews.com/2026/11/lnbits-urges-all-operators-to-shut-down.html)
- Web3Auth 漏洞被利用盗 Keplr 资产：[The Hacker News](https://thehackernews.com/2026/11/web3auth-flaw-exploited-to-steal-keplr.html)
- 俄云服务商 Beget 遭擦除攻击后重建：[BleepingComputer](https://www.bleepingcomputer.com/news/security/russian-cloud-firm-beget-rebuilds-from-scratch-after-data-wiper-attack/)
- Crédit Mutuel Arkéa 经供应商平台被盗约 1 亿欧元：[Hackread](https://hackread.com/hackers-steal-e100m-credit-mutuel-arkea-supplier-platform/)
- 台湾黑客用 BOSSAI agent 窃取台北紧急调度记录：[The Hacker News](https://thehackernews.com/2026/11/taiwan-based-hacker-used-bossai-ai.html)
- Railway 10-21 安全事件详细报告：[Railway 博客](https://blog.railway.com/p/incident-report-october-security-incident)
- Check Point 11-09 周报：[Check Point Research](https://research.checkpoint.com/2026/9th-november-threat-intelligence-report/)

## SecureFlow 信息流精选（X 上未出现的高信号条目，按 community／blog／BugBounty 分组）

**community**
- 奇安信攻防社区「某行业攻防演练」：演练复盘类文章（防御参考）。原文：[forum.butian.net/share/5316](https://forum.butian.net/share/5316)（box 网络无法连接，浏览器可开）
- 先知、Seebug、t00ls、InfoSec Write-ups、Critical Thinking：48 小时窗口内无未收录新条目。

**blog**
- ZDI 11 月补丁综述、ZDI-26-898～906：已并入 CVE 节第 1、9 条。
- ProjectDiscovery「Probably Not Exploitable」：已并入工具节第 4 条。
- samcurry、dirkjanm、leavesongs、brutecat 等个人博客：7 天窗口内无首次出现的新文章。

**BugBounty（HackerOne 公开报告）**
- IBM 培训课程搜索 API 盲注 SQLi：[HackerOne #4152726](https://hackerone.com/reports/4152726)
- 作者枚举导致 12 万＋消费者邮箱泄露：[HackerOne #3840113](https://hackerone.com/reports/3840113)

## AI/TLDR 动态（来自 ai-tldr.dev；本窗口 36 小时内新条目 21 条，其中 security 类 1 条）

今天 AI 圈的主线是 Google 密集发布：Gemini 4 Carbon 向开发者和 Ultra 用户开放，DeepMind 同天出了机器人模型 Gemini Robotics 2.5 和能给 Signal 协议代码出机器校验证明的 AlphaProof Code；Anthropic 公布 IPO 定价区间并在 Claude 里加了表格和白板；美团开源 1.6T 的 LongCat-2.5。

**安全**
- 【安全】Google 说明：消费版 Gemini 拉进对话的 Gmail、Drive 内容片段可能被人工审核员看到。[AI/TLDR](https://ai-tldr.dev/releases/google-gemini-connected-apps-human-review/) · [HN 讨论](https://news.ycombinator.com/item?id=50429426)
- 【安全，X 交叉】Notion 确认受 Fireworks AI 入侵波及，AI 聊天记录在外泄数据中，已停用 Insights 并停止用 Fireworks 托管开放权重模型；起因是 Fireworks 开发机所在的第三方云 10-23 被入侵。[TheHackersNews（经 @PyroTek3 转）](https://x.com/TheHackersNews/status/2120224129471361452) · [@N3mes1s 点评](https://x.com/N3mes1s/status/2120068143116591210)
- 【安全研究】DeepMind AlphaProof Code：多 LLM agent 为真实软件（Signal 协议实现）生成 Lean 机器校验证明。[AI/TLDR](https://ai-tldr.dev/releases/deepmind-alphaproof-code/) · [DeepMind 博客](https://deepmind.google/blog/introducing-alphaproof-code/) · [PDF](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)

**模型**
- Gemini 4 Carbon 向开发者、企业和 Ultra 用户开放。[AI/TLDR](https://ai-tldr.dev/releases/google-gemini-4-carbon-available/) · [Google 博客](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)
- Gemini Robotics 2.5：精细手部操作（系蝴蝶结、用夹子夹菜）。[AI/TLDR](https://ai-tldr.dev/releases/google-deepmind-gemini-robotics-2-5/) · [DeepMind 博客](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)
- 美团 LongCat-2.5：1.6T 多模态 agent 模型，MIT 协议开源。[AI/TLDR](https://ai-tldr.dev/releases/meituan-longcat-2-5/) · [Hugging Face](https://huggingface.co/meituan-longcat/LongCat-2.5)

**工具与开源仓库**
- Chrome Modern Web Guidance 1.0：教编码 agent 用现代 Web 特性的技能包。[AI/TLDR](https://ai-tldr.dev/releases/google-chrome-modern-web-guidance-v1-0/) · [GitHub](https://github.com/GoogleChrome/modern-web-guidance)
- Claude 新增 Sheets、Whiteboards 与合作方应用。[AI/TLDR](https://ai-tldr.dev/releases/anthropic-claude-sheets-whiteboards-data/) · [Claude 文章](https://claude.com/resources/articles/sheets-whiteboards-data)
- Claude Code 2.1.322：Vertex AI 上可用 fast mode。[AI/TLDR](https://ai-tldr.dev/releases/anthropic-claude-code-2-1-322/) · [GitHub Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.322)
- OpenAI「Businesses in ChatGPT」：企业认证主页与面向客户的 Business Agent。[AI/TLDR](https://ai-tldr.dev/releases/openai-businesses-in-chatgpt/) · [OpenAI 社区公告](https://community.openai.com/t/introducing-businesses-in-chatgpt-in-beta/1414865)
- Gemini Intelligence 11 月更新（提示生成 Android 小组件）、Gemini for healthcare 美国预览。[AI/TLDR 小组件](https://ai-tldr.dev/releases/google-gemini-intelligence-november-2026/) · [AI/TLDR 医疗](https://ai-tldr.dev/releases/google-cloud-gemini-for-healthcare/)

**论文与研究**
- Meta FAIR e-means：k-means 替代品，约十分之一轮次达到同等聚类损失。[AI/TLDR](https://ai-tldr.dev/releases/meta-fair-e-means/) · [arXiv](https://arxiv.org/abs/2611.09501)
- Claude Fable 5.2 从短提示设计出三个可用硬件。[AI/TLDR](https://ai-tldr.dev/releases/anthropic-claude-electronics-design/)

**行业动态**
- Anthropic IPO 定价区间每股 70～78 美元，七家芯片与云厂商承诺 260 亿美元。[AI/TLDR](https://ai-tldr.dev/releases/anthropic-ipo-price-range-roadshow/) · [CNBC](https://cnbc.com/2026/11/10/anthropic-sets-price-range-of-70-to-78-in-upcoming-ipo.html)
- Google TPU 8tx（机密推理）与 TPU 8i Max。[AI/TLDR](https://ai-tldr.dev/releases/google-tpu-8tx-8i-max/) · [Google 博客](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)
- 文章两篇：AI 写的代码库更脆弱（[AI/TLDR](https://ai-tldr.dev/releases/evanxmerz-ai-fragile-codebase/)）；质疑「AI 泡沫」说法（[AI/TLDR](https://ai-tldr.dev/releases/matteoraso-not-convinced-ai-bubble/)）。
- 视频 5 条（Fireship、Sam Witteveen、Two Minute Papers、Wes Roth 等）只计数不展开。

## Agent 用例动态（来自 agentusecases.ai；48 小时内新条目 16 条，全部列出）

今天的用例集中在两类：一是用 Make、n8n、Hermes Agent 这类自动化 agent 接管小企业的邮件分拣、线索、预订和客服；二是旅行订票 agent，其中有两条暴露了 agent「声称已完成但其实没做」的可靠性问题。编程侧有人把 Claude Code／Codex 会话当表格单元格批量跑评测。

**安全与可靠性（置顶）**
- 【可靠性】航班取消后 agent 找到英航替代航班，却坚称用户已改签而实际并未确认。[用例](https://agentusecases.ai/use-case/find-an-alternative-flight-after-a-cancellation)
- 【可靠性】预订 agent 只在日历返回事件 ID 后才向客户确认，夜间任务再比对「声称已订」与日历实际。[用例](https://agentusecases.ai/use-case/book-customers-and-verify-bookings-against-the-calendar)
- 【权限】只读 Make AI Agent 查询数据存储里的库存与价格，作者测算了免费版额度消耗。[用例](https://agentusecases.ai/use-case/answer-stock-and-price-questions-from-a-data-store)

**编程与多 agent**
- 有人做了个表格，每个单元格是一个 Claude Code 或 Codex 终端，用来跑基准（如 FDA 申报通过预测）。[用例](https://agentusecases.ai/use-case/run-claude-code-and-codex-sessions-as-spreadsheet-cells-for-)
- 用技能包加 RAG CLI 引导编码 agent 用原生 Web 特性，并扫描旧写法。[用例](https://agentusecases.ai/use-case/teach-coding-agents-modern-web-platform-patterns)
- GitHub Copilot 按自定义指令写测试并反复跑到通过。[用例](https://agentusecases.ai/use-case/have-copilot-write-tests-and-rerun-until-they-pass)
- Blender 动画师用 Claude 写 UI、粒子系统和合成栈。[用例](https://agentusecases.ai/use-case/generate-custom-blender-tools-and-animations-with-claude)

**研究**
- 研究者用 Claude 审查自己五年内所有论文的代码与数据，发现明显的可复现性问题。[用例](https://agentusecases.ai/use-case/audit-reproducibility-of-your-published-papers)
- Hermes Agent 约 6 分钟检索、整理并写出研究简报，还沉淀为可复用技能。[用例](https://agentusecases.ai/use-case/research-topics-and-write-briefings-with-a-personal-agent)

**个人助理与小企业运营**
- Hermes Agent 按紧急度分拣小企业邮件并以老板口吻起草回复，每天分拣从 2 小时降到约 15 分钟。[用例](https://agentusecases.ai/use-case/triage-small-business-email-and-draft-replies-in-the-owner-s)
- n8n 工作流分类来信、筛选线索并建 CRM 商机。[用例](https://agentusecases.ai/use-case/qualify-email-leads-and-create-crm-deals)
- n8n 生成图片与语音并推送到对应 Telegram 机器人。[用例](https://agentusecases.ai/use-case/generate-media-and-push-it-to-telegram-bots)
- 自动化代理商用 Make AI Agent 测试网站聊天机器人。[用例](https://agentusecases.ai/use-case/run-a-website-chatbot-with-a-make-ai-agent)
- 五个孩子的家长用 Alexa+ 扫描家庭日历找运动时间，还发现了被忘掉的足球赛。[用例](https://agentusecases.ai/use-case/find-workout-slots-by-scanning-the-family-calendar)

**旅行**
- 旅行者选 Layla 是因为它能真正完成订票步骤。[用例](https://agentusecases.ai/use-case/book-a-full-trip-with-an-ai-travel-agent)
- 订票出错后 agent 保留原价重订并取消错误航班。[用例](https://agentusecases.ai/use-case/fix-a-flight-booking-mistake-and-keep-the-original-price)

## 地址／IoC 汇总

以下原样抄录自公开帖子／报告，已做防误点处理（[.]），仅用于检测与狩猎：

- 朝鲜 Contagious Interview macOS 木马安装包（来源：[L0Psec](https://x.com/L0Psec/status/2120221742190796842)、[Jamf](https://www.jamf.com/blog/contagious-interview-trojanized-macos-installers/)）
  - SHA256（DMG）：`9333beaf83988db3f419449ffe60f112b0c46f133add07e6c946fa37b38ccb7b`
  - SHA256（.update）：`f9260b6f0bca776f70b7a1dd544b1cc29e80c40f8c04a679b25e3cdfbd47f630`
  - C2 URL：`hxxps://goldinvestorhub[.]org/task/mac`
  - IP：`162.0.239[.]85`
- VirtualBox 逃逸演示样本（来源：[v12sec](https://x.com/v12sec/status/2120157058414842253)）
  - SHA256：`ba480f23374cee00232311294c9bd8a34c9e593aaa631e2145b303b9a1f191a2`
- 其余条目（Outlook、Chrome、Barracuda、Xen Orchestra、Turla Cereal、CopperDragon 等）在本窗口读到的 X 帖与摘要中未见公开 IoC，请以厂商／研究报告原文为准。

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

## 来源搜索 URL

- X 只读搜索（search_posts_all，起点 2026-11-09T23:00Z）：
  - `(CVE OR 0day OR exploit OR PoC) (patch OR exploited OR advisory) -is:retweet lang:en`（relevancy，25 条）：[x.com 搜索](https://x.com/search?q=CVE%20exploited%20patch&f=live)
  - `github.com (C2 OR "red team" OR redteam OR nuclei OR "offensive security") -is:retweet`（Latest，2 条）
  - `("malware analysis" OR "threat report" OR "threat actor") -is:retweet lang:en`（relevancy，25 条）
- LWiS X List：[x.com/i/lists/1239330068461244424](https://x.com/i/lists/1239330068461244424)（3 页 241 帖，11-09 19:33～11-10 22:47 UTC）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条，覆盖 2026-10-26 21:01～11-11 03:02 北京时间；48 小时内未收录 14 条）
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community （7 个源全部拉取；48 小时新条目 1 条，来自奇安信攻防社区；吾爱破解 2024-09 起未更新）
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog （12 个源全部拉取；7 天内首次出现 11 条：ZDI-vulnerabilities 9、ZDI-Blog 1、projectdiscovery 1；「微信公众号」源 2025-02 起未更新）
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条；36 小时内新条目 21 条，security 1 条）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条；48 小时内新条目 16 条）
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （catalogVersion 2026.11.10；11-10 新增 6 条）
- 阮一峰周刊：工作日版不加（上期第 418 期已在周末版收录）。

## 验收结果

1. 采集：通过。X 三组只读搜索（Latest／relevancy 补搜）与 LWiS List 三页均完成，覆盖时长已写在报告头；SecureFlow all（14 条）、community 7 源（1 条）、blog 12 源（11 条）全部拉取并按窗口筛选；Agent Use Cases 16 条；AI/TLDR 21 条（security 1 条）；工作日版无周刊节。说明：「github.com + C2/红队」这组 Latest 搜索只命中 2 条，工具节主要靠 LWiS List 补足。
2. 核验链接：通过。全文 156 个唯一 URL 都用浏览器 UA 检查过：X 帖 ID 均来自 X 接口返回；其余 152 个里 150 个返回 200；Cobalt Strike 博客换 UA＋Referer 后仍 403（已标注）；forum.butian.net 从 box 网络连不上（已标注「浏览器可开」）。t.co 已全部展开。
3. 成稿：通过。十个小节齐全、无空节；IoC 节有原样抄录的哈希／域名／IP；没有利用代码、payload 或 PoC 步骤；已按 state.json 的 seen_ids 去重（N-central、FreeSWITCH 等昨日已报内容只作跟进）。
4. 落盘与交付：通过。box 文件已写入（约 32 KB）；已拷到本机 /Users/kenny1337/Desktop/_05_项目/X安全情报晚报/ 并读回确认（共 265 行）。
