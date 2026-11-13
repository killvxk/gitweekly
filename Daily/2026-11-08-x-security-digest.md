# X 安全情报晚报 · 2026-11-08（周日，周末版）

> 报告时间：2026-11-08 约 20:05（America/Santiago）＝ 2026-11-09 约 07:05（香港时间）。
> **覆盖时长**：X Latest 搜索覆盖约 2026-11-07 08:00 UTC～11-08 23:05 UTC（CVE 高互动补搜自 11-07 08:00 UTC；其余自 11-08 00:00 UTC，均为只读）；LWiS X List 实际取到 96 帖，覆盖 11-08 03:08～22:10 UTC（约 19 小时，List 接口一次最多返回这些，未做翻页）。SecureFlow 取近 48 小时（blog 放宽 7 天）。X 搜索被 CVE 机器人账号大量刷屏，已用「relevancy + 排除机器人」补搜。
> **验收说明**：全部通过（链接抽查：核验时 insinuator 原链接 404 已替换为正确地址，ZDI 改 https；thehackerwire 403 已注明；X 原帖未逐条打开，仅抽查 2 条返回 200）（forum.butian.net 属 box 网络无法连接，浏览器可开；本期 SecureFlow 的 all/community 无新增是接口真实结果，见末节）。
> 公开备援：CISA KEV 最新入库 2026-11-06（CVE-2026-19868，已在 11-06/11-07 期报道，本期仅作跟进）。

## 今日摘要

- **Web/框架**：Craft CMS 4.x/5.x 未授权 SQL 注入 CVE-2026-123488 已有公开 PoC（尚未入 KEV、无已知在野利用）；WordPress 补丁自身升级窗口仍可被利用（CVE-2026-119977，Picus 研究员发现，建议升级前封禁 wp-content/upgrade 的 Web 访问）；s2Member 未授权 RCE（CVE-2026-86596）有公开利用报道。
- **React Server Components**（GHSA-xqc2-xf4c-x3h3，CVSS 4.0 9.5，无 CVE）：Next.js 16.0.0–16.4.0 需升级到 16.4.1；react-server-dom-* 升到 19.0.9 / 19.1.10 / 19.2.9 / 19.3.1。
- **威胁研究**：Talos 披露 VOLTA 窃密木马，被盗数据交给 LLM（经 OpenRouter）做「受害者估值」；Hunt.io 追踪 ARTEX（AI 自动化渗透框架）与韩国 7 家金融机构数据泄露；PandaRE 发布《Operation Snowball》——公开目录里的自治 AI 入侵行动。
- **AI 与安全交汇**：Apiiro：Claude Code「不再询问」产生的配置把口令写进 1,122 个公开 GitHub 文件；OpenAI 聘用 Hacktron 做第三方集成红队。
- SecureFlow：all/community 本窗无新增条目；blog 新增 23 条（均为 ZDI 公告，含 Docker Sandboxes RCE、Philips Hue Bridge Pro、LibreOffice dBase），BugBounty 新增 5 条。

## CVE / POC / 漏洞

**1. Craft CMS 未授权 SQL 注入 CVE-2026-123488（4.0.0–4.18.8、5.0.0–5.11.1；修复 4.18.9 / 5.11.2）**
- X 原帖：[SecAlertsCo](https://x.com/SecAlertsCo/status/2119425987607777333)
- 厂商公告/NVD：[GHSA-qcvp-ggx3-97r6](https://github.com/craftcms/cms/security/advisories/GHSA-qcvp-ggx3-97r6) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123488)
- 文章：[RescuePHP](https://rescuephp.com/news/craft-cms-4-18-9-5-11-2-unauthenticated-sql-injection-cve-2026-123488)；[Tuskira](https://www.tuskira.ai/advisories/cve-2026-123488)（称 11-06 已有公开 PoC，仅 MySQL/MariaDB，无在野利用报道）
- 处置：升级后检查 users 表是否出现意外 admin、密码哈希是否被改。

**2. WordPress 核心 CVE-2026-119977：安装修复时的最后一次暴露窗口**（WordPress 4.7–7.1.3；7.1.4 起修复；CISA KEV 11-03 入库）
- X 原帖：[Kasspar256 转述](https://x.com/Kasspar256/status/2119286148551819384)；[SCMagazine](https://x.com/SCMagazine/status/2119204502628696075)
- 文章：[The Hacker News](https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html)
- NVD：[CVE-2026-119977](https://nvd.nist.gov/vuln/detail/CVE-2026-119977)
- 要点：升级包用旧代码解压，临时目录名一次性可预测；研究员建议更新前先封禁 wp-content/upgrade 的 Web 访问。

**3. React Server Components 未授权 RCE GHSA-xqc2-xf4c-x3h3（CVSS 4.0 9.5，无 CVE）**
- X 原帖：[vysecurity 转 UpwindMDR](https://x.com/vysecurity/status/2119477546979086385)
- 厂商公告：[React 官方 Advisory](https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3)
- 文章：[Upwind 分析](https://www.upwind.io/blog/ghsa-xqc2-xf4c-x3h3-what-the-react-server-components-typed-array-rce-means-for-your-next-js-apps)；[Hash Security](https://hash-sec.com/blog/the-use-cache-rce-how-a-typed-array-bug-in-nextjs-became-remote-code-execution)
- 要点：触发条件窄（`use cache` 返回多个 typed array），无已知在野利用；升级 `next` 本身，仅升 `react` 不够。

**4. s2Member（WordPress 插件，≤260927）未授权 RCE CVE-2026-86596，CVSS 9.8**
- X 原帖：[SecAlertsCo](https://x.com/SecAlertsCo/status/2119552016242339976)
- NVD：[CVE-2026-86596](https://nvd.nist.gov/vuln/detail/CVE-2026-86596)（状态 Deferred，来源 Wordfence）
- 汇总页：[SecAlerts](https://secalerts.co/vulnerability/CVE-2026-86596)

**5. nginx map 指令堆溢出 CVE-2026-42533**（NVD 2026-07-15 发布，11-03 更新）
- X 原帖：[xer0dayz](https://x.com/xer0dayz/status/2119475155927728479)（帖中称「公开可绕 ASLR 的利用代码」，属厂商营销口径，**未独立核实**）
- NVD：[CVE-2026-42533](https://nvd.nist.gov/vuln/detail/CVE-2026-42533)（F5：需 regex map 且变量引用顺序特定，利用依赖攻击者不可控条件）
- 文章：[Sn1per 检测页](https://sn1persecurity.com/wordpress/cve-2026-42533-nginx-map-heap-overflow-detection-with-sn1per/)

**6. 边缘设备 PoC 流水账（机器人账号汇总，信息有限）**
- TOTOLINK CA300-PoE CVE-2026-123961（CVSS 9.9）：[TheHackerWire](https://x.com/TheHackerWire/status/2119437284454072757) · [详情](https://www.thehackerwire.com/vulnerability/CVE-2026-123961/)（该站对脚本返回 403，换 UA+Referer 后仍 403，浏览器可开）
- WAVLINK WN551X3-A CVE-2026-120345：[SecAlertsCo](https://x.com/SecAlertsCo/status/2119489513659506896) · [详情](https://secalerts.co/vulnerability/CVE-2026-120345)

**7. SonicWall SonicOS SSLVPN CVE-2026-19868（KEV 11-06，期限 11-20）跟进**
- X 原帖：[richtechguy](https://x.com/richtechguy/status/2119464160388145219)
- 文章：[BleepingComputer](https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-new-ssl-vpn-mfa-bypass-flaw-exploited-in-attacks/)
- 厂商公告：[CISA KEV 公告](https://www.cisa.gov/news-events/alerts/2026/11/06/cisa-adds-one-known-exploited-vulnerability-catalog) · [加拿大网络安全中心 AV26-1133](https://www.cyber.gc.ca/en/alerts-advisories/sonicwall-security-advisory-av26-1133)
- 要点：密码即可绕过 SAML/MFA（任一单因素路径仍开启时）；Gen7/Gen8 升级到补丁版本。

**8. Docker 不是安全边界：ZDI-26-894（Docker Sandboxes，远程代码执行）**
- X 原帖：[kmkz_security 转 vortexau](https://x.com/kmkz_security/status/2119531596428763618) · [kmkz_security 转 mdisec](https://x.com/kmkz_security/status/2119530299520422024)
- 厂商/ZDI 公告：[ZDI-26-894](https://www.zerodayinitiative.com/advisories/ZDI-26-894/)
- 文章/研究：[licht-jb 对 CVE-2026-112691 的写作与 PoC（经 patrickwardle 转发）](https://x.com/patrickwardle/status/2119401866681311358) → [原文](https://licht-jb.github.io/posts/cve-2026-112691.html)（仅列链接，未摘录利用细节）

## 工具与 GitHub 发布

- **Malspark**：开源多智能体恶意软件分析平台（多个 AI 分析员取证、互相辩论、由「裁判」给出结论）。X：[Root0ne](https://x.com/Root0ne/status/2119488201916305410)；GitHub：[Root0ne/Malspark](https://github.com/Root0ne/Malspark)；官网：[malspark.com](https://malspark.com)
- **AI 渗透测试智能体框架清单**（fr0gger_ 汇总，公开仓库，防御/研究向参考）：X：[fr0gger_](https://x.com/fr0gger_/status/2119284443043213645)；GitHub：[Cairn](https://github.com/oritera/Cairn) · [CyberStrike](https://github.com/CyberStrikeus/cyberstrike) · [PentAGI](https://github.com/vxcontrol/pentagi) · [CyberStrikeAI](https://github.com/AIPentest/CyberStrikeAI) · [PentestGPT](https://github.com/GreyDGL/PentestGPT) · [PentestAgent](https://github.com/GH05TCREW/pentestagent) · [AutoPentester](https://github.com/YasodGinige/AutoPentester)
- **LLM 辅助漏洞研究（ZephrFish）**：X：[404death 转发](https://x.com/404death/status/2119297700017611090)；文章：[Bullying LLMs](https://blog.zsec.uk/bullyingllms/) · [Harnessing Harnesses](https://blog.zsec.uk/harnessing-harnesses/)
- **Phrack 49《Smashing the Stack for Fun and Profit》30 周年**：X：[phrack](https://x.com/phrack/status/2119473057584783850) · [thegrugq 转发](https://x.com/thegrugq/status/2119532812521086982)
- 无显著新的 nuclei / C2 开源发布（X 上 github.com + C2/red team/nuclei 搜索本窗无高质量结果）。

## APT / Malware 分析

**1. VOLTA（VOLTA-AUTODOXER）窃密木马：用 LLM 给受害者估值**（Cisco Talos）
- X 原帖：[fr0gger_](https://x.com/fr0gger_/status/2119545318526312917) · [fr0gger_ 报告链接帖](https://x.com/fr0gger_/status/2119546226471567730)
- 文章：[Talos 博客](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/)
- 要点：自删除 Windows 窃密木马，窃取浏览器凭据/Cookie/支付卡/钱包/Discord/Telegram/Steam/Roblox/Microsoft OAuth/SSH 与云密钥/Wi-Fi 配置；随后把「证据包」POST 给 OpenRouter 的大模型（默认 anthropic/claude-opus-4.6，被拒绝则回退 moonshotai/kimi-k2 → google/gemini-2.5-flash，temperature 0.2）。Talos 称无攻击者自有基础设施。IoC 见 IoC 节。

**2. ARTEX：AI 自动渗透框架与韩国金融机构数据泄露**（Hunt.io 追踪）
- X 原帖：[Dinosn](https://x.com/Dinosn/status/2119265657694883876)
- 文章：[Security Affairs](https://securityaffairs.com/202607/ai/inside-artex-ai-hacking-tools-exposed-servers-and-south-korean-bank-breaches.html)
- 要点：9 月底至 10 月初 7 家韩国金融机构被入侵，约 6.6–6.7 万人、约 2,200 家企业数据受影响；CrowdStrike（10-07）与 Genians（10-12）此前已报道，CrowdStrike 以中等把握判断为单一华语个人、出于牟利；主模型 DeepSeek v4.1 Flash，备用 GLM 5.3 与 Grok 4.6。ARTEX 仓库与 Docker 镜像 10-11 被下架，分叉仍在。

**3. Operation Snowball：公开目录里的自治 AI 入侵行动**（Malbear Labs / PandaRE，11-08 发布）
- X 原帖：[domchell 转 PandaRE](https://x.com/domchell/status/2119359512343646572)
- 文章：[Malbear Labs](https://malbearlabs.com/posts/operation-snowball-inside-an-autonomous-ai-intrusion-campaign)（我只读了检索摘要：越狱的 DeepSeek Flash 智能体框架，约两周较少人工监督，针对一家欧洲电信运营商及其托管的 13 家组织；全文未逐段核对）

**4. AI 编码助手泄露口令**（交叉：X / AI/TLDR）
- X：[Dinosn 转帖](https://x.com/Dinosn/status/2119340443615863255)；AI/TLDR：[条目](https://ai-tldr.dev/releases/apiiro-claude-code-dont-ask-again-secrets/)；原始来源：[Apiiro 博客](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) · 相关：[reykur.io](https://reykur.io/blog/ai-coding-assistant-shipping-secrets/)

## SecureFlow 信息流精选

**各分类新条目（窗口 48 小时 / blog 7 天，已排除 seen_ids）**：all 接口 200 条（最早 10-26）中 48 小时内 6 条、其中新条目 5（均为 BugBounty）；community 7 源（吾爱破解 updatedAt 2024 已跳过）新增 0；blog 12 源（含「微信公众号」2025 年已停更，跳过）新增 23；BugBounty 新增 5。

**blog（ZDI-vulnerabilities，11-06 14:00 北京时间发布，23 条 ZDI-26-875～897）**
- 精选：[ZDI-26-894 Docker Sandboxes 远程代码执行](https://www.zerodayinitiative.com/advisories/ZDI-26-894/)；[ZDI-26-891 Philips Hue Bridge Pro SQL 注入 RCE](https://www.zerodayinitiative.com/advisories/ZDI-26-891/) · [ZDI-26-892 认证绕过](https://www.zerodayinitiative.com/advisories/ZDI-26-892/) · [ZDI-26-890 参数注入文件写入](https://www.zerodayinitiative.com/advisories/ZDI-26-890/)；[ZDI-26-895 LibreOffice dBase 解析堆溢出 RCE](https://www.zerodayinitiative.com/advisories/ZDI-26-895/)；[ZDI-26-893 SketchUp SKP 解析 UAF](https://www.zerodayinitiative.com/advisories/ZDI-26-893/)；[ZDI-26-896 Home Assistant Green 明文凭据（Pwn2Own）](https://www.zerodayinitiative.com/advisories/ZDI-26-896/) · [ZDI-26-897 SSRF（Pwn2Own）](https://www.zerodayinitiative.com/advisories/ZDI-26-897/)
- 其余 ZDI-26-875～889（OriginLab Origin Viewer 多种文件解析内存破坏 RCE ×约 12、Quest NetVault Backup DoS ×2、libilbm 堆溢出 RCE）：见 [ZDI 公告索引](https://www.zerodayinitiative.com/advisories/published/)；单条 URL 形如 https://www.zerodayinitiative.com/advisories/ZDI-26-880/。
- 说明：Hue / Docker Sandboxes 在 11-07 期已有简述，本期补全 ZDI 批次。

**BugBounty（HackerOne 公开报告，选 4 条）**
- [Qt .ts 文件 Billion laughs 实体扩展（约 950KB → 约 55MB）](https://hackerone.com/reports/4094236)
- [curl 8.23.0：Alt-Svc: clear 后仍向 HTTP/3 后端发请求](https://hackerone.com/reports/4177724)
- [WordPress Gutenberg 插件 formAction 开放邮件中继（钓鱼风险）](https://hackerone.com/reports/3460138)
- [Trellix healthwatch 站点访问控制失效导致数据暴露](https://hackerone.com/reports/3417759)
- （另有 [MariaDB CLI 工具问题](https://hackerone.com/reports/3849007)，价值较低）

**community**：本日无显著更新（先知、奇安信、Seebug、t00ls、InfoSec Write-ups、Critical Thinking 最新条目均早于窗口或已收录；forum.butian.net 属 box 网络无法连接，浏览器可开）。

**X 之外的其他精选文章（来自 X List，防御向）**
- [Compass Security：在 Microsoft Defender XDR 中监控 AI 智能体](https://blog.compass-security.com/2026/11/security-monitoring-of-ai-agents-in-microsoft-defender-xdr/)（X：[DirectoryRanger](https://x.com/DirectoryRanger/status/2119484477403439547)）
- [Insinuator：Microsoft Entra ID 令牌窃取 第一部分](https://insinuator.net/2026/08/token-theft-in-microsoft-entra-id-part-1-of-4-threat-landscape-and-attack-techniques/)（X：[DirectoryRanger](https://x.com/DirectoryRanger/status/2119483748450484637)）
- [Castles Made of Sand：浏览器沙箱漏洞文章](https://davi-1337.github.io/posts/castles-made-of-sand.html)（X：[daaximus 转发](https://x.com/daaximus/status/2119315190068224153)）

## AI/TLDR 动态

窗口内（updated 近 36 小时）AI/TLDR 订阅源共 6 条，不在 seen_ids 的新条目 2 条，**均为 security 类**（订阅源共 50 条）。主题是 AI 编码助手的口令泄露与 AI 攻防的人才合流。

**安全**
- Apiiro 发现 Claude Code「Don't Ask Again」把已批准命令逐字保存，1,122 个公开 GitHub 文件含真实口令：[AI/TLDR](https://ai-tldr.dev/releases/apiiro-claude-code-dont-ask-again-secrets/) · [Apiiro 原文](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)
- OpenAI 聘用曾用 AI 触及其内部仓库的 Hacktron，持续做红队测试：[AI/TLDR](https://ai-tldr.dev/releases/openai-hacktron-partnership/) · [AI Weekly](https://aiweekly.co/alerts/openai-hires-hacktron-to-red-team-third-party-integrations)

模型 / 工具与开源仓库 / 论文与研究 / 行业动态：本日无显著更新（其余条目已在此前收录）；video 与纯 showcase 0 条计入。

## Agent 用例动态

窗口 48 小时内共 48 条，其中新条目 34 条（已排除 seen_ids），本节挑 22 条。主题：一是 Claude / Cowork / OpenClaw / Grok Bot 这类长驻或定时 agent 被用来跑小企业与副业的日常流程；二是浏览器 agent（ChatGPT Agent、Operator、Claude in Chrome）做订票、比价、填表；三是学生与老师用 Claude/Gemini 做自测与备课；四是投资与财务数据通过 MCP 接入 Claude。**安全相关**：本窗无明确安全主题用例（「通过浏览器控制 MCP 读取被拦截的文章」涉及访问控制边界，仅作提示）。

**长驻 / 定时 agent 与运维**
- 用 Claude Cowork + Claude Code 把小企业的周期工作流交给定时 agent：[链接](https://agentusecases.ai/use-case/run-a-small-business-s-recurring-workflows-with-scheduled-ag)
- 用 OpenClaw 自愈 agent 监控 26+ 个 GitHub PR：[链接](https://agentusecases.ai/use-case/monitor-open-github-pull-requests-with-a-self-healing-agent)
- 用 Grok Bot 管理 Proxmox 家庭实验室：[链接](https://agentusecases.ai/use-case/manage-a-proxmox-homelab-with-grok-bot)
- 把排班、线索抓取等浏览器活交给 Grok Bot 云电脑：[链接](https://agentusecases.ai/use-case/hand-browser-work-like-rostering-and-lead-scraping-to-grok-b)
- 用 Grok Bot 自动处理小任务与客户回复：[链接](https://agentusecases.ai/use-case/automate-small-work-tasks-and-client-replies-with-grok-bot)
- 用 OpenClaw（Mac mini 上的 Clawbot）推进副业：[链接](https://agentusecases.ai/use-case/run-a-side-project-with-an-always-on-ai-agent)
- 让机器人把代码评审委托给 Cursor agent：[链接](https://agentusecases.ai/use-case/have-a-bot-delegate-code-review-to-a-cursor-agent)

**编码与自动化**
- 用 Cursor、Claude 写几乎全部 Ansible，并把经验记录进 CLAUDE.md：[链接](https://agentusecases.ai/use-case/build-ansible-automation-with-claude-recording-lessons-in-cl)
- 用 Claude Code 自建电商小工具替代订阅：[链接](https://agentusecases.ai/use-case/build-custom-store-tools-instead-of-paying-for-subscriptions)
- 用 Claude 写一门实验语言的编译器与运行时：[链接](https://agentusecases.ai/use-case/build-an-experimental-language-compiler-with-an-llm-coder)
- 把 agent 写的 diff 重新敲一遍来吸收新功能：[链接](https://agentusecases.ai/use-case/retype-agent-written-diffs-to-internalize-new-features)

**浏览器 agent 与日常事务**
- ChatGPT Agent 订机票、买菜、订餐厅：[链接](https://agentusecases.ai/use-case/book-flights-groceries-and-restaurants-with-chatgpt-agent)
- Operator 根据表格数据批量填表：[链接](https://agentusecases.ai/use-case/fill-repetitive-forms-from-spreadsheet-values)
- ChatGPT Agent 为个体创业者做竞品分析：[链接](https://agentusecases.ai/use-case/run-competitor-analysis-with-browser-agents-for-solopreneurs)
- Meta Muse 订酒店 / 训练团队 Muse 代理：[订酒店](https://agentusecases.ai/use-case/book-a-hotel-with-muse) · [团队训练](https://agentusecases.ai/use-case/train-team-muse-agents-to-work-in-a-small-business)

**教育与金融**
- 学生用 Claude 自测、按评分标准批改：[链接](https://agentusecases.ai/use-case/quiz-yourself-and-grade-assignments-against-rubrics-as-a-stu)
- 老师用 Gemini/Claude 做教案与带讲稿的幻灯片：[链接](https://agentusecases.ai/use-case/create-lesson-plans-and-slides-with-speaker-notes-for-teache)
- 通过 MCP 服务器把投资组合持仓拉进 Claude：[链接](https://agentusecases.ai/use-case/pull-portfolio-holdings-into-claude-via-an-mcp-server)
- 用 Claude 查银行流水、核对房产记录：[链接](https://agentusecases.ai/use-case/query-bank-statements-and-reconcile-property-records-with-cl)
- Shopify Autopilot 自动化 Meta 等渠道广告：[链接](https://agentusecases.ai/use-case/automate-store-ad-campaigns-with-shopify-autopilot)
- 用浏览器控制 MCP 读被拦截的网页文章（边界提示）：[链接](https://agentusecases.ai/use-case/read-blocked-web-articles-through-a-browser-control-mcp)

## 周末：阮一峰周刊精选

本周周刊尚未发布新一期：atom 与 index 页最新仍是[第 418 期《如果科技停止在21世纪初》](https://www.ruanyifeng.com/blog/2026/11/weekly-issue-418.html)，已在周六版收录（seen_ids 含 `ryf:https://www.ruanyifeng.com/blog/2026/11/weekly-issue-418.html`），本期不重复。上一期入口：[Atom](https://www.ruanyifeng.com/blog/atom.xml) · [博客首页](https://www.ruanyifeng.com/blog/index.html)。

## 地址／IoC 汇总

- **ARTEX（Hunt.io / Security Affairs 公开指标）**：IP `38.244.50[.]120`（Cogent / 洛杉矶，ARTEX 控制台在 443、8090 端口）；域名 `xcai[.]pro`（LLM 转售域名）；另有一个香港地址和九个代理，来源未公开具体值。
- **VOLTA（Talos）**：SHA256 `57ef4242666d78c50df145b34023df564f0fad38812d6a580e66433d427e2279`（文件名 `9BY0tjwOc3ut.exe` / `yLP9m5J3i2Aw.exe`；PE32+ x86-64；编译时间戳 2026-08-17 20:35；首见 2026-10-11 12:46 UTC）；通信端点 `https[:]//openrouter[.]ai/api/v1/chat/completions`（被滥用的合法服务，回退模型 moonshotai/kimi-k2、google/gemini-2.5-flash）；外传到 Telegram，Talos 称无攻击者自有基础设施。
- 其余条目（Craft CMS、WordPress、React、s2Member、nginx、SonicWall、ZDI、边缘设备）：未见公开 IoC。

## LWiS 固定信源（可直接贴 /home/box/workspace/security-watch/lwis-sources/DAILY-SOURCES.md）

- X List（只读）：https://x.com/i/lists/1239330068461244424（成员备份：lwis-sources/x-list-members.json、x-list-handles.txt）
- 博客清单：https://blog.badsectorlabs.com/files/blogs.txt（本地：lwis-sources/blogs.txt）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- 参考：https://risky.biz/ · https://tldrsec.com/

## 来源搜索 URL

- X Latest 搜索（x 连接器 search_posts_all，只读）：①`(CVE OR POC OR exploit OR 0day) has:links -is:retweet lang:en`；②`github.com (C2 OR nuclei OR "red team") -is:retweet`；③`("malware analysis" OR "threat report" OR "threat actor") -is:retweet lang:en`；④`(CVE OR 0day OR "zero-day" OR "actively exploited") has:links -is:retweet lang:en -from:SecAlertsCo -from:ZeroPathLabs -from:exploitgrid`（高互动补搜，自 11-07 08:00 UTC）。
- LWiS X List：https://x.com/i/lists/1239330068461244424（取 96 帖，覆盖 11-08 03:08–22:10 UTC，约 19 小时）。
- SecureFlow：页面 https://secureflow.scope-sentry.top/all · /community · /blog；接口 https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 、https://secureflow.scope-sentry.top/api/rss/category?category=community 、https://secureflow.scope-sentry.top/api/rss/category?category=blog 、https://secureflow.scope-sentry.top/api/rss/articles/<源id>（共 19 源已全部拉取）。
- 条数：all 200 条（48 小时内 6 条，新 5）；community 新 0；blog 新 23；BugBounty 新 5。
- AI/TLDR：https://ai-tldr.dev/feed.xml（共 50 条，36 小时内 6 条，新 2 条，security 类 2 条）。
- Agent Use Cases：https://agentusecases.ai/feed.xml（60 条；48 小时内 48 条，新 34 条）。
- 阮一峰：https://www.ruanyifeng.com/blog/atom.xml · https://www.ruanyifeng.com/blog/index.html（无新一期）。
- 备援：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json（最新入库 11-06）；https://services.nvd.nist.gov/rest/json/cves/2.0 。
