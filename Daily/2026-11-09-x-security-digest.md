# X 安全情报晚报 · 2026-11-09（周一）

> 报告时间：2026-11-09 约 20:10（America/Santiago）＝ 2026-11-10 约 07:10（香港时间）。
> **覆盖时长**：X Latest/相关度搜索覆盖 2026-11-08 23:00 UTC～11-09 23:07 UTC（约 24 小时，只读）；纯 Latest 的 CVE 搜索被股票代码 $CVE、「exploit」口语等噪音刷屏，25 条只覆盖约 3 分钟，已用 relevancy 补搜及按事件关键词补搜补满 24 小时。LWiS X List 翻两页共 194 帖，覆盖约 11-08 12:00～11-09 22:22 UTC（超过 24 小时）。SecureFlow 取近 48 小时（blog 放宽 7 天）；AI/TLDR 取 36 小时；Agent Use Cases 取 48 小时。
> **验收说明**：见文末「验收结果」。
> 公开备援：CISA KEV 11-09 新增 4 条（GPUStack、OpenSSH、FreeSWITCH、IBM Aspera Faspex），联邦期限均为 11-12。

## 今日摘要

- **N-able N-central「Able2Shell」**：研究员 11-08 公开 33 个声称的 0day 及 PoC（含未授权 XXE→RCE 链），N-able 11-09 下线托管环境并要求本地部署客户暂时断网；厂商称尚未见在野利用，但 Lupovis、Previdian 蜜罐已观测到与 PoC 吻合的探测（IP 见 IoC 节）。
- **CISA KEV 新增 4 条**：OpenSSH「SSHole」CVE-2026-123158（仅 musl 且无 PAM，如 Alpine；修复 10.6p2）、GPUStack CVE-2026-102895（修复 2.2.0）、FreeSWITCH CVE-2026-116779（修复 1.11.3）、IBM Aspera Faspex CVE-2026-123218。
- **供应链 × AI 编码 agent**：Miasma/testmetest 蠕虫 11-09 投毒 12 个 GitHub 仓库，用 CLAUDE.md 里的提示注入让 agent 不看就执行 setup.js；另有 strutil-core（shai-hulud 载荷）出现在 14 个仓库；Socket 披露 Ethersphere 发布流水线被劫持，经 npm 和苹果公证的桌面应用投毒，关联 SleepyDuck。
- **威胁归因**：法国官方将超市冷柜（Danfoss/Copeland/Dixell）攻击归因于伊朗（CERT-FR CTI-009）；Expel 分析 The Gentlemen 勒索团伙用于干掉 EDR 的 0day。
- **AI 安全**：Fireworks AI 10 月入侵扩大（部分客户数据集与未完成微调权重被访问）；OpenAI 推出 Control Room 紧急停机层；微软 FORGE Lab 用 AI 工具发现 Rust core/std 内存安全问题。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

**1. N-able N-central「Able2Shell」33 个声称 0day（Appliance 2026.4.0.31 及可能更早版本；尚无 CVE、尚无补丁）**
- 谁／什么：研究员 11-08 在 GitHub 公开漏洞细节与 PoC，至少 4 条利用链（3 条 RCE、1 条提权到 root）；最严重的是未授权 XXE（服务导入）→ 会话窃取 → 重置口令 → 以 nable 用户执行命令。N-able 11-09 下线美洲／欧洲／亚太托管环境，建议本地部署暂时离线，等待热修复。截至 11-09 15:15 UTC 厂商称未见在野利用；Lupovis、Previdian 当天观测到 PoC 对齐的 SOAP 探测，但未见完整链。
- 处置：本地 N-central 先离线；复查 11-08 起登录与审计日志、新建管理员账号、异常脚本下发；关注 /dms/services/ServerUI、ImportServiceFromFile 等接口访问。
- X 原帖：[HuntressLabs](https://x.com/HuntressLabs/status/2119858184039043370) · [LupovisDefence 观测](https://x.com/LupovisDefence/status/2119923970237403163) · [SwitHak 转](https://x.com/SwitHak/status/2119881312056361194)
- 文章：[Huntress 博客](https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains)（box 换 UA＋Referer 后仍 403，浏览器可开） · [BleepingComputer](https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/) · [Previdian](https://blog.previdian.com/n-able-n-central-critical-vulnerabilities-what-we-know-so-far/) · [TechTarget](https://www.techtarget.com/news/n-able-takes-n-central-platform-offline-after-zero-day-dump/874195/)

**2. OpenSSH「SSHole」CVE-2026-123158 入 KEV（11-09；Linux 上 musl 且未用 PAM 时口令认证绕过，典型是 Alpine；修复 OpenSSH 10.6p2 或 Alpine 补丁包）**
- 跟进：11-06/11-07 期已报道披露与早期利用；今日新增 KEV 入库、JPCERT 通告、先知社区复现分析。Alpine 为回移补丁，`sshd -V` 不一定显示新版本，按包版本核对后重启 sshd。
- X 原帖：[CipherSecurityN（KEV）](https://x.com/CipherSecurityN/status/2119834531079614810) · [vuln_tracker 汇总](https://x.com/vuln_tracker/status/2119919263204917618) · [PacketReport1（影响面说明）](https://x.com/PacketReport1/status/2119808843698090470) · [__kokumoto](https://x.com/__kokumoto/status/2119925650014486994)
- 厂商公告：[CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [Alpine 公告](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/) · [OpenSSH Release Notes](https://www.openssh.org/releasenotes.html) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123158)
- 文章：[先知社区 复现与分析（SecureFlow）](https://xz.aliyun.com/news/93220)

**3. GPUStack CVE-2026-102895（CVSS 9.8，未授权管理员访问，回环认证绕过；修复 2.2.0）入 KEV**
- 可导致创建持久管理员 API key、泄露 worker／云厂商密钥、经推理后端接口执行代码。AI GPU 集群若对外暴露应立即升级并轮换密钥。
- X 原帖：[Rachidmarcil](https://x.com/Rachidmarcil/status/2119843114441646249) · [vuln_tracker](https://x.com/vuln_tracker/status/2119919263204917618)
- 厂商公告：[GHSA-gj9m-f8ph-pmhr](https://github.com/gpustack/gpustack/security/advisories/GHSA-gj9m-f8ph-pmhr) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-102895)

**4. SignalWire FreeSWITCH CVE-2026-116779（9.8，SIP MESSAGE 触发 API 命令／代码注入；修复 1.11.3）入 KEV**
- X 原帖：[vuln_tracker](https://x.com/vuln_tracker/status/2119919263204917618) · [yabetchi_iPhone 日文汇总](https://x.com/yabetchi_iPhone/status/2119926476376351114)
- 厂商公告：[GHSA-mg63-h38w-8p9p](https://github.com/signalwire/freeswitch/security/advisories/GHSA-mg63-h38w-8p9p) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-116779)

**5. IBM Aspera Faspex CVE-2026-123218（已认证用户越权提权）入 KEV**
- X 原帖：[__kokumoto](https://x.com/__kokumoto/status/2119925650014486994)
- 厂商公告：[IBM 公告 7295921](https://www.ibm.com/support/pages/node/7295921) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123218)

**6. iOS 沙箱逃逸 PoC「worse_query」公开（称影响 iOS 26.0–26.7.2、27.2、27.3 beta；bad_query 的后继）**
- 本地 App 逃出容器访问系统路径并改写其他 App 数据；尚未见 Apple 公告，关注后续更新，企业 MDM 可限制侧载。
- X 原帖：[blackorbird](https://x.com/blackorbird/status/2119623704011514103) · [XBToshi](https://x.com/XBToshi/status/2119705280686797062)
- GitHub／PoC：[forcequitOS/worse_query](https://github.com/forcequitOS/worse_query)

**7. Zyxel 交换机入侵：原以为是已修补漏洞，实为 0day（跟进 11-03～11-06 期）**
- X 原帖：[lcopelandjr](https://x.com/lcopelandjr/status/2119919077598908546)
- 文章：[SecurityWeek](https://www.securityweek.com/zyxel-switch-hacks-blamed-on-patched-flaw-actually-exploited-a-zero-day/)

**8. 其他值得一看**
- Project Zero：Samsung S24 WMF 媒体解析越界读 — [X 原帖](https://x.com/ProjectZeroBugs/status/2119874531787714985) · [Project Zero issue](https://project-zero.issues.chromium.org/issues/537859150)
- 微软 FORGE Lab：AI 辅助发现 Rust core/std 内存安全问题（安全 Rust 也能触发 UB，已与维护者修复） — [X 原帖](https://x.com/MsftSecIntel/status/2119890522466578648) · [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/11/09/forge-lab-uses-agentic-tools-to-identify-memory-safety-issues-in-rust/)
- LOLDrivers 新增 AmdTools64.sys 1.7.16.218 样本（IOCTL 可映射任意物理地址，等于内核读写），建议加入驱动阻止列表 — [X 原帖](https://x.com/_josehelps/status/2119475536611495979) · [LOLDrivers 条目](https://www.loldrivers.io/drivers/1bab0fae-7908-4fae-9db7-73562c7d92cd/)
- NetExec enum_cve 增加 LDAP 签名绕过补丁检测 — [X 原帖](https://x.com/al3x_n3ff/status/2119791469443916127)
- 汽车厂商服务器默认 admin:admin 致可远程解锁启动车辆 — [X 原帖](https://x.com/Dinosn/status/2119826076381954292) · [The Hacker News](https://thehackernews.com/2026/11/default-adminadmin-server-password.html)
- 微软 Azure Linux 一次修复 470+ 安全问题 — [X 原帖](https://x.com/Dinosn/status/2119819077724319957) · [The Register](https://www.theregister.com/security/2026/11/09/microsofts-azure-linux-gets-470-plus-security-fixes-in-one-almighty-patching-session/5308434)
- Apple 发布 macOS 27.2.1 / 26.7.3 / 15.8.3 更新 — [X 原帖](https://x.com/howardnoakley/status/2119859099684794566) · [Eclectic Light](https://eclecticlight.co/2026/11/09/apple-has-just-released-updates-to-macos-27-2-1-26-7-3-and-15-8-3/)

## 工具与 GitHub 发布（每条：说明 + 地址列表）

**1. Crucible：面向紫队的 Mythic C2 agent**，把 Atomic Red Team YAML 编成 .NET 9 单文件，按操作员指令执行并回报各技术结果，适合检测验证。
- X 原帖：[ipurple](https://x.com/ipurple/status/2119792519395303792)
- GitHub：[Whispergate/Crucible](https://github.com/Whispergate/Crucible)

**2. homer：Donut 的规避型分支**（生成从内存加载 PE 的位置无关 shellcode）——蓝队可据此补充内存加载检测。
- X 原帖：[ipurple](https://x.com/ipurple/status/2119896278507135118)
- GitHub：[twili8/homer](https://github.com/twili8/homer)

**3. Quick-Shift：恶意 LNK 诱导 NTLM 认证外泄的工具**——防御侧注意出站 SMB/WebDAV 与 LNK 图标路径。
- X 原帖：[ipurple](https://x.com/ipurple/status/2119887751730581816)
- GitHub：[Ossipher/Quick-Shift](https://github.com/Ossipher/Quick-Shift)

**4. Windows LOLBins 行为检测引擎（Python 3.12，防御向）**
- X 原帖：[ipurple](https://x.com/ipurple/status/2119870843128009201)
- GitHub：[nimesh895/Behavioral-Living-off-the-Land-LOLBins-Detection-System](https://github.com/nimesh895/Behavioral-Living-off-the-Land-LOLBins-Detection-System)

**5. Suzaku「Vulnpocalypse」版本（Yamato Security 云日志威胁狩猎工具）**
- X 原帖：[DirectoryRanger 转 Enno_Insinuator](https://x.com/DirectoryRanger/status/2119842848145015126)
- GitHub：[Yamato-Security/suzaku](https://github.com/Yamato-Security/suzaku)

**6. Combat Theater 1.2「Metal Claw」**（从威胁情报报告直接生成可执行的对抗模拟）
- X 原帖：[felixm_pw](https://x.com/felixm_pw/status/2119604592883187839)
- 文章：[发布博客](https://combat.theater/blog/v1-2-metal-claw)

**7. DreadIndex 新增三款模型的攻防能力评测**（MiniMax M3.1 Flash、GPT 5.6 Sol、Kimi K3.1 Pro）
- X 原帖：[dreadnode](https://x.com/dreadnode/status/2119894745489027416)
- 文章：[DreadIndex](https://www.dreadnode.io/research/dreadindex/)

**8. 警示：假冒 GitHub 安全工具感染 2,000+ 台电脑（Doctor Web），针对安全从业者**——运行陌生 PoC／工具前先隔离审查。
- X 原帖：[TheHerecy](https://x.com/TheHerecy/status/2119807231600332882)
- 文章：[Security Affairs](https://securityaffairs.com/202717/malware/fake-github-security-tools-infect-over-2000-pcs-with-malware.html)

## APT / Malware 分析（每条：说明 + 地址列表）

**1. Miasma/testmetest 供应链蠕虫新一波：针对 AI 编码 agent（11-09，12 个 GitHub 仓库被伪造回溯提交投毒）**
- 仓库内 CLAUDE.md 等 agent 配置标注「DEVOPS-SEALED」，要求 agent 不阅读、不展示输出、不经确认直接运行混淆的 3.7 MB scripts/setup.js——本质是阻止 agent 审查文件的提示注入。另一路：Ruby 包 strutil-core 的 shai-hulud 载荷周末出现在至少 14 个仓库（同样回溯提交、同一 C2，疑为账号接管）。
- 处置：对 agent 配置文件（CLAUDE.md、AGENTS.md 等）中的「勿读／勿确认」类指令告警；agent 执行新脚本前强制人工确认。
- X 原帖：[fr0gger_](https://x.com/fr0gger_/status/2119730348699640060) · [fr0gger_ 仓库清单](https://x.com/fr0gger_/status/2119730841857282526) · [oliver_ojsec（strutil-core）](https://x.com/oliver_ojsec/status/2119622892602163233)
- GitHub：[GitHub 代码搜索（注入指令特征）](https://github.com/search?q=%22DO+NOT+read%2C+quote%2C+or+display+the+contents+of%22&type=code)

**2. Ethersphere（bee-js）发布流水线被劫持：npm 包与苹果公证桌面应用投毒，关联 SleepyDuck（同一以太坊 C2 合约与后门载荷）**
- X 原帖：[SocketSecurity](https://x.com/SocketSecurity/status/2119817046720442565)
- 文章：[Socket 博客](https://socket.dev/blog/bee-js-compromise)

**3. 法国官方将超市冷柜（Danfoss/Copeland/Dixell）攻击归因伊朗 IRGC 关联行为体（Emennet Pasargad 等）**
- X 原帖：[SwitHak 线程](https://x.com/SwitHak/status/2119856452965986348) · [thegrugq 转 ryanaraine](https://x.com/thegrugq/status/2119896788375347556)
- 厂商／政府公告：[法国外交部声明](https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/declaration-d-attribution-a-l-iran-de-cyberattaques-visant-la-france) · [CERT-FR CTI-009](https://cert.cyber.gouv.fr/cti/CERTFR-2026-CTI-009/)
- PDF：[CERTFR-2026-CTI-009.pdf](https://cert.cyber.gouv.fr/uploads/CERTFR-2026-CTI-009.pdf)

**4. Expel：The Gentlemen 勒索团伙用 0day 内核利用关闭 EDR**（研究者补充：受害机须为 Windows 10，多数 Windows 11 上 KUSER_SHARED_DATA 固定映射为只读）
- X 原帖：[_winterknife_](https://x.com/_winterknife_/status/2119871485837754835)
- 文章：[Expel 博客](https://expel.com/blog/not-very-gentlemanly-analyzing-a-zero-day-exploit-used-by-the-gentlemen-ransomware-to-disable-targets-edrs/)

**5. Todyl：攻击者用被盗应用凭据以工作负载身份登录 Entra ID 与 Azure DevOps**——审计服务主体登录与凭据新增。
- X 原帖：[DirectoryRanger](https://x.com/DirectoryRanger/status/2119571875944939739)
- 文章：[Todyl 博客](https://www.todyl.com/blog/stolen-app-credentials-real-access-an-actor-is-signing-into-entra-id-and-azure-devops-as-your-workloads)

**6. 云访问密钥被滥用开启 LLM API（LLMjacking）造成巨额账单**——监控 Bedrock/Vertex 等服务的突然启用。
- X 原帖：[IEthics](https://x.com/IEthics/status/2119913582255374810)

**7. 数据泄露动态（摘要）**：SEGA 供应商泄露 220 万邮箱；Iris Ohyama 770 万客户；Frontline Education 300 万人；意大利外长数据遭亲俄黑客泄露。
- X 原帖：[Dinosn SEGA](https://x.com/Dinosn/status/2119825954378031430) · [Dinosn Iris](https://x.com/Dinosn/status/2119825361030832398) · [Dinosn Frontline](https://x.com/Dinosn/status/2119820191014240302) · [Dinosn Meloni](https://x.com/Dinosn/status/2119819625718571047)
- 文章：[CyberInsider](https://cyberinsider.com/sega-data-breach-2-2-million-email-addresses/) · [SC World](https://www.scworld.com/brief/iris-ohyama-discloses-data-breach-affecting-7-7-million-customers) · [SecurityWeek Frontline](https://www.securityweek.com/3-million-people-hit-by-frontline-education-data-breach/) · [SecurityWeek Meloni](https://www.securityweek.com/italys-meloni-blames-pro-russian-hackers-for-leak-of-foreign-ministers-data-on-the-dark-web/)

## SecureFlow 信息流精选（X 上未出现的高信号条目）

**community**
- 奇安信攻防社区：CVE-2026-96658 Foreman safemode 沙箱逃逸致 RCE 的源码级分析——Foreman/Satellite 用户核对版本与模板编辑权限。 [原文](https://forum.butian.net/share/5282)（box 网络无法连接，浏览器可开）
- （先知社区 OpenSSH/musl CVE-2026-123158 复现已合并进上文 CVE 第 2 条。）

**blog**
- 本日无显著更新（12 个博客源 7 天内无未收录的新文章）。

**BugBounty**
- HackerOne：`@aws-cdk/aws-redshift-alpha` 自定义资源中未净化的标识符与字符串导致 SQL 注入——使用该 alpha 模块的团队留意上游修复版本。 [原文](https://hackerone.com/reports/3797662)

## AI/TLDR 动态（来自 ai-tldr.dev；本窗口 36 小时内新条目 9 条，其中 security 类 2 条）

今天 AI 圈的重点是 Anthropic 发布新旗舰 Claude Fable 5.2（降价、提速）并同步更新 Claude Code；安全方面 Fireworks AI 的 10 月入侵被确认波及客户数据集与微调权重，OpenAI 把紧急停机做进推理层。开源侧有 Meta 小模型 Muse Ember、Nous 的 Arete-27B 以及在 64 GB CPU 上跑 284B MoE 的 llama-modchip。

**安全**
- 〔安全〕Fireworks AI 10 月入侵扩大：账单数据外，部分客户的数据集与未完成的微调权重被访问——使用其托管微调的团队应评估数据与权重泄露影响。 [AI/TLDR](https://ai-tldr.dev/releases/fireworks-ai-october-breach-update/) · [Fireworks 公告](https://fireworks.ai/security/bulletins/october-2026-security-incident-update)
- 〔安全〕OpenAI Control Room：把研究模型的紧急停止放到推理层，失效即关闭（fail-closed）。 [AI/TLDR](https://ai-tldr.dev/releases/openai-control-room/) · [OpenAI 对齐事件报告](https://alignment.openai.com/misalignment-reports/)

**模型**
- Anthropic Claude Fable 5.2：新旗舰，价格降约 20%、速度快至 30%。 [AI/TLDR](https://ai-tldr.dev/releases/anthropic-claude-fable-5-2/) · [Claude 模型文档](https://platform.claude.com/docs/en/about-claude/models/overview)
- Meta Muse Ember：Muse 家族最便宜的小模型，专做 agent 子任务。 [AI/TLDR](https://ai-tldr.dev/releases/meta-muse-ember/) · [HN 讨论](https://news.ycombinator.com/item?id=50429024)
- Nous Research Arete-27B：基于 Qwen3.8-27B，去除政治宣传式回答。 [AI/TLDR](https://ai-tldr.dev/releases/nousresearch-arete-27b/) · [Hugging Face](https://huggingface.co/NousResearch/Arete-27B)

**工具与开源仓库**
- Claude Code 2.1.321：默认 Fable 5.2，修复 MCP OAuth 及若干权限与 token 泄露问题（建议升级）。 [AI/TLDR](https://ai-tldr.dev/releases/anthropic-claude-code-2-1-321/) · [GitHub Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.321)
- llama-modchip 2.4：在 64 GB 内存 CPU 上运行 284B DeepSeek-V4-Flash，无需 GPU。 [AI/TLDR](https://ai-tldr.dev/releases/synchopate-llama-modchip-2-4-0/) · [GitHub](https://github.com/synchopate/llama-modchip)

**论文与研究／行业动态**
- 本日无显著更新（另有 video 2 条只计数：Fireship 讲 OpenAI agent 找到 948 个 Linux 内核提权、Sam Witteveen 讲 Nemotron 2-bit 模型）。

## Agent 用例动态（来自 agentusecases.ai；48 小时内新条目 35 条，以下精选 20 条）

今天的用例集中在三块：一是 Claude Code／Codex 做编程与设计落地（经 MCP 连 Figma、Paper，写测试、按规格带审查子 agent 开发）；二是常驻本地或云端的「个人助理」agent（Hermes、Dots、OpenClaw）24 小时盯价格、打电话、管项目；三是浏览器／电脑操控 agent（Comet、Operator、Claude in Chrome）做表格、邮箱整理和比价，普遍反馈慢或会卡住。安全相关的用例里，有人让 agent 加固 homelab 结果把自己锁在外面，也有人坚持「发送前人工批准」「到源系统核验结果」。

**〔安全相关〕权限、核验与风险**
- 用户让 Claude Opus 收紧 homelab 访问控制，它把自己锁在外面后拒绝继续，改用 OpenAI 完成。 [用例](https://agentusecases.ai/use-case/tighten-access-controls-and-isolation-in-a-homelab)
- 有人用 Hermes 常驻本地监控降价、经 Twilio 打电话、起草邮件且仅在批准后发送。 [用例](https://agentusecases.ai/use-case/run-a-24-7-local-agent-for-price-drops-calls-and-email-draft)
- 有人运营 Hermes agent 集群，只有在已发送邮件夹或 CRM 里核验到结果才算完成。 [用例](https://agentusecases.ai/use-case/run-an-agent-fleet-with-results-verified-in-source-systems)
- 有人通过桌面应用让 Dots 访问自己的 Linux 服务器并用云浏览器操作。 [用例](https://agentusecases.ai/use-case/let-an-agent-operate-your-linux-server-and-apps)

**编程与多 agent 编排**
- 创意开发者让 Codex 抓取 200+ 个 OpenProcessing 作品，整理成带提交说明的仓库上传 GitHub。 [用例](https://agentusecases.ai/use-case/migrate-200-sketches-from-openprocessing-to-github)
- 团队让 Claude 写全面测试补覆盖率，结果压垮 CI 节点、还测了已禁用功能，只算部分成功。 [用例](https://agentusecases.ai/use-case/write-exhaustive-test-suites-to-clear-a-coverage-backlog)
- 有人让 Claude Code 按详细规格开发，配审查子 agent、上下文管理与自动测试。 [用例](https://agentusecases.ai/use-case/build-software-from-a-spec-with-claude-code-and-review-sub-a)
- 有人用 bash＋Python＋Claude Code CLI 搭出自建 agent，它自己写了 MCP 服务器。 [用例](https://agentusecases.ai/use-case/grow-a-bespoke-agent-from-claude-code-that-builds-its-own-mc)
- 用户把一个 Claude 对话链接交给 Cowork 任务做独立复核。 [用例](https://agentusecases.ai/use-case/get-an-independent-review-of-a-task-from-another-claude-sess)

**设计**
- 设计师经 MCP 把 Claude Code 接到 Paper，生成 Robinhood 风格的 iOS 交易 App 设计稿。 [用例](https://agentusecases.ai/use-case/design-an-ios-trading-app-from-a-prompt-in-paper)
- 设计师用 Claude Code＋Figma 三天生成可编辑的乐队网站设计。 [用例](https://agentusecases.ai/use-case/generate-editable-website-designs-in-figma-from-the-terminal)
- 作者用 Claude Design 从 GitHub 链接生成着陆页原型，再由 Claude Code 实现上线。 [用例](https://agentusecases.ai/use-case/redesign-a-landing-page-and-ship-it-from-a-github-link)

**个人助理与常驻 agent**
- 有人把 Dot 当私人幕僚长管理多个项目。 [用例](https://agentusecases.ai/use-case/use-an-agent-as-a-personal-chief-of-staff)
- 有人在旧笔记本上跑 OpenClaw，规划 Kickstarter 上市并管理 PR 流程。 [用例](https://agentusecases.ai/use-case/plan-a-kickstarter-launch-and-manage-pr-with-an-agent)
- Hermes agent 帮用户调研购买选项并直接下单。 [用例](https://agentusecases.ai/use-case/research-purchase-options-and-place-the-order)
- 用户让 Alexa+ 找出重复的家居例程并自动修好。 [用例](https://agentusecases.ai/use-case/find-and-fix-duplicate-alexa-routines)

**电脑操控与浏览器 agent**
- 作者用 Claude Dispatch 电脑操控在 Fiverr 发需求、联系候选人并建广告表格。 [用例](https://agentusecases.ai/use-case/hire-a-fiverr-freelancer-and-build-an-ads-sheet-by-computer-)
- 用户让 Operator 规划行程写进 Notion、比较四家超市价格，但速度慢。 [用例](https://agentusecases.ai/use-case/plan-trips-and-compare-grocery-prices-with-operator)
- 用 Perplexity Comet 清理 Gmail、退订新闻信、找旧 Reddit 评论。 [用例](https://agentusecases.ai/use-case/clean-gmail-and-find-old-reddit-comments-with-a-browser-agen)

**学习与研究**
- ChatGPT 经 MCP 在共享画布上画图讲解物理、生物和几何并出练习。 [用例](https://agentusecases.ai/use-case/teach-topics-by-drawing-on-a-shared-canvas-board)

## 地址／IoC 汇总

以下为原文所列，原样抄录（已去活化），仅供检测与封禁：
- `3.74.48[.]121` — Lupovis 观测：与 Able2Shell PoC 吻合的 N-central SOAP 信息泄露探测（来源：https://x.com/LupovisDefence/status/2119923970237403163）
- `5.231.45[.]175` — Lupovis／Previdian 观测：N-central 服务导入 XXE 面侦察（来源同上及 https://blog.previdian.com/n-able-n-central-critical-vulnerabilities-what-we-know-so-far/）
- N-central 被探测接口：`/dms/services/ServerUI?wsdl`、`/dms/services/ServerUI?method=nci`、`ImportServiceFromFile`、`/dms/services/ServerMMS`（同上）
- `palebeast[.]top` — strutil-core／shai-hulud 载荷所用 C2（来源：https://x.com/oliver_ojsec/status/2119622892602163233）
- Miasma/testmetest 投毒特征：agent 配置含「DEVOPS-SEALED」、要求运行 `scripts/setup.js`（约 3.7 MB 混淆）（来源：https://x.com/fr0gger_/status/2119730348699640060）
- 漏洞驱动：AmdTools64.sys 1.7.16.218（LOLDrivers：https://www.loldrivers.io/drivers/1bab0fae-7908-4fae-9db7-73562c7d92cd/）
- Ethersphere/SleepyDuck 的以太坊 C2 合约地址：X 帖未列，见 Socket 原文 https://socket.dev/blog/bee-js-compromise
- 其余条目未见公开 IoC。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）: https://x.com/i/lists/1239330068461244424 （本期翻两页取 194 帖，覆盖约 11-08 12:00～11-09 22:22 UTC；成员备份：lwis-sources/x-list-members.json、x-list-handles.txt）
- 博客清单: https://blog.badsectorlabs.com/files/blogs.txt （本地: lwis-sources/blogs.txt）
- CISA KEV: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD: https://nvd.nist.gov/
- Risky Business: https://risky.biz/
- tl;dr sec: https://tldrsec.com/
- SecureFlow 安全信息流: https://secureflow.scope-sentry.top/all （只读接口: https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200）
- SecureFlow 社区: https://secureflow.scope-sentry.top/community （源列表: https://secureflow.scope-sentry.top/api/rss/category?category=community）
- SecureFlow 博客: https://secureflow.scope-sentry.top/blog （源列表: https://secureflow.scope-sentry.top/api/rss/category?category=blog）
- Agent Use Cases RSS: https://agentusecases.ai/feed.xml
- AI/TLDR Atom: https://ai-tldr.dev/feed.xml
- 阮一峰周刊（仅周末版）: https://www.ruanyifeng.com/blog/atom.xml

## 来源搜索 URL

- X 搜索（x 连接器 search_posts_all，只读，自 11-08 23:00 UTC）：①`(CVE OR 0day OR "zero-day" OR exploit OR PoC) (patch OR exploited OR advisory OR RCE) -is:retweet lang:en`（relevancy）；②`(CVE OR 0day OR PoC OR exploit) -is:retweet`（Latest，噪音大，仅覆盖约 3 分钟）；③`github.com (C2 OR "red team" OR nuclei OR redteam) -is:retweet`（仅 1 条）；④`has:links (github OR "new tool" OR "open source" OR release) (C2 OR "red team" OR nuclei OR BOF OR pentest OR offensive) -is:retweet`（补搜）；⑤`("malware analysis" OR "threat report" OR "threat actor") -is:retweet`；⑥事件补搜 `("N-central" OR Able2Shell OR "CVE-2026-123158" OR GPUStack OR Faspex OR FreeSwitch OR "CVE-2026-102764" OR "worse_query" OR Zyxel) -is:retweet`。
- LWiS X List：https://x.com/i/lists/1239330068461244424（X 插件只读 get_lists_posts，2 页 194 帖）。
- SecureFlow：页面 https://secureflow.scope-sentry.top/all · https://secureflow.scope-sentry.top/community · https://secureflow.scope-sentry.top/blog；接口 https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 、https://secureflow.scope-sentry.top/api/rss/category?category=community 、https://secureflow.scope-sentry.top/api/rss/category?category=blog 、https://secureflow.scope-sentry.top/api/rss/articles/<源id>（community 7 源、blog 12 源全部拉取成功；吾爱破解、微信公众号长期未更新）。
- 条数与区间：all 200 条（覆盖 10-26～11-10 02:53 北京时间），48 小时内新 3 条（community 2、BugBounty 1）；community 逐源新 0（已与 all 去重）；blog 7 天内新 0。
- AI/TLDR：https://ai-tldr.dev/feed.xml（共 50 条；36 小时内新 9 条，security 2 条）。
- Agent Use Cases：https://agentusecases.ai/feed.xml（60 条；48 小时内新 35 条）。
- 阮一峰周刊：非周末版不加；最新第 418 期已于 11-07 周末版收录。
- 备援：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json（dateReleased 2026-11-09T19:54Z，新增 4 条）。

## 验收结果

- 采集：通过。X 搜索与 LWiS List 均为只读实取；SecureFlow all、community 7 源、blog 12 源全部拉取成功；AI/TLDR、Agent Use Cases 订阅源已拉取；非周末版，不加阮一峰周刊节。
- 核验链接：通过。报告内 40 条 X 原帖经 X 接口逐条回查全部存在且作者一致；99 条非 X 链接用浏览器 UA 逐条请求，均返回 200，例外两条已注明：Huntress 博客 403（换 UA＋Referer 后仍 403），forum.butian.net 为 box 网络无法连接。
- 成稿：通过。十个小节齐全、无空节，IoC 原样抄录（已去活化），无利用代码／payload／PoC 步骤，已与 seen_ids 去重。
- 落盘与交付：box 文件已写入；本机副本结果见聊天消息。
