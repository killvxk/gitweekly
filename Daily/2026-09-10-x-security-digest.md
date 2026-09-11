# X 安全情报晚报 · 2026-09-10

> 搜集窗口：圣地亚哥时间 **2026-09-09 20:00 至 2026-09-10 ~20:22**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周四）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-10.json`（collected_at **2026-09-10T20:10:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-10.md`。CISA KEV catalogVersion **2026.09.10**／**1705** 条／dateReleased **2026-09-10T19:00:05.1949Z**（相对昨日 **+2**；新入 MikroTik RouterOS **CVE-2026-67277**、**CVE-2026-86060**，due **09-13**）。
> **期限今日 09-10：JFrog Artifactory CVE-2026-66384。期限明日 09-11：Adobe Magento CVE-2026-75650、N-able N-central CVE-2026-86218。** Sep2 五条联邦 BOD（Kestra／JFrog／Sangoma／SonicWall×2）自 **09-05** 起仍 **OVERDUE**。TrueConf **CVE-2026-72530**／MLflow **CVE-2026-64849** 仍逾期。due_near：Fortinet／Citrix／Cisco（**09-12**）；MikroTik 新两条（**09-13**）；PaperCut（**09-14**）；LiteLLM／Starlette（**09-16**）；Chromium **85046**（**09-18**）；微软两在野（**09-22**）；Chromium **87491**（**09-23**）。
> X：`/workspace/x-posts-2026-09-10.json`（合并 **20** 条唯一：A5／B0／C12／LWiS4；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.15h**（高噪声，**远不足 24h**）。Search B 约 **1.62h**（无保留工具帖）。Search C 约 **0.42h**。LWiS List 约 **21h**（保留 4）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · KEV +2 · MikroTrick】** CISA 将 MikroTik RouterOS **CVE-2026-67277**（due **09-13**，forensicTriage No）与 **CVE-2026-86060**（due **09-13**，forensicTriage **Yes**）入 KEV。CERT.pl／厂商称链式「**MikroTrick**」在 SSH 暴露设备上已在野；另有 **CVE-2026-67276**（厂商／CERT 提及，**未入本日 KEV 增量**）。立即升级并查 Flagged／未知用户。
  警报：https://www.cisa.gov/news-events/alerts/2026/09/10/cisa-adds-two-known-exploited-vulnerabilities-catalog
  厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
  CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/

- **【PaperCut · 维护版已发 + GreyNoise AI 战役】** 厂商页 **last_updated September 10, 2026**：NG/MF **26.0.5／25.0.13／24.1.10** 已发布（约 14:00 AEST），**取代 R1–R3 紧急补丁**；KEV due 仍 **09-14**。GreyNoise：疑似俄语 MCA 用数百 AI Agent（Codex harness＋DeepSeek）大规模利用 **CVE-2026-81578／82078**，至少 **440** 实例／**395** 组织／48 国。X 交叉：@GenAISpotlight。
  厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
  GreyNoise：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
  THN：https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html
  Register：https://www.theregister.com/security/2026/09/10/hundreds-of-ai-agents-helped-papercut-attacker-hit-395-orgs-and-some-went-off-script/5295650
  X：https://x.com/GenAISpotlight/status/2098185072700440906

- **【今日 due · JFrog 66384】** Artifactory 路径限制／Docker 缓存写越界；厂商公告与 NVD 见下。自托管尽快升至修复版本。
  https://docs.jfrog.com/releases/docs/jfrog-security-advisories
  https://nvd.nist.gov/vuln/detail/CVE-2026-66384

- **【ICS NEW】** ICSA-26-253-01 AVEVA PIM；ICSMA-26-253-01 NextGen Mirth Connect；ICSMA-26-253-02 Orthanc；ICSA-26-183-01 Update A（iDirect）。
  https://www.cisa.gov/news-events/ics-advisories/icsa-26-253-01
  https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-253-01
  https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-253-02

- **【X · PAN-OS CVE-2026-0310】** @securityLab_jp：PA-Series 未认证 root RCE／VM-Series DoS；厂商 09-09 公告，未见在野利用声明。
  厂商：https://security.paloaltonetworks.com/CVE-2026-0310
  X：https://x.com/securityLab_jp/status/2098185051351708146

- **【威胁报告】** Anthropic 2026-09 威胁情报报告（X／LWiS 多帖交叉）；Talos UAT-10147／SPECTRE（X 交叉，原文 08-20）。
  Anthropic：https://www.anthropic.com/threat-intelligence-report-september-2026
  Talos：https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/

- **【新闻 · Risky／tl;dr】** **NEW** SRB183；tl;dr **NEW #345**；Sliver／nuclei-templates 无升版。
  https://risky.biz/SRB183/
  https://tldrsec.com/blog/tldr-sec-345/

## CVE / POC / 漏洞

### 1. 【KEV NEW】MikroTik RouterOS 两条（2026-09-10）— MikroTrick

CISA 基于在野利用证据入目录。CERT.pl：两洞组合可在 **SSH 对公网开放** 时无认证接管；观察攻击至少自 **09-02**。厂商补丁：`7.25 beta 3`／`7.24.2`／`7.23.4`／`6.49.21`。升级后检查 Flagged、未知用户／脚本／隧道；**不转写利用链。**

| CVE | 产品 | due | 简述 |
|-----|------|-----|------|
| CVE-2026-67277 | MikroTik RouterOS | **09-13** | btest 缺认证 → 内核内存泄露／DoS；forensicTriage No |
| CVE-2026-86060 | MikroTik RouterOS | **09-13** | SSH 用户名参数分隔不当 → 提权；forensicTriage **Yes** |

相关（非本日 KEV 增量）：**CVE-2026-67276** SSH 公钥验证绕过（CERT／厂商）。

地址：
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/10/cisa-adds-two-known-exploited-vulnerabilities-catalog
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- Flagged 文档：https://manual.mikrotik.com/docs/system-information-and-utilities/device-mode#flagged-status
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67277 https://nvd.nist.gov/vuln/detail/CVE-2026-86060

IoC（CERT.pl 公开）：攻击源 IP `82.192.72.4`（自约 09-02，含创建特权用户 **ops**）、`103.102.31.18`（利用尝试）；日志特征含 `login failure for user -2 from <ip> via ssh`、`user <name> added by ssh:-2@<ip>`。完整狩猎以 CERT／厂商原文为准。

### 2. 【今日 due】JFrog Artifactory CVE-2026-66384

认证用户在特定远程仓库条件下可能写出 Docker 缓存预期路径之外。自托管按厂商公告升级（如 7.146.35／7.161.16 等分支修复版）；Cloud 侧厂商称已加固。

地址：
- 厂商：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-66384
- 发布说明：https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases

IoC：未见公开统一利用 IoC。

### 3. 【PaperCut】维护版发布 ＋ AI 编排大规模利用（交叉）

厂商 **09-10** 发布常规维护版，含公告 CVE 修复，**推荐全体客户迁离紧急补丁 R1–R3**。GreyNoise 跟踪 IP `45.142.193.132` 等：08-31 起用 AI Agent 规模化打 **CVE-2026-81578／82078**；教育行业美区占比高；部分路径达域管。防御：尽快升 **26.0.5／25.0.13／24.1.10**，按厂商 IoC／狩猎清单排查；**不转写利用步骤。**

地址：
- 厂商公告：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- GreyNoise：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
- THN：https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html
- The Register：https://www.theregister.com/security/2026/09/10/hundreds-of-ai-agents-helped-papercut-attacker-hit-395-orgs-and-some-went-off-script/5295650
- Blackpoint：https://blackpointcyber.com/blog/death-by-a-thousand-papercuts-ai-driven-exploitation-at-scale/
- X：https://x.com/GenAISpotlight/status/2098185072700440906
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-81578 https://nvd.nist.gov/vuln/detail/CVE-2026-82078

示例校验和（厂商页 MF 26.0.5 Windows Build 76602 SHA256）：`1927e72be3937f1271e590331c7d5e450716dd99982867a20fa73da156c26a40`

IoC（GreyNoise 公开节选）：IP `45.142.193.132`、`45.158.196.75`；账户名 `Administrator17`；路径如 `C:\Windows\Temp\pc-sys.hiv`、`C:\ProgramData\ligolo-agent.exe`、`C:\ProgramData\LegitSvc\legit-svc.exe`；样本 MD5 见 GreyNoise 表（`lsa_read.exe`／`save_hives.exe` 等）。完整表以 GreyNoise／GitHub 更新为准。

### 4. 【X】Palo Alto PAN-OS CVE-2026-0310

XML 处理缓冲区溢出：未认证网络可达管理／数据面时，**PA-Series** 可致 root 任意代码执行，**VM-Series** 主要为 DoS；Panorama 受影响。厂商 **09-09** 发布，声明**不知悉在野利用**；建议按版本表升级并将管理面限制到受信跳板。

地址：
- 厂商：https://security.paloaltonetworks.com/CVE-2026-0310
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-0310
- X：https://x.com/securityLab_jp/status/2098185051351708146
- 日文摘要：https://rocket-boys.co.jp/security-measures-lab/palo-alto-pan-os-cve-2026-0310-update/

IoC：未见公开利用 IoC（厂商称无已知恶意利用）。

### 5. 【ICS NEW】2026-09-10

| ID | 产品 | CVE | 说明 |
|----|------|-----|------|
| ICSA-26-253-01 | AVEVA Pipeline Integrity Monitor | CVE-2026-81821..81824 | 硬编码密钥／弱哈希／缺授权／XSS；升 2025 SP1 P2 并迁移工程 |
| ICSMA-26-253-01 | NextGen Mirth Connect | CVE-2026-82583／78224／82578 | SQL／XXE；升 **≥4.7.2** |
| ICSMA-26-253-02 | Orthanc DICOM | CVE-2026-87020 | 整数溢出堆写；升 **≥1.13.0** |
| ICSA-26-183-01 Update A | ST Engineering iDirect iQ-Series | （更新） | Update A |

地址：
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-253-01
- AVEVA PDF：https://www.aveva.com/content/dam/aveva/documents/support/cyber-security-updates/SecurityBulletin_AVEVA-2026-006.pdf
- https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-253-01
- https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-253-02
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-183-01
- Orthanc 下载：https://orthanc.uclouvain.be/downloads/index.html

IoC：CISA 称上述 ICS／ICSMA **暂无已知针对利用**。

### 6. 【KEV 逾期续】Sep2 BOD ＋ TrueConf／MLflow；明日 Magento／N-able

JFrog **82329**、Sangoma **9586**、SonicWall **83548／83549**、Kestra **49869** 自 09-05 逾期。TrueConf **72530**、MLflow **64849** 仍逾期。**明日 due：CVE-2026-75650（Magento）、CVE-2026-86218（N-able）。** 近期限 Fortinet／Citrix／Cisco（09-12）见昨日摘要。

地址：
- CISA 09-02：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- CISA 09-09：https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog
- SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016

IoC：未见本报新增统一列表（续用既有厂商／昨日汇总）。

## 工具与 GitHub 发布

### 1. 脉冲（无升版）

- Sliver **仍 v1.7.7**：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- nuclei-templates **仍 v10.4.8**：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

### 2. 【X Search B】

本日 Latest 窗口约 **1.62h**，滚动后**无保留**符合条件的 GitHub／C2／红队工具发布帖（`kept=0`）。

IoC：未见公开 IoC。

### 3. 【LWiS／防御配置】Defender ASR

@SwiftOnSecurity：Defender for Endpoint ASR「除非满足流行度／年龄／受信列表否则阻止可执行文件」在桌面与服务器落地经验。

地址：
- X：https://x.com/SwiftOnSecurity/status/2097865139588300854

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. 【X／公开】GreyNoise／PaperCut AI 编排战役（见 CVE 节）

主叙事与 IoC 见上「PaperCut」条；Search C 多帖交叉 Anthropic／PaperCut。

### 2. 【X】UAT-10147／SPECTRE（Talos）

@MalwareBibleJP 转发 Talos：中文关联 UAT-10147 部署跨平台 SPECTRE（Windows BYOVD＋Linux rootkit Specter），针对暴露 IIS／Linux。狩猎用官方 IoC 仓；**不转写利用细节。**

地址：
- 文章：https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/
- IoC 文件：https://github.com/Cisco-Talos/IOCs/blob/main/2026/08/UAT-10147%20deploys%20SPECTRE.txt
- X：https://x.com/MalwareBibleJP/status/2098185254620233974

IoC（Talos 文件节选，防御封锁用）：IP `27.124.2.46`／`27.124.2.48`／`27.124.2.52`／`139.180.197.150`；域名如 `js.jyzyps.com`、`vip8888vn.xyz`、`udvyiwvfs.cyou` 等；大量 SHA256 见 `/workspace/enrich-2026-09-10/talos-uat-10147-spectre-iocs.txt`。Linux 侧注意伪装模块 `acpi_pad.ko`、伪 systemd `hardware-monitor.service`、magic PID **31337**。

### 3. 【X／LWiS】Anthropic 2026-09 威胁情报报告

报告覆盖约 2025-12 至 2026-08 对 Claude 滥用：网络作战、影响行动、监视、诈骗、生物／常规武器相关探测、蒸馏等；已打断并强化防护。X／LWiS 多账号转述；Search A 另有 Anthropic 阻断国家级滥用叙事帖。

地址：
- 报告：https://www.anthropic.com/threat-intelligence-report-september-2026
- X：https://x.com/refpoliticalads/status/2098183522540220807 https://x.com/zhodonx/status/2098109777536807173 https://x.com/BreakinNewz01/status/2098185449890074663 https://x.com/fiossac78/status/2098185283736920493

IoC：未见本报可从帖面抄录的统一 C2／哈希表（以报告正文为准）。

### 4. 【LWiS】Teams／ClickFix 社交工程

@SwiftOnSecurity 引用 Black Hills 相关叙述：邮件轰炸＋假 Teams 客服，约 **2m32s** 从首条 Teams 到 ClickFix 执行；并转用免费 M365 试用租户。防御：限制外部 Teams、用户培训、禁非常规粘贴执行。

地址：
- X：https://x.com/SwiftOnSecurity/status/2097931648603926749
- 相关背景（SANS）：https://www.sans.org/blog/stay-ahead-ransomware-initial-access-via-evolving-social-engineering

IoC：未见本帖公开哈希／C2。

### 5. 【X Search C】勒索／泄露声称（需独立核验）

| 主题 | 说明 | 链接 |
|------|------|------|
| Veradigm／Gentlemen | 患者数据泄露披露（勒索声称后） | https://www.bleepingcomputer.com/news/security/veradigm-discloses-patient-data-breach-after-gentlemen-gang-claims-attack/ ；X：https://x.com/TechKimmi/status/2098188017970090354 |
| Qilin→Retelit（意电信） | ThreatCluster 叙事 | https://threatcluster.io/cluster/qilin-ransomware-targets-retelit-major-telecom-provider-in-i-611f2213 ；X：https://x.com/threatcluster/status/2098187802441617733 |
| Oxnull／Alibaba Cloud 文档声称 | 声称售卖内部文档（XMR $150） | https://x.com/CyberPulse56/status/2098183344408371525 |
| StarEmo／NoBox.AI 邮件文件声称 | 声称 14178 封 | https://x.com/CyberPulse56/status/2098182765812564469 ；https://www.nobox.ai/ |
| AI Agent 社工绕过密码叙事 | Undercode 文 | https://undercodetesting.com/ransomware-group-bypassed-passwords-entirely-by-social-engineering-ai-coding-agents-into-believing-attacks-were-security-drills-video/ ；X：https://x.com/UndercodeUpdate/status/2098182755766939904 |

IoC：上述多为公开声称／转载，**未见本报可核验的统一样本哈希**；勿默认真实性。

### 6. 【LWiS】FBI Cyber Strategy

@sec_hub93028 转发 FBI 网络战略路线图（破坏对手、支援受害者、伙伴关系、网空人力）。

地址：
- X：https://x.com/sec_hub93028/status/2098166741834899766

IoC：未见公开 IoC。

### 7. 【新闻备援】Risky／tl;dr

- **NEW** SRB183：https://risky.biz/SRB183/（美国驾照大规模泄露与国安叙事）
- 仍可见 RBNEWS611／RB852：https://risky.biz/RBNEWS611/ https://risky.biz/RB852/
- **NEW** tl;dr **#345**：https://tldrsec.com/blog/tldr-sec-345/（Bug rumor→exploit、VCS DFIR、Agentic worms）

## 地址／IoC 汇总

- **KEV 新入（09-10）**：MikroTik **CVE-2026-67277／86060**（due **09-13**）；相关 **67276** 见 CERT／厂商。
- **MikroTrick（CERT.pl）**：IP `82.192.72.4`、`103.102.31.18`；特权用户名 **ops**；日志 `user -2`／`ssh:-2@` 特征；升级后查 Flagged。
- **PaperCut／GreyNoise AI 战役**：IP `45.142.193.132`、`45.158.196.75`；`Administrator17`；`pc-*.hiv`／`ligolo-agent.exe`／`LegitSvc\legit-svc.exe`；维护版 SHA256 示例见上；due **09-14**。
- **SPECTRE／UAT-10147（Talos IoC 文件）**：`27.124.2.46`／`.48`／`.52`、`139.180.197.150`；域名与 SHA256 见官方 txt；`acpi_pad.ko`／`hardware-monitor.service`／PID **31337**。
- **PAN-OS CVE-2026-0310**：未见公开利用 IoC；按厂商版本表补丁。
- **KEV 逾期**：Kestra 49869／JFrog 82329／Sangoma 9586／SonicWall 83548+83549；TrueConf 72530／MLflow 64849；**今日** JFrog **66384** due。
- **明日 due**：Magento **75650**；N-able **86218**。
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

- X Latest A（CVE/POC）：https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day%20OR%20%220-day%22&src=typed_query&f=live
- X Latest B（GitHub 工具／C2）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20%22red-team%22%20OR%20nuclei%20OR%20sliver%20OR%20mythic%20OR%20cobalt)%20OR%20%22command%20and%20control%22&src=typed_query&f=live
- X Latest C（malware／threat）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20OR%20ransomware%20OR%20%22APT%20group%22&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky SRB183：https://risky.biz/SRB183/
- Risky RBNEWS611：https://risky.biz/RBNEWS611/
- Risky RB852：https://risky.biz/RB852/
- tl;dr sec：https://tldrsec.com/
- tl;dr #345：https://tldrsec.com/blog/tldr-sec-345/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 09-10 两条警报：https://www.cisa.gov/news-events/alerts/2026/09/10/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 09-09 四条警报：https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog
- CISA 09-02 七条警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- MikroTik 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl MikroTik：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- GreyNoise PaperCut：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
- PAN-OS CVE-2026-0310：https://security.paloaltonetworks.com/CVE-2026-0310
- Anthropic TI Sep2026：https://www.anthropic.com/threat-intelligence-report-september-2026
- Talos SPECTRE：https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/
- ICSA-26-253-01：https://www.cisa.gov/news-events/ics-advisories/icsa-26-253-01
- ICSMA-26-253-01：https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-253-01
- ICSMA-26-253-02：https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-253-02
