# X 安全情报晚报 · 2026-08-17

> 搜集窗口：约过去 24 小时（圣地亚哥时间 2026-08-16 21:50 至 2026-08-17 20:15，America/Santiago / UTC-4）
> 主源：X 已登录；Latest 搜索 1（CVE/POC）已收回。搜索 2／3（GitHub C2、APT/malware）因浏览器驱动中断未完成，不假装有这两路 X 内容
> 公开备援：CISA KEV / NVD / Apple / Rapid7 / BleepingComputer / GitHub
> 规则：每条含完整 https URL；没有指标就写「未见公开 IoC」
> 说明：防御向晚报。不转载利用代码、payload 或复现步骤；不把利用仓库当操作指南。

## 今日摘要

- **Forminator Forms CVE-2026-15748（X 补录，CVSS 9.8）**：未认证任意文件上传可导致 RCE。影响 ≤1.56.1，修复 1.56.2。约 60 万站点。
- **GitLab CE/EE CVE-2026-19478（X 补录，CVSS 9.4）**：未认证经 GraphQL 可改删公开项目。自管实例升到 19.2.4 / 19.1.6 / 19.0.8 / 18.11.11。
- **CISA KEV 新增 CVE-2025-62593（Ray）**：catalogVersion 2026.08.17，条目 1666。Ray <2.52.0 代码注入，Firefox/Safari + DNS 重绑定可打本地开发者。联邦期限 2026-08-20。升到 2.52.0。
- **Apple 8/17 安全更新**：iOS/iPadOS 26.6.1、iOS/iPadOS 18.7.10、macOS Tahoe 26.6.2、visionOS 26.6.1。含 ImageIO ACE CVE-2026-65346、内核 UAF CVE-2026-65343、iPhone IPSec 绕过 CVE-2026-65329 等。
- **Defender ShieldBreak CVE-2026-69414**：微软确认在跟，补丁尚未出。据报为 RoguePlanet CVE-2026-50656 的绕过。
- **Rapid7 Operation ASTERIX**：假 Trezor/Ledger/Exodus + 语音钓鱼，IoC 见下文。
- **事件**：TheHatman 叫卖约 364 万条 Azure/Entra 目录（受害方有争议）；Pokémon Center 经 CEVA 物流泄露；法国税务总局 DGFiP 67.8 万人税务数据。
- **工具**：nuclei-templates 仍为 v10.4.7。本窗口新建 meridian C2 仓。

## CVE / POC / 漏洞

### 1. CISA KEV 新增 CVE-2025-62593（Ray-Project Ray 代码注入）

2026-08-17 CISA 将 CVE-2025-62593 列入 KEV（catalogVersion 2026.08.17，dateReleased 2026-08-17T17:00:24Z，条目 1666）。Ray <2.52.0 对未认证 job API 的浏览器请求防护不足（仅看 User-Agent 是否以 Mozilla 开头）；Firefox/Safari 可改 UA，再配合 DNS 重绑定，可对本地跑 Ray 的开发者做 RCE。GitHub Advisory GHSA-q279-jhrf-cc6v 评 CVSS v4 9.4。已修 2.52.0，并增加默认关闭的 token 认证。BOD 26-04 联邦期限 2026-08-20。NVD 称 CISA-ADP exploitation=active；引用的 Bitsight RondoDox 文为 2026-03-11，非本日 IoC 包。本晚报不转载利用步骤。

地址：
- CISA 通报：https://www.cisa.gov/news-events/alerts/2026/08/17/cisa-adds-one-known-exploited-vulnerability-catalog
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- 厂商 Advisory：https://github.com/ray-project/ray/security/advisories/GHSA-q279-jhrf-cc6v
- 补丁：https://github.com/ray-project/ray/commit/70e7c72780bdec075dba6cad1afe0832772bfe09
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2025-62593
- 文章：https://www.bitsight.com/blog/rondodox-botnet-infrastructure-analysis

IoC：未见公开 IoC。

### 2. Apple 2026-08-17 安全更新

Apple 本日发布：iOS/iPadOS 26.6.1、iOS/iPadOS 18.7.10、macOS Tahoe 26.6.2、visionOS 26.6.1（后者详情页仍写 Details coming soon）。较显著条目包括 ImageIO 整数溢出任意代码执行 CVE-2026-65346、内核释放后使用 CVE-2026-65343、iPhone 11 及更新机型上特权网络攻击者可绕过 IPSec 认证 CVE-2026-65329、AVEVideoEncoder 内核 CVE-2026-64747、MediaRemote 至 root CVE-2026-43723。未见在野利用说明。macOS Screen Sharing CVE-2026-65400 已在前几日晚报覆盖，不展开。

地址：
- 厂商目录：https://support.apple.com/en-us/HT201222
- iOS/iPadOS 26.6.1：https://support.apple.com/en-us/148282
- macOS Tahoe 26.6.2：https://support.apple.com/en-us/148281
- iOS/iPadOS 18.7.10：https://support.apple.com/en-us/148287

IoC：未见公开 IoC。

### 3. Microsoft Defender ShieldBreak CVE-2026-69414（补丁未出）

BleepingComputer（2026-08-17 05:05）称微软确认在跟踪 Microsoft Malware Protection Engine 提权问题，公开名 ShieldBreak，CVE-2026-69414，正在做安全更新。研究者 Nightmare Eclipse 在 8 月补丁星期二之后披露，据报为 RoguePlanet CVE-2026-50656 的绕过。Will Dormann 称 Defender 开启时仍可触发。MSRC 更新指南页为 JS 应用，正文未抓到。未见在野利用确认。

地址：
- 厂商：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414
- 文章：https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/

IoC：未见公开 IoC。

### 4. CISA KEV 状态（8/17）

目录从昨日 1665 / 2026.08.14 增至 1666 / 2026.08.17。本窗口仅新增 CVE-2025-62593。Windows CVE-2026-68820 联邦期限仍为 2026-08-25。

地址：
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

IoC：未见公开 IoC。


### 5. Forminator Forms CVE-2026-15748（X 补录，CVSS 9.8）

X 本日流传（@aviatrixtrc、@yousukezan、@AikidoCommJP）。WordPress 插件 Forminator Forms ≤1.56.1 未认证任意文件上传，可上传恶意 PHP 导致 RCE。The Hacker News 称需表单同时含 File Upload 与 Select 字段；1.56.2（2026-07-31）已修。活跃安装约 60 万。本晚报不转载上传步骤。

X：https://x.com/aviatrixtrc/status/2089501683415933018
X：https://x.com/yousukezan/status/2089501986509218091

地址：
- 文章：https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-15748

IoC：未见公开 IoC。

### 6. GitLab CE/EE CVE-2026-19478（X 补录，CVSS 9.4）+ CVE-2026-19650

X 本日流传（@TheHackersNews、@__kokumoto）。GitLab 8/17 紧急补丁：未认证用户在特定条件下可经 GraphQL directive 远程修改或删除公开项目与用户数据。影响自管 18.2 至 18.11.11 之前、19.0 至 19.0.8 之前、19.1 至 19.1.6 之前、19.2 至 19.2.4 之前。GitLab.com / Dedicated 已修。同包还有 GraphQL multiplex CSRF CVE-2026-19650（CVSS 7.1）。未见公开利用。

X：https://x.com/TheHackersNews/status/2089458993639063827
X：https://x.com/__kokumoto/status/2089493856433897731

地址：
- 厂商：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/
- 文章：https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-19478

IoC：未见公开 IoC。

### 7. macOS CVE-2026-65400 在野跟进（昨日已列）

荷兰 NCSC 确认在野利用；X 称约 4 万台 Mac 暴露，攻击后装 Monero 挖矿。非新洞，仅记跟进。

X：https://x.com/QubbleOfficial/status/2089457355809305018
X：https://x.com/Malwarebytes/status/2089453970297086021
X：https://x.com/securityLab_jp/status/2089502819258941724
文章：https://rocket-boys.co.jp/security-measures-lab/macos-screen-sharing-cve-2026-65400-cyberattack-monero/

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### nuclei-templates 版本核对

最新标签仍为 v10.4.7（2026-08-03），本窗口无新版本。
https://github.com/projectdiscovery/nuclei-templates/releases
https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.7

IoC：未见公开 IoC。

### 本窗口新建 GitHub（仅列 URL，未逐仓核实）

- https://github.com/s1d9e/meridian （2026-08-17T07:41:05Z 创建；描述为授权红队用模块化 C2：Python 服务端、Go implant、HTTP(S)/DNS）

昨日已列、本日不展开：https://github.com/dsanpang/fei 、https://github.com/MoMhaidat05/EdgeStealth-C2

IoC：未见公开 IoC。

## APT / Malware 分析

### 1. Rapid7 Operation ASTERIX（假钱包 + 语音钓鱼）

Rapid7 Labs（2026-08-17）在欺诈基础设施上发现开放目录：约 88.5 万电话号码、Crypto.com/Kraken 账号探测、Asterisk/3CX 语音、假 Trezor Suite / Ledger Live / Exodus Electron 应用，以及 macos-claude[.]com 上的假 Claude Code 安装页。三套 Trezor 构建共用同一 app.asar。助记词经 Telegram 外带，消息头为 TREZOR SECRET PHRASE。操作者用 Copilot/Claude 辅助开发，遇拒后改 Kimi 并提交越狱提示。Rapid7 已通报含 Apple 在内的厂商。本晚报不转载越狱提示或利用代码。完整 IoC 亦在 Rapid7 GitHub。

地址：
- 文章：https://www.rapid7.com/blog/post/tr-operation-asterix-crypto-fraud-vishing-phishing/
- GitHub：https://github.com/rapid7/Rapid7-Labs

地址／IoC（Rapid7 原文，防御复制）：
- SHA-256 app.asar：ba9d459169a303067a4fe36c8b8582a5ea023b9c270dafe89613bab840501b19
- SHA-256 Trezor Suite.exe（Windows）：961a398a5c71e837626b5fce68e44b14a5d220e3bd74a3d0ecd61a2762c38176
- SHA-256 macOS launcher arm64：7073b2a3a34525c5969921dd17ef1fa5607af92be78b3fc6129cdea73216691a
- SHA-256 macOS launcher x64：0f2c7194f1f577e73460db9ec2e75fc0c7f845588cbd4246333b7a4fbec90d9f
- SHA-256 kraken_checker：4bee9affff9fa718a2c94f02ebe6a75143d4d461d291c2df9b769920fc927bf8
- 声明完整性（macOS，不匹配）：918fa540126b7db6424652d84a5ce7e968947136db3d6e3e0cab30ea309e25a2
- IP：82.25.35.77 ；82.25.35.200 ；31.57.35.88
- Kraken checker C2：http://136.0.213.184:1337/api/kraken-numio
- 域名：macos-claude[.]com ；ledger[.]com[.]lv ；ledgerhelp[.]com ；36mcrypto[.]com ；xcjnrucne9xfvmci[.]com
- Telegram chat ID：8017226744
- LaunchAgent：com.trezormovement.agent ；io.trezor.agent ；com.ledger.live.agent.plist ；com.exodusmovement.agent.plist
- 路径：~/Library/Application Support/Trezor SuiteFake/ ；~/Library/Application Support/.SystemData/.framework/.apps/
- 邮件基础设施：smtpdm-ap-southeast-1[.]aliyun[.]com:465 ；ses-noreply[.]com
- 可能被滥用站点：https://atechservicecentre.co.uk/

### 2. TheHatman 叫卖约 364 万条 Azure/Entra 员工目录

BleepingComputer（2026-08-17 15:35）：别名 TheHatman 自 7/31 起叫卖，最近称用失窃凭证拿到麦当劳 170 万+ Azure 内部员工记录。其他声称：TCS 80 万+、Vodafone 42.5 万、HCL 25 万、IHG 18.5 万、Kyndryl 17 万、Gap 8 万+ 等。TCS 向 NSE 称未见当前泄露证据、数据像至少 4 年前；Gap 称初步看是有限、非敏感、数年前数据。Hudson Rock 称样本像真实目录属性。BC 未独立核实。昨日 Hudson Rock Azure 传闻的跟进，受害方未确认。

地址：
- 文章：https://www.bleepingcomputer.com/news/security/hacker-claims-36-million-azure-account-records-stolen-from-major-companies/

IoC：未见公开 IoC（仅别名 TheHatman）。

### 3. Pokémon Center 经 CEVA Logistics 客户数据暴露

BleepingComputer（2026-08-17 15:12）：Pokémon Center 通知英/德客户，负责 PokemonCenter.com 发货的 CEVA 自 2026-07-30 起遭入侵（亦有 7/29–8/1 影响多家欧洲零售商的说法）。可能泄露姓名、地址、电话、邮箱、订单内容。CEVA 不持有支付卡。部分订单已取消。同事件此前已通知 Valve/Steam 硬件客户。

地址：
- 文章：https://www.bleepingcomputer.com/news/security/pokemon-center-data-breach-exposes-customer-info-cancels-some-orders/

IoC：未见公开 IoC。

### 4. 法国税务总局 DGFiP：67.8 万人税务数据被取走

BleepingComputer（2026-08-17 06:09）引法国经济财政部：自 8/12 起调查确认，中断的接入点被用来查阅并导出 678000 名个人与专业人士数据（参考税收入、家庭商数、预扣率；企业名称与 SIREN；地籍地址与面积）。用户名密码与在线账户未失。已报 CNIL，ANSSI 协助。演员 ZeroBytes 8/12 在 PwnForums 挂卖，并声称 SPDC 地籍（自称 252149 条 / 200 万+ 人，抓取未完成）。

地址：
- 文章：https://www.bleepingcomputer.com/news/security/french-tax-authority-data-breach-affects-678-000-individuals/

IoC：演员 handle ZeroBytes；论坛 PwnForums。未见公开哈希／域名／IP。

## 地址／IoC 汇总

### URL
- https://x.com/aviatrixtrc/status/2089501683415933018
- https://x.com/yousukezan/status/2089501986509218091
- https://x.com/TheHackersNews/status/2089458993639063827
- https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/
- https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html
- https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html
- https://nvd.nist.gov/vuln/detail/CVE-2026-15748
- https://nvd.nist.gov/vuln/detail/CVE-2026-19478
- https://www.cisa.gov/news-events/alerts/2026/08/17/cisa-adds-one-known-exploited-vulnerability-catalog
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://github.com/ray-project/ray/security/advisories/GHSA-q279-jhrf-cc6v
- https://github.com/ray-project/ray/commit/70e7c72780bdec075dba6cad1afe0832772bfe09
- https://nvd.nist.gov/vuln/detail/CVE-2025-62593
- https://support.apple.com/en-us/HT201222
- https://support.apple.com/en-us/148282
- https://support.apple.com/en-us/148281
- https://support.apple.com/en-us/148287
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414
- https://www.bleepingcomputer.com/news/security/microsoft-working-on-defender-patch-for-shieldbreak-zero-day/
- https://www.rapid7.com/blog/post/tr-operation-asterix-crypto-fraud-vishing-phishing/
- https://github.com/rapid7/Rapid7-Labs
- https://www.bleepingcomputer.com/news/security/hacker-claims-36-million-azure-account-records-stolen-from-major-companies/
- https://www.bleepingcomputer.com/news/security/pokemon-center-data-breach-exposes-customer-info-cancels-some-orders/
- https://www.bleepingcomputer.com/news/security/french-tax-authority-data-breach-affects-678-000-individuals/
- https://github.com/s1d9e/meridian
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.7

### Operation ASTERIX（Rapid7）
- ba9d459169a303067a4fe36c8b8582a5ea023b9c270dafe89613bab840501b19
- 961a398a5c71e837626b5fce68e44b14a5d220e3bd74a3d0ecd61a2762c38176
- 7073b2a3a34525c5969921dd17ef1fa5607af92be78b3fc6129cdea73216691a
- 0f2c7194f1f577e73460db9ec2e75fc0c7f845588cbd4246333b7a4fbec90d9f
- 4bee9affff9fa718a2c94f02ebe6a75143d4d461d291c2df9b769920fc927bf8
- 82.25.35.77
- 82.25.35.200
- 31.57.35.88
- http://136.0.213.184:1337/api/kraken-numio
- macos-claude[.]com
- ledger[.]com[.]lv
- ledgerhelp[.]com
- 36mcrypto[.]com
- xcjnrucne9xfvmci[.]com
- Telegram chat 8017226744

## 来源搜索 URL

- https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&src=typed_query&f=live
- https://x.com/search?q=(APT%20OR%20malware)%20(analysis%20OR%20report)&src=typed_query&f=live
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://www.cisa.gov/news-events/alerts/2026/08/17/cisa-adds-one-known-exploited-vulnerability-catalog
- https://support.apple.com/en-us/HT201222
- https://github.com/projectdiscovery/nuclei-templates/releases
