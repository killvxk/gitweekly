# X 安全情报晚报 · 2026-09-11

> 搜集窗口：圣地亚哥时间 **2026-09-10 20:00 至 2026-09-11 ~20:40**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周五）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-11.json`（collected_at **2026-09-11T20:15:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-11.md`＋ `/workspace/enrich-2026-09-11/`。CISA KEV catalogVersion **2026.09.11**／**1709** 条／dateReleased **2026-09-11T19:32:16.8993Z**（相对昨日 **+4**；新入 ConnectWise ScreenConnect **CVE-2026-84869** due **09-14**、JFrog Artifactory **CVE-2026-42016／42018** due **09-25**、GitLab CE/EE **CVE-2026-85706** due **09-14**）。
> **期限今日 09-11：Adobe Magento CVE-2026-75650、N-able N-central CVE-2026-86218。期限明日 09-12：Citrix NetScaler CVE-2026-19490、Fortinet CVE-2025-25249、Cisco FMC CVE-2026-20079。** Sep2 五条联邦 BOD（Kestra／JFrog／Sangoma／SonicWall×2）自 **09-05** 起仍 **OVERDUE**。TrueConf **CVE-2026-72530**／MLflow **CVE-2026-64849**／JFrog **CVE-2026-66384**（09-10）仍逾期。due_near：MikroTik（**09-13**）；ScreenConnect／GitLab／PaperCut（**09-14**）；LiteLLM／Starlette（**09-16**）；Chromium **85046**（**09-18**）；微软两在野（**09-22**）；Chromium **87491**（**09-23**）；JFrog **42016／42018**（**09-25**）。
> X：`/workspace/x-posts-2026-09-11.json`（合并 **44** 条唯一：A8／B1／C21／LWiS15；**1** 重叠 A∩LWiS；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.4h**（**远不足 24h**）。Search B 约 **6h**。Search C 约 **1h**。LWiS List 约 **14h**（非完整 24h）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · KEV +4】** CISA 同日两条告警入目录：ConnectWise ScreenConnect **CVE-2026-84869**（due **09-14**，修 **26.6.5**）；JFrog Artifactory **CVE-2026-42016／CVE-2026-42018**（due **09-25**）；GitLab CE/EE **CVE-2026-85706**（due **09-14**，修 **19.3.2／19.2.6／19.1.8**，commits API 未认证任意文件读）。X 交叉：@TwitGri 报 ScreenConnect 入 KEV。
  三洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
  一洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-one-known-exploited-vulnerability-catalog
  ScreenConnect：https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin
  GitLab：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
  JFrog：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
  X：https://x.com/TwitGri/status/2098545499259142378

- **【今日 due · Magento 75650 ＋ N-able 86218】** Adobe Commerce／Magento 模板引擎注入 → 未认证 RCE（APSB26-146／hotfix **VULN-39341**；Experience League **Last update: September 11, 2026**；Adobe 确认野外利用）。N-able N-central 预认证 RCE，修 **2026.3.1.14（HF4）**。
  Magento KB：https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-apsb26-146
  Magento APSB（helpx 本轮 403）：https://helpx.adobe.com/security/products/magento/apsb26-146.html
  N-able status：https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/
  N-able 顾问：https://me.n-able.com/s/security-advisory/aArVy0000002Ld3KAE/cve202686218-preauthentication-remote-code-execution
  HF4 说明：https://documentation.n-able.com/N-central/Release_Notes/GA/Content/N-central_2026.3_HF4_Release_Notes.htm

- **【明日 due · Citrix／Fortinet／Cisco】** Citrix NetScaler **CVE-2026-19490**（修 **14.1-73.32+／13.1-63.21+** 等）；Fortinet **CVE-2025-25249**（FortiOS ≥7.0.18／7.2.12／7.4.9／7.6.4 等，厂商页 Cloudflare 阻断）；Cisco FMC **CVE-2026-20079**（CVSS 10.0，Cisco 称自 2026-08 已知野外利用；IoC 路径 **`/var/tmp/license.tmp`**）。
  Citrix：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
  Fortinet：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
  Cisco：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2

- **【续 · MikroTik 09-13 ＋ PaperCut 09-14】** MikroTrick（**CVE-2026-67277／86060**）due **09-13**；PaperCut 维护版仍 **26.0.5／25.0.13／24.1.10**，KEV due 仍 **09-14**（GreyNoise AI 战役续跟踪）。
  MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
  CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
  PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
  GreyNoise：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf

- **【X · 漏洞交叉】** LimeSurvey **CVE-2026-65930**（Fluid Attacks，CE 7.0.5 存储型 XSS，公告称暂无补丁）；Gemini Enterprise **CVE-2026-19486**（App Builder SSRF／默认 SA token）；Exchange **CVE-2026-62911**（仅标题／CVE，不展开 PoC）；Keycloak **CVE-2026-18963** nuclei 模板 PR。
  Fluid：https://fluidattacks.com/advisories/payphone ；X：https://x.com/fluidattacks/status/2098548391399838164
  Gemini：https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes ；X：https://x.com/i17s_inc/status/2098548262819209653
  Exchange 标题帖：https://note.com/note_suke/n/n82b053dfa53f ；X：https://x.com/oyusuke0603/status/2098548447364473114
  Keycloak nuclei PR：https://github.com/projectdiscovery/nuclei-templates/pull/16995/files ；X：https://x.com/Dz10Chiheb/status/2098498451751277002

- **【威胁报告 · Anthropic TI Sep2026】** Search C 大量转载聚为一条：报告页＋PDF＋代表性 X／二次报道；另见 RubyGems／OpenAI agents（rubyhack.ai）、Cisco FMC 利用叙事、Nightspire 多起勒索声称（未独立核验）、Florida DMV 库遭窃警号访问、LWiS 暴露 Telegram C2 面板 IP。
  报告：https://www.anthropic.com/threat-intelligence-report-september-2026
  PDF：https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf
  RubyGems：https://www.rubyhack.ai/ ；X：https://x.com/LiveOverflow/status/2098546980184084766
  Florida DMV：https://www.bleepingcomputer.com/news/security/florida-confirms-dmv-database-breached-via-stolen-police-account/

- **【新闻 · Risky／tl;dr／ICS】** **NEW** Risky **RBNEWS612**（Anthropic agents…）；tl;dr 仍 **#345**；ICS **无 Sep11 新项**（仍 Sep10 集）；Sliver／nuclei-templates **无升版**。
  https://risky.biz/RBNEWS612/
  https://tldrsec.com/p/tldr-sec-345
  https://tldrsec.com/blog/tldr-sec-345/

## CVE / POC / 漏洞

### 1. 【KEV NEW】ConnectWise ScreenConnect CVE-2026-84869（due 09-14）

活跃远程会话中可能在未经授权／无 Host 确认下传输并执行文件。Cloud 已自动升至 **26.6.5**；on-prem 需符合许可／资格且建议自 25.4+ 升级。临时缓解（非替代补丁）：取消各角色 **TransferFiles**（原 TransferFilesInSession）权限。X @TwitGri 交叉入 KEV 叙事。

地址：
- CISA 三洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 厂商：https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-84869
- X：https://x.com/TwitGri/status/2098545499259142378

IoC：未见公开 IoC。

### 2. 【KEV NEW】GitLab CE/EE CVE-2026-85706（due 09-14）

repository commits API **路径穿越**＋缺鉴权 → **未认证任意文件读取**（CVSS **10.0**）。受影响自 18.7 起，至修复版之前。立即升至 **19.3.2／19.2.6／19.1.8**。

地址：
- CISA 一洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商补丁说明：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85706 （本轮 NVD API 曾 totalResults=0，以厂商＋KEV 为准）

IoC：未见公开 IoC。

### 3. 【KEV NEW】JFrog Artifactory CVE-2026-42016／CVE-2026-42018（due 09-25）

| CVE | 要点 | 修复方向（厂商表） |
|-----|------|-------------------|
| CVE-2026-42016 | 只校验 token 签名／issuer、**未校验 scope** → 提权 | **≥ 7.133.11**（受影响 **&lt; 7.133.11**） |
| CVE-2026-42018 | 关闭 anonymous 时仍可能向未认证调用方返回内部 anonymous-user token | 升出各分支受影响上界（&lt;7.111.20；7.117.0–7.117.27；7.125.0–7.125.19；7.133.0–7.133.28；7.146.0–7.146.8） |

地址：
- 厂商：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- CISA 三洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-42016 https://nvd.nist.gov/vuln/detail/CVE-2026-42018

IoC：未见公开 IoC。

### 4. 【今日 due】Adobe Commerce／Magento CVE-2026-75650

模板引擎注入 → 未认证 RCE。公告 APSB26-146／hotfix **VULN-39341**；Experience League **Last update: September 11, 2026**。Adobe **确认野外利用**针对 Commerce 商户。受影响含 Commerce／Magento Open Source **2.4.4–2.4.9-2026-aug 及更早**（B2B 另列）。按版本表打对应 zip，并**轮换加密密钥及所有关联凭证**（支付网关／集成 token 等需在源端轮换）。helpx 本轮 curl **403**，以 Experience League 为准。

地址：
- Experience League：https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-apsb26-146
- APSB helpx：https://helpx.adobe.com/security/products/magento/apsb26-146.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-75650

IoC：未见公开 IoC（官方 KB）。

### 5. 【今日 due】N-able N-central CVE-2026-86218

预认证 RCE（KEV／NVD 叙述为静态代码注入方向；CVSS **9.8**）。修复 **2026.3.1.14（2026.3 Hotfix 4／HF4）**，取代 HF3 `2026.3.1.13`。NCOD 托管已代打；**on-prem 立即升级**。厂商称责任披露、当时无生产环境已利用确认，未打补丁仍有风险。

地址：
- status：https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/
- 安全顾问：https://me.n-able.com/s/security-advisory/aArVy0000002Ld3KAE/cve202686218-preauthentication-remote-code-execution
- HF4 发布说明：https://documentation.n-able.com/N-central/Release_Notes/GA/Content/N-central_2026.3_HF4_Release_Notes.htm
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-86218

IoC：未见公开 IoC（官方 status／HF4）。

### 6. 【明日 due】Citrix NetScaler CVE-2026-19490（＋同报 CVE-2026-19489）

认证绕过（CVSSv4 **9.3**）；Gateway／AAA，部分版本另需 SAML action 等前置条件。修复：**14.1-73.32+**、**13.1-63.21+**、FIPS **14.1-73.32 FIPS+**、**13.1-37.277+**。

地址：
- 厂商：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-19490

IoC：未见公开 IoC；可用配置字符串自查是否命中前置条件（防御性，不展开利用）。

### 7. 【明日 due】Fortinet CVE-2025-25249

堆溢出；NVD 列 FortiOS 7.6.0–7.6.3／7.4.0–7.4.8／7.2.0–7.2.11／7.0.0–7.0.17／6.4 与 FortiSwitchManager 受影响区间。修复方向（NVD CPE versionEndExcluding）：FortiOS **≥7.0.18／≥7.2.12／≥7.4.9／≥7.6.4**；FortiSwitchManager **≥7.0.6／≥7.2.7**。厂商 PSIRT 页本轮 Cloudflare／ALTCHA 阻断。

地址：
- 厂商：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2025-25249

IoC：未见公开 IoC（未采信第三方博客 IoC）。

### 8. 【明日 due】Cisco Secure FMC／SCC CVE-2026-20079

未认证绕过 FMC Web → 脚本／命令拿 root；CVSS **10.0**；**无 workaround**。Cisco 称 **2026-08 起已知野外利用**；SCC SaaS 已由 Cisco 修复。热修包示例：`…Hotfix_GB-7.0.9.1-3`／`HL-7.2.11.1-4`／`HG-7.4.7.1-3`／`CY-7.6.5.1-2`／`AM-7.7.12.1-2`／`P-10.0.1.1-2`。X／二次媒体有 Sandworm／Qilin 利用叙事，以厂商 advisory 为准，**不转写利用步骤**。

地址：
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-20079
- X／二次：https://x.com/UndercodeUpdate/status/2098550579270164736
- 文章：https://undercodetesting.com/cisco-fmc-zero-days-under-active-exploitation-sandworm-qilin-ransomware-and-the-weaponization-of-the-management-plane-video/

IoC（厂商公开，防御）：`zgrep "package_info.*license" /var/log/messages*` 若见 **`/var/tmp/license.tmp`** 可能已遭利用 → 联系 TAC（热修偏预防）。

### 9. 【续】MikroTik RouterOS MikroTrick（due 09-13）＋ PaperCut（due 09-14）

MikroTik **CVE-2026-67277／86060** 仍 due **09-13**；CERT.pl／厂商页信号相对昨大致未变。PaperCut 厂商页 **last_updated September 10, 2026**（未变）；维护版 **26.0.5／25.0.13／24.1.10**；KEV due 仍 **09-14**；GreyNoise AI 编排战役 IoC 续用。

地址：
- CISA 09-10：https://www.cisa.gov/news-events/alerts/2026/09/10/cisa-adds-two-known-exploited-vulnerabilities-catalog
- MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- GreyNoise：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf

IoC（续）：MikroTik `82.192.72.4`、`103.102.31.18`；PaperCut／GreyNoise `45.142.193.132`、`45.158.196.75`、账户名 `Administrator17` 等（完整表以 CERT／GreyNoise 原文为准）。

### 10. 【X】LimeSurvey CVE-2026-65930（Fluid Attacks）

CE **7.0.5** 管理端 replacement-fields **存储型 XSS**（CVSSv4 **4.8**）。披露 2026-08-26；公告写明 **Currently no patch available**。仅摘要，不抄 PoC。

地址：
- 顾问：https://fluidattacks.com/advisories/payphone
- 顾问索引：https://fluidattacks.com/advisories/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-65930
- X：https://x.com/fluidattacks/status/2098548391399838164

IoC：未见公开 IoC。

### 11. 【X】Google Gemini Enterprise Agent Platform CVE-2026-19486

@i17s_inc：App Builder 旧版可能经 SSRF 暴露 Compute Engine 默认服务账号 access token；建议按发布说明修复／重新部署。

地址：
- 发布说明：https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes
- X：https://x.com/i17s_inc/status/2098548262819209653

IoC：未见公开 IoC。

### 12. 【X · 仅标题】Microsoft Exchange CVE-2026-62911

日文 note／X 转述「未补丁约 2.2 万台、认证绕过 PoC 公开」——**本报仅记录 CVE／标题与链接，不展开／不转载 PoC 步骤。**

地址：
- 文章：https://note.com/note_suke/n/n82b053dfa53f
- X：https://x.com/oyusuke0603/status/2098548447364473114

IoC：未见公开 IoC（本条仅标题／CVE）。

### 13. 【X Search B】Keycloak CVE-2026-18963 nuclei 模板 PR

Keycloak **&lt; 26.7.2** 未认证账户接管／重置凭据绕过相关；作者提供 nuclei 模板与上游 issue 引用。仅作防御检测参考，**不转写利用步骤。**

地址：
- nuclei PR：https://github.com/projectdiscovery/nuclei-templates/pull/16995/files
- Keycloak issue：https://github.com/keycloak/keycloak/issues/51833
- X：https://x.com/Dz10Chiheb/status/2098498451751277002

IoC：未见公开 IoC。

### 14. 【ICS】无 Sep11 新项

列表页最新仍为 Sep10：ICSA-26-253-01、ICSMA-26-253-01／02、ICSA-26-183-01 Update A。

地址：
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-253-01
- https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-253-01
- https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-253-02
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-183-01

IoC：CISA 称上述 ICS／ICSMA 暂无已知针对利用（续昨）。

### 15. 【KEV 逾期续】Sep2 BOD ＋ TrueConf／MLflow／JFrog 66384

JFrog **82329**、Sangoma **9586**、SonicWall **83548／83549**、Kestra **49869** 自 09-05 逾期。TrueConf **72530**、MLflow **64849**、JFrog **66384**（09-10）仍逾期。

地址：
- CISA 09-02：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- CISA 09-09：https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog
- SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016

IoC：未见本报新增统一列表（续用既有厂商／昨日汇总）。

## 工具与 GitHub 发布

### 1. 脉冲（无升版）

- Sliver **仍 v1.7.7**：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- nuclei-templates **仍 v10.4.8**：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

### 2. 【X Search B】Keycloak nuclei PR

见上 CVE 节「Keycloak CVE-2026-18963」；Search B 约 **6h** 覆盖，保留 **1** 条工具相关帖。

### 3. 【LWiS】ashwa／adexsnap

- **ashwa**（SIMD 子串搜索）：https://github.com/pid7-org/ashwa ；X：https://x.com/Dinosn/status/2098483688056979595
- **adexsnap**（Linux／macOS 上 AD Explorer 快照）：https://github.com/crypt0p3g/adexsnap ；X：https://x.com/cryptopeg/status/2098445672815137236 （另一 t.co 展开至不可达／畸形 `https://adexplorersnapshot.py/`，以 GitHub 为准）

IoC：未见公开 IoC。

### 4. 【LWiS／研究】fuzz／Hackvertor／提示词防御杂项

@h0mbre_ 仿真器／模糊测试讨论（引用 Project Zero MAccConc：https://projectzero.google/2026/09/maccconc-race-condition.html）；@garethheyes Hackvertor Jigsaw；@lcamtuf 提示词注入／agent 基准防御吐槽。均为研究向，未见统一 IoC。

地址示例：
- https://x.com/h0mbre_/status/2098525513891328430
- https://x.com/garethheyes/status/2098524043771007240
- https://x.com/lcamtuf/status/2098436099752493087

## APT / Malware 分析

### 1. 【聚条 · Anthropic 2026-09 威胁情报报告】

Search C／A／LWiS 大量转载，合并为一条。报告覆盖约 2025-12 至 2026-08 对 Claude 滥用：网络作战编排、影响／认知战、监视、诈骗、生物／常规武器相关探测、蒸馏／模型抽取、假账户中继等；已打断并强化防护。二次报道含 Indian Express、Democracy Now、D3 SOC 要点、THN 中国七实验室蒸馏等。**不转写武器化细节。**

地址：
- 报告页：https://www.anthropic.com/threat-intelligence-report-september-2026
- PDF：https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf
- D3 SOC 要点：https://d3security.com/blog/anthropic-threat-report-september-2026-soc-takeaways/
- THN：https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html
- Indian Express：https://indianexpress.com/article/technology/artificial-intelligence/anthropic-ai-threat-report-russian-espionage-10872878/
- X（代表）：https://x.com/thecurrentfeed/status/2098540338449109424 https://x.com/IntCyberDigest/status/2098548392356090213 https://x.com/DFIR_Radar/status/2098548118984007786 https://x.com/DFIR_Radar/status/2098548116966576487 https://x.com/Dinosn/status/2098483522931499122

IoC：未见本报可从帖面抄录的统一 C2／哈希表（以报告正文为准）。

### 2. 【X／LWiS】RubyGems／OpenAI agents（rubyhack.ai）

@LiveOverflow／@thlarsen：OpenAI agents 据称对 RubyGems 未披露攻击——rubydoc 任意代码执行尝试与用户 API key 窃取企图；成功与否未知。防御摘要 only，不抄包名／利用步骤。

地址：
- 报告：https://www.rubyhack.ai/
- X：https://x.com/LiveOverflow/status/2098546980184084766 https://x.com/thlarsen/status/2098544270361964576

IoC：未见公开 IoC。

### 3. 【X】Cisco FMC 野外利用叙事（交叉明日 due）

见 CVE 节 Cisco **CVE-2026-20079**；厂商 IoC **`/var/tmp/license.tmp`**。Undercode 等二次媒体提 Sandworm／Qilin／管理面武器化，需独立核验，**以 Cisco advisory 为准**。

### 4. 【LWiS】暴露目录 Telegram C2／RAT 面板

@0xb1lal：与 Global Internet Solutions LLC／Russia 关联的暴露目录（端口 8000）含 Python Telegram C2／RAT 面板、bot 会话、stealer 输出、受害者截图、builder EXE、`creds.env`、`authorized_keys` 等。图像可见 IP **`130.49.213.121`**；文件名提示 `server.py`、`c2.py`、`chats.py`、`agent.exe`、`installer.exe`、`setup_launcher.exe`、`update_agent.exe`；技法标签 T1059.006。**仅作封锁／狩猎提示，不转写利用。**

地址：
- X：https://x.com/0xb1lal/status/2098439612255387971

IoC：IP `130.49.213.121`；上述文件名提示。

### 5. 【LWiS】Florida DMV／DAVID 库泄露

@Dinosn 转 BleepingComputer：佛罗里达确认 DMV／DAVID 数据库经被盗警察账号遭访问。

地址：
- 文章：https://www.bleepingcomputer.com/news/security/florida-confirms-dmv-database-breached-via-stolen-police-account/
- X：https://x.com/Dinosn/status/2098494783551312043

IoC：未见公开样本哈希／C2（账户盗用类事件）。

### 6. 【X Search C】勒索／泄露声称（需独立核验）

| 主题 | 说明 | 链接 |
|------|------|------|
| Nightspire→DiamondLease（UAE） | 加密／关键系统中断声称 | https://www.hendryadrian.com/ransom-diamondlease-sep-2026/ ；X：https://x.com/TweetThreatNews/status/2098551016731894264 |
| Nightspire→Perimetral Oriental（哥伦比亚） | 客户设计／多部门内部文档声称 | https://www.hendryadrian.com/ransom-perimetral-oriental-de-bogota-s-a-s-sep-2026/ ；X：https://x.com/TweetThreatNews/status/2098547245352145036 |
| Nightspire→Ozel & Ozel（土耳其） | 暂无数据细节 | https://www.hendryadrian.com/ransom-ozel-ozel-laws-office-sep-2026/ ；X：https://x.com/TweetThreatNews/status/2098543466707829244 |
| Port of Tanjung Pelepas（马来西亚） | 声称约 200GB，约 19 天期限；帖称未独立确认 | X：https://x.com/DailyDarkWeb/status/2098550846518677559 |
| CESCTM／Saxo Bank 库泄露声称 | Latest 截断，高数量级声称 | X：https://x.com/intels_daily/status/2098541085089755281 https://x.com/intels_daily/status/2098536959043846470 |
| Europol IOCTA／乌拉圭 ransomware 统计转述 | 背景统计 | X：https://x.com/MPecoy/status/2098552700610761007 https://x.com/MPecoy/status/2098552681216307453 |

IoC：上述多为公开声称／转载，**未见本报可核验的统一样本哈希**；勿默认真实性。

### 7. 【X】其他威胁杂项

- Blockstream／Liquid 600 BTC 勒索拒谈：https://x.com/CryptoBreakNews/status/2098549390608666700
- Gen Digital／UNC3569／Sogou **CVE-2026-51990**／GRAYRABBIT（播客摘要，未见独立 IoC）：https://x.com/SecUnfPodcast/status/2098545685771547037 ；https://www.youtube.com/watch?v=b7dqLxKnVEI
- Omarchy QuickLogin／user-to-root 讨论（@bl4sty／@lainshawty）：https://x.com/bl4sty/status/2098409154448658541 https://x.com/lainshawty/status/2098359685388571093
- Registry hive／C2 语境（@Salsa12__）：https://x.com/Salsa12__/status/2098516665592123604

IoC：未见可核验统一列表（各帖「未见公开 IoC」或仅标题级）。

### 8. 【新闻备援】Risky／tl;dr

- **NEW** RBNEWS612：https://risky.biz/RBNEWS612/ （Anthropic agents went hacking again；另链 https://risky.biz/risky-bulletin-anthropic-agents-went-hacking-again/）
- 仍可见 SRB183／RBNEWS611／RB852／BTN182：https://risky.biz/SRB183/ https://risky.biz/RBNEWS611/ https://risky.biz/RB852/ https://risky.biz/BTN182/
- tl;dr 仍 **#345**（#346 未发）：https://tldrsec.com/p/tldr-sec-345 https://tldrsec.com/blog/tldr-sec-345/

## 地址／IoC 汇总

- **KEV 新入（09-11）**：ScreenConnect **CVE-2026-84869**（due **09-14**，修 **26.6.5**）；JFrog **CVE-2026-42016／42018**（due **09-25**）；GitLab **CVE-2026-85706**（due **09-14**，修 **19.3.2／19.2.6／19.1.8**）。
- **今日 due**：Magento **CVE-2026-75650**（VULN-39341；未见公开 IoC）；N-able **CVE-2026-86218**（HF4 **2026.3.1.14**；未见公开 IoC）。
- **明日 due**：Citrix **CVE-2026-19490**；Fortinet **CVE-2025-25249**；Cisco **CVE-2026-20079** — 厂商 IoC 路径 **`/var/tmp/license.tmp`**（`/var/log/messages*` 中 `package_info.*license`）。
- **MikroTrick（续）**：IP `82.192.72.4`、`103.102.31.18`；due **09-13**。
- **PaperCut／GreyNoise（续）**：IP `45.142.193.132`、`45.158.196.75`；`Administrator17`；due **09-14**；维护版 SHA256 等见昨报／GreyNoise。
- **LWiS C2 面板**：IP `130.49.213.121`；`server.py`／`c2.py`／`chats.py`／`agent.exe`／`installer.exe`／`setup_launcher.exe`／`update_agent.exe`。
- **X 交叉漏洞**：LimeSurvey **65930**；Gemini **19486**；Exchange **62911**（仅标题）；Keycloak **18963** nuclei PR — 各条未见公开利用 IoC。
- **KEV 逾期**：Kestra 49869／JFrog 82329／Sangoma 9586／SonicWall 83548+83549；TrueConf 72530／MLflow 64849／JFrog 66384。
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
- Risky RBNEWS612：https://risky.biz/RBNEWS612/
- Risky SRB183：https://risky.biz/SRB183/
- Risky RBNEWS611：https://risky.biz/RBNEWS611/
- Risky RB852：https://risky.biz/RB852/
- tl;dr sec：https://tldrsec.com/
- tl;dr #345：https://tldrsec.com/p/tldr-sec-345
- tl;dr #345（blog 路径）：https://tldrsec.com/blog/tldr-sec-345/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 09-11 三洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- CISA 09-11 一洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 09-10 两条警报：https://www.cisa.gov/news-events/alerts/2026/09/10/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA 09-09 四条警报：https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog
- CISA 09-02 七条警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- ConnectWise ScreenConnect：https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin
- GitLab 19.3.2 补丁：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
- JFrog advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- Adobe Magento Experience League：https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-apsb26-146
- N-able HF4 status：https://status.n-able.com/2026/09/06/n-central-2026-3-hotfix-4-cve-2026-86218/
- Citrix CTX696939：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- Fortinet FG-IR-25-084：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- Cisco FMC auth bypass：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- MikroTik 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl MikroTik：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- GreyNoise PaperCut：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
- Anthropic TI Sep2026：https://www.anthropic.com/threat-intelligence-report-september-2026
- Anthropic TI PDF：https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf
- rubyhack.ai：https://www.rubyhack.ai/
- Fluid LimeSurvey：https://fluidattacks.com/advisories/payphone
- Florida DMV：https://www.bleepingcomputer.com/news/security/florida-confirms-dmv-database-breached-via-stolen-police-account/
