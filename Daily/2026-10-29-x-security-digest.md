# X 安全情报晚报 · 2026-10-29（补做）

> 原定 10-29 20:00 的运行中途被打断，本份于 **10-30 00:40（America/Santiago／UTC-3）补做**。
> 搜集窗口：**2026-10-28 20:12 至 2026-10-30 00:40**（UTC-3）。X 参数 `start_time=2026-10-28T23:12:00Z`。实际抓到的帖子从 **10-28 20:35** 到 **10-29 23:58**（UTC-3），**有效覆盖约 27 小时 23 分**。
> **X 采集方式**：Grok Bot 只读公共 X 接口 `search_posts_all`（relevancy，每次 100 条）。本轮为补做精简版：**3 次 X 读取，0 次 429**（A 类 CVE/在野利用、C 类恶意软件/威胁报告、KEV/厂商补丁各 1 次）；未读 LWiS List、未单独跑 B 类工具查询。原始 75 条，与 seen_ids（9565）重叠 0。**全程只读，没有发帖、回复、点赞、转推、收藏或关注。**
> **公开备援**：CISA KEV JSON（curl 核对）。

## CISA KEV

**catalogVersion 2026.10.29／1764 条，Δ+2**（相对 2026.10.28／1762）。`dateReleased` 2026-10-29 16:09（UTC-3）。

- **今日新增**：
  - **CVE-2026-97229** GitLab CE/EE 整数溢出（CVSS 10，无需登录的代码执行），**due 11-01**。自托管请升级到 19.2.8／19.3.5／19.4.2。
  - **CVE-2026-76418** Cisco Secure Firewall ASA／FTD SSL VPN 拒绝服务（CVSS 8.6，在 tunnel group 启用二次认证时受影响），**due 11-01**，无缓解措施，需升级。
- **今日到期（10-29）**：PHP2Shell CVE-2026-109618／109619。
- **即将到期**：Fragnesia CVE-2026-46300 **10-31**；Plex 96655／96652、Siemens 110936 **11-03**；Magento 48356、Brotli 111497 **11-10**；VMware ESX 41709 **11-11**。
- **已逾期**：Arista 114625、Collabora 110447（10-26 起）；SiteGuard 106931、Plex 96656／96654（10-23 起）。

## 今日摘要

1. KEV 新增 GitLab 97229 与 Cisco ASA/FTD 76418，联邦期限都是本周日 11-01。
2. Cisco ASA/FTD SSL VPN 零日被用于远程让防火墙重启；Shadowserver 观察到 5.1 万台以上暴露的 ASA SSL VPN。
3. Cisco Talos：UAT-11473 利用 SD-WAN CVE-2026-20127 部署 KeyDrift，窃取 SD-WAN 控制面密钥。
4. Talos 披露 NIK C2：把窃取数据交给 OpenAI 分析的新 Windows C2 框架。
5. GOLD OGRE 在 Aur0ra 勒索行动中用 AI 编程代理辅助入侵（报道）。
6. PHP2Shell 今日 KEV 到期，Palo Alto 20 个热修复中 19 个已发布。
7. 其他在野：Ivanti Connect Secure 104935、FreeSWITCH 116779。
8. 数据泄露：Ymirlink Cuenote 扩大到 49 套系统、约 5163 万条；多起声称泄露待核实。

## CVE / 漏洞

### 1. Cisco ASA／FTD CVE-2026-76418：SSL VPN 零日被利用让设备重启（KEV due 11-01）
未认证攻击者可让启用二次认证 tunnel group 的 ASA/FTD 重载，造成 VPN 中断。Cisco 确认在野利用，无缓解措施，请升级到修复版本，并把异常重启当作可能的攻击信号排查。
- X 原帖：https://x.com/TheHackersNews/status/2115757006145593440
- X 原帖：https://x.com/The_Cyber_News/status/2115767798970437826
- X 原帖：https://x.com/TheLabLedger/status/2115827970351018171
- 厂商公告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tunnel-dos-s6mgkb75
- 文章：https://www.bleepingcomputer.com/news/security/cisco-warns-of-firewall-zero-day-exploited-to-crash-ssl-vpn-devices/

### 2. GitLab CE/EE CVE-2026-97229（CVSS 10，KEV due 11-01）
无需登录即可执行代码的整数溢出漏洞，CISA 确认在野利用。自托管实例请升级到 19.2.8／19.3.5／19.4.2，并检查 CI/CD runner 与 token 是否异常。
- X 原帖：https://x.com/notCVE/status/2115920270523285926
- X 原帖：https://x.com/phantmradar/status/2115887987921961347
- X 原帖：https://x.com/Aegisrecon/status/2115980922562732366
- 文章：https://securityarsenal.com/blog/cisa-kev-alert-gitlab-cve-2026-97229-and-cisco-asaftd-cve-2026-76418-under-active-exploitation-detection-and-remediation-guide

### 3. PHP2Shell（CVE-2026-109618／109619）：KEV 今日到期
Palo Alto PAN-OS 管理接口受影响，20 个热修复中 19 个已发布。PHP 本体修复版本 8.5.12／8.4.27／8.3.36 等。管理接口不要暴露在公网。
- X 原帖：https://x.com/FirewallFreddy/status/2115844383362723992
- X 原帖：https://x.com/cordobahq/status/2115988726920659078
- 厂商公告：https://security.paloaltonetworks.com/CVE-2026-109618

### 4. 其他在野利用（尚未进 KEV，待核实）
- Ivanti Connect Secure CVE-2026-104935 零日链：https://x.com/Daily_CyberSec/status/2116001749773267344
- SignalWire FreeSWITCH CVE-2026-116779（另修 116785、116790）：https://x.com/Daily_CyberSec/status/2115636789226405960
- 10 月 VM 趋势汇总（Windows ALPC 85880、Check Point 85102 等）：https://x.com/leonov_av/status/2115652821508890865
- Windows Print Spooler 未修堆溢出（需管理员权限，微软未紧急修补）：https://x.com/DFIR_Radar/status/2115640582164844825
- Arista VeloCloud 114625 已逾期，修复版本 5.2.3.18／6.1.3.10／6.4.2.12：https://x.com/abel_aguzmans/status/2115588325910417429

## APT / Malware 分析

### 1. KeyDrift：UAT-11473 窃取 Cisco SD-WAN 控制面密钥（Cisco Talos）
经 SD-WAN CVE-2026-20127（CVSS 10 认证绕过）进入 vSmart/vManage/vBond 控制器后，植入 KeyDrift（PolyFlame＋LittleFilch）读取控制面流量并窃取加密密钥。部分帖子将其与 Volt Typhoon 关联，**归因待核实**。建议升级 SD-WAN 控制器并轮换密钥。
- X 原帖：https://x.com/_pksharma/status/2115798632406348243
- X 原帖：https://x.com/AutoRemediate/status/2115833461692850688
- X 原帖：https://x.com/ADKCyber/status/2115950084575936768

### 2. NIK C2：调用 OpenAI 分析窃取数据的 Windows C2（Cisco Talos）
具备凭据窃取、监控、远控和锁屏勒索能力；攻击者未提供 API key 时会盗用受害者本机的 `OPENAI_API_KEY`。建议把环境变量里的 API key 纳入凭据保护与轮换。
- X 原帖：https://x.com/DailyUplink/status/2115848963928490261
- X 原帖：https://x.com/Python_s_/status/2115953797382263153

### 3. GOLD OGRE／Aur0ra 勒索：AI 编程代理用于入侵
报道称该俄语团伙在 Aur0ra 勒索行动中用 AI 代理自动提权到域管理员并外传数据。
- X 原帖：https://x.com/DFIR_Radar/status/2115806511809319190

### 4. 钓鱼与浏览器扩展
- UltraViewer DNS 关联出 QuickBooks 钓鱼行动（350+ 仿冒域名，木马安装包投递 njRAT／DarkKomet）：https://x.com/DFIR_Radar/status/2115987860004471227
- Socket 新发现 264 个劫持搜索流量的 Chrome 扩展（Searchjacked）：https://x.com/Python_s_/status/2115970769175917048

### 5. 勒索、入侵与数据泄露
- Ymirlink Cuenote FC 第二份报告：49 套系统、51,628,280 条记录可能外泄：https://x.com/DailyDarkWeb/status/2115689273630310414
- GMO Desktop Cloud 后续：泄露站点域名已于 10-28 被停用：https://x.com/Thuggeshwa60064/status/2115937588687274080
- **UNCONFIRMED** ScarlettGroup 声称攻击多伦多 Sunnybrook 医院：https://x.com/DailyDarkWeb/status/2115839146333966718
- **UNCONFIRMED** Rhysida 声称 Broadstreet HEOR（加拿大）：https://x.com/digvijay_k11/status/2115734770055537111
- **UNCONFIRMED** 委内瑞拉 VNET 用户数据（X01X00）：https://x.com/VECERTRadar/status/2115809038738817329
- **UNCONFIRMED** Edesur Dominicana 50 万条（K3RN3L_P4N1C）：https://x.com/VECERTRadar/status/2115865037998850257
- **UNCONFIRMED** 塞浦路斯数字政策部 7.3 万条（[Mod] Tanaka）：https://x.com/intels_daily/status/2115807651535696207
- **待核实** 美国 DHS 数据库泄露说法：https://x.com/BrightLabsMedia/status/2115973167910895649

## 工具与 GitHub 发布

本轮补做未单独跑 B 类工具查询，未见值得收录的新工具发布。

## 地址／IoC 汇总

未见公开 IoC（本轮读取的帖子未附可直接引用的 IP、域名或哈希；详细 IoC 请看各厂商原文）。

## 信源

- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- Cisco 公告：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tunnel-dos-s6mgkb75
- Palo Alto 公告：https://security.paloaltonetworks.com/CVE-2026-109618
- BleepingComputer：https://www.bleepingcomputer.com/news/security/cisco-warns-of-firewall-zero-day-exploited-to-crash-ssl-vpn-devices/
- LWiS List：本轮未读取
