# X 安全情报晚报 · 2026-10-10

> 搜集窗口：圣地亚哥时间 **2026-10-09 20:15 至 2026-10-10 20:16**（America/Santiago / UTC-3，约 24 小时）。ISO／X 搜索：`start_time=2026-10-09T23:15:00Z`，`end_time≈2026-10-10T23:10:00Z`（接口将 end 微调到至少 10 秒前）。
> **X 采集方式**：使用 Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`／`get_posts_by_id(s)`，含 t.co 展开字段），**未开浏览器，未检查 @seogoogle4 浏览器登录状态**。A／定向用 relevancy；B／C 各 relevancy；另做 PaperCut／Citrix／Ahsay／SonicWall／Atlassian／GhostAction／Longlegs／DarkSword／PoeLLM 定向；LWiS List 分批 `from:`（本轮约 4 批高价值：chudyPB／vxunderground／Dinosn／L0Psec／_xpn_／watchtowrcyber／DFIR_Radar／rad9800／pdiscoveryio／Synacktiv／jm33_m0／Flangvik／bohops／_RastaMouse／C5pider／TrustedSec／briankrebs 圈／cyb3rops／daaximus 等）。本轮约 **18** 次 X 读取（未触日限／分钟限）。合并 **52** 条安全相关新帖（A20／B3／C14／LWiS15），与 seen_ids 去重。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON `/workspace/kev-2026-10-10.json`（= `/workspace/enrich-2026-10-10/kev.json`）；厂商／研究页于 `/workspace/enrich-2026-10-10/`（CISA Citrix Alert 10-09 修订、Citrix CTX697191、AA26-281A、Atlassian CVE-2026-21589 公告、Previdian 利用观测、nulltap PaperCut、THN GoBalance、Picus Dire Wolf、Help Net Flax／FBI、Risky／tl;dr 首页、GitHub releases：emp3r0r／Sliver／nuclei／nuclei-templates）。
> **CISA KEV：catalogVersion 2026.10.08／1739 条，Δ+0**（相对昨日同一版本；dateReleased 仍 2026-10-08T20:09Z）。**今日无 NEW**。
> **due_today（10-10）：无**；**newly_overdue：无**（Citrix CVE-2026-88779 自 10-07 起继续逾期；Citrix 88771／88772、FortiMail 104286、Zammad 102489／102490、Cisco 76504 等仍逾期）；**upcoming 7 天：6 条**（AA26-281A 五条 due **2026-10-11（明天）**；Apple CVE-2026-86950 due **2026-10-13**）。CVE-2026-107406／CVE-2026-21589／CVE-2026-102255／Ahsay 105133／105134 **仍未进 KEV**。
> 抓取备注：BleepingComputer 相关页 Cloudflare／403；部分 SonicWall PSIRT 深链返回异常短页；tl;dr sec 首页可抓，最新仍 **#349**；Risky Business 首页仍见 **RBNEWS618**；Ahsay 厂商 hotfix 10.3.4.45 主要来自窗口内二次消息（伙伴门户），未见独立公开安全公告页可核验。
> 规则：每条含完整 https URL；分列 X 原帖／GitHub·PoC 仓库／厂商公告／文章；没有指标就写「未见公开 IoC」；不编造；**不转载利用代码／payload／PoC 步骤**；泄露／入侵／勒索声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【政府告警更新】CISA 于 10-09 修订 Citrix NetScaler 告警**：纳入 **CVE-2026-107406**，并强调 88771–88779 与 107406 尽快打补丁；打补丁前先保全证。
  政府：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
  厂商：https://support.citrix.com/external/article/CTX697191
- **【在野尝试 · 未进 KEV】Atlassian CVE-2026-21589**：披露后数小时内出现扫描／蜜罐命中；Previdian 称截至 10-10 约 **321** 次尝试／49 源 IP（**不等于生产端成功入侵**）。
  厂商：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
  文章：https://previdian.com/CVE-2026-21589
- **【蜜罐探测 · 有补丁 · 未进 KEV】SonicWall SMA1000 CVE-2026-102255**（CVSS 10.0 预认证 SSRF）；修复 **12.4.3-03670／12.5.0-03082**；成功入侵未见确认。
  文章：https://cybermerge.com/stories/sonicwall-sma1000-cve-2026-102255-exploited
  X 原帖：https://x.com/cybermergemedia/status/2108736247086903484
- **【在野 · 补丁争议】AhsayCBS CVE-2026-105133／105134**：Huntress 称 **10.3.4 仍受影响**；窗口内消息称厂商承认 10.3.4.0 未完全修复、伙伴门户有 **hotfix 10.3.4.45**（待厂商公开页交叉）。
  X 原帖：https://x.com/DFIR_Radar/status/2108815305581744458
  X 原帖（hotfix）：https://x.com/TwitGri/status/2109013502216044619
- **【KEV 明天到期】AA26-281A 五条 due 2026-10-11**（ProFTPD／BIND／Struts／ONLYOFFICE／Strapi）；Apple 86950 due 10-13。
  政府：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- **【工具】emp3r0r v5.1.0**（2026-10-10 发布）：C2 通道 ECH；operator 移除 mTLS。Sliver／nuclei／nuclei-templates 无新版。
  GitHub：https://github.com/jm33-m0/emp3r0r/releases/tag/v5.1.0
- **【Malware／DFIR】** Dire Wolf 狩猎特征公开；GoBalance 致 .onion 私钥可恢复；FBI 扣押 Flax Typhoon 相关 7 域名；GhostAction／PoeLLM／P7 DarkSword／Warlock 续报。
- **【合并统计】** X **52**（A20／B3／C14／LWiS15）；seen_ids **2572→2660**；KEV **2026.10.08／1739／Δ0**；Risky RBNEWS618；tl;dr #349。

## CVE / POC / 漏洞

### X-1. 【政府更新 · 跟踪】CISA 修订 Citrix NetScaler 告警（纳入 CVE-2026-107406）
CISA 告警页 **Last Revised October 09, 2026**：新增 **CVE-2026-107406**；纳入已于 10-04 进 KEV 的 **CVE-2026-88779**；澄清 88779 与 88771 可能关联；催促对 **88771–88779 与 107406** 尽快打补丁，并在升级前审查是否已遭入侵（升级可能削弱取证可见性）。**107406 仍未进 KEV**；Citrix 称公告时未见该条未缓解利用。防御：确认是否启用 SAML SP／IdP；升到 **14.1-73.46／13.1-64.29**（及对应 FIPS／NDcPP）；按 Citrix／NetScaler Console 指引狩猎；对已逾期的 88771／88772／88779 一并复查。
地址：
- X 原帖：https://x.com/Breachrr/status/2108842985152504235
- 政府告警：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- 厂商 CTX697191：https://support.citrix.com/external/article/CTX697191
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-107406
IoC：未见公开网络 IoC（107406 未见确认利用）；88771 相关狩猎关键词见 DFIR Radar 周报（pitboss／NSPPE／「unexpectedly died」等，**非完整利用步骤**）。

### X-2. 【在野尝试 · 未进 KEV】Atlassian CVE-2026-21589（任意文件读→条件性管理接管）
窗口内持续发酵：SANS ISC 日记与 Previdian 蜜罐均观察到针对 watchTowr 公开特征的请求。Previdian 称自首观（10-06）至 10-10：**321** 次尝试、**49** 个源 IP、17 国、4 个蜜罐——明确为 **尝试而非已证实的生产端成功入侵**。**仍未进 KEV**。防御：按厂商固定版本升级（Jira／Confluence／Bitbucket／Crowd／Bamboo／Crucible／Fisheye 等 Data Center）；无法立即打补丁则按 Atlassian 文档做 WAF／重写缓解；狩猎访问日志中 `..` 紧邻 `/` 或 `::`（含编码变体）；Crowd 集成环境轮换可能泄露的 application 凭据并审计异常建用户／加管。
地址：
- X 原帖（摘要）：https://x.com/Python_s_/status/2108754866906529894
- X 原帖：https://x.com/EHackerNews/status/2108944584944537720
- X 原帖：https://x.com/cybermergemedia/status/2109013896761884861
- 厂商公告：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
- 研究 watchTowr：https://labs.watchtowr.com/you-wont-hear-about-these-even-in-myths-atlassian-jira-confluence-and-more-pre-auth-arbitrary-file-read-cve-2026-21589/
- 蜜罐观测 Previdian：https://previdian.com/CVE-2026-21589
- SANS ISC：https://isc.sans.edu/diary/Scans%20for%20Atlassian%20vulnerablity%20%28CVE-2026-21589%29/33406
IoC：未见公开统一 C2／哈希表；狩猎以路径穿越特征与 WEB-INF 异常读取为主。

### X-3. 【蜜罐探测 · 有补丁 · 未进 KEV】SonicWall SMA1000 CVE-2026-102255（预认证 SSRF，CVSS 10.0）
WorkPlace 接口预认证 SSRF；窗口内多源称 Previdian 蜜罐见到指向内部 CouchDB 的探测（含 admin:admin 等特征叙述）。**成功入侵未见确认**；**未进 KEV**。厂商修复构建：**12.4.3-03670** 或 **12.5.0-03082**（10-06 热修语境）；有消息称 **9 月补丁构建仍暴露**。防御：暴露的 SMA1000／WorkPlace 优先升级；限制管理面；审查对内部服务的异常请求；补丁会重启并断开 VPN，预留窗口。BleepingComputer 原文页本轮 **403／Cloudflare**，以二次报道与 X 交叉。
地址：
- X 原帖：https://x.com/cybermergemedia/status/2108736247086903484
- X 原帖（修复版本）：https://x.com/cybermergemedia/status/2108740091762074009
- X 原帖：https://x.com/miciver/status/2108906670810112302
- 文章 CyberMerge：https://cybermerge.com/stories/sonicwall-sma1000-cve-2026-102255-exploited
- NVD（按 CVE 构造）：https://nvd.nist.gov/vuln/detail/CVE-2026-102255
IoC：厂商未见公开 IoC 清单；蜜罐侧描述见上（行为／请求特征）。

### X-4. 【在野 · 补丁争议】AhsayCBS CVE-2026-105133＋105134
Huntress／DFIR Radar：认证绕过＋命令注入链，投放 JSP webshell 与伪装 **edge.exe** 的 XMRig，持久化名如 **MicrosoftEdgeUpdateSvc**。Huntress 称 **10.3.4 仍受影响**；部分消息称厂商曾宣称 10.3.4 已修——**存在争议**。窗口内法语二次消息：厂商承认 **v10.3.4.0 未完全修复**，伙伴门户提供 **hotfix 10.3.4.45**（**未见本轮可抓取的独立厂商公告页**，标待核验）。防御：管理面仅可信网络；优先打 hotfix／厂商最新构建并重启；狩猎 `cbssvcX64.exe` 异常子进程（curl／certutil）、TEMP 中 **WinRing0x64.sys**／**Taskgmr.ps1**、假 Edge 挖矿服务；命中倾向整机重建。
地址：
- X 原帖（DFIR）：https://x.com/DFIR_Radar/status/2108815305581744458
- X 原帖（狩猎）：https://x.com/DFIR_Radar/status/2108830377682854349
- X 原帖（hotfix 二次消息）：https://x.com/TwitGri/status/2109013502216044619
- X 原帖（争议）：https://x.com/tsnmediahub/status/2108917472283811948
- 文章 Huntress（既有）：https://www.huntress.com/blog/ahsaycbs-flaws-exploit
- GitHub（Huntress 规则／目录）：https://github.com/huntresslabs/threat-intel/tree/main/2026/2026-10
IoC：见汇总「AhsayCBS」；本窗口无新完整哈希表。

### X-5. 【跟踪 · 有补丁】PaperCut NG／MF ≥26.0.5（昨日 watchTowr 链续报）
窗口内 Dinosn／nulltap／防御向帖继续强调：**26.0.5** 为收口构建；管理口默认 9191 勿对公网；审查 Scan-to-Fax／配置异常改动。防御同昨日，不升到 ≥26.0.5 视为未修。
地址：
- X 原帖（Dinosn）：https://x.com/Dinosn/status/2108759287757668519
- X 原帖（nulltap）：https://x.com/Nulltap_/status/2108961426073370863
- 文章 watchTowr：https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/
- 文章 nulltap：https://nulltap.sh/p/papercut-emergency-patches-scan-fax-rce/
- GitHub（DAG，非利用步骤）：https://github.com/watchtowrlabs/watchTowr-vs-PaperCut-WT-2026-0143/
IoC：未见公开 C2／哈希；行为／日志狩猎见昨日晚报。

### X-6. 【KEV · Δ0 · 明天到期】catalogVersion 2026.10.08／1739；AA26-281A 五条 due **2026-10-11**
本日 KEV **无更新**。即将到期：
- **2026-10-11**：CVE-2015-5477（ISC BIND）、CVE-2016-3081（Apache Struts）、CVE-2023-22894（Strapi）、CVE-2021-3199（ONLYOFFICE）、CVE-2015-3306（ProFTPD）
- **2026-10-13**：CVE-2026-86950（Apple）
联合通告：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
IoC：见 AA26-281A／既有晚报。

### X-7. 【其他提及／研究】
- Apache DataSketches（datasketches-cpp）多条 DoS／内存问题，修复语境 **5.3.0**：CVE-2026-103635／103636／103501 — X https://x.com/vulnipulse/status/2108869861724373288 等
- Microsoft CVE-2026-61936（MSRC）：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-61936 ／ X https://x.com/PRINCENULLBITE/status/2108893614927409273
- Splunk 多 CVE（含 CVE-2026-76269，NCSC-2026-0412 语境）：https://x.com/zoomeyebot/status/2109052634569327043
- GoBalance 加密截断致 .onion 私钥可从公开描述符恢复（Searchlight Cyber，10-08 披露语境）：见 APT／工具交叉节
- Joomla／WSO2 等「PoC live」扫描器广告帖：**仅作噪声过滤，不采信为新在野事件**
IoC：以上未见新增可核验公开 IoC（GoBalance 见下节）。

### P-1. 【仍逾期高信号】
Citrix **88771／88772／88779**、Check Point 85102／93616、Arista 93952、F5 94127、JFrog 42016／42018、Zyxel 7273、Microsoft 81963／85880／65660、Google 87491／85046／58704、Cisco 76460／**76504**、Acronis 87886、WSO2 5430、Adobe 71362、MikroTik 67279、WordPress 87902、Fortinet **104286**、Zammad **102489／102490**。
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

## 工具与 GitHub 发布

### 1. 【新】emp3r0r **v5.1.0**（2026-10-10T22:35:15Z）
相对昨日 v4.24.1／中间 v5.0.0 线：本标签注明 **ECH 支持进入 C2 通道**（utls／tls）；**operator 移除 mTLS**。防御／监测侧留意 C2 流量可能更多使用 ECH 封装。
- GitHub Release：https://github.com/jm33-m0/emp3r0r/releases/tag/v5.1.0
- Compare：https://github.com/jm33-m0/emp3r0r/compare/v5.0.0...v5.1.0

### 2. 核心扫描器／C2：其余无新版
- Sliver **v1.7.8**（2026-10-03）：https://github.com/BishopFox/sliver/releases/tag/v1.7.8
- nuclei **v3.11.1**：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates **v10.5.0**：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.0

### 3. Diaspore（rad9800）续：可自举／浏览器 playground
- X：https://x.com/rad9800/status/2108914378028531900
- 文档／Playground：https://radkawar.github.io/diaspore/playground.html
- GitHub：https://github.com/radkawar/diaspore

### 4. 其他
- ProjectDiscovery Neo 推广：https://x.com/pdiscoveryio/status/2108907672578011424
- TrustedSec SecurityNoise tabletop 预告：https://x.com/TrustedSec/status/2108937347832135838
- 窗口内 Group B「github.com + C2／nuclei…」噪声极大（非安全 Cobalt 撞名等），有效工具帖偏少。

## APT / Malware 分析

### X-1. 【DFIR · 有狩猎 IoC】Dire Wolf 勒索软件
Picus／DFIR Radar：双勒索；加密前杀 Event Log、wevtutil 清日志、删卷影；落盘 `.direwolf-encrypted`；自删。狩猎：**Global\\direwolfAppMutex**、`C:\\runfinish.exe`、`HowToRecoveryFiles.txt`。
地址：
- X 原帖：https://x.com/DFIR_Radar/status/2108936193068990765
- 文章 Picus：https://www.picussecurity.com/resource/blog/dire-wolf-ransomware-attacks-how-to-test-and-strengthen-your-defenses
IoC：见汇总「Dire Wolf」。

### X-2. 【供应链 · 续】GhostAction 恶意 GitHub Actions
窗口内称活动扩大（被盗维护者令牌、含游戏引擎作者等叙述）；Socket／THN 系续报。防御：搜 `security-audit.yml`／`github_actions_security.yml`；轮换 Actions／历史密钥。
地址：
- X 原帖：https://x.com/Python_s_/status/2108824943202906600
- X 原帖：https://x.com/y2_intel/status/2108714796048871818
- 文章 THN（既有）：https://thehackernews.com/2026/10/credential-stealing-github-actions.html
IoC：见汇总「GhostAction」（C2 `193.32.204.199`）。

### X-3. 【iOS · 续 · 有 IoC】P7 DarkSword
blackorbird／iVerify：减负调试日志、localStorage 防重复利用；Keychain 改为设备端 JSON 抽取；双向 C2（`/beacon` 等）；SpringBoard 注入。须 **iOS 18.4.1+**。
地址：
- X 原帖：https://x.com/blackorbird/status/2108750019457368444
- 文章：https://www.iverify.com/blog/darksword-variant-threat-research
IoC：见汇总「P7 DarkSword」（沿用昨日 IP／域名表）。

### X-4. 【续 · 有 IoC】PoeLLM／Warlock（Longlegs）
PoeLLM：续报称影响 3400+ 暴露 AI／LLM 相关服务，C2 藏于 GitHub 诗作等叙述。Warlock／Longlegs：SharePoint ToolShell→域内 SYSVOL／dfsrs 分发续报。
地址：
- X 原帖（PoeLLM）：https://x.com/bsubra/status/2108891823204597806
- 文章 Lumen（既有）：https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware
- GitHub IoC：https://github.com/blacklotuslabs/IOCs/blob/main/PoeLLM_IOCs.txt
- X 原帖（Warlock）：https://x.com/sh3ll_c0d3/status/2108943397075431525
- 文章 PolySwarm（既有）：https://blog.polyswarm.io/china-linked-warlock-ransomware-campaign-targets-critical-infrastructure
IoC：见汇总「PoeLLM」「Longlegs／Warlock」。

### X-5. 【执法】FBI 扣押 Flax Typhoon 相关 Microscan／FishHub 七域名
与 Integrity Tech／Mirai 变种僵尸网络语境相关；联合通告含 IoC。AA26-281A 中 Flax 所用老旧 CVE 明天到期。
地址：
- X 原帖：https://x.com/DFIR_Radar/status/2108890888524927299
- 文章：https://www.helpnetsecurity.com/2026/10/09/fbi-flax-typhoon-microscan-fishhub-domains/
IoC：见联合通告原文（本轮未完整抄录域名表；请以 DOJ／FBI／厂商通告为准）。

### X-6. 【漏洞利用面】GoBalance → .onion 地址劫持
Searchlight Cyber：从公开描述符恢复 Tor 格式私钥，可劫持 .onion（**不直接等于拿下源站服务器／库**）。已暴露密钥无法「吊销」，运营方须迁移新 .onion。
地址：
- X 原帖：https://x.com/DFIR_Radar/status/2108905839444508995
- 文章 THN：https://thehackernews.com/2026/10/gobalance-flaw-lets-attackers-hijack.html
IoC：未见公开通用 C2；处置以密钥轮换／地址迁移为主。

### X-7. 【检测工程】Azure Monitor DCR 可静默丢弃进 Sentinel 前的安全事件
DFIR Radar 摘要 detect.fyi：`transformKql` 可在入库前过滤；需为 DCR 打开诊断指标／错误日志，并对 `MICROSOFT.INSIGHTS`／dataCollectionRules 写操作做审计。
地址：
- X 原帖：https://x.com/DFIR_Radar/status/2109026787413958953
- 文章：https://detect.fyi/before-it-reaches-sentinel-how-your-own-pipeline-can-silently-drop-security-evidence-e4ab2640249d
IoC：未见公开 IoC（配置／检测问题）。

### X-8. 【UNCONFIRMED／跟踪】
- Silent Ransom Group 称 6 个月向 27 家律所勒索 2.07 亿美元（**无加密、社工电话**）— **UNCONFIRMED**：https://securityaffairs.com/200719/cyber-crime/silent-ransom-group-allegedly-extorted-207-million-without-encrypting-files.html ／ X https://x.com/Dinosn/status/2108988640017998107
- vxunderground／malwrhunterteam：「goop」类 ATM／POS 更新仿冒样本 — 截图向，**未见本轮完整公开 IoC 表**：https://x.com/vxunderground/status/2108765611996102685
- ThreatAtlas 等批量勒索受害者声称：一律 **UNCONFIRMED**
- DFIR Weekly 另列 TraderTraitor／Midnight Mimosa／CyberXero／PhantomPolia 等 — 多为周回顾，细节见分帖与既有晚报
IoC：声称类条目未见可核验公开 IoC。

## 地址／IoC 汇总

### Dire Wolf（DFIR Radar／Picus 摘要，原样）
- Mutex：`Global\\direwolfAppMutex`
- 路径：`C:\\runfinish.exe`
- 勒索说明：`HowToRecoveryFiles.txt`
- 扩展名：`.direwolf-encrypted`
- 行为：终止 Event Log 服务；`wevtutil` 清日志；删除卷影／备份；自删
- 文章：https://www.picussecurity.com/resource/blog/dire-wolf-ransomware-attacks-how-to-test-and-strengthen-your-defenses

### AhsayCBS（DFIR Radar／Huntress 摘要，原样）
- 投放：JSP webshell；XMRig 伪装 `edge.exe`；服务名语境 `MicrosoftEdgeUpdateSvc`
- 狩猎：`cbssvcX64.exe` 异常子进程（curl／certutil）；TEMP 中 `WinRing0x64.sys`、`Taskgmr.ps1`
- 补丁语境：10.3.4 争议；二次消息 hotfix **10.3.4.45**（伙伴门户，待厂商公告交叉）
- 文章：https://www.huntress.com/blog/ahsaycbs-flaws-exploit

### GhostAction（沿用）
- C2 IP：`193.32.204.199`
- 工作流文件名：`security-audit.yml`、`github_actions_security.yml`
- 文章：https://thehackernews.com/2026/10/credential-stealing-github-actions.html

### P7 DarkSword（沿用昨日＋blackorbird 续）
- 基础设施 IP：`43.134.165.205`、`166.88.95.90`、`23.148.212.237`、`47.102.192.23`、`156.239.230.120`
- 域名：`66ds.lol`、`agdx53.cc`、`cdn.gotoiphone.com`、`mzpo30.cam`
- 本机路径线索：`/private/var/tmp/keychain_c2_dump.json` 等
- 文章：https://www.iverify.com/blog/darksword-variant-threat-research

### PoeLLM（沿用 Black Lotus Labs）
- C2 IP／SHA256：见 https://github.com/blacklotuslabs/IOCs/blob/main/PoeLLM_IOCs.txt

### Longlegs／Warlock（沿用）
- 样本 SHA256：`206f27ae820783b7755bca89f83a0fe096dbb510018dd65b63fc80bd20c03261`、`ae9f7fce57c7b928e659dccf0e00fa79cd9cd61a106f18d4e03f92dc3a03c295`
- 文章：https://blog.polyswarm.io/china-linked-warlock-ransomware-campaign-targets-critical-infrastructure

### SonicWall SMA1000／Atlassian 21589／PaperCut／Citrix 107406
- 未见厂商发布的完整公开网络 IoC 清单；以补丁版本与日志狩猎为主。
- Flax Typhoon 扣押域名：以 FBI／DOJ／联合通告原文为准（本轮未整表抄录）。

### 其他
- AA26-281A／macOS Element／proxy08：见既有晚报
- 勒索受害者批量帖：未见公开可核验 IoC

## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/ （首页仍见 **RBNEWS618**，本窗口未见更新集）
- tl;dr sec 通讯：https://tldrsec.com/ （最新仍 **#349** — Vulns & Exploits in the AI Era…；未见 #350）
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form

本窗口 LWiS 交叉要点：@DFIR_Radar 周报／Ahsay／Dire Wolf／GoBalance／Flax／Azure DCR；@Dinosn PaperCut／Silent Ransom／Anthropic／Chromium typosquat／Eufy／Rust Actions；@watchtowrcyber 示意帖；@rad9800 Diaspore；@L0Psec 与 malwrhunterteam 互动；@vxunderground ATM「goop」；@pdiscoveryio Neo；@TrustedSec tabletop。

## 来源搜索 URL

- X A（relevancy）：`(CVE OR POC OR exploit OR 0day OR "zero-day") ("CVE-2026" OR RCE OR patch) -is:retweet` + 时间窗
- X A CVE：`CVE-2026 -is:retweet` + 时间窗
- X B：`github.com (C2 OR "red team" OR nuclei OR Sliver OR Cobalt OR emp3r0r) -is:retweet` + 时间窗
- X C：`("malware analysis" OR "threat report" OR "threat actor" OR ransomware) -is:retweet` + 时间窗
- X 定向：PaperCut／watchTowr；Citrix／NetScaler；Ahsay／AnyDesk／SonicWall／Atlassian；GhostAction／Longlegs／DarkSword／PoeLLM；emp3r0r／Sliver／nuclei
- X LWiS：`from:h1 OR from:h2 …`（约 4 批高价值）+ 时间窗
- KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA Citrix Alert：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway
- Risky：https://risky.biz/
- tl;dr：https://tldrsec.com/
