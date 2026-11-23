# X 安全情报晚报 · 2026-11-22（周日）

> 报告时间：2026-11-22 约 19:51（America/Santiago），即 2026-11-23 约 06:51（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-21 22:51 UTC 到 11-22 22:51 UTC（约 24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-22 22:46:57～22:50:49 UTC（约 4 分钟，CVE／POC／exploit 关键词噪声刷屏），所以加了 relevancy 补搜 25 条（11-21 23:37:47～11-22 20:39:57 UTC，约 21.0 小时），以及编号 CVE-2026／KEV／advisory 关键词 recency 25 条（11-22 21:03:16～22:50:42 UTC，约 1.8 小时，仍偏短）。另一次试图按 `min_likes:5` 做高互动补搜，但公开搜索接口去掉了该过滤器，结果窗口只有约 18 分钟，不计入有效覆盖。窗口起点 11-21 22:51 至 11-21 23:37 的约 46 分钟，主要靠工具组 Latest 与 LWiS List 补上。
> - 工具组 Latest 14 条覆盖 11-21 23:00:20～11-22 21:36:28 UTC（约 22.6 小时，距窗口起点约 9 分钟）。
> - 威胁组 Latest 25 条只覆盖 11-22 18:07:12～22:20:55 UTC（约 4.2 小时），relevancy 补搜 25 条覆盖 11-21 23:31:20～11-22 21:29:38 UTC（约 22.0 小时）。
> - LWiS List（`list:1239330068461244424` 只读 Latest）首屏 25 条覆盖 11-22 19:48:50～22:44:31 UTC；再翻 6 页共 128 条，覆盖 11-21 22:53:39～11-22 19:30:29 UTC。合并去重后约 153 条，整体 11-21 22:53:39～11-22 22:44:31 UTC（约 23.85 小时，距窗口起点约 2.6 分钟）。
> **其他信源**：SecureFlow 的 all／community／blog 三路接口（含站点首页）均返回 **HTTP 522**，随后用浏览器 UA＋站点 Referer 重试仍为 **522**（Cloudflare 源站错误，与 11-19 期相同，不是 UA 问题）。community／blog 各源未能逐个拉取，本窗口 SecureFlow 新条目计为 0，并在对应小节与来源节如实写明。pwn.watch 订阅源已拉取 100 条，**本窗口无新条目**（最新条目发布于 2026-11-08 20:19:52 GMT）。ExploitGrid exploits 列表已拉取 100 条，严格 48 小时窗口内新条目 0（列表最新 `date` 为 2026-11-20 19:48:48 UTC，略早于 48 小时起点 11-20 22:51 UTC）；因 11-20／11-21 两期未出报，今日 X 上讨论的 Etherpad CVE-2026-114516 与 11-20 收录的 CRITICAL 条目 EtherPadSniper（`EGE-GH-XMUshAT`）交叉合并，只记「已有公开 exploit」并附 ExploitGrid 页面，不链 PoC 仓库。ExploitGrid KEV 期限 10 条与 CISA 官方一致。CISA KEV 目录当前 1790 条，本 48 小时窗口无新增；11-20 新增的 4 条（上期 11-19 报告之后、随后两期失败未收录）今日在 X 上讨论密集，且联邦修补期限为 11-23，按新出现情报展开。AI/TLDR 订阅源 50 条，本窗口（约 36 小时，且不在 seen_ids）新条目 **19**，其中 security **3**；其 releases 详情页换 UA＋Referer 后仍 **403**，报告保留订阅链接并用已核验的原始来源页补链。Agent Use Cases RSS 120 条，本窗口（约 48 小时）新条目 **66**。因 11-21（周六，Santiago）那期失败未出报，本期补上阮一峰《科技爱好者周刊》第 420 期（2026-11-20 发布，不在 seen_ids）。
> **验收**：采集——SecureFlow 三路失败已如实写明，其余信源已拉取并按窗口筛选；核验链接——主链接已用浏览器 UA 抽查，404 已丢弃，AP News 与 AI/TLDR releases 页仍 403 已注明并改用或并列可打开的原文；成稿——周末版十一节齐全，无利用代码／payload／PoC 步骤；落盘与交付见文末。

## 今日摘要

- **今晚最紧急的是 4 条将于 11 月 23 日到期的 CISA KEV**：VMware vCenter 认证绕过（CVE-2026-123890）、Cisco Expressway 预认证 root 命令执行（CVE-2026-76466）、Apache Roller XML-RPC 反序列化 RCE（CVE-2026-129448）、SAP NetWeaver Enterprise Portal（CVE-2025-42884）。这 4 条是 11-20 才进入目录的，上期（11-19）之后的两期日报未能交付，故本期完整收录。香港时间已到 11-23 清晨，Santiago 报告日仍为 11-22 晚，期限在数小时内到来。
- **Amazon 披露中国关联行为体用开源自主渗透框架 Cairn 的 AI agent，在约 11 分钟内自己发现并利用了医疗影像标注软件 MONAI Label 的 0day**（CVE-2026-133968，CVSS 9.8）。官方安全版本 **0.8.6 已于今日发布**。Risky Business #860 的主题「Agentic hacking has crossed a threshold」与此事直接相关。
- Ghostscript「Upload2Shell」（CVE-2026-125396）在 X 上热度很高（@PaulosYibelo 研究帖互动高），根因补丁已在 10.08.0；尚未进入 KEV，也有观点认为「每个上传框都会中招」的表述偏夸大，但仍建议核对本站预览／转码链路里的 Ghostscript 版本。
- Etherpad 预认证任意文件读取（CVE-2026-114516，CVSS 9.8）今日有「已有公开 exploit」的提醒，修复版本为 3.3.3。
- FBI 正在调查其全国执法数据库 NCIC 的疑似入侵；eMudhra 证书事件仍有跟进。另补上周六未出的阮一峰周刊第 420 期。

## CVE / POC / 漏洞

### 1. CISA KEV 四条将于 11-23 到期（11-20 入目录，本期首次完整收录）

CISA 于 11 月 20 日一次加入 4 条已知被利用漏洞，联邦机构修补期限均为 **2026-11-23**。本期 KEV JSON 显示 11-20 之后没有再新增。ExploitGrid 的 active-deadlines 与官方一致。

- CISA 公告：https://www.cisa.gov/news-events/alerts/2026/11/20/cisa-adds-four-known-exploited-vulnerabilities-catalog

#### 1.1 VMware vCenter 认证绕过 CVE-2026-123890（CVSS 9.8）

- 说明：Broadcom／VMware vCenter Directory Service 存在认证绕过，网络攻击者可获得管理员权限。X 上今日跟进称，中国关联团伙 Armory Castle（有帖写作 ARMORY CASTLE）自 9 月起将其作为 0day 利用，并窃取 SAML 签名材料；因此「只打补丁不够」，怀疑失陷时还需按厂商指引轮换 STS 签名密钥与证书。官方顾问为 VMSA-2026-0009，**没有临时缓解措施**，也不能用 Quick Patch。升级目标包括 vCenter 8.0 U3m、9.0.x 至 9.0.2.0200、9.1.x 至 9.1.1.0200。
- X 原帖：https://x.com/abstraction_log/status/2124603675230490892 · https://x.com/yabetchi_iPhone/status/2124632266030911969 · https://x.com/catnap707/status/2124615821108650168 · https://x.com/Yasser_924/status/2124616890798477664
- 厂商公告：https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/VMSA-2026-0009--VMware-vCenter--Tools--and-SDDC-Manager-updates-address-multiple-vulnerabilities--CVE-2026-123890--CVE-2026-123891--CVE-2026-123892--CVE-2026-123893--CVE-2026-123894-/39495 · https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0009/README.md
- 厂商公告（KEV／NVD／交叉）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-123890 · https://nvd.nist.gov/vuln/detail/CVE-2026-123890 · https://www.cyber.gc.ca/en/alerts-advisories/vmware-security-advisory-av26-1185
- 文章／PDF：https://tldrcve.com/vcenter-zero-day/

#### 1.2 Cisco Expressway 预认证 root 命令执行 CVE-2026-76466（CVSS 9.8）

- 说明：Cisco Expressway-C／Expressway-E 的数据库服务存在硬编码凭据等问题（CWE-798，顾问 cisco-sa-vcs-static-cred-hr7EWZ8t），未认证远程攻击者可在设备上以 root 执行操作系统命令。影响集群中运行 X15.5.3 及更早版本的节点；修复版本为 **X15.5.20**，X14 及更早需迁移到已修复版本。**无临时缓解措施**。已确认被利用，有帖称 PoC 出现后很快出现在野利用。CISA KEV 期限 11-23。
- X 原帖：https://x.com/YourDailyCVE/status/2124474924001898900 · https://x.com/Q_cccat/status/2124628802097893886 · https://x.com/ALLITAustralia/status/2124622941359079720
- 厂商公告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-76466 · https://nvd.nist.gov/vuln/detail/CVE-2026-76466

#### 1.3 Apache Roller XML-RPC 反序列化 RCE CVE-2026-129448（CVSS 9.8）

- 说明：Apache Roller 4.0.0 至 6.1.4 的 XML-RPC 端点在认证前反序列化厂商扩展类型，未认证即可远程代码执行，且正在被活跃利用。官方建议升级到 **6.1.6 或更高**（有帖建议直接到 6.1.7）。**仅在管理界面关闭 XML-RPC 不够**；无法立即升级时应按公告在 `WEB-INF/web.xml` 中关闭扩展或移除 `/roller-services/xmlrpc` 映射并重启。CISA KEV 期限 11-23。
- X 原帖：https://x.com/superdoccimo/status/2124590283115426260 · https://x.com/InadaITReporter/status/2124636551732707675 · https://x.com/deadhandhq/status/2124286412640121008 · https://x.com/BlueVigilint/status/2124632842730647723
- 厂商公告：https://lists.apache.org/thread/q573hvzrjyjvb5z600z8hgk044jqfshc · https://roller.apache.org/security.html · https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-129448 · https://nvd.nist.gov/vuln/detail/CVE-2026-129448

#### 1.4 SAP NetWeaver Enterprise Portal CVE-2025-42884

- 说明：与上述三条同日进入 KEV，期限同样是 11-23。CISA 描述为 Enterprise Portal 数据查询逻辑中对特殊元素处理不当。本日 X 上多出现在「今日到期四件套」汇总里，细节讨论少于前三条，但仍应按 SAP 与 CISA 指引优先修补。
- X 原帖：https://x.com/yabetchi_iPhone/status/2124632266030911969 · https://x.com/P7RIM3/status/2124629981829689711
- 厂商公告：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-42884

### 2. MONAI Label 路径遍历 RCE CVE-2026-133968（CVSS 9.8，AI agent 自主发现并已被在野利用）

- 说明：Amazon Threat Intelligence（AWS Security Blog，11-20）披露，中国关联行为体只给开源自主渗透框架 **Cairn** 下达「拿到 shell」一类目标，其 AI agent 在约 11 分钟内对东亚一所大学的 MONAI Label 服务器走完侦察、发现未知路径遍历并写入文件，进而取得 root。漏洞影响 **≤0.8.5**：`PUT /datastore/image` 与 `PUT /datastore/label` 未把目标路径限制在数据存储内。默认认证关闭。项目安全公告为 GHSA-qc22-rmgc-vg94。**修复版 0.8.6 已于 11-22 01:29 UTC 发布**（`pip install -U monailabel==0.8.6` 或拉取对应容器镜像）。在升级前应限制网络暴露，并考虑启用 `MONAI_LABEL_AUTH_ENABLE=True`、以最小写权限运行服务。此条同时属于 AI 安全，与 AI/TLDR、Risky Business #860 交叉。
- X 原帖：https://x.com/dzqyzy/status/2124312037975310611 · https://x.com/ICHI_Global/status/2124399992978715011 · https://x.com/wirelesslyhere/status/2124530248293531654 · https://x.com/plyra/status/2124618571548614869 · https://x.com/TotallyLogit/status/2124544770018320654
- GitHub／公告：https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94 · https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6
- 厂商公告／文章：https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/ · https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html · https://risky.biz/RB860/

### 3. Ghostscript「Upload2Shell」沙箱逃逸 CVE-2026-125396

- 说明：@PaulosYibelo（pwn.ai）11-21 发布研究：Ghostscript Type 1 字体加载器中的 use-after-free 可绕过 `-dSAFER`，使图像／PDF 预览或转码链路变成命令执行面。根因修复已包含在 **Ghostscript 10.08.0**（研究页称 9 月 8 日已放出）。该洞不在 CISA KEV，亦未见公开在野利用的权威确认；@CVEStormSiren 等认为「每个上传框都会中招」的传播偏夸大（评分约 8.5），但仍建议向托管方确认预览链路中的 Ghostscript 是否已到 10.08.0。只记录存在公开研究这一事实，不转载利用步骤。
- X 原帖：https://x.com/PaulosYibelo/status/2124277899557822687 · https://x.com/CVEStormSiren/status/2124286181772849536 · https://x.com/superdoccimo/status/2124635387343560993 · https://x.com/CybercaveTech/status/2124634533572313166
- 文章／PDF：https://pwn.ai/upload2shell/research.html

### 4. Etherpad 预认证任意文件读取 CVE-2026-114516（CVSS 9.8，已有公开 exploit）

- 说明：Etherpad `/static/*` 在认证中间件之前处理路径，1.8.14 至 3.3.2 会在净化之后把编码反斜杠转成正斜杠，从而可读出服务器上任意文件。修复版本为 **3.3.3**。今日 X 有「Public PoC out」提醒；ExploitGrid 在 11-20 以 CRITICAL 收录相关条目（`EGE-GH-XMUshAT`），因稍早于严格 48 小时窗口、且 11-20／11-21 两期未出报，在此与今日讨论合并。只写已有公开 exploit，并附 ExploitGrid 与顾问页，**不链 PoC 仓库、不写利用步骤**。
- X 原帖：https://x.com/SecAlertsCo/status/2124636163164008625
- 厂商公告：https://github.com/ether/etherpad/releases/tag/v3.3.3 · https://github.com/advisories/GHSA-mc8w-wjhw-45x5
- 文章／PDF：https://neodyme.io/advisories/cve-2026-114516/ · https://exploitgrid.net/vulnerabilities/CVE-2026-114516 · https://exploitgrid.net/exploits/EGE-GH-XMUshAT

### 5. FastUnlock：Windows 讲述人锁屏绕过（物理接触 0day，正在 X 传播）

- 说明：@r1cksec 转发 MSNightmare／FastUnlock 仓库，称其为 Windows Narrator 锁屏绕过 0day。公开报道称其针对较新的 Windows 11 版本，需要本地／物理接触（并与联机账户等条件有关），不是远程 RCE。防御上可考虑用 AppLocker／WDAC 限制 `Narrator.exe`（会牺牲讲述人无障碍功能）。此处只记录存在公开讨论与仓库这一事实，不写操作步骤。
- X 原帖：https://x.com/r1cksec/status/2124445352938103282
- GitHub：https://github.com/MSNightmare/FastUnlock

### 6. 其他需留意的修补与讨论（信号低于以上条目）

- **已到期仍被点名**：Apache Axis 1.x CVE-2026-90436（KEV 期限 11-21，未认证 SOAP 反射／类实例化 RCE）；Synology DSM CVE-2024-10441、REDCap CVE-2026-90817 同日到期。SonicWall SSL VPN CVE-2026-19868 期限为 11-20。https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-90436
- **即将到期（11-24）**：Outlook／Microsoft Office CVE-2026-124194、Chrome／Chromium CVE-2026-125350、Cisco BroadWorks CVE-2026-20320、Openwave CVE-2026-111793。稍后还有 Puppet Enterprise CVE-2026-115731（12-01）、LiteLLM CVE-2026-40217（12-02）。
- **Java4Shell CVE-2026-114938 跟进**：有帖更正称 Red Hat 已提供修复后的 OpenJDK，不再是补丁计划中的缺口。不重复展开原理。X 原帖：https://x.com/modularciso/status/2124568343416012825
- **N-able MailAssure／SpamExperts CVE-2026-134624**（CVSS 9.3）：配置了 relay 时，经认证的 API 用户可通过 LDAP 同步检查做 SSRF。厂商称已修复（版本目标有帖写 20261121.1943），托管云仪表盘与 API 已恢复，邮件过滤未中断，并称除一台托管服务器外未见利用。X 原帖：https://x.com/BIMDefense/status/2124628576980910292 · https://x.com/DailyDarkWeb/status/2124626378884616364
- **Weblate 密码重置接管 CVE-2026-134838**（CVSS 9.1）：未认证攻击者可利用大小写折叠后的相似邮箱重置密码。修复版本有帖写 2026.11。X 原帖：https://x.com/cvedotnow/status/2124632114142286151
- **Bitcoin Core CVE-2026-117348**（中危）：有帖称 Block 的 Project Loupe 用 AI 扫描发现，对端可通过大量重复孤儿交易 inv 让节点停顿十余秒；已在 30.5／31.3／32.1 修复。X 原帖：https://x.com/grok/status/2124620298314019127 · https://x.com/sakuyasol/status/2124625503495901605
- 其余单帖或证据不足、本期不作为已确认要闻展开：DBHub CVE-2026-134803（有回复称 VulnCheck 顾问今日出现、修复在 1.7.0，未见广泛讨论）；GnuPG／GPGME CVE-2026-129975、TrueConf CVE-2026-72530（顾问被指细节不足）、Check Point Gaia CVE-2026-123039（扫描器账号推送）、D-Link DIR-600L CVE-2026-133993（EOL、声称无补丁）、Linux NFSD CVE-2026-99362、KVM 隔离 CVE-2026-99312、AMD PSP boot ROM CVE-2026-74127（仅 Zen 1／Zen+，需本地 SPI 闪存写入）、WordPress 插件存储型 XSS、Google Cloud Application Integration CVE-2026-85298（研究者分享自己获得的 CVE 编号，不是今日新爆发事件）。

## 工具与 GitHub 发布

### 1. Claude-BugHunter 持续热门：面向缺陷狩猎的 Claude Code skill 包

- 说明：@trending_repos 统计该仓库 24 小时新增约 1,803 star，总量约 16,815。定位是缺陷狩猎与外部红队用的 Claude Code skill 集合（仓库页称 82 个 skill、15 条斜杠命令等）。仅用于授权测试。上期已出现，今日热度仍高，作简要跟进。
- X 原帖：https://x.com/trending_repos/status/2124475007032324143 · https://x.com/yaro360/status/2124276756794192157
- GitHub：https://github.com/elementalsouls/Claude-BugHunter

### 2. SpringBoot-Scan V3.1.1

- 说明：@AabyssZG 宣布 SpringBoot-Scan 更新到 V3.1.1，新增对 2025–2026 若干高危 CVE 的支持，项目已维护约 3 年 10 个月。用于授权的 Spring Boot 资产与漏洞检查。仓库页 HTTP 200。
- X 原帖：https://x.com/AabyssZG/status/2124415026857713869
- GitHub：https://github.com/AabyssZG/SpringBoot-Scan

### 3. Ciel：可在非特权 Linux 上做 AD／Kerberos 分诊的 C2 控制台

- 说明：@sacrifice9091 与 @l0rdmalware 介绍 Ciel：Go teamserver 加原生 Qt6 界面，用于在无 root 的 Linux 上做 Kerberos 分诊与域会话测绘，仓库声明 GPLv3。帖文提醒项目很新、星标少、未经审计，只建议实验室／授权环境使用。
- X 原帖：https://x.com/sacrifice9091/status/2124502726499524895 · https://x.com/l0rdmalware/status/2124522941547446451
- GitHub：https://github.com/Mafifrizi/ciel

### 4. WhisperLoader、LogonStealer、EdgeShot、AgentsAllTheThings、llm-redteam-kit（简讯）

- 说明：@l0rdmalware 提到 Maldev Academy 的 WhisperLoader（线程名传递与 TP_DIRECT.Callback 相关的进程注入加载器，供蓝队检验 EDR）以及 Fir3n0x／EdgeShot（Mythic C2 的 Chromium MV3 扩展型 agent）。@r1cksec 介绍 LogonStealer，滥用 Credential Provider 接口从 logonui.exe 侧窃取明文口令，属凭据盗窃类开源工具，仅限授权测试。nullthrix／AgentsAllTheThings 把 OpenCode 配成带大量 skill 与 MCP 的赏金／授权测试 rig，帖文强调当日新建、零星标、未审计。gravion-ux／llm-redteam-kit 按 OWASP LLM Top 10 做回归探测。上述均只登记仓库与用途，不转载实现细节。
- X 原帖：https://x.com/l0rdmalware/status/2124522902934659391 · https://x.com/r1cksec/status/2124436817168462325 · https://x.com/l0rdmalware/status/2124332614337130778 · https://x.com/l0rdmalware/status/2124618037261472150 · https://x.com/_x_priyanshu/status/2124427678837338286
- GitHub：https://github.com/Maldev-Academy/WhisperLoader · https://github.com/S12cybersecurity/LogonStealer · https://github.com/Fir3n0x/edgeshot · https://github.com/nullthrix/AgentsAllTheThings · https://github.com/gravion-ux/llm-redteam-kit

### 5. OWASP Xpsd：用 LLM agent 做漏洞可达性分诊

- 说明：@Dinosn 介绍 OWASP／Xpsd，把扫描器发现交给 LLM agent 阅读源码，判断哪些 CVE 真正可达，用于减少不可达漏洞的噪音。仓库页 HTTP 200。
- X 原帖：https://x.com/Dinosn/status/2124458480757297488
- GitHub：https://github.com/OWASP/Xpsd

### 6. 绕过 Windows 应用白名单（dotSec 文章）

- 说明：@ipurple 分享 dotSec 文章《Bypassing Windows application whitelisting》，讨论不安全反序列化与应用控制绕过。只记录文章存在，不转载绕过步骤。
- X 原帖：https://x.com/ipurple/status/2124501422091776326
- 文章／PDF：https://www.dotsec.com/insecure-deserialisation-app-control-bypass/

## APT / Malware 分析

### 1. FBI 正在调查 NCIC 全国执法数据库疑似入侵

- 说明：@Dinosn 转发报道：美联社消息称，FBI 正在调查其关键全国刑事司法数据库（NCIC，供全美执法查询犯罪记录、通缉、失踪人口、被盗财物等）的疑似入侵。发现时间较近，规模、是否被窃改数据以及入侵途径均尚未公开。AP News 原页用浏览器 UA＋Referer 后仍返回 **403**，改以 SecurityWeek 转述页（HTTP 200）为可打开的文章链接，并保留 AP 链接备查。
- X 原帖：https://x.com/Dinosn/status/2124331595460911412
- 文章／PDF：https://www.securityweek.com/fbi-investigating-apparent-hack-of-its-key-national-criminal-justice-database-ap-source-says/ · https://apnews.com/article/fbi-database-ncic-hack-d066cff87a64a564db0a00172c124972 （403）

### 2. 中国关联行为体以 Cairn AI agent 开展入侵（与 MONAI 0day 为同一活动）

- 说明：见 CVE 节第 2 条。Amazon 将活动归为 Chinese-nexus，使用开源 Cairn 框架的 agent 在几乎无人值守的情况下发现并利用未知漏洞。这是本期最重要的威胁侧叙事，也是 Risky Business #860 的核心背景。
- X 原帖：https://x.com/dzqyzy/status/2124312037975310611
- 文章／PDF：https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/ · https://risky.biz/RB860/

### 3. eMudhra 中间 CA 私钥事件跟进

- 说明：@howardnoakley 今日发文更新 eMudhra 证书事件（「Compromised eMudhra certificates, an update」）。该事件此前已有 Google、Mozilla 等为保护用户而采取的中间证书不信任／保护措施。此处作为持续事件的更新记录，不展开历史细节。
- X 原帖：https://x.com/howardnoakley/status/2124616574829314245
- 文章／PDF：https://eclecticlight.co/2026/11/22/compromised-emudhra-certificates-an-update/ · https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/ · https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/

### 4. 其他威胁简讯

- 说明：@fr0gger_ 在讨论中提到 n0n 勒索软件正在使用「被削弱安全对齐」的编码 agent 协助行动，仅一条回复、无独立报告或 IoC，暂作观察。X 上还有 Meduza Locker／FALCON 等对具体公司的勒索声明，属威胁情报账号的索赔播报，未经本报告独立核实，不展开。@cyb3rops 的「new threat landscape」帖引用了其他用户帖，本身不是一份新的恶意软件分析。
- X 原帖：https://x.com/fr0gger_/status/2124402836641312846

## SecureFlow 信息流精选

本日无显著更新。SecureFlow 的 all、community、blog 三路公开接口及站点首页均返回 HTTP 522（Cloudflare 源站错误）；使用浏览器 UA 并加站点 Referer 后重试，结果相同。因此未能按源拉取先知／奇安信攻防社区／Seebug／ZDI 等条目，本窗口新条目计 0。forum.butian.net 未在本期单独探测；按既有经验，即便接口恢复，该论坛从 box 仍可能出现网络层超时（应标注为「box 网络无法连接，浏览器可开」，而不是 403）。

## AI/TLDR 动态

今日 AI 圈与安全重叠最明显的三条是：Dragos 用约 200 万条带金丝雀的提示词探测 AI 推理供应链、欧盟委员会确认针对内部系统的 AI 辅助入侵，以及 Google 公开用「Mirror Dimension」隔离环境测试 Chrome 浏览 agent。模型与工具侧则有 Apple Depth Pro 2、Hugging Face Transformers v5.24.0、OpenAI GPT-Live-1.1，以及一篇关于 Claude Code「网络攻击防护」误伤正当修复的评论。本窗口新条目 **19**（其中 security **3**，另有 video／showcase 若干只计数或从简）。ai-tldr 的 releases 详情页抽查为 **403**（换 UA＋Referer 后仍 403），下面同时给出已核验可打开的原始来源。

### 安全

- **Dragos 金丝雀探测 AI 推理供应链**：约 200 万条植入金丝雀的提示词显示，请求在途中被何处读取；公开报道称三家推理／托管提供商出现泄露或日志被访问题。AI/TLDR：https://ai-tldr.dev/releases/dragos-ai-supply-chain-canaries/ （403） 原始来源：https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens · https://lava.security/blog/ai-inference-canary-research-prompts-exposed
- **欧盟委员会确认 AI 辅助网络攻击，员工系统中断 10 天以上**：委员会称 10 月 22 日发现、26 日确认针对内部系统的活动，CERT-EU 认为公开的 AI 漏洞扫描工具 ARTEX 可能被使用；受影响的包括人事／报销等面向员工的系统及翻译服务，多数已恢复，目前未见大规模员工数据失窃或勒索声明，调查仍在进行。AI/TLDR：https://ai-tldr.dev/releases/european-commission-artex-ai-cyberattack/ （403） 原始来源：https://therecord.media/european-commission-confirms-cyberattack-using-ai · https://www.computerweekly.com/news/366654974/AI-red-team-tool-Artex-likely-behind-cyber-attack-on-EU-body
- **Google Mirror Dimension：给 Chrome 浏览 agent 用的假互联网**：在隔离环境中生成大量模拟站点，并注入隐藏的提示词注入载荷，用于安全测试而非替代真实互联网。AI/TLDR：https://ai-tldr.dev/releases/google-chrome-mirror-dimension-agents/ （403） 原始来源：https://blog.google/security/mirror-dimension-for-agents/
- **Herman Õunapuu：Claude Code 的网络攻击防护挡住了一行正当修复**（文章类，与安全相关）：开发者反映，防护策略会拦截人们修复自己的代码，而攻击者改用开放模型即可绕过。AI/TLDR：https://ai-tldr.dev/releases/ounapuu-claude-code-cyber-safeguards/ （403）
- 与 X／Amazon 交叉的 MONAI／Cairn 事件已合并进 CVE 节，此处不重复展开。Fireship 一条回顾当周三起 Web 安全事件的视频只计数，不展开。

### 模型

- Apple 开源 Depth Pro 2，强调物体边缘清晰且帧间稳定的视频深度：https://ai-tldr.dev/releases/apple-depth-pro-2/
- OpenAI GPT-Live-1.1：语音模型在多语言口音上更稳，并带有低费用的静音待机：https://ai-tldr.dev/releases/openai-gpt-live-1-1-api/

### 工具与开源仓库

- Hugging Face Transformers v5.24.0，纳入 Omnilingual ASR、Inkling 2 Mini 等，并统一 KV-cache 参数名：https://ai-tldr.dev/releases/huggingface-transformers-5-24-0/
- LookAtMyQuant：把 Inkling 2 Mini 量化到约 5.4 GB，以便在 Apple Silicon 上运行：https://ai-tldr.dev/releases/shinmegamiboson-lookatmyquant-inkling-2-mini/

### 论文与研究／行业动态

- OpenAI 分享内部预训练损失曲线，并呼吁实验室共同设上限：https://ai-tldr.dev/releases/openai-perplexity-and-intelligence/
- Tim O'Reilly《What Happened to Silicon Valley, and to AI》：强调 AI 建在公地之上，不应变成收费关卡：https://ai-tldr.dev/releases/tim-oreilly-what-happened-to-silicon-valley/
- 外部研究估算 Anthropic 规划数据中心 2028 年电力结构中天然气与煤炭占比较高：https://ai-tldr.dev/releases/better-data-center-project-anthropic-power-mix/
- 传闻（FT）：Amazon 接近以约 75 亿美元收购 Decart，报告仅记为传闻：https://ai-tldr.dev/releases/amazon-decart-acquisition-rumor/
- Mani Doraisamy：当 AI 负责写代码，开发者的工作更接近架构与设计决策：https://ai-tldr.dev/releases/mani-doraisamy-developers-into-architects/
- video／纯 showcase（Worker 755、ClawDOS、Wes Roth 视频、FPGA 上「vibecoding」推理芯片、Lean 证明相关展示等）本窗口有多条，低信号只计数不展开。

## Agent 用例动态

过去约两天（RSS 显示多条的 pubDate 落在 11-21 或 11-22 09:00 GMT），agentusecases.ai 新收 **66** 条。主题仍然以编程与办公自动化、个人助理（日程／邮件／健身饮食）、销售与招聘外联、出行预订为主；电脑操控／浏览器 agent（Claude in Chrome 访问 Outlook 等）继续出现，这类用法本身带有凭据与会话权限风险，放在前面提示，但不复制具体提示词。以下精选约 20 条代表，总数 66。

### 电脑操控与权限相关（请注意会话／凭据范围）

- 有人用 Claude in Chrome 在清晨登录 Outlook，把日程抄到 Gmail 日历并做邮件摘要：https://agentusecases.ai/use-case/sweep-email-and-sync-calendars-each-morning
- 有人用 Claude Code／Cowork 在 Xero 发票从草稿变为已授权后自动保存 PDF 并发给客户：https://agentusecases.ai/use-case/email-authorized-xero-invoices-to-clients-automatically
- 在 DOS 上跑编码 agent（ClawDOS，展示性质）：https://agentusecases.ai/use-case/run-an-ai-coding-agent-on-dos

### 编程、研发与个人工作流

- 用 Grok Bot 处理个体经营者的行政与工作流（也有人反馈后续更新后变差）：https://agentusecases.ai/use-case/run-solopreneur-admin-workflows-with-grok-bot
- 让 Grok Bot 阅读报告并建议下一步：https://agentusecases.ai/use-case/have-grok-bot-read-reports-and-suggest-next-steps
- 用 Gemini 把 Home Assistant 的实体与 YAML 做成专家 agent，辅助生成智能家居配置：https://agentusecases.ai/use-case/build-a-home-assistant-expert-agent-from-your-config

### 销售、招聘与客服

- 用 Claude 驱动的 Lindy agent 找线索并个性化首封外联，有人声称每月约 40 场会议：https://agentusecases.ai/use-case/find-leads-and-personalize-first-outreach
- Lindy 监控 YouTube 评论、识别线索并送进 Slack／CRM：https://agentusecases.ai/use-case/spot-youtube-comment-leads-and-send-to-crm
- 招聘人员用 Claude 连接 ATS，起草岗位说明与电话筛选：https://agentusecases.ai/use-case/query-the-ats-and-draft-intakes-and-phone-screens
- 用 Claude 按职位描述起草个性化招聘外联：https://agentusecases.ai/use-case/draft-personalized-recruiting-outreach-and-find-candidates
- Make 上的 agent 对表单分类（FAQ／报价／紧急）并起草回复，紧急情况再打 Slack：https://agentusecases.ai/use-case/classify-and-reply-to-customer-inquiries-with-an-ai-agent
- Zapier agent 自动处理过去 7 天、低于 50 美元的退款申请：https://agentusecases.ai/use-case/process-small-refund-requests-automatically-with-a-zapier-ag
- 用 Claude 起草不那么「像 AI」的 B2B 合作邮件：https://agentusecases.ai/use-case/draft-b2b-partnership-outreach-emails-that-don-t-sound-like-

### 生活、出行与购物

- 用 Claude 协助房屋买卖流程：https://agentusecases.ai/use-case/assist-a-home-sale-and-purchase-with-claude
- 做饭时用 AirPods 听 Grok 报食谱：https://agentusecases.ai/use-case/get-hands-free-recipes-while-cooking
- 用 Claude 做宏量营养、购物清单、配餐与训练计划：https://agentusecases.ai/use-case/run-fitness-meal-planning-and-weekly-shops
- 有人说 Claude 帮忙做了扫描 eBay、比价并自动出价的应用（涉及自动下单，需自行评估风险）：https://agentusecases.ai/use-case/auto-bid-on-sports-cards-on-ebay
- 测试出行预订 agent，有的在人工核验处卡住：https://agentusecases.ai/use-case/book-travel-with-an-ai-agent
- 用法律向 AI 工具（如 Spellbook、CoCounsel）先过一遍格式合同：https://agentusecases.ai/use-case/spot-issues-in-routine-contracts-with-legal-ai-tools

## 周末：阮一峰周刊精选

因 11-21（周六，America/Santiago）那期失败未出报，本期补录 11 月 20 日发布的《科技爱好者周刊（第 420 期）：最分心的一年》。周刊链接：https://www.ruanyifeng.com/blog/2026/11/weekly-issue-420.html

与 AI agent 相关的放在前面：文章《多智能体系统的三种模式》把同时使用多个代理归纳为管道式、编排式与白板式，https://kadhar.dev/blog/multi-agent-systems-from-scratch

### GitHub 项目（已排除 ruanyf/weekly 自身与 issues 链接）

- sgrep：按语义搜索的 grep 替代，https://github.com/arunsupe/semantic-grep
- Netdata：把服务器与服务状态汇总到同一块仪表板，https://github.com/netdata/netdata
- FlowVision：macOS 瀑布式图片浏览器，https://github.com/netdcy/FlowVision
- 13ft：自建后用于抓取付费墙后网页，https://github.com/wasi-master/13ft
- Srcbook：面向 TypeScript／JavaScript 的网页互动笔记本，https://github.com/srcbookdev/srcbook
- Photoshot：浏览器里的开源图片编辑器，https://github.com/Abraham721/photoshot
- XJY Editor：用表格可视化编辑 XML／KML／JSON／YAML 的静态网页应用，https://github.com/lizhaowu-79/xjyeditor
- GCS：非官方谷歌云命令行客户端，https://github.com/aeroxy/google-cloud-shell-cli
- Waytrace（漫迹）：可在后台记录当日足迹的开源 iOS 应用，https://github.com/lxyeternal/PathTracker
- Tomoru：捕获系统或指定应用声音并显示双语字幕，https://github.com/ACAne0320/Tomoru
- crFiles：桌面文件管理器，内置 Android Quick Share，https://github.com/libcr/crFiles/releases
- Arke：Windows 资源管理器替代，把排序／缩略图／搜索移出界面线程以免卡住，https://github.com/Koimsurai/Arke
- tinybrain：从零用 PyTorch 写一个以中文为主的小模型全流程，https://github.com/cai114514114514/tinybrain
- Lean Init IDE：浏览器里的 Lean 4 练习环境，https://github.com/3y3y3y-huaiji/lean-init-ide

另有非 GitHub 工具 netboot.xyz（把多种操作系统安装介质做进一张启动盘）：https://netboot.xyz/

### 有趣文章（挑 8 篇）

- 黄仁勋事件的深层分析（英文）：https://stratechery.com/2026/obituaries/
- 多智能体系统的三种模式（英文，与 AI agent 相关）：https://kadhar.dev/blog/multi-agent-systems-from-scratch
- 检查空格有多难？（Unicode 空白字符，英文）：https://serce.me/posts/2026-10-30-how-hard-is-it-to-check-for-whitespace
- 闭源模型占据了主导地位（英文）：https://village.dev/blog/closed-ai-models-now-dominate-the-price-performance-frontier/
- 个人如何定制芯片／wafer.space（英文）：https://essenceia.github.io/projects/expresso/ · https://wafer.space/
- AI 芯片的位置验证（IEEE Spectrum，英文）：https://spectrum.ieee.org/find-my-ai-chip
- 未来的战争（文摘，英文）：https://worksinprogress.co/issue/the-future-of-war/
- 生成式 AI 基础数学入门（预印本）：https://arxiv.org/abs/2605.29713

资源里还有《浏览器工程》英文电子书：https://browser.engineering/

## 地址／IoC 汇总

未见公开 IoC。本期高信号条目以漏洞编号、补丁版本与厂商公告为主，X 与公开报道中未见需要原样抄录的 C2 域名、IP、样本哈希或钱包地址。若干勒索索赔播报只给出受害者名称、未附可核验的技术指标，不当作 IoC。

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

## 来源搜索 URL

- X Latest 窗口：2026-11-21T22:51:00Z ～ 2026-11-22T22:51:00Z（America/Santiago 约过去 24 小时）。CVE Latest 25 条／约 4 分钟；CVE relevancy 25 条／约 21.0 小时；CVE advisory recency 25 条／约 1.8 小时；工具 Latest 14 条／约 22.6 小时；威胁 Latest 25 条／约 4.2 小时；威胁 relevancy 25 条／约 22.0 小时。LWiS List 只读时间线约 153 条／约 23.85 小时。合并去重后进入原始采集集的独特 X 帖约 195 条（各组 Latest／补搜）再加上 List 专有帖。
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 —— **HTTP 522**，新条目 0。
- SecureFlow community 源列表：https://secureflow.scope-sentry.top/api/rss/category?category=community —— **HTTP 522**，源数 0，新条目 0（48 小时窗口未能筛选）。
- SecureFlow blog 源列表：https://secureflow.scope-sentry.top/api/rss/category?category=blog —— **HTTP 522**，源数 0，新条目 0（7 天窗口未能筛选）。
- pwn.watch RSS：https://pwn.watch/feed.xml （另 JSON https://pwn.watch/feed.json）—— 拉到 100 条，本窗口新条目 **0**（最新 pubDate 2026-11-08 20:19:52 GMT）。
- ExploitGrid exploits：https://api.exploitgrid.net/api/exploits?page=1&limit=100 —— 拉到 100 条，严格 48 小时窗口新条目 **0**（最新 date 2026-11-20T19:48:48Z）；与今日 X 交叉收录 EtherPadSniper `EGE-GH-XMUshAT`。
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines —— 10 条，与 CISA 交叉核对。
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json —— 目录 1790 条；48 小时新增 0，近 7 日 9 条（含 11-20 的 4 条本日重点）。
- AI/TLDR Atom：https://ai-tldr.dev/feed.xml —— 源内 50 条，本窗口新条目 **19**，其中 security **3**。
- Agent Use Cases RSS：https://agentusecases.ai/feed.xml —— 源内 120 条，本窗口新条目 **66**，文中精选约 20 条。
- 阮一峰 Atom：https://www.ruanyifeng.com/blog/atom.xml —— 第 420 期 https://www.ruanyifeng.com/blog/2026/11/weekly-issue-420.html （补上周六未出报）。
- 备援：Risky Business #860 https://risky.biz/RB860/ （HTTP 200）；tl;dr sec 订阅源 https://tldrsec.com/feed.xml （HTTP 200，最新期为 #355，作新闻备援未单独成节）。

本机保存路径：`/Users/kenny1337/Desktop/_05_项目/X安全情报晚报/2026-11-22-x-security-digest.md`
Box 路径：`/home/box/workspace/security-watch/reports/2026-11-22-x-security-digest.md`
