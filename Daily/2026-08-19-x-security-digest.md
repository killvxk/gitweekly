# X 安全情报晚报 · 2026-08-19

> 搜集窗口：约过去 24 小时（圣地亚哥时间 2026-08-18 20:30 至 2026-08-19 20:10，America/Santiago / UTC-4）
> 主源：X 已登录 Latest 后到（三路均有回收；搜索 1 Latest 在 ~19:33Z / 圣地亚哥 16:33 报错耗尽，since/until 空时间线，窗口前约 16 小时 CVE 检索不全。搜索 2/3 曾限流后成功；搜索 2 Latest 从 16:34Z 直接跳到 7 月，仅 4 条窗口内）。公开备援已先出报，本节为 X 补录。
> 公开备援：CISA KEV / CISA 警报与 CSA / NVD / Cisco PSIRT / GitHub / Huntress / Siemens CERT / BleepingComputer
> 规则：每条含完整 https URL；没有指标就写「未见公开 IoC」；不编造 CVE、URL、哈希、日期、推文或 IoC。
> 说明：防御向晚报。不转载利用代码、payload 或复现步骤。

## 今日摘要

- **CISA KEV catalogVersion 2026.08.19（1671 条，+1）**：新入 KEV 的是 MLflow SSRF **CVE-2026-64849**（CWE-918，dateAdded 2026-08-19）。漏洞本身昨日已作披露；本日新的是入 KEV、CISA-ADP exploitation=active，联邦期限 2026-09-02。补丁 MLflow 3.15.0。勒索活动字段 Unknown。BOD 26-04。
- **Cisco PSIRT 2026-08-19 16:00 GMT**（预告 cisco-sa-notice-LDquvx5d v2.1 Final）：Crosswork 与 Secure Workload 各一组 Critical 10.0；另有 BroadWorks XXE、CUIC SQLi、RoomOS USB 溢出、IE 1000 XSS/DoS、PCCE/UCCE SSRF。IE XSS / RoomOS 官方称未见已知恶意利用。
- **AA26-231A（NSA/CISA/FBI/DOE/EPA，2026-08-19）**：未归属行为体对美国西门子 S7 系列 PLC 做侦察与能力准备；AI 生成 Python 工具掺入 snap7.dll / python-snap7，伪装成 OT 监测，走 S7comm。评估为持续侦察／预置，非已归因 APT 行动。
- **Huntress LSHIY／Azure CLI ROPC 口令喷洒**：BleepingComputer 2026-08-19 10:00 复述 Huntress 研究。活动本身在 6–7 月，8/19 是公开复述而非新战役起点。
- **美国司法部起诉 17 名伊朗人（Mabna Institute）**：约 34 亿美元知识产权窃取。BC 2026-08-19 11:56。无技术 IoC。
- **工具**：窗口内新见公开仓 SinyC2、sliver-defense-evasion（仅列 URL，未克隆）。nuclei-templates 仍为 v10.4.7（2026-08-03），无新版本。
- **Citrix NetScaler CVE-2026-19490（X 补录，CVSS v4 9.3）**：认证绕过（CWE-288）；同批 CVE-2026-19489 内存溢出 DoS（8.8）。Rapid7 ETR 2026-08-19 未见在野。修 14.1-73.32／13.1-63.21／FIPS 14.1-73.32／13.1-37.277。
- **WordPress 插件双洞（X 补录）**：W3 Total Cache **CVE-2026-18051** 未认证任意文件写（CISA-ADP CVSS 10.0，< 2.10.5，升 2.10.5）；Elementor Pro **CVE-2026-32475** 未认证危险文件上传（Patchstack 9.0，≤4.2.1，修 4.2.2）。均 CISA-ADP exploitation=none。
- **SilkParasite（Bitdefender Labs，X 补录）**：中等把握中国背景，打中亚政府。7 个 RAT，5 个新命名（DriveSilkRAT／CookiETagRAT／NomadRAT／GoginRAT／NodeEdgeRAT）。DriveSilkRAT 用 Google Drive 作 C2。
- **Maya Protocol／MAYAChain 2026-08-19 停网（X 补录）**：六缺陷链式会计错误，约 20 BTC／$1.4–1.7M。未见核验钱包／哈希。
- 短提醒（昨日已展开，不重复）：Ray **CVE-2025-62593** KEV 期限 2026-08-20；昨日四条 KEV **CVE-2026-33824 / 55040 / 59310 / 65400** 期限 2026-08-21。

## CVE / POC / 漏洞

### 1. CISA KEV 新列入 CVE-2026-64849（MLflow SSRF；catalog 2026.08.19）

CISA 于 2026-08-19T17:00:32.1366Z 发布 catalogVersion **2026.08.19**，条目 **1671**（昨日 2026.08.18／1670）。窗口内唯一新 dateAdded（2026-08-19）是 **CVE-2026-64849**：MLflow 服务端请求伪造（CWE-918），knownRansomwareCampaignUse=Unknown，联邦修复期限 **2026-09-02**（BOD 26-04）。CISA-ADP 于 2026-08-19T17:44:03.944227Z 将 SSVC exploitation 标为 active。厂商补丁为 **MLflow 3.15.0**。

该洞昨日晚报已作披露覆盖；本日新信息是入 KEV 与「已被利用」标注，不是新的漏洞发现。暴露的 MLflow Tracking Server 应按厂商说明升级，并按 BOD 26-04 做云服务侧风险排序。本晚报不转载接口路径或复现步骤。

地址：
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/08/19/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-64849
- 厂商 Advisory：https://github.com/mlflow/mlflow/security/advisories/GHSA-7gwp-5pfp-969j
- GitHub 发布：https://github.com/mlflow/mlflow/releases/tag/v3.15.0
- GitHub PR：https://github.com/mlflow/mlflow/pull/24258
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

X：https://x.com/__kokumoto/status/2090210638664732996

IoC：未见公开 IoC。

### 2. Cisco PSIRT 19 Aug 2026 16:00 GMT（cisco-sa-notice-LDquvx5d v2.1 Final）

Cisco 于 2026-08-19 16:00 GMT 发布当日安全公告集，预告编号 cisco-sa-notice-LDquvx5d，版本 2.1，状态 Final，日期 2026-AUG-19。PSIRT 称对 IE 1000 XSS 与 RoomOS 问题未见公开宣布或已知恶意利用。未见公开 IoC。按产品摘要如下（仅列官方已披露 CVE、评级与首修版本，不含利用细节）：

- **Crosswork Critical 10.0**：CVE-2026-20030 / CVE-2026-20357 / CVE-2026-20358 / CVE-2026-20359。首修 **7.2.1-SP**。
- **Secure Workload Critical 10.0**：CVE-2026-20231 / CVE-2026-20315 / CVE-2026-20317 / CVE-2026-20318 / CVE-2026-20319。首修 **3.10.9.1**（3.10 及更早）／**4.0.4.16**（4.0）。
- **BroadWorks XXE CVE-2026-20320** High 7.5：首修 **RI.2026.07**。
- **CUIC SQLi CVE-2026-20327** Medium 6.5：首修 **12.6(2) ES08**／**15.0(1) SU2**。
- **RoomOS USB 溢出 CVE-2026-20302** Medium 6.1：首修 **11.32.7.0**／**11.40.1.1**／**26.7.2.2**／**26.7.1.12**。
- **IE 1000 XSS CVE-2026-20232** 与 **DoS CVE-2026-20177**：首修 **1.9.6**。
- **PCCE/UCCE SSRF CVE-2026-20314**：首修 **15.0(1)ES202607**。

地址：
- 厂商预告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-LDquvx5d
- 厂商 Crosswork：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-crosswork-UzDTU9Vh
- 厂商 Secure Workload：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-csw1-shSvndWP
- 厂商 BroadWorks：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bworks-xxe-uwUd7CEt
- 厂商 CUIC：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cuic-sql-inject-2qbfWSm5
- 厂商 RoomOS：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-roomos-bof-vTMANZgu
- 厂商 IE 1000 XSS：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ie1k-NgXUFF52
- 厂商 IE 1000 DoS：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ie1k-uxq86Lnx
- 厂商 PCCE/UCCE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucce-pcce-ssrf-TghHxD
- NVD 示例：https://nvd.nist.gov/vuln/detail/CVE-2026-20030

IoC：未见公开 IoC。

### 3. CVE-2026-19490 Citrix NetScaler ADC/Gateway 认证绕过（X 补录，CVSS v4 9.3）

Citrix NetScaler ADC／Gateway 认证绕过（CWE-288），CVSS v4 **9.3**；同批 **CVE-2026-19489** 内存溢出 DoS（**8.8**）。Rapid7 ETR **2026-08-19**：未见在野。修复版本：**14.1-73.32**／**13.1-63.21**／FIPS **14.1-73.32**／**13.1-37.277**。受影响：Gateway SSL VPN／ICA／CVPN／RDP 或 AAA vserver；较新 build 还需 SAML action。未找到可核验的官方 CTX 编号，不编造。本晚报不转载复现步骤。

X：https://x.com/AverageITexpert/status/2090198465284288724

地址：
- Rapid7 ETR：https://www.rapid7.com/blog/post/etr-cve-2026-19490-critical-vulnerability-affecting-citrix-netscaler-adc-and-netscaler-gateway/
- 厂商：https://docs.netscaler.com/en-us/netscaler-console-service/instance-advisory/remediate-vulnerabilities-cve-2026-19490.html
- 文章：https://www.esecurityplanet.com/threats/netscaler-cve-2026-19490-lets-attackers-bypass-authentication/
- 文章：https://cybersecuritynews.com/critical-citrix-netscaler-vulnerability/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-19490

IoC：未见公开 IoC。未见在野。

### 4. CVE-2026-18051 W3 Total Cache 未认证任意文件写（X 补录，CISA-ADP CVSS 10.0）

W3 Total Cache 未认证任意文件写（CWE-22）。NVD published **2026-08-19**，WPScan 来源。影响 **< 2.10.5**。CISA-ADP SSVC exploitation=none。WPScan 称公开 PoC 计划 **2026-09-17**，本晚报不转载。升到 **2.10.5**。

X：https://x.com/45Hrsg/status/2090211866199126524

地址：
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-18051
- WPScan：https://wpscan.com/vulnerability/dc56cdd2-419b-4a64-9d2a-29dc7e79cb6d/
- 文章：https://securityonline.info/w3-total-cache-file-write-cve-2026-18051/

IoC：未见公开 IoC。未见在野。

### 5. CVE-2026-32475 Elementor Pro 未认证危险文件上传（X 补录，Patchstack CVSS 9.0）

Elementor Pro 未认证危险文件上传（CWE-434）。NVD published **2026-08-19**。影响 **≤4.2.1**，修 **4.2.2**。CISA-ADP exploitation=none。涉及 Forms 文件上传字段。本晚报不写复现步骤。

X：https://x.com/magicwp_io/status/2090225634022654237

地址：
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-32475
- Patchstack 文章：https://patchstack.com/articles/critical-unauthenticated-file-upload-to-rce-in-elementor-pro-plugin/
- Patchstack DB：https://patchstack.com/database/wordpress/plugin/elementor-pro/vulnerability/wordpress-elementor-pro-plugin-4-2-1-arbitrary-file-upload-vulnerability
- MagicWP：https://magicwp.io/blog/cve-2026-32475-elementor-pro-file-upload

IoC：未见公开 IoC。未见在野。

### 6. Maya Protocol／MAYAChain 2026-08-19 停网（X 补录）

Maya Protocol／MAYAChain 于 **2026-08-19** 停网：六缺陷链式会计错误，约 **20 BTC**／**$1.4–1.7M**。本晚报不写交易构造或复现。

X：https://x.com/Cryptorbix/status/2090227459249639607

地址：
- 文章：https://www.coindesk.com/markets/2026/08/19/maya-protocol-exploit-drains-bitcoin-and-other-assets-as-pool-value-drops-usd11-million
- 文章：https://cointelegraph.com/news/maya-protocol-1-7m-exploit-network-halt

IoC：未见核验钱包／哈希。

### 7. 短提醒（昨日已覆盖，不展开）

- Ray **CVE-2025-62593** 仍在 KEV，联邦期限 **2026-08-20**。
- 昨日四条 KEV **CVE-2026-33824**（Windows IKE）、**CVE-2026-55040**（SharePoint）、**CVE-2026-59310**（vCenter）、**CVE-2026-65400**（macOS）期限均为 **2026-08-21**。X：https://x.com/SOCMinute/status/2090213217129709768
- X 本日仍见暴露 macOS Screen Sharing（CVE-2026-65400 已覆盖）挖矿复述，不展开。X：https://x.com/Eidex_official/status/2090207432127443102

地址：
- CISA 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 1. SinyC2（新建公开仓，仅 URL）

GitHub 仓 https://github.com/sinyblack59-del/SinyC2 创建于 **2026-08-19T03:54:16Z**，描述为 “A simple Open-Source C2 framework for Red Teaming labs.” 本晚报仅记录 URL，**未克隆、不分析、不转载用法**。防御侧可把该仓 URL 当作出现面指标做监控／拦截清单。

地址：
- GitHub：https://github.com/sinyblack59-del/SinyC2

IoC：https://github.com/sinyblack59-del/SinyC2

### 2. sliver-defense-evasion（公开仓，仅 URL）

GitHub 仓 https://github.com/XyrL02/sliver-defense-evasion ，描述为 “Sliver C2 defense evasion tools and guide for authorized red team engagements”。本晚报仅记录 URL，**未克隆、不分析、不转载规避手法**。防御侧可把该仓 URL 当作出现面指标。

地址：
- GitHub：https://github.com/XyrL02/sliver-defense-evasion

IoC：https://github.com/XyrL02/sliver-defense-evasion

### 3. nuclei-templates 版本核对

projectdiscovery/nuclei-templates 最新标签仍为 **v10.4.7**（2026-08-03），本窗口无新版本。

地址：
- GitHub 发布页：https://github.com/projectdiscovery/nuclei-templates/releases

IoC：未见公开 IoC。

### 4. mythic_tailscale（Mythic C2 走 Tailscale，仅 URL，未克隆）

GitHub 仓 https://github.com/Yeeb1/mythic_tailscale ：Mythic C2 走 Tailscale。本晚报仅记录 URL，**未克隆、不分析、不转载用法**。防御：盯 Tailscale 异常出站。

X：https://x.com/PatchRequest/status/2090147690721989049

地址：
- GitHub：https://github.com/Yeeb1/mythic_tailscale

IoC：https://github.com/Yeeb1/mythic_tailscale

### 5. StummSchneide（DustHarbor PoC 植入仓，仅 URL）

GitHub 仓 https://github.com/iss4cf0ng/StummSchneide ，DustHarbor PoC 植入仓。本晚报仅记录 URL，**未克隆、不分析、不转载用法**。

X：https://x.com/iss4c_f0ng/status/2090144798154031261

地址：
- GitHub：https://github.com/iss4cf0ng/StummSchneide

IoC：https://github.com/iss4cf0ng/StummSchneide

### 6. InjectionRange（RAG/LLM 红队靶场，仅 URL）

GitHub 仓 https://github.com/17vivekupadhyay/InjectionRange ，RAG／LLM 红队靶场。本晚报仅记录 URL，**未克隆、不分析**。

X：https://x.com/17vivekupadhyay/status/2090161901535699054

地址：
- GitHub：https://github.com/17vivekupadhyay/InjectionRange

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. AA26-231A：防御针对西门子 S7 系列 PLC 的活跃威胁

联合网络安全建议 **AA26-231A**，日期 **August 19, 2026**，发布方 NSA／CISA／FBI／DOE／EPA。未归属行为体正对美国境内西门子 S7 系列 PLC 做侦察与能力开发：使用 AI 生成的 Python 工具，掺入 **snap7.dll**／**python-snap7**，伪装成合法 OT 监测软件，经 **S7comm** 做读写。涉及型号 **S7-200／S7-300／S7-400／S7-1200／S7-1500**（含 F 系列）。互联网暴露面扫描借助 Censys／ZoomEye。行业：关键制造、能源、水务、化工、食品、商业设施；国防工业基地（DIB）亦被点名。评估为持续侦察与预置，**未做归因**。公告未公布哈希。

高阶缓解（不含利用或复现步骤）：盘点固件并对照金样；按西门子指引打补丁；PLC 与互联网隔离；在边界阻断 **TCP/102**；在工程站以外狩猎 **snap7.dll**／**python-snap7**。

地址：
- CISA CSA：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a
- 厂商：https://www.siemens.com/cert
- 文章：https://www.bleepingcomputer.com/news/security/us-warns-of-ai-powered-attacks-on-siemens-plcs-in-critical-infrastructure/

地址／IoC（原文指标，无哈希）：
- snap7.dll
- python-snap7
- S7comm TCP/102
- Censys / ZoomEye scanning
- 型号 S7-200 / S7-300 / S7-400 / S7-1200 / S7-1500

### 2. Huntress LSHIY／Azure CLI ROPC 口令喷洒（8/19 公开复述）

BleepingComputer **2026-08-19 10:00** 复述 Huntress 对 Azure CLI 弃用 OAuth **ROPC** 授权、针对 Microsoft `/token` 的大规模口令喷洒研究。活动本身在 **2026 年 6–7 月**；8/19 是公开复述，**不是新战役起始日**。基础设施先后涉及 LSHIY（含 BYOIP IPv6）、FranTech，以及后续 3xK Tech IPv4。防御侧重点：全用户／全云应用／全客户端类型强制 MFA；禁用 ROPC；限制非管理员使用 Azure CLI。本晚报不转载攻击流程。

地址：
- 厂商／研究：https://www.huntress.com/blog/lshiy-password-spray-attack
- 文章：https://www.bleepingcomputer.com/news/security/password-spraying-attacks-surge-155x-as-hackers-exploit-mfa-gaps/

地址／IoC（Huntress／复述原文）：
- 2a0a:d683::/32（LSHIY AS32167；亦见 AS955）
- FranTech AS53667：2605:6400::/32 + 2605:6404::/32
- 后续 AS200373 3xK Tech IPv4
- OAuth ROPC against Azure CLI /token

### 3. 美国司法部起诉 17 名伊朗人（Mabna Institute）约 34 亿美元知识产权窃取

BleepingComputer **2026-08-19 11:56**：美国司法部起诉 17 名据称属黑客雇佣组织 Mabna Institute 的伊朗人，涉约 **34 亿美元**知识产权窃取。报道未给出技术 IoC。

地址：
- 文章：https://www.bleepingcomputer.com/news/security/us-charges-iranian-hackers-over-34-billion-intellectual-property-theft/

X：https://x.com/aviatrixtrc/status/2090098097678410020

IoC：未见公开 IoC。

### 4. SilkParasite（Bitdefender Labs，2026-08-19）

Bitdefender Labs（**2026-08-19**，Martin Zugec）：SilkParasite，中等把握中国背景，打中亚政府。7 个 RAT，5 个新命名：**DriveSilkRAT**、**CookiETagRAT**、**NomadRAT**、**GoginRAT**、**NodeEdgeRAT**；已知 **SpiceRAT**、**BloodAlchemy**。DriveSilkRAT 用 Google Drive 作 C2（约 65 个感染实例上限）。AI 辅助开发（非纯生成），中等把握。未见公开样本哈希（Bitdefender 称完整 IoC 在其 GitHub IOC 仓，本晚报未抄到具体哈希则不编）。

X：https://x.com/aviatrixtrc/status/2090158542565106018
X：https://x.com/checkleaked/status/2090076439781491188

地址：
- 厂商：https://businessinsights.bitdefender.com/silkparasite-tracking-china-nexus-apt-across-central-asia
- 文章：https://www.darkreading.com/threat-intelligence/silkparasite-central-asian-orgs-flurry-rats

地址／IoC（只抄 Bitdefender 正文已出现的，无哈希）：
- Google Drive 被滥用为 C2（DriveSilkRAT LOTS）
- NodeEdgeRAT C2 域名：evo.hoster-kg.com（原文 evo[.]hoster-kg[.]com；伪装 Kyrgyz hoster.kg）
- 计划任务：SysEdgeUpdateTaskMachineCore（NodeEdgeRAT）
- BloodAlchemy 持久化名：fl_bridge
- 侧载配对（狩猎）：ebook-edit.exe + calibre-launcher.dll；FineReader.exe + dsp_ippv2_x64.dll；emlproui.exe + scansts.dll；MpDefenderCoreService.exe + mpclient.dll；Mp3tag.exe + tak_deco_lib.dll；mscorsvc.dll（GoginRAT）
- SpiceRAT 路径：C:\ProgramData\USOShared\Logs\

### 5. Cruciferra + ErrTraffic + ClickFix（Infosecurity 复述 eSentire TRU）

Infosecurity **2026-08-19** 复述 eSentire TRU（活动在 7 月下旬）。EDR killer loader Cruciferra，经 ErrTraffic 生成的 ClickFix 投递，滥用已签名驱动 **DCRCVDrv.sys**。本晚报不写 PowerShell。未找到可核验的 eSentire 原文 URL，不编造。

X：https://x.com/YungBinary/status/2090129504089886773

地址：
- 文章：https://www.infosecurity-magazine.com/news/maas-clickfix-errtraffic-cruciferra/

IoC：DCRCVDrv.sys（文件名）；未见本晚报已核验的哈希。

### 6. VoltaStealer 首次现场信号（Lunar Cyber + Infoblox）

Lunar Cyber + Infoblox：VoltaStealer 首次现场信号，ClickFix 投递。本晚报不抄 PowerShell 命令。未见本晚报已核验的哈希（Infoblox Mastodon 有哈希但未从一手页核到，不抄二手）。

X：https://x.com/rst_cloud/status/2089987758051749957

地址：
- Lunar Cyber：https://lunarcyber.com/blog/voltastealers-first-field-signal-clickfix-delivery-memory-first-claims-and-the-stealer-tradecraft-behind-the-noise/

IoC：未见本晚报已核验的哈希。

### 7. 昨日已报（X 本日仍在传，不展开）

- QUICSILVER：X 本日仍在传，昨日已报，不展开。X：https://x.com/XQOPTRX/status/2090088731772342396
- CameraSwarm／大华：X 本日仍在传，昨日已报，不展开。X：https://x.com/checkleaked/status/2090076439781491188
- MacSync：X 本日仍在传，昨日已报，不展开。X：https://x.com/TechDiplomat/status/2090159559352479902

## 地址／IoC 汇总

### URL
- https://www.cisa.gov/news-events/alerts/2026/08/19/cisa-adds-one-known-exploited-vulnerability-catalog
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://nvd.nist.gov/vuln/detail/CVE-2026-64849
- https://github.com/mlflow/mlflow/security/advisories/GHSA-7gwp-5pfp-969j
- https://github.com/mlflow/mlflow/releases/tag/v3.15.0
- https://github.com/mlflow/mlflow/pull/24258
- https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-LDquvx5d
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-crosswork-UzDTU9Vh
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-csw1-shSvndWP
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bworks-xxe-uwUd7CEt
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cuic-sql-inject-2qbfWSm5
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-roomos-bof-vTMANZgu
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ie1k-NgXUFF52
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ie1k-uxq86Lnx
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucce-pcce-ssrf-TghHxD
- https://nvd.nist.gov/vuln/detail/CVE-2026-20030
- https://github.com/sinyblack59-del/SinyC2
- https://github.com/XyrL02/sliver-defense-evasion
- https://github.com/projectdiscovery/nuclei-templates/releases
- https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a
- https://www.siemens.com/cert
- https://www.bleepingcomputer.com/news/security/us-warns-of-ai-powered-attacks-on-siemens-plcs-in-critical-infrastructure/
- https://www.huntress.com/blog/lshiy-password-spray-attack
- https://www.bleepingcomputer.com/news/security/password-spraying-attacks-surge-155x-as-hackers-exploit-mfa-gaps/
- https://www.bleepingcomputer.com/news/security/us-charges-iranian-hackers-over-34-billion-intellectual-property-theft/
- https://x.com/AverageITexpert/status/2090198465284288724
- https://www.rapid7.com/blog/post/etr-cve-2026-19490-critical-vulnerability-affecting-citrix-netscaler-adc-and-netscaler-gateway/
- https://docs.netscaler.com/en-us/netscaler-console-service/instance-advisory/remediate-vulnerabilities-cve-2026-19490.html
- https://www.esecurityplanet.com/threats/netscaler-cve-2026-19490-lets-attackers-bypass-authentication/
- https://cybersecuritynews.com/critical-citrix-netscaler-vulnerability/
- https://nvd.nist.gov/vuln/detail/CVE-2026-19490
- https://x.com/45Hrsg/status/2090211866199126524
- https://nvd.nist.gov/vuln/detail/CVE-2026-18051
- https://wpscan.com/vulnerability/dc56cdd2-419b-4a64-9d2a-29dc7e79cb6d/
- https://securityonline.info/w3-total-cache-file-write-cve-2026-18051/
- https://x.com/magicwp_io/status/2090225634022654237
- https://nvd.nist.gov/vuln/detail/CVE-2026-32475
- https://patchstack.com/articles/critical-unauthenticated-file-upload-to-rce-in-elementor-pro-plugin/
- https://patchstack.com/database/wordpress/plugin/elementor-pro/vulnerability/wordpress-elementor-pro-plugin-4-2-1-arbitrary-file-upload-vulnerability
- https://magicwp.io/blog/cve-2026-32475-elementor-pro-file-upload
- https://x.com/Cryptorbix/status/2090227459249639607
- https://www.coindesk.com/markets/2026/08/19/maya-protocol-exploit-drains-bitcoin-and-other-assets-as-pool-value-drops-usd11-million
- https://cointelegraph.com/news/maya-protocol-1-7m-exploit-network-halt
- https://x.com/__kokumoto/status/2090210638664732996
- https://x.com/SOCMinute/status/2090213217129709768
- https://x.com/Eidex_official/status/2090207432127443102
- https://x.com/aviatrixtrc/status/2090098097678410020
- https://github.com/Yeeb1/mythic_tailscale
- https://x.com/PatchRequest/status/2090147690721989049
- https://github.com/iss4cf0ng/StummSchneide
- https://x.com/iss4c_f0ng/status/2090144798154031261
- https://github.com/17vivekupadhyay/InjectionRange
- https://x.com/17vivekupadhyay/status/2090161901535699054
- https://x.com/aviatrixtrc/status/2090158542565106018
- https://x.com/checkleaked/status/2090076439781491188
- https://businessinsights.bitdefender.com/silkparasite-tracking-china-nexus-apt-across-central-asia
- https://www.darkreading.com/threat-intelligence/silkparasite-central-asian-orgs-flurry-rats
- https://x.com/YungBinary/status/2090129504089886773
- https://www.infosecurity-magazine.com/news/maas-clickfix-errtraffic-cruciferra/
- https://x.com/rst_cloud/status/2089987758051749957
- https://lunarcyber.com/blog/voltastealers-first-field-signal-clickfix-delivery-memory-first-claims-and-the-stealer-tradecraft-behind-the-noise/
- https://x.com/XQOPTRX/status/2090088731772342396
- https://x.com/TechDiplomat/status/2090159559352479902

### AA26-231A（无哈希）
- snap7.dll
- python-snap7
- S7comm TCP/102
- Censys / ZoomEye scanning
- S7-200 / S7-300 / S7-400 / S7-1200 / S7-1500

### Huntress LSHIY / Azure CLI ROPC
- 2a0a:d683::/32
- AS32167
- AS955
- 2605:6400::/32
- 2605:6404::/32
- AS53667
- AS200373
- OAuth ROPC against Azure CLI /token

### SilkParasite（Bitdefender 正文，无哈希）
- Google Drive 被滥用为 C2（DriveSilkRAT LOTS）
- evo.hoster-kg.com（NodeEdgeRAT C2；伪装 Kyrgyz hoster.kg）
- SysEdgeUpdateTaskMachineCore
- fl_bridge
- ebook-edit.exe + calibre-launcher.dll
- FineReader.exe + dsp_ippv2_x64.dll
- emlproui.exe + scansts.dll
- MpDefenderCoreService.exe + mpclient.dll
- Mp3tag.exe + tak_deco_lib.dll
- mscorsvc.dll（GoginRAT）
- C:\ProgramData\USOShared\Logs\

### Cruciferra
- DCRCVDrv.sys（文件名；未见本晚报已核验的哈希）

### Maya Protocol
- 未见核验钱包／哈希

### 工具仓 URL
- https://github.com/sinyblack59-del/SinyC2
- https://github.com/XyrL02/sliver-defense-evasion
- https://github.com/Yeeb1/mythic_tailscale
- https://github.com/iss4cf0ng/StummSchneide
- https://github.com/17vivekupadhyay/InjectionRange

## 来源搜索 URL

- https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- https://x.com/search?q=github.com%20%28C2%20OR%20%22red%20team%22%20OR%20nuclei%29&src=typed_query&f=live
- https://x.com/search?q=APT%20OR%20%22malware%20analysis%22%20OR%20%22threat%20report%22&src=typed_query&f=live
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://nvd.nist.gov/
- https://sec.cloudapps.cisco.com/security/center/publicationListing.x
