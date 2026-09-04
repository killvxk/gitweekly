# X 安全情报晚报 · 2026-08-30

> 搜集窗口：圣地亚哥时间 **2026-08-29 20:00 至 2026-08-30 20:15**（America/Santiago / UTC-4）。**本报为官方 20:00 cron 晚报（周日）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-08-30.json`（collected_at **2026-08-30T20:10:00-04:00**）。CISA KEV catalogVersion **仍为 2026.08.27**／**1685** 条／dateReleased **2026-08-27T17:00:36.6632Z**。**2026-08-29／08-30 dateAdded：无新 CVE**；无 08-29／08-30 新 CISA Alert；无新 ICSA。**期限今日**是 ownCloud **CVE-2023-49105** 与 Linux Kernel **CVE-2026-53362**。PaperCut **CVE-2026-82078／81578 仍未入 KEV**，厂商页 Last updated **August 30, 2026**（AEST 10:34 官方版开发中＋jTDS FAQ；**15:35 追加 IoC**）。
> X：文件 `/workspace/x-posts-2026-08-30.json`（**11** 条，cve 8／tool 2／apt 1；collected_at **2026-08-30T20:35:00-04:00**；**logged_in=true**／账号 **@seogoogle4**）。搜索1 Latest 最旧可见约 **2026-08-30T22:30:54Z**（约 **1.6 小时**，高流量，**不可当作完整 24h**）。搜索2 量少可覆盖 24h+（最旧可见至 **2026-08-22T23:58:30Z**）。搜索3 最旧可见约 **2026-08-30T23:20:07Z**（约 **47 分钟**），随后反复出现 “Something went wrong. Try reloading.”（软限流，非登录墙／非 CAPTCHA）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉引用，且 A／C 窗口偏短；**本报起固定列入 LWiS 信源**（X List 500 ＋ blogs.txt 443 ＋ Risky Business ＋ tl;dr sec），与 X Latest 交叉、不替代。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造 CVE、URL、哈希、日期、推文或 IoC。无 URL 不写叙事。
> 说明：防御向晚报。只记谁／打什么／补丁与狩猎。不转载利用代码、payload、请求样例或 PoC。

## 今日摘要

- **期限今日 · ownCloud CVE-2023-49105 ＋ Linux Kernel CVE-2026-53362（KEV due 2026-08-30）**：dateAdded 均为 **2026-08-27**；ransomwareCampaignUse **Unknown**。ownCloud：已知用户名且目标未配置 signing-key 时可未认证访问／修改／删除文件；补丁语境仍是 WebDAV 预签名 URL 绕过（厂商 ≥10.13.1，后催 ≥10.13.3）。Kernel：IPv6 网络子系统提权，可影响 SUSE／Red Hat 及其他发行版。JFrog Artifactory **CVE-2026-66384** due **09-10**。Citrix **CVE-2026-8452** 与 SQL **CVE-2019-1068** 联邦期限已于 **昨日 08-29** 到期。本轮 KEV 无增量。IoC：未见公开 IoC。
  CISA：https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
  厂商：https://owncloud.com/security-advisories/webdav-api-authentication-bypass-using-pre-signed-urls/
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2023-49105 https://nvd.nist.gov/vuln/detail/CVE-2026-53362

- **紧急延续 · PaperCut NG／MF CVE-2026-82078／CVE-2026-81578（尚未入 KEV）**：Emergency Patch **Release 2** 仍须安装。厂商页 **Last updated August 30, 2026**。本窗口 **AEST 新增**：10:34 官方版仍在开发＋遗留 Sourceforge jTDS 持卡查找改用 Microsoft SQL JDBC；**15:35 追加狩猎 IoC**（`jdbc:derby:memory:pwn`、`CAST(X'cafebabe`、5 字符 `.class`／`.cmd`／`.out`、SimpleHelp「Remote Access Service」、AnyDesk、`sendit[.]sh`）。NVD Last Modified **2026-08-29**（NIST CVSS 仍仅厂商 v4.0）。受影响至 **24.1.10／25.0.13／26.0.5** 之前。公网 Application Server 仍须立刻把 Web 管理面限制到受信 IP。**不转写利用细节。** IoC：见地址／IoC 汇总。
  厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-82078 https://nvd.nist.gov/vuln/detail/CVE-2026-81578
  文章：https://www.huntress.com/blog/papercut-actively-exploited https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/
  X：https://x.com/securityLab_jp/status/2094198730652348729

- **本窗口新闻 · FulcrumSec 声称曼彻斯特机场集团 MAG 窃走约 86 GB（BC 2026-08-30）**：MAG 已于 08-27 披露停车／贵宾室／Fast Track／机场 Wi-Fi 数据被盗。FulcrumSec 向 BC 提供样本；BC 核验过一条旅客记录。声称 Iterable API 凭据暴露在客户端 JS；另称近 20 万条 2026 年余下行程记录。MAG 拒评具体数字，称已联系受影响旅客。此前曼城晚报引述约 **870 万** 客户（绝大多数仅邮箱）。IoC：未见公开 C2／样本哈希。
  文章：https://www.bleepingcomputer.com/news/security/fulcrumsec-claims-manchester-airports-hack-theft-of-86-gb-of-data/
  相关（08-27 披露）：https://www.bleepingcomputer.com/news/security/manchester-airports-group-says-hackers-stole-travelers-data/

- **本窗口新闻 · Chrome／Edge「Superior」扩展钱包盗号（Socket 08-27；BC 08-30 放大）**：18 个 Chrome＋1 个 Edge，WebSocket C2＋拆 CSP＋远程模块。最大面是收购后的 Enable Right Click & Copy（Chrome 约 7 万＋Edge 约 1 万）。Chrome 店面已下架，Edge 在 Socket 发文时仍在投毒（08-14 换 C2）。**不转写模块实现。** IoC：扩展 ID＋C2 域名见汇总。
  文章：https://socket.dev/blog/chrome-edge-extension-wallet-drainer https://www.bleepingcomputer.com/news/security/chrome-web-store-extensions-caught-stealing-crypto-browser-data/

- **本窗口交叉 · TerminalFix（微软 08-28；THN／转载 08-30）**：ClickFix 变种，假 Cloudflare CAPTCHA 诱使把 PowerShell 粘进 Windows Terminal。DLL 侧载 `LockScreenContentServer.exe`＋`dui70.dll`，PNG 隐写二阶段，Python 反向隧道到 `gitnow[.]dev:443`。**不转写粘贴命令。** IoC：微软官方表见汇总。
  厂商：https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/
  文章：https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html

- **X 旧 KEV 回放（非今日新加）**：IBM Langflow **CVE-2026-9198**（dateAdded **2026-08-04**／due **08-07**，补丁 **1.10.1**）；Broadcom VMware vCenter **CVE-2026-59310**（dateAdded **2026-08-18**／due **08-21**，路径遍历 CVSS 9.8）。X 今日把 Langflow 说成「CISA 刚加入」——**与本轮 KEV JSON 不符**，属旧条目回放。vCenter 在野活动来自 QUIRSO（约 361 IP／47 国，个别环境 Babuk 派生 ESXi 勒索）。IoC：Langflow 未见公开 IoC；vCenter 本轮 X 帖未见 IoC。
  厂商：https://www.ibm.com/support/pages/node/7278927 https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-9198 https://nvd.nist.gov/vuln/detail/CVE-2026-59310
  X：https://x.com/nik_kale/status/2094213580925403643 https://x.com/iss_kk_official/status/2094207905214136823

- **本窗口交叉 · hashcat CVE-2026-68766（NVD 发布 2026-08-22；尚未入 KEV）**：restore 文件参数注入导致任意文件写入。VulnCheck CVSS 3.1 **7.8**／4.0 **8.5**。影响至 **7.1.2**。修复提交 `fcae69f`（2026-08-17）。X 今日转载。**不转写利用步骤。** IoC：未见公开 IoC。
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-68766
  仓库：https://github.com/hashcat/hashcat/issues/4738 https://github.com/hashcat/hashcat/commit/fcae69f2438ff8eae0dc8e206b78067a1e465ed4
  X：https://x.com/DFIR_Lab/status/2094214972330951026

- **本窗口交叉 · JFrog Artifactory CVE-2026-82329（NVD 发布 2026-08-28，Awaiting Analysis；尚未入 KEV）**：JFrog CNA 给出 CVSS 3.1 **9.8**，默认配置下未认证网络访问或可拿到管理权限。这与已在 KEV 的路径穿越 **CVE-2026-66384**（due 09-10）**不是同一条**。X 作者自称未核验；公开备援以 NVD／JFrog 公告索引为准。IoC：未见公开 IoC。
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-82329
  厂商索引：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
  X：https://x.com/connect24h/status/2094195851833090529

- **工具**：Sliver **仍为 v1.7.6**；nuclei-templates **仍为 v10.4.8**。X 提及 **HT Forge** 模块化红队平台（帖子时间略早于本窗口起点约 14 分钟，昨日晚报未收录）。Objective-See 为昨日已见交叉，本报不重复展开。IoC：未见公开 IoC。
  仓库：https://github.com/BishopFox/sliver/releases/tag/v1.7.6 https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8 https://github.com/HackingTeamOficial/-HT-Forge

- **勒索／声称（X 窗口，公开备援未独立核验）**：Qilin → **AFSARD**（Finance · MK）。FulcrumSec／MAG 见上。ATF／Qilin「重大事件」为 08-27 延续，本报不升格为今日新披露。IoC：未见公开 IoC。
  X：https://x.com/sec_news_com/status/2094215423759958404
  文章（ATF 延续）：https://www.bleepingcomputer.com/news/security/atf-confirms-major-incident-after-recent-qilin-breach-claims/

- **ICS／Alert**：无 08-29／08-30 新 ICSA、无新 CISA Alert。KEV 目录本身未更新。

## CVE / POC / 漏洞

### 1. 【KEV 期限今日】ownCloud CVE-2023-49105（dateAdded 2026-08-27；联邦期限 2026-08-30）

不当认证。CISA 短描述：若已知受害者用户名且其未配置 signing-key，攻击者可未认证访问、修改或删除任意文件。已知在野（KEV）。厂商公告为 WebDAV API 预签名 URL 认证绕过；补丁 ≥10.13.1（后续催更 ≥10.13.3）。ransomwareCampaignUse **Unknown**。**不转写利用细节。**

狩猎：立刻核对本机 ownCloud 版本与公网 WebDAV／预签名 URL 暴露面；按 BOD 26-04 做补丁前取证分诊。

地址：
- CISA 08-27 三连加警报：https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- KEV 字段页：https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2023-49105
- 厂商 ownCloud：https://owncloud.com/security-advisories/webdav-api-authentication-bypass-using-pre-signed-urls/
- 厂商安全索引：https://owncloud.org/security
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2023-49105
- BOD 26-04：https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-on-risk

IoC：未见公开 IoC。

### 2. 【KEV 期限今日】Linux Kernel CVE-2026-53362（dateAdded 2026-08-27；联邦期限 2026-08-30）

CISA 短描述：未具名漏洞，可经 IPv6 网络子系统提权；可影响 SUSE、Red Hat 及其他使用该内核的产品。已知在野（KEV）。ransomwareCampaignUse **Unknown**。修复提交见 git.kernel.org stable 链接（KEV notes）。按发行版安全公告升级内核。

地址：
- CISA 08-27 警报：https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-53362
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- Kernel stable 提交（KEV notes）：https://git.kernel.org/stable/c/14200d435af9a9eeb444f529fc2f689a236b7962
- 另：https://git.kernel.org/stable/c/65fb14cbebb0cd0eff903a22d33537ddc8b95769
- 另：https://git.kernel.org/stable/c/46f201f8b4c39633a1fa3dc12459f506d470993d
- 另：https://git.kernel.org/stable/c/6374fb9edf72c67a118a2c214a0dddd04c921e0a
- 另：https://git.kernel.org/stable/c/e9eacf19281ea2498b36291b56c9606118c2d74e
- 另：https://git.kernel.org/stable/c/736b380e28d0480c7bc3e022f1950f31fe53a7c5

IoC：未见公开 IoC。

### 3. 【紧急／在野／尚未入 KEV】PaperCut NG／MF CVE-2026-82078＋CVE-2026-81578 · 厂商页更新 2026-08-30

相对昨日晚报：KEV **仍未收录**；NVD Last Modified 仍 **2026-08-29T04:18:08.953**（NIST 仅厂商 CVSS v4.0）。厂商页 Last updated 从 August 29 改为 **August 30, 2026**。AEST 新增两条 changelog：10:34 官方版开发中＋jTDS FAQ；**15:35 追加 IoC**。Release 2 要求不变。**本报不转写根因、请求样例或利用步骤。**

| CVE | 名称 | CWE | 分数 | NVD |
|---|---|---|---|---|
| CVE-2026-82078 | Unsafe Dynamic Class Loading in Database Connector | CWE-470 | 厂商 CVSS 4.0 **9.4** | Last Modified 2026-08-29 |
| CVE-2026-81578 | Authentication Bypass | CWE-306 | 厂商 CVSS 4.0 **8.8** | Last Modified 2026-08-29（昨日晚报） |

受影响（NVD／PaperCut semver）：MF／NG 在 **24.1.10、25.0.13、26.0.5** 之前。Release 2 覆盖 v24／v25／v26（Win／Linux／macOS）。v23 及更早：升级到最新。公网 Application Server：**立刻**限制 Web 管理面到受信 IP。Site Server／二级打印服务器也要打同一补丁。

狩猎信号与 Release 2 SHA256：**见地址／IoC 汇总**。厂商强调：缺失这些 IoC ≠ 未中招。

地址：
- 厂商紧急公告：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- NVD CVE-2026-82078：https://nvd.nist.gov/vuln/detail/CVE-2026-82078
- NVD CVE-2026-81578：https://nvd.nist.gov/vuln/detail/CVE-2026-81578
- Huntress：https://www.huntress.com/blog/papercut-actively-exploited
- Rapid7：https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/
- BC（Release 2）：https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/
- THN（链利用）：https://thehackernews.com/2026/08/attackers-chain-two-papercut-flaws-to.html
- X：https://x.com/securityLab_jp/status/2094198730652348729
- 日文转载：https://rocket-boys.co.jp/security-measures-lab/papercut-zero-day-cve-2026-82078-8157/

IoC：厂商狩猎字符串＋30 Aug 追加路径／SimpleHelp／AnyDesk／defanged 下载 URL＋全部 Release 2 SHA256 见「地址／IoC 汇总」。未见独立公开的攻击者 C2 IP 清单（`sendit[.]sh` 为厂商观察的下载主机）。

### 4. 【昨日到期／续报】Citrix NetScaler CVE-2026-8452 ＋ Microsoft SQL Server CVE-2019-1068（due 2026-08-29）

联邦期限已过。Citrix 补丁构建仍是 **14.1-72.61+**／**13.1-63.18+**／**14.1-72.61 FIPS+**／**13.1-37.272 FIPS/NDcPP+**。前置：Gateway（VPN／ICA／CVPN／RDP Proxy）或 AAA vserver。SQL Server 按 MSRC 打补丁。本轮 KEV 无增量。

地址：
- 厂商 CTX696604：https://support.citrix.com/external/article/CTX696604/netscaler-adc-and-netscaler-gateway-secu.html
- MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2019-1068
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-8452 https://nvd.nist.gov/vuln/detail/CVE-2019-1068
- CISA 08-26 六连加：https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog

IoC：CTX696604 本轮未见 C2／IP／域名。公开报道曾提 `/var/vpn/theme/x.php`、`/var/vpn/theme/z.php` 作为狩猎线索（非本轮新 IoC）。

### 5. 【X 回放／旧 KEV】IBM Langflow CVE-2026-9198（dateAdded 2026-08-04；due 2026-08-07）

未认证代码注入 → 默认部署 RCE。CISA 短描述与 X 一致。补丁 **1.10.1**。**不是今日新入 KEV**——X 帖「CISA added」为旧条目回放。另有同日入 KEV 的 Apache Tomcat **CVE-2026-34486**（dateAdded 同样 08-04）。

地址：
- 厂商 IBM：https://www.ibm.com/support/pages/node/7278927
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-9198
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 文章（THN 旧文，X 卡片）：https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html
- X：https://x.com/nik_kale/status/2094213580925403643

IoC：未见公开 IoC。

### 6. 【X 回放／旧 KEV】Broadcom VMware vCenter CVE-2026-59310（dateAdded 2026-08-18；due 2026-08-21）

路径遍历，CISA 短描述：有网络访问即可任意代码执行。CVSS 公开报道 **9.8**。厂商公告 VMSA-2026-0006（KEV notes 链到 Broadcom 38017）。QUIRSO 描述全球在野（约 361 个唯一 IP／47 国），个别环境把 Babuk 派生勒索打到 ESXi（`.babyk`）。**X 今日是续报，不是新加 KEV。不转写 Syslog 利用细节。**

地址：
- 厂商 Broadcom：https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-59310
- CISA KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- 文章：https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw
- X：https://x.com/iss_kk_official/status/2094207905214136823

IoC：本轮 X 帖未见 C2／IP／哈希。不以二手转述补造 QUIRSO IoC。

### 7. 【X 转载／NVD 已有／尚未入 KEV】hashcat CVE-2026-68766（NVD 发布 2026-08-22；Last Modified 2026-08-24）

restore 文件未限制命令行选项，可注入 `--outfile`／`--potfile-path` 一类输出路径，造成任意文件写入。VulnCheck CVSS 3.1 **7.8**、4.0 **8.5**。影响至 **7.1.2**。修复：提交 `fcae69f2438ff8eae0dc8e206b78067a1e465ed4`（2026-08-17，停止从 restore 解析 argv）。**不转写利用包构造。**

地址：
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-68766
- GitHub issue：https://github.com/hashcat/hashcat/issues/4738
- 修复提交：https://github.com/hashcat/hashcat/commit/fcae69f2438ff8eae0dc8e206b78067a1e465ed4
- VulnCheck：https://www.vulncheck.com/advisories/hashcat-through-arbitrary-file-write-via-restore-file-option-injection
- X：https://x.com/DFIR_Lab/status/2094214972330951026

IoC：未见公开 IoC。

### 8. 【X 交叉／NVD 已有／尚未入 KEV】JFrog Artifactory CVE-2026-82329（NVD 发布／修改 2026-08-28；Awaiting Analysis）

JFrog CNA（reefs@jfrog.com）CVSS 3.1 **9.8**。NVD 英文：默认配置下认证弱点，未认证且有网络访问的攻击者或可获得管理权限。**尚未入 KEV。** 勿与 KEV 路径穿越 **CVE-2026-66384**（due 2026-09-10）混淆。按 JFrog 安全公告索引核对本机 Artifactory 版本。

地址：
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-82329
- 厂商公告索引：https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- 厂商发行说明：https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases
- NVD（已在 KEV 的另一条）：https://nvd.nist.gov/vuln/detail/CVE-2026-66384
- X：https://x.com/connect24h/status/2094195851833090529

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 1. Sliver v1.7.6（延续；本窗口无更新）

仍为 **2026-08-28T18:37:03Z** 的 v1.7.6。nuclei-templates 仍 **v10.4.8**（2026-08-24T13:01:50Z）。

地址：
- https://github.com/BishopFox/sliver/releases/tag/v1.7.6
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

IoC：未见公开 IoC。

### 2. HT Forge（X 交叉；模块化进攻平台）

@HackingTeam77 指向 GitHub 仓库，自称面向 pentest／红队／bug bounty 的模块化平台。帖子时间 **2026-08-29T23:46:16Z**（圣地亚哥 08-29 19:46，略早于本窗口 20:00 起点，昨日晚报未收）。本报只记 URL，不评能力、不转写用法。

地址：
- 仓库：https://github.com/HackingTeamOficial/-HT-Forge
- X：https://x.com/HackingTeam77/status/2093847733798899804

IoC：未见公开 IoC。

### 3. 本日无其他显著红队工具版本 bump

Objective-See 仓库交叉已见昨日晚报，不重复。InfraGuard／tailcat／CyberStrike 亦为昨日已见。

## APT / Malware 分析

### 1. 【新】FulcrumSec 声称 MAG（曼彻斯特／Stansted／East Midlands）约 86 GB

BC **2026-08-30 11:00**。MAG 08-27 已确认停车、贵宾室、Fast Track 与机场 Wi-Fi 注册数据被盗。FulcrumSec 提供样本；BC 用一条真实旅客记录核对过 Fast Track 购买史。声称客户端 JS 暴露 Iterable API 凭据，并声称近 20 万条 2026 年余下行程。MAG 拒评这些具体主张，称已联系受影响旅客。曼城晚报此前引述约 870 万客户。**未见支付卡。** 运营未中断。

地址：
- 文章：https://www.bleepingcomputer.com/news/security/fulcrumsec-claims-manchester-airports-hack-theft-of-86-gb-of-data/
- MAG 08-27 披露：https://www.bleepingcomputer.com/news/security/manchester-airports-group-says-hackers-stole-travelers-data/

IoC：未见公开 C2／样本哈希／钱包。

### 2. 【新／放大】Chrome＋Edge「Superior」扩展框架（Socket 08-27；BC 08-30）

19 个扩展（14 自建＋5 收购），先发干净版本再建信任，再推恶意更新。C2 WebSocket、拆 CSP、隐藏 DOM 触发模块。模块含多链钱包 drainer、假 Ledger／Trezor 助记词页、交易所会话收割、ClickFix 假更新。最大面 Enable Right Click & Copy（`pkoccklolohdacbfooifnpebakpbeipc`）。Chrome 已下架；Socket 发文时 Edge 仍在投毒并已换 C2（08-14）。建议卸载列表中扩展、轮换凭据；持币者换新钱包。

地址：
- Socket：https://socket.dev/blog/chrome-edge-extension-wallet-drainer
- BC：https://www.bleepingcomputer.com/news/security/chrome-web-store-extensions-caught-stealing-crypto-browser-data/

IoC：扩展 ID 与 C2／投放域名见汇总（抄自 Socket「Indicators of Compromise」节）。

### 3. 【交叉】TerminalFix 假 Cloudflare CAPTCHA → 反向隧道（微软 08-28；THN 08-30）

ClickFix 变种，目标是 Windows Terminal／PowerShell 而不是 Win+R。侧载 `LockScreenContentServer.exe`＋恶意 `dui70.dll`，PNG 隐写二阶段，注册表 Run＋每 60 分钟计划任务（名 `LockScreenContentServer_MuODG5yBM`），Python `client.py` 经 WebSocket 连 `gitnow[.]dev:443`。目录 `C:\ProgramData\f47f2a8c21c9df4e`。**不转写剪贴板命令。**

地址：
- 微软：https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/
- THN：https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html

IoC：微软官方文件哈希＋域名见汇总。

### 4. 【X 声称／未独立核验】Qilin → AFSARD（Finance · MK）

@sec_news_com 监控帖，无文章卡。公开备援未找到对应厂商／执法确认。当声称、不升格。

地址：
- X：https://x.com/sec_news_com/status/2094215423759958404

IoC：未见公开 IoC。

### 5. 本日无显著更新（ICS／新 APT 报告）

无 08-29／08-30 新 ICSA。APT28 HOOKEDGE、柏林拒付、ATF／Qilin 均为 08-27／08-28 延续。

## 地址／IoC 汇总

### PaperCut（厂商页，含 30 Aug 15:35 AEST 追加；防御狩猎）

日志字符串：
- `ERROR No suitable driver found for jdbc:no:x`
- `ERROR DatabaseUtils - Database error looking up cardID: VALUES CAST`
- `DB URL: jdbc:derby:memory:pwn;create=true`
- `Database error looking up cardID: VALUES CAST(X'cafebabe`
- `Database error looking up cardID: VALUES CAST('`
- `DB URL: jdbc:no:x DB Driver: <5-char random name>`

落盘路径模式：
- `<install>\server\lib\<5-char-name>.class`
- `<install>\server\data\content\<5-char-name>.cmd`
- `<install>\server\data\content\<5-char-name>.out`

进程／服务：
- `pc-app.exe`／`pc-app` 拉起 `cmd.exe`（厂商观察）
- Windows 服务名 `Remote Access Service`，路径 `C:\ProgramData\JWrapper-Remote Access\JWAppsSharedConfig\restricted\SimpleService.exe`（SimpleHelp）
- `C:\ProgramData\ace.exe`；`C:\ProgramData\AnyDesk.exe`

厂商观察下载（已 defang，勿直接访问）：
- `hxxps://sendit[.]sh/Gg7Rp/ace[.]exe`
- `hxxps://download[.]anydesk[.]com/AnyDesk.exe`

**Emergency Patch Release 2 SHA-256（厂商表）**

PaperCut MF：
- v26 Win `5c63ef18c523c85d5e73efc7fbb2bd2edacf0b03bcf80fe4d7e4c1a7c8bcbcf4`／Linux `6117b53dd0610052c53aeafced91cd3d0ad80ed1dcc578e873291a8b697b802a`／macOS `7dea84473f8d00d4608b7e797b633f130139e23bf5bba02848a1df0a7e2cc7c6`
- v25 Win `b296de7da020152a83291378ab4ca5c461d76510648347fd6e69f3fb2cd5e9c9`／Linux `296498ef5ec1ac8927dc1ccae9a9aa3c04036da6d2768813e6df818049b3f4a1`／macOS `3e5509f0514228031967934d32e4a40512bd6fb5857bfde3002866bc3ede3f9a`
- v24 Win `75aba456d6629848c89513371c44037f2bdddbc1e39bdadc16d1fed8b59766eb`／Linux `7ac8f002fb602d1f54665d8a18a25fc57cf41239ae0c03b18591ee220b57d419`／macOS `40581392cc11a1f46b90ab5c2607fdacade77aca0de6629c1d78a2a71548fc9c`

PaperCut NG：
- v26 Win `c9a2b356910b5fef3c114d48cb7c508414d1d35ddac74c530d1e8923d357e7d4`／Linux `3261356ced056fd5ab0962a07178701e80c6ebbce30d7158d20ed3c57b1dcf59`／macOS `bdd54d5cb9f20924b059986a44f849df499f7de7cb5cd0a60290d2b2610850e7`
- v25 Win `b155cf19cdab1b7fc92c2dd030d1c0cd439397d83d7749042f65e2364ca03589`／Linux `282be7404a25c12317a2079eed59e8794f0c9d7bd257dee60c39b529da18a46a`／macOS `276ee64a7bb4d4e242fe7ddaecf3cd279eee91e83fbd1e6f44050db2f90bda6d`
- v24 Win `f58a3fe4e9d7543c38a3f01e53f4a9ad34884289a71df25f734af9d977c06319`／Linux `a7ea1e2cdb22a4349ae854491b10b89a52d075e9106ec68f838f12d5f2a15f51`／macOS `1e70dd6510d0b9618035a3db462b78ece06cd70f41bcccca8196c015c46a480b`

### TerminalFix（微软 08-28 官方表）

域名：
- `gitnow[.]dev`（反向隧道 C2，443／WebSocket）
- `bestsocialmedianewspapper[.]com`（PNG 隐写投放）
- `offlineupdater[.]com`（投放 failover）
- `hxxps://linked-log[.]com/`（被黑站点样例）

文件：
- 目录 `C:\ProgramData\f47f2a8c21c9df4e`
- `LockScreenContentServer.exe`（合法签名宿主）＋恶意 `dui70.dll`
- ZIP SHA-256 `18c2090e8a0ae0568af9b87e59eaf8270f23d2909600ed9db91a9444fd8b278f`
- `client.py` SHA-256 `b8d107800403b9197e5b7609ceacd8e4cac1b0f9a1d156e6dacd6c3f7794b36a`
- `dui70.dll` 多样本哈希见微软文（`ba77feed86bcda49308746421bdc684a432dd5d68c363975b2a3c6831bda3f07` 等）

### Socket Superior 扩展（官方 IoC 节）

扩展 ID（收购）：
- `pkoccklolohdacbfooifnpebakpbeipc` Enable Right Click & Copy — Smart Unlock + OCR
- `fegckejpfnlmfgkfjpinlbgmeeijjkel` RapidLens
- `kdenlnncndfnhkognokgfpabgkgehodd` QuickLens
- `jamminefolhgepgihbmcjjhgldbfcikp` Password Protect PDF
- `inmkjedjdhgpknjogbjomhnbgdccckkg` Allow Copy（Edge）

威胁方自建（Socket 表）：
- `fcgdejjichpgfaaafflplhfijcnieopb` PixelCheck
- `cfpnjdbpojpcongfaefcamjbaolpelcd` Creative Library - Ad Spy Tool
- `aapdalkmclfaahehnmicbglkohkldhne` Website Traffic Checker: MirrorSphere SEO Stats
- `dkdadldmiefjldmegbjbnhhfddnkhlhm` Site Signal
- `fjmlhlkccegopebcllcmafahkmeejpph` SEO Pulse Pro
- `iekoapohahgmogbagegmcgplbkikcgke` Private Crypto News Reader
- `ahpnnnjbnfbhoikhohglpohnoocjcoco` Blockfolio: Address Monitor
- `oeacadlaclegkkkdehjmiifnjhcekclj` Crypto Rates & Fiat Converter
- `jmlgannjlbliikgcaieomgmcnfplglea` Crypto Alerter
- `lhmcajhgadanidbopgaoobjlldegjmke` DeFi Pulse Tracker
- `gfackggoapepdmnjnkblogdcjpgcjiak` Crypto Price Badge
- `hfijkbdkpidafdbeebnnkhfccildbcle` Multi-Chain Explorer
- `pcngchfbfgejllcbhmeadjhiebebiome` LedgerLook: Wallet Checker
- `aodkjdeghbjiaienipfjkbpcikkacbcp` FeedX-Ray

主 C2／投放域名（Socket，已 defang）：
- `active-enable-right-click[.]top`
- `api[.]enable-right-click[.]click`
- `enable-right-click[.]click`
- `payload[.]siteinsight[.]bond`
- `api[.]extensionanalyticspro[.]top`
- `password-protect-pdf[.]com`
- `ws[.]site-signal[.]top`
- `cookie-whitelist[.]top`
- `whale-alert[.]art`
- `ggle-analytics[.]com`
- `extension[.]io-safe[.]icu`
- 其余见 Socket 文 Network Indicators 节

### Citrix 狩猎线索（非本轮新）

- `/var/vpn/theme/x.php`
- `/var/vpn/theme/z.php`

### 其他条目

其余 CVE／工具／勒索声称：**未见公开 IoC**（无 C2、下载 URL、IP、域名、钱包、样本哈希）。

### 全部 URL（便于复制）

- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/alerts/2026/08/26/cisa-adds-six-known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/cybersecurity-advisories
- https://www.cisa.gov/news-events/ics-advisories
- https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-on-risk
- https://owncloud.com/security-advisories/webdav-api-authentication-bypass-using-pre-signed-urls/
- https://owncloud.org/security
- https://nvd.nist.gov/vuln/detail/CVE-2023-49105
- https://nvd.nist.gov/vuln/detail/CVE-2026-53362
- https://git.kernel.org/stable/c/14200d435af9a9eeb444f529fc2f689a236b7962
- https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- https://nvd.nist.gov/vuln/detail/CVE-2026-82078
- https://nvd.nist.gov/vuln/detail/CVE-2026-81578
- https://www.huntress.com/blog/papercut-actively-exploited
- https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/
- https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/
- https://thehackernews.com/2026/08/attackers-chain-two-papercut-flaws-to.html
- https://support.citrix.com/external/article/CTX696604/netscaler-adc-and-netscaler-gateway-secu.html
- https://nvd.nist.gov/vuln/detail/CVE-2026-8452
- https://nvd.nist.gov/vuln/detail/CVE-2019-1068
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2019-1068
- https://nvd.nist.gov/vuln/detail/CVE-2026-66384
- https://nvd.nist.gov/vuln/detail/CVE-2026-82329
- https://docs.jfrog.com/releases/docs/jfrog-security-advisories
- https://www.ibm.com/support/pages/node/7278927
- https://nvd.nist.gov/vuln/detail/CVE-2026-9198
- https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html
- https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017
- https://nvd.nist.gov/vuln/detail/CVE-2026-59310
- https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw
- https://nvd.nist.gov/vuln/detail/CVE-2026-68766
- https://github.com/hashcat/hashcat/issues/4738
- https://github.com/hashcat/hashcat/commit/fcae69f2438ff8eae0dc8e206b78067a1e465ed4
- https://www.vulncheck.com/advisories/hashcat-through-arbitrary-file-write-via-restore-file-option-injection
- https://www.bleepingcomputer.com/news/security/fulcrumsec-claims-manchester-airports-hack-theft-of-86-gb-of-data/
- https://www.bleepingcomputer.com/news/security/manchester-airports-group-says-hackers-stole-travelers-data/
- https://socket.dev/blog/chrome-edge-extension-wallet-drainer
- https://www.bleepingcomputer.com/news/security/chrome-web-store-extensions-caught-stealing-crypto-browser-data/
- https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/
- https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html
- https://github.com/BishopFox/sliver/releases/tag/v1.7.6
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8
- https://github.com/HackingTeamOficial/-HT-Forge
- https://x.com/securityLab_jp/status/2094198730652348729
- https://x.com/nik_kale/status/2094213580925403643
- https://x.com/iss_kk_official/status/2094207905214136823
- https://x.com/DFIR_Lab/status/2094214972330951026
- https://x.com/connect24h/status/2094195851833090529
- https://x.com/HackingTeam77/status/2093847733798899804
- https://x.com/sec_news_com/status/2094215423759958404

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

## 来源搜索 URL

- https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- https://www.cisa.gov/news-events/alerts/2026/08/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
- https://www.cisa.gov/news-events/cybersecurity-advisories
- https://www.cisa.gov/news-events/ics-advisories
- https://nvd.nist.gov/vuln/detail/CVE-2023-49105
- https://nvd.nist.gov/vuln/detail/CVE-2026-82078
- https://socket.dev/blog/chrome-edge-extension-wallet-drainer
- https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/
- https://github.com/BishopFox/sliver/releases/tag/v1.7.6
- https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day%20OR%20%220-day%22&src=typed_query&f=live
- https://x.com/search?q=(github.com)%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20havoc%20OR%20cobalt)&src=typed_query&f=live
- https://x.com/search?q=(APT%20OR%20%22malware%20analysis%22%20OR%20ransomware%20OR%20%22threat%20report%22%20OR%20KEV)&src=typed_query&f=live
- https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- https://x.com/i/lists/1239330068461244424
- https://x.com/i/lists/1239330068461244424/members
- https://blog.badsectorlabs.com/files/blogs.txt
- https://risky.biz/
- https://tldrsec.com/
- https://subscribe.badsectorlabs.com/subscription/form
