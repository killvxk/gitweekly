# X 安全情报晚报 · 2026-11-03（America/Santiago）

> 生成时间：2026-11-03 20:20（America/Santiago）＝ 2026-11-04 07:20（香港时间）
> X 覆盖：LWiS List 时间线三页约 281 帖，覆盖 2026-11-03 00:35–22:51 UTC（约 22 小时）。Latest 搜索三组 + 高互动补搜 + 专项补搜（WordPress/F5、Binance）。Latest「CVE/PoC/exploit/0day」按时间排序 25 条全在 23:08 UTC 的十几秒内，被巴西真人秀「Peter Poc」刷屏，几乎没有安全内容，所以改用 min_likes:20 相关度补搜，覆盖 11-03 00:01–22:04 UTC；GitHub 组 7 条，覆盖 02:11–20:39 UTC（量少，基本是全天）；malware/threat 组覆盖 20:25–23:07 UTC（约 2.7 小时，多为暗网泄露声明类帖子，只取了可核实的）。
> 公开备援：CISA KEV（2026-11-03 20:00 UTC 发布，共 1767 条，本窗口新增 1 条：WordPress Core CVE-2026-119977）、厂商公告、ZDI。
> 验收：采集、链接核验、成稿均通过；本机副本见文末交付说明。

## 今日摘要

- **WordPress Core CVE-2026-119977 进 KEV，联邦截止日只有 3 天（11-06）**：4.7–7.1.3 在核心升级窗口期存在未认证 RCE（TOCTOU 竞争），已在野利用。升级到 7.1.4 或对应分支补丁，升级前先禁止 Web 访问 `wp-content/upgrade/`，并检查该目录残留文件。
- **Binance 63 亿美元被盗事件官方复盘**：入口是 DPRK 的 Contagious Interview（假面试）和被篡改的 Homebrew 安装，不是 AI 写的 0day；FBI 归因 TraderTraitor。
- **Siemens SIMATIC IoT2050 / Node-RED CVE-2026-58115（CVSS 10）在野利用**，被用来植入 Linux bot 和 HTTP 执行后门。
- **Binarly：Zyxel GS1900 的 KEV 漏洞补丁无效**，攻击者实际用的是另一个未修漏洞，新编号 CVE-2026-107441。
- **Keycloak 两个未公开漏洞（SAML 登录劫持 + realm 管理员提权）**和 **Opengear 控制台服务器预认证 RCE 链**公开；Firefox 159 一次修了 41 个 sec-high。
- APT／事件：ESET 披露俄系 **Gorbag**（WinRAR 漏洞 + 窃密木马打乌克兰前线机构）；SentinelLABS 分析**欧洲冷库／制冷系统被篡改**事件；**cPGuard 更新通道被劫持**给 Linux 服务器植后门；**GitBook** 遭 AI agent 驱动的定向攻击。
- SecureFlow：ZDI 一次公开 **15 个 Quest Foglight for Databases 漏洞**（多个 RCE）和 **Cisco Snort 越界写 RCE**（CVE-2026-20043）；HackerOne 新公开 curl `curl_easy_pause` 重入 UAF 等 4 份报告。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

### 1. WordPress Core CVE-2026-119977：升级窗口期未认证 RCE，已在野利用，KEV 截止 11-06
影响 4.7.0–7.1.3。在核心整包升级过程中，暂存安装文件的路径可预测且可被 Web 访问，未认证攻击者可借此执行代码。10-31 披露，WordPress 7.1.4 及各分支回补版本已修（如 7.0.8）。CISA 11-03 收录 KEV，联邦截止 11-06，勒索利用情况未知。防御建议：确认实际运行版本与核心文件校验和；升级前先拒绝对 `wp-content/upgrade/` 的 Web 访问；升级后检查该目录与访问日志中是否有异常文件或请求（打了补丁不代表之前没被打）。
- X 原帖：https://x.com/notCVE/status/2117739606720303302 、https://x.com/timsonner/status/2117714163514667067 、https://x.com/__kokumoto/status/2117751251811324017 、https://x.com/zerohuntai/status/2117716240152109193
- 厂商／KEV：https://wordpress.org/news/2026/10/wordpress-7-1-4/ 、https://www.cisa.gov/news-events/alerts/2026/11/03/cisa-adds-one-known-exploited-vulnerability-catalog 、https://nvd.nist.gov/vuln/detail/CVE-2026-119977
- 文章：https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-core/wordpress-core-470-713-unauthenticated-upgrade-window-staged-installer-remote

### 2. Siemens SIMATIC IoT2050 / Node-RED CVE-2026-58115（CVSS 10.0）在野利用
Node-RED 缺失认证，未认证远程执行系统命令；8 月披露，Siemens 分配编号，独立部署的 Node-RED 也可能受影响。VulnCheck 观测到攻击者用恶意 Node-RED flow 植入 Linux bot 和 HTTP exec 后门。排查建议见 IoC 小节。
- X 原帖：https://x.com/Netlas_io/status/2117548960453710211 、https://x.com/DFIR_Radar/status/2117542731153285555 、https://x.com/Dinosn/status/2117593479509324271
- 文章：https://www.securityweek.com/critical-node-red-flaw-exploited-in-attacks/ 、https://thehackernews.com/2026/11/attackers-exploit-critical-siemens.html 、https://www.theregister.com/security/2026/11/02/max-severity-bug-in-widely-used-ot-programming-tool-exploited-to-deliver-linux-malware/5307086

### 3. Zyxel GS1900 交换机：KEV 漏洞（CVE-2026-7273）补丁挡不住在野利用，新编号 CVE-2026-107441
Binarly 发现在野 RCE 实际利用的是另一个未修的预认证漏洞，报告给 Zyxel 后出了新补丁。提醒：不要只按固件版本号判断是否已修。
- X 原帖：https://x.com/binarly_io/status/2117651602823598202 、https://x.com/ant_av7/status/2117655223858499683
- 厂商：https://www.binarly.io/advisories/brly-2026-057
- 文章：https://www.binarly.io/blog/zyxel-gs1900-rce-cve-2026-107441

### 4. Keycloak：两个未公开漏洞（SAML 登录劫持、realm 管理员提权）
abraxas 公开：一是未认证远程劫持 SAML 登录（需要配置了重定向签名的 SAML broker）；二是 help-desk 级管理员通过预建 composite 角色提权到 realm 管理（CVE-2026-94000 的未披露兄弟问题）。目前未见厂商公告编号。建议核查 SAML broker 配置与 composite 角色分配，关注 Keycloak 官方更新。
- X 原帖：https://x.com/abraxas_null/status/2117602705774395468 （转推：https://x.com/vysecurity/status/2117719864324608464 ）
- GitHub／PoC（仓库含利用代码，本报告不转载内容）：https://github.com/abraxas/keycloak-saml-redirect-param-split 、https://github.com/abraxas/keycloak-manage-users-composite
- 文章：https://abraxaslabs.tech/research/keycloak-saml-redirect-param-split 、https://abraxaslabs.tech/research/keycloak-manage-users-composite

### 5. Opengear 控制台服务器预认证 RCE 链
Armadin 在 Opengear 带外管理设备的 HTTP 头解析器中发现堆溢出，可串成无凭据 RCE；已向厂商披露并分配 CVE。带外管理面应只对管理网段开放。
- X 原帖：https://x.com/ArmadinSecurity/status/2117706536537542893 、https://x.com/h4wkst3r/status/2117709109437046912
- 文章：https://www.armadin.com/blog-posts/compromising-the-out-of-band-management-plane-pre-auth-rce-via-heap-overflow-in-opengear-console-servers （box 换 UA 加 Referer 后仍 403，浏览器可开）

### 6. CryptoPayment Gateway for WordPress CVE-2026-81648（CVSS 10）在野利用尝试
Defused 观测到首次在野利用尝试：任何人可读取站点保存的支付网关配置（含明文钱包凭据）并改写配置。攻击源来自标榜「免 KYC VPS」的托管商。插件用户应立即更新或停用，并轮换钱包凭据。
- X 原帖：https://x.com/DefusedCyber/status/2117325160608870613 、https://x.com/Dinosn/status/2117495677089706233
- 文章：https://thehackernews.com/2026/11/attackers-target-unpatched.html

### 7. Drupal Commerce Core CVE-2026-118539 被利用（访问控制绕过）
维护方 Centarro 称有商户收到 0.01 美元等异常订单。修复版本 3.3.13 与 8.x-2.41，建议同时审计订单。
- X 原帖：https://x.com/cybersec24h/status/2117575886622896538 、https://x.com/OneSignalDesk/status/2117475143685710029
- 厂商：未在本窗口抓到 Drupal 官方公告链接，请以 https://www.drupal.org/security 为准

### 8. Firefox 159.0 一次修复 41 个 sec-high 漏洞
itszn13 与 ky1ebot 用 AI agent 辅助挖掘，多数可在渲染进程内代码执行。尽快升级 Firefox。
- X 原帖：https://x.com/itszn13/status/2117437996072837324 、https://x.com/LiveOverflow/status/2117526008748200139
- 厂商：https://www.mozilla.org/en-US/security/advisories/

### 9. 其他值得跟进的漏洞
- **Omnissa Unified Access Gateway 严重漏洞**（2609 版本发布说明）：https://x.com/Dinosn/status/2117687740183593471 ；厂商：https://docs.omnissa.com/UnifiedAccessGatewayReleaseNotes-V2609/unified-access-gateway-release-notes
- **Broadcom Symantec Ghost Solution Suite CVE-2026-101034**（硬编码密钥保护凭据）：https://x.com/rotassec/status/2117617900173328587 ；文章：https://hubs.ly/Q04D4S5y0
- **Rocket Remote Desktop 凭据存储与加密薄弱**（RedTeam Pentesting 公告）：https://x.com/DirectoryRanger/status/2117710227168522467 ；公告：https://www.redteam-pentesting.de/de/advisories/rt-sa-2026-001/
- **Dassault DELMIA Apriso CVE-2025-5086** 研究复盘（已被 CISA 确认在野利用）：https://x.com/HacktronAI/status/2117587945976734042 ；文章：https://www.hacktron.ai/blog/dassault-delmia-apriso-rce
- **Linux 内核跟进**：MalwareTech 称观测到疑似攻击者全网扫描 CVE-2026-98432（MPTCP/TCP UAF）暴露主机，https://x.com/MalwareTechBlog/status/2117508092321747077 ；CVE-2026-46300（Fragnesia，本地提权，10-28 已入 KEV）讨论升温：https://x.com/ido_cohen2/status/2117588510806782270
- **PHP2Shell 跟进**（CVE-2026-109618/109619，昨日已报）：调查发现 Palo Alto 防火墙被攻陷，Qurium 发布披露过程复盘。X：https://x.com/Dinosn/status/2117677510162874632 、https://x.com/Dinosn/status/2117575873507553682 ；文章：https://www.qurium.org/press-releases/php2shell-when-ai-powered-vulnerability-discovery-outpaces-responsible-disclosure/ 、https://www.cybersecuritydive.com/news/palo-alto-networks-firewalls-compromised-chained-attacks-php2shell/873323/ （box 403，浏览器可开）
- **Synology DSM 已修漏洞被勒索团伙利用**（昨日已提）：https://x.com/Dinosn/status/2117531344574033940 ；文章：https://thehackernews.com/2026/11/synology-nas-devices-targeted-in.html
- **iOS Lockdown Mode 讨论**：calif_io 发视频称 Lockdown Mode 并不能挡住其 AirDrop/PDF 攻击面，i0n1c 解释 Lockdown 会给更多系统进程启用 MTE。https://x.com/calif_io/status/2117720348322144733 、https://x.com/i0n1c/status/2117743545410801769
- **Apple XProtect 更新**：https://x.com/howardnoakley/status/2117698399172690145 ；文章：https://eclecticlight.co/2026/11/03/apple-has-just-released-an-update-to-xprotect-for-all-macos-24/

## 工具与 GitHub 发布（每条：说明 + 地址列表）

### 1. BOF-coerce-ipp：通过 IPP 打印机做认证强制的 BOF
用于把 HTTP 认证中继到 AD CS、LDAP 等。防御侧：限制打印服务出站认证，开启 LDAP 签名/通道绑定与 AD CS EPA。
- X 原帖：https://x.com/infosecnoodle/status/2117718319717564743
- GitHub：https://github.com/sudonoodle/BOF-coerce-ipp

### 2. Microsoft Defender for Identity 规避（2026，Part I）
cirosec 研究 MDI 检测盲点，蓝队可据此补检测。
- X 原帖：https://x.com/ipurple/status/2117685381319610399 、https://x.com/Dinosn/status/2117686758292804044
- 文章：https://cirosec.de/en/news/microsoft-defender-for-identity-evasions-in-2026-part-i/

### 3. AI 攻击框架 ARTEX／Cairn／PentAGI 的狩猎方法与实例情报
RST Cloud 给出互联网测绘查询方法；ThreatBook 公开在网运行的 ARTEX 与 CyberStrikeAI 实例清单；ARTEX 项目自带防御文档（指出默认 UA 未改）。
- X 原帖：https://x.com/rst_cloud/status/2117426101312258298 、https://x.com/s0what/status/2117595828114407713 、https://x.com/N3mes1s/status/2117499841794245051
- GitHub：https://github.com/jiwoochris/artex-global/blob/main/docs/defense-en.md
- 文章／Feed：https://www.rstcloud.com/hunting-ai-harnesses-cairn-artex-pentagi/ 、https://threatbook.io/hubfs/Feeds/ARTEX.txt 、https://threatbook.io/hubfs/Feeds/CSAI.txt

### 4. 其他
- **wifit3**（derv82 新版 Wi-Fi 审计工具）：https://x.com/vysecurity/status/2117512275171139587 ；GitHub：https://github.com/derv82/wifit3
- **浏览器缓存走私（macOS 可行性与防御）**：https://x.com/PhorionTech/status/2117610593490211152 ；文章：https://phorion.io/blog/browser-cache-smuggling-macos/
- **在隔离 vCPU（Windows Hypervisor Platform）中执行代码的研究**：https://x.com/papadelospapas_/status/2117729246902890865 ；文章：https://medium.com/@s12deff/executing-shellcode-in-an-isolated-vcpu-5ac0cc4baaac （box 403，浏览器可开）
- **Realm C2 用 KMeans 给 beacon 自动分组打标签**：https://x.com/Hultoko/status/2117450673499549781
- **恶意 AGENTS.md 投递手法**（网页静默存入 Downloads，诱导 AI 编码 agent 安装恶意 npm 包 function-color）：https://x.com/delivr_to/status/2117195208634819000
- **CrowdStrike 宣布收购 Dreadnode**：https://x.com/dreadnode/status/2117573774132367637

## APT / Malware 分析（每条：说明 + 地址列表）

### 1. Binance 约 63 亿美元被盗：官方复盘指向 DPRK 假面试 + 被篡改的 Homebrew
Binance 发布事件报告：一名工程师用被篡改的 Homebrew 安装 AI 工具中招，另一名下载了带恶意代码的面试作业仓库；攻击者拿到部署令牌用于钱包签名。约 28.5 亿美元已冻结，用户不承担损失；FBI 归因 DPRK TraderTraitor，朝方否认。MalwareTech 等指出这是 Contagious Interview 式社工，不是 AI 0day。
- X 原帖：https://x.com/binance/status/2117626126214504729 （X Article：https://x.com/i/article/2117598836831010816 ）、https://x.com/MalwareTechBlog/status/2117651234018767015 、https://x.com/L0Psec/status/2117677354130825546 、https://x.com/S1r1u5_/status/2117673206727458918
- 文章：https://ruysal.com/post/2026-11-01-disrupting-contagious-interview/ （Contagious Interview 战役综述）

### 2. ESET：俄系 Gorbag 利用 WinRAR 漏洞向乌克兰前线机构投递窃密木马
目标为乌克兰执法、司法、国防和地方政府；工具链包括 BeautyStealer、Prime ReverseShell、武器化 LNK。Nextron 公开了 YARA 与 IoC。
- X 原帖：https://x.com/ESETresearch/status/2117557431286862133 、https://x.com/nextronresearch/status/2117614720089780615 、https://x.com/Dinosn/status/2117613632913645579
- GitHub（IoC）：https://github.com/NextronSystems/iocs/tree/master/reports/Russia-Aligned%20Espionage%20Targeting%20Ukrainian%20Frontline%20Institutions
- 文章：https://www.welivesecurity.com/en/eset-research/gorbag-orcs-border-harvesting-intelligence-ukraine/ 、https://thehackernews.com/2026/11/russia-aligned-gorbag-hackers-exploit.html

### 3. SentinelLABS：欧洲制冷／冷库系统被篡改温度与除霜设置
受害方涉及瑞典、比利时、爱尔兰、卢森堡、爱沙尼亚、荷兰、芬兰、葡萄牙、德国等。入口是暴露的管理界面与弱口令；归因未定（俄系团伙有相关前科，但不足以定论）。
- X 原帖：https://x.com/TomHegel/status/2117640409266417988 、https://x.com/LabsSentinel/status/2117672800802718133 、https://x.com/lukOlejnik/status/2117665285771510138
- 文章：https://www.sentinelone.com/labs/defrost-and-disrupt-an-assessment-of-europe-s-refrigeration-attacks/ （box 429 限流，浏览器可开）

### 4. cPGuard（OPSSHIELD）更新通道被劫持，向 Linux 服务器植后门并收集密码哈希
使用 cPGuard 的主机应按厂商通告排查并轮换凭据。
- X 原帖：https://x.com/Dinosn/status/2117673931096166447 、https://x.com/Dinosn/status/2117455892534694024
- 厂商：https://opsshield.com/notice/cpguard-update-channel-compromise.html
- 文章：https://thehackernews.com/2026/11/cpguard-update-channel-hijacked-to.html

### 5. GitBook：AI agent 驱动的定向攻击，部分基础设施凭据被访问
11-02 19:00 CET 攻击者获取部分基础设施凭据。同期 Railway 也有客户容器被用来横向请求平台密钥的讨论。
- X 原帖：https://x.com/SwitHak/status/2117698950694420656 、https://x.com/joshmanders/status/2117530391183507484
- 厂商：https://www.gitbook.com/status/security-incident-2026-11-03

### 6. 其他
- **StyleSmuggler 利用链向 Magento 商店投递 PSK Agent RAT**（Imperva）：https://x.com/Dinosn/status/2117456216725361068 ；文章：https://www.imperva.com/blog/stylesmuggler-exploitation-deploys-psk-agent-rat-against-magento-stores/
- **Storm-0940 用 ARTEX 在 3 小时内拿到 Azure 特权访问**，微软将 ConnectWise 供应链事件归因于该活动（11-01 晚报已提 ARTEX）：https://x.com/Cloud_Breach/status/2117489717654573207
- **德国官员遭商业间谍软件攻击**：https://x.com/Dinosn/status/2117455836918292709 ；文章：https://www.scworld.com/brief/german-officials-targeted-by-mercenary-spyware
- **英国学校被 3AM 勒索，疑似 AI 辅助**：https://x.com/Dinosn/status/2117621629413179583 ；文章：https://www.bleepingcomputer.com/news/security/uk-school-estate-hit-by-3am-ransomware-in-suspected-ai-assisted-attack/
- **Harvard 85 万账户数据泄露**：https://x.com/Dinosn/status/2117559663629685010 ；https://haveibeenpwned.com/Breach/Harvard
- **漏洞趋势：「Black October」分析**（披露量涨约 2.3 倍，KEV 新增涨约 31%）：https://x.com/iruthreatintel/status/2117643330141946260 ；文章：https://www.iru.com/blog/black-october
- **AI 在漏洞研究中的能力演进**（Alisa Esage）：https://x.com/alisaesage/status/2117638545024467074 ；文章：https://alisaesage.substack.com/p/on-the-evolution-of-ai-capability
- **澳大利亚 ASD 年度网络威胁报告 2025-26**：https://x.com/ASDGovAu/status/2117753691327566105

## SecureFlow 信息流精选（X 上未出现的高信号条目，按 community／blog／BugBounty 分组）

### blog（ZDI）
- **ZDI：Quest Foglight for Databases 一次公开 15 个漏洞**（ZDI-26-851～866，除 863/864/865 外多为 RCE：反序列化、缺失认证、目录穿越、模板注入等；另有 XXE 信息泄露与本地提权）。例：ZDI-26-851 反序列化 RCE（CVE-2026-92190）、ZDI-26-854 缺失认证 RCE（CVE-2026-92188）、ZDI-26-866 SSTI RCE（CVE-2026-92196）。使用该产品的应尽快确认 Quest 补丁并收紧对其管理端口的访问。
  - https://www.zerodayinitiative.com/advisories/ZDI-26-851/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-854/ 、https://www.zerodayinitiative.com/advisories/ZDI-26-866/ 、https://www.zerodayinitiative.com/advisories/published/
- **ZDI-26-867：Cisco Snort `sf_unfold_header` 越界写 RCE**（CVE-2026-20043），影响用 Snort 的 Cisco 产品，关注 Cisco 公告。
  - https://www.zerodayinitiative.com/advisories/ZDI-26-867/
- **ZDI-26-868：Windows Aero 主题错误处理不当导致 DoS**。
  - https://www.zerodayinitiative.com/advisories/ZDI-26-868/

### community
- 奇安信攻防社区：**Mybatis 常见分页插件 Order by 注入演进史**（技术分析）。https://forum.butian.net/share/5196 （box 网络无法连接，浏览器可开）
- 奇安信攻防社区：**Java 反序列化从 Redis 开始 RCE**（技术分析）。https://forum.butian.net/share/5255 （box 网络无法连接，浏览器可开）
- 已过滤：先知社区「双倍积分和稿费的活动通知」（活动帖）。

### BugBounty（HackerOne 公开报告）
- **curl：`curl_easy_pause` 在 cw-pause 中重入导致 UAF**。https://hackerone.com/reports/4166602
- **Monero：`monero-wallet-rpc::rescan_spent` 信任不可信节点返回的花费状态，可被用于环交集攻击**。https://hackerone.com/reports/3719670
- **$3100：未认证访问 Checkout Blocks 员工专用接口，泄露商户元数据**。https://hackerone.com/reports/3954327
- **`Vary` 缓存键把缺失字段和空字段混为一谈**（缓存投毒类）。https://hackerone.com/reports/4062511

## 地址／IoC 汇总

以下均原样抄自公开帖子或报告，用于狩猎，不代表已独立验证：
- Node-RED / IoT2050（CVE-2026-58115）主机排查路径（来源 https://x.com/DFIR_Radar/status/2117542731153285555 ）：`/dev/shm/.b`、`/tmp/.kworker`；以及把 `/cmd` 接到 exec 节点的 Node-RED flow。
- AI 攻击框架在网实例清单（ThreatBook）：https://threatbook.io/hubfs/Feeds/ARTEX.txt 、https://threatbook.io/hubfs/Feeds/CSAI.txt
- AI 攻击框架测绘特征（RST Cloud，https://x.com/rst_cloud/status/2117426101312258298 ）：ARTEX 页面标题 `ARTEX — 自主渗透测试控制台`；Cairn 页面标题 `Cairn` + `server: uvicorn`；PentAGI `http.favicon.hash:-1596753120`。
- Gorbag 工具链 IoC 与 YARA（Nextron）：https://github.com/NextronSystems/iocs/tree/master/reports/Russia-Aligned%20Espionage%20Targeting%20Ukrainian%20Frontline%20Institutions ；ESET 报告：https://www.welivesecurity.com/en/eset-research/gorbag-orcs-border-harvesting-intelligence-ukraine/
- 恶意 npm 包名（AGENTS.md 投递，来源 https://x.com/delivr_to/status/2117195208634819000 ）：`function-color`
- WordPress CVE-2026-119977 排查目录：`wp-content/upgrade/`
- CryptoPayment Gateway（CVE-2026-81648）：Defused 称完整 IoC 在其 Radar 平台，需注册，帖内未见公开 IoC。
- 其余条目未见公开 IoC。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）：https://x.com/i/lists/1239330068461244424 （本次读取约 281 帖，覆盖约 22 小时）
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
  - https://x.com/search?q=CVE%20OR%20PoC%20OR%20exploit%20OR%200day&f=live （被「Peter Poc」真人秀刷屏，25 条覆盖仅十几秒）
  - https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20BOF)&f=live
  - https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
  - 补搜：https://x.com/search?q=(CVE%20OR%20exploit%20OR%200day%20OR%20%22in%20the%20wild%22%20OR%20%22actively%20exploited%22)%20min_faves%3A20
  - 专项：https://x.com/search?q=CVE-2026-119977%20OR%20CVE-2026-94127 、https://x.com/search?q=Binance%20hack%20min_faves%3A10
- X List：https://x.com/i/lists/1239330068461244424
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200
  - 返回 200 条；近 48 小时（2026-11-02 07:10 至 11-04 07:10，北京时间）新条目 24 条：ZDI 18 条、BugBounty 4 条、community 3 条（过滤 1 条活动通知）。
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community
  - 7 个源，跳过长期不更新的吾爱破解（最后更新 2024-09），其余 6 个逐源拉取 /api/rss/articles/<id>；近 48 小时内、all 接口之外的新条目 0 条。
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog
  - 12 个源，跳过长期不更新的「微信公众号」源（最后更新 2025-02），其余 11 个逐源拉取。
  - 近 7 天（2026-10-28 至 11-04，北京时间）all 接口之外、不在 seen_ids 里的条目 11 条，全部是 10-28/29 的 ZDI 公告，11-01 晚报已列过，本报告不重复，只补记去重。其余源本周无新文。
- 各接口均请求成功（浏览器 UA），无失败。
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （共 1767 条，2026-11-03 发布；本窗口新增 CVE-2026-119977）
- 链接核验：抽查 57 条主链接，其余均 200；403（换 UA 加 Referer 仍 403，已保留并注明）：armadin.com、cybersecuritydive.com、medium.com；429：sentinelone.com；box 网络无法连接：forum.butian.net；ZDI 的 http 链接返回 500，已全部改用 https 并验证 200。

---
本机保存路径：~/Desktop/X安全情报晚报/2026-11-03-x-security-digest.md（kenny1337s-MacBook-Pro.local），box 副本：/home/box/workspace/security-watch/reports/2026-11-03-x-security-digest.md
