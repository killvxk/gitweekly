# X 安全情报晚报 · 2026-11-04

覆盖窗口：2026-11-03 20:15 至 2026-11-04 20:10（America/Santiago，UTC-3），约 24 小时。X 只读读取 15 次（主题检索 4 次、LWiS 全部 500 个成员分 10 组检索、引用帖批量查询 1 次），0 次 429；全部为本窗口新帖，不与 seen_ids 重复。t.co 已逐条展开（只有图片的帖只列原帖）。公开备援：CISA KEV JSON（**2026.11.04，共 1768 条，Δ+1**）、NVD、厂商与研究机构页面。IoC 一律 defang。本报告为防御向，不转载利用代码、payload 或复现步骤。

## 今日摘要

- **APT29 移动端水坑（Sekoia「Poisoned Source」）**：被入侵网站、仿冒站（america250、The OWO 酒店）和乌克兰分析服务 Plerdy 的一周供应链投毒（8-27 至 9-03），向未打补丁的 iOS／Android 投放 n-day 零点击链（含 DarkSword），窃取 cookie、Wi-Fi 密码乃至整机数据。全部漏洞已有补丁，**更新系统即可防御**。带完整域名／IP／哈希。
- **KEV 新增 Apple CVE-2024-27834（PAC 绕过，11-04 加入，due 11-18）**——正是上面 APT29 iOS 16.7 链 A 的第二阶段。
- **WordPress 119977（due 11-06）** 在野请求量继续升（THN 称 24 小时拦截 12,600+ 次）；**Ivanti** 有人公开了在野链中提权样本的 VirusTotal 哈希，Morphisec 蜜罐自 10-01 起记录 105 次 104935 尝试。
- **新漏洞**：Debian／Ubuntu APT CVE-2026-109518（中间人可替换包、以 root 执行，已出修复）；Rails 8.0.5.2／8.1.4.1 修复 21 个问题（含 Active Storage RCE 级）；SonicWall GMS 109593／109594（EOL，**不再修补**）；macOS launchd 提权 CVE-2026-112445 公开 PoC（修于 macOS 27.2）；Docker Desktop／WSL2 隔离绕过 112917；GLPI 11 SQLi＋XSS；runZero「Lights Out」BMC 研究多项仍无补丁。
- **恶意软件**：WithSecure Phexia（macOS ClickFix 后门＋窃密，用 Polygon 智能合约做 C2 中转，带大量 IoC）；fr0gger 发现 73 个伪装 AI 智能体工具的 GitHub 仓库投 SmartLoader→StealC；Kimsuky GitPower 仓库仍在线；ESET Gorbag（UAC-0226）GIFTEDCROOK。
- **工具**：impacket PR #2361 新增 MS-RPRN opnum 88 的 HTTP 强制认证；同类 WSD 端口监视器 BOF；defender_observer、AiSOC、pyghidra-mcp、ARES、ShellCoder；SpecterOps iSCSI 无 CHAP 攻击面博客。

## CVE / POC / 漏洞

### 1. CISA KEV：今日新增 Apple CVE-2024-27834（due 11-18）
Apple 多产品指针认证（PAC）绕过，需攻击者已有内存读写；2024-05 已在 Safari 17.5、iOS 16.7.8 等修复。今日入 KEV 与 Sekoia 披露的 APT29 iOS 链 A 直接对应（见 APT 第 1 条）。X 上 cvedotnow、timsonner 报道，未见公开 PoC。
- X 原帖：https://x.com/cvedotnow/status/2118073464577745048 ；https://x.com/timsonner/status/2118091957780234724
- 厂商公告：https://support.apple.com/en-us/120896
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2024-27834
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 其他：https://cve.now/CVE-2024-27834
- 地址／IoC：未见公开 IoC（相关链路 IoC 见 APT 第 1 条）

### 2. WordPress Core CVE-2026-119977：KEV 期限 11-06，攻击量继续上升
4.7.0–7.1.3 核心升级窗口 TOCTOU 竞态可致未认证 RCE，7.1.4 修复。今日 X 上：THN 称 24 小时内拦截 12,600+ 次利用尝试，另有帖称 18,500+ 次利用相关请求；2Workly 提醒监控 setup-config.php 等暂存路径；GHSA-4w3m-c66w-69mg（https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-4w3m-c66w-69mg）。CISA 要求同时做取证排查。
- X 原帖：https://x.com/TheHackersNews/status/2117855457901715501 ；https://x.com/itsMikeKipruto/status/2117879099448230169 ；https://x.com/DailyDarkWeb/status/2117837111789601200 ；https://x.com/Python_s_/status/2118005570108023197
- 厂商公告：https://wordpress.org/news/category/releases/
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-119977
- 地址／IoC：未见公开 IoC

### 3. Ivanti Connect Secure 链（104935＋111357＋118527）：样本哈希公开、蜜罐数据
buffaloverflow 公开了 UTA0576 在野链中 CVE-2026-111357 提权组件的 VirusTotal 样本（只记哈希，不转载内容）；Morphisec 称蜜罐自 10-01 起记录 105 次 104935 利用尝试。修复版本 25.1.1.3／22.8R2.6；10 月打过补丁的仍需再升级，Integrity Checker 可能漏检，建议先狩猎。111357 自 11-03 已逾期，118527 due 11-13。
- X 原帖：https://x.com/buffaloverflow/status/2117920466849366122 ；https://x.com/morphisec/status/2117778878097702977 ；https://x.com/MarwanMoftah/status/2117980840713924854 ；https://x.com/gurvrx/status/2117940095252897810 ；https://x.com/TheExploitHQ/status/2117802233425244643
- 样本：https://www.virustotal.com/gui/file/17277527c95289a7ce8d9f69b07829edfd2e099bd664d79e54d3e9cad2d8307b
- 厂商公告：https://hub.ivanti.com/s/searchallcontent?language=en_US （Ivanti 安全公告入口）
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-111357 ；https://nvd.nist.gov/vuln/detail/CVE-2026-104935 ；https://nvd.nist.gov/vuln/detail/CVE-2026-118527
- 地址／IoC：SHA-256 `17277527c95289a7ce8d9f69b07829edfd2e099bd664d79e54d3e9cad2d8307b`

### 4. Debian／Ubuntu APT CVE-2026-109518：中间人可替换已校验包并以 root 执行
需要 APT 重试失败下载（Debian 12、Ubuntu 22.04 起默认开启 Acquire::Retries）。Debian 已发修复；Ubuntu 26.10＝3.3.3ubuntu0.1、26.04＝3.2.1ubuntu0.1、24.04＝2.8.4ubuntu0.1、22.04＝2.4.15ubuntu0.1；Debian 11 有 2.2.5。CVSS 4.0 为 7.7。未见在野。经 HTTP 源和不可信镜像／代理的机器优先。
- X 原帖：https://x.com/Dinosn/status/2118043291857916123
- 文章：https://thehackernews.com/2026/11/debian-and-ubuntu-apt-flaw-lets-mitm.html
- 厂商公告：https://security-tracker.debian.org/tracker/CVE-2026-109518 ；https://ubuntu.com/security/CVE-2026-109518
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-109518
- 地址／IoC：未见公开 IoC

### 5. Rails 8.0.5.2／8.1.4.1：21 个安全问题
其中 GHSA-f3w6-w445-fwh9（Active Storage ImageMagick 分析器，Critical）、GHSA-v924-7rp8-4mxh（视频预览／图像处理文件读与 RCE，High），以及 Strong Parameters 绕过、RemoteIp 伪造、多个 XSS／DoS。Pruva 称已复现 f3w6 可经上传 SVG 达 RCE（无 CVE）。8.0 系列安全支持 11-07 结束。
- X 原帖：https://x.com/rails/status/2117952487399342533 ；https://x.com/pruvadev/status/2117998813013016797 ；https://x.com/N3mes1s/status/2117999067645325520
- 厂商公告：https://rubyonrails.org/2026/11/4/Rails-8.0.5.2-and-8.1.4.1-have-been-released
- GitHub 公告：https://github.com/rails/rails/security/advisories/GHSA-f3w6-w445-fwh9 ；https://github.com/rails/rails/security/advisories/GHSA-v924-7rp8-4mxh
- 复现说明：见上方 Pruva 原帖（不转载步骤）；Rails 发布页 https://rubyonrails.org/category/releases
- 地址／IoC：未见公开 IoC

### 6. SonicWall GMS CVE-2026-109593／109594：EOL，不再修补
GMS 9.5.2 及更早：109593 未认证读内部文件（Critical），109594 高权限 SQL 注入。SonicWall 明确不发补丁，建议迁移至 NSM；在迁移前把 GMS 从外网撤下。Pentest-Tools 报告。
- X 原帖：https://x.com/DarkWebInformer/status/2117768370871267545 ；https://x.com/Dinosn/status/2118000325311582505
- 文章：https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-unpatched-flaws-in-end-of-life-gms-software/
- 厂商公告：https://psirt.global.sonicwall.com/vuln-list
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-109593
- 地址／IoC：未见公开 IoC

### 7. macOS CVE-2026-112445：launchd 守护进程本地提权，PoC 公开
旧守护进程 com.apple.xpc.uscwoap 可被控制台普通用户启动并获 root；Apple 在 macOS 27.2 删除该文件修复。研究者 Mas0nShi 公开 GitHub PoC（此处不转载）。未见在野。共享 Mac 环境优先升级。
- X 原帖：https://x.com/Daily_CyberSec/status/2117789091005681822
- 文章：https://securityonline.info/macos-privilege-escalation-poc-cve-2026-112445/
- 厂商公告：https://support.apple.com/en-us/100100
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-112445
- 地址／IoC：未见公开 IoC

### 8. Docker Desktop／WSL2 隔离绕过 CVE-2026-112917
修复需同时满足 Docker Desktop 4.98.0+ **和** WSL 3.0.3+；只升级 Desktop 而 WSL 旧版仍受影响。Windows x86-64 WSL2 主机上非特权容器代码可越界。
- X 原帖：https://x.com/lee1981b/status/2117918086858715365
- 厂商公告：https://docs.docker.com/security/security-announcements/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-112917
- 地址／IoC：未见公开 IoC

### 9. GLPI ≤11.0.9：认证后盲注 SQLi＋存储型 XSS（Synacktiv）
任意已登录账户（最低 Self-Service）可经表单 actors 下拉接口盲注读库（含密码哈希、API token）；XSS 经 alternative_email。修复 11.0.10。GHSA-pjj6-ww22-86qh、GHSA-75jp-p2vm-9vmh。
- X 原帖：https://x.com/Synacktiv/status/2117900493015978193
- 厂商／研究公告：https://www.synacktiv.com/en/advisories/sql-injection-and-stored-xss-vulnerabilities-in-glpi-11
- GitHub 公告：https://github.com/glpi-project/glpi/security/advisories/GHSA-pjj6-ww22-86qh
- 地址／IoC：未见公开 IoC

### 10. runZero「Lights Out」：BMC／带外管理多项漏洞，部分无补丁
hdmoore 称最终公告已发布、OOBscan 已能检测全部问题；涉及 OpenBMC、Lenovo XCC2、HPE iLO、Huawei openUBMC、H3C HDM、Vertiv Avocent、Dell iDRAC、Supermicro 等。BMC 务必隔离到管理网。
- X 原帖：https://x.com/hdmoore/status/2118050013141995595 ；https://x.com/tifkin_/status/2118076605167997410
- GitHub：https://github.com/runZeroInc/oobscan#research-and-disclosures
- 地址／IoC：未见公开 IoC

### 11. 其他跟进
- **Zyxel GS1900 CVE-2026-107441**：X 上补充称背后为 JITTERLY 后门与 SIXZUT rootkit，修复固件 10-22。https://x.com/dailytechonx/status/2117954989662331012 ；https://x.com/Daily_CyberSec/status/2117794252746850423 ；文章 https://securityonline.info/zyxel-gs1900-zero-day-cve-2026-107441/
- **GitLab 97229**：仍有 1000+ 实例未修，KEV 期限已过。https://x.com/morphisec/status/2117961332121088237
- **Cisco ASA/FTD 76418**：只影响配置了次级认证的隧道组。https://x.com/k_kueck/status/2118059650470035745 ；厂商 https://sec.cloudapps.cisco.com/security/center/publicationListing.x
- **PHP2Shell**：Cloudflare 更新 WAF 规则（仅代理且开启拦截的流量有效，不等于修补 PHP）。https://x.com/infrastack_ai/status/2117890082711732536
- **Project Zero**：Samsung sgpu 文件级引用计数下溢（`amdgpu_job_free_cb`）。https://x.com/ProjectZeroBugs/status/2118004087543509196 ；https://project-zero.issues.chromium.org/issues/532525847

## 工具与 GitHub 发布

### 1. impacket PR #2361：MS-RPRN opnum 88 强制 HTTP 认证
可对运行打印后台服务的 Windows 目标强制发起 HTTP 认证并中继；同日 iPurple 转介绍经 WSD 端口监视器触发 IPP 关联、让机器账户（HOSTNAME$）走 HTTP 认证的 BOF。防御：禁用不需要的 Spooler、在 HTTP 端启用 EPA／签名、监控机器账户异常 HTTP 认证。
- X 原帖：https://x.com/abdo_mhanni/status/2117907410635596091 ；https://x.com/Defte_/status/2117910933229957582 ；https://x.com/ipurple/status/2117983202421649636
- GitHub：https://github.com/fortra/impacket/pull/2361
- 地址／IoC：未见公开 IoC

### 2. defender_observer：采集／回放 Defender AV 与 EDR ETW 遥测（C#／.NET 9）
- X 原帖：https://x.com/ipurple/status/2117968102717554834
- GitHub：https://github.com/dobin/defender_observer

### 3. AiSOC：开源 AI SOC（告警融合、LLM 分诊、ATT&CK 调查，自带 MCP server）
- X 原帖：https://x.com/ipurple/status/2118014084704788563
- GitHub：https://github.com/beenuar/AiSOC

### 4. pyghidra-mcp：把 Ghidra 接入 MCP 的命令行服务器
- X 原帖：https://x.com/r1cksec/status/2117884444992512437
- GitHub：https://github.com/clearbluejar/pyghidra-mcp

### 5. ARES（开源 AI 红队平台）与 ShellCoder（本地 LLM 漏洞开发助手）
仅限授权测试。ARES 自称 66 个攻击模块覆盖 AD／Windows／Linux／三大云。
- X 原帖：https://x.com/CyberAlertpit/status/2117914959460069667 ；https://x.com/iam_super_user/status/2117940558589239594
- GitHub：https://github.com/mafifrizi/ares ；https://github.com/iam-super-user/ShellCoder

### 6. SpecterOps：AD 域内无 CHAP 的 iSCSI 目标可被冒充访问虚拟磁盘
共享 SPN 常见于 Hyper-V、故障转移群集、DFS；文中附防御建议。
- X 原帖：https://x.com/SpecterOps/status/2118065498260644157 ；https://x.com/unsigned_sh0rt/status/2118070228035002797
- 文章：https://specterops.io/blog/2026/11/04/unauthenticated-iscsi-target-server/

### 7. 其他
- Outflank／Cobalt Strike：kyleavery 称新功能随今日 teamserver 发布；12-03 有反射加载器工作坊。https://x.com/kyleavery/status/2118064353660346574 ；https://x.com/_CobaltStrike/status/2118022265442844877
- Florian Roth：Q4 趋势（AI 驱动入侵框架 ARTEX／Cairn、供应链、OAuth 滥用、EDR 致盲）。https://x.com/cyb3rops/status/2118040342557778315 ；https://x.com/cyb3rops/status/2118101645619814572
- ESPJack（ESP32-S3 渗透工具包，未给仓库链接）：https://x.com/ipurple/status/2118117707300110538

## APT / Malware 分析

### 1. APT29「Poisoned Source」：水坑＋Plerdy 供应链投毒，打未修补的 iOS／Android（Sekoia TDR）
三种入口：直接注入合法网站（乌克兰天然气企业、美国化工行业协会、保加利亚军事相关站、欧洲极右政党站）、反向代理仿冒站（america250、The OWO 酒店）、Plerdy 统计脚本 8-27 至 9-03 被投毒。指纹脚本 UltimateFingerprinter 筛选后投放：链 A（iOS 16.7，CVE-2025-43529＋CVE-2024-27834，偷 cookie）、链 B（iOS 18.5，DarkSword 全链，偷短信／iMessage／邮件／WhatsApp／Telegram／钥匙串等）、链 C（Android Chrome 139–145（除 143），CVE-2026-3910＋Adreno CVE-2025-27038，AndroSnitch 偷 Chrome 与 Wi-Fi 密码）。全部为已修补 n-day。中等至高置信归因 APT29（SVR）。
- X 原帖：https://x.com/sekoia_io/status/2117909696778539279 ；https://x.com/TheHackersNews/status/2117988067499987406 ；https://x.com/Dinosn/status/2118021982826672554
- 研究报告：https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits
- 文章：https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html
- 相关 KEV：https://nvd.nist.gov/vuln/detail/CVE-2024-27834
- 地址／IoC：见汇总「APT29」小节（域名、IP、9 个 SHA-256）

### 2. Phexia：macOS ClickFix 后门＋窃密，用 Polygon 智能合约当 C2 中转（WithSecure W/Labs）
终端粘贴命令 → curl 下载 update.sh 等 → AppleScript 投放器写 LaunchAgent（10 月起标签伪装 com.Apple.<16 位小写>）→ 从 Polygon 合约 getServerURL() 取 C2 → 拉 bmodule；用 `dscl . authonly` 验证骗来的登录密码存入 ~/.passphrase，窃取浏览器、钥匙串、LastPass／NordPass 扩展数据，并部署 XMRig。C2 轮换后旧感染不立即跟随，历史 IoC 仍有效。
- X 原帖：https://x.com/WithSecure/status/2117897508525597030
- 研究报告：https://www.withsecure.com/en/resources-hub/w-labs/phexia-macos-malware/
- 地址／IoC：见汇总「Phexia」小节（合约、14 个 C2、8 个投递主机、上传 IP、矿池与钱包）

### 3. 73 个伪装 AI 智能体工具的 GitHub 仓库投 SmartLoader→StealC（fr0gger／SecurityBreak）
冒充 Claude skills、Codex、MCP server、OpenClaw，发 ZIP「安装包」；当天早上仍有 51 个在线。载荷 SmartLoader（Lua 加载器），通常再投 StealC 窃密。帖内未列仓库清单。
- X 原帖：https://x.com/fr0gger_/status/2118075954740547684
- 文章：https://newsletter.securitybreak.io/archive/hello-from-san-francisco-0973
- 地址／IoC：未见公开 IoC（帖仅附截图）

### 4. Kimsuky Operation GitPower：GitHub 暂存仓库披露三周后仍在线（VULONE）
仓库托管伪装 AnyDesk 的恶意载荷，延续昨日 LNK 钓鱼线。
- X 原帖：https://x.com/f1tym1/status/2118117254596309073 ；https://x.com/Daily_CyberSec/status/2117867624348451042
- 研究报告：https://vulone.com/blog/north-korean-kimsuky-group-operation-gitpower-github-staging-still-live-three-weeks-after-disclosure
- 文章：https://securityonline.info/kimsuky-operation-gitpower-github/ ；https://f1tym1.com/2026/11/04/kimsuky-operation-gitpower-staging-infrastructure-remains-active-on-github/
- 地址／IoC：本窗口未抄录到具体 IoC，请看 VULONE 原文

### 5. 其他威胁报告
- **ESET：Gorbag（UAC-0226）GIFTEDCROOK** 针对乌克兰国防与军事后勤，Telegram 做 C2 外传。X https://x.com/sh3ll_c0d3/status/2117957676021817847 ；文章 https://sh3llc0d3.com/blog/eset-unmasks-gorbag-uac-0226-russian-giftedcrook-infostealer-campaign-targets-ukrainian-defense-logistics/ ；ESET 入口 https://www.welivesecurity.com/en/
- **CartSiphon**：以经济利益为主的 VShell 集群（JUMPSEC）。X https://x.com/rst_cloud/status/2117868256438411388 ；原链接 https://www.jumpsec.com/guides/cartsiphon-a-financially-motivated-vshell-cluster/ （今晚抓取 404）；JUMPSEC 博客 https://labs.jumpsec.com/
- **Astaroth** 巴西金融木马生态深度分析。X https://x.com/rst_cloud/status/2117906204848542201 ；https://0x0d4y.blog/inside-brazils-financial-malware-ecosystem-deep-dive-into-the-astaroth/
- **Yoba** 滥用已签名 AI 应用做 DLL 侧载投矿工（PolySwarm）。X https://x.com/rst_cloud/status/2117845183542788535 ；https://blog.polyswarm.io/yoba-malware-campaign-abuses-signed-ai-applications-to-evade-detection
- **3AM 勒索打欧洲学校**：人＋AI 智能体混合操作（Bitdefender）。X https://x.com/rst_cloud/status/2118052749275283671 ；https://www.bitdefender.com/en-us/blog/businessinsights/3am-ransomware-hybrid-ai-attack
- **pentestcode AI 智能体被用来打 25 家欧洲企业**，自称攻破 10 家（Huntback 开放目录调查）。X https://x.com/rst_cloud/status/2117852773110677675 ；https://huntback.io/blog/pentestcode-operator-open-directories
- **NIKKE PC 启动器投放远控**：vx-underground 称公开分析多为 AI 水文、无样本。X https://x.com/vxunderground/status/2118023701337678081 ；https://x.com/Dinosn/status/2117976929282207922 ；https://cyberinsider.com/nikke-pc-launcher-malware-remote-access-tool/
- **Google 日历钓鱼劫持会话、绕过 MFA**：https://x.com/Dinosn/status/2118000396958630318 ；https://www.bleepingcomputer.com/news/security/google-calendar-phishing-campaign-hijacks-sessions-bypasses-mfa/
- **OpenAI Codex「越狱工具包」藏提示词广告件**：https://x.com/Dinosn/status/2118043345234825514 ；https://thehackernews.com/2026/11/researchers-uncover-prompt-adware.html
- **欧洲超市冰柜攻击波及法国血库冰柜**（血液供应未受影响）：https://x.com/KimZetter/status/2117992461347782999 ；https://www.politico.eu/article/fridge-hacks-hit-french-blood-banks/
- **勒索受害者声明（未证实，仅作线索）**：FalconFeeds 列出 Unilever（WHITEARMOR）、IHG（Byod）、Sig Sauer（SCARLETTGROUP）、MAPFRE 巴西（新团伙 DESTELLO）、El Cajon 市政（Rhysida）等。https://x.com/FalconFeedsio/status/2118098643924516938 ；https://x.com/FalconFeedsio/status/2117774857006186666 ；https://x.com/FalconFeedsio/status/2117943465527119974 ；https://x.com/FalconFeedsio/status/2117999322646393318 ；https://x.com/FalconFeedsio/status/2118049251045613591

## 地址／IoC 汇总

所有条目已 defang，仅供检测与封堵。

### APT29「Poisoned Source」（来源：Sekoia）
仿冒站（反向代理）：
- `america250[.]holiday` — 192.121.46[.]25（EDIS GmbH，AS9009），投递域 `adsprism-stat[.]com`
- `theowo[.]club` — 188.190.17[.]232（EDIS GmbH，AS57169），投递域 `static.flux-telemetry[.]com`

投递与外传：
- `static.flux-telemetry[.]com` — 109.104.106[.]107（Shock Hosting，AS395092），投递
- `edge-ord.clouds-stacks[.]com` — 95.133.231[.]28（servinga GmbH，AS219399），投递／负载均衡
- `ad.starx-net[.]com` — 195.58.140[.]105（AS395092），外传 `hxxps://ad.starx-net[.]com:8881/telemetry/v12`
- 其他投递：`ads-it-assets[.]com`、`cdn.adv-static[.]com`、`wpvortex-mod[.]com`、`assets-int[.]com`
- 被投毒脚本：`hxxps://a.plerdy[.]com/public/js/click/main.js`（2026-08-27 至 09-03）
- 指纹脚本文件名：`5b4c8fea5cbcee273e8d830f52-temfp.js`；iOS 防重放 cookie：`VDGH_TOKEN_REF`

SHA-256：
- `a7d2493df00565c21587b0cad2a9fe7ca1e5590acf796da6e499be0ffde44cc3`（Class-A-Stage1）
- `bee3e014e3df87ddce0250b0985b87f6868a427a7b650a74b7ffedb9d57f3088`（Class-A-Stage2）
- `c170fda024183645c0aa681149304e50506509c3498bb6b9a5f5ced6aa73e5fa`（Class-B-Stage1）
- `2ffb35e3f9e55286a930fb887e73764a913166648135fe0ca7551736d97d7bfa`（Class-B-Stage2）
- `69b6cb327a4d5da99399718f6a66f84de69f89425b0a31f2dcee0682f811596f`（Class-B-Stage3）
- `29d283ebd08d0cd3b2e6f4a67718d3d6e7a6be01d0613d716bce218dba57a928`（Class-C-Stage1-JS）
- `06c17b31d36838f3d29044784aa047d5c2d9174d3356c1211cf25f9df677445f`（Class-C-Stage2-JS）
- `183d62d682aea8018491c8559544e8d6a9ab0e1abd05ecbb6c97daa4f438d2b8`（Class-C-Stage2，CVE-2025-27038）
- `387a7fb768db1350a9788d9704e7a72abe07152734e0ff026af72b417e36268c`（AndroSnitch）
- 文中另列：`35c0cd19a7334b544c193e392bcd9a8f1d1f43cf6b61be5bf1d9e35537aff2ef`（B /v1）、`621112712ec515e8791129c62feda8fff6654a0116882401609503cacc08054a`（B /v2）、`ae3241d96cc2d99538c7aff60f382cc8dac13859bcbea3ee84992d24d22a8108`（C v139–144）、`41e6fd33a30d36dabff9ea408d9766a6583edcc107968f6dc1499f2586381967`（C v145）

### Phexia（来源：WithSecure）
- Polygon 合约：`0xA3a603F8a454a9c905b4c579Bb72628F7C15C2A0`（选择器 `0x2686ecea`，6–10 月）；`0x3445fB8Df432320251f611e691fe6B0C6664C960`（10-27 新构建，解析到 dhsbdgs[.]icu）
- C2：`hf98x4d[.]site`、`apdhlhs3[.]xyz`、`j9af4sr[.]guru`、`67sixcebeh[.]surf`、`stv4ec5[.]shop`、`vg5sgxv[.]lol`、`d9mjs[.]sbs`、`jse8x92s[.]me`、`couhe79[.]xyz`、`xzttyt[.]xyz`、`secdarvin2026[.]icu`、`oreshnik[.]top`、`svo-zv[.]pro`、`dhsbdgs[.]icu`
- 投递主机：`hackersteersman[.]digital`、`coeuzgoq.bahisbiz[.]com`、`kefavkd.nextbahis[.]sex`、`d9j.everunningshoes[.]com`、`nox.usa-synadentix[.]com`、`zwa8.meritbethizligir[.]com`、`355uz90z.bolnhurstrally[.]site`、`7ulk.irvinaurus[.]fit`（脚本名 update.sh／script.sh／clear-cache.sh／Terminal.sh）
- 上传服务器：`hxxp://62.60.226[.]50/upload.php`
- 矿池：`pool.hashvault[.]sh:443`、`pool.supportxmr[.]com:3333`
- 门罗币钱包：`4ApYm7Cp1QKHYd34eWHTLMR9JwGxEiPkP5GYNbD7UaGUBsAE31oRt8zbCiz7yV6BbHa5mZUGYxeMRbihPXxo9o3vNWJxx2L`；`82hSZSZNcbCdWd3ESkMDnC5cegaJnFhcG8PUBkMPof5mEdMDCF8cLcE1QuW4h82ggwi4qtfnRwMEgZPKQEnogkvmLFuRLFv`
- 主机痕迹：`~/Library/LaunchAgents/com.<16 位小写>.plist`、`com.Apple.<16 位小写>.plist`、`~/.passphrase`、`~/.txid`、`~/tempFolderC/`、`/tmp/rigupdater/`、`/tmp/applecomlistupdate/`、`/tmp/updstat.txt`

### Ivanti 在野链（来源：buffaloverflow／VirusTotal）
- SHA-256 `17277527c95289a7ce8d9f69b07829edfd2e099bd664d79e54d3e9cad2d8307b`（CVE-2026-111357 提权组件）

### 其他条目
- 未见公开 IoC：Apple 27834、WordPress 119977、APT 109518、Rails、SonicWall GMS、macOS 112445、Docker 112917、GLPI、BMC、SmartLoader 仓库（帖仅截图）、Kimsuky GitPower（本窗口未抄录）、GIFTEDCROOK 及其他简讯。

### KEV 状态（2026.11.04／1768／Δ+1）
- 新增：CVE-2024-27834 Apple（11-04 加入，due 11-18）
- 即将到期：CVE-2026-119977 WordPress（11-06）、CVE-2026-48356 Adobe Commerce/Magento 与 CVE-2026-111497 Google Brotli（11-10）、CVE-2026-41709 VMware ESX（11-11）、CVE-2026-118527 Ivanti（11-13）
- 已逾期（节选）：Plex 96652／96655、Siemens 110936（due 11-03，自 11-04）；Ivanti 111357（due 11-02，自 11-03）；GitLab 97229、Cisco 76418（due 11-01，自 11-02）；Fragnesia 46300（due 10-31，自 11-01）

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

本日首次覆盖 LWiS 全部 500 个成员（10 组检索），共约 80 条新帖，多数为非技术内容（选举等）。已并入上文的有：Synacktiv（GLPI）、SpecterOps／unsigned_sh0rt（iSCSI）、ProjectZeroBugs（Samsung sgpu）、buffaloverflow（Ivanti 样本）、fr0gger_（SmartLoader 仓库）、tifkin_ 转 hdmoore（BMC）、Defte_ 转 abdo_mhanni 与 ipurple（强制认证、Defender 遥测、AiSOC）、cyb3rops（Q4 趋势）、Dinosn（APT、Rails、SonicWall 等新闻）、N3mes1s（Rails RCE 复现）、KimZetter（冰柜攻击）、vxunderground（NIKKE）、kyleavery／_CobaltStrike（Outflank 发布）。博客清单交叉：SpecterOps（https://posts.specterops.io/ ）、Synacktiv（https://www.synacktiv.com//en/publications.html ）、JUMPSEC（https://labs.jumpsec.com/ ）、Outflank（https://outflank.nl/blog/ ）在清单内；Sekoia、WithSecure 不在清单内，已直接引用厂商原文。

## 来源搜索 URL

- X Latest：CVE／PoC／exploit／0day：https://x.com/search?q=(CVE%20OR%20PoC%20OR%20exploit%20OR%200day)%20-is%3Aretweet&f=live
- X Latest：github.com＋C2／红队／nuclei：https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- X Latest：malware analysis／threat report／threat actor：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)&f=live
- X Latest：APT 组织名＋report／IOCs：https://x.com/search?q=(APT29%20OR%20Lazarus%20OR%20Kimsuky)%20(report%20OR%20IOCs)&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/vuln/search
