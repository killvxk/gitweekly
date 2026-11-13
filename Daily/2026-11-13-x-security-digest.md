# X 安全情报晚报 · 2026-11-13（周四）

> 报告时间：2026-11-13 约 19:00（香港时间）＝ 2026-11-13 约 08:00（America/Santiago）。
> **本期为机器侧提前版**：由本机生成，非 box 流水线。覆盖窗口只到采集时刻：**2026-11-12 23:00 UTC ～ 11-13 10:26 UTC（约 11.5 小时）**。正式晚报窗口应至 11-13 22:59 UTC；box 今晚若照常生成正式版，会覆盖本文件。
> **引文口径**：X 与工具检索在 Brave 失败后由搜索合成器作答，帖子 ID 与 CVE 叙述**不是拉到的原帖**。本期不把合成摘要当引文，不收录那些 status ID。只写本机实际拉到的订阅源，以及一份已读到的 KEV 公开快照。
> **实拉源**：pwn.watch（50 条，窗口内 0）、AI/TLDR（50 条，窗口内 3，均为工具发布）、Agent Use Cases（60 条，窗口内 0）、SecureFlow all（200 条，窗口内 2 条标题）。ExploitGrid、LWiS List、博客清单：**未抓取**。
> **CISA KEV**：本机读到的公开快照停在 snapshot 2026-11-11T09:09Z，页面写 catalog 口径 2026.11.10、共 1,779 条。**不能写成今日已核对**；11-13 目录是否更新，未核。快照里「今日到期」只表示该快照记录的 due date，不是 11-13 当日复核。
> 境内站点只记标题与编号，不放直链。工作日版，不加阮一峰周刊节。

## 今日摘要

- **KEV 快照（截至 11-11，非今日核对）**：catalogVersion 2026.11.10。快照 due date 落在 11-13 的是 Barracuda CVE-2026-116606、CVE-2026-111560，以及 Ivanti Connect Secure CVE-2026-118527。11-24 批次在同一快照里有 Outlook CVE-2026-124194、Chromium CVE-2026-125350（date added 11-10）、Cisco BroadWorks CVE-2026-20320、Openwave Webtop CVE-2026-111793。SonicWall CVE-2026-19868 due date 为 11-20。
- **实拉订阅源**：AI/TLDR 窗口内 3 条，全是工具发布（Codex CLI 0.168.0／0.169.0、OpenCode 2.3.0）。SecureFlow all 窗口内 2 条标题。pwn.watch 与 Agent Use Cases 本窗口 **0 条**。
- **不收录**：搜索合成器给出的 Chrome 批次细节、NetScaler／FrankenPHP／Rucio／Windchill／MongoDB 叙述、FORGE Lab 数字、Gootloader 新口径、GravityRAT，以及无日期的 C2 仓库页。那些不是本窗口拉到的帖或发布说明。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

**1. KEV 快照里 due date 为 11-13 的三条（快照截至 11-11，非今日核对）**
- 来源：已读页面 https://changeriskintel.com/tools/cisa-kev-live （snapshot 2026-11-11T09:09Z）。官方 JSON 直连在本机网络限制内，未拉。
- Barracuda Email Security Gateway CVE-2026-116606：快照原文为认证绕过，未认证远程攻击者可调用配置导入并恢复特制备份，可与 CVE-2026-111560 串联。date added 2026-11-10，due 2026-11-13。
- Barracuda 多产品 CVE-2026-111560：快照原文为 OS 命令注入，已认证管理员经时区字段以 root 执行命令，可与 CVE-2026-116606 串联。date added 2026-11-10，due 2026-11-13。
- Ivanti Connect Secure CVE-2026-118527：快照原文为可预测标识符，已认证远程攻击者可把受控内容上传到已知磁盘位置，可与 CVE-2026-104935、CVE-2026-111357 串联。date added 2026-10-30，due 2026-11-13。
- 地址：仅上述快照页。不附官方目录直链（本机网络限制）。

**2. 同一快照里已入列、due date 为 11-24 的条目（只记快照字段，不补合成叙述）**
- Chromium CVE-2026-125350：date added 2026-11-10，due 2026-11-24。快照描述为 XML 组件 use-after-free，特制网页可在沙箱内执行代码，影响 Chromium 系浏览器。
- Microsoft Office Outlook CVE-2026-124194：date added 2026-11-10，due 2026-11-24。快照描述为缺少用户交互的潜在不安全操作，可经网络做 spoofing。合成搜索里的 UNC／NTLMv2 细节**不写入**。
- Cisco BroadWorks CVE-2026-20320：XXE，未认证远程读配置。due 2026-11-24。
- Openwave Webtop Media Transcoder CVE-2026-111793：资源跨域传递。due 2026-11-24。

**3. SecureFlow 窗口内标题（只作信息流，不作独立漏洞核验）**
- 先知社区标题含「WordPress Core 竞争条件远程代码执行漏洞（CVE-2026-119977）」，published 2026-11-13 14:24（贝时）。编号 93320。境内站点，不放直链。该 CVE 已在上期前后的 KEV 快照中（date added 2026-11-03），此处只记新分析标题。

本窗口没有其他已核验的新 CVE 帖。合成检索里的其余 CVE 行本期空白，不编造地址。

## 工具与 GitHub 发布（每条：说明 + 地址列表）

只收录 AI/TLDR 订阅源里、窗口内实际解析到的 3 条。检索返回的 Covenant、Havoc、BeaconatorC2 等仓库页没有 11-12／11-13 发布日期，**不写入**。

**1. OpenAI Codex CLI 0.168.0 → 0.169.0**
- 0.168.0：并排会话、音频片段与动画 GIF。0.169.0：side-chat 标签页、任务搜索、可折叠轮次。
- [0.169](https://ai-tldr.dev/releases/openai-codex-cli-0-169/) · [0.168](https://ai-tldr.dev/releases/openai-codex-cli-0-168/)

**2. OpenCode 2.3.0**
- 子代理默认后台运行。[发布说明](https://ai-tldr.dev/releases/anomalyco-opencode-2-3-0/)

## APT / Malware 分析（每条：说明 + 地址列表）

本窗口 **0 条已核验新条目**。

Gootloader 新数字、GravityRAT、Black October 叙事来自搜索合成，不是拉到的帖，本期不收录。上期已报的执法行动不重复。

## SecureFlow 信息流精选（窗口内新条目；时间戳为贝时）

窗口起点 2026-11-12 23:00 UTC ＝ 贝时 11-13 07:00。`published` 字符串比较会把贝时凌晨条目算进来，那些属于上期 UTC 窗口，本期剔除。

**community（窗口内 2 条）**
- 先知社区「WordPress Core 竞争条件远程代码执行漏洞（CVE-2026-119977）」，2026-11-13 14:24，编号 93320。境内站点，不放直链。
- Seebug「面向移动 SQLite 数据库的上下文感知证据抽取：符号—神经框架」，2026-11-13 16:27，paper/3534。境内站点，不放直链。

**不计入本期（贝时 11-13 07:00 之前）**
- 红队 DollarTicket＋SPN 劫持＋RBCD，编号 93281，贝时 00:20。
- BugBounty「Unauthenticated UCP/MCP catalog access on a password-protected dev store」，贝时 03:58。

blog 分类本窗口未单拉。all 端点窗口内没有 blog 类新标题。

## AI/TLDR 动态（来自 ai-tldr.dev；本窗口新条目 3 条，均为工具发布类）

Codex CLI 0.168.0、0.169.0，OpenCode 2.3.0。窗口内 security 类 0 条。详见工具节。

## Agent 用例动态（来自 agentusecases.ai；本窗口新条目 0 条）

60 条存量，窗口起点之后 0 条。跳过。

## 地址／IoC 汇总

本期没有新的已核验 IoC。不从上期抄录，也不从合成摘要抄 IP、域名或哈希。

KEV 快照 due date 速记（截至 11-11，非今日核对）：11-13 Barracuda CVE-2026-116606／CVE-2026-111560、Ivanti CVE-2026-118527；11-20 SonicWall CVE-2026-19868；11-24 Outlook CVE-2026-124194、Chromium CVE-2026-125350、BroadWorks CVE-2026-20320、Webtop CVE-2026-111793。

## 来源搜索 URL

**本机实拉**
- pwn.watch：https://pwn.watch/feed.xml （50 条，窗口内 0）
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条，窗口内 3）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条，窗口内 0）
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条；贝时过滤后窗口内 2 条）
- KEV 快照：https://changeriskintel.com/tools/cisa-kev-live （snapshot 2026-11-11T09:09Z）

**未用作引文**
- `site:x.com` 与工具检索：Brave 失败后由搜索合成器作答。帖子 ID、无日期 C2 仓库页均未写入正文。
- ExploitGrid、LWiS List、博客清单：未抓取。
- KEV 官方 JSON、NVD：本机网络限制，未直连。

### LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）: https://x.com/i/lists/1239330068461244424 （本期未爬取）
- 博客清单: https://blog.badsectorlabs.com/files/blogs.txt （本期未爬取）
- CISA KEV / NVD：本机网络限制。本期只用公开快照 https://changeriskintel.com/tools/cisa-kev-live
- Risky Business: https://risky.biz/ （本期未拉）
- tl;dr sec: https://tldrsec.com/ （本期未拉）
- SecureFlow 安全信息流: https://secureflow.scope-sentry.top/all
- SecureFlow 社区: https://secureflow.scope-sentry.top/community （本期未单拉；条目来自 all）
- SecureFlow 博客: https://secureflow.scope-sentry.top/blog （本期未单拉）
- Agent Use Cases: https://agentusecases.ai/ （RSS https://agentusecases.ai/feed.xml）
- AI/TLDR: https://ai-tldr.dev/ （Atom https://ai-tldr.dev/feed.xml）
- pwn.watch: https://pwn.watch/ （RSS https://pwn.watch/feed.xml）
- ExploitGrid: https://exploitgrid.net/ （本期未抓取）

## 验收结果

1. 采集：按提前版收窄后通过。实拉四个订阅源并按窗口筛选；KEV 只用 11-11 快照，并写明不是今日核对。X 全量爬取、LWiS、ExploitGrid 未做，已标注。
2. 引文：合成搜索的 status ID 与无日期仓库页已从正文删除。留下的链接只有本机拉到的订阅源 URL 和已读的 KEV 快照页。境内站点无直链。
3. 成稿：十个小节仍在（工作日版，无周刊节）。无新核验材料的 APT 节写明 0 条，不拿合成摘要填空。无利用代码，无 exploit 仓库直链。
4. 落盘：覆盖写入本机 `/Users/kenny1337/Desktop/_05_项目/X安全情报晚报/2026-11-13-x-security-digest.md`。box 侧 state.json 不可见，本期没有新的 X 帖 ID 需要去重。
