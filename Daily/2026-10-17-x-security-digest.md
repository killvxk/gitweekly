# X 安全情报晚报 · 2026-10-17

> 搜集窗口：圣地亚哥时间 **2026-10-16 20:15 至 2026-10-17 20:10**（America/Santiago／UTC-3，约 **23 小时 55 分**，接昨晚窗口，没有缺口）。X 搜索参数：`start_time=2026-10-16T23:15:00Z`，`end_time=2026-10-17T23:10:00Z`。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all` + `get_posts_by_ids`）。本轮接口没有回传 entities，t.co 链接全部用 HTTP 跳转逐条展开。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** A／B／C 三类各跑原始与去噪查询（A：CVE-2026／0day／actively exploited／PoC，另跑一轮排除 BeyondTrust／Ivanti／Patch Tuesday 的补充查询；B：`url:github.com` + C2／red team／nuclei／PoC，另跑 BOF／implant／EDR／pentest；C：malware analysis／threat report／threat actor，另跑 infostealer／backdoor／RAT + IOC／C2）。LWiS List 500 成员分 10 段 `from:` 批次全量翻查，外加核心媒体／厂商账号两批（DFIR_Radar／Dinosn／BleepingComputer／THN／securityaffairs／Huntress／Unit42 等，及 malwrhunterteam／Nulltap_／Volexity）。本轮共 **20 次 X 读取**（search_posts_all 19 次 + get_posts_by_ids 1 次），未触发限速。
> 窗口内去重后 **333** 条帖子（与 seen_ids 无重叠），剔除空转发、闲聊、广告、教学推销后，关键词粗筛得 **203** 条安全相关新帖：**A47／B36／C48／LWiS72**（多查询重叠时按最后命中批次归类）。下文实际引用约 100 条。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**：CISA KEV JSON（`/workspace/enrich-2026-10-17/kev.json`）；厂商／研究页存于 `/workspace/enrich-2026-10-17/web/`：Rank Math 官方事件 KB、Huntress、ConnectWise Trust Center、SpecterOps、Todyl、THN（ConnectWise／MALFEX）、Recorded Future TAG-217、Varonis Snowflake、Horizon3 Ivanti、Quentin Kaiser（Broadcom Wi-Fi）、STAR Labs YuanKong、ReversingLabs APT29、Citizen Lab AdFection、GStreamer SA-2026-0088、CERT-In CIAD-2026-0049、Help Net、Security Affairs、Industrial Cyber、Nulltap、jm33.me、Risky Business、tl;dr sec。**BleepingComputer 与 Cybersecurity Dive 对 curl 返回 403（Cloudflare），Wordfence 返回 202 空页**，相关要点取自 X 原帖与其他转述。GitHub API 查了 nuclei／nuclei-templates／Sliver／emp3r0r／BloodHound／NetExec／Mythic／impacket 的 releases：**本窗口无新 release**（最新仍是 emp3r0r v5.3.0，10-16 06:07 圣地亚哥，已在昨晚报告）。
> **CISA KEV：catalogVersion 2026.10.16／1748 条，Δ0**（周六无更新，与昨日相同）。**due_today（10-17）：4 条**——AhsayCBS **CVE-2026-105133**、**CVE-2026-105134**，Cisco Secure Email Gateway **CVE-2026-76519**，PAN-OS **CVE-2026-0322**。**newly_overdue（10-16 到期）：2 条**——Ivanti Connect Secure **CVE-2026-104935**、Windows Shell **CVE-2026-96951**。Apple 86950 与 AA26-281A 五条仍逾期。**未来 7 天到期：3 条**——Atlassian **CVE-2026-21589**（10-18）、BeyondTrust **CVE-2026-102764** 与 Fortinet **CVE-2025-61624**（10-19）。**仍未进 KEV**：Rank Math PRO **CVE-2026-111862**（在野供应链）、Magento BlockStrap 103849、Nextcloud/Collabora 110447、Langflow 105740、GitLab 97229、PwnEscape 99999 等。
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接作狩猎用途。泄露、入侵类声称一律标 **UNCONFIRMED／未验证**。

## 今日摘要

- **【供应链 · M365】ConnectWise Cloud Backup（原 SkyKick）OAuth 应用凭据被盗，继续扩大**：Microsoft Threat Intelligence 今日公布 IoC（AppId `506e08f9-6e9a-4da4-942b-a099a03644ae`、源 IP `144.172.64[.]128`、Python UA）；Huntress 确认 **162** 个租户被未授权登录，近 1,000 个 Entra 租户出现该 IP 登录（300+ 成功），并发现 10-15 有**第二波定向尝试**打 16 个政策／国安／贸易／关键矿产行业租户；ConnectWise 已于 **10-17 17:15 ET（18:15 圣地亚哥）**停用相关应用。THN 报 173 租户。要做：查「服务主体登录」而非用户登录，查 10-13 以来新加的应用凭据。
- **【供应链 · WordPress】Rank Math SEO PRO 3.0.123 被植入后门，CVE-2026-111862（CVSS 9.8，在野）**：10-15 20:02 UTC 至 10-16 07:12 UTC（即 10-15 17:02 至 10-16 04:12 圣地亚哥）下载的副本带恶意代码，连 `rank1cdn.com`、建 `wpsupport_*` 管理员、伪造 `wp-includes/class-wp-cache-util.php`。只升 3.0.124 不够，要按官方顺序清理。未进 KEV。
- **【供应链 · npm】MALFEX 新包 `imgdecode`**：原生 Node 插件里藏 DLL shellcode loader，注入 `dllhost.exe`，投 RAT／窃密；C2 `104.234.65[.]75:7007`。
- **【AI 平台】OpenCode 确认遭「大规模蒸馏攻击」**，1.4% 绑定外部 AI 供应商的 Console 用户受影响，用户报告密钥被盗刷（细节 UNCONFIRMED）。
- **【KEV 到期】今天到期 4 条**（Ahsay×2／Cisco SEG／PAN-OS），**Ivanti 104935 与 Windows 96951 今起逾期**。Horizon3 公开 Ivanti 104935 技术分析，狩猎点为入站 `X-DSCGI-PATH` 头 + 内存取证。
- **【研究】** Recorded Future 发布 TAG-217 打韩国金融机构（ARTEX）的扩展时间线；Varonis 公开 Snowflake 托管 PostgreSQL 五步提权到 OS RCE（已服务端修复）；Quentin Kaiser 在 Hexacon 公开 Broadcom Wi-Fi WPS 解析漏洞，无需密码即可 RCE 比利时 ISP 路由器（无 CVE）；PwnEscape（CVE-2026-99999）让云厂商周末紧急重启宿主机。
- **【PoC／工具】** Gigabyte `gdrv3.sys` 签名驱动 LPE PoC（BYOVD 狩猎）、Plex Media Server 未认证 RCE 链 `plex2shell`（≤1.43.3.10828）、Perplexity「Escaping SPACE」沙箱逃逸红队文与仓库、jm33「Linux C2 from Scratch」系列开篇。监控的红队工具本窗口无新版本。
- **【IoC 速记】** malwrhunterteam 一晚抛出多组：低检出 `setup.iso`（3 个域名＋3 个 IP）、中国「onlycn」Linux bot opendir、copyparty opendir、「SourceUse」C2 面板；AOMEI Backupper 后门 IoC（ManageEngine）；SalatStealer C2；YuanKong Android RAT；日本金融仿冒 Android RAT。全部在「地址／IoC 汇总」。

## CVE / POC / 漏洞

### 1. Rank Math SEO PRO 3.0.123 供应链后门 · CVE-2026-111862（CVSS 9.8，在野，未进 KEV）
Rank Math 官方确认：**10-15 20:02 UTC 至 10-16 07:12 UTC** 下载或经后台更新的 PRO 3.0.123 部分副本被植入恶意代码（同一版本号、内容不同，所以光看版本号不够，要看安装时间）。激活后可建管理员、外连 `rank1cdn.com`、每次访问自我重建后门、暴露 WordPress 密码、数据库凭据与 API 密钥。免费版不受影响。修复：有 10-15 之前的备份就还原并轮换全部凭据，再从官网账号装 3.0.124；没有备份就**先删整个 `rank-math-pro` 目录和三条 wp_options**，再封域名，再逐项清理（停用插件无效）。官方提醒不会用邮件发下载链接。
- X 原帖：
  - https://x.com/Cyberintelg/status/2111327625440334178
  - https://x.com/faisalahammadwp/status/2111354569813041648
  - https://x.com/IvanPerezF_/status/2111359161896173771
  - https://x.com/DailyDarkWeb/status/2111454243853082951
  - https://x.com/IntCyberDigest/status/2111467266911121776
  - https://x.com/Daily_CyberSec/status/2111310253673341095
  - https://x.com/LoreleiWeb/status/2111376954771292228
- 厂商公告：https://rankmath.com/kb/pro-3-0-123-security-incident/
- 文章：
  - https://www.wordfence.com/blog/2026/10/rank-math-seo-pro-3-0-123-malware/
  - https://securityonline.info/rank-math-seo-pro-compromise-exploited/
  - https://wpdeeply.com/rank-math-seo-pro-3-0-123-supply-chain-malware-cve-2026-111862/
- 地址／IoC：域名 `rank1cdn.com`；管理员用户名前缀 `wpsupport_`、邮箱后缀 `@wp-mail[.]net`；伪核心文件 `wp-includes/class-wp-cache-util.php`；wp_options 条目 `_uf6qdn2hmm`、`t8krdk990phb`、`_np5pvf754c`（X 帖写作 uf6qdn2hmm／np5pvf754c，官方 KB 带下划线前缀）；含 PHP 的 `.cache` 文件；cron 标记 `ms6v46`（出自 @IvanPerezF_ 帖）。

### 2. KEV 今日到期 · Cisco Secure Email Gateway CVE-2026-76519（CVSS 9.8，在野）
带特制附件的邮件可在开启 File Reputation 时以 root 写文件、执行命令。升级 Content Scanner Tools 到 25.3.0.5525 或更高。DFIR_Radar 建议 `grep "System Security"` 系统日志并查外联上传。CISA due **10-17（今天）**。
- X 原帖：
  - https://x.com/snypet86/status/2111242412408320294
  - https://x.com/DFIR_Radar/status/2111337001035456875
  - https://x.com/TheCyphere/status/2111344127560618210
- 厂商公告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-76519
- 地址／IoC：未见公开 IoC。

### 3. KEV 今日到期 · PAN-OS CVE-2026-0322；AhsayCBS CVE-2026-105133／105134
均 10-14 入列、due **10-17（今天）**。本窗口 X 上只有汇总帖提及（@TheExploitHQ），无新技术细节。cybermergemedia 提到本周九家大型安全公司市值合计蒸发约 1,700 亿美元，与 PAN-OS 事件同周。
- X 原帖：
  - https://x.com/TheExploitHQ/status/2111572541475373517
  - https://x.com/cybermergemedia/status/2111556880783032747
- CISA KEV：
  - https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-0322
  - https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-105133
  - https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-105134
- 地址／IoC：未见公开 IoC。

### 4. 今起逾期 · Ivanti Connect Secure CVE-2026-104935（CVSS 8.6，未认证 RCE）
CISA due 10-16 已过。Horizon3 公开技术分析（认证绕过）；DFIR_Radar 摘要：狩猎入站 `X-DSCGI-PATH` 请求头，并做内存取证，因为 Integrity Checker 看不到纯内存执行；@yogsec 称至少自 10-01 起被利用。
- X 原帖：
  - https://x.com/DFIR_Radar/status/2111518276740170205
  - https://x.com/yogsec/status/2111471990158811532
- 文章：https://horizon3.ai/attack-research/vulnerabilities/cve-2026-104935/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-104935
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-104935
- 地址／IoC：HTTP 请求头 `X-DSCGI-PATH`（行为指标）；未见公开 IP／哈希。

### 5. 今起逾期 · Windows Shell CVE-2026-96951（MotW 绕过，10 月补丁日 ~1,413 个漏洞中唯一在野零日）
- X 原帖：
  - https://x.com/chris_uk2026/status/2111351915422392725
  - https://x.com/yogsec/status/2111291382996291674
- 文章：https://www.securityweek.com/microsoft-patches-record-1413-vulnerabilities-including-exploited-windows-zero-day/
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-96951
- 地址／IoC：未见公开 IoC。

### 6. BeyondTrust Remote Support CVE-2026-102764（KEV，due 10-19）续报
自托管 RS 26.2.3 及更早版本需立即升级；暴露期未打补丁者按已失陷处理。ARMORY CASTLE 投放 PHP webshell SAWFLY 与 SOCKS5 隧道 BARECLAW，并在得手后删日志，建议把设备日志外送 SIEM。
- X 原帖：
  - https://x.com/V0iD_0daY/status/2111457721249644884
  - https://x.com/DFIR_Radar/status/2111473144867205212
  - https://x.com/DFIR_Radar/status/2111261881864270266
  - https://x.com/UpwindMDR/status/2111337742114214196
  - https://x.com/Python_s_/status/2111495862874706022
- 厂商公告：https://www.beyondtrust.com/trust-center/security-advisories/bt26-05
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-102764
- 文章：
  - https://www.bleepingcomputer.com/news/security/beyondtrust-patches-zero-day-exploited-in-attacks-since-august/
  - https://www.cybersecuritydive.com/news/china-espionage-beyondtrust-zero-day-hacker/833240/
- 地址／IoC：恶意工具名 SAWFLY、BARECLAW；本窗口帖子未给 IP／哈希（见昨晚报告的 GTIG 来源）。

### 7. Fortinet CVE-2025-61624（KEV，due 10-19）与 Atlassian CVE-2026-21589（KEV，due 10-18）
Fortinet CLI 路径遍历（需读写管理员权限），用于投放 PEERSTITCH；距 Fortinet 公告 185 天才入 KEV。Atlassian 多款 Data Center 产品，联邦截止 10-18（明天）。
- X 原帖：
  - https://x.com/Python_s_/status/2111495761804317011
  - https://x.com/_pksharma/status/2111541812091592715
  - https://x.com/UpwindMDR/status/2111517059318218823
  - https://x.com/Nulltap_/status/2111464549501296823
  - https://x.com/sara_sdegen/status/2111359296705351707
- 厂商／研究：https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/
- 文章：https://nulltap.sh/p/fortinet-cli-file-traversal/
- CISA KEV：
  - https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-61624
  - https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-21589
- 地址／IoC：未见公开 IoC。

### 8. PwnEscape · Linux 内核 CVE-2026-99999（来宾 VM 读宿主内存）续：云厂商周末紧急重启
发现者 @PaulosYibelo 致歉称全球 VPS／算力工程师周末都在打补丁重启宿主机；Red Hat 定为 Important（CVSS 8.8），IPv4 校验和元数据处理可被本地攻击者或不受信来宾 VM 触发内存破坏。@4ndaxu 指出作者未放出可直接运行的完整 PoC。
- X 原帖：
  - https://x.com/PaulosYibelo/status/2111541156572013043
  - https://x.com/4ndaxu/status/2111450734084694053
  - https://x.com/TheExploitHQ/status/2111572541475373517
  - https://x.com/ntlmrelay/status/2111412848345653406
- 文章：https://pwn.ai/blog/pwnescape
- CVE 记录：https://www.cve.org/CVERecord?id=CVE-2026-99999
- GitHub（第三方检测工具，未核实）：https://github.com/MChorfa/csumguard
- 地址／IoC：未见公开 IoC。

### 9. Snowflake 托管 PostgreSQL：五步权限链从非超级用户到 OS 级 RCE（Varonis）
绕过所有已公开缓解措施；Snowflake 已服务端修复，客户无需操作，但模式可能在其他托管 Postgres 复现（可篡改堆文件、WAL，持久化 SECURITY DEFINER 函数可熬过凭据轮换）。
- X 原帖：
  - https://x.com/DFIR_Radar/status/2111578725384937614
  - https://x.com/DFIR_Radar/status/2111578727867883749
- 文章：https://www.varonis.com/blog/remote-code-execution-in-snowflake-managed-postgresql
- 地址／IoC：未见公开 IoC。

### 10. Broadcom 私有 Wi-Fi（WPS）解析漏洞：空口无密码 RCE（Hexacon 10-16）
Quentin Kaiser 演示对比利时 Orange ASKEY TCG3000、Proximus BBOX3V+ 的未认证 RCE；问题自 2010 年起存在于 Broadcom SDK，Broadcom 称 2018 年已有修复但拒绝分配 CVE；研究者放出指纹识别工具包。未见在野利用，结果尚未独立复现。
- X 原帖：https://x.com/DailyDarkWeb/status/2111503562589257938
- 文章：https://quentinkaiser.be/security/2026/10/16/one-parser-two-bugs/
- 地址／IoC：未见公开 IoC。

### 11. PoC 仓库（只给链接作狩猎用，不转载内容）
- **Gigabyte `gdrv3.sys` 签名内核驱动 LPE 到 SYSTEM**（IOCTL 处理缺陷，BYOVD 风险，建议加入易受攻击驱动阻止列表）
  - X 原帖：https://x.com/culldrz4/status/2111374134651580659
  - GitHub／PoC：https://github.com/mein-0/KnockGiga
- **Plex Media Server 未认证 RCE 链 `plex2shell`**（影响 1.43.3.10828 及更早，升级 Plex）
  - X 原帖：https://x.com/ridvanyagli/status/2111377994539225151
  - GitHub／PoC：https://github.com/code-zm/plex2shell
- **iOS 13.0–26.0 n-day「darksword」内核利用偏移自动化**（越狱研究向）
  - X 原帖：https://x.com/twili8t/status/2111553841036472530
  - GitHub：https://github.com/twili8/auto-darksword
- **macOS 链（theevilbit）**：App TCC 绕过 → 无交互「DirtyNib」注入任意 GUI 应用 → 更多 TCC 绕过 + 完整 LPE；仅公告，未放细节，已报 Apple。
  - X 原帖：https://x.com/theevilbit/status/2111343754774974668
- 地址／IoC：未见公开 IoC。

### 12. 其他补丁与持续跟踪
- **GStreamer RTP 音频堆溢出**（SA-2026-0088／ZDI-26-775，潜在 RCE）
  - X 原帖：https://x.com/Python_s_/status/2111358711574778319
  - 厂商公告：https://gstreamer.freedesktop.org/security/sa-2026-0088.html
  - ZDI：https://www.zerodayinitiative.com/advisories/ZDI-26-775/
- **Jackson 2.21.8／2.18.12**（各含 7 个 CVE 修复）
  - X 原帖：https://x.com/fasterxml/status/2111554325495664762 、https://x.com/fasterxml/status/2111529777085718787
  - GitHub：https://github.com/FasterXML/jackson/wiki/Jackson-Release-2.21.8 、https://github.com/FasterXML/jackson/wiki/Jackson-Release-2.18.12
- **GitHub Enterprise Server push-option 注入 RCE CVE-2026-3854**（来源为聚合站，待厂商核实）
  - X 原帖：https://x.com/dailycve/status/2111405324976410666
  - 文章：https://dailycve.com/github-enterprise-server-push-option-injection-rce-cve-2026-3854-critical-dc-oct2026-3328/
- **Nextcloud／Collabora CVE-2026-110447（在野，未进 KEV）**：https://x.com/sh3ll_c0d3/status/2111399321484587088 ；https://securityarsenal.com/blog/cve-2026-110447-critical-collabora-online-rce-in-nextcloud-under-active-exploitation-detection-and-remediation-guide
- **Magento／Adobe Commerce BlockStrap CVE-2026-103849（未进 KEV）**：https://x.com/SecurityAr58409/status/2111505993850925509 ；https://securityarsenal.com/blog/cve-2026-103849-critical-blockstrap-rce-in-magento-and-adobe-commerce-detection-hunting-and-remediation-guide
- **Langflow CVE-2026-105740（蜜罐记录 1,423 次尝试，升 1.9.0+）**：https://x.com/ThreatAlis/status/2111296895993762045
- **Joplin CVE-2026-55105（XSS→RCE，CVSS 7.7）**：https://x.com/HugoValters/status/2111310735556972567 ；https://www.valtersit.com/cve/CVE-2026-55105/
- ThreatWire 上线免费 PoC Finder（CVE→公开 PoC 引用＋KEV 状态）：https://x.com/ThreatWire_/status/2111345678890742185 ；https://www.threatwire.tech/tracker/poc
- 地址／IoC：未见公开 IoC。

## 工具与 GitHub 发布

监控清单（nuclei／nuclei-templates／Sliver／emp3r0r／BloodHound／NetExec／Mythic／impacket）**本窗口无新 release**；最新分别为 nuclei v3.11.1、nuclei-templates v10.5.0、Sliver v1.7.8、emp3r0r v5.3.0（10-16）、BloodHound v9.8.0、NetExec v1.5.1、Mythic v3.4.0.5、impacket 0.13.1。
- https://github.com/jm33-m0/emp3r0r/releases/tag/v5.3.0

### 1. Perplexity「Escaping SPACE, Part I」红队沙箱逃逸文 + 仓库
- X 原帖：https://x.com/Astrodevil_/status/2111393112220414315
- 文章：https://www.perplexity.ai/hub/blog/escaping-space-part-i
- GitHub：https://github.com/perplexityai/SPACE

### 2. jm33（emp3r0r 作者）「Linux C2 from Scratch」系列 0x00
- X 原帖：https://x.com/jm33_m0/status/2111260603084136660
- 文章：https://jm33.me/linux-c2-from-scratch-0x00-processes-syscalls-libc-and-tls.html

### 3. 蓝队／AD 工具（DirectoryRanger 转荐，非本窗口新版本）
- PersistenceSniper（Windows 持久化狩猎 PowerShell 模块）：https://x.com/DirectoryRanger/status/2111550400671146459 ；https://github.com/last-byte/PersistenceSniper
- AD_Miner（AD／Entra ID 审计）：https://x.com/DirectoryRanger/status/2111550193988702348 ；https://github.com/AD-Security/AD_Miner

### 4. 新出的小型安全工具（未审计，谨慎使用）
- agentsniff（被动／主动探测网络内 AI agent）：https://x.com/triplenickel/status/2111572613080166518 ；https://github.com/ThirdKeyAI/agentsniff
- ship-safe（本地确定性 AI／MCP 安全扫描，SARIF 输出）：https://x.com/EsGeeks/status/2111481961147433310 ；https://github.com/asamassekou10/ship-safe
- pentestplate（渗透项目／发现跟踪模板）：https://x.com/CaptureTheFlg/status/2111332144190808555 ；https://github.com/SentinelSAST/pentestplate
- SOC Prime LogTotal（上传日志跑检测规则）：https://x.com/cyb3rops/status/2111519772999331942
- P2Patch（利用引导的漏洞修复，论文＋代码）：https://x.com/FSFG/status/2111380611910828234 ；https://arxiv.org/abs/2610.20245 ；https://github.com/P2Patch/P2patch
- 地址／IoC：未见公开 IoC。

## APT / Malware 分析

### 1. ConnectWise Cloud Backup（SkyKick）OAuth 应用供应链入侵 M365 租户（续，今日大幅更新）
攻击者用 ConnectWise 自家租户里的应用凭据（client assertion）以服务主体身份在 10-15 06:13–08:34 UTC（03:13–05:34 圣地亚哥）按 GUID 顺序脚本化登录各客户租户，拿 Graph 令牌做侦察并尝试给服务主体加凭据当后门。Huntress：确认 162 租户；近 1,000 租户有该 IP 登录、300+ 成功；10-13/14 同 IP 对四家律所密码喷洒；10-15 第二波定向尝试 16 个政策／国安／贸易／关键矿产行业租户（未成功）；10-17 17:15 ET ConnectWise 停用相关应用。Microsoft 给出 AppId、IP、UA，Defender 告警名「Suspicious sign-in」「Graph API activity from a Microsoft threat intelligence IP address」「Verified Threat Actor IP」。THN 报 173 租户。暂无确认数据外泄。
- X 原帖：
  - https://x.com/MsftSecIntel/status/2111355916318581020
  - https://x.com/HuntressLabs/status/2111468907517399310
  - https://x.com/DFIR_Radar/status/2111503131377078549
  - https://x.com/DFIR_Radar/status/2111488059204145238
  - https://x.com/DFIR_Radar/status/2111563605078630429
  - https://x.com/cybermergemedia/status/2111479297915687256
  - https://x.com/Nulltap_/status/2111423034540151249
  - https://x.com/Python_s_/status/2111495660210123066
- 厂商公告：
  - https://www.connectwise.com/company/trust/advisories
  - https://msft.it/6013aQBvV （Microsoft 帖中链接，实际跳转到 https://status.connectwise.com/）
- 文章：
  - https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access
  - https://specterops.io/blog/2026/10/17/connectwise-skykick-breach-microsoft-365/
  - https://www.todyl.com/blog/investigation-unauthorized-access-through-the-connectwise-cloud-backup-microsoft-365-app
  - https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html
  - https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/
  - https://nulltap.sh/p/connectwise-backup-tenant-access/
- 地址／IoC：IP `144.172.64[.]128`（AS14956 RouterHosting）；AppId `506e08f9-6e9a-4da4-942b-a099a03644ae`；应用名 ConnectWise Cloud Backup，发布者 SkyKick；UA `Python-urllib/3.12`、`python-requests/2.31`、`python-requests/2.34.2`。

### 2. MALFEX npm 供应链：`imgdecode` 原生插件 shellcode loader
自 2023-08-06 起活动，发布者 malfexkkj、malfex_user、malfexteste2/3/4、malfexteste8；`imgdecode` 1.0.3（10-11 发布，979 次下载）完全自包含：DLL 检查开发者终端后从 GitHub 仓库 `cavecrew/proj` 拉 `banner.jpg`，用密钥解密后注入 `dllhost.exe`；解出图片头即停（运营者可远程关停）。早期链投放 Go 程序 `%APPDATA%\Microsoft\Windows\node_runtime_helper.exe` 和窃密程序「movinlike」，三个包投 Overlord RAT；计划任务 `MicrosoftEdgeUpdateService` 持久化。
- X 原帖：
  - https://x.com/DFIR_Radar/status/2111427640527917069
  - https://x.com/OrizonSignals/status/2111419504274125184
  - https://x.com/OffensiveLab/status/2111466167453807051
- 文章：https://thehackernews.com/2026/10/malfex-npm-package-imgdecode-hides.html
- 地址／IoC：C2 `104.234.65[.]75:7007`、下载 `104.234.65[.]75:700`；npm 包 `imgdecode`、`cdn-img-fetch`、`img-to-native`、`native-runner`；GitHub 仓库 `cavecrew/proj`（文件 banner.jpg）；落地路径 `%APPDATA%\Microsoft\Windows\node_runtime_helper.exe`；计划任务名 `MicrosoftEdgeUpdateService`。

### 3. OpenCode 遭「大规模蒸馏攻击」（UNCONFIRMED 细节）
OpenCode 10-17 在 X 上确认夜间遭入侵，1.4% 绑定外部 AI 供应商的 Console 用户受影响，已邮件通知，正与 Anthropic／OpenAI／Google 处置；用户报告密钥被盗刷。建议受影响者在各供应商处吊销重发密钥并查用量。入侵途径未公布。
- X 原帖：
  - https://x.com/opencode/status/2111519637049319818
  - https://x.com/DailyDarkWeb/status/2111535741285335434
- 地址／IoC：未见公开 IoC。

### 4. AOMEI Backupper 远程访问后门（UNC7017 短窗供应链续，ManageEngine IoC）
- X 原帖：
  - https://x.com/LandscapeThreat/status/2111591111617892366
  - https://x.com/rst_cloud/status/2111474713411166385
- 文章：https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering/
- 地址／IoC（原样抄录）：`8[.]218[.]65[.]184:41397`；`hxxps://promotion[.]storagedata[.]com/download/abpopup/upgrade-now[.]zip`；SHA-256 `a984fdb0830760446d2b599b263506e01fcf1e560a31a057c3bbe7b3f8ac155d`、`2e3b4bfb86224f079b8762ce78bb7ff10afdbf8421b08b23e96429f2e1ee7b50`、`130c3970f1c900191615b99d8be522d6a488a3d3b73938896ed937092007d96a`、`53b7d01163ccb679001f20e4a8a5e1f33d5d2837c375315f6514cc820f81bd12d167bc898e856da8a4003cb4dfc7de55fea109eee3cd64fc8999710314109464`（原帖如此，128 位，疑为两个哈希粘连）、`5837bc26a73cfb46ffd466cf889f03ce2f6a48f1f3fd42ec8be22189d51cab1e`、`100657d3e205bfd0e96f1c088ae1739b50657592a696201467b4c65b7d36289a`。

### 5. TAG-217（疑似中文背景）打韩国金融机构 · ARTEX（Recorded Future Insikt）
早在 2026-08 就在测试基础设施、组装工具；公开报道称至少 7 家金融机构、6.8 万人数据外泄；工具含加密钱包文件窃取、Linux 提权与弱点测试组件。
- X 原帖：
  - https://x.com/DFIR_Radar/status/2111548774694678786
  - https://x.com/DFIR_Radar/status/2111548777110618183
- 文章：https://www.recordedfuture.com/blog/tag-217-artex-south-korean-banks
- 地址／IoC：本窗口帖子未列；见报告原文。

### 6. malwrhunterteam 一晚多组新样本／基础设施
- 低检出 `setup.iso`（数百文件、异常外联），样本已上传 MalwareBazaar：
  - X 原帖：https://x.com/malwrhunterteam/status/2111569589209555362 、https://x.com/malwrhunterteam/status/2111570403923488983 、https://x.com/malwrhunterteam/status/2111570649986871574 、https://x.com/malwrhunterteam/status/2111570993806503967 、https://x.com/malwrhunterteam/status/2111571171816988717 、https://x.com/malwrhunterteam/status/2111571957212926311 、https://x.com/malwrhunterteam/status/2111572714200981744 、https://x.com/malwrhunterteam/status/2111573101297406364 、https://x.com/smica83/status/2111578710801600641
  - 样本：https://bazaar.abuse.ch/sample/36805ebcc0c295751c9b858fc9bbe75ba46362c672f860eafb73ec67f7ce8a4b/
- 疑似中国「onlycn」Linux bot（opendir 中 `cl-amd64` 低检出，脚本含大量中文注释）：
  - X 原帖：https://x.com/malwrhunterteam/status/2111559058348024065 、https://x.com/malwrhunterteam/status/2111560829506109444 、https://x.com/smica83/status/2111561639451328684
  - 样本：https://bazaar.abuse.ch/sample/317961c5a931f95d343d76898a161396baddb7ef1c5d8984d968c8e858d9ccfa/
- 「copyparty @ WIN-DTNS8IK8FVG」opendir 及下一阶段样本：
  - X 原帖：https://x.com/malwrhunterteam/status/2111524741043359984 、https://x.com/smica83/status/2111533556686008448
  - 样本：https://bazaar.abuse.ch/sample/f61d7feb73cb78573d419cd9e8191bcacb86527f9349bb280dc3a891607dac6b/ 、https://bazaar.abuse.ch/sample/8ae4f5c9dc93ac6caceeccf54ac5bc176031fff59d2d1d98363d73e1e40f19ee/
- 「SourceUse」C2 面板：
  - X 原帖：https://x.com/malwrhunterteam/status/2111515505282408472
- 地址／IoC：见汇总节（域名 jumalputty／nizariuserp／crataga，IP 94.26.0[.]118、195.63.130[.]47、79.132.128[.]88、45.198.224[.]91、108.187.43[.]139、91.92.40[.]28，面板域名 sourceuse[.]cyou、callmylove[.]cyou，以及 4 个 SHA-256）。

### 7. SalatStealer（WEB_RAT）仍活跃（Huntbackio）
176.12.71[.]122 上 990 字节 `config.json` 是面板引导文件，TLS 证书关联轮换 C2。
- X 原帖：https://x.com/Huntbackio/status/2111430099538948116
- 地址／IoC：`176.12.71[.]122`；`wruser[.]org`、`salator[.]es`、`websalat[.]top`。

### 8. Android：YuanKong RAT（STAR Labs）与日本金融仿冒 RAT
- YuanKong：多租户 Android RAT，操作者 ID 明文编进 DEX；110 个 dropper、57 个子载荷、42 个操作者账号；Socket.IO/WebSocket C2。
  - X 原帖：https://x.com/rst_cloud/status/2111520222330978617
  - 文章：https://starlabs.sg/blog/2026/10-yuankong-rat-the-android-remote-control-service-that-stamps-its-operators-names-into-every-build/
  - 地址／IoC：`apppanda.xyz`、`ktxapp.com`、`ktx123.net`、`206.82.1.14`；子载荷签名证书 SHA-256 `73cbe8e3730cacfdd208f22eab468bb5495a78c0eb2cb37eff5af0cafe321387`。
- 日本金融／税务／交友仿冒的 64 个样本背后同一 RAT（鹰标面板，WebSocket + Ed25519 + 证书钉扎，无线 ADB SPAKE2 自配对提权，盯支付宝／微信支付字段）。
  - X 原帖：https://x.com/DFIR_Radar/status/2111382345924190453
  - 地址／IoC：dropper SHA-256 `24e58e12c24180abf800f142b83348b318f60894f94571a68eea98481abd84f0`；包名 `com.nova.core.high`、`com[.]open.stone[.]love`；库 `libnauth[.]so`、`libspake2[.]so`、`libdxs[.]so`。

### 9. APT29（Midnight Blizzard）：RL 从两个哈希还原战役（10-15 报告，今日 X 扩散）
- X 原帖：https://x.com/rst_cloud/status/2111482307282387213
- 文章：https://www.reversinglabs.com/blog/how-rl-mapped-a-midnight-blizzard-linked-campaign-from-two-hashes
- 地址／IoC：`ms365-live.com`、`owa-ms365.com`（rst_cloud 摘录）。

### 10. 其他威胁情报
- **以色列雇佣间谍软件经网页广告零点击投放（Citizen Lab AdFection 续）**，vxunderground 评论：https://x.com/vxunderground/status/2111591780026028424 ；https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/ （未见公开 IoC）
- **朝鲜 IT 工人冒用美国身份赚 300 万美元**：https://x.com/securityaffairs/status/2111495066074353834 ；https://securityaffairs.com/201193/intelligence/north-korean-it-workers-used-stolen-us-identities-to-earn-3-million.html （未见公开 IoC）
- **法国超市经暴露的 Danfoss AK-SC／AK-SM 与 Copeland XWEB 冷链控制器被攻击**：https://x.com/DFIR_Radar/status/2111593888100073482 ；https://industrialcyber.co/control-device-security/french-supermarket-cyberattack-exposes-risks-of-unsecured-remote-access-and-legacy-refrigeration-systems/ （未见公开 IoC）
- **MONST3R-AI：攻击者粘贴被盗 OpenAI／Anthropic／Google 密钥，让受害者为自动扫描买单**：https://x.com/DFIR_Radar/status/2111533453917266124 ；https://www.helpnetsecurity.com/2026/10/16/stolen-ai-api-keys-autonomous-scans/ （未见公开 IoC）
- **CERT-In CIAD-2026-0049（Critical）：AI 模型评测中 agent 触达印度机构真实系统；另有人滥用开源 agent 攻击框架**：https://x.com/DailyDarkWeb/status/2111551047298900400 ；https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0049&pageid=PUBVLNOTES02
- **Volexity Volcano 在清理后的内存中找回浏览器利用痕迹**：https://x.com/Nulltap_/status/2111509792275742826 ；https://nulltap.sh/p/volexity-volcano-recovers-browser-traces/
- **KGB RAT 新变种（直接系统调用内存掏空＋惊吓音频）**，单一博客来源，待核实：https://x.com/sh3ll_c0d3/status/2111428516415696958 ；https://sh3llc0d3.com/blog/kgb-rat-threat-analysis-dissecting-the-stealth-infostealer-and-psychological-disorientation-vectors/
- DFIR 周回顾（UNC7017／ARMORY CASTLE／UTA0576）：https://x.com/DFIR_Radar/status/2111465139052388415
- **泄露／入侵声称（均 UNCONFIRMED）**：印度计算机学会 CSI 全库 https://x.com/DailyDarkWeb/status/2111585091449422308 ；保加利亚 Ekont 约 320 万订单 https://x.com/DailyDarkWeb/status/2111430190853464292 ；塞尔维亚 Triglav 52.5 万条 https://x.com/MonThreat/status/2111515622542578007 ；土耳其呼叫中心 UlakCX https://x.com/DailyDarkWeb/status/2111553925774184455 ；委内瑞拉油气供应商 InTech https://x.com/DailyDarkWeb/status/2111569372326281364 。**已确认**：日本 Yellow Hat 确认 180 万会员数据泄露 https://x.com/DailyDarkWeb/status/2111471845321084952 ；公告 PDF https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261015/20261015551180.pdf

## 地址／IoC 汇总

> 原样抄录，保持去武装格式；仅供检测与封堵，勿直接访问。

| 来源 | 类型 | 指标 |
|---|---|---|
| ConnectWise／SkyKick（Microsoft、Huntress） | IP | `144.172.64[.]128`（AS14956 RouterHosting） |
| ConnectWise／SkyKick | AppId | `506e08f9-6e9a-4da4-942b-a099a03644ae` |
| ConnectWise／SkyKick | UA | `Python-urllib/3.12`、`python-requests/2.31`、`python-requests/2.34.2` |
| Rank Math PRO 3.0.123 | 域名 | `rank1cdn.com` |
| Rank Math PRO 3.0.123 | 账号／文件／选项 | `wpsupport_*`、`@wp-mail[.]net`、`wp-includes/class-wp-cache-util.php`、`_uf6qdn2hmm`、`t8krdk990phb`、`_np5pvf754c`、cron `ms6v46` |
| MALFEX npm | C2／下载 | `104.234.65[.]75:7007`、`104.234.65[.]75:700` |
| MALFEX npm | 包／仓库／路径 | `imgdecode`、`cdn-img-fetch`、`img-to-native`、`native-runner`、GitHub `cavecrew/proj`、`%APPDATA%\Microsoft\Windows\node_runtime_helper.exe`、任务 `MicrosoftEdgeUpdateService` |
| AOMEI Backupper 后门 | IP:端口 | `8[.]218[.]65[.]184:41397` |
| AOMEI Backupper 后门 | URL | `hxxps://promotion[.]storagedata[.]com/download/abpopup/upgrade-now[.]zip` |
| AOMEI Backupper 后门 | SHA-256 | `a984fdb0830760446d2b599b263506e01fcf1e560a31a057c3bbe7b3f8ac155d`、`2e3b4bfb86224f079b8762ce78bb7ff10afdbf8421b08b23e96429f2e1ee7b50`、`130c3970f1c900191615b99d8be522d6a488a3d3b73938896ed937092007d96a`、`53b7d01163ccb679001f20e4a8a5e1f33d5d2837c375315f6514cc820f81bd12d167bc898e856da8a4003cb4dfc7de55fea109eee3cd64fc8999710314109464`（原文粘连）、`5837bc26a73cfb46ffd466cf889f03ce2f6a48f1f3fd42ec8be22189d51cab1e`、`100657d3e205bfd0e96f1c088ae1739b50657592a696201467b4c65b7d36289a` |
| malwrhunterteam setup.iso | 域名→IP | `jumalputty[.]com`→`94.26.0[.]118`；`nizariuserp[.]com`→`195.63.130[.]47`；`crataga[.]site`→`79.132.128[.]88` |
| malwrhunterteam setup.iso | SHA-256 | `36805ebcc0c295751c9b858fc9bbe75ba46362c672f860eafb73ec67f7ce8a4b` |
| onlycn Linux bot | opendir／SHA-256 | `http://45.198.224[.]91:42222/`；`317961c5a931f95d343d76898a161396baddb7ef1c5d8984d968c8e858d9ccfa` |
| copyparty opendir | opendir／SHA-256 | `http://108.187.43[.]139:8080/`；`f61d7feb73cb78573d419cd9e8191bcacb86527f9349bb280dc3a891607dac6b`、`8ae4f5c9dc93ac6caceeccf54ac5bc176031fff59d2d1d98363d73e1e40f19ee` |
| SourceUse C2 面板 | 域名／IP | `https://sourceuse[.]cyou/`、`https://callmylove[.]cyou/`、`http://91.92.40[.]28:7777/` |
| SalatStealer | IP／域名 | `176.12.71[.]122`；`wruser[.]org`、`salator[.]es`、`websalat[.]top` |
| YuanKong RAT | 域名／IP／证书 | `apppanda.xyz`、`ktxapp.com`、`ktx123.net`、`206.82.1.14`；证书 SHA-256 `73cbe8e3730cacfdd208f22eab468bb5495a78c0eb2cb37eff5af0cafe321387` |
| 日本金融仿冒 Android RAT | SHA-256／包名 | `24e58e12c24180abf800f142b83348b318f60894f94571a68eea98481abd84f0`；`com.nova.core.high`、`com[.]open.stone[.]love` |
| APT29（RL） | 域名 | `ms365-live.com`、`owa-ms365.com` |
| Ivanti 104935 | 行为 | 入站请求头 `X-DSCGI-PATH` |
| BeyondTrust 102764 | 工具名 | SAWFLY（PHP webshell）、BARECLAW（SOCKS5 隧道） |

其余条目（Cisco SEG、PAN-OS、Ahsay、Windows 96951、Fortinet、Atlassian、PwnEscape、Snowflake、Broadcom Wi-Fi、OpenCode、TAG-217、各 PoC 仓库）：**未见公开 IoC**。

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

本日 LWiS 成员高信号：@malwrhunterteam（多组新样本）、@theevilbit（macOS TCC/LPE 链）、@jm33_m0（Linux C2 系列）、@vxunderground（雇佣间谍软件评论）、@PaulosYibelo（PwnEscape）、@ntlmrelay（本周热门链接：PwnEscape、Calif「Big Fish」、Citizen Lab AdFection、Anthropic ECDSA 曲线研究）、@cyb3rops（LogTotal）、@DirectoryRanger（工具转荐）、@Dinosn（ConnectWise／朝鲜 IT 工人）。tl;dr sec 最新仍为 #350（10-15）。

## 来源搜索 URL

- A（CVE／0day／PoC）：https://x.com/search?q=%28CVE-2026%20OR%200day%20OR%20zero-day%20OR%20%22actively%20exploited%22%20OR%20PoC%29%20-is%3Aretweet&f=live
- A 补充：https://x.com/search?q=%28CVE-2026%20OR%20CVE-2025%29%20%28exploit%20OR%20PoC%20OR%20RCE%29%20-BeyondTrust%20-Ivanti&f=live
- B（GitHub 红队／C2）：https://x.com/search?q=url%3Agithub.com%20%28C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20PoC%29%20-is%3Aretweet&f=live
- B 补充：https://x.com/search?q=url%3Agithub.com%20%28BOF%20OR%20implant%20OR%20EDR%20OR%20pentest%29&f=live
- C（威胁报告）：https://x.com/search?q=%28%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%29%20-is%3Aretweet&f=live
- C 补充：https://x.com/search?q=%28infostealer%20OR%20backdoor%20OR%20RAT%29%20%28IOC%20OR%20C2%20OR%20sha256%29&f=live
- 供应链：https://x.com/search?q=%22Rank%20Math%22%20malware%20OR%20%22OpenCode%22%20breach&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
