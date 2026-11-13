# X 安全情报晚报 · 2026-11-04（America/Santiago）

> 生成时间：2026-11-04 20:25（America/Santiago）＝ 2026-11-05 07:25（香港时间）
> X 覆盖：LWiS List 时间线三页共 287 帖，覆盖 2026-11-03 20:28 至 11-04 22:57 UTC（约 26.5 小时，完整覆盖本窗口 11-03 23:00 至 11-04 23:00 UTC）。Latest 搜索三组：「CVE/PoC/exploit/0day」按时间排序 25 条只覆盖 22:59–23:03 UTC（约 4 分钟，几乎全是体育／政治里的 POC、exploit 字样和钱包诈骗帖），所以加了两组按相关度排序的补搜（X 搜索接口不支持点赞数过滤，min_likes 条件被忽略），覆盖 11-04 约 00:02–21:10 UTC；GitHub 组 10 条，覆盖 01:33–22:14 UTC；malware/threat 组 24 条，只覆盖 20:20–22:56 UTC（约 2.6 小时，多是暗网泄露声明，只取了能核实的）。
> 公开备援：CISA KEV（2026-11-04 20:00 UTC 发布，共 1768 条，本窗口新增 1 条：Apple CVE-2024-27834）、厂商公告（Debian／Ubuntu、Rails、Google Android、Xen、Airbyte／JVN）。
> 验收：采集、成稿、链接核验均通过。非 X 链接 83 条：80 条返回 200（含已改正的 Android 公告地址）；cisa.gov 两条与 medium.com 一条返回 403（加 Referer 重试后仍是 403，浏览器可正常打开）。X 原帖 id 均来自本次 API 读取结果。

## 今日摘要

- **Debian／Ubuntu APT 中间人提权 CVE-2026-109518**：恶意镜像或能改 HTTP 流量的人，可以在包通过校验后再替换内容，最终以 root 执行代码。Debian 12+、Ubuntu 22.04+ 默认受影响，修复版已发布，今天就该升级 apt。
- **Rails Active Storage GHSA-f3w6-w445-fwh9（CVSS 9.8，暂无 CVE）**：用 ImageMagick 处理附件的应用，上传即可任意写文件，用 Disk 存储时还能任意读文件（可读到 secret_key_base）。升级到 8.1.4.1／8.0.5.2。
- **在野利用新增**：Airbyte 自托管版 RCE 已被利用（JVN#12040144，升 2.2.0）；KEV 新增 Apple CVE-2024-27834（截止 11-18）；GitLab CVE-2026-97229 仍有 1000+ 台未修；Ivanti Connect Secure 链条（UTA0576）有研究者公开了提权样本哈希和攻击者代理轮换 IP。
- **虚拟化逃逸两连**：AWS Firecracker 快照恢复逃逸 CVE-2026-122192（修于 1.16.2／1.17.0）；Xen XSA-523（CVE-2026-102703/102704）恶意 VM 可读写其他 VM 内存，4.6 起全受影响。
- **Android 11 月补丁**：CVE-2026-58868 零交互 RCE（Android 14–17，补丁级别 2026-11-01）。
- APT／事件：Sekoia 披露 **APT29「Poisoned Source」**水坑（篡改乌克兰 Plerdy 统计脚本，向 iOS／Android 投 N-day 链）；CrowdStrike 披露中国 **Vapor Panda** 用 ARTEX AI 代理 3 周打 200+ 机构；ESET 披露 **SlippyNunchucks** 劫持搜狗输入法 DNS 投 DarkVigil（含香港目标）；**73 个伪装成 AI agent 工具的 GitHub 仓库**投 SmartLoader→StealC；法国血液中心 EFS 冷柜被篡改。
- 工具：impacket PR #2361 新增 MS-RPRN opnum 88 的 HTTP 强制认证；RustHound-CE v2.5.40 支持经 ADWS 收集 AD；runZero OOBscan 收录 BMC「Lights Out」全部 CVE（不少仍无补丁）。
- SecureFlow：ZDI 公开 5 个 **Ashlar-Vellum Cobalt 0day**（无补丁）和 MailEnable 目录穿越；HackerOne 新公开 11 份 **MariaDB Connector（C／C++／ODBC／r2dbc）**漏洞报告。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

### 1. Debian／Ubuntu APT CVE-2026-109518：中间人可在校验后篡改软件包并以 root 执行
能篡改 APT 与软件源之间 HTTP 流量的人（恶意镜像或代理）可借 HTTP 重定向和临时服务器错误让 APT 重试下载，在安装时以 root 执行代码；暂无在野利用报告。Debian 12、Ubuntu 22.04 起默认受影响；更老版本若手动开了 `Acquire::Retries` 也受影响。Debian 已发 apt 3.0.4（Debian 13）及 Debian 11 的 2.2.5；Ubuntu 已发 26.10／26.04／24.04／22.04 的新 apt。防御建议：立刻升级 apt；镜像尽量走 HTTPS；排查近期是否经不可信代理或镜像安装过包。
- X 原帖：https://x.com/IntCyberDigest/status/2117978169483395433 、https://x.com/just1cz/status/2118009777922228361 、https://x.com/Dinosn/status/2118043291857916123
- 文章：https://thehackernews.com/2026/11/debian-and-ubuntu-apt-flaw-lets-mitm.html 、https://www.phoronix.com/news/Debian-APT-MITM-RCE
- 厂商／NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-109518

### 2. Rails Active Storage GHSA-f3w6-w445-fwh9：上传即任意写文件，Disk 存储时可任意读（CVSS 9.8）
Active Storage 的 ImageMagick 分析器在附件挂上时就会运行，且没有限制可用的 coder，上传的 SVG 可以走到 MSL coder 读写服务器文件。用 Disk 服务时可读到 `secret_key_base` 和外部系统凭据，进而 RCE 或横向。修复版 8.1.4.1、8.0.5.2，目前无 CVE。防御建议：升级；升级前收紧 ImageMagick policy（禁用 MSL 等 coder）；若曾对外开放上传，轮换 `secret_key_base` 和存储的凭据。
- X 原帖：https://x.com/N3mes1s/status/2117968713597038745 、https://x.com/Dinosn/status/2117957750235771390
- 厂商公告：https://github.com/rails/rails/security/advisories/GHSA-f3w6-w445-fwh9
- 文章：https://thehackernews.com/2026/11/critical-rails-flaw-lets-attackers.html

### 3. Airbyte 自托管版任意代码执行，JPCERT/CC 确认在野利用（JVN#12040144）
2.2.0 之前，Connector Builder／Manifest Server 不限制声明式 manifest 能引用的 Python 类，即使没开 `AIRBYTE_ENABLE_UNSAFE_CODE` 也能在容器内执行命令。2.x 需 Workspace Reader 以上权限；1.x 旧 Helm chart 部署无需认证，且不会再修。Airbyte Cloud 无需处理。防御建议：升到 2.2.0（manifest-server 7.23.7）；只允许 Airbyte server 访问 Connector Builder；轮换容器里保存的各数据源凭据。
- X 原帖：https://x.com/f1tym1/status/2117997710066225445
- 厂商公告：https://jvn.jp/en/jp/JVN12040144/index.html 、https://github.com/airbytehq/airbyte/security/advisories/GHSA-g35w-6r6v-h4r7
- 文章：https://securityonline.info/airbyte-vulnerability-exploited/

### 4. Ivanti Connect Secure 链条（CVE-2026-104935 + 111357 + 118527）后续：提权样本与攻击者基础设施公开
已知 UTA0576 自 10-03 起把三个漏洞串起来拿到设备 root（22.8R2.4），并查询 Windows LAPS 密码和 BitLocker 恢复密钥，Integrity Checker 查不出。今天 @buffaloverflow 公开了 CVE-2026-111357 提权样本的 VirusTotal 哈希；etugen 爬到攻击者下一跳代理上的 9 GB 开放目录（含完整利用链、168 份运行日志和 AI agent 记忆文件），整理出攻击代理轮换 IP。KEV 截止：111357 为 11-02（已过），118527 为 11-13。防御建议：按 10-29 补丁再打一遍（10-13 打过的也要再打）；怀疑失陷就做取证并轮换 LDAP 等凭据；用下方 IoC 回查日志。
- X 原帖：https://x.com/buffaloverflow/status/2117920466849366122 、https://x.com/etugenio/status/2117871437734195312 、https://x.com/gurvrx/status/2117940095252897810
- 厂商／KEV：https://www.cisa.gov/news-events/alerts/2026/10/13/cisa-urges-patching-newly-exploited-vulnerabilities-ivanti-connect-secure
- 样本：https://www.virustotal.com/gui/file/17277527c95289a7ce8d9f69b07829edfd2e099bd664d79e54d3e9cad2d8307b
- 文章：https://etugen.io/blog/ivanti-zero-day-operation/

### 5. AWS Firecracker VM 逃逸 CVE-2026-122192（0.23.0–1.16.1）
使用 File 内存后端并带 balloon 或 virtio-mem 设备恢复快照时，过期的 KVM 内存槽让来宾访问到 Firecracker 自身内存，Coinspect 实现了来宾到 VMM 的逃逸。修于 1.16.2 与 1.17.0+（GHSA-48ww-rqpp-2mgm）。对多租户沙箱和 AI agent 沙箱影响大，尽快升级。
- X 原帖：https://x.com/coinspect/status/2118085901251440642 、https://x.com/julianor/status/2118033293614432755
- 厂商／NVD：https://github.com/firecracker-microvm/firecracker/security/advisories/GHSA-48ww-rqpp-2mgm 、https://nvd.nist.gov/vuln/detail/CVE-2026-122192
- 文章：https://www.coinspect.com/blog/firecracker-escape/

### 6. Xen XSA-523（CVE-2026-102703／102704）：恶意 VM 可读写其他 VM 内存
grant copy 批量拷贝时复用了已做过的权限检查，部分情况下该复查没复查。Xen 4.6 起全部受影响；XCP-ng 称单个失陷来宾即可接管整台宿主机；Qubes 4.3 已出修复。由 Anthropic 的 Claude 发现，Ada Logics 复核。暂无在野利用报告。
- X 原帖：https://x.com/Dinosn/status/2117958107070652822
- 厂商公告：https://xenbits.xen.org/xsa/advisory-523.html
- 文章：https://thehackernews.com/2026/11/xen-hypervisor-flaws-let-one-malicious.html

### 7. Android 11 月公告：CVE-2026-58868 零交互远程代码执行（Android 14–17）
FrameDecoder.cpp `onOutputReceived` 堆溢出导致越界写，无需用户交互。修复在补丁级别 2026-11-01 及以后；截至 11-04 未报告在野利用。企业 MDM 可按补丁级别筛出未更新设备。
- X 原帖：https://x.com/Dinosn/status/2117925532004180020 、https://x.com/Dinosn/status/2117967017445876196
- 厂商公告：https://source.android.com/docs/security/bulletin/2026/2026-11-01
- 文章：https://thehackernews.com/2026/11/google-patches-critical-android-flaw.html 、https://securityaffairs.com/202414/mobile-2/cve-2026-58868-critical-android-bug-could-let-attackers-run-remote-code.html

### 8. CISA KEV 新增 Apple CVE-2024-27834（Safari 等认证不当），截止 11-18
2024 年已修的老洞，11-04 被列入 KEV（勒索利用：未知）。没跟上系统更新的旧 macOS／iOS 设备要盘点。
- X 原帖：https://x.com/agentprime_io/status/2118076619449323771
- 厂商／KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog 、https://nvd.nist.gov/vuln/detail/CVE-2024-27834

### 9. GitLab CVE-2026-97229（CVSS 10，已在野利用）：仍有 1000+ 台暴露实例未修
CI/CD 正则表达式编译器的整数溢出，特定条件下未认证即可执行代码，修复版 19.4.2／19.3.5／19.2.8，CISA 已列 KEV。自托管 GitLab 请确认版本。
- X 原帖：https://x.com/techyoutbe/status/2117935140752015709
- 文章：https://www.bleepingcomputer.com/news/security/over-1-000-gitlab-servers-vulnerable-to-code-execution-attacks/
- 厂商／NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-97229

### 10. BMC／带外管理「Lights Out」研究收尾：Dell iDRAC、HPE iLO、Supermicro 等数十个 CVE，不少仍无补丁
runZero（HD Moore）公布最终公告，覆盖 OpenBMC、Lenovo XCC2、HPE iLO、华为 openUBMC、H3C HDM、Vertiv Avocent、Dell iDRAC、Supermicro，开源扫描器 OOBscan 已能检测全部问题。建议：BMC 管理口只放管理网段，不要暴露公网；用 OOBscan 自查。
- X 原帖：https://x.com/hdmoore/status/2118050013141995595 、https://x.com/tifkin_/status/2118076605167997410
- GitHub：https://github.com/runZeroInc/oobscan

### 11. 其他补丁与公告（简列）
- SonicWall GMS 9.5.2 及更早（已停止支持）两个不再修的漏洞 CVE-2026-109593（未认证读内部文件）／CVE-2026-109594，官方建议迁移到 NSM：https://x.com/Dinosn/status/2118000325311582505 、https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-unpatched-flaws-in-end-of-life-gms-software/
- Barracuda ESG 等多款设备 CVE-2026-116606（认证缺陷）／CVE-2026-111560（管理员命令注入为 root），限制管理口访问并打补丁：https://x.com/Dinosn/status/2117822450734190850 、https://www.scworld.com/brief/barracuda-networks-issues-patches-for-critical-security-vulnerabilities
- GLPI 11 盲注 SQL 注入与存储型 XSS（Synacktiv），升级到 11.0.10：https://x.com/Synacktiv/status/2117900493015978193 、https://www.synacktiv.com/en/advisories/sql-injection-and-stored-xss-vulnerabilities-in-glpi-11
- Genetec Security Center CVE-2026-65422：只读账户可拉取实时与归档视频，修于 5.14.1.2：https://x.com/xen_i0/status/2117906752662650938 、https://xen-i0.github.io/post-genetec-cve-2026-65422.html
- Project Zero：Samsung sgpu 驱动引用计数下溢（`amdgpu_job_free_cb`）：https://x.com/ProjectZeroBugs/status/2118004087543509196 、https://project-zero.issues.chromium.org/issues/532525847
- Cloudflare WAF 新增规则拦 PHP2Shell 相关 CVE-2026-109618／CVE-2026-115560：https://x.com/CFchangelog/status/2118116586951450995 、https://developers.cloudflare.com/changelog/post/2026-11-03-waf-release/

## 工具与 GitHub 发布（每条：说明 + 地址列表）

### 1. impacket PR #2361：MS-RPRN opnum 88 强制 HTTP 认证 + sudonoodle 的 IPP 强制认证 BOF
可以从运行打印后台服务的 Windows 主机强制发起 HTTP 机器账户认证，用于中继到 AD CS／LDAP。防御侧：关停不需要的 Spooler，启用 LDAP 签名／通道绑定与 AD CS 的 EPA。
- X 原帖：https://x.com/abdo_mhanni/status/2117907410635596091 、https://x.com/ipurple/status/2117983202421649636 、https://x.com/Defte_/status/2117910933229957582
- GitHub：https://github.com/fortra/impacket/pull/2361 、https://github.com/sudonoodle/BOF-coerce-ipp

### 2. RustHound-CE v2.5.40：支持通过 ADWS（SOAP，9389 端口）收集 AD 数据
防御侧：留意非域控管理主机对 9389/tcp 的大量查询。
- X 原帖：https://x.com/g0h4n_0/status/2118080747265270124
- GitHub：https://github.com/g0h4n/RustHound-CE

### 3. SpecterOps：AD 域里的 iSCSI 发起端／目标与无 CHAP 访问共享磁盘
猜中 IQN 即可访问磁盘，常与 Hyper-V、故障转移集群、DFS 共享 SPN。建议核查 iSCSI 目标是否启用 CHAP。
- X 原帖：https://x.com/unsigned_sh0rt/status/2118070228035002797 、https://x.com/SpecterOps/status/2118065498260644157

### 4. 检测与蓝队工具
- defender_observer（dobin）：采集、回放、分析 Defender AV／EDR ETW 遥测：https://x.com/ipurple/status/2117968102717554834 、https://github.com/dobin/defender_observer
- Microsoft-Antimalware-Engine ETW 事件解读：https://x.com/ipurple/status/2117952295002607727 、https://blog.deeb.ch/posts/defender-am-events/
- AiSOC 开源 AI SOC（告警融合、LLM 分诊、ATT&CK 调查，可自托管）：https://x.com/ipurple/status/2118014084704788563 、https://github.com/beenuar/AiSOC
- Suzaku（Yamato Security 云日志威胁狩猎）新版本：https://x.com/DirectoryRanger/status/2118097842594361847 、https://github.com/Yamato-Security/suzaku
- npmscan-action：在合并前拦截可疑 npm 依赖变化：https://x.com/Dinosn/status/2117828746120188281 、https://github.com/NPMscan/npmscan-action
- Insinuator：Entra ID 令牌窃取系列第 4 篇（OAuth 2.0 标准缺口）：https://x.com/DirectoryRanger/status/2118097793478951359 、https://insinuator.net/2026/11/token-theft-in-microsoft-entra-id-part-4-of-4-oauth-2.0-standard-gaps/

### 5. 红队研究（只记方向，供检测参考）
- SCRT（itm4n）：借 Microsoft Teams 会议 API 与 WebRTC 数据通道做 C2，检测需关注异常 Teams 会议流量：https://x.com/SEKTOR7net/status/2117234518755062119 、https://blog.scrt.ch/2026/04/21/from-a-regular-red-team-exercise-to-developing-a-custom-c2-channel-over-ms-teams/
- HyperLoader：在隔离 vCPU 内执行 shellcode 的加载器：https://x.com/papadelospapas_/status/2117900508589641839 、https://github.com/S12cybersecurity/HyperLoader
- Kali 博客：在 Kali 上构建 Windows C# 工具：https://x.com/kalilinux/status/2117991195079332215 、https://www.kali.org/blog/windows-csharp-payloads/

## APT / Malware 分析（每条：说明 + 地址列表）

### 1. APT29「Poisoned Source」：篡改乌克兰 Plerdy 统计脚本，对 iOS／Android 投 N-day 链（Sekoia）
10 月中发现。攻击者入侵网站、注册仿冒域名，并篡改乌克兰网站分析服务 Plerdy SEO Tracker 的脚本，先做指纹识别，再按平台投递 iOS 或 Android（Chrome 139–145）N-day 利用链，窃取浏览器 Cookie，部分情况下偷 Wi-Fi 密码或整机数据。防御建议：移动设备尽快更新系统和 Chrome；排查站点是否引用 Plerdy 脚本；拉黑下方域名与 IP。
- X 原帖：https://x.com/felixaime/status/2117893248366567427 、https://x.com/Dinosn/status/2118021982826672554
- 文章：https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits 、https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html

### 2. CrowdStrike：中国 Vapor Panda 借 ARTEX AI 代理 3 周攻击 200+ 机构
10-17 起针对 14 国 200 多个机构（外交部、某欧洲国家总统府与总理办公室、国防情报、美国 19 家医药／半导体／国防／核／金融机构、美比菲电信），约 70% 确认或中等置信度失陷；ARTEX + DeepSeek 让命令频率从每小时约 40 条升到 1500 条以上。另：印度 CERT-In 通报 CRAFTY FALCON 用 ARTEX、PentAGI、Cairn、CyberStrikeAI 攻击金融支付 API。防御建议：对边缘设备与 webshell 加强监测，关注异常高频的自动化命令节奏。
- X 原帖：https://x.com/CyberScoopNews/status/2118086134076969324 、https://x.com/choblin29/status/2117988157442646019 、https://x.com/cyb3rops/status/2118101645619814572
- 文章：https://cyberscoop.com/china-vapor-panda-agentic-ai-artex-campaign-crowdstrike/ 、https://medium.com/@cyb3rops/the-tipping-point-when-cyber-attacks-stop-being-limited-by-people-8f0395fdfe06

### 3. ESET：SlippyNunchucks 劫持搜狗输入法 DNS 请求投放 DarkVigil（FDMTP）后门，目标含香港
自 2026-07-01 起，利用 Windows 版搜狗输入法等中国软件的明文 HTTP 更新／配置请求，篡改 DNS 解析指向暂存服务器，投放 DarkVigil 后门，目标为香港、泰国、日本、越南、阿曼、斯里兰卡的机构与中文用户。防御建议：排查搜狗输入法等软件的 HTTP 请求被解析到异常 IP 的记录。
- X 原帖：https://x.com/Dinosn/status/2117958181859086370
- 文章：https://thehackernews.com/2026/11/china-aligned-hackers-hijack-sogou.html

### 4. 73 个伪装成 AI agent 工具（Claude skills、Codex、MCP server）的 GitHub 仓库投放 SmartLoader→StealC
SecurityBreak 发现，51 个仍在线。仓库复制 codex-mcp-go、mcp-superset、hermes-agent 等项目，SKILL.md 干净，陷阱在 README 里的 ZIP「安装包」（.bat/.cmd + LuaJIT + 伪装成 .txt 的混淆 Lua），有变种藏在 `.claude/hooks/config/`；持久化用伪装成 CCleaner 与 Office ClickToRun 的计划任务；部分账号疑似被盗号后只改了 README。建议：安装 AI 工具前核查仓库所有者与提交历史，不运行 README 里的 ZIP 安装器。
- X 原帖：https://x.com/fr0gger_/status/2118075954740547684 、https://x.com/fr0gger_/status/2118075962327969875 、https://x.com/fr0gger_/status/2118075973996581274
- IoC 列表：https://gist.github.com/fr0gger/3d0288bf0fee3b8df7b618e7c10334d7
- 样本：https://www.virustotal.com/gui/file/2a7afb187157a4052e5b9797d1d1c7ee807b2edeffef076a08b20b12e3dcf317/detection

### 5. 欧洲冷柜攻击扩大：法国血液中心 EFS 冷柜被篡改
继超市冷柜后，法国 EFS 经制冷承包商 Coolworld 的第三方组件被攻击，冷柜设置被篡改，血液已转移，据报未受影响；NoName057、Z-Pentest 声称负责（未核实）；Sekoia 蜜罐捕获到攻击。建议：联网制冷／楼宇控制设备不暴露公网，改默认口令。
- X 原帖：https://x.com/KimZetter/status/2117992461347782999 、https://x.com/evilsocket/status/2117920282673652118 、https://x.com/felixaime/status/2117601953693773946
- 文章：https://www.politico.eu/article/fridge-hacks-hit-french-blood-banks/

### 6. 其他事件（简列）
- MSP 相关攻击者以受信任 Azure 应用身份登录 Entra ID 与 Azure DevOps，绕过 MFA，从 Key Vault 取密钥后横向多个客户租户（11-01 起，单一来源 IP 见 IoC）：https://x.com/DFIR_Radar/status/2118101747273183543
- PolinRider 回归：被劫持的 npm 正式包用以太坊交易做 C2 死信箱（OX Security）：https://x.com/MosheTov/status/2118086706167689435 、https://www.ox.security/blog/polinrider-returns-hijacked-npm-packages-use-ethereum-blockchain-to-conceal-malware-infrastructure/
- 「Operation CloudFire」：Google Calendar 邀请钓鱼劫持会话、绕过 MFA（Material Security）：https://x.com/Dinosn/status/2118000396958630318 、https://www.bleepingcomputer.com/news/security/google-calendar-phishing-campaign-hijacks-sessions-bypasses-mfa/
- NIKKE PC 启动器 CDN 脚本被篡改，投放远控与窃密木马（最早 10-23 运行）：https://x.com/Dinosn/status/2117976929282207922 、https://cyberinsider.com/nikke-pc-launcher-malware-remote-access-tool/
- Beacon CRM 泄露（AWS 密钥暴露在前端构建产物中）影响英国 1500+ 慈善机构：https://x.com/Dinosn/status/2117967046395011285 、https://blog.bushidotoken.net/2026/11/uk-cybercrime-journal-beacon-crm-breach.html
- ZRON 泄露第 3 篇（Natto Thoughts）：https://x.com/Dinosn/status/2118000278951931928 、https://www.nattothoughts.com/p/the-zron-leak-part-3-what-does-it
- 勒索／泄露声明（未经核实，仅记录）：WhiteArmor 声称 Unilever、Brain Cipher 声称加拿大 FBC：https://x.com/DailyDarkWeb/status/2118090784729952470 、https://x.com/DailyDarkWeb/status/2118104528063250435

## SecureFlow 信息流精选（X 上未出现的高信号条目，按 community／blog／BugBounty 分组）

### community
本日无显著更新（7 个源近 48 小时内无未报过的新技术帖；唯一一条奇安信攻防社区「Mybatis 常见分页插件 Order by 注入演进史」在 11-03 晚报已列）。

### blog（ZDI-vulnerabilities）
- ZDI-26-870／871／872／873／874：Ashlar-Vellum Cobalt（XE／LI／AR 文件解析）UAF、栈溢出、堆溢出 RCE，均为 **0Day（厂商未修）**，只打开可信来源的 CAD 文件：https://www.zerodayinitiative.com/advisories/ZDI-26-870/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-871/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-872/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-873/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-874/
- ZDI-26-869：MailEnable Save 目录穿越任意文件创建：https://www.zerodayinitiative.com/advisories/ZDI-26-869/

### BugBounty（HackerOne 新公开报告，集中在 MariaDB 客户端连接器）
- Connector/C：TLS auth-switch 绕过导致主机名校验失败时泄露明文密码：https://hackerone.com/reports/3896617
- Connector/C：GSSAPI SPN 未终止导致越界读：https://hackerone.com/reports/3896684
- Connector/ODBC：10 个目录函数中 9 个栈溢出：https://hackerone.com/reports/3891319
- Connector/ODBC：`SQLGetDescRec` 句柄混淆导致堆越界写：https://hackerone.com/reports/3891337
- Connector/ODBC：定位 DELETE／UPDATE 中注入未加引号的列名：https://hackerone.com/reports/3891779
- Connector/ODBC：`SqlwcsOctetLen` 越界读并把客户端内存发给服务器：https://hackerone.com/reports/3920633 ；`ArrayOffset` 异常后未重置导致越界读：https://hackerone.com/reports/3920647
- Connector/C++：字符串转义器重复转义导致 SQL 注入：https://hackerone.com/reports/3890289 ；忽略 allowMultiQueries 注入 savepoint 名：https://hackerone.com/reports/3890329 ；会话跟踪包触发 `std::stoi` 使客户端崩溃：https://hackerone.com/reports/3890352
- r2dbc-mariadb：无在途命令时接受服务器消息导致连接错位、把一个用户的结果返回给另一个用户：https://hackerone.com/reports/3920629

## 地址／IoC 汇总

以下均从原文原样抄录（已去武装的保留原写法），仅供检测与封禁。

**APT29 Poisoned Source（Sekoia）**
- 域名：america250[.]holiday、theowo[.]club、static[.]flux-telemetry[.]com、ads-it-assets[.]com、cdn.adv-static[.]com、wpvortex-mod[.]com、assets-int[.]com、clouds-stacks[.]com、ad.starx-net[.]com、ad-track[.]live（THN）；被篡改的合法服务：a.plerdy[.]com
- IP：109.104.106[.]107、192.121.46[.]25、188.190.17[.]232
- SHA256：bee3e014e3df87ddce0250b0985b87f6868a427a7b650a74b7ffedb9d57f3088、35c0cd19a7334b544c193e392bcd9a8f1d1f43cf6b61be5bf1d9e35537aff2ef、621112712ec515e8791129c62feda8fff6654a0116882401609503cacc08054a、69b6cb327a4d5da99399718f6a66f84de69f89425b0a31f2dcee0682f811596f、ae3241d96cc2d99538c7aff60f382cc8dac13859bcbea3ee84992d24d22a8108、41e6fd33a30d36dabff9ea408d9766a6583edcc107968f6dc1499f2586381967、183d62d682aea8018491c8559544e8d6a9ab0e1abd05ecbb6c97daa4f438d2b8、387a7fb768db1350a9788d9704e7a72abe07152734e0ff026af72b417e36268c
- 来源：https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits

**Ivanti Connect Secure / UTA0576（etugen、@buffaloverflow）**
- 原公开 IoC：108.165.147[.]64
- 攻击代理轮换：70.34.215[.]12、139.84.235[.]230、108.165.147[.]64、208.85.17[.]99；操作者主机 185.130.227[.]232，出口 62.212.70[.]235
- 其他利用同一 CVE 的主机（未归因 UTA0576）：64.94.84[.]170、38.60.227[.]210
- SHA256：7aa9f64e71d7d6dde8a6c0db200dc73a7064ac4adf65bb0f9affd9236351ba0c（利用框架）、afc3f9b853243c88bfb5678fd86c4a2985fceffa8554a119fabb793eea2a8bd7（操作者记忆文件）、269a9b9539fa95a0fee5eb8ac5baa38dd350cae0611bd8e535dd8099a9548ffb、25b95f47359c327e3a5ae5ac5cd147f8d9afd98092faf136822ee287e25e3dc8（设备侧载荷）、17277527c95289a7ce8d9f69b07829edfd2e099bd664d79e54d3e9cad2d8307b（CVE-2026-111357 提权样本，VT）
- 来源：https://etugen.io/blog/ivanti-zero-day-operation/ 、https://www.virustotal.com/gui/file/17277527c95289a7ce8d9f69b07829edfd2e099bd664d79e54d3e9cad2d8307b

**伪装 AI agent 仓库 → SmartLoader／StealC（SecurityBreak）**
- SHA256：53039bdeb3e155236dce324281f59846c2da7518a54859c409286aaff86d61a2、bd2a6bff153d95ab3d94d7db4525c49c31f5c6f32ddbf8e7c466732b0a6eb071、4f5c5ad522d8dba60e89c443e07d65c3ce373ef1a617d220d3b69a185c11dae2、2a7afb187157a4052e5b9797d1d1c7ee807b2edeffef076a08b20b12e3dcf317、7ad4b911d05a12f91ab27ba3baa351a56653ca099dda7ad87ee2b94f8cd018c9、04d3c82782927330d56827ff551697666dbab4b3abf5b86bde492efdd142bc58、ce1e33483d353200a266b3bc383ccf500e5a760c6dcd8218747260f5bbe39509、8cede35b80b1deaf732c2b178d908f91b3e7a0c114d06dfae9075b8a9bf78b8f、f3e34c9e36f3be065d80d456281d31dd1cc85eb4980db7fa8c1b0eb6f29c25d8、ad9da27f72bb7abbfcba92f9302d3467f5487814bb34bbf4b1573abcb56e4efc
- Polygon 合约死信箱：0x1823A9a0Ec8e0C25dD957D0841e3D41a4474bAdc（经合法服务 polygon[.]drpc[.]org 读取，勿整域封禁）
- StealC 外传 IP：213.176.72[.]200；另见 217.119.129[.]110
- 来源：https://gist.github.com/fr0gger/3d0288bf0fee3b8df7b618e7c10334d7

**SlippyNunchucks / DarkVigil（ESET，经 THN）**
- 暂存服务器：47.239.250[.]102（sogou-cdn[.]com）、47.237.122[.]175
- 来源：https://thehackernews.com/2026/11/china-aligned-hackers-hijack-sogou.html

**PolinRider npm（OX Security）**
- C2 IP：103[.]179[.]143[.]219、166[.]88[.]134[.]75、23[.]27[.]13[.]72、95[.]135[.]181[.]151
- 攻击者 ETH 地址：0x1eef0849eda15d87f64e51c73c8442cf3c8bcef3
- 来源：https://www.ox.security/blog/polinrider-returns-hijacked-npm-packages-use-ethereum-blockchain-to-conceal-malware-infrastructure/

**MSP Azure 应用身份滥用（@DFIR_Radar）**
- 来源 IP：199.19.77[.]84（波兰）
- 来源：https://x.com/DFIR_Radar/status/2118101747273183543

其余条目（APT、Rails、Airbyte、Xen、Firecracker、Android 等）：未见公开 IoC。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）：https://x.com/i/lists/1239330068461244424 （本次读取三页共 287 帖，覆盖约 26.5 小时）
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
  - https://x.com/search?q=(CVE%20OR%20PoC%20OR%20exploit%20OR%200day)%20-is%3Aretweet%20lang%3Aen&f=live （25 条只覆盖约 4 分钟，大量非安全内容）
  - https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20BOF%20OR%20redteam)%20-is%3Aretweet&f=live （10 条，覆盖 01:33–22:14 UTC）
  - https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)%20-is%3Aretweet&f=live （24 条，覆盖约 2.6 小时）
  - 补搜：https://x.com/search?q=(CVE%20OR%20exploit%20OR%200day%20OR%20%22in%20the%20wild%22%20OR%20%22actively%20exploited%22%20OR%20ransomware)&f=top 、https://x.com/search?q=(%22CVE-2026%22%20OR%20%22zero-day%22%20OR%20%220-day%22%20OR%20PoC%20OR%20KEV)%20lang%3Aen&f=top
- X List：https://x.com/i/lists/1239330068461244424
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200
  - 覆盖近 48 小时（2026-11-03 07:05 至 11-05 07:05，北京时间）。SecureFlow 重新生成了条目 id，本次改按原文链接与往期晚报去重：30 条链接未出现过，再排除 11-03 已整组报过的 Quest Foglight ZDI 批次后剩 17 条（BugBounty 11 条、ZDI 6 条、community 0 条）。
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community
  - 7 个源，跳过长期不更新的吾爱破解（最后更新 2024-09），其余 6 个逐源拉取 /api/rss/articles/<id>；近 48 小时内、all 接口之外的新条目 0 条。
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog
  - 12 个源，跳过长期不更新的「微信公众号」源（最后更新 2025-02），其余 11 个逐源拉取；近 7 天（2026-10-29 至 11-05，北京时间）all 接口之外、未报过的条目 0 条。
- 各接口均请求成功（浏览器 UA），无失败。
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （共 1768 条，2026-11-04 20:00 UTC 发布；本窗口新增 CVE-2024-27834）
- 链接核验：非 X 链接 83 条中 80 条 200，3 条 403（cisa.gov ×2、medium.com ×1，加 Referer 重试后仍是 403）。

---
本机保存路径：~/Desktop/X安全情报晚报/2026-11-04-x-security-digest.md（kenny1337s-MacBook-Pro.local），box 副本：/home/box/workspace/security-watch/reports/2026-11-04-x-security-digest.md
