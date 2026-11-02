# X 安全情报晚报 · 2026-10-31

覆盖窗口：2026-10-30 20:00 至 2026-10-31 约 20:15（America/Santiago），约 24 小时。X 只读读取 5 次（主题检索 4 次、LWiS 成员时间线 1 次），0 次限流；t.co 均已展开。公开备援：CISA KEV 2026.10.30（共 1766 条，周六无更新，Δ0）。IoC 一律 defang。

## 今日摘要

- **Drupal Commerce Core CVE-2026-118539（Highly critical）在野利用**：缺失授权可绕过访问控制、篡改订单，无需登录；修复版 3.3.13／8.x-2.41，官方要求升级后审计订单。尚未进 KEV。
- **KEV 今日到期**：Linux 内核 Fragnesia CVE-2026-46300 截止 10-31；GitLab CVE-2026-97229 与 Cisco ASA/FTD CVE-2026-76418 明天 11-01 到期；Ivanti CVE-2026-111357 11-02 到期。
- **PHP2Shell（109618/109619）后续**：X 上多方复述中国关联组织串联 Fragnesia 提权拿下约 25 台防火墙（含美国政府系统），有勒索附属声称持有可用利用；仍以打补丁为主。
- **Node2Shell（Brotli CVE-2026-111497）**：SC Media 与新加坡 CSA 再次提醒，Node.js 22.23.4+/24.22.1+/26.12.1+，.NET 8–11 也受影响。
- **工具**：BEAR C2（GitHub 新发布，模拟 APT 的 C2 框架）、ProjectDiscovery 宣布 neo 免费开放；0rcruxe 发表 Google 密码管理器／passkey 被用户态恶意软件窃取的研究。
- **威胁情报**：微软发布朝鲜威胁行为者采用 AI 的追踪报告（经 X 转述）；勒索泄露站新增 Qilin（美国医疗）、Rhysida（美国学校）、EMPERADOR（Holcim、乌拉圭 Punta Shopping）等声称（未经核实）。

## CVE / POC / 漏洞

### 1. Drupal Commerce Core CVE-2026-118539（SA-CONTRIB-2026-254，在野）
特定路由与实体字段（含订单 JSON 字段写入）缺少授权检查，未认证攻击者可绕过访问控制、操纵订单。受影响：3.0.0–3.3.12、8.x-2.41 之前。Drupal 确认在野利用，用于欺诈订单尝试，未见大规模活动、未披露受害数量。处置：升级到 3.3.13 或 8.x-2.41，并审计近期订单的未付款或异常价格记录。
- X 原帖：https://x.com/securityaffairs/status/2116457590339088784
- X 原帖：https://x.com/BinaryBriefing/status/2116441718400630956
- X 原帖：https://x.com/vuln_tracker/status/2116485338558263404
- X 原帖：https://x.com/SCMagazine/status/2116330061364101480
- X 原帖：https://x.com/TwitGri/status/2116632834014368144
- 厂商公告：https://www.drupal.org/sa-contrib-2026-254
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-118539
- 文章：https://securityaffairs.com/202162/security/attackers-exploit-critical-drupal-commerce-core-vulnerability-cve-2026-118539.html
- 文章：https://www.scworld.com/news/drupal-commerce-core-access-bypass-flaw-exploited-in-attacks
- 文章（日文）：https://security.entamec.com/article/drupal-commerce-core-authz-cve-2026-118539/
- 地址／IoC：未见公开 IoC

### 2. KEV 到期提醒（无新增）
KEV 目录仍为 2026.10.30／1766 条。今天到期：Linux 内核 Fragnesia CVE-2026-46300。11-01 到期：GitLab CVE-2026-97229、Cisco ASA/FTD CVE-2026-76418。11-02：Ivanti CVE-2026-111357；11-03：CVE-2026-96652／96655／110936；11-10：Magento 48356、Brotli 111497；11-11：VMware ESX 41709；11-13：Ivanti 118527。
- X 原帖（Ivanti）：https://x.com/drerdalozkaya/status/2116528189430194224
- X 原帖（Ivanti）：https://x.com/BlairOnSec/status/2116325322811699425
- X 原帖（Cisco）：https://x.com/Soar_Infosec/status/2116304331645292708
- X 原帖（GitLab）：https://x.com/rootcausedev/status/2116596728853918083
- X 原帖（ESXi 41709）：https://x.com/Soar_Infosec/status/2116666912952242637
- X 原帖（Fragnesia）：https://x.com/i_osiemo/status/2116372013455413364
- CISA KEV 公告：https://www.cisa.gov/news-events/alerts/2026/10/30/cisa-adds-two-known-exploited-vulnerabilities-catalog
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- 文章：https://privacyneedle.com/cybersecurity/cisa-ivanti-connect-secure-flaws-kev/
- 文章：https://secbriefs.com/briefs/cisa-adds-actively-exploited-gitlab-and-cisco-flaws-to-kev
- 地址／IoC：未见公开 IoC

### 3. PHP2Shell CVE-2026-109618 / 109619 后续
X 上安全账号复述：中国关联组织把 PHP2Shell 与内核提权串联，拿下约 25 台 PAN-OS 防火墙（含美国政府系统）并投放 webshell；另有勒索附属声称持有可用利用（未核实）。KEV 截止日 10-29 已过，未修补系统应视为可能失陷并排查。
- X 原帖：https://x.com/DFIR_Radar/status/2116320330709148124
- X 原帖：https://x.com/DFIR_Radar/status/2116395437347201325
- X 原帖：https://x.com/PHPSiteAudit/status/2116428205900824775
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-109618 ／ https://nvd.nist.gov/vuln/detail/CVE-2026-109619
- 地址／IoC：未见公开 IoC（帖文为图片摘要，未含可抄录指标）

### 4. Node2Shell：Brotli CVE-2026-111497
解压攻击者可控数据时可致 RCE 或内存泄露。Node.js 升级到 22.23.4+、24.22.1+ 或 26.12.1+；.NET 8–11 同样受影响。KEV 截止 11-10。
- X 原帖：https://x.com/SCMagazine/status/2116665773410210224
- X 原帖：https://x.com/nurhayatdev/status/2116588426749505750
- 厂商／政府公告：https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2026-154/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-111497
- 文章：https://www.scworld.com/news/node2shell-flaw-in-brotli-added-to-cisa-exploited-vulnerabilities-list
- 地址／IoC：未见公开 IoC

## 工具与 GitHub 发布

### 1. BEAR C2（S3N4T0R-0X0）
以模拟 APT 行为为定位的红队 C2 框架，经 @C0d3Cr4zy 转介，本窗口热度最高的工具帖。蓝队可关注其公开特征做检测。
- X 原帖：https://x.com/C0d3Cr4zy/status/2116537990000390627
- GitHub：https://github.com/S3N4T0R-0X0/BEAR-C2
- 地址／IoC：未见公开 IoC

### 2. ProjectDiscovery neo 免费开放
ProjectDiscovery（nuclei 团队）宣布 neo 对所有人免费，用于复核「不可利用」的发现。
- X 原帖：https://x.com/pdiscoveryio/status/2116570128498467313
- 官网：https://go.projectdiscovery.io/try
- 地址／IoC：未见公开 IoC

### 3. 其他 GitHub 发布（信号较低）
- Lab-RATS v1.6（Android 远控／C2 实验工具，作者自宣）：X 原帖 https://x.com/K4N3CO/status/2116380407209787479 ；GitHub https://github.com/K4N3CO/Lab-RATS-v1.6
- AgentAudit（AI agent 对抗测试，对应 OWASP Agentic Top 10）：X 原帖 https://x.com/kamarifatizwx/status/2116655463227957345 ；GitHub https://github.com/TOUMO45/AgentAudit
- Hacking-Tools 分类合集：X 原帖 https://x.com/yogsec/status/2116361671354864034 ；GitHub https://github.com/yogsec/Hacking-Tools
- 地址／IoC：未见公开 IoC

## APT / Malware 分析

### 1. 用户态恶意软件窃取 Google 密码管理器／passkey（0rcruxe 研究）
LWiS 成员 @28zaaky 转介：研究称普通用户态恶意软件即可攻破 Google Password Manager，进而危及账户与 passkey。防御：关注终端上对浏览器凭据存储的异常访问。
- X 原帖：https://x.com/28zaaky/status/2116531603585515870
- 文章：https://0rcruxe.github.io/posts/pass-ta-key-golden-attack-sds-extraction/
- 地址／IoC：未见公开 IoC

### 2. 微软：追踪朝鲜威胁行为者对 AI 的采用
经 X 转述的微软报告（仅取得 Google News 跳转链接，未直接核对微软原文）。背景：前日 Binance 被盗归因朝鲜 TraderTraitor。
- X 原帖：https://x.com/compuchris/status/2116369573255545200
- 文章（Google News 跳转）：https://news.google.com/rss/articles/CBMiugFBVV95cUxNeVRiQjA5YVFOYjhEY1BKTnRoeEloU0RHZVVxM1FyT1Y1Y28yYUFEREVmWkI2T1ZOcWZ6WlVCMlJDZXNuUDROWklNVUtadDNxVGcwNGRDTmxNREZWa2pnTlVjdkd0d0ViNE9lcTkwekZzRl84bl9DREd5aFJQeFBITEFna2tXQmpYVmd0VGJqQ2R5RFI3VVRBYmg0SjNlYkVmSmdDeEp1MEY3SEdxTlpOaUxvTEx0c2c0R2c?oc=5
- 地址／IoC：未见公开 IoC

### 3. JavaScript .jsc 字节码反编译（恶意软件分析教学）
- X 原帖：https://x.com/Dinosn/status/2116534251256492136
- 视频：https://www.youtube.com/watch?v=oJTMIj4Cw7E
- 地址／IoC：未见公开 IoC

### 4. 勒索泄露站新增声称（FalconFeeds，未经核实）
Qilin（美国 Community Medical Center）、Rhysida（美国 Phoenix Charter Academy Network）、EMPERADOR（瑞士 Holcim、乌拉圭 Punta Shopping）、Sarcoma（美国 Ivan Smith Furniture，称 500GB）、WHITEARMOR（Gamdom）、Vexy（哥伦比亚 Jhamf Group）、SCARLETTGROUP（美国 Spencer's）。
- X 原帖：https://x.com/FalconFeedsio/status/2116608157309169916
- X 原帖：https://x.com/FalconFeedsio/status/2116530492069814483
- X 原帖：https://x.com/FalconFeedsio/status/2116474305991348315
- X 原帖：https://x.com/FalconFeedsio/status/2116624887427321889
- X 原帖：https://x.com/FalconFeedsio/status/2116519406058783120
- X 原帖：https://x.com/FalconFeedsio/status/2116516671959810494
- X 原帖：https://x.com/FalconFeedsio/status/2116642542813135282
- X 原帖：https://x.com/FalconFeedsio/status/2116372583398638040
- 地址／IoC：未见公开 IoC（仅受害方名称，泄露站地址未抄录）

## 地址／IoC 汇总

本窗口所有条目均未见公开 IoC（无 C2、IP、域名、钱包或样本哈希）。

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

本日 LWiS 成员时间线（随机抽 54 个 handle）21 条帖，安全相关仅 @28zaaky（passkey 研究）与 @pdiscoveryio（neo），其余多为闲聊（周六）。

## 来源搜索 URL

- X Latest（CVE/POC）：https://x.com/search?q=CVE%20OR%20PoC%20OR%20exploit%20OR%200day&f=live
- X Latest（GitHub 工具）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- X Latest（威胁报告）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- X Latest（Drupal）：https://x.com/search?q=CVE-2026-118539&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/
- Drupal 安全公告：https://www.drupal.org/security/contrib
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/ ；tl;dr sec：https://tldrsec.com/

说明：本次 X 采集走 Grok Bot 公共 X 只读接口（与浏览器 Latest 等价的检索），LWiS List 以成员备份中 54 个 handle 的时间线检索代替；无发帖／点赞／追踪等任何写操作。
