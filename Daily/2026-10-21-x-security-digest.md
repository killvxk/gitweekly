# X 安全情报晚报 · 2026-10-21

> 搜集窗口：圣地亚哥时间 **2026-10-20 20:00 至 2026-10-21 20:15**（America/Santiago／UTC-3，名义约 24.25 小时，接昨晚窗口）。X 搜索参数：`start_time=2026-10-20T23:10:00Z`，`end_time=2026-10-21T23:14:00Z`。实际抓到的帖子时间从 **10-20 20:16** 到 **10-21 20:12**（UTC-3），**实际有效覆盖约 24 小时**：**窗口起端约 16 分钟（20:00–20:16）无帖**；其后各时段均有关键词/LWiS/核心媒体批次覆盖，无大块空白。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`，Latest／recency／relevancy 排序）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** 本轮接口多数批次**没有回传 entities**，t.co 一律用 curl 跟随 HTTP 跳转展开（649 个短链中成功展开到非 t.co 目标 **632** 个；纯图片／视频 t.co 不列）。A 类（CVE／0day）原始＋去噪＋在野＋多时段切片；B 类（GitHub 红队／C2）两次；C 类（威胁报告／IoC）四次；LWiS List 500 成员分 10 段 `from:` 批次，并对活跃段做翻页；核心媒体／厂商账号多时段、IoC 猎人账号两页；专题（PHP／GitLab／LiteLLM／Node／Oracle／APT／供应链）共若干次。共 **38 次有效 X 读取，0 次 429**。
> **覆盖说明**：每次查询最多 25 条。宽泛 A/C 查询会被当日 PHP／GitLab 热帖占满，靠切片与专题补全。LWiS 部分批次当日发帖很少（如批次 0／1 各仅 1 条）。剔除广告营销号、空转发、政治隐喻「backdoor」及 `Python_s_` 类自动刷屏后粗筛。
> 窗口内去重后 **727** 条帖子（与 seen_ids 5345 条**零重叠**），关键词粗筛得约 **531** 条安全相关新帖（按最先命中批次归类约 **A204／B35／C92／LWiS64／核心＋IoC猎人75／专题61**）。下文实际引用约 100+ 条。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON（`/workspace/enrich-2026-10-21/kev.json`）；CISA 警报「Critical Vulnerabilities in PHP Require Immediate Patching」；php.net 安全公告与版本发布；watchTowr／Wiz／Datadog／Talos／Unit 42／Rapid7／Censys／Cloudflare／Huntress／SecurityWeek／BleepingComputer／THN；Microsoft Threat Intelligence（Storm-0940／ARTEX）；Citrix CTX697191（NetScaler 107406）；Oracle Security Alert CVE-2026-91403；Node.js 10-21 安全版；Kaspersky Securelist（Lazarus FlashHole）；Tor Project／tor-relays 邮件列表分析；TeamUpdraft／Patchstack（UpdraftCentral）；GMO／BleepingComputer（Onamae Desktop Cloud）。GitHub API 核对 nuclei／nuclei-templates／Sliver／emp3r0r／BloodHound／NetExec／Mythic／impacket／Havoc：**BloodHound 今日发 v9.9.0-rc2／rc3**；其余监控框架无新正式 release（process-watcher v0.2.2 为 10-20 已列）。
> **CISA KEV：catalogVersion 2026.10.21／1754 条，Δ+0**（相对昨天 2026.10.20／1754；`dateReleased` 2026-10-21 11:04 UTC-3，**仅版本号滚动与个别 notes 清理，无新增 CVE**）。昨日入列的六条（Plex2Shell×4、SiteGuard 106931、Siemens 110936）仍在。**due_today（10-21）：0 条。** **newly_overdue（续）**：BeyondTrust **CVE-2026-102764**、Fortinet **CVE-2025-61624**（10-19 到期）；Atlassian **CVE-2026-21589**（10-18）；AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322（10-17）；Ivanti 104935、Windows 96951（10-16）；Apple 86950（10-13）。**upcoming：10-23** SiteGuard 106931、Plex 96656、Plex 96654；**11-03** Plex 96652、Plex 96655、Siemens 110936。**仍未进 KEV、今日高优先**：PHP 109618／109619（补丁已发、多方报利用尝试／扫描，CISA 警报称发布时未见在野成功利用）、GitLab 110264（CVSS 10，未见在野）、Node.js 111497、Oracle Java 91403、LiteLLM 供应链、FortiSIEM 106173、NetScaler 107406（厂商称未见未缓解利用）、Nextcloud Collabora 110447（单源称在野）。
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接作狩猎用途。泄露、入侵类声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【补丁日 · 全网级】PHP2Shell（CVE-2026-109618／109619）紧急安全版已于今日约 14:00 UTC 发布**：修复版 **8.5.12／8.4.27／8.3.36／8.2.35**；另有 7.4／8.0／8.1 最小源码回移。官方确认 mod_php 上未认证 RCE（部分路径在应用代码运行前触发）；配置缓解**不能**完全挡住。CISA 发警报要求立即打补丁，并写明**发布时未见在野利用**；Cloudflare／watchTowr／Hadrian／Patchstack／Vega／SecurityWeek 等报告**利用尝试／扫描已现**（含公开 PoC 流量，Vega 点名 `64.95.12[.]7`）。Censys：约 **629 万主机／1.15 亿 Web 属性**跑 PHP（暴露≠脆弱）。Chainguard 提前 6h+ 发含补丁镜像被 PHP 基金会批评破坏协调披露。**唯一完整修复是升级并重启所有 worker**。
- **【供应链 · AI 工具链】LiteLLM 1.107.0 第二次 PyPI／Docker 挂马（2026 年内第二次）**：窃取的 GitHub CLI OAuth 令牌触发 releaser；wheel 注入 `cook.pth`→`cook`（privcollect 凭据窃取）＋每小时拉 GitHub dead-drop 执行的后门；外带到 `litellm[.]dev/healthcheck`；dead-drop `github[.]com/letters9813`。Pin **1.106.2**（按 digest），轮换密钥。
- **【未认证 RCE · DevOps】GitLab CVE-2026-110264（CVSS 10.0）**：Onigmo 正则编译器整数溢出，未认证 RCE，影响自管实例可追溯至 **7.0（2014）**；修复 **19.5.1／19.4.3／19.3.6** 及回移 **19.2.9／19.1.9／19.0.10／18.11.13**。GitLab.com 已修；**未见在野、未进 KEV**。注意：10-12 的 97229 补丁不覆盖本洞。
- **【运行时】Node.js 10-21 安全版**：含 Brotli 解码器越界写 **CVE-2026-111497（HIGH，可达 RCE）** 及 TLS／DNS 等高危项；升 **22.23.4／24.22.1／26.12.1**（并含 eMudhra 中间 CA 处置）。
- **【带外警报】Oracle Java／GraalVM CVE-2026-91403（CVSS 9.1）**：JSSE，未认证远程可利用；影响 Java SE 8u511…27.0.1 等。Oracle 打破季度 CPU 节奏发 Security Alert——通常意味着高紧迫性。
- **【APT · AI】Microsoft：中国关联 Storm-0940 用 ARTEX 多智能体渗透框架加速 ConnectWise Cloud Backup 供应链下游攻击**：可达 **2250+ 租户**、峰值约 **2900 次登录/分钟**；部分环境 <3 小时拿到特权云访问。IoC：`144.172.64[.]99／128／60` 等。
- **【基础设施】Tor 出口节点劫持拦截 SSH 密码登录**：10-1～10-5 约 **333+** 出口把 SSH 重定向到 12 台拦截服务器，峰值占出口容量 **7.46%**；与 Ebury OpenSSH 后门相关；Tor 已 BadExit。密码经 Tor 登录者按已泄露处理。
- **【APT】Lazarus Operation FlashHole**：用 **ML-KEM-1024** 后量子密钥封装保护载荷下发；打韩国软件／建筑／通信设备制造；LPEClient／TechHub／Cubridge 链。
- **【CMS】UpdraftCentral 连接密钥被滥用种后门插件**（TeamUpdraft 站点遭入侵后）；Patchstack 见 99 种后门插件名；另 Rank Math PRO 111862 供应链续报。
- **【日本】GMO Onamae Desktop Cloud 遭入侵，最多约 26739 台客户服务器被装恶意程序**；服务已关停排查。
- **【工具】** BloodHound **v9.9.0-rc2／rc3** 今日发布；OpenAI `php2shell-checker`、Neo23x0 process-watcher、多家 nuclei／检测签名仓库涌现（仅链接，不转载 PoC）。

## CVE / POC / 漏洞

### 1. PHP 核心 · PHP2Shell CVE-2026-109618／109619（未认证 RCE）· 补丁已发／利用尝试在野
PHP 安全团队今日发布安全版：**8.5.12／8.4.27／8.3.36／8.2.35**，并提供 7.4／8.0／8.1 最小源码回移。两洞官方 **CVSS v4.0 各 9.2**：109618＝OOM／longjmp 后请求内存半初始化被清理路径误用；109619＝worker 全局残留指向已释放请求内存（UAF／陈旧状态）。影响所有对外提供 Web 请求的 PHP（mod_php／FPM／cgi／FrankenPHP／LiteSpeed）；**mod_php 风险最高，可在应用代码前触发**。OpenAI／Wiz／Calif 等在禁运下发现；细节 10-20 泄露后披露提前一天。Cloudflare 提前约 9h 部署 WAF；Chainguard 提前发布含补丁镜像被基金会批评。CISA 警报要求立即升级，**发布时未见在野成功利用**；多家厂商传感器见**扫描／PoC 级尝试**。临时 `session.upload_progress.enabled=0`／`memory_limit=-1` 等**不能完全防护**。升级后必须**重启全部 worker**。
- X 原帖：
  - https://x.com/BleepinComputer/status/2112908598321758361
  - https://x.com/TheHackersNews/status/2112915567179174102
  - https://x.com/CISACyber/status/2112947079458717969
  - https://x.com/Unit42_Intel/status/2112907015295021149
  - https://x.com/rapid7/status/2112930810110021685
  - https://x.com/censysio/status/2112934042345595000
  - https://x.com/Vega_Threat/status/2112922163967840256
  - https://x.com/Frichette_n/status/2113026956266799239
  - https://x.com/KimZetter/status/2112950944199491793
- 厂商公告：
  - https://www.php.net/archive/2026.php#2026-10-21-5
  - https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w
  - https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp
  - https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching
  - https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq
- 文章／检测：
  - https://www.bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws/
  - https://www.securityweek.com/php2shell-patches-land-as-first-exploitation-attempts-hit-sensors/
  - https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/
  - https://blog.talosintelligence.com/two-critical-rces-in-php-core/
  - https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
  - https://www.rapid7.com/blog/post/etr-cve-2026-109618-and-cve-2026-109619-critical-unauthenticated-remote-code-execution-in-php/
  - https://censys.com/advisory/cve-2026-109618-cve-2026-109619/
  - https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
- GitHub／检测（狩猎用，不转载步骤）：
  - https://github.com/openai/php2shell-checker
  - https://github.com/Neo23x0/process-watcher
  - https://github.com/slabwren/php2shell-detection
  - https://github.com/Ademking/php2shell-nuclei-templates
- 地址／IoC：利用尝试源（单源 Vega）`64.95.12[.]7`；狩猎：PHP worker 拉起 `sh`／`bash`、超长表单字段名、`Unknown on line 0` 内存耗尽错误。未见官方完整 C2 列表。

### 2. GitLab · CVE-2026-110264（未认证 RCE，CVSS 10.0）· 未见在野
自管 GitLab CE／EE 的 Onigmo 正则编译器整数溢出，特制正则可达未认证 RCE；影响可追溯至 **7.0（2014）**。修复：19.5.1／19.4.3／19.3.6／19.2.9／19.1.9／19.0.10／18.11.13。GitLab.com 与 Dedicated 内部版已修。同日发布含 CVE-2026-15723（SAML+LDAP 自动链接下账号接管）等共 11 项。与 10-12 的 CVE-2026-97229 不同——若只打了 10-12 补丁仍需再升。厂商称未见在野；未进 KEV。
- X 原帖：
  - https://x.com/TheHackersNews/status/2112981939984671090
  - https://x.com/phantmradar/status/2113003575274062172
  - https://x.com/AikidoSecurity/status/2113005713387815033
  - https://x.com/Daily_CyberSec/status/2113036100096692305
- 文章：https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html
- 地址／IoC：未见公开 IoC（GitLab TLDR／Sigma：「Onigmo native worker crash」「Org mode render error burst」）。

### 3. Node.js · CVE-2026-111497 等（Brotli OOB 写→RCE 等）· 安全版已发
10-21 安全版修多个问题，头条 **CVE-2026-111497**：Brotli 解码器越界写，HIGH，可达 RCE；另有 TLS 主机名绕过（105483／106069）、DNS NUL 截断（105482）等。固定版：**22.23.4／24.22.1／26.12.1**。依赖更新含 eMudhra 中间 CA 处置。Express 等若默认接受 Brotli 请求体需同步关注。
- X 原帖：
  - https://x.com/iamnrdas/status/2113044040555929724
  - https://x.com/AndrewMohawk/status/2112980986099388677
  - https://x.com/coinspect/status/2113026411883901284
- 厂商公告：https://nodejs.org/en/blog/vulnerability/october-2026-security-releases
- 地址／IoC：未见公开 IoC。

### 4. Oracle Java SE／GraalVM · CVE-2026-91403（JSSE，CVSS 9.1）· 带外 Security Alert
Oracle 今日发 Security Alert（非常规 CPU）：JSSE 组件，**未认证、网络可达**，CVSS 9.1（C／I 高、A 无）。影响 Java SE 8u511、11.0.33、17.0.21、21.0.13、25.0.5、27.0.1 及对应 GraalVM。按 Oracle 惯例，打乱季度节奏通常意味着紧迫。
- X 原帖：
  - https://x.com/DanteMMartin/status/2113036626649850091
  - https://x.com/hmier/status/2113039894809375027
  - https://x.com/__kokumoto/status/2113035384871682207
- 厂商公告：https://www.oracle.com/security-alerts/alert-cve-2026-91403.html
- 地址／IoC：未见公开 IoC。

### 5. Citrix NetScaler · CVE-2026-107406（SAML 内存溢出→RCE／DoS，CVSS 9.5）· 续／扩散
SAML SP／IdP 配置下内存溢出；升 **14.1-73.46+／13.1-64.29+**（及 FIPS 对应）。**上周 SAML 补丁不覆盖本洞**。厂商称公告时未见未缓解利用；未进 KEV。另有 S2W 对相关 NetScaler 洞的分析扩散。
- X 原帖：https://x.com/emits_ca/status/2112986888021606472 ；https://x.com/S2W_Official/status/2112802524495573502
- 厂商公告：https://support.citrix.com/external/article/CTX697191/citrix-netscaler-adc-and-citrix-netscale.html
- 地址／IoC：未见本洞新公开网络 IoC（88771／88779 链 IoC 见昨日 Rapid7）。

### 6. 昨日 KEV 六条与逾期项 · 续报（Plex2Shell／SiteGuard／Siemens／BeyondTrust 等）
CISA 昨日入列的 Plex2Shell（96652／96654／96655／96656）、SiteGuard 106931、Siemens 110936 今日持续被媒体与狩猎帖复述；**10-23 为 SiteGuard／Plex96656／96654 联邦 due**。BeyondTrust 102764（Armory Castle／UNC5221）Mandiant 分析续传；FortiSIEM 106173 公开 PoC 续报（未进 KEV）。
- X 原帖：
  - https://x.com/TheHackersNews/status/2112808297564881184
  - https://x.com/BleepinComputer/status/2112975948089856189
  - https://x.com/CyberScoopNews/status/2113012703807557743
- 厂商／文章：
  - https://www.cisa.gov/news-events/alerts/2026/10/20/cisa-adds-six-known-exploited-vulnerabilities-catalog
  - https://thehackernews.com/2026/10/cisa-orders-federal-agencies-to-patch.html
  - https://www.bleepingcomputer.com/news/security/cisa-hackers-chain-plex-flaws-in-plex2shell-attacks-to-breach-servers/
- 地址／IoC：沿用昨日 Plex／Siemens／BeyondTrust／NetScaler 表；本轮无强制新官方 IoC。

### 7. 其它新披露／单源
- **MariaDB CVE-2026-92262 等 RCE 链**（含 PoC 讨论）：https://securityonline.info/mariadb-critical-vulnerabilities-rce/ ；X https://x.com/Daily_CyberSec/status/2112705592464703522
- **LiteLLM 逻辑洞 CVE-2026-35029／59823**（Check Point，与今日供应链事件不同）：X https://x.com/ptdbugs/status/2112945792583352549
- **Archon CVE-2026-111322**（无认证控制 API）：X https://x.com/alexlee20122022/status/2112850564266500469
- **aaPanel CVE-2026-113506**（命令注入，PoC）：https://www.thehackerwire.com/vulnerability/CVE-2026-113506/
- **Nextcloud Collabora CODE CVE-2026-110447**（单源称在野 RCE）：https://github.com/alan-turing-institute/cyber-threat-observatory/blob/main/reports/2026-10-14/TIER_1_CVE-2026-110447.md
- **Windows Defender「BlueHammer」CVE-2026-33825**（DFIR_Radar 摘要，升 Antimalware Platform 4.18.26030.3011）：X https://x.com/DFIR_Radar/status/2112967632462708825
- **Ollama CVE-2026-103663 PoC**（意大利用户 CSIRT）：https://www.acn.gov.it/portale/w/ollama-disponibile-poc-per-lo-sfruttamento-della-cve-2026-103663
- 地址／IoC：以上多数未见公开网络 IoC（PoC 仅作狩猎）。

## 工具与 GitHub 发布

> GitHub API 核对：nuclei v3.11.1、nuclei-templates v10.5.0、Sliver v1.7.8、emp3r0r v5.3.0、NetExec v1.5.1、Mythic v3.4.0.5、impacket 0.13.1 均无本窗口新正式版；**BloodHound v9.9.0-rc2（10-21 01:10Z）／rc3（10-21 23:17Z）**；Neo23x0 process-watcher v0.2.2（10-20）。以下多为 PHP2Shell 检测／研究仓库与红队技术文。

- **BloodHound v9.9.0-rc2／rc3**：https://github.com/SpecterOps/BloodHound/releases
- **OpenAI php2shell-checker**（仅查版本头，不发利用请求）：https://github.com/openai/php2shell-checker ；X https://x.com/CodexUpdate/status/2112947766649348532
- **process-watcher（Neo23x0）**：https://github.com/Neo23x0/process-watcher
- **php2shell-detection（Sigma／Suricata／WAF，防御向）**：https://github.com/slabwren/php2shell-detection ；X https://x.com/Slabwren/status/2112987051998241231
- **php2shell-nuclei-templates**：https://github.com/Ademking/php2shell-nuclei-templates
- **ConfluenceC2**（研究／红队概念，仅链接）：https://github.com/dagowda/ConfluenceC2/ ；X https://x.com/ipurple/status/2112811420081385845
- **PhantomBuffer（EDR 规避研究）**：https://github.com/TwoSevenOneT/PhantomBuffer ；文章 https://www.zerosalarium.com/2026/10/PhantomBuffer-Effective-EDR-Evasion-Stealth-Injection.html
- **Crowbar（本地 CVE／KEV／EPSS MCP）**：https://github.com/kushvinth/crowbar
- **ipurple：从 PEB Loader 列表隐藏 DLL**：https://trainsec.net/library/windows-internals/hiding-a-dll-from-the-peb-loader-list-and-why-process-explorer-still-sees-it/
- 多个 **php2shell PoC 仓库**在 X 流传（ikow／eness／godylockz／twili8／wakemeiflose／9bie 等）——**仅作狩猎索引，本报告不转载内容或步骤**。
- 地址／IoC：以上工具条目未见公开恶意 IoC。

## APT / Malware 分析

### 1. Storm-0940（中国关联）用 ARTEX 加速 ConnectWise 供应链下游攻击（Microsoft，今日）
Microsoft Threat Intelligence：Storm-0940（活跃自 2021，数据窃取向）最早自 2026-09 起用开源多智能体渗透框架 **ARTEX**（Go＋Next.js，可切中／韩／西／日）自动化侦察、密码喷洒与 OAuth 应用滥用。认定其应对 ConnectWise Cloud Backup 多租户应用供应链事件负责；下游可达 **2250+ 租户**、峰值约 **2900 次登录尝试/分钟**；多例从锁定目标到特权云访问 **<3 小时**。10-10～14 对 8 家组织 327 账号喷洒（`144.172.64[.]99`，15 万+ 失败登录）。后续用失陷应用身份经 Graph 做侦察、改应用凭据、提权。应用 ID：`506e08f9-…`（Cloud Backup）、`24205314-…`（Teams）、`0de14c77-…`（Graph）、`c921256f-…`（SkyKick Partner Portal）。
- X 原帖：
  - https://x.com/MsftSecIntel/status/2112975078266716390
  - https://x.com/DFIR_Radar/status/2112998042290843968
  - https://x.com/Threatlabz/status/2113006215567724767
- 文章：https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
- 地址／IoC（Microsoft）：IP `144.172.64[.]128`、`144.172.64[.]99`、`144.172.64[.]60`；VPN（仅 10-15／16 语境）`187.15.88[.]186`、`187.15.90[.]217`、`187.15.89[.]186`；UA `Python-urllib/3.12`、`python-requests/2.31.0`、`python-requests/2.34.2`、`curl/7.88.1`、`azure-toolkit/1.0`。

### 2. LiteLLM 1.107.0 PyPI／Docker 供应链（第二次，2026）
SafeDep／Socket／StepSecurity／Upwind／JFrog／THN：v1.107.0 七个平台 wheel＋被篡改的 pyproject；`cook.pth`→`import cook` 在解释器启动时跑 **privcollect**（云／浏览器／AI 工具／SSH／LiteLLM 代理配置），打包 GZIP TAR POST 至 `litellm[.]dev/healthcheck`；后台守护每小时读 `github[.]com/letters9813` 的 `domain.txt` 并 GET `/codepy` 执行。官方：三名工程师 GitHub CLI OAuth 被盗触发 releaser＋批准；令牌已吊销、组织成员收缩。sdist 无载荷但 toml 被改。Pin **1.106.2** digest，全量轮换。
- X 原帖：
  - https://x.com/TheHackersNews/status/2112967698103894257
  - https://x.com/JFrogSecurity/status/2112882176156909646
  - https://x.com/UpwindMDR/status/2112875118485516430
  - https://x.com/Dinosn/status/2112977939688288532
- 文章：
  - https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html
  - https://www.theregister.com/security/2026/10/21/litellm-supply-chain-attack-hoovers-up-passwords-and-secrets/5304548
  - https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-docker/
- 地址／IoC：外带 `litellm[.]dev/healthcheck`；dead-drop `github[.]com/letters9813`；文件 `cook.pth`／`cook.py`；仿冒仓库名 `Berri-AI/litellm`（报道）。

### 3. Tor 出口劫持 + Ebury：拦截经 Tor 的 SSH 密码登录
研究员 kaba：10-2 扫描约 3000 出口，**333** 个把 SSH 重定向到同一组 **12** 台拦截服务器；目录数据分析峰值出口容量 **7.46%**（约 377 中继／59 运营者改 exit policy）。接受变更 host key 后输入的密码被窃，并可跟进装 Ebury 类安装器。Tor 10-4 起 BadExit／MiddleOnly，10-5 共识中清除。Quetzalcoatl 家族运营者 Zimmer 证实管理机 Ebury 1.8.3。**密钥登录无法被中继到真实服务器**；密码登录高风险。
- X 原帖：
  - https://x.com/TheHackersNews/status/2112854217362706554
  - https://x.com/DFIR_Radar/status/2112877196448542778
  - https://x.com/Dinosn/status/2112874736023638085
- 文章：https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html
- 地址／IoC（Zimmer／THN 转引）：Ebury 落点 `libkeyutils.so.1.10.2`；抽象套接字 `@event-0YsOG9WSOE`；登录源 `185.225.226[.]62`；拦截 host key `ED25519 SHA256:6baCZCPsl+AfQuujUS81fMEE/C7UeJ+AwjrImqmDB3E`；植入内嵌密钥指纹见原文。

### 4. Lazarus · Operation FlashHole（后量子 ML-KEM-1024 护载荷）
Kaspersky：7 月起针对韩国，钓鱼→仿造 GitHub 页→滥用 INISAFE CrossWeb EX→TechHub／ClientHub／LPEClient→Cubridge。**LPEClient 从 C2 取 4×1568 字节 ML-KEM-1024 公钥**，派生共享密钥后经 GOST／Threefish 解载荷。另有 Chromium 凭据窃取模块。Securelist：https://securelist.com/lazarus-operation-flashhole/121541/
- X 原帖：
  - https://x.com/BleepinComputer/status/2113005418339344513
  - https://x.com/_skinnyguinea/status/2113028554451525661
  - https://x.com/Dinosn/status/2112745036135956693
- 文章：https://www.bleepingcomputer.com/news/security/lazarus-hackers-use-post-quantum-cryptography-for-malware-delivery/
- 地址／IoC：具体哈希／C2 见 Kaspersky 原文 IoC 节（页面动态加载，本轮未完整抄录表）；狩猎点：CrossWeb EX 高完整性子进程、私有 GitHub raw 拉取、ML-KEM 相关异常流量。

### 5. UpdraftCentral 密钥滥用 + Rank Math 供应链续
TeamUpdraft 站点 10-17/18 遭未授权访问，连接密钥等可能泄露；攻击者用有效 UpdraftCentral 密钥远程 `plugin.upload_plugin` 种后门。Patchstack：连续约 18 小时、**99** 种后门插件名；账号如 `data-ops43`／`system_team850` 等。升 UpdraftPlus **≥1.26.13／2.26.13**，删旧连接密钥，查陌生管理员／MU-插件。Rank Math PRO CVE-2026-111862 续报（3.0.123 窗口下载有后门，修 3.0.124，C2 `rank1cdn[.]com`）。
- X 原帖：
  - https://x.com/TheHackersNews/status/2112831962281099387
  - https://x.com/Dinosn/status/2112724870287020339
- 文章：https://thehackernews.com/2026/10/attackers-abuse-updraftcentral-keys-to.html
- 地址／IoC（Patchstack／Nethemba）：IP `43.250.53[.]42`、`2a09:bac5:4e21:2e3c::49b:9`；URL 参数 `?_9f5696=`；插件名含 Site Health Cache、Asset Forge 2、Content Helper、Wp Forge、Query Shelf、Style Bridge 8F5、Media Kit 183、Post Dock 776、Nav Hub、Speed Desk、Speed Kit 300、Link Latch、Script Shelf、Feed Case 等；账号 `system_team850`／`web.tech988`／`cmseditor170`／`cms.tech644`／`web_mgr684`（@example.com）；Rank Math：`rank1cdn[.]com`。

### 6. 其它威胁报告
- **Bronze Sandcastle（中国关联）** Sandboxie DLL 侧加载打亚非：https://thehackernews.com/2026/10/china-aligned-bronze-sandcastle-abuses.html ；X https://x.com/TheHackersNews/status/2112878135629017440
- **Vasilek 藏 VMware Tools**（白俄罗斯关联 Cyber Partisans，俄医疗网潜伏近两年）：X https://x.com/TheHackersNews/status/2112788043581329535
- **Amazon ClickFix→Doina RAT／Lumma／NetSupport**：X https://x.com/DFIR_Radar/status/2112922397930315959
- **UNC7017／AOMEI CROSSROAD／SHINYROAD** 续：X https://x.com/DFIR_Radar/status/2112937490185150920 ；https://www.securityweek.com/aomei-backupper-compromised-in-short-burst-supply-chain-campaign/
- **GlassWorm→OVHcloud CLI** 续（Dark Reading／SecurityWeek）：https://www.darkreading.com/cyberattacks-data-breaches/ovhcloud-github-compromise-glassworm-threat-actors
- **hugo-paper／mevn-cli 伪造 commit preinstall**（ForceMemo／GlassWorm）：https://safedep.io/hugo-paper-mevn-cli-forged-commit-preinstall-dropper
- **Graphalgo** 扩至 Terraform provider／Go module（Aikido，Slack＋以太坊 C2）：X https://x.com/TweetThreatNews/status/2113021606159081903
- **PhantomStealer4** 含勒索模块（默认关）：SHA-256 `13cee49212b02538acec3887804d62cd696f29cbe37e5231809f16f384619be9`
- **SEAL：假白帽向加密项目投「PoC」实为恶意**：X https://x.com/_SEAL_Org/status/2112901629875732919
- **HoneyMyte／Mustang Panda CoolClient + 内核 rootkit**（巴基斯坦）：X https://x.com/CyberAlertpit/status/2112872778378707268
- **Kimsuky LNK 多语钓鱼**（Nextron／360）：X https://x.com/nextronresearch/status/2113018268462301533
- **Unit 42：AI 辅助网络犯罪分析**：https://unit42.paloaltonetworks.com/ai-assisted-cybercrime-analysis/
- **APT28／HOOKEDGE／SafePay／eMudhra** 昨日主文今日仍在扩散，无实质新 IoC 批次。

### 7. 零散 IoC 投放（猎人账号，单源，UNCONFIRMED）
- ClickFix：`ktoktotam[.]cc`、`vahuebivaet[.]cc`、`82[.]25[.]63[.]33`（@skocherhan）：https://x.com/skocherhan/status/2112982341731910035
- 协作诱饵：`eurywastselk[.]com`、`172[.]86[.]126[.]251`；SHA-256 `92589172ef4b160bfe6a56ecf224d6be7c1c259923b9afc779a6ebf3f11400d8`（@smica83／@skocherhan）
- 电子发票诱饵哈希：`5a15f996dd4157ea7e88ed80d6a77dfcdd81f54305f4414fee99bd609d01f1b4`、`1b519c70fe1f04dfed8e09bbbd7deb376b9c7bc6ce828fc62eba326fe71a26f2`（源 `lhdn.tos-cn-hongkong.volces[.]com`）、`247b3244ccbb8e33ebba0d3aa66a38f66cfe7d27d91fb299927628249532d10e`
- 俄语诱饵：`725fa840a70c47196797db5977b2d99654063d01310e23d0887bfc4054e143cc`；`aesmartdata[.]cloud`
- 疑 NK C2：`h92jcihwicllow.wuaze[.]com`（@malwrhunterteam）
- 签名恶意 MSI（Azure blob）：`linkprofile.blob.core.windows.net/files/WindowsDefender.msi`、`…/DefenderUpdate.msi`；相关 SHA-256 `ebd865e5901bd5881f6a932d5f7a58e69ef54d25a58df50547e1b1fc8612789d`、`0329c3dcb71f6ed5eed1d17f1e945612aeba5d67cc80699d734a2df64bba1cdf`（CrocoRAT／Rust remote shell，@SquiblydooBlog）
- SliverC2 列表续：https://github.com/orlofv/Indicators/blob/main/SliverC2 ；例 `139.180.192[.]248`、`159.112.188[.]117`、`2.27.120[.]130`、`80.78.22[.]149`
- DeskPilot 面板：`5.75.168[.]252:8766`

### 8. 入侵／泄露声称（除厂商自述外 UNCONFIRMED）
- **Onamae Desktop Cloud（GMO，厂商自述）**：最多约 **26739** 台客户服务器被装恶意程序；10-21 04:00 JST 起关停；支付信息称在另一基础设施。https://www.bleepingcomputer.com/news/security/japans-onamae-desktop-cloud-hacked-up-to-27-000-servers-affected/ ；X https://x.com/BleepinComputer/status/2113023441162957297
- **BAE Systems 事件致美国联邦破产法院通知停发**（CyberScoop）：X https://x.com/CyberScoopNews/status/2113027801041244232
- **SBI**：银行确认 3897 条客户记录现于暗网（威胁人称更大集合，UNCONFIRMED）：https://thehackernews.com/2026/10/state-bank-of-india-confirms-data-leak.html
- Everest／n0n／INTERLOCK／Aur0ra／WHITEARMOR／The Gentlemen／GLOBAL SECRET GROUP 等多条受害者声称：**UNCONFIRMED**。
- 地址／IoC：未见（或仅厂商内部）。

## 地址／IoC 汇总

> 全部原样抄录自来源，已去武装（`[.]`）的保持原样；单源条目标 UNCONFIRMED。**只用于检测与封堵。**

| 关联 | 类型 | 指标 | 来源 |
|---|---|---|---|
| Storm-0940／ARTEX／ConnectWise | IP | `144.172.64[.]99`、`144.172.64[.]128`、`144.172.64[.]60` | Microsoft |
| Storm-0940 | IP（VPN，10-15/16） | `187.15.88[.]186`、`187.15.90[.]217`、`187.15.89[.]186` | Microsoft |
| Storm-0940 | User-Agent | `Python-urllib/3.12`、`python-requests/2.31.0`、`python-requests/2.34.2`、`curl/7.88.1`、`azure-toolkit/1.0` | Microsoft |
| Storm-0940 | App ID | `506e08f9-6e9a-4da4-942b-a099a03644ae`、`24205314-2b89-4e07-a2a4-579e898a5640`、`0de14c77-b9b0-4137-9360-34878a929827`、`c921256f-04a7-44e8-9b2a-69c33929ba19` | Microsoft |
| LiteLLM 供应链 | 外带／控制 | `litellm[.]dev/healthcheck`；`github[.]com/letters9813` | THN／StepSecurity |
| LiteLLM | 文件 | `cook.pth`、`cook.py` | 多方 |
| Tor／Ebury SSH 拦截 | IP／套接字／文件 | `185.225.226[.]62`；`@event-0YsOG9WSOE`；`libkeyutils.so.1.10.2` | Zimmer／THN |
| Tor 拦截 | Host key | `ED25519 SHA256:6baCZCPsl+AfQuujUS81fMEE/C7UeJ+AwjrImqmDB3E` | kaba／THN |
| UpdraftCentral 后门 | IP | `43.250.53[.]42`、`2a09:bac5:4e21:2e3c::49b:9` | Patchstack |
| UpdraftCentral | 账号／参数 | `data-ops43`、`system_team850`、`web.tech988`、`cmseditor170`、`cms.tech644`、`web_mgr684`；`?_9f5696=` | Nethemba／Patchstack |
| Rank Math | 域名 | `rank1cdn[.]com` | Wordfence／THN |
| PHP2Shell 扫描（UNCONFIRMED） | IP | `64.95.12[.]7` | @Vega_Threat |
| ClickFix（UNCONFIRMED） | 域名／IP | `ktoktotam[.]cc`、`vahuebivaet[.]cc`、`82[.]25[.]63[.]33` | @skocherhan |
| 诱饵样本 | SHA-256 | `92589172…1400d8`、`5a15f996…01f1b4`、`1b519c70…1a26f2`、`247b3244…32d10e`、`725fa840…e143cc`、`a355496c…db02be`、`13cee492…619be9`、`ebd865e5…12789d`、`0329c3dc…ba1cdf` | abuse.ch／猎人 |
| 签名 MSI | URL | `linkprofile.blob.core.windows.net/files/WindowsDefender.msi`、`…/DefenderUpdate.msi` | @malwrhunterteam |
| 疑 NK C2（UNCONFIRMED） | 域名 | `h92jcihwicllow.wuaze[.]com` | @malwrhunterteam |
| SliverC2（UNCONFIRMED） | IP | `139.180.192[.]248`、`159.112.188[.]117`、`2.27.120[.]130`、`80.78.22[.]149`（+5 见仓库） | @orlof_v |
| DeskPilot（UNCONFIRMED） | IP:port | `5.75.168[.]252:8766` | @malwrhunterteam |
| 协作域（UNCONFIRMED） | 域名／IP | `eurywastselk[.]com`、`172[.]86[.]126[.]251`；`aesmartdata[.]cloud` | 猎人 |

其余条目（GitLab 110264、Node 111497、Oracle 91403、NetScaler 107406、MariaDB、Onamae、BAE、多数工具仓库）：**未见公开 IoC**（或 IoC 仅在未完整抓取的原文附件中）。

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

**今日 LWiS 交叉要点**：List 成员本轮贡献较多的是 @Dinosn（PHP 实验／FlashHole／Tor／LiteLLM／KEV 转发）、@cyb3rops／@Frichette_n（PHP 补丁与 Datadog 分析）、@ipurple（ConfluenceC2、PEB DLL 隐藏）、@vxunderground／@pdiscoveryio／@runZeroInc（PHP 暴露面）、@_xpn_／@N3mes1s／@i0n1c（补丁绕过讨论）、@KimZetter（CISA PHP 警报）。blogs.txt 命中高信号：Unit 42、Wiz、Cloudflare、watchTowr labs、Microsoft／MSRC。Risky Business 首页可访问；tl;dr sec 最新仍是 **#350**（10-15），无新一期。

## 来源搜索 URL

- A（CVE／0day／PoC）：https://x.com/search?q=%28CVE-2026%20OR%20CVE-2025%29%20%28exploit%20OR%20exploited%20OR%20PoC%20OR%20RCE%20OR%20patch%20OR%20advisory%20OR%20KEV%20OR%200day%20OR%20zero-day%29%20-is%3Aretweet%20-from%3Avulnipulse&f=live
- A 在野：https://x.com/search?q=%28%22zero-day%22%20OR%200day%20OR%20%22in%20the%20wild%22%20OR%20%22actively%20exploited%22%29%20%28vulnerability%20OR%20exploit%20OR%20CVE%20OR%20patch%29%20-is%3Aretweet%20-is%3Areply&f=live
- B（GitHub 红队／C2）：https://x.com/search?q=url%3Agithub.com%20%28C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20PoC%20OR%20exploit%20OR%20BOF%20OR%20EDR%20OR%20implant%20OR%20loader%29%20-is%3Aretweet&f=live
- C（威胁报告）：https://x.com/search?q=%28%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%29%20-is%3Aretweet%20-is%3Areply&f=live
- C IoC：https://x.com/search?q=%28malware%20OR%20infostealer%20OR%20RAT%20OR%20backdoor%20OR%20ransomware%20OR%20loader%29%20%28IOC%20OR%20C2%20OR%20sha256%20OR%20%22threat%20report%22%29%20-is%3Aretweet%20-is%3Areply&f=live
- 专题（PHP2Shell／GitLab／LiteLLM／Node／Oracle）：https://x.com/search?q=%28CVE-2026-109618%20OR%20CVE-2026-109619%20OR%20CVE-2026-110264%20OR%20LiteLLM%20OR%20CVE-2026-111497%20OR%20CVE-2026-91403%20OR%20php2shell%29&f=live
- 专题（APT／供应链）：https://x.com/search?q=%28Storm-0940%20OR%20ARTEX%20OR%20FlashHole%20OR%20UpdraftCentral%20OR%20%22Tor%20exit%22%20OR%20ConnectWise%29%20-is%3Aretweet&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog


> **本机拷贝状态（America/Santiago）**：2026-10-21 约 20:30 尝试 CopyFromBox 至 Revision-PC（`fdf9b752-388f-4373-a714-53a93a7e43f6`）`Desktop/X安全情报晚报/2026-10-21-x-security-digest.md` **失败**——本机未连接（Grok Bot desktop app 需在线）。box 主文件已落盘，待本机上线后重试拷贝。
