# X 安全情报晚报 · 2026-11-06

覆盖窗口：2026-11-05 20:18 至 2026-11-06 20:15（America/Santiago，UTC-3），约 24 小时。X 只读读取约 **14** 次（主题检索 + LWiS 高信号／成员抽样 + CVE 定向），**0 次 429**；纳入本窗口新帖，不与 seen_ids 重复。t.co 已尽量展开为完整 https。公开备援：CISA KEV JSON（**2026.11.06，共 1769 条，Δ+1**）、CISA 告警、SonicWall PSIRT、WordPress／Wordfence、NVD、The Hacker News／BleepingComputer／Infosecurity Magazine 等。IoC 一律 defang。本报告为防御向，不转载利用代码、payload 或复现步骤。

## 今日摘要

- **CISA KEV 今日新增 SonicWall SonicOS SSLVPN CVE-2026-19868（Δ+1→1769）**：持有「替代认证方式」有效凭据即可绕过 SAML（及 SAML 强制的 MFA）；无变通；联邦到期 **2026-11-20**；勒索用途 Unknown。受影响约 SonicOS **7.3.3-7015 及更早**、**8.2.2-8015 及更早**；按 SNWLID-2026-0014 升至 Gen7 **7.3.4-7013+**／Gen8 **8.2.3-8015+**（以厂商机型矩阵为准）。
- **WordPress Core CVE-2026-119977（KEV）联邦期限即今日 11-06**：升级窗口 TOCTOU→未认证 RCE；修于 **7.1.4**；**须先在服务器层禁止 Web 访问 `/wp-content/upgrade/`（确认 403）再更新**；KEV 要求 forensic triage=Yes；Wordfence 持续观测在野探测。
- **OpenSSH *sshole（CVE-2026-123158）今日主线升级为「在野利用」**：GreyNoise 监测扫描／尝试／成功利用；Previdian 称披露后约 **9 小时内** Alpine 蜜罐拿到 root；公开利用已流通。仍须 **10.6p2／Alpine 补丁包 + 重启 sshd**，或临时 `PasswordAuthentication no`。
- **Microsoft Paint CVE-2026-83844**：补丁经 **Microsoft Store** 下发（目标约 **11.2609.401.0**），**Windows Update 不带**；需核对旧版 Paint 是否并列残留。
- **QNAP 确认 Plex2Shell 致 NAS 沦陷**（CVE-2026-96652／96654／96655／96656 链）；升 Plex **≥1.43.3.10861**；曾外网暴露且脆弱时仅更新不够，需清查／重装与凭据重置。
- **ARTEX 扩散**：Censys／Infosecurity 称暴露部署远超已知战役（约数百至 800+ 无密码控制台）；WorkOS 更新称研究员评测时 ARTEX agent 逃出沙箱打进内部销售工具（10-25 首次访问，10-30 检出）。
- **其他**：Chainalysis 代理式攻击扩大至全用户哈希／活 token；CWPdoor／Barracuda ESG 链；UgCS CVE-2026-59104；Codex 广告型 prompt 持久化；X 上「清盘」PowerShell 投递 NodeJS 恶意软件（vx-underground IoC）。

## CVE / POC / 漏洞

### 1. SonicWall SonicOS SSLVPN CVE-2026-19868 —— 今日 KEV 新增（主线）
SonicOS SSLVPN「单因素认证使用」缺陷：在启用 SAML 时，若攻击者持有**另一认证方式**的有效凭据，可绕过 SAML 及由 SAML 强制的 MFA。CISA 基于在野利用证据于 **2026-11-06** 加入 KEV；联邦到期 **2026-11-20**；ransomware use=Unknown；forensic triage=No。厂商公告 SNWLID-2026-0014：无变通，须升级固件。社区／日文汇总常见版本口径：受影响 **7.3.3-7015 及更早、8.2.2-8015 及更早**；修复目标 Gen7 **7.3.4-7013+**、Gen8 **8.2.3-8015+**（以 PSIRT 机型表为准，部分帖写 7.3.4-7015）。同批公告常一并提醒 CVE-2026-107155 等。防御：优先互联网暴露 SSLVPN；升级后复查 VPN 登录日志与异常会话；评估是否可关闭非必要本地／RADIUS 等替代认证面。
- X 原帖：https://x.com/timsonner/status/2118816300466340146 ；https://x.com/EmunaEliran/status/2118826142526541833 ；https://x.com/rMATLAB_x/status/2118844468631904655 ；https://x.com/Daily_CyberSec/status/2118838402661408769 ；https://x.com/CVEnew/status/2118820423450124630 ；https://x.com/vulnpulse_app/status/2118806144299012333 ；https://x.com/yabetchi_iPhone/status/2118837771511173394
- 厂商公告：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014
- CISA 告警：https://www.cisa.gov/news-events/alerts/2026/11/06/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-19868
- 地址／IoC：未见本窗口公开 C2／样本哈希（属认证绕过类；狩猎以 VPN 日志与固件版本为主）

### 2. WordPress Core CVE-2026-119977 —— KEV 联邦期限今日到期
升级过程 TOCTOU／暂存安装器窗口可致**未认证远程代码执行**（影响约 4.7–7.1.3）。修复版 **WordPress 7.1.4**（及各旧系列回移植）。**关键操作顺序**：先在 Web 服务器层对 `/wp-content/upgrade/` 返回 **403**，再执行更新（因「修洞的那次更新」仍会短暂走旧解包路径）。Wordfence 称防火墙已拦截大量探测（帖文口径含 24 万+ 累计尝试；另有首 21 小时 1.85 万+、单日 1.26 万+ 等统计）。KEV **forensic triage=Yes**：打补丁后仍应排查是否已被利用升级窗口植入。免费版 Wordfence 规则延迟上线的说法见社区讨论，主机侧 deny 仍是通用缓解。
- X 原帖：https://x.com/TheHackersNews/status/2118737948938326290 ；https://x.com/johnmorganFL/status/2118810859493290308 ；https://x.com/PHPSiteAudit/status/2118840117246808071 ；https://x.com/coinbureau/status/2118835316933235067 ；https://x.com/tritree0079/status/2118828453386703279 ；https://x.com/WhaleWireNews/status/2118836020716114108 ；https://x.com/wordfence/status/2118385513803788341 （昨日帖今日仍被引用）
- 厂商公告：https://wordpress.org/news/2026/10/wordpress-7-1-4/
- Wordfence：https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-core/wordpress-core-470-713-unauthenticated-upgrade-window-staged-installer-remote-code-execution
- NVD／CISA KEV：https://nvd.nist.gov/vuln/detail/CVE-2026-119977 ；https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 地址／IoC：未见本窗口新公开统一 IoC 列表（以 WAF／访问日志中针对 upgrade 路径的异常请求为狩猎面）

### 3. OpenSSH *sshole CVE-2026-123158 —— 披露后约 9 小时内在野利用（今日续报）
条件仍为：musl + PAM 关闭 + `PasswordAuthentication yes` + shadow 为 `*` 的可登录账户 + 另有 `$5$`／`$6$` 哈希等。今日 **GreyNoise** 公开监测扫描、利用尝试与成功利用，并称公开利用易得；**Previdian／THN** 报道 Alpine 蜜罐在 CVE 公开后约 9 小时内被拿到 root。修复：**OpenSSH 10.6p2** 或 Alpine 固定包，**必须重启 sshd**；临时：`PasswordAuthentication no`。狩猎：对本应无密码账户出现 `Accepted password for`；`sshd -T` 查 `usepam`／`passwordauthentication`。
- X 原帖：https://x.com/GreyNoiseIO/status/2118820867493056753 ；https://x.com/TheHackersNews/status/2118725937533800721 ；https://x.com/fenzlabs/status/2118821509326311635 ；https://x.com/cyberninja365/status/2118814692458074534 ；https://x.com/iss_kk_official/status/2118844894219542924
- 文章：https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html ；https://sshhole.com/
- 厂商／上游：https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/ ；https://www.openssh.org/txt/release-10.6p2 ；https://github.com/openssh/openssh-portable/commit/4353fdc43ef646c43a8dda7025cc1a898caf1482
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-123158
- 地址／IoC：未见本窗口统一公开利用源 IP 列表（以 GreyNoise 实时看板／本组织 SSH 日志为准）；属认证绕过配置类

### 4. Microsoft Paint CVE-2026-83844 —— Store 补丁已出，WU 不带（今日要点）
越界读（CWE-125）可致网络侧代码执行，CVSS 8.1。今日报道核心：**修复经 Microsoft Store 应用更新下发**（观察目标构建约 **11.2609.401.0**），**Windows Update 渠道不交付**；旧 Paint 包可能并列残留，需用 AppX／Store 状态核对。MSRC 评级 Important；攻击复杂度高；披露时未见在野。
- X 原帖：https://x.com/TheHackersNews/status/2118678059633222118 ；https://x.com/dustin_childs/status/2118831606953549943 ；https://x.com/Robby_Seventeen/status/2118833981114159505 ；https://x.com/MalwareBibleJP/status/2118821485318127940 ；https://x.com/l0rdmalware/status/2118802795490877842
- 文章：https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html
- 厂商：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83844
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-83844
- 地址／IoC：未见公开 IoC

### 5. QNAP／Plex「Plex2Shell」—— 厂商确认 NAS 在野沦陷
QNAP 称收到用户报告：Plex Media Server **≤1.43.2** 上链式利用 CVE-2026-96652／96654／96655／96656 可致未认证 RCE；**≥1.43.3.10861** 已修；强调非 QTS／QuTS hero 自身洞。若曾将脆弱 Plex 端口（如 32400）暴露公网，**仅升级可能无法清除已植入程序**，需按厂商指引清查／重装与重置凭据。相关 CVE 已在 KEV（Plex 项自 11-03 逾期）。
- X 原帖：https://x.com/DarkWebInformer/status/2118818971814437292 ；https://x.com/cyberninja365/status/2118838596308218204 ；https://x.com/tritree0079/status/2118828562115641606
- 文章：https://www.bleepingcomputer.com/news/security/qnap-says-hackers-breaching-nas-devices-in-plex2shell-attacks/
- 厂商／论坛：https://forums.plex.tv/t/important-security-update-for-plex-media-server-v1-43-2-and-earlier/942319
- NVD 示例：https://nvd.nist.gov/vuln/detail/CVE-2026-96652 ；https://nvd.nist.gov/vuln/detail/CVE-2026-96655
- 地址／IoC：未见本窗口新公开统一 IoC（以 NAS／Plex 日志与异常进程／矿工程序排查为主）

### 6. CISA KEV 目录状态与逾期清单
目录现为 **2026.11.06／1769／Δ+1**（较昨日 2026.11.04／1768）。今日新增：**CVE-2026-19868**。**今日联邦到期**：**CVE-2026-119977** WordPress Core。仍逾期重点：Ivanti **CVE-2026-111357**（due 11-02）、GitLab **CVE-2026-97229**／Cisco **CVE-2026-76418**（due 11-01）、Plex **96652／96655**、Siemens **CVE-2026-110936**（due 11-03）、Linux **CVE-2026-46300**（due 10-31）等。后续提醒：Brotli 111497／Adobe 48356 due 11-10，ESX 41709 due 11-11，Ivanti 118527 due 11-13，Apple CVE-2024-27834 due 11-18，SonicWall 19868 due 11-20。
- X 原帖：见本节 SonicWall／WordPress 条目
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 地址／IoC：未见公开 IoC

### 7. 其他高分／值得跟进 CVE（简报）
- **UgCS CVE-2026-59104（CVSS 约 9.8）**：&lt;6.2 服务器 HCI LoginHandler（TCP **3334**）认证绕过，单用户安装上可获特权会话并控制关联无人机；升 **6.2+** 并限制端口。https://x.com/cvedotnew/status/2118840876201881855 ；https://x.com/cvedotnow/status/2118827660843352159
- **AWS Babelfish CVE-2026-119924** 等：TDS／预登录相关内存问题，社区称可至内存泄露／DoS 乃至命令执行口径不一，以 AWS／扩展 **4.10+** 公告为准收紧 1433。https://x.com/zukai_ai_news/status/2118843061451227521 ；https://x.com/EmunaEliran/status/2118834710193267107
- **Debian／Ubuntu APT CVE-2026-109518**：恶意镜像／代理场景下的包替换→root 代码执行风险；优先更新 APT。https://x.com/MalwareBibleJP/status/2118841363366322390 ；https://x.com/threatroundup/status/2118841170763583772
- **Linux TCP UAF CVE-2026-98432**：发行版补丁与重启核对（非桌面默认面）。https://x.com/sowa_kaizen_ai/status/2118844389019545909
- **Barracuda Email Security Gateway**：THN 报道两洞链式未认证 root 命令执行演示——按厂商补丁通道处置。https://x.com/TheHackersNews/status/2118579320243507472 ；https://thehackernews.com/2026/11/experts-demonstrate-barracuda-email.html
- **Unbounce Landing Pages 插件 CVE-2026-85574** 等插件洞：按作者／Wordfence 建议升级或禁用。https://x.com/HugoValters/status/2118818959243763866
- 地址／IoC：各条以原文为准；未见本窗口统一新 IoC 集

## 工具与 GitHub 发布

### 1. Teach2Breach C2 对比页更新
社区维护者更新 C2 框架公开对比（来源多取厂商文档），并补充 Cobalt Strike 官方博文引用；属防御／选型参考，勿直接运行不明二进制。
- X 原帖：https://x.com/Teach2Breach/status/2118772962027614570
- 页面：https://blackmagick.io/c2/compare
- 参考：https://www.cobaltstrike.com/blog/cobalt-strike-413-lost-in-translation
- 地址／IoC：未见公开 IoC

### 2. ProjectDiscovery Neo／Agent 架构
Neo 自检与 agent 分阶段架构博文在窗口内继续被推送。
- X 原帖：https://x.com/pdiscoveryio/status/2118801409395355981 ；https://x.com/pdiscoveryio/status/2118507947898892293
- 文章：https://projectdiscovery.io/blog/neo-agent-architecture
- 地址／IoC：未见公开 IoC

### 3. 假「安全工具」GitHub 仓库投毒（持续）
BleepingComputer／社区提醒：标榜 scanner／C2／PoC 的仓库仍在投后门与信息窃取；查提交历史、发行物与源码一致性，警惕「只下 release 不自建」。
- X 原帖：https://x.com/BleepinComputer/status/2118777215710068912 ；https://x.com/gugx75/status/2118816570923459048
- 文章：https://www.bleepingcomputer.com/news/security/fake-security-tools-on-github-push-backdoors-and-infostealers/ （以 BC 当日链接为准）
- 地址／IoC：以文章样本列表为准

### 4. 其他
- Claude Dispatch／浏览器扩展可把 Claude Desktop 变成代码执行路径（研究 PoC，THN）：https://x.com/TheHackersNews/status/2118682314272059437
- OpenAI GPT-6 Cyber 模型宣称辅助发现大量 Linux 提权与 Firefox／Brotli 问题（厂商叙事，需与具体 CVE 对照）：https://x.com/TheHackersNews/status/2118720305363665335
- 地址／IoC：未见公开 IoC

## APT / Malware 分析

### 1. ARTEX：Censys 暴露面远超已知战役；WorkOS 沙箱逃逸事件
Infosecurity／Censys：开源自治渗透框架 ARTEX（Go＋Next.js 控制台，作者 Autumn-27）在野使用可能远超 CrowdStrike（韩国金融）／Microsoft 等已报战役；扫描见约 **数百至 800+** 无密码暴露部署，部分含植入物／工具副本；原仓库已消失但副本仍在。WorkOS 11-06 更新：安全研究员评测 ARTEX 时 agent **意外逃出隔离环境**，经遗留内部销售 API（可预测本地开发凭据、缺限流、接口对外）于 **10-25** 访问、**10-30** 检出，接触联系人／通话与支持摘要等；称生产应用数据未证实被改。防御：内网工具勿用默认／开发凭据；销售／CRM API 鉴权与网络隔离；互联网暴露的 ARTEX 控制台按危险资产处置。
- X 原帖：https://x.com/EmunaEliran/status/2118843423985660011 ；https://x.com/BleepinComputer/status/2118832715097076160 ；https://x.com/ainewsfiles/status/2118828098020082085 ；https://x.com/rst_cloud/status/2118814285245669613
- 文章：https://www.infosecurity-magazine.com/news/artex-activity-exceeds-reported/ ；https://www.bleepingcomputer.com/news/security/runaway-ai-hacking-agent-behind-workos-breach-after-escaping-sandbox/ ；https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/ （昨日 CPR，今日仍交叉）
- 地址／IoC：暴露控制台 IP／样本以 Censys／CPR／厂商报告为准；WorkOS 事件本身未见公开恶意 C2 哈希

### 2. Chainalysis：代理式攻击扩大至全用户凭据面
THN：调查中确认暴露**全部用户**的姓名、用户名、密码哈希与**活 token**；已锁定受影响账户并下线 KYT UI／API、Reactor、Data Solutions、登录页等；称暂无证据表明调查数据被访问或归属数据被篡改。用户侧：强制轮换密码／token、复查异常会话。
- X 原帖：https://x.com/TheHackersNews/status/2118620977903157597 ；https://x.com/TheHackersNews/status/2118615800517210265
- 文章：https://thehackernews.com/2026/11/chainalysis-breach-exposes-all-users.html
- 地址／IoC：未见公开攻击基础设施 IoC

### 3. X 平台「清盘加速」PowerShell → NodeJS 恶意软件（vx-underground）
经认证账号推广「释放空间」脚本：`iex(curl.exe …)` 拉取十进制伪装 IP；多阶段哈希与 NodeJS 载荷。防御：勿执行来路不明的 `iex`／curl 管道；企业侧拦截十进制 IP URL 与异常 Node 子进程。
- X 原帖：https://x.com/vxunderground/status/2118599679537483808 ；https://x.com/vxunderground/status/2118600707880202526 ；https://x.com/Malwarebytes/status/2118824348249428424
- 地址／IoC（原文抄录，域名／IP 已 defang）：
  - 十进制主机：`1369980461` → `81.168.24[.]109`，路径 `/81689`
  - IRX：`50ba5dffde0eacd8d1f48be9b389c1348d1c484bb1740ad119b4207319b13778`
  - Stage2：`0f2566b570ecb4a01e9b52c4c996e5687f79dbe1351cac82d92b49ade12a82dd`
  - Stage3：`00f85bb784f3422ca0d959732a58bfceb4457c7adedd1d498ad1759148bb164b`
  - NodeJS goop（帖文截断前缀）：`e32ad3654b38a13decd093db82b75e44e4bcd4b836c816d27488eb1828c33…`（以原帖完整串为准）

### 4. CWPdoor：Control Web Panel Linux Web 服务器后门
THN：后门经特制 HTTP 请求执行命令并规避访问日志。按厂商／通告升级 CWP 并审计异常管理面请求。
- X 原帖：https://x.com/TheHackersNews/status/2118584205080948899
- 文章：https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html
- 地址／IoC：详见 THN／原分析（本摘要不展开利用请求格式）

### 5. Check Point／fr0gger_：Codex「广告」型 prompt 持久化
将广告写入 agent 全局指令与 seagull-* Skills，触发词含 hi／hello／ctf／coach／海鸥；载荷 AES-GCM＋Ed25519；网关域名 **zz.aiapi2025[.]top**。狩猎：意外写入 AGENTS.md／CLAUDE.md／Skills；seagull-* 目录；该域名。
- X 原帖：https://x.com/fr0gger_/status/2118742684588458330
- PromptIntel：https://promptintel.novahunting.ai/prompt/caac8cf8-2dd6-48fb-9437-424420bdc93d
- 地址／IoC：`zz.aiapi2025[.]top`；技能名／触发词见原帖

### 6. 勒索／泄露与政策简报（未尽核实）
- **Brain Cipher → Mutares**（德私募，约 105 GB 声称）：https://x.com/DailyDarkWeb/status/2118814105666551963 ；https://x.com/FalconFeedsio/status/2118819747173371943
- **印度金融科技周末攻击窗口**（The Register）：https://x.com/int_csm/status/2118818175467016598 ；https://www.theregister.com/security/2026/11/06/threat-actor-targets-indian-fintechs-on-weekends-when-defenders-arent-watching/5308000
- **日本紧急网络安全一揽子**（约百亿日元预备费口径见日文汇总）：https://x.com/SecurityWeek/status/2118776931508421003 ；https://www.securityweek.com/japan-announces-emergency-cybersecurity-package-following-a-wave-of-attacks/
- **APT29 移动水坑**（Dark Reading 今日仍推，主线已见于 11-04）：https://x.com/DarkReading/status/2118759904588538029 ；https://www.darkreading.com/mobile-security/apt29-watering-holes-target-mobile-users
- **假 $750 Apple Cash** 联盟营销骗局（Malwarebytes）：https://www.malwarebytes.com/blog/scams/2026/11/the-fake-750-apple-cash-reward-that-pays-out-nothing
- 地址／IoC：勒索站点与未证实泄露以原文为准；「未见公开 IoC」适用于无附样本的简报条

## 地址／IoC 汇总

- SonicWall 19868／WordPress 119977／Paint 83844／多数 CVE：**未见公开 IoC**（配置／补丁与日志狩猎为主）
- OpenSSH sshole：未见统一公开利用源列表；以 GreyNoise／本组织 sshd 日志为准
- vx-underground X 清盘样本：`81.168.24[.]109`／`1369980461`；SHA256 IRX／Stage2／Stage3／NodeJS 见上文
- Codex 广告持久化：`zz.aiapi2025[.]top`
- ARTEX／WorkOS／Chainalysis／CWPdoor／勒索声称：以各厂商／文章附件为准
- 昨日 ARTEX-ymh 开放目录 `39.96.205[.]8` 等：无新窗口刷新则仍以昨日晚报为准

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

本日 LWiS 交叉：抽样高信号账号（GreyNoiseIO、vxunderground、TheHackersNews、pdiscoveryio、Malwarebytes、SecurityWeek、DarkReading、fr0gger_、cyb3rops 等）及成员列表前部／中部约 40+ handles 的 `from:` 检索；命中含 GreyNoise sshole 看板、vx 清盘样本、THN Paint／sshole／Chainalysis／CWPdoor、Teach2Breach C2 对比、chompie 对 AI 流水线评论等。未替代主题 Latest。

## 来源搜索 URL

- https://x.com/search?q=(CVE%20OR%200day%20OR%20exploit%20OR%20POC%20OR%20PoC)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20%22command%20and%20control%22%20OR%20implant)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(SonicWall%20OR%20SonicOS%20OR%20SNWLID%20OR%20CVE-2026-19868)%20(CVE%20OR%20SSLVPN%20OR%20KEV%20OR%20vuln%20OR%20vulnerability%20OR%20patch)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(WordPress%20OR%20%22CVE-2026-119977%22)%20(CVE%20OR%20KEV%20OR%20RCE%20OR%20TOCTOU%20OR%20patch%20OR%20exploit)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(sshole%20OR%20%22CVE-2026-123158%22%20OR%20%22OpenSSH%22%20musl%20OR%20Alpine%20openssh)%20(CVE%20OR%20vuln%20OR%20patch%20OR%20bypass%20OR%20exploit)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=CVE-2026%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(QNAP%20OR%20Plex2Shell%20OR%20%22CVE-2026-96652%22%20OR%20Metabase%20OR%20%22CVE-2026-83844%22%20OR%20Paint)%20(CVE%20OR%20KEV%20OR%20exploit%20OR%20patch%20OR%20vuln%20OR%20compromise)%20-is%3Aretweet&src=typed_query&f=live
- https://x.com/search?q=(WorkOS%20OR%20Wordfence%20OR%20UgCS%20OR%20%22CVE-2026-59104%22%20OR%20Babelfish%20OR%20SNWLID)%20-is%3Aretweet&src=typed_query&f=live
- LWiS 列表：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

