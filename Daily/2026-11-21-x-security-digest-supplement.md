# X 安全情报晚报 · 2026-11-21（周六）补刊

> 补采核验时间：2026-11-23 19:14 HKT（香港）。不冒充当日出报。
> 窗口为左闭右开：America/Santiago（UTC−03）2026-11-20 20:00 → 2026-11-21 20:00；UTC 2026-11-20T23:00:00Z → 2026-11-21T23:00:00Z；香港 HKT（UTC+08）2026-11-21 07:00 → 2026-11-22 07:00。

本刊是事后回溯，不是当日实时快照。已核对实际目录：有 11-19、11-22 原刊，既无 11-20／11-21 原刊，也无对应日期 raw 目录；缺失日期据此确认。没有找到失败 run 的原始日志，因此“额度不足”的原因仅来自任务交接，未独立核实。

边界依据：11-19 原刊明确结束于 11-19 23:00 UTC；11-22 原刊开始于 11-21 22:51 UTC。两天采用衔接前刊的各 24 小时**约定窗口**，不是恢复出来的失败 run 精确执行时间；第二天末尾与 11-22 的采集窗重合 9 分钟，按帖子 ID／原文链接另行去重。原规则对 SecureFlow、AUC、AI/TLDR 分别有 48 小时／7 天／36 小时浮动窗口，本次主台账使用不重叠日窗，AI 的特殊日期归属见该节。没有用当前 seen_ids 丢弃候选，没有修改 state 或 routine。

**阅读标记**：〔本次新补采〕=在 11-22 成稿中未展开的回溯条目；〔11-22 已补收〕=为还原日期而归档，不计第二次新情报；〔重复但重大跟进〕=旧事件出现新的利用、补丁或调查状态。该标记只比较“是否在已交付正文中出现”，不代表当时一定未采到。报告之外的完整候选／去重证据保存在独立 backfill 台账。

**验收：部分通过。** X 历史 Latest、相关度和高信号补搜及 LWiS 均实采；但有限检索不等于 X 全量。SecureFlow 三路及 19 个历史已知源均 522，不能恢复；AI/TLDR 的原始 updated 历史不可恢复、详情页 403；滚动源和删除内容不能保证全量。所有这些均记为缺口，而不是“无更新”。


## 今日摘要

- **本次新补采重点**是 Microsoft Entra Connect Health 已遭利用的数据暴露、Bazuka 安卓恶意框架、Burp Suite Sharpener 和 bettercap 发布；Upload2Shell、Cairn 与 FBI 调查在 11-22 已讲过，现回归当窗并补上证据边界。
- 当窗 LWiS **157 条**，与多组历史 X 搜索合并为 **276 条独特候选**（含噪声）。AI/TLDR 可归属条目 **7 条、security 0 条**；AUC 去重 **20 条**，其中 15 条在 11-22 正文已选录，本刊为日期归档，不重复算新增。
- ExploitGrid 最新 date 仍为 11-20 19:48:48 UTC（香港 11-21 03:48:48），本窗匹配 0，但不能据此说当天没有新 exploit。CISA 现有目录 `dateAdded=11-21` 也为 0，只代表目录记录。
- 本期按周六规则收第 **420** 期周刊：14 个 GitHub 项目、7 篇文章／专题，较 11-22 的少量精选更完整；与 11-22 重叠的明确保留为日期归档。

## CVE / POC / 漏洞

### 1. Upload2Shell／Ghostscript CVE-2026-125396〔11-22 已补收；回归原始研究日〕

Paulos Yibelo／pwn.ai 在本窗发布研究，指出文件上传、预览、转码依赖可间接触发 Ghostscript 字体加载器内存问题，突破渲染沙箱并执行代码。研究页日期是 11-21，不是 11-22 新披露。影响取决于实际解码链，**不是有上传框就必然受影响**。

根因修复已在 **Ghostscript 10.08.0（研究称 9 月 8 日发布）**；核对发行版回补，尤其容器、应用捆绑的渲染器，不要只更新宿主机。最小权限运行预览服务、禁用不用的格式／delegate、隔离上传处理。只列研究页，不转载研究中的利用代码或步骤。
- 当窗 X 证据时间：2026-11-22 02:11:12 HKT（香港）；Santiago 11-21 15:11:12。
- X 原帖：https://x.com/PaulosYibelo/status/2124203995329933441 · https://x.com/Dinosn/status/2124213119090090464
- 文章／研究：https://pwn.ai/upload2shell/research.html

### 2. Entra Connect Health 漏洞被利用窃取租户元数据〔本次新补采〕

微软通知称该 API 问题在 11-09 被发现、11-19 服务端修复、11-20 完成调查并通知客户；BleepingComputer 当窗获微软确认。暴露包括管理员／技术联系人邮箱、租户和同步状态、旧的已过期注册证书。**并非用户密码、密码哈希、认证 token 或有效加密密钥泄露**；通知称未发现未授权配置修改。

无须安装客户侧软件补丁。防守建议检查 Azure Service Health 通知、Entra 登录／审计日志和 Connect Health 配置，优先抗钓鱼 MFA，警惕利用管理员邮箱和租户信息的定向社工。未公开 CVE、攻击者或受害数量，不能补造。
- 当窗 X 证据时间：2026-11-22 03:10:18 HKT（香港）。
- X 原帖：https://x.com/Dinosn/status/2124218867165831511
- 文章／研究：https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/

### 3. MONAI Label／Cairn 修复状态〔重复但重大跟进；11-22 已补收〕

本窗继续出现 Amazon 研究报道；这不是 11-21 才发生的攻击，而是披露 9 月事件。MONAI Label 公告显示 ≤0.8.5 有任意写入风险、补丁已合入但当时没有标注发行修复版本。先隔离不可信网络、启用认证、不向不可信用户授予可写权限，并以非特权账户运行。

**事后核验，不倒灌到本窗：**0.8.6 的正式 release 时间为香港 11-22 09:29（UTC 01:29；Santiago 11-21 22:29），晚于本刊结束 2 小时 29 分，现应按该修复版或更高版本更新。研究中两次长时间失败也应计入能力评估。
- X 原帖：https://x.com/Dinosn/status/2124148071256690871
- 厂商／官方公告：https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/ · https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94 · https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6
- 文章／研究：https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/

### 4. Cisco Expressway 与 Roller 在野利用状态、KEV 到期提醒〔重复但重大跟进／11-22 已补收〕

Expressway CVE-2026-76466 的当窗帖子描述了公开研究后攻击集群节点的案例；本次以 CISA 的已利用状态和 Cisco 的 X15.5.20 修复表为基线，不从二手帖拼攻击步骤。Roller CVE-2026-129448 的公开研究在本窗继续传播，修复为 6.1.6 或更高。

CISA 四条 11-20 新增 KEV（含 vCenter、SAP）期限均为 11-23；**11-21** 是 Synology CVE-2024-10441、REDCap CVE-2026-90817、Apache Axis CVE-2026-90436 的目录期限。日期是联邦合规期限，不是漏洞开始危险的日期，也无可证具体小时。
- X 原帖：https://x.com/Sujeet/status/2123944031533297802 · https://x.com/ridvanyagli/status/2124078696877130070
- 厂商／官方公告：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json · https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t
- 公开 exploit 索引（只记收录事实）：https://exploitgrid.net/vulnerabilities/CVE-2026-129448


## 工具与 GitHub 发布

### 1. Burp Suite Sharpener〔本次新补采；当窗介绍〕

Burp 扩展通过 UI 与功能增强改善测试操作。记录本窗传播，不把未核对的 commit 时间说成当天发版；仅用于自有／授权环境，安装前审查扩展权限与来源。
- 当窗 X 证据时间：2026-11-21 14:32:50 HKT（香港）。
- X 原帖：https://x.com/Dinosn/status/2124028243158372608
- GitHub 工具项目（非 PoC）：https://github.com/irsdl/BurpSuiteSharpenerEx

### 2. bettercap v2.42.0〔本次新补采〕

官方账号于香港 11-22 06:20:28（UTC 11-21 22:20:28，Santiago 11-21 19:20:28）宣布 “eMudhra Edition” v2.42.0；LWiS 中 evilsocket 的转帖形成交叉证据。只记录发布事实和官方 release，未执行工具、未提供攻击用法。
- X 原帖：https://x.com/bettercap/status/2124266722471387260 · https://x.com/evilsocket/status/2124266825781301474
- GitHub 工具项目（非 PoC）：https://github.com/bettercap/bettercap/releases/tag/v2.42.0

### 3. 工程 agent 技能与本地控制面板〔本次新补采〕

`mattpocock/skills` 是工程技能集合；Phonebox 把旧 Android 设备变为本地桌面面板。两者是当窗被介绍的项目，不确认首次发布日期。引入 agent 技能前应检查权限、外部调用和数据读取范围；配对控制面板不要在不可信网络裸露。
- X 原帖：https://x.com/Dinosn/status/2124027848058884317 · https://x.com/Dinosn/status/2123991001656385729
- GitHub 工具项目（非 PoC）：https://github.com/mattpocock/skills · https://github.com/ersinkoc/phonebox


## APT / Malware 分析

### 1. Bazuka 安卓恶意框架〔本次新补采〕

ThreatFabric 研究描述一个含 dropper、core 和 23 个模块的 Android 框架，支持覆盖层、键盘记录、短信／验证码窃取及远控，控制面板还把 LLM 用于受害者筛选。公开研究未把它归到已知 APT，不根据俄语 UI 直接归因。

狩猎重点：伪装 TikTok 的非官方 APK、异常辅助功能授权、无线调试／ADB 状态变化与可疑覆盖层。包名只能作为线索，需结合签名、哈希与行为。可核证的 C2 与 26 个样本哈希见 IoC 节；部分服务器在研究时已离线，不把旧 IP 命中当确定入侵。
- 当窗 X 证据时间：2026-11-21 10:56:58 HKT（香港）。
- X 原帖：https://x.com/Dinosn/status/2123973917366792659
- 厂商／官方公告：https://www.threatfabric.com/blogs/bazuka-the-fraud-framework-that-can-do-it-all
- 文章／研究：https://thehackernews.com/2026/11/bazuka-android-malware-uses-fake-screen.html

### 2. FBI／NCIC 疑似入侵调查〔11-22 已补收；本次校正证据措辞〕

当窗媒体援引知情人士称 FBI 调查 NCIC 疑似入侵；**报道时 FBI 未公开确认**。入口、时间、失窃与可用性影响均未知，不能写成“全国警方数据库已被盗”。与此前 FBIJobs／PeopleSoft 事件暂无公开证据关联，不拼接成同一攻击链。
- 当窗 X 证据时间：2026-11-21 22:34:41 HKT（香港，Dinosn 帖）。
- X 原帖：https://x.com/Dinosn/status/2124149503766962388 · https://x.com/vxunderground/status/2123976187516952869
- 文章／研究：https://www.bleepingcomputer.com/news/security/fbi-reportedly-hacked-again-this-time-targeting-nationwide-police-database/

### 3. Bell “agentic” 入侵持续传播〔重复但重大跟进：保留调查边界〕

本窗多条 X 帖继续讨论 Bell 企业客户信息外泄，但没有找到新增官方归因或公开 IoC。主事实归入 11-20 补刊，不把每条转述算一宗新事件；仍需警惕冒充 Bell 的社工。此处只保留跨日跟踪，不声称本日有新调查结论。
- X 原帖：https://x.com/f1tym1/status/2124012312667345393
- 文章／研究：https://www.bleepingcomputer.com/news/security/bell-canada-says-agentic-hacker-stole-enterprise-customer-data/


## SecureFlow 信息流精选

**采集失败／无法追溯，不是“本日无显著更新”。** all、community、blog 三路各首试及换浏览器 UA＋站点 Referer 重试仍 HTTP 522；未取得当前分类源目录。另用 11-05 的实际缓存目录，对 **community 7 源、blog 12 源，共 19 源**逐一只读拉取，每个源两次均 522。历史目录可能已变，不能把这些当成当前完整源集合。

- community：先知、奇安信、Seebug、t00ls、吾爱破解、InfoSec Write-ups、Critical Thinking 等已知源均失败，窗口内数量 **未知**。
- blog：历史目录 12 源（含长期旧源也做了尝试）均失败，48 小时及 7 天补充范围均 **无法筛选**。
- BugBounty：无法从 all 取得 HackerOne 等当窗记录，数量 **未知**。
- 已通过 X／官方研究恢复的内容放在对应节；它们不是 SecureFlow 采集成功的替代证明。失败证据：独立 backfill 中 `sf-*.meta.json`、`sf-cached-sources.json`。接口地址见末节。

## AI/TLDR 动态

回溯可恢复 **7 条独特链接**，其中 security **0 条**。这里按 `published` 落入本刊窗（均是日期标签的 00:00 UTC）归档；**原 routine 用 updated 的 24–36 小时窗口**，但当前 feed 和 11-22 缓存的 updated 随构建整体刷新，无法恢复 11-20／21 首次 updated、当时排序与完整候选。不能把这些数称作当日原始快照总数。未来改期／删除／被挤出的条目仍可能缺失。

本日主线是量化和 Transformers 工具更新、PC XT 展示、收购传闻及数学证明话题。security 类为 0 只是本恢复集合的分类计数；不能据此断言当天没有 AI 安全新闻。详情页全部在换 UA＋Referer 后仍 403，以下依据 Atom 标题／摘要。

### 工具与开源

- 〔本次新补采〕 **ClawDOS — a Claude coding agent running on a 4.77 MHz IBM PC XT**：ClawDOS 展示在 4.77 MHz IBM PC XT／DOS 上调用 Claude 编码；是展示，不是模型本地跑在 8088 上。 链接（403，摘要可读）：https://ai-tldr.dev/releases/ricapar-clawdos/
- 〔11-22 已补收〕 **LookAtMyQuant — Inkling 2 Mini squeezed into 5.4 GB for Apple Silicon**：LookAtMyQuant 宣称把 Inkling 2 Mini 量化到 5.4 GB，面向 Apple Silicon；本次未复现性能或精度。 链接（403，摘要可读）：https://ai-tldr.dev/releases/shinmegamiboson-lookatmyquant-inkling-2-mini/
- 〔11-22 已补收〕 **Transformers v5.24.0 — Omnilingual ASR, Inkling 2 Mini and one cache name**：Transformers 5.24.0 的订阅摘要列出 Omnilingual ASR、Inkling 2 Mini 与统一 KV-cache 参数命名。 链接（403，摘要可读）：https://ai-tldr.dev/releases/huggingface-transformers-5-24-0/

### 论文与研究

- 〔本次新补采〕 **Riemann Hypothesis proof certified — Lean checks Alpöge and Claude's proof**：订阅源声称 Lean 专家及多种检查器确认 Alpöge／Claude 的黎曼假设证明；本次未读取原始证明或联合声明，**不可据此宣布数学界已公认问题解决**。 链接（403，摘要可读）：https://ai-tldr.dev/releases/lean-mathlib-riemann-hypothesis-proof-certified/

### 行业与评论

- 〔11-22 已补收〕 **RUMOR — FT: Amazon nears a $7.5B deal to buy Decart**：【传闻】订阅源转述 FT：Amazon 接近以 75 亿美元收购 Decart；未获当事方公告，不写成已成交。 链接（403，摘要可读）：https://ai-tldr.dev/releases/amazon-decart-acquisition-rumor/

### 视频与展示

- 〔本次新补采〕 **Wes Roth — 'AI just BROKE SaaS...'**：Wes Roth 展示用 Codex 自建视频编辑工具替代订阅；只记用例，不把演示推广为普遍成本结论。 链接（403，摘要可读）：https://ai-tldr.dev/releases/wes-roth-ai-broke-saas-codex-video-editor-nov21/
- 〔本次新补采〕 **Wes Roth — 'Claude JUST solved the Riemann Hypothesis...'**：Wes Roth 讲解 Claude 辅助黎曼证明的声称和反响；视频不构成证明成立的独立证据。 链接（403，摘要可读）：https://ai-tldr.dev/releases/wes-roth-claude-riemann-hypothesis-nov21/


## Agent 用例动态

按 RSS pubDate 归属本窗，链接去重后 **20 条，全部列出**。当前 RSS 有 60 条；11-22 原始 XML 实为 60 个 item／60 个独特链接（旧解析文件误记 120）；两份不同时点的 feed 合并为 72 个独特链接。11-20 可恢复 18 条（其中 3 条仅在 11-22 缓存），11-21 为 20 条。原 11-22 解析文件的“66 条新条目”实际上只有 33 个独特链接、每条重复两次；本刊按原 XML／链接去重修正计数，不改写原刊。

主线是办公、营销、招聘和出行；退款、竞价、发票邮件和登录态跨服务操作最值得检查权限。20 条中 15 条已在 11-22 选录，现归档回本窗，另外 5 条本次首次展开。这些只是别人发布的用例，不是本任务在真实账户上执行它们的授权。

### 权限与安全

- 〔11-22 已补收〕 小型 SaaS 作者用 Zapier Agents 拉取 Stripe 信息、检查 Google Docs 退款政策并发送确认，限小额退款；这是他人的用例，不是本任务授权退款。 https://agentusecases.ai/use-case/process-small-refund-requests-automatically-with-a-zapier-ag
- 〔11-22 已补收〕 用户用 Claude in Chrome 访问 Outlook、向 Gmail 同步日程并整理邮件；涉及完整登录会话和跨服务复制权限。 https://agentusecases.ai/use-case/sweep-email-and-sync-calendars-each-morning
- 〔11-22 已补收〕 用户把 Home Assistant 实体与 YAML 配置放入 Gemini Gem，辅助生成智能家居代码；配置导入前应移除密钥和家庭敏感信息。 https://agentusecases.ai/use-case/build-a-home-assistant-expert-agent-from-your-config
- 〔11-22 已补收〕 用户称 Claude 构建扫描 eBay、比较历史价格和利润并自动竞价的应用；涉及真实支出，应设置限额与逐笔授权边界。 https://agentusecases.ai/use-case/auto-bid-on-sports-cards-on-ebay
- 〔11-22 已补收〕 用户用 Claude Code／Cowork 监视 Xero 发票从 draft 变 authorized 后存 PDF 并发客户；应用内 authorized 不一定代表用户授权 agent 对外发信。 https://agentusecases.ai/use-case/email-authorized-xero-invoices-to-clients-automatically

### 编程与工程

- 〔11-22 已补收〕 Show HN 展示 ClawDOS 在 DOS 上运行编码 agent；摘要细节有限，不声称模型本地推理。 https://agentusecases.ai/use-case/run-an-ai-coding-agent-on-dos

### 办公与研究

- 〔11-22 已补收〕 用户以 Make agent 分类询盘、拟答复、向 Slack 报紧急事项；另一个模块负责发信，区分“拟稿”和“发送”。 https://agentusecases.ai/use-case/classify-and-reply-to-customer-inquiries-with-an-ai-agent
- 〔11-22 已补收〕 SaaS 团队用 Claude 驱动的 Lindy 找线索、拟个性化触达；每月 40 多场会议是供应商来源主张。 https://agentusecases.ai/use-case/find-leads-and-personalize-first-outreach
- 〔11-22 已补收〕 Lindy 监测 YouTube 评论、筛选和补充线索，再发送到 Slack 或 CRM；需注意数据使用与外发范围。 https://agentusecases.ai/use-case/spot-youtube-comment-leads-and-send-to-crm
- 〔11-22 已补收〕 用户让 Claude 修改 B2B 合作外联措辞，声称回复率改善；仅记录其经验，不替其发信。 https://agentusecases.ai/use-case/draft-b2b-partnership-outreach-emails-that-don-t-sound-like-
- 〔本次新补采〕 营销人员用 Claude Code／Cowork 做竞品研究、博客／落地页和社媒回复草稿。 https://agentusecases.ai/use-case/run-marketing-research-content-and-campaigns-with-claude
- 〔本次新补采〕 用户经 MCP 连接 Meta、Google、TikTok 广告数据，让 Claude 生成报告与建议，未说明自动投放。 https://agentusecases.ai/use-case/generate-ad-reports-and-recommendations-from-ads-data
- 〔本次新补采〕 用户的 Claude Code skill 研究竞品／社区并在 Excel 中形成跨平台帖子和短片计划。 https://agentusecases.ai/use-case/build-a-researched-monthly-social-media-calendar
- 〔本次新补采〕 团队为房地产经纪开发定时发布 agent，并处理 Meta API 权限变化和重试；平台许可不是一次设置后永远有效。 https://agentusecases.ai/use-case/run-a-realtor-s-facebook-page-with-a-scheduling-agent
- 〔11-22 已补收〕 招聘人员用连接 ATS 的 Claude 查信息、拟经理 intake 和电话筛选材料；注意候选人隐私。 https://agentusecases.ai/use-case/query-the-ats-and-draft-intakes-and-phone-screens
- 〔11-22 已补收〕 创始人把职位描述给 Claude，用于找候选人和起草个性化招聘触达。 https://agentusecases.ai/use-case/draft-personalized-recruiting-outreach-and-find-candidates
- 〔11-22 已补收〕 用户用 Spellbook、CoCounsel 初筛常规合同，再决定是否请专门律师，不把工具替代专业判断。 https://agentusecases.ai/use-case/spot-issues-in-routine-contracts-with-legal-ai-tools

### 出行与个人事务

- 〔11-22 已补收〕 用户称 Claude 协助热量、健身、餐单、每周采购及家庭事务规划。 https://agentusecases.ai/use-case/run-fitness-meal-planning-and-weekly-shops
- 〔11-22 已补收〕 作者测试 Meta Muse 等旅行预订 agent；一例卡在人工验证并请求协助，不能写成已成功出票。 https://agentusecases.ai/use-case/book-travel-with-an-ai-agent
- 〔本次新补采〕 供应商演示 agent 三分钟内规划 Dulles–Barcelona 往返和七晚住宿，以 dry run 检验可预订性；不是已付款预订。 https://agentusecases.ai/use-case/plan-and-price-a-full-trip-through-a-booking-cli


## 周末：阮一峰周刊精选

本刊按原规则归档第 420 期《最分心的一年》。**11-22 已补收周刊及部分精选，本次不是新一期**；本次完整提取正文所有 14 个独特 GitHub 项目链接（排除 ruanyf/weekly 自身与投稿 issues），并列 7 篇专题／文章。工具“netboot.xyz”在正文不是 GitHub 地址，不计入 14 个项目。

周刊原文（200）：https://www.ruanyifeng.com/blog/2026/11/weekly-issue-420.html

### GitHub 项目

- 〔11-22 已补收〕 **sgrep**：语义代码搜索，需注意索引内容和嵌入数据的保存位置。 https://github.com/arunsupe/semantic-grep
- 〔11-22 已补收〕 **Netdata**：集中展示服务器与服务状态的开源观测仪表板。 https://github.com/netdata/netdata
- 〔11-22 已补收〕 **FlowVision**：macOS 瀑布式图像浏览器。 https://github.com/netdcy/FlowVision
- 〔11-22 已补收〕 **13ft**：可自托管的网页读取工具；遵守内容访问与版权约束，本刊不提供绕过步骤。 https://github.com/wasi-master/13ft
- 〔11-22 已补收〕 **Srcbook**：适合 TypeScript／JavaScript 的交互式笔记本。 https://github.com/srcbookdev/srcbook
- 〔11-22 已补收〕 **Photoshot**：浏览器图片编辑器。 https://github.com/Abraham721/photoshot
- 〔11-22 已补收〕 **XJY Editor**：表格形式编辑 XML、KML、JSON 与 YAML 的静态网页应用。 https://github.com/lizhaowu-79/xjyeditor
- 〔11-22 已补收〕 **GCS**：非官方 Google Cloud 命令行工具；授权前审查云权限。 https://github.com/aeroxy/google-cloud-shell-cli
- 〔11-22 已补收〕 **Waytrace**：后台记录足迹的 iOS 应用，涉及位置隐私。 https://github.com/lxyeternal/PathTracker
- 〔11-22 已补收〕 **Tomoru**：捕获指定音频并输出双语浮动字幕，注意录音与旁人隐私。 https://github.com/ACAne0320/Tomoru
- 〔11-22 已补收〕 **crFiles**：跨平台文件管理器，集成 Android Quick Share。 https://github.com/libcr/crFiles/releases
- 〔11-22 已补收〕 **Arke**：将读取、排序、缩略图和搜索移出 UI 线程的 Windows 文件管理器。 https://github.com/Koimsurai/Arke
- 〔11-22 已补收〕 **tinybrain**：从数据清洗到预训练、SFT、蒸馏、强化学习的中文小模型教学实现。 https://github.com/cai114514114514/tinybrain
- 〔11-22 已补收〕 **Lean Init IDE**：浏览器 Lean 4 学习环境及中英课程。 https://github.com/3y3y3y-huaiji/lean-init-ide

### 有趣文章／专题

- 〔本次新补采〕 **年度回顾**：【AI agent】多项目并行并不增加总时间，应聚焦最重要的工作。 https://alejandro-ao.com/blog/one-year-at-hugging-face/
- 〔11-22 已补收〕 **黄仁勋事件的深层分析**：周刊推荐的行业分析；涉及付费文章时只记录周刊推荐，不声称读完付费全文。 https://stratechery.com/2026/obituaries/
- 〔11-22 已补收〕 **多智能体系统的三种模式**：【AI agent】管道、编排器、白板三类协作模式。 https://kadhar.dev/blog/multi-agent-systems-from-scratch
- 〔11-22 已补收〕 **检查空格有多难？**：【工程／安全】Unicode 空白字符与跨语言过滤差异。 https://serce.me/posts/2026-10-30-how-hard-is-it-to-check-for-whitespace
- 〔11-22 已补收〕 **闭源模型占据了主导地位**：价格—性能前沿比较，属于当时的分析结论。 https://village.dev/blog/closed-ai-models-now-dominate-the-price-performance-frontier/
- 〔11-22 已补收〕 **个人如何定制芯片**：个人芯片设计与流片服务经验。 https://essenceia.github.io/projects/expresso/
- 〔11-22 已补收〕 **AI 芯片的位置验证**：【安全／政策】芯片定位要求及操作系统协作的讨论。 https://spectrum.ieee.org/find-my-ai-chip

## 地址／IoC 汇总

### Bazuka（ThreatFabric 原样摘录）

来源：https://www.threatfabric.com/blogs/bazuka-the-fraud-framework-that-can-do-it-all

研究说明在 **2026 年 10 月下旬**发现；本次核验时间见报告头（HKT）。下列地址按源文格式原样保留，不变成可点击攻击链接。研究时 `95.181.213.21` 已离线、另一个仍响应；这是历史观察，不能当作补采时的实时存活状态。

- `95.181.213[.]21`
- `170.168.61[.]117`
- `gargona[.]cash`
- 包名线索：`com.tiktok.premium`、`com.tiktok.premium.pro`；需与签名／行为交叉，不能仅凭包名认定恶意。

公开 SHA256（Appendix File hashes，26 个，原样抄录）：

| 组件 | SHA256 |
|---|---|
| Dropper/Downloader | `4d572669d6000304a692874c1583021dfdb4f2f113ea487e470f7e4c486e503a` |
| Dropper/Downloader | `f046b50166c8229b49839eeebcc7fd14bf3f198e4ec1bfde8a5b271e1407dec5` |
| The Core | `3cb8711a51331123247476eef768c435d6286a21cd8ac5479a6276349632c82b` |
| call_forwarding.dex | `c08a5f3df1693b03540db8c6c001b5e7f98ea6121ad4aca9c6904c798f4f4635` |
| clip_monitor.dex | `84849921d229c4e6c1a43af86582bff7560e938e96ad8b01b0ff13dafe559757` |
| contacts.dex | `ffc35c48d8a5cb1ee3e5bdc80e0df3e8509e8dd840edd0b9fb0ff5d5880834d0` |
| device_control.dex | `3da80bbcf6c6e7ff117db4cdfe1422375ecf1db97b61574359f97a1da43566ae` |
| file_manager.dex | `7361a1ad372367dfc11421385632586da4aaf164c41f67e0acb2ccdb7931e3c1` |
| input_recorder.dex | `910911b7d1be3f67c926067e923ba86be6100366e52f0fe30484176353bf1701` |
| location.dex | `38bf5b694512cf14620edc0af700c08e7570fa5a20b4c3c052c7fe8823b2ec5f` |
| media.dex | `b97b3ca1fdce56ae41418b287ca0e97d93ea16ec7b9182bdde459bba8b09f661` |
| oem_power.dex | `d0fc542db2602d3a881c825c4d58e5ae34db054496d64c9185a84dceab30a850` |
| optics.dex | `5cf38406fbed48fe110bcf1e84314429e1f649a2539c00b78216a5808fb53aa0` |
| preflight.dex | `de97f4864e94eb9fecd018d51c36fc0a2e0d3a67e9bb83ab0e5ac29ad101f292` |
| proxy.dex | `b7987e06d515fa06751a014a034b680f5a2c185bf0eb1fcf76c29b8626527d53` |
| push.dex | `2cc693857f47758e974c3ee928a4fe0fdba444b7efe5a284dcfc0d3b47429275` |
| screen_control.dex | `4dcad3a1547c72d08ccb86dc393e14935c7f06ebe3ca63ba30e51b98ab4930e1` |
| self_adb.dex | `1c29e14001edcfc548e1ae43572aa17f91ad89ce09a0e9028737077d7af97d30` |
| session_ui.dex | `d0ba986440b06c4b587690acd3e594cc674c82408cd4f5c59c7f6675a2b4d9c0` |
| smsmessage.dex | `0785f8ca820ccfb62be61ac4bd55fd5295a771cab9e4cd91fc4eb1e3c43af3db` |
| system_checker.dex | `ac57a003ad4464ac357ae78e8e4eb24aae9d8442545129f82ad683efa1b2ad99` |
| tapread-nfc_module.dex | `5be63e04a98988d8d15d12cdf2af8cd6b1b6b8681e511587bb1a22ebcb32583f` |
| toast.dex | `ac34c61cb7368ba4409311a7492bf14316e1cee1f2984955005915d6ec7336f3` |
| twofa.dex | `c181d5c6c098f9f4ac6b10e4b1d69a0278bb3e07f260d0013244113c8504f39a` |
| uninstall_shield.dex | `adf9a4689e4c178a8c8fedef5e0bdf7be6ab443264125efabfadd8e1594bd471` |
| ussd.dex | `8ee9d88db8874662c7743bb0f7d06e852c372b2bdb1846a12afb71a62b8f0a7b` |

### 其余

Cairn 的 2 个历史地址见 11-20 补刊；两日都可用 AWS 原文核对：https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/

Entra、FBI／NCIC 未公开可核证攻击 IoC；不把管理员邮箱、受害租户元数据或系统证书当成可传播指标。本刊没有复制利用载荷、命令或步骤。

## LWiS 固定信源

- X List（只读）：https://x.com/i/lists/1239330068461244424
- 固定博客清单：https://blog.badsectorlabs.com/files/blogs.txt （现有本地副本 `lwis-sources/blogs.txt`，只作选源，不声称全部博客当日都已抓取）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/
- Risky Business：https://risky.biz/ ；tl;dr sec：https://tldrsec.com/ （保留为原有备援，本次未冒充完成这两站历史全量）
- SecureFlow 三路、pwn.watch、ExploitGrid、AI/TLDR、AUC 与周六周刊接口见下节。

## 来源搜索 URL

### 方法与覆盖

X 为当日原帖的**事后历史检索**，Latest 即 `sort_order=recency`；同时做 relevancy 和带补丁／公告／互动词的高信号补搜。每组工具实际最多返回 25 条；不把最早到最晚的跨度说成该跨度内每帖全量覆盖。LWiS 则从当前列表连续往回分页，直到越过 11-19 23:00 UTC；8 页共 695 条、跨两日窗口 428 条。删除／受限帖、当时的列表成员和排序不可恢复。

本窗：独特 X 候选 276，LWiS 157；List 最早／最晚实际帖子为 2026-11-20T23:00:37.000Z 至 2026-11-21T22:38:42.000Z（UTC 原始证据；同区间香港为 11-21 07:00:37 至 11-22 06:38:42 HKT）。这是当前可见帖子范围，不是失败 run 快照。

| X 查询组 | 实得条数 | 原始 created_at 区间（UTC；香港加 8 小时） |
|---|---:|---|
| 21-cve-high.json | 25 | 2026-11-21T00:05:18.000Z → 2026-11-21T21:42:44.000Z；香港 11-21 08:05:18 HKT → 11-22 05:42:44 HKT |
| 21-cve-latest.json | 25 | 2026-11-21T22:52:35.000Z → 2026-11-21T22:59:54.000Z；香港 11-22 06:52:35 HKT → 11-22 06:59:54 HKT |
| 21-cve-relevancy.json | 25 | 2026-11-21T00:58:12.000Z → 2026-11-21T22:25:09.000Z；香港 11-21 08:58:12 HKT → 11-22 06:25:09 HKT |
| 21-threat-latest.json | 25 | 2026-11-21T18:18:39.000Z → 2026-11-21T22:25:36.000Z；香港 11-22 02:18:39 HKT → 11-22 06:25:36 HKT |
| 21-threat-relevancy.json | 25 | 2026-11-20T23:39:04.000Z → 2026-11-21T22:25:36.000Z；香港 11-21 07:39:04 HKT → 11-22 06:25:36 HKT |
| 21-tools-latest.json | 2 | 2026-11-21T09:02:05.000Z → 2026-11-21T16:20:20.000Z；香港 11-21 17:02:05 HKT → 11-22 00:20:20 HKT |

- X 搜索：https://x.com/search?q=%28CVE%20OR%20POC%20OR%20exploit%20OR%200day%29%20-is%3Aretweet%20since%3A2026-11-20_23%3A00%3A00_UTC%20until%3A2026-11-21_23%3A00%3A00_UTC&f=live

- X 搜索：https://x.com/search?q=github.com%20%28C2%20OR%20%22red%20team%22%20OR%20nuclei%29%20-is%3Aretweet%20since%3A2026-11-20_23%3A00%3A00_UTC%20until%3A2026-11-21_23%3A00%3A00_UTC&f=live

- X 搜索：https://x.com/search?q=%28%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%29%20-is%3Aretweet%20since%3A2026-11-20_23%3A00%3A00_UTC%20until%3A2026-11-21_23%3A00%3A00_UTC&f=live

### 指定信源逐一结果

| 信源／读取地址 | 本次证据与数量 | 缺口 |
|---|---|---|
| SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 | 两次 HTTP 522 | 无法追溯，条数未知，不记 0 |
| community：https://secureflow.scope-sentry.top/api/rss/category?category=community | 两次 522；历史已知 7 源逐一请求亦失败 | 不能恢复当前源目录与 48h 内容 |
| blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog | 两次 522；历史已知 12 源逐一请求亦失败 | 不能恢复当前源目录与 7d 首见内容 |
| pwn.watch：https://pwn.watch/feed.xml ／ https://pwn.watch/feed.json | 两种格式均 200；RSS 50 条／JSON 50 条（相同条目，不相加），最新香港 11-09 04:19:52（源文 11-08 20:19:52 GMT）；目标窗匹配 0 | 仅能证明当前与缓存状态；无当日快照 |
| ExploitGrid：https://api.exploitgrid.net/api/exploits?page=1&limit=100 | 页 1–3 共 300 条，已越过两日共同起点；目标窗见下 | 索引收录不等于有效 exploit，数据可能滞后 |
| ExploitGrid KEV：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines | 200，10 条当前 active deadline | 不能用当前 active 列表恢复已过期期限；另查 CISA 全目录 |
| CISA：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json | 200，1790 条，dateAdded=11-20 有 4 条、=11-21 为 0 | 日期字段不是小时级历史快照 |
| AI/TLDR：https://ai-tldr.dev/feed.xml | 当前 50 entry，与 11-22 缓存合并 55 独特链接；本窗归属见正文 | updated 历史不可恢复；全部目标详情页 403 |
| AUC：https://agentusecases.ai/feed.xml | 当前 60 item，缓存 60 item，两个时点按链接合并 72；本窗归属见正文 | 滚动 feed 不保证历史全集；18/20 为可恢复下限 |

ExploitGrid 本窗 0 条，HIGH／CRITICAL 0 条，去重 CVE 数 0。匹配 0 不代表当天全网没有公开研究，最新 API date 仍停在前一日；nginx／Roller 等 X 帖的公开研究事实独立保留。

周刊 Atom：https://www.ruanyifeng.com/blog/atom.xml （200）；第 420 期正文 200，本次提取 14 个 GitHub 项目和 7 篇专题／文章。

### 核验与交付说明

- 主来源 HTTP 状态、最终地址、抓取时间、SHA256 和重试在独立 backfill 的 `*.meta.json`；X ID／作者／created_at／原帖地址保存在 `x-all.json`，各组原始结果独立保存。
- 无 `t.co` 短链接出现在成稿；使用帖实体展开地址。403／400／522 不伪称 200；最终链接抽查台账见覆盖说明及 `report-link-check.json`。HTTP 404 的主链接需替换或删除后交付。
- `2026-11-20_21-backfill-coverage.md` 是跨两刊覆盖与缺口总表。没有修改 seen_ids、last_report_date、profile、技能、routine，未直接外发消息。

最终链接核验：两刊合计 181 个独特 https URL；114 个 HTTP 200、32 个原帖 ID 经 X 工具核验、7 个列表／搜索参考 URL；24 个 403（23 个 AI/TLDR 详情＋1 个 Medium）、3 个 SecureFlow 522 均已注明；AWS Ruby 公告脚本传输中断后由公共 WebFetch 读取核对。没有 404 主链接。检验基于当前可读性，不是当日可用性证明。

Box：`/home/box/workspace/security-watch/reports/2026-11-21-x-security-digest-supplement.md`
本机副本目标：`/Users/kenny1337/Desktop/_05_项目/X安全情报晚报/2026-11-21-x-security-digest-supplement.md`。复制／读回结果以覆盖台账的最终交付状态为准。
