# X 安全情报晚报 · 2026-11-20（周五）补刊

> 补采核验时间：2026-11-23 19:14 HKT（香港）。不冒充当日出报。
> 窗口为左闭右开：America/Santiago（UTC−03）2026-11-19 20:00 → 2026-11-20 20:00；UTC 2026-11-19T23:00:00Z → 2026-11-20T23:00:00Z；香港 HKT（UTC+08）2026-11-20 07:00 → 2026-11-21 07:00。

本刊是事后回溯，不是当日实时快照。已核对实际目录：有 11-19、11-22 原刊，既无 11-20／11-21 原刊，也无对应日期 raw 目录；缺失日期据此确认。没有找到失败 run 的原始日志，因此“额度不足”的原因仅来自任务交接，未独立核实。

边界依据：11-19 原刊明确结束于 11-19 23:00 UTC；11-22 原刊开始于 11-21 22:51 UTC。两天采用衔接前刊的各 24 小时**约定窗口**，不是恢复出来的失败 run 精确执行时间；第二天末尾与 11-22 的采集窗重合 9 分钟，按帖子 ID／原文链接另行去重。原规则对 SecureFlow、AUC、AI/TLDR 分别有 48 小时／7 天／36 小时浮动窗口，本次主台账使用不重叠日窗，AI 的特殊日期归属见该节。没有用当前 seen_ids 丢弃候选，没有修改 state 或 routine。

**阅读标记**：〔本次新补采〕=在 11-22 成稿中未展开的回溯条目；〔11-22 已补收〕=为还原日期而归档，不计第二次新情报；〔重复但重大跟进〕=旧事件出现新的利用、补丁或调查状态。该标记只比较“是否在已交付正文中出现”，不代表当时一定未采到。报告之外的完整候选／去重证据保存在独立 backfill 台账。

**验收：部分通过。** X 历史 Latest、相关度和高信号补搜及 LWiS 均实采；但有限检索不等于 X 全量。SecureFlow 三路及 19 个历史已知源均 522，不能恢复；AI/TLDR 的原始 updated 历史不可恢复、详情页 403；滚动源和删除内容不能保证全量。所有这些均记为缺口，而不是“无更新”。


## 今日摘要

- **不只 KEV**：本次实际补出 PHP 后续会话文件缺陷、Ruby2Shell、AMD KVM 隔离问题、WhatsApp 修复，以及 Bell、欧委会和 Cairn 入侵研究。
- CISA `dateAdded=2026-11-20` 有 4 条，11-22 已补收；现归档回本日，联邦期限均为 11-23。不要把它们再次算新发现。
- LWiS 实际日窗内 **271 条**；多组 X 检索并入后独特候选 **393 条**，含噪声、回复、转帖，并非 393 条情报。AI/TLDR 按可恢复的 published 日标签 **16 条、security 2 条**；AUC 按 pubDate 去重 **18 条**。ExploitGrid 按 date 命中 **93 条**，不是 93 个漏洞或 93 个有效 exploit。
- SecureFlow 无法追溯；pwn.watch 当前和 11-22 缓存均停在 11-08，未发现目标窗口条目，但不能证明历史从未短暂更新。

## CVE / POC / 漏洞

### 1. 四条漏洞进入 CISA KEV〔11-22 已补收；日期归档〕

官方目录记录四条均在 11-20 加入、11-23 到期。`dateAdded` 只有日期，不能据此推断入库时分或把截止日解释成“香港清晨数小时内”。

| 漏洞 | 影响／处理 |
|---|---|
| VMware vCenter CVE-2026-123890 | 认证绕过、已在野利用。按分支升级，例如 8.0 U3m；无临时绕过修复。怀疑失陷时做调查，不能把安装补丁等同清除入侵。 |
| Cisco Expressway CVE-2026-76466 | 集群设备数据库服务缺陷，可导致 root 权限命令执行；升级 X15.5.20。官方公告还保留旧的“未见利用”措辞，利用状态以较新的 CISA 入库记录交叉确认，不能说 Cisco 已更新确认。 |
| Apache Roller CVE-2026-129448 | XML-RPC 预认证反序列化，和 CVE-2026-82384 同一根因、覆盖版本不同；升 6.1.6 或更高。 |
| SAP NetWeaver Enterprise Portal CVE-2025-42884 | 数据查询逻辑特殊元素处理缺陷，可能披露／修改服务器信息；按 SAP 对应安全说明修补，不凭二手摘要猜具体补丁号。 |
- X 原帖：https://x.com/SamAiPr/status/2123734717048455409
- 厂商／官方公告：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json · https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t · https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495 · https://lists.apache.org/thread/cc0jck13nb9vvcmzxzwotr6n16mx28z9 · https://support.sap.com/en/my-support/knowledge-base/security-notes-news/bulletin-2025.html

### 2. PHP phpAfterShell CVE-2026-126714〔本次新补采〕

默认 files 会话处理器在写入中断后可能遗留新旧会话混合数据，造成对象反序列化；官方说明 RCE 需要适合的应用对象链及相应输入／中断条件，不能写成所有 PHP 网站均可无条件远程接管。与此前 PHP2Shell 不是同一枚 CVE；旧补丁不够。

官方列出的修复版本为 **8.2.36／8.3.37／8.4.28／8.5.13**。升级发行版／应用内嵌 PHP 并重启工作进程。关闭上传进度只能去掉一种输入途径，不能代替修复。SecurityWeek 当窗报道这批共 7 枚严重漏洞；本文只对已核对的缺陷展开。ExploitGrid 本日已有多份相关收录，但其中包含实验／检测项目，不能据标题等同“经验证武器化”。
- X 原帖：https://x.com/LearnInvest2026/status/2123584790095855764 · https://x.com/TheExploitHQ/status/2123780817264513509
- 厂商／官方公告：https://github.com/php/php-src/security/advisories/GHSA-fm2m-fjf5-v3cp
- 文章／研究：https://www.securityweek.com/php-patches-seven-critical-rce-vulnerabilities/
- 公开 exploit 索引（只记收录事实）：https://exploitgrid.net/vulnerabilities/CVE-2026-126714

### 3. Ruby2Shell CVE-2026-132825〔本次新补采〕

某些非 UTF-8 单字节编码的大小写转换存在堆越界写；部署与分配器、运行时及应用逻辑条件决定实际可利用性，不把高危评分直接等同可靠远程接管。Ruby 这批修复同时涉及正则与字符串处理。

升级至 **3.3.14／3.4.13／4.0.10** 或供应商修复包，重启应用／worker、重建容器。AWS 公告的原时区日期为 11-19／20（香港分别 11-20 07:05／11-21 05:45），列出 Elastic Beanstalk、Lambda 与 Amazon Linux 状态；托管运行时不要假定所有区域已同时完成推送。该 AWS 页面脚本 GET 两次传输中断，随后以公共 WebFetch 读取全文核对；不是 404。ExploitGrid 本日多次收录，仅作公开研究存在的佐证。
- 厂商／官方公告：https://aws.amazon.com/security/security-bulletins/2026-193-aws/
- 文章／研究：https://www.securityweek.com/ruby-patches-ruby2shell-vulnerability-that-could-lead-to-rce/
- 公开 exploit 索引（只记收录事实）：https://exploitgrid.net/vulnerabilities/CVE-2026-132825

### 4. Linux AMD KVM CVE-2026-99312〔本次新补采〕

影响启用了嵌套虚拟化的 **AMD KVM 宿主机**；攻击前提是控制客户机并拥有其中的 root，不是互联网任意用户直接攻击。DigitalOcean 确认研究可从自有 VM 读取宿主机内存，并已修补其基础设施。上游修复包括 **7.3.5／6.18.64／6.12.118**；发行版版本应以其回补公告为准。

修复在宿主机，不在来宾系统；更新并按厂商要求重启，暂不能更新时禁用嵌套虚拟化并评估租户业务影响。报道说未见在野攻击、未发布 exploit，而 ExploitGrid 同日出现名为 pve-cve 的记录：仅能确认索引收录，**不据此推翻研究者状态或宣称已有有效 exploit**。
- 当窗 X 证据时间：2026-11-20 22:45:57 HKT（香港）。
- X 原帖：https://x.com/Dinosn/status/2123789952156942493
- 厂商／官方公告：https://www.digitalocean.com/blog/cve-2026-99312-kvm-patch
- 文章／研究：https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html
- 公开 exploit 索引（只记收录事实）：https://exploitgrid.net/vulnerabilities/CVE-2026-99312

### 5. WhatsApp CVE-2026-23871 修复〔本次新补采〕

Click to WhatsApp 广告回复 URL 验证不完整，可泄露设备 IP；影响 Android 上 WhatsApp 和 WhatsApp Business **早于 2.26.17.4** 的版本。更新客户端，并留意仿冒广告与消息。SecurityWeek 称该问题在打击诈骗活动时发现；不要把 IP 暴露写成聊天解密或设备 RCE。厂商年度安全页面本次 HTTP 400，正文依据可读取报道，不冒称已读厂商全文。
- 当窗 X 证据时间：2026-11-21 00:46:32 HKT（香港）。
- X 原帖：https://x.com/Dinosn/status/2123820296637690137
- 文章／研究：https://www.securityweek.com/whatsapp-fixes-flaw-uncovered-while-disrupting-scam-campaign/

### 6. nginx／FreeSWITCH／Etherpad 的公开研究跟进〔重复但重大跟进；Etherpad 11-22 已补收〕

- nginx **CVE-2026-123633／123007**：研究者在本窗报告完成验证；按厂商公告修补，不能将停止 HTTP/2 当成这批所有缺陷的完整修复。11-18／19 已报道主漏洞，本次只增记验证与公开索引状态。
- FreeSWITCH **CVE-2026-116779**：本窗 X 再次传播公开研究；沿用已披露的 1.11.3 修复要求，未发现本窗新的厂商版本，不重写成新 0day。
- Etherpad **CVE-2026-114516**：ExploitGrid `EGE-GH-XMUshAT` 的 date 是本日，预认证文件读取已在 **3.3.3** 修复；11-22 已讲解，本次归档其首次索引日期。
- X 原帖：https://x.com/pyn3rd/status/2123751325016228064 · https://x.com/Dinosn/status/2123649340820636044
- 厂商／官方公告：https://nginx.org/en/security_advisories.html · https://github.com/advisories/GHSA-mc8w-wjhw-45x5
- 公开 exploit 索引（只记收录事实）：https://exploitgrid.net/vulnerabilities/CVE-2026-123633 · https://exploitgrid.net/vulnerabilities/CVE-2026-116779 · https://exploitgrid.net/exploits/EGE-GH-XMUshAT

### 7. SonicWall Gen 6 生命周期与本日期限〔本次新补采／既有期限跟进〕

当窗报道提醒 Gen 6 防火墙不再获得安全补丁，不能把“没有可装的新补丁”当安全信号；应核对具体型号支持周期、迁移受支持设备并限制管理／VPN 暴露。CISA 记录的 SonicOS **CVE-2026-19868** 期限为 11-20；11-19 已预告，本次为历史到期提醒，不宣称它与全部 Gen 6 设备一一对应。
- X 原帖：https://x.com/Dinosn/status/2123791323354263703
- 厂商／官方公告：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-19868
- 文章／研究：https://thehackernews.com/2026/11/sonicwall-warns-gen-6-firewalls-wont.html


## 工具与 GitHub 发布

### 1. capa 能力识别介绍〔本次新补采；不是确认当日发版〕

当窗 LWiS 介绍 capa 对 PE、ELF、.NET 及沙箱报告做能力识别，可辅助恶意样本分诊。这里记录的是本窗传播，不虚构版本发布。应在隔离分析环境中处理不可信样本。
- X 原帖：https://x.com/Dinosn/status/2123789262856302739
- GitHub 工具项目（非 PoC）：https://github.com/mandiant/capa

### 2. kiri 跨平台容器运行时〔本次新补采〕

当窗介绍一个跨 macOS、Windows、Linux 的轻量容器运行时及隧道功能。防守关注点是容器／隧道会扩大开发机可达面，使用前核对网络暴露与权限；不把第三方项目介绍等同安全背书。
- X 原帖：https://x.com/Dinosn/status/2123650915827622003
- GitHub 工具项目（非 PoC）：https://github.com/libracoder/kiri

### 3. “最新但隔一天”的依赖更新观点〔本次新补采；研究观点〕

Florian Roth 当窗文章讨论升级带来的供应链风险与延迟更新的折中。它是作者观点，不是可统一套用的紧急补丁政策：在野利用漏洞不能机械延迟一天。文章本次两次 403，仅确认原帖文本及文章地址。
- X 原帖：https://x.com/cyb3rops/status/2123762976469426677
- 文章／研究：https://cyb3rops.medium.com/the-sweet-spot-is-a-day-old-11881459f82b


## APT / Malware 分析

### 1. AWS：Cairn agent 自主发现并利用医疗应用 0day〔11-22 已补收；本次补回首日报道日〕

AWS 从暴露的 Cairn 实例恢复了 9 月 8–10 日、针对东亚高校的操作记录，中等置信度判断为中国关联行为体。约 11 分钟发现医疗影像应用任意写入问题，但另两组持续多小时的尝试失败，不能只引用成功样本暗示 agent 无所不能。防守侧减少研究服务公网暴露、最小权限运行、对异常文件写入和外联自动告警／隔离。

补采时官方 MONAI Label 公告确认 **≤0.8.5** 受影响，补丁已合入但公告当时写“下个版本包含”，patched versions 仍为 None。**事后修复信息：0.8.6 发布于香港 11-22 09:29（UTC 01:29；Santiago 11-21 22:29），晚于两刊窗口**，故不能写成本日已发布版本。该版本将本问题列为 CVE-2026-133968。11-22 原刊已给升级建议，本刊不修改原文件。
- 当窗 X 证据时间：2026-11-21 03:30:08 HKT（香港）。
- X 原帖：https://x.com/Dinosn/status/2123861468512677927
- 厂商／官方公告：https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/ · https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94 · https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6
- 文章／研究：https://www.bleepingcomputer.com/news/security/hackers-use-autonomous-ai-tool-cairn-to-find-zero-day-take-over-server/

### 2. Bell Canada 承认企业客户数据被盗〔本次新补采〕

Bell 称 11-17 的入侵涉及预生产 Maximo 等系统，可能暴露企业联系人、工单标题、部分网络 IP；称无客户服务中断、相关数据不含凭据。公司用“agentic threat actor”描述攻击者，但未公开具体模型、工具、归因或受影响总数，不应自行归到 ARTEX／Cairn。留意冒充运营商的社工；Bell 只向客户与 CCCS 分享 IoC，未公开，不能伪造指标。
- 当窗 X 证据时间：2026-11-21 03:28:33 HKT（香港）。
- X 原帖：https://x.com/Dinosn/status/2123861070024528174
- 文章／研究：https://www.bleepingcomputer.com/news/security/bell-canada-says-agentic-hacker-stole-enterprise-customer-data/

### 3. 欧委会确认 AI 辅助攻击〔11-22 已补收；补回早期证据与不确定性〕

SecurityWeek 当窗报道欧委会确认攻击使用 AI、服务因保护措施暂时下线；发言人称未见员工数据外泄证据。媒体称中断超过 10 天，但**具体 AI 工具未获官方命名**。CERT-EU 同期警告 ARTEX，并不等于已证明此案使用 ARTEX；保留两者的证据边界。
- 当窗 X 证据时间：2026-11-20 19:08:41 HKT（香港）。
- X 原帖：https://x.com/Dinosn/status/2123735276510167536
- 文章／研究：https://www.securityweek.com/european-commission-confirms-ai-assisted-cyberattack-disrupted-services/

### 4. SBC Medical 客户数据泄露〔本次新补采；数量有口径差异〕

BleepingComputer 当窗标题称 160 万客户，SecurityWeek 同窗标题称超过 200 万；本次已读取前者正文，不将两数相加或选较大数当最终事实。按实际通知关注身份资料与后续社工，规模仍以公司通知范围为准。
- X 原帖：https://x.com/Dinosn/status/2123620538275029207 · https://x.com/Dinosn/status/2123753613361311764
- 文章／研究：https://www.bleepingcomputer.com/news/security/hackers-steal-data-of-16-million-sbc-medical-group-customers/ · https://www.securityweek.com/sbc-medical-group-data-breach-impacts-over-2-million/


## SecureFlow 信息流精选

**采集失败／无法追溯，不是“本日无显著更新”。** all、community、blog 三路各首试及换浏览器 UA＋站点 Referer 重试仍 HTTP 522；未取得当前分类源目录。另用 11-05 的实际缓存目录，对 **community 7 源、blog 12 源，共 19 源**逐一只读拉取，每个源两次均 522。历史目录可能已变，不能把这些当成当前完整源集合。

- community：先知、奇安信、Seebug、t00ls、吾爱破解、InfoSec Write-ups、Critical Thinking 等已知源均失败，窗口内数量 **未知**。
- blog：历史目录 12 源（含长期旧源也做了尝试）均失败，48 小时及 7 天补充范围均 **无法筛选**。
- BugBounty：无法从 all 取得 HackerOne 等当窗记录，数量 **未知**。
- 已通过 X／官方研究恢复的内容放在对应节；它们不是 SecureFlow 采集成功的替代证明。失败证据：独立 backfill 中 `sf-*.meta.json`、`sf-cached-sources.json`。接口地址见末节。

## AI/TLDR 动态

回溯可恢复 **16 条独特链接**，其中 security **2 条**。这里按 `published` 落入本刊窗（均是日期标签的 00:00 UTC）归档；**原 routine 用 updated 的 24–36 小时窗口**，但当前 feed 和 11-22 缓存的 updated 随构建整体刷新，无法恢复 11-20／21 首次 updated、当时排序与完整候选。不能把这些数称作当日原始快照总数。未来改期／删除／被挤出的条目仍可能缺失。

本日主线是编码工具更新、开放小模型、AI 防护和数学研究声称。Signal 的隐私保护有可读官方原文；其余详情页换 UA＋Referer 后仍 403，以下清楚归因于 Atom 标题／摘要，不冒称已核验原文全文。

### 安全

- 〔本次新补采〕 **OpenAI Combatting Adversarial Distillation — new API safeguards for GPT-6.2 reasoning**：OpenAI 宣称加强 GPT-6.2 推理 API 的抗对抗蒸馏保护；本次仅可读 Atom 摘要，未验证保护效果。 链接（403，摘要可读）：https://ai-tldr.dev/releases/openai-combatting-adversarial-distillation/
- 〔本次新补采〕 **Signal blocks Siri AI and Gemini — screenshots off by default to stop AI agents**：Signal 宣布阻止 OS 级 AI 截取聊天画面；官方原文说明 Android 依赖可检测能力、macOS 不能同等阻止，关闭截图保护会增加会话泄露风险。已与当窗 X／官方博客交叉，不能说跨平台绝对防读。 链接（403，摘要可读）：https://ai-tldr.dev/releases/signal-blocks-os-ai-agents-screenshots/

### 模型

- 〔本次新补采〕 **Inkling 2 Mini — Thinking Machines' 26.4B looped open model for local use**：Thinking Machines 的 Inkling 2 Mini 被介绍为 26.4B、循环中间层的开放 MoE，面向本地使用。 链接（403，摘要可读）：https://ai-tldr.dev/releases/thinking-machines-inkling-2-mini/

### 工具与开源

- 〔本次新补采〕 **DreamCoder — a coding harness and IDE from the author of Mastering Emacs**：DreamCoder 把聊天、终端与审查并排放到键盘优先的编码工作区。 链接（403，摘要可读）：https://ai-tldr.dev/releases/masteringemacs-dreamcoder/
- 〔本次新补采〕 **Claude Code 2.1.330 — scheduled tasks run 30 days, charts with Easel**：Claude Code 2.1.330 的订阅摘要称定时任务可运行 30 天，加入 Easel 图表及企业登录。 链接（403，摘要可读）：https://ai-tldr.dev/releases/anthropic-claude-code-2-1-330/
- 〔本次新补采〕 **Codex CLI 0.171.0 — GPT-6.2 Sol becomes the default, TUI workspace on**：Codex CLI 0.171.0 的订阅摘要称默认切至 GPT-6.2 Sol，并开启工作区预览与子 agent transcript 视图。 链接（403，摘要可读）：https://ai-tldr.dev/releases/openai-codex-cli-0-171/

### 论文与研究

- 〔本次新补采〕 **Coding agents audit Masullo's 940-page Riemann claim in Lean**：开源项目使用编码 agent，逐行把 Masullo 的 940 页黎曼假设声称形式化到 Lean；这是核验项目，不是本刊确认该证明成立。 链接（403，摘要可读）：https://ai-tldr.dev/releases/mccorvie-riemann-masullo-lean/
- 〔本次新补采〕 **Scott Aaronson — 'The stochastic parrots have apparently proved' RH**：Scott Aaronson 对 AI 辅助黎曼假设证明发表评论；视为当时观点，不当作正式验证证据。 链接（403，摘要可读）：https://ai-tldr.dev/releases/scott-aaronson-stochastic-parrots-riemann-nov20/
- 〔本次新补采〕 **Unforced Navier–Stokes blowup — Buckmaster and Alpöge post an AI-aided proof**：Buckmaster 与 Alpöge 发布 AI 辅助、无外力 Navier–Stokes 爆破解的声称；未经本刊独立数学核验。 链接（403，摘要可读）：https://ai-tldr.dev/releases/buckmaster-alpoge-unforced-navier-stokes-blowup/
- 〔本次新补采〕 **MedChemBench — OpenAI's test of AI reasoning in medicinal chemistry**：MedChemBench 用分子与实验线索评估模型的药物化学推理；只记评测目的。 链接（403，摘要可读）：https://ai-tldr.dev/releases/openai-medchembench/
- 〔本次新补采〕 **Riemann Hypothesis proof claim — Anthropic's Levent Alpöge and Claude**：Anthropic 数学家 Alpöge 声称借助 Claude 得到黎曼假设证明；本标签日的摘要明确表示公开 Lean 文件尚待核验。 链接（403，摘要可读）：https://ai-tldr.dev/releases/anthropic-alpoge-riemann-hypothesis-claude-proof/

### 行业与评论

- 〔11-22 已补收〕 **Tim O'Reilly — What Happened to Silicon Valley, and to AI**：Tim O’Reilly 讨论 AI 依赖公共知识，却可能把这些公共资源变成私人收费通道。 链接（403，摘要可读）：https://ai-tldr.dev/releases/tim-oreilly-what-happened-to-silicon-valley/
- 〔11-22 已补收〕 **Mani Doraisamy — AI coding quietly promoted developers into architects**：文章认为 AI 写代码后，开发者的主要职责转向架构选择和设计判断；属于观点。 链接（403，摘要可读）：https://ai-tldr.dev/releases/mani-doraisamy-developers-into-architects/

### 视频与展示

- 〔本次新补采〕 **Fireship — 'If you've deployed anything since 2015, I have bad news...'**：Fireship 回顾一周三起网络安全事件；属于视频回顾，未独立核验视频全部论断。 链接（403，摘要可读）：https://ai-tldr.dev/releases/fireship-deployed-since-2015-bad-news-nov20/
- 〔本次新补采〕 **Vibecoding an inference chip — coding agents tune an FPGA to run an LLM**：工程师让 coding agent 持续优化 FPGA 推理设计；摘要宣称超越一台 CPU，本刊未复现基准。 链接（403，摘要可读）：https://ai-tldr.dev/releases/ankit-gupta-vibecoding-inference-chip/
- 〔本次新补采〕 **Sam Witteveen — 'Microsoft's Best AI Isn't a Model — It's a Harness'**：Sam Witteveen 认为 Ignite 发布里 agent harness 比单一模型更重要，属于评论。 链接（403，摘要可读）：https://ai-tldr.dev/releases/sam-witteveen-microsoft-harness-not-model-nov20/

Signal 官方原文（200）：https://signal.org/blog/protecting-your-privacy/
X 交叉证据：https://x.com/Dinosn/status/2123786210321830021


## Agent 用例动态

按 RSS pubDate 归属本窗，链接去重后 **18 条，全部列出**。当前 RSS 有 60 条；11-22 原始 XML 实为 60 个 item／60 个独特链接（旧解析文件误记 120）；两份不同时点的 feed 合并为 72 个独特链接。11-20 可恢复 18 条（其中 3 条仅在 11-22 缓存），11-21 为 20 条。原 11-22 解析文件的“66 条新条目”实际上只有 33 个独特链接、每条重复两次；本刊按原 XML／链接去重修正计数，不改写原刊。

主线是编程／CI 自动化和个人事务。尤其要注意同事会话日志、联网设备控制、常开助手的外发权限；百分比与节省时间均按案例作者或供应商自述处理。这些只是别人发布的用例，不是本任务在真实账户上执行它们的授权。

### 权限与安全

- 〔本次新补采〕 Microsoft 高管称用 Scout 保护家庭晚餐时段、记录双方承诺；曾发出格式不佳的邮件，说明常开助手仍需审阅外发内容。 https://agentusecases.ai/use-case/protect-family-time-and-log-commitments-with-an-always-on-ag
- 〔本次新补采〕 用户用 Claude Code 发现局域网 Kasa 插座并设置灯光定时；涉及网络发现和设备控制，应限于自有设备。 https://agentusecases.ai/use-case/find-and-automate-a-smart-plug-with-timers
- 〔本次新补采〕 安全人员在 brotli2bitcoin 挑战中编排 agent，报告 37 分钟完成；只记授权挑战事实，不复制利用实现或步骤。 https://agentusecases.ai/use-case/develop-a-working-exploit-for-a-security-challenge-with-agen
- 〔本次新补采〕 工程师先搜索自己的 agent 会话日志，后希望搜索同事日志；这是权限边界风险，不能把想法当作已获授权的跨人访问。 https://agentusecases.ai/use-case/search-coworkers-agent-session-logs

### 编程与工程

- 〔本次新补采〕 Nubank 使用 Devin 拆分大规模 ETL 单体；“周代替月、成本省 20 倍”是供应商案例主张，未复测。 https://agentusecases.ai/use-case/migrate-a-multi-million-line-etl-monolith-into-sub-modules
- 〔本次新补采〕 Ramp 用 Devin 提交移除陈旧 feature flag 的 PR，并处理 flaky test／CI；属于供应商案例。 https://agentusecases.ai/use-case/remove-stale-feature-flags-and-fix-ci-via-automated-prs
- 〔本次新补采〕 评测者让 Replit Agent 3 构建分账应用并做浏览器测试；约 8 分钟完成，但也指出慢和成本风险。 https://agentusecases.ai/use-case/build-a-bill-splitting-app-with-browser-testing
- 〔本次新补采〕 评测者让 Replit Agent 3 实现认证与 feed 的社交功能，自主运行 193 分钟；长运行不等于代码已安全。 https://agentusecases.ai/use-case/build-a-social-networking-feature-with-auth-and-feeds
- 〔本次新补采〕 用户用 Cursor Agent 在 14 个文件迁移 NextAuth.js，手工修 3 处；背景 agent 首轮 34 个测试通过 28 个。 https://agentusecases.ai/use-case/migrate-dashboard-auth-to-nextauth-js-and-generate-tests
- 〔本次新补采〕 开发者用 Copilot 增补 GitHub Action 文档、元数据和输入验证，并修复自己的 CI 失败。 https://agentusecases.ai/use-case/add-docs-metadata-fixes-and-validation-to-a-github-action-re
- 〔本次新补采〕 用户把约 15 个 Sentry 缺陷交给 Copilot，称约六成无需帮助；也记录了它对失败测试自信误判。 https://agentusecases.ai/use-case/send-sentry-bugs-to-copilot-as-github-issues-for-fixing
- 〔本次新补采〕 用户用 Copilot 写单测并接入审查／失败分析，声称 CI 失败率从 18% 降到 9%；未独立验证。 https://agentusecases.ai/use-case/write-unit-tests-and-add-ai-review-to-a-ci-cd-pipeline
- 〔本次新补采〕 .NET 团队分享用 Copilot coding agent 写测试的经验，也指出旧框架兼容和 CI 失败问题。 https://agentusecases.ai/use-case/use-copilot-coding-agent-to-write-tests-in-dotnet-runtime

### 办公与研究

- 〔本次新补采〕 Bluesky 团队通过 diderot 的 Slack／Discord、CLI 与 MCP 回答团队问题；摘要未说明底层查询对象，不补造。 https://agentusecases.ai/use-case/answer-team-questions-through-a-slack-discord-bot-cli-and-mc

### 出行与个人事务

- 〔本次新补采〕 用户称 Claude Code 协助旅行预订并生成含票据与航班号的行程网站／打印指南；这类文件需控制分享范围。 https://agentusecases.ai/use-case/plan-and-book-a-vacation-with-a-travel-website-and-guide
- 〔本次新补采〕 家长用 Claude 规划孩子大学访校公路旅行、航班选项、联系人和课程安排。 https://agentusecases.ai/use-case/map-out-a-road-trip-for-college-tours
- 〔本次新补采〕 用户把账单／续费通知交给 ChatGPT 标出费用并写协商电话提纲，不是 agent 已代打电话。 https://agentusecases.ai/use-case/flag-fees-and-script-calls-to-negotiate-lower-bills
- 〔本次新补采〕 用户称 Claude 帮写瑕疵笔记本退货法律通知、48 小时内退款；个案不保证同样结果。 https://agentusecases.ai/use-case/draft-a-legal-notice-to-get-a-defective-laptop-refunded


## 地址／IoC 汇总

### Cairn 行动地址（原样，非点击格式）

原始来源 AWS：https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/

AWS 给出的观测期为 **2026-09-08 至 09-10**（源文只有日期，无可转换的时分），本次于上列 HKT 补采时核验。不是 11-20 才开始活跃的地址，也不是“当前必然恶意”的判定。

| 原样 IoC | 备注 |
|---|---|
| `142[.]4.98.145` | AWS Indicators of compromise 原文 |
| `142[.]4.107.34` | 同上 |

Bell 的 IoC 未公开，仅对客户／CCCS 分享；其余本刊条目未见本次可核证的公开攻击指标，不从截图或二手帖猜哈希／IP。软件版本、CVE、文章域名不是攻击 IoC。

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

本窗：独特 X 候选 393，LWiS 271；List 最早／最晚实际帖子为 2026-11-19T23:12:18.000Z 至 2026-11-20T22:48:52.000Z（UTC 原始证据；同区间香港为 11-20 07:12:18 至 11-21 06:48:52 HKT）。这是当前可见帖子范围，不是失败 run 快照。

| X 查询组 | 实得条数 | 原始 created_at 区间（UTC；香港加 8 小时） |
|---|---:|---|
| 20-cve-high.json | 25 | 2026-11-19T23:45:37.000Z → 2026-11-20T19:59:11.000Z；香港 11-20 07:45:37 HKT → 11-21 03:59:11 HKT |
| 20-cve-latest.json | 25 | 2026-11-20T22:55:39.000Z → 2026-11-20T22:59:29.000Z；香港 11-21 06:55:39 HKT → 11-21 06:59:29 HKT |
| 20-cve-relevancy.json | 25 | 2026-11-19T23:06:02.000Z → 2026-11-20T22:07:24.000Z；香港 11-20 07:06:02 HKT → 11-21 06:07:24 HKT |
| 20-threat-latest.json | 25 | 2026-11-20T19:22:39.000Z → 2026-11-20T22:58:43.000Z；香港 11-21 03:22:39 HKT → 11-21 06:58:43 HKT |
| 20-threat-relevancy.json | 25 | 2026-11-19T23:37:24.000Z → 2026-11-20T22:58:43.000Z；香港 11-20 07:37:24 HKT → 11-21 06:58:43 HKT |
| 20-tools-latest.json | 2 | 2026-11-20T03:48:09.000Z → 2026-11-20T04:55:54.000Z；香港 11-20 11:48:09 HKT → 11-20 12:55:54 HKT |

- X 搜索：https://x.com/search?q=%28CVE%20OR%20POC%20OR%20exploit%20OR%200day%29%20-is%3Aretweet%20since%3A2026-11-19_23%3A00%3A00_UTC%20until%3A2026-11-20_23%3A00%3A00_UTC&f=live

- X 搜索：https://x.com/search?q=github.com%20%28C2%20OR%20%22red%20team%22%20OR%20nuclei%29%20-is%3Aretweet%20since%3A2026-11-19_23%3A00%3A00_UTC%20until%3A2026-11-20_23%3A00%3A00_UTC&f=live

- X 搜索：https://x.com/search?q=%28%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%29%20-is%3Aretweet%20since%3A2026-11-19_23%3A00%3A00_UTC%20until%3A2026-11-20_23%3A00%3A00_UTC&f=live

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

ExploitGrid 本窗 93 条，HIGH／CRITICAL 76 条，去重 CVE 数 67。同批包含老 CVE 重复项目、检测器和实验室；仅展开有当窗交叉证据或高风险新披露的条目。所有候选的 date、internalId、CVE 及软件字段都保存在 `eg-ledger.json`。

### 核验与交付说明

- 主来源 HTTP 状态、最终地址、抓取时间、SHA256 和重试在独立 backfill 的 `*.meta.json`；X ID／作者／created_at／原帖地址保存在 `x-all.json`，各组原始结果独立保存。
- 无 `t.co` 短链接出现在成稿；使用帖实体展开地址。403／400／522 不伪称 200；最终链接抽查台账见覆盖说明及 `report-link-check.json`。HTTP 404 的主链接需替换或删除后交付。
- `2026-11-20_21-backfill-coverage.md` 是跨两刊覆盖与缺口总表。没有修改 seen_ids、last_report_date、profile、技能、routine，未直接外发消息。

最终链接核验：两刊合计 181 个独特 https URL；114 个 HTTP 200、32 个原帖 ID 经 X 工具核验、7 个列表／搜索参考 URL；24 个 403（23 个 AI/TLDR 详情＋1 个 Medium）、3 个 SecureFlow 522 均已注明；AWS Ruby 公告脚本传输中断后由公共 WebFetch 读取核对。没有 404 主链接。检验基于当前可读性，不是当日可用性证明。

Box：`/home/box/workspace/security-watch/reports/2026-11-20-x-security-digest-supplement.md`
本机副本目标：`/Users/kenny1337/Desktop/_05_项目/X安全情报晚报/2026-11-20-x-security-digest-supplement.md`。复制／读回结果以覆盖台账的最终交付状态为准。
