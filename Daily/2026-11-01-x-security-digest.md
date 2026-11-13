# X 安全情报晚报 · 2026-11-01（America/Santiago）

> 生成时间：2026-11-01 20:00 前后（America/Santiago）／2026-11-02 07:00（香港时间）
> X 覆盖：Latest 搜索窗口 2026-10-31T23:00Z – 2026-11-01T22:59Z（约 24h）；LWiS List 时间线实际覆盖 2026-10-31T16:17Z – 2026-11-01T22:45Z（约 30h，取其中近 24h 帖子为主）。
> SecureFlow：严格 48h 窗口（北京时间 2026-10-31 07:00 之后）内 0 条新条目，信息流最新一条为 2026-10-31 05:41（北京时间），本期实际采用区间为北京时间 2026-10-29 13:00 – 2026-10-31 05:41（因该源滞后，向前放宽）。
> 验收：采集 / 核验链接 / 成稿 / box 落盘 均通过；本机副本拷贝结果见文末「交付状态」。
> 说明：防御向摘要，不转载利用代码、payload 或 PoC 步骤。

## 今日摘要

- **Linux 内核 CVE-2026-98432（IPv4 TCP 握手 UAF，CVSS 9.8）** 继续发酵：Anthropic 披露其红队用 Claude 写出零点击远程 root 利用；上游 10/11、10/15 已修，Ubuntu/RHEL 发稿时仍未出修复内核，Red Hat 已给缓解。优先排查对外暴露、开启 multipath TCP 监听（Go 程序默认开启）的服务器。
- **Canonical LXD / MicroCloud CVE-2026-112816（CVSS 10.0）**：mTLS 证书链校验缺陷，可冒充受信客户端；已出修复版。
- **ARTEX**：多方追踪的新型攻击框架／网关，X 上有人公开了基于 FOFA 的狩猎特征与一批 IP（见 IoC 节）；Profero IR 团队发长线程。
- **CISA KEV**：10/30 新增两条 Ivanti Connect Secure（CVE-2026-118527、CVE-2026-111357），后者截止日为 **2026-11-02**。
- **供应链**：Polymarket 因 DebugBear 第三方 RUM 脚本被替换（注册商侧 DNS 被劫持），约 270 万美元被盗；Kaspersky 披露针对亚洲政府定制 Win10 的 NetamLoader（AppDomainManager 注入，疑似供应链投递）。
- Android「SMS of Death」CVE-2026-58882 公开 PoC，Android 12/13 无修复；Windows 11 LPE（TrustedHive）与 Chrome 密码管理器 passkey「Pass-ta-key」研究工具在 LWiS List 上流传。

## CVE / POC / 漏洞（每条：说明 + 地址列表）

### 1. Linux 内核 CVE-2026-98432 — IPv4 TCP 握手远程 UAF（CVSS 9.8）
谁／打什么：远程未认证对端可触发，影响 4.4 起的内核；Anthropic 红队称 AI 写出零点击 root 利用（需 multipath TCP 监听）。补丁：5.10.272、5.15.223、6.1.190、6.6.159、6.12.113、6.18.56、7.2.10、7.3；Amazon Linux 已修，AlmaLinux 测试中，Red Hat 已发缓解，Ubuntu/RHEL 截至文章更新时未出修复内核。狩猎：盘点开启 MPTCP 的监听服务、优先对外服务器打补丁或按发行版缓解。业内（@S1r1u5_）对真实可利用性仍有争议。
- X 原帖：https://x.com/Secretof_forest/status/2116669612800778515 ；https://x.com/DIYprojects55/status/2116790165800935687 ；https://x.com/podalirius_/status/2116992394562261145 （LWiS 转推）；https://x.com/S1r1u5_/status/2116949613555159161 （LWiS）
- 厂商／研究：https://www.anthropic.com/research/discovering-vulnerabilities-with-claude
- 文章：https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf

### 2. Canonical LXD / MicroCloud CVE-2026-112816（CVSS 10.0）
谁／打什么：服务器把客户端附带的整条证书链都和信任库比对，攻击者可拼接受信客户端的公开证书冒充其身份，特权身份可致宿主机 root。前提：能访问 HTTPS API（单机 LXD 默认只监听本地 socket，需 core.https_address 才暴露）；MicroCloud 入群时证书可被截获。补丁：升级到 Canonical 公布的修复 snap 版本。
- X 原帖：https://x.com/Dinosn/status/2116846712354406563 （LWiS）
- 文章：https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html

### 3. CISA KEV 新增：Ivanti Connect Secure CVE-2026-118527 / CVE-2026-111357
谁／打什么：已在野利用；CVE-2026-111357 为关键功能缺认证，KEV 修复截止 2026-11-02；CVE-2026-118527 为可预测标识符，截止 2026-11-13。补丁与狩猎：按 Ivanti 公告升级，并检查设备完整性。
- X 原帖：https://x.com/Dinosn/status/2116740344922452437 （LWiS）
- 厂商／KEV／NVD：https://www.cisa.gov/known-exploited-vulnerabilities-catalog ；https://nvd.nist.gov/vuln/detail/CVE-2026-111357 ；https://nvd.nist.gov/vuln/detail/CVE-2026-118527
- 文章：https://securityaffairs.com/202175/security/u-s-cisa-adds-ivanti-connect-secure-flaws-to-its-known-exploited-vulnerabilities-catalog.html

### 4. Android「SMS of Death」CVE-2026-58882 — 零点击远程崩溃
谁／打什么：畸形 WAP Push 短信可使电话进程崩溃、掉线（含紧急呼叫）；已有公开 PoC。补丁：10 月安全更新修复 Android 14–17，12/13 据称无修复。
- X 原帖：https://x.com/V0iD_0daY/status/2116908105938461137 ；https://x.com/sambenjamin___/status/2116836585043800196 ；https://x.com/White_Hunters/status/2116689683623321826
- 文章：https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/ （抽查返回 403，链接保留）

### 5. Microsoft 365 AiTM 会话 Cookie 劫持（Mirage2FA，CVE-2026-69836）
谁／打什么：AiTM 代理绕过 MFA，文中称窃取 4,561 个 M365 会话 Cookie；文章给出检测规则与 WHfB／Cloud Kerberos Trust 加固指南。
- X 原帖：https://x.com/Dinosn/status/2116946099059511340 （LWiS）
- 文章：https://doit4everyone.github.io/mvc-nlpd-m365/aitm-cookie-hijacking/

### 6. NetScaler ADC CVE-2026-107406 — SAML 内存溢出，公开利用已出
补丁：14.1-73.46、13.1-64.29 及以上。
- X 原帖：https://x.com/cvedotnow/status/2116899225187357163
- 文章：https://cve.now/CVE-2026-107406

### 7. LightSAML（PHP）CVE-2026-63182 — 签名校验缺陷，威胁 SSO 信任
Alan Turing 研究所 Cyber Threat Observatory 分析称已有现成 PoC；排查依赖 LightSAML 的 SSO 组件。
- X 原帖：https://x.com/TuringCyberObs/status/2116925246338904499
- 分析（GitHub）：https://github.com/alan-turing-institute/cyber-threat-observatory/blob/main/reports/2026-10-30/TIER_2_CVE-2026-63182.md

### 8. SOHO／IoT：D-Link DIR-505 CVE-2026-120189（CVSS 10，EOL 无补丁）与 WAVLINK WL-WN530BE1-A CVE-2026-120198（CVSS 9.3，命令注入）
处置：D-Link 已 EOL，厂商建议下线替换；WAVLINK 关注固件更新，限制管理面暴露。
- X 原帖：https://x.com/ThreatAft/status/2116714715779117248 ；https://x.com/cveintelligence/status/2116955487556206965 ；https://x.com/cveintelligence/status/2116942240153317440
- 文章：https://threataft.com/articles/d-link-dir-505-cve-2026-120189-tftp-stack-overflow ；https://learnctem.com/cve-intelligence-hub/cve-2026-120198

### 9. Apple macOS CVE-2026-112487 — 路径处理问题，已出 PoC
补丁：macOS Golden Gate 27.2。
- X 原帖：https://x.com/ptdbugs/status/2116796575297008083
- 文章：https://dbu.gs/vulnerability/PT-2026-125183

### 10. Windows 11 LPE「TrustedHive」（CBS 会话 COM 对象 + junction 任意写）
研究者称可能与已有 CVE 重复；防御：关注 TrustedInstaller/CBS 相关异常 junction 与文件写入。
- X 原帖：https://x.com/ipurple/status/2117010291095478545 （LWiS）；https://x.com/ipurple/status/2117002763494359127 （LWiS 转推原作者）
- GitHub／PoC：https://github.com/dis0rder0x00/TrustedHive

## 工具与 GitHub 发布（每条：说明 + 地址列表）

- **Pass-ta-key**：研究从 Chrome 进程内存提取 Google 密码管理器 Security Domain Secret 并解密同步 passkey（含博客与工具）。防御：关注对 Chrome 进程的内存读取。
  - X：https://x.com/ipurple/status/2116947982146732368 ；https://x.com/ipurple/status/2116963482629230789 ；https://x.com/maxime_tz/status/2116796331930816745
  - GitHub：https://github.com/0rcruxe/pass-ta-key
  - 文章：https://0rcruxe.github.io/posts/pass-ta-key-golden-attack-sds-extraction/
- **blackmagick-c2**（Teach2Breach 发布的商业／申请制 C2，附厂商对比页）。
  - X：https://x.com/Teach2Breach/status/2116731215424188655 ；https://x.com/Teach2Breach/status/2116746533068521623
  - 地址：https://blackmagick.io/c2/compare
- **Suzaku「Vulnpocalypse」版本**（Yamato Security 云日志威胁狩猎工具）。
  - X：https://x.com/DirectoryRanger/status/2116938028132511999
  - GitHub：https://github.com/Yamato-Security/suzaku
- **Trawler**（PowerShell，IR 发现持久化机制，映射 MITRE）。
  - X：https://x.com/EsGeeks/status/2117002875624882555
  - GitHub：https://github.com/joeavanzato/Trawler
- **AgentSec Inspector**（开源 AI 红队／MCP、RAG 安全审计桌面工具）。
  - X：https://x.com/St0rnPentest/status/2116850362963358011
  - GitHub：https://github.com/St0rn/agentsec-inspector
- **PentestCode**（多智能体渗透测试框架）及实战复盘。
  - X：https://x.com/altereddude/status/2116895639975899330
  - GitHub：https://github.com/s0ld13rr/pentestcode
  - 文章：https://blog.zakaria.lu/a-pentest-agent-fleet-against-my-own-site-what-the-architecture-got-right
- **智能体安全清单**：cloudflare/security-audit-skill、NVIDIA/SkillSpector 等。
  - X：https://x.com/AsWill11/status/2116829624034369745
  - GitHub：https://github.com/cloudflare/security-audit-skill ；https://github.com/NVIDIA/SkillSpector
- **gecko**（ioncodes）与 **LinuxMalwareTechniques**（Linuxfest 资料）。
  - X：https://x.com/layle_ctf/status/2116995149834461457 ；https://x.com/m3g9tr0n/status/2116773749512970658
  - GitHub：https://github.com/ioncodes/gecko ；https://github.com/akazemi67/LinuxMalwareTechniques

## APT / Malware 分析（每条：说明 + 地址列表）

- **ARTEX 攻击框架／网关**：被报道波及韩国银行、日本企业，并有微软公告；Profero IR 在 10 月下旬事件中见到操作者将其作为工具链一环。@stop_spammerz 公开了基于 FOFA 的网关特征和一批疑似基础设施（原样见 IoC 节）。
  - X：https://x.com/ProferoSec/status/2116650839435882923 ；https://x.com/stop_spammerz/status/2116576361976418689 ；https://x.com/cyb3rops/status/2116863132081742080 （LWiS 转推）；https://x.com/N3mes1s/status/2116776015431143657 （LWiS 转推）
- **NetamLoader**（Kaspersky）：针对亚洲政府专用 Windows 10 定制版，CAB 包放在 Windows Update 下载目录、借 Patch My PC 合法组件做 AppDomainManager 注入加载 .NET 程序集，疑似供应链；未归因。
  - X：https://x.com/Dinosn/status/2116846894467166506 （LWiS）
  - 文章：https://thehackernews.com/2026/11/netamloader-malware-targets-government.html
- **Polymarket／DebugBear 脚本劫持**：DebugBear 域名注册商侧 DNS 被改，Polymarket 加载的 RUM 脚本被替换，盗走约 270 万美元（726 个钱包，平台承诺退款）。狩猎：审计第三方前端脚本、启用 SRI/CSP。
  - X：https://x.com/Dinosn/status/2116846797263921193 （LWiS）
  - 文章：https://thehackernews.com/2026/11/hackers-steal-about-27-million-from.html
- **Alpine Linux GitLab 遭 RCE 尝试后重建**。
  - X：https://x.com/Dinosn/status/2116945993782464795 （LWiS）
  - 文章：https://www.bleepingcomputer.com/news/security/alpine-linux-rebuilds-gitlab-after-attempted-rce-attack/ （抽查返回 403，链接保留）
- **检测与取证（LWiS）**：Elastic 解读 Windows Endpoint Security Platform（wesp.sys）；Defender 远程会话字段不覆盖 PowerShell Remoting；Windows 功能更新对取证时间线的影响；MDE 自定义数据采集规则；PowerShell「shedskin」规避 Defender 扫描研究。
  - X：https://x.com/DirectoryRanger/status/2116911302203306181 ；https://x.com/DirectoryRanger/status/2116910229220626563 ；https://x.com/DirectoryRanger/status/2116909364543918340 ；https://x.com/DirectoryRanger/status/2116907901067432141 ；https://x.com/ipurple/status/2116977211404419278
  - 文章：https://www.elastic.co/security-labs/blog/windows-endpoint-security-platform-wesp ；https://ridgelinecyber.com/blog/remote-session-columns-that-miss-powershell-remoting/ ；https://thelocalh0st.com/posts/windows-feature-update-evidence/ ；https://jeffreyappel.nl/microsoft-defender-for-endpoint-beyond-default-telemetry-with-custom-data-collection-rules/ ；https://cornfield.sh/shedskin/
- **勒索通报（X 聚合账号，未经核实）**：Qilin 声称攻击 Global Holding、Danser Inc.、fzmb GmbH；HYFLOCK 声称 Hitech Group；SHIBA 声称 TEMA；BARRACUDA 声称 Evinoks。
  - X：https://x.com/FalconFeedsio/status/2116938696230658269 ；https://x.com/FalconFeedsio/status/2116747521154592912 ；https://x.com/FalconFeedsio/status/2116955938683035773 ；https://x.com/FalconFeedsio/status/2116921518462751125 ；https://x.com/FalconFeedsio/status/2117010026401607991 ；https://x.com/digvijay_k11/status/2116759426338099365

## SecureFlow 信息流精选（X 上未出现的高信号条目；每条：来源 + 说明 + 原文链接）

（实际区间：北京时间 2026-10-29 13:00 – 2026-10-31 05:41；本期与 X 无同一事件重叠。）

- **ZDI｜MLflow 批量漏洞（ZDI-26-839 ~ 847）**：多处不可信数据反序列化 RCE、SSRF、缺失授权提权／信息泄露。自建 MLflow 尽快升级并勿对外暴露 Tracking Server。
  - https://www.zerodayinitiative.com/advisories/ZDI-26-845/ （同批：ZDI-26-839、840、841、842、843、844、846、847，路径同格式）
- **ZDI｜Linux 内核本地提权批次**：XFRM UAF（ZDI-26-837）、IPv6 AH 路由头整数下溢（ZDI-26-834）、Logitech HIDPP UAF（ZDI-26-835）、CIFS UAF（ZDI-26-836）；另 FreeBSD TTY 竞争 LPE（ZDI-26-838）。
  - https://www.zerodayinitiative.com/advisories/ZDI-26-837/ ；https://www.zerodayinitiative.com/advisories/ZDI-26-838/
- **ZDI｜Valkey clusterCreatePublishMsgBlock 数值截断 RCE（ZDI-26-833）**。
  - https://www.zerodayinitiative.com/advisories/ZDI-26-833/
- **ZDI｜0Day：Pwn2Own Alpine iLX-F511 车机多处 RCE（ZDI-26-821/824/827/828/829）与 Ultralytics 代码注入／反序列化（ZDI-26-813/815/816）**（发布于 10-28，未修复 0Day，供参考）。
  - https://www.zerodayinitiative.com/advisories/ZDI-26-828/ ；https://www.zerodayinitiative.com/advisories/ZDI-26-813/
- **奇安信攻防社区｜RouterOS CVE-2026-67281 分析**。
  - https://forum.butian.net/share/5166 （抽查 403，可能需浏览器访问）
- **HackerOne｜37signals／Basecamp OAuth 系列**：OAuth 授权服务器向未验证重定向颁发凭据导致账户接管、第三方 OAuth token 可换取完整 launchpad 会话、跨账户 webhook 接管。
  - https://hackerone.com/reports/3955956 ；https://hackerone.com/reports/3999856 ；https://hackerone.com/reports/3979217
- **HackerOne｜CVE-2026-61792 修复不完整（.svn/.bzr 元数据排除绕过）**。
  - https://hackerone.com/reports/4037976
- **Seebug Paper｜LLM 智能体跨会话残留攻击基准；证据锚定的 LLM 辅助 Android 取证**。
  - https://paper.seebug.org/3530 ；https://paper.seebug.org/3531 （抽查返回 521，源站暂不可达，链接保留）

## 地址／IoC 汇总

以下为原帖原样抄录，未经本报独立验证，仅供狩猎比对：

**ARTEX（来源：https://x.com/stop_spammerz/status/2116576361976418689 ，FOFA 特征 `header="ARTEX Gateway"`）**
```
43.98.163.80
47.84.111.176
43.98.196.73
88.216.191.9
47.236.38.40
47.237.6.12
43.106.102.56
124.243.189.69:10443
www.payload-usa[.]com
43.98.181.63
47.84.127.146
43.98.168.25
47.84.127.193
43.98.196.73:8080
```

**NetamLoader（来源：https://thehackernews.com/2026/11/netamloader-malware-targets-government.html ，引述 Kaspersky）**
```
C:\Windows\SoftwareDistribution\Download\e4537a1762fcafd2fd96bfc825bad34f9db9a24
C:\Windows\SoftwareDistribution\Download\Install\
fabric.config
```

其他条目：未见公开 IoC。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）: https://x.com/i/lists/1239330068461244424 （本期读取 192 条，覆盖 2026-10-31T16:17Z – 2026-11-01T22:45Z；成员备份已写入 lwis-sources/x-list-members.json 与 x-list-handles.txt，先存前 200 名，列表还有后续页）
- 博客清单: https://blog.badsectorlabs.com/files/blogs.txt （本地: lwis-sources/blogs.txt）
- CISA KEV: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD: https://nvd.nist.gov/
- Risky Business: https://risky.biz/
- tl;dr sec: https://tldrsec.com/
- SecureFlow 安全信息流: https://secureflow.scope-sentry.top/all （只读接口: https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200）

## 来源搜索 URL（含 SecureFlow 接口与覆盖区间）

- X Latest（CVE/PoC/exploit/0day）：https://x.com/search?q=%28CVE%20OR%20PoC%20OR%20exploit%20OR%200day%29%20-filter%3Areplies&f=live
- X Latest（GitHub + C2/red team/nuclei）：https://x.com/search?q=url%3Agithub.com%20%28C2%20OR%20%22red%20team%22%20OR%20nuclei%29&f=live
- X Latest（malware analysis / threat report / threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- X 读取方式：Grok Bot 公开只读检索（时间窗 2026-10-31T23:00Z – 2026-11-01T22:59Z）+ 已连接 X 插件只读读取 List；未发帖、点赞、转推、收藏、回复。
- SecureFlow 接口：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （总量 13878；严格 48h 内 0 条，实际采用北京时间 2026-10-29 13:00 – 2026-10-31 05:41）
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （最近新增 2026-10-30）

## 交付状态

- Box：/home/box/workspace/security-watch/reports/2026-11-01-x-security-digest.md
- 本机：~/Desktop/X安全情报晚报/2026-11-01-x-security-digest.md（2026-11-02 补投，原定时任务在拷贝前中断）
