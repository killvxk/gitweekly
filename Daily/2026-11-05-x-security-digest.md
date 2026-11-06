# X 安全情报晚报 · 2026-11-05

覆盖窗口：2026-11-04 20:10 至 2026-11-05 20:18（America/Santiago，UTC-3），约 24 小时。X 只读读取约 35 次（主题检索 + LWiS 前 200 个成员分 5 组 + 引用帖批量查询），0 次 429；纳入本窗口新帖，不与 seen_ids 重复。t.co 已展开为完整 https。公开备援：CISA KEV JSON（**2026.11.04，共 1768 条，Δ+0**）、NVD、Alpine／OpenSSH／厂商与研究机构页面。IoC 一律 defang。本报告为防御向，不转载利用代码、payload 或复现步骤。

## 今日摘要

- **OpenSSH × musl「*sshole」（CVE-2026-123158，CVSS 8.1）**：无 PAM、开启密码认证的 musl 系统（典型为 Alpine `openssh-server`）上，对 shadow 中密码字段为 `*` 的密钥专用账户，提交 257–1024 字节超长密码即可登录。OpenSSH 10.6p2 与 Alpine 各分支补丁包已出；**升级后必须重启 sshd**，临时缓解：`PasswordAuthentication no`。云上 tiny-cloud 的 `alpine` 用户常可 `doas` 提权，优先排查。
- **WordPress Core CVE-2026-119977（KEV）明天 11-06 到期**；Ivanti 111357、GitLab 97229、Cisco 76418、Plex／Siemens 等仍逾期。KEV 目录今日无新增。
- **Microsoft Paint CVE-2026-83844（CVSS 8.1）**：越界读可致网络侧代码执行；按微软／Windows 更新通道打补丁。
- **mSecure／mSeven**：加密云库据称被窃，现／前用户被要求改密、重置 2FA、删除 passkey；未见解密证据，但离线撞主密码风险存在。
- **Check Point Research：ARTEX 在野自治渗透**——追踪 2000+ 控制台并拿到对话库；huntback 另披露带蜜罐检测模块的 ARTEX-ymh 分叉（含暴露 IP）。
- **工具**：Exegol Studio（IHE）发布；xcpe-guard（Android TV 关停 XCPE 后门）；yogsec Red-Team-Tools 清单；Microsoft PyRIT。

## CVE / POC / 漏洞

### 1. OpenSSH／Alpine *sshole（CVE-2026-123158）——今日主线
条件叠加：musl + 无 PAM（或 `UsePAM no`）+ `PasswordAuthentication yes` + 至少一账户 shadow 为 `*` + 另有 `$5$`／`$6$` 哈希。musl `crypt()` 对超长口令返回 `*`，与无密码账户字段一致即判成功。glibc／启用 PAM 一般不受影响。修复：OpenSSH **10.6p2**；Alpine 各分支固定 openssh 包见公告；**`apk upgrade` 后务必 `rc-service sshd restart`**。狩猎：日志中对本应无密码账户出现 `Accepted password for`。
- X 原帖：https://x.com/kultekin/status/2118306312736116835 ；https://x.com/IntCyberDigest/status/2118343325770006690 ；https://x.com/DarkWebInformer/status/2118412864767557672 ；https://x.com/DazedProgrammer/status/2118472689308299770 ；https://x.com/vxunderground/status/2118432930145952173 ；https://x.com/arstechnica/status/2118481997236736159
- 研究者站点：https://sshhole.com/
- 厂商公告：https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/ ；https://www.openssh.org/txt/release-10.6p2 ；https://www.openssh.org/releasenotes.html
- 文章：https://arstechnica.com/security/2026/11/vulnerability-allows-attackers-to-log-into-some-linux-devices-sans-password/ ；https://www.bleepingcomputer.com/news/security/openssh-flaw-lets-attackers-log-into-password-disabled-linux-accounts/ ；https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html ；https://www.openwall.com/lists/oss-security/2026/11/05/3 ；https://www.theregister.com/security/2026/11/05/get-root-on-a-musl-linux-system-by-slamming-it-with-an-overly-long-password/5307910
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-123158
- GitHub 修复提交：https://github.com/openssh/openssh-portable/commit/4353fdc43ef646c43a8dda7025cc1a898caf1482
- 地址／IoC：未见公开 IoC（属配置类认证绕过）

### 2. CISA KEV：本日无新增；WordPress 119977 明天到期
目录仍为 **2026.11.04／1768／Δ0**。明日（11-06）联邦期限：**CVE-2026-119977** WordPress Core（升级窗口 TOCTOU→未认证 RCE，修于 7.1.4）。已逾期重点：Ivanti CVE-2026-111357（due 11-02）、GitLab CVE-2026-97229／Cisco CVE-2026-76418（due 11-01）、Plex CVE-2026-96652／96655、Siemens CVE-2026-110936（due 11-03）。后续：Brotli 111497／Adobe 48356 due 11-10，ESX 41709 due 11-11，Ivanti 118527 due 11-13，Apple CVE-2024-27834 due 11-18。
- X 原帖：https://x.com/rMATLAB_x/status/2118476893460775014 ；https://x.com/neo_logos_/status/2118471092964913487 ；https://x.com/toushikaka/status/2118469037952786727 ；https://x.com/cyberninja365/status/2118467394704150826
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-119977
- 地址／IoC：未见公开 IoC

### 3. Microsoft Paint CVE-2026-83844（CVSS 8.1）：网络可达代码执行
NVD：Windows Paint 越界读，未授权攻击者可经网络执行代码。X 上大量讨论；按微软安全更新指南／Windows Update 打补丁。未见公开在野利用细节。
- X 原帖：https://x.com/Dieter_be/status/2118394588394397708 ；https://x.com/jedisct1/status/2118426473576972603 ；https://x.com/Pirat_Nation/status/2118446148713361874 ；https://x.com/vxunderground/status/2118453965201514752 ；https://x.com/dedene/status/2118459278126366855
- CVE 记录：https://www.cve.org/CVERecord?id=CVE-2026-83844
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-83844
- 厂商：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83844
- 地址／IoC：未见公开 IoC

### 4. Kubeflow Pipelines CVE-2026-77596（CVSS 约 9.6）：共享流水线上传鉴权绕过
多用户模式下上传共享流水线接口缺授权检查，低权限网络用户可创建／注入恶意版本。补丁 **2.18.0**。
- X 原帖：https://x.com/cvedotnow/status/2118474101517914236 ；https://x.com/EmunaEliran/status/2118480609404223962
- 其他：https://cve.now/CVE-2026-77596
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-77596
- 地址／IoC：未见公开 IoC

### 5. Kyverno CVE-2026-122302：命名空间管理员权限提升（&lt;1.19.2）
generate 规则接纳时校验的是 background controller 权限而非策略作者。升级至 1.19.2+。
- X 原帖：https://x.com/EnclaveRadar/status/2118482432294789329
- 其他：https://app.enclave.ai/threat-feed/CVE-2026-122302
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-122302
- 地址／IoC：未见公开 IoC

### 6. Zyxel GS1900 CVE-2026-107441：六月补丁不够，约 996 台仍沦陷
Binarly／GreyNoise 称在野利用绕过 6 月 Patch 2；需装 **2.90(…).3**（10-22 真修复），UI 下公网、改默认口令。
- X 原帖：https://x.com/threatroundup/status/2118478616220574105 ；https://x.com/neocloudsol/status/2118471696688759281
- 厂商／NVD：查阅 Zyxel 安全公告；https://nvd.nist.gov/vuln/detail/CVE-2026-107441
- 地址／IoC：未见本窗口新公开 IoC

### 7. 其他高分 CVE（简报）
- **Rails Active Storage CVE-2026-122006**：与昨日 Rails 8.0.5.2／8.1.4.1 公告同源，继续督促升级。https://x.com/EnclaveRadar/status/2118482430382235724
- **FreeSWITCH** 116779／116785／116790 等顾问在 X 反复刷屏（昨日已覆盖，今日仍有提交链接）。示例：https://x.com/EmunaEliran/status/2118482571269218681
- **SuiteCRM** CVE-2026-71550（工作流文件包含→代码执行，修 7.15.2／8.10.2）；**OpenEMR** CVE-2026-102940（文档写操作缺权）。https://x.com/busenur038/status/2118480690203230317
- **MatchPoint** Android TLS 信任任意证书 CVE-2026-111494；API IDOR CVE-2026-111490。
- **Brotli Node2Shell CVE-2026-111497（KEV）**：提醒扫描镜像中 libbrotli 1.0.3–1.2.0。https://x.com/White_Hunters/status/2118480913721880679
- 地址／IoC：未见公开 IoC

## 工具与 GitHub 发布

### 1. Exegol Studio：面向黑客的集成环境（IHE）
Exegol 发布 Studio，定位「开发者有 IDE，黑客应有 IHE」，宣称 AI 就绪，可免费起步。
- X 原帖：https://x.com/exegolHQ/status/2118429414799077802 ；https://x.com/_nwodtuhs/status/2118433410892919224
- 产品：https://exegol.com/studio
- 地址／IoC：未见公开 IoC

### 2. xcpe-guard：在 Android TV 本机发现并关闭 XCPE 后门
基于 Google XCPE 报告中的应用与 C2，开源 APK／源码，无需 root／电脑。
- X 原帖：https://x.com/nerdingen/status/2118237491589177564
- GitHub：https://github.com/burakztrk/xcpe-guard
- 背景（Google）：https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet
- 地址／IoC：C2／应用列表以 Google 报告为准，此处不复述利用步骤

### 3. 其他清单／框架
- yogsec Red-Team-Tools（C2／对抗仿真策展）：https://github.com/yogsec/Red-Team-Tools ；https://x.com/yogsec/status/2118299372530356674
- Microsoft PyRIT（生成式 AI 红队）：https://github.com/microsoft/PyRIT ；https://x.com/SagarXploit/status/2118185438699770167
- ProjectDiscovery Neo Goal 模式更新：https://x.com/pdiscoveryio/status/2118394484883120490 ；https://neo.projectdiscovery.io/
- Harness 工程入门（漏洞研究）：https://grahamhelton.github.io/harness-engineering-workshop-book/introduction.html
- 地址／IoC：未见公开 IoC

## APT / Malware 分析

### 1. Check Point Research：ARTEX 自治网络犯罪战役
CPR 追踪 2000+ ARTEX 服务器，拿到含完整 agent 对话的数据库，论证「全自动网络犯罪已出现」。eversinc33／Tera0017 同步强调可见 agent 对话与所用模型。Censys 侧有人报约 1465 暴露控制台。
- X 原帖：https://x.com/_CPResearch_/status/2118395415364079679 ；https://x.com/eversinc33/status/2118395540933124196 ；https://x.com/DFIR_Radar/status/2118478986317902089
- 文章：https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/
- 地址／IoC：详见 CPR 原文（样本／基础设施以厂商报告为准）

### 2. huntback：ARTEX-ymh 分叉学会识别蜜罐
阿里云杭州开放目录暴露 ARTEX-ymh 工作区（含蜜罐检测设计文档与签名引擎）。单信号→只读降级；双信号→放弃目标；另有防 attestation／prompt 注入与 egress 哈希过滤。防御侧可猎：固定过期 Chrome UA + 非浏览器 TLS、约 40 次同主机抓取后安静、登录后对 `/proc/meminfo` 双读等（见原文）。
- 文章：https://huntback.io/blog/artex-fork-learns-to-spot-honeypots
- X 转述：https://x.com/rst_cloud/status/2118476686089969901
- 地址／IoC：`39.96.205[.]8`（AS37963，Alibaba Cloud Hangzhou）；开放目录 `http://39.96.205[.]8:9001/` 、`http://39.96.205[.]8:8081/`；目录名 `artex-ymh-probe/`（含 `HONEYPOT-DETECTION-DESIGN.md` 等）

### 3. mSecure／mSeven：加密密码库据称失窃
11-03 起通知现／前用户改密、重置 2FA、删除 passkey；支持回复称 mSecure Cloud 加密库被盗、未见解密证据。仅同步云用户受影响；弱主密码有离线破解风险（类比 LastPass）。警惕仿冒「mSecure 重置」钓鱼。
- X 原帖：https://x.com/Malwarebytes/status/2118445003248714178 ；https://x.com/ndgmlondon/status/2118437769886277687
- 文章：https://www.bleepingcomputer.com/news/security/msecure-password-manager-hack-prompts-password-reset-warnings/ ；https://www.malwarebytes.com/blog/data-breaches/2026/11/msecure-tells-users-to-change-passwords-but-wont-say-why
- 地址／IoC：未见公开样本哈希／C2

### 4. 其他事件简报
- **Queens Public Library** 勒索软件致 66 分馆 Web／App／Wi-Fi／借还中断：https://ny1.com/nyc/all-boroughs/news/2026/11/05/ransomware-attack-disrupts-queens-public-library-services ；https://x.com/White_Hunters/status/2118480790635888822
- **MonsterCloud** 老板被控向勒索受害者收费却暗中代付赎金：https://www.justice.gov/usao-edny/pr/owner-florida-ransomware-remediation-company-charged-defrauding-clients ；https://x.com/White_Hunters/status/2118480701834105168
- **Coinbase Prime** 机构投资者库叫卖（地下论坛，未证实）：https://x.com/DailyDarkWeb/status/2118481571216781534
- **Bitdefender 3AM** 欧校勒索（人机混合／疑似 agentic 循环，11-03 文今日仍被引用）：https://businessinsights.bitdefender.com/3am-ransomware-hybrid-ai-attack
- **DigiCert** Mozilla Bugzilla「Unauthorized access to business system」：https://bugzilla.mozilla.org/show_bug.cgi?id=2084460 ；https://x.com/pfiatde/status/2118247104355381661
- **SmartLoader／StealC** 假 AI 工具仓库投毒（昨日主线，vx-underground 今日仍跟进）：https://x.com/vxunderground/status/2118127715572425131
- 地址／IoC：各条以原文为准；Coinbase／部分勒索声明未核实

## 地址／IoC 汇总

- ARTEX-ymh 暴露主机：`39.96.205[.]8`；目录 `http://39.96.205[.]8:9001/` 、`http://39.96.205[.]8:8081/`（huntback，防御狩猎用）
- *sshole／Paint／WordPress／Kubeflow／Kyverno／mSecure：未见本报告需单列的新公开哈希／钱包；配置与补丁优先
- 其余条目：未见公开 IoC 或沿用厂商报告（不在此复述利用细节）

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

- X Latest CVE／POC：https://x.com/search?q=(CVE%20OR%200day%20OR%20POC%20OR%20exploit)%20-is%3Aretweet&src=typed_query&f=live
- X *sshole／Alpine：https://x.com/search?q=(sshole%20OR%20Alpine)%20(OpenSSH%20OR%20musl)%20-is%3Aretweet&src=typed_query&f=live
- X malware／threat：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20-is%3Aretweet&src=typed_query&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- Alpine 公告：https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/
- OpenSSH 10.6p2：https://www.openssh.org/txt/release-10.6p2
