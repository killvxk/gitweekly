# X 安全情报晚报 · 2026-09-13

> 搜集窗口：圣地亚哥时间 **2026-09-12 20:00 至 2026-09-13 ~20:45**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周日）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-13.json`（collected_at **2026-09-13T20:30:07-03:00**）＋ `/workspace/tools-news-pulse-2026-09-13.md`＋ `/workspace/enrich-2026-09-13/`。CISA KEV catalogVersion **2026.09.11**／**1709** 条／dateReleased **2026-09-11T19:32:16.8993Z**（相对昨日 **+0**；无新 KEV 入目；Sep12／13 CISA adds-* 告警探针 **404**）。
> **期限今日 09-13：MikroTik RouterOS CVE-2026-67277／CVE-2026-86060。** 昨日起逾期：Citrix NetScaler **CVE-2026-19490**、Fortinet **CVE-2025-25249**、Cisco FMC **CVE-2026-20079**。期限明日 09-14：ConnectWise ScreenConnect **CVE-2026-84869**、GitLab **CVE-2026-85706**、PaperCut **CVE-2026-81578／82078**。Sep2 五条联邦 BOD（Kestra／JFrog／Sangoma／SonicWall×2）自 **09-05** 起仍 **OVERDUE**。TrueConf **72530**／MLflow **64849**／JFrog **66384**／Magento **75650**／N-able **86218** 仍逾期。due_near：LiteLLM／Starlette（**09-16**）；Chromium **85046**（**09-18**）；微软两在野（**09-22**）；Chromium **87491**（**09-23**）；JFrog **42016／42018**（**09-25**）。
> X：`/workspace/x-posts-2026-09-13.json`（合并 **34** 条唯一：A9／B3／C15／LWiS7；**0** 重叠；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.28h**（远不足 24h）。Search B 约 **21h**。Search C 约 **4.3h**。LWiS List 扫描约 **44h**（作交叉，不假装为本窗口 Latest）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · 今日 due · MikroTik】** KEV due **今日 09-13**：**CVE-2026-67277／CVE-2026-86060**。厂商 Sep2026 公告＋CERT.pl 活跃利用说明；修方向含 **6.49.21／7.23.4／7.24.2／7.25 beta 3**（以厂商表为准）。
  厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
  CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67277 · https://nvd.nist.gov/vuln/detail/CVE-2026-86060

- **【逾期 · Cisco FMC 20079】** 昨 due 已过。Talos 续跟 UAT-12197／11823／11988（含 Qilin／Cyclops Blink 叙事）；THN Sep12 二次报道。
  Talos：https://blog.talosintelligence.com/fmc-ongoing-exploitation/
  IoC：https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.txt
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
  THN：https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html

- **【逾期 · Citrix／Fortinet】** **CVE-2026-19490**／**CVE-2025-25249** 自 09-12 due 起逾期。
  Citrix：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
  Fortinet：https://fortiguard.fortinet.com/psirt/FG-IR-25-084

- **【明日 due · GitLab／PaperCut／ScreenConnect】** **CVE-2026-85706**（CVSS 10 文件读）／PaperCut **81578／82078**（维护版 26.0.5／25.0.13／24.1.10，公告 last-updated 仍 Sep10）／ScreenConnect **84869**。
  GitLab 补丁：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
  PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
  GreyNoise：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
  THN GitLab：https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html
  THN PaperCut：https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html

- **【X · Sogou／GrayRabbit】** Latest 多条转载：UNC3569 利用搜狗输入法链（**CVE-2026-51990** 等叙述）部署 GrayRabbit；交叉 Gen Digital／THN／BC。
  Gen Digital：https://www.gendigital.com/blog/insights/research/one-click-backdoor-sogou
  THN：https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html
  BC（X 卡片）：https://www.bleepingcomputer.com/news/security/hackers-exploit-tencent-app-flaw-to-deploy-grayrabbit-malware/
  X：https://x.com/roaring_dog/status/2099276801898090724 · https://x.com/__kokumoto/status/2099276319171498335

- **【威胁报告 · Anthropic TI】** Search C 大量转载 Sep2026 TI（伊朗／胡塞／APT29／中国关联等二次叙事）；以官方页／PDF 为准。
  报告：https://www.anthropic.com/threat-intelligence-report-september-2026
  PDF：https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf
  Axios：https://www.axios.com/2026/09/12/anthropic-ai-threat-report-russia-iran-china
  X：https://x.com/thecurrentfeed/status/2099273167382389122

- **【LWiS · ArangoDB／防御检测】** List 见 Pruva 未认证路径至系统任务叙述（REPRO-2026-00355，防御向只记暴露面）；另有 Defender XDR 隔离、注册表取证、WSC 禁用 Defender 检测事件。
  Pruva：https://www.pruva.dev/reproductions/REPRO-2026-00355 · X https://x.com/pruvadev/status/2099230641485132169
  Defender XDR：https://jeffreyappel.nl/microsoft-defender-xdr-attack-disruption-automatic-device-isolation-explained/
  WSC 检测：https://ipurple.team/2026/09/09/windows-security-center/

- **【工具 · ipblocklist】** Search B 集中转载出入站 IP 封锁清单（每 2h 刷新，含出站 C2 叙事）。
  仓库：https://github.com/bitwire-it/ipblocklist
  X：https://x.com/hemran_7282/status/2099086520959508753

- **【新闻 · Risky／tl;dr／工具脉冲】** KEV **+0**；Risky 仍 **RBNEWS612**；tl;dr 仍 **#345**；Sliver **v1.7.7**／nuclei-templates **v10.4.8** 无升版；ICS Sep12–13 无新项（254–256 探针 404）。
  https://risky.biz/RBNEWS612/
  https://tldrsec.com/p/tldr-sec-345

## CVE / POC / 漏洞

### 1. 【今日 due】MikroTik RouterOS CVE-2026-67277／CVE-2026-86060

KEV due **2026-09-13**。厂商 September 2026 安全公告＋CERT.pl「活跃利用」说明。防御：升级至厂商列出的修复版本、限制管理面暴露、对照 CERT.pl IP 狩猎。

地址：
- 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67277 · https://nvd.nist.gov/vuln/detail/CVE-2026-86060
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- THN（KEV 复述）：https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html

IoC：IP `82.192.72.4` · `103.102.31.18`（CERT.pl）。

### 2. 【逾期 · 昨 due】Cisco FMC CVE-2026-20079（＋CVE-2026-20316 链式叙事）

认证绕过（CVSS **10.0**）。Talos：UAT-12197／UAT-11823（Sandworm 工具重叠／Cyclops Blink）／UAT-11988（Qilin）。热修防未来利用，**不清除既有沦陷**。Cloud-delivered FMC 不受影响（厂商叙述）。防御：打补丁、限制管理面、狩猎 `license.tmp`／web shell／Cyclops Blink。

地址：
- Talos：https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- IoC txt：https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.txt
- IoC raw：https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/09/ongoing-fmc-exploitation.txt
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-20079
- THN Sep12：https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html

IoC（Talos 公开表，原样）：
- 路径／文件：`/var/tmp/license.tmp`；`home.jsp`；`cmd.jar`
- SHA256：`B037f45e02a289325a1a5eb0d4db6a9fce9954fd0fdfd07162cb4eb2acbef77d`（home.jsp）；`Db491181ece3f319de6567ab6f6daa90c6879911cd890155e6b7d8cc7a1a8c8e`（cmd.jar）；`6f98add5d1a7729192b6ad8491d85c505c64836f7881742d6b93bd8e3d2fe461`（Cyclops Blink）
- IP：`89.34.96.56`；`208.123.119.215`；`104.218.165.253`；`91.214.78.118`；`43.204.2.142`

### 3. 【逾期 · 昨 due】Citrix NetScaler CVE-2026-19490

认证绕过（Gateway／AAA 等配置场景）。修复方向含 **14.1-73.32+**、**13.1-63.21+** 等（以厂商表为准）。

地址：
- 厂商：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-19490
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC（厂商页本轮未抽出独立指标表）。

### 4. 【逾期 · 昨 due】Fortinet CVE-2025-25249

FortiOS／FortiSwitchManager／FortiSASE 等堆溢出 → 未授权代码／命令执行叙事。厂商页可能被 Cloudflare 拦截，以 PSIRT／KEV／NVD 为准。

地址：
- 厂商：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2025-25249
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC（本轮公开页）。

### 5. 【明日 due · 09-14】GitLab CVE-2026-85706

commits API 路径穿越 → 未认证任意文件读（CVSS **10.0**）。修 **19.3.2／19.2.6／19.1.8**。媒体称披露后迅速出现探测。

地址：
- CISA 告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-one-known-exploited-vulnerability-catalog
- 补丁：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85706
- THN：https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html

IoC：未见公开利用 IoC（本轮以狩猎／补丁为主）。

### 6. 【明日 due · 09-14】PaperCut NG/MF CVE-2026-81578／CVE-2026-82078

公告 last-updated 仍 **September 10, 2026**；安全维护版 **26.0.5／25.0.13／24.1.10** 取代紧急补丁。GreyNoise「AI 编排」战役叙述仍相关。

地址：
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- GreyNoise：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
- THN：https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-81578 · https://nvd.nist.gov/vuln/detail/CVE-2026-82078

IoC：见 GreyNoise／厂商公告既有表（本轮无新抄）；无新则对照既报 IP／账户。

### 7. 【明日 due · 09-14】ConnectWise ScreenConnect CVE-2026-84869

KEV dateAdded **2026-09-11**，due **09-14**。

地址：
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- CISA 告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-84869
- THN：https://thehackernews.com/2026/09/cisa-adds-5-actively-exploited.html

IoC：未见本轮新公开 IoC。

### 8. 【X 交叉】Sogou Input Method／GrayRabbit · CVE-2026-51990（UNC3569）

X Latest 多条转载：搜狗输入法 Windows 链被中国关联 UNC3569 利用部署 GrayRabbit。Gen Digital 一键后门研究；THN 二次报道。防御：升级／移除受影响输入法组件、对照 Gen Digital 哈希狩猎、限制 `sgbiz:` URI 处理面。

地址：
- Gen Digital：https://www.gendigital.com/blog/insights/research/one-click-backdoor-sogou
- THN：https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html
- BC（X 展开）：https://www.bleepingcomputer.com/news/security/hackers-exploit-tencent-app-flaw-to-deploy-grayrabbit-malware/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-51990
- X：https://x.com/roaring_dog/status/2099276801898090724 · https://x.com/eng_digest_jp/status/2099276439463813595 · https://x.com/__kokumoto/status/2099276319171498335

IoC（THN 页可见 SHA256，原样）：
- `29c7ee41d0cc9e07d981e451df56d0c3d37c41ac4ec10c7b516cc033ee397a63`
- `749160a2f20f82744026719cf72e483595c6aad718efa74d675a98662e02422e`
- `d7a3c7eb94edc0e020f74c678743d71d61e944634aade4a67a96c3589e828b3a`

### 9. 【LWiS】ArangoDB 暴露面叙述（Pruva REPRO-2026-00355）

LWiS List：未认证 HTTP 路径／`_users`／回收 root 凭据／`isSystem:true` 任务 JSON 等链式叙述。**本报只记暴露面与狩猎方向，不转载利用步骤。**

地址：
- 文章：https://www.pruva.dev/reproductions/REPRO-2026-00355
- X：https://x.com/pruvadev/status/2099230641485132169

IoC：未见独立公开 IoC 表（以文章为准）。

## 工具与 GitHub 发布

### 1. bitwire-it／ipblocklist

聚合恶意 IP 清单，约每 2 小时刷新；叙述含入站扫描／爆破与出站 C2 阻断、主流 DNS 解析器自动排除。Search B 三条转载。

地址：
- 仓库：https://github.com/bitwire-it/ipblocklist
- X：https://x.com/hemran_7282/status/2099086520959508753 · https://x.com/NeoteoCom/status/2099000241517404496 · https://x.com/t1gerxt1ger/status/2098962721018642574

IoC：仓库即清单源；未见单独样本哈希。

### 2. Sliver／nuclei-templates 版本脉冲

本日无显著更新：Sliver 仍 **v1.7.7**；nuclei-templates 仍 **v10.4.8**。

地址：
- https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

### 3. 防御／取证写作成文（LWiS）

- Microsoft Defender XDR Attack Disruption 自动隔离：https://jeffreyappel.nl/microsoft-defender-xdr-attack-disruption-automatic-device-isolation-explained/ · X https://x.com/DirectoryRanger/status/2099241876423360846
- Windows 注册表取证叙事：https://sethenoka.com/registry-as-narrative/ · X https://x.com/DirectoryRanger/status/2099241729597620243
- 经 WSC API 禁用 Defender 的检测（事件 4657／4663／5007／15 等）：https://ipurple.team/2026/09/09/windows-security-center/ · X https://x.com/ipurple/status/2099238203928592791

IoC：未见公开恶意 IoC（检测向）。

## APT / Malware 分析

### 1. Cisco FMC 三簇（UAT-12197／11823／11988）

见 CVE 节逾期主条。Sandworm 工具重叠＋Cyclops Blink；Qilin 关联侦察／勒索部署叙事。

地址：
- https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.txt

IoC：见 CVE 节 Cisco 条。

### 2. UNC3569 · GrayRabbit（Sogou）

见 CVE 节 Sogou 条。

### 3. Anthropic Threat Intelligence · September 2026（续）

Search C 大量转载（伊朗海军目标叙事、胡塞武器软件、APT29、中国关联监控等二次报道）。以官方报告／PDF 为准；Axios／WSJ 为媒体交叉。

地址：
- https://www.anthropic.com/threat-intelligence-report-september-2026
- https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf
- Axios：https://www.axios.com/2026/09/12/anthropic-ai-threat-report-russia-iran-china
- WSJ（X 展开，本轮可能 DataDome）：https://www.wsj.com/politics/national-security/anthropic-says-iran-used-its-american-ai-model-to-target-u-s-navy-warships-67583e05
- X：https://x.com/thecurrentfeed/status/2099273167382389122 · https://x.com/HilareMoniz/status/2099265323367035021 · https://x.com/24log/status/2099248152578797965 · https://x.com/SweetHomeUSA1/status/2099237510933328068

IoC：未见本轮从报告页新抄公开 IoC（以官方 PDF／附录为准）。

### 4. PaperCut AI 编排战役（GreyNoise）

见 CVE／PaperCut 节。

### 5. 暗网／勒索／泄露声称（未独立核验）

- 伊拉克 PMF 数据集声称：https://x.com/DailyDarkWeb/status/2099278589283692896
- 印度金融／支付库集合叫卖声称：https://x.com/intels_daily/status/2099258605740417047
- Claro 多米尼加客户数据声称：https://x.com/intels_daily/status/2099221861917659464 · https://x.com/VECERTRadar/status/2099221666052100239
- Revolut 数据事件升级／勒索叙事：https://thecybersecguru.com/news/revolut-data-breach-2026/ · X https://x.com/thecybersecguru/status/2099213636413923714
- 印尼新首都 Nusantara 58GB 文档声称：https://x.com/intels_daily/status/2099213318976152032
- LAPSUS$ Chapter II 挑战 FBI 叙事（UnderCode；页可能 Cloudflare）：https://undercodetesting.com/lapsus-chapter-ii-threat-actor-returns-with-pgp-signed-challenge-to-fbi-countdown-to-first-victim-leak-video/ · X https://x.com/UndercodeUpdate/status/2099232805838311767

IoC：未见可核验公开 IoC（声称级）。

### 6. 其他 LWiS 讨论帖（低优先级）

- XNU／macOS LPE 面闲聊：https://x.com/h0mbre_/status/2099252106276348042
- Flare-On 12 全自动解题叙述（无附件链接）：https://x.com/expend20/status/2099190156846678471

## 地址／IoC 汇总

- **今日 due · MikroTik**：IP `82.192.72.4` · `103.102.31.18`（CERT.pl）。
- **逾期 · Cisco FMC**：路径 `/var/tmp/license.tmp`；`home.jsp`／`cmd.jar`；SHA256 `B037f45e02a289325a1a5eb0d4db6a9fce9954fd0fdfd07162cb4eb2acbef77d` · `Db491181ece3f319de6567ab6f6daa90c6879911cd890155e6b7d8cc7a1a8c8e` · `6f98add5d1a7729192b6ad8491d85c505c64836f7881742d6b93bd8e3d2fe461`；IP `89.34.96.56` · `208.123.119.215` · `104.218.165.253` · `91.214.78.118` · `43.204.2.142`。
- **逾期 · Citrix／Fortinet**：未见公开 IoC。
- **Sogou／GrayRabbit**：SHA256 `29c7ee41d0cc9e07d981e451df56d0c3d37c41ac4ec10c7b516cc033ee397a63` · `749160a2f20f82744026719cf72e483595c6aad718efa74d675a98662e02422e` · `d7a3c7eb94edc0e020f74c678743d71d61e944634aade4a67a96c3589e828b3a`。
- **明日 due · GitLab／ScreenConnect／PaperCut**：本轮以补丁／狩猎为主；PaperCut 对照既报 GreyNoise 表。
- **工具 ipblocklist**：https://github.com/bitwire-it/ipblocklist（清单源）。
- **KEV 逾期提醒**：Kestra 49869／JFrog 82329／Sangoma 9586／SonicWall 83548+83549；TrueConf 72530／MLflow 64849／JFrog 66384；Magento 75650／N-able 86218；外加昨 due 三洞。
- **声称级泄露**：未见可核验公开 IoC。


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

- X Latest A（CVE/POC）：https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- X Latest B（GitHub 工具／C2）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20mythic%20OR%20havoc)&src=typed_query&f=live
- X Latest C（malware／threat）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS612：https://risky.biz/RBNEWS612/
- tl;dr sec：https://tldrsec.com/
- tl;dr #345：https://tldrsec.com/p/tldr-sec-345
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 09-11 三洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-three-known-exploited-vulnerabilities-catalog
- CISA 09-11 一洞告警：https://www.cisa.gov/news-events/alerts/2026/09/11/cisa-adds-one-known-exploited-vulnerability-catalog
- Talos FMC：https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- Talos IoC：https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.txt
- Cisco FMC 顾问：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- Citrix CTX696939：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- Fortinet FG-IR-25-084：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl MikroTik：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- GitLab 补丁：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- GreyNoise PaperCut：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf
- Gen Digital Sogou：https://www.gendigital.com/blog/insights/research/one-click-backdoor-sogou
- Anthropic TI：https://www.anthropic.com/threat-intelligence-report-september-2026
- ipblocklist：https://github.com/bitwire-it/ipblocklist
- Pruva ArangoDB：https://www.pruva.dev/reproductions/REPRO-2026-00355
