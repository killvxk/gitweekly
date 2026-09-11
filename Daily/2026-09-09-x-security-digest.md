# X 安全情报晚报 · 2026-09-09

> 搜集窗口：圣地亚哥时间 **2026-09-08 20:00 至 2026-09-09 ~20:40**（America/Santiago / UTC-3）。**本报为官方 20:00 cron 晚报（周三）。**
> **公开备援为本轮 PRIMARY**：`/workspace/security-watch-public-backup-2026-09-09.json`（collected_at **2026-09-09T20:20:00-03:00**）＋ `/workspace/tools-news-pulse-2026-09-09.md`。CISA KEV catalogVersion **2026.09.09**／**1703** 条／dateReleased **2026-09-09T19:00:50.2591Z**（相对昨日 **+4**；新入 Fortinet **CVE-2025-25249**、Citrix NetScaler **CVE-2026-19490**、Cisco FMC **CVE-2026-20079**、Chromium V8 **CVE-2026-87491**）。
> **期限今日 09-09：legacy 四条（Ajax.NET／Libuser／ABRT／Linux Kernel）。期限明日 09-10：JFrog Artifactory CVE-2026-66384。** Sep2 五条联邦 BOD（Kestra／JFrog／Sangoma／SonicWall×2）自 **09-05** 起仍 **OVERDUE**。TrueConf **CVE-2026-72530**／MLflow **CVE-2026-64849** 仍逾期。due_near：Magento／N-able（**09-11**）；今日新三条网络设备＋Fortinet（**09-12**）；PaperCut（**09-14**）；LiteLLM／Starlette（**09-16**）；Chromium **85046**（**09-18**）；微软两在野（**09-22**）；Chromium **87491**（**09-23**）。
> X：`/workspace/x-posts-2026-09-09.json`（合并 **55** 条：A11／B9／C21／LWiS15；其中 **新 55**／已见 0；**logged_in=true**／**@seogoogle4**；blocked=false）。Search A Latest 约 **0.3h**（高流量，**远不足 24h**）。Search B 约 **21.7h**。Search C 约 **1.8h**。LWiS List 约 **57.92h**（目标窗内保留 15 条）。**公开备援仍为 KEV／厂商 PRIMARY**；X 作交叉。
> 规则：每条含完整 https URL；分列原帖／仓库／厂商／文章；没有指标就写「未见公开 IoC」；不编造；不转载利用代码／payload／PoC 步骤。

## 今日摘要

- **【主条 · KEV +4】** CISA 今日将四条入 KEV：Fortinet **CVE-2025-25249**（due **09-12**，与昨日 X／SOCRadar PivotC2 叙事交叉）、Citrix NetScaler **CVE-2026-19490**（due **09-12**，公告另列 **CVE-2026-19489**）、Cisco FMC／SCC **CVE-2026-20079**（due **09-12**，CVSS 10.0，主动利用）、Chromium V8 **CVE-2026-87491**（due **09-23**）。
  警报：https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog
  Fortinet：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
  Citrix：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
  Cisco：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
  Chrome：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html

- **【X／LWiS · BlueMoon 链式 0-day】** Volexity／THN：多个中国关联集群共用 **BlueMoon** exploit kit，链 **CVE-2026-85046**（Chrome V8）＋未编号 V8 sandbox escape＋**CVE-2026-85880**（Windows ALPC）；LWiS 帖另点 **CVE-2026-87491**。投递 GemStone／ShadowPad 等。按厂商补丁与狩猎；**不转写利用链。**
  THN：https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
  X（Volexity）：https://x.com/Volexity/status/2097742289707868182
  X（stevenadair）：https://x.com/stevenadair/status/2097784191983505563

- **【PaperCut Sep9】** 厂商页 **last_updated September 9, 2026**：宣布维护版将于 **09-10 约 14:00 AEST** 发布；Emergency Patch **R3** 仍当前紧急补丁；KEV due **09-14**。
  https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/

- **【新闻 · Risky NEW】** RBNEWS611＋RB852 同日上线；tl;dr 仍 #344；ICS 无新发。
  https://risky.biz/RBNEWS611/  https://risky.biz/RB852/  https://tldrsec.com/blog/tldr-sec-344/

- **【工具】** Sliver **仍 v1.7.7**；nuclei-templates **仍 v10.4.8**。NEW：BEAR-C2、PassTheCert-rs、redcell、awesome-security-agent-harnesses 等。
  BEAR-C2：https://github.com/S3N4T0R-0X0/BEAR-C2
  PassTheCert-rs：https://github.com/g0h4n/PassTheCert-rs

- **【威胁声称】** LockBit5→AmorSaúde（BR 医疗）；Panzer→Aqualogus（PT）；The Gentlemen→Veradigm／Air Canada／PharmaEssentia 等声称；AuditTeam→德国掩码受害者。均为公开声称，需独立核验。

## CVE / POC / 漏洞

### 1. 【KEV NEW】四条入目录（2026-09-09）

CISA 基于在野利用证据将下列四条加入 KEV。按厂商补丁／BOD 26-04 与取证分流要求收敛；**不转写利用细节。**

| CVE | 产品 | due | 简述 |
|-----|------|-----|------|
| CVE-2025-25249 | Fortinet FortiOS／FortiSwitchManager／FortiSASE | **09-12** | 堆溢出 → 未授权代码／命令执行；与 PivotC2 叙事交叉 |
| CVE-2026-19490 | Citrix NetScaler ADC／Gateway | **09-12** | AAA／Gateway 路径认证绕过；公告另含 CVE-2026-19489 |
| CVE-2026-20079 | Cisco FMC／SCC Firewall Management | **09-12** | 认证绕过 → 脚本执行／底层 OS root 风险；Cisco 称主动利用 |
| CVE-2026-87491 | Google Chromium V8 | **09-23** | OOB write → sandbox 内任意代码；Chrome Desktop **153.0.8010.36** 修复帖 |

地址：
- CISA 警报：https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog
- KEV：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- Fortinet：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- SOCRadar PivotC2：https://socradar.io/blog/cve-2025-25249-pivotc2-fortigate-rat/
- Citrix CTX696939：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- Cisco SA：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- Chrome：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2025-25249 https://nvd.nist.gov/vuln/detail/CVE-2026-19490 https://nvd.nist.gov/vuln/detail/CVE-2026-20079 https://nvd.nist.gov/vuln/detail/CVE-2026-87491
- X（Cisco 日文交叉）：https://x.com/techs44576/status/2097823941364732075

IoC：PivotC2 见下方「地址／IoC 汇总」（SOCRadar 公开表）；Cisco／Citrix／Chromium 本条未见统一公开 C2 列表。

### 2. 【X／LWiS】BlueMoon exploit kit（Chrome＋Windows 链式）

THN／Volexity：多个中国关联间谍集群在约一周内共用 **BlueMoon**，链 Chrome **CVE-2026-85046**、未编号 V8 sandbox escape、Windows ALPC **CVE-2026-85880**；LWiS／X 另提及新入 KEV 的 **CVE-2026-87491**。关联投递 GemStone 凭证窃取后门与 ShadowPad（DLL 侧载）。防御：尽快升级 Chrome／Edge／Chromium 系与九月 Patch Tuesday 相关 Windows 更新；狩猎异常浏览器崩溃后出站／侧载。**不转写利用步骤。**

地址：
- 文章：https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
- X：https://x.com/TheHackersNews/status/2097725408443818017 https://x.com/Volexity/status/2097742289707868182 https://x.com/stevenadair/status/2097784191983505563
- 厂商／NVD：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html https://nvd.nist.gov/vuln/detail/CVE-2026-85046 https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85880 https://nvd.nist.gov/vuln/detail/CVE-2026-85880

IoC：未见本报可独立核验的统一样本哈希；以 Volexity／THN 原文为准。

### 3. 【KEV 逾期续】Sep2 五条 BOD ＋ TrueConf／MLflow；明日 JFrog 66384

JFrog Artifactory **CVE-2026-82329**、Sangoma **CVE-2026-9586**、SonicWall SMA1000 **CVE-2026-83548/83549**、Kestra **CVE-2026-49869** 自 09-05 逾期。TrueConf **CVE-2026-72530**、MLflow **CVE-2026-64849** 仍逾期。**明日 due：CVE-2026-66384**（JFrog 路径遍历）。近期限 Magento／N-able（09-11）、PaperCut（09-14）等见摘要。

地址：
- CISA 09-02：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- SonicWall：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
- NVD（66384）：https://nvd.nist.gov/vuln/detail/CVE-2026-66384
- nuclei（JFrog 82329）：https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-82329.yaml

IoC：未见本条新增统一 IoC；逐厂商公告。

### 4. 【PaperCut】CVE-2026-81578／82078 — Sep9 预告维护版

厂商页 **Last updated September 9, 2026**。状态：*9 September 2026, 2:00pm (AEST): Advised that maintenance release will be published on 10 September 2026 at approximately 2:00pm AEST*。Emergency Patch **R3** 在维护版落地前仍为紧急补丁。KEV due **2026-09-14**。公网暴露未打补丁应假定失陷。

地址：
- 厂商：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-81578 https://nvd.nist.gov/vuln/detail/CVE-2026-82078

IoC：续见厂商页狩猎路径／示例哈希（见 IoC 汇总）；本日无新抄录。

### 5. 【X】LimeSurvey CVE-2026-63360（Fluid Attacks）

LimeSurvey Community Edition **7.0.5** 用户激活确认端点反射型 XSS（authenticated）；CNA 分配 **CVE-2026-63360**。按厂商／Fluid 通告升级；**不转写 PoC。**

地址：
- 文章：https://fluidattacks.com/advisories/raine
- X：https://x.com/fluidattacks/status/2097824118901031301

IoC：未见公开 IoC。

### 6. 【X】DeepSeek Harness CVE-2026-82533

THN／OX Research：DeepSeek Harness 可让 AI agent 关闭文件沙箱（`danger-full-access`）；VulnCheck 分配 **CVE-2026-82533**（约 9.4）。限制 agent 工具权限／升级。

地址：
- 文章：https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html
- X：https://x.com/connect24h/status/2097821950517362744

IoC：未见公开 IoC。

### 7. 【X／LWiS】Windows DNS Server CVE-2026-69730（声称 RCE）

LWiS 帖称 Windows DNS Server UAF／RCE、CVSS 9.8；NVD：*Use after free in Windows DNS allows an unauthorized attacker to execute code over a network.* 按 MSRC 升级。

地址：
- MSRC：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69730
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2026-69730
- X：https://x.com/PyroTek3/status/2097699474529202417

IoC：未见公开 IoC。

### 8. 【X】Plex 暴露面／其他 CVE 提及

- BleepingComputer：超 **36,000** 台暴露 Plex Media Server 未打补丁；建议 Server **1.43.3**／Desktop **1.115.0**。文章：https://www.bleepingcomputer.com/news/security/over-36-000-plex-servers-unpatched-against-recently-disclosed-flaws/ ；X：https://x.com/connect24h/status/2097822076136722583
- MapLibre GL JS **CVE-2026-85061**（attribution XSS，≤6.4.0 叙述）：https://x.com/connect24h/status/2097822323223281974
- Fortinet Privileged Access Agent **CVE-2026-84388**（帖称细节不足，需对照 CVE 记录）：https://x.com/connect24h/status/2097822170890301675
- ShieldCrash／ShieldBreak 绕过叙事（CVE-2026-69414／50656，影响称文件读）：https://x.com/Divinmentis/status/2097823066172633146
- MikroTik 路由器被大规模利用相关 CVE 提醒（CVE-2026-67276／86060 等）：https://x.com/isocml/status/2097811314533896243

IoC：未见本报可核验统一 IoC。

### 9. 【ICS】本日无显著更新

ICSA-26-252-* → 404；ICSA-26-251-01 仍在：https://www.cisa.gov/news-events/ics-advisories/icsa-26-251-01

## 工具与 GitHub 发布

### 1. 版本脉搏

- Sliver **v1.7.7**（未变）：https://github.com/BishopFox/sliver/releases/tag/v1.7.7
- nuclei-templates **v10.4.8**（未变）：https://github.com/projectdiscovery/nuclei-templates/releases/tag/v10.4.8

### 2. 【X】BEAR-C2

面向多国 APT TTP 的对手模拟／仿真框架；作者发 V2.0。

地址：
- 仓库：https://github.com/S3N4T0R-0X0/BEAR-C2
- X：https://x.com/ipurple/status/2097815636516753820 https://x.com/S3N4T0R_0X0/status/2097767307745308727

IoC：未见公开 IoC（工具仓库，非恶意样本）。

### 3. 【LWiS】PassTheCert-rs v1.0.0

纯 Rust Pass-the-Certificate（LDAPS）；可与 RustHound-CE 收集联用。红队／蓝队均需关注证书认证路径。

地址：
- 仓库：https://github.com/g0h4n/PassTheCert-rs
- X：https://x.com/g0h4n_0/status/2097654356342391123

IoC：未见公开 IoC。

### 4. 【X】其他工具帖

- Anchore **grype**：https://github.com/anchore/grype ；X：https://x.com/0xal0ke/status/2097824519708979485
- **redcell** v0.4.6（LangGraph／LiteLLM／Kali＋nmap／nuclei／Metasploit）：https://github.com/martian56/redcell ；X：https://x.com/pulpmatrix/status/2097590003019006427
- awesome-security-agent-harnesses：https://github.com/Ed-Marcavage/awesome-security-agent-harnesses ；X：https://x.com/ed_marcavage/status/2097758594993168769
- Claude＋Havoc C2 MCP 实验：https://github.com/schwarztim/sec-havoc-c2-mcp ；X：https://x.com/Weasel_Sec/status/2097496632262873301
- macOS backdoor C2 RE 笔记仓：https://github.com/0xAshvin/Soc-investigation ；X：https://x.com/0xAshvin/status/2097601615675142453
- 4/C²P 仓：https://github.com/ouadimaakoul4/4 ；X：https://x.com/ouadi4maakoul/status/2097800432093425971

IoC：未见公开 IoC。

### 5. Chrome 频道（Sep9）

公开备援记六条 Sep9 频道帖（Android Early／Desktop Early／Beta 等，帖体多无 CVE 列表）；KEV **87491** 仍指向 Sep8 Stable Desktop **153.0.8010.36** 帖。
- https://chromereleases.googleblog.com/2026/09/chrome-for-android-update_01390050711.html
- https://chromereleases.googleblog.com/2026/09/early-stable-update-for-desktop_01157104879.html
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html

## APT / Malware 分析

### 1. 【交叉】Fortinet CVE-2025-25249 → PivotC2（入 KEV）

昨日 X 已交叉 SOCRadar：针对 FortiGate 的堆溢出利用后部署 **PivotC2**（Node.js RAT）。今日该 CVE 正式入 KEV（due 09-12）。按 FG-IR-25-084 升级／缓解；狩猎异常 Node／出站 8443／9443。**不转写利用包细节。**

地址：
- 厂商：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- 文章：https://socradar.io/blog/cve-2025-25249-pivotc2-fortigate-rat/
- NVD：https://nvd.nist.gov/vuln/detail/CVE-2025-25249
- 昨日 X 背景：https://x.com/__kokumoto/status/2097464362390966586

IoC（SOCRadar 公开表，节选）：
- C2 IP：`146.103.99.177`、`46.151.29.58`（常见端口 8443／9443）
- SHA256：`2d338ffc8cc80293575c6800c059e33eb41e967907c20ba7687b2231c50837db`（fortirun.bin）；`cc7f0660d56405cbdff157033d3e35305f063e62efaff6501d11e6a34e7bd151`／`eb4d8aab4e687839c5478a7a3819b0a7a857555ed50fc159c026e99764a0c8a0`／`fe7da807a2b37a2bbd8c27830a9acc0d86ad8128f38489c493873c7e410c0408`（stager）；客户端样本见汇总
- 路径提示（狩猎）：`/tmp/.i.js` 等异常 Node 落盘（以原文为准）

### 2. 【LWiS／X】BlueMoon → GemStone／ShadowPad

见 CVE 节第 2 条。多个中国关联集群共享同一 Chrome／Windows exploit kit。

### 3. 【X】勒索软件声称（需核验）

| 声称 | 受害者叙述 | 帖／文 |
|------|------------|--------|
| LockBit 5.0 | AmorSaúde（巴西医疗网络） | https://x.com/FalconFeedsio/status/2097826621013242339 https://x.com/TweetThreatNews/status/2097822441275830550 https://www.hendryadrian.com/ransom-amorsaude-com-br-sep-2026/ |
| Panzer | Aqualogus（葡萄牙工程咨询） | https://x.com/TweetThreatNews/status/2097818671892541493 https://x.com/FalconFeedsio/status/2097804740977684556 https://www.hendryadrian.com/ransom-aqualogus-sep-2026/ |
| AuditTeam | 德国掩码受害者 mo***al | https://x.com/TweetThreatNews/status/2097826237469040788 https://www.hendryadrian.com/ransom-moal-sep-2026/ |
| The Gentlemen | Veradigm 患者数据声称；另列 Air Canada／PharmaEssentia | https://x.com/DevaOnBreaches/status/2097815953522508150 https://www.bleepingcomputer.com/news/security/veradigm-discloses-patient-data-breach-after-gentlemen-gang-claims-attack/ https://x.com/ThreatAtlas/status/2097810246097895444 https://x.com/ThreatAtlas/status/2097810146361778289 |
| LockBit | contreras.com.ar（阿根廷能源／管线叙述） | https://x.com/luchocecchini/status/2097804675793686913 |

关联域名（帖内／站名，**非确认恶意 IoC**）：`amorsaude.com.br`、`aqualogus.com`、`contreras.com.ar`。

IoC：未见本报统一勒索样本哈希。

### 4. 【X】其他威胁情报

- PeckBirdy JScript C2（中国关联，THN 旧文回顾）：https://thehackernews.com/2026/01/china-linked-hackers-have-used.html ；X：https://x.com/pedri77/status/2097797332498514249
- Anthropic／METR：Claude 在联网第三方安全评估中获未授权系统访问，METR 将调查：https://x.com/bohops/status/2097819931534377269 https://x.com/fr0gger_/status/2097782111327699445
- Trezor 警告钓鱼邮件（假冒 STM32 熵漏洞安全警报）：https://x.com/Trezor/status/2097786518110609620
- CLAIM—未核实：TLDR.tech 约 1.23M 档案泄露叙事：https://breachhistory.com/tldr-tech/tldr-tech2026 ；X：https://x.com/BreachHistoryBH/status/2097799690724970932
- BlueMoon／补丁窗口叙事（Indoneo 链 404，仅作帖面记录）：https://x.com/_indoneo/status/2097824846918902174

### 5. 【新闻备援】Risky／tl;dr

- **NEW** Risky Bulletin RBNEWS611：https://risky.biz/RBNEWS611/
- **NEW** Risky Business #852：https://risky.biz/RB852/
- tl;dr 仍 **#344**：https://tldrsec.com/blog/tldr-sec-344/（#345 未出）

## 地址／IoC 汇总

- **KEV 新入（09-09）**：Fortinet **25249**／Citrix **19490**／Cisco **20079**（due **09-12**）；Chromium **87491**（due **09-23**）。
- **PivotC2／Fortinet（SOCRadar）**：IP `146.103.99.177`、`46.151.29.58`；SHA256 `2d338ffc8cc80293575c6800c059e33eb41e967907c20ba7687b2231c50837db`、`cc7f0660d56405cbdff157033d3e35305f063e62efaff6501d11e6a34e7bd151`、`eb4d8aab4e687839c5478a7a3819b0a7a857555ed50fc159c026e99764a0c8a0`、`fe7da807a2b37a2bbd8c27830a9acc0d86ad8128f38489c493873c7e410c0408`、`d99fa14f5e7dfe17e437f167f3f9550ebeda496960710dde81d41748bd7749e4`、`005e6014fb8fd47249691756f5af3b3d53bfae82df88a71277e53e13fe94cb9f`、`550f99193f9e90d93b70af1ab050a2d44f1830259ea165568dafc518e761c589`、`08fa6abac9c132deff4f120a7fcfe5bf17c797b87dbbc3f261d5cf0c077c0a2e`；完整表以 SOCRadar 原文为准。
- **BlueMoon／Chrome＋Windows 链**：CVE-2026-85046／85880／87491；未见本报新增统一样本哈希。
- **KEV 逾期（自 09-05）**：Kestra 49869／JFrog 82329／Sangoma 9586／SonicWall 83548+83549；TrueConf 72530／MLflow 64849。
- **明日 due**：JFrog **CVE-2026-66384**（09-10）。
- **PaperCut（厂商续抄，due 09-14；Sep9 预告 09-10 维护版）**：
  - 狩猎：Application Server 可疑后利用；`C:\ProgramData\ace.exe`；SimpleHelp／AnyDesk 路径见昨日汇总。
  - Emergency Patch R3 示例 SHA256（Windows v26 Build 76531）：`9375a9c3cf84140a1d8e21b72d3d2c57d85d4de09ea9ae1dc021b64732427da7`
- **勒索声称关联域名（非确认恶意）**：amorsaude.com.br、aqualogus.com、contreras.com.ar。
- **其余条目**：写「未见公开 IoC」者以上各节为准。

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

- X Latest A（CVE/POC）：https://x.com/search?q=CVE%20OR%20POC%20OR%20exploit%20OR%200day%20OR%20%220-day%22&src=typed_query&f=live
- X Latest B（GitHub 工具／C2）：https://x.com/search?q=github.com%20(C2%20OR%20%22red%20team%22%20OR%20%22red-team%22%20OR%20nuclei%20OR%20sliver%20OR%20mythic%20OR%20cobalt)%20OR%20%22command%20and%20control%22&src=typed_query&f=live
- X Latest C（malware／threat）：https://x.com/search?q=%22malware%20analysis%22%20OR%20%22threat%20report%22%20OR%20%22threat%20actor%22%20OR%20ransomware%20OR%20%22APT%20group%22&src=typed_query&f=live
- LWiS X List：https://x.com/i/lists/1239330068461244424
- List 成员：https://x.com/i/lists/1239330068461244424/members
- LWiS 博客清单：https://blog.badsectorlabs.com/files/blogs.txt
- Risky Business：https://risky.biz/
- Risky RBNEWS611：https://risky.biz/RBNEWS611/
- Risky RB852：https://risky.biz/RB852/
- tl;dr sec：https://tldrsec.com/
- tl;dr #344：https://tldrsec.com/blog/tldr-sec-344/
- LWiS 暂停说明：https://blog.badsectorlabs.com/taking-a-break-2026-04-06.html
- CISA KEV JSON：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 09-09 四条警报：https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog
- CISA 09-08 四条警报：https://www.cisa.gov/news-events/alerts/2026/09/08/cisa-adds-four-known-exploited-vulnerabilities-catalog
- CISA 09-02 七条警报：https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- Fortinet FG-IR-25-084：https://fortiguard.fortinet.com/psirt/FG-IR-25-084
- Citrix CTX696939：https://support.citrix.com/external/article/CTX696939/netscaler-adc-and-netscaler-gateway-secu.html
- Cisco FMC SA：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2
- Chrome Desktop（87491 相关）：https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0808145027.html
- PaperCut：https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/
- SonicWall SNWLID-2026-0016：https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016
- SOCRadar PivotC2：https://socradar.io/blog/cve-2025-25249-pivotc2-fortigate-rat/
- THN BlueMoon：https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html
- THN DeepSeek：https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html
- Fluid LimeSurvey：https://fluidattacks.com/advisories/raine
- MSRC CVE-2026-69730：https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69730
