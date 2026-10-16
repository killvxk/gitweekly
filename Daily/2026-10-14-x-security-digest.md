# X 安全情报晚报 · 2026-10-14

> 搜集窗口：圣地亚哥时间 **2026-10-13 20:13 至 2026-10-14 20:09**（America/Santiago／UTC-3，约 **23 小时 56 分**，接昨晚窗口，没有缺口）。ISO／X 搜索参数：`start_time=2026-10-13T23:13:00Z`，`end_time=2026-10-14T23:09:00Z`。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all` + `get_posts_by_ids`，带 entities／note_tweet；t.co 链接一律用 entities.expanded_url／unwound_url 展开，127 条短正文帖已按 ID 补取全文与实体）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** A／B／C 三类各跑 1 条原始查询和 1 条去噪查询：A 去掉 Patch Tuesday 转发刷屏，B 限 `url:github.com`，C 排除 ThreatAtlas／FalconFeeds 勒索受害者刷屏。LWiS 用 `from:` + recency，分三层：①优先批 48 个账号（List 核心成员加 BleepingComputer／THN／securityaffairs／malwrhunterteam／Nulltap_／cybermergemedia／Volexity／Unit42 等），按 4 个时段分段并翻页，覆盖整个窗口；②扩展厂商／媒体批 30 个账号（CISA／CrowdStrike／ESET／abuse.ch／Shadowserver／SecurityWeek／DailyDarkWeb／Python_s_／ThreatWire_／threatintel／sans_isc／Horizon3／TheRecord／kaspersky 等），3 段加翻页；③List 其余约 475 名成员分 9 批全量覆盖。本轮约 **38 次 X 读取**：search_posts_all 约 36 次（不足 25 条的页视为已取完，并抽查过 next_token 的空页），get_posts_by_ids 2 次。另有 **1 次参数错误**（`from:` 用户名超过 15 字符：sansinternetstorm／zerodayinitiative），已改用 `sans_isc` 并去掉重复账号，**未触发限速**。窗口内共拿到 **689** 条帖子，与 seen_ids 比对重复 0 条。按规则筛选（去掉广告、空转发、闲聊回复、刷屏）并人工抽检后，合并 **294** 条安全相关新帖：**A18／B5／C15／LWiS256**。归类规则：命中 LWiS `from:` 批次的算 LWiS，其余按 A／B／C 查询来源算。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON（`/workspace/enrich-2026-10-14/kev.json`）。厂商／研究页存于 `/workspace/enrich-2026-10-14/web/`，共 49 页加 Talos IOC txt：Cisco PSIRT、PAN PSIRT、Huntress／Horizon3／Ahsay、Collabora GHSA／THN Nextcloud、Unit 42（Casbaneiro／PEERSTITCH／第三方 VPN）、Talos UAT-6275 与 RF TAG-193、Microsoft 威胁情报博客与 DCU、Resecurity、Forescout、Huntress（WatchGuard／ChatGPT GPT）、EG Secure SiteGuard、Corelight、curl、Tencent Vghost 与 oss-security、Fox-IT、Netskope／securityaffairs XWorm、ThreatFabric Hirudo、Group-IB KGB RAT、ASEC、Rapid7 Zimbra、XBOW、SentinelOne BYOVD、ANY.RUN、CrowdStrike、Pen Test Partners、Amberwolf、VulnCheck、THN／BleepingComputer Ivanti、F5 NGINX、Malwarebytes、ProjectDiscovery、Docker、Risky／tl;dr 首页。GitHub API 查了 nuclei／nuclei-templates／Sliver／emp3r0r／BloodHound／NetExec／Mythic／impacket 的 releases 与 commits。
> **CISA KEV：catalogVersion 2026.10.14／1745 条，Δ+4**（对比昨日 2026.10.13／1741；dateReleased 2026-10-14T19:27Z＝**10-14 16:27 圣地亚哥**）。**今天新增 4 条**：CVE-2026-105133（Ahsay AhsayCBS 认证不当）、CVE-2026-105134（AhsayCBS 命令注入）、CVE-2026-76519（Cisco Secure Email Gateway 路径遍历）、CVE-2026-0322（PAN-OS 代码注入）。四条期限都只有 **3 天**（**due 2026-10-17**），其中 105134／76519／0322 标 `forensicTriage: Yes`，105133 为 No。
> **due_today（10-14）：0 条。newly_overdue（10-13 到期）：1 条**，即 Apple CVE-2026-86950（CoreGraphics）。AA26-281A 五条（BIND／Struts／Strapi／ONLYOFFICE／ProFTPD，10-11 到期）仍逾期。**未来 7 天到期：6 条**：Ivanti CVE-2026-104935 与 Windows CVE-2026-96951 在 **10-16**；今天新增的 4 条在 **10-17**。下列 CVE **仍未进 KEV**：Citrix 107406、Atlassian 21589、SonicWall 102255、Bricksforge 85097、GitLab 97229、Nextcloud／Collabora 110447、SiteGuard 106931、Vghost 74580、curl 92392、REDCap 90817。**Ahsay 两条今天进了 KEV**。
> 抓取备注：DOJ 新闻页对 curl 返回 401，链接取自 X 原帖与 CrowdStrike／THN 转述。Fox-IT 博文 http 链接改走 https 后取到 200。ASEC AgentTesla 完整 IoC 要订阅 AhnLab TIP，只抄公开部分。Risky Business 首页最新：RB #855「ShinyHunters done sowing, enters reaping phase」、Risky Bulletin「Spyware chip found in Ledger crypto-wallets」。tl;dr sec 最新仍是 **#349**。监控的红队工具今天**都没有新 release**（emp3r0r 最新 v5.2.2 发于 10-11，Sliver v1.7.8 发于 10-03，nuclei-templates v10.5.0 发于 10-05），但 nuclei-templates 主干窗口内并入了 **Ivanti CVE-2026-104935 检测模板**（PR #17419）。
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接作狩猎用途。泄露、入侵、勒索类声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【KEV 新增 · 邮件网关零日】Cisco Secure Email Gateway CVE-2026-76519**（CVSS 9.8）：未认证攻击者用特制附件即可拿到 root，前提是开启了 File Reputation／AMP 且 Content Scanner Tools 版本低于 25.3.0.5525。已有在野利用，今天进 KEV（due 10-17）。修复方式：更新 Content Scanner Tools 到 25.3.0.5525 或以上，**不用重启**；或升级 AsyncOS 到 15.5.5-014／16.5.0-780。**没有缓解措施**，每个集群成员都要跑 `grep "System Security"` 自查。
  X 原帖：https://x.com/BleepinComputer/status/2110422760203620843
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp
  文章：https://www.bleepingcomputer.com/news/security/cisco-patches-actively-exploited-secure-email-gateway-zero-day/
- **【KEV 新增 · 防火墙】PAN-OS CVE-2026-0322**（管理接口代码注入，攻击者需持有高权限账号即可提权到 root，CVSS-BT 8.6）：PAN 确认「非常有限的利用」，**并公开了 3 个攻击 IP**。PA／VM 系列与 Panorama 受影响，Cloud NGFW 和 Prisma Access 不受影响。修复版本表见下文 X-2，11.2.16 预计 10-15 发布。要点：把管理面收紧到跳板机。
  X 原帖：https://x.com/BleepinComputer/status/2110505197705310305
  厂商：https://security.paloaltonetworks.com/CVE-2026-0322
- **【KEV 新增 · 备份】AhsayCBS CVE-2026-105133／105134**：Huntress 观测到自 **10-07 23:20 UTC** 起被利用，攻击者落 JSP webshell，再部署伪装成 Edge 的 XMRig 加 WinRing0 驱动。厂商称早先补丁 9.15.2.59／10.3.4.0 修复不完整，须升到热修复 **10.3.4.45（v10）／9.15.2.70（v7–9）** 并重启。
  X 原帖：https://x.com/Horizon3Attack/status/2110413491823648770
  研究：https://www.huntress.com/blog/ahsaycbs-flaws-exploit
  厂商：https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update
- **【在野 · 未进 KEV】Nextcloud「Collabora Online – Built-in CODE Server」CVE-2026-110447**（CVSS 4.0 9.2，未认证 OS 命令注入，入口为 proxy.php）：**自 09-10 起被利用并落 webshell**。修复版本为 richdocumentscode **26.4.303**。**仅禁用这个 app 不够**，必须升级或卸载。独立部署的 Collabora 不受影响。
  X 原帖：https://x.com/TheHackersNews/status/2110428820042104994
  厂商：https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh
  文章：https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html
- **【KEV 后续】Ivanti CVE-2026-104935**：CISA 要求「立即」更新（期限 10-16）。Previdian 蜜罐到 10-14 共记录 **105 次尝试、50 个 IP**（新加坡／美国）。Defused 称 10-01 就看到披露前的利用。nuclei-templates 已并入检测模板。
  X 原帖：https://x.com/BleepinComputer/status/2110354748838645883
  文章：https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html
  GitHub（检测模板 PR）：https://github.com/projectdiscovery/nuclei-templates/pull/17419
- **【执法 · 钓鱼生态】Microsoft DCU + Health-ISAC + Resecurity 打击中文 PhaaS**：涉及 YAM Store（Storm-3119，转卖被劫持的 M365／Google 租户）与 CoGUI／Haozi／Iron Man（Storm-2990）。自 2026 年 1 月以来发出超过 10 亿条钓鱼邮件／短信，波及 75,000 多个组织。
  X 原帖：https://x.com/BleepinComputer/status/2110358322289254675
  厂商：https://www.microsoft.com/en-us/security/blog/2026/10/14/the-hidden-network-inside-the-phishing-infrastructure-ecosystem-powering-global-cybercrime/
  研究：https://www.resecurity.com/blog/article/iron-man-yamstore-powering-a-global-phishing-as-a-service-ecosystem
- **【APT · 新 IoC】Unit 42 PEERSTITCH（CL-STA-0954／UNC5820）**：利用 FortiManager CVE-2024-47575 入侵电信 MSP，植入 ARM64 内存驻留后门，期间还注册过伪造的虚拟 FortiGate。**Talos UAT-6275（Silent Lynx）**：利用 WinRAR CVE-2025-8088 投放 PickleShell，目标是独联体政府。
  研究：https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/
  研究：https://blog.talosintelligence.com/break-the-silence-kazakhstan-nexus-uat-6275-targets-cis-government-organizations/
- **【DPRK】FAMOUS CHOLLIMA 笔记本农场**：DOJ 起诉 14 人、逮捕 2 人；FBI 在「Operation Lonestar Roundup」中搜查德州 40 多处住所，查获约 187 台设备，涉及 70 多家雇主、约 300 万美元。
  X 原帖：https://x.com/CrowdStrike/status/2110363350278304230
  研究：https://www.crowdstrike.com/en-us/blog/fbi-disrupts-famous-chollima-operation-with-crowdstrike-assistance/
- **【其他高危】**Linux **Vghost** CVE-2026-74580（vhost IOTLB 本地提权，有条件下可逃逸虚拟机，PoC 已公开）；**curl** CVE-2026-92392（HTTP/2 上传 UAF，修复于 8.23.0）；**SiteGuard Server Edition** CVE-2026-106931（**已被利用**，更新前**先下载诊断信息留证**）；GitLab 97229 **公开 PoC**；Splunk 76268 公开 PoC；Adobe ColdFusion／Commerce 两个 CVSS 10.0；Fortinet FortiSandbox／FortiSIEM；SAP 89111（10.0）。
  X 原帖：https://x.com/Dinosn/status/2110223904484606349
  厂商：https://curl.se/docs/CVE-2026-92392.html
  厂商：https://eg-secure.co.jp/siteguard/news/alert-202610-1
- **【事件 · 后续】**Ledger 叫停亚洲经销商销售（CryptoBilis 间谍芯片）；Meta GitHub 泄露约 1,500 人；Gamdom 全站下线；日本 Arcadia 灾害通知与 NET119、Ride On Express 最多 650 万条；韩国 FSC 确认 16 家金融机构遭泄露；CenterPoint 106 万人。
  文章：https://www.bleepingcomputer.com/news/security/ledger-asks-sellers-across-asia-to-halt-sales-after-supply-chain-attack/
  X 原帖：https://x.com/DailyDarkWeb/status/2110148022420246559
- **【统计】** X 合并 **294**（A18／B5／C15／LWiS256），窗口内共见 689 条；seen_ids **2960→（见 state）**；KEV **2026.10.14／1745／Δ+4**；due_today **0**；newly_overdue **1**（Apple 86950）；未来 7 天到期 **6**（10-16 两条、10-17 四条）；tl;dr #349。


## CVE / POC / 漏洞

### X-1. 【KEV 新增 · 在野】Cisco Secure Email Gateway／Secure Email and Web Manager CVE-2026-76519（CWE-23 路径遍历 → root）
Cisco 10-14 发布公告：AsyncOS 在处理特制邮件附件时存在路径遍历。开启了 **File Reputation 或 File Analysis（AMP）**、且 **Content Scanner Tools 低于 25.3.0.5525** 的设备，可被未认证攻击者以 root 身份写文件并执行（CVSS 9.8）。Cisco 确认已有利用，CISA 当天收进 KEV（due 10-17，forensicTriage: Yes）。
**修复**：首选把 Content Scanner Tools 更新到 **25.3.0.5525+**（自动更新或用 CLI `contentscannerupdate`，**不用重启**）；也可升级 AsyncOS 到 **15.5.5-014** 或 **16.5.0-780**；16.0 系列需迁移到修复分支。Cisco Secure Email Cloud 已由厂商代为修复。**没有缓解措施**。
**狩猎**：在**每个集群成员**上执行 `grep "System Security" system_logs`。看到「Suspected compromise indicator was found」就按入侵处理，看到「No compromise indicator was found」为未见迹象。同时交叉比对设备之外的网络和防火墙日志，看是否有异常外联。虚拟设备若怀疑已被入侵，**先做快照或取证再升级**。
地址：
- X 原帖（BleepingComputer）：https://x.com/BleepinComputer/status/2110422760203620843
- X 原帖（THN）：https://x.com/TheHackersNews/status/2110442674167926933
- X 原帖（DailyDarkWeb，CISA 收录）：https://x.com/DailyDarkWeb/status/2110464661925794218
- X 原帖（CISA「4 CVEs」）：https://x.com/CISACyber/status/2110459179584356406
- X 原帖（cybermergemedia 处置要点）：https://x.com/cybermergemedia/status/2110474207050240024；https://x.com/cybermergemedia/status/2110477654474596754；https://x.com/cybermergemedia/status/2110480236802695394
- X 原帖（Python_s_）：https://x.com/Python_s_/status/2110453423174783140
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp
- 文章：https://www.bleepingcomputer.com/news/security/cisco-patches-actively-exploited-secure-email-gateway-zero-day/
- 文章：https://thehackernews.com/2026/10/cisco-warns-of-active-attacks.html
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
IoC：未见公开网络 IoC（厂商只给了上面的日志字符串）。

### X-2. 【KEV 新增 · 有限利用】Palo Alto Networks PAN-OS CVE-2026-0322（管理接口代码注入 → root）
需要**已认证的高权限管理员**，可通过管理 Web 界面注入代码并以 root 执行（CVSS 4.0 BT 8.6）。PAN 说明「Very limited exploitation」。影响 PA 系列、VM 系列与 Panorama；**Cloud NGFW 和 Prisma Access 不受影响**。CISA 10-14 收进 KEV（due 10-17，forensicTriage: Yes）。
**修复版本**：12.2.4；12.1.4-h12／12.1.7-h8／12.1.10-h2；11.2.4-h22／11.2.7-h21／11.2.10-h15／11.2.13-h3／11.2.16（预计 10/15）；11.1.4-h37／11.1.6-h39／11.1.7-h11／11.1.10-h35／11.1.13-h15／11.1.16-h3；10.2.7-h38／10.2.10-h41／10.2.13-h26／10.2.16-h11／10.2.18-h12。**没有临时缓解**。Threat ID **510046／510047**（content 9159-10287 及以上）只能有限覆盖，且需要开启解密。
**防御**：把管理接口限制在专用跳板机或管理网段，不要暴露到互联网；轮换管理员凭据，审计近期管理员登录来源；按下面的厂商 IP 回溯日志。
地址：
- X 原帖（BleepingComputer）：https://x.com/BleepinComputer/status/2110505197705310305
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2110495804041412989
- X 原帖（Python_s_）：https://x.com/Python_s_/status/2110483086605467947；https://x.com/Python_s_/status/2110453402966655248
- 厂商：https://security.paloaltonetworks.com/CVE-2026-0322
- 文章：https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-pan-os-rce-flaw-exploited-in-attacks/
IoC（厂商公告原样）：`66[.]42[.]72[.]14`、`208[.]83[.]239[.]114`、`149[.]248[.]47[.]234`

### X-3. 【KEV 新增 · 在野】AhsayCBS CVE-2026-105133（认证不当）／CVE-2026-105134（命令注入，`/rps/api/json/UpdateReceivers.do`）
Huntress 报告：**2026-10-07 23:20:15 UTC** 起有攻击者利用这两个漏洞。到 10-08 已有 5 个组织中招，攻击者落 JSP webshell，再从阿里云 OSS 拉取 `Taskgmr.ps1`，部署改过名的 NSSM（`msedge.exe`）和伪装成 Edge 的 XMRig（`edge.exe`），并加载 WinRing0 驱动。Horizon3 发布了技术分析，涉及认证绕过加 AddSysUser，以及 `/rps/obs7/rpsfile` 路径遍历（此处只记要点）。影响 **≤10.3.4**。厂商热修复：**10.3.4.45（v10）**、**9.15.2.70（v7–9）**，打完必须重启。厂商承认早先的 9.15.2.59／10.3.4.0 修复不完整。CISA 今天收录两条（due 10-17；105134 要求 forensicTriage）。
**狩猎**：查 `cbssvcX64.exe`／`cbssvcX86.exe` 的子进程（powershell、cmd、certutil 等）；查 Web 目录下新增的 JSP；查连
向下面 OSS／矿池地址的外联。
地址：
- X 原帖（Horizon3）：https://x.com/Horizon3Attack/status/2110413491823648770
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2110416115243372859；https://x.com/DFIR_Radar/status/2110416117554352278
- X 原帖：https://x.com/Python_s_/status/2110406199216631886
- 研究（Huntress）：https://www.huntress.com/blog/ahsaycbs-flaws-exploit
- 研究（Horizon3）：https://horizon3.ai/attack-research/attack-blogs/ahsaycbs-cve-2026-105133-cve-2026-105134-technical-analysis/
- 厂商：https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update
IoC（Huntress，原样）：
- IP：`177.4.12[.]11`、`38.60.252[.]110`、`107.191.47[.]199`、`185.220.236[.]49`、`104.234.26[.]10`、`123.202.208[.]37`
- 下载地址：`hxxp://imagefiles-backup.oss-ap-southeast-7.aliyuncs[.]com/javas/Office/win/{Taskgmr.ps1, edge.exe, msedge.exe, config.json, WinRing0x64.sys}`
- 矿池：`xmr.kryptex[.]network:8029`（`51.195.127[.]124`），user `krxYMRN97D/creativejs`
- SHA256：`05f69ae6b2b89c1c4dcf836bff032232f11bf0109f2b498e2345045d06139034`（msedge.exe，改过的 NSSM）、`4dcb0202fe8b2d4d7b183764e38184cd6ed50132786cc7e7d1f7f4bce1dd6f3d`（edge.exe，矿机）、`481728a7c9c4c02be07051d9c1958d902ea6397ebb8952ab83944818e3d25d21`（Taskgmr.ps1）

### X-4. 【在野 · 未进 KEV】Nextcloud「Collabora Online – Built-in CODE Server」（richdocumentscode）CVE-2026-110447（未认证 OS 命令注入）
Collabora 10-14 发布关键公告（GHSA-g3vx-3m76-fghh，CVSS 4.0 9.2）：内置 CODE 服务器的 `proxy.php` 存在未认证命令注入，**仅当内置 CODE 服务器没有在运行时**才会触发。THN 报道自 **2026-09-10** 起被在野利用、落 webshell。**修复**：richdocumentscode **26.4.303**（09-11）。**仅在 Nextcloud 里禁用该 app 不足以防护**，必须升级或卸载；Nextcloud ≤29 要先升级 Nextcloud 再升应用。**独立部署的 Collabora 不受影响**。与 CVE-2025-66208 路径不同。26.4.402 有稳定性问题。**仍未进 KEV**。
**狩猎**：查 `apps/richdocumentscode` 下的 `shx*.php`／`shrf*.php` 文件；查 09-10 以来对 `proxy.php?status` 带 `%2e%2e`／`$(`／`${IFS}` 的请求；查 web 账户发起的 sudo 尝试。
地址：
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2110410349174288583
- X 原帖：https://x.com/ThreatWire_/status/2110224199604220150；https://x.com/TheHackersNews/status/2110428820042104994；https://x.com/Python_s_/status/2110369113797198228
- 厂商（GHSA）：https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh
- 厂商（issue）：https://github.com/CollaboraOnline/richdocumentscode/issues/354
- 文章：https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html
- CVE：https://www.cve.org/CVERecord?id=CVE-2026-110447
IoC（公开 webshell 文件名，原样）：`shrf4645.php`、`shxa35d0.php`、`shx5cf91.php`、`shxd33ce.php`、`shxf4645.php`、`shx13a86.php`、`shx56367.php`

### X-5. 【KEV 续 · 紧急】Ivanti Connect Secure CVE-2026-104935（认证绕过 + RCE）
CISA 10-14 发出「立即修补」提醒，期限仍是 **10-16**。Previdian（CEO Ryan Dewhurst）称到 10-14 蜜罐共记录 **105 次利用尝试、50 个唯一 IP**（地理定位新加坡与美国）：攻击者用 `X-DSCGI-PATH` 头到达内部 CGI handler，上传伪装成 ZIP 的 Perl 脚本，目前多为「测试能否执行代码」而非投放恶意载荷。Defused Cyber 称自 **10-01** 就捕获到披露前利用，Volexity 归因未知团伙 **UTA0576**（犯罪动机）。Shadowserver 现跟踪 5,600 多台暴露在公网的 ICS 指纹主机。Ivanti 另修 **Xtraction CVE-2026-106042**（9.9，凭据暴露，2026.4 修复）。nuclei-templates 已并入检测模板（PR #17419，被动指纹 `X-DSCGI-PATH`）。
地址：
- X 原帖（THN）：https://x.com/BleepinComputer/status/2110354748838645883
- X 原帖：https://x.com/TheHackersNews/status/2110353632122286230；https://x.com/pdiscoveryio/status/2110340670758195418；https://x.com/DFIR_Radar/status/2110461668685668560；https://x.com/DFIR_Radar/status/2110476830847455684
- X 原帖（CISA，go.dhs.gov/5Kc）：https://x.com/CISACyber/status/2110165190004064282
- 文章：https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html
- 文章：https://www.bleepingcomputer.com/news/security/cisa-warns-admins-to-immediately-fix-ivanti-flaw-exploited-as-zero-day/
- 研究（Volexity，10-13）：https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/
- 厂商（Xtraction）：https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Xtraction-Multiple-CVEs
- 检测模板：https://github.com/projectdiscovery/nuclei-templates/pull/17419
IoC（Previdian 公布的攻击 IP 示例，原样）：`216.73.160[.]59`、`216.73.160[.]61`、`216.73.160[.]210`、`45.8.19[.]111`

### X-6. 【Patch Tuesday 续】Windows CVE-2026-96951（Shell MotW 绕过，在野）＋ 10 月创纪录补丁
本月补丁量各家统计 1,411–1,417 条（BleepingComputer 1,411／3 零日，SecurityWeek 1,413）。**唯一确认在野**的是 Windows Shell CVE-2026-96951（MotW／SmartScreen 绕过，KEV due 10-16）；狩猎点是丢失的 Zone.Identifier，补丁 KB5126646。其它关键项：OpenSSH for Windows CVE-2026-97816（9.8）、QUIC CVE-2026-100219（9.8）、DHCP Server CVE-2026-96934（9.8）、Outlook CVE-2026-70242（9.8）、Exchange CVE-2026-70571、AD DS CVE-2026-70229、NDES CVE-2026-69802。另：VS/SSMS Copilot **CVE-2026-103572**（Johann Rehberger；提示注入 → 恶意 MCP → 代码执行；修复 VS 2022 17.14.42／VS 2026 18.10.4）；**mup.sys DFS CVE-2026-70111**（Corelight 发现的 0day，一个特制 DFS referral 包可让 Server 2019/2022/2025 蓝屏，Event ID 41/6008）；SmartScreen VBS enclave CVE-2026-83498（9 月补丁，四字节写加时序）。另有近期 Windows 更新可能触发 RDP 连接失败的已知问题。
地址：
- X 原帖（crysis939386，排序）：https://x.com/crysis939386/status/2110244055108178282
- X 原帖（wunderwuzzi23，VS/SSMS）：https://x.com/wunderwuzzi23/status/2110152411423953267
- X 原帖（richardhicks，关键清单）：https://x.com/richardhicks/status/2110172848002408640
- X 原帖（ThreatAft，1,413/96951）：https://x.com/ThreatAft/status/2110234043849773482
- X 原帖（cybermergemedia，96951 狩猎）：https://x.com/cybermergemedia/status/2110364079923814687
- X 原帖（cyb3rops）：https://x.com/cyb3rops/status/2110323529447018638
- X 原帖（SecurityWeek）：https://x.com/SecurityWeek/status/2110268928970608724
- 文章：https://www.securityweek.com/microsoft-patches-record-1413-vulnerabilities-including-exploited-windows-zero-day/
- 文章：https://thehackernews.com/2026/10/microsoft-patches-record-1413-flaws.html
- 播客（SANS ISC）：https://isc.sans.edu/podcastdetail/10136
- MSRC（103572）：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-103572
- 研究（Corelight DFS）：https://corelight.com/blog/cve-2026-70111-microsoft-distributed-file-system-0-day
- 文章（RDP 问题）：https://www.bleepingcomputer.com/news/security/microsoft-recent-windows-updates-may-trigger-remote-desktop-failures/
- 文章（SmartScreen 83498）：https://thehackernews.com/2026/10/four-byte-write-and-timing-bug-let.html
IoC：未见公开 IoC（96951 为 MotW 绕过，以 Zone.Identifier 缺失作狩猎信号）。

### X-7. 【PoC 公开 · 未进 KEV】Linux 内核 Vghost CVE-2026-74580（vhost 过期 IOTLB，本地提权）
腾讯朱雀实验室披露：vhost 子系统的过期 IOTLB 条目可被有 `/dev/vhost-*` 访问权的本地用户利用提权到 root（CVSS 8.8）；在配置了 vIOMMU 的场景下有条件地可从客户机逃逸到 QEMU。PoC 已公开（本报告不转载步骤）。**修复**：5.10.265／5.15.216／6.1.183／6.6.152／6.12.104／6.18.45／7.1.9。RHEL 8/9/10 当前仍列为受影响，关注发行版补丁。
地址：
- X 原帖：https://x.com/Dinosn/status/2110223904484606349；https://x.com/TheHackersNews/status/2110278636754575716；https://x.com/ThreatWire_/status/2110280729166749913；https://x.com/DFIR_Radar/status/2110204828400103735
- 研究（腾讯）：https://matrix.tencent.com/en/2026/10/12/vghost-cve-2026-74580
- oss-security：https://www.openwall.com/lists/oss-security/2026/10/14/2
- 内核提交：https://git.kernel.org/linus/de845981da67a6b049080c87e605130b0c30adc5
- Ubuntu 追踪：https://ubuntu.com/security/CVE-2026-74580
- 文章：https://thehackernews.com/2026/10/ai-found-linux-kernel-flaw-gives-local.html
IoC：无（本地提权漏洞，不涉及网络 IoC）。

### X-8. 【修复 · 未进 KEV】curl CVE-2026-92392（HTTP/2 上传 Use-After-Free）
恶意或被攻陷的服务器可在 HTTP/2 上传场景触发 UAF，有条件下可导致 RCE。影响 **8.12.0–8.22.0**，修复 **8.23.0**，回移分支 8.14.3／8.16.2／8.20.2。由 Luna Tong 借助 Claude 发现，pruva 给出复现。
地址：
- X 原帖：https://x.com/TheHackersNews/status/2110344777413837218；https://x.com/ThreatWire_/status/2110432385296638158；https://x.com/N3mes1s/status/2110461814232240470
- 厂商：https://curl.se/docs/CVE-2026-92392.html
- 文章：https://thehackernews.com/2026/10/curl-patches-http2-upload-flaw-after.html
- 复现：https://www.pruva.dev/reproductions/REPRO-2026-00386
IoC：无（库漏洞）。

### X-9. 【在野 · 未进 KEV】SiteGuard Server Edition CVE-2026-106931（OS 命令注入 → root/SYSTEM）
日本 EG Secure 10-14 公告：WAF 产品 SiteGuard Server Edition 的**统计功能**（默认开启）存在 OS 命令注入，已确认在野利用；本地低权限可提权到 root/SYSTEM。影响 Ver2.20 起、低于 Apache/Nginx/IIS 版 **Ver8.00 Update5** 与 FreeBSD 版 **Ver7.00 Update6**（IIS 版 Ver3.10–Ver4.00 Update4 不受影响）。**更新或打补丁前，务必先从 Web 管理界面下载并保存「诊断信息」留证**，否则攻击痕迹可能被清除。JVN#88474777。
地址：
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2110480775888118223
- 厂商：https://eg-secure.co.jp/siteguard/news/alert-202610-1
IoC：未见公开 IoC（只给了保全诊断信息的指引）。

### X-10. 【PoC 公开 · 未进 KEV】GitLab CVE-2026-97229（CI lint 整数溢出 → RCE）
Rapid7 的 jburgess 公开 PoC 仓库（已对官方修复验证，仓库只给链接作狩猎用途）。**狩猎**：查带 `content_ref` 的匿名 `ci/lint` GET 请求。**仍未进 KEV**。
地址：
- X 原帖：https://x.com/ThreatWire_/status/2110275956191424584；https://x.com/cybermergemedia/status/2110395109107986505；https://x.com/cybermergemedia/status/2110398526257787351
- GitHub·PoC：https://github.com/jburgess-r7/CVE-2026-97229-PoC
IoC：无。

### X-11. 【PoC 公开】Splunk Enterprise CVE-2026-76268（SHC Patroni REST API 未认证 RCE）
未认证可经 Patroni REST API 触发（CVSS 9.8）。影响 10.4 < 10.4.3、10.2 < 10.2.7。公开 PoC 仓库（仅链接）。
地址：
- X 原帖（DarkWebInformer）：https://x.com/DarkWebInformer/status/2110412670461419767
- X 原帖（Python_s_）：https://x.com/Python_s_/status/2110345285310288189
- 厂商：https://advisory.splunk.com/advisories/SVD-2026-1001.html
- GitHub·PoC：https://github.com/murrez/CVE-2026-76268
IoC：无。

### X-12. 【扫描中 · 未进 KEV】Atlassian / SonicWall / Citrix / Bricksforge 利用遥测
- **Atlassian CVE-2026-21589**：Previdian 遥测自 10-06 起 **579 次尝试、64 个 IP、19 国**。X：https://x.com/Python_s_/status/2110449431019475243；研究：https://previdian.com/CVE-2026-21589
- **SonicWall SMA1000 CVE-2026-102255**：Previdian 记录 135 次尝试。X：https://x.com/Python_s_/status/2110345111741612295
- **Citrix NetScaler CVE-2026-107406**：一周内第三个在野零日（CVE-2026-88771「Pitscaler」已在 KEV）。X：https://x.com/xbhaveshverma/status/2110151097776238806；https://x.com/Python_s_/status/2110345339483926621
- **Bricksforge CVE-2026-85097**（WordPress 插件）：Patchstack 称自 10-07 起 63 个 IP 扫描；修复 3.1.8.10／4.0.2。X：https://x.com/ThreatWire_/status/2110292522257797290
IoC：以上为扫描遥测，厂商未统一公布攻击 IP。

### X-13. 【厂商补丁日合集】Adobe / Fortinet / SAP / 浏览器 / NGINX / Docker / ICS
- **Adobe**（140 个漏洞，10 个产品）：Commerce CVE-2026-103849（10.0）、ColdFusion CVE-2026-105899（10.0；升 2025 U14／2023 U26）、AEM CVE-2026-90532。X：https://x.com/SecurityWeek/status/2110196392899572198；厂商：https://www.adobe.com/trust/security/products/coldfusion/apsb26-144.html ；文章：https://www.securityweek.com/adobe-patches-140-vulnerabilities-across-10-products/
- **Fortinet**：FortiSandbox CVE-2026-107656（9.6 认证绕过）、FortiSIEM CVE-2026-106173（9.4 未认证 RCE）；暂无已知利用。X：https://x.com/DailyDarkWeb/status/2110241718083932180；厂商：https://fortiguard.fortinet.com/psirt/FG-IR-26-185 ；文章：https://www.securityweek.com/citrix-fortinet-ivanti-patch-29-vulnerabilities-across-their-products/
- **SAP**（10-13 补丁日，16 条）：NetWeaver OAuth2 SSRF CVE-2026-89111（10.0），另有 89107（9.9）／89108／89110。X：https://x.com/DailyDarkWeb/status/2110151972271906889；https://x.com/SecurityWeek/status/2110252583633977419；文章：https://www.securityweek.com/sap-patches-critical-netweaver-s-4hana-vulnerabilities/
- **Chrome/Firefox**（共 114 个）：Firefox 修复 158／ESR 153.5（CVE-2026-109705）。X：https://x.com/SecurityWeek/status/2110274451879465079；厂商：https://www.mozilla.org/en-US/security/advisories/mfsa2026-106/ ；文章：https://www.securityweek.com/chrome-firefox-updates-patch-114-flaws-as-mozilla-unveils-firefox-enterprise/
- **F5 NGINX**：CVE-2026-97205／93479／15176（内存，OSS 1.31.7／1.30.6）。X：https://x.com/ThreatWire_/status/2110504713359671558；文章：https://www.threatwire.tech/news/f5-patches-three-nginx-memory-flaws-rated-cvss-9-2
- **Docker Hub** CVE-2026-105445：https://www.docker.com/blog/docker-hub-security-advisory-cve-2026-105445/
- **ICS Patch Tuesday**：Siemens 17 条，Rockwell 修 ArmorBlock 接管漏洞 CVE-2026-12655。X：https://x.com/SecurityWeek/status/2110389817582526827；厂商：https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1801.html
IoC：均为补丁类，无在野 IoC。

### X-14. 【研究 · 链利用与越权】XBOW / UniFi / Zimbra / Intune / ServiceNext / OCI
- **XBOW Chrome 全链**（CVE-2026-85045／78952，GPT-5.6 "Sol"，奖金 $250K）：https://xbow.com/labs/research/zero-to-calc-in-six-days-inside-xbow-chrome-full-chain ；文章：https://thehackernews.com/2026/10/researchers-used-public-openai-model-to.html
- **UniFi Protect AI Key** 六漏洞链（ZephrFish）：https://x.com/ZephrFish/status/2110347903294156874；厂商：https://community.ui.com/releases/Security-Advisory-Bulletin-070-070/e7ffc9fa-9129-4a90-b5e3-d597c5ee7a73
- **Zimbra**（Rapid7）：CVE-2026-93637／93635 未修，CVE-2026-73571 已在 10.1.17 修复：https://www.rapid7.com/blog/post/ve-breaking-zimbra-identity-boundaries-part-1/
- **Intune Company Portal LPE**（Amberwolf）：https://x.com/buffaloverflow/status/2110356418985374137；研究：https://blog.amberwolf.com/blog/2026/october/company-portal-self-service-to-system/
- **ServiceNext CVE-2026-79957 IDOR**（BlackLantern）：https://x.com/BlackLanternLLC/status/2110432058388676866
- **OCI Identity Domains 权限绕过**（NetSPI）：https://www.netspi.com/blog/technical-blog/cloud-pentesting/administrating-the-administrator-an-oci-identity-domains-permission-bypass/
- **CVE-2026-83834 exploit 仓库**（z0v3r1n，仅链接）：https://x.com/z0v3r1n/status/2110408938776838360；https://github.com/wkpwn/CVE-2026-83834/
IoC：无。

### X-15. 【OT · 续】Danfoss 冷链控制器 CVE-2025-41450
Shadowserver 仍每日观测 **≥365** 台暴露在公网的 Danfoss AK-SM 800A（较此前 >550 下降）。Pen Test Partners 发文复盘 CVE-2025-41450 认证绕过（入口仍未官方确认）。
地址：
- X 原帖：https://x.com/Shadowserver/status/2110432207261077759；https://x.com/DFIR_Radar/status/2110492109325168930；https://x.com/DFIR_Radar/status/2110250051909935378
- 研究（PTP）：https://www.pentestpartners.com/security-blog/you-dont-need-a-nation-state-to-warm-up-a-fridge/
- 研究（Claroty Team82）：https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers
- 统计（Shadowserver）：https://dashboard.shadowserver.org/statistics/iot-devices/time-series/?vendor=danfoss&model=ak-sm+800a
IoC：无新增。

## 工具与 GitHub 发布

> 防御视角收录，均为公开仓库／发布，只给链接，不含利用步骤。

### G-1. rad9800 开源 lindm（Linux 车队 MDM）
自托管的 Linux 设备管理：注册、分阶段推送配置、磁盘加密、锁定／擦除、RBAC／审批／SCIM、带策略的「征得同意式」远程协助。蓝队可用于管控 Linux 终端。
- X 原帖：https://x.com/rad9800/status/2110185671000523165
- GitHub：https://github.com/radkawar/lindm

### G-2. rad9800 screenlogger v0.2.0（macOS 屏幕历史）
私有、可搜索的 macOS 屏幕历史工具，0.2.0 新 UI、更省磁盘。取证／自查可参考。
- X 原帖：https://x.com/rad9800/status/2110501433011589632
- GitHub（release）：https://github.com/radkawar/screenlogger/releases/tag/v0.2.0

### G-3. chryzsh/redteam-bofs（BOF 合集，ipurple 转介）
后渗透用 Beacon Object File 合集（凭据搜寻、系统侦察等）。蓝队可据此建检测。
- X 原帖：https://x.com/ipurple/status/2110368577752531184
- GitHub：https://github.com/chryzsh/redteam-bofs

### G-4. 博客／技术文章
- **AMSI/ETW 绕过（自定义 PowerShell Runspace）**（ipurple 转介 by7e.dev）：https://by7e.dev/blog/runspace ；X：https://x.com/ipurple/status/2110281068431429781
- **Synacktiv：Rikugan vs Frontkick**（IDA 上的 agentic AI 逆向对比）：https://www.synacktiv.com/en/publications/ufc-666-frontkick-vs-rikugan ；X：https://x.com/Synacktiv/status/2110296456582095172
- **ntlmrelay 本周高频分享链接**（含 Pwn2Own Automotive 2026 Alpine iLX-F511 0-Click RCE Writeup）：https://github.com/newbe3e/Pwn2Own-Automotive-2026-Alpine-iLX-F511-0-Click-RCE-Exploit-Writeup ；X：https://x.com/ntlmrelay/status/2110325446470762945

### G-5. 红队工具 Release 巡检（GitHub API）
本窗口内监控的主流工具**无新 release**：emp3r0r 最新 v5.2.2（10-11）、Sliver v1.7.8（10-03）、nuclei v3.11.1（08-08）、nuclei-templates v10.5.0（10-05）、NetExec v1.5.1、Mythic v3.4.0.5、BloodHound v9.8.0（10-07）。**nuclei-templates 主干**在窗口内并入 Ivanti CVE-2026-104935 被动检测模板（PR #17419）及多条 Patch Tuesday / Check Point 等模板。
- GitHub：https://github.com/projectdiscovery/nuclei-templates/pull/17419

## APT / Malware 分析

### M-1. Microsoft DCU + Health-ISAC + Resecurity 打掉中文 PhaaS 生态（YAM Store / CoGUI / Haozi / Iron Man）
Microsoft 把转卖被劫持 M365／Azure for Education 租户的初始访问经纪商 **YAM Store** 追踪为 **Storm-3119**，把 CoGUI（又名 NX／FA）、Haozi（又名 Phoenix）、Iron Man System 三个钓鱼套件及其开发者追踪为 **Storm-2990**。自 2026 年 1 月以来，这些套件共促成 **10 亿+** 条钓鱼邮件／短信，波及 150 多国 **75,000+** 组织（仅针对 Microsoft 客户就 7.5 亿+），获利数千万美元。Iron Man 含 2,335+ 模板、覆盖 139 国，许可服务器域名硬编码进套件；多托管在中国境内、用 GoFrame 框架。Microsoft 与 Health-ISAC 正拆除 YAM Store／CoGUI／Iron Man 三块基础设施。
地址：
- X 原帖（DFIR_Radar）：https://x.com/BleepinComputer/status/2110358322289254675
- X 原帖（MsftSecIntel）：https://x.com/MsftSecIntel/status/2110357939047272473
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2110413341625606634
- X 原帖（SecurityWeek）：https://x.com/SecurityWeek/status/2110358780089352261
- 研究（Microsoft 威胁情报）：https://www.microsoft.com/en-us/security/blog/2026/10/14/the-hidden-network-inside-the-phishing-infrastructure-ecosystem-powering-global-cybercrime/
- 博客（Microsoft On the Issues／DCU）：https://blogs.microsoft.com/on-the-issues/2026/10/14/disrupting-the-service-economy-behind-transnational-cybercrime-operations/
- 研究（Resecurity）：https://www.resecurity.com/blog/article/iron-man-yamstore-powering-a-global-phishing-as-a-service-ecosystem
- 文章（BleepingComputer）：https://www.bleepingcomputer.com/news/security/global-takedown-hits-network-behind-1-billion-phishing-messages/
- 文章（THN）：https://thehackernews.com/2026/10/microsoft-disrupts-3-phishing-kits.html
IoC（Resecurity，defang 原样）：`docker.aidchildren[.]cc`、`docker.loveboy[.]xyz`、`install.loveboy[.]xyz`、`api2.peaceman[.]cc`、`ipapi2.peaceman[.]cc`、`bin2.peaceman[.]cc`、`log2.peaceloving[.]xyz`、`ossapi.haoeryu[.]top`、`api2.haoyutai`；YAM Store 伪造非营利域名示例 `jewishchoice[.]org`。

### M-2. Unit 42：Casbaneiro + "Painel Gangster"（滥用 ScreenConnect 试用租户）
巴西银行木马 Casbaneiro 通过被滥用的 ScreenConnect 试用租户投递，配合名为「Painel Gangster」的 Chromium 扩展。完整 IoC 见 Unit42 仓库。
地址：
- 研究（Unit 42 IoC）：https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-13-Casbaneiro-Banking-Trojan.txt
- X 原帖（Unit42_Intel）：https://x.com/Unit42_Intel/status/2110431971088253318
IoC（原样摘录）：
- 域名：`n1.youconnectedssl[.]digital`、`updatehostingfree[.]top`、`euromasterx[.]com`、`xdrivewin[.]com`、`uixfilepdfview[.]top`、`locuralocuralocuraloocura[.]top`、`arneighti[.]com`、`knowledgerknolle[.]com`、`learnflourishspace[.]com`、`zytherostudio[.]com`
- IP：`216.203.21[.]119`、`190.2.184[.]201`、`216.203.20[.]116`、`65.38.121[.]128`、`134.209.200[.]162`、`142.93.109[.]181`、`45.76.69[.]213`、`45.61.136[.]99`
- SHA256：`d180a1978cd547f8aa4c387f951c720f0b2ff9641a45a8153994a8f29cfdf610`（zlibai.dll）、`6cdf132ee130b4cec889e39e06b07559fb4119c61a62d48c03cf357f66eb8900`（loader）、`c14c25792af4e1552b54b4fe0aca6e405ed052b4ba4af67a439bfdad5b3919ed`（crx）
- 落地物：`C:\Docstar\zlibai.dll`＋`VmLauncher.exe`；`chrome.exe --load-extension=C:\chrome`

### M-3. Unit 42：PEERSTITCH / CL-STA-0954（又名 UNC5820）—— FortiManager CVE-2024-47575
针对电信 MSP，2024 年 9 月入侵，利用 FortiManager CVE-2024-47575，植入 ARM64 内存驻留 implant，并注册过伪造虚拟 FortiGate（序列号 `FMG-VMTM23017412`，名为 "localhost"）。10-14 发文。
地址：
- 研究（Unit 42）：https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/
- X 原帖：https://x.com/DFIR_Radar/status/2110506667443921193
IoC（原样摘录）：
- IP：`45.32.41[.]202`、`198.199.122[.]22`、`23.240.77[.]233`、`47.18.167[.]159`
- URL：`hxxp[:]//23.240.77[.]233:8085/pM.js`、`hxxp[:]//47.18.167[.]159:8085/pM.js`、`hxxp[:]//23.240.77[.]233:8084/acme/...`（directory／new-acct／order／authz／finalize）
- SHA256：`b9fb0b27ddd59b58d3ae53c7227298a3e0de1e6f868b9429ae21533bb9cd1e70`（核心 ptrace 注入器）、`829b1cd270b30565739a478441833f49f10a49bd06f0d18cc96c8ae4a0431f11`、`bd064244dad748cf2a44074bee56f5bfab4a2b18ee944b75d1b3febd4c1fe02a`、`9c4c4436ff5cdf0d6d68f5108031cbf3708a095cde4ef8c09316af7a7110437e`、`fc1b10c58057ef9f1f9a1e2a3d4a1c89f43b0ead451398c70ed7a6e0312b36ee`、`f84eea718526706afdf2d1a2774fab76ecb11c18fb61995a37be8249c5e379ab`、`b7ae166fd49a7ecfe6322a80b8aa56d6aa0825d8f5d106dab2e4fb7d14ce15a8`

### M-4. Talos UAT-6275（Silent Lynx）/ Recorded Future TAG-193
哈萨克斯坦相关团伙，针对独联体政府，四条感染链之一用 WinRAR CVE-2025-8088 把 PickleShell 放进启动目录；家族含 Chvost／Laplas／PickleShell／FoalShell。Talos 给出 ClamAV 签名 `Win.Backdoor.PickleShell-10060602-0` 与 Snort 规则（SID 1:11192／1:15306／1:46983／1:47398 等），完整 IoC 在 GitHub。
地址：
- 研究（Talos）：https://blog.talosintelligence.com/break-the-silence-kazakhstan-nexus-uat-6275-targets-cis-government-organizations/
- GitHub IoC：https://github.com/Cisco-Talos/IOCs/tree/main/2026/10
- 研究（Recorded Future TAG-193）：https://www.recordedfuture.com/blog/tag193-regional-espionage-operations
- X 原帖：https://x.com/DFIR_Radar/status/2110371079860744545；https://x.com/Dinosn/status/2110374348867424291
IoC（Talos 仓库节选，C2 子域，原样）：`catalog-update-microsoft.servehttp[.]com`、`microsoft-update-catalog.servehttp[.]com`、`cdn-redhatupdate.serveftp[.]com`、`repo-centos-vault.serveftp[.]com`、`esd.asan.gov.zapto[.]org`、`gptbot.sytes[.]net`、`n8nbot.sytes[.]net`（完整约 300 条见仓库）。

### M-5. DPRK FAMOUS CHOLLIMA 笔记本农场被端（DOJ / FBI / CrowdStrike）
DOJ 宣布协调行动：起诉 14 人、逮捕 2 名美国公民；FBI「Operation Lonestar Roundup」搜查德州 40 多处住所，查获约 187 台设备，涉及 70 多家雇主、约 300 万美元。
地址：
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2110168486949589444
- X 原帖（SecurityWeek）：https://x.com/SecurityWeek/status/2110323740647305450
- X 原帖：https://x.com/CrowdStrike/status/2110363350278304230；https://x.com/CrowdStrike/status/2110400238343131371
- 研究（CrowdStrike）：https://www.crowdstrike.com/en-us/blog/fbi-disrupts-famous-chollima-operation-with-crowdstrike-assistance/
- 政府（DOJ）：https://www.justice.gov/opa/pr/justice-department-announces-coordinated-actions-combat-north-korean-remote-it-worker
- 文章（THN）：https://thehackernews.com/2026/10/us-shuts-down-over-40-laptop-farms.html
- 文章（BleepingComputer）：https://www.bleepingcomputer.com/news/security/fbi-raids-dprk-it-worker-laptop-farms-in-texas-us-nationals-arrested/
IoC：未见统一公开 IoC（执法行动）。

### M-6. Forescout：Lorem Ipsum Loader / Axolotl（Vanilla Tempest / Vice Society）
对比分析两款加载器，溯源到 Rapid Brigantine（又名 Vanilla Tempest／Vice Society，曾部署 Rhysida／BlackCat 等勒索）。本次 IR 事件在部署 Python 隧道前被遏制。用 SEO 投毒＋木马化 Teams／MSI 投递，经公共论坛死投点解析 C2。
地址：
- 研究（Forescout）：https://www.forescout.com/blog/from-clickfix-to-c2-comparative-analysis-of-two-malware-loaders/
- X 原帖：https://x.com/DFIR_Radar/status/2110340744292471099；https://x.com/Dinosn/status/2110351372571099577
IoC（原样摘录）：
- SHA256：`13a3fa500e91e35a34f71e0e88f07a5b3dd8251e9b423188030e31dbd8eaf603`（MT_setup_v3.22.7182.msi）、`074e58df3af3e83ca4fff7006ff6006b24b7182fde75fdbf894ee60161a6ed15`（stage_03）、`ec7c33d434af7635f202dd726f34e03304f9a7d839c4625d962515d655d190c5`（o1.ps1）
- 死投点：`letsdiskuss[.]com/user/{lindawilliams51453, dhuahsd12d2752, joeblack1673}`（亦见 `digitalpoint[.]com`）；联系邮箱 `lindawilliams@onionmail[.]org`
- C2 域名：`scriptedgeapp[.]com`（213.109.203[.]107）、`transferrootway[.]com`（45.66.249[.]57）、`updaterdeskarc[.]com`（185.28.119[.]81）、`signinbyte[.]com`（185.28.119[.]14）、`bloganimals[.]com`（185.28.119[.]138，Axolotl）
- C2 流量：POST `/api/init/<uuid>`，Content-Type `image/jpeg`，UA `Firefox/143.0`

### M-7. Huntress：假 WatchGuard VPN + ChatGPT 自定义 GPT ClickFix
- **假 WatchGuard VPN**（SEO 投毒）：`watchguard-vpn[.]net` 用弹窗窃取 VPN 服务器地址／账号／密码，凭据回传 `watchguard-ssl[.]online`；下载的是**真**的已签名安装包。10-13 该域已下线。微软曾把相关更广活动归于 Storm-2561。研究：https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing ；X：https://x.com/DFIR_Radar/status/2110280456562221547
- **ChatGPT 自定义 GPT ClickFix RAT**：通过 Google 广告把受害者引到 ChatGPT 上的自定义 GPT 页，再跳 Google Sites 假 CAPTCHA，诱导粘贴终端命令。研究：https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat ；X：https://x.com/HuntressLabs/status/2110415938860314666
IoC（Huntress，原样）：
- WatchGuard：`watchguard-vpn[.]net`（80.249.132[.]140）、`watchguard-ssl[.]online`（158.94.209[.]19）
- ChatGPT GPT：`hxxps://chatgpt[.]com/g/g-6ab595ad6554819181b686d4876efb80-plus-5-6`、`hxxps://chatgpt[.]com/g/g-6ab6ba039440819185ed491740b11cf8-plus-5-6`、`gptverification[.]com`、`sites[.]google[.]com/view/antibot172881`、`sites[.]google[.]com/view/antibot381122`、`hxxp://1614733393/app/afafa98279c9/ISOSimple[.]msi`（=96.62.224[.]81）、`45.140.205[.]28`

### M-8. Netskope：XWorm 泄露 V6.4 builder，演化为监控平台
Netskope 跟踪到 4 个在野版本、46 个插件（新增 SteamTokenRecovery／Rootkit／ResetSurvival／Cmstp-Bypass 等，并带 HBrowser 实时浏览器控制）。2025 年 6 月 builder 被破解、8 月 6.4 源码泄露后检测量大涨；2026 Q3 检测 1,236 次，金融业约占 35%。
地址：
- X 原帖（securityaffairs）：https://x.com/securityaffairs/status/2110273495649095731
- X 原帖（SecurityWeek）：https://x.com/SecurityWeek/status/2110192366061519124
- 文章：https://securityaffairs.com/200910/malware/how-a-leaked-builder-of-xworm-turned-a-remote-access-trojan-into-a-surveillance-kit.html
- 文章：https://www.securityweek.com/xworm-rat-evolves-into-surveillance-platform/
IoC：见 Netskope 原报告（本摘要未逐条抄录）。

### M-9. ThreatFabric：Hirudo Android 银行木马
通过假更新诱导，再替换为打过补丁的银行 App 以规避检测；诱饵 App 包括 Shopora、1V1 X、ZoyaTV、KoiShort。
地址：
- X 原帖：https://x.com/TheHackersNews/status/2110332067590676755
- 研究：https://www.threatfabric.com/blogs/hirudo-from-fake-updates-to-patched-banking-apps
- 文章：https://www.bleepingcomputer.com/news/security/hirudo-android-malware-replaces-banking-apps-to-evade-security-checks/
IoC（ThreatFabric，SHA256，原样）：`f796eb9ecf516e4f1fafcf89200d9f7d8ddd234f705e63f1bc8fc3ef583f0248`、`0097a0406be20544e98e981075427f40789db40fe4a53b1b4523383a945328b7`（Shopora 诱饵）、`2e45277acfde3fb704179476b08f428f66a03670bbdbf2e8ec79c0b0333c009b`（1v1 vip）、`d51f2bd7ffb49c224d8eaec2c8ca1c8ab9fce2fd5fdceea01eb54296c2f47b4d`（KoiShort）、`425cd7072b5e9386ac94e97fe272980b6ef36240df6b5d77b371ab7378004c83`（ZoyaTV）、`b2270c29b3d0a49a716730d6ef108cffec0b1a4b159dd02e93333fb85e492b99`（Hirudo RAT 7 月版）

### M-10. Group-IB：KGB RAT（NjRAT 分支，MaaS）
基于 NjRAT 的 FUD 木马即服务，用 Telegram Bot API 做 C2 通知、ip-api 做地理定位，配每日更新的加壳器对抗 Windows Defender。
地址：
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2110295439337521314
- 研究：https://www.group-ib.com/blog/kgb-rat-windows-fud-trojan/
IoC（Group-IB，原样）：C2 `104[.]248[.]130[.]195`，次要 C2 `2[.]59[.]134[.]215:443`；滥用 `api.telegram[.]org`、`ip-api[.]com`。

### M-11. 其它恶意软件 / 情报简讯
- **ASEC：AgentTesla 位图加载器**（`%APPDATA%\AH.Exe`）：https://asec.ahnlab.com/en/95840/ ；公开 MD5：`8777a9b0533660fddc2a73b819638c18`、`cbcc4ba1a1485cb01a4b65fc7915e629`（完整 IoC 需 AhnLab TIP）。X：https://x.com/threatintel/status/2110392061036023865
- **abuse.ch：Nyxar Stealer**：C2 `nyxar[.]cc`、`nyxar[.]lol`、`nyxarstealer[.]lol`、`nyxarst[.]lol`、`polnet[.]lol`。https://bazaar.abuse.ch/browse/signature/NyxarStealer ；X：https://x.com/abuse_ch/status/2110358543362646201
- **Symantec：Warden Stealer**：https://www.broadcom.com/support/security-center/protection-bulletin/warden-stealer ；X：https://x.com/threatintel/status/2110277128944304471
- **SentinelOne：BYOVD EDR-killer 市场**（ipurple 转介）：https://www.sentinelone.com/blog/bring-your-own-vulnerable-driver-how-edr-killing-became-an-industry/ ；X：https://x.com/ipurple/status/2110445176040693915
- **ANY.RUN：伪 AI 工具（Claude/ChatGPT 投毒）**：landing 自 2026-04 活跃；域名如 `claudecode[.]us[.]com`、`cladesktop-apps[.]com`、`openai-backup[.]one`、`claude-ai[.]us`；C2 `nucleflowers[.]xyz`。https://any.run/cybersecurity-blog/fake-ai-tools-us-companies/
- **eBPF rootkits（LinkPro/VoidLink）取证空白**（DFIR_Radar 转介）：https://andreafortuna.org/2026/10/14/ebpf-forensics-gap/ ；X：https://x.com/DFIR_Radar/status/2110355670079856731
- **ReliaQuest：AI agent 把一个暴露端点变成服务器接管**：https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/
- **Unit 42：第三方 VPN 导致的入侵噪声**：https://unit42.paloaltonetworks.com/noise-inside-network-third-party-risk/
- **VulnCheck：Integrity Tech（Flax Typhoon 相关）IoC 仍活跃**：https://www.vulncheck.com/blog/integrity-technology-group-advisory
- **ESET：Sandworm 与 UAC-0099 的 MythicRatatoskr（Yggdrasil C2，VB2026）**：X：https://x.com/ESETresearch/status/2110260614194975217
- **malwrhunterteam**：假 Ollama macOS 站点 `ollama-for-macos.github[.]io/Ollama_0.23.1.dmg`（X：https://x.com/malwrhunterteam/status/2110328081516998964）；YouTube 评论死投点解析器（频道 `UCi6eziCmEaPclr6EzeCtvyQ`，X：https://x.com/malwrhunterteam/status/2110484745813680557）；钓鱼链 `ojsdocument.blob.core.windows.net → my-document-101607.proposal-union-9173673.workers[.]dev`（X：https://x.com/malwrhunterteam/status/2110308027530412318）
- **vxunderground**：POS 恶意软件元数据（X：https://x.com/vxunderground/status/2110238348639883295）；CLOUDHAZE／UNC7072（Rust，X：https://x.com/vxunderground/status/2110222399241126337）
- **Malwarebytes：假 Calendly「Meta Careers」窃取 FB/Google 登录**：https://www.malwarebytes.com/blog/threat-intel/2026/10/fake-calendly-meta-careers-pages-steal-facebook-and-google-logins ；X：https://x.com/Dinosn/status/2110342243144049017
- **SANS ISC：DWG 文件里的孤儿 VBA**：https://isc.sans.edu/diary/33420 ；X：https://x.com/sans_isc/status/2110261964022935736
- **ProjectDiscovery：从员工侧泄露 AI 实验室 API key**：https://projectdiscovery.io/research/pwning-ai-labs-via-employees ；X：https://x.com/pdiscoveryio/status/2110387041590710506

### M-12. 供应链 / 事件（声称类标 UNCONFIRMED）
- **Ledger / CryptoBilis 间谍芯片**：Ledger 要求亚洲经销商暂停销售；称植入芯片能从屏幕读取助记词并经 LTE 外传；KimZetter 对部分技术细节提出质疑（UNCONFIRMED）。文章：https://www.bleepingcomputer.com/news/security/ledger-asks-sellers-across-asia-to-halt-sales-after-supply-chain-attack/ ；X：https://x.com/KimZetter/status/2110441837185863930；https://x.com/DailyDarkWeb/status/2110149334457336086
- **Meta GitHub 泄露**：约 1,500 人（多为美籍员工），攻击者用员工被盗凭据访问部分仓库，99% 为源码、1% 为误提交的个人数据。文章：https://www.securityweek.com/meta-says-hackers-took-code-personal-data-of-1500-in-github-breach/ ；X：https://x.com/DailyDarkWeb/status/2110148022420246559
- **Gamdom** 加密赌场全站下线：自动化服务器现「未授权连接」；FairGambling 称下线前约 2 小时有 >$2.3M 流出热钱包（是否被盗未定，UNCONFIRMED）。X：https://x.com/DailyDarkWeb/status/2110414679101087824
- **日本 Arcadia**（SpeeCAN RAIDEN／NET119／119RAIDEN）：最多约 313.6 万邮箱等暴露。X：https://x.com/DailyDarkWeb/status/2110327757142217099
- **Ride On Express**（Gin no Sara）：10-07 遭勒索，最多约 650 万条客户记录可能暴露。X：https://x.com/DailyDarkWeb/status/2110257631671750689
- **韩国 FSC**：确认 16 家金融机构近期遭数据泄露，约 10 万条客户数据（含居民登记号）。X：https://x.com/DailyDarkWeb/status/2110412285675995563
- **CenterPoint Energy**：德州登记 106.2 万人受影响（含 SSN／驾照）。X：https://x.com/DailyDarkWeb/status/2110213647859638408
- **Ahold Delhaize**：称「无证据数据被窃」，美国多家杂货网站仍受影响。X：https://x.com/DailyDarkWeb/status/2110150667864351013；厂商：https://newsroom.aholddelhaize.com/update-on-ahold-delhaizes-cybersecurity-incident/
- **OpenAI 录音器**：工程主管被控在高管会议室安装隐蔽录音设备。X：https://x.com/TheHackersNews/status/2110189921139085496；政府：https://www.justice.gov/opa/pr/saudi-national-arrested-installing-surreptitious-audio-recording-device-openai
- **Kaspersky**：10-14 大部分产品与 My Kaspersky 已恢复。X：https://x.com/kaspersky/status/2110384394221305858；支持页：http://support.kaspersky.com/faq/service-status
- **MI5 年度威胁通报**（SwitHak 转介）：X：https://x.com/SwitHak/status/2110245788202705194
- **Yandex 数据中心遇袭影响**（TrustedSec／LloydLabs 讨论）：X：https://x.com/TrustedSec/status/2110473967945343389；https://x.com/LloydLabs/status/2110507216830661034
- **UNCONFIRMED 地下兜售／声称**（DailyDarkWeb／intels_daily／FalconFeeds）：BNI 印尼银行、Interpol「参与者」数据、Geidea（MENA 支付）、Poland Citizen DB、Paraguay 警方 ~8.75M、Coinbase「14M」、Money Network ~1.04M、DRDO、NoName057(16) #OpFrance DDoS、以及 ThreatAtlas／FalconFeeds 的多起勒索受害者上架（Qilin／n0n／Beelzebub 等）。相关 X：https://x.com/DailyDarkWeb/status/2110424723473457233；https://x.com/ThreatAtlas/status/2110426121401483367；https://x.com/CyberPulse56/status/2110275485670441129；https://x.com/ISGofficial_/status/2110323050352881907


## 地址／IoC 汇总

> 以下原样抄自原帖／原文（保留 defang）；不要直接访问。各家完整列表见对应厂商页／仓库。

### PAN-OS CVE-2026-0322（PAN 公告，原样）
- IP：`66[.]42[.]72[.]14`、`208[.]83[.]239[.]114`、`149[.]248[.]47[.]234`

### Ivanti CVE-2026-104935（Previdian 蜜罐攻击 IP，原样）
- IP：`216.73.160[.]59`、`216.73.160[.]61`、`216.73.160[.]210`、`45.8.19[.]111`

### AhsayCBS 105133/105134（Huntress，原样）
- IP：`177.4.12[.]11`、`38.60.252[.]110`、`107.191.47[.]199`、`185.220.236[.]49`、`104.234.26[.]10`、`123.202.208[.]37`
- OSS 下载：`hxxp://imagefiles-backup.oss-ap-southeast-7.aliyuncs[.]com/javas/Office/win/{Taskgmr.ps1, edge.exe, msedge.exe, config.json, WinRing0x64.sys}`
- 矿池：`xmr.kryptex[.]network:8029`（`51.195.127[.]124`）user `krxYMRN97D/creativejs`
- SHA256：`05f69ae6b2b89c1c4dcf836bff032232f11bf0109f2b498e2345045d06139034`、`4dcb0202fe8b2d4d7b183764e38184cd6ed50132786cc7e7d1f7f4bce1dd6f3d`、`481728a7c9c4c02be07051d9c1958d902ea6397ebb8952ab83944818e3d25d21`

### Nextcloud/Collabora CVE-2026-110447（webshell 文件名，原样）
- `shrf4645.php`、`shxa35d0.php`、`shx5cf91.php`、`shxd33ce.php`、`shxf4645.php`、`shx13a86.php`、`shx56367.php`

### Microsoft PhaaS / Resecurity（原样）
- `docker.aidchildren[.]cc`、`docker.loveboy[.]xyz`、`install.loveboy[.]xyz`、`api2.peaceman[.]cc`、`ipapi2.peaceman[.]cc`、`bin2.peaceman[.]cc`、`log2.peaceloving[.]xyz`、`ossapi.haoeryu[.]top`、`jewishchoice[.]org`（伪造非营利）

### Unit 42 Casbaneiro（原样摘录）
- 域名：`n1.youconnectedssl[.]digital`、`updatehostingfree[.]top`、`euromasterx[.]com`、`xdrivewin[.]com`、`uixfilepdfview[.]top`、`arneighti[.]com`、`knowledgerknolle[.]com`、`learnflourishspace[.]com`、`zytherostudio[.]com`
- IP：`216.203.21[.]119`、`190.2.184[.]201`、`216.203.20[.]116`、`65.38.121[.]128`、`134.209.200[.]162`、`142.93.109[.]181`、`45.76.69[.]213`、`45.61.136[.]99`
- SHA256：`d180a1978cd547f8aa4c387f951c720f0b2ff9641a45a8153994a8f29cfdf610`、`6cdf132ee130b4cec889e39e06b07559fb4119c61a62d48c03cf357f66eb8900`、`c14c25792af4e1552b54b4fe0aca6e405ed052b4ba4af67a439bfdad5b3919ed`

### Unit 42 PEERSTITCH（原样摘录）
- IP：`45.32.41[.]202`、`198.199.122[.]22`、`23.240.77[.]233`、`47.18.167[.]159`
- URL：`hxxp[:]//23.240.77[.]233:8085/pM.js`、`hxxp[:]//47.18.167[.]159:8085/pM.js`
- SHA256（核心注入器）：`b9fb0b27ddd59b58d3ae53c7227298a3e0de1e6f868b9429ae21533bb9cd1e70`（完整 8 条见 X-M3）

### Forescout Lorem Ipsum / Axolotl（原样摘录）
- 死投点：`letsdiskuss[.]com/user/{lindawilliams51453, dhuahsd12d2752, joeblack1673}`、`digitalpoint[.]com`
- C2：`scriptedgeapp[.]com`、`transferrootway[.]com`、`updaterdeskarc[.]com`、`signinbyte[.]com`、`bloganimals[.]com`
- SHA256：`13a3fa500e91e35a34f71e0e88f07a5b3dd8251e9b423188030e31dbd8eaf603`

### Huntress WatchGuard / ChatGPT GPT（原样）
- `watchguard-vpn[.]net`（80.249.132[.]140）、`watchguard-ssl[.]online`（158.94.209[.]19）
- `gptverification[.]com`、`sites[.]google[.]com/view/antibot172881`、`sites[.]google[.]com/view/antibot381122`、`hxxp://1614733393/...ISOSimple[.]msi`（=`96.62.224[.]81`）、`45.140.205[.]28`

### KGB RAT / Nyxar / 其它（原样）
- KGB RAT C2：`104[.]248[.]130[.]195`、`2[.]59[.]134[.]215:443`
- Nyxar Stealer：`nyxar[.]cc`、`nyxar[.]lol`、`nyxarstealer[.]lol`、`nyxarst[.]lol`、`polnet[.]lol`
- ANY.RUN 伪 AI：`claudecode[.]us[.]com`、`cladesktop-apps[.]com`、`openai-backup[.]one`、`nucleflowers[.]xyz`
- 假 Ollama：`ollama-for-macos.github[.]io/Ollama_0.23.1.dmg`

### 误报澄清
- vxunderground 先前提到的 "goopdate" 哈希 `91fc3bf4caf5d6014b1f344b865ab1e063d6a7e9acf5705ad7ced4df91620771` 经确认为**良性 Google Update DLL**（巧合，非 IoC），请勿加入封锁名单。
- @Dave_Joe_9377 称 Zammad CVE-2026-102489/102490 已进 KEV：**核对 KEV 无 Zammad 条目，未采纳（未验证）**。
- @pidoras3458 的「P7 DarkSword」仓库 `github.com/latte3458/p7-darksword-rce` 可疑、疑似诱饵，**不建议下载／运行**，仅作警示。

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

- X A（relevancy）：`(CVE OR POC OR exploit OR 0day OR "zero-day") -is:retweet lang:en` + 时间窗；去噪版 `"CVE-2026" (exploited OR "in the wild" OR PoC OR patch OR advisory OR KEV) -is:retweet -is:reply -"Patch Tuesday"`
  - https://x.com/search?q=%22CVE-2026%22%20(exploited%20OR%20%22in%20the%20wild%22%20OR%20PoC%20OR%20advisory%20OR%20KEV)%20-is%3Aretweet&f=live
- X B：`url:github.com (C2 OR "red team" OR nuclei OR Sliver OR Mythic OR BOF OR EDR OR YARA OR Sigma OR DFIR OR PoC)`
  - https://x.com/search?q=url%3Agithub.com%20(%22red%20team%22%20OR%20BOF%20OR%20EDR%20OR%20PoC%20OR%20nuclei)&f=live
- X C：`(malware OR stealer OR loader OR backdoor OR botnet OR ransomware) (analysis OR campaign OR IOCs) -is:retweet -from:ThreatAtlas -from:FalconFeedsio`
  - https://x.com/search?q=(malware%20OR%20stealer%20OR%20loader%20OR%20ransomware)%20(analysis%20OR%20campaign%20OR%20IOCs)%20-is%3Aretweet&f=live
- X 定向：Cisco SEG／76519；PAN-OS／0322；Ahsay／105133／105134；Nextcloud／Collabora／110447；Ivanti／104935；Patch Tuesday／96951／103572／70111；Vghost／74580；curl／92392；SiteGuard／106931；GitLab／97229；Splunk／76268；Adobe／Fortinet／SAP；PhaaS／YAM Store；PEERSTITCH；UAT-6275；DPRK laptop farm；Ledger／Meta／Gamdom
- X LWiS：优先批 48 账号（4 时段分段＋翻页）＋扩展批 30 账号（3 段＋翻页）＋其余成员 9 批 `from:` + 时间窗（recency）
- LWiS X List：https://x.com/i/lists/1239330068461244424
- KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- Cisco SEG：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp
- PAN-OS：https://security.paloaltonetworks.com/CVE-2026-0322
- Huntress Ahsay：https://www.huntress.com/blog/ahsaycbs-flaws-exploit
- Collabora GHSA：https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh
- Microsoft PhaaS：https://www.microsoft.com/en-us/security/blog/2026/10/14/the-hidden-network-inside-the-phishing-infrastructure-ecosystem-powering-global-cybercrime/
- Unit 42 PEERSTITCH：https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/
- Talos UAT-6275：https://blog.talosintelligence.com/break-the-silence-kazakhstan-nexus-uat-6275-targets-cis-government-organizations/
- AA26-281A：https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-281a
- Risky：https://risky.biz/
- tl;dr：https://tldrsec.com/
