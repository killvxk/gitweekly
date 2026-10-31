# X 安全情报晚报 · 2026-10-30

覆盖窗口：2026-10-29 20:00 至 2026-10-30 约 20:15（America/Santiago），约 24 小时。X 只读读取 7 次（Latest/相关度检索 4 次、LWiS 成员时间线 1 次、原帖详情 1 次批量），0 次限流；t.co 均已展开。公开备援：CISA KEV 2026.10.30（共 1766 条，较上次报告 +4）。IoC 一律 defang（`[.]`、`hxxp`）。

## 今日摘要

- **Ivanti Connect Secure 再进 KEV 两条**：CVE-2026-111357（due 11-02）、CVE-2026-118527（due 11-13），可与本月 0day CVE-2026-104935 串成链。
- **GitLab CVE-2026-97229（CVSS 10）在野**：10-29 进 KEV，due 11-01；Alpine Linux 的 GitLab 遭攻击未遂；自带 Ruby 的部署还要把 Ruby 升到 3.3.13/3.4.12/4.0.9+。
- **Cisco ASA/FTD CVE-2026-76418**：SSL VPN 未认证 DoS，在野，due 11-01。
- **Oracle EBS CVE-2026-101767（CVSS 9.8）**：比利时 CCB 告警，已见试探性利用。
- **PHP2Shell（109618/109619）**：在野确认，但需针对目标调优，未出现 Log4Shell 式大规模扫射；Fragnesia（46300）KEV 明天 10-31 到期。
- **VAPOR PANDA / ARTEX**：CrowdStrike 报告中国关联组织用 AI 代理框架 11 天打 14 国 200+ 机构，投放 BLOODALCHEMY。
- **木马化 Claude Code 2.1.313 扩展**植入持久 SSH 后门（报称最多 5000 台开发机）；Arid Gopher 新活动；Redis/Portainer → Nezha 后门；NetamLoader；Talos NIK C2。
- 背景：Binance 约 63 亿美元被盗，归因朝鲜 TraderTraitor，约 30 亿美元冻结（仅 X 报道，未见官方完整技术报告）。

## CVE / POC / 漏洞

### 1. Ivanti Connect Secure CVE-2026-111357 / CVE-2026-118527（今日进 KEV）
111357 为缺失认证可本地提权，118527 为可预测标识符导致已认证攻击者向已知路径写文件；两者均可与 CVE-2026-104935 串联。处置：按 Ivanti 公告升级，并按 CISA 取证分诊要求排查入侵痕迹。
- X 原帖：https://x.com/EvergreenCS117/status/2116264526761054648
- X 原帖（104935 链）：https://x.com/Daily_CyberSec/status/2116001749773267344
- CISA KEV 公告：https://www.cisa.gov/news-events/alerts/2026/10/30/cisa-adds-two-known-exploited-vulnerabilities-catalog
- 厂商公告：https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935?language=en_US
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-111357 ／ https://nvd.nist.gov/vuln/detail/CVE-2026-118527
- 文章：https://securityonline.info/ivanti-connect-secure-vulnerability-exploited/
- 地址／IoC：未见公开 IoC

### 2. GitLab CE/EE CVE-2026-97229（CVSS 10，KEV 10-29，due 11-01）
CI/CD 正则编译器整数溢出导致以 git 用户执行代码；受影响 19.2<19.2.8、19.3<19.3.5、19.4<19.4.2。研究者指出需能向公开项目分支推送恶意 `.gitlab-ci.yml`。Alpine Linux 报告攻击未遂。底层是 Ruby/Onigmo，自建 Ruby 需同步升级。
- X 原帖：https://x.com/YourDailyCVE/status/2116231763349684542
- X 原帖：https://x.com/V0iD_0daY/status/2116170280116903994
- X 原帖：https://x.com/FORTBRIDGE/status/2116103965444092189
- X 原帖：https://x.com/CCBalert/status/2116235392059875433
- 厂商公告：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/
- 厂商公告（Ruby）：https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-97229
- 文章：https://www.securityweek.com/max-severity-gitlab-vulnerability-exploited-against-alpine-linux/
- 文章：https://4tify.io/article/cisa-flags-actively-exploited-gitlab-rce-and-cisco-firewall-dos-bugs
- 地址／IoC：未见公开 IoC

### 3. Cisco Secure Firewall ASA/FTD CVE-2026-76418（KEV 10-29，due 11-01）
SSL VPN 未认证远程 DoS，设备崩溃重启，已在野利用。
- X 原帖：https://x.com/fugedizs/status/2116108195512930608
- X 原帖（引用 BleepingComputer）：https://x.com/bleepincomputer/status/2115763221231489241
- X 原帖：https://x.com/isectech_/status/2116264700384006225
- 厂商公告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tunnel-dos-s6mgkb75
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76418
- 地址／IoC：未见公开 IoC

### 4. Oracle E-Business Suite CVE-2026-101767（CVSS 9.8，未进 KEV）
Application Object Library 未认证 SQL 注入，可接管 EBS 并串 RCE；Defused 蜜罐见到试探性利用。
- X 原帖：https://x.com/CCBalert/status/2116120961648922649
- 告警（比利时 CCB）：https://ccb.belgium.be/advisories/warning-unauthenticated-remote-code-execution-oracle-e-business-suite-patch-immediately
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-101767
- 地址／IoC：未见公开 IoC

### 5. PHP2Shell CVE-2026-109618 / 109619 后续
DFIR Radar 汇总：在野确认（蜜罐 35 次 shell 执行；与 Fragnesia 46300 串联据称拿下 25 台 PAN-OS 防火墙／管理服务器），但利用需针对 PHP 版本、SAPI、内存布局调优，暂未大规模化。Exploit-DB 出现相关条目的说法待核实。修补到 PHP 8.5.12 等修复版本。
- X 原帖：https://x.com/DFIR_Radar/status/2116003426517848249
- X 原帖：https://x.com/PHPSiteAudit/status/2116093743052775580
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-109618 ／ https://nvd.nist.gov/vuln/detail/CVE-2026-109619 ／ https://nvd.nist.gov/vuln/detail/CVE-2026-46300
- 地址／IoC：未见公开 IoC

### 6. 其他
- Synology DSM CVE-2024-10441（9.8）被用于投放勒索：https://x.com/CCBalert/status/2116209866960240959 ；NVD：https://nvd.nist.gov/vuln/detail/CVE-2024-10441
- Linux 内核 MPTCP RCE CVE-2026-98432（由 Claude 发现，SANS Stormcast 提及）：https://x.com/sans_isc/status/2116009959230234650 ；https://isc.sans.edu/podcastdetail/10158 ；NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-98432
- FreeSWITCH CVE-2026-116779 「在野」说法仅见低信誉账号，待核实：https://x.com/YourAnon_irc/status/2116009503577518540
- 地址／IoC：未见公开 IoC

## 工具与 GitHub 发布

### 1. Cloudflare security-audit-skill
Cloudflare 开源其漏洞挖掘框架的种子 skill：6 阶段审计，另起代理反证每个候选后才报告，输出 schema 校验 JSON。
- X 原帖：https://x.com/bighouse0310/status/2116076542132703495
- X 原帖：https://x.com/Hatimpatwa312/status/2116245595803521340
- GitHub：https://github.com/cloudflare/security-audit-skill

### 2. CAU（Go 恶意软件检测引擎，MIT）
每个检测器附 FP/FN 实测数，需评测通过才发布。
- X 原帖：https://x.com/thecybersecorg/status/2116058879247478897
- GitHub：https://github.com/s-b-repo/cau

### 3. invaris-agentsec
在注入了恶意指令的仓库上测试 AI 代理行为。
- X 原帖：https://x.com/arunimastwt/status/2116072797827170552
- GitHub：https://github.com/invarislabs/invaris-agentsec

### 4. LWiS 成员观察
- Burp Suite 配置 SOCKS 代理并开 DNS 转发时，其 portswigger.net / oastify.net 遥测也会经代理流入目标环境（红队 OPSEC 注意）：https://x.com/Octoberfest73/status/2116225890560462896
- rad9800 提醒停用 VS Code 扩展自动更新（关联扩展投毒事件）：https://x.com/rad9800/status/2116022643354952123 ；引用：https://x.com/adnanthekhan/status/2116010483702706337

地址／IoC：未见公开 IoC

## APT / Malware 分析

### 1. VAPOR PANDA 使用 ARTEX AI 代理框架（CrowdStrike）
10-17 起单一 ARTEX 控制器 11 天内对 14+ 国 200+ 机构（外交部、美国 19 家药企／半导体／国防／核／金融、美比菲电信）发起入侵，OverWatch 确认 9 家后渗透；投放 BLOODALCHEMY，使用 Chisel、SoftEther、密码喷洒，关联 GhostEmperor/Storm-0940。
- X 原帖：https://x.com/DFIR_Radar/status/2115942124956831965
- X 原帖：https://x.com/rst_cloud/status/2116306194117669024
- X 原帖：https://x.com/alphahunt_io/status/2116241412727378282
- 报告：https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/
- 地址／IoC：报告含 3 域名、3 IP、3 哈希，X 帖未原文列出，请到报告取。

### 2. 木马化 Claude Code 2.1.313 扩展植入持久 SSH 后门
据称由 Cursor 披露，最多约 5000 台开发机受影响。
- X 原帖：https://x.com/threatcluster/status/2116154309750428106
- 文章：https://threatcluster.io/cluster/malicious-claude-code-extension-distributes-persistent-ssh-b-97aef86b
- 地址／IoC：SHA256 `432ccdee3801f99e52b8fe31f69ea9870118e96ea7ef9ecabed1479621b5ab62`（另 3 个见上链接）

### 3. Arid Gopher（Arid Viper）两起新活动（Nextron，基于 ESET APT 报告）
针对中东阿拉伯语政府、HR、外交、学生、NGO；活动一：宏文档→WMI 拉 HTA→从 PNG 解出 Go 后门，Run 键 HostHelpLoader；活动二：VHDX 内 4MB libcurl 植入物绕过 MotW。
- X 原帖：https://x.com/nextronresearch/status/2116155238570680509
- 地址／IoC：C&C `mmarketplaces[.]com`；持久化 Run 值 `HostHelpLoader`

### 4. 中国关联攻击者扫 Redis / Portainer Agent 投放 Nezha 后门
Redis 模块 system.exec，每分钟 cron 持久化＋容器逃逸，劫持其他 Nezha agent，窃取云密钥并回传 Telegram。
- X 原帖：https://x.com/etugenio/status/2116072405508472926
- 平台：https://app.etugen.io/trashpile/144.91.103.172
- 地址／IoC：`144[.]91.103.172`、`51[.]83.71.4`、`uau[.]pp[.]ua`

### 5. Cisco Talos：NIK C2（Go，带 OpenAI API 辅助与锁屏勒索模块）
- X 原帖：https://x.com/Python_s_/status/2115953797382263153
- 地址／IoC：`87.120.196[.]120`、`total-sitevv[.]lol`（Talos 原文链接 X 帖未给出）

### 6. NetamLoader 攻击亚洲政府定制版 Win10（Kaspersky Securelist）
- X 原帖：https://x.com/rst_cloud/status/2116177441714487443
- 报告：https://securelist.com/netamloader/121676/
- 地址／IoC：报告含 11 哈希、1 IP、1 域名、3 URL，X 帖未原文列出。

### 7. KeyDrift：Cisco Catalyst SD-WAN（CVE-2026-20127）上窃取 AES-256 密钥，与 Volt Typhoon 基础设施重叠
- X 原帖：https://x.com/DFIR_Radar/status/2115972836686700779
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-20127
- 地址／IoC：未见公开 IoC（X 帖截断）

### 8. UltraViewer DNS 关联出 QuickBooks 钓鱼（350+ 仿冒域名，njRAT / DarkKometa）
- X 原帖：https://x.com/DFIR_Radar/status/2115987860004471227
- 地址／IoC：追踪域 `track.chanret[.]com`（示例 `hxxp://track.chanret[.]com/images/4x406rtk5/...`）；诈骗电话 +1 (805) 835-8090、+1 (805) 699-1139

### 9. 其他
- Binance 约 63 亿美元被盗，疑朝鲜 TraderTraitor：https://x.com/MrWhale/status/2116020561587708143 ；https://x.com/vxunderground/status/2115976907585950201 （钱包地址 X 帖未列出：未见公开 IoC）
- The Gentlemen 勒索团伙声称攻击法国 INED：https://x.com/DailyDarkWeb/status/2116141622245433415
- Hugging Face 31 个恶意账号挖矿（Pluto Security）：https://x.com/sans_isc/status/2116009959230234650

## 地址／IoC 汇总（defang）

| 来源 | 类型 | 值 |
|---|---|---|
| Claude Code 扩展后门 | SHA256 | 432ccdee3801f99e52b8fe31f69ea9870118e96ea7ef9ecabed1479621b5ab62 |
| Arid Gopher | C&C 域名 | mmarketplaces[.]com |
| Redis/Nezha | IP | 144[.]91.103.172 |
| Redis/Nezha | IP | 51[.]83.71.4 |
| Redis/Nezha | 域名 | uau[.]pp[.]ua |
| NIK C2 | IP | 87.120.196[.]120 |
| NIK C2 | 域名 | total-sitevv[.]lol |
| QuickBooks 钓鱼 | 追踪域 | track.chanret[.]com |
| QuickBooks 钓鱼 | 电话 | +1 (805) 835-8090 ／ +1 (805) 699-1139 |

KEV 到期提醒：Fragnesia CVE-2026-46300 due 10-31；GitLab 97229、Cisco 76418 due 11-01；Ivanti 111357 due 11-02；96652/96655/110936 due 11-03；48356/111497 due 11-10；VMware 41709 due 11-11；Ivanti 118527 due 11-13。

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

- X Latest（CVE/POC）：https://x.com/search?q=CVE%20OR%20PoC%20OR%20exploit%20OR%200day&f=live
- X Latest（GitHub 工具）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei)&f=live
- X Latest（威胁报告）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/ ；tl;dr sec：https://tldrsec.com/

说明：本次 X 采集走 Grok Bot 公共 X 只读接口（与浏览器 Latest 等价的检索），LWiS List 以成员备份中 55 个 handle 的时间线检索代替；无发帖／点赞／追踪等任何写操作。
