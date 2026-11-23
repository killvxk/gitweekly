# 2026-11-20／21 安全情报补采覆盖与证据台账

生成：2026-11-23 19:19 HKT（香港）。本文件是可交付补刊的审计说明，不是“补齐全量”的证明。未直接联系用户、发帖、外发邮件；未修改任何 routine、profile、技能或 state。

## 1. 缺失日期与边界的实际依据

- 实际 `reports/` 有 2026-11-19 和 11-22 原刊，缺 11-20、11-21；`raw/` 也只有 11-19、11-22，无中间两天目录。补刊生成前的目录证据和原文 SHA256 记入 `preservation-manifest.json`。
- 11-19 原刊开头写 X 窗结束 **2026-11-19 23:00 UTC = Santiago 11-19 20:00 = 香港 11-20 07:00 HKT**。
- 11-22 原刊末节写开始 **2026-11-21 22:51 UTC = Santiago 11-21 19:51 = 香港 11-22 06:51 HKT**。
- 所以两个原刊之间的明确 X 间隙为 **47 小时 51 分**。未找到 11-20／21 失败 run 原始日志，不能恢复它们计划开始／结束的秒级时间；“因额度不足”是交接说法，未独立核实。
- 为无缝衔接，采用下面两个各 24h 的左闭右开约定日窗。第二窗末 9 分钟与 11-22 重合，按 ID／链接去重；没有用本次执行时间反推当时窗口。

| 补刊日期 | America/Santiago（UTC−03） | UTC | 香港 HKT（UTC+08） |
|---|---|---|---|
| 11-20（周五） | 11-19 20:00 → 11-20 20:00 | 11-19 23:00 → 11-20 23:00 | 11-20 07:00 → 11-21 07:00 |
| 11-21（周六） | 11-20 20:00 → 11-21 20:00 | 11-20 23:00 → 11-21 23:00 | 11-21 07:00 → 11-22 07:00 |

原流程对部分 feed 用 36／48 小时浮动范围，blog 首见甚至可到 7 天。本次按事件／条目原始时间分别归属主日窗；AI/TLDR 因 updated 已整体刷新，只能明确降级使用 published 日期标签。**不能声称精确重放当时的首见集合或全部动态。**

## 2. 逐源实采结果

| 源 | 方法与证据 | 11-20 可恢复 | 11-21 可恢复 | 无法恢复／限制 |
|---|---|---:|---:|---|
| X Latest | sanctioned `x.search_posts_all`，CVE／工具／威胁三组，recency；每组实际最多 25 | 25＋2＋25 | 25＋2＋25 | CVE Latest 只跨数分钟、威胁 Latest 约数小时；不是全量 |
| X 补搜 | 两日各 CVE relevancy、补丁／公告／互动高信号 relevancy、威胁 relevancy | 每组 25 | 每组 25 | 相关度排序不是穷尽；工具组虽仅 2 条仍有 next_token，未宣称检索完成 |
| X 合并独特候选 | 原始 ID 去重，含 List，`x-all.json`／`x-candidate-ledger.csv` | **393** | **276** | 含噪声／回复／RT，不等于情报数；删除或受限帖不能找回 |
| LWiS List | 已连接 user-X 只读 `get_lists_posts`，100/page；连续 8 页共 695 条，最旧越过共同起点 | **271** | **157** | 当前成员／可见性，不是当日 List 成员与原始快照；已取到起点前才停止 |
| SecureFlow all | 指定公开 all GET，浏览器 UA；换 UA＋Referer 再试 | **未知** | **未知** | 两次均 522 |
| SecureFlow community | 分类 GET 两次 522；以 11-05 实际源目录的 7 源逐个 GET | **未知** | **未知** | 每源两次均 522；不能确认当前全部源目录 |
| SecureFlow blog | 分类 GET 两次 522；以同缓存 12 源逐个 GET | **未知** | **未知** | 每源两次均 522；48h／7d 规则不可恢复 |
| pwn.watch | RSS 与 JSON 均 200，各 50 条、相同事件，不重复相加；11-22 缓存同样停 11-08 | 匹配 0 | 匹配 0 | 最新香港 11-09 04:19:52 HKT；不能证明当时源未短暂变化 |
| ExploitGrid exploits | `page=1,2,3&limit=100`，3 页 300 条；page 2 已越过起点，page 3 额外交叉确认 | **93** 条；HIGH/CRITICAL **76**；**67** 个独特 CVE | 匹配 **0** | 最新 date 香港 11-21 03:48:48，说明索引滞后；标题含 detector／lab，不能一律算有效 exploit |
| ExploitGrid deadlines | 当前接口 200，10 条；并用官方 CISA 全目录补已过期项 | 当前交叉 | 当前交叉 | active 不是历史快照，期限以 CISA 为准 |
| CISA KEV | 官方 JSON 200，1790 条；按 dateAdded 日期归属 | **4** 条 | **0** 条 | dateAdded 无时分；不能宣称小时级入库顺序或日内无增删 |
| AI/TLDR | 当前 Atom 50 entry＋11-22 缓存 50 entry，合并 55 个独特链接；按 published 标签 | **16**；security **2** | **7**；security **0** | 原 updated 窗口不可恢复；23 个目标详情页换 UA+Referer 后仍 403，仅引用 Atom 摘要；Signal 另核官方文 |
| Agent Use Cases | 当前 60 item＋11-22 缓存 60 item，合并 72 个独特链接；按 pubDate | **18**（3 条仅缓存保住） | **20** | 滚动源非历史全集；38 条已全部在补刊分组列出 |
| 阮一峰周刊 | Atom 与 420 正文均 200，提取正文 GitHub 链接、排除 weekly 自身与 issues | 不适用（周五） | **14** 个项目＋**7** 篇文章／专题 | 11-22 已补过部分，本次归档并扩展，不伪称新一期 |
| 厂商／威胁报告 | AWS／MONAI／Cisco／DigitalOcean／PHP／Signal／ThreatFabric 等当前公开原文交叉 | 按补刊逐条列 | 按补刊逐条列 | 当前页面可能事后更新，不冒充当日全文快照；MONAI 0.8.6 明确标事后版本 |

补采所有脚本 HTTP 均显式浏览器 UA，403 按原要求换 UA＋站点 Referer 一次；SecureFlow 两轮后停止，没有无限重试，没有登录或调用管理端接口。

## 3. 与 11-22 的关系，以及本次实际补出的内容

### 11-20

- 11-22 已补收、现归档回正确日期：4 条 KEV、Cairn／MONAI、欧委会 AI 辅助入侵、Etherpad 的 ExploitGrid 收录，以及部分 AI 条目。
- 本次新展开：PHP phpAfterShell 与官方适用条件、Ruby2Shell、AMD KVM、WhatsApp IP 暴露修复、SonicWall Gen 6 生命周期、Bell 企业客户数据泄露、SBC 数量口径差异、capa／kiri／依赖更新观点、16 条 AI 动态与 18 条 AUC。
- 旧漏洞有新验证／传播：nginx 研究者完成验证、FreeSWITCH 公开研究；已标“重复但重大跟进”，不当成当天新 CVE。

### 11-21

- 11-22 已补收：Ghostscript Upload2Shell、Cairn、FBI／NCIC 调查、周刊及其部分项目／文章；本次为正确历史归属，不重计“新增”。
- 本次新展开：Microsoft Entra Connect Health 已遭利用的元数据外泄、Bazuka 与原始 IoC、Burp Sharpener、bettercap 2.42.0、工程 skills／Phonebox；以及 7 条 AI 动态和 20 条 AUC。
- AUC 20 条中 **15** 条在 11-22 正文已有链接，**5** 条本次首次展开；11-20 的 18 条没有在 11-22 正文展开。每条均按链接标记，详见 `feed-candidate-ledger.csv`。
- AI 11-20 的 16 条里 2 条、11-21 的 7 条里 3 条在 11-22 正文已有链接。因为原 updated 不可恢复，不据此认定首次发布日，只按可恢复 published 标签归档。

“本次新补采”比较的是已交付成稿，不等于之前采集程序从未看到；`state-before.json`／当前 state 的 seen_ids 不能充当当日首见证据，因此未用它们过滤。

## 4. 回溯中发现的计数与事实边界问题

1. **AUC 原解析双计数。** 11-22 `auc-feed.xml` 实际只有 **60 item／60 独特链接**，但 `auc-parsed.json.total=120`；`new_items` 列表 66 项仅有 **33 个独特链接，每条重复两次**。原报告“66 条”不能沿用。本刊直接解析 XML 并按链接去重，未修改历史文件。
2. **pwn.watch 原计数也应区分格式。** 当前 RSS 50、JSON 50，为同一批链接，不是 100 个独特事件。本刊记 50；都停在 11-08。
3. **MONAI 正式发行版不能倒灌。** 公告 11-18 显示补丁已合入但 patched versions=None；0.8.6 release 的真实机器时间为 **2026-11-22 01:29 UTC = Santiago 11-21 22:29 = 香港 11-22 09:29 HKT**，比第二窗结束晚 2h29m。补刊只把它当事后补充。早期媒体“11-18 released security update”与正式发版有差异，不混为同一个日期。
4. **CISA 截止日不是“香港清晨几小时内”。** dueDate 没有具体时分，四条 11-20 新增的日期是 11-23；本刊不推断即将过期的小时倒计时。
5. 欧委会未官方命名 AI 工具，不能把 CERT-EU 对 ARTEX 的一般警告当本案归因；Bell “agentic”也未公开模型／工具。
6. FBI／NCIC 报道是知情人士称正调查，报道时 FBI 未公开确认，更未证明全国执法数据已经失窃。
7. GitHub／索引上出现“PoC”“detector”“lab”标题，不足以证明代码有效或在野利用。本刊仅链接 ExploitGrid 页面、厂商修复或正常工具，不链接 PoC 仓库，不提供载荷与攻击步骤。

## 5. X 实采范围与分页证据

8 页列表原始返回：

| 文件 | 条数 | created_at UTC | 对应香港 HKT |
|---|---:|---|---|
| lwis-01.json | 97 | 2026-11-22T20:17:56.000Z → 2026-11-23T11:00:09.000Z | 11-23 04:17:56 HKT → 11-23 19:00:09 HKT |
| lwis-02.json | 92 | 2026-11-22T05:54:21.000Z → 2026-11-22T20:17:48.000Z | 11-22 13:54:21 HKT → 11-23 04:17:48 HKT |
| lwis-03.json | 96 | 2026-11-21T17:39:52.000Z → 2026-11-22T05:41:07.000Z | 11-22 01:39:52 HKT → 11-22 13:41:07 HKT |
| lwis-04.json | 86 | 2026-11-21T02:56:48.000Z → 2026-11-21T17:38:25.000Z | 11-21 10:56:48 HKT → 11-22 01:38:25 HKT |
| lwis-05.json | 91 | 2026-11-20T16:21:56.000Z → 2026-11-21T02:56:39.000Z | 11-21 00:21:56 HKT → 11-21 10:56:39 HKT |
| lwis-06.json | 94 | 2026-11-20T08:43:32.000Z → 2026-11-20T16:21:10.000Z | 11-20 16:43:32 HKT → 11-21 00:21:10 HKT |
| lwis-07.json | 96 | 2026-11-20T00:13:26.000Z → 2026-11-20T08:36:48.000Z | 11-20 08:13:26 HKT → 11-20 16:36:48 HKT |
| lwis-08.json | 43 | 2026-11-19T19:54:19.000Z → 2026-11-20T00:04:14.000Z | 11-20 03:54:19 HKT → 11-20 08:04:14 HKT |

在目标窗内，11-20 List 首末帖香港为 11-20 07:12:18 → 11-21 06:48:52 HKT，11-21 为 11-21 07:00:37 → 11-22 06:38:42 HKT。边界没有帖并不代表采集缺页；列表已翻到起点前，不能把首末差当连续发帖密度。三组检索与补搜各自区间见两刊末节／`x-coverage.json`。

## 6. 链接核验与不能恢复的东西

两刊合计 **181 个独特 https URL**：114 个 HTTP 200；32 个原帖 ID 经 sanctioned X 读取，作者／时间／ID 保留；7 个 List／搜索参考 URL 不当作正文原文核验；24 个 403（23 个 AI/TLDR＋1 个 Medium），3 个 SecureFlow 522；1 个 AWS Ruby 公告脚本 HTTP 传输不完整，随后公共 WebFetch 成功读取全文。**没有 404 主链接**。每个状态见 `report-link-check.json`。X 不用 Shell 调 API，也没有浏览器绕过认证。

这些验证证明当前可读性，不证明发布当日页面未更改。无法恢复项包括：失败 run 的时分和配额日志、当日 X 删除帖／限制内容／List 原成员、SecureFlow 全部分类与首见集合、滚动 feed 已淘汰条目、AI 原 updated 时间和详情全文。报告已逐节标明，不把它们改写成“无更新”。

公开 IoC 仅抄自 AWS 与 ThreatFabric：Cairn 2 个历史 IP、Bazuka 3 个地址／域名和 26 个 SHA256，以及文中包名。没有把受害者个人数据、凭据或未知截图值当指标。

## 7. 可复核文件与保护范围

- 主补刊：`2026-11-20-x-security-digest-supplement.md`（10 节）与 `2026-11-21-x-security-digest-supplement.md`（11 节含周刊）。
- 独立证据目录：`/home/box/workspace/security-watch/backfill/2026-11-20_21/`。
- `x-all.json`、`x-coverage.json`、`lwis-01..08.json`、`20-*.json`、`21-*.json`：X 原始读取／来源组、原作者和时间。
- `x-candidate-ledger.csv`：669 个窗口内 X 候选的 ID、原作者、UTC／HKT、日期归属、组别、与前后成稿比对；没有用当前 seen_ids 排除候选。
- `feed-candidate-ledger.csv`、`ai-ledger.json`、`auc-ledger.json`：每条原始日期、updated（若存在）与成稿重复标记。
- `eg-1..3.json`、`eg-ledger.json`、`kev-target.json`：完整已取到的元数据和时间筛选结果。
- `*.meta.json`：每个 HTTP 请求状态、字节、时间、SHA256、重试；`sf-cached-sources.json` 是明确标日期的旧目录，不假称当前完整目录。
- `preservation-manifest.json`／`deliverable-manifest.json`：原件和交付文件指纹。现有 state 的 SHA256 应保持 `789473dd50c4e2d0d216163cc18cc0365cffc98e6f791b639dfa7ebd279d0893`。
- 未覆盖旧文件，未改 routine、profile、技能或 last_report_date；未执行任何漏洞代码、样本或安全工具。

## 8. 交付状态

Box 两刊与本覆盖文件已生成。两刊已通过 CopyFromBox 写入指定 Mac，随后各自 Read 读回标题／窗口，并以 Mac 的 shasum 验证与 Box 完全一致：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| 2026-11-20-x-security-digest-supplement.md | 35347 | `a9b6815383d45d6a2fdaf32b1e40665d3cab51cce928bbaf971de5ddfe4992db` |
| 2026-11-21-x-security-digest-supplement.md | 34761 | `1b99f9d1ad024a92722c6d29f955b76fcc7db01578da18b2d30fbef3904bc03e` |

Mac 输出目录：`/Users/kenny1337/Desktop/_05_项目/X安全情报晚报/`，machineId `c9e26e05-d6b7-4046-8cea-229a76fbeb39`。目标文件在复制前均不存在，未覆盖原稿。本覆盖台账也在同目录交付，独立哈希和读回回执保存于 `backfill/2026-11-20_21/mac-delivery-receipt.json`。

验收结果：结构／日期归属／来源与缺口标签／去重台账／无攻击步骤／Box 落盘通过；两刊 Mac 拷贝与哈希通过。全量采集不通过：SecureFlow 522、AI 原 updated 与详情 403、历史删除／滚动内容不可穷尽。不能对用户说“已补齐全量”或“所有验收通过”。是否补入正常去重 state 留给父级判断，本次没有合并。
