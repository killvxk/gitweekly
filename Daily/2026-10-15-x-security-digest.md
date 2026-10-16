# X 安全情报晚报 · 2026-10-15

> 搜集窗口：圣地亚哥时间 **2026-10-14 20:09 至 2026-10-15 20:10**（America/Santiago／UTC-3，约 **24 小时 1 分**，接昨晚窗口，没有缺口）。ISO／X 搜索参数：`start_time=2026-10-14T23:09:00Z`，`end_time=2026-10-15T23:10:00Z`。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all` + `get_posts_by_ids`，带 entities／note_tweet；t.co 链接一律用 entities.expanded_url／unwound_url 展开）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** A／B／C 三类各跑原始与去噪查询：A 用 `CVE-2026`／安全语境去噪（去掉刷屏 RT）；B 限 `url:github.com` + C2／red team／nuclei；C 为 malware analysis／threat report／threat actor，排除 ThreatAtlas／FalconFeeds。LWiS 用 `from:` + recency：①优先批核心账号（BleepingComputer／THN／securityaffairs／malwrhunterteam／Nulltap_／cybermergemedia／DailyDarkWeb／Python_s_／ThreatWire_／CISA／CrowdStrike 等）分段翻页；②扩展厂商／媒体（SecurityWeek／Shadowserver／sans_isc／Unit42／Huntress／DFIR_Radar／Dinosn／Talos 等）；③部分 List 研究账号抽检。`from:` 用户名均 ≤15 字符。本轮约 **25 次 X 读取**（search_posts_all 约 24 次 + get_posts_by_ids 1 次），**未触发限速**（当日额度仍余约 980/1000）。窗口内去重后约 **180+** 条相关帖（多查询重叠），与 seen_ids 比对后筛选（去掉广告、空转发、闲聊、勒索受害者刷屏），合并 **125** 条安全相关新帖：**A18／B5／C14／LWiS88**（归类：命中 LWiS `from:` 批次的算 LWiS，其余按 A／B／C 来源）。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON（`/workspace/enrich-2026-10-15/kev.json`）。厂商／研究页存于 `/workspace/enrich-2026-10-15/web/`：Atlassian CVE-2026-21589 公告、Google／Mandiant GTI「ARMORY CASTLE Exploits BeyondTrust」、Next.js 10-14 安全更新博文与 GitHub advisories、THN（PwnEscape／Next.js／Candiru／Silent Lynx／Help TDS 等）、Security Affairs AdFection、pwn.ai PwnEscape、CISA 10-15 KEV 警报、Risky Bulletin（Gemini）。GitHub API 查了 nuclei／nuclei-templates／Sliver／emp3r0r／BloodHound／NetExec／Mythic／impacket 的 releases。BleepingComputer 部分文章对 curl 返回 **403**，链接取自 X 原帖 entities 展开。tl;dr sec 首页返回 **403**（Cloudflare），未取到正文。
> **CISA KEV：catalogVersion 2026.10.15／1746 条，Δ+1**（对比昨日 2026.10.14／1745；dateReleased 2026-10-15T17:00:11Z＝**10-15 14:00 圣地亚哥**）。**今天新增 1 条**：**CVE-2026-21589**（Atlassian 多产品任意文件访问，due **2026-10-18**，ransomware: Unknown；需按 BOD 26-04 做 forensic triage）。
> **due_today（10-15）：0 条。newly_overdue（10-14 到期）：0 条。** Apple CVE-2026-86950（due 10-13）与 AA26-281A 五条（BIND／Struts／Strapi／ONLYOFFICE／ProFTPD，due 10-11）仍逾期。**未来 7 天到期：7 条**：Ivanti CVE-2026-104935 与 Windows CVE-2026-96951 在 **10-16**；Ahsay 105133／105134、Cisco 76519、PAN-OS 0322 在 **10-17**；Atlassian 21589 在 **10-18**。下列 CVE **仍未进 KEV**：BeyondTrust **102764**、Nextcloud／Collabora **110447**、PwnEscape **99999**、Next.js／librsvg **96889**、Discourse **55420**、Drupal **108097**、GitLab **97229**、curl **92392**、SiteGuard **106931**、SonicWall **102255** 等。
> 抓取备注：BeyondTrust 厂商 trust-center 页对 curl 返回 403，处置要点取自 Mandiant／GTI 博客与 DailyDarkWeb／DFIR_Radar 转述。Risky Business 首页仍突出 RB #855；另有 Risky Bulletin「Gemini hacked three companies too」。监控的红队工具今天**都没有新 release**（emp3r0r 最新仍为 10-11 的 v5.2.2；Sliver v1.7.8／nuclei-templates v10.5.0 等均早于本窗口）。
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接作狩猎用途。泄露、入侵、勒索类声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【KEV 新增 · 自托管 Atlassian】CVE-2026-21589**（CVSS 4.0 **9.3**）：Bitbucket／Confluence／Jira Software／Jira Service Management／Bamboo／Crowd Data Center 与 Crucible／Fisheye 的未认证任意文件读取（需已知精确路径，不能列目录）。CISA **10-15** 收进 KEV，联邦期限 **10-18**，要求 forensic triage。Cloud 已由厂商代修；自托管须升到公告中的固定版本（如 Bitbucket 9.4.26／10.2.8／10.5.1，Confluence 9.2.26／10.2.19，Jira Software 9.12.40／10.3.26／11.3.12 等），或先 WAF／RewriteValve 缓解并限制公网暴露。与 Crowd SSO 联用时注意 `crowd.properties` 明文凭据风险；补丁后回溯约 **10-06** 起的访问日志。
  X 原帖：https://x.com/CISACyber/status/2110814549297246595
  厂商：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
  CISA：https://www.cisa.gov/news-events/alerts/2026/10/15/cisa-adds-one-known-exploited-vulnerability-catalog
  KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **【在野零日 · 未进 KEV】BeyondTrust Remote Support CVE-2026-102764**（CVSS **9.3**，BT26-05）：未认证文件操作 → 主机级控制。Mandiant／GTIG：**ARMORY CASTLE**（原 UNC5221，疑似 PRC 背景）自 **2026-08 下旬** 起当零日利用，部署 **SAWFLY** webshell 与 **BARECLAW** SOCKS5／WebSocket 隧道，并抽 vault、改 haproxy、清日志。SaaS 租户已于 **10-09** 代补；自托管须打 **BT26-05-RS**（或先升到 ≥24.3.1 再打）。互联网暴露且窗口内脆弱的设备应按已入侵对待，优先重建而非原地清理。
  X 原帖：https://x.com/DailyDarkWeb/status/2110856005198213489
  研究：https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust
  厂商：https://www.beyondtrust.com/trust-center/security-advisories
- **【内核 · 未进 KEV】PwnEscape CVE-2026-99999**（CVSS **9.3**）：Linux 网络栈校验和 TOCTOU，访客 VM 可泄露主机内存；实验室演示可致主机崩溃／提权逃逸。发现于 Vercel $1M Sandbox 挑战，生产侧确认内存泄露；**未见在野利用**。修复需打**主机内核**（如 5.10.272／5.15.223／6.1.190／6.6.159／6.12.113／6.18.57／7.2.11 等或发行版 backport）并重启；只升客户机无效。
  X 原帖：https://x.com/TheHackersNews/status/2110832582812369295
  研究：https://pwn.ai/blog/pwnescape
  文章：https://thehackernews.com/2026/10/critical-pwnescape-linux-kernel.html
- **【框架 · 紧急补丁】Next.js 定例外更新**：未认证 RCE 两枚（`use cache` 类型数组 **GHSA-673q-mjm6-r5xr**；SVG／librsvg **CVE-2026-96889**／GHSA-2464-fhr4-w9xw，均 CVSS **9.5**）+ Server Actions DoS。升到 **16.4.1** 或 **15.5.28**；确认 `sharp` ≥ **0.35.5**。截至 10-15 **未见在野**。
  X 原帖：https://x.com/TheHackersNews/status/2110711243942330566
  厂商：https://nextjs.org/blog/nextjs-security-update-october-14-2026
  文章：https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html
- **【KEV 临期】Ivanti 104935 与 Windows 96951 due 明天（10-16）**；Cisco 76519／PAN-OS 0322／Ahsay 两条 due **10-17**。继续收紧 ICS／邮件网关／防火墙管理面，并核验 Content Scanner Tools ≥25.3.0.5525、PAN 管理面是否仅跳板可达。
  文章：https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html
  厂商：https://security.paloaltonetworks.com/CVE-2026-0322
- **【间谍软件】Citizen Lab AdFection**：Candiru 间谍软件经 Discover-Tech 定向广告 **零点击**投放到半岛电视台至少 **45** 台设备；为公开技术证实的「广告投间谍软件」案例。Google／IAB Europe 等已下架该广告商。IoC 含样本 SHA-256 与 `mtrtb[.]com` 等（见下文）。
  X 原帖：https://x.com/TheHackersNews/status/2110767657159151707
  研究：https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/
  文章：https://securityaffairs.com/201015/hacking/adfection-beyond-the-click-citizen-lab-exposes-ad-delivered-spyware-networks.html
- **【APT 续】Silent Lynx／UAT-6275**：继续用 WinRAR **CVE-2025-8088** 在独联体政府目标投放 PickleShell 等反向壳。
  文章：https://thehackernews.com/2026/10/silent-lynx-exploits-winrar-flaw-to.html
- **【供应链／物联网】**假 Arch 包（仿 yay／paru）提权投毒；D-Link／Ubiquiti **proxyjacking** 转售带宽（34 国）；Shadowserver／CERT-FR：Copeland／Dixell XWEB 冷柜控制器约 **1200** 台日均暴露（Danfoss 事件扩大）。
  X 原帖：https://x.com/BleepinComputer/status/2110780972530565459
  X 原帖：https://x.com/BleepinComputer/status/2110798191037677631
  X 原帖：https://x.com/Shadowserver/status/2110826263401333193
- **【泄露事件】**日本 SourceNext 最多约 **2252 万**会员（含密码字段）；Burger King Japan 约 **1118 万**；BAE Systems 事件扰动美国破产通知中心；CenterPoint 德州 AG 披露逾 **106 万**（SSN／驾照）。巴基斯坦核监管机构文件、阿联酋 EMSO 27GB 等标 **UNCONFIRMED**。
  厂商：https://www.sourcenext.com/support/i/2026/1015_info/
  厂商：https://www.burgerking.co.jp/images/notice/2026/10/15/d4d114ca-ebd7-4f3d-94ef-c4ea7a84a139.pdf
- **【其他】**Drupal Field UI **CVE-2026-108097** 关键路径（经贡献模块可未认证）；NGINX 1.30.6／1.31.7 修 5 洞；Help TDS／Hotejka 技术支持诈骗（2 万+ Cloudflare Pages）；JPCERT 确认 AI 辅助 Web API 攻击；GhostAction 扩大（约 1900 账号／3 万仓库，偏 10-08／09 高峰）。
- **【统计】** X 合并 **125**（A18／B5／C14／LWiS88）；KEV **2026.10.15／1746／Δ+1**；due_today **0**；newly_overdue **0**；未来 7 天到期 **7**；红队工具无新 release。

## CVE / POC / 漏洞

### X-1. 【KEV 新增 · 在野】Atlassian 多产品 CVE-2026-21589（未认证任意文件读取）
Atlassian 于 10-05 披露：自托管 Data Center／部分 Server 产品存在任意文件访问（CWE 类「外部可访问文件／目录」），未认证攻击者在已知精确文件路径时可读取 Web 应用根目录下特定文件（**不能枚举目录**）。CVSS 4.0 **9.3 Critical**。CISA **2026-10-15** 加入 KEV，due **2026-10-18**，并引用 BOD 26-04 与 forensic triage 要求。公开讨论称 Crowd 集成场景下可读到含明文凭据的配置（如 `crowd.properties`）进而扩大为管理接管；PoC 出现后短时间内即有探测／利用声称（以厂商与 CISA 为准）。
**修复版本（摘录）**：Bitbucket DC 9.4.26／10.2.8／10.5.1；Confluence DC 9.2.26／10.2.19；Jira Service Management DC 5.12.40／10.3.26／11.3.12；Jira Software DC 9.12.40／10.3.26／11.3.12；Bamboo DC 10.2.24／12.1.12；Crowd DC 6.3.7／7.0.3／7.1.7／7.2.4；Crucible／Fisheye 4.9.15。无法立即打补丁时：限制公网暴露；WAF 拦截含 `..` 与 `/`、`\\`、`::` 邻接的路径模式；或对部分产品启用 Tomcat RewriteValve（见厂商公告）。Cloud 实例已由 Atlassian 处理。
**狩猎**：回溯约 10-06 以来对编码路径／异常静态文件读取的访问日志；补丁后轮换可能暴露的 SSO／目录绑定密钥。
地址：
- X 原帖（CISA）：https://x.com/CISACyber/status/2110814549297246595
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2110816638010585472
- X 原帖（cybermergemedia）：https://x.com/cybermergemedia/status/2110800008673157304
- X 原帖（Python_s_）：https://x.com/Python_s_/status/2110785591499448763
- 厂商：https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/10/15/cisa-adds-one-known-exploited-vulnerability-catalog
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 文章（cybermerge）：https://cybermerge.com/stories/atlassian-cve-2026-21589-cisa-kev-due-oct-18
IoC：未见公开网络 IoC（以路径探测与文件读取日志为狩猎信号）。

### X-2. 【在野零日 · 未进 KEV】BeyondTrust Remote Support CVE-2026-102764（未认证文件操作 → root）
BeyondTrust **10-15** 披露 BT26-05：Remote Support（原 Bomgar）至 **26.2.3** 的未认证文件操作缺陷，可导致任意文件上传与主机级控制（CVSS 9.3）。Mandiant 在事件响应中确认疑似 PRC 背景的 **ARMORY CASTLE**（原 UNC5221）于 **2026 年 8 月下旬** 起零日利用。
**入侵链要点（防御向）**：投放 SAWFLY（`mangoapi.php`，POST 参数 `_c94mfe`，缺失则 404）；复制 `/bin/sh`→`/usr/bin/dbus-authd` 并置 SUID；用 `/ns/sbin/bt-secrets` 抽 vault；写 `post_boot.d/zz-root-persist` 持久化 sudoers.template；部署 BARECLAW（`ingredi_ws`，监听 19800，路径 `/uidchanarge`）并改 `/ns/config/haproxy.conf` 引入外联；系统删除多份日志。
**处置**：SaaS 已于 10-09 代补；自托管 ≥24.3.1 打 BT26-05-RS，更旧版本先升级再打补丁。对暴露窗口内的互联网可达设备：**先取证快照（含内存）→ 隔离 → 倾向重建**；补丁后再按依赖顺序轮换 `/appliance`、`/login`、API、Vault／Password Safe、SAML 等凭据；查 `user_changed` 将 Jump Item 升为 Administrator、异常 `.php`、haproxy 未知 ACL、SUID `dbus-authd`、syslog 缺口。
地址：
- X 原帖（DailyDarkWeb）：https://x.com/DailyDarkWeb/status/2110856005198213489
- X 原帖（DFIR_Radar）：https://x.com/DFIR_Radar/status/2110853927302521162
- X 原帖（转述 Mandiant）：https://x.com/Big_Bad_W0lf_/status/2110845070975119585
- 研究（GTI／Mandiant）：https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust
- 厂商：https://www.beyondtrust.com/trust-center/security-advisories
IoC（Mandiant 公开文件哈希，原样）：
- SAWFLY `mangoapi.php` SHA-256：`dc14e215269a93fdbc4c1a80b984c23faf7af0911c6dbb85309796a6f2ae95fb`
- BARECLAW `ingredi_ws` SHA-256：`1f19b9a27d79c11bda00a1e8faf74a7fdd683d38ccef1b60df2fd0307e3aa462`
- 文件名线索：`app_84304470%2Ephp`、`mangoapi.php`、WebSocket 路径 `/uidchanarge`、haproxy ACL `wswsws`／backend `webskd3`

### X-3. 【披露 · 未进 KEV】PwnEscape／Linux CVE-2026-99999（访客读主机内存／实验室逃逸）
pwn.ai（Paulos Yibelo）披露：Linux 内核网络栈 IPv4 checksum 相关 TOCTOU，访客构造报文可泄漏主机内存（约每包 32 字节）；实验室可致主机崩溃与 root 级逃逸。Vercel 确认其生产 Sandbox 存在内存泄露演示；**无客户数据被读出的报告**；**未见在野利用**。漏洞在共享内核层，影响面不限于单一云厂商。修复提交 `6785011f8b16`（Red Hat Michael S. Tsirkin），已 backport 至多条稳定分支。
**动作**：更新**宿主机**内核至固定版本或发行版安全内核并 reboot；无法立即打补丁时限制嵌套虚拟化与微 VM 权限（不能替代补丁）。
地址：
- X 原帖（THN）：https://x.com/TheHackersNews/status/2110832582812369295
- X 原帖（研究者）：https://x.com/PaulosYibelo/status/2110777553581388140
- 研究：https://pwn.ai/blog/pwnescape
- 文章：https://thehackernews.com/2026/10/critical-pwnescape-linux-kernel.html
IoC：未见公开网络 IoC（本地／访客侧触发）。

### X-4. 【紧急补丁 · 未见在野】Next.js 未认证 RCE（GHSA-673q-mjm6-r5xr／CVE-2026-96889）+ DoS
Vercel **10-14** 定例外发布 **16.4.1**／**15.5.28**：① App Router Cache Components 下 `use cache` 返回多个 typed array 时可未认证 RCE；② glibc Linux 上经 `sharp`／librsvg 处理攻击者可控 SVG 时 RCE（常需 `dangerouslyAllowSVG` 或 `next/og` 路径）；③ Server Actions DoS。两枚 RCE 均为 CVSS **9.5**。临时：至少将 `sharp` 升到 **0.35.5+** 或按 sharp 公告阻断 SVG loader；`use cache`／DoS **无变通**。
地址：
- X 原帖（THN）：https://x.com/TheHackersNews/status/2110711243942330566
- X 原帖（ThreatWire_）：https://x.com/ThreatWire_/status/2110605887907713139
- 厂商：https://nextjs.org/blog/nextjs-security-update-october-14-2026
- GHSA：https://github.com/vercel/next.js/security/advisories/GHSA-673q-mjm6-r5xr
- GHSA：https://github.com/vercel/next.js/security/advisories/GHSA-2464-fhr4-w9xw
- 文章：https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html
IoC：未见公开 IoC。

### X-5. 【KEV 续 · 明天到期】Ivanti Connect Secure CVE-2026-104935 ＋ Windows CVE-2026-96951
两条均 **due 2026-10-16**。Ivanti 仍为认证绕过链式 RCE 紧急项；Windows Shell MotW／SmartScreen 绕过为 Patch Tuesday 唯一确认在野项。另有 ThreatWire 提示 Windows Health 服务 **CVE-2026-85884** PoC、Chrome **CVE-2026-91737** PDF UAF PoC、Splunk **CVE-2026-76268** 未认证 RCE PoC（链接仅作狩猎，本报告不转步骤）。
地址：
- X 原帖（续报语境）：https://x.com/read__the__diff/status/2110853392234860856
- X 原帖（ThreatWire Splunk PoC）：https://x.com/ThreatWire_/status/2110528685350469758
- 文章：https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html
IoC：沿用昨日公开的蜜罐攻击 IP 示例时请交叉厂商最新情报；本日未见强制更新的新官方 IoC 包。

### X-6. 【KEV 续 · due 10-17】Cisco SEG 76519 ／ PAN-OS 0322 ／ AhsayCBS 105133／105134
Cisco：File Reputation／AMP 开启且 Content Scanner Tools < **25.3.0.5525** 时附件路径遍历 → root；无缓解，集群每节点 `grep "System Security" system_logs`。PAN-OS：已认证高权限管理面代码注入；IoC IP `66[.]42[.]72[.]14`、`208[.]83[.]239[.]114`、`149[.]248[.]47[.]234`；11.2.16 原定今日前后。Ahsay：须热修复 **10.3.4.45／9.15.2.70** 并重启。
地址：
- X 原帖（cybermerge PAN）：https://x.com/cybermergemedia/status/2110753655016263716
- 厂商（PAN）：https://security.paloaltonetworks.com/CVE-2026-0322
- 厂商（Cisco）：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp
- 文章：https://www.securityweek.com/cisco-warns-of-exploited-secure-email-gateway-vulnerability/
IoC（PAN，原样）：`66[.]42[.]72[.]14`、`208[.]83[.]239[.]114`、`149[.]248[.]47[.]234`

### X-7. 【其他高危／补丁】Drupal 108097、NGINX、Discourse、GitLab PoC 续、curl 92392 续
Drupal core Field UI **CVE-2026-108097**：经部分贡献模块可出现未认证 RCE 路径；升 **11.4.10／11.3.19／10.6.19**，不能升级则临时卸载 `field_ui`。NGINX **1.30.6／1.31.7** 修 5 洞（含古老 alias 问题 CVE-2026-15176）。Discourse **CVE-2026-55420**（新成员可读服务器文件）有扫描器传播。GitLab **97229** PoC 与暴露主机统计续报。curl **92392**（HTTP/2 上传 UAF→RCE）修于 8.23.0。
地址：
- X 原帖（cybermerge Drupal／NGINX 要点）：https://x.com/cybermergemedia/status/2110761435563462698 ；https://x.com/cybermergemedia/status/2110734993366679960
- 文章（THN Next.js 同日专题流内 Drupal／NGINX 条目）：https://thehackernews.com/
- 厂商（curl）：https://curl.se/docs/CVE-2026-92392.html
IoC：未见公开 IoC。

### X-8. 【在野 · 未进 KEV】Nextcloud Collabora CVE-2026-110447 续
BC 今日再推：内置 CODE Server `proxy.php` 未认证命令注入，自 09-10 起被利用落 webshell；须升 richdocumentscode **26.4.303** 或卸载，仅禁用不够。
地址：
- X 原帖：https://x.com/BleepinComputer/status/2110829398605607206
- 文章：https://www.bleepingcomputer.com/news/security/hackers-exploit-collabora-rce-flaw-to-backdoor-nextcloud-servers/
- 厂商：https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh
IoC（公开 webshell 文件名，原样）：`shrf4645.php`、`shxa35d0.php`、`shx5cf91.php`、`shxd33ce.php`、`shxf4645.php`、`shx13a86.php`、`shx56367.php`

## 工具与 GitHub 发布

- 本窗口监控的 **nuclei／nuclei-templates／Sliver／emp3r0r／BloodHound／NetExec／Mythic／impacket**：**无新 GitHub release**（相对昨日）。
- X／GitHub 相关分享（防御／实验室向，非利用教程）：AI 红队编排 **artex-global**；红队拓扑导出 Terraform／Ansible 的画布项目；AlphaSOC 对抗仿真覆盖评测；「RedTeam-Tools」150+ 工具索引清单。
地址：
- X 原帖：https://x.com/Marco_Ramilli/status/2110826337212526679
- X 原帖：https://x.com/ipurple/status/2110775902368137575
- X 原帖：https://x.com/alphasoc/status/2110748675391566056
- X 原帖：https://x.com/aoteman1can/status/2110702231834038417
- Cobalt Strike Beacon 语料（研究）：https://x.com/cyb3rops/status/2110756582678040579
本日无显著「新版 C2 框架 release」；上列为社区工具索引与仿真资源。

## APT / Malware 分析

### M-1. ARMORY CASTLE × BeyondTrust（见 X-2）
完整 TTPs／YARA／狩猎见 GTI 博文。Google SecOps 规则名示例：「Echo Pipes Base64 To Shell」「Suspicious Curl Download to tmp」等。

### M-2. AdFection／Candiru 广告零点击
Citizen Lab：Discover-Tech 广告在加载时回传广告 ID／IP，命中目标后再下发攻击代码；半岛电视台 2024–2025 至少 45 台设备。Google／IAB Europe／Beeswax／Vungle／Eskimi 已采取措施。
地址：
- X 原帖：https://x.com/TheHackersNews/status/2110767657159151707
- 研究：https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/
- 文章：https://thehackernews.com/2026/10/citizen-lab-traces-zero-click-candiru.html
IoC（公开，原样）：
- SHA-256：`255869de85e2a171993fc5eb8a556d873a1b8966e040f6f55926f2fa2d595cc8`
- 域名：`mtrtb[.]com`（Discover-Tech 广告服务器；完整列表见 Citizen Lab／Confiant 报告）

### M-3. Silent Lynx（UAT-6275／TAG-193）WinRAR 8088
独联体政府目标；Startup 文件夹反向壳（PickleShell 等）。
地址：
- X 原帖：https://x.com/TheHackersNews/status/2110763451048157604
- 文章：https://thehackernews.com/2026/10/silent-lynx-exploits-winrar-flaw-to.html
IoC：未见本日新公开批量 IoC；以 WinRAR 版本与 Startup 异常为狩猎点。

### M-4. 其他恶意软件／活动
- **CikaBika** Bot RAT（Discord C2）；**Hirudo** Android 银行木马（替换银行 App）；Symantec **Aoki** 信息窃取（瞄准 Claude／Codex／Cursor／Gemini 等 AI 编程助手凭据）；**YuanKong** Android 银行 RAT；Help TDS／Hotejka 技术支持诈骗（2 万+ Cloudflare Pages）；假 Arch AUR 包；D-Link／Ubiquiti proxyjacking。
地址：
- https://www.securityweek.com/cikabika-bot-rat-uses-discord-for-cc/
- https://www.securityweek.com/novel-android-banking-rat-hirudo-replaces-banking-apps-with-trojanized-copies/
- https://x.com/threatintel/status/2110680286556000274
- https://thehackernews.com/2026/10/help-tds-linked-to-hotejka-as-20000.html
- https://x.com/BleepinComputer/status/2110780972530565459
- https://x.com/BleepinComputer/status/2110798191037677631
- malwrhunterteam 开放目录／域名线索：`5.83.136[.]39:8080`／`:5001`，`dist-cdn[.]net`，`updpkg[.]net`，`13.140.43[.]225`，`isgraphicsport[.]net`（https://x.com/malwrhunterteam/status/2110810471263576420 等）

### M-5. 泄露与事件（部分 UNCONFIRMED）
- SourceNext ≈22.52M（官方确认，含密码字段）：https://www.sourcenext.com/support/i/2026/1015_info/
- Burger King Japan ≈11.18M：https://www.burgerking.co.jp/images/notice/2026/10/15/d4d114ca-ebd7-4f3d-94ef-c4ea7a84a139.pdf
- BAE → 美国破产法院通知中断：https://www.uscourts.gov/data-news/judiciary-news/2026/10/15/cybersecurity-incident-disrupting-bankruptcy-court-operations
- CenterPoint ≥1,062,060 德州居民：https://www.securityweek.com/centerpoint-energy-data-breach-impacts-1-million-texans/
- PNRA 文件、EMSO 27GB：**UNCONFIRMED**（https://x.com/DailyDarkWeb/status/2110850836406403216 等）

## 地址／IoC 汇总

| 主题 | IoC／狩猎信号 | 来源 |
|------|----------------|------|
| BeyondTrust／ARMORY CASTLE | SHA256 `dc14e215…ae95fb`（SAWFLY）、`1f19b9a2…3aa462`（BARECLAW）；路径 `/uidchanarge`；SUID `dbus-authd`；haproxy ACL `wswsws` | GTI |
| PAN-OS 0322 | `66[.]42[.]72[.]14`、`208[.]83[.]239[.]114`、`149[.]248[.]47[.]234` | Palo Alto |
| AdFection／Candiru | SHA256 `255869de…595cc8`；`mtrtb[.]com` | Citizen Lab／THN |
| Collabora／Nextcloud | webshell 文件名 `shx*.php`／`shrf*.php`（见 X-8） | Collabora／THN |
| malwrhunterteam | `5.83.136[.]39`、`dist-cdn[.]net`、`updpkg[.]net`、`13.140.43[.]225` | X |
| Atlassian／PwnEscape／Next.js 等 | 未见公开网络 IoC | — |

其余条目：**未见公开 IoC**。

## LWiS 固定信源

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

- X A（CVE 去噪）：`https://x.com/search?q=(CVE-2026%20OR%20CVE-2025)%20(patch%20OR%20exploit%20OR%20PoC%20OR%20RCE%20OR%20KEV)%20-is%3Aretweet&src=typed_query&f=live`
- X B（GitHub 工具）：`https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)%20-is%3Aretweet&src=typed_query&f=live`
- X C（威胁分析）：`https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)%20-is%3Aretweet&src=typed_query&f=live`
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
