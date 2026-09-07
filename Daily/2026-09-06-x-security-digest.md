# X 安全情报晚报 · 2026-09-06

> 搜集窗口：圣地亚哥时间 **2026-09-05 20:00 至 2026-09-06 ~20:15**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周日）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-06.json`（collected_at **2026-09-06T20:11:26-03:00**）＋ `/workspace/tools-news-pulse-2026-09-06.md`。CISA KEV catalogVersion **2026.09.04**／**1695** 条／dateReleased **2026-09-04T16:47:03.5197Z**（相对昨日 **+0**，无 09-05／09-06 新入 KEV）。
> **期限今日 09-06：无。期限明日 09-07：无。** Sep2 五条联邦 BOD（Kestra **CVE-2026-49869**、JFrog **CVE-2026-82329**、Sangoma **CVE-2026-9586**、SonicWall **CVE-2026-83548/83549**）自 **09-05** 起已 **OVERDUE**。due_near：JFrog 路径 **CVE-2026-66384**（09-10）；PaperCut **81578/82078**（09-14）；LiteLLM／Starlette（09-16）；Chromium **85046**（09-18）。TrueConf **72530**／MLflow **64849** 仍逾期。
> X：`/workspace/x-posts-2026-09-06.json`（合并 **35** 条：A7／B5／C17／LWiS6；其中 **新 29**／已见 6；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.32h**（高流量，**远不足 24h**）。Search B 约 **41h**（窗内保留 5）。Search C 约 **6.1h**。LWiS List 约 **1.0h**（6 条均已在昨日 seen_ids）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · KEV 逾期续】** Sep2 五条 BOD 昨日到期后进入 **OVERDUE**：Kestra OSS **CVE-2026-49869**、JFrog Artifactory **CVE-2026-82329**、Sangoma Switchvox **CVE-2026-9586**、SonicWall SMA1000 **CVE-2026-83548/83549**。目录仍停在 2026.09.04／1695（+0）。未打补丁资产按厂商说明与 KEV 要求处理。
  警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
  SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

- **【NEW · Chrome Early Stable 153】** Google 发布 Early Stable **153.0.8010.27/.28**（Windows；Mac 即将）。KEV **CVE-2026-85046** 仍锚定 Stable **152.0.7977.82+**（due 09-18）；Early Stable 帖体未见 CVE 列表。
  Early Stable：https://chromereleases.googleblog.com/2026/09/early-stable-update-for-desktop.html
  Stable（安全修复／在野）：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html

- **【X · Roundcube】** 称修复 12 项 Webmail 漏洞（叙述无 CVE），含零点击存储型 XSS；影响 **1.6.19／1.7.4 之前**。升级至厂商最新；**不转写利用细节。**
  X：https://x.com/__kokumoto/status/2096736601602945472

- **【X · Telegram】** 称 0-click sticker crash／DoS（已报告 Telegram／有 PoC 声称）。防御向仅记现象；**不转写 PoC。**
  X：https://x.com/ridvanyagli/status/2096737117565071681

- **【X · CrowdStrike Falcon／FalconFlank】** 研究者称权限提升 PoC 已确认，厂商调查中；日文分析文。
  文章：https://rocket-boys.co.jp/security-measures-lab/crowdstrike-falconflank-edr-design-risk/
  X：https://x.com/securityLab_jp/status/2096735497985093955

- **【PaperCut 续】** NG／MF **CVE-2026-81578/82078** 仍 KEV（due 09-14）。**R3** 仍为紧急补丁；last_updated 仍 **September 5, 2026**（无 09-06  bump）。公网未打补丁应假定失陷。
  厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/

- **【工具】** Sliver **仍 v1.7.7**；nuclei-templates **仍 v10.4.8**。X 窗：KHAØS C2、OWASP Amass、prompt-injection-example、Audn Ethical Hacker Agent、Subfinder 汇总。
  仓库：https://github.com/BishopFox/sliver/releases/tag/v1.7.7 https://github.com/28Zaaky/khaos-c2 https://github.com/owasp-amass/amass https://github.com/Antolius/prompt-injection-example https://github.com/apps/audn-ethical-hacker-agent/ https://github.com/projectdiscovery/subfinder

- **【APT／勒索／声称】** 多起未核实暗网／勒索声称：Alpha SMS、ShinyHunters／JD.com、ASUS DB、DYSPHOR1A→RTAD、SNU IDOR、Dire Wolf→eAssist、VEXY→Sancity、DragonForce→Norwood 等。LWiS 窗内 6 条（DirectoryRanger 串）均已在昨日 seen。
  https://x.com/intels_daily/status/2096736995124912504
  https://x.com/intels_daily/status/2096721913754042475
  https://x.com/DailyDarkWeb/status/2096720818164334846
  https://x.com/FalconFeedsio/status/2096682939383984142
  https://darkatlas.io/blog/dragonforce-ransomware-analysis-windows-locker

- **【新闻备援】** Risky Biz **无新 ID**（仍 RBNEWS609／RBFEATURES38／SRB182／RB851／RBNEWS608／BTN181）；tl;dr sec 仍 **#343**（#344 soft-404）。ICS **无新发**（仍 ICSA-26-246-*）。
  https://risky.biz/RBNEWS609/ https://tldrsec.com/blog/tldr-sec-343/

## CVE / POC / 漏洞

### 1. 【KEV 逾期】Sep2 五条 BOD（due 已过 2026-09-05）

JFrog Artifactory **CVE-2026-82329**、Sangoma Switchvox **CVE-2026-9586**、SonicWall SMA1000 **CVE-2026-83548/83549**、Kestra OSS **CVE-2026-49869** 自昨日起逾期。LiteLLM **CVE-2026-59822**／Starlette **CVE-2026-48710** due 09-16；JFrog 路径 **CVE-2026-66384** due 09-10。按厂商补丁／缓解与联邦 BOD 要求收敛暴露面。**不转写利用细节。**

地址：
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-82329 https://nvd.nist.gov/vuln/detail/CVE-2026-9586 https://nvd.nist.gov/vuln/detail/CVE-2026-83548 https://nvd.nist.gov/vuln/detail/CVE-2026-83549 https://nvd.nist.gov/vuln/detail/CVE-2026-49869 https://nvd.nist.gov/vuln/detail/CVE-2026-59822 https://nvd.nist.gov/vuln/detail/CVE-2026-48710 https://nvd.nist.gov/vuln/detail/CVE-2026-66384
- SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
- nuclei（JFrog）：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-82329.yaml
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见本条新增统一 IoC；逐厂商公告。

### 2. 【NEW】Chrome Early Stable 153 ＋ KEV Chromium CVE-2026-85046 续

KEV **CVE-2026-85046**（dateAdded 2026-09-04，due **2026-09-18**）仍对应 Stable **152.0.7977.82+**（Google 确认在野）。今日新增 Early Stable 推送 **153.0.8010.27/.28**（Windows）；帖体无 CVE 枚举。生产环境优先按 KEV／Stable 安全通道收敛。

地址：
- Early Stable：https://chromereleases.googleblog.com/2026/09/early-stable-update-for-desktop.html
- Stable 安全更新：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- CISA 09-04 警报：https://www.cisa.gov/news-events/alerts/2026/09/04/cisa-adds-one-known-exploited-vulnerability-catalog
- NVD／KEV：https://nvd.nist.gov/vuln/detail/CVE-2026-85046 https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85046

IoC：未见公开攻击者 C2／样本哈希；行动以浏览器升级为主。

### 3. 【X】Roundcube Webmail 12 项修复（叙述无 CVE）

日文转述称 Roundcube 修复 12 项漏洞，含零点击存储型 XSS；受影响叙述为 **1.6.19／1.7.4 之前**。升级至厂商最新发行版；**不转写利用链。**

地址：
- X：https://x.com/__kokumoto/status/2096736601602945472

IoC：未见公开 IoC。

### 4. 【X】Telegram 0-click sticker crash／DoS 声称

转述称特制 sticker 可致客户端不可用（与版本／平台无关的声称）；称已向 Telegram 报告并提供 PoC。防御向仅记现象与厂商通报路径；**不转写 PoC／步骤。**

地址：
- X：https://x.com/ridvanyagli/status/2096737117565071681
- 相关披露说明：https://x.com/0x6rss/status/2096733544798187882

IoC：未见公开 IoC。

### 5. 【X】CrowdStrike Falcon／FalconFlank 权限提升 PoC 声称

研究者称已确认设计风险相关权限提升，厂商调查中。日文实验室分析文；**不转写 PoC。**

地址：
- 文章：https://rocket-boys.co.jp/security-measures-lab/crowdstrike-falconflank-edr-design-risk/
- X：https://x.com/securityLab_jp/status/2096735497985093955

IoC：未见公开 IoC。

### 6. 【X】Next.js image optimizer 攻击面提示

建议限制 `remotePatterns`／关闭 remote loaders 等防御性缓解；未见 CVE 编号。

地址：
- X：https://x.com/0xhashlol/status/2096733894519230642

IoC：未见公开 IoC。

### 7. 【X】CS2 VAC Live／Liquid Network（周边）

CS2 VAC Live 取消比赛利用分析（服务器信任未充分校验 disconnect reason 的公开分析）。Liquid Network 暂停／攻击者自称白帽（卡片称约 4,000 BTC）— 非传统 CVE，作事件交叉。

地址：
- CS2：https://x.com/itzsagka/status/2096735195529695411
- Liquid：https://x.com/freeAgent85/status/2096735604436611322

IoC：未见公开 IoC。

### 8. 【PaperCut 续】CVE-2026-81578／82078（KEV due 09-14）

Emergency Patch **R3** 仍最新；厂商页 last_updated 仍 **5 September 2026**（无 09-06 新情报）。公网暴露未打补丁应假定失陷。

地址：
- 厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-81578 https://nvd.nist.gov/vuln/detail/CVE-2026-82078

IoC：续见厂商页狩猎路径／示例哈希（见下方 IoC 汇总）；本日无新抄录。

## 工具与 GitHub 发布

### 1. Sliver／nuclei-templates（公开备援）

Sliver **仍 v1.7.7**（2026-09-03）；nuclei-templates **仍 v10.4.8**（2026-08-24）。本窗 X Latest B 未见二者新 release 帖。

地址：
- https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

IoC：不适用。

### 2. 【X】KHAØS C2

称经 Teams／GitHub／DNS 等可信服务路由 agent 流量的后渗透 C2 框架。

地址：
- 仓库：https://github.com/28Zaaky/khaos-c2
- X：https://x.com/28zaaky/status/2096626008115822683

IoC：未见公开 IoC。

### 3. 【X】OWASP Amass／Subfinder 侦察工具

Amass 攻击面测绘；Subfinder 等 bug bounty 侦察工具汇总。

地址：
- Amass：https://github.com/owasp-amass/amass
- Subfinder：https://github.com/projectdiscovery/subfinder
- X：https://x.com/EsGeeks/status/2096671684547764626 https://x.com/NitinGavhane_/status/2096533136826081591

IoC：未见公开 IoC。

### 4. 【X】prompt-injection-example／Audn Ethical Hacker Agent

电子表格隐藏 prompt-injection 红队示例仓库；Audn GitHub App（PR 内伦理黑客／SAST 风格检查）。

地址：
- https://github.com/Antolius/prompt-injection-example
- https://github.com/apps/audn-ethical-hacker-agent/
- X：https://x.com/di_zhang_fdu/status/2096645921845239848 https://x.com/audn_ai/status/2096594762249785549

IoC：未见公开 IoC。

### 5. 【LWiS 已见】BYOVD／EDR、AD CS、SCOM、BloodHound 后渗透（昨日交叉）

窗内 LWiS 6 条均已在昨日 seen_ids；续链供交叉。

地址：
- BYOVD：https://cham1ndux.github.io/posts/BYOVD-EDR-killer-with-a-UAC-bypass-and-a-lying-comment-block/
- AD CS：https://www.mannulinux.org/2026/08/Privilege-escalation-from-IIS-AppPool-to-NT-AuthoritySYSTEM-via-AD-CS-RPC-endpoint.html
- SCOM：https://www.guidepointsecurity.com/blog/attacking-and-defending-scom/
- OSINT：https://medium.com/@dzianisskliar29/internal-osint-post-compromise-reconnaissance-beyond-bloodhound-ea8b4d4f594f
- X：https://x.com/DirectoryRanger/status/2096382176489054596 https://x.com/DirectoryRanger/status/2096381485586555220 https://x.com/DirectoryRanger/status/2096380060580065480 https://x.com/DirectoryRanger/status/2096378802947469806

IoC：未见公开 IoC。**不转写利用步骤。**

## APT / Malware 分析

### 1. 【X】勒索／数据泄露声称（均未独立核实）

窗内多起暗网出售／勒索站点声称，仅作威胁情报交叉，不作确认：

| 声称 | X 原帖 |
|------|--------|
| Alpha SMS（乌克兰 SMS 网关）客户／日志／API | https://x.com/intels_daily/status/2096736995124912504 |
| ShinyHunters／JD.com ~7.5 亿条 | https://x.com/intels_daily/status/2096721913754042475 |
| ASUS 数据库 ~1023 GB 私售 | https://x.com/DailyDarkWeb/status/2096720818164334846 |
| 约旦情报官员 DB 声称 | https://x.com/DailyDarkWeb/status/2096722501296349631 |
| Vedicline ~10 万条 | https://x.com/ThreatIntelIN/status/2096731430399463746 |
| 77 Diamonds 客户数据调查 | https://x.com/ICPLEGEND1966/status/2096697850893590877 |
| Bitbuy.ca 交易／风险分 | https://x.com/intels_daily/status/2096691687468814689 |
| DYSPHOR1A → Myanmar RTAD ~1.08 GB | https://x.com/FalconFeedsio/status/2096682939383984142 https://x.com/ThreatAtlas/status/2096660269615161639 |
| DragonForce → Norwood Law Firm | https://x.com/ThreatAtlas/status/2096678246200816030 |
| Dire Wolf → eAssist Dental | https://x.com/FalconFeedsio/status/2096668446952161714 |
| VEXY → Sancity（印度地产） | https://x.com/FalconFeedsio/status/2096668352592916976 |
| PHOENIX Pharma Serbia／Bulgaria ~293 MB | https://x.com/DarkWebInformer/status/2096661267918299644 |
| 法国 SNU 门户 IDOR ~275K | https://x.com/DarkWebInformer/status/2096658412968808849 |
| Strezhevoy 门户 ~54K | https://x.com/DarkWebInformer/status/2096656574747992103 |
| 1.95 亿身份／驾照数据集出售声称 | https://x.com/DarkWebInformer/status/2096652573013143778 |
| 求购 cPanel／Plesk／WHM（stealer 日志） | https://x.com/DarkWebInformer/status/2096650313046356452 |

关联站点（帖内，非 IoC 确认）：https://rtad.gov.mm https://dentalbilling.com https://sancity.in

IoC：未见本报可核验统一样本哈希；不转载广告包或凭证内容。

### 2. 【LWiS 已见】DragonForce Windows locker 分析

DFIR 分析文（昨日已交叉）；今日 List 窗再次出现。

地址：
- 文章：https://darkatlas.io/blog/dragonforce-ransomware-analysis-windows-locker
- X：https://x.com/DirectoryRanger/status/2096377312405041585

IoC：未见公开 IoC（以原文为准）。

### 3. 【LWiS 已见】Windows 取证／IRFlow

地址：
- 视频：https://www.youtube.com/watch?v=W9xHbNgZuT0
- X：https://x.com/DirectoryRanger/status/2096382581029609753

IoC：不适用。

## 地址／IoC 汇总

- **KEV 逾期（自 09-05）**：Kestra 49869／JFrog 82329／Sangoma 9586／SonicWall 83548+83549 — 以厂商补丁与 KEV 要求为准；未见本报新增统一哈希。
- **Chromium CVE-2026-85046**：升级至 Stable **152.0.7977.82+**；关注 Early Stable **153.0.8010.27/.28**（Win）；Google 确认在野利用。
- **PaperCut（厂商续抄，due 09-14）**：
  - 狩猎：Application Server 上可疑后利用；`C:\ProgramData\ace.exe`；SimpleHelp 路径 `C:\ProgramData\JWrapper-Remote Access\JWAppsSharedConfig\restricted\SimpleService.exe`（服务名 “Remote Access Service”）；AnyDesk 落盘 `C:\ProgramData\AnyDesk.exe`。
  - 投放 URL（去活化）：`hxxps://sendit[.]sh/Gg7Rp/ace[.]exe`；`hxxps://download[.]anydesk[.]com/AnyDesk.exe`（后者为合法下载域被滥用场景，需结合上下文）。
  - Emergency Patch R3 示例 SHA256（Windows v26 Build 76531）：`9375a9c3cf84140a1d8e21b72d3d2c57d85d4de09ea9ae1dc021b64732427da7`（完整多版本校验和见厂商页）。
- **Roundcube／Telegram／FalconFlank／Next.js／KHAØS 等本日 X 条**：未见额外可核验公开 IoC。
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
- X Latest B（GitHub 工具／C2）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20mythic)&src=typed_query&f=live
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
- Chrome Early Stable：https://chromereleases.googleblog.com/2026/09/early-stable-update-for-desktop.html
- Chrome Stable 安全：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- SonicWall SNWLID-2026-0016：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
