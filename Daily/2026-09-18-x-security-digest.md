# X 安全情报晚报 · 2026-09-18

> 搜集窗口：圣地亚哥时间 **2026-09-17 20:00 至 2026-09-18 ~20:30**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周五）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-18.json`（collected_at **2026-09-18T20:19:21-03:00**）＋ `/workspace/tools-news-pulse-2026-09-18.json`＋ `/workspace/enrich-extra-2026-09-18.json`＋ `/workspace/enrich-2026-09-18/`。CISA KEV catalogVersion **2026.09.18**／**1716** 条／dateReleased **2026-09-18T19:00:05.0974Z**（相对昨日 **+3**，版本号跳过 09.17）。
> **期限今日 09-18**：**Chromium V8 CVE-2026-85046**（在野利用）。**新起逾期（due 曾为 09-17）**：**Cisco ESA CVE-2026-76461**。**期限明日 09-19**：**Pixel CVE-2026-58704**／**Cisco ISE CVE-2026-76460**／**Acronis CVE-2026-87886**。**今日 NEW（due 09-21）**：Linux Kernel **CVE-2025-39964**／**CVE-2026-53266**／**CVE-2025-39682**。仍逾期：LiteLLM **59822**／Starlette **48710**／ScreenConnect **84869**／GitLab **85706**／PaperCut **81578／82078**／MikroTik **67277／86060**／Citrix **19490**／Fortinet **25249**／Cisco FMC **20079**／Magento **75650**／N-able **86218**。
> X：`/workspace/x-posts-2026-09-18.json`（合并 **45** 条唯一：A4／B13／C19／LWiS9；**0** 跨源重叠；其中约 **7** 条已见于 prior seen_ids，仍记高信号但标「先前已见」；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.18h**。Search B 约 **21h**（含 Sep 17 date-only）。Search C 约 **1.0h**。LWiS List 保留／扫描约 **20h**（另有 Sep 16 date-only；**交叉校验，不假装为本窗口 24h Latest**）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · 今日 due · Chromium V8 85046 · 在野】** 联邦 due **今日 09-18**：**CVE-2026-85046**（V8 类型混淆 → 沙箱内 RCE）。Google 称 **exploitation in the wild**。稳定通道修复：**152.0.7977.82/.83**（Win／Mac）／**152.0.7977.82**（Linux）。防御：全舰队尽快验证 Chrome／Edge／基于 Chromium 的浏览器版本并强制重启。
  厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85046

- **【KEV NEW · Linux Kernel ×3 · due 09-21】** catalog **+3**：
  - **CVE-2025-39964** AF_ALG socket 竞态／并发写交错；
  - **CVE-2026-53266** ebtables SNAT 越界写（非线性 skb／splice 页）；
  - **CVE-2025-39682** TLS 接收路径零长度记录绕过 recvmsg 类型处理。
  防御：按发行版内核更新；遵循 **BOD 26-04**；对暴露面做 triage。
  CISA +2：https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-two-known-exploited-vulnerabilities-catalog
  CISA +1：https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-one-known-exploited-vulnerability-catalog
  BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

- **【明日 due · Pixel／Cisco ISE／Acronis】** **CVE-2026-58704**／**CVE-2026-76460**／**CVE-2026-87886** 仍开放，due **09-19**。ISE：未认证特权 API 误用（CVSS 叙事 10）；补丁方向 **3.1P12／3.2P11／3.3P12／3.4P7／3.5P4**；X 交叉强调狩猎 `ise-kong/access.log`。
  Pixel：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
  Cisco ISE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  Acronis：https://security-advisory.acronis.com/advisories/SEC-10986
  X 原帖（ISE）：https://x.com/HoustonIntrove1/status/2101087054612353402

- **【新起逾期 · Cisco ESA 76461】** due 曾为 **09-17**，今日起标逾期。未认证 SQLi → 底层 OS **root**。修复示例：**15.5.5-014／16.0.4-302／16.5.0-780**。X：补丁后仍需妥协评估（防火墙出站／邮件流／凭证轮换）。
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX
  文章：https://www.theregister.com/security/2026/09/15/cisco-email-security-boxes-can-be-rooted-by-an-email/5296604
  原帖：https://x.com/gdlinux/status/2101086627988689319

- **【X · Plugin4Shell／AI coding 插件供应链】** Air Security：**Plugin4Shell**（Claude Code／Codex／Copilot／Gemini CLI 插件完整性）。防御：Claude Code **≥2.1.179**／Codex **≥0.146.0**；Copilot 先停自动更新并审计插件。
  主披露：https://www.air.security/blog-posts/plugin4shell
  原帖：https://x.com/shehackspurple/status/2101086299511828640

- **【X／LWiS · libheif CVE-2026-32882→Discourse／OpenAI 论坛】** 上游已修未及时标安全的 **libheif** 仍留 Discourse；上传 HEIF → RCE。防御：升 Discourse 对应 2026.x 补丁分支、更新 libheif、沙箱化图片处理。
  研究员：https://www.hacktron.ai/blog/hacking-openai
  GHSA：https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335
  原帖：https://x.com/BillDemirkapi/status/2101059606307037466

- **【LWiS · TeamPCP 供应链／Mandiant 卧底】** Google／Mandiant 渗入 **TeamPCP**（CanisterWorm）；FBI／Unit 42 有公开 IoC。防御：轮换 CI／云凭据、固定依赖哈希、监控异常发布。
  FBI：https://www.ic3.gov/CSA/2026/260702.pdf
  Unit 42：https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/
  原帖：https://x.com/DarkWebInformer/status/2101007019230552325

- **【威胁 · 勒索／泄露／OT】** UCSal **Wallstreet**；**Ellis County（Kansas）** 勒索；**Panzer→K3G Solutions（BR）**；**Gyazo 厂商确认**约 **2362 万**用户记录＋**4.9 亿**图片元数据；多起地下库售声称；Medium：EarthTime→MSBuild 三团伙勒索剖析。
  Gyazo：https://corp.helpfeel.com/en/news/news-20260916
  Ellis：https://ellisco.net/564/Ransomware
  UCSal：https://www.hendryadrian.com/ucsal-students-report-hacker-attack-and-suspended-classes-in-salvador/
  Medium：https://medium.com/@VampireXRay/from-earthtime-to-msbuild-anatomy-of-a-three-gang-ransomware-intrusion-914ead353313

- **【工具 · 核心无升版 · X 交叉】** Sliver **v1.7.7**／nuclei **v3.11.1**／nuclei-templates **v10.4.9** 均无升版。Risky 仍 **RBNEWS612**／**SRB183**；tl;dr 仍 **#346**。X／LWiS：CiliumHound、askWAM、Mr.SIP、adnullenum、chatgpt-app-analysis、Red-Team-Roadmap；先前已见 ARES／Mythic Telegram／flightsim。
  CiliumHound：https://specterops.io/blog/2026/09/17/ciliumhound-graphing-kubernetes-network-policies/
  nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9

## CVE / POC / 漏洞

### 1. 【今日 due · 在野】Google Chromium V8 CVE-2026-85046

CISA due **2026-09-18**（added 2026-09-04）。V8 类型混淆 → 沙箱内 RCE（特制 HTML）；影响 Chrome／Edge／Opera 等。Google 公告称 **exploitation is in the wild**。修复：**152.0.7977.82/.83**（Windows／Mac）、**152.0.7977.82**（Linux）。X 另见地下市场声称 Chromium／Android WebView 0-day 链（**未验证**，仅作威胁情报信号，勿当确认利用）。

地址：
- 厂商：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85046
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- X 声称帖：https://x.com/intels_daily/status/2101085644646727730

IoC：未见公开 IoC。

### 2. 【KEV NEW】Linux Kernel CVE-2025-39964／CVE-2026-53266／CVE-2025-39682

CISA **2026-09-18** 入目三则；联邦 due **2026-09-21**。均为 Linux Kernel：
- **CVE-2025-39964**：AF_ALG socket 竞态，并发写导致内部状态不一致。
- **CVE-2026-53266**：ebtables SNAT 目标越界写，可写入 nonlinear skb 的 splice 导入页；说明含 EoL／EoS 提示。
- **CVE-2025-39682**：TLS 接收路径对零长度记录检查不当，可能绕过 recvmsg 记录类型处理。
防御：按发行版尽快内核更新；遵循 BOD 26-04 与 Forensics Triage；评估互联网暴露面。**本报不转载利用细节。**

地址：
- CISA +2：https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA +1：https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-one-known-exploited-vulnerability-catalog
- NVD 39964：https://nvd.nist.gov/vuln/detail/CVE-2025-39964
- NVD 53266：https://nvd.nist.gov/vuln/detail/CVE-2026-53266
- NVD 39682：https://nvd.nist.gov/vuln/detail/CVE-2025-39682
- 内核补丁示例（39964）：https://git.kernel.org/stable/c/0f28c4adbc4a97437874c9b669fd7958a8c6d6ce
- 内核补丁示例（53266）：https://git.kernel.org/stable/c/bf84ad7c7a9ede46e31afaa41a1ba06a159e8c87
- 内核补丁示例（39682）：https://git.kernel.org/stable/c/2902c3ebcca52ca845c03182000e8d71d3a5196f
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

IoC：未见公开 IoC。

### 3. 【明日 due】Pixel CVE-2026-58704／Cisco ISE CVE-2026-76460／Acronis CVE-2026-87886

三条仍 due **2026-09-19**（added 2026-09-16）。续报：
- **CVE-2026-58704** Google Pixel 蜂窝基带不当授权／权限绕过 → 提权。
- **CVE-2026-76460** Cisco ISE／ISE-PIC 特权 API 误用 → 未认证可绕过 Web 管理；修方向含 ISE **3.1P12／3.2P11／3.3P12／3.4P7／3.5P4**；X 建议狩猎 `ise-kong/access.log`。
- **CVE-2026-87886** Acronis Backup cPanel／WHM／Plesk 扩展默认权限不当 → 本地提权；厂商称有限在野。

地址：
- Pixel 厂商：https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- Cisco ISE：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
- Acronis：https://security-advisory.acronis.com/advisories/SEC-10986
- NVD Pixel：https://nvd.nist.gov/vuln/detail/CVE-2026-58704
- NVD ISE：https://nvd.nist.gov/vuln/detail/CVE-2026-76460
- NVD Acronis：https://nvd.nist.gov/vuln/detail/CVE-2026-87886
- X 原帖（ISE）：https://x.com/HoustonIntrove1/status/2101087054612353402

IoC：未见公开 IoC。

### 4. 【新起逾期】Cisco Secure Email Gateway CVE-2026-76461

联邦 due 曾为 **2026-09-17**，今日起标逾期。未认证 SQL 注入（经特制邮件）可在底层 OS 以 **root** 执行任意命令。防御：升级至固定版本（示例 **15.5.5-014／16.0.4-302／16.5.0-780**）、限制网关暴露；X／The Register 语境强调补丁≠事件结束——需审查历史出站／邮件流变更、保留取证镜像、轮换管理与加密材料。

地址：
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76461
- 文章：https://www.theregister.com/security/2026/09/15/cisco-email-security-boxes-can-be-rooted-by-an-email/5296604
- X 原帖：https://x.com/gdlinux/status/2101086627988689319

IoC：未见公开 IoC。

### 5. 【X】Plugin4Shell（AI coding agent 插件供应链）

Air Security 主披露 **Plugin4Shell**：四类编码代理插件完整性校验问题，可能导致已信任插件被替换；受影响叙事含 Claude Code／OpenAI Codex／GitHub Copilot／Gemini CLI。防御：Claude Code **≥2.1.179**、Codex **≥0.146.0**；Copilot 披露时无修复则停用插件自动更新并审计第三方插件；Gemini CLI 已弃用且不修复则迁移并收紧主机权限。X @shehackspurple 补充供应链治理建议。**本报不转载 PoC／利用步骤。**

地址：
- 主披露：https://www.air.security/blog-posts/plugin4shell
- 报道：https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335
- X 原帖：https://x.com/shehackspurple/status/2101086299511828640
- 讨论视频：https://www.youtube.com/watch?v=YAm8LhQRNFk

IoC：未见公开攻击 IP／域名／哈希（风险指标为代理版本与插件信任链）。

### 6. 【LWiS／X】libheif（CVE-2026-32882）→ Discourse／OpenAI 论坛 RCE 叙事

研究员披露：上游已修但未及时标安全的 **libheif** 缺陷仍存在于 Discourse；上传 HEIF 可致 RCE（OpenAI 社区论坛语境）。Discourse advisory 归因 **CVE-2026-32882**。防御：自托管升级对应 **2026.7.0／2026.6.1／2026.5.2／2026.1.6** 分支补丁并重建 Docker app、更新 libheif、启用图片处理沙箱、限制不必要 HEIF／AVIF 解码。

地址：
- 研究员文：https://www.hacktron.ai/blog/hacking-openai
- Discourse GHSA：https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335
- 报道：https://www.securityweek.com/ai-built-exploit-and-sign-in-flaw-opened-path-to-internal-openai-code/
- 仓库：https://github.com/strukturag/libheif
- X 原帖：https://x.com/BillDemirkapi/status/2101059606307037466

IoC：未见公开攻击 IoC。

### 7. 【续报 · 仍逾期重点】LiteLLM／Starlette／ScreenConnect／GitLab／PaperCut 等

昨日已详述条目今日无 KEV 元数据变更，仅续报仍逾期：LiteLLM **CVE-2026-59822**、Starlette **CVE-2026-48710**、ScreenConnect **CVE-2026-84869**、GitLab **CVE-2026-85706**、PaperCut **CVE-2026-81578／82078**，以及 MikroTik／Citrix／Fortinet／Cisco FMC／Magento／N-able 等（见公开备援表）。防御：对照各厂商 advisory 完成补丁验证。

地址：
- LiteLLM GHSA：https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q
- Starlette GHSA：https://github.com/Kludex/starlette/security/advisories/GHSA-86qp-5c8j-p5mr
- KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 1. 核心工具版本脉冲（公开备援）

相对昨日：**无升版**。Sliver **v1.7.7**、nuclei **v3.11.1**、nuclei-templates **v10.4.9**。Risky Business 仍 **RBNEWS612**／播客 **SRB183**；tl;dr sec 仍 **#346**（#347／RBNEWS613／SRB184 探测 404）。

地址：
- Sliver：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- nuclei：https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1
- nuclei-templates：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.9
- Risky RBNEWS612：https://risky.biz/RBNEWS612/
- Risky SRB183：https://risky.biz/SRB183/
- tl;dr #346：https://tldrsec.com/p/tldr-sec-346

IoC：未见公开 IoC。

### 2. 【LWiS NEW】SpecterOps CiliumHound（BloodHound OpenGraph）

@SpecterOps 介绍 **CiliumHound**：把 Cilium 网络策略（YAML／JSON）导入 BloodHound OpenGraph，按 K8s namespace 可搜索。防御／蓝队：用图分析审查过度放行策略。

地址：
- 文章：https://specterops.io/blog/2026/09/17/ciliumhound-graphing-kubernetes-network-policies/
- X 原帖：https://x.com/SpecterOps/status/2100655780470964559

IoC：未见公开 IoC。

### 3. 【X Search B NEW】askWAM／Mr.SIP／adnullenum／chatgpt-app-analysis／Red-Team-Roadmap

防御向仅记存在与用途：
- **askWAM**（dirkjanm）：Entra ID／WAM 相关工具；帖子谈登录日志／会话可见性检测语境。
- **Mr.SIP**：授权场景 SIP／VoIP 审计框架。
- **adnullenum**：经 SAMR／LSARPC 的 AD 枚举工具（存在性）。
- **chatgpt-app-analysis**：ChatGPT 桌面应用红队研究仓库。
- **Red-Team-Roadmap**：系列学习模块帖（多条）。

地址：
- askWAM：https://github.com/dirkjanm/askWAM · 原帖 https://x.com/_xDeJesus/status/2100952567178031374
- Mr.SIP：https://github.com/meliht/Mr.SIP · 原帖 https://x.com/EsGeeks/status/2100790918232097025
- adnullenum：https://github.com/crypt0p3g/adnullenum · 原帖 https://x.com/cryptopeg/status/2100775763792539936
- chatgpt-app-analysis：https://github.com/reddpy/chatgpt-app-analysis · 原帖 https://x.com/sh_karan_sh/status/2100766894974267606
- Red-Team-Roadmap：https://github.com/Dev-Chukwuma/Red-Team-Roadmap · 示例原帖 https://x.com/httpschuks/status/2101052443207598499

IoC：未见公开 IoC。

### 4. 【先前已见】ARES／Mythic Telegram profile／flightsim

Search B 中 Sep 17 卡片继续出现，已在 prior seen_ids：ARES、Mythic Telegram profile、flightsim 及部分 Roadmap 帖。

地址：
- ARES：https://github.com/Mafifrizi/ARES · https://x.com/FieryBagels/status/2100689353919877312
- Mythic Telegram：https://github.com/DavidCarliez/mythic_telegram_profile · https://x.com/ipurple/status/2100671558729499058
- flightsim：https://github.com/alphasoc/flightsim · https://x.com/alphasoc/status/2100601138760360207

IoC：未见公开 IoC。

### 5. 【LWiS】LocalKDC／LocalKDCPotato（研究信号）

@decoder_it 称在 W11 Insider 跑通 LocalKDC；@_EthicalChaos_ 跟帖提及 LocalKDCPotato。防御向仅记研究／工具信号，**不展开利用**。

地址：
- 原帖：https://x.com/decoder_it/status/2100963440105861463
- 跟帖：https://x.com/_EthicalChaos_/status/2101053250074030322

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. 【LWiS】TeamPCP 供应链攻击／Mandiant 卧底叙事

公开报道：Google／Mandiant 分析员被动进入 **TeamPCP** 的 CanisterWorm 频道，协助凭据撤销、受害者通知与执法线索；供应链投毒影响开发者工具／CI／CD（云令牌、SSH、K8s secrets 等）。防御：立即轮换暴露窗内 CI／注册表／云凭据；短期最小权限令牌；固定并验证依赖与 Actions 哈希；监控异常发布与 CI 出站；抗钓鱼 MFA。

地址：
- FBI FLASH：https://www.ic3.gov/CSA/2026/260702.pdf
- Unit 42：https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/
- 公开报道：https://www.cyberkendra.com/2026/09/how-google-broke-teampcp-from-the-inside.html
- X 原帖：https://x.com/DarkWebInformer/status/2101007019230552325

IoC（FBI PDF 原样摘录，防御狩猎用；完整清单以 PDF 为准）：
- IP：`83.142.209.11` · `45.148.10.212` · `83.142.209.194` · `83.142.209.203` · `94.154.172.43` · `67.217.57.240`
- 域名（defanged 已还原写法，狩猎时注意仿冒品牌域）：`scan.aquasecurtiy.org` · `checkmarx.zone` · `models.litellm.cloud` · `check.git-service.com` · `t.m-kosche.com` · `git-tanstack.com` · `recv.hackmoltrepeat.com` 等（见 FBI PDF）
- 家族／标签：`tpcp-docs` · `docs-tpcp` · `CanisterWorm` · `SANDCLOCK` · `Mini Shai-Hulud` · `Miasma`
- SHA-256：见 FBI PDF（26 枚）与 `/workspace/enrich-extra-2026-09-18.json`

### 2. 【X】Wallstreet 勒索 → UCSal（萨尔瓦多／巴西语境报道）

报道称 UCSal 遭 **Wallstreet** 勒索，软件工程实验室受影响、威胁 SQL 泄露、部分课程推迟。

地址：
- 文章：https://www.hendryadrian.com/ucsal-students-report-hacker-attack-and-suspended-classes-in-salvador/
- X 原帖：https://x.com/TweetThreatNews/status/2101087720609059296

IoC：未见公开 IoC。

### 3. 【X】Panzer 勒索声称 → K3G Solutions（巴西）

@ThreatAtlas／@FalconFeedsio：**Panzer** 声称受害者为巴西电信／IT 咨询 **K3G Solutions**；叙事称约 20–21 日内公布数据。

地址：
- 原帖：https://x.com/ThreatAtlas/status/2101076141670838684
- 原帖：https://x.com/FalconFeedsio/status/2101075838900805730
- 厂商站点（受害声称关联）：https://k3gsolutions.com.br/

IoC：未见公开 IoC。

### 4. 【X】Kansas Ellis County 县政府勒索

**Ellis County** 称已隔离受影响系统并调查；地方报道部分服务受影响。防御：离线／不可变备份、验证恢复、监控冒用县域邮箱钓鱼；暂不推断已外泄。

地址：
- 官方页：https://ellisco.net/564/Ransomware
- 地方报道：https://www.kwch.com/2026/09/18/ellis-county-investigating-ransomware-incident-affecting-it-systems/
- KSN：https://www.ksn.com/news/state-regional/ransomware-attack-on-kansas-county-will-affect-some-services/
- X 原帖：https://x.com/KSNNews/status/2101080994178826695

IoC：未见公开 IoC。

### 5. 【X】Gyazo 泄露（厂商确认）

Helpfeel／Gyazo 官方：约 **2026-09-11** 图片上传服务器遭未授权访问；约 **2362 万**用户记录与约 **4.9 亿**图片元数据受影响。防御：用户立即更换 Gyazo／复用密码、审查会话与整合、警惕钓鱼；运营方继续失效认证材料并完成通知。

地址：
- 厂商通告：https://corp.helpfeel.com/en/news/news-20260916
- 厂商更新：https://corp.helpfeel.com/en/news/news-20260918
- X 原帖：https://x.com/IntCyberDigest/status/2101084087150629297

IoC：官方通告未见攻击 IP／域名／样本哈希。

### 6. 【X】地下库售／访问售（声称汇总）

Search C 短窗口内多条 **声称**（未独立核验）：Iran Bank Sepah ~4400 万行；BitMax.io ~36.1 万；CUC Loisirs；Paraguay SENAVE／TSJE；Ecuador 医疗 ~668 万；法国 FFTIR／SIA／枪械零售；乌克兰工业 OT／热处理炉控制访问售；以及 Auditteam／Securotrop／Gammax 勒索受害者观测帖。防御：按行业监测暗网声称、验证真实影响、通知相关方。

地址：
- Sepah 声称：https://x.com/DailyDarkWeb/status/2101089655936401761
- BitMax 声称：https://x.com/intels_daily/status/2101072664622428533
- Ecuador 医疗声称：https://x.com/intels_daily/status/2101071731779854713
- 乌克兰 OT 声称：https://x.com/intels_daily/status/2101070541235048740
- 勒索受害者观测示例：https://x.com/sec_news_com/status/2101084403409826157

IoC：未见公开 IoC（帖内未给出可抄录哈希／C2 IP 列表）。

### 7. 【X】BYOVD／LOLDrivers 与 ESXi／三团伙勒索分析

- @Kostastsale：讨论威胁者携带脆弱驱动禁用 EDR（BYOVD）；指向 LOLDrivers 资源。
- @ro0TCr4k：勒索运营在拿下 vCenter 后加密整片 ESXi 的趋势叙事。
- @VampireXray：Medium 文《From EarthTime to MSBuild…》三团伙勒索入侵剖析（防御阅读；不转载步骤）。

地址：
- LOLDrivers：https://www.loldrivers.io/
- BYOVD 原帖：https://x.com/Kostastsale/status/2101073730411876739
- ESXi 叙事原帖：https://x.com/ro0TCr4k/status/2101069931643363520
- Medium：https://medium.com/@VampireXRay/from-earthtime-to-msbuild-anatomy-of-a-three-gang-ransomware-intrusion-914ead353313
- Medium 原帖：https://x.com/VampireXray/status/2101067302762365397

IoC：未见公开 IoC（以原文附录为准）。

### 8. 【LWiS】LNK 滥用技术讨论／俄罗斯选举系统承包商入侵叙事

- @ShitSecure：转发 @Wietze 在 MCTTP_Con 的新 LNK 滥用技术讨论（仅存在性；无步骤）。
- @lukOlejnik：称黑客入侵承建俄罗斯新选举系统的公司，外泄大量代码／文档／开发者聊天及约 **1.113 亿**选民个人数据叙事。

地址：
- LNK 原帖：https://x.com/ShitSecure/status/2100558262600946100
- 选举系统叙事原帖：https://x.com/lukOlejnik/status/2100841730136326197

IoC：未见公开 IoC。

### 9. 【先前已见／续】TrustedSec Kerberoasting 硬化文

LWiS 再现 @PyroTek3／TrustedSec 蜜罐账户检测口令喷洒／Kerberoasting 硬化文（先前已见）。

地址：
- 文章：https://trustedsec.com/blog/detecting-password-spraying-with-a-honeypot-account
- 原帖：https://x.com/PyroTek3/status/2100318707314815236

IoC：未见公开 IoC。

### 10. ICS

本日窗口 **无 2026-09-18 新 ICS advisory**。昨报 ICSA-26-260-01..07＋ICSA-26-211-07 Update A（pub 09-17 早于本窗口）不重复展开。

地址：
- ICS 列表：https://www.cisa.gov/news-events/ics-advisories

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **今日 KEV／厂商主条（85046／Linux×3／ISE／ESA／Pixel／Acronis）**：未见可抄录公开 IoC IP／样本哈希列表。
- **TeamPCP（FBI FLASH）**：IP `83.142.209.11` · `45.148.10.212` · `83.142.209.194` · `83.142.209.203` · `94.154.172.43` · `67.217.57.240`；域名见 FBI PDF／enrich-extra；标签 `CanisterWorm`／`SANDCLOCK`／`Mini Shai-Hulud`／`Miasma`／`tpcp-docs`；SHA-256 共 26 枚见 https://www.ic3.gov/CSA/2026/260702.pdf
- **Plugin4Shell／libheif／Gyazo／勒索与库售声称**：未见可抄录新攻击 IP／样本哈希（Gyazo 为厂商确认事件但无公开攻击 IoC）→ **未见公开 IoC**（或以原文附录为准）。
- **LOLDrivers**：资源站 https://www.loldrivers.io/ （驱动目录，非单次事件 IoC）。
- **昨日续报 IoC**（Settra／MikroTik／FMC Talos 等）本日无新交叉确认，不重复抄录。
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

- X Latest A（CVE／POC／exploit／0day／vulnerability）：https://x.com/search?q=(CVE%20OR%20POC%20OR%20exploit%20OR%200day%20OR%20%220-day%22%20OR%20vulnerability)%20-filter%3Areplies&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei／sliver／havoc／cobalt／implant）：https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20redteam%20OR%20nuclei%20OR%20sliver%20OR%20havoc%20OR%20cobalt%20OR%20%22command%20and%20control%22%20OR%20implant)%20-filter%3Areplies&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor／ransomware／threat intel）：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20OR%20ransomware%20OR%20%22threat%20intel%22)%20-filter%3Areplies&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
