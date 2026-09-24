# X 安全情报晚报 · 2026-09-16

> 搜集窗口：圣地亚哥时间 **2026-09-15 20:00 至 2026-09-16 ~20:30**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周三）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-16.json`（collected_at **2026-09-16T20:13:11-03:00**）＋ `/workspace/tools-news-pulse-2026-09-16.json`＋ `/workspace/enrich-2026-09-16/`。CISA KEV catalogVersion **2026.09.16**／**1713** 条／dateReleased **2026-09-16T18:47:50.6796Z**（相对昨日 **2026.09.14／1710／+3**）。
> **NEW KEV（dateAdded 2026-09-16，due 09-19）**：**CVE-2026-58704** Google Pixel／**CVE-2026-76460** Cisco ISE／**CVE-2026-87886** Acronis Backup。
> **期限今日 09-16**：**LiteLLM CVE-2026-59822**／**Starlette CVE-2026-48710**。**期限明日 09-17**：**Cisco ESA CVE-2026-76461**。**新起逾期（due 曾为 09-15）**：无。仍逾期：ScreenConnect **84869**／GitLab **85706**／PaperCut **81578／82078**／MikroTik **67277／86060**／Citrix **19490**／Fortinet **25249**／Cisco FMC **20079**／Magento **75650**／N-able **86218**。
> **NEW ICS**：ICSA-26-258-**04..08**（Schneider SCADAPack x70／Siemens Reyrolle 7SR5／Mendix SAML／Teamcenter／CareCam CM2507）；昨日已报 01..03 仍列。
> X：`/workspace/x-posts-2026-09-16.json`（合并 **67** 条唯一：A26／B8／C21／LWiS12；**0** 重叠；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.15h**（远不足 24h；大量 @CVEnew 低信号洪水）。Search B 约 **27.4h**。Search C 约 **1.5h**。LWiS List 保留约 **56.3h**／扫描约 **57h**（**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · KEV +3 · Pixel／Cisco ISE／Acronis】** catalogVersion **2026.09.16／1713／+3**。**CVE-2026-58704**（Google Pixel 蜂窝基带不当授权／权限绕过 → 提权；公告称有限定向利用；补丁级别 **2026-09-05+**）／**CVE-2026-76460**（Cisco ISE／ISE-PIC 特权 API 误用 → 未认证可绕过 Web 管理；修方向含 ISE 3.1P12／3.2P11／3.3P12／3.4P7／3.5P4）／**CVE-2026-87886**（Acronis Backup cPanel／WHM 插件与 Plesk 扩展默认权限不当 → 本地提权；厂商称有限在野）。联邦 due 均 **09-19**。本窗口 X Latest **未见**直接点名这三条的高信号原帖（A 被 @CVEnew 洪水淹没）。
  CISA +1：https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-one-known-exploited-vulnerability-catalog
  CISA +2：https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
  Pixel 厂商：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
  Pixel BC：https://www.bleepingcomputer.com/news/security/google-fixes-actively-exploited-android-zero-day-on-pixel-devices/
  Cisco ISE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  Acronis：https://security-advisory.acronis.com/advisories/SEC-10986
  Acronis BC：https://www.bleepingcomputer.com/news/security/acronis-warns-of-actively-exploited-flaw-in-its-cpanel-backup-plugin/

- **【今日 due · LiteLLM／Starlette】** 联邦 due **今日 09-16**：**CVE-2026-59822**（MCP Streamable HTTP 不当认证）／**CVE-2026-48710**（Host 头未校验 → 路径类认证绕过风险）。防御：升级 LiteLLM **≥1.84.0**／Starlette **≥1.0.1**，限制 MCP／ASGI 对外暴露。
  LiteLLM：https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q
  Starlette：https://github.com/Kludex/starlette/security/advisories/GHSA-86qp-5c8j-p5mr
  OSTIF BadHost：https://ostif.org/disclosing-the-badhost-vulnerability-in-starlette

- **【明日 due · Cisco ESA 76461】** **CVE-2026-76461**（Secure Email Gateway／AsyncOS 未认证 SQLi → 底层 OS root 命令执行）联邦 due **明日 09-17**。修复示例：`15.5.5-014`／`16.0.4-302`／`16.5.0-780`。
  CISA：https://www.cisa.gov/news-events/alerts/2026/09/14/cisa-adds-one-known-exploited-vulnerability-catalog
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX

- **【NEW ICS · 258-04..08】** 相对昨日 01..03，CISA ICS 列表新增 **04..08**（发布日标 Sep 15）：Schneider SCADAPack x70／Siemens Reyrolle 7SR5（CVSS 至 **9.8**）／Mendix SAML／Teamcenter／CareCam CM2507（CVSS 至 **9.3**）。
  https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-04
  https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-05
  https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-06
  https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-07
  https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-08

- **【仍逾期 · ScreenConnect + BC 活跃利用】** **CVE-2026-84869** 仍逾期（due 09-14）；BC 报道现已遭活跃利用。同步仍逾期 GitLab **85706**／PaperCut **81578／82078**／MikroTik **67277／86060**（IoC IP 仍见 CERT.pl）等。
  ScreenConnect 厂商：https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin
  BC：https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-critical-screenconnect-flaw/

- **【工具 · nuclei-templates v10.4.9 NEW】** nuclei-templates **v10.4.8 → v10.4.9**（published ~2026-09-16 14:58Z）；Sliver **v1.7.7**／nuclei **v3.11.1** 无升版。X：nuclei 解码器泄漏 goroutine 议题；Hackvertor Check tags；rcekit／OpenHunterAI／dsh-redteam-model 等（防御向仅记存在）。
  nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
  nuclei #7749：https://github.com/projectdiscovery/nuclei/issues/7749
  Hackvertor：https://thespanner.co.uk/hackvertor-check-tags-and-conditions
  X Hackvertor：https://x.com/garethheyes/status/2100326415153430563

- **【威胁 · CHOSEN BRICK／KREMLIN 扩展／BambooToken／NCSC 间谍软件／Anthropic 续传】** BC：伊朗相关 **CHOSEN BRICK** Windows 间谍恶意软件；**KREMLIN** 工具包绕过浏览器检查强制安装 Chrome／Edge 扩展；**BambooToken** 经 MQTT 控制 Windows／Linux。LWiS：NCSC＋FBI＋荷兰 AIVD 伊朗针对异见人士／记者间谍软件联合公告；Kaspersky NightEagle；Anthropic Sep 2026 TI 续传（含模型蒸馏战役叙事）。
  CHOSEN BRICK BC：https://www.bleepingcomputer.com/news/security/iranian-hackers-use-chosen-brick-windows-malware-to-spy-on-targets/
  KREMLIN 扩展 BC：https://www.bleepingcomputer.com/news/security/malware-bypasses-browser-checks-to-force-install-chrome-edge-extensions/
  BambooToken BC：https://www.bleepingcomputer.com/news/security/bambootoken-malware-controls-windows-and-linux-systems-via-mqtt/
  NCSC：https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
  X NCSC：https://x.com/NCSC/status/2099863580640260391
  Anthropic 官方：https://www.anthropic.com/threat-intelligence-report-september-2026
  X Anthropic：https://x.com/killedbyclaude/status/2100345734373818794

- **【新闻 · Risky／tl;dr／其他】** Risky 仍 **RBNEWS612**（另见 **SRB183**；613／184 仍 404）；tl;dr 仍 **#345**（#346 未发布）。另见：HumHub **CVE-2026-18430**（@fluidattacks CNA）；BIND 9 一批 High／Medium（修 9.20.29／9.21.26）；CISA 网络诱饵指南；瑞士勒索开发者判决续传；Search C 大量勒索受害者监控／未验证库泄作噪声折叠。
  https://risky.biz/RBNEWS612/
  https://risky.biz/SRB183/
  https://tldrsec.com/p/tldr-sec-345
  HumHub：https://fluidattacks.com/advisories/personajes
  X HumHub：https://x.com/fluidattacks/status/2100361588834259012

## CVE / POC / 漏洞

### 1. 【KEV NEW】Google Pixel CVE-2026-58704

CISA **2026-09-16** 入目；due **2026-09-19**。蜂窝基带不当授权／权限绕过 → 提权；Pixel 公告称有限定向利用。防御：尽快升至 Pixel 安全补丁级别 **2026-09-05** 或更新；限制不可信蜂窝／基带攻击面。

地址：
- CISA 告警：https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商 Pixel 公告：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-58704
- BC：https://www.bleepingcomputer.com/news/security/google-fixes-actively-exploited-android-zero-day-on-pixel-devices/
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC。

### 2. 【KEV NEW】Cisco ISE／ISE-PIC CVE-2026-76460

CISA **2026-09-16** 入目；due **2026-09-19**。特权 API 误用：未认证远程攻击者可绕过 Web 管理（活跃利用报道）。防御：按 advisory 升级（示例 **3.1 Patch 12／3.2 Patch 11／3.3 Patch 12／3.4 Patch 7／3.5 Patch 4**）；限制管理面暴露；审阅 `ise-kong/access.log` 与外部网络日志（防御向，不展开攻击步骤）。

地址：
- CISA 告警：https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76460

IoC：未见公开 IoC（厂商建议日志狩猎，本报不转载利用步骤）。

### 3. 【KEV NEW】Acronis Backup CVE-2026-87886

CISA **2026-09-16** 入目；due **2026-09-19**。cPanel／WHM 插件与 Plesk 扩展默认权限不当 → 本地提权；厂商／BC 称有限在野。防御：升级至厂商修复（叙事示例 cPanel／WHM 插件 **1.9.3 HF3**；Plesk 扩展 **1.8.11**，以 SEC-10986 为准）；加固面板暴露面。

地址：
- 厂商：https://security-advisory.acronis.com/advisories/SEC-10986
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87886
- CISA：https://www.cisa.gov/news-events/alerts/2026/09/16/cisa-adds-two-known-exploited-vulnerabilities-catalog
- BC：https://www.bleepingcomputer.com/news/security/acronis-warns-of-actively-exploited-flaw-in-its-cpanel-backup-plugin/

IoC：未见公开 IoC（厂商称 limited targeted）。

### 4. 【今日 due】LiteLLM CVE-2026-59822／Starlette CVE-2026-48710

联邦 due **2026-09-16**。LiteLLM：MCP Streamable HTTP 不当认证，伪造 Bearer 可触及 MCP tooling。Starlette：Host 头未校验，`request.url.path` 可与路由路径偏离（路径类认证绕过风险）。防御：对照 GHSA 升级、限制对外暴露的 MCP／ASGI 入口。

地址：
- LiteLLM GHSA：https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q
- LiteLLM NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-59822
- Starlette GHSA：https://github.com/Kludex/starlette/security/advisories/GHSA-86qp-5c8j-p5mr
- Starlette NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-48710
- OSTIF：https://ostif.org/disclosing-the-badhost-vulnerability-in-starlette

IoC：未见公开 IoC。

### 5. 【明日 due】Cisco Secure Email Gateway CVE-2026-76461

CISA **2026-09-14** 入目；due **2026-09-17**。未认证 SQL 注入（经特制邮件）可在底层 OS 以 **root** 执行任意命令。防御：升级至厂商修复版本、限制网关暴露、按 advisory 在 `mail_logs` 狩猎相关异常（防御向）。

地址：
- CISA：https://www.cisa.gov/news-events/alerts/2026/09/14/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76461

IoC：未见公开 IoC IP／样本哈希列表。

### 6. 【仍逾期 · 活跃利用报道】ConnectWise ScreenConnect CVE-2026-84869

KEV due **2026-09-14** 已过；BC 报道现已遭活跃利用。防御：按厂商公告升级（叙事升 **26.6.5**）、限制暴露面、审计异常远程会话。

地址：
- 厂商：https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-84869
- BC：https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-critical-screenconnect-flaw/

IoC：未见公开 IoC。

### 7. 【仍逾期】GitLab CVE-2026-85706／PaperCut CVE-2026-81578／82078

GitLab：未认证任意文件读（自管 CE／EE）；补丁叙事 **19.3.2／19.2.6／19.1.8**。PaperCut：维护版叙事 **26.0.5／25.0.13／24.1.10**。due 均自 **09-14** 起逾期。

地址：
- GitLab：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
- GitLab NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85706
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/

IoC：未见本窗口新公开 IoC。

### 8. 【仍逾期】MikroTik RouterOS CVE-2026-67277／CVE-2026-86060

KEV due **2026-09-13** 已过。修方向含 **6.49.21／7.23.4／7.24.2／7.25 beta 3**（以厂商表为准）。

地址：
- 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67277 · https://nvd.nist.gov/vuln/detail/CVE-2026-86060

IoC：IP `82.192.72.4` · `103.102.31.18`（CERT.pl，仍见于今日备援）。

### 9. 【仍逾期 · 09-12 due】Cisco FMC CVE-2026-20079／Citrix CVE-2026-19490／Fortinet CVE-2025-25249

FMC 认证绕过（CVSS **10.0**）。Talos 续跟。另 Magento **75650**／N-able **86218**（due 09-11）仍逾期。

地址：
- Talos：https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- IoC raw：https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/09/ongoing-fmc-exploitation.txt
- 厂商 FMC：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- Citrix：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- Fortinet：https://fortiguard.fortinet.com/psirt/FG-IR-25-084

IoC：见 Talos IoC raw（本报不重复展开完整列表；摘要见「地址／IoC 汇总」）。

### 10. 【NEW ICS】ICSA-26-258-04..08（相对昨日 +5）

- **258-04** Schneider Electric SCADAPack x70（CVE-2026-81861；CVSS 叙事约 **6.5**）
- **258-05** Siemens Reyrolle 7SR5（多 CVE，含 2024／2026 批次；CVSS 至 **9.8**）
- **258-06** Siemens Mendix SAML（CVE-2026-80465；CVSS 约 **8.7**）
- **258-07** Siemens Teamcenter（CVE-2026-58113；CVSS 约 **6.1**）
- **258-08** CareCam CM2507（多 CVE；CVSS 至 **9.3**）
- 昨日 **258-01..03**（Digital Watchdog／Wärtsilä／mySCADA）仍列于 ICS 列表。

地址：
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-04
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-05
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-06
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-07
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-08
- 列表：https://www.cisa.gov/news-events/ics-advisories
- 仍列 01..03：https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-01 · https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-02 · https://www.cisa.gov/news-events/ics-advisories/icsa-26-258-03

IoC：未见公开 IoC（见各 ICS advisory 缓解措施）。

### 11. 【X · CNA】HumHub CVE-2026-18430（@fluidattacks）

Fluid Attacks 作为 CNA 分配 **CVE-2026-18430**，称 AI SAST 检出并披露 HumHub 新零日；细节见 advisory「personajes」。**本报仅记公开披露存在，不转载 PoC／利用步骤。**

地址：
- Advisory：https://fluidattacks.com/advisories/personajes
- 目录：https://fluidattacks.com/advisories/
- 原帖：https://x.com/fluidattacks/status/2100361588834259012

IoC：未见公开 IoC。

### 12. 【X · 厂商批次】BIND 9 多 CVE（修 9.20.29／9.21.26）

@omokazuki 转述 BIND 9 一批 High／Medium CVE 与修正版本 **9.20.29／9.21.26**。防御：按 ISC／发行版安全通道升级 named。

地址：
- 转引门户：https://security.sios.jp/
- 原帖：https://x.com/omokazuki/status/2100360066922885447

IoC：未见公开 IoC。

### 13. 【噪声过滤】@CVEnew 洪水／Search C 勒索受害者监控

Search A 保留 26 条中约 **24** 条为 @CVEnew 连续新 CVE 倾倒（AVideo／n8n／Craft CMS／Nodemailer／joi／djust 等），**无一匹配今日 NEW KEV 或高信号在野条目** → 叙事折叠为低信号噪声，不逐条升格。Search C 约 **1.5h** 窗口内大量 Akira／Qilin／ShadowByt3$／Kairos 等受害者监控与未验证库泄声称 → 统一标为情报噪声（见 APT 节）。

地址（噪声样例，不升格）：
- CVEnew 例：https://x.com/CVEnew/status/2100361543472824416
- 勒索监控例：https://x.com/sec_news_com/status/2100345482447102152

IoC：未见可靠公开 IoC。

## 工具与 GitHub 发布

### 1. nuclei-templates **v10.4.9**（NEW vs 昨 v10.4.8）

published_at **2026-09-16T14:58:45Z**。防御向模板库更新，建议同步拉取。

地址：
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9

IoC：不适用。

### 2. Sliver／nuclei — 无升版

| 项目 | 标签 | 较昨 | URL |
|------|------|------|-----|
| BishopFox/sliver | v1.7.7 | unchanged | https://github.com/BishopFox/sliver/releases/tag/v1.7.7 |
| projectdiscovery/nuclei | v3.11.1 | unchanged | https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1 |
| projectdiscovery/nuclei-templates | **v10.4.9** | **NEW** | https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9 |

另：@geeknik 指向 nuclei 解码器／goroutine 泄漏议题（工程缺陷讨论，非利用教程）。

地址：
- Issue：https://github.com/projectdiscovery/nuclei/issues/7749
- 原帖：https://x.com/geeknik/status/2100346854370070985

### 3. Hackvertor — Check tags（LWiS）

@garethheyes：Hackvertor 新增 Check tags，可对标签做条件表达式（例：校验 JSON 后再 base64）。Web 安全编码／解码辅助，防御／研究向。

地址：
- 文章：https://thespanner.co.uk/hackvertor-check-tags-and-conditions
- 原帖：https://x.com/garethheyes/status/2100326415153430563

IoC：不适用。

### 4. rcekit／OpenHunterAI／dsh-redteam-model 等 — 防御向仅记存在

Search B 覆盖约 **27.4h**，可见：
- **rcekit**（kabiri-labs）：命令注入结果判定辅助。**仅记公开存在，不提供使用步骤／payload。**
- **OpenHunterAI**（LumosLab）：本地 AI 对外评估公开 Web／API／LLM。
- **dsh-redteam-model**（SeaOf0）：十类安全研究模式拆为 persona／playbook／skills。
- **Supply-Chain-Parasite** 模拟：AI Agent Skill → C2 叙事研究仓。
- Phantom Loader LetsDefend write-up（Ghidra 分析笔记）。
- 其他低信号（calc 补丁玩笑、Cobalt Strike 吐槽、CS-Remote-OPs-BOF 链）不升格。

地址：
- rcekit：https://github.com/kabiri-labs/rcekit · https://x.com/AhmadKabiri_/status/2099965366453621053
- OpenHunterAI：https://github.com/LumosLab-Innovation/OpenHunterAI · https://x.com/AlAssaf_H/status/2100171061618679820
- dsh-redteam-model：https://github.com/SeaOf0/dsh-redteam-model · https://x.com/vintcessun/status/2100187703518405055
- Supply-Chain-Parasite：https://github.com/Th3g4ntl3m4n/Supply-Chain-Parasite-Simulaci-n-de-una-Skill-Maliciosa-en-Agentes-de-IA · https://x.com/th3g4ntl3m4n/status/2100020754196705578
- Phantom Loader 笔记：https://github.com/0xAshvin/Soc-investigation/tree/main/letsdefend · https://x.com/0xAshvin/status/2100204724314419380

IoC：不适用（工具／研究发布）。

### 5. DroneRTS（LWiS · 边缘）

@DanHMcInerney：自主 agent 无人机对抗演示仓（Zenoh／MAVLINK）。与传统红队工具弱相关，作边缘记录。

地址：
- 仓库：https://github.com/DanMcInerney/DroneRTS
- 原帖：https://x.com/DanHMcInerney/status/2100348696189603895

IoC：不适用。

### 6. CISA — Using Cyber Decoys 指南（LWiS）

CISA 发布「Using Cyber Decoys to Strengthen Detection and Response」（约 22 页；tripwires／honeytokens／MITRE Engage 等）。

地址：
- https://www.cisa.gov/resources-tools/resources/using-cyber-decoys-strengthen-detection-and-response
- 原帖：https://x.com/blackroomsec/status/2100255408103252250

IoC：不适用（指南）。

## APT / Malware 分析

### 1. CHOSEN BRICK — 伊朗相关 Windows 间谍恶意软件（BC）

BC：**CHOSEN BRICK** Windows 恶意软件用于监视目标（伊朗黑客叙事）。防御：终端 EDR／行为检测、钓鱼入口加固、按原文附录狩猎（若有）。

地址：
- BC：https://www.bleepingcomputer.com/news/security/iranian-hackers-use-chosen-brick-windows-malware-to-spy-on-targets/

IoC：未见公开 IoC（本备援未抄录；以原文为准）。

### 2. KREMLIN 工具包 — 强制安装浏览器扩展（BC）

BC：恶意软件绕过浏览器检查，强制安装 Chrome／Edge 扩展。防御：企业浏览器扩展白名单、审查强制安装策略与异常扩展、终端完整性监控。

地址：
- BC：https://www.bleepingcomputer.com/news/security/malware-bypasses-browser-checks-to-force-install-chrome-edge-extensions/

IoC：未见公开 IoC。

### 3. BambooToken — MQTT C2（BC，09-15）

BambooToken 经 MQTT 控制 Windows／Linux。防御：监控异常 MQTT 出站、终端行为分析。

地址：
- BC：https://www.bleepingcomputer.com/news/security/bambootoken-malware-controls-windows-and-linux-systems-via-mqtt/

IoC：未见公开 IoC。

### 4. NCSC／FBI／AIVD — 伊朗针对异见人士／记者间谍软件联合公告（LWiS）

@NCSC：与 FBI、荷兰 AIVD 联合发布公告，揭露伊朗国家行为体用于针对异见人士、活动人士与记者的间谍软件；建议识别鱼叉钓鱼并防御数据收集活动。

地址：
- 公告：https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
- 原帖 1/2：https://x.com/NCSC/status/2099863580640260391
- 原帖 2/2：https://x.com/NCSC/status/2099863582624096627

IoC：以 NCSC 公告正文／附录为准；本窗口 X 帖未见独立 IoC 列表抄录。

### 5. Anthropic September 2026 TI 续传

官方报告续在 X 传播；@killedbyclaude 强调模型蒸馏战役叙事（约 3500 伪造账户／1.51 亿次交互等摘要——**以官方页／PDF 为准，社交媒体可能夸大**）。@GenestMark6167 日文摘要同主题。

地址：
- 官方：https://www.anthropic.com/threat-intelligence-report-september-2026
- PDF：https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf
- X：https://x.com/killedbyclaude/status/2100345734373818794 · https://x.com/GenestMark6167/status/2100359514109391021

IoC：以官方 PDF／附录为准；本窗口未见新独立 IoC 列表。

### 6. NightEagle APT — Kaspersky（LWiS）

@shakirov2036：Kaspersky 报道 NightEagle 对俄企业攻击、地理扩展；该行为体 2025-07 由奇安信（APT-Q-95）／360（APT-C-78）曝光，当时标为北美 APT。

地址：
- Securelist：https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/
- 原帖：https://x.com/shakirov2036/status/2100296036770050504

IoC：见 Securelist 文；本报不转载利用步骤。

### 7. 防御加固短讯（LWiS）

- Kerberoasting／密码喷洒检测与蜜罐账户（TrustedSec）：https://trustedsec.com/blog/detecting-password-spraying-with-a-honeypot-account · https://x.com/PyroTek3/status/2100318707314815236
- NetExec 扩展 DPAPI 至 WMI／WinRM／MSSQL 等协议（蓝队需相应扩大监控）：https://x.com/al3x_n3ff/status/2099498723038416995

IoC：未见独立公开 IoC。

### 8. 司法／事件续传

- 瑞士法院判处 LockerGoga／MegaCortex／Nefilim 关键开发者近 13 年：https://x.com/IntCyberDigest/status/2100359206394020070
- LockBit 事件 CISO 不付赎金叙事（@ncxgroup）：https://x.com/ncxgroup/status/2100359705163878760
- 西班牙数据机构首份 AI 驱动数据泄露报告（BC）：https://www.bleepingcomputer.com/news/security/spains-data-agency-gets-first-report-of-ai-powered-data-breach/
- Admin Menu Editor Pro 供应链后门续跟（昨主条，今日备援仍列）：https://www.bleepingcomputer.com/news/security/malcious-admin-menu-editor-pro-plugin-backdoors-1-500-wordpress-sites/

IoC：不适用或未见新公开 IoC。

### 9. 未验证库泄／勒索受害者监控（情报噪声）

Search C ~1.5h 内多条 **未验证声称／受害者监控**，一律不升格为主条：ChimeraZ／IAD GROUP；Uways Qarani 针对 Fu Pao／Rafael／Elbit 声称；Akira（Bee Maid／Manders）；Qilin（Thema Foundries／Huskies）；ShadowByt3$／HandyTrac；Kairos／Leisure Coast；EM／RDA Motors；Pocket Bitcoin；St James Anglican；Cedar County Memorial（医院仅确认宕机）；MUIS／Avelogic；bf.st／Generation Tux 等。

地址（样例）：
- https://x.com/intels_daily/status/2100360863202824211
- https://x.com/intels_daily/status/2100345785044910094
- https://x.com/FalconFeedsio/status/2100344366581813651
- https://x.com/BreachHistoryBH/status/2100338940200751407

IoC：未见可靠公开 IoC。

## 地址／IoC 汇总

- **NEW KEV Pixel 58704／ISE 76460／Acronis 87886**：未见公开 IoC。
- **LiteLLM／Starlette（今日 due）／Cisco ESA 76461（明日 due）**：未见公开 IP／hash。
- **ScreenConnect 84869**：未见公开 IoC（BC 活跃利用报道）。
- **MikroTik（CERT.pl）**：`82.192.72.4` · `103.102.31.18`。
- **Cisco FMC Talos**：完整列表见 https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/09/ongoing-fmc-exploitation.txt
- **CHOSEN BRICK／KREMLIN／BambooToken／NCSC 间谍软件／NightEagle**：本窗口公开备援／X 帖未见可抄录独立 IoC 列表（以各原文附录为准）→ **未见公开 IoC**（或见原文）。
- **其余条目**：未见公开 IoC。

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

- X Latest A（CVE／POC／exploit／0day）：https://x.com/search?q=(CVE%20OR%20POC%20OR%20exploit%20OR%200day%20OR%20%220-day%22)%20-filter%3Areplies&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／cobalt／implant）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20redteam%20OR%20nuclei%20OR%20sliver%20OR%20cobalt%20OR%20implant)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor／ransomware／threat intelligence）：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20OR%20ransomware%20OR%20%22threat%20intelligence%22)%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
