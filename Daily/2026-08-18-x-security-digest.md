# X 安全情报晚报 · 2026-08-18

> 搜集窗口：约过去 24 小时（圣地亚哥时间 2026-08-17 20:25 至 2026-08-18 20:15，America/Santiago / UTC-4）
> 主源：X 已登录 Latest（CVE／GitHub C2／APT 三路均收回；搜索 2／3 曾限流后重试成功）。公开备援已先出报，本节为 X 补录
> 公开备援：CISA KEV / NVD / MSRC / Apple / Broadcom / ReliaQuest / Microsoft / BleepingComputer / GitHub
> 规则：每条含完整 https URL；没有指标就写「未见公开 IoC」
> 说明：防御向晚报。不转载利用代码、payload 或复现步骤。

## 今日摘要

- **MLflow CVE-2026-64849（X 补录，CVSS 9.3）**：未认证 SSRF，watchTowr 称在野打云元数据。升到 3.15.0。
- **CoSnitch CVE-2026-24301（X 补录）**：Copilot Personal 一键外带。微软 8/18 已修，企业版不受影响。未见在野。
- **Operation CameraSwarm（X 补录）**：Hunt.io 称逾 1.4 万台大华摄像头被控。
- **CISA KEV 一次加四条（catalog 2026.08.18，1670 条，联邦期限 8/21）**：CVE-2026-33824 Windows IKE 双重释放 RCE（CVSS 9.8，新）；CVE-2026-55040 SharePoint 弱认证绕过（CVSS 9.1，新）；CVE-2026-59310 vCenter 路径穿越、CVE-2026-65400 macOS Screen Sharing 此前已报，本日入 KEV。
- **Clop 定制 Windchill JSP webshell**：ReliaQuest 拆 CVE-2026-12569 后续植入，哈希与 IP 见下文。
- **MacSync Stealer**：微软 8/18 用行为轴扩出 31 个轮换域名。无样本哈希。
- **工具**：nuclei-templates 仍为 v10.4.7。本窗口新建 c2probe 等仓。
- Ray CVE-2025-62593 仍在 KEV（期限 8/20），不重复展开。

## CVE / POC / 漏洞

### 1. CISA KEV 2026.08.18 新增四条（期限 2026-08-21）

CISA 于 2026-08-18T16:52:08Z 发布 catalogVersion 2026.08.18，条目 1670（昨日 1666）。四条 dateAdded 均为 8/18，knownRansomwareCampaignUse 均为 Unknown。BOD 26-04 联邦期限 2026-08-21。

地址：
- 通报：https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog
- 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

X：https://x.com/__kokumoto/status/2089856032860422230
X：https://x.com/notCVE/status/2089809155104129105

IoC：未见公开 IoC。

### 2. CVE-2026-33824 Microsoft IKE Service Extensions 双重释放（CVSS 9.8，新入 KEV）

Windows IKE Extension 双重释放（CWE-415），未授权攻击者可经网络执行代码。CNA CVSS 3.1 9.8。CISA-ADP 于 8/18 标 exploitation=active。MSRC 更新指南页为 JS 应用，正文未抓到；以 NVD／KEV 为准。

地址：
- 厂商：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33824
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-33824
- CISA：https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC。

### 3. CVE-2026-55040 Microsoft SharePoint 弱认证（CVSS 9.1，新入 KEV）

SharePoint 弱认证（CWE-1390），未授权可经网络绕过安全特性。CVSS 3.1 9.1。NVD 受影响：SharePoint 2016（修 16.0.5561.1001）、2019（16.0.10417.20175）、Subscription Edition（16.0.19725.20434）。CISA-ADP 8/18 从 poc 改为 active。

地址：
- 厂商：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-55040
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-55040
- CISA：https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC。

### 4. CVE-2026-59310 vCenter／CVE-2026-65400 macOS 入 KEV（昨日已列漏洞）

两条此前晚报已报漏洞本身。本日变化是入 KEV，联邦期限 8/21。vCenter 路径穿越（CWE-22）；macOS Screen Sharing 不当认证（CWE-287）。

地址：
- Broadcom：https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
- NVD vCenter：https://nvd.nist.gov/vuln/detail/CVE-2026-59310
- Apple：https://support.apple.com/en-us/148170
- NVD macOS：https://nvd.nist.gov/vuln/detail/CVE-2026-65400

IoC：未见公开 IoC。


### 5. MLflow CVE-2026-64849（X 补录，CVSS 9.3，据称在野）

X 本日流传。MLflow <3.15.0 未认证 webhook /test 接口存在全读 SSRF：URL 校验不跟重定向／DNS 重绑定，可打内网或云元数据并回显响应。GitHub Advisory GHSA-7gwp-5pfp-969j。watchTowr／Cybersecuritynews 称披露后数小时蜜罐见到打暴露 Tracking Server、偷云凭证。升到 3.15.0，限制 Tracking Server 出站，轮换可能暴露的云凭证。本晚报不转载复现步骤。

X：https://x.com/CyberAlertsHQ/status/2089812647680393520

地址：
- 厂商 Advisory：https://github.com/mlflow/mlflow/security/advisories/GHSA-7gwp-5pfp-969j
- 补丁：https://github.com/mlflow/mlflow/commit/ba949522477cbd5915aa55d29b0cfad7d5ddf939
- 文章：https://cybersecuritynews.com/mlflow-ssrf-vulnerability/

IoC：未见公开 IoC。

### 6. CoSnitch CVE-2026-24301（X 补录；Copilot Personal）

Varonis Threat Labs 8/18 公开：Copilot Personal 一键链可自动跑提示并从已连接应用外带数据。微软同日补丁，CVSS 8.8；企业 Copilot 不受影响，官方称用户无需操作。Varonis 未见在野。本晚报不转载构造参数。

X：https://x.com/DFIR_Radar/status/2089805567174889585

地址：
- Varonis：https://www.varonis.com/blog/cosnitch
- 文章：https://www.darkreading.com/vulnerabilities-threats/cosnitch-attack-copilot-mapping-out-architecture
- 文章：https://thehackernews.com/2026/08/microsoft-copilot-personal-flaws-could.html

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### nuclei-templates 版本核对

最新标签仍为 v10.4.7（2026-08-03），本窗口无新版本。
https://github.com/projectdiscovery/nuclei-templates/releases
https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.7

IoC：未见公开 IoC。

### 本窗口新建 GitHub（仅列 URL，未逐仓核实）

- https://github.com/kurokuma/c2probe （高速 C2 IP 发现）
- https://github.com/pbyhre/red-team-tools
- https://github.com/payload10/RT-Recon
- https://github.com/controleFG2/C2-Server （无描述）

昨日已列 meridian 不展开。

X 补录：
- Nuclei 检测模板 CVE-2026-19478：https://x.com/DhiyaneshDK/status/2089806779526025511
- DutchOven：https://github.com/loosehose/DutchOven （https://x.com/ipurple/status/2089678908807344154）
- Decepticon：https://github.com/PurpleAILAB/Decepticon （https://x.com/AiAdventurerx/status/2089623333880869085）

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. Clop 定制 PTC Windchill JSP webshell（CVE-2026-12569 后续）

ReliaQuest（本日）+ BleepingComputer（2026-08-18 13:29）：在 CVE-2026-12569（CVSS 9.3）利用后部署的 JSP 不是通用壳，而是导入 Windchill 类 MethodContext、WTConnection、WTKeyStoreUtil，用应用自身身份查库、解密 keystore、枚举文件库。控制走 HTTP 头 X-windchill-req（8 字符）；E 命令回显走 X-windchill-prm；L 命令把库清单写到 flst.txt。ReliaQuest 高置信归属 Clop。漏洞与 KEV 入目在 6 月已报；本日新的是定制植入分析与 IoC。防御：打补丁、搜 windchill/codebase 与 /Windchill/login/ 下异常 JSP、轮换 LDAP/keystore。本晚报不转载命令细节。

地址：
- ReliaQuest：https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign/
- 文章：https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/
- 厂商：https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-rce-vulnerability
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-12569
- Ransom-ISAC：https://ransom-isac.org/blog/clop-windchill-flexplm-exploitation/

地址／IoC（ReliaQuest／厂商，防御复制）：
- SHA-256（ReliaQuest 定制壳）：321e1fb01eb3462b48ff6ccdef132acc1182e3f7456548439f0d4ead12fd98bf
- SHA-256（PTC／Ransom-ISAC 已知 JSP）：55a1eb4c2d3da04376df39d7ba832569c6af1a37a0cf2b95f754ac898023a30c
- IP：5.180.41.35 ；78.128.113.10 ；104.194.9.14 ；104.243.35.63 ；185.227.83.236 ；209.222.98.44 ；216.152.151.204
- 头：X-windchill-req ；X-windchill-prm
- 文件：flst.txt

### 2. Microsoft：用行为轴扩 MacSync Stealer 轮换 C2（31 域）

Microsoft Defender Experts（2026-08-18）在 RST Cloud 早前 MacSync 笔记上，用 /curl/、/dynamic?txd=、/gate?buildtxd= 与 upload_id／chunk_index／total_chunks 等持久请求形状扩到 30+ 轮换域名。ClickFix 诱骗终端粘贴后 curl 取载荷，数据落到 /tmp/sync* 再打成 /tmp/osalogging.zip 分块 PUT。无样本哈希。域名是时点 IoC，优先打行为轴。

地址：
- 厂商：https://www.microsoft.com/en-us/security/blog/2026/08/18/hunting-macsync-stealer-infrastructure-through-behavioral-pivots/

地址／IoC（微软原文，防御复制）：
- URI：/curl/ ；/dynamic?txd= ；/gate?buildtxd=
- 参数：upload_id= ；chunk_index= ；total_chunks=
- 路径：/tmp/osalogging.zip ；/tmp/sync*
- 域名：aihealthring[.]com ；cabinrentalsnc[.]com ；chatbasedos[.]com ；commercialroofingsd[.]com ；dogtrainersgeorgia[.]com ；fintelliganceai[.]com ；homeinspectionsdelaware[.]com ；intopython[.]com ；lalandscapelighting[.]com ；lumenagnet[.]com ；marbellaresales[.]com ；miamipcsupport[.]com ；moldinspectiondayton[.]com ；nailscanai[.]com ；newjerseypetsitter[.]com ；numericagent[.]com ；oaklandwaterdamage[.]com ；oklahomawarehousing[.]com ；olympiapetemergency[.]com ；peaecagent[.]com ；plasmaticsystems[.]com ；plethorawallet[.]com ；premierrentalpurchase[.]com ；ricewaterbeauty[.]com ；rvieragent[.]com ；sandiegotkd[.]com ；secueragent[.]com ；shiledagent[.]com ；syracusefertilitycenter[.]com ；vastbets[.]com ；wvaeagent[.]com

### 3. Operation CameraSwarm（X 补录）

Hunt.io：逾 1.4 万台大华摄像头（乌／俄）经弱口令、CVE 绕过与 P2P 中继被控，可拿云恢复码。推文未列哈希。

X：https://x.com/Cyber_O51NT/status/2089862113275617709
文章：https://hunt.io/blog/operation-cameraswarm-dahua-cameras-compromised
IoC：未见公开 IoC（推文未列；详见 Hunt.io）。

### 4. Rapid7 Q2 2026 威胁景观（无 IoC）

季报：Q2 新增高危／严重 CVE 8539 条（同比约翻倍），新被利用洞仍约 40。无认证利用占比升至 62%。与 ASTERIX 无关。

地址：https://www.rapid7.com/blog/post/tr-new-report-ai-threats-q2-2026-ends-traditional-patch-cycles/
IoC：未见公开 IoC。

## 地址／IoC 汇总

### URL
- https://x.com/__kokumoto/status/2089856032860422230
- https://x.com/CyberAlertsHQ/status/2089812647680393520
- https://x.com/DFIR_Radar/status/2089805567174889585
- https://github.com/mlflow/mlflow/security/advisories/GHSA-7gwp-5pfp-969j
- https://www.varonis.com/blog/cosnitch
- https://hunt.io/blog/operation-cameraswarm-dahua-cameras-compromised
- https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33824
- https://nvd.nist.gov/vuln/detail/CVE-2026-33824
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-55040
- https://nvd.nist.gov/vuln/detail/CVE-2026-55040
- https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
- https://nvd.nist.gov/vuln/detail/CVE-2026-59310
- https://support.apple.com/en-us/148170
- https://nvd.nist.gov/vuln/detail/CVE-2026-65400
- https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign/
- https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/
- https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-rce-vulnerability
- https://nvd.nist.gov/vuln/detail/CVE-2026-12569
- https://www.microsoft.com/en-us/security/blog/2026/08/18/hunting-macsync-stealer-infrastructure-through-behavioral-pivots/
- https://github.com/kurokuma/c2probe
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.7

### Clop Windchill
- 321e1fb01eb3462b48ff6ccdef132acc1182e3f7456548439f0d4ead12fd98bf
- 55a1eb4c2d3da04376df39d7ba832569c6af1a37a0cf2b95f754ac898023a30c
- 5.180.41.35
- 78.128.113.10
- 104.194.9.14
- 104.243.35.63
- 185.227.83.236
- 209.222.98.44
- 216.152.151.204

### MacSync Stealer 域名
- aihealthring[.]com
- cabinrentalsnc[.]com
- chatbasedos[.]com
- commercialroofingsd[.]com
- dogtrainersgeorgia[.]com
- fintelliganceai[.]com
- homeinspectionsdelaware[.]com
- intopython[.]com
- lalandscapelighting[.]com
- lumenagnet[.]com
- marbellaresales[.]com
- miamipcsupport[.]com
- moldinspectiondayton[.]com
- nailscanai[.]com
- newjerseypetsitter[.]com
- numericagent[.]com
- oaklandwaterdamage[.]com
- oklahomawarehousing[.]com
- olympiapetemergency[.]com
- peaecagent[.]com
- plasmaticsystems[.]com
- plethorawallet[.]com
- premierrentalpurchase[.]com
- ricewaterbeauty[.]com
- rvieragent[.]com
- sandiegotkd[.]com
- secueragent[.]com
- shiledagent[.]com
- syracusefertilitycenter[.]com
- vastbets[.]com
- wvaeagent[.]com

## 来源搜索 URL

- https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&src=typed_query&f=live
- https://x.com/search?q=(APT%20OR%20malware)%20(analysis%20OR%20report)&src=typed_query&f=live
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog
- https://github.com/projectdiscovery/nuclei-templates/releases
