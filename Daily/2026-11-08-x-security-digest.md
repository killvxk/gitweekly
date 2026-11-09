# X 安全情报晚报 · 2026-11-08

覆盖窗口：2026-11-07 20:15 至 2026-11-08 约 20:15（America/Santiago，UTC-3），约 24 小时（窗口内最晚收录帖为 20:04）。X 只读读取 **10** 次（search_posts_all 主题检索 ×3、LWiS 成员 `from:` 抽样前 135 名 ×3、事件定向 ×2、get_posts_by_ids ×1、search_news ×1），**0 次 429**；与 state.json seen_ids 去重，过滤广告、课程引流、空转发与明显玩笑帖（如「CVE-1944-0002 Enigma」）。t.co 已用 `curl -sI` 展开。公开备援：CISA KEV JSON（**2026.11.06，共 1769 条，Δ0**，周日无更新）、SANS ISC、nginx.org／F5、ZDI、Cisco Talos、Lumen、Volexity／Proofpoint、BleepingComputer、The Hacker News 等。IoC 一律 defang。本报告为防御向，不转载利用代码、payload 或复现步骤。

注：今天是周日，X 上新内容偏少，不少高互动帖是 10 月底／9 月旧报告回流（Silent Train、KeyDrift、BlueMoon、APT29 水坑），下文已标注「旧闻回流」，不当作新事件。

## 今日摘要

- **CISA KEV 周末无更新（2026.11.06／1769／Δ0）**：WordPress Core CVE-2026-119977（due 11-06）、Ivanti CVE-2026-111357（due 11-02）仍逾期；**后天 11-10 到期** Google（Brotli）CVE-2026-111497、Adobe CVE-2026-48356；11-11 Broadcom CVE-2026-41709；11-13 Ivanti CVE-2026-118527；11-18 Apple CVE-2024-27834；11-20 SonicWall CVE-2026-19868。
- **OpenSSH *sshole（CVE-2026-123158）扫描数据**：SANS ISC Johannes Ullrich 今日发文，Cowrie 蜜罐自 11-05 起看到真正的利用尝试（全「A」长密码），11-06 峰值 713 次，之后回落；附首批扫描源 IP 列表（见 IoC 节）。补丁建议不变：升级 OpenSSH 10.6p2／发行版补丁并重启 sshd，或关闭 `PasswordAuthentication`。
- **LNbits 紧急通告：所有运营者立即关停服务器**：攻击者可擅自创建账户并提走资金，单个 BitTipBot 实例被盗 2,285,545 sats；官方停掉 my.lnbits.com 托管服务，补丁预计 24–48 小时内发布，暂无 CVE。
- **Claude Code「不再询问」写入明文密钥**：Apiiro 在公开 GitHub 找到 1,122 份含密钥的 `.claude/settings.local.json`（共 1,379 个密钥，其中 215 份 Gitleaks 和 TruffleHog 都漏报）。先轮换密钥，再从仓库与历史中移除并在仓库级 `.gitignore` 加入该文件。
- **其他漏洞**：MLflow CVE-2026-118628 未认证 SSRF（ZDI-26-844，CVSS 8.2，修复于 3.17.0）有公开请求级 PoC；nginx CVE-2026-42533（map＋regex 堆溢出）有人宣称有可绕过 ASLR 的公开利用代码，属 7 月旧洞但值得复查版本，nginx 当前最新为 1.31.7／1.30.6；Tenda AC19 CVE-2026-123966 公开利用、无补丁。
- **未经证实的说法**：@CrackmesOne 称发现 VirtualBox 与 UTM 最新版的 guest-to-host 逃逸（0day，仅有视频）；@gergely_kalman 发布「新 macOS LPE」视频，无 CVE 与细节；VECERT 称 RansomSwagger 在地下论坛出售「DarkMatter 勒索软件」源码。三者均未见厂商确认。
- **APT／Malware**：今日无全新的大型厂商报告；X 上回流的是 Lumen「Silent Train」（Volt Typhoon）＋Talos KeyDrift（UAT-11473，Cisco SD-WAN CVE-2026-20127）、Volexity／Proofpoint BlueMoon（Chrome＋Windows 链，VT 新上样本哈希）、Sekoia APT29 水坑。勒索方面 DeadLock、Akira、Qilin、SafePay、WhiteArmor、PixelLeaks 有新受害者帖。
- **工具**：BLA（干扰 AI 逆向的诱饵注入工具）、Malspark（多智能体恶意软件分析平台）、CyberStrike、viperclaw，以及 Nous Research 为 Hermes Agent 发布的安全插件。

## CVE / POC / 漏洞

### 1. OpenSSH *sshole CVE-2026-123158：SANS ISC 蜜罐扫描数据（续报）
SANS ISC 用 Cowrie 蜜罐统计超长密码登录：11-01 有 23 次但与漏洞无关（是把下载命令错放进密码字段的劣质暴力脚本）；真正的利用尝试从 11-05 开始，计数为 11-05 232、11-06 713、11-07 246、11-08 51。作者认为不少尝试可能在蜜罐上成功，会继续跟进。ICHI 等聚合账号同步转发。防御：打补丁并重启 sshd；在 musl 无 PAM 系统（Alpine、OpenWrt、Buildroot、Yocto）上关闭密码登录；用下方 IP 列表回查 sshd 日志里的 `Accepted password`。
- X 原帖：https://x.com/sans_isc/status/2119456283590037577
- X 转述：https://x.com/ICHI_Global/status/2119536616922370081 、https://x.com/Npj8448/status/2119371771791155519
- 文章：https://isc.sans.edu/diary/33498
- 厂商公告：https://www.openssh.com/security.html （OpenSSH 安全页）
- 地址／IoC：见「地址／IoC 汇总」sshole 节（1 个下载 URL＋18 个扫描源 IP）

### 2. LNbits 实例被批量盗币，官方要求全部关停
LNbits（开源闪电网络钱包／账户系统）11-08 发紧急通告：攻击者在暴露公网的实例上创建未授权账户并提款；BitTipBot 运营者 5 小时内损失 2,285,545 sats。官方暂停 my.lnbits.com，修复预计 24–48 小时，暂无 CVE、无公开利用细节。影响仅限 LNbits，不涉及闪电网络协议本身。防御：立即停机或断开公网；补丁发布后升级；回查新建账户与随后的提款记录。
- X 原帖（X 新闻摘要）：https://x.com/i/trending/2119471425191034893
- 文章：https://thedefiant.io/news/security/lnbits-urges-all-server-operators-to-shut-down-after-attacks
- 文章：https://news.bitcoin.com/security/lightning-network-security-scare-forces-lnbits-servers-offline/
- 狩猎思路：https://ctxsec.com/items/hunt-lnbits-new-accounts-unexpected-withdrawals-nov-8
- 厂商公告：本次未取到 LNbits 官方公告的独立 URL（以上为二手报道）
- 地址／IoC：未见公开 IoC

### 3. Claude Code「Yes, and don't ask again」把命令中的密钥存成明文
Apiiro 统计公开 GitHub 上 104,185 份 `.claude/settings.local.json`，其中 1,122 份含至少一个真实密钥（共 1,379 个，含数据库密码、AWS 密钥、Supabase service-role key 等），215 份两种主流扫描器都漏掉。原因：批准规则会保存完整命令；忽略规则只写进本机全局 git excludes，不在仓库 `.gitignore`。Anthropic 称在评估修正。防御：搜组织内所有仓库及历史（`git log --all -- .claude/settings.local.json`），先轮换再清理。
- X 原帖：https://x.com/jondot/status/2119317746362273832 、https://x.com/pandaxia0613/status/2119290098806366498 、https://x.com/plavecmario3/status/2119483564752273485
- 文章：https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html
- 文章：https://latent.tokyo/en/articles/2026-11-08-claude-code-dont-ask-again-secrets
- 地址／IoC：未见公开 IoC

### 4. MLflow CVE-2026-118628 未认证 SSRF（有公开 PoC）
`get-artifacts` 不校验客户端提供的 artifact URI，未认证即可让服务器连接任意主机（含云元数据端点）。CVSS 8.2，修复于 MLflow 3.17.0（PR #25891，GHSA-mr9f-g8qf-4w4j）。防御：升级；MLflow 跟踪服务器默认无认证，不要暴露公网；检查实验的 artifact_location 是否有陌生主机。
- X 原帖：https://x.com/ZeroPathLabs/status/2119300332022870206
- 厂商公告：https://www.zerodayinitiative.com/advisories/ZDI-26-844/
- 修复：https://github.com/mlflow/mlflow/pull/25891
- 文章：https://zeropath.com/blog/cve-2026-118628-mlflow-get-artifacts-ssrf
- 厂商公告：https://access.redhat.com/security/cve/cve-2026-118628
- 地址／IoC：未见公开 IoC

### 5. nginx CVE-2026-42533（map＋regex 堆溢出）再被炒热
xer0dayz／Sn1per 称已有可绕过 ASLR 的公开利用代码并发布 nuclei 检测模板。该洞 7 月已修（1.31.3／1.30.4），但 nginx 之后又修了多批漏洞，当前安全版本为 **1.31.7+／1.30.6+**。AlmaLinux 8/9/10 的修正包曾引发 HTTP 500，已发测试版修复。缓解：不用匿名捕获，改用唯一命名捕获且只在同一块中引用。
- X 原帖：https://x.com/xer0dayz/status/2119475155927728479 、https://x.com/tarohs/status/2118855208021504405
- 厂商公告：https://nginx.org/en/security_advisories.html
- 厂商公告：https://my.f5.com/s/article/K000162097
- 厂商公告：https://msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2026-42533
- 文章：https://sn1persecurity.com/wordpress/cve-2026-42533-nginx-map-heap-overflow-detection-with-sn1per/
- 地址／IoC：未见公开 IoC

### 6. 未证实的 0day 说法（仅供关注）
- **VirtualBox／UTM 虚拟机逃逸**：@CrackmesOne 称用 AI 找到两条最新版 guest-to-host 完整逃逸链（11k 浏览，仅视频，无厂商确认、无 CVE）。若在 VM 里跑不可信样本，暂时别依赖这两款作为隔离边界。
  - X 原帖：https://x.com/CrackmesOne/status/2119251565718483101
- **新 macOS LPE**：@gergely_kalman（LWiS 成员）仅发视频。
  - X 原帖：https://x.com/gergely_kalman/status/2119221736784961657
  - 视频：https://twitter.com/gergely_kalman/status/2119221736784961657/video/1
- 地址／IoC：未见公开 IoC

### 7. 其他
- **Tenda AC19 CVE-2026-123966**（CVSS 9.3，堆溢出，公开利用，无补丁）：https://x.com/cveintelligence/status/2119260244031484351 ；https://learnctem.com/cve-intelligence-hub/cve-2026-123966
- **WP Libre Form CVE-2026-118423**（CVSS 10，PoC，无修复，昨日已报，建议停用插件）：https://x.com/exploitgrid/status/2119451125975851029 ；https://exploitgrid.net/exploits/3aa97ac0-51d6-4c09-836a-0cf6190efe98
- **Ivanti UTA0576**（Volexity，链 CVE-2026-104935＋CVE-2026-111357；Integrity Checker 可能漏检）：https://x.com/vulnpulse_app/status/2119400258338001193 ；https://vulnpulse.app/actors/uta0576
- **CISA KEV 联邦期限**：https://www.cisa.gov/known-exploited-vulnerabilities-catalog ；JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- 地址／IoC：未见公开 IoC

## 工具与 GitHub 发布

### 1. BLA（Blind LLM Agents）——干扰 AI 逆向的构建期加固
向 Electron、WebAssembly、原生二进制注入假密钥、资源陷阱和误导逻辑，让 AI 逆向代理消耗更多 token，运行时行为不变。MIT 开源，作者提醒倍数因目标而异。
- X 原帖：https://x.com/xteam3301/status/2119481837609521339
- X 新闻：https://x.com/i/trending/2119471426621288551
- GitHub：https://github.com/qybaihe/bla

### 2. Malspark——开源多智能体恶意软件分析平台
自托管，LLM 代理调用插件工具和沙箱，报告中每条结论引用对应工具调用。
- X 原帖：https://x.com/Root0ne/status/2119488201916305410
- GitHub：https://github.com/Root0ne/Malspark
- 官网：https://malspark.com

### 3. 进攻向 AI 框架（仅限授权测试）
- CyberStrike（13+ AI 代理的进攻安全框架）：https://x.com/ptlegion/status/2119439975829700739 ；https://github.com/CyberStrikeus/CyberStrike
- viperclaw（面向 Claude Code／Codex／Cursor 的进攻安全 harness 与 MCP 服务器）：https://x.com/zahidoverflow/status/2119530749200322700 ；https://github.com/zahidoverflow/viperclaw
- Nous Research Hermes Agent 安全插件（验证型漏洞扫描，导出 SARIF）：https://x.com/i/trending/2119541236256415755

### 4. 其他
- nuclei 检测模板（nginx 42533／42945，Sn1per）：https://sn1persecurity.com/wordpress/cve-2026-42945-nginx-rift-heap-overflow-detection-with-sn1per/
- FLARE-VM 介绍帖（逆向分析环境）：https://x.com/EsGeeks/status/2119517006328188980 ；https://github.com/mandiant/flare-vm
- BlueMoon／UTA0560 CrowdStrike 狩猎查询（HuntPack）：https://slapopotamus.github.io/HuntPack/hunts/BlueMoon-JungleBamboo-UTA0560-Hunt.html
- 地址／IoC：未见公开 IoC

## APT / Malware 分析

### 1. BlueMoon 样本上 VT（旧闻回流＋新哈希）
@Now_on_VT 报告与 Volexity UTA0560 报告关联的样本已上传 VirusTotal。BlueMoon 链：Chrome V8 CVE-2026-85046＋CVE-2026-87491，Windows 内核 CVE-2026-85880；UTA0560 投 GRIMWEDGE JScript 后门，JungleBamboo（APT31）投 SUPERSTOMP＋LONGTALE 假 Gemini 扩展。原报告为 9 月。
- X 原帖：https://x.com/Now_on_VT/status/2119451613513351577
- 厂商报告：https://www.volexity.com/blog/2026/09/09/mind-the-patch-gap-multiple-chinese-threat-actors-chain-0-day-exploits-in-chrome-windows/
- 厂商报告：https://www.proofpoint.com/us/blog/threat-insight/once-bluemoon-multiple-state-aligned-threat-actors-rapidly-adopt-novel-exploit
- 地址／IoC：样本 SHA256、C2 域名与 IP、扩展 ID 见汇总节

### 2. Volt Typhoon「Silent Train」＋Talos KeyDrift（旧闻回流，10-28 发布）
Lumen Black Lotus Labs：Volt Typhoon 用快速轮换的 SOHO／IoT／企业设备链做 4–6 跳中继，确认 4 个 0day 战役（Versa Director CVE-2024-39717、N-able N-central CVE-2025-8875/8876、Cisco Catalyst SD-WAN CVE-2026-20127、Arista VeloCloud CVE-2026-16812）及疑似 Quest KACE。Talos：UAT-11473 利用 CVE-2026-20127 在 SD-WAN 控制器植入 KeyDrift（PolyFlame 注入 vdaemon、LittleFilch hook SSL_read 窃取 IPsec 密钥），基础设施与 Silent Train 高度重叠。
- X 原帖：https://x.com/hCharizard_/status/2119566826850103654 、https://x.com/0aPoplin/status/2119324039340765391
- 厂商报告：https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework
- 厂商报告：https://blog.talosintelligence.com/uat-11473-keydrift/
- 文章：https://www.bleepingcomputer.com/news/security/volt-typhoon-hides-zero-day-attacks-using-silent-train-framework/
- 地址／IoC：主机痕迹 `/var/tmp/vdaemon.bin`、`/var/tmp/vdaemon.conf`、模块 `libdssl.so`、`libcommon.so`、伪装名 `aaamgrd`（Talos 称 PolyFlame 样本中未发现硬编码 IP／域名）

### 3. APT29「Poisoned Source」水坑（旧闻回流，11-04 已报）
- X 原帖：https://x.com/DeathAngelSec/status/2119503118530699653
- 厂商报告：https://sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits
- 地址／IoC：见 2026-11-04 晚报

### 4. 勒索与地下市场
- DarkMatter 勒索软件源码据称被 RansomSwagger 出售（未证实）：https://x.com/VECERTRadar/status/2119433172358185312
- DeadLock 新受害者 Chonlatee Innovation（泰国）、Kadick Integrated（尼日利亚）：https://x.com/FalconFeedsio/status/2119456061908570246 、https://x.com/FalconFeedsio/status/2119493500756779146
- Akira：Calmont Wire & Cable（美国）：https://x.com/FalconFeedsio/status/2119510141469147559
- Qilin：XK net（墨西哥）：https://x.com/digvijay_k11/status/2119267530321879400
- SafePay：Ramat Academic Be'er Ya'akov（以色列）：https://x.com/digvijay_k11/status/2119248362721657180
- WhiteArmor：Clínica La Sagrada Familia（哥伦比亚）：https://x.com/FalconFeedsio/status/2119290420928852352
- PixelLeaks：TDS Technology（越南）：https://x.com/FalconFeedsio/status/2119271125880561678
- Rosstat 数据泄露（Silent Crow 与白俄罗斯网络游击队，X 新闻摘要）：https://x.com/i/trending/2119137176814305640
- 地址／IoC：未见公开 IoC（受害者官网不列为 IoC）

## 地址／IoC 汇总

所有条目已 defang，请勿直接访问。

**sshole CVE-2026-123158（SANS ISC diary 33498）**
- 劣质暴力脚本下载 URL：`hxxp://156.238.252[.]37:8000/bot.x86_64`
- 首批扫描源 IP：`213.86.169[.]133`、`152.233.50[.]185`、`92.255.57[.]7`、`195.178.110[.]78`、`109.94.173[.]13`、`87.241.132[.]12`、`52.119.124[.]122`、`185.2.148[.]137`、`220.77.237[.]35`、`82.74.132[.]129`、`220.70.219[.]98`、`154.80.128[.]173`、`121.190.39[.]238`、`121.163.224[.]97`、`58.151.184[.]226`、`62.210.173[.]100`、`183.99.38[.]238`、`112.162.23[.]132`

**BlueMoon／UTA0560／JungleBamboo（Now_on_VT、Volexity、HuntPack）**
- SHA256：`3b71d721c39fad92a44ddd764bbb34afeae44a5db886d0a4827a399a5fbd367f`
- 投递 URL：`hxxps://cloud.shinewrist[.]net/ /Files1.html`
- C2 域名：`cloud.shinewrist[.]net`、`ocr.opusaccel[.]top`
- IP：`206.166.251[.]164`
- 计划任务名：`Windows Scheduled System`；文件：`msgbox.exe`、`wsc.dll`
- LONGTALE 扩展 ID：`ckiknalbeplpcpofpnabcnhjcegckfei`

**KeyDrift（Talos）**：`/var/tmp/vdaemon.bin`、`/var/tmp/vdaemon.conf`、`libdssl.so`、`libcommon.so`、`aaamgrd`

**其余条目**（LNbits、Claude Code、MLflow、nginx、Tenda、VM 逃逸、macOS LPE、工具发布、勒索帖）：未见公开 IoC。

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


今日 LWiS 抽样：成员前 135 名 `from:` 检索，原创帖 6 条，安全相关为 @gergely_kalman（macOS LPE 视频）；@vxunderground、@passthehashbrwn、@deadvolvo、@pomerium_io 为闲聊或产品帖，未收录为情报。

## 来源搜索 URL

- X Latest（CVE/POC/exploit/0day）：https://x.com/search?q=CVE%20OR%20PoC%20OR%20exploit%20OR%200day&f=live
- X Latest（GitHub＋C2/red team/nuclei）：https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- X Latest（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/vuln/search
- SANS ISC：https://isc.sans.edu/
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
