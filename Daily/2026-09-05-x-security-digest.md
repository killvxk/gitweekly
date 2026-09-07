# X 安全情报晚报 · 2026-09-05

> 搜集窗口：圣地亚哥时间 **2026-09-04 20:00 至 2026-09-05 ~20:40**（America/Santiago / UTC-4）。**本报为官方 20:00 cron 晚报（周六）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-05.json`（collected_at **2026-09-05T20:12:57-04:00**）＋ `/workspace/tools-news-pulse-2026-09-05.md`。CISA KEV catalogVersion **2026.09.04**／**1695** 条／dateReleased **2026-09-04T16:47:03.5197Z**（相对昨日 **+0**，无 09-05 新入 KEV）。
> **期限今日 09-05（5 条紧急，BOD 到期日）**：Kestra **CVE-2026-49869**、JFrog **CVE-2026-82329**、Sangoma **CVE-2026-9586**、SonicWall **CVE-2026-83548/83549**（SNWLID-2026-0016）。**期限明日 09-06：无。** PaperCut due **2026-09-14**；LiteLLM／Starlette due **09-16**；Chromium 85046 due **09-18**；JFrog 路径 **CVE-2026-66384** due **09-10**。TrueConf **CVE-2026-72530**／MLflow **CVE-2026-64849** 已过 due。
> X：`/workspace/x-posts-2026-09-05.json`（合并 **54** 条：A 11／B 4／C 21／LWiS 18；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.65h**（高流量，**远不足 24h**）。Search B 约 **19h**。Search C 约 **5h**。LWiS List 约 **23h**。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · KEV 到期日】五条联邦 BOD 期限今日 09-05**：Kestra OSS **CVE-2026-49869**、JFrog Artifactory **CVE-2026-82329**、Sangoma Switchvox **CVE-2026-9586**、SonicWall SMA1000 **CVE-2026-83548/83549**。目录本身仍停在 2026.09.04／1695（+0）。未打补丁资产按厂商说明与 KEV 要求处理。
  警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
  SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

- **【X 交叉 · Cisco Nexus 9000】CVE-2026-20212**（未入本报 KEV）：Silicon One 场景未认证根代码执行讨论；缓解要点含封锁 TCP **43210/43211** 并升级 NX-OS。**不转写利用链。**
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-20212
  X：https://x.com/i/status/2096388158015656130

- **【X 交叉 · JetBrains Cadence／TeamCity】CVE-2026-63077**（已在 KEV，dateAdded 2026-08-05，due 已过 08-08）：第三方报道称 Cadence 环境经未打补丁 TeamCity 遭入侵，可能暴露 AWS IAM／备份／源码／密钥；厂商侧呼吁轮换凭证。核对 JetBrains 公告后轮换连接系统凭据。
  厂商：https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/
  文章：https://www.hendryadrian.com/attackers-breached-jetbrains-cadence-via-unpatched-teamcity-extracting-aws-credentials/
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-63077
  X：https://x.com/i/status/2096388008798830718

- **【X 交叉 · VMware／Ceph】** VMware Workstation／Fusion **CVE-2026-59346**（Broadcom VMSA-2026-0007，未入 KEV）；Ceph **CVE-2026-50152** 配置键机密可读（CVSS 8.2，未入 KEV）。
  Broadcom：https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38288
  Ceph：https://docs.ceph.com/en/latest/security/CVE-2026-50152/
  X：https://x.com/i/status/2096384233967083689 https://x.com/i/status/2096388008480301213

- **【X · Magento StyleSmuggler】** 称未认证 RCE（尚无 CVE），影响 Magento Open Source／Adobe Commerce 2.4.x；狩猎侧重 `~/.local/share/.gvfsd/gvfsd-user` 与 crontab 植入。**不转写利用步骤。**
  X：https://x.com/i/status/2096388541710250401

- **【PaperCut 续】** NG／MF **CVE-2026-81578/82078** 仍 KEV（due 09-14）。**R3** 仍为紧急补丁；09-05 10:30 AEST 仅状态更新（无新情报，正式版仍在推进）。公网未打补丁应假定失陷。
  厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/

- **【Chromium 续】** **CVE-2026-85046** 仍为最新入 KEV（due 09-18）；Stable **152.0.7977.82+**。
  厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html

- **【工具】** Sliver **仍 v1.7.7**；nuclei-templates **仍 v10.4.8**。X 窗：M365Pwned、SpecterOps/skills、VulnClaw、Veneficus；LWiS：0xM0nCrush BYOVD、edrEvasionWorkshop（边界外续传）。
  仓库：https://github.com/BishopFox/sliver/releases/tag/v1.7.7 https://github.com/OtterHacker/M365Pwned https://github.com/SpecterOps/skills https://github.com/Netw0rkNoob/VulnClaw https://github.com/abraxas/veneficus https://github.com/DeathShotXD/0xM0nCrush

- **【APT／勒索／声称】** Rhysida 柏林政府数据声称；Dire Wolf→Mission Pet Health；Ledger／Trezor 工具广告；DragonForce Windows locker 分析；多起数据泄露／暗网出售声称（未独立核实）。
  https://darkatlas.io/blog/dragonforce-ransomware-analysis-windows-locker
  https://x.com/XQOPTRX/status/2096387906864865440
  https://x.com/FalconFeedsio/status/2096365371947397448

- **【新闻备援】** Risky Biz **无新 ID**（仍 RBNEWS609／RBFEATURES38／SRB182／RB851／RBNEWS608／BTN181）；tl;dr sec 仍 **#343**。ICS **无新发**（仍 ICSA-26-246-*）。
  https://risky.biz/RBNEWS609/ https://tldrsec.com/blog/tldr-sec-343/

## CVE / POC / 漏洞

### 1. 【KEV 到期日】五条紧急（due 2026-09-05）

JFrog Artifactory **CVE-2026-82329**、Sangoma Switchvox **CVE-2026-9586**、SonicWall SMA1000 **CVE-2026-83548/83549**、Kestra OSS **CVE-2026-49869** 今日到期。LiteLLM **CVE-2026-59822**／Starlette **CVE-2026-48710** due 09-16。按厂商补丁／缓解与联邦 BOD 要求收敛暴露面。**不转写利用细节。**

地址：
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-82329 https://nvd.nist.gov/vuln/detail/CVE-2026-9586 https://nvd.nist.gov/vuln/detail/CVE-2026-83548 https://nvd.nist.gov/vuln/detail/CVE-2026-83549 https://nvd.nist.gov/vuln/detail/CVE-2026-49869 https://nvd.nist.gov/vuln/detail/CVE-2026-59822 https://nvd.nist.gov/vuln/detail/CVE-2026-48710
- SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
- nuclei（JFrog）：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-82329.yaml
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见本条新增统一 IoC；逐厂商公告。

### 2. 【X 交叉 · 未入 KEV】Cisco Nexus 9000 Silicon One CVE-2026-20212

X 讨论未认证根代码执行（CVSS 叙述 9.8）；Cisco 公告编号 cisco-sa-n9k-s1-rce-EH8dEtr。缓解：限制／封锁 TCP **43210/43211**，升级 NX-OS。**本报 KEV 未见此 CVE。**

地址：
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-20212
- X：https://x.com/i/status/2096388158015656130

IoC：狩猎侧重异常监听／访问 TCP 43210/43211；未见公开攻击者 C2 域名／样本哈希。

### 3. 【X 交叉 · 已在 KEV】JetBrains TeamCity CVE-2026-63077 → Cadence 事件报道

KEV 自 **2026-08-05**（due **2026-08-08**）。今日 X／第三方称 Cadence 经未打补丁 TeamCity 遭入侵，可能触及 AWS IAM、S3、备份与源码；JetBrains 侧有 TeamCity 公告与凭证轮换呼吁。升级 On-Premises 至厂商修复版本并轮换相关密钥。

地址：
- 厂商：https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/
- 议题汇总：https://www.jetbrains.com/privacy-security/issues-fixed/
- 文章：https://www.hendryadrian.com/attackers-breached-jetbrains-cadence-via-unpatched-teamcity-extracting-aws-credentials/
- NVD／KEV：https://nvd.nist.gov/vuln/detail/CVE-2026-63077 https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-63077
- X：https://x.com/i/status/2096388008798830718 https://x.com/i/status/2096387193346412965

IoC：未见本报统一公开样本哈希；行动以轮换 AWS／插件／连接系统凭据与审计可疑会话为主。

### 4. 【X 交叉 · 未入 KEV】VMware Workstation／Fusion CVE-2026-59346

Broadcom **VMSA-2026-0007**（2026-09-03）：VMXNET3 整数溢出可致宿主机代码执行；修复叙述含 **26H1u1**。升级 Workstation／Fusion；**不转写 PoC。**

地址：
- 厂商：https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38288
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-59346
- X：https://x.com/i/status/2096384233967083689 https://x.com/i/status/2096387188329967699

IoC：未见公开攻击者 IoC。

### 5. 【X 交叉 · 未入 KEV】Ceph CVE-2026-50152

Monitor 配置键存储机密可读（CVSS 8.2）。官方文档／Red Hat／GHSA 通道；修复叙述含 Tentacle **20.2.4**／Squid **19.2.6**。

地址：
- 厂商：https://docs.ceph.com/en/latest/security/CVE-2026-50152/
- Red Hat：https://access.redhat.com/security/cve/cve-2026-50152
- 文章：https://www.cybernote.click/2026/08/29/ceph-cve-2026-50152-monitor-config-key-secrets/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-50152
- X：https://x.com/i/status/2096388008480301213

IoC：未见公开攻击者 C2／样本哈希。

### 6. 【X】Magento／Adobe Commerce StyleSmuggler（无 CVE）

称经「Payment Transaction Failed Reminder」路径触发未认证 RCE；称 2.4.x（含 2.4.9）受影响，自 2026-09-04 有利用观察，至采集时未见官方补丁叙述。**防御向仅记狩猎路径；不转写利用步骤。**

地址：
- X：https://x.com/i/status/2096388541710250401

IoC（帖内狩猎线索，去活化／路径原样）：
- 路径：`~/.local/share/.gvfsd/gvfsd-user`
- crontab：`*/5 * * * *` 指向上述二进制；`/var/spool/cron/crontabs/`
- 进程伪装叙述：`[kworker/u:8:0]`

### 7. 【KEV 续】PaperCut NG／MF CVE-2026-81578 ＋ CVE-2026-82078（due 2026-09-14）

Emergency Patch Release 3 仍为累积紧急补丁。09-05 厂商状态更新（10:30am AEST）：无新情报，正式版仍在推进。公网 Application Server 未打补丁应假定失陷并对照厂商 IoC 狩猎。

地址：
- 厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- KEV／NVD：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-81578 https://nvd.nist.gov/vuln/detail/CVE-2026-81578 https://nvd.nist.gov/vuln/detail/CVE-2026-82078

IoC：见「地址／IoC 汇总」。

### 8. 【KEV 续】Google Chromium V8 CVE-2026-85046（due 2026-09-18）

昨日入 KEV；Google 确认在野利用。升级至 **152.0.7977.82+**。本日目录无新 stamp。

地址：
- 厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- CISA：https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog
- NVD／KEV：https://nvd.nist.gov/vuln/detail/CVE-2026-85046 https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85046

IoC：未见本报统一公开样本哈希。

### 9. 【过期提醒】TrueConf CVE-2026-72530／MLflow CVE-2026-64849

仍在 KEV；due 已过。未补丁环境继续按厂商修复与暴露面处理。

地址：
- TrueConf：https://trueconf.com/blog/news/security-fixes-updates-and-advisories https://nvd.nist.gov/vuln/detail/CVE-2026-72530
- MLflow：https://nvd.nist.gov/vuln/detail/CVE-2026-64849

IoC：TrueConf 关注 4307/TCP 异常。

### 10. ICS

本日 **无显著新发**（仍为 ICSA-26-246-01..08 等）。例：https://www.cisa.gov/news-events/ics-advisories/icsa-26-246-06

### 11. 【边缘 · DeFi／链上声称】

Longbow spot-oracle、Twofold LP、Balancer V1、Cronos 等链上利用／归还谈判讨论。属加密货币安全事件，非企业补丁主线；地址与哈希见 IoC 汇总（若需链上追踪）。

地址：
- X：https://x.com/JaceHoiX/status/2096390063747903629 https://x.com/i/status/2096388490418368778 https://x.com/i/status/2096387982676898005 https://x.com/i/status/2096382933795848300

## 工具与 GitHub 发布

### 1. Sliver v1.7.7／nuclei-templates v10.4.8（续／无新版本）

相对昨日无版本 bump。

地址：
- 仓库：https://github.com/BishopFox/sliver/releases/tag/v1.7.7 https://github.com/BishopFox/sliver
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

IoC：不适用（合法红队框架发布）。

### 2. M365Pwned／SpecterOps skills／VulnClaw／Veneficus

Microsoft 365／Graph 红队工具 M365Pwned；SpecterOps LLM skills 市场；VulnClaw（AI Agent＋MCP，授权实验语境）；Veneficus 全杀伤链植入研究页＋仓库声明。

地址：
- https://github.com/OtterHacker/M365Pwned
- https://github.com/SpecterOps/skills
- https://outflank.nl/blog/2026/09/02/red-team-ai-skills/
- https://github.com/Netw0rkNoob/VulnClaw
- https://abraxaslabs.tech/research/veneficus
- https://github.com/abraxas/veneficus
- X：https://x.com/DirectoryRanger/status/2096327122495180962 https://x.com/ntlmrelay/status/2096285194546208904 https://x.com/EsGeeks/status/2096076626266083410 https://x.com/abraxas_null/status/2096062631413166124

IoC：未见公开攻击者 IoC。

### 3. 【LWiS】BYOVD／EDR 规避与检测基础材料

0xM0nCrush（signed BYOVD process terminator 仓库）；edrEvasionWorkshop（边界外续传）；TrustedSec 检测基础系列；SystemOptimizer BYOVD 分析页。

地址：
- https://github.com/DeathShotXD/0xM0nCrush
- https://github.com/tyeurada/edrEvasionWorkshop
- https://trustedsec.com/blog/building-a-detection-foundation-part-1-the-single-source-problem
- https://cham1ndux.github.io/
- X：https://x.com/ipurple/status/2096173492290928825 https://x.com/DirectoryRanger/status/2096382176489054596 https://x.com/r1cksec/status/2095794818039320755

IoC：未见公开攻击者 IoC（研究／工具材料）。

## APT / Malware 分析

### 1. 【LWiS】DragonForce Ransomware（Windows locker）

DarkAtlas 对已验证 Windows locker 样本的分析文。

地址：
- 文章：https://darkatlas.io/blog/dragonforce-ransomware-analysis-windows-locker
- X：https://x.com/DirectoryRanger/status/2096377312405041585

IoC：以 DarkAtlas 原文样本表为准；本帖未见额外统一哈希列表。

### 2. 【X】Rhysida／Dire Wolf 等勒索与数据声称（未独立核实）

Rhysida 声称 5.79 TB 柏林政府数据；Dire Wolf 关联 Mission Pet Health；另有 Atout France／HopCharge／Medisage／伊拉克卫生系统等泄露或出售声称。**一律按声称记录。**

地址：
- https://x.com/XQOPTRX/status/2096387906864865440
- https://x.com/FalconFeedsio/status/2096365371947397448
- https://missionpethealth.com/
- https://x.com/DarkWebInformer/status/2096351271930184153
- https://x.com/ThreatIntelIN/status/2096322229126746354
- https://x.com/ThreatIntelIN/status/2096321334406230462
- https://x.com/intels_daily/status/2096374595494273120

IoC：上述声称帖多数未见可核验公开哈希。

### 3. 【X】Ledger／Trezor 相关工具广告／社交工程

暗网侧「unleaked」钱包工具广告；另有 Bitcoin IRA／iTrustCapital 社交工程归因讨论（声称）。

地址：
- https://x.com/DarkWebInformer/status/2096353389022007343
- https://x.com/otagherasad/status/2096387804444115389
- https://x.com/patriots50_/status/2096317100889444854

IoC：未见本报可核验统一样本哈希；不转载广告包或凭证内容。

### 4. 【LWiS】AD／IIS／SCOM／GPO 与「bulgaria crime group」线索

IIS AppPool→SYSTEM via AD CS RPC；SCOM Relay／Run As；GPO 利用研究；孤立 agent 组「bulgaria crime group」相关 URL。

地址：
- https://mannulinux.org/2026/08/Privilege-escalation-from-IIS-AppPool-to-NT-AuthoritySYSTEM-via-AD-CS-RPC-endpoint.html
- https://guidepointsecurity.com/
- https://synacktiv.com/
- https://x.com/DirectoryRanger/status/2096381485586555220
- https://x.com/DirectoryRanger/status/2096380060580065480
- https://x.com/ipurple/status/2096155892521595183
- https://x.com/j0wimo/status/2096037573365776532

IoC（帖内 URL，需谨慎核验，可能为投毒／诱饵）：
- https://tmcleod.org/cgi-bin/apchem/wiki.cgi?action=history&id=FederalDataReferenceXYZ
- https://texteditors.org/cgi-bin/wiki.pl?action=rc&from=1777216005
- https://yourls.pro/mv194q48045692%2B

### 5. asmresolver 里程碑

@washi_dev 称 asmresolver 达 100 万次下载（.NET 逆向／恶意软件分析常用库）。

地址：
- https://x.com/washi_dev/status/2096366721439277072

IoC：不适用。

## 地址／IoC 汇总

- **KEV due 今日（09-05）**：Kestra 49869／JFrog 82329／Sangoma 9586／SonicWall 83548+83549 — 以厂商补丁与 KEV 要求为准；未见本报新增统一哈希。
- **Cisco CVE-2026-20212**：关注 TCP **43210/43211**；未见公开 C2／样本哈希。
- **TeamCity／Cadence CVE-2026-63077**：轮换 AWS IAM／插件令牌／连接系统密钥；未见统一公开样本哈希。
- **Magento StyleSmuggler 狩猎路径**：`~/.local/share/.gvfsd/gvfsd-user`；crontab `*/5 * * * *`；`/var/spool/cron/crontabs/`；进程名伪装 `[kworker/u:8:0]`。
- **PaperCut（厂商续抄，due 09-14）**：
  - 狩猎：Application Server 上可疑后利用；`C:\ProgramData\ace.exe`；SimpleHelp 路径 `C:\ProgramData\JWrapper-Remote Access\JWAppsSharedConfig\restricted\SimpleService.exe`（服务名 “Remote Access Service”）；AnyDesk 落盘 `C:\ProgramData\AnyDesk.exe`。
  - 投放 URL（去活化）：`hxxps://sendit[.]sh/Gg7Rp/ace[.]exe`；`hxxps://download[.]anydesk[.]com/AnyDesk.exe`（后者为合法下载域被滥用场景，需结合上下文）。
  - Emergency Patch R3 示例 SHA256（Windows v26 Build 76531）：`9375a9c3cf84140a1d8e21b72d3d2c57d85d4de09ea9ae1dc021b64732427da7`（完整多版本校验和见厂商页）。
- **Chromium CVE-2026-85046**：升级至 **152.0.7977.82+**；Google 确认在野利用。
- **「bulgaria crime group」相关 URL（未核实）**：见 APT 第 4 节。
- **DeFi 链上（可选追踪）**：tx `0x414b5b7c832b67dcd0c3f16907c8702ff794ce9dd0b749d0100e7549ba202d49`；EOA `0x0F932e0fE68B0219820ffcB4C2B1906E29BedacC`、`0x19d55f7FE2d3962796F5825CbDae2dd493Be0986`、`0xC8720447712e6C4c851B3884b4Ec93F9cE8aD5fD`。
- **其余条目**：未见额外可核验公开 IoC，或仅见于原文 — 写「未见公开 IoC」者以上各节为准。

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
- X Latest B（GitHub 工具／C2）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt%20OR%20mythic)&src=typed_query&f=live
- X Latest C（malware／threat）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 09-02 七条警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- CISA 09-04 Chromium 警报：https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog
- Cisco Nexus：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr
- JetBrains TeamCity：https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/
- Broadcom VMSA：https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38288
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
