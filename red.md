# 红队作战架构地图 v1.1

**从基础设施到攻击影响的综合操作手册**

---

## 攻击链图例

**基础设施** → **初始访问** → **执行** → **规避** → **横向移动/持久化** → **收集** → **数据外传**

### 操作流程：钓鱼 → 执行 → 规避 → 移动 → 收集 → 外传

---

## 端到端攻击链

展示红队操作如何从基础设施连接到最终影响的完整攻击链。

### 经典钓鱼 → Beacon → 域管理员
构建 C2 + 重定向器 → 钓鱼 → HTML 走私 → ISO/LNK → 执行 → Shellcode 加载器 → beacon → C2 回连 → AD 攻击 → 域管理员权限

### EvilGinx MFA 绕过 → 令牌窃取 → 云访问
设置 EvilGinx 代理 → 诱饵邮件 → 受害者输入凭据 + MFA → 捕获 → 会话 cookie 被窃取 → 重放 → 以用户身份认证 → 横向移动 → M365 / Azure / 本地网络

### 加载器 → 解钩 → 注入 → Beacon（EDR 绕过链）
自定义加载器（Rust/C）→ 修补 AMSI → AMSI + ETW 绕过 → 新鲜 ntdll → 解除 EDR 钩子 → 系统调用注入 → 进程注入 → 睡眠混淆 → 稳定 C2 beacon

### DLL 侧加载 → 签名二进制 → 持久化
找到签名 EXE + DLL → 制作 DLL → 代理 DLL（导出）→ 放置配对文件 → 签名 EXE 加载我们的 DLL → 持久化 → 注册表运行键 / 计划任务 → beacon → 持久化 C2

### 横向移动 → 枢纽 → 外传
转储凭据（LSASS/DPAPI）→ PtH / PtT → 移动到高价值目标 → SMB 管道 → 部署 beacon（子进程）→ Snaffler → 收集敏感数据 → 分阶段外传 → HTTPS C2 外传

### 域前置 → CDN → C2（隐蔽通道）
分类域名 + SSL → CDN 配置 → CloudFront / Azure CDN → Host 头 → TLS SNI = 合法域名 → 路由到 C2 → 流量看起来合法 → beacon → 隐蔽 C2 通道

---

## C2 框架深度解析

命令与控制是任何红队行动的支柱。

### Cobalt Strike
**行业标准 — Beacon 载荷、可塑 C2、成熟生态系统**

- **Beacon**：分阶段/无阶段，HTTP/HTTPS/DNS/SMB/TCP 监听器
- **可塑 C2**：完全控制网络指标 — 模仿任何 HTTP 流量模式
- **BOFs（Beacon 对象文件）**：在 Beacon 内存中运行编译的 C 代码 — 无需 fork & run
- **睡眠掩码**：在睡眠期间加密内存中的 Beacon — 规避内存扫描器
- **OPSEC 问题**：默认配置被大量特征化 — 必须自定义配置文件
- **关键功能**：spawn & inject、jump（横向）、mimikatz 集成、socks 代理
- **Arsenal Kit**：修改工件/资源/睡眠掩码/进程注入行为

### Havoc
**开源、现代 C2 — Demon 代理，通过 Python/C 可扩展**

- **Demon 代理**：位置无关，原生支持间接系统调用
- **睡眠混淆**：内置 Ekko/Zilean — 在睡眠期间加密内存中的代理
- **无 fork & run**：默认内联执行 — 比 CS fork & run 更好的 OPSEC
- **可扩展**：Python API 用于自定义命令、模块和后渗透
- **监听器**：HTTP/HTTPS，可自定义配置文件
- **免费开源** — 积极开发，社区不断增长

### Sliver
**BishopFox 开源 — Go 语言植入体，多协议**

- **植入体**：编译的 Go 二进制文件 — 跨平台（Windows/Linux/macOS）
- **协议**：mTLS、WireGuard、HTTP(S)、DNS — 默认全部加密
- **多人协作**：多个操作员、基于角色的访问、实时协作
- **Armory**：扩展/别名包管理器（BOFs、.NET 程序集）
- **OPSEC 注意**：Go 植入体较大（~10MB+），运行时被某些 EDR 特征化

### Mythic
**协作式多代理 C2 平台 — 容器化架构**

- **多代理**：Apollo（C#）、Athena（.NET）、Poseidon（Go）、Medusa（Python）、Merlin
- **容器化**：每个代理/C2 配置文件在 Docker 中运行 — 模块化，易于扩展
- **UI**：基于 Web 的仪表板，具有任务跟踪、文件浏览器、MITRE ATT&CK 映射
- **自定义代理**：使用 Mythic 代理框架以任何语言构建自己的代理

### Brute Ratel C4
**商业对抗模拟 — Badger 代理，专注于 EDR 规避**

- **Badger**：从头开始设计用于 EDR 规避
- **系统调用**：默认间接系统调用 — 完全避免用户模式钩子
- **睡眠混淆**：内置回调期间的内存加密
- **堆栈欺骗**：返回地址欺骗以规避基于堆栈的检测
- **LDAP 哨兵**：通过 LDAP 协议的 C2 — 独特的隐蔽通道

---

## 红队基础设施

你的基础设施就是你的 OPSEC。糟糕的设置 = 行动暴露。

### 基础设施架构

```
操作员机器
└── VPN / Tor / 跳板机
    └── C2 团队服务器（VPS）
        ├── HTTPS 重定向器（nginx/Apache 反向代理）
        │   ├── CDN 层（CloudFront / Azure CDN）
        │   └── 域前置（SNI = legit.com，Host: = evil.com）
        ├── DNS 重定向器（socat UDP 中继）
        ├── SMB 管道监听器（内部枢纽）
        └── 载荷托管（S3 / Azure Blob）

钓鱼基础设施（与 C2 分离！）
├── SMTP 服务器（Postfix + DKIM + SPF + DMARC）
├── GoPhish / 自定义（活动管理）
├── EvilGinx（MFA 绕过的透明代理）
└── 登陆页面（克隆门户 • HTTPS • 分类域名）
```

### 重定向器
**永远不要暴露你的团队服务器 — 始终通过重定向器代理**

- **HTTPS 重定向器**：nginx 反向代理 — 按 User-Agent、URI、头部过滤
- **Apache mod_rewrite**：基于请求属性的条件转发
- **socat**：用于 DNS 监听器的简单 TCP/UDP 中继
- **CDN 前置**：CloudFront、Azure CDN — C2 流量看起来像 CDN HTTPS
- **销毁协议**：如果重定向器被标记 → 更换 VPS + 域名，团队服务器不受影响

### 可塑 C2 配置文件
**塑造你的 C2 流量，使其看起来像合法服务**

- **目的**：定义 Beacon 如何通信 — HTTP 头、URI、编码、时间
- **模仿**：jQuery、Amazon、Google API、Microsoft 更新流量
- **关键设置**：`set sleeptime`、`set jitter`、`set useragent`
- **JARM 指纹**：默认 CS JARM 被特征化 — 使用自定义 TLS 或前置 nginx

---

## 初始访问

### HTML 走私
**通过 HTML/JS 传递载荷 — 绕过邮件网关**

- 将载荷作为 base64 或加密 blob 嵌入 HTML 文件中
- JavaScript 在浏览器中打开时解码并提供文件下载
- **绕过**：邮件附件扫描器只看到 HTML 文件
- **Blob 方法**：`window.URL.createObjectURL(new Blob([bytes]))`

### 无宏载荷
**Microsoft 默认阻止 VBA 宏 — 后宏时代载体**

- **LNK 文件**：带有 PowerShell/cmd 命令行的快捷方式
- **ISO / IMG / VHD**：自动挂载的容器文件 — 内容绕过 MOTW
- **OneNote（.one）**：将脚本、HTA 或 EXE 作为附件嵌入
- **CHM（编译的 HTML 帮助）**：通过 hh.exe 执行嵌入的脚本
- **XLL（Excel 加载项）**：Excel 加载的原生 DLL — 打开时执行代码

### 凭据钓鱼（AitM）
**中间人代理 — 捕获凭据和 MFA 令牌**

- **EvilGinx 3**：透明反向代理 — 位于受害者和真实登录页面之间
- 捕获用户名、密码和 **MFA 后的会话 cookie**
- **MFA 绕过**：适用于 TOTP、推送通知、SMS — 只有 FIDO2/WebAuthn 有抵抗力
- **Cookie 重放**：将窃取的会话 cookie 导入浏览器 → 完全认证的会话

### 设备代码钓鱼
**绕过包括 FIDO2 在内的 MFA — 捕获 OAuth 令牌**

- **动态代码生成**：当受害者登陆页面时生成设备代码
- **流程**：受害者在 `microsoft.com/devicelogin` 输入代码 → 使用 MFA 认证 → 攻击者捕获令牌
- **绕过 FIDO2**：设备代码流捕获完整的访问+刷新令牌
- **持久化**：捕获的刷新令牌在密码更改后仍然有效

---

## 载荷开发

### Shellcode 加载器
**解密、分配和执行 shellcode 的代码**

- **基本流程**：读取加密的 shellcode → 解密 → 分配 RWX 内存 → 执行
- **更好的方法**：NtAllocateVirtualMemory（系统调用）→ NtWriteVirtualMemory → NtCreateThreadEx
- **回调执行**：使用 Windows 回调触发 shellcode（EnumFonts、CreateFiber）
- **语言**：C/C++（最小）、Rust（安全 + 小）、Nim（新兴）、Go（大但跨平台）

### DLL 侧加载
**滥用签名二进制文件的 DLL 搜索顺序**

- **概念**：签名的 EXE 查找 DLL → 将你的 DLL 放在它首先搜索的位置
- **代理 DLL**：将所有原始导出转发到真实 DLL + 添加恶意代码
- **查找候选**：`Spartacus`、`DLLSpy`、Process Monitor
- **为什么有效**：签名的 EXE 加载你的 DLL — EDR 看到受信任的进程

---

## 防御规避

### EDR 检测层和绕过

**层 1：静态特征**
- 磁盘上的 AV/YARA 规则 → 绕过：加密、混淆、打包

**层 2：用户态钩子**
- ntdll.dll 钩子 → 绕过：解钩、直接系统调用

**层 3：ETW 遥测**
- EtwEventWrite → 绕过：修补为 ret、NtTraceEvent 钩子

**层 4：内核回调**
- 进程/线程/映像加载通知 → 无法从用户态绕过

**层 5：内存扫描**
- 定期内存扫描 → 绕过：睡眠混淆、堆加密

**层 6：行为/调用堆栈**
- 调用堆栈分析 → 绕过：堆栈欺骗、返回地址覆盖

### AMSI 绕过
**反恶意软件扫描接口 — 在运行时扫描 PowerShell、.NET、VBScript**

- **修补 AmsiScanBuffer**：用 `ret` 覆盖前几个字节 — 所有扫描返回干净
- **硬件断点**：在 AmsiScanBuffer 上设置 BP，在异常处理程序中修改参数
- **反射**：通过 .NET 反射将 `amsiContext` 字段设置为 null

### 直接/间接系统调用
**直接调用内核 — 绕过所有用户态钩子**

- **直接系统调用**：在代码中嵌入系统调用指令 — 永远不触及 ntdll.dll
- **间接系统调用**：跳转到 ntdll.dll 内部的系统调用指令
- **SysWhispers3**：生成具有多种绕过选项的系统调用存根
- **HellsGate**：在运行时动态解析系统调用号

### 睡眠混淆
**在睡眠期间加密内存中的植入体**

- **问题**：C2 植入体 90%+ 的时间在睡眠 — 内存扫描器寻找特征
- **Ekko**：使用 `CreateTimerQueueTimer` 链接 ROP：RW → 加密 → 睡眠 → 解密 → RX
- **Foliage**：基于 APC 的睡眠混淆
- **Deathsleep**：在睡眠期间完全取消映射植入体内存

---

## 进程注入技术

### 经典注入（VirtualAllocEx）
**教科书方法 — 被大量检测**

1. `OpenProcess` 使用 PROCESS_ALL_ACCESS
2. `VirtualAllocEx` — 在远程进程中分配 RWX 内存
3. `WriteProcessMemory` — 写入 shellcode
4. `CreateRemoteThread` — 执行 shellcode

### 模块踩踏/幽灵 DLL
**用 shellcode 覆盖合法 DLL 的 .text 部分**

- **问题**：无支持内存中的 shellcode 可疑
- **模块踩踏**：加载良性 DLL → 用 shellcode 覆盖其 .text
- 内存区域现在显示为由合法 DLL 支持

### 无线程注入
**无线程创建或 APC 队列 — 钩子 API 以触发 shellcode**

- 在目标进程中对定期调用的 API 放置钩子
- 当目标自然调用被钩住的 API 时，shellcode 触发
- **无线程创建**：无 CreateRemoteThread、无 APC、无线程劫持

---

## 持久化机制

### 注册表运行键
- **HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run**：每用户，无需管理员
- **UserInitMprLogonScript**：登录时执行，很少被监控

### COM 对象劫持
- 为仅存在于 HKLM 中的 CLSID 创建 HKCU 键 → 加载你的 DLL
- **OPSEC**：极其隐蔽 — 由正常系统活动触发

### 计划任务
- **基于 COM 的创建**：使用 ITaskService COM 接口 — 避免 schtasks.exe 日志记录
- **隐藏任务**：删除 SD 注册表值以使其不可见

### DLL 侧加载持久化
- **最 OPSEC 友好**：结合签名二进制信任和 DLL 劫持
- 将签名 EXE + 代理 DLL 放到持久位置
- 通过计划任务、运行键或服务触发

---

## 凭据访问

### LSASS 凭据转储
- **直接转储**：`procdump -ma lsass.exe lsass.dmp`
- **Comsvcs.dll**：`rundll32 comsvcs.dll MiniDump PID file full`
- **离线解析**：`pypykatz lsa minidump lsass.dmp`
- **OPSEC**：打开 LSASS 句柄触发 ObRegisterCallbacks

### DPAPI 凭据收集
- **Chrome/Edge 密码**：SQLite DB + DPAPI 加密的 AES 密钥
- **Chrome/Edge cookie**：会话 cookie → 绕过 MFA
- **工具**：`DonPAPI`、`SharpDPAPI`、`dploot`

### Kerberos 票据收集
- `Rubeus dump` — 从当前登录会话提取所有票据
- `Rubeus triage` — 列出跨会话的所有可访问票据
- **ccache 文件**：复制并与 impacket 工具一起使用

---

## 横向移动

### 基于 SMB 的执行
- **PsExec**：上传服务二进制 → 创建/启动服务
- **smbexec**：使用 cmd.exe 和基于 echo 的输出 — 无二进制上传
- **检测**：服务创建（7045）、命名管道创建

### WMI 执行
- `wmiexec.py`：通过 WMI + SMB 输出重定向的半交互式 shell
- **无二进制上传**：命令通过 WMI 提供程序原生执行
- **端口**：TCP 135（RPC）+ 动态高端口

### WinRM / PowerShell 远程处理
- `evil-winrm`：完整的交互式 PS 会话
- **Enter-PSSession**：原生 PowerShell 远程处理
- **OPSEC**：常见的管理工具 — 与正常管理活动混合

### 哈希传递/票据传递
- **哈希传递**：直接使用 NT 哈希通过 NTLM 认证
- **票据传递**：注入窃取的 Kerberos TGT/TGS
- **过哈希**：使用 NT 哈希请求 Kerberos TGT

---

## 外传和数据暂存

### HTTPS C2 通道
- 通过 Beacon 下载文件 — 数据通过现有 C2 通道流动
- **分块**：大文件分成小块
- **时间**：将外传速率与正常 C2 回调间隔匹配

### DNS 外传
- 将数据编码为子域 — `base64data.evil.com`
- **dnscat2**：通过 DNS 的完整 C2
- **DOH**：通过 HTTPS 向 Cloudflare/Google 发送 DNS 查询

### 云存储外传
- **OneDrive / SharePoint**：使用受害者自己的 M365 令牌
- **Google Drive**：OAuth 令牌或服务帐户上传
- **OPSEC**：使用组织现有的云提供商

---

## OPSEC 注意事项

### 按操作的检测风险

| 操作 | 风险级别 | 检测来源 |
|------|---------|---------|
| 发送钓鱼邮件 | 低 | 邮件网关、用户报告 |
| C2 beacon 回连 | 低-中 | 网络 IDS、JA3/JARM 指纹 |
| 进程注入 | 高 | 内核回调、ETW、Sysmon |
| LSASS 访问 | 非常高 | ObRegisterCallbacks、Sysmon 10 |
| PsExec 横向移动 | 高 | 服务创建 7045 |
| DCSync | 非常高 | 事件 4662、DRS 复制 |

### 常见错误
- 默认 C2 配置文件 — 立即被标记
- 直接运行 Mimikatz — 最被检测的工具
- 到处使用 PsExec — 明显的横向移动
- 无睡眠混淆 — 被内存扫描检测
- 直接触及 LSASS — #1 EDR 警报触发器

### 保持安静
- **利用现有工具**：使用系统上已有的合法工具
- **内联执行**：运行 BOFs 而不是 fork & run
- **长时间睡眠**：60 秒以上睡眠，高抖动（50%+）
- **仅工作时间**：在工作时间内操作

---

*本文档是红队操作的综合参考。所有技术仅应在具有适当法律授权的授权安全评估中使用。*
