# X 安全情报晚报 · 2026-09-21

> 搜集窗口：圣地亚哥时间 **2026-09-20 20:00 至 2026-09-21 ~20:40**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周一）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-21.json`（collected_at **2026-09-21T20:18:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-21.json`＋ `/workspace/enrich-extra-2026-09-21.json`＋ `/workspace/enrich-2026-09-21/`。CISA KEV catalogVersion **2026.09.21**／**1717** 条／dateReleased **2026-09-21T18:46:35.0873Z**（相对昨日基线 **2026.09.18／1716** 为 **+1**；**NEW CVE-2026-7273**）。
> **期限今日 09-21**：Linux Kernel **CVE-2025-39682**／**CVE-2025-39964**／**CVE-2026-53266**（在野）。**新起逾期（due=09-20）**：**无**。**明日 due 09-22**：Microsoft **CVE-2026-81963**／**CVE-2026-85880**。仍近期限：**Chromium V8 CVE-2026-87491**（due 09-23）／**Zyxel CVE-2026-7273**（due 09-24）。仍逾期重点：**Chromium CVE-2026-85046**／**Pixel CVE-2026-58704**／**Cisco ISE CVE-2026-76460**／**Acronis CVE-2026-87886** 等（另见备援仍逾期清单）。
> X：`/workspace/x-posts-2026-09-21.json`（合并 **38** 条唯一：A6／B8／C10／LWiS14；跨源 ID 重叠 **0**；相对 prior seen_ids 重叠 **5**／**+33** 新 id；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **3h**（宽查询仅约 14min，已用 CVE-2026-7273 精炼）。Search B 可见约 **72h**（Sep 21 约 4–9h；另保留 Sep 20 工具帖作信号延续，其中 5 条已见 prior seen_ids）。Search C 约 **4h**。LWiS List 约 **21h**（**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；地下泄露声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【主条 · NEW KEV · Zyxel CVE-2026-7273 · 在野】** CISA 于 **2026-09-21** 将 **CVE-2026-7273**（GS1900 系列交换机 CGI 栈溢出）加入 KEV；due **2026-09-24**。CISA／CVE.org ADP 称 **active exploitation**；GreyNoise 关联 Kapibala 活动（约自 2026-08-17）。防御：按厂商表安装 **2.90(*.2)C0** 固件；隔离管理面；优先互联网／管理可达交换机；遵循 **BOD 26-04**。
  CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/21/cisa-adds-one-known-exploited-vulnerability-catalog
  厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273
  X 原帖（CISA）：https://x.com/CISACyber/status/2102122524972568782

- **【期限今日 · Linux×3 · 在野】** **CVE-2025-39682**／**CVE-2025-39964**／**CVE-2026-53266** 联邦 due **今日 09-21**；KEV 在野。防御：发行版／内核更新；盘点高暴露宿主／容器；BOD 26-04 triage。
  NVD 39682：https://nvd.nist.gov/vuln/detail/CVE-2025-39682
  NVD 39964：https://nvd.nist.gov/vuln/detail/CVE-2025-39964
  NVD 53266：https://nvd.nist.gov/vuln/detail/CVE-2026-53266

- **【仍逾期／链 · Chromium 85046＋87491 · UTA0565】** **CVE-2026-85046**（due 曾 09-18，仍逾期）与 **CVE-2026-87491**（due **09-23**）均在野。Volexity Part 2（2026-09-21）：**UTA0565** 经仿冒媒体站串联 Chrome／Windows 0-day（另含 **CVE-2026-85880**）。防御：Chrome ≥**152.0.7977.82+**（85046）／≥**153.0.8010.36+**（87491）；狩猎托管浏览器旧构建与 Volexity IoC。
  Volexity：https://www.volexity.com/blog/2026/09/21/mind-the-patch-gap-part-2-fake-websites-used-to-deploy-chrome-windows-0-day-exploits/
  X 原帖：https://x.com/Volexity/status/2102142700149510544
  X 原帖：https://x.com/HoustonIntrove1/status/2102174781848113532

- **【仍逾期 · ISE／Pixel／Acronis】** **CVE-2026-76460**（Cisco ISE，在野）／**CVE-2026-58704**（Pixel，有限定向）／**CVE-2026-87886**（Acronis，有限定向）due 曾为 **09-19**，仍逾期。
  Cisco：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
  Acronis：https://security-advisory.acronis.com/advisories/SEC-10986

- **【明日 due 09-22 · Microsoft×2】** **CVE-2026-81963**（Windows Update Stack 链接跟随 → 本地 SYSTEM）／**CVE-2026-85880**（Windows 堆溢出；亦出现在 UTA0565 链叙述中）。防御：按 MSRC 安装安全更新；盘点未打补丁 Windows。
  MSRC 81963：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963
  NVD 85880：https://nvd.nist.gov/vuln/detail/CVE-2026-85880

- **【X · 非 KEV】Windows Cross Device CVE-2026-66804** Project Zero／NEXSIGHT：悬挂 COM／ProgramData DLL 本地提权；**exploitation=none**；非 KEV。防御：安装 2026-08 Windows 安全更新（22H2／24H2／25H2／26H1 各见 enrich）。
  MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-66804
  Project Zero：https://projectzero.google/2026/09/windows-dangling-com.html
  X 原帖：https://x.com/NEXSIGHTNEWS/status/2102174726529433889

- **【工具 · RBNEWS613＋PureRAT 等】** Sliver／nuclei／nuclei-templates **无升版**；Risky **RBNEWS612→RBNEWS613**；tl;dr 仍 **#346**。X：PureRAT 逆向（含 C2 指标）、Claude-BugHunter、BotC2／CnaEmulator／OneDrive-UDC2／DeepTeam／nuclei PR#17240（部分为 Sep 20 信号延续）。
  RBNEWS613：https://risky.biz/RBNEWS613/
  PureRAT 仓：https://github.com/kaandemir993/PureRAT-msbuild.exe--C2-Extraction--Net-Evasion-Analysis

- **【威胁 · 未验证＋厂商报告】** 地下声称：Hogan Lovells／Cadwalader、印尼公民记录、Qilin→Telrad、巴西 Receita Federal 7e7、沙特 313 Team、ANUBIS→Summa Gold、NightSpire 学校——**均 UNCONFIRMED**。厂商／公开：Anthropic 9 月威胁情报报告；PhantomRaven npm 声称（未独立核实）；伪造 LastPass Authenticator；CrowdSec 源码供应链；Rust 定向社工。
  Anthropic：https://www.anthropic.com/threat-intelligence-report-september-2026
  LastPass 仿冒：https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html

## CVE / POC / 漏洞

### 1. 【NEW KEV · 在野】Zyxel GS1900 CVE-2026-7273

CISA 于 **2026-09-21** 将本 CVE 加入 KEV（catalogVersion **2026.09.21**，全库 **1717／+1**）；联邦 due **2026-09-24**。LAN 侧未认证 CGI 栈溢出 → 潜在 OS 命令执行。CISA 警报与 CVE.org ADP SSVC 均标 **active**；GreyNoise 文章记载 GS1900／Kapibala 活动。厂商公告本身未自称在野。防御：按型号安装 **2.90(*.2)C0**（GS1900-8／8HP／10HP／16／24／24E／24EP／24HPv2／48／48HPv2 等见表）；隔离管理平面；优先暴露交换机；BOD 26-04＋取证分流。**本报不转载利用细节。** X：@CISACyber／@SOCMinute／@notCVE／@HoustonIntrove1。

地址：
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/21/cisa-adds-one-known-exploited-vulnerability-catalog
- KEV 条目：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-7273
- 厂商：https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-7273
- CVE.org：https://www.cve.org/CVERecord?id=CVE-2026-7273
- GreyNoise 文章：https://www.greynoise.io/blog/open-season-on-kapibala-attacker-steals-government-records-wordpress-exploitation
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- X 原帖：https://x.com/CISACyber/status/2102122524972568782
- X 原帖：https://x.com/SOCMinute/status/2102173897248415937
- X 原帖：https://x.com/notCVE/status/2102131799207956717
- X 原帖：https://x.com/HoustonIntrove1/status/2102127827302732184

IoC（GreyNoise Kapibala 战役级，非 Zyxel 专属；原样抄录）：
- `0e81d80b40eaacbf6cb1e817fb1824c30a824af5cb4faca4aa9b03fd506d480f`（sha256）
- `0f6e757e82c4d91df5bd249f775b9970b59dee42cc0dfe40f879d77fc16821c6`（sha256）
- `2ff2945b13a4cd0e9a65c85af29ea1539e162a516466c0de682dbf9f8a4000b1`（sha256）
- `*.981666.xyz`（domain_pattern）
- `74.48.66.73`（ip）
- `104.225.153.141`（ip）
- `172.245.247.21`（ip）
- `kapibala`／`kapibala2`（account）

### 2. 【期限今日 · 在野】Linux Kernel CVE-2025-39682／CVE-2025-39964／CVE-2026-53266

KEV due **2026-09-21**（added 2026-09-18）。分别为 TLS recvmsg 异常检查、AF_ALG 并发写竞态、ebtables SNAT 越界写。CVE.org ADP 标 active。防御：应用含 KEV 所列 git.kernel.org stable 提交的发行版内核；EoL 宿主迁移；BOD 26-04。

地址：
- NVD 39682：https://nvd.nist.gov/vuln/detail/CVE-2025-39682
- NVD 39964：https://nvd.nist.gov/vuln/detail/CVE-2025-39964
- NVD 53266：https://nvd.nist.gov/vuln/detail/CVE-2026-53266
- KEV 39682：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-39682
- KEV 39964：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-39964
- KEV 53266：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-53266
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- 示例稳定提交（39682）：https://git.kernel.org/stable/c/2902c3ebcca52ca845c03182000e8d71d3a5196f

IoC：未见公开 IoC。

### 3. 【仍逾期／链 · 在野】Chromium V8 CVE-2026-85046＋CVE-2026-87491（UTA0565）

**CVE-2026-85046**：due 曾 **2026-09-18**，仍逾期；Google 称在野；修复示例 **152.0.7977.82／.83**。**CVE-2026-87491**：due **2026-09-23**；在野；修复 **153.0.8010.36／.37**。Volexity 2026-09-21 Part 2：UTA0565 用仿冒站点部署 Chrome／Windows 0-day 链（另述 **CVE-2026-85880**）。防御：强制浏览器升版；狩猎托管 Chrome 旧构建；对照 Volexity 域名／样本狩猎 drive-by。**本报不转载利用步骤。**

地址：
- Volexity Part 2：https://www.volexity.com/blog/2026/09/21/mind-the-patch-gap-part-2-fake-websites-used-to-deploy-chrome-windows-0-day-exploits/
- Chrome 85046 Stable：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- Chrome 87491 Stable：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- NVD 85046：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
- NVD 87491：https://nvd.nist.gov/vuln/detail/CVE-2026-87491
- KEV 85046：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-85046
- KEV 87491：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-87491
- X 原帖：https://x.com/Volexity/status/2102142700149510544
- X 原帖：https://x.com/HoustonIntrove1/status/2102174781848113532

IoC（Volexity UTA0565／CLEANGULP，原样抄录）：
- `chinadigitaltimes.top`（domain）
- `americanprgoress.top`（domain）
- `96.9.125.52`（ip）
- `thecovnresation.com`（domain）
- `thecovnresation.net`（domain）
- `personclouds.com`／`outsourcingwise.net`／`halal-navi.net`／`halaltak.net`／`borneobulletins.top`（domain）
- `8858ea412dc306b3558885af18006c5ca24689e8875733b5e13b3c2692e603cb`（sha256，chrome_cleanup.exe／CLEANGULP）
- `177652713dad3c128bd9195abf2b7603`（md5）
- `668aa5551315ab26b67118fbb29f8e4560a1e1af`（sha1）
- `%LOCALAPPDATA%\Microsoft\IME\MicrosoftIME.exe`（path）
- `MicrosoftIME`（scheduled_task）

### 4. 【仍逾期 · 在野】Cisco ISE CVE-2026-76460／Pixel CVE-2026-58704／Acronis CVE-2026-87886

三者 due 曾为 **2026-09-19**，仍逾期，均在野（Cisco PSIRT active；Pixel／Acronis 有限定向）。防御：ISE 升至 **3.1P12／3.2P11／3.3P12／3.4P7／3.5P4**（临时 iACL）；Pixel 补丁级别 ≥**2026-09-05**；Acronis cPanel ≥**1.9.3.1021**／Plesk ≥**1.8.11.638**／DirectAdmin ≥**1.2.3.238**。

地址：
- Cisco：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- NVD 76460：https://nvd.nist.gov/vuln/detail/CVE-2026-76460
- Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- NVD 58704：https://nvd.nist.gov/vuln/detail/CVE-2026-58704
- Acronis：https://security-advisory.acronis.com/advisories/SEC-10986
- NVD 87886：https://nvd.nist.gov/vuln/detail/CVE-2026-87886

IoC：未见公开 IoC。

### 5. 【明日 due 09-22】Microsoft CVE-2026-81963／CVE-2026-85880

KEV due **2026-09-22**。81963：Windows Update Stack 链接跟随 → 本地提权至 SYSTEM。85880：Windows 堆溢出；亦出现在 Volexity UTA0565 链叙述。防御：按 MSRC 安装更新；盘点未补丁主机。

地址：
- MSRC 81963：https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-81963
- NVD 81963：https://nvd.nist.gov/vuln/detail/CVE-2026-81963
- NVD 85880：https://nvd.nist.gov/vuln/detail/CVE-2026-85880
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC。

### 6. 【X · 非 KEV】Microsoft Windows Cross Device CVE-2026-66804

Project Zero（2026-09-21）与 NEXSIGHT／二次文章讨论悬挂 COM／ProgramData DLL 本地提权。**非 KEV**；NVD／CVE.org ADP **exploitation=none**。修复构建示例：Win10 22H2 ≥**10.0.19045.7663**；Win11 24H2 ≥**10.0.26100.9168**；25H2 ≥**10.0.26200.9168**；26H1 ≥**10.0.28000.2704**。防御：安装 2026-08 安全更新；监控非预期 `C:\ProgramData\CrossDevice\` DLL 加载。

地址：
- MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-66804
- Project Zero：https://projectzero.google/2026/09/windows-dangling-com.html
- 文章：https://davidcarliez.github.io/blog/cve-2026-66804-crossdevice-frameserver-lpe/
- NEXSIGHT：https://cyber.nexsight.co/articles/2026/09/22/projectzero-dangling-com-cve-2026-66804-privilege-escalation-2026-09-22/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-66804
- X 原帖：https://x.com/NEXSIGHTNEWS/status/2102174726529433889

IoC：未见公开 IoC。

### 7. 【延续 · expected】Check Point CVE-2026-85102／CVE-2026-85103

昨日主条延续：NCSC-NL 高紧迫／预期利用；**今晚仍非 KEV**；未见确认在野。Jumbo：**R81.20 Take166+／R82 Take126+／R82.10 Take44+／R81.10 Take190+**。今晚 Search A 未再保留相关帖。

地址：
- SK85102：https://support.checkpoint.com/results/sk/sk1000117
- SK85103：https://support.checkpoint.com/results/sk/sk1000118
- NCSC：https://advisories.ncsc.nl/2026/ncsc-2026-0365.html
- CERT-EU：https://cert.europa.eu/publications/security-advisories/2026-012/

IoC：未见公开 IoC。

### 8. 【LWiS · 研究】CVE-2025-13032（Avast 沙箱 · Part 2）／Safari／Muse 0-day 警示

@SAFATeamApS：CVE-2025-13032 Part 2（称已修复；仅保留补丁／研究摘要）。@moo9000：iPhone Safari 野外 RCE／DarkSword 转引（**未独立核实 CVE 编号与厂商公告**）。@patrickwardle：勿装 Muse，称 AI 助手可被本地劫持的严重 0-day（研究仓 not-a-mused）。**均不转载利用步骤。**

地址：
- SAFA 文章：https://www.safateam.com/intelligence-hub/research/technical-articles/cve-2025-13032-entering-and-breaking-the-avast-antivirus-sandbox-part-2
- X 原帖：https://x.com/SAFATeamApS/status/2101957314819342813
- X 原帖（Safari／DarkSword）：https://x.com/moo9000/status/2101987863193645178
- not-a-mused：https://github.com/pwardle/not-a-mused
- X 原帖：https://x.com/patrickwardle/status/2102045926474785265

IoC：未见公开 IoC（DarkSword 仅为名称提及）。

## 工具与 GitHub 发布

### 1. 核心工具版本 pulse（无升版；Risky 升期）

Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 相对昨日均无变化。Risky Business：**RBNEWS612→RBNEWS613**（NEW；标题 *Gemini finally did some crimes*）；**SRB183** 不变（SRB184=404）。tl;dr sec 仍 **#346**（#347 未确认）。

地址：
- Sliver：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- nuclei：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- RBNEWS613：https://risky.biz/RBNEWS613/
- SRB183：https://risky.biz/SRB183/
- tl;dr #346：https://tldrsec.com/p/tldr-sec-346

IoC：未见公开 IoC。

### 2. 【X · 新】PureRAT 逆向分析（含 C2 指标）

@Dinosn：kaandemir993／PureRAT-msbuild.exe--C2-Extraction--Net-Evasion-Analysis — msbuild 执行、C2 提取、.NET 规避的防御逆向报告。防御：对照仓库 README 行为特征做 EDR／DNS／出站狩猎；勿部署样本于生产。

地址：
- 仓库：https://github.com/kaandemir993/PureRAT-msbuild.exe--C2-Extraction--Net-Evasion-Analysis
- X 原帖：https://x.com/Dinosn/status/2102053980163436723

IoC（原样抄录自采集）：
- `pure8s.ddnsfree.com`
- `52.241.248.38`

### 3. 【X · 新】Claude-BugHunter 技能包

@EsGeeks：elementalsouls/Claude-BugHunter — 宣称面向漏洞狩猎／外部红队的 Claude 技能包。防御：仅授权评测环境；限制对生产资产的自动化扫描权限。

地址：
- 仓库：https://github.com/elementalsouls/Claude-BugHunter
- X 原帖：https://x.com/EsGeeks/status/2102040304291287219

IoC：未见公开 IoC。

### 4. 【X · 信号延续 · 已见 prior】BotC2／CnaEmulator／OneDrive-UDC2／DeepTeam／nuclei PR#17240

Search B 保留 Sep 20 工具帖（覆盖约 72h；**5 条 ID 已在 prior seen_ids**）：BotC2 RAT 研究报告、CnaEmulator、OneDrive-UDC2、DeepTeam 合辑、nuclei-templates PR#17240（CVE-2026-31807 matcher 误报修复）。另有 Red-Team-Roadmap 教育帖（Sep 21）。

地址：
- BotC2 PDF：https://github.com/ShadowOpCode/BotC2-RAT/blob/main/BotC2_RAT.pdf
- X：https://x.com/ShadowOpCode/status/2101786509653254376
- CnaEmulator：https://github.com/iterat0r/CnaEmulator
- X：https://x.com/Dinosn/status/2101725772461359372
- OneDrive-UDC2：https://github.com/nmht3t/OneDrive-UDC2
- X：https://x.com/Dinosn/status/2101598125785833743
- DeepTeam：https://github.com/confident-ai/deepteam
- X：https://x.com/shushant_l/status/2101628457180692968
- nuclei PR#17240：https://github.com/projectdiscovery/nuclei-templates/pull/17240
- X：https://x.com/shaivarth/status/2101604871736795360
- Red-Team-Roadmap：https://github.com/Dev-Chukwuma/Red-Team-Roadmap
- X：https://x.com/httpschuks/status/2102105619515969974

IoC：未见公开 IoC。

### 5. 【LWiS】vPhone Workstation／Recurse／Maester AD／Jev

@tom_doerr（@thegrugq 转）：zqxwce/vphone-ws — macOS 上虚拟 iPhone／iOS 研究 VM。@5mukx（@thegrugq 转）：Recurse-Labs/recurse — 基于 radare2 的 agentic 逆向环境。@techspence：Maester／AD 安全测试文。@_xpn_：Jev／Mythic 命令 opsec 评分概念（工具观察）。

地址：
- vPhone：https://github.com/zqxwce/vphone-ws
- X：https://x.com/tom_doerr/status/2101942193178980746
- Recurse：https://github.com/Recurse-Labs/recurse
- X：https://x.com/5mukx/status/2101856211826340014
- AD 文：https://entra.news/p/active-directory-security-testing
- X：https://x.com/techspence/status/2102054019669655719
- X：https://x.com/_xpn_/status/2102150280854868159

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. 【厂商确认】Volexity UTA0565 — 仿冒站部署 Chrome／Windows 0-day

见 CVE 节第 3 条。属厂商报告交叉，非地下声称。

地址：
- 报告：https://www.volexity.com/blog/2026/09/21/mind-the-patch-gap-part-2-fake-websites-used-to-deploy-chrome-windows-0-day-exploits/
- X：https://x.com/Volexity/status/2102142700149510544

IoC：见 CVE 节第 3 条抄录。

### 2. 【厂商报告】Anthropic 2026-09 威胁情报报告

@soycronus：评论 Anthropic 官方威胁情报报告（强调被盗 AI API 密钥可转售／滥用算力／掩护流量）。防御：轮换／审计 API 密钥；监控异常 token 用量与来源。

地址：
- Anthropic：https://www.anthropic.com/threat-intelligence-report-september-2026
- X：https://x.com/soycronus/status/2102107997333774367

IoC：未见公开 IoC。

### 3. 【LWiS】伪造 LastPass Authenticator 安装包（BYOVD／窃密）

@TheHackersNews（@PyroTek3 转）：伪造 LastPass Authenticator 下载包，滥用 Microsoft 签名内核驱动关闭 AV／EDR，并窃取浏览器密码、加密钱包与即时通讯会话。防御：限制驱动加载策略；校验官方下载通道；狩猎异常内核驱动与会话窃取行为。

地址：
- 文章：https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html
- X：https://x.com/TheHackersNews/status/2102088891629248884

IoC：未见公开 IoC（详见原文）。

### 4. 【LWiS】CrowdSec 源码供应链／Rust 定向社工／BYD Shark 6

@Dinosn：CrowdSec 确认源码在供应链攻击中被窃；Rust 团队／热门 crate 维护者遭视频通话定向；Rust 求职面试恶意载荷警告；BYD Shark 6 联网汽车攻击面案例。防御：供应链审计、面试／视频通话安全流程、车载暴露面盘点。

地址：
- CrowdSec：https://www.securityweek.com/crowdsec-confirms-source-code-stolen-in-supply-chain-attack/
- X：https://x.com/Dinosn/status/2102012143126155308
- Rust 定向：https://www.securityweek.com/rust-team-members-and-popular-crate-owners-targeted-via-video-calls/
- X：https://x.com/Dinosn/status/2102012115355668671
- Rust 面试警告：https://www.theregister.com/security/2026/09/21/rustaceans-warned-of-job-interviews-with-a-malicious-payload/5297690
- X：https://x.com/Dinosn/status/2102024274303242562
- BYD：https://securityaffairs.com/199460/hacking/a-byd-shark-6-hack-shows-the-risks-of-connected-cars.html
- X：https://x.com/Dinosn/status/2102012270452539615

IoC：未见公开 IoC。

### 5. 【X · 未验证】PhantomRaven（恶意 npm／CI）

@intels_daily：称自定义 LLM 生成信息窃取木马 **PhantomRaven** 经恶意 npm 包针对开发环境与 GitHub Actions。**无独立厂商链接；UNCONFIRMED。**

地址：
- X：https://x.com/intels_daily/status/2102142611561607609

IoC：未见公开 IoC。

### 6. 【X · 未验证】地下勒索／泄露声称（合辑）

以下均为社交／泄露站列表报道，**一律 UNCONFIRMED／未验证**：
- @ThreatAtlas：Leakeddata 声称 Hogan Lovells Cadwalader（美国律所）— https://x.com/ThreatAtlas/status/2102176776847859979
- @intels_daily：XH4XCYB3R 声称印尼内政部公民记录 — https://x.com/intels_daily/status/2102172814929183124
- @DailyDarkWeb：Qilin 声称 Telrad Networks（ransomware.live）— https://x.com/DailyDarkWeb/status/2102166866253021244 ；列表 https://www.ransomware.live/id/VGVscmFkIE5ldHdvcmtzQHFpbGlu
- @Splint3r7：巴西 Receita Federal 约 7000 万公司注册记录声称 — https://x.com/Splint3r7/status/2102144097796653496 ；https://darkwiser.com/scan
- @VECERTRadar：313 Team 针对沙特关键数字服务声称（帖文自标 claims）— https://x.com/VECERTRadar/status/2102109848330526780
- @FalconFeedsio：ANUBIS → Summa Gold（秘鲁，声称 544GB）— https://x.com/FalconFeedsio/status/2102105417518354621 ；https://summagold.com/
- @FalconFeedsio：NightSpire 未具名学校受害者 — https://x.com/FalconFeedsio/status/2102105073652469900

IoC：未见可核验公开 IoC。

### 7. ICS

本日公开备援 **无 2026-09-21 新 ICS advisory 显著条目**。联网汽车（BYD）见上，属公开报道交叉。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **NEW KEV CVE-2026-7273／Kapibala**：见 CVE 节第 1 条（sha256×3、domain_pattern、IP×3、账户名）。
- **UTA0565／CLEANGULP（Chromium 85046／87491 链）**：见 CVE 节第 3 条（域名、IP、哈希、路径、计划任务）。
- **PureRAT**：`pure8s.ddnsfree.com`／`52.241.248.38`。
- **Linux 今日 due×3／仍逾期 ISE／Pixel／Acronis／明日 MS×2／Check Point 85102／85103／CVE-2026-66804**：未见可抄录公开 IoC。
- **地下声称（Hogan／印尼／Telrad／巴西／沙特／Summa／NightSpire／PhantomRaven）**：未见可核验公开 IoC；一律未验证。
- **工具仓与其余条目**：未见公开 IoC（或仅仓库 URL）。

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

- X Latest A（CVE／POC／exploit／0day）：https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- X Latest A 精炼（CVE-2026-7273）：https://x.com/search?q=CVE-2026-7273&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／cobalt）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20cobalt)&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
