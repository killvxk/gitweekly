# X 安全情报晚报 · 2026-11-02

覆盖窗口：2026-11-01 20:15 至 2026-11-02 20:15（America/Santiago，UTC-3），约 24 小时。X 只读读取 11 次（主题检索、LWiS 成员检索 3 次、指定帖批量查询 2 次），0 次 429；所收帖子均为本窗口新帖，不与 seen_ids 重复。t.co 均已从卡片展开（只有图片的帖只列原帖）。公开备援：CISA KEV JSON（2026.10.30，共 1766 条，截至 20:15 本日未更新，Δ0）、NVD、厂商与研究机构页面。IoC 一律 defang。本报告为防御向，不转载利用代码、payload 或复现步骤。

## 今日摘要

- **Ivanti Connect Secure CVE-2026-111357 今日（11-02）KEV 到期**：X 上 DFIR Radar 整理 Volexity 狩猎要点——10-13 的 25.1.1.2／22.8R2.5 只修了 104935，**必须升级到 25.1.1.3 或 22.8R2.6**；Ivanti ICT 完整性检查在已失陷设备上也会显示干净。118527 截止 11-13。
- **WordPress CryptoPayment Gateway CVE-2026-81648（CVSS 10）首次观测到在野利用尝试**（Defused 蜜罐），可读取明文钱包凭据并覆盖网关设置；未进 KEV。
- **Citrix NetScaler ADC/Gateway CVE-2026-88773（CVSS 9.3，HTTP 请求走私）研究员公开 PoC**；未进 KEV、未见在野；修复 14.1-73.37／13.1-64.23（建议 14.1-73.49／13.1-64.32）。
- **Linux TCP UAF CVE-2026-98432 后续**：Ubuntu 与 RHEL 8/9/10 截至 11-01 19:30 UTC 仍有版本无修复，Red Hat 公告 RHSB-2026-016 给出 nftables 临时缓解；仍未进 KEV，未见在野。
- **GTIG／Mandiant「LLMJacking」报告（11-02）**：攻击者窃取云 IAM／GitHub PAT／LLM API key，用 max_tokens=1 的小请求验证 key，再经「LLM Mixer」转卖配额，单日盗刷超 10 万美元。
- **Cisco Talos：VOLTA-AUTODOXER 窃密木马**把偷到的数据经 OpenRouter 交给大模型评估「受害者价值」；Talos 未确认在野部署。
- **智利相关**：FalconFeeds 称 Isapre Consalud 被列上 Qilin 勒索泄露站（未经证实）。
- **工具**：Impacket-IoCs（Impacket 检测特征）、NWH Stealer 静态分析仓库、Quarry（Claude Code 渗透插件）、PortSwigger 官方 Burp MCP Server。

## CVE / POC / 漏洞

### 1. Ivanti Connect Secure 三连 0day（104935／111357／118527）：111357 今日 KEV 到期
UTA0576 自 10-03 起利用链式漏洞拿到未认证 root，行动不落 webshell，每条命令都重跑整条链；落地后用自制 Python LDAP 工具查询 LAPS 密码、BitLocker 恢复密钥，并做 Kerberos 凭据测试与密码喷洒。关键补丁缺口：10-13 发布的 25.1.1.2／22.8R2.5 只修 CVE-2026-104935，**111357 与 118527 要到 25.1.1.3 或 22.8R2.6 才修**。Ivanti Integrity Checker 可能漏报（内存补丁、事后恢复 DSCache 条目、删日志）。狩猎：至少回溯到 10-01；查 `/dana-na/auth/url_default/welcome.cgi` 请求中 URL 路径与 `X-DSCGI-PATH` 头不一致；查 `/data/.icscap` 隐藏目录、`/home/runtime/tmp/ics-root-*` 文件、名为 `dsstatmond` 的进程；疑似失陷则恢复出厂、重置 AD 服务账号、轮换所有可读到的 LAPS／BitLocker 秘密。KEV：111357 due 11-02（今日），118527 due 11-13。
- X 原帖：https://x.com/DFIR_Radar/status/2117316361240084825
- X 原帖：https://x.com/DFIR_Radar/status/2117346460723269668
- X 原帖：https://x.com/Dinosn/status/2117240316545650928
- X 原帖：https://x.com/exploitgrid/status/2117268620992753711
- 文章（Volexity，含 IoC 与 YARA）：https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/
- 文章（Rapid7）：https://www.rapid7.com/blog/post/etr-additional-ivanti-connect-secure-zero-days-exploited-in-the-wild-cve-2026-111357-cve-2026-118527/
- 文章（THN）：https://thehackernews.com/2026/10/attackers-chain-three-ivanti-connect.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-111357
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-118527
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-111357
- 地址／IoC（引自 DFIR Radar 转述 Volexity）：`108.165.147[.]64`（攻击者 OpenVPN VPS，9-30 至 10-07 活跃）；主机文件名 `/tmp/ml[.]py`、`/tmp/rq5[.]py`、`/tmp/mk[.]py`、`/tmp/rr[.]py`、`/tmp/pu.txt`、`/tmp/sp_out.txt`、`/tmp/spray_hits.json`、`/data/.icscap/dsstatmond`、`/data/.icscap/h[.]py`、`/home/runtime/tmp/ics-root-run-inband-*.pl`、`/home/runtime/tmp/ics-root-result-inband-*`

### 2. WordPress CryptoPayment Gateway CVE-2026-81648（CVSS 10）：首次观测到在野利用尝试
Defused 称其蜜罐记录到针对该插件的利用尝试，此前无公开在野报告。漏洞可让未认证者读取站点保存的支付网关设置（含明文钱包凭据）并覆盖配置。攻击来源为自称「Anonymous KYC-Free VPS Hosting」的基础设施。未进 KEV。处置：确认插件是否使用、升级或停用插件，并轮换网关里存过的钱包／API 凭据。
- X 原帖：https://x.com/DefusedCyber/status/2117325160608870613
- 厂商／IoC 平台（需注册）：http://console.defusedcyber.com/signup
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-81648
- 地址／IoC：Defused 称完整 IoC 在其 Radar 平台（需注册），帖内未公开，故未抄录

### 3. Citrix NetScaler ADC & Gateway CVE-2026-88773（CVSS 9.3）：公开 PoC
HTTP/SSL vserver 上的 HTTP 请求走私。受影响 14.1 < 14.1-73.37、13.1 < 13.1-64.23（含 FIPS/NDcPP）。ThreatWire 称研究员已发布 PoC（未经 Citrix 确认），无缓解措施，未进 KEV，未见在野。建议直接升到 14.1-73.49／13.1-64.32。
- X 原帖：https://x.com/ThreatWire_/status/2117171954058764792
- 文章：https://www.threatwire.tech/news/upgrade-netscaler-researchers-publish-poc-for-request-smuggling-flaw-cve-2026-88773
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-88773
- 地址／IoC：未见公开 IoC

### 4. Linux 内核 TCP UAF CVE-2026-98432 后续（未进 KEV）
X 上 Roland Gorczynski 整理的补丁状态（截至 11-01 19:30 UTC）：已修 Debian bookworm/trixie、SLES 16.0／15 SP4–SP6 LTSS、openSUSE Leap 16.0、Oracle UEK、Amazon Linux 2/2023；未修 Ubuntu 22.04–26.10（修复进行中）与 RHEL 8/9/10（公告 RHSB-2026-016）；AlmaLinux 只在 testing 源有修复。上游修复版本 5.10.272、5.15.223、6.1.190、6.6.159、6.12.113、6.18.56、7.2.10、7.3。临时缓解见 Red Hat 公告中的 nftables 规则（不能完全防护）；装完内核必须重启。Liran Tal 等人质疑为何仍未进 KEV——目前无在野证据。
- X 原帖：https://x.com/RGorczynskiOPS/status/2117136195989713170
- X 原帖：https://x.com/TweetThreatNews/status/2117373326750285936
- X 原帖：https://x.com/liran_tal/status/2117181170383278517
- 文章：https://cyber.hendryadrian.com/article/14144/linux-kernel-tcp-flaw-cve-2026-98432-may-enable-remote-code-execution
- 厂商公告：https://ubuntu.com/security/CVE-2026-98432
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-98432
- 地址／IoC：未见公开 IoC

### 5. 其他：PAN-OS CVE-2026-0322 提醒；OpenAirInterface 5G 核心网一批 CVE
EMITS 再次提醒 PAN-OS CVE-2026-0322（8.6，需管理接口访问即可 root 执行命令，KEV 中自 10-17 逾期）：限制管理面到可信 IP 并打补丁。Kaitan 自动账号把 OpenAirInterface CN5G AMF/UDM v2.2.1 的 CVE-2026-117067／117068／117069／106808 标为「Exploit in the wild」，但未给出一手来源，KEV 中也没有，**可信度低，仅作观察**。
- X 原帖：https://x.com/emits_ca/status/2117330428797559011
- X 原帖：https://x.com/KaitanSecurity/status/2117368663028154878
- 文章：https://emits.ca/advisories.html
- 文章：https://sec.kaitan.id/cves/CVE-2026-117069
- 文章：https://sec.kaitan.id/cves/CVE-2026-117067
- 文章：https://sec.kaitan.id/cves/CVE-2026-117068
- 文章：https://sec.kaitan.id/cves/CVE-2026-106808
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-0322
- 地址／IoC：未见公开 IoC

### 6. KEV 到期提醒（本日无新增）
新出现 CVE 推送账号 EnclaveRadar（仅作补充源）。目录仍为 2026.10.30／1766 条（截至 20:15 周一未更新，Δ0）。**今日 11-02 到期**：Ivanti Connect Secure CVE-2026-111357。**11-03**：Plex Media Server CVE-2026-96652／96655、Siemens Software Center CVE-2026-110936。之后：11-10 Magento 48356、Brotli 111497；11-11 VMware ESX 41709；11-13 Ivanti 118527。**昨日起逾期**：GitLab 97229、Cisco ASA/FTD 76418；更早逾期：Fragnesia 46300（10-31）、PHP2Shell 109618/109619（10-29）等。
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 文章：https://threatpodium.com/threat-intelligence-report-2026-11-01/
- X 原帖：https://x.com/EnclaveAI/status/2117232863552958597
- 文章：https://app.enclave.ai/threat-feed
- 地址／IoC：未见公开 IoC

## 工具与 GitHub 发布

### 1. Impacket-IoCs：Impacket 检测特征整理
作者内部重写 Impacket 时整理出库内固有的可检测特征（IoC），对蓝队写 Impacket 检测规则、红队评估暴露面都有用。
- X 原帖：https://x.com/CyberWarship/status/2117265506851791245
- GitHub：https://github.com/ThatTotallyRealMyth/Impacket-IoCs
- 地址／IoC：仓库本身即特征清单，未逐条抄录

### 2. NWH Stealer 静态分析仓库（ipurple 转发）
分析 NWH Stealer：借 Bun JavaScript 运行时无文件执行、内存中窃取剪贴板图片、滥用 AWS／Cloudflare R2 作 C2 外传。
- X 原帖：https://x.com/ipurple/status/2117388030063612318
- GitHub：https://github.com/kaandemir993/NWH-Stealer-Analysis-Fileless-Bun-Runtime-Execution-Clipboard-Image-Theft-Cloud-C2-AWS-R2-
- 地址／IoC：帖文未列具体 IoC，请看仓库；未抄录

### 3. Quarry：Claude Code 渗透测试插件
开源全流程渗透插件，强调哈希链证据与防「幻觉漏洞」规则；作者自称在 DVWA／crAPI／Juice Shop 上 100% 召回（未独立验证）。
- X 原帖：https://x.com/myco_razon/status/2117281338114048427
- GitHub：https://github.com/mahumadad/quarry
- 地址／IoC：未见公开 IoC

### 4. PortSwigger 官方 Burp Suite MCP Server
把 Burp 暴露给 MCP 客户端，让模型直接基于被测流量工作。
- X 原帖：https://x.com/PentestAIStack/status/2117269829199818798
- GitHub：https://github.com/PortSwigger/mcp-server
- 地址／IoC：未见公开 IoC

### 5. LWiS 成员动态（低信号）
ProjectDiscovery 继续推 neo AI 渗透（Skyscanner 案例）；runZero 的 HD Moore 节目谈 5k 个暴露 BACnet 设备；Rad 讨论给攻击工具植入后门的问题。
- X 原帖：https://x.com/pdiscoveryio/status/2117310687273992455
- X 原帖：https://x.com/runZeroInc/status/2117272552691171486
- X 原帖：https://x.com/rad9800/status/2117115193864102232
- 地址／IoC：未见公开 IoC

## APT / Malware 分析

### 1. GTIG／Mandiant：LLMJacking 报告（11-02）
Mandiant 2026 年处理多起企业 LLM 访问被劫持事件（北美、南美、亚太；金融、零售、科技、运输）。初始访问主要是云身份被盗：IAM 凭据、服务账号密钥、GitHub PAT、会话令牌；随后克隆仓库找秘密、创建高权限服务账号令牌、注入 SSH 密钥、伪装成「计费优化工具」的后门服务账号。用 max_tokens=1 的极小请求验证偷来的 LLM key 以避开用量告警，再通过「LLM Mixer」网关以约 60 美元/月转卖配额；单日盗刷超 10 万美元，累计可达 100 万美元。报告点名 UNC6993 等集群。防御：集中轮换秘密、最小权限 IAM、代码秘密扫描、API 配额与支出上限、把「未授权启用 LLM 服务」视为高危告警。
- X 原帖：https://x.com/fr0gger_/status/2117335710781079893
- X 原帖：https://x.com/fr0gger_/status/2117335712714588509
- X 原帖：https://x.com/fr0gger_/status/2117335714400731212
- 文章（GTIG）：https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models/
- 文章：https://siliconangle.com/2026/11/02/google-finds-llmjacking-attackers-running-up-100k-a-day-in-fraudulent-cloud-charges/
- 文章：https://www.theregister.com/security/2026/11/02/token-thieves-costing-companies-100k-per-day-in-illicit-llm-charges/5306967
- IoC 汇总（第三方）：https://ioc.socradar.io/reports/the-rise-of-llmjacking-how-threat-actors-monetize-compromised-cloud-and-model-resources-fd209ff2917c
- 地址／IoC（SOCRadar 摘自报告）：SHA256 `4377d2403ea17a04744ca871113c1313b0162f190f0b785f5a10b744e8528245`；域名 `newapi[.]pro`；代号 `D1337-KAIROS`

### 2. Cisco Talos：VOLTA-AUTODOXER 窃密木马用大模型给受害者「估价」
Windows 窃密木马，窃取浏览器密码、银行卡、加密钱包助记词、会话令牌与云凭据，汇总成受害者档案，再经 OpenRouter 发给大模型（配置默认 Claude Opus 4.6，被拒时依次换 Kimi K2、Gemini 2.5 Flash）生成「WHAT THEY'RE WORTH」评估；也可跳过 AI 步骤并自删除。**Talos 未确认在野投放**。狩猎建议（X 帖转述）：告警无头 Chrome、保留 `volta_debug.txt`、吊销令牌。
- X 原帖：https://x.com/arcXonline/status/2117190212862235007
- X 原帖：https://x.com/AndruEdwards/status/2117035490209603922
- X 原帖：https://x.com/tsnmediahub/status/2117259204025016392
- 文章（Talos）：https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/
- 文章（WIRED）：https://www.wired.com/story/kernel-panic-volta-autodoxer-ai-infostealer-malware/
- 文章：https://www.tomshardware.com/tech-industry/cyber-security/new-ai-driven-windows-malware-feeds-stolen-data-to-claude-to-rank-victims-assets-by-value-then-deletes-itself-payload-builds-custom-target-assessment-can-switch-models-if-one-refuses-or-skip-the-ai-step-entirely
- 地址／IoC：X 帖仅提到文件名 `volta_debug.txt`；哈希等请看 Talos 原文，本报告未抄录

### 3. Volt Typhoon「Silent Train」后续报道（CyberScoop）
CyberScoop 引 Lumen Black Lotus Labs：Volt Typhoon 自 2023 年底起不断轮换被控 SOHO 路由器、IoT 与企业设备，组成一次性中继网络掩护对关键基础设施的 0day 攻击（10-28 晚报已收录首发）。另：X 上流传「五眼＋日本联合预警 Salt Typhoon」「100 万部美国手机被黑」等帖，均无一手来源链接，**未核实，不采信**。
- X 原帖：https://x.com/CyberScoopNews/status/2117394072063111496
- X 原帖：https://x.com/Security_PLo/status/2117244895740215311
- 文章：https://scoopmedia.co/47Pjdgn
- 地址／IoC：未见公开 IoC

### 4. 勒索与数据泄露（未经证实，仅受害方公告）
FalconFeeds 等称：**智利 Isapre Consalud 被 Qilin 列上泄露站**；另有 Michigan State University（Byod）、阿根廷 REFSA（NightSpire）及 Akira、SAFEPAY 新增受害者帖。欧洲超市冷链系统被攻击的说法（WarMonitor）缺来源，vx-underground 称暴露在网上的冷柜控制面板被滥用。
- X 原帖：https://x.com/FalconFeedsio/status/2117364792784794002
- X 原帖：https://x.com/FalconFeedsio/status/2117124554413985810
- X 原帖：https://x.com/FalconFeedsio/status/2117226808299139155
- X 原帖：https://x.com/vxunderground/status/2117335140313780446
- X 原帖：https://x.com/WarMonitor3/status/2117227376077676887
- 受害方网站：https://www.consalud.cl/
- 地址／IoC：未见公开 IoC

## 地址／IoC 汇总

全部已 defang，抄自所引来源：
- Ivanti ICS（UTA0576，经 DFIR Radar 转述 Volexity）：IP `108.165.147[.]64`；主机路径 `/tmp/ml[.]py`、`/tmp/rq5[.]py`、`/tmp/mk[.]py`、`/tmp/rr[.]py`、`/tmp/pu.txt`、`/tmp/sp_out.txt`、`/tmp/spray_hits.json`、`/data/.icscap/`（含 `dsstatmond`、`cap*`、`h[.]py`）、`/home/runtime/tmp/ics-root-run-inband-*.pl`、`/home/runtime/tmp/ics-root-result-inband-*`；进程名 `dsstatmond`；请求特征为 `welcome.cgi` 路径与 `X-DSCGI-PATH` 头不一致。完整列表：https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/
- LLMJacking（GTIG，经 SOCRadar）：SHA256 `4377d2403ea17a04744ca871113c1313b0162f190f0b785f5a10b744e8528245`；域名 `newapi[.]pro`
- VOLTA：文件名 `volta_debug.txt`（哈希见 Talos 原文）
- CryptoPayment Gateway 81648、NWH Stealer：IoC 在 Defused 平台／GitHub 仓库，帖内未公开
- 其余条目：未见公开 IoC

## LWiS 固定信源（每日交叉，不替代 X Latest）

Bad Sector Labs [Taking a Break - 2026-04-06](https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html) 公开的 LWiS 信源。情报仍与 X Latest 交叉合并。

- LWiS X List（Cybersecurity，500 Members）：https://x.com/i/lists/1239330068461244424
- List 成员页：https://x.com/i/lists/1239330068461244424/members
- 成员备份（500 handle）：`/home/box/workspace/security-watch/lwis-sources/x-list-handles.txt`
- 成员 JSON：`/home/box/workspace/security-watch/lwis-sources/x-list-members.json`
- LWiS 博客清单（443 URL）：https://blog.badsectorlabs.com/files/blogs.txt
- 博客清单本地副本：`/home/box/workspace/security-watch/lwis-sources/blogs.txt`
- Risky Business 播客：https://risky.biz/
- tl;dr sec 通讯：https://tldrsec.com/
- 复刊通知：https://subscribe.badsectorlabs.com/subscription/form


本日对 LWiS List 成员做了 3 次检索，大多为非安全内容；有用的 vx-underground（Base64 编码的 Python 恶意代码提醒：https://x.com/vxunderground/status/2117316330193858817 ）、ProjectDiscovery、runZero、Rad 数条已并入上文。

## 来源搜索 URL

- https://x.com/search?q=CVE%20PoC%20exploit%200day&f=live
- https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- https://x.com/i/lists/1239330068461244424
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://nvd.nist.gov/vuln/search
- https://blog.badsectorlabs.com/files/blogs.txt
- https://risky.biz/
- https://tldrsec.com/
