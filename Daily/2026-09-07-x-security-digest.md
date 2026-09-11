# X 安全情报晚报 · 2026-09-07

> 搜集窗口：圣地亚哥时间 **2026-09-06 20:00 至 2026-09-07 ~21:15**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周一）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-07.json`（collected_at **2026-09-07T20:40:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-07.md`。CISA KEV catalogVersion **2026.09.04**／**1695** 条／dateReleased **2026-09-04T16:47:03.5197Z**（相对昨日 **+0**，无 09-05／09-06／09-07 新入 KEV）。
> **期限今日 09-07：无。期限明日 09-08：无。** Sep2 五条联邦 BOD（Kestra **CVE-2026-49869**、JFrog **CVE-2026-82329**、Sangoma **CVE-2026-9586**、SonicWall **CVE-2026-83548/83549**）自 **09-05** 起仍 **OVERDUE**。TrueConf **CVE-2026-72530**（due 09-03）／MLflow **CVE-2026-64849**（due 09-02）仍逾期。due_near：legacy 条目（09-09）；JFrog 路径 **CVE-2026-66384**（09-10）；PaperCut **81578/82078**（09-14）；LiteLLM／Starlette（09-16）；Chromium **85046**（09-18）。
> X：`/workspace/x-posts-2026-09-07.json`（合并 **40** 条：A4／B10／C18／LWiS8；其中 **新 32**／已见 8；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.17h**（高流量，**远不足 24h**）。Search B 约 **65h**（多数窗外／昨日已见工具帖，标【已见／续】）。Search C 约 **1.22h**。LWiS List 约 **49.3h**（保留 8 条安全相关）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · KEV 逾期续】** Sep2 五条 BOD 仍 **OVERDUE**：Kestra OSS **CVE-2026-49869**、JFrog Artifactory **CVE-2026-82329**、Sangoma Switchvox **CVE-2026-9586**、SonicWall SMA1000 **CVE-2026-83548/83549**。TrueConf **72530**／MLflow **64849** 亦逾期。目录仍停在 2026.09.04／1695（+0）。未打补丁资产按厂商说明与 KEV 要求处理。
  警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
  SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

- **【NEW · PaperCut Sep7 状态 bump】** 厂商页 **last_updated: September 7, 2026**（原 Sep5）：*No new information to report; work continues towards the official release.* Emergency Patch **R3** 仍最新；KEV **CVE-2026-81578/82078** due **2026-09-14**。公网未打补丁应假定失陷。
  厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/

- **【X · Cisco Secure Email】** S/MIME 相关 **CVE-2026-20354／CVE-2026-20355**（卡片亦提及 **CVE-2026-20281**／IP 电话 DoS 语境）。可能致加密邮件明文被恢复（需路径上 MitM）；按 Cisco 公告与缓解收敛。
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-smime-disc-dzw4rEdY
  文章：https://rocket-boys.co.jp/security-measures-lab/cisco-secure-email-smime-cve-incident/
  X：https://x.com/securityLab_jp/status/2097105461187420331

- **【X · PREY-0058】** 针对 Microsoft 365 的 vishing＋AitM 会话令牌窃取／住宅代理回放；影响 SharePoint／OneDrive／Exchange／Box；无端点恶意软件部署叙述。防御：条件访问、抗钓鱼 MFA、限制 SharePoint 范围、检测异常令牌回放。
  文章：https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html
  X：https://x.com/hCharizard_/status/2097097497659498660

- **【LWiS · Florida DMV／ShinyHunters 声称】** vxunderground 转述 ShinyHunters 声称攻破 Florida DMV 并泄露驾照记录；首发归功 @DarkWebInformer。与 Krebs **FBI 调查出售 1.53 亿+驾照数据服务**交叉（**未核实**）。
  X：https://x.com/vxunderground/status/2097103006000902446 https://x.com/vxunderground/status/2097104139335393327
  Krebs：https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/

- **【新闻 · Risky Biz NEW】** **RBNEWS610** 法国公证 BEC 窃取约 €3500 万；**BTN182** AI 能否防御关键基础设施。tl;dr sec 仍 **#343**。
  https://risky.biz/RBNEWS610/ https://risky.biz/BTN182/ https://tldrsec.com/blog/tldr-sec-343/

- **【工具】** Sliver **仍 v1.7.7**；nuclei-templates **仍 v10.4.8**。NEW：cyber-resume-reviewer-skill；Agent Provocateur 讨论。Search B 窗外续见 KHAØS／Amass／Subfinder／VulnClaw／M365Pwned／SpecterOps skills（【已见／续】）。
  仓库：https://github.com/BishopFox/sliver/releases/tag/v1.7.7 https://github.com/mubix/cyber-resume-reviewer-skill https://github.com/28Zaaky/khaos-c2

- **【Chrome】** **NEW** ChromeOS／Flex Stable 频道帖（帖体 **无 CVE-2026-***）；KEV Chromium **CVE-2026-85046** 仍 due **09-18**（Stable 152.0.7977.82+）。
  ChromeOS：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-chromeos.html
  Stable：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html

## CVE / POC / 漏洞

### 1. 【KEV 逾期】Sep2 五条 BOD ＋ TrueConf／MLflow

JFrog Artifactory **CVE-2026-82329**、Sangoma Switchvox **CVE-2026-9586**、SonicWall SMA1000 **CVE-2026-83548/83549**、Kestra OSS **CVE-2026-49869** 自 09-05 起逾期。TrueConf Server **CVE-2026-72530**（due 09-03）、MLflow **CVE-2026-64849**（due 09-02）仍逾期。近期限：JFrog 路径 **CVE-2026-66384**（09-10）；LiteLLM **CVE-2026-59822**／Starlette **CVE-2026-48710**（09-16）。按厂商补丁／缓解与联邦 BOD 要求收敛暴露面。**不转写利用细节。**

地址：
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-82329 https://nvd.nist.gov/vuln/detail/CVE-2026-9586 https://nvd.nist.gov/vuln/detail/CVE-2026-83548 https://nvd.nist.gov/vuln/detail/CVE-2026-83549 https://nvd.nist.gov/vuln/detail/CVE-2026-49869 https://nvd.nist.gov/vuln/detail/CVE-2026-72530 https://nvd.nist.gov/vuln/detail/CVE-2026-64849 https://nvd.nist.gov/vuln/detail/CVE-2026-59822 https://nvd.nist.gov/vuln/detail/CVE-2026-48710 https://nvd.nist.gov/vuln/detail/CVE-2026-66384
- SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
- nuclei（JFrog）：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-82329.yaml
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见本条新增统一 IoC；逐厂商公告。

### 2. 【PaperCut】CVE-2026-81578／82078（KEV due 09-14）— Sep7 状态 bump

厂商页 **last_updated September 7, 2026, 5:18pm (AEST)**：无新情报，正式版仍在推进。Emergency Patch **R3** 仍为当前紧急补丁。公网暴露未打补丁应假定失陷。

地址：
- 厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-81578 https://nvd.nist.gov/vuln/detail/CVE-2026-82078

IoC：续见厂商页狩猎路径／示例哈希（见下方 IoC 汇总）；本日无新抄录。

### 3. 【X】Cisco Secure Email S/MIME CVE-2026-20354／20355（＋卡片 CVE-2026-20281）

日文转述＋Cisco 公告：Secure Email S/MIME 解密完整性校验不足，路径上攻击者可能恢复加密邮件明文；影响 AsyncOS **16.5.0 及更早且启用 S/MIME** 的叙述。卡片另提及 **CVE-2026-20281** 与 IP 电话 DoS 语境。按 Cisco 公告升级／缓解；**不转写利用链。**

地址：
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-smime-disc-dzw4rEdY
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-20354 https://nvd.nist.gov/vuln/detail/CVE-2026-20355
- 文章：https://rocket-boys.co.jp/security-measures-lab/cisco-secure-email-smime-cve-incident/
- X：https://x.com/securityLab_jp/status/2097105461187420331

IoC：未见公开 IoC。

### 4. 【X】BYOTC／BYOVD 分析（Bring Your Own Trusted Caller）

威胁报告摘要指向 Windows 脆弱驱动／TOCTOU 相关分析（Part 1）；提及与 Defender／Malwarebytes／System Informer 等交互语境。**仅记防御向参考；不转写利用／驱动加载步骤。**

地址：
- 文章：https://xusheng.dev/posts/byotc/main/
- X：https://x.com/rst_cloud/status/2097107642820776199

IoC：未见公开 IoC。

### 5. 【LWiS】MariaDB 授权逻辑问题（HackerOne #3876430）

披露称授权逻辑缺陷可允许未授权用户更改其他用户（含 root）密码。按厂商／报告路径打补丁与审计账户变更；**不转写复现步骤。**

地址：
- HackerOne：https://hackerone.com/reports/3876430
- X：https://x.com/kevin_mizu/status/2097055819447550388

IoC：未见公开 IoC。

### 6. 【Chrome／ChromeOS】Stable 续 ＋ KEV CVE-2026-85046（due 09-18）

KEV **CVE-2026-85046**（dateAdded 2026-09-04，due **2026-09-18**）仍对应 Desktop Stable **152.0.7977.82+**（Google 确认在野）。今日 **NEW** ChromeOS／Flex Stable 频道更新帖，帖体 **未见 CVE-2026-*** 枚举。生产优先按 KEV／Desktop Stable 安全通道收敛。

地址：
- ChromeOS Stable：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-chromeos.html
- Desktop Stable 安全：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- Early Stable（已知）：https://chromereleases.googleblog.com/2026/09/early-stable-update-for-desktop.html
- CISA 09-04 警报：https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog
- NVD／KEV：https://nvd.nist.gov/vuln/detail/CVE-2026-85046 https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85046

IoC：未见公开攻击者 C2／样本哈希；行动以浏览器升级为主。

### 7. 【低价值／未核实】广告软件过热声称

西班牙语帖称广告点击触发「过热／后台开页」类 adware／exploit 叙事；**证据不足，仅简记，不展开。**

地址：
- X：https://x.com/AstarothRol/status/2097106824952516673

IoC：未见公开 IoC。

### 8. 【周边】防御向 code review／补丁叙述

日文帖强调认证注入／密钥泄露的防御报告与补丁导向（明确拒绝攻击用 PoC）。作文化交叉，无 CVE。

地址：
- X：https://x.com/LankC11/status/2097105414949052456

IoC：不适用。

## 工具与 GitHub 发布

### 1. Sliver／nuclei-templates（公开备援）

Sliver **仍 v1.7.7**（2026-09-03）；nuclei-templates **仍 v10.4.8**（2026-08-24）。本窗未见二者新 release 帖。

地址：
- https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

IoC：不适用。

### 2. 【NEW · LWiS】cyber-resume-reviewer-skill

@mubix 公开网络安全简历审阅 AI skill；欢迎反馈／PR。

地址：
- 仓库：https://github.com/mubix/cyber-resume-reviewer-skill
- X：https://x.com/mubix/status/2097087670681821272

IoC：未见公开 IoC。

### 3. 【NEW · LWiS】Agent Provocateur 讨论

@haroonmeer 宣布用于检测偏离预期行为的自主 agent／讨论其安全弱点的工具「Agent Provocateur」（帖内未见仓库 URL）。

地址：
- X：https://x.com/haroonmeer/status/2096942697206403420

IoC：未见公开 IoC。

### 4. 【LWiS】LiveOverflow — agent／沙箱设计讨论

讨论 agent 利用事件是否由受限环境驱动及沙箱设计选择；防御向交叉。

地址：
- X：https://x.com/LiveOverflow/status/2097080326577078336

IoC：不适用。

### 5. 【LWiS】Intune APv2／OpenSecTraining（周边）

MSIntune APv2 新选项（仅新配置文件）；Windows Kernel Internals 2 培训推广。

地址：
- X：https://x.com/xenappblog/status/2096978431606923644
- 培训：https://ost2.fyi/Arch2821
- X：https://x.com/OpenSecTraining/status/2096912027822248290

IoC：不适用。

### 6. 【已见／续 · Search B】KHAØS／Amass／Subfinder／prompt-injection／Audn／VulnClaw／M365Pwned／SpecterOps skills

Search B 覆盖约 **65h**，以下多条已在 09-06 digest／seen_ids，作工具交叉续列：

| 标记 | 工具 | 仓库 | X |
|------|------|------|---|
| 【已见／续】 | KHAØS C2 | https://github.com/28Zaaky/khaos-c2 | https://x.com/28zaaky/status/2096626008115822683 |
| 【已见／续】 | OWASP Amass | https://github.com/owasp-amass/amass | https://x.com/EsGeeks/status/2096671684547764626 |
| 【已见／续】 | Subfinder | https://github.com/projectdiscovery/subfinder | https://x.com/NitinGavhane_/status/2096533136826081591 |
| 【已见／续】 | prompt-injection-example | https://github.com/Antolius/prompt-injection-example | https://x.com/di_zhang_fdu/status/2096645921845239848 |
| 【已见／续】 | Audn Ethical Hacker Agent | https://github.com/apps/audn-ethical-hacker-agent/ | https://x.com/audn_ai/status/2096594762249785549 |
| 【已见／续】 | VulnClaw | https://github.com/Netw0rkNoob/VulnClaw | https://x.com/EsGeeks/status/2096076626266083410 |
| 【已见／续】 | M365Pwned | https://github.com/OtterHacker/M365Pwned | https://x.com/DirectoryRanger/status/2096327122495180962 |
| 【已见／续】 | SpecterOps skills／Outflank | https://github.com/SpecterOps/skills https://www.outflank.nl/blog/2026/09/02/red-team-ai-skills/ | https://x.com/ntlmrelay/status/2096285194546208904 |

窗外新 id（非 24h 主窗，简记）：LLM guardrails 汇总 https://x.com/0xal0ke/status/2096676281417072750（https://github.com/guardrails-ai/guardrails）；AI 红队学习资源汇总 https://x.com/CyberA94/status/2096254022441132358。

IoC：未见公开 IoC。**不转写利用步骤。**

## APT / Malware 分析

### 1. 【X】PREY-0058 — M365 会话令牌窃取（vishing＋AitM）

威胁集群 PREY-0058（Arctic Wolf 追踪）结合假 IT／help desk **vishing** 与 **AitM** 登录页窃取会话令牌，经住宅代理回放访问 SharePoint／OneDrive／Exchange／Box 等并勒索。叙述称**不部署端点恶意软件**。防御：条件访问、抗钓鱼 MFA（FIDO2／通行密钥）、限制 SaaS 数据范围、检测异常住宅代理令牌回放／批量 SharePoint 访问。**不转写诱饵域名完整列表或利用步骤。**

地址：
- 文章：https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html
- X：https://x.com/hCharizard_/status/2097097497659498660

IoC：未见本报可独立核验的统一哈希；以厂商／Arctic Wolf 原文为准。

### 2. 【LWiS】ShinyHunters／Florida DMV 声称 ＋ Krebs FBI 驾照数据调查

vxunderground 转述 ShinyHunters 勒索团伙声称攻破 Florida DMV，并以驾照记录作证明；首发归功 @DarkWebInformer。与 Krebs 报道 FBI 调查出售约 **1.53 亿+** 驾照数据的服务交叉。**均为未核实／调查中情报，不作确认。**

地址：
- X：https://x.com/vxunderground/status/2097103006000902446 https://x.com/vxunderground/status/2097104139335393327
- Krebs：https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/

IoC：未见公开 IoC（不转载证件图像或个人数据）。

### 3. 【X】勒索／数据泄露声称（均未独立核实）

窗内多起暗网／勒索站点声称，仅作威胁情报交叉，**标签：未核实**：

| 声称 | X 原帖 |
|------|--------|
| 巴西 Arcos 市政府数据集 ~484.7 MB | https://x.com/DarkWebInformer/status/2097102354361274594 |
| Noon（noon.com）~200 万条 DB | https://x.com/DailyDarkWeb/status/2097093000598020133 |
| Investigate Europe ~20 TB | https://x.com/DailyDarkWeb/status/2097092140694159446 |
| Chaos → Evergen ~700 GB | https://x.com/DailyDarkWeb/status/2097088185050484935 |
| LOCKBIT 5.0 → VSB Attorneys（vbsattorneys.co.za） | https://x.com/FalconFeedsio/status/2097088117358637232 |
| VFirst ~12 TB | https://x.com/DailyDarkWeb/status/2097086972007223399 |
| SmartSearch（smartsearchinc.com）~1805 万条 | https://x.com/DailyDarkWeb/status/2097084884174975227 |
| Dark Project → MEI Architects（SG） | https://x.com/ThreatAtlas/status/2097090727339778334 |
| thegentlemen → El Carriel（CO） | https://x.com/ThreatAtlas/status/2097085236446118130 |
| thegentlemen → AbacoViaggi（IT） | https://x.com/ThreatAtlas/status/2097085051171201389 |
| thegentlemen → Ritz Safety（US） | https://x.com/ThreatAtlas/status/2097084743896465632 |
| thegentlemen → Biotipo Jeans（BR） | https://x.com/ThreatAtlas/status/2097084568754925986 |
| thegentlemen → Metro（DE） | https://x.com/ThreatAtlas/status/2097084419530006678 |
| thegentlemen → Domis（DK） | https://x.com/ThreatAtlas/status/2097084335996215333 |
| thegentlemen → Zanini（BR） | https://x.com/ThreatAtlas/status/2097084139744751865 |
| thegentlemen → Soni Dwarkadas Virchand（IN） | https://x.com/ThreatAtlas/status/2097084018709713253 |
| thegentlemen → S A Chile（CL） | https://x.com/ThreatAtlas/status/2097083869396660550 |

关联站点（帖内展开，**非确认 IoC**）：https://www.noon.com/ https://vbsattorneys.co.za/ https://smartsearchinc.com/

IoC：未见本报可核验统一样本哈希；不转载广告包或凭证内容。

### 4. 【新闻备援】Risky Biz RBNEWS610／BTN182

**NEW** RBNEWS610：针对法国公证的 BEC 活动，声称损失约 €3500 万。**NEW** BTN182：Between Two Nerds — AI 能否防御关键基础设施。已知 RBNEWS609／RBFEATURES38／SRB182 等仍在列。

地址：
- https://risky.biz/RBNEWS610/
- https://risky.biz/BTN182/
- https://risky.biz/RBNEWS609/
- tl;dr sec #343：https://tldrsec.com/blog/tldr-sec-343/

IoC：以原文为准；本报未见统一新增哈希。

## 地址／IoC 汇总

- **KEV 逾期（自 09-05）**：Kestra 49869／JFrog 82329／Sangoma 9586／SonicWall 83548+83549 — 以厂商补丁与 KEV 要求为准；未见本报新增统一哈希。TrueConf 72530／MLflow 64849 亦逾期。
- **Chromium CVE-2026-85046**：升级至 Stable **152.0.7977.82+**；关注 ChromeOS Stable 频道帖（无 CVE 枚举）；Google 确认在野利用。
- **PaperCut（厂商续抄，due 09-14；Sep7 仍无新情报）**：
  - 狩猎：Application Server 上可疑后利用；`C:\ProgramData\ace.exe`；SimpleHelp 路径 `C:\ProgramData\JWrapper-Remote Access\JWAppsSharedConfig\restricted\SimpleService.exe`（服务名 “Remote Access Service”）；AnyDesk 落盘 `C:\ProgramData\AnyDesk.exe`。
  - 投放 URL（去活化）：`hxxps://sendit[.]sh/Gg7Rp/ace[.]exe`；`hxxps://download[.]anydesk[.]com/AnyDesk.exe`（后者为合法下载域被滥用场景，需结合上下文）。
  - Emergency Patch R3 示例 SHA256（Windows v26 Build 76531）：`9375a9c3cf84140a1d8e21b72d3d2c57d85d4de09ea9ae1dc021b64732427da7`（完整多版本校验和见厂商页）。
- **Cisco／MariaDB／BYOTC／PREY-0058**：未见本报新增可核验统一样本哈希；以厂商／文章原文为准。
- **关联域名（帖内，非确认 IoC）**：noon.com、vbsattorneys.co.za、smartsearchinc.com。
- **勒索／泄露声称**：未见统一公开样本哈希；表内均为未核实声称。
- **其余条目**：写「未见公开 IoC」者以上各节为准。

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

## 来源搜索 URL

- X Latest A（CVE/POC）：https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- X Latest B（GitHub 工具／C2）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt)&src=typed_query&f=live
- X Latest B 备援：https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20%22red-team%22%20OR%20nuclei%20OR%20implant%20OR%20c2)&src=typed_query&f=live
- X Latest C（malware／threat）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS610：https://risky.biz/RBNEWS610/
- Risky BTN182：https://risky.biz/BTN182/
- tl;dr sec：https://tldrsec.com/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 09-02 七条警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- CISA 09-04 Chromium 警报：https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog
- ChromeOS Stable：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-chromeos.html
- Chrome Stable 安全：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- Chrome Early Stable：https://chromereleases.googleblog.com/2026/09/early-stable-update-for-desktop.html
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- SonicWall SNWLID-2026-0016：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
- Cisco ESA S/MIME：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-smime-disc-dzw4rEdY
- Krebs FBI DL：https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/
- The Hacker News PREY-0058：https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html
