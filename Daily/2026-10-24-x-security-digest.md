# X 安全情报晚报 · 2026-10-24

> 搜集窗口：圣地亚哥时间 **2026-10-23 20:13 至 2026-10-24 20:08**（America/Santiago／UTC-3，接昨晚窗口）。X 搜索参数：`start_time=2026-10-23T23:13:00Z`，不设 end_time。实际抓到的帖子从 **10-23 20:13** 到 **10-24 20:08**（UTC-3），**实际有效覆盖约 23 小时 55 分**。10-23 深夜到 10-24 清晨（UTC-3）帖子较少，宽泛查询多数结果落在 10-24 白天，所以另做了一次早段补查（A7）。
> **X 采集方式**：Grok Bot 自带的 X 只读公共数据接口（`search_posts_all`，用 Latest／recency 和 relevancy 两种排序；`get_posts_by_ids` 读重要原帖全文）。**没有开浏览器，也没有检查 @seogoogle4 的浏览器登录状态。** t.co 短链按接口返回的 `entities.urls[].expanded_url` 展开，本次**没有逐条用 curl 再跟一遍跳转**。下文列出的外部文章和仓库，已用 curl 核对过可访问性（BleepingComputer、SecurityWeek Capcom 页对本机返回 403，以 X 原帖为准）。纯图片／视频链接不列。
> 本轮各类查询：
> - A 类（CVE／0day／PoC）：recency、relevancy、四个时间切片、早段补查，共七次
> - B 类（GitHub 红队／C2／nuclei）：两次
> - C 类（malware analysis／threat report／threat actor、IoC）：三次
> - LWiS List：500 名成员分 10 段做 `from:` 批次（10 次）
> - 核心媒体／厂商账号：一次；IoC 猎人账号：一次
> - 专题（PHP2Shell／115560、Brotli、LiteLLM）：三次
> - 原帖全文读取：一次（40 个 ID）
>
> 合计 **28 次有效 X 读取，0 次 429**（当日配额剩余 972/1000）。
> **覆盖说明**：每次查询最多返回 25 条，PHP2Shell／LiteLLM 热帖会占满宽泛查询，所以用切片和专题查询补齐。剔除了广告／营销、空转发、Grok 自动回复、体育／加密货币刷屏帖。
> 各批次原始返回共 609 条，窗口内去重后 **522** 条帖子（与 seen_ids 7188 条**零重叠**）。关键词粗筛得 **356** 条安全相关新帖（排除纯转推），下文实际引用约 90 条。全程只读，没有发帖、回复、点赞、转推、收藏或关注。
> **公开备援**（`/workspace/enrich-2026-10-24/`）：CISA KEV JSON；NVD API（核对 CVE-2026-9256、42945、111497、115560）；nginx.org 安全公告页；CrowdStrike 博客（PHP2Shell 武器化障碍）；Unit 42 PHP 简报；0x4D31 蜜罐报告原文（GitHub）；THN（LiteLLM 根因、Popcorn Time）；AlmaLinux 博客（ZDI-CAN-33367）；CYFIRMA；Zscaler。
> GitHub API 核对了 nuclei／nuclei-templates／Sliver／BloodHound／NetExec／Mythic／impacket／AdaptixC2：**本窗口内没有新的正式 release**。最近的分别是 nuclei-templates v10.5.1（10-23 08:19 UTC-3，在本窗口之前）和 BloodHound v9.9.0-rc3（10-21 20:31 UTC-3）。
> **CISA KEV：catalogVersion 2026.10.23／1756 条，Δ0**（与昨晚相同）。`dateReleased` 为 2026-10-23 16:30 UTC-3，今天（周六）没有更新。
> - **今日 10-24 到期**：无。
> - **今日起转为逾期**（10-23 到期）：SiteGuard Server Edition **CVE-2026-106931**、Plex **CVE-2026-96656**、Plex **CVE-2026-96654**。
> - **10-26（周一）到期**：Arista VeloCloud Orchestrator **CVE-2026-114625**、Collabora Online CODE **CVE-2026-110447**。
> - **11-03 到期**：Plex 96652、Plex 96655、Siemens 110936。
> - **逾期（续）**：
>   - 10-19 到期：BeyondTrust 102764、Fortinet CVE-2025-61624
>   - 10-18 到期：Atlassian 21589
>   - 10-17 到期：AhsayCBS 105133／105134、Cisco SEG 76519、PAN-OS 0322
>   - 10-16 到期：Ivanti 104935、Windows 96951
>   - 10-13 到期：Apple 86950
>   - 10-11 到期：CVE-2015-5477、CVE-2016-3081、CVE-2023-22894、CVE-2021-3199、CVE-2015-3306
> - **X 上的说法与 KEV JSON 不符，需注意**：
>   - @threatpodium 称「7 new KEVs」：KEV JSON 今日 Δ0，可能是按周统计或口径不同
>   - @blueteamsec1 转发「CISA 新增 SharePoint CVE-2026-58644」：KEV JSON 显示该条早在 **2026-07-16** 就已入列，属于旧闻再推。NVD 评分 9.8，修复版本为 SP2016 16.0.5556.1005、SP2019 16.0.10417.20153、SE 16.0.19725.20384
> - **仍未进 KEV、但今日高优先**：
>   - **PHP2Shell 109618／109619**：今天首次出现公开、可复核的蜜罐 RCE 证据（0x4D31）
>   - PHP 115560（未修）
>   - Brotli 111497
>   - FortiSIEM 106173：已有两个公开 PoC 仓库
>   - NGINX 9256／42945
>   - YOOtheme Pro 102785
>   - Atlassian 65637：只有 SecBoard 一家称在野，**UNCONFIRMED**
>
> 规则：每条都带完整 https URL，X 原帖／GitHub·PoC 仓库／厂商公告／文章分开列；没有指标的写「未见公开 IoC」；不编造。**不转载利用代码、payload 或 PoC 步骤**，PoC 仓库只给链接，供狩猎用。泄露、入侵类声称一律标 **UNCONFIRMED／未验证**。IoC 已去武器化（`[.]`、`hxxp`）。

## 今日摘要

1. **PHP2Shell 出现首个公开、可复核的在野 RCE 证据**：0x4D31 的 phpot 蜜罐（PHP 8.4.26 + Apache mod_php）记录到 **35 次由 Apache worker 直接派生 `/bin/sh`**。来源有两个 IP 簇：15.204.59[.]70（OVH）和 162.35.99[.]94（Interserver）。手法与公开的 HTTP-only PoC 家族一致，利用「泄露引导绕 ASLR」。第一次确认的 shell 出现在 10-24 12:35（UTC-3）。
2. **各方对 PHP2Shell 的判断不一**：
   - CrowdStrike（10-23）：已在内部复现 RCE，但「未观察到成功的在野利用」，并认为武器化门槛高
   - Unit 42：确认在野利用，攻击者用 agentic AI 做后渗透（命令分段标记 `==SHELLUSER==`／`==PASSWD==`），暴露面约 2260 万个实例
   - CISA：更新警报并附 SIGMA 规则；建议 PHP 8.1 及更早版本下线
   - CYFIRMA：称疑似 DPRK「Minjun」活动正在为 PHP2Shell 做侦察
3. **LiteLLM 根因公布**：2026-05-27，Agent Platform 的 master key 误提交到公开仓库，事后**没有吊销**。攻击者（69.48.229[.]143）10-10 用这把 key 取得一个未限权的 GitHub owner OAuth token，10-21 改了发布流水线，把源指向仿冒仓库 `Berri-AI/litellm`，发布 1.107.0。
4. **FortiSIEM CVE-2026-106173**：除 Horizon3 官方 PoC 外，又出现社区 PoC 仓库。漏洞在 gRPC QueryResultReq（TCP 27918），影响 7.0.0–7.5.0，修复版为 7.5.1／7.6.0。
5. **Brotli CVE-2026-111497**：THN 报道影响面扩展到 Bun、Python、Envoy、Istio；受影响版本 1.0.3–1.2.0，目前未见在野利用。
6. **新内核 LPE ZDI-CAN-33367**（与 Dirty Frag／Fragnesia 同类，CVSS 7.8）：公开邮件列表已附可用 PoC。AlmaLinux 8／9／10 的测试版内核已出。
7. **APT／恶意软件**：
   - BlackX UEFI bootkit（APT41，Baton Drop CVE-2022-21894）
   - Lazarus 用 ML-KEM-1024 保护 C2
   - APT37 新增气隙网络能力（Zscaler）
   - MuddyWater 冒充 Chaos 勒索做假旗（C2 moonzonet[.]com）
   - 0x0v1 披露 UCreator：基于虚拟化的 Android 间谍平台
   - AtlasRAT／ValleyRAT 用伪造的 Microsoft 更新域名证书
8. **IoC 猎人**：
   - malwrhunterteam：S3 上的 CobaltStrike＋TigerRAT 压缩包
   - Malwarehunterr：63 个流媒体域名重定向到 MediaGet.exe
   - SliverC2 IP、Meduza 开放目录、cyuop[.]com 等，详见 IoC 汇总
9. **其他补丁与事件**：
   - YOOtheme Pro 5.0.53（修复 CVE-2026-102785，CVSS 10）
   - Postiz 2.25.3（修复三个 CVE）
   - NGINX 1.30.2／1.31.1（9256＋42945 可串成链）
   - jxrlib 多个内存错误，多数发行版未修
   - Initia 链 MoveVM 零日，被盗约 270 万美元
   - Capcom 泄露影响 1100 万人
   - Eye Security 推送 200 万次更新，关停 Popcorn Time 分支的遗留更新器

## CVE / POC / 漏洞

### 1. PHP2Shell CVE-2026-109618／109619：首个公开蜜罐 RCE 证据，各方对在野规模判断不一（未进 KEV）
- **谁／打什么**：
  - **0x4D31 蜜罐报告（10-24）**：三台 phpot 蜜罐（PHP 8.4.26、单 worker Apache mod_php、内存上限 128 MiB），35 个完整的执行阶段 POST 对应 35 次 Apache worker（uid=33）派生 `/bin/sh`。
    - Episode A：15.204.59[.]70，首个 shell 出现在 10-24 12:35（UTC-3）
    - Episode B：162.35.99[.]94，13:46 到 15:57（UTC-3）之间共 32 次 shell
    - 两个簇共用同一套四阶段 multipart 模板，作者明确说明**不能据此判定为同一行动者**
    - 另有 104.28.208[.]84、144.48.4[.]242 发送了符合利用特征的请求，但**没有确认 RCE**，只算尝试指标
    - 回连命令都是 `id` 加 curl／wget／php 的探活，**未见后续落地载荷**
  - **CrowdStrike（10-23 博客）**：内部已复现 RCE（权限为 mod_php／FPM worker），但「未观察到成功的在野利用，也未见完全武器化的 exploit」。认为利用需要针对具体的 PHP、libc、SAPI 和镜像版本校准，构成门槛。
  - **Unit 42（10-23 更新）**：确认在野利用。某欧洲政府机构被攻破后，攻击者 2 小时内拿到密码哈希和 MFA 密钥，搭建 NTLM relay 并尝试提权到域管。命令按 `==SHELLUSER==`、`==PASSWD==` 分段，Unit 42 认为是 agentic 攻击者的特征。Xpanse 统计约 2260 万个潜在暴露实例。
  - **CYFIRMA（经 @rst_cloud 摘要）**：疑似韩语、与 DPRK／Lazarus 有关的「Minjun」活动正处于侦察和武器化阶段，目标涵盖政府、金融、制造、物流、航运、航空等行业。报告提到 17 个与 webshell／session 投毒相关的源 IP，并说明这些 IP **与 DPRK 活动没有独立关联**。归因为中等置信度，**UNCONFIRMED**。
  - **CISA**：更新 PHP2Shell 警报，附 SIGMA 规则；PHP 8.1 及更早的 EOL 版本建议下线。
  - **社区观点**：LiveOverflow 认为可以打到真实系统，但目前不是大规模利用；@domchell 引用 CrowdStrike 文章；@i0n1c 也有讨论。
  - **@Knaitobureza**：推测 Good Smile Company 网店后台 10-19 至 10-22 被入侵与此有关，属**推测，UNCONFIRMED**；官方只确认了入侵事件本身。
- **补丁／缓解**：
  - 升级到 8.5.12／8.4.27／8.3.36／8.2.35，**并重启所有 Apache／FPM worker，重建容器镜像**
  - 不需要时关闭 `session.upload_progress.enabled` 和 `file_uploads`；注意这对 109618 的 HashTable 问题无效
  - 在反向代理层限制请求体大小、multipart 字段数和参数名长度
- **狩猎**：
  - Apache／php-fpm 进程派生 sh、curl、wget、php -r 子进程
  - 异常巨大的 `PHPSESSID` 响应（0x4D31 观察到约 819,200 字节）
  - 同一源 IP 连续发送超大 multipart（上千个 `files*`／`x*` 字段），伴随 `Unknown on line 0` 的 PHP 启动期错误
  - 新出现的 PHP webshell，`.user.ini`／`.htaccess` 被改，cron 或 SSH key 持久化
  - 回溯时间从 10-17 起
- 地址：
  - X 原帖：https://x.com/0x4D31/status/2114100034593820876 ｜ https://x.com/DailyDarkWeb/status/2114077776688869721 ｜ https://x.com/CISACyber/status/2113985888774451685 ｜ https://x.com/InfraWatchHQ/status/2114013283854254407 ｜ https://x.com/domchell/status/2113904109396873644 ｜ https://x.com/LiveOverflow/status/2114061866808824188 ｜ https://x.com/i0n1c/status/2114053797152518373 ｜ https://x.com/rst_cloud/status/2114084643779613011 ｜ https://x.com/CrowdStrike/status/2113774974582313361 ｜ https://x.com/Knaitobureza/status/2113820680529514965 ｜ https://twitter.com/goodsmile_en/status/2113630247006371894
  - GitHub·PoC 仓库：https://github.com/0x4D31/honeypot-data/tree/main/reports/php2shell （证据报告，不含利用代码）
  - 厂商公告：https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching ｜ https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
  - 文章·PDF：https://www.crowdstrike.com/en-us/blog/obstacles-to-weaponizing-php2shell-likely-constrain-exploitation/ ｜ https://github.com/0x4D31/honeypot-data/blob/main/reports/php2shell/2026-10-24-confirmed-rce.md ｜ https://www.cyfirma.com/research/cyfirma-threat-advisory-suspected-dprk-campaign-staging-php2shell-targeting-against-global-php-infrastructure/
  - IoC：15.204.59[.]70、162.35.99[.]94（回连 162.35.99[.]94:8080、:80；15.204.59[.]70:8081），尝试源 104.28.208[.]84、144.48.4[.]242（均来自 0x4D31 报告）。CYFIRMA 帖称报告含 IoC，但**帖内未列出**，本报告未抄录。

### 2. PHP CVE-2026-115560（未修）与 json_encode UAF 变种
- **谁／打什么**：
  - 115560 仍然没有正式补丁，只影响运行时修改了 `session.serialize_handler` 的应用（@PHPSiteAudit）
  - @ksg93rd 建议关闭 session upload progress
  - @AdrianDacka 发布 json_encode UAF 新变种仓库，是否获得 CVE、是否可利用都**未经厂商确认**
  - NVD 目前查不到 115560
- **补丁／缓解**：保持 `session.upload_progress.enabled=0`，不要在运行时切换 serialize_handler，等下一次常规版本。
- **狩猎**：审计代码里的 `ini_set('session.serialize_handler'…)` 调用；狩猎方法同第 1 条。
- 地址：
  - X 原帖：https://x.com/PHPSiteAudit/status/2114114526627217728 ｜ https://x.com/ksg93rd/status/2114015181583867984 ｜ https://x.com/AdrianDacka/status/2113958855864434987
  - GitHub·PoC 仓库：https://github.com/syrex1013/php-json-encode-uaf
  - 厂商公告：https://www.php.net/
  - IoC：未见公开 IoC

### 3. FortiSIEM CVE-2026-106173 —— 第二个公开 PoC 仓库（未进 KEV）
- **谁／打什么**：未认证的 gRPC QueryResultReq 路径（TCP/27918）。Horizon3 官方 PoC 之外，又出现社区仓库 MRdark-ops/rce-FortiSIEM，**来源可信度未核实**，第三方 PoC 有夹带恶意代码的风险。尚未确认在野利用。
- **补丁／缓解**：影响 7.0.0–7.5.0，升级到 7.5.1／7.6.0；27918 端口不要暴露到互联网。
- **狩猎**：检查外部来源访问 27918 的连接，以及 phMonitor／gRPC 服务进程派生的异常子进程和异常写文件。
- 地址：
  - X 原帖：https://x.com/DarkWebInformer/status/2114092646847201702 ｜ https://x.com/DarkWebInformer/status/2114088622093717848
  - GitHub·PoC 仓库：https://github.com/horizon3ai/CVE-2026-106173 ｜ https://github.com/MRdark-ops/rce-FortiSIEM
  - IoC：未见公开 IoC

### 4. Brotli CVE-2026-111497（HTTP2Shell）—— 下游扩散
- **谁／打什么**：Brotli 解码器（c/dec/decode.c）缓冲区溢出，受影响版本 1.0.3–1.2.0（NVD，状态 Awaiting Analysis）。THN 报道波及 Bun、Python、Envoy、Istio。@DazedProgrammer 称目前未见利用。
- **补丁／缓解**：升级到 Brotli 1.2.1，Node 22.23.4／24.22.1／26.12.1（@SecWireDaily），逐个确认各下游的修复版本。
- **狩猎**：资产清单里查静态链接的 libbrotli；关注接收 `Content-Encoding: br` 的服务是否异常崩溃。
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2113916077923303786 ｜ https://x.com/DazedProgrammer/status/2114099663426982192 ｜ https://x.com/SecWireDaily/status/2114009244290650396
  - 文章·PDF：https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html
  - IoC：未见公开 IoC

### 5. 尚未见攻击的补丁清单：GitLab 110264／Node 111497／Pillow CVE-2026-112900
- **谁／打什么**：@SecWireDaily 汇总了目前没有在野报告的补丁：
  - GitLab 110264：修复版 19.5.1／19.4.3／19.3.6
  - Node：修复版 22.23.4／24.22.1／26.12.1
  - Pillow CVE-2026-112900（CVSS 9.2）：修复版 13.0.0
- **狩猎**：按版本盘点资产。
- 地址：
  - X 原帖：https://x.com/SecWireDaily/status/2114009244290650396
  - IoC：未见公开 IoC

### 6. KEV 新条目后续：Arista VCO 114625、Collabora CODE 110447（10-26 到期）
- **谁／打什么**：
  - Arista：修复版 5.2.3.18（@VarunChopr17597）；@2Workly 列出攻击 IP
  - Collabora：漏洞在 proxy.php，**只在 CODE server 停止时**可被利用（@Spaceprogrammer）
  - THN 报道 CISA 将两者标为在野利用
- **补丁／缓解**：Arista VCO 升到 5.2.3.18；Nextcloud 的 richdocumentscode 升级或删除。
- **狩猎**：VCO 日志里的 SQL 注入特征和来自下列 IP 的访问；Nextcloud 对 proxy.php 的异常请求和新增 PHP 文件。
- 地址：
  - X 原帖：https://x.com/VarunChopr17597/status/2114051142032179250 ｜ https://x.com/2Workly/status/2113899924249268451 ｜ https://x.com/Spaceprogrammer/status/2114082070918213671 ｜ https://x.com/TheHackersNews/status/2113879925950501308 ｜ https://x.com/sunsetwatch26/status/2114034107235840393
  - 文章·PDF：https://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html
  - IoC：74.82.197[.]86、38.54.50[.]151（@2Workly，Arista 相关）

### 7. NGINX CVE-2026-9256＋CVE-2026-42945 链式利用分析（旧 CVE，新串联）
- **谁／打什么**：@DFIR_Radar 称两者可串成链：ngx_http_rewrite_module 的堆越界读加堆溢出，在特定 rewrite 配置下可未认证 RCE（帖中 CVSS 8.1）。nginx.org 对两者的评级都是 medium，NVD 发布日期为 2026-05-13 和 2026-05-22，**都是旧漏洞**。未见在野报告。
- **补丁／缓解**：
  - 9256：1.31.1+、1.30.2+ 不受影响
  - 42945：1.31.0+、1.30.1+ 不受影响
  - F5 公告 K000161377、K000161019
- **狩猎**：审计 rewrite 规则，重点看重叠 PCRE 捕获（`$1$2`）和后接 `?` 的替换串。
- 地址：
  - X 原帖：https://x.com/DFIR_Radar/status/2114130782377623979
  - 厂商公告：https://nginx.org/en/security_advisories.html ｜ https://my.f5.com/manage/s/article/K000161377 ｜ https://my.f5.com/manage/s/article/K000161019
  - IoC：未见公开 IoC

### 8. Linux 内核 ZDI-CAN-33367（Dirty Frag 同类 LPE）
- **谁／打什么**：本地无特权用户可以篡改自己只能读、不能写的文件（比如 root 文件）在 page cache 中的内容，ZDI 评分 CVSS 7.8。10-21 报到内核安全团队和公开邮件列表时**附带了可用 PoC**。
- **补丁／缓解**：AlmaLinux 8／9／10 测试版内核已出，其他发行版请关注各自公告。多租户主机、CI runner、容器构建机优先处理。
- **狩猎**：非特权用户进程修改 SUID 二进制或 /etc 关键文件后出现提权；文件哈希与磁盘内容不一致（page cache 被篡改）。
- 地址：
  - X 原帖：https://x.com/AlmaLinux/status/2113791131213246811
  - 厂商公告：https://almalinux.org/blog/2026-10-23-zdi-can-33367/
  - IoC：未见公开 IoC

### 9. YOOtheme Pro CVE-2026-102785（CVSS 10，未认证 RCE）
- **谁／打什么**：影响 YOOtheme Pro 5.0.0–5.0.52（WordPress／Joomla 主题框架），Pro 4 及更早版本不受影响。未见在野报告。
- **补丁／缓解**：升级到 5.0.53 及以上。
- **狩猎**：wp-content／templates 目录中新出现的 PHP 文件。
- 地址：
  - X 原帖：https://x.com/ZeroKaiLabs/status/2114037602101989723
  - 厂商公告：https://yootheme.com/changelog
  - IoC：未见公开 IoC

### 10. Postiz CVE-2026-115931／115932／115933
- **谁／打什么**：
  - 115931：已登录用户可调用 provider 辅助方法，造成本地文件读取等问题，2.25.2 修复
  - 115932：媒体路径穿越，2.25.3 修复
  - 115933：各类 token 共用签名密钥、没有绑定用途，2.25.3 修复
  - CVSS 分别为 9.9／9.6／9.9，未见在野利用
- **补丁／缓解**：升级到 2.25.3 或更高版本。
- 地址：
  - X 原帖：https://x.com/_pksharma/status/2114100687785402596
  - IoC：未见公开 IoC

### 11. jxrlib（JPEG XR）多个内存错误，多数发行版未修
- **谁／打什么**：Joachim Rütter 于 10-24 04:52（UTC-3）在 oss-security 报告 6 个崩溃类问题，暂无 CVE，**未证实可执行代码**。
  - mircomir/jxrlib 1.4.4 已修
  - Debian／Ubuntu、Fedora／EPEL、Homebrew、vcpkg 以及 Wine 自带的版本尚未修复
  - 通过 ImageMagick 的 delegate、FreeImage、Calibre 等途径可能暴露
- **补丁／缓解**：在 ImageMagick policy 中禁用 jxr／wdp 格式。
- 地址：
  - X 原帖：https://x.com/superdoccimo/status/2113935194243633330
  - IoC：未见公开 IoC

### 12. Initia 链 MoveVM 零日（加密货币）
- **谁／打什么**：攻击者利用 MoveVM 零日增发 AUSD、USDC、ETH 并跨链转出，约 270 万美元。L1 和各 rollup 于 10-23 12:41:30（UTC-3）停链。
- 地址：
  - X 原帖：https://x.com/blockscout/status/2113813735039230078
  - 文章·PDF：https://eth.blockscout.com/address/0x358eF0130f7A5aA516dCd81Bdc80B18CdE41CAC8
  - IoC：0x358eF0130f7A5aA516dCd81Bdc80B18CdE41CAC8（资金归集地址）

### 13. 其他与 UNCONFIRMED
- **Atlassian CVE-2026-65637**：SecBoard 称「actively exploited」，KEV 中没有，其他来源也未见佐证，**UNCONFIRMED**。https://x.com/BytesNora/status/2113854156020621691
- **Aruba AOS**：8 个满分漏洞，管理口应隔离到独立 VLAN（汇总帖）。https://x.com/sunsetwatch26/status/2114034107235840393
- **SharePoint CVE-2026-58644**：被当作「新增 KEV」转发，实为 07-16 入列的旧条目。https://x.com/blueteamsec1/status/2114107734841016644
- **ThreatPodium「7 new KEVs」**：与 KEV JSON 的 Δ0 不符。https://x.com/threatpodium/status/2114126367184789609 ｜ https://threatpodium.com/threat-intelligence-report-2026-10-24/
- **k0t**：继续大规模利用 FortiWeb CVE-2025-64446 和 GlobalProtect CVE-2026-0257，复述昨日的 Group-IB 情报。https://x.com/DEVOTOMSOLUTION/status/2113844373968257208
- **Capcom 数据泄露**：影响 1100 万人，SecurityWeek 报道。https://x.com/SecurityWeek/status/2114047770495717437 ｜ https://www.securityweek.com/11-million-impacted-by-capcom-data-breach/
- **Microsoft Defender 无法扫描 WebDAV 共享**：研究者观察，未经厂商确认。https://x.com/MSNightmare2000/status/2113905487217389837

## 工具与 GitHub 发布

> 主流框架（nuclei、nuclei-templates、Sliver、BloodHound、NetExec、Mythic、impacket、AdaptixC2）**本窗口内没有新的正式 release**（已用 GitHub API 核对）。以下是 X 上的新仓库和更新，**均未审计代码，仅供参考**。

1. **TornadoC2**（新 C2 框架，@ipurple 介绍）：可据此提前编写检测。
   - X 原帖：https://x.com/ipurple/status/2114034563529740706
   - GitHub：https://github.com/kamalx06/TornadoC2
2. **WhatAboutSAM**：SAM dumper，新增 WRITE_DAC 滥用路径（@PedroGabaldon）。狩猎：注册表 SAM／SECURITY hive 的 DACL 被修改。
   - X 原帖：https://x.com/PedroGabaldon/status/2114056947112558903
   - GitHub：https://github.com/PeterGabaldon/WhatAboutSAM/tree/main
3. **chryzsh/redteam-bofs**：Beacon Object Files 合集，用于凭据搜寻、日志解析、共享枚举。
   - X 原帖：https://x.com/Dinosn/status/2113983607823823033 ｜ https://x.com/PumpkinSecurity/status/2114041137514328311
   - GitHub：https://github.com/chryzsh/redteam-bofs
4. **KillerLand → LOLDrivers**：又有两个 BYOVD EDR killer 驱动收入 LOLDrivers（PR #475）。防御：导入 LOLDrivers 阻断列表或 WDAC 驱动阻断规则。
   - X 原帖：https://x.com/_josehelps/status/2114069162553483298 ｜ https://x.com/_josehelps/status/2114069198439952541
   - GitHub：https://github.com/redteamfortress/KillerLand ｜ https://github.com/magicsword-io/LOLDrivers/pull/475
   - 厂商：https://www.magicsword.io/threat-intelligence
5. **SnailSploit/Claude-Red**：LLM 红队技能库，GitHub 热榜，约 8K 星。
   - X 原帖：https://x.com/nexbit_art/status/2114051206880629118 ｜ https://x.com/Yance16z/status/2113825608669241358
   - GitHub：https://github.com/SnailSploit/Claude-Red
6. **NVIDIA/OpenShell**：AI agent 隔离运行时，GitHub 日榜，一天涨 1119 星。
   - X 原帖：https://x.com/EricYua28626524/status/2113811297821458768
   - GitHub：https://github.com/NVIDIA/OpenShell
7. **ioncodes/wii-exploits**：@layle_ctf 发布的两个 Wii 游戏漏洞利用及 writeup，属研究性质。
   - X 原帖：https://x.com/layle_ctf/status/2114013212601655559
   - GitHub：https://github.com/ioncodes/wii-exploits
   - 文章：https://layle.me/posts/another-code-r/ ｜ https://layle.me/posts/ffcc-crystal-bearers/
8. **artex-ko-plus**：ARTEX 新变种仓库，与昨日 Storm-0940／ARTEX 相关，请谨慎对待。
   - X 原帖：https://x.com/Dinosn/status/2113840145447215603
   - GitHub：https://github.com/bdg9412/artex-ko-plus
9. **0x4D31/honeypot-data**：PHP2Shell 蜜罐证据报告，见 CVE 第 1 条。
   - GitHub：https://github.com/0x4D31/honeypot-data/tree/main/reports/php2shell

## APT / Malware 分析

### 1. LiteLLM 1.107.0 供应链投毒：根因公布
- **谁／打什么**：
  - 2026-05-27，配置文件被提交到公开仓库 LiteLLM-Labs/lite-harness，里面含有 Agent Platform 的 master key；当时 force-push 覆盖了提交，但**这把 key 没有吊销**
  - 10-10：攻击者（69.48.229[.]143）用这把 key 进入 Agent Platform，取出未限权的 GitHub owner OAuth token，又借 workflow 和 webhook[.]site 窃取两名维护者的 token
  - 10-21：绕过分支保护，把发布源指向仿冒仓库 `Berri-AI/litellm`，08:39（UTC-3）发布 PyPI 1.107.0，随后推送 Docker Hub 和 GHCR 镜像，并删除运行记录
  - 暴露时长：PyPI 约 1h45，Docker 约 2h30（@justabreach）
  - 恶意代码在 Python 启动时触发，**不需要 import**（@DFIR_Radar）
- **补丁／缓解**：确认环境中没有 1.107.0；在**干净的主机上**轮换所有可能接触过的密钥（LLM 供应商 key、云凭据、CI token）。组织层面：泄露的密钥必须吊销，OAuth token 要按最小权限限定范围。
- **狩猎**：
  - site-packages 中可疑的 `.pth` 文件
  - CI 日志里 10-21 拉取过 1.107.0 的记录
  - 访问 webhook[.]site 的流量
  - GitHub 审计日志中来自 69.48.229[.]143 的操作
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2113951301059113271 ｜ https://x.com/DFIR_Radar/status/2113965185933169006 ｜ https://x.com/justabreach/status/2114104694951846267
  - 文章·PDF：https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html ｜ https://www.securityweek.com/litellm-compromised-in-fresh-supply-chain-attack/
  - IoC：69.48.229[.]143；仿冒仓库 `Berri-AI/litellm`；恶意版本 litellm==1.107.0（PyPI、Docker Hub、GHCR）

### 2. BlackX UEFI bootkit（APT41）
- **谁／打什么**：疑似 APT41，目标是中亚外交机构。利用 Baton Drop（CVE-2022-21894），在已打补丁、但没有完成 DBX 手动吊销的系统上绕过 Secure Boot。
- **补丁／缓解**：按微软 BlackLotus 指引完成 DBX 更新，吊销「Windows Production PCA 2011」证书。
- 地址：
  - X 原帖：https://x.com/BleepinComputer/status/2113998497686908960 ｜ https://x.com/DFIR_Radar/status/2114010209031000442 ｜ https://x.com/_pksharma/status/2114001375772262615
  - 文章·PDF：https://www.bleepingcomputer.com/news/security/blackx-uefi-bootkit-exploits-baton-drop-flaw-to-bypass-secure-boot/
  - IoC：未见公开 IoC（X 帖内未列出）

### 3. Lazarus：用后量子密码（ML-KEM-1024）保护载荷投递和 C2
- 地址：
  - X 原帖：https://x.com/srinikatta/status/2114045370213052899
  - 文章·PDF：https://www.bleepingcomputer.com/news/security/lazarus-hackers-use-post-quantum-cryptography-for-malware-delivery/
  - IoC：未见公开 IoC

### 4. APT37：新增气隙网络渗透能力（Zscaler）
- 地址：
  - X 原帖：https://x.com/JustWantToQ1/status/2114092567792890185
  - 文章·PDF：https://www.zscaler.com/blogs/security-research/apt37-adds-new-capabilities-air-gapped-networks
  - IoC：未见公开 IoC（X 帖内未列出，详见 Zscaler 原文）

### 5. MuddyWater 冒充 Chaos 勒索做假旗
- **谁／打什么**：后门 Darkcomp，C2 为 moonzonet[.]com，代码签名主体为 "Donald Gay"（@JeskoRiot）。归因来自单一来源，**UNCONFIRMED**。
- 地址：
  - X 原帖：https://x.com/JeskoRiot/status/2113996936088846651
  - IoC：moonzonet[.]com；签名者 "Donald Gay"

### 6. UCreator：基于虚拟化的 Android 间谍平台（0x0v1）
- **谁／打什么**：借虚拟化容器窃取微信、Telegram 等通讯应用的数据。
- 地址：
  - X 原帖：https://x.com/0x0v1/status/2114116833552846996
  - 文章·PDF：https://www.0x0v1.com/ucreator-virtualization-based-android-spyware-platform-targeting-wechat-telegram-and-other-messaging-apps/
  - VT：https://www.virustotal.com/gui/url/80d91e50010be215b8ab3a6ec9160fff946be10eb4b00e8e6344674cc0132a7d/content
  - IoC：VT URL 对象 80d91e50010be215b8ab3a6ec9160fff946be10eb4b00e8e6344674cc0132a7d；其余见原文

### 7. AtlasRAT／ValleyRAT：伪造 fe2.update.microsoft.com 的 TLS 证书
- **狩猎**：TLS 证书的 CN／SAN 是微软更新域名，但目标 IP 不属于微软 ASN。
- 地址：
  - X 原帖：https://x.com/threadlinqs/status/2114125927441711284
  - 文章：https://intel.threadlinqs.com/threat/TL-2026-4419?utm_source=x
  - IoC：伪造证书主题 fe2.update.microsoft.com（其余见原文）

### 8. S3 上的 CobaltStrike＋TigerRAT 压缩包（malwrhunterteam）
- **谁／打什么**：S3 桶 share-adminsimple 上放着 AS-2026-1048.zip，内含 CobaltStrike 和 TigerRAT（TigerRAT 通常与 Andariel／Lazarus 关联，**本例归因 UNCONFIRMED**）。@skocherhan 补充了构建环境指纹。
- 地址：
  - X 原帖：https://x.com/malwrhunterteam/status/2114073233796337896 ｜ https://x.com/skocherhan/status/2114076037952717269
  - 样本：https://bazaar.abuse.ch/sample/2e2612d964aaf92e7b57bccab58349518bcdfd3a3f07e1c70a71f4f6f6fef16c/
  - IoC：见汇总表

### 9. 流媒体重定向集群（Malwarehunterr）
- **谁／打什么**：63 个使用同一模板的 streamb*／stream*[.]cyou 域名，点击视频后依次跳转到 werefilledwit[.]org、mediagetapp[.]com/mget-2-en/，最后投放 MediaGet.exe。作者注明**该文件的恶意分类尚待确认**。
- 地址：
  - X 原帖：https://x.com/Malwarehunterr/status/2114021415678832768
  - IoC：见汇总表

### 10. 其他 IoC 猎人线索
- cyuop[.]com／104.194.133[.]95 及相关 ISO 样本：https://x.com/malwrhunterteam/status/2113950715156877642 ｜ https://x.com/smica83/status/2114093728046494057 ｜ https://bazaar.abuse.ch/browse/tag/cyuop-com/
- MSI 样本：https://x.com/smica83/status/2114043849228063068
- SliverC2 IP：https://x.com/orlof_v/status/2114040446808736010 ｜ https://github.com/orlofv/Indicators/blob/main/SliverC2
- Meduza 开放目录：https://x.com/DunstableToble1/status/2114023413811744855
- 针对巴基斯坦的 Python RAT（trycloudflare C2）：https://x.com/G60930953/status/2113926735431610824
- RAT 面板：https://x.com/Fact_Finder03/status/2113918670502322295
- 可疑域名与主机名：https://x.com/skocherhan/status/2114105128890331168 ｜ https://x.com/skocherhan/status/2114095062975943141 ｜ https://x.com/skocherhan/status/2114089648276250740
- Hybrid Analysis 样本：https://hybrid-analysis.com/sample/8a8100572d7375dc1a342c77da5a6f85271a0d6f0cce0af31c5246ceddeece8c

### 11. Popcorn Time 遗留更新器（Eye Security「Operation IXIM」）
- **谁／打什么**：Time4Popcorn 的 Updater.exe 一直连接一个已过期的域名，谁注册这个域名，谁就能以 SYSTEM／root 权限下发代码。Eye Security 注册了该域名，在 2025-11 至 2026-03 期间推送 200 多万次更新，关停了这个更新器。估计影响 250–300 万台 Windows 和 25–35 万台 Mac。
- 地址：
  - X 原帖：https://x.com/TheHackersNews/status/2113919839735844959
  - 文章·PDF：https://thehackernews.com/2026/10/researchers-push-over-2-million-updates.html
  - IoC：未见公开 IoC（域名见原文）

## 地址／IoC 汇总

> 全部原样抄自原帖或报告，仅做去武器化处理。下列指标**只用于狩猎和封堵**，不代表已确认恶意，请结合上下文判断。

| 类型 | 指标 | 关联 | 来源 |
|---|---|---|---|
| IPv4 | 15.204.59[.]70（回连 :8081） | PHP2Shell 蜜罐确认 RCE，Episode A（OVH） | https://github.com/0x4D31/honeypot-data/blob/main/reports/php2shell/2026-10-24-confirmed-rce.md |
| IPv4 | 162.35.99[.]94（回连 :8080／:80） | PHP2Shell 蜜罐确认 RCE，Episode B（Interserver） | 同上 |
| IPv4 | 104.28.208[.]84、144.48.4[.]242 | PHP2Shell 尝试，未确认 RCE | 同上 |
| IPv4 | 69.48.229[.]143 | LiteLLM 攻击者 | https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html |
| 仓库 | Berri-AI/litellm（仿冒） | LiteLLM 发布流水线被篡改 | 同上 |
| 包 | litellm==1.107.0 | 恶意版本（PyPI、Docker Hub、GHCR） | https://x.com/justabreach/status/2114104694951846267 |
| IPv4 | 74.82.197[.]86、38.54.50[.]151 | Arista VCO 114625 攻击源 | https://x.com/2Workly/status/2113899924249268451 |
| 域名 | moonzonet[.]com | MuddyWater Darkcomp C2（假旗 Chaos） | https://x.com/JeskoRiot/status/2113996936088846651 |
| 签名者 | "Donald Gay" | MuddyWater 代码签名 | 同上 |
| URL | hxxps://share-adminsimple.s3.eu-west-2.amazonaws[.]com/October2026/AS-2026-1048.zip?utm_source=chatgpt.com | CobaltStrike＋TigerRAT 压缩包 | https://x.com/malwrhunterteam/status/2114073233796337896 |
| SHA256 | 2e2612d964aaf92e7b57bccab58349518bcdfd3a3f07e1c70a71f4f6f6fef16c | 同上（Bazaar） | https://bazaar.abuse.ch/sample/2e2612d964aaf92e7b57bccab58349518bcdfd3a3f07e1c70a71f4f6f6fef16c/ |
| 主机指纹 | MAC 00:0c:29:f1:2a:62；machine id castelblack | 同上的构建环境 | https://x.com/skocherhan/status/2114076037952717269 |
| 域名／IPv4 | cyuop[.]com、104.194.133[.]95 | 恶意 ISO 分发 | https://x.com/malwrhunterteam/status/2113950715156877642 |
| SHA256 | 838f3f24867b7ec93a6ad13c225b50f34959e7ed558175f9bc1be2a62337e7b7 | MSI 样本，来源 hxxp://23.94.145(.)201/61844 | https://x.com/smica83/status/2114043849228063068 |
| 域名 | torchpanel[.]duckdns[.]org | 可疑面板 | https://x.com/skocherhan/status/2114105128890331168 |
| 域名 | hellowtest[.]ru | 可疑 | https://x.com/skocherhan/status/2114095062975943141 |
| 主机名 | WIN-OKK4OGP4LT7 | 待识别 | https://x.com/skocherhan/status/2114089648276250740 |
| SHA256 | d02e2f6c2ef750d5e93910f371c2e874f6b96d407a65fba87f7718f23eba9a59 | MediaGet.exe（分类待确认） | https://x.com/Malwarehunterr/status/2114021415678832768 |
| 域名 | werefilledwit[.]org、mediagetapp[.]com/mget-2-en/ | 流媒体重定向链 | 同上 |
| favicon 哈希 | 015d656140983c33965fef9b6893127e15da222d06a8b3ab216b70599c17ccd9 | 流媒体模板 | 同上 |
| 域名（63 个） | `streambambam[.]cyou`、`streambambino[.]cyou`、`streambanana[.]cyou`、`streambingo[.]cyou`、`streambingobop[.]cyou`、`streambiscuit[.]cyou`、`streambloop[.]cyou`、`streambobo[.]cyou`、`streambonbon[.]cyou`、`streambongozo[.]cyou`、`streamboop[.]cyou`、`streamboppo[.]cyou`、`streambork[.]cyou`、`streambubbles[.]cyou`、`streambubu[.]cyou`、`streamburrito[.]cyou`、`streamcheeky[.]cyou`、`streamchubby[.]cyou`、`streamchurro[.]cyou`、`streamcoconut[.]cyou`、`streamdingdong[.]cyou`、`streamdizzy[.]cyou`、`streamdoodle[.]cyou`、`streamducky[.]cyou`、`streamdude[.]cyou`、`streamdumpling[.]cyou`、`streameasts[.]cyou`、`streamgiggle[.]cyou`、`streamgizmo[.]cyou`、`streamgoblin[.]cyou`、`streamgoofy[.]cyou`、`streamjuju[.]cyou`、`streamketchup[.]cyou`、`streamkiki[.]cyou`、`streamking[.]cyou`、`streammuffin[.]cyou`、`streammunch[.]cyou`、`streammuppet[.]cyou`、`streamnibbles[.]cyou`、`streamnono[.]cyou`、`streamnoodle[.]cyou`、`streamnugget[.]cyou`、`streampickle[.]cyou`、`streampipo[.]cyou`、`streampompom[.]cyou`、`streampookie[.]cyou`、`streampudding[.]cyou`、`streampuff[.]cyou`、`streampunky[.]cyou`、`streamsnappy[.]cyou`、`streamsnickers[.]cyou`、`streamson[.]cyou`、`streamsquid[.]cyou`、`streamtater[.]cyou`、`streamtonton[.]cyou`、`streamtutu[.]cyou`、`streamwaffle[.]cyou`、`streamwawa[.]cyou`、`streamwiggle[.]cyou`、`streamwobble[.]cyou`、`streamyoyo[.]cyou`、`streamzippy[.]cyou`、`streamzuzu[.]cyou` | 流媒体重定向集群 | 同上 |
| IPv4 | 151.245.121[.]241、168.138.40[.]244、185.193.125[.]201 | SliverC2 | https://github.com/orlofv/Indicators/blob/main/SliverC2 |
| URL／IPv4 | hxxp://104.238.140[.]55/；SOCKS5 45.63.50[.]164:443 | 开放目录（含 Meduza） | https://x.com/DunstableToble1/status/2114023413811744855 |
| 域名 | bathroom-sheriff-lat-alcohol.trycloudflare[.]com | 针对巴基斯坦的 Python RAT C2 | https://x.com/G60930953/status/2113926735431610824 |
| MD5 | 052d3ac9f896fa2823d3f0cbcccc2e48 | 同上 | 同上 |
| IPv4／域名 | 64.224.17[.]108:10000、149.33.8[.]214、c2.bigboxotulet[.]com、cdmx[.]group | RAT 面板 | https://x.com/Fact_Finder03/status/2113918670502322295 |
| SHA256 | 8a8100572d7375dc1a342c77da5a6f85271a0d6f0cce0af31c5246ceddeece8c | Hybrid Analysis 样本 | https://hybrid-analysis.com/sample/8a8100572d7375dc1a342c77da5a6f85271a0d6f0cce0af31c5246ceddeece8c |
| 证书 | 伪造 fe2.update.microsoft.com | AtlasRAT／ValleyRAT | https://x.com/threadlinqs/status/2114125927441711284 |
| 链上地址 | 0x358eF0130f7A5aA516dCd81Bdc80B18CdE41CAC8 | Initia 被盗资金归集 | https://x.com/blockscout/status/2113813735039230078 |
| 命令标记 | ==SHELLUSER==、==PASSWD== | PHP2Shell 后渗透中的 agentic 攻击者特征 | https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/ |

以下条目**未见公开 IoC**：PHP 115560、FortiSIEM 106173、Brotli、NGINX、ZDI-CAN-33367、YOOtheme、Postiz、jxrlib、BlackX、Lazarus ML-KEM、APT37（指标在 Zscaler 原文中，X 帖内未列出）、CYFIRMA DPRK（帖称有 IoC 但未列出）。


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

### 本日交叉情况
- **LWiS X List**：500 名成员分 10 段做 `from:` 查询（共 10 次读取，各段分别返回 10／11／10／25／11／25／5／10／25／25 条，共 157 条）。按关键词粗筛，安全相关的有 **45** 条，主要包括：
  - PHP2Shell 讨论：@domchell 引 CrowdStrike，@LiveOverflow 和 @i0n1c 发表看法
  - @ipurple 介绍 TornadoC2
  - @PedroGabaldon 的 WhatAboutSAM 新增 WRITE_DAC 路径
  - @layle_ctf 的 Wii 漏洞研究
  - @MSNightmare2000：Defender 与 WebDAV
  - @Dinosn 的大量转发：ARTEX 变种、redteam-bofs、BlackX、LiteLLM、Brotli、Popcorn Time
  - @AlmaLinux 的 ZDI-CAN-33367
  - malwrhunterteam、smica83 的 IoC

  其余大多是闲聊、回复和会议宣传，已剔除。
- **blogs.txt 高信号源**：本日交叉核对了 CrowdStrike（PHP2Shell 武器化障碍，10-23）、Unit 42（PHP 简报）、Zscaler（APT37）和 CYFIRMA（DPRK／PHP2Shell）。Kaspersky 的 BlackX 原报告没有直接抓取，以 BleepingComputer／DFIR_Radar 的转述为准。
- **Risky Business**：RSS 最新一期仍是 **#856「8-bit encryption, PHP megabugs and more」**（10-21 01:43 UTC-3 发布，早于本窗口），本日没有新一期：https://risky.biz/
- **tl;dr sec**：首页可以访问，但只抓到旧的 `/p/` 文章，**无法确认**本窗口内有没有新一期：https://tldrsec.com/
- **结论**：今天的重点（0x4D31 蜜罐 RCE、CrowdStrike／Unit 42 的分歧、LiteLLM 根因、FortiSIEM 第二个 PoC、ZDI-CAN-33367、BlackX、IoC 猎人线索）**都先在 X Latest 上出现**，公开信源只用来核对版本号、IP、日期和 KEV 状态。

## 来源搜索 URL

- X 只读接口查询（下列为等价的 X 网页搜索 URL，便于人工复核；实际用接口 `search_posts_all` 执行，`start_time=2026-10-23T23:13:00Z`）：
  - A 类：https://x.com/search?q=(CVE-2026%20OR%20CVE-2025%20OR%200day%20OR%20zero-day)%20(exploit%20OR%20exploited%20OR%20PoC%20OR%20RCE%20OR%20patch%20OR%20KEV)%20-is%3Aretweet&f=live
  - B 类：https://x.com/search?q=url%3Agithub.com%20(C2%20OR%20%22red%20team%22%20OR%20redteam%20OR%20BOF%20OR%20EDR%20OR%20nuclei)%20-is%3Aretweet&f=live
  - C 类：https://x.com/search?q=(%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22)%20-is%3Aretweet&f=live
  - LWiS List：https://x.com/i/lists/1239330068461244424
  - 专题 PHP2Shell／115560：https://x.com/search?q=(php2shell%20OR%20CVE-2026-109618%20OR%20CVE-2026-115560)%20-is%3Aretweet&f=live
  - 专题 Brotli：https://x.com/search?q=(CVE-2026-111497%20OR%20brotli)%20-is%3Aretweet&f=live
  - 专题 LiteLLM：https://x.com/search?q=litellm%20-is%3Aretweet&f=live
  - IoC 猎人：https://x.com/search?q=(from%3Amalwrhunterteam%20OR%20from%3Asmica83%20OR%20from%3Askocherhan)&f=live
- 公开备援：
  - CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - CISA KEV 页：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  - CISA PHP 警报：https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching
  - NVD：https://nvd.nist.gov/vuln/search
  - nginx 安全公告：https://nginx.org/en/security_advisories.html
  - Unit 42 PHP 简报：https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
  - CrowdStrike：https://www.crowdstrike.com/en-us/blog/obstacles-to-weaponizing-php2shell-likely-constrain-exploitation/
  - AlmaLinux：https://almalinux.org/blog/2026-10-23-zdi-can-33367/
  - LWiS blogs.txt：https://blog.badsectorlabs.com/files/blogs.txt
  - Risky Business：https://risky.biz/
  - tl;dr sec：https://tldrsec.com/
