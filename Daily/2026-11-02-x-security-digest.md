# X 安全情报晚报 · 2026-11-02（America/Santiago）

> 生成时间：2026-11-02 20:10（America/Santiago）＝ 2026-11-03 07:10（香港时间）
> X 覆盖：LWiS List 时间线两页约 191 帖，覆盖 2026-11-02 02:58–22:56 UTC（约 20 小时）；Latest 搜索三组 + 高互动 CVE 补搜一组。Latest「CVE/PoC/exploit/0day」按时间排序仅覆盖约 45 分钟（22:24–23:10 UTC，被自动 CVE 机器人刷屏），所以加了一组 min_likes:20 的相关度补搜，覆盖完整 24 小时；GitHub 组覆盖 01:08–22:47 UTC；malware/threat 组覆盖 13:35–23:01 UTC（约 9.5 小时）。
> 公开备援：CISA KEV（目录 2026-10-30 发布，本窗口无新增；最近新增是 10-30 的两条 Ivanti）、厂商公告、ZDI。
> 验收：采集、链接核验、成稿均通过；本机副本见文末交付说明。

## 今日摘要

- **Ivanti Connect Secure 又有两枚 0day 在野利用**（CVE-2026-111357、CVE-2026-118527），已进 KEV，其中 111357 的 KEV 截止日就是今天 11-02。Rapid7 给出了 UTA0576 的利用 IP。
- **Palo Alto PAN-OS CVE-2026-0322 在野利用**：能访问管理接口的攻击者可以 root 执行命令，先把管理面收窄到可信 IP。
- **Google GTIG 发布 LLMJacking 报告**：攻击者用 max_tokens=1 的请求验证偷来的 LLM key，再通过「LLM mixer」转卖额度；GTIG 同时公布了对 XCPE 百万级 Android 电视盒僵尸网络的处置。
- **伊朗系 DarkBlinders** 攻击以色列与伊拉克库尔德地区政府云；**Unit 42 CL-UNK-1211** 用 SysGoRAT 打政府 Linux 服务器。
- Linux 内核方向：a13xp0p0v 发了 CVE-2026-31695 的深度分析；CVE-2026-98432（MPTCP/TCP UAF）讨论持续，Ubuntu 补丁仍滞后。
- SecureFlow：ZDI 新公开 3 个 Microsoft Qlib 反序列化 RCE（ZDI-26-848/849/850）；近 7 天还有 MLflow、Ultralytics、Alpine 车机（Pwn2Own）、Safari、Valkey 等一批 ZDI 公告。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

### 1. Ivanti Connect Secure 新增两枚在野 0day（CVE-2026-111357 / CVE-2026-118527）
Ivanti 10-29 更新 ICS 公告，新增两个已在野利用的漏洞（认证缺失、可预测标识符），常与此前的漏洞串联使用。KEV 10-30 已收录，CVE-2026-111357 联邦截止日 11-02，CVE-2026-118527 截止 11-13。建议立即升级，并按 Rapid7 给的日志路径（debuglog、audit.log）排查有选择性删日志的痕迹。（昨天晚报已提过一轮，今天是 Rapid7 的详细跟进。）
- X 原帖：https://x.com/rapid7/status/2117255308288680209 、https://x.com/Dinosn/status/2117240316545650928 、https://x.com/Dinosn/status/2117189203511627917
- 厂商／KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 文章：https://www.rapid7.com/blog/post/etr-additional-ivanti-connect-secure-zero-days-exploited-in-the-wild-cve-2026-111357-cve-2026-118527 、https://www.bleepingcomputer.com/news/security/ivanti-patches-two-more-connect-secure-zero-days-chained-in-attacks/

### 2. Palo Alto PAN-OS CVE-2026-0322（CVSS 8.6，在野利用）
能访问管理接口的攻击者可以 root 身份执行命令。处置：管理接口只放可信 IP，按公告升级。
- X 原帖：https://x.com/emits_ca/status/2117330428797559011
- 厂商公告：https://security.paloaltonetworks.com/CVE-2026-0322

### 3. Linux 内核 CVE-2026-31695（struct device 相关竞争条件）深度分析
Alexander Popov 发布长文，介绍如何把一个难以稳定触发的竞争条件做成稳定利用，附内核加固讨论。防御向：关注发行版内核更新。
- X 原帖：https://x.com/a13xp0p0v/status/2117227603161735232
- 文章：https://a13xp0p0v.tech/2026/11/02/CVE-2026-31695.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-31695

### 4. Linux 内核 CVE-2026-98432（IPv4 TCP UAF，MPTCP 条件下可远程提权）后续
Red Hat 11-01 已推 RHEL 8/9/10 内核修复；有帖子指出 Ubuntu 仍无修复内核，Go 1.24+ 服务默认监听 Multipath TCP；还有人发现宿主机加固后容器命名空间里 MPTCP 仍开着。AWS 称未见在野利用。
- X 原帖：https://x.com/CobaltHere/status/2117285606086562247 、https://x.com/DailyCyberNews_/status/2117217164050530679 、https://x.com/Ghourchiani/status/2117390016938680763
- 文章：https://ghourchiani.ir/blog/cve-2026-98432-docker-container-namespaces

### 5. PHP2Shell（CVE-2026-109618 / CVE-2026-109619）披露风波与在野利用
ReversingLabs 称 AI 辅助研究把两个沉睡的 PHP 漏洞串成 PHP2Shell，披露前泄露导致补丁前就有利用尝试；HN 讨论引述一个 AI 辅助攻击活动在 10-25 拿下 25 台服务器，其中包括美国政府关联环境。
- X 原帖：https://x.com/LiveOverflow/status/2117281363200201033 、https://x.com/TweetThreatNews/status/2117382289730490581 、https://x.com/LiveOverflow/status/2117110101160993264
- 文章：https://cyber.hendryadrian.com/article/14168/php2shell-disclosure-turmoil-follows-ai-assisted-exploit-discovery 、https://news.ycombinator.com/item?id=50286987 、https://pavursec.com/blog/stealmybitcoin/

### 6. WordPress pingback + Brotli RCE（CVE-2026-111497）复现分析，及 Project Zero 的 Brotli 解码器越界读写
Fortbridge 发布 CVE-2026-111497 复现分析；Project Zero 同日公开 Brotli 解码器内部输入缓冲区的堆越界读写（DecodeBlockTypeAndLength）。WordPress 站点升级到最新版本，并关注依赖 Brotli 的组件。
- X 原帖：https://x.com/Dinosn/status/2117186693677875492 、https://x.com/ProjectZeroBugs/status/2117225924492181996
- 文章：https://fortbridge.co.uk/research/cve-2026-111497-wordpress-pingback-rce-reproduction/
- 厂商／跟踪单：https://project-zero.issues.chromium.org/issues/565308158 、https://nvd.nist.gov/vuln/detail/CVE-2026-111497

### 7. Project Zero：Apple RawCamera 两个堆溢出（Phase One、Canon sRAW 解码器）
- X 原帖：https://x.com/ProjectZeroBugs/status/2117210525344124989 、https://x.com/ProjectZeroBugs/status/2117209976259375527
- 跟踪单：https://project-zero.issues.chromium.org/issues/552305156 、https://project-zero.issues.chromium.org/issues/552300026

### 8. Langflow 1.0.0–1.12.8 多个严重漏洞（无需账号即可绕过认证或执行代码）
IBM 10-28 发布公告（列出 CVE-2026-93680 等多个 CVE），唯一修复版本是 1.13.0，目前不在 KEV 里。
- X 原帖：https://x.com/Dinosn/status/2117250287274717216
- 文章：https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html

### 9. GitLab 在野 RCE：超过 1,000 台服务器仍暴露；补丁在 Ruby 层
有受害方指出 10-22 升级到 GitLab 19.3.6 并没有修掉漏洞，因为修复在 GitLab 附带的 Ruby 补丁里。请核对实际的 Ruby 补丁是否生效。（昨天晚报已提过 GitLab 在野利用。）
- X 原帖：https://x.com/N3mes1s/status/2117260494230729098 、https://x.com/Dinosn/status/2117239903717314797 、https://x.com/CIDC_Ops/status/2117089667300687877
- 文章：https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/

### 10. VMware ESXi CVE-2026-41709（CVSS 2.7，已进 KEV）被 Warp Panda 利用
这是一个日志记录不足的漏洞：拥有管理员权限的攻击者可以做某些操作而不留日志。CrowdStrike 称 Warp Panda 用它攻击美国机构，包括律所。处置：升级，并把日志外送。
- X 原帖：https://x.com/EvergreenCS117/status/2117390388415824235
- 文章：https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html

### 11. OpenAirInterface CN5G AMF/UDM 多个漏洞（标注有在野利用）
包括 CVE-2026-117067、117068、117069 和 106808，影响 OAI CN5G v2.2.1；来源是自动化 CVE 帖，可信度一般，自建 5G 核心网的话应关注。
- X 原帖：https://x.com/KaitanSecurity/status/2117368663028154878 、https://x.com/KaitanSecurity/status/2117338461929631952

### 12. Microsoft Qlib 三个反序列化 RCE（ZDI-26-848/849/850，SecureFlow 与 ZDI）
StaticDataLoader、RestrictedUnpickler、MLflowRecorder 处理 pickle 数据时可被利用（需要用户打开恶意文件，CVSS 7.8）。X 上暂未见讨论。
- 厂商／ZDI：https://www.zerodayinitiative.com/advisories/ZDI-26-848/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-849/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-850/

## 工具与 GitHub 发布（每条：说明 + 地址列表）

### 1. CredGuardRuntimeShutdown（Win11 24H2 上运行时关闭 Credential Guard）
防御向：关注 LSA_ISO 相关的注册表和服务变更，以及 LSASS 访问。
- X 原帖：https://x.com/ipurple/status/2117372679015514187
- GitHub：https://github.com/S12cybersecurity/CredGuardRuntimeShutdown

### 2. tprtdll-Injection（用 tprtdll.dll 替代 ntdll 的导出来规避 EDR hook）
- X 原帖：https://x.com/ipurple/status/2117250385509241153
- GitHub：https://github.com/ivancabrera02/tprtdll-Injection

### 3. HorusEye（AD 攻击路径映射 + 修复方案对比，红蓝通用）
- X 原帖：https://x.com/ipurple/status/2117356667788578908
- GitHub：https://github.com/Omar-tamerr/HorusEye/

### 4. blackmagick C2 发布与更新（Teach2Breach），附 stargate、moonwalk
平台新增 Horus loader、RRCfg 恶意软件分析文章和 C2 发布视频；作者同时提到 API 解析不走 PEB walk、改用内存扫描的思路。
- X 原帖：https://x.com/Teach2Breach/status/2117367115590115728 、https://x.com/Teach2Breach/status/2117376744357351580
- GitHub：https://github.com/Teach2Breach/stargate 、https://github.com/Teach2Breach/moonwalk
- 站点：https://blackmagick.io

### 5. Impacket-IoCs（重写 impacket 时整理出的特征，适合写检测）
- X 原帖：https://x.com/CyberWarship/status/2117265506851791245
- GitHub：https://github.com/ThatTotallyRealMyth/Impacket-IoCs

### 6. SmartScreen 自定义扩展名绕过（ipurple 文章）
- X 原帖：https://x.com/ipurple/status/2117381386239701411
- 文章：https://ipurple.team/2026/10/22/custom-extensions/

### 7. Trail of Bits：用 Codex 大规模回移安全补丁
- X 原帖：https://x.com/Dinosn/status/2117240570456518671
- 文章：https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/

### 8. Mac Monitor v3.0 发布（macOS 动态分析，新增 CLI）
- X 原帖：https://x.com/L0Psec/status/2117298773713977466 、https://x.com/_D00mfist/status/2117324448055566789

## APT / Malware 分析（每条：说明 + 地址列表）

### 1. Google GTIG：LLMJacking，盗用云上大模型额度变现
初始访问主要靠窃取 IAM 凭据、服务账号密钥、GitHub PAT；用 max_tokens=1 或 temperature=0 的小请求验证 key，避开用量告警；通过「LLM mixer」转卖，jet-night 月费约 60 美元，有一个用户 8 小时内调用 50 万次以上，造成近 100 万美元的 token 费用；还有人用基于 Manus 的容器化 agent 做后门。狩猎：查 LLM 网关日志里的 max_tokens=1 探测、异常 Bedrock 和 Vertex 调用、伪装成计费优化的服务账号。
- X 原帖：https://x.com/fr0gger_/status/2117335710781079893 、https://x.com/fr0gger_/status/2117335719878561837 、https://x.com/fr0gger_/status/2117335717756178700
- 文章：https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models 、https://www.theregister.com/security/2026/11/02/token-thieves-costing-companies-100k-per-day-in-illicit-llm-charges/5306967

### 2. Google 处置 XCPE 百万级 Android 电视盒僵尸网络
- X 原帖：https://x.com/Dinosn/status/2117249213541060730 、https://x.com/Dinosn/status/2117332181823484303
- 文章：https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet/ 、https://www.bleepingcomputer.com/news/security/google-disrupts-million-device-xcpe-android-malware-botnet-bans-tv-box-maker/

### 3. DarkBlinders（伊朗国家背景）攻击以色列与伊拉克库尔德地区政府云
据 Dream Research Labs 报告，活动时间是 2026 年 8 月至 10 月，已攻陷以色列一位高知名度人士和库尔德地区的政府云环境。同文提到另一个伊朗组织在美国境内运营 Tornado（Tonnerre 变种）的二级 C2。
- X 原帖：https://x.com/Dinosn/status/2117281385459380522
- 文章：https://thehackernews.com/2026/11/darkblinders-compromises-israeli-target.html

### 4. Unit 42 CL-UNK-1211：SysGoRAT 攻击政府 Linux 服务器（疑似用了 AI 生成的脚本）
活动时间是 2025 年 10 月至 2026 年 4 月；SysGoRAT 通过 WebSocket 连硬编码 C2，支持命令执行、交互 shell、截屏和外传。
- X 原帖：https://x.com/Dinosn/status/2117240192629412232
- 文章：https://thehackernews.com/2026/11/government-linux-servers-targeted-with.html

### 5. VOLTA（VOLTA-AUTODOXER）信息窃取器：用 Claude、Gemini、Kimi 按财务价值给受害者排序
Talos 发现它最多串三个模型应对拒答，并通过 Telegram 外传数据。
- X 原帖：https://x.com/Dinosn/status/2117160879208964344
- 文章：https://thehackernews.com/2026/11/new-volta-infostealer-uses-claude.html

### 6. 冒充 IT 支持走 Microsoft Teams 社工 + 滥用 AD CS（ESC1/ESC8）窃取数据
- X 原帖：https://x.com/Dinosn/status/2117240332308062294
- 文章：https://thehackernews.com/2026/11/attackers-pose-as-it-support-on.html

### 7. NWH Stealer 静态分析（Bun 运行时无文件执行、剪贴板图片窃取、借 AWS 和 Cloudflare R2 做 C2）
- X 原帖：https://x.com/ipurple/status/2117388030063612318
- GitHub：https://github.com/kaandemir993/NWH-Stealer-Analysis-Fileless-Bun-Runtime-Execution-Clipboard-Image-Theft-Cloud-C2-AWS-R2-

### 8. Synology 警告 C3RB3R 勒索攻击 NAS
- X 原帖：https://x.com/Dinosn/status/2117239965264556267
- 文章：https://www.bleepingcomputer.com/news/security/synology-warns-customers-of-ongoing-c3rb3r-ransomware-attacks/

### 9. 欧洲超市冷柜遭远程「解冻」攻击第二波（比利时、卢森堡、瑞典、爱沙尼亚）
暴露在公网上的冷柜控制面板被用于远程操作。vx-underground 指出几个月前就有人讨论过这类暴露面。
- X 原帖：https://x.com/Dinosn/status/2117243716138381448 、https://x.com/Dinosn/status/2117250162443567394 、https://x.com/vxunderground/status/2117335140313780446
- 文章：https://securityaffairs.com/202260/security/another-fridge-cyberattack-hits-european-supermarkets-this-time-in-belgium-luxembourg-sweden-and-estonia.html 、https://www.theregister.com/cyber-crime/2026/11/02/frozen-part-ii-hackers-remotely-defrost-produce-in-euro-supermarkets-again/5306924

### 10. Binance 大额被盗：FBI 公布 600 多个与朝鲜相关的地址；BTCPay 旧版热钱包被盗
- X 原帖：https://x.com/Dinosn/status/2117186779732418654 、https://x.com/Dinosn/status/2117278211243683981 、https://x.com/vxunderground/status/2117379973904310654
- 文章：https://www.securityweek.com/fbi-flags-over-600-addresses-tied-to-north-koreas-binance-heist/、https://www.bleepingcomputer.com/news/security/btcpay-server-warns-of-hot-wallet-thefts-targeting-outdated-instances/

### 11. 其他
Trigger.dev 云端 AI 工作流工具的环境变量被窃，所有密钥都要轮换；Check Point 11-02 威胁情报周报；Phantom Stealer 配置失误的样本（ANY.RUN）；勒索帖：Qilin 声称攻击智利 Isapre Consalud，Akira 声称攻击多家美国公司（均为未核实的声称）。
- X 原帖：https://x.com/Dinosn/status/2117311920755912983 、https://x.com/Dinosn/status/2117306974509424911 、https://x.com/James_inthe_box/status/2117326298058277027 、https://x.com/FalconFeedsio/status/2117364792784794002
- 文章：https://www.theregister.com/security/2026/11/02/cloud-hosted-ai-workflow-tool-has-environment-variables-snatched-in-security-incident/5306998 、https://research.checkpoint.com/2026/2nd-november-threat-intelligence-report/ 、https://app.any.run/tasks/52088266-db7d-4e22-9edb-d5d6215c355c

## SecureFlow 信息流精选（X 上未出现的高信号条目）

### community
- 奇安信攻防社区：「Java 反序列化从 Redis 开始 RCE」，一篇反序列化利用链的分析文章。链接：https://forum.butian.net/share/5255 （box 网络无法连接该站，浏览器可开）
- （已过滤：先知社区「双倍积分和稿费的活动通知」，非技术帖）

### blog（ZDI，近 7 天首次出现、昨天晚报未列的）
- ZDI Blog：「CVE-2026-35273: SSRF to RCE in Oracle PeopleSoft」 https://www.thezdi.com/blog/2026/10/20/cve-2026-35273-ssrf-to-rce-in-oracle-peoplesoft
- MLflow 一组（SSRF、越权、反序列化）：https://www.zerodayinitiative.com/advisories/ZDI-26-840/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-841/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-842/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-843/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-844/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-846/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-847/
- Ultralytics（0Day，未修补）：https://www.zerodayinitiative.com/advisories/ZDI-26-812/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-814/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-815/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-816/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-817/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-818/
- Alpine iLX-F511 车机（Pwn2Own 0Day）：https://www.zerodayinitiative.com/advisories/ZDI-26-819/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-820/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-822/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-823/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-824/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-825/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-826/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-827/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-829/
- Apple Safari jsToWasm 类型混淆 RCE：https://www.zerodayinitiative.com/advisories/ZDI-26-830/ ；macOS CoreText 越界读：https://www.zerodayinitiative.com/advisories/ZDI-26-831/
- AVG Internet Security 本地提权：https://www.zerodayinitiative.com/advisories/ZDI-26-832/
- MailEnable XXE 与明文存储：https://www.zerodayinitiative.com/advisories/ZDI-26-810/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-811/

### BugBounty
- HackerOne：monero-wallet-rpc 的 rescan_spent 接受不可信 daemon 提供的花费状态，可用于环交集去匿名。链接：https://hackerone.com/reports/3719670

## 地址／IoC 汇总

以下原样抄录自公开报告，已去武装化（defanged），仅供检测与封堵：

- **Ivanti ICS（UTA0576 利用 IP，来源 Rapid7 引 Volexity）**：108.165.147[.]64
- **SysGoRAT C2（Unit 42 / THN）**：104.194.158[.]65:443（WebSocket）
- **DarkBlinders 相关基础设施（THN 引 Dream Research Labs）**：gcc-sg[.]cloud、mfakuwait[.]online、moelcloud[.]online、stark-meet[.]com、stark-meet[.]online、stark-meet[.]website；伊朗系 Tornado 二级 C2：68.65.122[.]203
- **XCPE 僵尸网络（GTIG）**：运营服务器 38.145.197[.]135、23.94.49[.]57；broker 节点 219.134.163[.]210、219.134.163[.]211（设备走 3885–3887 端口；管理面走 8082/8083 端口）。部分样本 SHA256：
  - 0135b69bab304564628488829b825050d1dd6dab98e86ec6776839dac9365af9
  - 01b8c78f5509119b3e27ea4d628048985b94b5e00db0431d843519cf1d3e2cde
  - 02490fa9f472ec872723d64d03402967e77932d2df72c588b0d7a7df9e17ae62
  - （完整列表见 GTIG 原文）
- **LLMJacking 转卖平台（GTIG / @fr0gger_）**：newapi[.]pro、jet-night[.]com
- **Teams 冒充 IT 支持 + AD CS 活动样本 SHA256（THN）**：
  - 06c5c14f043aee3bcc5843b5f50909623d5c9a6239a7c1fba9cddad4111469e7
  - 85b6c424117494d3056e88689dbc94c75e9afdb187a339714043aec0da109f17
  - f326201269f1ee2f803ae435317507263bb6e0dbfdeb70bd1bb5446e2e46f001
- **Binance 被盗相关钱包**：FBI 公布了 600 多个地址，见 SecurityWeek 原文，本报告不逐一抄录。
- 其余条目未见公开 IoC。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）：https://x.com/i/lists/1239330068461244424 （本次读取约 191 帖，覆盖约 20 小时）
- 博客清单：https://blog.badsectorlabs.com/files/blogs.txt （本地：lwis-sources/blogs.txt）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- SecureFlow 安全信息流：https://secureflow.scope-sentry.top/all （只读接口：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200）
- SecureFlow 社区：https://secureflow.scope-sentry.top/community （源列表：https://secureflow.scope-sentry.top/api/rss/category?category=community）
- SecureFlow 博客：https://secureflow.scope-sentry.top/blog （源列表：https://secureflow.scope-sentry.top/api/rss/category?category=blog）

## 来源搜索 URL（含 SecureFlow 三个接口、各分类条数与覆盖区间）

- X Latest：
  - https://x.com/search?q=CVE%20OR%20PoC%20OR%20exploit%20OR%200day&f=live
  - https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20BOF)&f=live
  - https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
  - 补搜：https://x.com/search?q=(CVE%20OR%20exploit%20OR%200day%20OR%20%22in%20the%20wild%22)%20min_faves%3A20
- X List：https://x.com/i/lists/1239330068461244424
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200
  - 返回 200 条，最早一条是 2026-10-19；近 48 小时（2026-11-01 07:10 至 11-03 07:10，北京时间）新条目 6 条。其中 BugBounty 1 条、ZDI 3 条、community 2 条，过滤了 1 条活动通知。
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community
  - 7 个源，跳过长期不更新的吾爱破解，其余 6 个逐源拉取 /api/rss/articles/<id>。
  - 近 48 小时内、all 接口之外的新条目 0 条。
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog
  - 12 个源，跳过长期不更新的「微信公众号」源，其余逐源拉取。
  - 近 7 天（2026-10-27 至 11-03，北京时间）不在 seen_ids 里的条目 39 条，全部来自 ZDI。
  - 去掉昨天晚报已列的 11 条后，本报告列出 28 条，其余源本周无新文。
- 各接口均请求成功，无失败。
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （共 1766 条，2026-10-30 发布；本窗口无新增）

---
本机保存路径：~/Desktop/X安全情报晚报/2026-11-02-x-security-digest.md（kenny1337s-MacBook-Pro.local），box 副本：/home/box/workspace/security-watch/reports/2026-11-02-x-security-digest.md
