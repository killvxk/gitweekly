# X 安全情報晚報 · 2026-08-13

> 蒐集窗口：約過去 24 小時（至聖地牙哥時間 2026-08-13 20:30）  
> 主源：X 瀏覽器 session（已登入 Latest 搜尋；X API 仍 `client-not-enrolled`，未用 API 假裝有搜尋結果）  
> 備援：CISA / NVD / GitHub / Check Point / Huntress / BleepingComputer / The Hacker News / Rapid7 / Unit 42 / Wiz  
> 規則：每條含完整 https URL；沒有 IoC 寫明「未見公開 IoC」

## 今日摘要

- **CISA KEV（8/11）**：Metabase **CVE-2026-72898**（CVSS 10.0 未授權 SQLi）、Windows **CVE-2026-68820**（Lazarus 在野 0day）、Cisco ASA/FTD **CVE-2026-20349**。聯邦期限：**8/14**（68820 為 **8/25**）。
- **SharePoint CVE-2026-55040**：Rapid7 公開 PoC 後，8/12–13 蜜罐已見利用；可鏈 **CVE-2026-63520** 做未授權 RCE。
- **vCenter CVE-2026-59310**：今晚 X Latest 多帳在轉；QUIRSO 稱至少 **361** 個受害 IP 被打上 reverse SSH。
- **Adobe Commerce CVE-2026-71362**（APSB26-92）：Sansec 已擋到帳號劫持利用。
- **Gitea CVE-2026-59774**（CVSS 9.8 未授權讀檔→RCE）與 **WordPress XSS2Shell CVE-2026-64638** PoC／Nuclei 模板在 X 上擴散。
- **ShieldBreak**：Nightmare Eclipse 稱繞過 Defender 對 **CVE-2026-50656** 的修補。
- **Lazarus Dream Job**：Check Point 全文給出 Troy／RelayShell／SecurityPDF C2 與雜湊。
- **Akira**：Huntress 首次記錄該家族用 Safe Mode 關 EDR。

---

## CVE / POC / 漏洞

### 1. CVE-2026-72898 — Metabase 未授權 SQLi（KEV，CVSS 10.0）
入口 `/api/session/reset_password`，未授權即可向應用庫注入 SQL、拿管理員並竊取連庫憑證。Wiz 稱 8/10 已見公開 PoC；CISA 8/11 入 KEV，期限 **2026-08-14**。臨時緩解：擋該 endpoint。  
X：https://x.com/DhiyaneshDK/status/2087422651648422269 （Nuclei 模板＋GHSA）  
地址：
- https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf
- https://www.metabase.com/blog/security-update
- https://nvd.nist.gov/vuln/detail/CVE-2026-72898
- https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.wiz.io/blog/inside-the-metabase-sqli-exploited-in-the-wild
- https://www.dataminr.com/resources/intel-brief/cve-2026-72898-exposes-thousands-of-self-hosted-instances/
- https://github.com/codeb0ssx/CVE-2026-72898-PoC
- https://github.com/0xBlackash/CVE-2026-72898
- https://denizhalil.com/2026/08/13/cve-2026-72898-metabase-unauthenticated-sql-injection/  
IoC：未見公開 C2／掃描源 IP（漏洞面為公開 HTTP API）。修補版本以 GHSA 為準：x.58.24 / x.59.21 / x.60.17 / x.61.11 / x.62.9 / x.63.5（後續點修可能更高，以廠商頁為準）。

### 2. CVE-2026-55040 — SharePoint JWT 認證繞過（PoC 後即遭利用）+ CVE-2026-63520 RCE 鏈
Rapid7（Stephen Fewer）8/11 公開技術分析與 PoC。Defused 蜜罐 8/12 起見到同一 PoC；KEVIntel 稱 8/12–13 有多次嘗試。Microsoft 7 月已修 55040、8 月修 63520。CISA 尚未把 55040 列入 KEV。  
X：https://x.com/SecurityWeek/status/2087747974269153457 · https://x.com/rokmc_sns/status/2088035455497601298 · https://x.com/boss_sec_labo/status/2088035877486559487  
地址：
- https://github.com/sfewer-r7/CVE-2026-55040
- https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-jwt-token-authentication-bypass-cve-2026-55040/
- https://www.rapid7.com/blog/post/etr-cve-2026-63520-microsoft-sharepoint-remote-code-execution-fixed/
- https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed/
- https://nvd.nist.gov/vuln/detail/CVE-2026-55040
- https://nvd.nist.gov/vuln/detail/CVE-2026-63520
- https://www.helpnetsecurity.com/2026/08/13/microsoft-sharepoint-cve-2026-55040-poc-exploit/
- https://www.securityweek.com/sharepoint-vulnerability-exploited-shortly-after-poc-release/
- https://securityaffairs.com/197137/hacking/sharepoint-cve-2026-55040-comes-under-attack-following-public-exploit.html
- https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html
- https://www.bleepingcomputer.com/news/microsoft/hackers-leverage-new-microsoft-sharepoint-exploit-in-attacks/  
IoC：公開報導提到嘗試來自香港／日本／荷蘭／台灣／美國共 8 個 IP；具體 IP 清單未見公開（寫「未見完整掃描源 IP 表」）。PoC 腳本：`CVE-2026-55040.py`。

### 3. CVE-2026-59310 — VMware vCenter Syslog 目錄遍歷 RCE（在野 reverse SSH）
Broadcom VMSA-2026-0006，CVSS 9.8，無 workaround。QUIRSO：8/3 起 C2，8/7 已見 361 受害 IP（47 國）。落地開源 reverse SSH 做出站 C2。同公告還有認證繞過 **CVE-2026-59309**。  
X：https://x.com/aviatrixtrc/status/2088054438892077265 · https://x.com/SecureChap/status/2088053313086410828 · https://x.com/Hoorge/status/2088051727698206858 · https://x.com/connect24h/status/2088038288640930022  
地址：
- https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
- https://www.rapid7.com/blog/post/etr-critical-vmware-vcenter-vulnerabilities-allow-authentication-bypass-and-remote-code-execution-cve-2026-59309-cve-2026-59310/
- https://nvd.nist.gov/vuln/detail/CVE-2026-59310
- https://nvd.nist.gov/vuln/detail/CVE-2026-59309
- https://www.bleepingcomputer.com/news/security/critical-vmware-vcenter-rce-flaw-exploited-for-reverse-ssh-access/
- https://github.com/NHAS/reverse_ssh  
修補：vCenter 9.1.0.0300 / 9.0.2.0100 / 8.0 U3k 或 8.0 U2f。  
IoC：QUIRSO **因執法協調未公開** C2 IP／域名／樣本雜湊。未見公開 IoC 表。

### 4. CVE-2026-68820 — Windows AFD.sys／WinSock 在野 0day（Lazarus，KEV）
Check Point 7/28 報給 MSRC，8/11 Patch Tuesday 修。CISA 8/11 入 KEV，聯邦期限 **2026-08-25**。針對 Win11 build 26100／26200。細節見 APT 節。  
X：https://x.com/EsGeeks/status/2087745613295165670 · https://x.com/NeowinFeed/status/2087716542301798793 · https://x.com/BotBauR/status/2087676062117384298 · https://x.com/CyberTLDR/status/2088049907185647911 · https://x.com/iss_kk_official/status/2088040883514146819  
地址：
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820
- https://nvd.nist.gov/vuln/detail/CVE-2026-68820
- https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
- https://blog.checkpoint.com/research/state-sponsored-hackers-use-fake-job-offers-to-deliver-new-zero-day-exploit/
- https://www.bleepingcomputer.com/news/security/lazarus-hackers-exploited-windows-zero-day-to-target-defense-firms/
- https://thehackernews.com/2026/08/lazarus-exploits-windows-zero-day-to.html
- https://www.helpnetsecurity.com/2026/08/12/august-2026-patch-tuesday-cve-2026-68820/
- https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog  
IoC：見下方 APT／Lazarus 節（C2 域名／IP／雜湊已抽出）。

### 5. CVE-2026-20349 — Cisco ASA/FTD SSL VPN DoS（KEV，期限明天 8/14）
未授權特製 HTTP 打 Remote Access SSL VPN → 裝置重載。  
X：https://x.com/DFIR_Radar/status/2087737028637270401  
地址：
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF
- https://nvd.nist.gov/vuln/detail/CVE-2026-20349
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.bleepingcomputer.com/news/security/cisco-warns-of-asa-and-ftd-vpn-flaw-exploited-to-crash-devices/
- https://www.securityweek.com/cisco-patches-firewall-zero-day-exploited-for-dos-attacks/  
IoC：未見公開掃描源 IP。

### 6. CVE-2026-62832 — Windows User Profile Service「LegacyHive」LPE
Nightmare Eclipse 7 月 Patch Tuesday 當日丟 PoC；8 月正式修。需本機另一帳戶憑證，跟進 classes hive 等管理員登入執行。  
X：https://x.com/aviatrixtrc/status/2088053356891705751  
地址：
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62832
- https://nvd.nist.gov/vuln/detail/CVE-2026-62832
- https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-legacyhive-windows-zero-day-vulnerability/  
IoC：未見公開 C2（本機 LPE PoC）。

### 7. CVE-2026-63077 — JetBrains TeamCity 未授權 RCE（KEV）
Agent polling 反序列化，未授權 OS 命令。升級 2025.11.7 或 2026.1.3。  
地址：
- https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/
- https://blog.jetbrains.com/teamcity/2026/08/cve-2026-63077-update/
- https://github.com/advisories/GHSA-94gx-v738-fx9w
- https://github.com/sfewer-r7/CVE-2026-63077
- https://www.rapid7.com/blog/post/ra-unauthenticated-rce-in-jetbrains-teamcity-cve-2026-63077/
- https://nvd.nist.gov/vuln/detail/CVE-2026-63077
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog  
IoC：未見公開 C2。

### 8. CVE-2026-66804 — Windows Cross Device Service LPE
X：https://x.com/Nadsec11/status/2087751567965663686  
地址：
- https://github.com/Rat5ak/CVE-2026-66804-CrossDevice-Service-EoP
- https://github.com/DavidCarliez/CVE-2026-66804-CrossDevice-LPE
- https://nvd.nist.gov/vuln/detail/CVE-2026-66804  
IoC：未見公開 C2（PoC 倉庫）。

### 9. CVE-2026-27912 ResetNightmare（任意 AD 密碼重設）
X：https://x.com/nicoboettcher/status/2087722532665270722  
地址：
- https://www.semperis.com/blog/identity-crisis-novel-vulnerabilities-leading-to-kerberos-downgrade-dos-and-full-domain-takeover/
- https://github.com/Semperis-Community/ResetNightmare
- https://github.com/XedSama/ResetNightmare-CVE-2026-27912-
- https://github.com/XedSama/ResetNightmare-Python
- https://github.com/mihat2/ResetNightmare-impacket
- https://github.com/YildirimMesut/ResetNightmare.py
- https://nvd.nist.gov/vuln/detail/CVE-2026-27912  
IoC：未見外網 C2（域內攻擊）。

### 10. Adobe ColdFusion／Campaign Classic 三則 CVSS 10.0（8/11–12 公告，尚未見利用）
- ColdFusion OS command injection **CVE-2026-48362**（10.0）；另 **CVE-2026-48273**（9.9 eval injection）、**CVE-2026-71384**（9.6）
- Campaign Classic 錯誤授權 **CVE-2026-71398**、**CVE-2026-27302**（皆 10.0）；SQLi **CVE-2026-48381**（9.0）
修補：ColdFusion 2025.0.12 / 2023.0.23；Campaign Classic v7 7.4.4 build 9400。Adobe 稱當時未知在野利用。  
地址：
- https://www.securityweek.com/adobe-urges-immediate-patching-of-critical-coldfusion-campaign-classic-flaws/
- https://thehackernews.com/2026/08/adobe-patches-three-cvss-100-coldfusion.html
- https://nvd.nist.gov/vuln/detail/CVE-2026-48362
- https://nvd.nist.gov/vuln/detail/CVE-2026-71398
- https://nvd.nist.gov/vuln/detail/CVE-2026-27302
- https://helpx.adobe.com/security.html  
IoC：未見公開 IoC。

### 11. WordPress 相關 KEV（早報）
X：https://x.com/Npj8448/status/2087731887322341429  
地址：
- https://nvd.nist.gov/vuln/detail/CVE-2026-15459
- https://nvd.nist.gov/vuln/detail/CVE-2026-28139
- https://nvd.nist.gov/vuln/detail/CVE-2026-66665
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog  
IoC：未見公開 C2。

### 12. Palo Alto 8/12 公告（含 CVE-2026-0301）
X：https://x.com/The_Cyber_News/status/2087715510490440136  
地址：
- https://security.paloaltonetworks.com/CVE-2026-0301
- https://security.paloaltonetworks.com/CVE-2026-0300
- https://security.paloaltonetworks.com/CVE-2026-0281  
IoC：未見公開 C2。

### 13. CISA ICS 公告（2026-08-13）
本日多則 ICS 諮詢（Siemens Parasolid／SLS／Desigo／Siveillance、Johnson Controls Airwall／Metasys 等）。  
地址：
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-10
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-07
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-08
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-03
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-14
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-09
- https://www.cisa.gov/cybersecurity-advisories/all.xml  
IoC：未見公開 C2（產品漏洞公告）。

### 14. CVE-2026-71362 — Adobe Commerce／Magento 未授權帳號劫持（APSB26-92，已見利用）
Sansec Shield 在公告後已擋到利用：未授權即可把 session 切到其他顧客帳號。Adobe 用獨立 patch 檔發佈，非完整 Composer 包。
X：https://x.com/CwealthSentinel/status/2088056006123164104
地址：
- https://helpx.adobe.com/security/products/magento/apsb26-92.html
- https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-adobe-commerce-flaw-to-hijack-customer-accounts/
- https://sansec.io/research/adobe-commerce-account-takeover-apsb26-92
- https://securityaffairs.com/197149/hacking/adobe-commerce-cve-2026-71362-comes-under-attack-shortly-after-public-disclosure.html
- https://www.cve.org/CVERecord?id=CVE-2026-71362
IoC：未見公開 C2／掃描源 IP（Sansec 未公開攻擊 IP）。

### 15. CVE-2026-59774 — Gitea 未授權任意檔案讀取 → RCE（CVSS 9.8）
公開倉 `POST /{owner}/{repo}/markup` 的 Org-mode `#+INCLUDE` 可讀 `app.ini` 的 `INTERNAL_TOKEN`，再打內部 API 寫 Git hook。影響 1.22.1–1.27.0，修 1.27.1。
X：https://x.com/MalwareBibleJP/status/2088051983911682544
地址：
- https://github.com/go-gitea/gitea/security/advisories/GHSA-6v53-hr58-556r
- https://nvd.nist.gov/vuln/detail/CVE-2026-59774
- https://github.com/FlowerWitch/CVE-2026-59774_docker
IoC：未見公開 C2（自我託管服務漏洞）。

### 16. CVE-2026-64638 — WordPress XSS2Shell（pre-auth XSS → 管理員 RCE）
`wp-login.php` 解析差異 XSS，鏈 Application Password 上傳外掛。WordPress 7.0.3（回溯至 4.7 維護分支）。
X：https://x.com/wilderko/status/2087313471327138300 · https://x.com/nethemba/status/2087313285766943013 · https://x.com/emgeekboy/status/2085825147009995249
地址：
- https://github.com/Boreas37/CVE-2026-64638-PoC-XSS2Shell-
- https://github.com/4minx/CVE-2026-64638
- https://pwn.ai/blog/xss2shell
- https://github.com/projectdiscovery/nuclei-templates/pull/16785
- https://nvd.nist.gov/vuln/detail/CVE-2026-64638
- https://wordpress.org/news/2026/08/wordpress-7-0-3-release/
IoC：未見公開 C2。落地外掛路徑示意：`/wp-content/plugins/xss2shell/xss2shell.php`（PoC）。

### 17. CVE-2026-43074 — Linux eventpoll 提權（Pixel 10 Pro PoC）
X 稱 Anthropic Mythos 發現，PoC 打 Pixel 10 Pro。
X：https://x.com/securityLab_jp/status/2088053246611067098
地址：
- https://rocket-boys.co.jp/security-measures-lab/linux-kernel-eventpoll-privilege-escalation-cve-2026-43074/
- https://nvd.nist.gov/vuln/detail/CVE-2026-43074
IoC：未見公開 C2（本機 LPE）。


---

## 工具與 GitHub 發佈

### 1. Rapid7 SharePoint JWT PoC
- https://github.com/sfewer-r7/CVE-2026-55040
- https://github.com/sfewer-r7/CVE-2026-63077

### 2. Metabase SQLi PoC（今日新建）
- https://github.com/codeb0ssx/CVE-2026-72898-PoC （2026-08-13）
- https://github.com/0xBlackash/CVE-2026-72898

### 3. cPanel/WHM 認證繞過 CVE-2026-41940 PoC（今日，119★）
- https://github.com/pemarine/cve-2026-41940-PoC

### 4. ResetNightmare 遠端／Python 移植（今日）
- https://github.com/YildirimMesut/ResetNightmare.py
- https://github.com/Semperis-Community/ResetNightmare

### 5. Android GKI futex PI UAF GhostLock（CVE-2026-43499）
- https://github.com/wzhdgithub/GhostLock
- https://github.com/pimpamebanihah/cve-2026-43499-app.so

### 6. Joomla AcyMailing 未授權 SQLi 掃描器
- https://github.com/nullwhisper/CVE-2026-56292-AcyMailing-SQLi

### 7. Netis NC63 PoC CVE-2026-73673
- https://github.com/ozcanpng/CVE-2026-73673

### 8. Cross Device LPE / ShieldBreak
X：https://x.com/Nadsec11/status/2087751567965663686 · https://x.com/shojiueda/status/2087699837609509063  
- https://github.com/Rat5ak/CVE-2026-66804-CrossDevice-Service-EoP
- https://github.com/MSNightmare/ShieldBreak

### 9. Nuclei
- 引擎 v3.11.1（2026-08-08，JS 模板須簽名）：https://github.com/projectdiscovery/nuclei/releases
- 模板庫（持續推送）：https://github.com/projectdiscovery/nuclei-templates
- C2 SSL 指紋模板目錄：https://github.com/projectdiscovery/nuclei-templates/tree/main/ssl/c2

### 10. reverse_ssh（vCenter 活動中被用來做 C2）
- https://github.com/NHAS/reverse_ssh

### 11. TrustMeBro — Authenticode 簽名操縱（紅隊）
X：https://x.com/Dinosn/status/2086863509988540591
- https://github.com/KriyosArcane/TrustMeBro

### 12. XSS2Shell PoC + Nuclei
- https://github.com/Boreas37/CVE-2026-64638-PoC-XSS2Shell-
- https://github.com/projectdiscovery/nuclei-templates/pull/16785

### 13. ShieldBreak（Nightmare Eclipse，稱繞過 CVE-2026-50656）
X：https://x.com/ThreatLocker/status/2088021300266545498 · https://x.com/dejital_secure/status/2088018022732800314 · https://x.com/ncxceo/status/2088038425676923349 · https://x.com/shojiueda/status/2087699837609509063
- https://github.com/MSNightmare/ShieldBreak
- https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html


---

## APT / Malware 分析

### 1. Lazarus — Operation Dream Job + CVE-2026-68820 + Troy + RelayShell
假求職（Lockheed Martin／Enveil 偽裝）、SecurityPDF 篡改閱讀器、MISTPEN（Graph/OneDrive C2）、FudModule v3.1、ForestTiger、新後門 **Troy**（17 條命令）、Roundcube **CVE-2025-49113** + **RelayShell** PHP 中繼。目標：歐印巴防務／航太。  
X：https://x.com/EsGeeks/status/2087745613295165670 · https://x.com/BotBauR/status/2087676062117384298  
地址：
- https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
- https://blog.checkpoint.com/research/state-sponsored-hackers-use-fake-job-offers-to-deliver-new-zero-day-exploit/
- https://www.bleepingcomputer.com/news/security/lazarus-hackers-exploited-windows-zero-day-to-target-defense-firms/
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820  
地址／IoC（Check Point 原文，defang 已保留）：
- 域名：`envell.xyz` · `enveil.online` · `uxtramine.org`（原文 `envell[.]xyz` / `enveil[.]online` / `uxtramine[.]org`）
- IP：`135.181.67.203` · `135.181.185.158`（原文 `135.181.67[.]203` / `135.181.185[.]158`）
- PDF 標記字串：`This document is encrypted with sumatrapdf reader!!!!!!!!!!!!`
- XOR key：`0x39`；落地：`%TEMP%\new.exe`
- Sideload DLL：`libmupdf.dll`
- PDB：`E:\HK\Tool_Module\Troy_Handle\1Troy_Create_Dll_Tool\x64\Release\Test_Dll.pdb`
- FudModule 樣本：`3b6378df8442e63a6ed7317075913e4720847a510d95022d4a8347c2637c245d`
- RelayShell：`21c3ad4838c4324bc5f081021da5fb2e9073d0c9304087811c21eb47c9e22762` · `cc4e06aa378a190f71384c03023bb3d18a6d66e297d46701220e132963d2e222`
- SecurityPDF.exe：`743172aab606974b054a64561534ae66baa3a840657f79d7c6fa18350e8d45d1` · `db3d69b7eeda2e35e23006bf4b7e206281fce809584207214fc213f9bc30376d`
- Troy：`590fb6ae19480d694e08ee85859cad8066f2f87e7e5abba2960c6d115e1615d6` · `68d4fba7b1300a59cd6212c08910a260cd71b40cd9f51cac933030a68faac0bb` · `a738059ce07c951c31ab2da3d93d8f69bff32f9b7d933dbf5943441b9cc99075`
- 完整 loader／MISTPEN／ForestTiger／PDF payload 雜湊表見 Check Point「IOCs」節（過長不重複全貼，以原文為準）。

### 2. Akira — 首次用 Safe Mode 關 EDR（加密失敗，外洩成功）
2026-08-04：無 MFA 的 SonicWall SSL VPN 噴憑證 → DC RDP → WinRAR + s5cmd 上傳 S3 → AnyDesk → `msconfig` 進 Safe Mode with Networking。Huntress／Defender RTP 失效約 10 分鐘；`akira.exe` 因虛擬記憶體不足未加密。  
地址：
- https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr
- https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/  
地址／IoC（Huntress）：
- 初始 VPN 成功來源 IP：`72.23.77.35`（原文 `72.23.77[.]35`）
- 跳板主機名：`WIN-DNCVG09TAT8`
- 落地檔：`C:\ProgramData\AdUsers.txt` · `C:\ProgramData\AdComp.txt`
- `s5cmd.exe` SHA256：`e2356c742c74cce5c6b6100162d0071a3f71e2fed2ed895c2011061a95b3299a`
- `akira.exe` SHA256：`414b9985f46714f44dd1bd63860d2a48dcfababcfe5c712a4b4f575378127a56`
- AnyDesk Client-ID：`1778787240`
- 登錄：`HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\AnyDesk`
- 偵測名：`Ransom:Win32/Akira.B!ibt`
- 事件：Kernel-Boot EID 27 `SAFEBOOT:NETWORK` · Kernel-General EID 12 `BootMode=2`

### 3. Kimwolf v7 殭屍網路（Unit 42，8/11）
X：https://x.com/rst_cloud/status/2087753121556488593  
地址：
- https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/  
IoC：報導提及以太坊解析 C2、Android/ELF payload；完整 IP／合約見 Unit 42 原文表（本節未逐條轉錄）。

### 4. LiteLLM 供應鏈（TeamPCP／遭入侵 Trivy Action）
X：https://x.com/BigVikDada/status/2087695871328600201  
地址：
- https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-ai-gateway-attack-chain-20260617-c/
- https://nvd.nist.gov/vuln/detail/CVE-2026-42271
- https://github.com/advisories/GHSA-V4P8-MG3P-G94G  
IoC：PyPI `LiteLLM 1.82.7`、`1.82.8`；檔 `litellm_init.pth`；路徑 `/root/.config/sysmon/sysmon.py`。

### 5. DeadLock ransomware（Microsoft 8/10）
Rust 加密器 + 去中心化復原基礎設施。  
地址：
- https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/  
IoC：見 Microsoft 原文 IoC 表（本輪未逐條轉錄）。

### 6. Armored Likho APT — BusySnake 資訊竊取
X 稱假捐款 App，俄／巴西／哈薩克政府網，橫向後偷 Telegram session 與錄音。
X：https://x.com/aviatrixtrc/status/2088053112531562622
地址：卡片指向 aviatrix.ai「Armored Likho Deploys BusySnake Infostealer in 2026 Cyber-Espionage Campaign」（t.co：https://t.co/ymGueeExML，未展開到獨立原文 permalink）。
IoC：未見公開 IoC。

### 7. ShieldBreak vs Defender CVE-2026-50656
Nightmare Eclipse 稱既有修補可被繞過，Win11 25H2／Server 2025 得 SYSTEM。與早報 ShieldBreak 倉庫為同一條線。
X：https://x.com/ThreatLocker/status/2088021300266545498 · https://x.com/dejital_secure/status/2088018022732800314
地址：
- https://github.com/MSNightmare/ShieldBreak
- https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html
IoC：未見公開 C2（本機 PoC）。


---

## 地址／IoC 匯總（可複製）

```
# 公告／文章
https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
https://www.cisa.gov/known-exploited-vulnerabilities-catalog
https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf
https://www.wiz.io/blog/inside-the-metabase-sqli-exploited-in-the-wild
https://github.com/sfewer-r7/CVE-2026-55040
https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-jwt-token-authentication-bypass-cve-2026-55040/
https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
https://www.bleepingcomputer.com/news/security/critical-vmware-vcenter-rce-flaw-exploited-for-reverse-ssh-access/
https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62832
https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF
https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr
https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/
https://github.com/projectdiscovery/nuclei/releases
https://github.com/NHAS/reverse_ssh
https://github.com/pemarine/cve-2026-41940-PoC
https://github.com/codeb0ssx/CVE-2026-72898-PoC
https://github.com/Semperis-Community/ResetNightmare
https://github.com/Rat5ak/CVE-2026-66804-CrossDevice-Service-EoP
https://nvd.nist.gov/vuln/detail/CVE-2026-72898
https://nvd.nist.gov/vuln/detail/CVE-2026-55040
https://nvd.nist.gov/vuln/detail/CVE-2026-59310
https://nvd.nist.gov/vuln/detail/CVE-2026-68820
https://nvd.nist.gov/vuln/detail/CVE-2026-20349
https://nvd.nist.gov/vuln/detail/CVE-2026-62832
https://nvd.nist.gov/vuln/detail/CVE-2026-63077
https://nvd.nist.gov/vuln/detail/CVE-2026-48362

https://helpx.adobe.com/security/products/magento/apsb26-92.html
https://github.com/go-gitea/gitea/security/advisories/GHSA-6v53-hr58-556r
https://github.com/Boreas37/CVE-2026-64638-PoC-XSS2Shell-
https://github.com/KriyosArcane/TrustMeBro
https://pwn.ai/blog/xss2shell
https://sansec.io/research/adobe-commerce-account-takeover-apsb26-92
https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-adobe-commerce-flaw-to-hijack-customer-accounts/
https://nvd.nist.gov/vuln/detail/CVE-2026-59774
https://nvd.nist.gov/vuln/detail/CVE-2026-64638
https://nvd.nist.gov/vuln/detail/CVE-2026-71362
https://x.com/aviatrixtrc/status/2088054438892077265
https://x.com/MalwareBibleJP/status/2088051983911682544
https://x.com/DhiyaneshDK/status/2087422651648422269
https://x.com/wilderko/status/2087313471327138300
https://x.com/CyberTLDR/status/2088049907185647911


https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage
https://sed-cms.broadcom.com/sites/default/files/2026-08/Jewelbug%20Dossier.pdf
https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/
https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/08/dissecting-the-jwr-phishing-framework.txt
https://nvd.nist.gov/vuln/detail/CVE-2026-73570
https://nvd.nist.gov/vuln/detail/CVE-2026-33017
https://github.com/lxxexxbxx/CVE-2026-33017
https://www.sysdig.com/blog/cve-2026-33017-how-attackers-compromised-langflow-ai-pipelines-in-20-hours
https://www.manageengine.com/products/passwordmanagerpro/advisory/cve-2026-12263.html
https://github.com/QUIRSO/QTRDetectionContent/blob/main/2026-08-10_reverse_ssh_generic.yar
https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-02

# Lazarus C2 / 站點
https://envell.xyz
https://enveil.online
https://uxtramine.org
135.181.67.203
135.181.185.158

# Lazarus 雜湊（節選）
3b6378df8442e63a6ed7317075913e4720847a510d95022d4a8347c2637c245d
21c3ad4838c4324bc5f081021da5fb2e9073d0c9304087811c21eb47c9e22762
743172aab606974b054a64561534ae66baa3a840657f79d7c6fa18350e8d45d1
590fb6ae19480d694e08ee85859cad8066f2f87e7e5abba2960c6d115e1615d6

# Akira
72.23.77.35
WIN-DNCVG09TAT8
e2356c742c74cce5c6b6100162d0071a3f71e2fed2ed895c2011061a95b3299a
414b9985f46714f44dd1bd63860d2a48dcfababcfe5c712a4b4f575378127a56
AnyDesk 1778787240
C:\ProgramData\AdUsers.txt
C:\ProgramData\AdComp.txt

# LiteLLM
LiteLLM 1.82.7 / 1.82.8
litellm_init.pth
/root/.config/sysmon/sysmon.py
```

vCenter 活動：QUIRSO 未見公開 IoC。SharePoint 掃描源：未見完整 IP 表。


---

## 補遺（公開源交叉核對，晚報交稿後補）

X 瀏覽器掃完後，GitHub／NVD／Symantec／Talos 又對上幾條晚報初版沒寫進去的。

### CVE

#### CVE-2026-73570 — Zimbra Collaboration SNMP 路徑未授權 RCE
可選套件 `zimbra-snmp` 開啟通知時，未淨化 SMTP 輸入可以 zimbra 用戶跑 OS 命令。ZCS < 10.1.20。NVD 今日公開。  
地址：
- https://nvd.nist.gov/vuln/detail/CVE-2026-73570
- https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories
- https://wiki.zimbra.com/wiki/Security_Center  
IoC：未見公開 IoC。

#### CVE-2026-33017 — Langflow 未授權 RCE（已在 KEV；今日多個 PoC）
`POST /api/v1/build_public_tmp/{flow_id}/flow` 未授權即可執行節點 Python。  
地址：
- https://github.com/lxxexxbxx/CVE-2026-33017
- https://github.com/sonnelon/CVE-2026-33017-PoC
- https://github.com/langflow-ai/langflow/security/advisories/GHSA-vwmf-pq79-vjvx
- https://www.sysdig.com/blog/cve-2026-33017-how-attackers-compromised-langflow-ai-pipelines-in-20-hours
- https://nvd.nist.gov/vuln/detail/CVE-2026-33017
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-33017  
IoC：未見公開 C2（PoC 倉庫）。

#### CVE-2026-12263 / CVE-2026-11840 — ManageEngine PMP／PAM360
SAML 驗證繞過與已認證 SQLi。PMP < 13232；PAM360 < 8551／8552。  
地址：
- https://www.manageengine.com/products/passwordmanagerpro/advisory/cve-2026-12263.html
- https://www.manageengine.com/products/passwordmanagerpro/advisory/cve-2026-11840.html
- https://nvd.nist.gov/vuln/detail/CVE-2026-12263
- https://nvd.nist.gov/vuln/detail/CVE-2026-11840  
IoC：未見公開 IoC。

#### Flowise < 3.1.3 多則嚴重漏洞（NVD 今日）
含 CVE-2026-73483（9.4）、CVE-2026-73601 等。  
地址：
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-9gvv-qjj3-2p6g
- https://nvd.nist.gov/vuln/detail/CVE-2026-73483
- https://nvd.nist.gov/vuln/detail/CVE-2026-73601  
IoC：未見公開 IoC。

#### ICS 補 CVE
- Haiwell IoT Cloud HMI Gateway 命令注入（root）：https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-02 · https://nvd.nist.gov/vuln/detail/CVE-2026-19188
- Siemens Siveillance VMS RCE：https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-09 · https://nvd.nist.gov/vuln/detail/CVE-2026-3014
- AVEVA Enterprise SCADA 反序列化：https://www.cisa.gov/news-events/ics-advisories/icsa-26-225-01 · https://nvd.nist.gov/vuln/detail/CVE-2025-7639  
IoC：未見公開 C2。

#### 工具補
- QUIRSO reverse_ssh YARA：https://github.com/QUIRSO/QTRDetectionContent/blob/main/2026-08-10_reverse_ssh_generic.yar
- FUXA 未授權 RCE CVE-2026-25938：https://github.com/judgedbykira/CVE-2026-25938-FUXA-Unauthenticated-RCE
- cPanel 另見 watchTowr 分析／Sorry 勒索利用：https://labs.watchtowr.com/the-internet-is-falling-down-falling-down-falling-down-cpanel-whm-authentication-bypass-cve-2026-41940/ · https://github.com/watchtowrlabs/watchTowr-vs-cPanel-WHM-AuthBypass-to-RCE.py

### APT

#### Jewelbug（Earth Alux／REF7707／CL-STA-0049）
Symantec：中東 15 個政府 webmail 種腳本、WebSocket C2、假 Flash 裝 Antino、PDF Viewer 擴充；並行加密貨幣詐騙共用 XG-Web 面板。另有 ClientKing Linux／路由器植入。  
地址：
- https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage
- https://sed-cms.broadcom.com/sites/default/files/2026-08/Jewelbug%20Dossier.pdf
- https://www.bleepingcomputer.com/news/security/hackers-breach-govt-webmail-while-running-parallel-crypto-fraud/  
地址／IoC（卷宗節選，defang 保留）：
- 域名：`fonts.tarotfree101.top` · `fonts.chrorne.com` · `robot.avbliud.com` · `microsoft-flash.com` · `www.wps-cn.com` · `www.f1ash.org.cn` · `browser-update.pages.dev` · `eastus2.wac-azure.com` · `mailbycloud.com` · `www.jkskhei.com` · `ns1.jkskhei.com` · `dns.wizkidblogger.com`
- IP：`43.246.208.236` · `103.87.9.62` · `152.42.174.151` · `43.246.208.179` · `47.84.37.113:8080` · `47.84.51.173:1880` · `167.71.195.255` · `38.12.1.47` · `129.212.237.224`
- 下載：`hxxp://d2nq35tel3ucuo.cloudfront.net/LtVGUSsyUTDA.log` · `hxxps://pub-abfa7742e315485a98a5fafd6dbfb68e.r2.dev/hjgzBskgslc.dll.iwq`
- 擴充 ID：`kijgcnllicmahabnlhpomdlgnjnhnloe` · `kcadidgfgpkkogolajeofgbfnoadiccj` · `popoijcenfhnkdfeppmjfbmjankcpojl`
- 雜湊與完整表：見 PDF（55 條已抄進 inbox JSON）。

#### Talos — JWR 釣魚框架（疑 The Outsider PhaaS）
44 個假結帳／登入頁，AES-CTR WebSocket C2，東南亞／中東 SMS 偽裝過路費／郵政。  
地址：
- https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/
- https://github.com/Cisco-Talos/IOCs/blob/main/2026/08/dissecting-the-jwr-phishing-framework.txt
- https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/08/dissecting-the-jwr-phishing-framework.txt  
地址／IoC（Talos 原文 defang）：
- 域名：`xiaomimiyizu.xyz` · `dubai.customszf.top` · `anzrewardse-homes.info` · `hsbcrewards-homesa.info` · `lloydsbank-homesa.info` · `rbcroyalbank-homesa.cc` · `westpacone-homesc.info` · `ae.emiratea-post.top` · `bankfab-alert.cfd` · `lta-billcenter.com` · `lta-epayment.top`
- IP：`47.88.78.148` · `47.90.223.199` · `43.156.227.15` · `43.160.241.151`
- 樣本 SHA256：`464e46e3e45dc99228aae7b0c0051d2759b937f164eeca7e34416963c195d227` · `00f36ddd07320d492035ccc2f09142139120ed5d6b58705777647e1e4b05aacc` · `1a27e992576f8aaf2c1f177c580622923d3d3a9264f43740bb1f4fb8676a7c5d` · `917234a575bfe049b6cefcee7f8e98808bcc2753c681793ccc55b6b7c1be7017`

## 來源搜尋 URL

- https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20mythic)&src=typed_query&f=live
- https://x.com/search?q=(APT%20OR%20%22malware%20analysis%22%20OR%20%22threat%20report%22)&src=typed_query&f=live
- https://x.com/search?q=(CVE-2026%20OR%20CVE-2025)%20(PoC%20OR%20exploit%20OR%20patch)&src=typed_query&f=live
- https://api.github.com/search/repositories?q=CVE-2026+created:%3E2026-08-11
- https://www.cisa.gov/cybersecurity-advisories/all.xml
- https://www.bleepingcomputer.com/feed/
- https://feeds.feedburner.com/TheHackersNews
