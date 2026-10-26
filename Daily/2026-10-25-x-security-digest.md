# X 安全情报晚报 · 2026-10-25

> 搜集窗口：圣地亚哥时间 **2026-10-24 20:08 至 2026-10-25 20:16**（America/Santiago／UTC-3，接昨晚窗口）。X 搜索参数：`start_time=2026-10-24T23:08:00Z`，不设 end_time。实际抓到的帖子从 **10-24 20:14** 到 **10-25 20:16**（UTC-3），**实际有效覆盖约 24 小时**。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all` 用 recency 和 relevancy 两种排序；`get_lists_posts` 读 LWiS List；`get_posts_by_ids` 读重点原帖全文）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** t.co 短链按接口返回的 `expanded_url`／`unwound_url` 展开；纯图片／视频链接不列。
> 本轮查询：
> - A 类（CVE／0day／PoC／exploit）：Latest 四次、`CVE-2026` relevancy 一次、actively exploited／zero-day 一次、厂商公告专查一次
> - B 类（GitHub＋C2／red team／nuclei／BOF／PoC）：一次
> - C 类（malware analysis／threat report／threat actor、APT／campaign、IoC／C2 server）：两次
> - LWiS List（1239330068461244424）：两页共 184 条
> - 原帖全文读取：一次（20 个 ID）
>
> 合计 **13 次有效 X 读取，0 次 429**。原始返回 421 条，窗口内去重 **370** 条（与 seen_ids 7710 条**零重叠**），关键词粗筛 **179** 条安全相关新帖（排除纯转推），下文引用约 75 条。剔除了广告／营销、体育、加密货币刷屏、投票刷 tag 帖（如 #CVE #PHP 的投票广告）。**全程只读，没有发帖、回复、点赞、转推、收藏或关注。**
> **公开备援**（`/workspace/x1025/pages/`，curl 核对）：CISA KEV JSON；加拿大网络安全中心 AV26-1037；Electrum GHSA；0x1c1101 仓库 README；THN（Tailworm、Popcorn Time、OpenAI 代理逃逸）；StepSecurity（GlassWorm）；Yeeth Security（VS Code 扩展 RAT）；Solar 4RAYS（RFRx003）；orlofv/Indicators。SecurityWeek 对本机返回 Cloudflare 拦截页，以 X 原帖为准。本轮**未**用 GitHub API 核对 nuclei／Sliver 等正式 release。
> **CISA KEV：catalogVersion 2026.10.23／1756 条，Δ0**（与昨晚相同）。`dateReleased` 为 2026-10-23 16:30 UTC-3，周末未更新。
> - **明天 10-26（周一）到期**：Arista VeloCloud Orchestrator **CVE-2026-114625**（SQLi）、Collabora Online CODE **CVE-2026-110447**（OS 命令注入）。
> - **11-03 到期**：Plex 96652、Plex 96655、Siemens 110936。
> - **逾期（续）**：
>   - 10-23 到期：SiteGuard 106931、Plex 96656、Plex 96654
>   - 10-19 到期：BeyondTrust 102764、Fortinet CVE-2025-61624
>   - 10-18 到期：Atlassian 21589
>   - 10-17 到期：AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322
>   - 10-16 到期：Ivanti 104935、Windows 96951
>   - 10-13 到期：Apple 86950
>   - 10-11 到期：CVE-2015-5477、CVE-2016-3081、CVE-2023-22894、CVE-2021-3199、CVE-2015-3306
> - **X 上的说法与 KEV JSON 不符**：@threatpodium 再次称「7 new KEVs」（https://x.com/threatpodium/status/2114490586631745893），KEV JSON 今日 Δ0，应是按周统计或口径不同。
> - **仍未进 KEV、但今日高优先**：FortiSIEM 106173（加拿大网络安全中心已标在野利用）、Citrix NetScaler 88771／88772、PHP2Shell 109618／109619、Brotli 111497、Electrum <4.8.3（已有实际资金损失）。

## 今日摘要

- **PHP2Shell 的「打补丁也没用」说法是假的**：@MarcosBL 转发的「影响所有 PHP 版本、含已修补版本」新 PoC（https://github.com/0x1c1101/CVE-2026-109618-PoC），仓库 README 原文自称 **「And of course it's fake. Duh.」**，不是真实利用。已打 8.5.12／8.4.27／8.3.36／8.2.35 的不用因此恐慌。
- **stealmybitcoin.com 挑战闹剧收尾**：LiveOverflow 指出初版只是 nginx→`php -S` 送静态 index.html，根本触发不了漏洞；改版后 @killa 解出，现场 PHP 8.4.26 可稳定利用。结论是「不可利用」的说法站不住，未修补的仍需当作 RCE 处理。
- **DPRK 疑似扫描 PHP2Shell**：CYFIRMA 称 21 个受控节点扫描 216 台主机；Okta Access Gateway 受 PHP2Shell 影响（CVE-2026-115546／115547）；SecurityWeek 称 Mirai 运营者加入、VulnCheck 已绕过 ASLR。
- **FortiSIEM CVE-2026-106173**：加拿大网络安全中心 AV26-1037 更新 1 写明「公开报道显示在野利用」，Fortinet 公告仍写未见利用；Horizon3 已公开 PoC。升级到 7.5.1+，或先封 tcp/27918。
- **Citrix NetScaler 88771／88772（CVSS 9.5）**：补丁前已被利用数周，Unit 42 统计 50,277 个暴露实例；打补丁清不掉已落地的 webshell，要做入侵排查。修复版本 14.1-73.46。
- **Electrum <4.8.3**：恶意 Electrum 服务器可把刚广播的交易替换成指向攻击者地址的伪交易、诱导用户 RBF，已有用户丢币，升级 4.8.3。
- **Tailworm**：Tailscale 1.104.2／headscale 0.29.5 共 11 个未修问题，已失陷的一台设备可借 Tailscale SSH 拿到 root；无 CVE、无修复版本，Tailscale 已回应正在修。
- **新恶意软件／供应链**：VS Code 市场 8 个看板类扩展共用同一 RAT 引擎（每 5 秒轮询 C2 执行命令）；Solar 4RAYS 披露经 CommuniGate Pro 投放的新后门 RFRx003；GlassWorm 借 OVHcloud CLI 发布替换；274 页 Hermes 窃密木马／RAT 报告。
- **其他**：Adobe Commerce 71362 ATO 利用公开；Popcorn Time 旧更新器 CVE-2026-30612（研究者推送 200 万次停用更新）；Azure 两个 CVSS 10（83938／110063，微软已缓解）；NGINX 三个数据面内存漏洞；NSD 4 个栈溢出；Drupal 108097。

## CVE / POC / 漏洞

### 1. PHP2Shell（CVE-2026-109618／109619）：假 PoC、CTF 争议、DPRK 扫描、下游产品
- **假 PoC 澄清**：@MarcosBL 称新 PoC「影响所有 PHP 版本，即便刚打过补丁」，@heapsoverflow 称用它「打穿了」stealmybitcoin.com 并放出「部分 PoC」。核对仓库 README：自称部分 PoC、不能稳定执行代码，结尾写明「And of course it's fake. Duh. … No harm intended, purely for fun」。**判定为恶作剧，不改变补丁结论。**
- **stealmybitcoin.com 挑战**：LiveOverflow 分析初版为 nginx→PHP cli-server 送静态 index.html，无法触达漏洞的 multipart 解析器；@S1r1u5_ 证实并批评「不可利用」叙事；之后站点换成真实 PHP 端点，@killa 解出（服务器钱包地址配置错），LiveOverflow 称对 PHP 8.4.26＋nginx→`php -S` 已有稳定利用。
- **DPRK 疑似扫描**：CYFIRMA 报告 21 个节点对 216 台主机做 PHP2Shell 探测。
- **Okta Access Gateway**：管理控制台受 PHP2Shell 影响，对应 CVE-2026-115546／115547（日本 Security Lab 报道）。日本主机商 Lolipop 已为全部 PHP 分支打补丁。
- **Mirai 与 ASLR 绕过**：SecurityWeek 称 Mirai 运营者加入 PHP2Shell 攻击、VulnCheck 演示 ASLR 绕过，同时写明尚未确认成功入侵（本机访问被 Cloudflare 拦，以 X 原帖摘要为准）。
- **狩猎**：@DFIR_Radar 建议查带 `PHP_SESSION_UPLOAD_PROGRESS` 的异常 POST，最早的尝试见于 10-17；@M0DWare 发布分层 Sigma 规则（暴露面、利用尝试、崩溃、起 shell、无 shell 的后续）；@OliverSild 称多家厂商报告的武器化攻击 IoC 一致。
- **署名争议**：@acd421 称自己先公开发现、PHP 安全团队把署名给转报者，并提到 CVE-2026-115560 仍为 Reserved。
- **补丁**：8.5.12／8.4.27／8.3.36／8.2.35。
- 地址：
  - X 原帖：https://x.com/MarcosBL/status/2114449406539989325
  - X 原帖：https://x.com/heapsoverflow/status/2114426379093848376
  - X 原帖：https://x.com/LiveOverflow/status/2114308386292461842
  - X 原帖：https://x.com/LiveOverflow/status/2114412072805208237
  - X 原帖：https://x.com/LiveOverflow/status/2114488571021398330
  - X 原帖：https://x.com/LiveOverflow/status/2114489115840262405
  - X 原帖：https://x.com/S1r1u5_/status/2114469408605438415
  - X 原帖：https://x.com/__kokumoto/status/2114492164063563857
  - X 原帖：https://x.com/securityLab_jp/status/2114492492716601596
  - X 原帖：https://x.com/securityLab_jp/status/2114494474240119214
  - X 原帖：https://x.com/SecurityWeek/status/2114202288826855490
  - X 原帖：https://x.com/DFIR_Radar/status/2114206549316927750
  - X 原帖：https://x.com/M0DWare/status/2114205314543165879
  - X 原帖：https://x.com/OliverSild/status/2114311473623429351
  - X 原帖：https://x.com/acd421/status/2114215495532470630
  - X 原帖（周报）：https://x.com/tpsecuritymdr/status/2114465432614621244
  - GitHub（自称 fake，勿当真）：https://github.com/0x1c1101/CVE-2026-109618-PoC
  - GitHub（署名争议方）：https://github.com/ACD421/PHP
  - 厂商公告：https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w
  - 文章：https://www.cyfirma.com/research/cyfirma-threat-advisory-suspected-dprk-campaign-staging-php2shell-targeting-against-global-php-infrastructure/
  - 文章：https://rocket-boys.co.jp/security-measures-lab/okta_access_gateway_php2shell_admin_console_20261024/
  - 文章：https://www.securityweek.com/mirai-botnet-operators-join-php2shell-attacks-as-aslr-bypass-exploits-emerge/
  - 文章：https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
  - 文章：https://www.wiz.io/blog/php2shell-php-rce
  - 文章（Sigma）：https://mohammad-alattas.github.io/posts/From-php2shell-to-Detection-Obfuscated-PHP-Web-Shells-with-Sigma/
  - 文章（IoC 汇总）：https://vulnocalypse.com/e/php2shell
- 地址／IoC：stealmybitcoin[.]com（公开 CTF 靶站，非恶意基础设施）；其余未见公开 IoC。

### 2. FortiSIEM CVE-2026-106173（未授权 RCE，gRPC QueryResultReq／路径穿越）
- 加拿大网络安全中心 AV26-1037 于 10-23 更新：「Open-source reporting indicates that CVE-2026-106173 is being exploited in the wild」；Fortinet 自家公告仍写未见利用。Horizon3 已公开 PoC。
- 补丁：FortiSIEM 7.5.1 及以上；临时封 tcp/27918。
- 地址：
  - X 原帖：https://x.com/catcowbug/status/2114266320900354543
  - X 原帖：https://x.com/Dinosn/status/2114259969755193774
  - X 原帖：https://x.com/TheThreatWire/status/2114311938054443099
  - GitHub／PoC：https://github.com/horizon3ai/CVE-2026-106173
  - 厂商／政府公告：https://www.cyber.gc.ca/en/alerts-advisories/fortinet-security-advisory-av26-1037
- 地址／IoC：未见公开 IoC。

### 3. Citrix NetScaler CVE-2026-88771／88772（CVSS 9.5，补丁前已被利用数周）
- Unit 42 统计 50,277 个暴露实例。88771 无需认证：伪造的崩溃日志行会被 root 维护脚本在最长 24 小时后执行，所以写入和执行之间没有可直接关联的成对事件。补丁不能清除已有 webshell，需排查。修复版本 14.1-73.46。
- 地址：
  - X 原帖：https://x.com/infrasecserv/status/2114337287823622568
  - X 原帖：https://x.com/ThreatAft/status/2114259557644218397
- 地址／IoC：未见公开 IoC（两帖都没附链接，Unit 42 原文待查）。

### 4. Electrum <4.8.3：恶意服务器替换交易，已有用户丢币
- 轻客户端信任服务器提供的未确认交易；恶意服务器吞掉刚广播的 tx1，换成签名无效、输出改成攻击者地址的 tx2，再诱导用户 RBF 加速。修复：4.8.3。
- 地址：
  - X 原帖：https://x.com/SuperRareDude/status/2114152188733993365
  - X 原帖：https://x.com/StickyDev420/status/2114306861096661056
  - 厂商公告：https://github.com/spesmilo/electrum/security/advisories/GHSA-6jp4-8v48-cc5v
- 地址／IoC：未见公开 IoC（公告未列攻击服务器）。

### 5. Node2Shell／HTTP2Shell（CVE-2026-111497，Brotli）
- Assetnote 开源黑盒扫描器；GlobularOne、syrex1013 声称公开 PoC（未核实）；Wiz 发 Node.js 影响分析。
- 地址：
  - X 原帖：https://x.com/infosec_au/status/2114212833797996864
  - X 原帖：https://x.com/Dinosn/status/2114227651703439555
  - X 原帖：https://x.com/AdrianDacka/status/2114457270071488752
  - X 原帖：https://x.com/GlobularOne/status/2114215053285085232
  - X 原帖：https://x.com/N3mes1s/status/2114462924509159745
  - X 原帖：https://x.com/DerkiesAd001/status/2114488436979839241
  - GitHub（扫描器）：https://github.com/assetnote/node2shell-scanner
  - GitHub／PoC：https://github.com/syrex1013/CVE-2026-111497-node2shell
  - GitHub／PoC：https://github.com/GlobularOne/HTTP2Shell-PoC
  - GitHub（靶场）：https://github.com/tani2shell/node2shell-lab
  - 文章：https://www.wiz.io/blog/cve-2026-111497-brotli-rce-node-js
  - 文章：https://broccoli2shell.com/
- 地址／IoC：未见公开 IoC。

### 6. Tailworm：Tailscale／headscale 11 个未修问题
- Cyberdione Labs 的 Erica Windisch 在实验室测试 Tailscale 1.104.2 和 headscale 0.29.5；核心是 Tailscale SSH 按设备而非凭据授权，已失陷的一台设备可借 Unix socket 转发拿 root。无公告、无 CVE、无修复版本；Tailscale 工程副总裁回应正在修，但不建议所有人关掉 Tailscale SSH。@vysecurity 对结论有异议。
- 地址：
  - X 原帖：https://x.com/Dinosn/status/2114302182212153379
  - X 原帖：https://x.com/__kokumoto/status/2114495976811717093
  - X 原帖：https://x.com/vysecurity/status/2114453949004788005
  - 文章：https://tailworm.com/
  - 文章：https://thehackernews.com/2026/10/unpatched-tailscale-ssh-flaws-could-let.html
- 地址／IoC：未见公开 IoC。

### 7. Adobe Commerce／Magento CVE-2026-71362（CVSS 9.1，账户接管，利用公开）
- 授权错误，可篡改客户会话身份、免密登录他人账户，无需认证或交互。影响到 2026 年 7 月隔离补丁级别，8 月隔离补丁修复。
- 地址：
  - X 原帖：https://x.com/DarkWebInformer/status/2114135916990410754
  - GitHub／PoC：https://github.com/mahumadad/cve-2026-71362-magento-ato
- 地址／IoC：未见公开 IoC。

### 8. Popcorn Time 旧更新器 CVE-2026-30612（CVSS 9.8）
- 废弃的 Time4Popcorn 更新器信任已过期域名，谁注册这些域名就能在用户电脑上执行代码；研究者推送了 200 多万次停用更新，但建议直接卸载。
- 地址：
  - X 原帖：https://x.com/omvapt/status/2114133340177514781
  - X 原帖：https://x.com/DEVOTOMSOLUTION/status/2114209532654059577
  - 文章：https://thehackernews.com/2026/10/researchers-push-over-2-million-updates.html
  - 文章：https://www.reddit.com/r/netsec/comments/1xe25f5/we_used_rce_on_3_million_pcs_to_prevent_a_botnet/
- 地址／IoC：未见公开 IoC。

### 9. 其他漏洞（简列）
- **Azure CVE-2026-83938（AKS 配置服务缺认证）／CVE-2026-110063（VM Inspector 链接跟随）**，均 CVSS 10，微软已缓解、客户无需操作、未见利用。X 原帖：https://x.com/EmunaEliran/status/2114251085372154355
- **F5 NGINX CVE-2026-93479／97205／15176** 数据面内存安全漏洞。X 原帖：https://x.com/zoomeyebot/status/2114397902386921662
- **NLnet Labs NSD 4.10.0–4.15.2** CVE-2026-101337／101338／101339／101341 区域文件解析栈溢出。X 原帖：https://x.com/zoomeyebot/status/2114488499097522292
- **Drupal 核心 Field UI CVE-2026-108097** RCE。X 原帖：https://x.com/zoomeyebot/status/2114357651962528040
- **Python ssl 拉黑被泄私钥的 eMudhra 中间 CA（CVE-2026-115557）**；老版本 Node／certifi 仍信任伪造链。X 原帖：https://x.com/securitytopic/status/2114492215926096326 、https://x.com/theomlondhe/status/2114237713205322027 ；文章：https://security.entamec.com/article/python-ssl-emudhra-denylist-certifi-cve-2026-115557/
- **openapi-typescript-codegen CVE-2026-108551** PoC 公开。X 原帖：https://x.com/DarkWebInformer/status/2114142464588034149 ；GitHub：https://github.com/Zombie-Kaiser/CVE-2026-108551-POC
- **Zimbra CVE-2026-73570** 日志投毒到未授权 RCE，检测与修复指南。X 原帖：https://x.com/SecurityAr58409/status/2114160903033598131 ；文章：https://securityarsenal.com/blog/cve-2026-73570-zimbra-log-poisoning-to-unauthenticated-rce-detection-validation-and-remediation-guide
- **Elementor Pro CVE-2026-32475**。X 原帖：https://x.com/systemforce/status/2114280929707356288
- **Plex2Shell** 用户报告服务器被装挖矿程序。X 原帖：https://x.com/finesse_server/status/2114363127576002789
- **Arista VeloCloud 114625（KEV，10-26 到期）** 回顾：https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/ 、https://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html
- **微软 10 月补丁日 1,413 个漏洞**，仅一个 Windows Shell 漏洞被利用（帖子未给 CVE）。X 原帖：https://x.com/alex_cuciureanu/status/2114444183284908220 、https://x.com/prioriq/status/2114322410639884731
- **Project Zero 谈紧急修补**：https://projectzero.google/2026/10/emergency-patching.html
- **未经证实的声称**：Depov 称持有 Cisco Nexus 3000／9000 NX-OS（CVE-2026-76471／76485）相关利用，仅为声称。X 原帖：https://x.com/intels_daily/status/2114493994956710043
- **Genesys 内部业务系统安全事件**：https://www.genesys.com/blog/post/security-update-incident-affecting-certain-genesys-internal-business-systems
- 以上地址／IoC：未见公开 IoC。

## 工具与 GitHub 发布

本轮未用 GitHub API 核对 nuclei／nuclei-templates／Sliver／BloodHound／NetExec／Mythic 的正式 release，以下为 X 上出现的新仓库：

- **whokilleddb/TTs**：借 TextTransform.exe 加载 shellcode 的加载器（检测侧可关注该程序异常调用）。X：https://x.com/r1cksec/status/2114330777282351615 ；GitHub：https://github.com/whokilleddb/TTs
- **chryzsh/redteam-bofs**：红队 BOF 合集。X：https://x.com/PumpkinSecurity/status/2114225236124287478 ；GitHub：https://github.com/chryzsh/redteam-bofs
- **totekuh/winbox**：97 个 MCP 工具的 Windows 测试工具箱。X：https://x.com/EsGeeks/status/2114172560426561727 ；GitHub：https://github.com/totekuh/winbox
- **baguette168/nmg**：生成注入 IIS／ASP.NET 的 .NET 内存马，可接 Godzilla／Behinder／AntSword（防守方需关注无文件 webshell）。X：https://x.com/ipurple/status/2114368613193064480 ；GitHub：https://github.com/baguette168/nmg
- **JoasASantos/SysWhispers4**：直接系统调用生成器。X：https://x.com/Dinosn/status/2114236405778190620 ；GitHub：https://github.com/JoasASantos/SysWhispers4
- **EthanArbuckle/fairplay-decrypt**：iOS FairPlay 解密。X：https://x.com/Dinosn/status/2114228594830704947 ；GitHub：https://github.com/EthanArbuckle/fairplay-decrypt
- **fedman0/Arad-Code**。X：https://x.com/MMD_Abedinii/status/2114344185184571572 ；GitHub：https://github.com/fedman0/Arad-Code
- **trhhubsd/ARTEX**。X：https://x.com/Marco_Ramilli/status/2114483752508276851 ；GitHub：https://github.com/trhhubsd/ARTEX
- **smile178998/php2shell-toolkit**、**tani2shell/php2shell-lab**：PHP2Shell 检测／靶场。X：https://x.com/Nonameulno/status/2114419044480913757 、https://x.com/tani2shell/status/2114327287357427861 ；GitHub：https://github.com/smile178998/php2shell-toolkit 、https://github.com/tani2shell/php2shell-lab
- **grayhatkiller/switcheroo**：@ntlmrelay 网络中 10-24 分享最多的链接之一。X：https://x.com/ntlmrelay/status/2114311494846263634 ；GitHub：https://github.com/grayhatkiller/switcheroo
- **LogonUI PIN 截获研究**：用 CPU 硬件断点在 LogonUI.exe 内读取 PIN，登录照常成功（帖子未附仓库链接）。X：https://x.com/ipurple/status/2114435324218855477
- **Windows Rootkits／Bootkits 指南 v2.1（PDF）**。X：https://x.com/DirectoryRanger/status/2114349689445253296 ；PDF：https://github.com/ArtemBaranov/WindowsRootkitsGuide/blob/main/rootkits_bootkits_v2_1.pdf
- **ripgrep 作为 LOLBin**（Hexacorn）。X：https://x.com/DirectoryRanger/status/2114351409122422947 ；文章：https://www.hexacorn.com/blog/2026/10/25/ripgrep-as-a-lolbin/
- **i0n1c Secure Kernel 初探勘误**。X：https://x.com/i0n1c/status/2114456820286923086 ；文章：https://antid0te.sg/blog/secure-kernel-first-look-erratum.html
- **METR 红队测试 OpenAI 代理监控**。X：https://x.com/Z3nlyte/status/2114496111847084426 ；文章：https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/
- **OpenAI 代理演示 VM 逃逸与跨沙箱秘密通信**。X：https://x.com/Dinosn/status/2114327775658074479 ；文章：https://thehackernews.com/2026/10/openai-ai-agents-demonstrate-vm-escapes.html
- **红队行动被发现的复盘**。X：https://x.com/ipurple/status/2114419288547250352 ；文章：https://gikaku.net/2026/10/25/red-team-engagement-detected/

## APT / Malware 分析

### 1. VS Code 市场 8 个看板扩展共用一个 RAT 引擎（Yeeth Security）
- 8 个发布者、10 小时内上架、全部通过微软审核；扩展每 5 秒轮询 C2，等待指令后用 `child_process.exec` 执行。服务器下发代码、没有固定载荷，检测应盯客户端行为（SecretStorage 键名、日志字符串）而非单一样本。
- 地址：
  - X 原帖：https://x.com/YeethSecurity/status/2114376507598778751
  - 文章：https://yeethsecurity.com/blog/2026-10-25-Shared-RAT-Engine-VS-Code-Task-Boards
- IoC 见汇总（8 个 .vsix 的 SHA-256、SecretStorage 键名、声称的 GitHub 仓库）。

### 2. RFRx003：经 CommuniGate Pro 攻击 IT 公司的新后门（Solar 4RAYS）
- 受害者为 IT 公司，后门支持 PTY、SOCKS5 隧道（DNS 走 8.8.8.8）。
- 地址：
  - X 原帖：https://x.com/rst_cloud/status/2114422523303518360
  - 文章：https://rt-solar.ru/solar-4rays/blog/7122/
- IoC 见汇总（MD5／SHA1／SHA256）。

### 3. GlassWorm 借 OVHcloud CLI GitHub Release 替换投毒（StepSecurity）
- 攻击者替换 5 个 OVHcloud CLI 版本的二进制，在线 94 分钟后删痕；执行 `ovhcloud version` 即可识别恶意构建。关联账户 Hassenbf、Forcememo。
- 地址：
  - X 原帖：https://x.com/rst_cloud/status/2114354345177157908
  - 文章：https://www.stepsecurity.io/blog/ovhcloud-cli-github-release-swap-glassworm
- IoC 见汇总。

### 4. Hermes：俄语市场窃密木马／RAT，274 页报告
- 从一个可疑 Python 仓库追出，两条投递路径、15 个模块构建，隔离实验室测试。
- 地址：
  - X 原帖：https://x.com/suuci2/status/2114399403351896504
  - PDF：https://papers.lisdex.sh/hermes/paper.pdf
  - PDF：https://papers.lisdex.sh/hermes/report.pdf
- 地址／IoC：帖子未直接列出，IoC 在 PDF 内（本轮未逐条抄录）。

### 5. 其他情报
- **SliverC2 基础设施（Shodan 发现）**：X：https://x.com/orlof_v/status/2114370012031123491 ；完整列表：https://github.com/orlofv/Indicators/blob/main/SliverC2 （列表为数百个 IP，汇总仅抄帖子原文 4 个）。
- **Natalism Stealer**（作者称疑为 AI 生成的拼凑窃密木马）：X：https://x.com/Moltricks/status/2114462003334963405 ；GitHub：https://github.com/natalismst/Natalism-Stealer
- **Boundless Discord 被入侵**，假「NobleGuard」验证机器人导向 Inferno 式钱包抽干页：X：https://x.com/SY36111111/status/2114225432484864405
- **QuickLens、ShotBird Chrome 扩展被卖后变成假 Windows 更新陷阱**：X：https://x.com/windowsforum/status/2114457446127206653
- **用诗歌提示挖矿的僵尸网络，超 3,000 台服务器**：X：https://x.com/PVynckier/status/2114239548444033499 ；文章：https://www.bgr.com/2291192/botnet-uses-poetry-mine-crypto-ai-servers/
- **ConnectWise 入侵与 Entra OAuth 应用滥用（Mitiga）**：X：https://x.com/DirectoryRanger/status/2114350583222321169 ；文章：https://www.mitiga.io/blog/connectwise-breach-entra-app-abuse
- **Microsoft Authenticator（Android）可被零权限 App 冒充 Teams 截取令牌（EnclaveAI）**：X：https://x.com/Yanir_/status/2114368230512820293
- **GhostAction：OIDC 到 AWS 的滥用**：X：https://x.com/theomlondhe/status/2114358701104521310
- **俄罗斯情报部门试图窃取乌克兰 TechEx 无人机拦截器资料**：X：https://x.com/SwitHak/status/2114415456404808066 ；文章：https://24tv.ua/military/droni-perehoplyuvachi-spetssluzhbi-rosiyi-namagalis-vikrasti_n3034636
- **GMO Internet 事件赔偿公告**：X：https://x.com/SwitHak/status/2114418817359065431 ；公告：https://group.gmo/en/ir_news/article/691/
- **LiteLLM v1.107.0 攻击链调查完结**（昨晚已报根因）：X：https://x.com/kmkz_security/status/2114316733083201655 ；文章：https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain
- **DFIR 读物**：攻击者工作流笔记 https://dfir.ch/posts/field_note_attacker_workflow/ ；WMI 永久事件订阅持久化 https://www.forensicfocus.com/articles/investigating-wmi-permanent-event-subscription-persistence/ ；Entra ID 令牌窃取第 3 篇 https://insinuator.net/2026/10/token-theft-in-microsoft-entra-id-part-3-of-4-token-protection/
- **勒索声称（FalconFeeds，仅为声称、未证实）**：Cloak→Medi Porta；Anubis→Newcomer；WHITEARMOR→Hisense；EMPERADOR→AB InBev、AyT；Qilin→ETO GRUPPE、ECOM。示例：https://x.com/FalconFeedsio/status/2114204837319671990
- 以上未单列 IoC 的条目：未见公开 IoC。

## 地址／IoC 汇总

以下均原样抄录自来源，未做验证；勿直接访问。

**VS Code 看板扩展 RAT（Yeeth Security）**，.vsix SHA-256：
- flowstate.luaslope-1.0.2.vsix `8af9bf0e37b61763ba437007b425f3cf1d8c0273e91c5532c7cb29fe785f2f37`
- opentask.opentask-1.0.0.vsix `b7345ddd0bdb7490f2ed50229d97d4ab7cc78fb7ab9e9faf6f6c743aafec3e00`
- Markers.markersboard-2.2.4.vsix `22d7197c305aef735d01e34779af40454bf6804e83039c812b5c27c7ec017ff0`
- GiantManage.giantmanage-1.0.0.vsix `a087c1c13d322be354c0b8dd85ad29f293b93a14f9a07cad4bc2e10a032fc3f2`
- DawnTask.dawntask-1.0.1.vsix `4146488d3f89edd70e9d69ca77e400d8cc43521251e6598d17c123b867ad09a1`
- starktask.starktask-1.0.1.vsix `bae2e82ec138f7e8d9bd0db35b715967f5acad5284ebb905fd2811aaf5f9d0d2`
- greenbeans.greenbeans-2.0.0.vsix `6b67ff0cc465b7e9e2de6d1f7a8775c77eb1aa2b96f753a0882e6c18943022f1`
- parsley.parsley-4.0.0.vsix `b35471954e9ed7702298adf36ac95583d996a82d5a7be665936a24f0b67d5485`
- SecretStorage 键名：`opentask_session`、`markersboard_session`、`giantmanage_session`、`dawntask_session`、`starktask_session`、`greenbeans_session`、`parsley_client_session_v4`、`parsley_client_session`、`parsley_session`、`actionClientSession`
- 声称的仓库（均 404）：github[.]com/opentask/opentask、github[.]com/markers/markersboard、github[.]com/giantmanage/giantmanage、github[.]com/flowstate/luaslope、github[.]com/DawnTask/dawntask、github[.]com/starktask/starktask、github[.]com/greenbeans/greenbeans、github[.]com/parsley/parsley
- 来源：https://yeethsecurity.com/blog/2026-10-25-Shared-RAT-Engine-VS-Code-Task-Boards

**RFRx003（Solar 4RAYS）**：
- MD5：`2c4e238da1f6293f3a58d9b1b54b5f9f`（RFRx003）、`2b255e5ab646352cdde7630e5aae145e`（RFRx003）、`7797a72112b79332ff279b8bceeb671b`（加载服务）
- SHA1：`0254de8d244077c88aad04568d92edae38f3fbbc`（RFRx003）、`435ba7ebb7b5c7c865f92ec1b71403f719c551a0`（RFRx003）、`71ae6c5a51ac01b7e92fda9b7a26debd6e453a93`（加载服务）
- SHA256：`fbb6a011c382e78e8d74ab62af2b16b88fae435029dff5652570d92e4eb52554`（RFRx003）、`6bd9a1819550861ae65bae89a2f8ba6c932812a58c9bb482cf1e9dbe3ec0c28b`（RFRx003）、`942137727eb02afcf4c60abeb40b65874545983be12bb22886d1a67c0f8ea6f5`（加载服务）
- 来源：https://rt-solar.ru/solar-4rays/blog/7122/

**GlassWorm／OVHcloud CLI（StepSecurity）**：
- 恶意构建 commit：`5ead8ef9b43d354dfb5caadff803b11afc8c5c58`
- 恶意二进制 MD5：Darwin_arm64 `6f2f086239f3d88eb2750e871901927d`、Darwin_x86_64 `347e65eb7f2d78d1c6872690272a6cc3`、Linux_arm64 `01f57206d37c28cf711677f612052913`、Linux_x86_64 `301bff0b51980b9e76c93633e7cfd3bd`
- 加载器 stage 1（HassenBF/next-dashboard@227207ce preinstall.js）SHA-256：`43df42fd79f6f81e530892b54634598770d6e496796a863c596e616bcb3fec70`
- 加载器 stage 2 SHA-256：`0f79989912572a24ba13baabb32b3fd084496271c51448d47b66fe1aedbf293c`
- 外传地址：`https://45.32.148.174/upload`
- 文中时间线里的持久化 NodeJS 后门 C2：`162.33.177.177`
- 来源：https://www.stepsecurity.io/blog/ovhcloud-cli-github-release-swap-glassworm

**SliverC2（@orlof_v，Shodan）**，帖子原文：
- 136.70.229[.]109、138.3.216[.]107、204.168.131[.]234、209.74.83[.]47（另有 1 个及更多见列表）
- 来源：https://x.com/orlof_v/status/2114370012031123491 、https://github.com/orlofv/Indicators/blob/main/SliverC2

**Natalism Stealer（@Moltricks）**：
- 面板：`https://panel.cryptowtf.info/login`
- 发帖者邮箱：`pompake3169@gmail.com`
- 仓库：https://github.com/natalismst/Natalism-Stealer
- 来源：https://x.com/Moltricks/status/2114462003334963405

**Boundless Discord 钱包抽干（@SY36111111）**：
- 钓鱼域名：`noblehub.net`
- 来源：https://x.com/SY36111111/status/2114225432484864405

**PHP2Shell 挑战靶站**：stealmybitcoin[.]com（公开 CTF，不是恶意基础设施）。

**Tailworm 受影响版本**（非 IoC）：Tailscale 1.104.2、headscale 0.29.5。

**其余条目**：未见公开 IoC。

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

本轮 List 窗口内 184 条，高信号条目已并入上文：Tailworm（@Dinosn）、LiveOverflow 系列、FortiSIEM PoC（@Dinosn）、NMG 与 PIN 截获（@ipurple）、Hexacorn ripgrep、Mitiga、Unit 42 PHP2Shell（@ntlmrelay 汇总）、LiteLLM 攻击链（@kmkz_security）、OpenAI 代理逃逸（@Dinosn）、i0n1c 勘误。博客清单、Risky Business、tl;dr sec 本轮未发现需单列的新条目（未逐站抓取）。

## 来源搜索 URL

- CVE／PoC Latest：https://x.com/search?q=(CVE%20OR%20POC%20OR%20exploit%20OR%200day)&f=live
- CVE-2026 热门：https://x.com/search?q=%22CVE-2026%22&f=top
- 在野利用：https://x.com/search?q=(%22actively%20exploited%22%20OR%20%22zero-day%22)&f=live
- 厂商公告：https://x.com/search?q=(NetScaler%20OR%20Fortinet%20OR%20Cisco%20OR%20Ivanti)%20(exploited%20OR%20patch)&f=live
- GitHub 红队工具：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20BOF)&f=live
- 恶意软件分析：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)&f=live
- IoC：https://x.com/search?q=(IOCs%20OR%20%22C2%20server%22%20OR%20sha256)&f=live
- LWiS List：https://x.com/i/lists/1239330068461244424
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
