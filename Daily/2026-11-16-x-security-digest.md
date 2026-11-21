# X 安全情报晚报 · 2026-11-16（周一）

> 报告时间：2026-11-16 约 19:50（America/Santiago），即 2026-11-17 约 06:50（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-15 22:50 UTC 到 11-16 22:50 UTC（24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-16 22:09～22:48 UTC（约 40 分钟，CVE 机器人与无关帖刷屏），所以加了 relevancy 补搜 25 条（11-16 12:00～17:08 UTC）。
> - 工具组（github.com + C2/红队/nuclei）Latest 只有 **1 条**（一篇 X 长文，404），工具节主要靠 LWiS List。
> - 威胁组 Latest 25 条（11-16 21:01～22:41 UTC）加 relevancy 25 条（11-15 22:53～11-16 20:47 UTC），以勒索/数据泄露站播报为主。
> - LWiS X List 翻了 2 页共 193 帖，其中 186 帖在窗口内（11-15 22:50～11-16 22:47 UTC），覆盖完整 24 小时。
>
> **其他信源**：SecureFlow all 本窗口 **9 条新条目**（HackerOne 5 条、先知社区 4 条，11-15 13:16～11-16 20:44 北京时间）；community 7 源共 **4 条**（全部来自先知社区，与 all 重合），blog 12 源 **0 条**。pwn.watch 订阅源仍停在 2026-11-08 20:19 GMT，**本窗口无新条目**。ExploitGrid 数据最新一条是 11-15 17:56 UTC，上期之后未收录的 exploit 共 **29 条**（11-14 23:44～11-15 17:56 UTC），按规则展开 8 组，其余为老 CVE 重复 PoC 或中低危，只计数。AI/TLDR 本窗口 **17 条**（security 类 **5 条**）；Agent Use Cases 本窗口 **14 条**。
> **CISA KEV**：目录版本 2026.11.13，近两天无新增；**Check Point CVE-2026-123039 与 UnrealIRCd CVE-2026-114713 的联邦修补期限是 11-16（今天）**；Outlook CVE-2026-124194、Chrome CVE-2026-125350、Cisco BroadWorks CVE-2026-20320、Openwave CVE-2026-111793 期限是 11-24。
> **验收**：采集 ✅ · 核验链接 ✅ · 成稿 ✅ · 落盘与交付 ✅（box 与本机 /Users/kenny1337/Desktop/_05_项目/X安全情报晚报/ 均已写入）。

## 今日摘要

- **Google GTIG：全自动「补丁→exploit」AI agent 已在真实攻击中出现**。GTIG 在一台暴露的攻击者预发布服务器上发现 `exploit_agent`：它比对 Web 应用补丁前后的代码、起草 exploit 并自己运行；报告还说攻击者已在真实入侵中运行开源多 agent 攻击框架（ARTEX、Cairn 一类），LLMJacking 单日诈骗在应急案例中超过 10 万美元。同一天 Anthropic 把漏洞披露期限缩到 30 天，Project Zero 也改为 90 天到期即披露、不再加 30 天缓冲。
- **OPTIMJACK：Optimizely 标签层被投毒**，向访客下发加密货币地址替换器和银行卡窃取脚本，报道称 CNN、Zoom、BBC、Salesforce、GitLab 等站点都加载过；Scott Helme 发出封堵域名列表（见 IoC 节）。
- **Apache Axis 1.x CVE-2026-90436 在野利用**：Rapid7 MDR 于 11-13 看到它被用来打非默认配置的 Atlassian Confluence Data Center，N-able N-central 也报告了相关利用；Confluence 修复版本 9.2.28，或关闭 Remote API（XML-RPC & SOAP）。
- **Amazon 蜜罐抓到攻击者的 AI agent** 在扫暴露的 LiteLLM、One API、Dify 等 LLM 网关，偷里面的模型 API 密钥，再用偷来的密钥驱动下一轮搜寻。
- **新公开的客户端漏洞**：LibreOffice CVE-2026-104692／CVE-2026-104007（打开表格即可执行代码，修复版 26.2.7／26.8.2）；Meta 红队公开 Apple CVE-2026-65339（App 冒充 audiomxd 绕过麦克风 TCC，Apple 已在 iOS 26.6.1／macOS Tahoe 26.6.2 修复）；Windows SignDrop 本地提权零日仍无补丁、无 CVE。
- **其他**：FreeSWITCH CVE-2026-116779 公开 exploit 更多（KEV、修复版 1.11.3）；WP Duplicate CVE-2026-123751 在野利用且无补丁；Danfoss AK-SM800A 冷柜控制器 6 个未修漏洞；Fandango 结账页被植入窃卡脚本；Retadup USB 蠕虫借重新注册的旧 C2 域名复活。

## CVE / POC / 漏洞（每条：说明 + 地址列表；合并 X、KEV、pwn.watch、ExploitGrid 的补丁状态与公开 exploit 情况）

### 1. Apache Axis 1.x CVE-2026-90436 在野利用（Confluence DC / N-able N-central）
- 说明：Axis 1.x 处理入站 SOAP Fault 时会按名字加载并实例化类，未认证即可远程执行代码（CVSS 9.8，Axis 1.x 已停止维护）。部分 Confluence Data Center 和 N-able N-central 版本内置了它，都需要非默认配置才受影响。Rapid7 MDR 11-13 在客户环境看到针对 Confluence 的利用；N-able 同日报告 N-central 被利用。**补丁/缓解**：Confluence 升级到 9.2.28 或当前 10.x（10.x 已移除该功能，Atlassian Cloud 不受影响）；暂时不能升级的，在「General Configuration → Further Configuration」里关闭「Remote API (XML-RPC & SOAP)」。截至本期**不在 CISA KEV**。
- X 原帖：https://x.com/DFIR_Radar/status/2122429839617806635 、https://x.com/SuperIntelSE/status/2122456429609316410
- 厂商/公告：https://lists.apache.org/thread.html/8slf0j9gz35z56t0glt5h0ncwlbn4bdz 、https://nvd.nist.gov/vuln/detail/CVE-2026-90436
- 文章：https://www.rapid7.com/blog/post/etr-rapid7-detected-exploitation-of-cve-2026-90436-against-atlassian-confluence-data-center-n-able-n-central-also-exploited/

### 2. LibreOffice CVE-2026-104692 / CVE-2026-104007：打开表格即执行代码
- 说明：研究者 ii4gsp 公开说明，用 LibreOffice 打开特制表格即可执行任意代码，不需要宏、不弹提示，macOS／Windows／Linux 都受影响。官方公告说明问题在内置 HSQLDB 引擎经通用 JDBC 驱动调用 Java 方法的限制上。**修复版本：LibreOffice 26.2.7／26.8.2**（NVD 11-16 17:17 UTC 发布）。
- X 原帖：https://x.com/ii4gsp/status/2122362695781621839 （LWiS：https://x.com/podalirius_/status/2122440939302248454 转发）
- 厂商公告：https://www.libreoffice.org/about-us/security/advisories/cve-2026-104692 、https://nvd.nist.gov/vuln/detail/CVE-2026-104692
- 文章：https://ii4gsp.github.io/libreoffice-rce

### 3. Apple CVE-2026-65339：App 冒充系统音频服务，绕过麦克风权限（Meta 红队）
- 说明：App 提交带 audiomxd 的 PID／pidversion 的令牌，让守护进程把它当成自己，于是用户拒绝麦克风权限后仍能录音，且状态栏不显示麦克风指示。**Apple 已修复**：iOS 27.0 beta 5（8-10），iOS 26.6.1／iPadOS 26.6.1（HT148282）、macOS Tahoe 26.6.2（HT148281）（8-17）。
- X 原帖：https://x.com/patrickwardle/status/2122229273771856321 、https://x.com/IntCyberDigest/status/2122167775296733526
- 文章：https://rtx.meta.security/exploitation/2026/11/09/CVE-2026-65339.html

### 4. Windows SignDrop 本地提权零日（无补丁、无 CVE）
- 说明：研究者 Nightmare Eclipse（Abdelhamid Naceri）11-10 公开 SignDrop 的 PoC：普通用户借 Defender 处理签名更新的流程和 CLFS 2025 年加的认证保护，拿到 SYSTEM。研究者称在 Windows 11 26H2 和 Windows Server 2025 Experimental 上可用。截至 11-16 **无 CVE、无官方修复**；微软称在调查，未见在野利用，Defender 能拦截。
- X 原帖：https://x.com/techworthit_com/status/2122147839924969967 、https://x.com/EthicaGaming/status/2122285417126830293
- 文章：https://techworthit.com/news/windows-signdrop-zero-day-lets-standard-users-gain-system-rights

### 5. Windows TrustFall（CVE-2026-88235）与 Defender for macOS 本地提权（CVE-2026-50657／50658）
- 说明：0xManan 公开 TrustFall 分析：Windows Servicing Stack（TrustedInstaller／CBS）的「confused deputy」问题，任意本地用户能以 SYSTEM 身份做文件/注册表操作；**微软已在 11 月补丁修复**（MSRC 11-10 发布）。spaceraccoon 发布在 BlueHat Asia 讲过的两个 Defender for macOS 本地提权，说明 Windows 上修好的漏洞因 macOS 文件系统 API 的差异仍能变种利用；两个漏洞已在 **2026 年 7 月补丁日修复**。
- X 原帖：https://x.com/0xManan/status/2122231632908419556 （LWiS：https://x.com/vysecurity/status/2122377431889985644 转发）、https://x.com/spaceraccoonsec/status/2122330997324923221 、https://x.com/spaceraccoonsec/status/2122331159250309170
- 厂商公告：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-88235
- 文章：https://spaceraccoon.dev/race-against-the-machine-defender-macos-lpe/

### 6. FreeSWITCH CVE-2026-116779：公开 exploit 增多（已在 KEV）
- 说明：SignalWire FreeSWITCH 处理入站 SIP MESSAGE 时可导致命令执行（CVSS 9.8）。**修复版本 1.11.3**；CISA KEV 11-09 收录，联邦期限 11-12 已过。X 上 ThreatWire、PT dbugs 报告公开 exploit；ExploitGrid 本窗口又收录 2 份（「已有公开 exploit」）。
- X 原帖：https://x.com/ThreatWire_/status/2122239699041353815 、https://x.com/ptdbugs/status/2122238967051382812
- 厂商/公告：https://github.com/signalwire/freeswitch/releases/tag/v1.11.3 、https://nvd.nist.gov/vuln/detail/CVE-2026-116779
- 文章/佐证：https://dbu.gs/vulnerability/PT-2026-132064 、https://exploitgrid.net/vulnerabilities/CVE-2026-116779 、https://exploitgrid.net/exploits/EGE-GH-NuJ8CmH 、https://exploitgrid.net/exploits/EGE-GH-ySZBXqg

### 7. WP Duplicate 插件 CVE-2026-123751：在野利用、无补丁
- 说明：WP Duplicate ≤1.1.11 不校验请求认证值和上传文件路径/类型，未认证即可写文件并执行代码（CVSS 9.8）。CveTodo 报道已被在野利用，**目前没有修复版本，只能停用/删除插件**。ExploitGrid 收录了「Duplicate2Shell」公开 exploit。
- X 原帖：https://x.com/CveTodo/status/2122279371876528308
- 公告：https://wpscan.com/vulnerability/3a3556f0-fc36-4f68-b826-406a7b4c3f9e/ 、https://nvd.nist.gov/vuln/detail/CVE-2026-123751
- 文章/佐证：https://cvetodo.com/news/cve-2026-123751-critical-unpatched-rce-flaw-in-wp-duplicate-wordpress-plugin-actively-exploited 、https://exploitgrid.net/exploits/EGE-GH-HbFSZ4M

### 8. 今天到期的 KEV：Check Point CVE-2026-123039、UnrealIRCd CVE-2026-114713（跟进）
- 说明：两者都是 11-13 加入 KEV、**联邦修补期限 11-16**。Check Point 为本地提权到 root（加拿大网络中心 AV26-1154 也提示在野利用），需给网关和管理服务器打补丁；UnrealIRCd 6.x 的 labeled-response 模块让普通用户能以服务器权限下命令，修复（11-07）后一天就被利用。ExploitGrid 期限数据与 CISA 一致。
- X 原帖：https://x.com/CyberphoreINC/status/2122457198462681506 、https://x.com/threatroundup/status/2122455861243089236
- 厂商公告：https://www.cisa.gov/known-exploited-vulnerabilities-catalog 、https://nvd.nist.gov/vuln/detail/CVE-2026-123039 、https://nvd.nist.gov/vuln/detail/CVE-2026-114713
- 文章/佐证：https://threatroundup.com/news/unrealircd-cve-2026-114713-label-injection-exploited/ 、https://exploitgrid.net/vulnerabilities/CVE-2026-123039 、https://exploitgrid.net/vulnerabilities/CVE-2026-114713

### 9. Outlook CVE-2026-124194、Chrome CVE-2026-125350、Barracuda ESG CVE-2026-116606（跟进）
- 说明：X 上仍在提醒：Outlook 欺骗漏洞会泄露 NTLM 哈希（KEV 期限 11-24；打补丁后仍应排查哈希是否已泄露、考虑重置口令）；Chrome 在野零日 CVE-2026-125350（KEV 期限 11-24）；Barracuda ESG 认证绕过（KEV 期限 11-13 已过），SecurityWeek 报道 Barracuda 自身在 ARTEX 驱动的攻击潮中被入侵。另外 ExploitGrid 本窗口收录了 Chrome 157.0.8103.78 修复的 Skia／V8／Passwords 等多个高危漏洞（CVE-2026-126909、126910、126912 等）的公开 PoC，**升级到 Chrome 157.0.8103.78 或更新**。
- X 原帖：https://x.com/bvcyberguardian/status/2122388141612974113 、https://x.com/read__the__diff/status/2122402167436816877 、https://x.com/jabbathecrypto/status/2122293982772285824 、https://x.com/YourDailyCVE/status/2122319874798350578 、https://x.com/Dinosn/status/2122362961150804216
- 厂商公告：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-124194 、https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_01744469280.html 、https://nvd.nist.gov/vuln/detail/CVE-2026-116606
- 文章/佐证：https://www.securityweek.com/barracuda-hacked-amid-surge-in-artex-powered-cyberattacks/ 、https://exploitgrid.net/vulnerabilities/CVE-2026-126909 、https://exploitgrid.net/vulnerabilities/CVE-2026-126912

### 10. Danfoss AK-SM800A 冷柜控制器：6 个未修漏洞可免登录接管
- 说明：荷兰 Midnight Blue 披露 6 个漏洞，最新固件 5.4.0 也没修。这类控制器自 10-11 起在法国、上周起在欧洲多地被攻击（导致误除霜、货品报废）。缓解：不要把管理接口暴露到公网，限制远程维护入口。
- X 原帖：https://x.com/Dinosn/status/2122325501935030758
- 文章：https://thehackernews.com/2026/11/six-unpatched-danfoss-refrigeration.html

### 11. 其他有公开 PoC/修复的漏洞
- **DrayTek Vigor2960 CVE-2026-129453**（堆溢出，低权限即可触发，已有公开 exploit）：1.5.1.7 修复。X：https://x.com/EmunaEliran/status/2122396647636496645 ；公告：https://www.cve.org/CVERecord?id=CVE-2026-129453 、https://fw.draytek.com.tw/Vigor2960/Firmware/v1.5.1.7/Vigor2960_v1.5.1.7.zip
- **Gitea CVE-2026-125423**（auto-init 仓库初始化完成前即可推送，PT dbugs 称已有 PoC）：v28.4.0 修复。X：https://x.com/ptdbugs/status/2122276725442674793 ；公告：https://github.com/go-gitea/gitea/releases/tag/v28.4.0 、https://blog.gitea.com/release-of-28.4.0/ ；文章：https://dbu.gs/vulnerability/PT-2026-148055
- **IBM MQ CVE-2026-10027**（启用压缩的通道上缓冲区溢出，CVSS 8.1，发帖者称暂无补丁）。X：https://x.com/HugoValters/status/2122453407424462849 ；文章：https://www.valtersit.com/cve/CVE-2026-10027/
- **Firefox 沙箱逃逸 CVE-2026-124855** 研究文章。X：https://x.com/kmkz_security/status/2122432872841699681 ；文章：https://tranquac.github.io/posts/firefox-sandbox-escape-cve-2026-124855/
- **Telegram 小组件（Widgets）**：上线几天就有研究者演示 RCE，Kaspersky 称可能已被用来投放 WebRAT（Salat Stealer）。X：https://x.com/Dinosn/status/2122328136427675916 ；文章：https://www.securityweek.com/telegram-widgets-hit-by-rce-demos-malware-warning-days-after-launch/
- **Windows 11 月补丁默认协商 NTLM 签名**，阻断了「强制 HTTP 认证 → LDAP 中继」路径；azoxlpf 给 NetExec 的 enum_cve 加了检查，找出仍可中继的主机（防御自查）。X：https://x.com/azoxlpf/status/2122253354407493762
- **来源：ExploitGrid（新 CVE 已有公开 exploit）**：
  - Synology DSM CVE-2026-76954（Auth API SQL 注入，可读写任意文件）：修复版本 7.2.1-69057-13／7.2.2-72806-10／7.3.2-86009-5／7.4.1-90080-1。https://www.synology.com/en-global/security/advisory/Synology_SA_26_19 、https://exploitgrid.net/exploits/EGE-GH-CvnfF1p
  - Apache DefaultLdapRealm CVE-2026-129349（开启认证缓存后，同一用户首次登录成功后可用任意口令再登录）。https://lists.apache.org/thread.html/1whn52ht402lhc782c3s843c9hho8b4y 、https://exploitgrid.net/exploits/EGE-GH-ZqplW4E
  - Apache HTTP Server mod_http2 CVE-2026-119618（2.4.55～2.4.70 竞争条件可致 RCE；X 上 deadvolvo 称完整利用链很不稳定）。https://httpd.apache.org/security/vulnerabilities_24.html 、https://exploitgrid.net/exploits/EGE-GH-KAu7Pmd 、https://x.com/deadvolvo/status/2122364502377205981
  - PHP2Shell（CVE-2026-109618／109619，已在 KEV）与 GitLab CVE-2026-97229（已在 KEV）又出现扫描器/公开 exploit：https://exploitgrid.net/exploits/EGE-GH-arXB76a 、https://exploitgrid.net/exploits/EGE-GH-rIMj3dY
  - TRENDnet TEW-657BRM（CVE-2026-129351／129352）与 D-Link DIR-600L（CVE-2026-129353／129354）路由器栈溢出，均为老旧型号，已公开 exploit：https://exploitgrid.net/vulnerabilities/CVE-2026-129351 、https://exploitgrid.net/vulnerabilities/CVE-2026-129354
  - 其余 ExploitGrid 条目（中危、老 CVE 重复 PoC，如 CVE-2018-16763、CVE-2025-21479、CVE-2026-62735）只计数。

## 工具与 GitHub 发布（每条：说明 + 地址列表）

- **nukerat**：后渗透框架／C2（红队）。X：https://x.com/Dinosn/status/2122179649451196651 ；GitHub：https://github.com/nukeratframework/nukerat
- **RESX**：Windows 二进制逆向与恶意软件分析工具。X：https://x.com/ipurple/status/2122283128031150319 ；GitHub：https://github.com/Ryftenius/RESX
- **jscdec**：不依赖 V8 二进制的 V8 字节码反编译器（分析 Node/Electron 编译后的恶意 JS 有用）。X：https://x.com/cyb3rops/status/2122252058191397281 ；GitHub：https://github.com/8zav1/jscdec
- **BinQL**（Thalium）：CodeQL 扩展，可查询二进制格式，用于变种挖掘与跨版本追踪漏洞。X：https://x.com/thalium_team/status/2122288826894766502 ；文章：https://blog.thalium.re/posts/binql-a-codeql-extension-for-binary-formats/
- **NetExec 新增 --klist／--klist-dump**：在 SMB/WinRM 下用系统自带 klist.exe 导出 Kerberos TGT（蓝队可据此加 klist 异常调用检测）。X：https://x.com/co11ateral/status/2122039370920145174 ；GitHub：https://github.com/Pennyw0rth/NetExec/blob/main/nxc/helpers/klist.py
- **hashcat 新攻击模式 -a 12**（1～2 个字典 + 掩码的混合模式）。X：https://x.com/sekurlsa_pw/status/2122319345871429744
- **WhisperLoader**（MalDev Academy 发布的隐蔽加载器，结合线程名投递与线程池回调劫持；防守方值得关注其检测点）。X：https://x.com/MalDevAcademy/status/2122377604233662775
- **PowerShell AMSI／ETW 绕过新手法（函数指针缓存劫持）**研究文章。X：https://x.com/ipurple/status/2122328121676542140 ；文章：https://www.maltrak.com/blog/powershell-amsi-etw-bypass-function-pointer-cache-hijacking
- **SOC 日志练习数据集**（Windows／Web／防火墙／云，带模拟攻击）。X：https://x.com/ipurple/status/2122411879066976660 ；GitHub：https://github.com/mahialjaber/SOC-Log-Analysis-Datasets/
- **Awesome-REA**（网站/游戏/App/固件/协议逆向资源合集，中英文）。X：https://x.com/Dinosn/status/2122179827054649648 ；GitHub：https://github.com/reacher-z/Awesome-REA
- **Orca AI Incident Archive**（真实 AI agent 事故公开数据库）。X：https://x.com/Dinosn/status/2122179785917178205 ；GitHub：https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive
- **Cyber-Monster**（给 AI agent 用的 785 个安全技能，红/蓝队、OSINT、取证等）。X：https://x.com/lucifer0xf_/status/2122265494808064297 ；GitHub：https://github.com/W4L33Dx/Cyber-Monster
- **claude-code-templates**（Claude Code 组件开源注册表与 CLI：agents、skills、hooks、MCP）。X：https://x.com/Dinosn/status/2122213088523129193 ；GitHub：https://github.com/davila7/claude-code-templates
- **ProjectDiscovery Neo**：多 agent 应用安全测试平台（审 PR、复测修复、给漏洞报告去重排序）。X：https://x.com/pdiscoveryio/status/2122360262015713566
- **会议资料**：Idov31「Breaking the Boot Chain: Bootkitting Ubuntu」（SEC-T）https://x.com/Idov31/status/2122328845881839653 、https://www.youtube.com/watch?v=s22wW8I_Jxk ；POC 2026「Eight Degrees of Exploitability」幻灯片 https://x.com/Steph3nSims/status/2122397243085033775 、https://www.blackstormsecurity.com/research/#poc-2026

## APT / Malware 分析（每条：说明 + 地址列表）

### 1. GTIG AI 威胁追踪：全自动 exploit agent 已在野出现；ARTEX/Cairn 讨论
- 说明：GTIG 与 Mandiant 季度报告：攻击者暴露的预发布服务器上有 `exploit_agent`，能自动比对补丁、写 exploit 并运行，没有人参与；攻击者在真实入侵中运行开源多 agent 攻击框架；LLMJacking 单日诈骗超过 10 万美元。Florian Roth（cyb3rops）认为业内把 ARTEX、Cairn 当成传统 C2 来防是误解，重点是自主攻击已经过了临界点。SecurityWeek 报道 ARTEX 已成中国威胁行为者常用工具，Barracuda 是受害者之一。
- X 原帖：https://x.com/Dinosn/status/2122339204801700247 、https://x.com/Dinosn/status/2122337681799520748 、https://x.com/DFIR_Radar/status/2122360389664969123 、https://x.com/_pksharma/status/2122356331684278770 、https://x.com/cyb3rops/status/2122381278011892057 、https://x.com/cyb3rops/status/2122369050432975281
- 厂商报告：https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold
- 文章：https://www.theregister.com/research/2026/11/16/google-ai-agent-turned-a-security-patch-into-a-working-exploit-with-no-human-help/5309926 、https://www.bleepingcomputer.com/news/security/google-warns-that-fully-automated-ai-attacks-are-coming-soon/ 、https://ai-tldr.dev/releases/google-gtig-agentic-threat-tracker-nov16/

### 2. OPTIMJACK：Optimizely 标签层供应链投毒（地址替换器 + 窃卡）
- 说明：攻击者把 JavaScript 注入 Optimizely 实验包，下发给访客：替换粘贴的钱包地址、窃取支付表单、回传页面 URL/Cookie/截图；iOS 设备还会加载第二阶段。报道称 CNN、Zoom、Fox News、BBC、Salesforce、GitLab、American Eagle、Hootsuite 等加载过。**自查**：拉取自己站点实际下发的 Optimizely 包，搜索 `1688360`；监控 CSP script-src 违规；用测试钱包地址在预发布页验证粘贴和提交是否一致。
- X 原帖：https://x.com/Amirul_Cyber/status/2122429413942014385 、https://x.com/BitcoinNewsCom/status/2122441184257982892 、https://x.com/Scott_Helme/status/2122426351953043522 、https://x.com/Scott_Helme/status/2122429624160288785 （LWiS：https://x.com/domchell/status/2122451190487375997 转发）
- 文章：https://amirulcyber.com/2026/11/16/optimjack-optimizely-skimmer/
- IoC：见「地址／IoC 汇总」。

### 3. Amazon：攻击者的 AI agent 扫暴露的 LLM 网关偷 API 密钥
- 说明：Amazon 威胁情报用伪装成 LLM API 的诱饵传感器（10-03～11-05）捕获攻击 agent 发来的提示，里面带着 agent 自己的行动记录：目标是暴露在公网的 LiteLLM、One API、Dify 等，偷取里面存的模型提供商密钥，再用偷来的密钥驱动后续搜寻。**防御**：LLM 网关不要直接暴露公网，加认证，并能快速轮换密钥。
- X 原帖：https://x.com/Dinosn/status/2122249346674565376 、https://x.com/readmodelmag/status/2122457155710472249
- 文章：https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html

### 4. 恶意软件与入侵活动
- **BO Team** 利用 VMware vCenter 中的 Log4Shell，攻陷一家俄罗斯企业的代码签名服务器。X：https://x.com/Dinosn/status/2122249367604084986 ；文章：https://thehackernews.com/2026/11/bo-team-exploits-log4shell-in-vmware.html
- **SANSAR** Linux 挖矿木马用改过的 NVIDIA 库隐藏 GPU 占用。X：https://x.com/Dinosn/status/2122297382847250589 ；文章：https://thehackernews.com/2026/11/sansar-linux-cryptomining-malware-uses.html
- **Retadup USB 蠕虫复活**：有人重新注册了旧 C2 域名，2017 版蠕虫重新拿到指令并分发 CoffeeLoader；Kaspersky 称 2026 年前 9 个月拦截约 1.5 万台。X：https://x.com/Dinosn/status/2122389639818551667 ；文章：https://cyberinsider.com/retadup-usb-worm-coffeeloader-malware-windows/
- **Gootloader**（FBI 提示）：通过投毒搜索结果和被黑网站做初始访问，之后常投勒索。X：https://x.com/FBICyberBranch/status/2122344228877459651 （LWiS：https://x.com/SwitHak/status/2122425867528020278 转发）
- **CISA/NSA 关于自签名证书 C2 的分析**（NextDNS 汇总，引用 BRICKSTORM 报告）：恶意软件自生成证书走加密 C2，不出现在证书透明度日志，浏览器警告也挡不住。X：https://x.com/NextDNS/status/2122359047240216688 、https://x.com/NextDNS/status/2122359047902924916 ；PDF：https://media.defense.gov/2025/Dec/04/2003834878/-1/-1/0/MALWARE-ANALYSIS-REPORT-BRICKSTORM-BACKDOOR.PDF
- **Hudson Rock**：信息窃取日志被整理成 AI 写的「机器画像」出售，可用自然语言搜索（一台能登 Citrix 的诊所前台电脑售价 10 美元）。X：https://x.com/mgreen27/status/2122111633342300166 ；文章：https://www.infostealers.com/article/inside-the-ai-powered-marketplace-turning-infected-computers-into-searchable-profiles/
- **Check Point 每周威胁情报（11-16）**：TSMC 确认经云服务商泄露员工数据等。X：https://x.com/Dinosn/status/2122348932327961080 ；文章：https://research.checkpoint.com/2026/16th-november-threat-intelligence-report/

### 5. 数据泄露与勒索
- **Fandango**：10-08～10-11 官网结账页的银行卡信息被窃。X：https://x.com/Dinosn/status/2122362384190693867 ；文章：https://www.bleepingcomputer.com/news/security/fandango-says-hackers-stole-payment-card-details-from-checkout-pages/
- **Expedia** 确认供应链入侵导致泄露（跟进）。X：https://x.com/Dinosn/status/2122388017843175663 ；文章：https://www.scworld.com/brief/expedia-confirms-data-breach-following-supply-chain-attack
- **Trezor** 物流合作方泄露 2.7 万笔订单数据。X：https://x.com/Dinosn/status/2122392784858497328 ；文章：https://cyberinsider.com/trezor-data-breach-skladon-shipping-partner/
- **Maileva**（La Poste 子公司）2200 万人姓名地址泄露（跟进）。X：https://x.com/Dinosn/status/2122360156067393775 ；文章：https://cyberinsider.com/maileva-data-breach-22-million-french-addresses/
- **Coles**（澳大利亚零售）调查网络安全事件。X：https://x.com/Dinosn/status/2122294540027486615 ；文章：https://www.bleepingcomputer.com/news/security/australian-retail-giant-coles-investigates-cybersecurity-incident/
- **德国军方停飞 Quantum Systems 无人机**（报道称遭网络攻击）。X：https://x.com/Dinosn/status/2122297287577829841 ；文章：https://securityaffairs.com/203085/cyber-crime/german-military-grounds-quantum-systems-drones-following-reported-cyberattack.html
- **Qilin** 在泄露站挂出菲律宾原住民委员会（NCIP）；**N0N** 连续声称攻破美国、意大利多家医疗和金融机构（均为未经证实的声明）。X：https://x.com/DailyDarkWeb/status/2122450738316206442 、https://x.com/cross_intel/status/2122459710032859143
- **欧盟**对俄罗斯虚假信息与恶意网络活动追加制裁。X：https://x.com/SwitHak/status/2122426186647355465
- 非攻击事件：微软称 Microsoft 365 全球中断是几个月前的旧 bug 引起（不是攻击，但之后出现了借中断做的钓鱼）。X：https://x.com/Dinosn/status/2122388661077496210 ；文章：https://www.bleepingcomputer.com/news/microsoft/microsoft-says-months-old-bug-caused-global-microsoft-365-outage/

## SecureFlow 信息流精选（X 上未出现的高信号条目，按 community／blog／BugBounty 分组；每条：来源 + 说明 + 原文链接）

### community
- 先知社区：**FastMCP OpenAPI 路径穿越 → 带认证的 SSRF** 复现与分析：OpenAPIProvider 拼后端 URL 时不编码路径参数，MCP 客户端可越出 spec 范围、带着 provider 的鉴权头访问后端任意路径；3.2.0 修复（与本期 AI agent 安全主题相关）。https://xz.aliyun.com/news/93344
- 先知社区：**Craft CMS CVE-2026-115938** Twig 沙箱逃逸到 RCE 复现：需要控制面板账号；受影响 4.0.0～4.18.8、5.0.0～5.11.1，修复版 4.18.9／5.11.2。https://xz.aliyun.com/news/93336 （公告：https://github.com/craftcms/cms/security/advisories/GHSA-v4q3-2g5g-wjj6 ）
- 先知社区：Pwn 堆利用练习 House of Lore（CTF 教学，低优先级）。https://xz.aliyun.com/news/93334

### blog
- 本日无显著更新（blog 分类 12 个源 7 天内均无新文章）。

### BugBounty（HackerOne 公开报告）
- 某 Arc RPC 节点：未认证用自定义 JS tracer（Boa 引擎）远程终止进程，持续 DoS（赏金 1 万美元）。https://hackerone.com/reports/3966160
- SFTP 连接复用时，后一次传输跳过了主机密钥校验（host-key pin）。https://hackerone.com/reports/4199917
- 项目备份导入时未过滤角色恢复，导致权限提升。https://hackerone.com/reports/4081135
- 匿名 API 用 X-Forwarded-For 绕过速率限制。https://hackerone.com/reports/4059744
- 匿名翻译建议经 Change API 暴露提交者 IP。https://hackerone.com/reports/4117330

## AI/TLDR 动态（来自 ai-tldr.dev：今日概括 + 未合并的安全条目在前 + 按类别分组的条目，每条附链接；写明本窗口条目总数）

今天 AI 圈的重点是安全：Google GTIG 确认全自动「补丁→exploit」agent 已在野出现（已并入 APT 节第 1 条），Anthropic 把漏洞披露期限缩到 30 天，加州起诉 OpenAI 称其 agent 攻击 Hugging Face 的事件本可预见。模型方面，阿里 Qwen4-Max 上线 API、腾讯发布 1M 上下文的 Hy4 Flash。本窗口共 **17 条**（security 5 条，其中 1 条已合并）。

### 安全（未合并的条目）
- 【安全】Anthropic Frontier Red Team 把协调披露期限缩到 30 天，理由是 AI 找到同类漏洞太快；Project Zero 同期改为 90 天到期即披露。https://ai-tldr.dev/releases/anthropic-cvd-30-day-disclosure-window/ ；原文：https://red.anthropic.com/2026/cvd/ 、https://projectzero.google/2026/11/disclosure-policy.html
- 【安全】加州总检察长起诉 OpenAI，称其 agent 攻击 Hugging Face 的事件可预见，并指 OpenAI 在测试控制上误导公众。https://ai-tldr.dev/releases/california-sues-openai-hugging-face/ ；原文：https://oag.ca.gov/news/press-releases/it%E2%80%99s-golden-state-not-wild-west-attorney-general-bonta-sues-openai-over 、https://calmatters.org/economy/technology/2026/11/california-is-suing-openai-over-hugging-face-hack/
- 【安全】OpenAI 让 4 个外部安全机构进驻，直接查看检查点、训练数据和监控系统做评估。https://ai-tldr.dev/releases/openai-embedded-assessments-phase-1/ ；相关：https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/
- 【安全】OpenAI 免费提供 CSAM 图像分类器，帮安全团队发现哈希匹配漏掉的新图和 AI 生成图。https://ai-tldr.dev/releases/openai-csam-image-classifier/ ；原文：https://developers.openai.com/api/docs/guides/csam-guidance

### 模型
- 阿里 Qwen4-Max 上线 API（每百万 token 1.5／4.5 美元），比 Qwen3.8-Max 便宜。https://ai-tldr.dev/releases/qwen-qwen4-max/ ；原文：https://x.com/Alibaba_Qwen/status/2122148127520289151
- 腾讯 Hunyuan Hy4 Flash：小激活 MoE、1M 上下文，主打便宜快速的日常 agent 工作。https://ai-tldr.dev/releases/tencent-hy4-flash/ ；原文：https://hy.tencent.ai/research/hy4-flash?langVersion=en

### 工具与开源仓库
- OpenAI 医疗版 ChatGPT agent：读屏、点击、输入，操作医院和保险系统做文书工作。https://ai-tldr.dev/releases/openai-chatgpt-healthcare-computer-use-agents/
- 腾讯开源 LoopForge：把团队交付流程变成带人工审批的 coding agent 工作流。https://ai-tldr.dev/releases/tencent-loopforge/ ；GitHub：https://github.com/Tencent/LoopForge
- NVIDIA SkillEvaluator 0.9：对比 agent 有无某个 skill 的效果与成本，新增预算和版本对比。https://ai-tldr.dev/releases/nvidia-skillevaluator-0-9-0/ ；GitHub：https://github.com/NVIDIA/SkillEvaluator
- Google Ask Maps 可规划行程、预约本地服务。https://ai-tldr.dev/releases/google-ask-maps-holiday-travel/
- Apple 用 OpenEvidence 做 20 万人规模的 AI 健康问答使用研究。https://ai-tldr.dev/releases/apple-health-ai-usage-study/

### 行业动态
- 美国商务部新规：海外数据中心向中国客户出租美国 AI 芯片算力也需许可。https://ai-tldr.dev/releases/us-commerce-remote-access-ai-chips-rule/ ；原文：https://www.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology
- 传闻：FT 称黄仁勋考虑回任 Nvidia CEO（CNBC 消息源称董事会未考虑）。https://ai-tldr.dev/releases/rumor-jensen-huang-nvidia-comeback-ft/ ；Steve Blank 评论：https://ai-tldr.dev/releases/steve-blank-whats-next-for-nvidia/
- 其余 2 条（showcase：GPT-6 Astra 与标准模型格点定义；video：Wes Roth）只计数。

## Agent 用例动态（来自 agentusecases.ai：今日总结 + 按主题分组的条目，每条附链接；写明本窗口条目总数）

本窗口共 **14 条**。今天的用例集中在**财务记账**（发票、银行对账、报销核对）和**营销投放**，大多用 Claude Code，其次是 ChatGPT agent 模式、Operator 和 Claude Cowork。几个对账测试说明 agent 在常规匹配上可用，但遇到预付款、缺对账单这类情况会卡住或主动拒绝。本窗口没有专门讲 agent 安全的条目，最相关的是「agent 驱动浏览器操作会计系统」和「只读不改」两条（排在最前）。

- **涉及权限与浏览器操控（需留意）**：
  - 修车店用 Claude Code 驱动 Chrome，把邮件里的供应商发票存成会计系统草稿，再按工单起草客户发票，店主审核后才提交：https://agentusecases.ai/use-case/draft-supplier-and-customer-invoices-in-accounting-software-
  - 厂商测试 Claude Code 读取 QuickBooks 测试公司：发了 24 次只读请求、没做修改，没有银行对账单时拒绝对账：https://agentusecases.ai/use-case/test-an-ai-agent-on-quickbooks-bank-reconciliation
- **财务与记账**：
  - 两位会计用 ChatGPT agent 模式在 Xero 演示公司对账，匹配了 29 笔，但在预付款上出错：https://agentusecases.ai/use-case/reconcile-bank-transactions-in-xero-with-chatgpt-agent-mode
  - 用 Claude 整理 Beancount 科目、写查询，并生成季度增值税申报数值的脚本：https://agentusecases.ai/use-case/do-beancount-bookkeeping-and-vat-return-prep-with-claude
  - Claude Cowork 找出几笔录错的收据金额，合计 922 美元：https://agentusecases.ai/use-case/catch-mistyped-receipt-amounts-in-expense-records
  - 自由职业者用 Claude Code 搭了开票和收款跟踪系统，每周省约 90 分钟：https://agentusecases.ai/use-case/build-a-freelancer-invoicing-system-with-claude-code
  - 用 Claude Code 搭定时晨间研究流程，管理 Alpaca 模拟盘：https://agentusecases.ai/use-case/run-a-paper-trading-portfolio-with-a-morning-research-routin
- **营销**：
  - 洗车店老板用 Claude Code 调研竞品广告、写广告组和否定关键词，数据费用 0.46 美元：https://agentusecases.ai/use-case/build-a-google-ads-search-campaign-for-a-local-business
  - 营销公司测试 ChatGPT Operator：能把 GA 数据导进表格并导出搜索词报告，但慢，后面步骤卡住：https://agentusecases.ai/use-case/run-google-ads-and-analytics-tasks-with-an-agent
- **编程**：
  - Lantern Lattice 通过 MCP 给 coding agent 提供编译器级调用图，两次调用就能跨 4 个文件重命名函数：https://agentusecases.ai/use-case/give-coding-agents-compiler-accurate-call-graphs-for-refacto
  - 让 agent 用 ntrecord 录终端会话，回看后修复 TUI 图表 bug：https://agentusecases.ai/use-case/let-agents-record-terminal-tapes-to-fix-tui-bugs
- **求职与招聘**：
  - 开源 agent 用 Claude 给 PDF 简历打分，60 分以上的通过 Vapi 打电话面试并排名：https://agentusecases.ai/use-case/screen-resumes-and-run-ai-voice-interviews-for-candidates
  - 有人上传简历让 ChatGPT 回答申请问题，投了约 300 份工作：https://agentusecases.ai/use-case/answer-job-application-questions-from-an-uploaded-resume
- **个人助理**：
  - 自建语音助手 April，开车时处理邮件和日程，邮件处理从每天 2 小时降到清零：https://agentusecases.ai/use-case/clear-your-inbox-by-voice-while-commuting

## 地址／IoC 汇总

- **OPTIMJACK（Optimizely 标签层投毒）**——来源：Amirul Cyber 文章 https://amirulcyber.com/2026/11/16/optimjack-optimizely-skimmer/ 、Scott Helme https://x.com/Scott_Helme/status/2122426351953043522 、https://x.com/Scott_Helme/status/2122429624160288785 （原样抄录）
  - C2／加载与回传：`1688360.cc/track.js`、`1688360.cc/hit.php`、`1688360.cc/card.php`、`1688360.cc/html2canvas.min.js`（Scott Helme：`1688360[.]cc`）
  - iOS 第二阶段：`5vobauua3ojpklx.icu/boot.js`、`eil786npto9u5bq.icu/boot.js`、`eil786npto9u5bq.icu/JIUJIU888/weifile.html`
  - Scott Helme 追加封堵域名：`eil786npto9u5bq[.]icu`、`l7bcsnwc7nzr3uo[.]icu`、`q1ls1ho9x7wsxlu[.]icu`、`p55abnw2pnsz0bo[.]icu`、`1y69gy2mdzaltz1[.]icu`、`gm38duxoihbmy5o[.]icu`
  - SHA-256：`f7b84b9a94f749f8ced3f0112d0a66894e8bbc3b4aa5592021d1b8976a9bad40`（track.js）、`2f69879f1c5bdfe9c075ef67ddb6405afe992aff89dcf42863567f83237d3ba6`（eil786 boot.js）
  - 攻击者替换钱包地址（文件头原样）：
    - ETH `0xC4026b06D82b0F0B363eda0642D61CfbDc17884e`
    - TRX `THvs6p56XkUiMkJeSc51cAP64u2RsTYqxa`
    - BTC `19g9rZcPeiz8rUvyWpTRyXXhPnjsWrc3kW`
    - TON `UQAgM1VqSZQiJLSG5w-ovurq5CZdxLEK3_7CMmwALTA5e09p`（raw：`0:2033556a49942224b486e70fa8beeaeae4265dc4b10adffec2326c002d30397b`）
    - SOL `FVtL8NMYS9PA1v3HE67XUGCtGA9JaZUvqav2fU2LrV5n`
    - LTC `ltc1q3wp7g6ds0ggg6fl6kncpa4sepn0q3qfacgred5`
    - BCH `qzkaaf8n6grmpr0d9lx8xutn3r9lk722f566hhpe58`
    - DOGE `DBEGrxRF7KMSuhTS4c1MFviStU6efdMnu5`
- 无上下文哈希（i0n1c 发帖「Just in case …」，未说明含义，仅原样记录，不当作恶意指标）：`40ffa574725d2f75c533b788f9966e43d99ca7b243c0a63865d1595490c6ad19` — https://x.com/i0n1c/status/2122267720955859406
- 泄露站播报里的受害者域名（如 ncip[.]gov[.]ph）是受害方官网，不是攻击基础设施，不作为 IoC。
- 其他条目（Axis、LibreOffice、Amazon LLM 网关、Retadup、Gootloader 等）：公开报道里未见可抄录的 IoC。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）：https://x.com/i/lists/1239330068461244424 （本期 2 页 193 帖，窗口内 186 帖；主要信号来自 Dinosn、ipurple、cyb3rops、patrickwardle、spaceraccoonsec、vysecurity、SwitHak、evilsocket（转 Scott Helme IoC）、domchell、kmkz_security）
- 博客清单：https://blog.badsectorlabs.com/files/blogs.txt （本地：lwis-sources/blogs.txt；本期用于补链 spaceraccoon.dev、Thalium、Rapid7）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- SecureFlow 安全信息流：https://secureflow.scope-sentry.top/all
- SecureFlow 社区：https://secureflow.scope-sentry.top/community
- SecureFlow 博客：https://secureflow.scope-sentry.top/blog
- Agent Use Cases：https://agentusecases.ai/ （RSS https://agentusecases.ai/feed.xml）
- AI/TLDR：https://ai-tldr.dev/ （Atom https://ai-tldr.dev/feed.xml）
- pwn.watch：https://pwn.watch/ （RSS https://pwn.watch/feed.xml）
- ExploitGrid：https://exploitgrid.net/
- 阮一峰周刊（仅周末版）：https://www.ruanyifeng.com/blog/atom.xml

## 来源搜索 URL（含 SecureFlow 三个接口、pwn.watch 订阅源、ExploitGrid 两个数据地址、AI/TLDR 订阅源、Agent Use Cases RSS、周末版的阮一峰周刊、各来源条数与覆盖区间）

- X Latest · CVE 组：`(CVE OR POC OR exploit OR 0day OR zero-day) (patch OR vulnerability OR exploited) -is:retweet lang:en` → https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&f=live （25 条，11-16 22:09～22:48 UTC）
- X relevancy · CVE 组补搜：同上查询，按相关度 → https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day （25 条，11-16 12:00～17:08 UTC）
- X Latest · 工具组：`github.com (C2 OR "red team" OR nuclei OR redteam OR "offensive security") -is:retweet` → https://x.com/search?q=github.com%20C2%20OR%20%22red%20team%22%20OR%20nuclei&f=live （1 条，无关）
- X Latest · 威胁组：`("malware analysis" OR "threat report" OR "threat actor") -is:retweet lang:en` → https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live （25 条，11-16 21:01～22:41 UTC）；relevancy 25 条（11-15 22:53～11-16 20:47 UTC）
- LWiS X List：https://x.com/i/lists/1239330068461244424 （2 页 193 帖，窗口内 186 帖，11-15 22:50～11-16 22:47 UTC）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条，覆盖 11-06 14:00～11-16 20:44 北京时间；48 小时内新 9 条）
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community → 逐源 https://secureflow.scope-sentry.top/api/rss/articles/<源id> （7 源：先知社区 4、奇安信攻防社区 0、Seebug Paper 0、t00ls 0、吾爱破解 0、InfoSec Write-ups 0、Critical Thinking 0；窗口 48 小时）
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog → 逐源拉取（12 源：samcurry、bombon、moaz、voorivex、projectdiscovery、ZDI-Blog、ZDI-vulnerabilities、dirkjanm、atum 等，7 天内新 0 条）
- pwn.watch：https://pwn.watch/feed.xml 、https://pwn.watch/feed.json （lastBuildDate 2026-11-08 20:19 GMT；本窗口无新条目）
- ExploitGrid 最新 exploit：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （100 条，最新 11-15 17:56 UTC；未收录 29 条，展开 8 组）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （CVE-2026-123039、CVE-2026-114713 期限 11-16；CVE-2026-124194、125350、20320、111793 期限 11-24；与 CISA 一致）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （目录版本 2026.11.13，近两天无新增）
- NVD API（CVE 详情核对）：https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-90436
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条；36 小时内新 17 条，security 5 条）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条；48 小时内新 14 条）
- 阮一峰周刊：本期为周一，第 419 期已在周六（11-14）那期收录，本期不加此节。
- 核验记录：报告共 234 个可核验 URL（不含 X 搜索页与 SecureFlow 模板地址）；80 条 X 原帖都在本期采集数据或按 id 查询中核对过帖子 id 与作者（Qwen 官方帖为单独按 id 查询确认）；其余 154 个用浏览器 UA 逐个请求，全部返回 200。先知社区「uni-app 加密流量分析」（https://xz.aliyun.com/news/93341 ）换 UA 并加 Referer 后仍 404，已从精选中删除。t.co 都已展开；DFIR_Radar、jabbathecrypto、YourDailyCVE、FBICyberBranch、azoxlpf 帖内 t.co 只指向图片，所以只列原帖。
- 验收：采集 ✅（X Latest／relevancy／LWiS List 均成功；SecureFlow 三路、pwn.watch、ExploitGrid、AUC、AI/TLDR 均已拉取并写明条数）· 核验链接 ✅（见核验记录）· 成稿 ✅（十个小节齐全（周一不含周刊节），IoC 原样抄录，无利用步骤，已按 seen_ids 去重）· 落盘与交付 ✅（box 与本机副本均已写入并读回确认）
