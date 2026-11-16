# X 安全情报晚报 · 2026-11-13（周五）

> 报告时间：2026-11-13 约 20:30（America/Santiago），即 2026-11-14 约 07:30（香港时间）。
> **覆盖时长**：X 只读窗口为 2026-11-12 22:55 UTC 到 11-13 22:55 UTC（24 小时）。各组覆盖情况：
> - CVE 组 Latest 25 条只覆盖 11-13 21:50～22:51 UTC（约 1 小时），所以加了 relevancy 补搜 25 条（11-12 22:58～11-13 20:34）和「在野利用」组 25 条（11-13 03:42～22:00）。
> - 工具组（github.com + C2/红队）Latest 只有 2 条，且与安全工具无关，所以工具节主要靠 LWiS List。
> - 威胁组 Latest 25 条（11-13 18:16～22:52）加 relevancy 25 条（11-13 00:51～21:49）。
> - LWiS X List 翻了 4 页共 369 帖，其中 215 帖在窗口内（11-12 22:55～11-13 22:52 UTC），覆盖完整 24 小时。
>
> **新信源**：pwn.watch 订阅源最后生成于 2026-11-08 20:19 UTC，**本窗口 0 条新事件**。ExploitGrid 本窗口新增 2 条 exploit，都是老 CVE 的重复 PoC（CVE-2018-4990、CVE-2017-7494），只计数不展开。另外对今天的 6 个 CVE 按编号查询，结果只有 WordPress CVE-2026-119977 有 9 条公开 exploit 收录。
> **CISA KEV**：目录版本 2026.11.13，**11-13 新增 2 条：Check Point CVE-2026-123039、UnrealIRCd CVE-2026-114713，联邦修补期限都是 11-16**。
> 本期是工作日版（十个小节），不加阮一峰周刊节。11-07 那期周六版已经收录周刊，不需要补。

## 今日摘要

- **Check Point Gaia 提权 0day CVE-2026-123039 进入 KEV（期限 11-16）**：已被在野利用。攻击者先用 PHP2Shell（CVE-2026-109618/109619）打 Mobile Access 门户拿到初始访问，再用 DynamicCLI 的全局可写本地 socket 提权到 root，然后植入 PHP webshell 和 TSGA/TSProxy（PhiliKit 家族）后门。有受害者被横向到 ESXi 并投放 destroy_v6 擦除器。Check Point 已发布 November Jumbo Hotfix（sk1000362），CPR 公开了 IoC。
- **UnrealIRCd CVE-2026-114713 进入 KEV（期限 11-16）**：问题出在 labeled-response 模块。在两台及以上互联服务器的网络中，任意用户都能注入服务器间命令。修复方式是升级到 6.2.7.1 或打 hot-patch。
- **未修补、已被利用的 WordPress 插件 WP Duplicate CVE-2026-123751**（CVSS 9.8，未认证任意文件上传可导致 RCE，目前没有修复），应立即删除该插件。另有 **Tactical RMM CVE-2026-129165**（CVSS 9.4）：拥有报表权限的用户可读取 Django SECRET_KEY，而这个密钥被复用为 NATS 密码，可借此控制所有受管 agent。**Red Hat Quay CVE-2026-123710**（CVSS 9.8）可读写所有私有镜像。
- **威胁研究**：Kaspersky Securelist 发布 ESXi/vCenter 勒索专题（BlackNevas 等），Elastic 披露 CyberStrikeAI（LLM agent 加攻击工具）首次被用于 AWS 入侵，Enea 披露新国家级组织 SilentAir 从被控运营商节点拦截台湾用户的通话和短信验证码。FBI 发布 FLASH，称朝鲜「FaceStealer」用伪造视频会议窃取超过 4 亿美元加密货币。微软研究院的「Lazarus」研究表明，只改不到 10 个神经元就能在开源权重模型里植入 agent 后门。
- **政策与工具**：Google Project Zero 发布 2026 版披露政策，原因是 AI 让「补丁发布到被利用」的时间趋近于零。ZDI 一次公开 56 个漏洞公告，其中有 Pwn2Own 的 OpenAI Codex GUI、Philips Hue 等，另有 llama.cpp GGUF 和 Linux KSMBD 远程 RCE。PingCastle 4.1.2.0 新增了 AD 检查项。

## CVE / POC / 漏洞（每条：说明 + 地址列表；合并 X、KEV、pwn.watch、ExploitGrid 的补丁状态与公开 exploit 情况）

**1. Check Point Gaia OS 本地提权 CVE-2026-123039：已被在野利用，11-13 进入 KEV，期限 11-16**
- 谁／什么：Gaia OS 的 DynamicCLI 守护进程以 root 运行，监听一个全局可写的本地 socket，且不对连接进程做认证，所以已登录的本地用户可以让它以 root 执行命令。影响 Firewall、Security Gateway、Security Management Server、Multi-Domain、Scalable Platforms（Gaia R82.20、R82.10、R82、R81.20 等）。
- 在野利用链（CPR）：从 10-30 起，攻击者用 PHP2Shell（CVE-2026-109618/109619）打未修补的 Mobile Access 门户，然后用本漏洞提权到 root，在门户模板目录写入 zz*.tpl webshell，再部署持久化后门 TSGA 和内嵌的 TSProxy。部分以色列目标被横向到 VMware ESXi，被投放 destroy_v6 擦除器，并留下 DREAM_ANNEXATION.txt。11-02 的第二波扫描范围扩大到多个国家，没有发现破坏行为。TSGA/TSProxy 是 PhiliKit 的变种（ESET 曾把 PhiliKit 关联到 UNC5221），但 CPR 表示不能高置信度归因，也不排除假旗。
- 补丁与公开 exploit：安装 November Jumbo Hotfix（sk1000362；X 上有人列出 R82.20 T14+、R82.10 T52+ 等版本），同时修补 PHP2Shell。ExploitGrid 按 CVE 查询为 0 条公开 exploit；pwn.watch 本窗口无条目。
- 狩猎：检查 /opt/CPcvpn-*/tmp/ 下带 upload_progress_pwn 标记的 PHP 会话文件，以及门户模板目录里是否多出 zz*.tpl。IoC 见「地址／IoC 汇总」。
- X 原帖：[DailyCyberNews_](https://x.com/DailyCyberNews_/status/2121374990260138049) · [BursaMatus（修复版本）](https://x.com/BursaMatus/status/2121270568456749316) · [SockAnalystHQ](https://x.com/SockAnalystHQ/status/2121231731755811000) · [yogsec（socket 细节）](https://x.com/yogsec/status/2121231468815110639) · [EnclaveRadar](https://x.com/EnclaveRadar/status/2121317403837538769) · [yabetchi_iPhone（日文汇总）](https://x.com/yabetchi_iPhone/status/2121375332620230918)
- 厂商公告：[Check Point sk1000362](https://support.checkpoint.com/results/sk/sk1000362) · [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-123039) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-123039)
- 文章／PDF：[Check Point Research：PHP2Shell Exploitation on Check Point Gateway](https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/) · [ExploitGrid CVE 页](https://exploitgrid.net/vulnerabilities/CVE-2026-123039) · [Cloudflare：php2shell 防护说明](https://blog.cloudflare.com/php-vulnerabilities-waf-protection/)

**2. UnrealIRCd labeled-response 分隔符注入 CVE-2026-114713：11-13 进入 KEV，期限 11-16**
- 谁／什么：影响 UnrealIRCd 6.0.0～6.2.7。在两台及以上互联服务器的网络中，任何用户都能借 IRCv3 label 标签注入服务器间（S2S）命令，并以服务器权限执行。CVSS 8.6。
- 补丁：升级到 6.2.7.1，或打官方 hot-patch-bundle-20261107。6.0.4 及以上版本的网络可以临时用 spamfilter 规则缓解。可以用 `./unrealircd module-status` 确认 labeled-response 模块的状态。ExploitGrid 为 0 条公开 exploit。
- X 原帖：[junli_sec8（自查方法）](https://x.com/junli_sec8/status/2121371289088672188) · [EnclaveRadar](https://x.com/EnclaveRadar/status/2121317405066461670) · [threatpodium](https://x.com/threatpodium/status/2121374907087061431)
- 厂商公告：[UnrealIRCd 论坛公告 t=9487](https://forums.unrealircd.org/viewtopic.php?t=9487)（box 直连返回 403，换 UA 并加 Referer 后仍是 403；浏览器可以打开）· [GitHub Advisory GHSA-237f-p9h6-wq4r](https://github.com/advisories/GHSA-237f-p9h6-wq4r) · [CCB Belgium 预警](https://ccb.belgium.be/advisories/warning-actively-exploited-cve-2026-114713-affects-unrealircd-patch-immediately)（box 返回 403，浏览器可开） · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-114713)
- 文章：[ExploitGrid CVE 页](https://exploitgrid.net/vulnerabilities/CVE-2026-114713)

**3. WP Duplicate（原 LocalSync）未认证任意文件上传 CVE-2026-123751：已被利用，没有修复**
- 谁／什么：影响 1.1.11 及更早版本。插件没有正确校验请求认证值，也不校验上传路径和文件类型，可直接导致 RCE，CVSS 9.8。WPScan 标注为在野利用，但没有公布 IoC。同一插件还有需订阅者权限的上传漏洞 CVE-2026-39755，同样没有修复。安装量约 200。不在 CISA KEV，ExploitGrid 为 0 条。
- 处置：停用并删除插件；检查 uploads 和插件目录是否有异常 PHP 文件，排查是否有陌生管理员账号。
- X 原帖：[ksanjeev284](https://x.com/ksanjeev284/status/2121279537065644156)
- 厂商／漏洞库：[NVD](https://nvd.nist.gov/vuln/detail/cve-2026-123751)
- 文章：[SecurityOnline](https://securityonline.info/wp-duplicate-vulnerability-cve-2026-123751-exploited/)（box 上 TLS 连接被断开，内容经搜索索引确认） · [IONIX](https://www.ionix.io/threat-center/cve-2026-123751/)

**4. Tactical RMM 报表预览任意文件读取 CVE-2026-129165（CVSS 9.4，可影响所有受管 agent）**
- 谁／什么：影响 0.17.0～1.6.1。WeasyPrint 会解析报表模板里的 file:// 链接，导致可以读取服务器文件。拥有 report management 权限的用户能读到 Django SECRET_KEY，而它同时是 NATS 密码，拿到后可以向每个受管 agent 发布 runscript 命令。NVD 于 11-13 发布，不在 KEV。
- 处置：升级到 1.6.1 之后的版本；收紧报表管理权限；轮换 SECRET_KEY 和 NATS 密码。
- X 原帖：[ICHI_Global](https://x.com/ICHI_Global/status/2121363588288045528)
- 公告：[VulnCheck 公告](https://www.vulncheck.com/advisories/tactical-rmm-0.17.0-through-1.6.1-arbitrary-file-read-via-report-preview) · [NVD](https://nvd.nist.gov/vuln/detail/cve-2026-129165)
- 文章：[Rapid7 漏洞库](https://www.rapid7.com/db/vulnerabilities/cve-2026-129165/)

**5. Red Hat Quay 签名密钥注入 CVE-2026-123710（CVSS 9.8）**
- 谁／什么：攻击者能把自己的密钥加进 Quay 的信任密钥，且不会过期，之后就能读取、覆盖所有仓库的私有镜像（包括镜像里的密钥和凭据），还能删除正常密钥让推送和拉取失败。默认开启匿名访问时不需要账号。Red Hat 已为 8 个 Quay 3 分支发布修复。
- 处置：升级；关闭匿名访问；审计密钥服务器里的异常密钥，以及近期被覆盖的镜像。
- X 原帖：[Dinosn 转 THN](https://x.com/Dinosn/status/2121033854677143616)
- 文章：[The Hacker News](https://thehackernews.com/2026/11/critical-red-hat-quay-flaw-lets.html)

**6. WordPress Core 升级窗口竞争条件 RCE CVE-2026-119977（来源：SecureFlow／先知；ExploitGrid 已有公开 exploit）**
- 谁／什么：影响 4.7～7.1.3 各分支。完整包升级时，会在 wp-content/upgrade/ 下生成路径可预测、可从 Web 访问的临时目录，里面带有 setup-config.php，未认证攻击者可在升级窗口内竞争写入配置实现 RCE（CVSS 8.1，攻击复杂度高）。先知社区文章引用的测绘数据称全球关联资产约 122 万。
- 公开 exploit：ExploitGrid 按 CVE 查询有 **9 条公开 exploit 收录**（[ExploitGrid CVE 页](https://exploitgrid.net/vulnerabilities/CVE-2026-119977)）。这里不链 PoC 仓库。
- 处置：升级到各分支的最新安全版本；禁止 Web 访问 wp-content/upgrade/；尽量在维护窗口内手动升级。
- 文章：[先知社区分析](https://xz.aliyun.com/news/93320) · [CVE 记录](https://www.cve.org/CVERecord?id=CVE-2026-119977)

**7. Control Web Panel 两个严重漏洞 CVE-2026-124021 / CVE-2026-124020（CVSS 9.2）**
- 谁／什么：CWP 低于 webpanel_version 1.30.6 的版本，validate() 存在授权绕过（124021），还存在 Host 头注入导致的密码重置投毒（124020），都可远程、无需登录。修复版本为 1.30.6。
- X 原帖：[EnclaveRadar（124021）](https://x.com/EnclaveRadar/status/2121368954585198751) · [EnclaveRadar（124020）](https://x.com/EnclaveRadar/status/2121368953607823678)
- 文章：[Enclave 威胁条目](https://app.enclave.ai/threat-feed/CVE-2026-124021) · [NVD 124021](https://nvd.nist.gov/vuln/detail/CVE-2026-124021) · [NVD 124020](https://nvd.nist.gov/vuln/detail/CVE-2026-124020)

**8. rConfig 未授权反序列化 RCE CVE-2026-124079（来源：SecureFlow／先知）**
- 谁／什么：rConfig ≤ 8.2.17 依赖 Laravel Horizon 加 Redis。只要 Redis 端口可以访问，就能向队列投递恶意序列化对象并执行命令。8.2.18 为缓解修复，8.2.19 为根因修复。rConfig 里存有大量网络设备凭据。
- 处置：升级到 8.2.19；Redis 只监听本机并加认证；轮换 NCM 中保存的设备凭据。
- 文章：[先知社区分析](https://xz.aliyun.com/news/93271) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-124079)

**9. HPE ArubaOS AOS-10 未认证 PAPI 命令注入 CVE-2026-79861（严重）**
- 谁／什么：X 上的 ZoomEye 机器人称全球约有 210 个暴露实例。请按 HPE Aruba 公告升级，并限制 PAPI（UDP 8211）只能从可信网段访问。
- X 原帖：[zoomeyebot](https://x.com/zoomeyebot/status/2121373880229212176)
- 公告：[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-79861)

**10. 微软 11 月更新改变 NTLM 签名默认值：HTTP 强制认证转发到 LDAP 的链路失效**
- 说明：decoder_it 指出，打了补丁的客户端默认会协商 SIGN+KEY_EXCH，所以通过 WebClient/WebDAV、IPP 发起的 HTTP 强制认证再转发到 LDAP 的老路线会失败，因为攻击者拿不到真实的会话密钥。蓝队可借这个时间点推进 LDAP 签名和通道绑定；仍有未打补丁的客户端时，风险依旧存在。
- X 原帖：[decoder_it](https://x.com/decoder_it/status/2121308199307661470)

**11. 往期跟进（简报）**
- Outlook 在野 0day CVE-2026-124194（KEV，期限 11-24）：X 上讨论仍在继续，CERT-In 发布 CIAD-2026-0059。[Lumideezy](https://x.com/Lumideezy/status/2121333043055006112) · [PaidFreeDroid（CERT-In）](https://x.com/PaidFreeDroid/status/2121323630357283318) · [ExploitGrid](https://exploitgrid.net/vulnerabilities/CVE-2026-124194)
- N-able N-central「4EverAble2Shell」：GreyNoise 上线利用监测看板，eSentire 也发了预警。[ImposeCost 看板（经 stvemillertime 转推）](https://x.com/stvemillertime/status/2121237397413519758) · [GreyNoise 看板](https://nable.events.greynoise.io/) · [eSentire](https://x.com/eSentire/status/2121339844798374052)
- 老漏洞出现新的公开 exploit：Wazuh CVE-2025-24016（升级到 4.9.1+）、Office CVE-2026-21509（KEV）。[infrastack_ai（Wazuh）](https://x.com/infrastack_ai/status/2121362543553937912) · [infrastack_ai（Office）](https://x.com/infrastack_ai/status/2121236443549057469)
- ExploitGrid 本窗口另有 2 条老 CVE 的重复 PoC 收录（CVE-2018-4990、CVE-2017-7494），只计数不展开。

## 工具与 GitHub 发布（每条：说明 + 地址列表）

1. **PingCastle 4.1.2.0（免费版新增 AD 检查项）**：Netwrix 发布，用于 AD 安全评估。
   - X 原帖：[DebugPrivilege](https://x.com/DebugPrivilege/status/2121303952507691128)
   - GitHub：https://github.com/netwrix/pingcastle/releases/tag/4.1.2.0
2. **appboundkatz**：用 Rust 移植 ElevationKatz，演示如何绕过 Chrome/Edge 的 App-Bound Encryption。防守方可以拿它验证 EDR 对浏览器凭据窃取的检测。
   - X 原帖：[ipurple](https://x.com/ipurple/status/2121228220645457999)
   - GitHub：https://github.com/Harrison-Wells-Cyber/appboundkatz
3. **CipherStrike**：勒索行为测试工具，可生成模拟数据、做目录加密和恢复演练，默认不做破坏性配置。适合验证勒索检测规则。
   - X 原帖：[ipurple](https://x.com/ipurple/status/2121151152993808480)
   - GitHub：https://github.com/Cursed271/CipherStrike
4. **idasignwriter**（crackinglandia）：IDA 签名相关工具。
   - X 原帖：[ilove2pwn_ 转推](https://x.com/ilove2pwn_/status/2121320467093168483)
   - GitHub：https://github.com/crackinglandia/idasignwriter
5. **Windows COM 入门与 CVE-2026-97793 解析**（yo-yo-yo-jbo）
   - X 原帖：[maxime_tz 转推](https://x.com/maxime_tz/status/2121152801187197150)
   - GitHub：https://github.com/yo-yo-yo-jbo/intro_to_com
6. **blackmagick-c2 更新**：新增 CDN 重定向器指南和视频教程（红队 C2）。
   - X 原帖：[Teach2Breach](https://x.com/Teach2Breach/status/2121341666124562700)
   - 站点：https://blackmagick.io
7. **Authlab 更新**：digininja 的靶场新增 3 种 JWT 弱点（Audience Bypass、JWK 校验失败、未校验 JKU），用于教学。
   - X 原帖：[digininja](https://x.com/digininja/status/2121265018150789618)
   - 站点：https://authlab.digi.ninja/
8. **MLOKit 新模块（攻击 MLOps 平台）**：将在 BurningRiverCon 上演讲。
   - X 原帖：[h4wkst3r](https://x.com/h4wkst3r/status/2121353657044398256)
9. **isa.layle.dev**：交互式查看指令集编码，已加入 NVIDIA GPU 和主机平台。
   - X 原帖：[layle_ctf](https://x.com/layle_ctf/status/2121337606432547271)
   - 站点：https://isa.layle.dev/
10. **SIFT Workstation 加 REMnux 合装指南**（DFIR 和恶意软件分析）
    - X 原帖：[lennyzeltser](https://x.com/lennyzeltser/status/2121329940490830170)
    - 文章：https://zeltser.com/sift-workstation-and-remnux
11. **Google Project Zero「Policy and Disclosure: 2026 Edition」**：P0 认为 AI 让补丁逆向和利用的时间趋近于零，原来「90+30」中的补丁缓冲期已经没有意义，要求厂商更快修复并缩短补丁到位时间（patch gap）。
    - X 原帖：[ProjectZeroBugs](https://x.com/ProjectZeroBugs/status/2121287397828952146)
    - 文章：https://projectzero.google/2026/11/disclosure-policy.html
12. **OpenAI Daybreak Red Team / Defense Factory（AI/TLDR security 条目，已合并到这里）**：Red Team 处于早期访问阶段，用 agent 对 Web 应用做渗透测试；Defense Factory 自动发现、验证并修复代码缺陷，生成 PR 交给工程师审批。X 上 nickvangilder 等人批评把它叫作「自动化红队」有误导性。
    - X 原帖：[nickvangilder](https://x.com/nickvangilder/status/2121332316630917274) · [Dinosn 转 The Register](https://x.com/Dinosn/status/2121034146265141492)
    - 文章：[AI/TLDR](https://ai-tldr.dev/releases/openai-daybreak-red-team-defense-factory/) · [CybersecurityNews](https://cybersecuritynews.com/openai-two-ai-cybersecurity-tools/) · [The Register](https://www.theregister.com/security/2026/11/12/openai-launches-security-products-tells-orgs-theyre-doomed-if-they-dont-use-them/5309500)

## APT / Malware 分析（每条：说明 + 地址列表）

1. **Check Point 网关被入侵后的 TSGA/TSProxy 加 ESXi 擦除器**（详见 CVE 节第 1 条）
   - 来源 IP 托管在 LightNode VPS 上；扫描集中在 00:00～09:00 UTC。CPR 给出 UNC5221 关联、初始访问中介、假旗等多种可能，没有定论。
   - 文章：https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/
2. **Kaspersky Securelist：勒索团伙转向虚拟化层（ESXi/vCenter）**
   - 说明：分析攻击者如何借 AD 集成、从 Windows 环境复用凭据、以备份设施为跳板拿到 vCenter，把 vCenter 当作攻击控制面，再用 Babuk 衍生的 ESXi 锁定器批量加密。涉及 BlackNevas、C0met、Babuk、ESXiArgs 等。另外，infrastack_ai 引述的 BlackNevas 案例中，攻击者没有用任何 VMware 漏洞，而是凭被盗凭据登录 vCenter，擦除了虚拟机和备份。
   - 防御：vCenter 和 ESXi 与域隔离，启用 MFA 和锁定模式，备份使用独立凭据并保留离线副本。
   - X 原帖：[rst_cloud](https://x.com/rst_cloud/status/2121371083391549675) · [infrastack_ai](https://x.com/infrastack_ai/status/2121177240159576341)
   - 文章：https://securelist.com/esxi-ransomware/121959/
3. **Elastic Security Labs：CyberStrikeAI 被用于 AWS 入侵**
   - 说明：9-30 到 10-16 期间，一台 CyberStrikeAI 服务器用 4 个账户中 8 个身份的被盗凭据，依次做身份校验、拉取 Secrets Manager、读取 EC2 user data（141 毫秒内 56 次）、解密 SSM 参数，并发出 SSM SendCommand，共触发 78 条中低危告警，期间有 14 天静默。Elastic 认为固定时间窗口的关联规则会漏掉这类攻击。
   - X 原帖：[SBousseaden](https://x.com/SBousseaden/status/2121242261849817222)
   - 文章：https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion
4. **Enea：SilentAir（新的国家级组织，与中国的关联为低置信度）劫持亚洲运营商节点**
   - 说明：攻击者从至少 6 个亚洲国家被控的运营商节点发起 SS7 和 Diameter 信令攻击，主要目标是台湾用户，可拦截通话和短信（包括 2FA 验证码），并大量发送静默短信。拦截类攻击占 18.3%。Enea 同时披露 LIMINAL PANDA 的 GTPDoor v3 把 C2 通信藏在 GTP-U 流量里。
   - X 原帖：[infrastack_ai](https://x.com/infrastack_ai/status/2121167317354865048)
   - 文章：[Enea 报告](https://www.enea.com/insights/the-enemy-within-tracking-liminal-panda-and-silentair-through-mobile-networks/) · [SecurityWeek](https://www.securityweek.com/silentair-hackers-intercept-calls-sms-from-inside-mobile-networks/) · [The Hacker News](https://thehackernews.com/2026/11/silentair-hijacks-asian-telecom.html)
5. **FBI FLASH：朝鲜「FaceStealer」用伪造视频会议实施盗窃**
   - 说明：FBI 归因于 Sapphire Sleet、UNC1069、BlueNoroff 等朝鲜团伙。他们用被劫持的 Telegram、LinkedIn、Slack、Discord 账号发出会议邀请，在仿冒的 Zoom/Teams/Meet 里播放前一个受害者的录像，再以「音频故障」为由诱导目标运行修复脚本，从而植入 cookie 窃取、键盘记录和后门。18 个月内窃取超过 4 亿美元，还曾尝试攻击开源供应链。
   - 防御：会议一律从官方客户端输入会议 ID 加入；会中出现的任何「修复」或终端命令都不要执行。
   - X 原帖：[infrastack_ai](https://x.com/infrastack_ai/status/2121258074967343432)
   - 厂商／官方：[FBI IC3 FLASH PDF](https://www.ic3.gov/CSA/2026/261112.pdf) · [FBI 专题页](https://www.fbi.gov/investigate/cyber/facestealer-cryptocurrency-theft-scheme)
   - 文章：[Help Net Security](https://www.helpnetsecurity.com/2026/11/13/fbi-north-korean-fake-zoom-calls/) · [BBC](https://www.bbc.com/news/articles/cqdj1ellpd70o)
6. **微软研究院「Lazarus」：改动不到 10 个神经元即可在开源权重模型中植入 agent 后门**
   - 说明：改动模型最后一层前馈网络里的休眠神经元，让它在特定触发条件下（例如日期跨入 2027 年）输出攻击者的命令，再由 agent 用自身权限执行。在 Nemotron-Terminal-8B 上只改了 7 个神经元，测试中触发率为 98.8%。微软威胁情报团队称尚未发现被实际利用。启示是：要校验模型权重的完整性，内部模型也不例外。
   - X 原帖：[koltregaskes2](https://x.com/koltregaskes2/status/2121370774099628209) · [OwenGregorian](https://x.com/OwenGregorian/status/2121362477006864413)
   - 文章：https://www.infoworld.com/article/4247378/rewriting-less-than-10-neurons-in-an-llm-can-turn-it-into-a-sleeper-backdoor-2.html
7. **其他 X 线索（未独立核实，只记录事实）**
   - Aviatrix 称 ARTEX agent 自动扫描暴露在公网的 LLM 网关，利用 CVE-2025-3248 窃取 API Key 来支付后续攻击费用：[aviatrixtrc](https://x.com/aviatrixtrc/status/2121362005407813780)
   - 有攻击者把 Latvia 的中转服务器完全暴露在公网，里面有 1 万多个窃取 Claude/OpenAI token 的文件（经 int20z 转推）：[int20z](https://x.com/int20z/status/2121286254084124955)
   - Trezor Safe 5 经销商 CryptoBilis 的设备被发现藏有蜂窝植入件，会外传助记词；Macfinger ClickFix 用伪造验证码页面诱导 Mac 用户粘贴终端命令，安装钱包窃取器：[infrastack_ai（Trezor）](https://x.com/infrastack_ai/status/2121247766127284537) · [infrastack_ai（Macfinger）](https://x.com/infrastack_ai/status/2121095928971174071)
   - 勒索受害者声明：丹麦邮政 MailMak 确认遭 The Gentlemen 勒索（[Comparitech](https://x.com/Comparitech/status/2121191605671690709)）；Wallstreet 声称攻击了 Walgreens（[FalconFeedsio](https://x.com/FalconFeedsio/status/2121306304648196571)）；Panzer 声称拿到 RE/MAX 德国 610GB 数据（[DailyDarkWeb](https://x.com/DailyDarkWeb/status/2121369589485347117)）；INC Ransom 声称攻击了 Sportsman's Guide（[FalconFeedsio](https://x.com/FalconFeedsio/status/2121288075515228418)）。以上都是团伙的单方面声明，未经证实。

## SecureFlow 信息流精选（X 上未出现的高信号条目，按 community／blog／BugBounty 分组）

**community（先知 6、Seebug 1；WordPress CVE-2026-119977 与 rConfig 已并入 CVE 节）**
- 先知社区：红队实战复盘，DollarTicket 加 SPN 劫持加 RBCD 桥接（AD 横向，蓝队可对照检测）：https://xz.aliyun.com/news/93281
- 先知社区：Fastjson 反序列化实战复盘，从黑盒 AutoType 探测到容器层面的利用边界：https://xz.aliyun.com/news/93279
- 先知社区：安卓安全基础，四大组件剖析：https://xz.aliyun.com/news/93278
- 先知社区：从一道反 AI 的 CTF 题中学习：https://xz.aliyun.com/news/93270
- Seebug Paper：面向移动 SQLite 数据库的上下文感知证据抽取（取证研究）：https://paper.seebug.org/3534 （核验时站点返回 521，源站暂时不可用；链接来自 SecureFlow）

**blog（ZDI-vulnerabilities 一次公开 56 条公告）**
- Pwn2Own：OpenAI Codex GUI OpenProjectInCodex 参数注入 RCE（ZDI-26-968）：https://www.zerodayinitiative.com/advisories/ZDI-26-968/
- Pwn2Own：Philips Hue Bridge HomeKit 5 个漏洞，含默认密码认证绕过和堆溢出 RCE（ZDI-26-962～966）：https://www.zerodayinitiative.com/advisories/ZDI-26-963/
- Pwn2Own：Qualcomm QCA7005 GreenPhy 堆溢出（ZDI-26-1008）、Synology DS925+ C2 Identity 插件信息泄露（ZDI-26-1009）：https://www.zerodayinitiative.com/advisories/ZDI-26-1008/ · https://www.zerodayinitiative.com/advisories/ZDI-26-1009/
- llama.cpp GGUF 和 MTMD 解析共 3 个 RCE（ZDI-26-954/975/976），llama.cpp 恰好在 11-13 发布了 v1.0.0：https://www.zerodayinitiative.com/advisories/ZDI-26-975/
- Linux 内核 10 条，包括 KSMBD SMB Direct 整数下溢远程 RCE（ZDI-26-998）和 eBPF、SCTP、Qdisc 等多个本地提权：https://www.zerodayinitiative.com/advisories/ZDI-26-998/
- SmarterMail 4 条，包括熵不足导致的认证绕过（ZDI-26-997）和文件编辑 API 目录穿越 RCE（ZDI-26-994）：https://www.zerodayinitiative.com/advisories/ZDI-26-997/
- 其他值得关注：Netgate pfSense CE XMLRPC 授权错误 RCE（ZDI-26-960）、Docker Agent read_skill 缺授权 RCE（ZDI-26-959）、Signal for Windows UI 警告不足 RCE（ZDI-26-971）、PostgreSQL pg_stat_statements 堆溢出（ZDI-26-974）、Windows 远程桌面客户端链接跟随 RCE（ZDI-26-967）、TrendAI Vision One 安全 agent 12 个本地提权：https://www.zerodayinitiative.com/advisories/ZDI-26-960/ · https://www.zerodayinitiative.com/advisories/ZDI-26-959/ · https://www.zerodayinitiative.com/advisories/ZDI-26-971/
- 其余 11 个个人和厂商博客（samcurry、projectdiscovery、ZDI-Blog、dirkjanm、leavesongs、brutecat 等）7 天内没有首次出现的新文章。

**BugBounty（HackerOne 公开报告 2 条）**
- Basecamp：跨账户存储型 XSS，可导致持久的管理员接管：https://hackerone.com/reports/4175245
- Burp Community：OpenAPI site-map 操作经 $id rebasing 读取本地 schema 示例（$1000）：https://hackerone.com/reports/4000535

## AI/TLDR 动态（来自 ai-tldr.dev；本窗口 36 小时内新条目 21 条，其中 security 类 1 条）

**今日概括**：AI 编程 agent 工具密集发版，安全默认值在收紧，例如 Claude Code 2.1.325 默认不再静默执行沙箱内的 Bash 命令。「agent 能花钱」成了新主题：ChatGPT Wallet 推出，Brave Search API 支持 x402 按次付费。开源推理方面，llama.cpp 发布首个稳定版 v1.0.0，同时有大型 MoE 模型能在消费级硬件上运行。另外，微软 365 故障超过 20 小时，导致 Claude/ChatGPT 里的 M365 连接器一起失效。

**安全（已合并到工具节第 12 条）**
- OpenAI Daybreak Red Team / Defense Factory：https://ai-tldr.dev/releases/openai-daybreak-red-team-defense-factory/

**工具与开源仓库**
- Claude Code 2.1.325：沙箱内的 Bash 命令改为需要确认（安全默认值更严）：https://ai-tldr.dev/releases/anthropic-claude-code-2-1-325/ · 原始来源 https://github.com/anthropics/claude-code/releases/tag/v2.1.325
- Claude Code 2.1.323：实验性 Code Mode，Claude 可以用 JavaScript 调用自己的工具：https://ai-tldr.dev/releases/anthropic-claude-code-2-1-323/
- ChatGPT Wallet：OpenAI 的 agent 可以代购物，使用一次性卡 token，每笔订单都要用户批准：https://ai-tldr.dev/releases/openai-chatgpt-wallet/ · 原始来源 https://www.cnbc.com/2026/11/13/openai-chatgpt-wallet-dot-purchases.html
- Brave Search API 支持 x402：agent 用稳定币按次付费，不需要账号和 API Key：https://ai-tldr.dev/releases/brave-search-api-x402-agent-payments/
- llama.cpp v1.0.0：首个稳定版，开始采用语义化版本：https://ai-tldr.dev/releases/llama-cpp-v1-0-0/ · 原始来源 https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0 · https://huggingface.co/blog/ggml-org/llama-cpp-v1
- Transformers v5.23.0：新增 7 种模型类型，并重做了导出 API：https://ai-tldr.dev/releases/huggingface-transformers-5-23-0/
- Codex CLI 0.169.0 和 0.168.0：侧边对话标签页、任务搜索、分屏、音频输入：https://ai-tldr.dev/releases/openai-codex-cli-0-169/ · https://ai-tldr.dev/releases/openai-codex-cli-0-168/
- OpenCode 2.3.0：子 agent 默认在后台运行：https://ai-tldr.dev/releases/anomalyco-opencode-2-3-0/
- Self-hosted Claude Managed Agents：整套 agent 服务可以完全部署在企业内网：https://ai-tldr.dev/releases/anthropic-self-hosted-claude-managed-agents/
- Claude Meetings：Claude 作为参会者加入视频会议：https://ai-tldr.dev/releases/anthropic-claude-meetings/
- smolmaxxing：16B MoE 模型能在 1GB 内存的电视盒子上运行：https://ai-tldr.dev/releases/hyperionaidev-smolmaxxing/

**模型**
- Edge0-145B：开源 145B MoE 编程和 agent 模型，单张消费级 GPU 可运行：https://ai-tldr.dev/releases/edge0-145b/
- Zyphra ZONOS3-Mini：Apache-2.0 授权的 TTS 模型，可实时克隆声音（注意语音冒充风险）：https://ai-tldr.dev/releases/zyphra-zonos3-mini/

**论文与研究**
- Checkpoint forensics：已发布权重中的随机数痕迹能看出训练所用的 NVIDIA 芯片代际：https://ai-tldr.dev/releases/unemployment-labs-checkpoint-forensics-blackwell/

**行业动态**
- Microsoft 365 故障超过 20 小时，Copilot 和 AI 连接器同时失效：https://ai-tldr.dev/releases/microsoft-365-outage-copilot-connectors-nov12/ · 原始来源 https://techcrunch.com/2026/11/12/microsofts-outlook-email-hit-by-new-outage
- Mirendil（前 Anthropic 成员创办）完成 10 亿美元 A 轮融资：https://ai-tldr.dev/releases/mirendil-1b-series-a/
- showcase 和 video 类共 3 条只计数（Claude 整理哥德尔笔记、Wes Roth、Fireship）。

## Agent 用例动态（来自 agentusecases.ai；48 小时内新条目 33 条，以下列出 25 条代表）

**今日总结**：大家主要用 agent 做三类事：小企业和个人事务的「全能助理」（记账、发票、营销、邮件和日程）、用浏览器 agent 操控真实网站（报税、找牙医），以及编程和研究工作流（质量门禁流水线、论文语料、并行市场调研）。OpenClaw 和 Meta Muse 的个人助理用例集中出现；也有 agent 主动打电话、用合成语音代人致电银行的例子。

**安全相关（放在最前）**
- 有人用 Meta Muse 监控聊天群并做定期分析，任务因安全标记被平台中止，说明平台对监控类用法有护栏：https://agentusecases.ai/use-case/monitor-chat-threads-and-deliver-regular-discussion-analysis
- 某 AI 工具用 Joshua Browder 的合成语音致电 Wells Fargo，要回电汇费用（声音克隆加代理通话，涉及身份核验风险）：https://agentusecases.ai/use-case/phone-the-bank-to-get-wire-fees-refunded
- 作者用 Claude Cowork 操控真实浏览器填报印度 ITR-2，登录和付款仍由本人掌控，并发现预填数据里的 2 处错误：https://agentusecases.ai/use-case/file-an-indian-itr-2-with-capital-gains-via-browser-agent
- 作者让 agent 分类单据、操作瑞士报税表，最后由本人复核：https://agentusecases.ai/use-case/let-an-agent-fill-in-your-swiss-tax-declaration
- 有人用 OpenClaw 自动回复消息、排日程（agent 拥有收发权限）：https://agentusecases.ai/use-case/handle-mail-replies-and-calendar-with-openclaw

**编程与工程**
- 让 agent 只能经过带覆盖率、依赖和 lint 门禁的工具构建、测试、部署：https://agentusecases.ai/use-case/run-agents-through-quality-gated-build-test-and-deploy-tools
- 作者用 Claude 写了一个批量静态重写 Rust 编译器代码的工具：https://agentusecases.ai/use-case/rewrite-rust-compiler-code-in-bulk-with-a-query-driven-tool
- 用户用 ChatGPT Agent 修好失败的代码，并清理积压邮件：https://agentusecases.ai/use-case/fix-failing-code-and-clear-email-backlog-with-agent-mode
- Rainshare：把闲置的 AI 编程额度借给开源项目：https://agentusecases.ai/use-case/lend-spare-ai-usage-to-help-on-open-software-issues
- 评论者用 OpenClaw 加 Hermes Agent 做开发和研究，并让一个 agent 教另一个 agent：https://agentusecases.ai/use-case/use-openclaw-for-development-research-and-ad-hoc-tasks
- 有人用对话方式让 agent 部署云服务：https://agentusecases.ai/use-case/deploy-to-the-cloud-by-talking-to-an-agent

**研究**
- PaperRaven 用 Claude Code 构建经过核验的论文语料库：https://agentusecases.ai/use-case/build-verified-paper-corpora-on-any-scientific-topic
- Claude Code 插件并行跑市场调研、竞品分析和财务预测：https://agentusecases.ai/use-case/validate-startup-ideas-with-parallel-research-agents
- 用 Claude Code 技能做论文研究和数据分析：https://agentusecases.ai/use-case/run-thesis-research-and-data-analysis-with-claude-code-skill
- 用 ChatGPT Agent 阅读书籍、PDF 和博客：https://agentusecases.ai/use-case/read-books-pdfs-and-blogs-with-agent-mode

**个人助理与生活**
- Meta Muse 作为每日助理，负责接送和提醒：https://agentusecases.ai/use-case/run-a-daily-assistant-for-school-run-and-reminder-logistics
- 把任务交给 Muse 这个「AI 幕僚长」：https://agentusecases.ai/use-case/delegate-tasks-to-an-ai-chief-of-staff
- 用 Operator 浏览器 agent 找医保网络内的牙医：https://agentusecases.ai/use-case/find-an-in-network-dentist-with-a-browser-agent
- OpenClaw 需要用户输入时直接打电话给手机：https://agentusecases.ai/use-case/let-your-agent-phone-you-when-it-needs-input
- 基于 OpenClaw 自建家庭多用户聊天应用：https://agentusecases.ai/use-case/run-a-household-ai-chat-app-for-the-family
- 用 Grok Bot 搜索五年的 Gmail 并生成时间线：https://agentusecases.ai/use-case/search-years-of-gmail-and-build-a-timeline-with-grok-bot

**小企业经营**
- 用 Claude 处理提案、外联和开票：https://agentusecases.ai/use-case/automate-small-business-proposals-outreach-and-invoicing
- 用 Claude 加 ChatGPT 做记账、订货和传单：https://agentusecases.ai/use-case/handle-small-business-accounting-ordering-and-flyers-with-ai
- 独立创始人用 OpenClaw 处理入站聊天、邮件和社媒：https://agentusecases.ai/use-case/handle-inbound-chat-email-and-social-as-a-solo-founder
- 用一组 Grok Bot 打理家务和 HVAC 生意：https://agentusecases.ai/use-case/run-family-and-hvac-business-tasks-with-a-fleet-of-bots

## 地址／IoC 汇总

**Check Point PHP2Shell 加 CVE-2026-123039 入侵（原样抄自 CPR）**
- IP：130.94.19[.]204、130.94.19[.]168
- SHA256：
  - edb3e92eb7bda7413a09edcc4b1ba3cbed4bcdf42808a8abce63b6e4c3fda2b3（tpl webshell）
  - 4171b521fa6441382aa2fa014a08e18ff9a6e0ab6096c9144072bf46b37a2ec8（slot_CPconfigdaemon）
  - d7549671c7189979f0624ec52dad9ea6a707d23146e3585ab8f8c4720eca0c63（CPconfigdaemon）
  - 3b51080a909023f7d484e2443740b572307ce0054eb9e32d98f0a06bfcd2db90（gogo）
  - c7d9477309fac6c638a1128442056a242de086996add8cb49cd6496c36003237（destory_v6）
  - 0522937c0c0337be54fe25493539e5f5f8ceb9742c980aaff1cfc9515f3a96f7（DREAM_ANNEXATION.txt）
  - ee16e1695711b9d60c62925fcfb2fe1a29c18ae26565bc05410a14e16d2a39d7（philistine）
  - fb1a6235eb6bce8c9ec8cd8bb85f17c9c2bde8ecb45b7a243a30ceadf26654da（libdssafe.so）
- 文件和路径特征：门户模板目录下的 zz*.tpl；/opt/CPcvpn-R81.20/tmp/ 中带 upload_progress_pwn 的会话文件
- 来源：https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/

**CyberStrikeAI AWS 入侵（Elastic）**
- IP：43[.]240[.]29[.]11、43[.]240[.]29[.]28、43[.]240[.]29[.]33（截至 11 月已不再提供界面，只适合回溯狩猎）
- 来源：https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion

**FaceStealer（FBI FLASH 示例仿冒域名）**
- uu01webzoom[.]us、teams.livemeet[.]us
- 来源：https://www.ic3.gov/CSA/2026/261112.pdf

**其他**：UnrealIRCd、WP Duplicate、Tactical RMM、Quay、SilentAir 都未见公开 IoC（WPScan 明确表示没有公布）。

## LWiS 固定信源（每日交叉，不替代 X Latest）

- X List（只读）：https://x.com/i/lists/1239330068461244424 （本期 4 页 369 帖，窗口内 215 帖）
- 博客清单：https://blog.badsectorlabs.com/files/blogs.txt （本地：lwis-sources/blogs.txt；本期用于补链 Elastic Security Labs、Securelist、Project Zero）
- CISA KEV：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NVD：https://nvd.nist.gov/
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- SecureFlow 安全信息流：https://secureflow.scope-sentry.top/all
- SecureFlow 社区：https://secureflow.scope-sentry.top/community
- SecureFlow 博客：https://secureflow.scope-sentry.top/blog
- Agent Use Cases：https://agentusecases.ai/ （RSS https://agentusecases.ai/feed.xml）
- AI/TLDR：https://ai-tldr.dev/ （Atom https://ai-tldr.dev/feed.xml）
- pwn.watch：https://pwn.watch/ （RSS https://pwn.watch/feed.xml）
- ExploitGrid：https://exploitgrid.net/
- 阮一峰周刊（仅周末版）：https://www.ruanyifeng.com/blog/atom.xml

## 来源搜索 URL

**X 只读搜索（search_posts_all，起点 2026-11-12T22:55Z）**
- `(CVE OR 0day OR "zero-day" OR PoC OR exploit) (patch OR exploited OR vulnerability) -is:retweet -is:reply`：Latest 25 条（11-13 21:50～22:51 UTC）。[x.com 搜索](https://x.com/search?q=CVE%20exploited%20patch&f=live)
- `(CVE OR 0day OR "zero-day" OR "actively exploited") (patch OR exploited OR advisory) -is:retweet -is:reply`：relevancy 25 条（11-12 22:58～11-13 20:34）
- `("exploited in the wild" OR "in-the-wild" OR "under active exploitation" OR "emergency patch" OR "security update") -is:retweet -is:reply lang:en`：relevancy 25 条（11-13 03:42～22:00）
- `github.com (C2 OR "red team" OR redteam OR nuclei OR "offensive security" OR BOF) -is:retweet`：Latest 2 条（都与安全工具无关）
- `("malware analysis" OR "threat report" OR "threat actor") -is:retweet -is:reply`：Latest 25 条（11-13 18:16～22:52）
- `("malware analysis" OR "threat report" OR "threat actor" OR ransomware OR "state-sponsored") -is:retweet -is:reply`：relevancy 25 条（11-13 00:51～21:49）
- LWiS X List（get_lists_posts）：4 页 369 帖，窗口内 215 帖（11-12 22:55～11-13 22:52 UTC）
- X 合计：有效只读调用 10 次共 496 帖，去重后在窗口内的约 340 帖；另有 6 次调用因结果落盘被截断而作废重取。

**其他信源**
- SecureFlow all：https://secureflow.scope-sentry.top/api/rss/all/articles?search=&page=1&pageSize=200 （200 条，覆盖 2026-11-06 14:00～11-13 21:07 北京时间；48 小时内未收录 65 条：ZDI 56、先知 6、HackerOne 2、Seebug 1）
- SecureFlow community：https://secureflow.scope-sentry.top/api/rss/category?category=community （7 个源全部拉取；48 小时新条目 7 条：先知 6、Seebug 1；奇安信攻防社区、t00ls、吾爱破解、InfoSec Write-ups、Critical Thinking 都是 0 条。吾爱破解 2024-09 后已不更新）
- SecureFlow blog：https://secureflow.scope-sentry.top/api/rss/category?category=blog （12 个源全部拉取；7 天内首次出现 56 条，全部来自 ZDI-vulnerabilities；其余 11 个源 0 条；「微信公众号」源 2025-02 后已不更新）
- 三路按原文链接合并去重后共 65 条。
- pwn.watch：https://pwn.watch/feed.xml （50 条，lastBuildDate 为 2026-11-08 20:19 GMT；本窗口新条目 0 条）
- ExploitGrid 最新 exploit：https://api.exploitgrid.net/api/exploits?page=1&limit=100 （100 条，覆盖 11-10 04:27～11-12 15:37 UTC；48 小时内未收录 2 条，都是老 CVE；按 CVE 查询 6 次，只有 CVE-2026-119977 有 9 条）
- ExploitGrid KEV 期限：https://api.exploitgrid.net/api/vulnerabilities/kev/active-deadlines （CVE-2026-114713、CVE-2026-123039 期限 11-16；CVE-2026-124194 期限 11-24；Barracuda CVE-2026-111560 期限 11-13，今天到期）
- AI/TLDR：https://ai-tldr.dev/feed.xml （50 条；36 小时内新条目 21 条，其中 security 类 1 条）
- Agent Use Cases：https://agentusecases.ai/feed.xml （60 条；48 小时内新条目 33 条）
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （catalogVersion 2026.11.13；11-13 新增 2 条）
- 阮一峰周刊：工作日版不加。

## 验收结果

- 采集：X Latest、relevancy 和 LWiS List 都已覆盖 24 小时；SecureFlow 三路、pwn.watch、ExploitGrid、AI/TLDR、Agent Use Cases、KEV 都已拉取，条数见上。**通过**。
- 核验链接：报告中共 189 个唯一 https URL，用浏览器 UA 逐个核验。50 个 X 原帖链接都和采集数据里的帖子 ID、作者对得上；其余 139 个里 135 个返回 200，4 个保留并注明（UnrealIRCd 论坛、CCB 返回 403，Seebug 返回 521，SecurityOnline TLS 中断）。没有 404。t.co 已展开（本期展开 20 个）。**通过**。
- 成稿：十个小节齐全，无空节；IoC 节已原样抄录；没有利用代码或步骤。**通过**。
- 落盘与交付：见聊天消息（本机副本状态以聊天消息为准）。
