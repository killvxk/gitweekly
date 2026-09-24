# X 安全情报晚报 · 2026-09-14

> 搜集窗口：圣地亚哥时间 **2026-09-13 20:00 至 2026-09-14 ~20:41**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周一）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-14.json`（collected_at **2026-09-14T20:23:38-03:00**）＋ `/workspace/tools-news-pulse-2026-09-14.md`＋ `/workspace/enrich-2026-09-14/`。CISA KEV catalogVersion **2026.09.14**／**1710** 条／dateReleased **2026-09-14T19:00:02.426Z**（相对昨日 **+1**；新入 **CVE-2026-76461** Cisco Secure Email Gateway）。
> **期限今日 09-14：ConnectWise ScreenConnect CVE-2026-84869；GitLab CVE-2026-85706；PaperCut CVE-2026-81578／82078。** 昨日起逾期：MikroTik **CVE-2026-67277／86060**；Citrix **CVE-2026-19490**、Fortinet **CVE-2025-25249**、Cisco FMC **CVE-2026-20079**（自 09-12）。期限明日 09-15：**无**。Sep2 五条联邦 BOD（Kestra／JFrog／Sangoma／SonicWall×2）自 **09-05** 起仍 **OVERDUE**。due_near：LiteLLM／Starlette（**09-16**）；**Cisco ESA 76461（09-17）**；Chromium **85046**（**09-18**）；微软两在野（**09-22**）；Chromium **87491**（**09-23**）；JFrog **42016／42018**（**09-25**）。
> X：`/workspace/x-posts-2026-09-14.json`（合并 **43** 条唯一：A12／B5／C15／LWiS11；**0** 重叠；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.24h**（远不足 24h）。Search B 约 **15.4h**。Search C 约 **2.53h**。LWiS List 扫描约 **50.4h**（保留约 **27.9h**，作交叉，不假装为本窗口 Latest）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · 新入 KEV · Cisco ESA】** CISA 今日将 **CVE-2026-76461**（Secure Email Gateway／AsyncOS SQLi → 未认证 root 命令执行，CVSS **9.8**）加入 KEV；due **09-17**。修复 `15.5.5-014`／`16.0.4-302`／`16.5.0-780`（建议迁至 16.5.0-780）；无 workaround。
  CISA 告警：https://www.cisa.gov/news-events/alerts/2026/09/14/cisa-adds-one-known-exploited-vulnerability-catalog
  厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX
  NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76461

- **【今日 due · GitLab／ScreenConnect／PaperCut】** 联邦 due **今日 09-14**：**CVE-2026-85706**（CVSS 10 未认证任意文件读，自管实例）／**CVE-2026-84869**（ScreenConnect，升 **26.6.5**）／PaperCut **81578／82078**（维护版 26.0.5／25.0.13／24.1.10；公告 last-updated 仍 Sep10）。X Latest 多条复述 GitLab／BC「CISA：已在野利用」。
  GitLab 补丁：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
  ScreenConnect：https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin
  PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
  BC GitLab：https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploit-max-severity-gitlab-flaw-in-attacks/
  X：https://x.com/DailyCVEBrief/status/2099638848716206585 · https://x.com/TechKimmi/status/2099637571357700237

- **【逾期 · MikroTik／Cisco FMC／Citrix／Fortinet】** MikroTik **67277／86060** 自 09-13 due 起逾期；Cisco FMC **20079**／Citrix **19490**／Fortinet **25249** 自 09-12 逾期。Talos 续跟 UAT-12197／11823／11988。
  MikroTik：https://mikrotik.com/supportsec/september-2026-vulnerability/
  CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
  Talos：https://blog.talosintelligence.com/fmc-ongoing-exploitation/
  IoC：https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.txt

- **【X · 新披露／狩猎】** LimeSurvey **CVE-2026-16809**（Fluid Attacks CNA）；Windows UMPS **CVE-2026-62721**（MSRC）；Lovable RLS **CVE-2025-48757** 审计叙事；暴露 Vite dev server **CVE-2026-39364** 窃密；n8n AI Agent 授权绕过 **CVE-2026-65015** 等；Marimo **CVE-2026-39987** KEV／在野狩猎提示。
  Fluid：https://fluidattacks.com/advisories/wellerman
  MSRC：https://msrc.microsoft.com/update-guide/advisory/CVE-2026-62721
  BC Vite：https://www.bleepingcomputer.com/news/security/hackers-target-exposed-vite-dev-servers-to-steal-aws-azure-secrets/
  n8n：https://deturris.io/posts/n8n-ai-agents-authorization-bypasses/
  X Marimo：https://x.com/DFIR_Radar/status/2099636255663259871

- **【工具 · C2／红队】** OpenHunterAI 红队引擎开源；BEAR-C2 V2.0；Mythic MS Teams（Graph API）profile；StealC 分析仓库；另有 Claude-Red 红队 playbook 仓库（防御向只记存在，不抄步骤）。
  OpenHunterAI：https://github.com/LumosLab-Innovation/OpenHunterAI
  BEAR-C2：https://github.com/S3N4T0R-0X0/BEAR-C2
  msteams：https://github.com/Whispergate/msteams
  StealC 分析：https://github.com/kaandemir993/StealC-Stealer-RuntimeBroker-Hollowing-C2-Extraction-Payload-Extraction-Analysis
  Claude-Red：https://github.com/SnailSploit/Claude-Red

- **【LWiS · Brevo CDN／Oracle AIDB／askWAM】** List 见 Brevo CDN／站 ClickFix＋恶意 WP 扩展上传脚本叙事；Oracle AIDB RCE write-up（已修）；Entra ID askWAM 取 token 工具；另有域凭据转储文章／BYOVD 进程终结工具（防御向只记暴露面）。
  VT URL：https://www.virustotal.com/gui/url/545cf8c6e356c1bc9b0616e3bb86e756ddde7cda2f75ba4b261c97f3cce878fc/details
  Oracle write-up：https://github.com/Metnew/write-ups/tree/main/oracle-aidb-rce-26.2.4.2
  askWAM：https://github.com/dirkjanm/askWAM
  X Brevo：https://x.com/cnotin/status/2099604133036626356

- **【威胁报告 · Anthropic TI 续传】** Search C 大量二次转载 Sep2026 TI（俄／也门／Claude 使用叙事）；以官方页／PDF 为准。另有 PureRat 破解声称、多起未验证库泄声称（作情报噪声标注）。
  报告：https://www.anthropic.com/threat-intelligence-report-september-2026
  PDF：https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf
  Record：https://therecord.media/anthropic-russia-hackers-claude

- **【新闻 · Risky／tl;dr／工具脉冲】** KEV **+1**；Risky 仍 **RBNEWS612**（另见 SRB183）；tl;dr 仍 **#345**；Sliver **v1.7.7**／nuclei-templates **v10.4.8**／nuclei **v3.11.1** 无升版；ICS Sep13–14 无确认新项（254–257／259–260 404；258 403）。
  https://risky.biz/RBNEWS612/
  https://tldrsec.com/p/tldr-sec-345

## CVE / POC / 漏洞

### 1. 【新入 KEV】Cisco Secure Email Gateway CVE-2026-76461

CISA **2026-09-14** 入目；due **2026-09-17**。未认证 SQL 注入（经特制邮件）可在底层 OS 以 **root** 执行任意命令（CVSS **9.8**）。防御：升级至厂商列出的修复版本、限制网关暴露、按 advisory 在 `mail_logs` 狩猎 `COPY.*TO PROGRAM`；云客户如有恶意活动由 Cisco 直接联系。

地址：
- CISA 告警：https://www.cisa.gov/news-events/alerts/2026/09/14/cisa-adds-one-known-exploited-vulnerability-catalog
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-76461
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog

IoC：未见公开 IoC IP／样本哈希列表（advisory 仅给日志狩猎线索）。

### 2. 【今日 due】GitLab CVE-2026-85706（CVSS 10.0）

未认证任意文件读（自管 CE／EE）。补丁 **19.3.2／19.2.6／19.1.8**（Sep10）；KEV Sep11；窗口内 BC／X 称已有在野利用／探测。防御：立即打补丁、限制外网暴露、审计异常文件访问。

地址：
- 厂商补丁：https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-85706
- BC：https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploit-max-severity-gitlab-flaw-in-attacks/
- 二次摘要：https://cvebrief.com/cve/cve-2026-85706
- X：https://x.com/DailyCVEBrief/status/2099638848716206585 · https://x.com/TechKimmi/status/2099637571357700237

IoC：未见公开 IoC。

### 3. 【今日 due】ConnectWise ScreenConnect CVE-2026-84869

CVSS **9.9**。升级 **26.6.5**；临时可取消 TransferFiles 权限；升级后需重装 host clients／更新 access agents（以厂商公告为准）。

地址：
- 厂商：https://www.connectwise.com/company/trust/security-bulletins/2026-09-08-screenconnect-bulletin
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-84869

IoC：未见公开 IoC。

### 4. 【今日 due】PaperCut NG/MF CVE-2026-81578／CVE-2026-82078

维护版 **26.0.5／25.0.13／24.1.10** 取代紧急补丁；公告 last-updated 仍 **September 10, 2026**；KEV due **今日 09-14**。GreyNoise 先前 AI 编排战役狩猎文仍相关。

地址：
- 厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- GreyNoise：https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf

IoC：见 GreyNoise 文内狩猎线索；本报不转载利用步骤。

### 5. 【逾期 · 昨 due】MikroTik RouterOS CVE-2026-67277／CVE-2026-86060

KEV due **2026-09-13** 已过。厂商 September 2026 公告＋CERT.pl 活跃利用说明。修方向含 **6.49.21／7.23.4／7.24.2／7.25 beta 3**（以厂商表为准）。

地址：
- 厂商：https://mikrotik.com/supportsec/september-2026-vulnerability/
- CERT.pl：https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-67277 · https://nvd.nist.gov/vuln/detail/CVE-2026-86060

IoC：IP `82.192.72.4` · `103.102.31.18`（CERT.pl）。

### 6. 【逾期 · 09-12 due】Cisco FMC CVE-2026-20079（＋链式叙事）

认证绕过（CVSS **10.0**）。Talos：UAT-12197／UAT-11823（Sandworm 工具重叠／Cyclops Blink）／UAT-11988（Qilin）。热修防未来利用，**不清除既有沦陷**。

地址：
- Talos：https://blog.talosintelligence.com/fmc-ongoing-exploitation/
- IoC txt：https://github.com/Cisco-Talos/IOCs/blob/main/2026/09/ongoing-fmc-exploitation.txt
- IoC raw：https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/09/ongoing-fmc-exploitation.txt
- 厂商：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2

IoC（verbatim 摘要）：hashes `B037f45e…bef77d`（home.jsp）／`Db491181…a8c8e`（cmd.jar）；IPs `89.34.96.56`／`208.123.119.215`／`104.218.165.253`／`91.214.78.118`／`43.204.2.142`；Cyclops Blink `6f98add5…2fe461`。完整列表见 IoC raw。

### 7. 【逾期 · 09-12 due】Citrix NetScaler CVE-2026-19490／Fortinet CVE-2025-25249

地址：
- Citrix：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- Fortinet：https://fortiguard.fortinet.com/psirt/FG-IR-25-084

IoC：未见本窗口新公开 IoC。

### 8. 【X · 新披露】LimeSurvey CVE-2026-16809

Fluid Attacks 以 CNA 分配；称 AI SAST 检出／Miguel Gómez 披露。防御：对照 advisory 升级／限制管理面。

地址：
- 厂商／研究：https://fluidattacks.com/advisories/wellerman
- 索引：https://fluidattacks.com/advisories/
- X：https://x.com/fluidattacks/status/2099638574476046361

IoC：未见公开 IoC。

### 9. 【X · 补丁】Windows UMPS CVE-2026-62721

User-Mode Power Service 特权提升。对照 MSRC 安装补丁。

地址：
- MSRC：https://msrc.microsoft.com/update-guide/advisory/CVE-2026-62721
- X：https://x.com/taikoyaP/status/2099638708760916421

IoC：未见公开 IoC。

### 10. 【X · 审计叙事】Lovable RLS CVE-2025-48757

称大量应用 RLS「存在但不生效」。防御：复核 RLS 策略有效性，不依赖「有策略」扫描结果。

地址：
- X：https://x.com/auditdpro/status/2099639752542531741

IoC：未见公开 IoC。

### 11. 【X · 在野】暴露 Vite dev server CVE-2026-39364

BC／F5 叙事：公开 Vite 开发服务器被用于窃取云凭证；窗口内日文二次转载。防御：勿将 Vite dev 暴露公网、轮换泄露凭证、审计异常云 API。

地址：
- BC：https://www.bleepingcomputer.com/news/security/hackers-target-exposed-vite-dev-servers-to-steal-aws-azure-secrets/
- X：https://x.com/connect24h/status/2099636443870322748

IoC：见 BC／F5 原文狩猎线索；本报不抄利用步骤。

### 12. 【X · 研究】n8n AI Agent 授权绕过（含 CVE-2026-65015 叙述）

read-only Project Viewer 经工具路径提权执行等叙述。防御：限制 AI Agent／工具权限、升级 n8n、审计异常 workflow 执行。

地址：
- 文章：https://deturris.io/posts/n8n-ai-agents-authorization-bypasses/
- X：https://x.com/connect24h/status/2099636363998228832

IoC：未见公开 IoC。

### 13. 【X · KEV／狩猎】Marimo CVE-2026-39987

未认证终端 WebSocket 预认证 RCE；称在野且在 KEV。狩猎提示含 AWS Secrets Manager／SSH 密钥拉取等（以帖为准）。

地址：
- X：https://x.com/DFIR_Radar/status/2099636255663259871
- NVD（交叉）：https://nvd.nist.gov/vuln/detail/CVE-2026-39987

IoC：帖内狩猎行为描述；未见独立公开 IoC 列表。

### 14. 【LWiS】Oracle AIDB RCE（v26.2.4.2，称已修）

P2O／ZDI 相关 write-up：未消毒 bash 调用＋自最小权限到 ADMIN 的 LPE 叙事；称 late July 已修。防御向只记暴露面与补丁状态核对。

地址：
- 仓库：https://github.com/Metnew/write-ups/tree/main/oracle-aidb-rce-26.2.4.2
- X：https://x.com/v_metnew/status/2099623056670880120 · https://x.com/v_metnew/status/2099623882403496128

IoC：未见公开 IoC。

## 工具与 GitHub 发布

### 1. OpenHunterAI（红队引擎开源）

称原 AI Security 创业方向改为开源红队引擎。

地址：
- 仓库：https://github.com/LumosLab-Innovation/OpenHunterAI
- X：https://x.com/Dinosn/status/2099505079048945883

IoC：未见公开 IoC。

### 2. BEAR-C2 V2.0

对抗仿真／多协议与 OPSEC／外传配置切换叙事。防御：检测与封禁相关 C2 特征，不部署未授权 C2。

地址：
- 仓库：https://github.com/S3N4T0R-0X0/BEAR-C2
- X：https://x.com/S3N4T0R_0X0/status/2099469431424389174

IoC：未见公开 IoC。

### 3. Mythic C2 profile · Microsoft Teams（Graph API）

经 Teams 频道通信的 Mythic profile。防御：监控异常 Graph／Teams 机器人与应用权限。

地址：
- 仓库：https://github.com/Whispergate/msteams
- X：https://x.com/Dinosn/status/2099445591860256934 · https://x.com/ipurple/status/2099429279314374869

IoC：未见公开 IoC。

### 4. StealC 分析仓库（RuntimeBroker Hollowing／C2 提取）

分析向仓库；防御只记样本分析入口，不转载提取步骤。

地址：
- 仓库：https://github.com/kaandemir993/StealC-Stealer-RuntimeBroker-Hollowing-C2-Extraction-Payload-Extraction-Analysis
- X：https://x.com/Dinosn/status/2099408945429319891

IoC：见仓库分析产物（如有）；本报未见单独公开列表。

### 5. Claude-Red（红队 playbook 仓库）

Search A 转载。防御向仅记录仓库存在；不转载 playbook 步骤。

地址：
- 仓库：https://github.com/SnailSploit/Claude-Red
- X：https://x.com/0x0SojalSec/status/2099637006133518580

IoC：未见公开 IoC。

### 6. askWAM（Entra ID／WAM 取 token）

合法 SSO 流替代 PRT cookie 取 token 的研究工具。防御：审计异常 WAM／SSO token 申请、条件访问。

地址：
- 仓库：https://github.com/dirkjanm/askWAM
- X：https://x.com/_dirkjan/status/2099451141956178127

IoC：未见公开 IoC。

### 7. EVENSTAR ETWSyscallConsumer／0xM0nCrush（BYOVD）

用户态异步 syscall＋栈追踪消费者；以及加载签名 HONOR 驱动终结进程的 BYOVD 工具叙事。防御：监控异常驱动加载／进程被内核终结。

地址：
- ETW：https://github.com/winterknife/EVENSTAR/tree/master/ETWSyscallConsumer
- 0xM0nCrush：https://github.com/DeathShotXD/0xM0nCrush
- X：https://x.com/_winterknife_/status/2099208429201940676 · https://x.com/ipurple/status/2099206948063179044

IoC：未见公开 IoC。

### 8. 工具版本脉冲（公开备援）

- Sliver **v1.7.7** 无升版：https://github.com/BishopFox/sliver/releases
- nuclei-templates **v10.4.8** 无升版：https://github.com/projectdiscovery/nuclei-templates/releases
- nuclei **v3.11.1** 无升版：https://github.com/projectdiscovery/nuclei/releases

本日无显著工具官方升版更新。

## APT / Malware 分析

### 1. Anthropic 威胁情报报告（Sep2026）二次传播

Search C 大量转载：俄关联／也门单元／Claude Code 用于武器软件研发与攻击适应等叙事。以官方报告／PDF 为准；社交媒体摘要可能夸大。

地址：
- 官方：https://www.anthropic.com/threat-intelligence-report-september-2026
- PDF：https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf
- Record：https://therecord.media/anthropic-russia-hackers-claude
- X 例：https://x.com/killedbyclaude/status/2099639329345962208 · https://x.com/LandscapeThreat/status/2099623140879974711 · https://x.com/vainio_vesa_/status/2099608492482982345

IoC：以官方 PDF／附录为准；本窗口 X 帖未见新独立 IoC 列表。

### 2. PureRat／PureRAT V4.1 破解释放声称

情报源称威胁行为体分享破解版 .NET RAT（HVNC／隐藏 RDP／键盘记录等）。作声称标注，未独立验证。

地址：
- X：https://x.com/intels_daily/status/2099624547615928820

IoC：未见公开哈希列表（帖内未展开完整指标）。

### 3. Brevo CDN／站点 ClickFix＋恶意 WordPress 扩展

LWiS：加拿大访问主站见 ClickFix；后续称恶意 JS 可在管理员会话上传「wmedia-optimizer」恶意扩展。

地址：
- X：https://x.com/cnotin/status/2099604133036626356 · https://x.com/cnotin/status/2099611241949860002
- VT URL：https://www.virustotal.com/gui/url/545cf8c6e356c1bc9b0616e3bb86e756ddde7cda2f75ba4b261c97f3cce878fc/details
- VT 文件：https://www.virustotal.com/gui/file/901ef043f83c9f83dbd289b627e8249007e6d58f8709cbd6d6411c6000f10c49/details

IoC：
- VT URL id：`545cf8c6e356c1bc9b0616e3bb86e756ddde7cda2f75ba4b261c97f3cce878fc`
- 文件 SHA-256：`901ef043f83c9f83dbd289b627e8249007e6d58f8709cbd6d6411c6000f10c49`
- 扩展名叙事：`wmedia-optimizer`／「Web Media Optimizer」

### 4. Konni／AI 生成 PowerShell 后门（二次转载，注意日期）

X 卡片链到 THN **2026-01** 旧文，属窗口内再传播，非新事件。

地址：
- THN（旧文）：https://thehackernews.com/2026/01/konni-hackers-deploy-ai-generated.html
- X：https://x.com/pedri77/status/2099609293741813848

IoC：见原 THN／厂商报告；本报不重抄。

### 5. 未验证库泄／勒索声称（噪声）

NTUA、委内瑞拉市政、菲律宾 DOLE、Telegram「1.2 亿」、以色列 SIBAT、Revolut 等多起声称。一律标注**未验证**；无独立证据不升格为主条。

地址（原帖例）：
- https://x.com/CyberPulse56/status/2099641341173223864
- https://x.com/intels_daily/status/2099636094857880037
- https://x.com/intels_daily/status/2099620998500765715
- https://x.com/IntCyberDigest/status/2099603178173939908

IoC：未见可靠公开 IoC。

### 6. 域凭据转储技术文（防御向）

File Handle Redirection 扩展到 DC 抽取 ntds.dit／SYSTEM／SECURITY 的研究文。防御：加固 DC、监控异常文件句柄／备份通道。

地址：
- Medium：https://medium.com/@s12deff/domain-credential-dumping-via-file-handle-redirection-749c24820ea8
- X：https://x.com/Salsa12__/status/2099236612223758487

IoC：未见公开 IoC。

## 地址／IoC 汇总

- **Cisco ESA 76461**：未见公开 IP／hash；日志狩猎 `COPY.*TO PROGRAM`（mail_logs）。
- **MikroTik**：`82.192.72.4` · `103.102.31.18`（CERT.pl）。
- **Cisco FMC Talos**：`B037f45e02a289325a1a5eb0d4db6a9fce9954fd0fdfd07162cb4eb2acbef77d`；`Db491181ece3f319de6567ab6f6daa90c6879911cd890155e6b7d8cc7a1a8c8e`；`6f98add5d1a7729192b6ad8491d85c505c64836f7881742d6b93bd8e3d2fe461`；IP `89.34.96.56`／`208.123.119.215`／`104.218.165.253`／`91.214.78.118`／`43.204.2.142`。完整：https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/09/ongoing-fmc-exploitation.txt
- **Brevo／ClickFix**：VT URL `545cf8c6…e878fc`；文件 SHA-256 `901ef043…f10c49`；扩展名 `wmedia-optimizer`。
- **其余条目**：未见公开 IoC（或仅有文章内狩猎线索，见各节）。

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

- X Latest A（CVE／POC／exploit／0day）：https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day&src=typed_query&f=live
- X Latest B（github.com + C2／red team／nuclei 等）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20nuclei%20OR%20sliver%20OR%20mythic%20OR%20cobalt)&src=typed_query&f=live
- X Latest C（malware analysis／threat report／threat actor）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- LWiS List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- tl;dr sec：https://tldrsec.com/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV 目录：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
