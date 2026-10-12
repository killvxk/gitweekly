# X 安全情报晚报 · 2026-10-06

> 搜集窗口：圣地亚哥时间 **2026-10-05 20:00 至 2026-10-06 ~20:30**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-10-06.json`＋`/workspace/tools-news-pulse-2026-10-06.json`＋`/workspace/enrich-2026-10-06/`＋`/workspace/_kev_buckets_2026-10-06.json`。CISA KEV catalogVersion **2026.10.04**／**1734** 条，**Δ0**（与昨日文件逐字节一致，连续第 2 天无更新；10-05／10-06 所有「CISA adds…」URL 均 404）。
> **due_today：无**；**newly_overdue：Zammad CVE-2026-102489／102490**；**upcoming：Citrix CVE-2026-88779 明天 10-07 到期**（未来 7 天仅此一条）；**仍逾期高信号 24 条**（昨 23＋Fortinet 104286）。
> X：`/workspace/x-posts-2026-10-06.json`（合并 **18** 条：A3／B4／C6／LWiS5；与 prior seen_ids 重叠 **1**（@LittleJoeTables sliver-gui 旧帖），**+17**）。**logged_in=true**／**@seogoogle4**／**blocked=false**。覆盖：A 约 **0.2h**（扫 47 留 3，POC/exploit 泛义噪声极高）；B 约 **75h**（扫 23，其中 24h 内约 6 条，留 4）；C 约 **2h**（扫 20 留 6，多为勒索受害者播报 bot）；LWiS 约 **43h**（扫 35 留 5）。时间与 status_url 取自时间线；t.co 已用 curl 展开。全程只读，未发帖／回复／点赞／转推／收藏／追踪。
> 抓取备注：Cisco RSS 仍 TLS 失败／WebFetch 500；Citrix 公告列表为 JS 空壳（改用搜索）；Google 威胁情报与 MSRC 博客 feed 返回 HTML 未能确认 24h 内容。
> 规则：每条含完整 https URL；分列 X 原帖／GitHub·PoC 仓库／厂商公告／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；泄露／入侵声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【KEV】今日无更新**：仍 2026.10.04／1734，Δ0，无 NEW；今日无到期项。
  KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **【upcoming · 明天到期 · Citrix CVE-2026-88779】** 厂商 CTX697174 无变化；Field Effect 等新报道强调 **9/27 修补版本（14.1-73.37／13.1-64.23）仍在受影响范围**，启用 SAML 者须再升级至 14.1-73.41／13.1-64.28。
  厂商：https://support.citrix.com/external/article/CTX697174
  文章：https://fieldeffect.com/blog/citrix-patches-another-exploited-netscaler-vulnerability
- **【newly_overdue · Zammad CVE-2026-102489／102490 · 新版 7.2.1】** Zammad 今日发布安全版本 7.2.1，同日 GitHub 出 27 条安全公告（2 critical／12 high）；但 **27 条均未提及这两个 KEV CVE**，不能据此认定已修复。
  厂商：https://zammad.com/en/product/releases/7-2-1
  GitHub 公告：https://github.com/zammad/zammad/security/advisories
- **【新 Critical · Atlassian CVE-2026-21589（未进 KEV）】** 多款 Data Center 产品未认证任意文件读取（CVSS4 9.3）；厂商称未见利用；watchTowr 今日发技术分析、Horizon3 加检测，利用门槛快速下降。
  厂商：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
- **【APT · Unit 42 Blinder Tunnel · 有 IoC · X 交叉】** 伊朗国家关联 CL-STA-1178 以伪造迪拜机场编程测试为饵攻击伊拉克关键基础设施，GitHub Issues 作 C2；X 上 @undercode_news 转述。
  厂商：https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/
  X 原帖：https://x.com/undercode_news/status/2107592303808286966
- **【Malware · Huntress Akira 勒索事件复盘 · 有 IoC】** RDP 入侵→停 Bitdefender→procdump→GOST 隧道→Rclone 外传→删卷影。
  厂商：https://www.huntress.com/blog/mapping-akira-ransomware-attack
- **【供应链 · npm @subql/common 5.8.3 后门（X）】** StepSecurity 发现，恶意代码在构建与发布之间注入。
  X 原帖：https://x.com/nineshoot/status/2107383233495359713
- **【工具】** 核心工具均无新版（Sliver v1.7.8／nuclei v3.11.1／nuclei-templates v10.5.0）；X 上 sliver-gui 继续被转、dreadnode 发布 ScopeBench、vx-underground GitHub 账号解封。
  sliver-gui：https://github.com/sliverarmory/sliver-gui
- **【其他】** CISA 今日 6 条 ICS 公告（lwIP SMTP、Hitachi Energy RTU500 等 CVSS 9.8）；Cisco 预告 10-07 发布 APIC／Finesse／Meraki／NX-OS 等公告；Pwn2Own Ireland 第一天结束。
  Cisco 预告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-fBn58ELx
- **【合并统计】** X **18**（A3／B4／C6／LWiS5；+17 NEW 帖＋1 附带 id；cross 1）；seen_ids **2352→2370**；Risky 仍 RBNEWS618、tl;dr 仍 #348；报告 `/home/box/workspace/security-watch/reports/2026-10-06-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【upcoming · due 10-07 · 在野】Citrix NetScaler ADC／Gateway CVE-2026-88779（SAML DoS）

CISA 10-04 加入 KEV，联邦 due **2026-10-07（明天）**。前提：配置为 SAML SP 或 IdP。修复版本：14.1-73.41／13.1-64.28／14.1-73.41 FIPS／13.1-37.282。CTX697174 与昨日一致（changelog 仍两条 10-03）；Beazley BSL-A1216 仍 Update 6；NVD Analyzed（10-05 最后修改）。今日新增第三方报道（Field Effect、CyberTechEdition、FirewallSync）一致指出：**9/27 为 88771／88772 打的补丁版本仍受 88779 影响**。防御：启用 SAML 的设备今晚／明天内升级；狩猎 nsaaad 反复崩溃与 `ns.log` 中 "unexpectedly died"。

地址：
- X 原帖：本窗口 X 未采到相关帖，不编造
- GitHub／PoC 仓库：未见公开 PoC 仓库
- 厂商 CTX697174：https://support.citrix.com/external/article/CTX697174
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88779
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-88779
- CISA Adds One（10-04）：https://www.cisa.gov/news-events/alerts/2026/10/04/cisa-adds-one-known-exploited-vulnerability-catalog
- 文章 Field Effect：https://fieldeffect.com/blog/citrix-patches-another-exploited-netscaler-vulnerability
- 文章 CyberTechEdition：https://cybertechedition.com/news/cisa-lists-netscaler-saml-flaw-cve-2026-88779-known-exploited/
- 文章 FirewallSync：https://firewallsync.com/posts/netscaler-cve-2026-88779-saml-denial-of-service-exploited-patched-last-weeks-zero-days/
- 文章 Beazley BSL-A1216：https://labs.beazley.security/advisories/BSL-A1216

IoC：未见公开 IoC（厂商与新报道均无）。

### 2. 【newly_overdue · 在野】Zammad CVE-2026-102489／102490（今日发布 7.2.1）

CISA 10-02 加入 KEV，联邦 due **10-05**，今日起逾期。**新：Zammad 10-06 发布 7.2.1**，GitHub 同日公开 27 条安全公告（2 critical、12 high、10 medium、3 low；均影响 ≤7.2.0、7.2.1 修复、无 CVE 编号；含模板 sanitizer RCE、MFA 绕过、跨组织工单接管、二阶 SQLi）。**27 条均未提及 102489／102490**，不能写成「7.2.1 修复 KEV 条目」。厂商仍称仅 ≤6.5 可利用；DIVD 称 102490 影响 1.5 至 7.1.0-alpha。社区帖（最后 10-01）、DIVD 页、NVD（10-03）无变化。防御：升级至 7.2.1（同时修掉 27 个新问题）；迁出 ≤6.5；限制本地提权面；按 BOD 26-04 取证。

地址：
- X 原帖：本窗口 X 未采到相关帖，不编造
- GitHub 安全公告列表：https://github.com/zammad/zammad/security/advisories
- 厂商 7.2.1 发布说明：https://zammad.com/en/product/releases/7-2-1
- 厂商社区声明：https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297
- DIVD 案件：https://csirt.divd.nl/cases/DIVD-2026-00015/
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-102489
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-102489
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-102490

IoC：未见公开 IoC。

### 3. 【新 Critical · 未进 KEV】Atlassian CVE-2026-21589（多产品未认证任意文件读取）

Atlassian 10-05 发布（窗口前夕），CVSS 4.0 9.3：Bitbucket、Confluence、Jira、Jira Service Management、Bamboo、Crowd Data Center 及 Crucible／Fisheye 可被未认证读取 Web 根目录文件。厂商称未发现利用。窗口内：watchTowr 10-06 14:01（UTC-3）发布技术分析，Horizon3 20:15（UTC-3）加入检测测试——公开细节已出，预计很快出现扫描。修复版本：Bitbucket 9.4.26／10.2.8／10.5.1；Confluence 9.2.26／10.2.19；Jira Software 9.12.40／10.3.26／11.3.12；JSM 5.12.40／10.3.26／11.3.12；Bamboo 10.2.24／12.1.12；Crowd 6.3.7／7.0.3／7.1.7／7.2.4；Crucible／Fisheye 4.9.15。防御：优先升级外网暴露实例；复现细节不转载。

地址：
- X 原帖：本窗口 X 未采到相关帖，不编造
- GitHub／PoC 仓库：未见（不编造）
- 厂商：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
- NVD（按 CVE 构造）：https://nvd.nist.gov/vuln/detail/CVE-2026-21589
- 文章 watchTowr：https://labs.watchtowr.com/you-wont-hear-about-these-even-in-myths-atlassian-jira-confluence-and-more-pre-auth-arbitrary-file-read-cve-2026-21589/
- 文章 Horizon3：https://horizon3.ai/attack-research/vulnerabilities/cve-2026-21589/

IoC：未见公开 IoC。

### 4. 【X · 已在 KEV】Oracle PeopleSoft CVE-2026-35273：ShinyHunters 用 URL 编码绕过 WAF

@jfernandogg 转述 Mandiant：ShinyHunters 以 URL 编码（`%50`）绕过 WAF 对 `/PSEMHUB` 路径的拦截。该 CVE 已于 2026-06-12 进 KEV（due 06-15，早已逾期）；NVD Analyzed，影响 PeopleTools 8.61／8.62。防御：WAF 规则须在解码后匹配；直接打补丁并限制 PSEMHUB 暴露。Mandiant 原文链接帖中未附，未核对。

地址：
- X 原帖：https://x.com/jfernandogg/status/2107609346226143509
- GitHub／PoC 仓库：未见
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-35273
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-35273

IoC：原帖路径 `/PSEMHUB`（狩猎路径，非攻击设施）；未见公开 IP／哈希。

### 5. 【X】WordPress Kirki 插件 CVE-2026-102173（CVSS 7.2，50 万+站点）

@mgn_jpn：需升级至 6.3.2。NVD API 暂查不到该 CVE（**未从厂商侧验证**）。卡片只取得域名 shindan.m-g-n.me，完整 URL 未取得。

地址：
- X 原帖：https://x.com/mgn_jpn/status/2107610355522281677
- GitHub／PoC 仓库：未见
- 文章：shindan.m-g-n.me（卡片，完整 URL 未取得，不编造）

IoC：未见公开 IoC。

### 6. 【X · 区块链】Onyx DAO 疑遭治理攻击（UNCONFIRMED）

@DiarioBitcoin 引 Blockaid：约 6.2 亿 XCN（约 291 万美元）从以太坊金库转出。

地址：
- X 原帖：https://x.com/DiarioBitcoin/status/2107609137068540083

IoC：帖中未给出地址或交易哈希，未见公开 IoC。

### 7. 【CISA ICS · 10-06 六条】

无 IoC，无 KEV 新增。
- Johnson Controls EasyIO FG（EOL 无补丁）：https://www.cisa.gov/news-events/ics-advisories/icsa-26-279-01
- lwIP SMTP 客户端（CVSS 9.8，补丁提交修复）：https://www.cisa.gov/news-events/ics-advisories/icsa-26-279-02
- Hitachi Energy Asset Suite（修复 9.9.1）：https://www.cisa.gov/news-events/ics-advisories/icsa-26-279-03
- Hitachi Energy SOI（含 KEV 中的 ActiveMQ CVE-2026-34197，修复 SOI EP2）：https://www.cisa.gov/news-events/ics-advisories/icsa-26-279-04
- Hitachi Energy REB500（修复 8.3.4.0）：https://www.cisa.gov/news-events/ics-advisories/icsa-26-279-05
- Hitachi Energy RTU500（CVSS 9.8，修复 12.7.8／13.9.1）：https://www.cisa.gov/news-events/ics-advisories/icsa-26-279-06

### 8. 【仍逾期高信号 24 条】

Fortinet **104286**（FG-IR-26-175 无变化，修复 FortiMail 8.0.2／7.6.7／7.4.9）、Citrix 88771／88772、Apple 86950、Check Point 85102／93616、Arista 93952、F5 94127、JFrog 42016／42018、Zyxel 7273、Microsoft 81963／85880／65660、Google 87491／85046／58704、Cisco 76460／76504（仍 rev 1.1）、Acronis 87886、WSO2 5430、Adobe 71362、MikroTik 67279、WordPress 87902。

地址：
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- Fortinet FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- Cisco cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU

### 9. 【其他厂商】

Cisco 预告 10-07 发布 APIC、Finesse、License On-Prem、Meraki、NX-OS/UCS 公告（https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-fBn58ELx）。MSRC 仅 2026-Jul CVE-2026-50387／54128 致谢信息修订，无带外公告（https://msrc.microsoft.com/update-guide）。Fortinet PSIRT、Palo Alto（仍 10-02 CVE-2026-0250）、Ivanti（最新 09-08）无新公告；Citrix 未搜到新公告。Pwn2Own Ireland 第一天结束（X @yves_bieri：https://x.com/yves_bieri/status/2107559235009613956）。

## 工具与 GitHub 发布

### 1. sliver-gui（Sliver C2 官方图形界面，持续转发）
- X 原帖：https://x.com/RustXML/status/2107366658721681689
- X 原帖（原始发布，早于窗口，已见）：https://x.com/LittleJoeTables/status/2106957831928963490
- GitHub：https://github.com/sliverarmory/sliver-gui
- 对照：Sliver 仍 v1.7.8 https://github.com/BishopFox/sliver/releases/tag/v1.7.8

### 2. agent-redteam-benchmark／sixi-scanner（AI agent 红队基准）
- X 原帖：https://x.com/sixi4ai/status/2107518001851597255
- GitHub：https://github.com/rbrus/agent-redteam-benchmark
- GitHub：https://github.com/rbrus/sixi-scanner

### 3. dreadnode ScopeBench（评估黑客 agent 是否越出授权范围）
- X 原帖：https://x.com/moo_hax/status/2107554132974538919
- GitHub／文章：帖中未取得外链（不编造）

### 4. ProjectDiscovery：低成本给开源模型植入后门的研究
不到 50 美元给 7B 开源模型植入后门，由 Codex 触发窃取凭据，称成功率 100%。防御向：本地模型来源校验。
- X 原帖：https://x.com/princechaddha/status/2107527299239498042
- 文章：帖中未取得外链

### 5. vx-underground GitHub 账号解封（恶意软件源码合集恢复）
- X 原帖：https://x.com/vxunderground/status/2107609627101987107

### 6. 其他
- Cutter（rizin 逆向工具，推荐帖，非新版）：X https://x.com/EsGeeks/status/2107600560484466759 ／ GitHub https://github.com/rizinorg/cutter
- Project-LION（自称 C2 注入器／间谍软件架构，**可信度低**，仅记录）：X https://x.com/lexs17/status/2107290404798316650 ／ GitHub https://github.com/lexs201992-gif/Project-LION-Manager-Provisioning-Enterprise
- 核心工具无新版：Sliver v1.7.8、nuclei v3.11.1（https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1）、nuclei-templates v10.5.0（https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.0）、Mythic v3.4.0.5、Impacket 0.13.1、NetExec v1.5.1；Havoc 无 release（最后 commit 2025-12-18）。

## APT / Malware 分析

### 1. 【Unit 42】Blinder Tunnel：伊朗国家关联 CL-STA-1178 攻击伊拉克关键基础设施
10-06 07:00（UTC-3）。以伪造迪拜机场编程测试为诱饵投递木马化 .csproj，随后 AppDomainManager 劫持＋DLL 侧载；载荷 ShelbyLoader V2、ShelbyC2 V2、Blackwood（Chisel 隧道封装）；以 GitHub API／Issues 作 C2。狩猎：开发者机器构建陌生 .csproj、下列 Run 键、到下列 GitHub 账号的 API 流量。
- X 原帖：https://x.com/undercode_news/status/2107592303808286966
- 文章（X 外链展开）：https://undercodenews.com/blinder-tunnel-campaign-iranian-linked-threat-actor-uses-fake-dubai-airports-tests-to-target-iraqi-critical-infrastructure-video/
- 厂商：https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/
- IoC JSON：`/workspace/enrich-2026-10-06/unit42-blinder-tunnel-iocs.json`
- IoC：见汇总

### 2. 【Huntress】Akira 勒索攻击全程复盘
作者 Harlan Carvey、Lindsey O'Donnell-Welch，10-06 10:00（UTC-3）。RDP 入侵→停用 Bitdefender 服务→procdump→GOST 隧道→Rclone 外传→删除卷影副本。
- X 原帖：本窗口未采到
- 厂商：https://www.huntress.com/blog/mapping-akira-ransomware-attack
- IoC JSON：`/workspace/enrich-2026-10-06/huntress-akira-iocs.json`
- IoC：见汇总

### 3. 【供应链】npm @subql/common 5.8.3 被植入后门（StepSecurity，经 X）
从建分支到发布仅 33 分钟，恶意代码在构建与发布之间注入。防御：锁定版本、检查是否安装过 5.8.3。StepSecurity 原文帖中未附链接，未核对。
- X 原帖：https://x.com/nineshoot/status/2107383233495359713
- 包页（按包名构造）：https://www.npmjs.com/package/@subql/common
- IoC：npm 包 `@subql/common@5.8.3`

### 4. 其他（声称类，UNCONFIRMED）
- Trump Mobile 泄露：第三方员工感染 infostealer、无 MFA，3,615 条暴露（**未验证**）：https://x.com/ndgmlondon/status/2107592840654082275
- SORB 兜售土耳其 200 万+学生家长 PII（**UNCONFIRMED**）：https://x.com/VECERTRadar/status/2107606452059709910
- LockBit5 声称攻击阿根廷 avsa.com.ar（另德国 grunenwald.com，https://x.com/ThreatAtlas/status/2107608282353271238）：https://x.com/ThreatAtlas/status/2107608354830893487
- UmBra 勒索声称攻击埃及 Beni Suef 技术大学：https://x.com/FalconFeedsio/status/2107585196539478032

## 地址／IoC 汇总

**Unit 42 Blinder Tunnel（厂商原样，defang 保留）**
- SHA256：
  - `6e7d9b33f1e72ea1ede71373a604ecdb060dab7d42055179c1eede9ecd1fd239`
  - `f5b12772db6817f7a765a6fe7565fd3d4f87edc28e42fe3ec0244a372a410fc9`
  - `53f35e49eb9b271fd8cbcd3daacb525328dbf159a03dbd1c7adebe0363daa402`
  - `3fd810a3aa0039993393741b32287c367a9a5037a41e826906440887cdd3ed13`
  - `76273382e4252c1f60a2251141e108942494409c759358320735891762c0682e`
  - `d3561bd4aad003dc3e08157b0891860bb496b80cd6e44901692e08ab1d4e8260`
  - `f5ba1645694c62f527ed6ceda8c68a5c3dd92b4032439167e8e937e72803b4bd`
  - `7cc571aca6d8715d9aaad3d83e1bcd30467565d583db1dfe73697c5d00a1f875`
- IP：`91.107.156[.]29`／`87.248.129[.]239`／`65.109.214[.]145`／`38.180.136[.]127`
- 钓鱼域名：`cloud.g-drive[.]cam`／`googeldrive[.]cam`／`drivegoogel[.]cam`／`googelmeet[.]online`／`meetonline[.]cam`／`asdfafadafg[.]online`
- 注册表：`HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\MicrosoftRuntime`
- GitHub C2：`hxxps[:]//github[.]com/peakyblinders-tm`／`hxxps[:]//github[.]com/GreenBeret0`

**Huntress Akira（厂商原样）**
- 攻击者主机名：`C1IFRYXI`
- GOST 隧道 C2：`64.227.4[.]134`
- `C:\storage\win.exe` SHA256 `1f1bb322591b6d27fd2946e373d7d2efc2f4e1e66818846060d391600b600fba`（勒索程序）
- `C:\PerfLogs\temp\svchost.exe` SHA256 `d00833318a04caa019c6f95dcb3598ad947d405010bfb2f3cbd04530a00bc3a4`（GOST）

**Fortinet FG-IR-26-175（CVE-2026-104286，与昨日相同）**
- IP：`79.141.169.187`／`45.129.0.192`；7 个文件哈希见 2026-10-05 报告与 `/workspace/enrich-2026-10-06/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`

**X 帖中出现的指标**
- @nineshoot：npm 包 `@subql/common@5.8.3`（https://x.com/nineshoot/status/2107383233495359713）
- @jfernandogg：狩猎路径 `/PSEMHUB`（URL 编码 `%50` 绕过）（https://x.com/jfernandogg/status/2107609346226143509）
- 勒索受害方域名（非攻击设施）：`avsa.com[.]ar`、`grunenwald[.]com`、`btu.edu[.]eg`

**其余条目**：Citrix 88779、Zammad 102489／102490（含 7.2.1 公告）、Atlassian 21589、Kirki 102173、Onyx DAO、CISA ICS、各工具——**未见公开 IoC**。

## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/ （仍 RBNEWS618／SRB185／BTN184；RBNEWS619／620、SRB186／187、BTN185／186 均 404）
- tl;dr sec 通讯：https://tldrsec.com/ （仍 #348 https://tldrsec.com/p/tldr-sec-348）
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form

本日 LWiS List 抽取 5 条（约 43h 覆盖，多为闲聊）：vx-underground 解封、ProjectDiscovery 模型后门研究、dreadnode ScopeBench、Pwn2Own Ireland 第一天、sliver-gui（旧帖）。博客清单交叉：Unit 42、Huntress、watchTowr 当日有新文（已入正文）；SentinelLabs、Talos、Trend Micro、Elastic、DoublePulsar 无新文。

## 来源搜索 URL

- X Search A（Latest）：https://x.com/search?q=(CVE%20OR%20POC%20OR%20exploit%20OR%200day)&f=live
- X Search B（Latest）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- X Search C（Latest）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA ICS 公告：https://www.cisa.gov/news-events/ics-advisories
- NVD API：https://services.nvd.nist.gov/rest/json/cves/2.0
- Fortinet PSIRT RSS：https://filestore.fortinet.com/fortiguard/rss/ir.xml
- MSRC 更新指南：https://msrc.microsoft.com/update-guide
- Cisco 安全公告：https://sec.cloudapps.cisco.com/security/center/publicationListing.x
- Atlassian 安全公告：https://confluence.atlassian.com/security
- GitHub releases：https://github.com/BishopFox/sliver/releases ／ https://github.com/projectdiscovery/nuclei/releases ／ https://github.com/projectdiscovery/nuclei-templates/releases
