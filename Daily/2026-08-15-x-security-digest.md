# X 安全情报晚报 · 2026-08-15

> 蒐集窗口：約過去 24 小時（自聖地牙哥時間 2026-08-14 23:30 至 2026-08-15 20:10，America/Santiago / UTC-4）
> 主源：X 瀏覽器 session（已登入 Latest 搜尋；唯讀，未發帖／按讚／追蹤）
> 公開備援：CISA / NVD / 廠商公告 / RST Cloud / Acronis / Microsoft / Varonis / Fortinet
> 規則：每條含完整 https URL；沒有指標就寫「未見公開 IoC」
> 說明：防禦向晚報。不轉載利用程式碼、payload 或重現步驟；不把利用倉庫當操作指南。

## 今日摘要

- **Linux eventpoll UAF CVE-2026-43074（新，CVSS 7.8）**：本地提權面。X 本日流傳；有人宣稱 Pixel 10 Pro PoC 成功率超過 80%，**在野利用未經確認**。上游以 RCU 延後釋放修復。影響自 6.4 起核心；已修 6.6.136 / 6.12.83 / 6.18.24 / 6.19.14 / 7.0。鄰近更嚴重的 neighbor「Bad Epoll」CVE-2026-46242 僅作關聯提及。據報由 Anthropic Mythos 發現。
- **Metabase CVE-2026-72898**：已入 KEV（聯邦期限為昨日 8/14）。本日 X 出現非官方 hotfix 倉，非新洞。
- **SAP Commerce Cloud CVE-2026-58231**：8/14 已列，本日再流傳；蜜罐有命中，無公開 PoC。
- **Atlassian RovoBlast**：一鍵 rovoChatPrompt 注入（來源未給 CVE 編號）；DEF CON 34 / Varonis，約 7 月已伺服器端修補。
- **CVE-2026-53362**：未確認臆測，不作已確認漏洞處理。
- **CISA KEV**：仍 1665 條，最新 dateAdded 2026-08-11。8/15 無新增。Windows CVE-2026-68820 期限仍 8/25。
- **惡意程式**：RST Cloud 未公開文件化的 OtterCookie 譜系建置與隱形 C2 艦隊；Acronis PATCHCORD／SHEETCORD／HACKERAI；CaptiveCrunch／Midnight Blizzard 再流傳；Evooo1Bot 後續（8/14 已列）。
- **工具**：neuroaudit Linux Python 稽核套件。Ibis Wallet 賞金為低優先一筆。

## CVE / POC / 漏洞

### 1. Linux eventpoll UAF CVE-2026-43074（CVSS 7.8，本地提權）

Linux 核心 eventpoll 釋放後使用（UAF），屬本地權限提升面。X 本日流傳。有人宣稱 Pixel 10 Pro 上 PoC 成功率超過 80%；**在野利用未經確認**。上游修復將釋放延後至 RCU。影響自 6.4 起的核心；已修版本：6.6.136、6.12.83、6.18.24、6.19.14、7.0。據報導由 Anthropic Mythos 發現。鄰近更嚴重的 neighbor「Bad Epoll」CVE-2026-46242 僅作關聯提及，本晚報不展開、不給步驟。本晚報不轉載利用倉庫作為操作指南。

X：https://x.com/catnap707/status/2088769035907567886

地址：
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-43074
- 文章：https://rocket-boys.co.jp/security-measures-lab/linux-kernel-eventpoll-privilege-escalation-cve-2026-43074/
- 文章：https://securityonline.info/linux-kernel-eventpoll-flaw/
- 修補：https://git.kernel.org/stable/c/07712db80857d5d09ae08f3df85a708ecfc3b61f

IoC：未見公開 IoC。

### 2. Metabase 非官方 hotfix 倉（已知 CVE-2026-72898，KEV 昨日到期）

X 本日流傳 ubitquity 的非官方修補倉，針對**已公開**的 Metabase 漏洞 CVE-2026-72898。該洞昨日（2026-08-14）已為 CISA KEV 聯邦期限。非新漏洞；請以廠商公告為準套用官方修補，勿把第三方倉當成唯一修補來源。

X：https://x.com/ubitquity_io/status/2088772153101500476

地址：
- GitHub：https://github.com/ubitquity/Metabase-Setup-Endpoint-SQLi-Fix
- 廠商：https://www.metabase.com/blog/security-update
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-72898
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未見公開 IoC。

### 3. SAP Commerce Cloud CVE-2026-58231（再流傳，8/14 已列）

8/14 晚报已覆盖披露。Field Effect 8/14 称官方补丁后约 3 天即观察到利用尝试；本日 X 再转蜜罐命中，无公开 PoC。本条不重复展开技术细节。

X：https://x.com/yousukezan/status/2088769869093503102

地址：
- 文章：https://cybersecuritynews.com/hackers-exploit-sap-commerce-cloud/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-58231
- Field Effect：https://fieldeffect.com/blog/active-exploitation-sap-commerce-cloud-vulnerability
- SAP Note：https://me.sap.com/notes/3771065

IoC：未見公開 IoC。

### 4. Atlassian RovoBlast（一鍵 rovoChatPrompt 注入；來源未給 CVE 編號）

DEF CON 34 / Varonis 披露：經 rovoChatPrompt URL 參數的一鍵提示注入，可外洩企業資料。來源未提供 CVE 編號。約 2026 年 7 月已於伺服器端修補。X 本日流傳。Bugcrowd 披露標題為 Confluence Rovo 上一鍵資料外洩。

X：https://x.com/fiona_novesai/status/2088778203477299648

地址：
- Varonis：https://www.varonis.com/blog/rovoblast
- SecurityWeek：https://www.securityweek.com/critical-one-click-vulnerability-in-atlassians-rovo-ai-exposed-enterprise-data/
- Bugcrowd：https://bugcrowd.com/disclosures/bf1922fb-99d0-4d3b-b419-1728720d29ec/one-click-data-exfiltration-via-rovochatprompt-url-parameter-confluence-rovo

IoC：未見公開 IoC。

### 5. CVE-2026-53362（未確認臆測）

X 出現對 CVE-2026-53362 的臆測；**不作已確認漏洞處理**，本晚報僅記一筆。X：https://x.com/zeynep/status/2088772844045951384

### 6. CISA KEV 狀態（8/15 核對）

目錄仍為 1665 條，最新 dateAdded 仍為 2026-08-11。8/15 無新增 KEV。Windows CVE-2026-68820 聯邦期限仍為 2026-08-25。

地址：
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog

IoC：未見公開 IoC。

## 工具与 GitHub 发布

### neuroaudit — Linux Python 稽核套件

X 本日轉發 neuroaudit：Linux 上的 Python 稽核／審計套件（防禦向工具，非攻擊基礎設施）。

X：https://x.com/EsGeeks/status/2088638593627570354
GitHub：https://github.com/N1x-afl/neuroaudit
IoC：未見公開 IoC。

### Ibis Wallet 賞金（低優先）

@aeonBTC 公布 Ibis Wallet v4.7.0-beta 與賞金資訊。

X：https://x.com/aeonBTC/status/2088686310810894481
GitHub：https://github.com/aeonBTC/IbisWallet/releases/tag/v4.7.0-beta
IoC：未見公開 IoC。

### 周末新建 GitHub（仅列 URL）

- https://github.com/hackpatato/EV-L-ORANGE-MSG
- https://github.com/Cyt3rTo0ls/hackerbrain-os
- https://github.com/BalMM-hub/dns-threat-hunting-zeek-splunk
- https://github.com/Yahya-hacker/c2_server

IoC：未见公开 IoC。

### nuclei-templates 版本核对

projectdiscovery／nuclei-templates 最新标签仍为 v10.4.7（发布 2026-08-03），本窗口无新版本。

地址：https://github.com/projectdiscovery/nuclei-templates/releases

## APT / Malware 分析

### RST Cloud — 未公開文件化的 OtterCookie 譜系建置與隱形 C2 艦隊

RST Cloud（2026-08-14/15）：記錄一款未公開文件化的 OtterCookie 譜系建置及其隱形 C2 艦隊，歸於 Contagious Interview / Famous Chollima。

Gen2 Express 層級 5000／5056／3011。存活 Gen2 樣本 VirusTotal 0/91。投遞套件見 IoC。公開指標原文未脫逸，供封鎖與獵捕，不含利用步驟。

X：https://x.com/rst_cloud/status/2088491795185373253
文章：https://www.rstcloud.com/an-undocumented-ottercookie-lineage-build-and-its-invisible-c2-fleet/

IoC：
- IP：66.235.168.14、165.140.86.58、38.92.47.164、45.43.11.224、91.202.5.124
  5.175.213.199、45.59.160.215、165.140.86.190、147.189.172.163
- 域名：btwknrll.s.gy
- 投遞：bdmkaoyijqmqa6bg.public.blob.vercel-storage.com
- SHA-256：
  - 0747ae321ecddc3936d53fe3ead743218732d6f39e31f3728f1977f6ae8b0c62
  - fd3061f4f0e1c1cd92070659c1623a62809e0552223491bd2a016989f1e56bdd
  - 482230569e6d03f29f6f8b77b39185e0a71b7c256e0e10630e23c192433c7c10
  - e171ff04f6dac7c6c9e810be6ee7795bde765ac61f70f663b45e02772351d882
  - d49cd526ac7fe6cfec4a390abc64ea0bc4ee2ad7db898b4ff8f50e0f13285eae
- 套件：@sqlite-labs/createsql、@safehttp/strict-uri-encode
- 路徑：~/.task、~/.vs_cache

### Acronis — PATCHCORD / SHEETCORD / HACKERAI

Acronis 報告 PATCHCORD／SHEETCORD／HACKERAI 叢集，瞄準阿富汗電信與南亞關鍵基礎設施。中等信心歸於 APT36／Transparent Tribe。C2：46.30.188.13、appstoore.solutions。

X：https://x.com/rst_cloud/status/2088476615210680792
文章：https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/

IoC：
- IP：46.30.188.13
- 域名：appstoore.solutions、afghantelecom.site、afghanistanupdates.site、nic-support.site
  caprispine.health、servicesindia.services、zala-aer.info、nicservice.org
- SHA256 TMS_AfghanTelecom.exe：cf7184c0dfe882dc6e3016f16e4ede32b75d7648f83d6f4f87eb6a703be7b8d6
- SHA256 PATCHCORD tms_launcher：d46ee94d6a27ff9f02cff6fb57780acac2833ce48c95e63042a6274e24a040bb
- User-Agent：Beacon/1.0.0
- 登錄：HKCU\...\Run\BeaconBrowserHijack

### CaptiveCrunch / Midnight Blizzard（MS 官博 2026-07-31，X 再流傳）

Microsoft 2026-07-31 官博：CaptiveCrunch（Midnight Blizzard）針對全球旅客投放惡意程式並竊取憑證。本日 X 再轉，非新活動。

X：https://x.com/dennisw5/status/2088643086435959018
文章：https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
IoC：未見公開 IoC。

### Evooo1Bot（8/14 已列，後續指標）

8/14 晚報已覆蓋 Fortinet 分析。本日 X／BleepingComputer 後續：Linux 殭屍網路將路由器變成流量中繼節點。細節見昨日晚報，不重複展開。

X：https://x.com/trubetech/status/2088631140219322764
文章：https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/
Fortinet：https://www.fortinet.com/blog/threat-research/multi-functional-linux-botnet-evooo1bot
IoC：未見公開新 IoC（本窗口為後續指標；昨日晚報已列 Fortinet 指標）。

### 釣魚域名（scanmalware 公開清單）

本窗口公開列出的釣魚／仿冒域名（原文未脫逸，供封鎖）：

- www.igfun.vercel.app
- app-aave-com-dashboard.deckardsdreams.net
- web-swiftmdmdapp.pages.dev
- updateserv-owa.vercel.app
- awsapprunner-west-0clinedcom.netlify.app
- lighthearted-zabaione-c450ce.netlify.app

### HoneyMyte／CoolClient（昨报已列）

昨报已列 HoneyMyte（Mustang Panda）CoolClient 已签名内核驱动 rootkit 分析，本日无新指标，不重复展开。

https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/

### Pawn Storm / APT28 回顧

X 本日出現 Pawn Storm／APT28 回顧向貼文；來源偏薄，僅作指標，不展開。

X：https://x.com/ForIntOrg/status/2088703796511965417

## 地址／IoC 汇总

```
# X permalinks
https://x.com/catnap707/status/2088769035907567886
https://x.com/ubitquity_io/status/2088772153101500476
https://x.com/yousukezan/status/2088769869093503102
https://x.com/fiona_novesai/status/2088778203477299648
https://x.com/zeynep/status/2088772844045951384
https://x.com/EsGeeks/status/2088638593627570354
https://x.com/aeonBTC/status/2088686310810894481
https://x.com/rst_cloud/status/2088491795185373253
https://x.com/rst_cloud/status/2088476615210680792
https://x.com/dennisw5/status/2088643086435959018
https://x.com/trubetech/status/2088631140219322764
https://x.com/ForIntOrg/status/2088703796511965417

# advisories
https://nvd.nist.gov/vuln/detail/CVE-2026-43074
https://rocket-boys.co.jp/security-measures-lab/linux-kernel-eventpoll-privilege-escalation-cve-2026-43074/
https://securityonline.info/linux-kernel-eventpoll-flaw/
https://git.kernel.org/stable/c/07712db80857d5d09ae08f3df85a708ecfc3b61f
https://github.com/ubitquity/Metabase-Setup-Endpoint-SQLi-Fix
https://www.metabase.com/blog/security-update
https://nvd.nist.gov/vuln/detail/CVE-2026-72898
https://www.cisa.gov/known-exploited-vulnerabilities-catalog
https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
https://cybersecuritynews.com/hackers-exploit-sap-commerce-cloud/
https://nvd.nist.gov/vuln/detail/CVE-2026-58231
https://www.varonis.com/blog/rovoblast
https://www.securityweek.com/critical-one-click-vulnerability-in-atlassians-rovo-ai-exposed-enterprise-data/
https://bugcrowd.com/disclosures/bf1922fb-99d0-4d3b-b419-1728720d29ec/one-click-data-exfiltration-via-rovochatprompt-url-parameter-confluence-rovo
https://github.com/N1x-afl/neuroaudit
https://github.com/aeonBTC/IbisWallet/releases/tag/v4.7.0-beta
https://www.rstcloud.com/an-undocumented-ottercookie-lineage-build-and-its-invisible-c2-fleet/
https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/
https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/
https://www.fortinet.com/blog/threat-research/multi-functional-linux-botnet-evooo1bot

# OtterCookie-lineage (RST Cloud, undfang)
66.235.168.14
165.140.86.58
38.92.47.164
45.43.11.224
91.202.5.124
5.175.213.199
45.59.160.215
165.140.86.190
147.189.172.163
btwknrll.s.gy
bdmkaoyijqmqa6bg.public.blob.vercel-storage.com
0747ae321ecddc3936d53fe3ead743218732d6f39e31f3728f1977f6ae8b0c62
fd3061f4f0e1c1cd92070659c1623a62809e0552223491bd2a016989f1e56bdd
482230569e6d03f29f6f8b77b39185e0a71b7c256e0e10630e23c192433c7c10
e171ff04f6dac7c6c9e810be6ee7795bde765ac61f70f663b45e02772351d882
d49cd526ac7fe6cfec4a390abc64ea0bc4ee2ad7db898b4ff8f50e0f13285eae
@sqlite-labs/createsql
@safehttp/strict-uri-encode
~/.task
~/.vs_cache

# PATCHCORD / SHEETCORD / HACKERAI (Acronis, undfang)
46.30.188.13
appstoore.solutions
afghantelecom.site
afghanistanupdates.site
nic-support.site
caprispine.health
servicesindia.services
zala-aer.info
nicservice.org
cf7184c0dfe882dc6e3016f16e4ede32b75d7648f83d6f4f87eb6a703be7b8d6
d46ee94d6a27ff9f02cff6fb57780acac2833ce48c95e63042a6274e24a040bb
Beacon/1.0.0
HKCU\...\Run\BeaconBrowserHijack

# scanmalware phishing domains (undfang)
www.igfun.vercel.app
app-aave-com-dashboard.deckardsdreams.net
web-swiftmdmdapp.pages.dev
updateserv-owa.vercel.app
awsapprunner-west-0clinedcom.netlify.app
lighthearted-zabaione-c450ce.netlify.app
```

CVE-2026-43074／72898／58231／RovoBlast／neuroaudit／Ibis Wallet／CaptiveCrunch／Pawn Storm：未見公開 IoC。CVE-2026-53362：未確認臆測，無 IoC。

## 来源搜索 URL

- https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&src=typed_query&f=live
- https://x.com/search?q=(APT%20OR%20malware)%20(analysis%20OR%20report)&src=typed_query&f=live
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- https://github.com/projectdiscovery/nuclei-templates/releases
- https://fieldeffect.com/blog/active-exploitation-sap-commerce-cloud-vulnerability
- https://me.sap.com/notes/3771065
- https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/
