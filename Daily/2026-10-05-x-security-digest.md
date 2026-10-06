# X 安全情报晚报 · 2026-10-05

> 搜集窗口：圣地亚哥时间 **2026-10-04 20:00 至 2026-10-05 ~20:25**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-10-05.json`（collected_at 约 **2026-10-05T20:24-03:00**）＋ `/workspace/tools-news-pulse-2026-10-05.json`＋ `/workspace/enrich-2026-10-05/`＋ buckets `/workspace/_kev_buckets_2026-10-05.json`。CISA KEV catalogVersion **2026.10.04**／**1734** 条（相对昨日 **Δ0**，文件与昨日快照逐字节一致；无 NEW／removed／字段变化）。CISA 10-05 的 Adds 页 6 种命名均 404。
> **due_today：Zammad CVE-2026-102489／102490**；**newly_overdue：Fortinet CVE-2026-104286**（厂商今日已发布修复版本）；**upcoming：Citrix CVE-2026-88779 due 10-07**（未来 7 天仅此一条）；**仍逾期高信号 23 条**（昨 22＋Cisco 76504；全库 dueDate 早于 10-05 共 1731 条）。
> X：`/workspace/x-posts-2026-10-05.json`（合并 **20** 条：A4／B4／C4／LWiS8；唯一数字 id **20**，全部带 `status_url`；与 prior seen_ids 重叠 **0**，**+20**；其中 @volker_simonis 一条 C2 指 JVM 编译器，低相关未入正文）。**logged_in=true**／**@seogoogle4**／**blocked=false**——昨晚卡住的 B／C 今晚均正常加载。覆盖：A 约 **0.2h**（扫 40 留 4，exploit/POC 语义噪声极高）；B **24h**（扫 21 留 4）；C 约 **2.8h**（扫 30 留 4）；LWiS 约 **5h**（扫 43 留 8）。只有 B 覆盖满 24h，其余受 Latest 窗口限制。全程只读，未发帖／回复／点赞／转推／收藏／追踪。
> 抓取备注：Cisco RSS（box TLS 失败、WebFetch 500）、Cisco CSAF 403；Citrix 社区博客 Cloudflare 拦截；Citrix 公告列表与 Ivanti 页为 JS 空壳；Sophos 文章 curl 超时／WebFetch 500；NVD 网页 301，改用 NVD API。**Cisco／Ivanti／Citrix 近 24h 有无新公告未能确认。**
> 规则：每条含完整 https URL；分列 X 原帖／GitHub·PoC 仓库／厂商公告／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；泄露／入侵声称／未证实传闻一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【KEV】今日无更新**：仍 2026.10.04／1734，Δ0，无 NEW。
  KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **【newly_overdue · Fortinet CVE-2026-104286 · 修复已发布】** FG-IR-26-175 于 10-05 做 Solution update：FortiMail **8.0.2／7.6.7／7.4.9 已发布**（之前标 upcoming）；7.2 迁移至 7.4+。联邦 due 10-04 已过。厂商 IoC 未变（2 IP＋7 文件哈希）。
  厂商：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- **【due_today · Zammad CVE-2026-102489／102490】** 厂商信息无变化：102489 仅 ≤6.5 可利用，建议 7.2.0；102490 仍待 DIVD 细节、无专门修复。**未见公开 IoC。**
  厂商社区：https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297
- **【upcoming · Citrix CVE-2026-88779 due 10-07】** NVD 由 Received 变为 Analyzed（NVD CVSS3.1 7.5；Citrix CVSS4 8.7）。SecurityWeek：watchTowr 复现后确认仅 DoS；Kevin Beaumont（"PitScaler 2"）称已打补丁的蜜罐也见利用尝试，其中一台运行了下载的恶意程序。加拿大 CCCS 发 AV26-996。X 上 @0x5 亦发帖提醒。
  SecurityWeek：https://www.securityweek.com/exploitation-of-citrix-netscaler-zero-day-hits-appliances-patched-days-earlier/
  X 原帖：https://x.com/0x5/status/2107245699481956534
- **【APT／Malware · ClingSTUN Linux 后门 · 有 IoC】** FortiGuard 10-05 新文：未归因攻击者利用 30 多个已知 IoT／边缘设备漏洞（含 Ivanti CVE-2023-46805／CVE-2024-21887、TP-Link CVE-2023-1389）植入回连代理后门，滥用公共 STUN 服务器做 NAT 穿透。IoC：3 IP＋22 行 SHA256。
  厂商：https://www.fortinet.com/blog/threat-research/clingstun-linux-backdoor-abuses-public-stun-infrastructure
- **【APT／Malware · RATHat 移动木马】** Cleafy 与 Zimperium 分析 RATHat 的 C2 面板演变（X @arpsyndicate）。
  X 原帖：https://x.com/arpsyndicate/status/2107073558442889571
- **【APT · TA419 AitM 钓鱼（经 X 转述）】** @hCharizard_ 转述 Proofpoint 报告：TA419 针对美国 AI 政策专家做 AitM 钓鱼（原文链接为二层短链，未展开确认）。
  X 原帖：https://x.com/hCharizard_/status/2107245518506328153
- **【工具】** nuclei-templates **v10.4.9→v10.5.0**（295 新模板、36 个 CVE，含仍逾期 KEV WordPress 87902、JFrog 42018 的检测模板）；X 上新出现 BOFKatz、sliver-gui、ClaudeHopper。Sliver v1.7.8／nuclei v3.11.1 无变化。
  nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.0
- **【新闻】** Risky Business 仍 RBNEWS618／SRB185／BTN184；tl;dr sec 仍 #348。ZDI 公布 Pwn2Own Ireland 2026 完整赛程（Pixel 10／Galaxy S26 报名多）。
  ZDI：https://www.zerodayinitiative.com/blog/2026/10/5/pwn2own-ireland-2026-the-full-schedule#day-one
- **【合并统计】** X **20**（A4／B4／C4／LWiS8；+20 NEW 数字 id；cross 0）；`logged_in=true`／`@seogoogle4`／`blocked=false`；seen_ids **2332→2352**；报告 `/home/box/workspace/security-watch/reports/2026-10-05-x-security-digest.md`

## CVE / POC / 漏洞

### 1. 【newly_overdue · 在野】Fortinet FortiMail CVE-2026-104286（修复版本已发布）

CISA 于 2026-10-01 加入 KEV；联邦 due **2026-10-04**，今日起逾期。路径遍历＋NULL 字节处理不当 → 未认证任意文件写入（CVSS3 9.8）。**10-05 FG-IR-26-175 Solution update：FortiMail 8.0.2／7.6.7／7.4.9 已发布**；7.2 迁移到 7.4 以上。IoC 段与昨日 diff 无变化。防御：立即升级；未能升级前按公告禁用 IBE、限制 webmail／管理面暴露；比对下列 IoC；按 BOD 26-04 取证。**不转载利用步骤。**

地址：
- X 原帖：本窗口 X 未采到相关帖，不编造
- GitHub／PoC 仓库：未见公开 PoC 仓库
- 厂商 FG-IR-26-175：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- 厂商 PSIRT RSS：https://filestore.fortinet.com/fortiguard/rss/ir.xml
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-104286
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-104286
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- enrich IoC JSON：`/workspace/enrich-2026-10-05/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`

IoC（厂商 FG-IR-26-175 原样，见「地址／IoC 汇总」）。

### 2. 【due_today · 在野】Zammad CVE-2026-102489／CVE-2026-102490

CISA 于 2026-10-02 加入 KEV；联邦 due **2026-10-05＝今日**。102489：会话固定 → 以 zammad 用户 RCE，可与 102490 链式利用；厂商称仅 ≤6.5（EOS）可利用，7.2.0 已加固。102490：不当权限管理 → 本地 zammad→root；厂商仍未收到 DIVD 技术细节，无专门修复版本。社区帖、releases 页（最新 7.2，09-23）、GitHub 安全公告、DIVD 案件均无新变化。防御：升级或迁出 ≤6.5；限制本地提权面；按 BOD 26-04 取证。

地址：
- X 原帖：本窗口 X 未采到相关帖，不编造
- GitHub／PoC 仓库：未见
- 厂商社区声明：https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297
- 厂商 releases：https://zammad.com/en/product/releases/
- DIVD 案件：https://csirt.divd.nl/cases/DIVD-2026-00015/
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-102489
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-102489
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-102490

IoC：未见公开 IoC。

### 3. 【upcoming · due 10-07 · 在野】Citrix NetScaler ADC／Gateway CVE-2026-88779（SAML DoS）

CISA 于 2026-10-04 加入 KEV；due **2026-10-07**（剩 2 天）。前提：配置为 SAML SP 或 SAML IdP。修复：14.1-73.41／13.1-64.28／14.1-73.41 FIPS／13.1-37.282。CTX697174 文本与昨日一致；**NVD 今日 Analyzed**（NVD CVSS3.1 7.5）。新第三方报道：SecurityWeek 引 watchTowr 复现确认仅 DoS；Kevin Beaumont 称已打 9/27 补丁的蜜罐上也见利用尝试，其中一台运行了下载来的恶意程序（**未独立验证**）。Beazley BSL-A1216 今日未更新（仍 Update 6）。X：@0x5 发 X Article 提醒（无外链）；@Huntbackio 蜜罐称观测到 NetScaler SAML 批量利用尝试（见第 5 条）。防御：已于 9/27 修补 88771／88772 但启用 SAML 者须再次升级；狩猎 nsaaad 反复崩溃、`ns.log` 中 "unexpectedly died"。

地址：
- X 原帖：https://x.com/0x5/status/2107245699481956534
- X 原帖（蜜罐观测）：https://x.com/Huntbackio/status/2107248332863086975
- GitHub／PoC 仓库：未见公开 PoC 仓库
- 厂商 CTX697174：https://support.citrix.com/external/article/CTX697174
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88779
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-88779
- CISA Adds One（10-04）：https://www.cisa.gov/news-events/alerts/2026/10/04/cisa-adds-one-known-exploited-vulnerability-catalog
- 加拿大 CCCS AV26-996：https://www.cyber.gc.ca/en/alerts-advisories/citrix-security-advisory-av26-996
- 文章 SecurityWeek：https://www.securityweek.com/exploitation-of-citrix-netscaler-zero-day-hits-appliances-patched-days-earlier/
- 文章 CSO：https://www.csoonline.com/article/4230642/citrix-warns-of-actively-exploited-netscaler-flaw-days-after-zero-day-patch-rush.html
- 文章 Sophos（原文未抓到，仅搜索摘要）：https://www.sophos.com/en-us/blog/citrix-netscaler-vulnerability-cve-2026-88779-in-active-exploitation
- 文章 Beazley BSL-A1216：https://labs.beazley.security/advisories/BSL-A1216

IoC：厂商未见公开 IoC。Beazley 战役级 IoC（主要对应 88771／88772）今日未更新，见 2026-10-04 报告及链接。

### 4. 【X · 未进 KEV】Microsoft Exchange CVE-2026-96940（权限提升，CVSS 8.8）

@__kokumoto 转 The Hacker News：经认证攻击者可读取其他用户邮箱。X 卡片完整 URL 未能取得；MSRC 近 24h 无新月度文档或带外公告，**本报未从厂商侧确认细节（未验证）**。

地址：
- X 原帖：https://x.com/__kokumoto/status/2107248610379440464
- GitHub／PoC 仓库：未见
- 厂商（MSRC 条目页，按 CVE 构造，未逐页核对）：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-96940
- NVD（按 CVE 构造）：https://nvd.nist.gov/vuln/detail/CVE-2026-96940
- 文章：The Hacker News（卡片，完整 URL 未取得）

IoC：未见公开 IoC。

### 5. 【X · 蜜罐观测】批量利用多个老旧与新近漏洞

@Huntbackio 蜜罐观察到批量利用 CVE-2017-9841（PHPUnit）、CVE-2023-46747（F5 BIG-IP）、CVE-2021-42013（Apache）、NetScaler SAML 与 PHP-CGI。防御：确认上述资产已修补，WAF／日志中狩猎下列 UA。

地址：
- X 原帖：https://x.com/Huntbackio/status/2107248332863086975
- GitHub／PoC 仓库：未见
- 厂商：未附

IoC（原帖原样）：UA `libredtail-http`

### 6. 【X · PoC 传闻】Apple CoreGraphics PoC

@LifeboatHQ 称出现 Apple CoreGraphics PoC，WhatsApp 的 PDF 预览检查可能是投递路径。卡片仅拿到域名 lifeboat.com，**未验证**，CVE 编号未给出。

地址：
- X 原帖：https://x.com/LifeboatHQ/status/2107248610903568815
- GitHub／PoC 仓库：未见（不编造）
- 文章：lifeboat.com（卡片，完整 URL 未取得）

IoC：未见公开 IoC。

### 7. 【LWiS · 复现】LibreOffice Calc RCE CVE-2026-63277

@pruvadev 发布复现记录 REPRO-2026-00374。非 KEV。防御：升级 LibreOffice，谨慎打开外部表格。**不转载复现步骤。**

地址：
- X 原帖：https://x.com/pruvadev/status/2107182001862168765
- 文章：https://www.pruva.dev/reproductions/REPRO-2026-00374
- NVD（按 CVE 构造）：https://nvd.nist.gov/vuln/detail/CVE-2026-63277

IoC：未见公开 IoC。

### 8. 【仍逾期高信号 23 条】

Citrix 88771／88772、Apple 86950、Check Point 85102／93616、Arista 93952、F5 94127、JFrog 42016／42018、Zyxel 7273、Microsoft 81963／85880／65660、Google 87491／85046／58704、Cisco 76460／**76504**（rev 1.1 无新修订）、Acronis 87886、WSO2 5430、Adobe 71362、MikroTik 67279、WordPress 87902。防御：补丁落地＋BOD 26-04 取证；nuclei-templates v10.5.0 已含 WordPress 87902、JFrog 42018 检测模板。

地址：
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- Cisco cisco-sa-sdwan-webauth：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU
- CISA Citrix zero-day：https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway

### 9. 【其他厂商】

Palo Alto 最新仍 10-02 CVE-2026-0250（MEDIUM）；CISA ICS 最新仍 10-01 ICSA-26-274；MSRC 只有历史文档修订时间戳。Cisco／Ivanti／Citrix 列表抓取失败，近 24h 有无新公告未能确认。

## 工具与 GitHub 发布

### 1. nuclei-templates v10.5.0（升版）
10-05 04:27（UTC-3）发布：295 个新模板、36 个 CVE，含 KEV 条目 WordPress CVE-2026-87902、JFrog CVE-2026-42018，以及 Ivanti EPMM CVE-2026-1340、N-able N-central CVE-2026-86218 等。
- X 原帖：本窗口未采到
- GitHub：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.0

### 2. BOFKatz（mimikatz 的 BOF 实现）
防御：关注 Beacon 内存内凭据读取（LSASS 访问）检测。
- X 原帖：https://x.com/ipurple/status/2107197416164540623
- GitHub：https://github.com/KrakenEU/BOFKatz

### 3. sliver-gui（Sliver C2 图形界面）
- X 原帖：https://x.com/LittleJoeTables/status/2106957831928963490
- GitHub：https://github.com/sliverarmory/sliver-gui
- 对照：Sliver 仍 v1.7.8 https://github.com/BishopFox/sliver/releases/tag/v1.7.8

### 4. ClaudeHopper（Claude 代理拦截工具）
- X 原帖：https://x.com/3ndG4me_/status/2107200167191462286
- GitHub：https://github.com/3ndG4me/ClaudeHopper

### 5. Console Named Pipe 进程注入检测实验
@ipurple 介绍新进程注入技术的检测实验；PoC 在引用帖串中，外链未展开，**不转载**。
- X 原帖：https://x.com/ipurple/status/2107213485511966859
- GitHub：未展开（不编造）

### 6. Android 投影仪预装 C2／RAT 研究仓库
- X 原帖：https://x.com/rst_cloud/status/2107117808769257601
- GitHub：https://github.com/Kavan00/Android-Projector-C2-Malware

### 7. 其他
- CMTrace Open v1.6.2（日志查看工具）：X https://x.com/AdamGell/status/2107199344743252306 ／ GitHub https://github.com/adamgell/cmtraceopen/releases/tag/v1.6.2
- Red-Team-Roadmap（30 模块学习路线）：X https://x.com/httpschuks/status/2107043980475076910 ／ GitHub https://github.com/Dev-Chukwuma/Red-Team-Roadmap
- Chainguard forkstore（禁运期修复存放）：X https://x.com/chainguard_dev/status/2107198974650372572 ／ 厂商 https://www.chainguard.dev/unchained/this-shit-is-hard-building-forkstore
- 核心工具：Sliver v1.7.8、nuclei v3.11.1 无变化（https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1）；Mythic、Impacket、NetExec 近 24h 无新 release；Havoc 无 GitHub release；Cobalt Strike 博客首条 4.13 无日期，未算作新发版。

## APT / Malware 分析

### 1. 【FortiGuard】ClingSTUN Linux 后门滥用公共 STUN 基础设施
作者 Vincent Li（FortiGuard Labs），10-05 10:00（UTC-3）。未归因。利用 30 多个已知未修补 IoT／边缘设备漏洞（含 CVE-2014-8361、CVE-2021-35394、CVE-2023-1389、CVE-2023-46805、CVE-2024-21887、CVE-2024-3721、CVE-2026-87827 等）落地，三阶段分别从 3 个下载源投递，滥用公共 STUN 服务器做 NAT 穿透与保活，把设备变成远控代理节点。注意：被滥用的公共 STUN 服务器本身不应判为攻击者基础设施。狩猎：边缘／IoT 设备到下列 IP 的下载、异常 UDP 3478 STUN 保活、看门狗篡改；修补或下线 EOL 设备。
- X 原帖：本窗口未采到
- 厂商：https://www.fortinet.com/blog/threat-research/clingstun-linux-backdoor-abuses-public-stun-infrastructure
- IoC JSON：`/workspace/enrich-2026-10-05/fortinet-clingstun-iocs.json`
- IoC：见汇总（3 IP＋22 行 SHA256）

### 2. RATHat 移动木马（C2 面板演变）
- X 原帖：https://x.com/arpsyndicate/status/2107073558442889571
- GitHub：https://github.com/ARPSyndicate/encryptlayer-intelligence
- 厂商 Cleafy：https://www.cleafy.com/cleafy-labs/from-blackcat-to-panda-workshop-inside-the-evolving-c2-panel-behind-rathat
- 厂商 Zimperium：https://zimperium.com/blog/rathat-ai-powered-mobile-threat-is-here-for-your-credentials-bank-accounts
- 其他：https://encryptlayer.net
- IoC：X 帖未见公开 IoC（厂商原文未逐条抄录）

### 3. TA419 针对美国 AI 政策专家的 AitM 钓鱼（Proofpoint，经 X 转述）
- X 原帖：https://x.com/hCharizard_/status/2107245518506328153
- 文章：二层短链 https://reurl.cc/6Xx4Ak（未展开，未确认指向 Proofpoint 原文）
- IoC：未见公开 IoC

### 4. 其他（多为声称，UNCONFIRMED）
- 亚洲周度威胁情报报告（X Article，无外链）：https://x.com/Team_D4rkn3ttz/status/2107237093298827487
- Trump Mobile 据称遭 infostealer 入侵（**UNCONFIRMED／未验证**）：https://x.com/IntCyberDigest/status/2107235125167874085
- IFAPME 约 70 万条记录据称泄露（**UNCONFIRMED／未验证**）：https://x.com/DailyDarkWeb/status/2107219638840885445 ；IoC：`ifapme[.]be`（受害方域名，非攻击设施）
- Pwn2Own Ireland 2026 赛程：X https://x.com/l33d0hyun/status/2107174661209595999 ／ ZDI https://www.zerodayinitiative.com/blog/2026/10/5/pwn2own-ireland-2026-the-full-schedule#day-one

## 地址／IoC 汇总

**Fortinet FG-IR-26-175（CVE-2026-104286，厂商原样）**
- IP：`79.141.169.187`／`45.129.0.192`
- `/data/lib/liblog.so` ADDED MD5 `64c90a00c7fda4d5c7973ed64c25783a` SHA256 `8015f34dc84922b03688399d7f9fe7a00361789f7e420c7e2a2cdb23e75cef84`
- `/bin/smit` MODIFIED MD5 `5241738a3e9988404239e12243f6d35b` SHA256 `77324ac428bde86d351fc5fc06f6d64a6bfe737dfb2743df1d4c5ac2418a5b6a`
- `/data/bin/webconsole` ADDED MD5 `ae0ea6502d3fa5f0664bceb73189eb54` SHA256 `7a6cea9f5c9e2e9994d4e3c4da73f86cf5acd05ea5d312c066c9d1dafd69ee38`
- `/data/bin/mailservice` ADDED MD5 `f90fa81a5f521d785f2b2f765e3ab897` SHA256 `4000276a150a165d3c2537d1e19fb393c4de8333076a16655e28059cae82157b`
- `/data/etc/httpd.conf` MODIFIED MD5 `61af1c4bce1c2eebc8ff689ca5337791` SHA256 `703e97c64e61e41dc3aaba580d82bb2aa7b6a11b54ee6fb467ed5d5a3bffdef5`
- `/data/etc/ld.so.preload` ADDED MD5 `8eb64f25d2a8e18e05aae058629473cf` SHA256 `8953ec7960b09f544a880b072ad4e6cfda7a8303f486251d3478dcfdfbac23b6`
- `/data/migadmin.tar.gz` MODIFIED MD5 `49a7156a7d043cc8f9f680579db22f86` SHA256 `d6fe51c22b91776f4c961ea58bcac5917f15d560a619d7ce726d3d51795609d3`

**FortiGuard ClingSTUN（厂商原样，defang 保留；9391c6ad…8068 原文重复两次）**
- IP：`124[.]163[.]212[.]119`／`222[.]223[.]152[.]97`／`118[.]145[.]196[.]225`
- SHA256：
  - `dc892f5013edb0aa1e61e808511387373d8d120348b5be0929621d21e6e9946a`
  - `a297eddfa7abea8d411afc0f150f8f6f30e470a77204de87e3b0815fa9bb8a84`
  - `4fbd61cb9181ebbc4fe9a6e59d3c346dc00001da48d66bd890556fc6fad22b07`
  - `121f2050e3c891b29565fd73451fff7ae60199c86eb8d79ec1eb1d9844578487`
  - `48f9b72ce72ab7087794650d6eef10135345088384fbde1482f1c74a02b80302`
  - `e6e113783356446aef66e5296db45b244f318292af7cebc2a9bd76f095a95c4c`
  - `c1d8e2829ea63b9dc1cf2c3421a5093406adad4d6622e238376e78e908e0e6e8`
  - `48962b3893f2c8261e32e6b95ea7d463d145a529a8b2a6c987dd979454405c73`
  - `76692a23abe718b93e63edefd743971ec627c0cdf3778f856bd5ec88003deaa2`
  - `ec199c78c11040fd3127887222fd75a85e5797bf96aa691a117fdd83dd663d81`
  - `c0d8ffebfba969b1c1ca76bd9623bb623e9f95155c8ceca77d8fcc521435a497`
  - `f49f45303cbfccee14ff193ac9608f860e6d616f08c0ecbef1ec44f7c863d7ec`
  - `9391c6ad17aced1142607c0c623b18d86a7697cc483d204ffac94093e26b8068`
  - `9391c6ad17aced1142607c0c623b18d86a7697cc483d204ffac94093e26b8068`
  - `e4d12208789f36efc5a1ff765088fed95d6bb5972d1a804a4536fd42366797d4`
  - `284e5ec8748f99fd1b8c331b699a5fe5fd4448bbaae0347a940f427f931c4d14`
  - `6581bf37184bb2db899b9893064d39dd314ea691adf3281cc0aa7e0a31e5138a`
  - `10d83c1748895361e07320f68d44d427b43cadd2cbffe0ab5e607ab03aec83da`
  - `2ed54e0f988a62039abed88f6394eb1e3d5ed931f0183556055417fb08844ecf`
  - `b90640b392827b4f2d280f6cf67860862953331917d42df23e1653a92f2f98ad`
  - `dfba6008a2c828a9cb62342aec53006ae05a60cb8d4c41c3fa216fd727e8c6a3`
  - `5c4e263546fb21f8fe8732789a5b6583eaa8ae11ebeef099462a7c9bf50e022d`

**X 帖中出现的指标**
- @Huntbackio 蜜罐：UA `libredtail-http`（https://x.com/Huntbackio/status/2107248332863086975）
- @DailyDarkWeb：`ifapme[.]be`（受害方域名，非攻击设施；https://x.com/DailyDarkWeb/status/2107219638840885445）

**其余条目**：Zammad 102489／102490、Citrix 88779（厂商）、Exchange 96940、Apple CoreGraphics、LibreOffice 63277、TA419、RATHat（X 帖层面）、各工具发布——**未见公开 IoC**。Cisco 76504 仅日志狩猎指引（见 2026-10-04 报告）。

## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/ （仍 RBNEWS618／SRB185／BTN184；RBNEWS619／620、SRB186、BTN185 均 404）
- tl;dr sec 通讯：https://tldrsec.com/ （仍 #348；#349／#350 为 soft-404）
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form

本日 LWiS List 抽取 8 条（约 5h 覆盖）：sliver-gui、BOFKatz、Console Named Pipe 注入检测、ClaudeHopper、LibreOffice CVE-2026-63277 复现、Chainguard forkstore、Pwn2Own Ireland 2026 赛程、CMTrace Open v1.6.2。

## 来源搜索 URL

- X Search A（Latest）：https://x.com/search?q=(CVE%20OR%20POC%20OR%20exploit%20OR%200day)&f=live
- X Search B（Latest）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- X Search C（Latest）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 网络安全公告列表：https://www.cisa.gov/news-events/cybersecurity-advisories
- NVD API：https://services.nvd.nist.gov/rest/json/cves/2.0
- Fortinet PSIRT RSS：https://filestore.fortinet.com/fortiguard/rss/ir.xml
- FortiGuard 威胁研究 feed：https://feeds.fortinet.com/fortinet/blog/threat-research
- MSRC 更新指南：https://msrc.microsoft.com/update-guide
- Cisco 安全公告：https://sec.cloudapps.cisco.com/security/center/publicationListing.x
- GitHub releases：https://github.com/BishopFox/sliver/releases ／ https://github.com/projectdiscovery/nuclei/releases ／ https://github.com/projectdiscovery/nuclei-templates/releases
