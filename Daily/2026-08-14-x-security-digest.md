# X 安全情報晚報 · 2026-08-14

> 蒐集窗口：約過去 24 小時（至聖地牙哥時間 2026-08-14 20:15）  
> 主源：X 瀏覽器 session（**已登入** Latest 搜尋；未發帖／按讚／追蹤；X API 仍未用）  
> 備援：CISA / NVD / MSRC / Rapid7 / Check Point / The Hacker News / SecurityWeek / Socket / watchTowr / GitHub  
> 規則：每條含完整 https URL；沒有 IoC 寫明「未見公開 IoC」

## 今日摘要

- **CISA KEV 期限今日（8/14）**：Metabase **CVE-2026-72898**、Cisco ASA/FTD **CVE-2026-20349** 聯邦 due date 就是今天。Windows **CVE-2026-68820** 期限 **8/25**。
- **GeoServer 未修 0day**：`jsonArrayContains` 未授權 SQLi，尚無 CVE／廠商補丁；watchTowr 稱公開後數小時已見數百次探測。X 原披露帳 **@q1uf3ng**（本輪 Latest 未刷到該原帖 permalink）。
- **SAP Commerce Cloud CVE-2026-58231**（CVSS 10.0）：Defused 蜜罐 8/14 見到利用嘗試（patch day 後 3 天，尚無公開 PoC）。
- **SharePoint CVE-2026-55040**：Rapid7 PoC 後利用持續；TechTimes 8/14 跟進（蜜罐 8/12–13 高峰）。
- **X Latest 新工具**：OctoC2、SquidC5、PentestAgent、ICMP-Ghost；Nuclei 模板已覆蓋 **CVE-2026-64638** XSS2Shell。
- **APT／惡意**：Lazarus Dream Job + AFD.sys 0day 仍是主線；**Kaspersky 今日 HoneyMyte／CoolClient 簽名核心根套件**；Jewelbug 間諜＋加密詐騙同 C2；Socket 737 假 Chrome VPN；UAC-0145 改裝 WireGuard。
- **補遺**：FreePBX **CVE-2026-73665** 未授權 RCE（8/13 進 CVE）；LXD **CVE-2026-63298**；macOS Screen Sharing **CVE-2026-65400** 已見在野（門羅礦工，埠 5900）。

---

## CVE / POC / 漏洞

### 1. GeoServer `jsonArrayContains` 未授權 SQLi → 條件 RCE（無 CVE、無補丁、已見掃描）
OSGeo GeoServer 過濾函式 `jsonArrayContains` 把使用者參數寫進 PostGIS／Oracle JDBC SQL。未授權可從公開 OGC（WFS/WMS）觸發。DB 帳號有 superuser／`pg_execute_server_program` 時可 `COPY TO PROGRAM` 做 RCE。@q1uf3ng 8/12 在 X 公開；watchTowr：數小時內數百次嘗試、來源 IP 很少，目前多為探測。  
X：本輪 Latest 未刷到 @q1uf3ng 原帖 permalink（搜尋詞被 POC=people of color 洗版）。搜尋：https://x.com/search?q=q1uf3ng%20GeoServer&src=typed_query&f=live  
地址：
- https://www.securityweek.com/hackers-exploiting-unpatched-geoserver-zero-day/
- https://www.csoonline.com/article/4209388/attackers-target-zero-day-vulnerability-in-geospatial-data-platform-geoserver.html
- https://thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html
- https://hadrian.io/blog/here-be-dragons-geoserver-pre-auth-sql-injection-to-rce
- https://byteiota.com/geoserver-zero-day-sql-injection-rce/
- https://gist.github.com/portbuster1337/70d75ec246b85e3199037ce212ff1a06
- https://geoserver.org/  
IoC：watchTowr 稱「少數來源 IP」，**未見公開掃描源 IP 表**。gist 為公開 PoC 位址（本晚報不貼 payload）。緩解：限制公網 OGC、關掉 `jsonArrayContains`／PostGIS encode functions、開 prepared statements；等官方修補。

### 2. CVE-2026-58231 — SAP Commerce Cloud Data Hub Adapter 未授權 RCE（CVSS 10.0，8/14 蜜罐已見打）
濫用預設認證 client + 輸入未驗證 → 任意程式碼。SAP Note **3771065**（8/11 Patch Day）。Defused：無公開 PoC 但蜜罐已見嘗試。修 **2211.55**／**2211-jdk21.17**；臨時用 IP Filter 限制 import endpoint。  
X：本輪 Latest 未刷到 Defused 原帖。  
地址：
- https://me.sap.com/notes/3771065
- https://support.sap.com/en/my-support/knowledge-base/security-notes-news/august-2026.html
- https://url.sap/sapsecuritypatchday
- https://nvd.nist.gov/vuln/detail/CVE-2026-58231
- https://github.com/advisories/GHSA-686g-q5w6-7j38
- https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/
- https://thehackernews.com/2026/08/sap-commerce-cloud-flaw-could-let.html
- https://fieldeffect.com/blog/active-exploitation-sap-commerce-cloud-vulnerability  
IoC：未見公開掃描源 IP／C2（蜜罐未放 IP 表）。

### 3. CVE-2026-55040 — SharePoint JWT 認證繞過（PoC 後持續利用）+ CVE-2026-63520 RCE 鏈
Rapid7 8/11 技術文＋PoC；Defused／KEVIntel：8/12–13 蜜罐高峰（8 個來源 IP、五地）。CVSS 9.1。7 月已修 55040、8 月修 63520。CISA **尚未**列入 KEV。  
X：昨報已列 SecurityWeek 等帖；今晚 Latest 未再刷到新 permalink。  
地址：
- https://github.com/sfewer-r7/CVE-2026-55040
- https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-jwt-token-authentication-bypass-cve-2026-55040/
- https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed/
- https://www.rapid7.com/blog/post/etr-cve-2026-63520-microsoft-sharepoint-remote-code-execution-fixed/
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-55040
- https://nvd.nist.gov/vuln/detail/CVE-2026-55040
- https://nvd.nist.gov/vuln/detail/CVE-2026-63520
- https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html
- https://www.techtimes.com/articles/324475/20260814/sharepoint-cve-2026-55040-actively-exploited-attackers-forge-admin-credentials-no-password.htm
- https://www.helpnetsecurity.com/2026/08/13/microsoft-sharepoint-cve-2026-55040-poc-exploit/
- https://www.securityweek.com/sharepoint-vulnerability-exploited-shortly-after-poc-release/  
修補：KB5002882 / KB5002883 / KB5002891（7 月）＋ 8 月 63520。  
IoC：公開報導稱香港／日本／荷蘭／台灣／美國共 8 個 IP；**未見完整掃描源 IP 表**。PoC：`CVE-2026-55040.py`（Rapid7 倉）。

### 4. CVE-2026-72898 — Metabase 未授權 SQLi（KEV，**期限今日 8/14**，CVSS 10.0）
`/api/session/reset_password` 未授權注入應用庫。CISA 8/11 入 KEV。  
X：https://x.com/DhiyaneshDK/status/2087422651648422269 （昨報已列；今晚未刷到新帖）  
地址：
- https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf
- https://www.metabase.com/blog/security-update
- https://nvd.nist.gov/vuln/detail/CVE-2026-72898
- https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.wiz.io/blog/inside-the-metabase-sqli-exploited-in-the-wild
- https://github.com/codeb0ssx/CVE-2026-72898-PoC
- https://github.com/0xBlackash/CVE-2026-72898  
IoC：未見公開 C2／掃描源 IP。修補版本以 GHSA 為準。

### 5. CVE-2026-20349 — Cisco ASA/FTD SSL VPN 遠端 DoS（KEV，**期限今日 8/14**）
未授權特製 HTTP 打 Remote Access SSL VPN → 裝置重載。  
X：https://x.com/DFIR_Radar/status/2087737028637270401 （昨報）  
地址：
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF
- https://nvd.nist.gov/vuln/detail/CVE-2026-20349
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://thehackernews.com/2026/08/cisco-asa-and-ftd-flaw-exploited-in.html  
IoC：未見公開掃描源 IP。

### 6. CVE-2026-68820 — Windows AFD.sys／WinSock 在野 0day（Lazarus，KEV，期限 8/25）
Check Point 歸因 Operation Dream Job；8/11 Patch Tuesday。細節見 APT 節。  
X：https://x.com/EsGeeks/status/2087745613295165670  
地址：
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820
- https://nvd.nist.gov/vuln/detail/CVE-2026-68820
- https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
- https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- https://www.crowdstrike.com/en-us/blog/patch-tuesday-analysis-august-2026/  
IoC：見下方 Lazarus 節。

### 7. CVE-2026-59310 — VMware vCenter Syslog 目錄遍歷 RCE（在野 reverse SSH）
Broadcom VMSA-2026-0006。QUIRSO：至少 361 受害 IP／47 國。  
地址：
- https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
- https://nvd.nist.gov/vuln/detail/CVE-2026-59310
- https://nvd.nist.gov/vuln/detail/CVE-2026-59309
- https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html
- https://github.com/NHAS/reverse_ssh  
IoC：QUIRSO **因執法協調未公開** C2 IP／域名／雜湊。未見公開 IoC 表。

### 8. CVE-2026-64638 — WordPress XSS2Shell（今晚 X 仍在轉 Nuclei）
`wp-login.php` pre-auth XSS → 管理員 RCE。WP 7.0.3 起修。  
X：https://x.com/luckyhacker43/status/2088175754638987609 · https://x.com/luckyhacker43/status/2088178339873787978  
地址：
- https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-64638.yaml
- https://github.com/Boreas37/CVE-2026-64638-PoC-XSS2Shell-
- https://pwn.ai/blog/xss2shell
- https://nvd.nist.gov/vuln/detail/CVE-2026-64638
- https://wordpress.org/news/2026/08/wordpress-7-0-3-release/  
IoC：未見公開 C2。落地外掛路徑示意：`/wp-content/plugins/xss2shell/xss2shell.php`（PoC）。

### 9. CVE-2026-65640 — WordPress 7.0.4 Author+ RCE（Imagick＋Ghostscript）
Author 上傳惡意檔（內容為 PostScript、副檔名偽裝）→ Imagick 交給 Ghostscript 執行。影響 4.7.0–7.0.3。pwn.ai 回報。公開時未確認在野。  
地址：
- https://wordpress.org/news/2026/08/wordpress-7-0-4-release/
- https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-8vr3-7mxf-gx8w
- https://www.securityweek.com/wordpress-7-0-4-patches-remote-code-execution-vulnerability/
- https://nvd.nist.gov/vuln/detail/CVE-2026-65640  
IoC：未見公開 C2（需已登入 Author）。

### 10. CVE-2026-48362 等 — Adobe ColdFusion／Campaign Classic CVSS 10.0（APSB26-90）
ColdFusion OS command injection **CVE-2026-48362**（10.0）。修 CF 2025.0.12／2023.0.23。Adobe 稱當時未知在野。  
地址：
- https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html
- https://coldfusion.adobe.com/2026/08/now-live-coldfusion-2025-and-2023-august-2026-security-updates/
- https://thehackernews.com/2026/08/adobe-patches-three-cvss-100-coldfusion.html
- https://nvd.nist.gov/vuln/detail/CVE-2026-48362  
IoC：未見公開 IoC。

### 11. CVE-2026-71362 — Adobe Commerce／Magento 帳號劫持（APSB26-92，已見利用）
地址：
- https://helpx.adobe.com/security/products/magento/apsb26-92.html
- https://sansec.io/research/adobe-commerce-account-takeover-apsb26-92
- https://www.cve.org/CVERecord?id=CVE-2026-71362  
IoC：未見公開掃描源 IP。

### 12. Citrix NetScaler SAML 記憶體漏洞（CVE-2026-8451／8452 線）
watchTowr：SAML canonicalization heap overflow，可到 RCE（作者標 CVE-2026-8452?）。修 14.1-72.61／13.1-63.18。另有 CitrixBleed 系 **CVE-2026-8451** 未授權記憶體外洩。  
地址：
- https://labs.watchtowr.com/youre-back-in-the-room-citrix-netscaler-pre-auth-rce-cve-2026-8452/
- https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX696604
- https://github.com/0xBlackash/CVE-2026-8451  
IoC：未見公開在野利用確認。需 SAML SP/IdP 組態。

### 13. CVE-2026-73665 — FreePBX 17 UCP 未授權 RCE
Socket.IO 只對預設 namespace 做 `io.use(checkAuth)`，自訂 namespace 可跳過認證並對 AMI 做 CR/LF 注入，以 `asterisk` 使用者執行。修 **ucp 17.0.9**。CVSS 4.0 9.3。GitHub_M 8/13 22:17 UTC 公開 CVE。  
地址：
- https://github.com/FreePBX/security-reporting/security/advisories/GHSA-37j8-fhxx-9vhp
- https://www.cve.org/CVERecord?id=CVE-2026-73665
- https://nvd.nist.gov/vuln/detail/CVE-2026-73665  
IoC：未見公開 IoC。埠：8001／8003。

### 14. CVE-2026-63298 — LXD NVIDIA 設定換行注入
已認證攻擊者往 `nvidia.driver.capabilities`／`nvidia.require.*` 注入換行，寫進 `lxc.conf` 任意指令，以 LXD daemon 執行。影響 4.0.x < 4.0.12、5.0.x < 5.0.8、5.21.x < 5.21.6。Canonical 8/12 公開。  
地址：
- https://cve.report/CVE-2026-63298
- https://app.opencve.io/cve/CVE-2026-63298  
IoC：未見公開 IoC（本機／已認證）。


### 15. CVE-2026-65400 — macOS Screen Sharing 未授權登入，已見在野門羅礦工
Screen Sharing（VNC／TCP 5900）狀態管理錯誤，網路上攻擊者可無帳密通過認證；Huntress 稱可走到預認證 RCE。Apple 8/6 修 Tahoe 26.6.1／Sequoia 15.7.9／Sonoma 14.8.9。荷蘭 NCSC：多台 5900 對公網的機器已被打到 root 並放 Monero miner。NVD 8/14 更新。  
地址：
- https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/
- https://arstechnica.com/security/2026/08/vulnerability-giving-attackers-full-control-of-macs-is-under-active-exploitation/
- https://www.tenable.com/cve/CVE-2026-65400
- https://support.apple.com/en-us/148170  
IoC：未見公開 IoC（NCSC 未公布掃描源 IP）。緩解：更新；或關掉 Screen Sharing（系統設定 → 一般 → 共享），擋 5900。


---

## 工具與 GitHub 發佈

### 1. OctoC2（今晚 X）
HTTPS／gRPC／mTLS、proxy、Codespaces；Beacon TypeScript；Ed25519／X25519。  
X：https://x.com/EsGeeks/status/2088247034134290540  
地址：https://github.com/dstours/OctoC2  
IoC：未見公開 IoC（紅隊框架倉庫）。

### 2. SquidC5 C2（今晚 X）
X：https://x.com/DotNetRussell/status/2088302568296341742  
地址：https://github.com/SquidSec/SquidC5  
IoC：未見公開 IoC。

### 3. PentestAgent — AI 黑盒滲透框架
X：https://x.com/ThreatVect/status/2088302280072376607  
地址：https://github.com/GH05TCREW/pentestagent  
IoC：未見公開 IoC。

### 4. ICMP-Ghost — 無檔 x64 組合語言 ICMP C2
X：https://x.com/rustyLAKEX/status/2088349253232165102  
地址：https://github.com/JM00NJ/ICMP-Ghost-A-Fileless-x64-Assembly-C2-Agent  
IoC：未見公開 IoC。

### 5. RedLine Stealer C2／Defender bypass 逆向倉
X：https://x.com/rustyLAKEX/status/2088169564777697336  
地址：https://github.com/kaandemir993/RedLine-Stealer-C2-Defender-Bypass-Payload-Analysis  
IoC：未見公開 C2 IP（分析倉；家族為 RedLine）。

### 6. Nuclei 模板
- 引擎／模板庫：https://github.com/projectdiscovery/nuclei/releases · https://github.com/projectdiscovery/nuclei-templates
- v10.4.7（8/3，122 新模板／49 CVE）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.7
- XSS2Shell 檢測：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-64638.yaml
- C2 SSL 指紋目錄：https://github.com/projectdiscovery/nuclei-templates/tree/main/ssl/c2

### 7. Rapid7／既有 PoC 倉（持續被轉）
- https://github.com/sfewer-r7/CVE-2026-55040
- https://github.com/sfewer-r7/CVE-2026-63077
- https://github.com/MSNightmare/ShieldBreak
- https://github.com/NHAS/reverse_ssh

### 8. GeoServer 公開 gist PoC
- https://gist.github.com/portbuster1337/70d75ec246b85e3199037ce212ff1a06  
IoC：未見 C2（漏洞 PoC）。

---

## APT / Malware 分析

### 1. Lazarus — Operation Dream Job + CVE-2026-68820 + FudModule／Troy
假求職、SecurityPDF、MISTPEN、FudModule v3.1、ForestTiger、Troy。目標歐印巴防務／航太。  
X：https://x.com/EsGeeks/status/2087745613295165670  
地址：
- https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
- https://blog.checkpoint.com/research/state-sponsored-hackers-use-fake-job-offers-to-deliver-new-zero-day-exploit/
- https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820  
地址／IoC（Check Point 原文，defang 已展開）：
- 域名：`envell.xyz` · `enveil.online` · `uxtramine.org`
- IP：`135.181.67.203` · `135.181.185.158`
- PDF 標記：`This document is encrypted with sumatrapdf reader!!!!!!!!!!!!`
- XOR key：`0x39`；落地：`%TEMP%\new.exe`；Sideload：`libmupdf.dll`
- FudModule：`3b6378df8442e63a6ed7317075913e4720847a510d95022d4a8347c2637c245d`
- RelayShell：`21c3ad4838c4324bc5f081021da5fb2e9073d0c9304087811c21eb47c9e22762` · `cc4e06aa378a190f71384c03023bb3d18a6d66e297d46701220e132963d2e222`
- SecurityPDF.exe：`743172aab606974b054a64561534ae66baa3a840657f79d7c6fa18350e8d45d1` · `db3d69b7eeda2e35e23006bf4b7e206281fce809584207214fc213f9bc30376d`
- Troy：`590fb6ae19480d694e08ee85859cad8066f2f87e7e5abba2960c6d115e1615d6` · `68d4fba7b1300a59cd6212c08910a260cd71b40cd9f51cac933030a68faac0bb` · `a738059ce07c951c31ab2da3d93d8f69bff32f9b7d933dbf5943441b9cc99075`
- 完整 loader／MISTPEN／ForestTiger 表見 Check Point「IOCs」節。

### 2. Socket — 737 個假 Chrome VPN／proxy 外掛（Myxa VPN）
40+ 開發者帳、75,486 安裝；520/522 把流量打到 SOCKS5 **port 1082**；274 個假冒 66 個品牌。Google 已下 221 個，寫作時仍有 516 個在架。  
地址：
- https://socket.dev/blog/chrome-vpn-extension-impersonation
- https://thehackernews.com/2026/08/737-chrome-vpn-extensions-caught.html
- https://www.bleepingcomputer.com/news/security/hundreds-of-fake-chrome-vpn-extensions-route-traffic-through-a-proxy/  
地址／IoC（Socket 原文，摘關鍵；完整 516 個 extension ID 以 Socket 文為準）：
- 域名：`myxavpn.pro` · `myxavpn.com` · `getmyxa.com` · `myxavpn.site` · `myxavpn.online` · `myxavpn.tech` · `myxasafe.space` · `skyproxy.space` · `stealthpath.space` · `sverchtun.store` · `vpnkomar.space` · `vpnmyxa.site` · `maskirovka.space` · `t.me/myxavpn_bot`
- IP：`212.192.14.75` · `158.160.228.178` · `147.45.60.241` · `178.130.47.43` · `178.130.47.44` · `178.130.47.50` · `185.252.215.97` · `185.252.215.98` · `80.92.204.47` · `5.180.30.15`
- 埠：SOCKS5 `1082`；付費層 VLESS-REALITY `443`
- 範例外掛 ID：`aaeiefggdeljohngedhpmgidkjcdoebb`（Myxa 付費層綁定）· `ilbpmeeaifiojjiohfffjmgpgcfcaajg`（假 1.1.1.1 VPN）
- SHA-256（九份相同審核說詞）：`1dea4975f7aaba71bf7821fcf62deca470ef5e21f45c947b103ddeb836ef9b81`

### 3. UAC-0145／Sandworm — 假面試＋改裝 WireGuard（SopraVPN）
自 2026-05 起打烏克蘭 IT。Telegram／Zoom → 失敗的 WireGuard conf → SourceForge「SopraVPN」。非標準 `SymmetricKey` 解密後走 `PostUp`／`runScriptCommand`。  
地址：
- https://www.bleepingcomputer.com/news/security/sandworm-hackers-target-it-pros-with-trojanized-wireguard-vpn-client/
- https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html
- https://cert.gov.ua/  
地址／IoC：
- 域名：`soprasteria-bg.com`（仿 Sopra Steria Bulgaria）
- 下載：SourceForge 上的 SopraVPN（具體專案 permalink 未見穩定公開 URL）
- 設定鍵：`SymmetricKey`（非官方 WireGuard 欄位）  
完整樣本雜湊／C2：CERT-UA 原文有表，本輪未取得穩定 article permalink，**雜湊未見可核對公開表**（寫「未見可核對雜湊表」）。

### 4. BabaDeda → CNCMachineRMS（LevelBlue SpiderLabs，今晚 X）
ClickFix 鏈末端未記錄 RAT。  
X：https://x.com/rst_cloud/status/2088408264207679619  
地址：https://levelblue.com/blogs/spiderlabs-blog/cncmachinerms-the-undocumented-rat-at-the-end-of-a-babadeda-chain  
IoC：帖文未列 IP／雜湊；以原文表為準。未見公開 IoC（帖面）。

### 5. 惡意 crypting 服務（Recorded Future，今晚 X）
GoldenCrypt、O1oo1、BianLian；Fvncbot／Albiriox／Mirax。  
X：https://x.com/rst_cloud/status/2088370294285095257  
地址：https://www.recordedfuture.com/research/malware-crypting-services-threat-actors  
IoC：未見公開 IoC（帖面）。

### 6. Weaxor 勒索 — 用 SQL Server 當初始啟動器（K7，今晚 X）
X：https://x.com/rst_cloud/status/2088362705400848389  
地址：https://labs.k7computing.com/index.php/when-sql-server-becomes-the-initial-launcher-a-deep-dive-into-weaxor-ransomware-execution/  
IoC：未見公開 IoC（帖面）。

### 7. Kimwolf v7（Unit 42）
HTTP/2 DDoS＋Chrome 指紋；ENS／Tor C2。  
地址：https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/  
IoC：完整 IP／ENS 合約見 Unit 42 原文表（本節不逐條轉錄）。

### 8. Mozilla 撤銷 Firefox／Thunderbird Linux 簽名金鑰（今晚 X）
私有倉誤提交未加密金鑰。  
X：https://x.com/NitinGavhane_/status/2088417296801018093  
地址：https://thehackernews.com/2026/08/mozilla-revokes-firefox-and-thunderbird.html  
IoC：未見惡意 C2（金鑰事故）。

### 9. X 掃到的釣魚域名（@scanmalware，1–2h）
X：https://x.com/scanmalware/status/2088393492397445456 · https://x.com/scanmalware/status/2088387700113981447  
IoC（帖面 defang 已展開）：
- `seri3sawsapprunner-south1-dpkkvw2rkadj.edgeone.dev`
- `awsforensicl3ns-west1apprunner-dprd03feve9j.edgeone.dev`

### 10. HoneyMyte（Mustang Panda）— CoolClient 加上簽名核心根套件（Kaspersky，**今日 8/14**）
最新 CoolClient 丟簽名驅動 `msagent.sys`（服務 `msagent`，裝置 `\\.\msagent`／`\Device\ToolTool`），IOCTL `0x222120`／`0x2221E0`／`0x2220F0`。藏行程／檔／登錄／C2 IP。鏈：PlugX → Sangfor DLL 側載 → `loadcert.ini` 注入 `synchost.exe`。目標緬甸／蒙古／巴基斯坦／俄國政府。簽名：Nanjing Ranyi Technology Co., Ltd.（序號 `3E 62 DC 5D 8D 61 2A 26 33 E7 6B DF D6 07 19 DD`，證 2014 已過期）。  
地址：
- https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/
- https://www.neowin.net/news/windows-rootkit-now-included-with-coolclient-backdoor-targeting-governments/  
地址／IoC（Kaspersky）：
- 雜湊：`2d7c8780e97409770a9d4f31c66c9d63` · `9460E150E1981D5C165043520C5C12FE`（msagent.sys）· `9717F005C5FB98E08D2AD983D88F94EE` · `F518D8E5FE70D9090F6280C68A95998F`（libngs.dll）· `EB79558B037669792652A816E2C669DE`（ctxmui.dll）
- 域名：`cloudtroe.giize.com` · `employers.theworkpc.com` · `freeread.casacam.net` · `us.lenovoappstore.com` · `sundanish.freeddns.org` · `torinarlabs.webredirect.org` · `news.dursamjbataar.org` · `video.dursamjbataar.org` · `black-popular.com` · `whatismybestthing.com`
- 路徑：`C:\Program Files\microsoft\windows defender\` · `C:\ProgramData\symantecdir\` · 排程 `Microsoft\Windows\Windows Defender Advanced Threat Protection Service` · 服務 `media_updaten` · HKCU Run `goopdate`

### 11. Jewelbug（Earth Alux／Ink Dragon／REF7707）— 間諜＋加密詐騙共用 C2（Symantec，8/13 報導）
XG-Web（React/Node C2）並行 Antino（Graph API 後門）、「PDF Viewer」瀏覽器外掛＋native host `com.microsoft.runedge`、Rust Linux／路由器植入 ClientKing。中東電信共用 webmail 被當水坑，15+ 政府租戶。PDF：The Jewelbug Dossier。  
地址：
- https://sed-cms.broadcom.com/sites/default/files/2026-08/Jewelbug%20Dossier.pdf
- https://www.bleepingcomputer.com/news/security/hackers-breach-govt-webmail-while-running-parallel-crypto-fraud/
- https://www.darkreading.com/threat-intelligence/jewelbug-apt-state-espionage-cryptocurrency-theft  
地址／IoC（Symantec／Broadcom，摘）：
- 域名：`fonts.tarotfree101.top` · `fonts.chrorne.com` · `robot.avbliud.com` · `microsoft-flash.com` · `www.wps-cn.com` · `www.f1ash.org.cn` · `browser-update.pages.dev` · `eastus2.wac-azure.com` · `mailbycloud.com` · `www.jkskhei.com` · `ns1.jkskhei.com` · `dns.wizkidblogger.com`
- IP：`43.246.208.236` · `103.87.9.62` · `152.42.174.151` · `43.246.208.179` · `47.84.37.113:8080` · `47.84.51.173:1880` · `167.71.195.255` · `38.12.1.47` · `129.212.237.224`
- 下載：`http://d2nq35tel3ucuo.cloudfront.net/LtVGUSsyUTDA.log` · `https://pub-abfa7742e315485a98a5fafd6dbfb68e.r2.dev/hjgzBskgslc.dll.iwq`
- 主機：`nativeMessagingHosts\com.microsoft.runedge` · 外掛「PDF Viewer」v2026.5.13.1 · `client-king` · LKM `clientking` · `pam_security.so` · `/usr/local/share/.assist` · 標記 `pq9i75DhW1`
- SHA-256：`e6ff096a0562c0042b09d250bd60272ffcd8d72bd95c563842acf765a8dc8bcf` · `01b5c6acb20e41799a0e96d9d1d6e1c44791883706b6285e874fcb15cc93b31a` · `e2eb7703047b37b28dc34e6990205d758a2454b39bc655b460606745fadcb530`（slc.dll Antino）· `0c39264337a1186b2e765e24073399cbdcba118306614eb411e315887af578bd` · `b90a4e770869c28fd2140acb3ebdc50c113bb6f096b4bbdb9ac87c349c70e85e`
- 完整雜湊見 PDF 第 12 節。


---

## 地址／IoC 匯總（可複製）

```
# 公告／文章
https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
https://www.cisa.gov/known-exploited-vulnerabilities-catalog
https://www.securityweek.com/hackers-exploiting-unpatched-geoserver-zero-day/
https://gist.github.com/portbuster1337/70d75ec246b85e3199037ce212ff1a06
https://me.sap.com/notes/3771065
https://nvd.nist.gov/vuln/detail/CVE-2026-58231
https://github.com/sfewer-r7/CVE-2026-55040
https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-jwt-token-authentication-bypass-cve-2026-55040/
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820
https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF
https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html
https://wordpress.org/news/2026/08/wordpress-7-0-4-release/
https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-8vr3-7mxf-gx8w
https://labs.watchtowr.com/youre-back-in-the-room-citrix-netscaler-pre-auth-rce-cve-2026-8452/
https://socket.dev/blog/chrome-vpn-extension-impersonation
https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/
https://levelblue.com/blogs/spiderlabs-blog/cncmachinerms-the-undocumented-rat-at-the-end-of-a-babadeda-chain
https://www.recordedfuture.com/research/malware-crypting-services-threat-actors
https://labs.k7computing.com/index.php/when-sql-server-becomes-the-initial-launcher-a-deep-dive-into-weaxor-ransomware-execution/

# GitHub／工具
https://github.com/dstours/OctoC2
https://github.com/SquidSec/SquidC5
https://github.com/GH05TCREW/pentestagent
https://github.com/JM00NJ/ICMP-Ghost-A-Fileless-x64-Assembly-C2-Agent
https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-64638.yaml
https://github.com/Boreas37/CVE-2026-64638-PoC-XSS2Shell-
https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.7
https://github.com/NHAS/reverse_ssh
https://github.com/MSNightmare/ShieldBreak

# X 原帖
https://x.com/luckyhacker43/status/2088175754638987609
https://x.com/luckyhacker43/status/2088178339873787978
https://x.com/EsGeeks/status/2088247034134290540
https://x.com/DotNetRussell/status/2088302568296341742
https://x.com/ThreatVect/status/2088302280072376607
https://x.com/rustyLAKEX/status/2088349253232165102
https://x.com/rustyLAKEX/status/2088169564777697336
https://x.com/rst_cloud/status/2088408264207679619
https://x.com/rst_cloud/status/2088370294285095257
https://x.com/rst_cloud/status/2088362705400848389
https://x.com/NitinGavhane_/status/2088417296801018093
https://x.com/scanmalware/status/2088393492397445456
https://x.com/scanmalware/status/2088387700113981447

# Lazarus C2／樣本
envell.xyz
enveil.online
uxtramine.org
135.181.67.203
135.181.185.158
3b6378df8442e63a6ed7317075913e4720847a510d95022d4a8347c2637c245d
21c3ad4838c4324bc5f081021da5fb2e9073d0c9304087811c21eb47c9e22762
cc4e06aa378a190f71384c03023bb3d18a6d66e297d46701220e132963d2e222
743172aab606974b054a64561534ae66baa3a840657f79d7c6fa18350e8d45d1
db3d69b7eeda2e35e23006bf4b7e206281fce809584207214fc213f9bc30376d
590fb6ae19480d694e08ee85859cad8066f2f87e7e5abba2960c6d115e1615d6
68d4fba7b1300a59cd6212c08910a260cd71b40cd9f51cac933030a68faac0bb
a738059ce07c951c31ab2da3d93d8f69bff32f9b7d933dbf5943441b9cc99075

# Myxa／假 VPN
myxavpn.pro
skyproxy.space
stealthpath.space
212.192.14.75
158.160.228.178
SOCKS5:1082
aaeiefggdeljohngedhpmgidkjcdoebb
ilbpmeeaifiojjiohfffjmgpgcfcaajg

# UAC-0145
soprasteria-bg.com

# 釣魚（X @scanmalware）
seri3sawsapprunner-south1-dpkkvw2rkadj.edgeone.dev
awsforensicl3ns-west1apprunner-dprd03feve9j.edgeone.dev

# FreePBX / LXD
https://github.com/FreePBX/security-reporting/security/advisories/GHSA-37j8-fhxx-9vhp
https://nvd.nist.gov/vuln/detail/CVE-2026-73665
https://cve.report/CVE-2026-63298

# macOS Screen Sharing
https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/
https://www.tenable.com/cve/CVE-2026-65400


# HoneyMyte CoolClient
https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/
cloudtroe.giize.com
employers.theworkpc.com
us.lenovoappstore.com
sundanish.freeddns.org
2d7c8780e97409770a9d4f31c66c9d63
9460E150E1981D5C165043520C5C12FE

# Jewelbug
https://sed-cms.broadcom.com/sites/default/files/2026-08/Jewelbug%20Dossier.pdf
fonts.tarotfree101.top
fonts.chrorne.com
microsoft-flash.com
43.246.208.236
103.87.9.62
152.42.174.151
e2eb7703047b37b28dc34e6990205d758a2454b39bc655b460606745fadcb530
```

---

## 來源搜尋 URL

- X Latest CVE/POC：https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- X Latest GitHub C2／紅隊：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&src=typed_query&f=live
- X Latest APT／malware：https://x.com/search?q=(APT%20OR%20malware)%20(analysis%20OR%20report)&src=typed_query&f=live
- X GeoServer 原披露：https://x.com/search?q=q1uf3ng%20GeoServer&src=typed_query&f=live
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 諮詢 RSS：https://www.cisa.gov/cybersecurity-advisories/all.xml
- The Hacker News RSS：https://feeds.feedburner.com/TheHackersNews
- Nuclei templates releases：https://github.com/projectdiscovery/nuclei-templates/releases
