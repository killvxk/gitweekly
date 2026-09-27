# X 安全情报晚报 · 2026-09-23

> 搜集窗口：圣地亚哥时间 **2026-09-22 20:00 至 2026-09-23 ~20:45**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周三）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-23.json`（collected_at **2026-09-23T20:30:00-03:00** 量级）＋ `/workspace/tools-news-pulse-2026-09-23.json`＋ `/workspace/enrich-extra-2026-09-23.json`＋ `/workspace/enrich-2026-09-23/`。CISA KEV catalogVersion **2026.09.23**／**1721** 条／dateReleased **2026-09-23T12:51:35.821Z**（相对昨日 **2026.09.22／1721**：**count Δ0**；CVE 集合相同；**无 NEW dateAdded=2026-09-23**；无今日 CISA new-KEV 警报页——属 **catalog 再发布／重打戳**）。
> **期限今日 09-23**：Google Chromium V8 **CVE-2026-87491**（在野）。**新起逾期（due 曾=09-22）**：Microsoft **CVE-2026-81963**／**CVE-2026-85880**。**明日 due 09-24**：**Zyxel CVE-2026-7273**。仍 due **09-25**：Check Point **CVE-2026-85102／CVE-2026-93616**、Arista VeloCloud **CVE-2026-93952**、F5 BIG-IP APM **CVE-2026-94127**（＋ JFrog Artifactory **CVE-2026-42016／CVE-2026-42018**）。仍逾期重点：**Chromium CVE-2026-85046**／**Pixel CVE-2026-58704**／**Cisco ISE CVE-2026-76460**／**Acronis CVE-2026-87886**／Linux trio **CVE-2025-39682／CVE-2025-39964／CVE-2026-53266** 等。
> X：`/workspace/x-posts-2026-09-23.json`（合并 **72** 条唯一：A28／B10／C21／LWiS14；跨源 ID 重叠 **1**；相对 prior seen_ids 重叠 **1**／**+71** 新 id；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **1.0h**。Search B 可见约 **34h**（含 Sep 22 工具帖延续，其中 1 条已见 prior seen_ids）。Search C 约 **3.7h**。LWiS List 约 **21h**（**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。Latest 窗口常远短于 24h。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【主条 · KEV 无 NEW · catalog 再发布】** CISA KEV catalogVersion **2026.09.23**／**1721** 条／dateReleased **2026-09-23T12:51:35.821Z**（相对昨日 **2026.09.22／1721**：**count Δ0**，CVE 集合相同；无 09-23 新增 dateAdded；无今日 CISA new-KEV 警报页）。公开备援仍为 KEV／厂商 PRIMARY；X 作交叉。昨日四条警报（仍适用）：https://www.cisa.gov/news-events/alerts/2026/09/22/cisa-adds-four-known-exploited-vulnerabilities-catalog

- **【期限今日 · Chromium CVE-2026-87491 · 在野】** Google Chromium V8 越界写；Google 已知在野利用；联邦 due **今日 09-23**。防御：立即升至 Chrome **153.0.8010.36+**（及 Edge-Chromium 等）；BOD 26-04 triage。
  Chrome：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87491
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87491

- **【新起逾期 · Microsoft×2】** **CVE-2026-81963**（Windows Update Stack 链接跟随 → SYSTEM）／**CVE-2026-85880**（Windows 堆溢出）due 曾为 **09-22**，今日起 **newly_overdue**。防御：核验 9 月 Windows 更新；BOD 26-04。
  MSRC 81963：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963
  MSRC 85880：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880
  NVD 81963：https://nvd.nist.gov/vuln/detail/CVE-2026-81963
  NVD 85880：https://nvd.nist.gov/vuln/detail/CVE-2026-85880

- **【明日 due 09-24 · Zyxel CVE-2026-7273】** GS1900 CGI 栈溢出；LAN 未认证 OS 命令面。防御：升至列明 2.90(*.2)C0；限制管理网。
  厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273

- **【仍 due 09-25 · Check Point／Arista／F5（+ JFrog）】** 昨日 NEW：**CVE-2026-85102**／**93616**（Check Point）、**93952**（Arista VeloCloud）、**94127**（F5 BIG-IP APM）均 due **09-25**；另 near：**CVE-2026-42016**／**42018**（JFrog）。X A／LWiS 今日热议 Check Point 在野声称、watchTowr BIG-IP 研究、VeloCloud、BleepingComputer 转述。
  Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
  SK85102：https://support.checkpoint.com/results/sk/sk1000117
  SK93616：https://support.checkpoint.com/results/sk/sk1000171/
  Arista SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
  F5 K000162605：https://my.f5.com/manage/s/article/K000162605
  watchTowr：https://labs.watchtowr.com/is-this-a-joke-in-the-auth-header-f5-big-ip-unauth-heap-overflow-to-rce-cve-2026-94127/
  X：https://x.com/TweetThreatNews/status/2102903447871750610
  X：https://x.com/watchtowrcyber/status/2102900734249377909
  X（LWiS）：https://x.com/BleepinComputer/status/2102849013829541920

- **【仍逾期重点】** Chromium **CVE-2026-85046**（due 09-18）／Pixel **CVE-2026-58704**／Cisco ISE **CVE-2026-76460**／Acronis **CVE-2026-87886**（均 due 09-19）／Linux trio **CVE-2025-39682**／**CVE-2025-39964**／**CVE-2026-53266**（due 09-21）＋今日新起逾期 MS×2。
  Chrome 85046：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
  Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
  Cisco ISE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  Acronis：https://security-advisory.acronis.com/advisories/SEC-10986

- **【工具 · 核心无升版；Risky NEW RBNEWS614】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 不变；tl;dr 仍 **#346**；Risky **RBNEWS613→614**（Team Cymru 揭中国代理网络等）；BTN183／SRB183 不变。X B：AuthStrike／HackMyAgent／DeepTeam／dpapi-toolkit／KaliGPT／nuclei-templates（WP 87902）／OneDrive-UDC2（prior）等。
  RBNEWS614：https://risky.biz/RBNEWS614/
  BTN183：https://risky.biz/BTN183/
  Sliver：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
  nuclei：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
  nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
  tl;dr #346：https://tldrsec.com/p/tldr-sec-346

- **【X／LWiS 交叉 · 非 KEV】** WordPress **CVE-2026-87902**（跨 A／LWiS）、Next.js **CVE-2026-94545**、cPanel **CVE-2026-87899**、MikroTik 多 CVE 声称、LWiS **PostgreSQL CVE-2026-15742**「已 PoC→RCE」声称——**非今晚 NEW KEV**；利用／PoC 声称标 **UNCONFIRMED**，**不转载步骤**。威胁面：WatchGuard／ESET AI skills／ThruntingLabs SEO→RMM；大量地下泄露 **一律 UNCONFIRMED**。
  WP GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
  Next.js：https://nextjs.org/blog/nextjs-security-update-september-22-2026
  THN cPanel：https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account_0272795595.html
  X（PG 声称）：https://x.com/kmkz_security/status/2102867842764861732

- **【LWiS List · ~21h 交叉】** 保留 14 条（与 A 重叠 1：WP 87902）。要点：Check Point／F5 watchTowr 交叉、PG 15742 声称、Oxygen Forensics 高管被捕报道、澳大利亚政府站／AIHW AI agent 入侵声称（**UNCONFIRMED**）、Windows LAPS 迁移残留、AI 代理混淆二进制研究视频等——**交叉校验，不假装为本窗口 24h Latest**。
  List：https://x.com/i/lists/1239330068461244424

## CVE / POC / 漏洞

### 1. 【期限今日 · 在野】Chromium V8 CVE-2026-87491

KEV due **2026-09-23**（今日）。V8 越界写；Chrome 稳定版博客称 Google 已知在野利用。修复示例：Chrome **153.0.8010.36+**（Linux）／**.36／.37**（Windows／Mac）。仍逾期姊妹 **CVE-2026-85046**（due 09-18）。防御：立即全量升浏览器（含托管 Edge-Chromium）；BOD 26-04 取证分流。**本报不转载利用细节。**

地址：
- Chrome：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-87491
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87491
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-87491

IoC：未见公开 IoC。

### 2. 【新起逾期 · 在野】Microsoft CVE-2026-81963／CVE-2026-85880

KEV due 曾为 **2026-09-22**，今日起 **newly_overdue**。81963：Windows Update Stack 链接跟随 → 本地提权至 SYSTEM。85880：Windows 堆溢出。防御：核验 9 月 Windows 安全更新已落地；盘点未补丁主机；BOD 26-04。

地址：
- MSRC 81963：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963
- MSRC 85880：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85880
- NVD 81963：https://nvd.nist.gov/vuln/detail/CVE-2026-81963
- NVD 85880：https://nvd.nist.gov/vuln/detail/CVE-2026-85880
- KEV 81963：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-81963
- KEV 85880：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85880

IoC：未见公开 IoC。

### 3. 【仍 due 09-25 · 在野】Check Point CVE-2026-85102／CVE-2026-93616

CISA 于 **2026-09-22** 加入 KEV（昨日 NEW；今日 catalog 再发布仍保留）；联邦 due **2026-09-25**。85102：VPN 不当证书校验 → 未认证 RCE。93616：管理面路径穿越 → 未认证脚本执行。X A／LWiS／BleepingComputer 今日继续称在野／PoC 出现——**不转载利用步骤**。修复示例见 SK：85102 — **R82.10 Jumbo Take 44+／R82 Take 126+／R81.20 Take 166+**；93616 — **R82.20 Hotfix／R82.10 Take 45+／R82 Take 127+／R81.20 Take 170+** 等。防御：立即按 SK 打 Jumbo／Hotfix；限制管理／VPN 面；证书 subject 狩猎；BOD 26-04。

地址：
- CISA 09-22 警报：https://www.cisa.gov/news-events/alerts/2026/09/22/cisa-adds-four-known-exploited-vulnerabilities-catalog
- 厂商 SK85102：https://support.checkpoint.com/results/sk/sk1000117
- 厂商 SK93616：https://support.checkpoint.com/results/sk/sk1000171/
- Check Point 博客：https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/
- 文章：https://www.hendryadrian.com/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/
- BleepingComputer：https://bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/
- NVD 85102：https://nvd.nist.gov/vuln/detail/CVE-2026-85102
- NVD 93616：https://nvd.nist.gov/vuln/detail/CVE-2026-93616
- X 原帖：https://x.com/TweetThreatNews/status/2102903447871750610
- X 原帖：https://x.com/SOCMinute/status/2102895702544179238
- X 原帖：https://x.com/ridvanyagli/status/2102900484285558784
- X 原帖：https://x.com/AbuSaud_Cyber/status/2102898008236958160
- X 原帖：https://x.com/SecNews_GR/status/2102890894055690505
- X（LWiS）：https://x.com/BleepinComputer/status/2102849013829541920

IoC（厂商观测 cert_subject，原样抄录，非穷尽）：
- `CN=vpn,OU=users,O=global`
- `CN=vpn-user,OU=users,O=global`
- `CN=vpnuser,OU=users,O=global`

### 4. 【仍 due 09-25 · 在野】F5 BIG-IP APM CVE-2026-94127

KEV due **2026-09-25**。虚拟服务器配置访问策略＋OAuth profile 时堆溢出 → 未认证数据面 RCE。watchTowr 今日公开研究标题／技术文（X A／LWiS @SinSinology 引用）——**不转载利用细节**。防御：按 K000162605 盘点 APM＋OAuth VS；先临时 iRule 再 ENG hotfix；BOD 26-04。

地址：
- 厂商 K000162605：https://my.f5.com/manage/s/article/K000162605
- watchTowr：https://labs.watchtowr.com/is-this-a-joke-in-the-auth-header-f5-big-ip-unauth-heap-overflow-to-rce-cve-2026-94127/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-94127
- X 原帖：https://x.com/_r_netsec/status/2102902852742205696
- X 原帖：https://x.com/watchtowrcyber/status/2102900734249377909
- X（LWiS）：https://x.com/SinSinology/status/2102901248068309498

IoC：未见公开 IoC。

### 5. 【仍 due 09-25 · 在野】Arista VeloCloud CVE-2026-93952

KEV due **2026-09-25**。on-prem VCO 不当输入校验。修复示例：**VCO 5.2.3.16+／6.4.2.8+**；Hosted／Dedicated 侧厂商称已处理。防御：升 on-prem VCO；将 VCO Web 限制到可信管理网；BOD 26-04。

地址：
- 厂商 SA-0183：https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-93952
- X 原帖：https://x.com/TwitGri/status/2102891232754110849
- X 原帖：https://x.com/boss_sec_labo/status/2102889368667226392

IoC：未见公开 IoC。

### 6. 【明日 due · 在野】Zyxel GS1900 CVE-2026-7273

KEV due **2026-09-24**。LAN 向 CGI 栈溢出 → 未认证 OS 命令面。防御：升至列明 **2.90(*.2)C0** 固件；限制 LAN 管理暴露。

地址：
- 厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273

IoC：未见公开 IoC。

### 7. 【仍 due 09-25 · near】JFrog Artifactory CVE-2026-42016／CVE-2026-42018

公开备援仍列 due **2026-09-25**。防御：按 JFrog Security Advisories／Self-Managed Releases 升版；限制 Artifactory 管理面。

地址：
- NVD 42016：https://nvd.nist.gov/vuln/detail/CVE-2026-42016
- NVD 42018：https://nvd.nist.gov/vuln/detail/CVE-2026-42018
- 厂商 advisories：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- 发行说明：https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases

IoC：未见公开 IoC。

### 8. 【仍逾期 · 在野】Chromium 85046／Pixel 58704／Cisco ISE 76460／Acronis 87886／Linux trio

仍逾期重点（非今日 NEW）：Chromium **CVE-2026-85046**（due 09-18）；Pixel **CVE-2026-58704**／Cisco ISE **CVE-2026-76460**／Acronis **CVE-2026-87886**（due 09-19）；Linux **CVE-2025-39682／CVE-2025-39964／CVE-2026-53266**（due 09-21）。防御：按厂商公告／发行版内核补丁；BOD 26-04。

地址：
- Chrome 85046：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- NVD 85046：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
- Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- NVD 58704：https://nvd.nist.gov/vuln/detail/CVE-2026-58704
- Cisco ISE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- NVD 76460：https://nvd.nist.gov/vuln/detail/CVE-2026-76460
- Acronis：https://security-advisory.acronis.com/advisories/SEC-10986
- NVD 87886：https://nvd.nist.gov/vuln/detail/CVE-2026-87886
- NVD 39682：https://nvd.nist.gov/vuln/detail/CVE-2025-39682
- NVD 39964：https://nvd.nist.gov/vuln/detail/CVE-2025-39964
- NVD 53266：https://nvd.nist.gov/vuln/detail/CVE-2026-53266

IoC：未见公开 IoC（或仅厂商 SK／通报内）。

### 9. 【X／LWiS · 非 KEV】WordPress CVE-2026-87902

未认证页面模板路径穿越 → 条件性 RCE；GHSA 已发；帖文建议升至 **7.1.2**。**今晚非 NEW KEV**。利用／流量上升声称 **UNCONFIRMED**。nuclei-templates 已有 yaml（Search B）。跨源重叠：A＋LWiS 同帖 `2102902106034524362`。

地址：
- GHSA：https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-7hp8-65ch-5whp
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-87902.yaml
- 日文文：https://rocket-boys.co.jp/security-measures-lab/wordpress-cve-2026-87902-71-2/
- X 原帖：https://x.com/pdiscoveryio/status/2102902106034524362
- X 原帖：https://x.com/securityLab_jp/status/2102899892800889285
- X 原帖：https://x.com/fredmdl/status/2102893237962789014
- X 原帖：https://x.com/DhiyaneshDK/status/2102720074809544970

IoC：未见公开 IoC。

### 10. 【LWiS · 非 KEV · 声称】PostgreSQL CVE-2026-15742（fuzzystrmatch OOB → RCE 声称）

@kmkz_security 称 **CVE-2026-15742**（PostgreSQL `fuzzystrmatch` 越界写）「已 PoC 到 RCE」。**本报仅记录声称；UNCONFIRMED；不转载 PoC／利用步骤。** 防御：关注 PostgreSQL 安全公告／发行版补丁；限制不可信扩展／函数面；对暴露实例做版本盘点。

地址：
- X 原帖：https://x.com/kmkz_security/status/2102867842764861732
- NVD（若已收录）：https://nvd.nist.gov/vuln/detail/CVE-2026-15742

IoC：未见公开 IoC。

### 11. 【X · 非 KEV】Next.js／cPanel／MikroTik／Forcepoint／Veeam 等

- **Next.js CVE-2026-94545**：https://nextjs.org/blog/nextjs-security-update-september-22-2026 · X https://x.com/Python_s_/status/2102899262283509792
- **cPanel CVE-2026-87899**：https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account_0272795595.html · X https://x.com/NeoteoCom/status/2102895911969947704
- **MikroTik 多 CVE 声称**（含 CVE-2026-67279／86060／67276）：https://x.com/SOCMinute/status/2102901892087005414 · https://x.com/ZannEncrypted/status/2102892151109738593 · https://socprime.com/es/blog/cve-2026-67276-dia-cero-ssh-mikrotik-routeros/（**UNCONFIRMED**；不转载利用）
- **Forcepoint CVE-2026-12974**：https://support.forcepoint.com/s/article/Security-Advisory-Security-Policy-Bypass-in-Forcepoint-Security-Engine-NGFW-CVE-2026-12974 · X https://x.com/AndreGironda/status/2102896079088021714
- **Veeam CVE-2026-32996**：https://www.veeam.com/kb4852 · X https://x.com/ngsk_ciso/status/2102889265713881188
- **Eye Security CVE-2026-75754**：https://research.eye.security/ai-vulnerability-discovery-using-the-kitten-process-how-we-found-cve-2026-75754/
- 其他 A 提及（Tomcat／GitLab／Adobe Connect／Redis CVE-2025-49844 等）：防御跟进厂商公告，**不转载 PoC**。示例 X：https://x.com/McM1Alex/status/2102901028148728215 · https://x.com/DailyDarkWeb/status/2102893367637979603 · https://x.com/djangonewsbot/status/2102895820471423006

IoC：未见公开 IoC（除非厂商另行发布）。

## 工具与 GitHub 发布

### 核心版本脉冲（公开备援）

Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 相对昨日 **无升版**。Risky Business **RBNEWS613→614（NEW 2026-09-23）**；BTN183／SRB183 不变；tl;dr 仍 **#346**。

地址：
- Sliver：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- nuclei：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- RBNEWS614：https://risky.biz/RBNEWS614/
- BTN183：https://risky.biz/BTN183/
- SRB183：https://risky.biz/SRB183/
- tl;dr #346：https://tldrsec.com/p/tldr-sec-346

IoC：未见公开 IoC。

### X Search B／相关工具仓（防御认知）

- **AuthStrike**：https://github.com/cloudbreach/AuthStrike · 原帖 https://x.com/Cloud_Breach/status/2102858268905259147（Storm-2372 测试租户声称 → **UNCONFIRMED**）
- **HackMyAgent／NanoMind**：https://github.com/opena2a-org/hackmyagent · https://x.com/EsGeeks/status/2102777566515847519
- **DeepTeam**：https://github.com/confident-ai/deepteam · https://x.com/ChrisShort/status/2102773315643334713
- **dpapi-toolkit**：https://github.com/crypt0p3g/dpapi-toolkit · https://x.com/cryptopeg/status/2102753493123752365
- **nuclei-templates WP CVE-2026-87902**：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-87902.yaml · https://x.com/DhiyaneshDK/status/2102720074809544970
- **awesome-cyber-security-tools**：https://github.com/0xh3xa/awesome-cyber-security-tools/blob/master/README.md · https://x.com/HackerOx26/status/2102709880364634458
- **adk-demo-target**：https://github.com/rbrus/adk-demo-target · https://x.com/sixi4ai/status/2102618219882438705
- **KaliGPT**：https://github.com/SudoHopeX/KaliGPT · https://x.com/r0psx_ninja/status/2102598052397932552
- **nuclei-templates Strapi CVE-2026-27886 PR**：https://github.com/projectdiscovery/nuclei-templates/pull/16304/changes/7247bac3eb5eb27cba9bc613a91abb8c9c697853 · https://x.com/zeroc00i/status/2102580743075463229（落地状态 **UNCONFIRMED**）
- **OneDrive-UDC2**：https://github.com/nmht3t/OneDrive-UDC2 · https://x.com/r1cksec/status/2102348916935012788（**prior_seen**；Cobalt Strike C2 传输面——防御认知，不转操作步骤）

IoC：工具帖未见公开 IoC。

### LWiS 相关研究／工具向交叉

- **AI 代理混淆二进制研究**（@mr_phrazer 视频＋slides／samples 仓）：https://www.youtube.com/watch?v=oGBj1v8t7Fc · https://github.com/mrphrazer/binary-cartography/tree/main/2026-09-agentic_deobfuscation · X https://x.com/mr_phrazer/status/2102855489172238667（**不转载攻击剧本步骤**）
- **Windows LAPS 迁移残留**（@RidgelineCyber）：https://x.com/RidgelineCyber/status/2102727699076714782（运维防御；命令语法省略）
- **ScriptSentry／SYSVOL**（@acjuelich）：https://x.com/acjuelich/status/2102583096348438668

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. WatchGuard Global Threat Report 2026

厂商／市场报告称网络攻击检测下降与新型终端恶意软件上升；AI tooling 支撑战术转移。防御：关注终端／EDR 覆盖与检测盲区；审阅报告中的趋势项。

地址：
- 报告：https://mysecuritymarketplace.com/reports/global-threat-report-2026/
- 厂商 PR：https://www.watchguard.com/wgrd-news/press-releases/new-watchguard-threat-report-reveals-ai-tooling-underpins-tactical-shift
- X：https://x.com/MSM_Marketplace/status/2102901516906741978
- X：https://x.com/watchguard/status/2102850537414668292

IoC：未见公开 IoC（详见原文）。

### 2. AI agent 框架攻击在线零售（归因未明）

@NSIguy 称开源 AI agent 框架被用于攻击在线零售。防御：监控异常自动化扫描／代理流量；加固互联网暴露面。

地址：
- X：https://x.com/NSIguy/status/2102898556080095551

IoC：未见公开 IoC。

### 3. ESET ～3000 恶意 AI skills

报道称 ESET 发现约 3000 个恶意 AI skills，勒索风险面转移。防御：仅从可信渠道安装 AI／助手扩展；校验签名与来源。

地址：
- 文章：https://insight.tmcnet.com/insight/eset-uncovers-3-000-malicious-ai-skills-as-ransomware-risks-shift-mudu1rsl
- X：https://x.com/rtehrani/status/2102847975399522720

IoC：未见公开 IoC。

### 4. ThruntingLabs：SEO 投毒 → 定制 RMM + Cobalt Strike

案例叙述：SEO 投毒落地定制 RMM 并衔接 Cobalt Strike。防御：狩猎异常 RMM／CS beacon；加固搜索结果点击与软件分发链。**操作步骤省略。**

地址：
- 案例：https://www.threathuntinglabs.com/threat-hunting/cases/0011
- X：https://x.com/ThruntingLabs/status/2102847943309164757

IoC：未见公开 IoC（详见案例页）。

### 5. ENISA Threat Landscape 2026 同行评议

Treadstone71 对 ENISA 2026 威胁态势的同行评议。

地址：
- 文：https://www.treadstone71.com/osint/enisa-threat-landscape-2026-peer-review-treadstone-71
- X：https://x.com/Treadstone71LLC/status/2102860607791735081

IoC：未见公开 IoC。

### 6. 【LWiS】Oxygen Forensics 高管被捕报道／AI 代理与 AD／澳政府站声称

- **@KimZetter**：称 Oxygen Forensics 两名高管因对美政府客户隐瞒俄属权／研发地被捕——按报道收录，待独立核实。文章：https://www.zetter-zeroday.com/us-based-digital-forensics-firm-hid-its-russian-ownership-from-u-s-government-customers/ · X https://x.com/KimZetter/status/2102888553944338802
- **@UK_Daniel_Card**：称 Claude 被用于攻击脆弱 AD，活动类似真实入侵杀伤链——**观察向；不转载步骤**。X https://x.com/UK_Daniel_Card/status/2102729536609919170
- **@AndrewCurran_／@j0wimo**：澳大利亚政府站／AIHW 处方数据被 OpenAI agent 渗透声称——**一律 UNCONFIRMED**。X https://x.com/AndrewCurran_/status/2102863476767297540 · https://x.com/j0wimo/status/2102873408698826952
- **@yoavalon**：开源权重模型对 Opus 5 security unlock 测试观察。X https://x.com/yoavalon/status/2102808634749296978
- **@gergely_kalman／@C2IRIS**：macOS GateKeeper 深度研究引用；HEIC 解码器→SHA-256 计算演示（研究向）。X https://x.com/gergely_kalman/status/2102884919143702976 · https://x.com/C2IRIS/status/2102863478675443845

IoC：未见公开 IoC。

### 7. 【X · 未验证】地下勒索／泄露声称（合辑）

以下均为社交／论坛列表报道，**一律 UNCONFIRMED／未验证**：
- GOLO／Shopify：https://x.com/BreachNewsHQ/status/2102899583181275551
- UlakCX／7zzz+c7k：https://x.com/CyberPulse56/status/2102897923411595745
- DaOnlySpark／GlobalAdmissions／China-Admissions：https://x.com/intels_daily/status/2102882497222615522
- ShinchanReal／Pobeda：https://x.com/intels_daily/status/2102867386361634946
- EndZone／Trump Mobile：https://x.com/DailyDarkWeb/status/2102861117970149741
- FUN&SUN：https://x.com/MonThreat/status/2102859792838721866
- Autobacs France：https://x.com/DailyDarkWeb/status/2102857599284596784
- 西班牙约 5 万条：https://x.com/DailyDarkWeb/status/2102872661307077025
- NJIK.SA：https://x.com/DailyDarkWeb/status/2102848600409547194
- Anka Team／SINEPE：https://x.com/DailyDarkWeb/status/2102844411688407422
- Barracuda／emperador／Abtach：https://x.com/ThreatAtlas/status/2102843109625188753 · https://x.com/ThreatAtlas/status/2102864741190242526 · https://x.com/FalconFeedsio/status/2102848545435038064

IoC：帖文可见主机名声称（非核验）— `GlobalAdmissions.com`／`China-Admissions.com`／`flypobeda.ru`／`njik.sa`／`sinepenopr.com.br`；其余多数 **未见公开 IoC**。Risky RBNEWS614 提及相关地下叙事亦标 **UNCONFIRMED**（https://risky.biz/RBNEWS614/）。

### 8. ICS

本日公开备援 **无 2026-09-23 新 ICS advisory 显著条目**（KEV Δ0；昨日四枚 NEW 仍为网关／编排／APM／VPN 类）。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Check Point 85102／93616（仍 due 09-25）**：证书 subject `CN=vpn,OU=users,O=global`／`CN=vpn-user,OU=users,O=global`／`CN=vpnuser,OU=users,O=global`；另见 sk1000171 厂商狩猎节。
- **地下声称可见主机名（UNCONFIRMED）**：`GlobalAdmissions.com`／`China-Admissions.com`／`flypobeda.ru`／`njik.sa`／`sinepenopr.com.br`。
- **Chromium 87491（今日 due）／MS 新逾期×2／Zyxel 明日 due／Arista 93952／F5 94127／JFrog／仍逾期 ISE／Pixel／Acronis／Linux trio／WP 87902／PG 15742 声称／工具仓**：未见可抄录公开 IoC（或仅厂商 SK 内）。
- **WatchGuard／ESET／ThruntingLabs／ENISA 评议／LWiS 澳政府站声称等**：未见公开 IoC 或详见原文；澳相关一律未验证。
- 默认无指标条目：写「未见公开 IoC」。

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

本窗口 LWiS List 只读采集：保留 **14** 条、覆盖约 **21h**（`logged_in=true`／`@seogoogle4`／`blocked=false`）；与 A 跨源重叠 1（WP 87902）；meta：`/workspace/x-lwis-list-meta-2026-09-23.json`。

## 来源搜索 URL

- X Latest A（CVE-2026 精炼）：https://x.com/search?q=%22CVE-2026%22%20-filter%3Areplies%20-from%3ACVEnew%20-from%3AIhhsanMuhammad&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／mythic／cobalt）：https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20mythic%20OR%20cobalt)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS614：https://risky.biz/RBNEWS614/
- tl;dr sec：https://tldrsec.com/
- tl;dr #346：https://tldrsec.com/p/tldr-sec-346
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 昨日四条 KEV 警报（仍适用）：https://www.cisa.gov/news-events/alerts/2026/09/22/cisa-adds-four-known-exploited-vulnerabilities-catalog
