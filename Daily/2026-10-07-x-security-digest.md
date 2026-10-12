# X 安全情报晚报 · 2026-10-07

> 搜集窗口：圣地亚哥时间 **2026-10-06 20:00 至 2026-10-07 ~20:30**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报。**
> **X 采集方式（本轮变更）**：使用 Grok Bot 自带的 X 只读公共数据接口（搜索与按 id 取帖，含 t.co 展开字段），**本轮未开浏览器，未检查 @seogoogle4 浏览器登录状态**。覆盖：A／B／C 三组搜索均为完整 24h 窗口（按相关度取前 25，噪声过滤后保留）；LWiS List 以 500 名成员备份分 10 批 `from:` 查询覆盖完整 24h（共返回 99 帖）。合并 **53** 条新帖（A17／B7／C7／LWiS22；另 1 条 vx-underground 解封帖与昨日 seen_ids 重叠，不重复计入）。全程只读，未发帖／回复／点赞／转推／收藏／追踪。
> **公开备援 PRIMARY**：`/workspace/security-watch-public-backup-2026-10-07.json`＋`/workspace/tools-news-pulse-2026-10-07.json`＋`/workspace/enrich-2026-10-07/`＋`/workspace/_kev_buckets_2026-10-07.json`。CISA KEV catalogVersion **2026.10.04**／**1734** 条，**Δ0**（与 10-06 文件逐字节相同，**连续第 3 天未更新**；10-06／10-07「CISA adds…」URL 均 404）。
> **due_today：Citrix CVE-2026-88779（今天到期）**；**newly_overdue：无**；**upcoming 7 天：无**（明天起 KEV 全库均已过期）；**仍逾期高信号 26 条**。
> 抓取备注：Trend Micro 原 RSS 404（改 feedburner）；CISA alerts 列表 404；SonicWall SNWLID-2026-0017 页尚未上线；Proofpoint threat-insight、ZeroHour、CERT-EU PDF 未抓取；SolarWinds ARM 原文被 Cloudflare 挡（仅凭 X 卡片标题）。
> 规则：每条含完整 https URL；分列 X 原帖／GitHub·PoC 仓库／厂商公告／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤；泄露／入侵声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【新起在野 · 未进 KEV】Atlassian CVE-2026-21589**：公开 PoC 后约 2 小时 Previdian 蜜罐即见利用，X 一手帖给出 3 个攻击源 IP；nuclei 模板已上线。
  X 原帖：https://x.com/PrevidianCyber/status/2107731944616153480
  文章：https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-atlassian-flaw-after-public-poc-release/
- **【今日 KEV 到期 · Citrix CVE-2026-88779】** 须升 14.1-73.41／13.1-64.28（9 月补丁不覆盖）；SOCRadar 同日揭露针对 88771 的中文自动化攻击框架「NetScaler C2」，带 C2 IP 与 6 个哈希。
  厂商：https://support.citrix.com/external/article/CTX697174
  X 原帖：https://x.com/socradar/status/2107848739394109508
- **【Zammad 102489 PoC 公开】** Horizon3 发布技术分析与 PoC 仓库；Zammad 官方 advisory 称 7.0+ 实际不受影响、102490 提权仍在修复。
  X 原帖：https://x.com/Horizon3Attack/status/2107835809747603939
  厂商：https://zammad.com/en/advisories/cve-2026-102489-cve-2026-102490
- **【Cisco 10-07 批量 14 条 · 8 条 Critical】** NX-API／MPLS OAM／NGOAM 未认证 root RCE（9.8）、License On-Prem hardening（10.0）等，均未见利用、无 workaround。
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-napi-rce-r2shwu2j
- **【Splunk SVD-2026-1001】** CVE-2026-76268 Patroni REST API 未认证命令执行（9.8）。
  厂商：https://advisory.splunk.com/advisories/SVD-2026-1001
- **【APT · 有 IoC】CrowdStrike：未归因行为者用开源 AI 渗透工具 ARTEX 打韩国金融机构**（WSJ 称 7 家、6.8 万人）。
  厂商：https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/
  X 原帖：https://x.com/DFIR_Radar/status/2107924892415111628
- **【Malware · 有 IoC】Lumen PoeLLM**：用 GitHub 诗歌隐藏 C2，感染 3,400+ 暴露的 AI 服务器挖矿。
  厂商：https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware
- **【Malware · 有 IoC】Huntress：Power BI 钓鱼投放 rogue ScreenConnect**；Barricade：BLACKNET-00 勒索实为 XOR 可免费解密。
  厂商：https://www.huntress.com/blog/screenconnect-power-bi
  文章：https://barricadecyber.com/blacknet-00-ransomware/
- **【工具】** emp3r0r C2 v4.23.0 发布；dreadnode ScopeBench 正式发布；核心工具（Sliver／nuclei／Mythic 等）无新版。
  GitHub：https://github.com/jm33-m0/emp3r0r/releases/tag/v4.23.0
- **【合并统计】** X **53**（A17／B7／C7／LWiS22）；seen_ids **2370→2423**；Risky 仍 RBNEWS618、tl;dr 仍 #348；报告 `/home/box/workspace/security-watch/reports/2026-10-07-x-security-digest.md`

## CVE / POC / 漏洞

### X-1. 【X 交叉 · 新起在野 · 未进 CISA KEV】Atlassian CVE-2026-21589 已被利用（公开 PoC 后约 2 小时）
昨日报告的 Atlassian 多产品未认证任意文件读取（CVSS4 9.3）今日升级：BleepingComputer 报道 Previdian 蜜罐网络在 watchTowr 技术文发布后数小时即观测到利用；watchTowr 指出在集成 Crowd 的 Jira 部署中可读取 `WEB-INF/classes/crowd.properties` 明文凭据并经 Crowd API 建管理员。ProjectDiscovery 已发布 nuclei 检测模板。**CISA KEV 仍未收录**（2026.10.04 版）。防御：立即升级至厂商修复版本（见昨日报告）；限制 Crowd 可达 IP 白名单；轮换 Crowd 应用凭据；检查 web 日志中针对插件资源端点的 `::` 路径穿越请求。
地址：
- X 原帖（Previdian 蜜罐 IoC，一手）：https://x.com/PrevidianCyber/status/2107731944616153480
- X 原帖（Previdian 首次观测，10-06 18:58 UTC-3，窗口前）：https://x.com/PrevidianCyber/status/2107591310391824699
- X 原帖（在野转述）：https://x.com/V0iD_0daY/status/2107837799969808841
- X 原帖（nuclei 模板）：https://x.com/DhiyaneshDK/status/2107730985483944432
- X 原帖（ProjectDiscovery）：https://x.com/pdiscoveryio/status/2107930767125016866
- X 原帖（@cyb3rops 转 watchTowr）：https://x.com/cyb3rops/status/2107722894201573451
- GitHub（nuclei 检测模板）：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-21589.yaml
- 厂商：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-21589
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-atlassian-flaw-after-public-poc-release/
- 文章 watchTowr：https://labs.watchtowr.com/you-wont-hear-about-these-even-in-myths-atlassian-jira-confluence-and-more-pre-auth-arbitrary-file-read-cve-2026-21589/
- 文章 Help Net Security：https://www.helpnetsecurity.com/2026/10/07/exploitation-critical-atlassian-flaw-cve-2026-21589/
- GitHub（watchTowr 检测仓库）：https://github.com/watchtowrlabs/watchTowr-vs-Atlassian-CVE-2026-21589
IoC：Previdian 蜜罐攻击源 IP `38.60.157[.]86`／`146.70.187[.]234`／`159.26.119[.]225`（X 原帖与 BleepingComputer 一致）；狩猎文件路径 `WEB-INF/classes/crowd.properties`。

### X-2. 【X 交叉 · 在野 · 已逾期】Zammad CVE-2026-102489：Horizon3 发布深度分析与公开 PoC
Horizon3（Zach Hanley，10-07）复现 102489：未认证 WebSocket 请求触发错误回显，泄露所有已登录用户会话 cookie；再借管理员会话经包安装端点写文件、覆盖密码重置邮件模板实现以 zammad 用户执行代码；102490 提权到 root，Horizon3 暂不公开细节。DIVD 已发布 IoC 脚本（扫描错误日志中的泄露 cookie）。**另：今日首次发现 Zammad 官方 advisory（页面日期 10-05）**——称 102489「7.0 及以上实际不受影响」，仅已 EOL 的 6.5 及更早可利用；102490 为本地提权、与 packager.io 已确认漏洞相关、**修复中**（与 Horizon3「仍未修补」一致）。NVD 10-07 已把该 advisory 加为引用。防御：6.5 及更早立即升级（至 7.2.1）；运行 DIVD IoC 脚本；查 `/ws` 端点异常单次请求、应用目录新文件、被改的 ERB 模板；一旦命中按全面失陷处理。
地址：
- X 原帖（Horizon3）：https://x.com/Horizon3Attack/status/2107835809747603939
- X 原帖（DFIR Radar 摘要）：https://x.com/DFIR_Radar/status/2107773855985181057
- X 原帖（Dinosn）：https://x.com/Dinosn/status/2107832707480961038
- GitHub／PoC 仓库（Horizon3，仅记录不转载）：https://github.com/horizon3ai/CVE-2026-102489
- 文章 Horizon3：https://horizon3.ai/attack-research/disclosures/cve-2026-102489-zammad-session-leak-rce/
- DIVD 案件：https://csirt.divd.nl/cases/DIVD-2026-00015/
- 厂商 advisory：https://zammad.com/en/advisories/cve-2026-102489-cve-2026-102490
- 厂商 7.2.1：https://zammad.com/en/product/releases/7-2-1
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-102489
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-102489
IoC：狩猎特征为 `/ws` WebSocket 端点与错误日志中的 cookie 片段；未见公开 IP／哈希。

### X-3. 【X 交叉 · 今日 KEV 到期】Citrix NetScaler CVE-2026-88779（SAML）＋ SOCRadar 揭露 88771 自动化 C2 框架（有 IoC）
88779 联邦期限即今天 10-07；X 上多帖（@vuln_tracker、@isectech_、@HC_McGlasson 等）一致提醒：9 月为 88771／88772 打的版本不覆盖 88779，须升至 14.1-73.41／13.1-64.28。**新**：SOCRadar 10-07 披露一个针对 CVE-2026-88771（ns.log 日志注入）的自动化攻击框架「NetScaler C2」：FOFA 批量侦察→指纹→在 11 个 HTTP 端点注入→拉取轻量 C2 agent（DNS OOB 备援），每 30 分钟循环；代码注释为简体中文。SOCRadar 另称 10-02 起已打 88771 补丁的 SAML 设备上仍有命令执行。防御：升级到 88779 修复版；在 ns.log 归档中搜下列触发字符串与 C2 IP；查 `/tmp/.nsagent` 等隐藏文件；Citrix 称升级不清除失陷痕迹，疑似失陷应重建实例。
地址：
- X 原帖（SOCRadar）：https://x.com/socradar/status/2107848739394109508
- X 原帖（VulnTracker）：https://x.com/vuln_tracker/status/2107788025266627069
- X 原帖（iSECTECH）：https://x.com/isectech_/status/2107776781730115676
- X 原帖（McGlasson）：https://x.com/HC_McGlasson/status/2107878295542857928
- 厂商 CTX697174：https://support.citrix.com/external/article/CTX697174
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-88779
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-88779
- 文章 SOCRadar（X 外链 hubs.la 展开）：https://socradar.io/blog/netscaler-c2-cve-2026-88771-exploitation/
- 文章 VulnTracker：http://vulntracker.io/cves/CVE-2026-88779
IoC：见汇总「SOCRadar NetScaler C2」。

### X-4. 【X · 新 Critical】Splunk Enterprise SVD-2026-1001（17 个漏洞，最高 CVE-2026-76268 未认证命令执行）
Splunk 10-07 发布：搜索头集群成员上的 Patroni REST API 缺少认证，网络可达的未认证者可执行系统命令（CVE-2026-76268，Critical）。修复版本 10.4.3／10.2.7／10.0.10／9.4.15；CVE-2026-76264／76265／76272／76280 需额外步骤。未见在野利用报告。防御：升级；网络上隔离 Patroni REST API。
地址：
- X 原帖：https://x.com/Orbitaley/status/2107972847259852948
- 厂商：https://advisory.splunk.com/advisories/SVD-2026-1001
- NVD（按 CVE 构造）：https://nvd.nist.gov/vuln/detail/CVE-2026-76268
- 文章（X 外链展开）：https://orbitaley.com/news/splunk-fixes-a-critical-splunk-enterprise-flaw-that-allows-unauthenticated-q5o3q?lang=en&src=x
IoC：未见公开 IoC。

### X-5. 【X · 探测中】Rejetto HFS CVE-2026-61500（会话伪造→RCE，非 CISA KEV）
HFS 3.0.0–3.2.0 以 `Math.random()` 生成会话签名密钥并在登录中泄露同一 PRNG 输出，可伪造管理员会话再经 `server_code` 执行代码（CVSS4 9.3）。7 月 3.2.1 已修；Horizon3 9-30 公开细节后，VulnCheck 自 10-01 起在蜜罐观测到来自中国电信 IP 的探测并纳入 VulnCheck KEV；报道称尚无确认的成功入侵。防御：升级 3.2.1+，作废会话、轮换管理员凭据，检查 server_code 配置。
地址：
- X 原帖：https://x.com/Npj8448/status/2107723736371859595
- NVD（按 CVE 构造）：https://nvd.nist.gov/vuln/detail/CVE-2026-61500
- 文章 The Hacker News：https://thehackernews.com/2026/10/attackers-target-rejetto-hfs-flaw-that.html
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/rejetto-hfs-servers-now-actively-scanned-for-critical-rce-flaw/
IoC：报道提到单一中国电信来源 IP，但未公开具体地址，未见公开 IoC。

### X-6. 【X · LWiS】SolarWinds Access Rights Manager 三个未认证 RCE 技术细节公开（Armadin）
@AndrewOliveau、@h4wkst3r 转发 Armadin 红队 @mhskai2017 的三篇系列：SolarWinds ARM 未认证 RCE，可致整个 AD 域失陷（负责任披露，part 1）。厂商公告编号帖中未给出，未核对。防御：确认 ARM 版本已更新到厂商修复版，限制 ARM 服务暴露面。
地址：
- X 原帖：https://x.com/AndrewOliveau/status/2107895720749744300
- X 原帖：https://x.com/h4wkst3r/status/2107892192916148426
- 文章 Armadin：https://www.armadin.com/blog-posts/unauthenticated-rce-in-solarwinds-access-rights-manager-responsible-disclosure-part-1
IoC：未见公开 IoC。

### X-7. 【X · LWiS】LMCache CVE-2026-105192（未认证 RCE，**无补丁**）
JFrog 披露：LMCache 0.3.9–0.5.5（含 0.5.6 RC）多进程服务器的 ZeroMQ 套接字无认证并用 pickle 反序列化，绑定可路由地址时可远程执行代码（官方容器以 root 运行）。无修复版本。防御：不要把多进程服务器绑在可路由地址，端口仅限本机／隔离网络。
地址：
- X 原帖：https://x.com/Dinosn/status/2107884938465014243
- NVD（按 CVE 构造）：https://nvd.nist.gov/vuln/detail/CVE-2026-105192
- 文章 The Hacker News：https://thehackernews.com/2026/10/unpatched-critical-lmcache-flaw-lets.html
IoC：未见公开 IoC。

### X-8. 【X · 研究公开】其他 PoC／研究（仅记录，不转载利用细节）
- WordPress＋ImageMagick＋libheif 认证上传 RCE 链（FORTBRIDGE，涉及 CVE-2026-32740，限定 Ubuntu／Debian 特定版本栈）：X https://x.com/ksg93rd/status/2107807125569163350 ／ 文章 https://fortbridge.co.uk/research/wordpress-libheif-rce ／ GitHub https://github.com/FORTBRIDGE-UK/libheif-unci-wordpress-rce
- Home Assistant Green：去年 Pwn2Own 的 go2shell 链公开（SSDP）：X https://x.com/_mccaulay/status/2107959435561673136 ／ 文章 https://mccaulay.co.uk/go2shell-rooting-home-assistant-through-ssdp/
- MySQL Community Server mysqlbinlog 客户端文件写（@abraxas_null 自称「今日第 3 个 0day」，**可信度未验证**）：X https://x.com/abraxas_null/status/2107608307615850899 ／ 文章 https://abraxaslabs.tech/research/mysql-mysqlbinlog-raw-path ／ GitHub https://github.com/abraxas/mysql-mysqlbinlog-raw-path
- macOS 沙箱用户→root 提权预告（@theevilbit，无细节）：https://x.com/theevilbit/status/2107767534866821614
- FortiMail CVE-2026-104286 X 上持续提醒（修复 8.0.2／7.6.7／7.4.9，查可疑归档账户）：https://x.com/IamChrisFamous/status/2107882993255579826 ；FBI／USSS 联合通告 FortiBleed 凭据导致防火墙锁定（报道称 SOCRadar 核实 86,644 台设备）：X https://x.com/Dinosn/status/2107788151205073352 ／ 文章 https://www.theregister.com/security/2026/10/07/fortibleed-still-a-bleeding-nuisance-as-fbi-confirms-ongoing-attacks/5301585
- Oracle EBS CVE-2026-46817「在野」帖为旧闻转发（KEV 2026-07-15 已收录，链接为 6 月文章）：X https://x.com/blueteamsec1/status/2107895351135043725 ／ 文章 https://thehackernews.com/2026/06/oracle-e-business-suite-flaw-cve-2026.html
IoC：以上均未见公开 IoC。

### P-1. 【厂商 · Cisco 10-07 批量发布 14 条（Critical 8／High 1／Medium 5）】
10-07 13:00（UTC-3）发布；全部「PSIRT 未知恶意利用」、均未入 KEV、均无 workaround；4 条 hardening 合集为内部审查（含前沿 AI 模型）发现。Finesse SSRF 修复尚未发布但已有公开披露。防御：优先修补暴露 NX-API、启用 MPLS OAM／NGOAM 的 Nexus 3000／9000，以及 License On-Prem。
- Critical · License On-Prem Hardening（CVSS 10.0，CVE-2026-76480／76482／76483／76484）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ssm-Ph77wdhf
- Critical · License On-Prem 多漏洞（9.1，CVE-2026-20328／76437／76452／76454）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ssm-access-nttb2dhE
- Critical · APIC Hardening（9.8，CVE-2026-76498／76499／76500）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-apic-UOXWtfh
- Critical · NX-OS Hardening（9.8，CVE-2026-76453／76455～76459）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR
- Critical · Meraki Hardening（9.6，CVE-2026-76463／76464／76467～76470／76472）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH
- Critical · NX-OS NX-API 未认证 root RCE（9.8，CVE-2026-76471）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-napi-rce-r2shwu2j
- Critical · Nexus 3000／9000 MPLS OAM RCE（9.8，CVE-2026-76465）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-moam-rce-uBTzYV7
- Critical · Nexus 3000／9000 NGOAM RCE（9.8，CVE-2026-76485／76486／76501）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ngoam-rce-LWKQ4BU
- High · Finesse 未认证 SSRF（7.2，CVE-2026-20362，修复待发）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-finesse-ssrf-mmSuyugS
- Medium · APIC API 命令注入（CVE-2026-20321）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apic-cmdinj-L6VR4E7
- Medium · APIC 未授权文件访问（CVE-2026-76488）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-apic-info-priv-enAdB5vD
- Medium · ACI 模式 EPG contract 绕过（CVE-2026-20038）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-aci-epgcbp-SfDU7NLf
- Medium · NX-OS 控制面 DoS（CVE-2026-20173）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nxos-nscpdos-SnderkC7
- Medium · NX-OS Python 沙箱逃逸（CVE-2026-20032）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nxos-mppe-dhKZAFgb
- 预告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-fBn58ELx
- X 原帖：本窗口 X 未采到 Cisco 批量公告相关帖，不编造
IoC：未见公开 IoC。

### P-2. 【NVD 窗口内其他高分新 CVE（343 条中摘取，均非 KEV）】
- SonicWall SMA1000 CVE-2026-102255（CVSS 10.0，未认证 SSRF；厂商页尚未上线，仅 NVD）：https://nvd.nist.gov/vuln/detail/CVE-2026-102255 ／ 厂商（未上线）https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0017 ；X 上 @Digital_Warfare 播客提及：https://x.com/Digital_Warfare/status/2107859925678334106
- Veeam B&R CVE-2025-64393（9.4，Backup Viewer 角色以 SYSTEM 执行代码）：https://nvd.nist.gov/vuln/detail/CVE-2025-64393 ／ 厂商 https://www.veeam.com/KB4934
- VMware Workstation／Fusion CVE-2026-59346（9.3，VMXNET3 虚拟机逃逸，修复 26H1u1）：https://nvd.nist.gov/vuln/detail/CVE-2026-59346 ／ 厂商 https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/security-advisories/0/38288
- IBM Langflow OSS CVE-2026-93674／104334（9.8 RCE）：https://nvd.nist.gov/vuln/detail/CVE-2026-93674 ／ 厂商 https://www.ibm.com/support/pages/node/7290694
- Movable Type CVE-2026-96408（9.3，未认证代码注入，MT 9.3.0 修复）：https://nvd.nist.gov/vuln/detail/CVE-2026-96408 ／ 厂商 https://movabletype.org/news/2026/10/mt-930-released.html
- Apache Jackrabbit WebDAV CVE-2026-92414（9.3 会话固定）：https://nvd.nist.gov/vuln/detail/CVE-2026-92414 ／ 公告 https://lists.apache.org/thread.html/gmbsmrs2lycl9nld7rd0h1r1fc4t75qr
IoC：未见公开 IoC（厂商页多未逐一抓取）。

### P-3. 【跟踪项状态】
- Fortinet FG-IR-26-175（CVE-2026-104286，逾期）：10-07 更新仅为 FortiMail Cloud 修复澄清（10-05 已升级，Cloud 客户无需操作）；修复版本与 IoC 不变：https://fortiguard.fortinet.com/psirt/FG-IR-26-175
- MSRC：10-07 01:51Z「October 2026 Early Security Updates」仅第三方组件（Azure Linux 类）206 条修订，Exploited:Yes 为 0；10 月 Patch Tuesday 为 10-13：https://msrc.microsoft.com/update-guide
- Palo Alto（最新仍 10-02 CVE-2026-0250）：https://security.paloaltonetworks.com/ ；Ivanti 最新 09-08；Fortinet 无新 IR。
- CISA：无新 CSA／ICS（最新仍 10-06 ICSA-26-279-01～06）：https://www.cisa.gov/news-events/ics-advisories
- Talos 漏洞汇总（Adobe／macOS／Foxit／Windows，均已修复）：https://blog.talosintelligence.com/microsoft-adobe-apple-and-foxit-vulnerabilities/

### P-4. 【仍逾期高信号 26 条】
Citrix 88771／88772、Apple 86950、Check Point 85102／93616、Arista 93952、F5 94127、JFrog 42016／42018、Zyxel 7273、Microsoft 81963／85880／65660、Google 87491／85046／58704、Cisco 76460／76504、Acronis 87886、WSO2 5430、Adobe 71362、MikroTik 67279、WordPress 87902、Fortinet 104286、Zammad 102489／102490。明天起 Citrix 88779 也将转入逾期，KEV 全库 1734 条均过期。
- KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

## 工具与 GitHub 发布

### 1. emp3r0r C2 v4.23.0（Go 后渗透框架，载荷瘦身至约 11MB／PIC 约 5MB）
作者 @jm33_m0 称瘦身后仍保留 P2P mesh、Starlark 引擎、BOF loader，Linux／Windows 均可。GitHub release v4.23.0 发布于 10-06 20:44（UTC-3），在窗口内。防御向：Go 编写的 C2 内存占用变小，EDR 内存特征需更新。
- X 原帖：https://x.com/jm33_m0/status/2107624383892328617
- GitHub release：https://github.com/jm33-m0/emp3r0r/releases/tag/v4.23.0

### 2. dreadnode：ScopeBench 正式发布（Offensive AI Con）＋ DreadGOAD Console
ScopeBench 评估攻击型 agent 是否越出授权范围；DreadGOAD 新增 agentic Web UI 部署管理 AD 靶场。
- X 原帖（ScopeBench）：https://x.com/dreadnode/status/2107881942373052755
- X 原帖（DreadGOAD Console）：https://x.com/dreadnode/status/2107867296341585959
- 视频：https://www.youtube.com/watch?v=7OmCifoEWsU

### 3. kiosk-mode-breakout（kiosk 模式逃逸技巧集）
- X 原帖：https://x.com/r1cksec/status/2107898560809250884
- GitHub：https://github.com/ikarus23/kiosk-mode-breakout

### 4. AI 渗透／红队工具与清单
- VulnHunter（Hunt→Fix→Verify 循环）：X https://x.com/EsGeeks/status/2107849268186988905 ／ GitHub https://github.com/nealbridges/VulnHunter
- RedAudit（加固与渗透范围梳理）：X https://x.com/EsGeeks/status/2107920925354086475 ／ GitHub https://github.com/dorinbadea/RedAudit
- automated-pentest-list（自动更新的自动化渗透项目清单）：X https://x.com/schiste/status/2107828581539967325 ／ GitHub https://github.com/schiste/automated-pentest-list
- 攻击 AI agent 的开源仓库合集（promptfoo、garak 等）：X https://x.com/konig0000/status/2107681656589173025 ／ GitHub https://github.com/NVIDIA/garak
- authsec（agent 凭据代理）：X https://x.com/asifalis/status/2107960897159282768 ／ GitHub https://github.com/authsec-ai/authsec
- stackd 新增可选原生网络（@rad9800 用于观察 agent 在 AWS 沙箱的行为）：X https://x.com/rad9800/status/2107916710745604443

### 5. 紫队检测研究（@ipurple）
- Console Named Pipe 进程注入的检测策略（Sysmon 1／17／18／3）：X https://x.com/ipurple/status/2107903569936445928
- 用微软签名 WerEnc.dll 加密 implant：X https://x.com/ipurple/status/2107955057169756531 ／ 文章 https://ipurple.team/2026/09/21/dump-encoding-library/

### 6. 其他
- Cobalt Strike 推出 CSCO II 培训（UDRL、Sleep Mask、Beacon Gate、UDC2）：X https://x.com/_CobaltStrike/status/2107907627388744146 ／ 文章 https://www.cobaltstrike.com/blog/cobalt-strike-certified-operator-training-2
- blackmagick.io 新增技术 BM-T3008 STUN Field Tasking 与 DragonForce 分析：X https://x.com/Teach2Breach/status/2107909331694010862 ／ 站点 https://blackmagick.io

### 7. 核心工具无新版
Sliver v1.7.8（https://github.com/BishopFox/sliver/releases/tag/v1.7.8）、nuclei v3.11.1（https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1）、nuclei-templates v10.5.0（https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.5.0，新增 CVE-2026-21589 模板已在 main 分支）、Mythic v3.4.0.5、Impacket 0.13.1、NetExec v1.5.1；Havoc 无 release（最后 commit 2025-12-18）。

## APT / Malware 分析

### X-1. 【CrowdStrike · 有 IoC】疑似讲中文的未归因行为者用开源 agentic 渗透工具 ARTEX 攻击韩国金融机构
CrowdStrike 10-07：9 月底至 10 月初，行为者用中国开发的开源 AI 渗透框架 ARTEX（DeepSeek v4.1-flash 为主，辅以 GLM-5.3、Grok 4.6，经 `xcai[.]pro` 代理）攻击韩国金融机构并外传数据；暴露的开放目录含 Claude Code 会话历史与配置。WSJ 报道首尔官方称至少 7 家金融机构、6.8 万人数据被窃；AhnLab 称全球约 600 个 IP 托管 ARTEX 实例（不等于都是攻击者）。防御：封禁下列 IP，金融机构狩猎来自代理 IP 的入站连接，Web 日志查 ARTEX 字符串。
- X 原帖：https://x.com/DFIR_Radar/status/2107924892415111628
- 厂商 CrowdStrike：https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/
- 文章 WSJ：https://wsj.com/world/asia/hackers-use-chinese-ai-tool-to-hit-south-korean-banks-exposing-new-risk-5d4d3885
- 文章 RuntimeWire（AhnLab 600 IP）：https://runtimewire.com/article/south-korea-bank-breaches-artex-ai-probe
- IoC：见汇总「CrowdStrike ARTEX」

### X-2. 【Lumen Black Lotus Labs · 有 IoC】PoeLLM（Canto Incognito）：用 GitHub 上的诗歌隐藏 C2，感染 3,400+ 暴露的 AI 服务器挖矿
自 2026-04 活跃，打 LiteLLM、Ollama、Gotenberg、Gitea，并见 Ivanti Sentry 尝试；被控主机转为扫描器（端口 3000／4000）并尝试 CVE-2026-42271（LiteLLM，已在 KEV）。ELF 名 `libgcrypt`，含远程 shell、XMRig 等矿工。BLL 中等置信度认为行为者讲意大利语。防御：不要把 LiteLLM／Ollama 等直接暴露公网；补 42271；封禁下列 C2。
- X 原帖：https://x.com/Dinosn/status/2107853481881076032
- 厂商 Lumen：https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware
- 文章 BleepingComputer：https://www.bleepingcomputer.com/news/security/poellm-malware-infects-exposed-ai-servers-in-cryptomining-attacks/
- 文章 The Hacker News：https://thehackernews.com/2026/10/poellm-malware-infects-3400-servers-to.html
- KEV（CVE-2026-42271）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-42271
- IoC：见汇总「Lumen PoeLLM」

### X-3. 【Barricade Cyber · 有 IoC】BLACKNET-00 勒索：号称 RSA-2048＋AES-256，实为可逆的重复密钥 XOR，可免费解密
该团伙（亦称 Infrastructure Destruction Squad）9 月起大量声称攻击政府、军队、银行、电厂，多数经核查站不住；10-01 起兜售 2017 年 Apache Struts 漏洞利用，其余多靠默认口令、开放 SNMP 与路由器管理口。另有 TRK25 SCADA 工具（多为装饰功能）。受害方：保留加密文件与勒索信，勿付款。
- X 原帖：https://x.com/bcs_erictaylor/status/2107848673648685135
- 文章 Barricade Cyber（X 外链展开）：https://barricadecyber.com/blacknet-00-ransomware/
- IoC：见汇总「BLACKNET-00」

### X-4. 【vx-underground · 有 IoC · 未验证】Telegram 插件伪装的 Android 间谍软件
@vxunderground 收到 Telegram 私信线索（`t(.)me/Exterav` 推荐的俄语「插件」），解码后为下载器，需特定 UA 和 `X-LD-Code` 头才下发 Android 载荷，作者称 VT 未见。**个人分析，未经厂商验证**。
- X 原帖：https://x.com/vxunderground/status/2107647082857206196
- IoC：见汇总「vx-underground Telegram 插件」

### X-5. 【CERT-UA】UAC-0277：100+ 被黑网站伪造 Cloudflare 验证（ClickFix）投放 LunexStealer
9 月观测；用 EtherHiding 从 Polygon／以太坊智能合约取配置；诱导用户执行命令下载 MSI。防御：拦截 ClickFix 剪贴板执行、监控 msiexec 远程安装。
- X 原帖：https://x.com/Dinosn/status/2107756084882780364
- 文章 The Hacker News：https://thehackernews.com/2026/10/100-compromised-websites-use-fake.html
- 文章 Security Affairs：https://securityaffairs.com/200537/hacking/cert-ua-fake-cloudflare-checks-deliver-lunexstealer-malware.html
- IoC：转载文中未见具体指标；CERT-UA 原文未核对，未见公开 IoC。

### X-6. 其他事件（多为声称／报道，标注可信度）
- IDC Frontier（软银子公司）宣布遭勒索攻击，托管服务受影响（@SwitHak）：https://x.com/SwitHak/status/2107873424995496258
- 「EndZone」勒索团伙向 vx-underground 自述借 ISP 客户管理门户越权（IDOR）入侵 Momentum Telecom、停用 10 万+ 调制解调器（**UNCONFIRMED／自述**）：https://x.com/vxunderground/status/2107689092553015772
- 丹麦 PET 称俄罗斯已对丹麦军工企业实施破坏：X https://x.com/SwitHak/status/2107953192608886888 ／ 文章 https://www.reuters.com/business/aerospace-defense/denmark-says-russia-has-conducted-sabotage-attacks-against-its-defense-firms-2026-10-07/
- Google 因国家顶级域注册基础设施被劫持而在 Chrome 中封锁非法 HTTPS 证书：X https://x.com/Dinosn/status/2107832852658467036 ／ 文章 https://cyberinsider.com/google-blocks-rogue-https-certificates-after-domain-registry-hijacks/
- Nikkei 两个员工云账号被盗，其一发出约 9,000 封钓鱼邮件：X https://x.com/Dinosn/status/2107845387549876686 ／ 文章 https://www.scworld.com/brief/nikkei-discloses-two-employee-account-compromises-one-used-for-phishing
- 亚利桑那法院系统备份被窃，约 130 万人：X https://x.com/Dinosn/status/2107831903076454422 ／ 文章 https://cyberinsider.com/arizona-court-suffered-data-breach-exposing-1-3-million-people/
- Huntress Akira 复盘被 RST Cloud 抽取（归 Unc5330，昨日已收）：https://x.com/rst_cloud/status/2107791478248411439
- Microsoft 威胁情报播客谈 2026 MDDR：https://x.com/MsftSecIntel/status/2107893072801444256

### P-1. 【Huntress · 有 IoC】Power BI 公开报表钓鱼 → rogue ScreenConnect
10-07 10:00（UTC-3）。自 9-10 起，邮件嵌入合法 `app.powerbi.com` 公开报表链接绕过邮件网关，「Download Reference」跳到带指纹与反分析、经 Telegram Bot 回传受害者信息的落地页，自动下载恶意 ScreenConnect 安装器；先后部署两个 rogue 实例，运行 HideUL_x64.exe，建每 2 分钟执行的修复计划任务；回溯又发现 22 台端点受同一客户端影响。防御：审视受信云服务托管链接的下载、监控未经批准的 ScreenConnect 实例与多 RMM 共存、可疑计划任务。
- X 原帖：本窗口 X 未采到，不编造
- 厂商 Huntress：https://www.huntress.com/blog/screenconnect-power-bi
- IoC JSON：`/workspace/enrich-2026-10-07/huntress-powerbi-screenconnect-iocs.json`
- IoC：见汇总「Huntress Power BI」

### P-2. 【Unit 42】Web3 在云供应链攻击中的演进（综述，无 IoC）
10-07 19:00（UTC-3）。供应链恶意软件以区块链做 C2 的三阶段：EtherHiding（合约状态存 C2）→ TxDataHiding（交易 calldata 存加密 C2，如 PolinRider）→ NullReceiver（从零值交易接收地址字节解出 C2 IPv4）；案例含 ChainDrop npm 蠕虫（Shai-Hulud 家族，400+ 包）与 DPRK 关联 Alluring Pisces 对 Axios、Mastra AI、Rust arrayref 的投毒。建议：不需要区块链访问的环境直接阻断 Web3／RPC 流量。与今日 CERT-UA LunexStealer 的 EtherHiding 手法可交叉。
- X 原帖：本窗口 X 未采到，不编造
- 厂商 Unit 42：https://unit42.paloaltonetworks.com/web3-cloud-supply-chain-attacks/
- IoC：未见公开 IoC（文章主张行为检测）。

## 地址／IoC 汇总

**CrowdStrike ARTEX（厂商原样，defang 保留）**
- ARTEX 节点：`38.244.50[.]120`（端口 18899；`http[:]//38.244.50[.]120:18899/.claude/CLAUDE.md`）
- LLM 代理／转售：`xcai[.]pro`
- 代理 IP（9 个）：`101.53.80[.]20`／`205.214.59[.]31`／`124.155.252[.]63`／`154.201.79[.]246`／`23.248.249[.]90`／`23.158.220[.]98`／`103.248.148[.]84`／`203.160.133[.]172`／`209.209.85[.]38`
- 疑似行为者标识（CrowdStrike 称无法确认）：Telegram `@YY520CN`
- 来源：https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/

**Lumen PoeLLM（厂商原样）**
- 仍活跃 C2：`92.119.164.50`／`103.249.201.108`／`178.128.14.204`
- 历史 C2：`191.37.28.160`／`89.39.253.46`／`120.224.114.212`／`5.78.73.122`／`15.204.178.28`／`92.119.165.74`／`45.133.73.28`／`185.132.53.158`／`136.148.69.233`
- 样本 SHA256：`6fab94577364beec314afae3b082dd680933f08a8349b9f35b92667e8231b501`（ELF `libgcrypt`）
- 存放诗歌的 GitHub 账号：`github[.]com/ejejejdfbbebe`（文件 `dash.css`）
- 来源：https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware

**SOCRadar NetScaler C2（CVE-2026-88771，厂商原样）**
- C2：`45.143.130[.]195`（端口 8899 与 53；DNS OOB 形如 `<bid>.p1.oob.45.143.130[.]195`）
- ns.log 狩猎字符串：`pitboss NSPPE-00;`、`/s/<bid>|sh`、`;# unexpectedly died`
- C2 路径：`/s/<bid>`、`/a/<bid>`、`/p/<bid>?h=…&u=…&src=agent`、`/c/<bid>`、`/r/<bid>?d=…`；文件 `/tmp/.nsagent`
- SHA256：`8588d11874ab52a1637953dc5538984647023d00b529f695fbd0e40cf8e5e852`（run.sh）／`4992f575f3f1fc448cf54a4a0ce13cf6548790777abe0af1f935663498ea5639`（targets.py）／`69a34c591eaaa2cbecaeed10c303b8dcf04c846b8408491da5452b9cfc93f686`（probe.py）／`a3e26053975daa0a12a4848ce9533e5c439617cd7f69851347be2061999b4cd4`（exploit.py）／`a9142989d912098856e58f2c74c2266e39150d50bc59722f915dade1ddfddf4a`（c2_server.py）／`f9e06d412dee96d98db4d4588f0012af859cc11caaae3e130697f282447cf07f`（pollctl.py）
- 来源：https://socradar.io/blog/netscaler-c2-cve-2026-88771-exploitation/

**BLACKNET-00（Barricade Cyber 原样）**
- TRK25：SHA256 `5f1ebc84cdee3a4e97c530ff2ffc907e903544b8b5b119f9de2e9bd035058629`／SHA1 `18e14a1e9ba76fa8c7f89e14ea971c11307af23b`／MD5 `28c62e5e820de249ddfb9204fec31bbc`
- BLACKNET-0077.exe（勒索）SHA256 `ad5cb5c9cc36b23a56f456ce35b7051fbca3817bb7541f46c8feae1675005d7d`
- SHADOW-GHOST ULTIMATE v4.0.exe（扫描器）SHA256 `85adbf2a80b13a55e19114203af3151b0fa9aaef195b316a7b18b571994be21a`
- 文件标记：扩展名 `.blacknet`、勒索信 `READ_ME_BLACKNET.txt`
- 来源：https://barricadecyber.com/blacknet-00-ransomware/

**vx-underground Telegram 插件（X 帖原样，未验证）**
- 初始载荷 SHA256 `84aaa0c388ad46322e2155212c182e00548eb18de769fcfa2b919e3ebcec45de`
- Android 主载荷 SHA256 `018368d56a4b272be8825efd4e965354b56f3b9fae73137cee7ad039d3c3e347`
- C2：`intark(.)shop`（`intark(.)shop/api/bkeepfile`）、`185.99.97.216:8081`
- 诱饵：`t(.)me/Exterav`；请求头 `X-LD-Code: GYW7gDO5dyKO0VCt8uAKS9rY5vENZW_g`
- 来源：https://x.com/vxunderground/status/2107647082857206196

**Atlassian CVE-2026-21589 利用源（Previdian 蜜罐，X 一手＋BleepingComputer）**
- IP：`38.60.157[.]86`／`146.70.187[.]234`／`159.26.119[.]225`
- 来源：https://x.com/PrevidianCyber/status/2107731944616153480

**Huntress Power BI → rogue ScreenConnect（厂商原样）**
- SHA256：`5956f9afb3ba610c38b2cfda88dd15be98783963769a12020c93ce05e749b3c3`（ScreenConnect.ClientService.exe，初始 rogue 客户端）／`f048400c23add8c75abe189393d33c873c02c74eeaf43d47b950c8d643763b35`（二次 rogue 客户端）
- 计划任务 `SCAutoRepairEvery2Min`（运行 `SCAutoFix.ps1`）；工具 `HideUL_x64.exe`；`LyN03DvVjUKPrun.cmd`
- 钓鱼诱饵：`hxxps[://]app[.]powerbi[.]com/view?r=eyJrIjoiNTk0NmViNDktYzM1Yy00MjEwLTkyZTctNGU5ZTJmYzMzYjEwIiwidCI6IjU1YTI4YmU2LTFiYzQtNDIzMS05MTA0LTdkMmFlYTVmMGZhNiJ9`
- 落地页：`hxxps[://]dailylifeproject[.]site/S/`／`hxxps[://]burnsworth[.]site/S/main.html`／`hxxps[://]essaywritingservice[.]site/S/main[.]html`／`hxxps[://]openpediatrics[.]site/S/main.html`；指纹失败跳转 `check.vykyn[.]click/E/`
- 安装器：`hxxps[://]hamham27[.]screenconnect[.]com/Bin/ScreenConnect.ClientSetup.exe?e=Access&y=Guest&t=ILEAYEASAN`（另 `t=PERFECTO`／`t=PAPASUPE`）；`hxxps[://]onthegotree[.]site/Bin/ScreenConnect.ClientSetup.msi?e=Access&y=Guest`
- 中继／C2：`instance-g01s1n-relay[.]screenconnect[.]com`／`onthegotree[.]site`
- 来源：https://www.huntress.com/blog/screenconnect-power-bi

**Fortinet FG-IR-26-175（CVE-2026-104286，与前两日相同）**
- IP：`79.141.169.187`／`45.129.0.192`；文件哈希见 2026-10-05 报告与 `/workspace/enrich-2026-10-07/fortinet-FG-IR-26-175-CVE-2026-104286-iocs.json`

**其余条目**：Citrix 88779（厂商）、Zammad 102489／102490、Cisco 14 条、Splunk、Rejetto HFS、SolarWinds ARM、LMCache、NVD 高分 CVE、Unit 42 Web3、CERT-UA LunexStealer（转载文未列）、各工具——**未见公开 IoC**。

## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/ （仍 RBNEWS618 https://risky.biz/RBNEWS618/ ／SRB185／BTN184；RBNEWS619／620、SRB186、BTN185 均 404）
- tl;dr sec 通讯：https://tldrsec.com/ （仍 #348 https://tldrsec.com/p/tldr-sec-348）
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form

本日 LWiS List（500 成员按备份分 10 批查询，完整 24h，共 99 帖）抽取 22 条：Previdian 之外的 Atlassian 讨论（@pdiscoveryio、@cyb3rops）、SolarWinds ARM RCE（@AndrewOliveau、@h4wkst3r）、Home Assistant go2shell（@_mccaulay）、LMCache／PoeLLM／LunexStealer／FortiBleed／Google 证书等新闻转发（@Dinosn）、IDC Frontier 勒索与丹麦破坏（@SwitHak）、vx-underground 的 Telegram 插件样本与 EndZone 自述、emp3r0r（@jm33_m0）、dreadnode、ipurple 检测研究、Cobalt Strike 培训、macOS LPE 预告（@theevilbit）。博客清单交叉：Unit 42、Huntress、Horizon3、Talos、Microsoft Security 当日有新文（威胁类已入正文）；watchTowr、SentinelLabs、Trend Micro、Elastic、GTIG、Check Point、ESET、Securelist、Proofpoint、DoublePulsar 无新文。

## 来源搜索 URL

- X Search A（Latest）：https://x.com/search?q=(CVE%20OR%20POC%20OR%20exploit%20OR%200day)&f=live
- X Search A′（本轮实际查询，去噪）：https://x.com/search?q=(%22CVE-2026%22%20OR%200day%20OR%20%22zero-day%22%20OR%20%22actively%20exploited%22%20OR%20%22exploited%20in%20the%20wild%22)%20-filter%3Areplies&f=live
- X Search B（Latest）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- X Search C（Latest）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA ICS 公告：https://www.cisa.gov/news-events/ics-advisories
- NVD API（本窗口）：https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate=2026-10-06T23:00:00.000Z&pubEndDate=2026-10-07T23:30:00.000Z
- Cisco PSIRT RSS：https://sec.cloudapps.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml
- Fortinet PSIRT RSS：https://filestore.fortinet.com/fortiguard/rss/ir.xml
- MSRC 更新 API：https://api.msrc.microsoft.com/cvrf/v3.0/updates
- Palo Alto RSS：https://security.paloaltonetworks.com/rss.xml
- Atlassian 安全公告：https://confluence.atlassian.com/security
- GitHub releases：https://github.com/BishopFox/sliver/releases ／ https://github.com/projectdiscovery/nuclei/releases ／ https://github.com/projectdiscovery/nuclei-templates/releases ／ https://github.com/jm33-m0/emp3r0r/releases
