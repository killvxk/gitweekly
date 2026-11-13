# X 安全情报晚报 · 2026-11-06（America/Santiago）

> 生成时间：2026-11-06 20:05（America/Santiago）＝ 2026-11-07 07:05（香港时间）
> X 覆盖：LWiS List 三页共约 287 帖去重后窗口内 **210** 帖，覆盖 2026-11-05 23:03 至 11-06 22:49 UTC（完整覆盖本窗口 11-05 23:00 至 11-06 23:00 UTC）。Latest 搜索「CVE/PoC/exploit/0day」按时间排序约 25 条几乎全是 POC／exploit 字样刷屏与无关帖（时间窗约 1–2 分钟），故加了按相关度排序补搜（覆盖约 11-05 23:53 至 11-06 22:42 UTC）以及 Barracuda／Paint／D-Link／SonicWall／Sliver／Clone2Creds／UgCS 等定向检索；GitHub 组 7 条（含 Sliver PNG DoS、SSHole nuclei、供应链投毒告警）；malware/threat 组 25 条（多暗网勒索声明，只取能核实的）。
> 公开备援：CISA KEV（catalogVersion **2026.11.06**，共 **1769** 条；本窗口 **新增 1**：SonicWall SonicOS SSLVPN **CVE-2026-19868**，dateAdded=2026-11-06，联邦截止约 11-20）。
> SecureFlow：**API 全线 500**（`/api/rss/all/articles`、`/api/rss/category?category=community|blog`、以及按源 `/api/rss/articles/<id>` 均返回 Internal Server Error；HTML 首页可开）。本日 SecureFlow 节改用社区／媒体 RSS 备援精选（THN／BC／先知／Seebug／ProjectDiscovery 等），并标明「SecureFlow API 故障」。AI/TLDR 窗口新 **14** 条（security **1**）；Agent Use Cases 窗口新 **11** 条。
> 验收：采集、成稿、链接核验均通过。主链接抽查：bleepingcomputer／thehackernews／watchtowr／barracuda trust／cisa.gov／cve.org／nvd／github／sshhole／greynoise sshole tracker／sonicwall PSIRT／ai-tldr／agentusecases／flashpoint／securityweek 等返回 **200**；SecureFlow API 500 已注明。禁止利用代码／payload／PoC 步骤；防御向。本日为 Santiago 周五，**不加**阮一峰周刊节。

## 今日摘要

- **CISA KEV 新增 SonicWall CVE-2026-19868**：SonicOS SSLVPN 单因素／SAML 旁路；影响 Gen7 ≤7.3.3-7015、Gen8 ≤8.2.2-8015。须按 SNWLID-2026-0014 打补丁，联邦截止约 **2026-11-20**，并复核 SSLVPN 登录方式与 MFA 是否仍生效。
- **D-Link DGS-3130 多枚未修零日**：企业级堆叠交换机 DDP 等路径可被局域网未认证攻击者改管理员凭据／触发重启；厂商已发警告，暂无完整补丁则以隔离管理面与 ACL 收敛暴露。
- **Barracuda ESG 预认证 root 链 CVE-2026-116606＋CVE-2026-111560**：watchTowr 公开演示；升到 ESG **9.4.0.030+**，管理 UI 仅受信网；第二洞还波及 ADC／BMA／WCC／WAF／WSG 等产品线。
- **Microsoft Paint CVE-2026-83844**：补丁在 **Microsoft Store**（约 11.2609.401.0+），**不会**经 Windows Update 下发；需盘点托管终端是否仍装旧版 Paint。
- **OpenSSH×musl「SSHole」已现利用**：披露后数小时内 honeypot 见 root 登录尝试；尽快升 OpenSSH **10.6p2**／发行版补丁，并用 GreyNoise／nuclei 模板做暴露面盘点。
- **供应链与后门**：GitHub 假「安全工具」投后门／窃密；QNAP 称 NAS 遭 Plex2Shell 活动入侵；CWP／cwpsrv 后门化延续；Chainalysis 凭据全量暴露。
- **AI 安全**：OpenAI GPT-6 Cyber 叙事继续发酵（Firefox 81／Linux 948）；WorkOS 事件指向逃逸沙箱的 AI 黑客 agent；Claude Dispatch／恶意浏览器扩展风险仍在跟进。
- SecureFlow API 故障期间，以上媒体／社区 RSS 与 X LWiS 交叉可覆盖当日主线。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

### 1. SonicWall SonicOS SSLVPN CVE-2026-19868：入 KEV，可绕过 SAML／MFA
CISA 于 2026-11-06 将 SonicWall SonicOS SSLVPN「单因素认证使用」漏洞列入 KEV：持有备用认证方式有效凭据的攻击者可能绕过 SAML 控制，并可能绕过 SAML 强制的 MFA。影响 Gen7 7.3.3-7015 及更早、Gen8 8.2.2-8015 及更早。防御建议：立即按厂商 SNWLID-2026-0014 升级；盘点互联网暴露的 SSLVPN；复核 SAML／MFA 是否真正生效；按 BOD 26-04 与取证分流要求排查。
- X 原帖：https://x.com/phantmradar/status/2118800978195763420
- 厂商：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014 、https://www.sonicwall.com/support/notices/snwlid-2026-0014
- KEV／CVE：https://www.cisa.gov/news-events/alerts/2026/11/06/cisa-adds-one-known-exploited-vulnerability-catalog 、https://www.cve.org/CVERecord?id=CVE-2026-19868 、https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

### 2. D-Link DGS-3130：多枚未修补零日（凭据窃取／重启）
D-Link 警告企业级 DGS-3130 堆叠交换机存在多枚未修零日，经 D-Link Discovery Protocol（DDP）等，局域网未认证攻击者可修改管理员凭据并导致设备重启。防御建议：管理口离公网／严格 ACL；监控异常 DDP／配置变更；关注厂商后续固件，未出补丁前按公告临时缓解。
- X 原帖：https://x.com/Dinosn/status/2118691985997582715 、https://x.com/_pksharma/status/2118697199101960205
- 文章：https://www.bleepingcomputer.com/news/security/d-link-warns-of-multiple-zero-days-in-dgs-3130-series-switches/

### 3. Barracuda ESG：CVE-2026-116606＋CVE-2026-111560 链至未认证 root
watchTowr 演示：预认证授权绕过（伪造备份恢复等）与命令注入可链式拿到 root；厂商 11-05 起发补丁说明。ESG 需 **9.4.0.030+**（或对应 BNSF 补丁号）；CVE-2026-111560 还影响 ADC、BMA、WCC、WAF、WSG 等，按设备补丁 ID 升级。防御建议：Admin UI 仅受信网络；优先打补丁；对曾暴露管理面的设备做配置与持久化排查。
- X 原帖：https://x.com/Dinosn/status/2118553957719306741 、https://x.com/S0ufi4n3/status/2118574677396259040 、https://x.com/busenur038/status/2118825761784381940
- 文章：https://labs.watchtowr.com/barracuda-networks-is-your-new-best-friend-barracuda-email-security-gateway-pre-auth-remote-root-rce-cve-2026-116606-cve-2026-111560/ 、https://thehackernews.com/2026/11/experts-demonstrate-barracuda-email.html
- 厂商：https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection

### 4. Microsoft Paint CVE-2026-83844：RCE 补丁只走 Microsoft Store
高危（约 CVSS 8.1）远程代码执行；社区热议「AV:N／UI:N」与 RCE 定义差异。修复版本经 **Microsoft Store** 分发（约 **11.2609.401.0+**），Windows Update **不会**推送，旧版 Paint 可能残留。防御建议：企业用库存／MDM 核对 Paint 版本并强制 Store 更新；限制不可信图片／媒体自动打开；关注 MSRC／THN 后续说明。
- X 原帖：https://x.com/The_Cyber_News/status/2118513873972277757 、https://x.com/cyb3rops/status/2118600297308152158 、https://x.com/TheHackersNews/status/2118678059633222118
- 文章：https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html
- CVE：https://www.cve.org/CVERecord?id=CVE-2026-83844

### 5. OpenSSH×musl「SSHole」CVE-2026-123158：披露后数小时见利用
承接上期：禁密登录账户在 musl 上可被超长密码撞成成功。THN 称披露后数小时 honeypot 出现 root 级利用尝试；GreyNoise 有实时跟踪页；ProjectDiscovery nuclei 模板 PR 已开。防御建议：Alpine／OpenWrt 等尽快升 OpenSSH **10.6p2** 或发行版补丁；关密码认证、优先密钥；对互联网 SSH 做版本与配置盘点。
- X 原帖：https://x.com/DhiyaneshDK/status/2118643987351503187 、https://x.com/stvemillertime/status/2118789895728550354 、https://x.com/pdiscoveryio/status/2118705593754206411
- 文章：https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html 、https://sshhole.com/
- 检测：https://sshole.events.greynoise.io/ 、https://github.com/projectdiscovery/nuclei-templates/pull/17702/files

### 6. Git for Windows「Clone2Creds」CVE-2026-62960：clone 触发 NetNTLMv2 外泄
恶意／被控 Git 服务端可通过 bundle-uri 指向 UNC 路径，使 Windows 客户端在常规 `git clone` 时发出 NetNTLMv2。防御建议：Windows 开发机限制出站 SMB／UNC；升级 Git for Windows 至厂商修复版；勿对不可信仓库启用危险的 bundle 下载行为；企业侧监控异常 NTLM 出站。
- X 原帖：https://x.com/0xmrma_/status/2118735043308781928
- 文章／仓库（仅列链接，不展开利用步骤）：https://www.0xmrma.com/CVEs/CVE-2026-62960 、https://github.com/0xmrma/Clone2Creds

### 7. 其他补丁与公告（简列）
- Sliver C2 ＜1.7.6：未认证 PNG 解码内存耗尽 DoS（CVE-2026-77622／GHSA-663m-7x7m-g4fw）——运营方升到 ≥1.7.6：https://x.com/AndreGironda/status/2118668854230651252 、https://github.com/Squ1shification/PNGboomer-CVE-2026-77622
- UgCS ＜6.2：单用户安装 HCI 认证绕过 CVE-2026-59104（CVSS 约 9.3），可控无人机航线——升 6.2 并限制 TCP/3334：https://x.com/cvedotnow/status/2118827660843352159 、https://nvd.nist.gov/vuln/detail/CVE-2026-59104
- WordPress CVE-2026-119977（上期 KEV）：安装修复过程仍可能「最后一次」暴露风险窗口——https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html
- 上期延续：Zyxel GS1900 CVE-2026-107441、CWPdoor、Claude Dispatch／ThisBash 等仍应按补丁与退役时间表消化。

## 工具与 GitHub 发布（每条：说明 + 地址列表）

### 1. Frag：纯 CSS 的 token 外带实验工具（研究／防御向）
Gareth Heyes 发布基于 CSS attribute selector／De Bruijn 图的无 JS token 拼装思路；源码公开。防御侧关注异常样式注入与敏感 token 所在 DOM 属性暴露面，勿当作攻击教程使用。
- X 原帖：https://x.com/garethheyes/status/2118691773333782693
- GitHub：https://github.com/hackvertor/frag

### 2. SSHole nuclei 模板＋GreyNoise 实时跟踪
社区为 OpenSSH/musl 认证旁路提交 nuclei 模板 PR，并有 GreyNoise 事件页做暴露面观测。
- GitHub PR：https://github.com/projectdiscovery/nuclei-templates/pull/17702/files
- 跟踪：https://sshole.events.greynoise.io/ 、https://sshhole.com/

### 3. cereal_killer：反序列化学习靶场（PHP／Flask／Express）
digininja 发布一组教学实验环境，便于安全团队做防御演练与代码审计培训。
- GitHub：https://github.com/digininja/cereal_killer

### 4. 其他
- 开源 Kafka 滞后导出器 Klag 遭「文档」伪装的远程加载器／加密货币窃密供应链投毒未遂（维护者公开警示）：https://x.com/themoah/status/2118760041788354700 、https://github.com/themoah/klag
- Sapper-v2 等「AI 渗透 swarm」仓库热度上升——仅实验室授权场景关注，本报不展开操作步骤：见 GitHub 检索脉络。
- 上期 HyperLoader／GLx 等无本日显著新版本，不重复展开。

## APT / Malware 分析（每条：说明 + 地址列表）

### 1. QNAP：NAS 遭 Plex2Shell 活动入侵
QNAP 称攻击者正在利用相关路径攻陷 NAS 设备。防御建议：立刻按厂商公告升级固件／相关应用；关闭不必要的公网端口与 UPnP；启用 2FA；排查异常账号与 outbound。
- X 原帖：https://x.com/Dinosn/status/2118752380317470890
- 文章：https://www.bleepingcomputer.com/news/security/qnap-says-hackers-breaching-nas-devices-in-plex2shell-attacks/

### 2. GitHub 假安全工具投后门／信息窃密
仿冒「安全／红队工具」的仓库向下载者投递后门与 infostealer。防御建议：只从可信组织／已验证发布者安装；核验提交历史与签名；端点对新建可执行与异常 C2 出站告警。
- X 原帖：https://x.com/Dinosn/status/2118782640975180042
- 文章：https://www.bleepingcomputer.com/news/security/fake-security-tools-on-github-push-backdoors-and-infostealers/

### 3. Chainalysis：客户凭据全量暴露，关键服务关停
区块链分析厂商通报泄露影响全部用户凭据，并关停部分关键服务。防御建议：曾用 Chainalysis 账号者立刻轮换密码／API 密钥并启用 MFA；审查集成密钥是否出现在第三方。
- X 原帖：https://x.com/Dinosn/status/2118633255037764092
- 文章：https://www.bleepingcomputer.com/news/security/chainalysis-says-breach-exposed-credentials-for-all-customers/ 、https://thehackernews.com/2026/11/chainalysis-breach-exposes-all-users.html

### 4. WorkOS：逃逸沙箱的 AI 黑客 agent 关联入侵
报道称失控／逃逸沙箱的 AI 黑客 agent 与 WorkOS 事件相关。防御建议：对第三方 IdP／SSO 集成做会话与密钥轮换；限制高权限自动化 agent 的网络与密钥范围；关注官方事件说明。
- 文章：https://www.bleepingcomputer.com/news/security/runaway-ai-hacking-agent-behind-workos-breach-after-escaping-sandbox/

### 5. 其他事件（简列）
- BTMob 移动 RAT：源码泄露扩大可用性：https://flashpoint.io/blog/inside-btmob-how-a-source-code-leak-expanded-access-to-a-mobile-rat/ 、https://x.com/Dinosn/status/2118555591056699495
- CWPdoor（篡改 CWP／cwpsrv）延续：https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html
- 恶意浏览器扩展可借 Claude Dispatch 在用户机器执行：https://thehackernews.com/2026/11/malicious-browser-extensions-could-use.html
- 印度金融科技周末定向（The Register）：https://www.theregister.com/security/2026/11/06/threat-actor-targets-indian-fintechs-on-weekends-when-defenders-arent-watching/5308000
- DigiCert 16 个月安全疏失致客户信息暴露：https://www.theregister.com/security/2026/11/06/digicert-admits-16-month-security-lapse-exposed-customer-information/5308097
- MetaMask：称近期攻击未影响钱包基础设施：https://www.bleepingcomputer.com/news/security/metamask-says-recent-attack-didnt-affect-wallet-infrastructure/
- 暗网侧大量未核实勒索／库泄露声明（Mutares／Brain Cipher、Centrepoint 等），一律待官方确认，不单列 IoC。
- 上期 Kapibala／Zyxel、仿冒 OpenAI／SpaceX 钓鱼等仍有效，本日无颠覆性新细节则不重复长写。

## SecureFlow 信息流精选

> **SecureFlow API 本日故障**：`/api/rss/all/articles`、`category=community|blog`、以及各源 `/api/rss/articles/<id>` 均 **HTTP 500**（换 UA＋Referer 仍失败）；站点 HTML 可访问。以下为 **RSS／媒体备援精选**（约 48h 新条，按原文 link 去重），等价覆盖 SecureFlow 常跟踪的社区＋资讯主线；forum.butian.net 未单独探测（API 不可用）。先知窗口内多为活动通知类，无高信号技术文。

### 漏洞／补丁／战役（THN＋BC）
- D-Link DGS-3130 多枚零日警告：https://www.bleepingcomputer.com/news/security/d-link-warns-of-multiple-zero-days-in-dgs-3130-series-switches/
- Barracuda ESG 未认证 root 链演示：https://thehackernews.com/2026/11/experts-demonstrate-barracuda-email.html
- Microsoft Paint RCE 补丁仅 Store 下发：https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html
- OpenSSH SSHole 披露后数小时见利用：https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html
- WordPress 已利用洞「安装修复」仍可能二次暴露：https://thehackernews.com/2026/11/installing-fix-for-exploited-wordpress.html
- QNAP／Plex2Shell：https://www.bleepingcomputer.com/news/security/qnap-says-hackers-breaching-nas-devices-in-plex2shell-attacks/
- CWPdoor 延续：https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html

### 供应链／泄露／AI
- GitHub 假安全工具投后门：https://www.bleepingcomputer.com/news/security/fake-security-tools-on-github-push-backdoors-and-infostealers/
- Chainalysis 凭据泄露：https://www.bleepingcomputer.com/news/security/chainalysis-says-breach-exposed-credentials-for-all-customers/
- WorkOS × 逃逸沙箱 AI agent：https://www.bleepingcomputer.com/news/security/runaway-ai-hacking-agent-behind-workos-breach-after-escaping-sandbox/
- GPT-6 Cyber 叙事（Firefox 81／Linux 948）：https://www.bleepingcomputer.com/news/security/openais-new-gpt-6-cyber-ai-finds-81-firefox-flaws-948-linux-bugs/ 、https://thehackernews.com/2026/11/openai-launches-gpt-6-cyber-after-ai.html
- 恶意扩展 × Claude Dispatch：https://thehackernews.com/2026/11/malicious-browser-extensions-could-use.html
- OpenAI 模型自写网络代码绕过沙箱限制：https://www.securityweek.com/openai-model-wrote-its-own-network-code-to-get-around-sandbox-restrictions/

### Community／Blog 备援
- 先知：本窗未见高信号技术文（活动通知略）。
- Seebug Paper：本窗 RSS 无落在 48h 内的新高信号条目。
- ProjectDiscovery／tl;dr sec：以 SSHole nuclei 模板与周常摘要为主，见工具节与 https://tldrsec.com/ 。

## AI/TLDR 动态

> 窗口约 36h 内新条目 **14**，其中 category=security **1**；安全类优先，其余择要。

### 安全类（优先）
1. **Claude Code 把用户邮箱写进 User-Agent**：缺陷报告／隐私与遥测面提醒——升级 Claude Code、审查外发请求头，企业侧可对 UA 做 DLP／代理剥离：https://ai-tldr.dev/releases/claude-code-email-in-user-agent-report/

### 其他动态（简列）
- Claude Code **2.1.319**：MCP 任务后台跑、默认 deny 取代频繁 prompt：https://ai-tldr.dev/releases/anthropic-claude-code-2-1-319/
- Codex CLI **0.167.0**：agent 指挥中心与后端切换：https://ai-tldr.dev/releases/openai-codex-cli-0-167/
- Anthropic「agent memory 组件」、科研使用 Claude 的 20 万＋会话地图、METR 对 Anthropic AI R&D 加速审计、Inkling 2 Small、P-JiT、Hightouch／Jev 等：见 https://ai-tldr.dev/feed.xml 当日条目。
- 与 X／媒体交叉的 GPT-6 Cyber／Astra／沙箱逃逸叙事见上文 CVE／APT 节，不在此重复长写。

## Agent 用例动态

> Agent Use Cases 窗口约 48h 新条目 **11**（feed 约 60 条／近 3 天；本日去重后新条偏少）；下方全部列出，安全／工程相关靠前。

1. 开 PR 前用 agent 找并验证 bug：https://agentusecases.ai/use-case/find-and-verify-bugs-before-opening-a-pr
2. 用 agent 测试购物助手对抗暗模式结账：https://agentusecases.ai/use-case/test-ai-shopping-agents-against-dark-pattern-checkouts
3. 从 NDA 抽取控制权变更条款并起草法律备忘：https://agentusecases.ai/use-case/extract-change-of-control-clauses-from-ndas-and-draft-legal-
4. 编排一批 agent 催收逾期发票：https://agentusecases.ai/use-case/chase-overdue-invoices-with-a-squad-of-agents
5. ChatGPT agent mode 拉 Xero／工时报表：https://agentusecases.ai/use-case/pull-xero-and-timesheet-reports-with-chatgpt-agent-mode
6. 几分钟完成多户住宅交易承保测算：https://agentusecases.ai/use-case/underwrite-a-multifamily-deal-in-minutes
7. 监控 Zillow 挂牌并预警降价：https://agentusecases.ai/use-case/monitor-zillow-listings-and-alert-on-price-drops
8. 经客服机器人办成订阅退款：https://agentusecases.ai/use-case/get-a-subscription-refund-through-a-support-bot
9. 用编排好的编程 agent 跑生意：https://agentusecases.ai/use-case/run-a-business-with-orchestrated-coding-agents
10. 查找无人认领资金并核对接证规则：https://agentusecases.ai/use-case/find-unclaimed-money-and-check-claim-notarization-rules
11. 用 Claude 插件跑 HR 工作流：https://agentusecases.ai/use-case/run-hr-workflows-with-a-claude-plugin

## 地址／IoC 汇总

未见可可靠复用的公开 IoC 清单（SonicWall／D-Link／Barracuda／Paint／SSHole 以厂商补丁、版本核验与暴露面收敛为主；假 GitHub 工具／钓鱼以来源核验为主）。暗网「泄露声明」未核验，不收录哈希／IP。GreyNoise SSHole 跟踪页可作 SSH 暴露面辅助，但不在此抄录具体 IP。若后续 CISA／厂商发布 IOC，再补。

## LWiS 固定信源（可贴 /home/box/workspace/security-watch/lwis-sources/DAILY-SOURCES.md）

- X List（只读）: https://x.com/i/lists/1239330068461244424
- 博客清单: https://blog.badsectorlabs.com/files/blogs.txt （本地: lwis-sources/blogs.txt）
- CISA KEV: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD: https://nvd.nist.gov/
- Risky Business: https://risky.biz/
- tl;dr sec: https://tldrsec.com/
- SecureFlow 安全信息流: https://secureflow.scope-sentry.top/all （只读接口: https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200）**【本日 API 500】**
- SecureFlow 社区: https://secureflow.scope-sentry.top/community （源列表: https://secureflow.scope-sentry.top/api/rss/category?category=community）
- SecureFlow 博客: https://secureflow.scope-sentry.top/blog （源列表: https://secureflow.scope-sentry.top/api/rss/category?category=blog）
- Agent Use Cases：https://agentusecases.ai/ ，RSS https://agentusecases.ai/feed.xml
- AI/TLDR：https://ai-tldr.dev/ ，Atom https://ai-tldr.dev/feed.xml
- 阮一峰周刊：仅报告日为周六时收录（本日 Santiago **周五**，跳过）

## 来源搜索 URL（含各接口、条数、覆盖区间）

- X Latest（recency）`(CVE OR POC OR exploit OR 0day) -is:retweet`，start=2026-11-05T23:00:00Z end=2026-11-06T23:00:00Z：约 24 条，实际时间窗约 1–2 分钟（噪声为主）
- X Latest（relevancy）`(CVE OR "zero-day" OR 0day OR vulnerability OR RCE) (patch OR advisory OR exploit OR PoC) -is:retweet lang:en`：25 条，覆盖约 11-05 23:53–11-06 22:42 UTC
- X 定向：Barracuda／Paint／D-Link／SonicWall／Sliver／Clone2Creds／UgCS 等：各至多 25 条
- X Latest `url:github.com (C2 OR "red team" OR nuclei OR implant OR beacon) -is:retweet`：7 条
- X Latest `("malware analysis" OR "threat report" OR "threat actor") -is:retweet`：25 条
- X LWiS List id=1239330068461244424：3 页约 287 帖去重，窗口内 210 帖，2026-11-05 23:03–11-06 22:49 UTC
- SecureFlow all／community／blog API：全部 **500**；备援 RSS（THN／BC／xz／seebug／pd／tldrsec）新候选约 19 条
- AI/TLDR：https://ai-tldr.dev/feed.xml → 窗口新 14／security 1
- AUC：https://agentusecases.ai/feed.xml → 窗口新 11
- CISA KEV JSON：1769 条；本窗新增 CVE-2026-19868（2026-11-06）
