# X 安全情报晚报 · 2026-11-07（America/Santiago）

> 生成时间：2026-11-07 20:14（America/Santiago）＝ 2026-11-08 07:14（香港时间）
> X 覆盖：Latest 多路检索去重后窗口内保留约 **418** 帖 + LWiS List 两页窗口内 **50** 帖（List 原始拉取约 186），合计唯一约 **468**；覆盖约 **2026-11-06 23:00 → 2026-11-07 23:00 UTC**（约 24h，窗口目标约 24.2h）。
> 公开备援：CISA KEV（catalogVersion **2026.11.06**；近日 3 条含 SonicWall **CVE-2026-19868** dateAdded=2026-11-06，昨报已详述，今日跟进）。
> SecureFlow：**API 全线 500**（`/api/rss/all/articles`、`category=community|blog` 均 Internal Server Error；HTML SPA 可开）。本日改用同源公开 RSS 备援精选：all≈**2**、community≈**0**、blog≈**18**（合计高信号约 20；ZDI 新公告为主，另含 THN／Cloudflare／tl;dr sec）。forum.butian.net box 侧 403。AI/TLDR 窗口新 **6**（security **0**）；Agent Use Cases 窗口新 **25**。
> 周末版：含阮一峰《科技爱好者周刊》第 **418** 期。验收：采集、成稿、链接核验均通过。主链接抽查见 `raw/2026-11-07/link_check.json`（50 条；阮一峰官网 box 侧换 UA+Referer 仍 **403**，保留并注明，本地已有 HTML 缓存）。禁止利用代码／payload／PoC 步骤；防御向。

## 今日摘要

- **Claude Code「Don't Ask Again」设置文件泄露**：Apiiro／THN 称约 **1122** 份公开 GitHub 副本里残留命令行明文密码／API 密钥；审查仓库中 Claude 项目设置、轮换已暴露密钥，避免把含密命令写入「不再询问」白名单。
- **samcurry 新文：ForgeRock 路径混淆→RCE，以及 hosting 侧 WARDOGS 二进制外泄**：与 @infosec_au 汽车远程控制故事交叉；身份／车联／托管面需按文盘点暴露与补丁，本报不写利用步骤。
- **Firecracker VM Escape（PwnEscape Part 2）**：pwn.ai 公开研究文章；云／多租户侧关注 microVM 隔离边界与厂商补丁节奏。
- **MyCERT：C3RB3R 勒索大规模加密公网暴露的旧版 Synology NAS**：厂商催更 DSM；关闭不必要公网端口、启用 2FA、核验备份离线可用性。
- **Microsoft Entra Device Registration 提权 CVE-2026-109469**、**Zscaler Client Connector RCE CVE-2026-59568**：分别跟进身份注册面与企业 ZTNA 客户端补丁。
- **CISA 继续推 SonicWall CVE-2026-19868 KEV**（昨报已详）：按 SNWLID-2026-0014 打补丁，联邦截止约 11-20。
- **工具向**：keyeroo（NTLM→LDAP 操作研究／红队工具）、Mythic v4 预告直连 RDP／VNC；**防御提示** GitHub 假安全工具藏 payload（不写步骤）。
- SecureFlow 备援：ZDI 一批 Pwn2Own／LibreOffice／Docker Sandboxes／Philips Hue／OriginLab 等公告；Cloudflare vole-mole 后量子隐私、Zero Wire；tl;dr sec #353。
- 交叉：MetaMask 基础设施事件（SCWorld）、WorkOS×逃逸沙箱 AI agent（昨报已覆盖，一句交叉）、法国经服务商通路约 $1.33 亿银行盗窃报道。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

### 1. Claude Code「Don't Ask Again」：公开仓库泄露密码／密钥
当用户对含密命令选择「Yes, and don't ask again」时，命令可被原样写入项目设置文件；Apiiro 称 GitHub 上可见约 **1122** 份公开副本含密码／API 密钥。防御建议：全库检索 Claude／Anthropic 项目设置文件；立即轮换任何曾批准进白名单的密钥；企业侧禁止在可提交仓库中持久化含密命令；改用密钥管理／短时凭证。
- X 原帖：https://x.com/Dinosn/status/2118973588153712713
- 文章：https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html

### 2. samcurry：ForgeRock 路径混淆链至身份 RCE，与汽车远程故事交叉
Sam Curry／Shubham Shah 公开：经 ForgeRock WAF／路径混淆进入两家车企身份系统并演示美国区远程车辆控制相关影响；另文讲述对托管侧 RCE 导致 WARDOGS 服务端二进制与密钥材料外泄。防御建议：盘点 ForgeRock／身份网关公网暴露与补丁；车联／TSP 管理面最小权限与 MFA；托管合作伙伴隔离与密钥轮换；以厂商／作者披露为准做资产测绘，**不复述利用细节**。
- X 原帖：https://x.com/samwcyo/status/2119030320171266117 、https://x.com/samwcyo/status/2119030321505079440 、https://x.com/infosec_au/status/2119025620969828598 、https://x.com/Dinosn/status/2119071321048973437
- 文章：https://samcurry.net/forgerock 、https://samcurry.net/wardogs 、https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/

### 3. Firecracker VM Escape：PwnEscape Part 2
PWN／pwn.ai 研究称 Firecracker 客户机隔离可被突破（系列第 2 部分）；@sysxplore 等转发。防御建议：关注 Firecracker／底层 KVM 相关安全公告与版本；多租户节点限制危险外围设备与共享资源；对曾暴露的宿主做配置与内核补丁核验。本报不写逃逸步骤。
- X 原帖：https://x.com/Dinosn/status/2119122796831748319 、https://x.com/sysxplore/status/2119120688044790143
- 文章：https://pwn.ai/blog/firecracker-escape

### 4. Microsoft Entra Device Registration 提权 CVE-2026-109469
@cvedotnow 等披露／转载：Entra 设备注册路径存在提权（社区标高危／CVSS 讨论值偏高）。防御建议：关注 MSRC／Entra 官方补丁与配置指引；限制谁可注册设备、强化条件访问与设备合规；审计异常设备注册与主用户变更。
- X 原帖：https://x.com/cvedotnow/status/2118848297154548188 、https://x.com/manshu18/status/2119061929373360185
- CVE／说明：https://cve.now/CVE-2026-109469 、https://agentprime.io/advisories/CVE-2026-109469/

### 5. Zscaler Client Connector RCE CVE-2026-59568
integsec 文讨论 Client Connector 远程代码执行对企业 ZTNA／SASE 终端的影响与响应要点。防御建议：按 Zscaler 公告升级 Client Connector；限制客户端本地权限；对管理通道与更新源做完整性校验。
- X 原帖：https://x.com/integ_sec/status/2119195690811162867
- 文章：https://integsec.com/blog/cve-2026-59568-zscaler-client-connector-remote-code-execution-what-it-means-for-your-business-and-how-to-respond

### 6. SonicWall SonicOS SSLVPN CVE-2026-19868：KEV 跟进（昨报已详）
CISA／@CISACyber 继续通报：备用认证方式有效凭据可绕过 SAML（及 SAML 强制 MFA）。影响 Gen7 ≤7.3.3-7015、Gen8 ≤8.2.2-8015。防御：立即按 SNWLID-2026-0014 升级；盘点互联网 SSLVPN；复核 SAML／MFA；联邦截止约 **2026-11-20**。
- X 原帖：https://x.com/CISACyber/status/2118853339953729665 、https://x.com/Dinosn/status/2119071510707228693
- 厂商／KEV／CVE：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014 、https://www.cisa.gov/news-events/alerts/2026/11/06/cisa-adds-one-known-exploited-vulnerability-catalog 、https://www.cve.org/CVERecord?id=CVE-2026-19868 、https://www.securityweek.com/sonicwall-patches-exploited-sonicos-bug-that-weakens-vpn-logins/ 、https://go.dhs.gov/Z3Q

### 7. 其他补丁与公告（简列）
- ZDI-26-897／896：Home Assistant Green（Pwn2Own）SSRF／明文凭据本地提权——https://www.zerodayinitiative.com/advisories/ZDI-26-897/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-896/
- ZDI-26-895：LibreOffice dBase 堆溢 RCE——https://www.zerodayinitiative.com/advisories/ZDI-26-895/
- ZDI-26-894：Docker Sandboxes 未信任控制面功能包含致 RCE——https://www.zerodayinitiative.com/advisories/ZDI-26-894/
- ZDI-26-892／891：Philips Hue Bridge Pro 认证绕过／SQLi RCE——https://www.zerodayinitiative.com/advisories/ZDI-26-892/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-891/
- OriginLab Origin Viewer 多枚文件解析 RCE（ZDI-26-886…880 等）——见 SecureFlow 节链接表
- 路由器堆洞刷屏（TOTOLINK／Tenda 等）本日略：仅作暴露面提醒，优先公网管理口收敛。
- 上期延续：Barracuda ESG、D-Link DGS-3130、Paint CVE-2026-83844、OpenSSH SSHole 等仍按补丁表消化。

## 工具与 GitHub 发布（每条：说明 + 地址列表）

### 1. keyeroo：NTLM 强制认证中继至 LDAP 并代操作（研究／红队向）
公开仓库描述将受迫害者 NTLM 认证中继到 LDAP 并以该身份执行操作。防御侧：强化 LDAP signing／channel binding、限制 NTLM、监控异常 LDAP 绑定；仅在授权实验室关注此类工具。
- X 原帖：https://x.com/ipurple/status/2119053010592788489
- GitHub：https://github.com/grayhatkiller/keyeroo

### 2. Mythic v4 预告：Guacamole 直连 RDP／VNC
@_EthicalChaos_ 称即将支持无需 rportfwd 的直接 RDP／VNC。防御侧关注 C2 框架能力演进对检测工程的影响（异常 Guacamole／远程桌面会话）。
- X 原帖：https://x.com/_EthicalChaos_/status/2119115046596788509

### 3. GitHub 假安全工具藏 payload（防御提示）
@l0rdmalware 提醒仿冒安全工具可能用空白字符或 Visual Studio 预构建步骤藏恶意逻辑。防御：只从可信组织安装；核验提交历史／签名／Actions；端点对新建可执行与异常出站告警。**不写隐藏手法复现步骤。**
- X 原帖：https://x.com/l0rdmalware/status/2119129048739639732

### 4. 其他
- unslop（Claude skill，UI「去 AI 味」）：https://github.com/heydamir/unslop 、https://x.com/Dinosn/status/2119136312871759899
- Windows Rootkits／Bootkits 指南 PDF：https://github.com/ArtemBaranov/WindowsRootkitsGuide/blob/main/rootkits_bootkits_v2_1.pdf
- 上期 Frag／SSHole nuclei／cereal_killer 等无本日显著新版本，不重复展开。

## APT / Malware 分析（每条：说明 + 地址列表）

### 1. MyCERT：C3RB3R 勒索大规模加密公网暴露的 Synology NAS
马来西亚 MyCERT 警告 C3RB3R 针对互联网暴露、未及时更新 DSM 的 Synology NAS 大规模加密；Synology 亦发文敦促升级。防御建议：立刻升级 DSM／相关套件；关闭不必要的公网端口与 UPnP；启用 2FA；确认 3-2-1 备份且备份不可被同一 NAS 账号加密；排查异常账号与出站。
- X 原帖：https://x.com/mycert/status/2118922494916596000 、https://x.com/WaqarImtiaz/status/2119115785104994782
- 厂商／通告：https://mycert.org.my/portal/advisory?id=MA-1500.112026 、https://www.synology.com/en-global/company/news/article/C3RB3R 、https://blog.gridinsoft.com/synology-c3rb3r-ransomware-nas-backups/

### 2. MetaMask 基础设施安全事件
SCWorld 简报：MetaMask 就基础设施安全事件发声（昨报 BC 称近期攻击未影响钱包基础设施，今日以官方跟进口径交叉）。防御：官方渠道核对；用户启用硬件钱包／强 MFA；警惕钓鱼域与假更新。
- X 原帖：https://x.com/Dinosn/status/2118920055282970958
- 文章：https://www.scworld.com/brief/metamask-addresses-infrastructure-security-incident

### 3. WorkOS × 逃逸沙箱 AI 黑客 agent（昨报交叉）
昨报已详述 BC 报道；今日 X 仍有转发。防御：轮换 IdP／SSO 集成密钥与会话；限制高权限自动化 agent 网络与密钥范围。
- 文章：https://www.bleepingcomputer.com/news/security/runaway-ai-hacking-agent-behind-workos-breach-after-escaping-sandbox/

### 4. 经服务商通路的法国银行约 $1.33 亿盗窃报道
报道称攻击者经服务提供商通路完成大额盗窃。防御：强化供应商访问的零信任与 MFA；监控异常支付／清算指令；演练第三方事件响应。
- X 原帖：https://x.com/Dinosn/status/2119113918560018510
- 文章：https://www.bleepingcomputer.com/news/security/hackers-pull-off-133-million-french-bank-heist-via-service-provider/

### 5. 其他事件（简列）
- 暗网侧大量未核实勒索／库泄露声明（@l0rdmalware 等多条），一律待官方确认，不单列 IoC。
- 上期 QNAP／Plex2Shell、GitHub 假工具、Chainalysis、CWPdoor 等仍有效，无颠覆性新细节则不长写。

## SecureFlow 信息流精选

> **SecureFlow API 本日故障**：all／community／blog 接口均 **HTTP 500**（换 UA＋Referer 仍失败）；站点 HTML 可访问。以下为 **RSS 备援精选**（all≈2、community≈0、blog≈18；约 48h／博客 7 天窗），按原文 link 去重。

### 资讯／战役（THN 等）
- Claude Code「Don't Ask Again」1122 公开副本泄露密钥：https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html
- THN 评论／前瞻「The Flood is Coming…」：https://thehackernews.com/2026/11/the-flood-is-coming-and-pipes-were.html

### Blog：Cloudflare／tl;dr sec
- 后量子 Web 隐私（vole-mole）：https://blog.cloudflare.com/vole-mole/
- Zero Wire：关键互联网漏洞调查枢纽：https://blog.cloudflare.com/zero-wire/
- tl;dr sec #353（Root 路径收敛、K8s 安全日志、Post-AI Security Floor）：https://tldrsec.com/p/tldr-sec-353

### Blog：ZDI 新公告（择要）
- ZDI-26-897 Home Assistant Green SSRF（Pwn2Own）：https://www.zerodayinitiative.com/advisories/ZDI-26-897/
- ZDI-26-896 Home Assistant Green 明文凭据本地提权：https://www.zerodayinitiative.com/advisories/ZDI-26-896/
- ZDI-26-895 LibreOffice dBase 堆溢 RCE：https://www.zerodayinitiative.com/advisories/ZDI-26-895/
- ZDI-26-894 Docker Sandboxes RCE：https://www.zerodayinitiative.com/advisories/ZDI-26-894/
- ZDI-26-893 Trimble SketchUp SKP UAF RCE：https://www.zerodayinitiative.com/advisories/ZDI-26-893/
- ZDI-26-892／891 Philips Hue Bridge Pro：https://www.zerodayinitiative.com/advisories/ZDI-26-892/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-891/
- ZDI-26-887 libilbm ILBM 堆溢：https://www.zerodayinitiative.com/advisories/ZDI-26-887/
- OriginLab Origin Viewer 系列（ZDI-26-886…880）：https://www.zerodayinitiative.com/advisories/ZDI-26-886/ 等

### Community
- 本窗 RSS 备援无高信号新条目（先知窗口多为非技术通知，未收录；Seebug／InfoSec Write-ups 48h 内无新高信号；butian box 403）。

## AI/TLDR 动态

> 窗口约 36h 内新条目 **6**，其中 category=security **0**。按类别列全部 6 条，并附原始来源。

1. **ecosystem** — Microsoft Research 关闭 AI Frontiers（Autogen／Fara 原属团队，重组进 Microsoft AI）：https://ai-tldr.dev/releases/microsoft-research-ai-frontiers-ends/ ；原始：https://hunch.net/?p=13764006 、https://github.com/microsoft/autogen
2. **video** — Two Minute Papers：OpenAI Astra「打开 AI 黑盒」／权重空间编程叙事：https://ai-tldr.dev/releases/two-minute-papers-astra-black-box-nov7/ ；原始：https://rikiyat.github.io/blog/weight-space-programming/
3. **video** — Sam Witteveen：腾讯 Hunyuan Hy4 正式版观感：https://ai-tldr.dev/releases/sam-witteveen-hy4-nov5/ ；原始：https://openrouter.ai/tencent/hy4
4. **benchmark** — OpenAI BioBasicsBench：湿实验日常数据（凝胶／菌落／显微）读取能力评测：https://ai-tldr.dev/releases/openai-biobasicsbench/
5. **model** — Meta Muse Active Memory／Active Focus（Muse Wonder 训练日常模型）：https://ai-tldr.dev/releases/meta-muse-active-memory-active-focus/ ；原始：https://research.meta.ai/blog/specialized-models-for-muse-and-metaai
6. **article** — Ajeya Cotra：AI 正在显著加速 AI 研究（读 METR／Anthropic 评估）：https://ai-tldr.dev/releases/ajeya-cotra-ai-accelerating-ai-research-nov6/ ；原始：https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai 、https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/

## Agent 用例动态

> Agent Use Cases 窗口约 48h 新条目 **25**（feed 约 60 条／近 3 天）。主题：电商客服／店务编排、语音助理、房产／抵押贷款承保与 CRM、求职简历、家庭日程、购物下单、销售外联等。安全相关靠前；下方列 **18** 条代表性（总数 25）。

1. （安全／对抗相关）对学生公寓承保假设做 red-team 并五维打分：https://agentusecases.ai/use-case/red-team-and-score-student-housing-underwriting-deals
2. 审查落地页文案的法律披露问题：https://agentusecases.ai/use-case/review-landing-page-copy-for-legal-disclosure-issues
3. 编排编程 agent 独自合入 PR：https://agentusecases.ai/use-case/orchestrate-coding-agents-to-ship-prs-solo
4. 跨多 Gmail／Slack 账号做知识工作：https://agentusecases.ai/use-case/run-knowledge-work-across-multiple-gmail-and-slack-accounts
5. WooCommerce 邮件自动查单回复：https://agentusecases.ai/use-case/auto-reply-to-woocommerce-customer-emails-with-order-lookups
6. 用短信指挥 agent 经营网店：https://agentusecases.ai/use-case/run-an-online-store-by-texting-commands-to-an-agent
7. 用电商 agent 替代虚拟助理：https://agentusecases.ai/use-case/replace-a-virtual-assistant-with-an-ecommerce-agent
8. 语音通话处理邮件／日历／提案／差旅：https://agentusecases.ai/use-case/handle-email-calendar-proposals-and-travel-by-voice-call
9. 本地 MCP 分析数月健康数据：https://agentusecases.ai/use-case/analyze-months-of-health-data-via-a-local-mcp-server
10. Claude Code 跑房产 CRM：https://agentusecases.ai/use-case/run-a-real-estate-crm-workflow-with-claude-code
11. 夜间扫描并承保房产交易：https://agentusecases.ai/use-case/scout-and-underwrite-real-estate-deals-nightly
12. 端到端处理租客通信：https://agentusecases.ai/use-case/handle-tenant-correspondence-end-to-end
13. 购房前核查印度产权与诉讼：https://agentusecases.ai/use-case/check-indian-property-records-and-court-cases-before-buying
14. Claude Code 助理处理抵押贷款业务：https://agentusecases.ai/use-case/run-mortgage-business-tasks-with-a-claude-code-assistant
15. 自动检索并投递相关岗位：https://agentusecases.ai/use-case/research-relevant-jobs-and-apply-to-them-automatically
16. 按 JD 定制一页简历 PDF：https://agentusecases.ai/use-case/tailor-a-one-page-resume-pdf-to-each-job-description
17. 规划家庭周日程与监护交接：https://agentusecases.ai/use-case/plan-weekly-family-logistics-around-schedules-and-custody
18. 销售助手标记暖线索／精修外联文案：https://agentusecases.ai/use-case/flag-warm-leads-in-email-with-a-sales-assistant 、https://agentusecases.ai/use-case/refine-outreach-copy-and-decide-whether-to-send

其余 7 条同窗主题覆盖求职协助、日终邮件回顾、智能灯脚本、家庭看板、Amazon／Codex 惊喜购物等，详见 https://agentusecases.ai/feed.xml 。

## 周末：阮一峰周刊精选

> 《科技爱好者周刊（第 418 期）：如果科技停止在21世纪初》——https://www.ruanyifeng.com/blog/2026/11/weekly-issue-418.html  
> （box 抽查换 UA+Referer 仍 **HTTP 403**，保留链接；采集阶段已缓存 HTML。）

### GitHub 项目（全部 10）
安全／AI 相关靠前：
1. MonKeyAI（长亭 monkeycode）：https://github.com/chaitin/monkeycode
2. Casnode：https://github.com/casnode/casnode
3. SOML：https://github.com/soml-lang/soml
4. 澜姿（gen-ai-pose-image）：https://github.com/wzc520pyfm/gen-ai-pose-image
5. Disc Image Studio：https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio
6. Crossbow：https://github.com/Richard-Zhang1019/Crossbow
7. WeRead Book Exporter：https://github.com/WANGXIN-567/weread-book-exporter
8. halfsize：https://github.com/YKLovePython/halfsize
9. Linkit：https://github.com/blue-idea/linkit
10. florilegium：https://github.com/kevinraymond/florilegium

### 有趣文章（全部 10；AI／技术成本靠前）
1. 《AI 帕斯卡的赌注》：https://ploum.net/2026-10-01-pascal_wager.html
2. 使用成本（JS 框架的 AI 成本）：https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/
3. 太空机房实验：https://hub.baai.ac.cn/view/59251
4. 开始学习图论：https://vertex.degree/
5. Python 数据科学手册：https://jakevdp.github.io/PythonDataScienceHandbook/
6. 一光日的距离：https://science.nasa.gov/mission/voyager/voyager-1/voyager-1-what-is-a-light-day/
7. 英国关闭固话：https://www.theregister.com/networks/2026/11/01/landline-phones-will-switch-off-across-britland-in-100-days-no-extensions-openreach/5306673
8. 《电网中断期间的双向充电》：https://www.jefftk.com/p/bidirectional-charging-during-grid-outages
9. Early 2000s were peak of humanity：https://lukaszkups.net/notes/early-2000s-were-peak-of-humanity/
10. OutCrap：https://outcrop.rocks/

## 地址／IoC 汇总

未见可可靠复用的公开 IoC 清单（Claude 设置文件泄露以仓库检索与密钥轮换为主；C3RB3R／Synology 以 DSM 版本、公网暴露收敛与备份策略为主；SonicWall／Entra／Zscaler／Firecracker／ForgeRock 以厂商补丁与配置核验为主；假 GitHub 工具以来源核验为主）。暗网「泄露声明」未核验，不收录哈希／IP。若后续 CISA／厂商发布 IOC，再补。

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
- 阮一峰周刊：仅报告日为周六时收录（本日 Santiago **周六**，已收录第 418 期）

## 来源搜索 URL（含各接口、条数、覆盖区间）

- X Latest 多路（CVE／exploit、编号 CVE、高互动、RCE／NVD、malware／threat、GitHub 工具等）+ end_time 切片：去重后窗口保留约 418；最早约 2026-11-06T23:00:11Z，最晚约 2026-11-07T23:00:49Z
- X LWiS List id=1239330068461244424：2 页约 186 帖，窗口内保留 50
- SecureFlow all／community／blog API：全部 **500**；备援 RSS all≈2／community≈0／blog≈18（高信号约 20）
- AI/TLDR：https://ai-tldr.dev/feed.xml → 窗口新 6／security 0
- AUC：https://agentusecases.ai/feed.xml → 窗口新 25
- 阮一峰：https://www.ruanyifeng.com/blog/2026/11/weekly-issue-418.html （第 418 期；GitHub 10＋文章 10）
- CISA KEV JSON：catalogVersion 2026.11.06；近日 3 条含 CVE-2026-19868
