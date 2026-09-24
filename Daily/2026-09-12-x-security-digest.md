# X 安全情报晚报 · 2026-09-12

> 搜集窗口：圣地亚哥时间 **2026-09-11 20:00 至 2026-09-12 ~20:29**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周六）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-12.json`（collected_at **2026-09-12T20:15:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-12.md`＋ `/workspace/enrich-2026-09-12/`。CISA KEV catalogVersion **2026.09.11**／**1709** 条／dateReleased **2026-09-11T19:32:16.8993Z**（相对昨日 **+0**；无新 KEV 入目）。
> **期限今日 09-12：Citrix NetScaler CVE-2026-19490、Fortinet CVE-2025-25249、Cisco FMC CVE-2026-20079。期限明日 09-13：MikroTik RouterOS CVE-2026-67277／CVE-2026-86060。** Sep2 五条联邦 BOD（Kestra／JFrog／Sangoma／SonicWall×2）自 **09-05** 起仍 **OVERDUE**。TrueConf **CVE-2026-72530**／MLflow **CVE-2026-64849**／JFrog **CVE-2026-66384** 仍逾期；Magento **75650**／N-able **86218**（09-11）亦逾期。due_near：ScreenConnect／GitLab／PaperCut（**09-14**）；LiteLLM／Starlette（**09-16**）；Chromium **85046**（**09-18**）；微软两在野（**09-22**）；Chromium **87491**（**09-23**）；JFrog **42016／42018**（**09-25**）。
> X：`/workspace/x-posts-2026-09-12.json`（合并 **32** 条唯一：A3／B7／C11／LWiS11；**0** 重叠；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.5h**（salvage；远不足 24h）。Search B 约 **45h**（3 滚后已超 24h 停）。Search C 约 **2h**（10 滚硬限）。LWiS List 约 **41h** 扫描，但雪花时间戳显示保留帖多在窗口起点之前（作交叉，不假装为本窗口 Latest）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · 今日 due · Cisco FMC 20079】** KEV due **今日 09-12**。Talos 跟踪三簇：UAT-12197（web shell／cmd.jar）、UAT-11823（Sandworm 关联／Cyclops Blink）、UAT-11988（Qilin 关联）。厂商热修；IoC 含 `/var/tmp/license.tmp` 与多 IP／哈希。
  Talos：https://blog.talosintelligence.com/fmc-ongoing-exploitation/
  IoC 仓库：https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.txt
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
  SecurityWeek：https://www.securityweek.com/organizations-warned-of-cisco-secure-fmc-exploitation/
  SecurityAffairs：https://securityaffairs.com/198884/cyber-crime/attackers-exploit-critical-cisco-fmc-flaw-to-deploy-qilin-ransomware.html

- **【今日 due · Citrix／Fortinet】** Citrix NetScaler **CVE-2026-19490**（修 **14.1-73.32+／13.1-63.21+** 等）；Fortinet **CVE-2025-25249**（厂商页可能 Cloudflare 阻断）。
  Citrix：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
  Fortinet：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-19490 · https://nvd.nist.gov/vuln/detail/CVE-2025-25249

- **【明日 due · MikroTik】** **CVE-2026-67277／86060** due **09-13**；CERT.pl IoC IP 仍见。
  厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
  CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/

- **【X · SharePoint 链】** Rapid7 提前公布 **CVE-2026-63520**（SharePoint RCE）技术分析；可与已入 KEV 的 **CVE-2026-55040**（JWT 认证绕过，due 已过）串联。X @MalwareBibleJP 交叉。
  Rapid7 RCE：https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-remote-code-execution-cve-2026-63520/
  Rapid7 认证绕过：https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-jwt-token-authentication-bypass-cve-2026-55040/
  MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-63520 · https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-55040
  X：https://x.com/MalwareBibleJP/status/2098912546669695200

- **【X · GitLab 85706 狩猎】** KEV due **09-14**；X 见 Nuclei 检测 PR；LWiS／媒体称披露后数小时即有野外探测。
  Nuclei PR：https://github.com/projectdiscovery/nuclei-templates/pull/17231/files
  X：https://x.com/rxerium/status/2098812887200395469
  补丁：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
  THN：https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html

- **【续 · PaperCut／GreyNoise】** KEV due 仍 **09-14**；X Search C 大量转载 GreyNoise「AI 编排」战役。
  GreyNoise：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
  PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
  X：https://x.com/kysstalol/status/2098911662862663884

- **【威胁报告 · Anthropic TI】** 续报 Sep2026 TI（含 GTG／蒸馏等叙事）；X／LWiS 多条二次报道。
  报告：https://www.anthropic.com/threat-intelligence-report-september-2026
  PDF：https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf

- **【新闻 · Risky／tl;dr／工具】** KEV **+0**；Risky 仍 **RBNEWS612**；tl;dr 仍 **#345**；Sliver **v1.7.7**／nuclei-templates **v10.4.8** 无升版；ICS 无 Sep12 新项。
  https://risky.biz/RBNEWS612/
  https://tldrsec.com/p/tldr-sec-345

## CVE / POC / 漏洞

### 1. 【今日 due】Cisco FMC CVE-2026-20079（＋CVE-2026-20316 链式）

认证绕过（CVSS **10.0**），未认证可向 FMC Web 管理面发构造请求并获 root。Talos：UAT-12197／UAT-11823（Sandworm 工具重叠／Cyclops Blink）／UAT-11988（Qilin）。热修防未来利用，**不清除既有沦陷**；发现 IoC 联系 Cisco TAC。Cloud-delivered FMC 不受影响（厂商叙述）。防御：打补丁、限制管理面暴露、狩猎 `license.tmp`／web shell／Cyclops Blink。

地址：
- Talos：https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- IoC txt：https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.txt
- IoC json：https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.json
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-20079
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- SecurityWeek：https://www.securityweek.com/organizations-warned-of-cisco-secure-fmc-exploitation/

IoC（Talos 公开表／仓库，原样）：
- 路径／文件：`/var/tmp/license.tmp`；`home.jsp`；`cmd.jar`；`package_info.pl`
- SHA256：`B037f45e02a289325a1a5eb0d4db6a9fce9954fd0fdfd07162cb4eb2acbef77d`（home.jsp）；`Db491181ece3f319de6567ab6f6daa90c6879911cd890155e6b7d8cc7a1a8c8e`（cmd.jar）；`6f98add5d1a7729192b6ad8491d85c505c64836f7881742d6b93bd8e3d2fe461`（Cyclops Blink）
- IP：`89.34.96.56`；`208.123.119.215`；`104.218.165.253`；`91.214.78.118`；`43.204.2.142`

### 2. 【今日 due】Citrix NetScaler CVE-2026-19490

认证绕过（Gateway／AAA 等配置场景）。修复方向含 **14.1-73.32+**、**13.1-63.21+**、FIPS 相关分支等（以厂商表为准）。

地址：
- 厂商：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-19490
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC（厂商页本轮未抽出独立指标表）。

### 3. 【今日 due】Fortinet CVE-2025-25249

FortiOS／FortiSwitchManager／FortiSASE 等堆溢出 → 未授权代码／命令执行叙事。厂商页本轮可能被 Cloudflare 拦截，以 PSIRT／KEV／NVD 为准。

地址：
- 厂商：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2025-25249
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC（本轮公开页）。

### 4. 【明日 due】MikroTik RouterOS CVE-2026-67277／CVE-2026-86060

KEV due **09-13**。厂商 Sep2026 公告＋CERT.pl 活跃利用说明。

地址：
- 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67277 · https://nvd.nist.gov/vuln/detail/CVE-2026-86060

IoC：IP `82.192.72.4` · `103.102.31.18`（CERT.pl）。

### 5. 【KEV 续 · due 09-14】GitLab CVE-2026-85706

commits API 路径穿越 → 未认证任意文件读（CVSS **10.0**）。修 **19.3.2／19.2.6／19.1.8**。X／媒体称披露后迅速出现探测；Nuclei 模板 PR 可用。

地址：
- CISA 告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-one-known-exploited-vulnerability-catalog
- 补丁：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
- Nuclei PR：https://github.com/projectdiscovery/nuclei-templates/pull/17231/files
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85706
- X：https://x.com/rxerium/status/2098812887200395469
- LWiS／THN：https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html · https://x.com/Dinosn/status/2098480407121461502

IoC：未见公开利用 IoC（本轮以狩猎／补丁为主）。

### 6. 【KEV 续 · due 09-14】ConnectWise ScreenConnect CVE-2026-84869／JFrog 42016／42018

昨报已详；目录未变。修 ScreenConnect **26.6.5**；JFrog 见厂商 advisories（due **09-25**）。

地址：
- CISA 三洞：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- ScreenConnect：https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin
- JFrog：https://docs.jfrog.com/releases/docs/jfrog-security-advisories

IoC：未见公开 IoC。

### 7. 【X · SharePoint】CVE-2026-63520 ＋ CVE-2026-55040

Rapid7：63520 为 BCS 不安全类型实例化 RCE；与 **55040**（JWT 认证绕过，已入 KEV，due **2026-08-21**）可形成未认证 RCE 链。防御：打微软 Aug2026 相关更新（KB 以 MSRC 为准）；勿复现 PoC。

地址：
- Rapid7 63520 分析：https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-remote-code-execution-cve-2026-63520/
- Rapid7 55040 分析：https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-jwt-token-authentication-bypass-cve-2026-55040/
- Rapid7 披露：https://www.rapid7.com/blog/post/etr-cve-2026-63520-microsoft-sharepoint-remote-code-execution-fixed/
- MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-63520 · https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-55040
- 仓库（仅作参考，不展开步骤）：https://github.com/sfewer-r7/CVE-2026-55040
- X：https://x.com/MalwareBibleJP/status/2098912546669695200

IoC：未见公开 IoC（官方分析以补丁／配置加固为主）。

### 8. 【X】PAN-OS CVE-2026-0310

管理面 XML 处理缓冲区溢出叙事（需网络可达管理面）。续跟踪厂商公告。

地址：
- 厂商：https://security.paloaltonetworks.com/CVE-2026-0310
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-0310
- X：https://x.com/modokey/status/2098907345963426295

IoC：未见公开 IoC。

### 9. 【X】Keycloak CVE-2026-18963（续）

&lt; 26.7.2 重置凭证路径未认证账户接管叙事；Nuclei 模板／上游 issue。

地址：
- Nuclei PR：https://github.com/projectdiscovery/nuclei-templates/pull/16995/files
- Issue：https://github.com/keycloak/keycloak/issues/51833
- X：https://x.com/Dz10Chiheb/status/2098498451751277002

IoC：未见公开 IoC。

### 10. 【续 · PaperCut】CVE-2026-81578／82078（due 09-14）

维护版仍 **26.0.5／25.0.13／24.1.10**；bulletin last_updated 仍 **September 10, 2026**。GreyNoise AI 战役续在 X 传播。

地址：
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- GreyNoise：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
- X：https://x.com/kysstalol/status/2098911662862663884 · https://x.com/webspired_/status/2098909681607451103

IoC：IP `45.142.193.132` · `45.158.196.75`；账户名提示 `Administrator17`；MD5（GreyNoise）：`528cd4e69ecfa5191adbcf6ef28667bf` · `ce870a91e8d27e8f663f0687abc60b04` · `a6437ac3d6798090a218520985d36a3f` · `fc92dfafa7aa741c5f2b9cbcf75d1d19` · `974decb9ff4c8f9ccb0937c96d513347`。

## 工具与 GitHub 发布

### 1. Nuclei 模板 · GitLab CVE-2026-85706

地址：
- PR：https://github.com/projectdiscovery/nuclei-templates/pull/17231/files
- X：https://x.com/rxerium/status/2098812887200395469
- nuclei：https://github.com/projectdiscovery/nuclei

IoC：未见公开 IoC。

### 2. Claude-Red（红队技能库）

地址：
- 仓库：https://github.com/SnailSploit/Claude-Red
- X：https://x.com/LFrefman/status/2098726276836295052

IoC：未见公开 IoC。

### 3. ipblocklist（入／出站封锁，阻 C2）

地址：
- 仓库：https://github.com/bitwire-it/ipblocklist
- X：https://x.com/tom_doerr/status/2098900453480083837

IoC：未见公开 IoC。

### 4. Metasploit wrap-up（16 模块）

覆盖 Cisco／SonicWall／JetBrains／PaperCut／Langflow 等（官方总结；不展开利用步骤）。

地址：
- Rapid7：https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-goes-to-sixteen/
- X：https://x.com/metasploit/status/2098469199483990522 · https://x.com/kmkz_security/status/2098473184488210939

IoC：未见公开 IoC。

### 5. Sliver／nuclei-templates 版本脉冲

本日无显著更新：Sliver 仍 **v1.7.7**；nuclei-templates 仍 **v10.4.8**。

地址：
- https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

### 6. 其他

- Bitcoin Core RPC／REST 缓冲相关 PR（红队发现叙述，非共识）：https://github.com/bitcoin/bitcoin/pull/36174 · X https://x.com/nvee3/status/2098221540525343066
- Beacon 2026／Crystal Palace 演讲预告：https://info.fortra.com/beacon-2026 · X https://x.com/_RastaMouse/status/2098455283353674168

## APT / Malware 分析

### 1. Cisco FMC 三簇（UAT-12197／11823／11988）

见 CVE 节主条。Sandworm 工具重叠＋Cyclops Blink；Qilin 关联侦察／勒索部署叙事。

地址：
- https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.txt

IoC：见 CVE 节 Cisco 条。

### 2. Anthropic Threat Intelligence · September 2026（续）

X／LWiS 多条转载（含中国实验室蒸馏、Claude agent 滥用等二次报道）。以官方报告／PDF 为准。

地址：
- https://www.anthropic.com/threat-intelligence-report-september-2026
- https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf
- THN 蒸馏：https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html
- X 样例：https://x.com/IAenBruto/status/2098889986837770719 · https://x.com/MichaelARothman/status/2098886288686698961 · https://x.com/Dinosn/status/2098483522931499122

IoC：未见本轮从报告页新抄公开 IoC（以官方 PDF／附录为准）。

### 3. PaperCut AI 编排战役（GreyNoise）

见 CVE／PaperCut 节。

### 4. 暗网／勒索声称（未独立核验）

- IP-PBX 0day 叫卖：https://x.com/DailyDarkWeb/status/2098914486988259376
- 智利诊所数据声称：https://x.com/VECERTRadar/status/2098902813669777759
- 政府／机场／军事 shell 叫卖声称：https://x.com/VECERTRadar/status/2098902123371282435
- 利比亚电信勒索声称：https://x.com/intels_daily/status/2098896211939901686
- Senheng 客户记录声称：https://x.com/DailyDarkWeb/status/2098873826528420262

IoC：未见可核验公开 IoC（声称级）。

### 5. 其他威胁基础设施帖

- `81.70.21.248`（帖内写为 `81[.]70.21.248`）：https://app.etugen.io/trashpile/81.70.21.248 · X https://x.com/etugenio/status/2098900906615918981
- CyberGlobes／间谍软件监控报道：https://haaretz.com/israel-news/security-aviation/2026-09-10/ty-article-magazine/.premium/targeted-gays-and-protesters-the-israeli-cyber-firm-quietly-arming-autocrats/000001a0-8bb2-d219-a3ed-bffa9bb70000 · X https://x.com/jsrailton/status/2098437440180535776

## 地址／IoC 汇总

- **今日 due · Cisco FMC**：路径 `/var/tmp/license.tmp`；`home.jsp`／`cmd.jar`；SHA256 `B037f45e02a289325a1a5eb0d4db6a9fce9954fd0fdfd07162cb4eb2acbef77d` · `Db491181ece3f319de6567ab6f6daa90c6879911cd890155e6b7d8cc7a1a8c8e` · `6f98add5d1a7729192b6ad8491d85c505c64836f7881742d6b93bd8e3d2fe461`；IP `89.34.96.56` · `208.123.119.215` · `104.218.165.253` · `91.214.78.118` · `43.204.2.142`。
- **今日 due · Citrix／Fortinet**：未见公开 IoC。
- **明日 due · MikroTik**：IP `82.192.72.4` · `103.102.31.18`。
- **PaperCut／GreyNoise**：IP `45.142.193.132` · `45.158.196.75`；`Administrator17`；上述 MD5 五条。
- **基础设施帖**：`81.70.21.248`（etugen）。
- **SharePoint／GitLab／Keycloak／PAN-OS／ScreenConnect／JFrog**：本轮写「未见公开 IoC」或仅补丁／狩猎。
- **KEV 逾期提醒**：Kestra 49869／JFrog 82329／Sangoma 9586／SonicWall 83548+83549；TrueConf 72530／MLflow 64849／JFrog 66384；Magento 75650／N-able 86218。

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

- X Latest A（CVE/POC）：https://x.com/search?q=(CVE%20OR%20POC%20OR%20exploit%20OR%200day%20OR%20%220-day%22)%20-filter%3Areplies&src=typed_query&f=live
- X Latest B（GitHub 工具／C2）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20mythic%20OR%20havoc)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware／threat）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS612：https://risky.biz/RBNEWS612/
- Risky SRB183：https://risky.biz/SRB183/
- Risky RBNEWS611：https://risky.biz/RBNEWS611/
- tl;dr sec：https://tldrsec.com/
- tl;dr #345：https://tldrsec.com/p/tldr-sec-345
- tl;dr #345（blog 路径）：https://tldrsec.com/blog/tldr-sec-345/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 09-11 三洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- CISA 09-11 一洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-one-known-exploited-vulnerability-catalog
- Talos FMC：https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- Talos IoC：https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.txt
- Cisco FMC 顾问：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- Citrix CTX696939：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- Fortinet FG-IR-25-084：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl MikroTik：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- Rapid7 SharePoint 63520：https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-remote-code-execution-cve-2026-63520/
- Rapid7 SharePoint 55040：https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-jwt-token-authentication-bypass-cve-2026-55040/
- GitLab 补丁：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- GreyNoise PaperCut：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
- Anthropic TI：https://www.anthropic.com/threat-intelligence-report-september-2026
- ConnectWise ScreenConnect：https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin
- JFrog advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
