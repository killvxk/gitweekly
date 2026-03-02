# =========================================
# MSYS2 自动安装与配置脚本（带管理员检测）
# =========================================
# 必须以管理员权限运行！
# =========================================

# --- 检测当前是否为管理员 ---
$principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "❌ 错误：此脚本需要以管理员身份运行！" -ForegroundColor Red
    Write-Host "💡 请右键 PowerShell，选择 '以管理员身份运行' 后再执行此脚本。" -ForegroundColor Yellow
    Write-Host ""
    Pause
    exit 1
}

Write-Host "✅ 已检测到管理员权限，开始执行安装流程..." -ForegroundColor Green
Write-Host ""

# =========================================
# === 1. 下载 MSYS2 安装包 ===
# =========================================
$msys2Url  = 'https://github.com/msys2/msys2-installer/releases/download/nightly-x86_64/msys2-base-x86_64-latest.sfx.exe'
$msys2File = "$env:TEMP\msys2.exe"

Write-Host "📦 下载 MSYS2 安装包..."
(New-Object System.Net.WebClient).DownloadFile($msys2Url, $msys2File)

# =========================================
# === 2. 计算 SHA256 哈希 ===
# =========================================
Write-Host "🔑 计算文件哈希..."
$hash = Get-FileHash $msys2File -Algorithm SHA256
$hash | Format-List

# =========================================
# === 3. 解压到 C:\msys64 ===
# =========================================
Write-Host "📂 解压安装文件..."
if (Test-Path "C:\msys64") {
    Write-Host "⚠️ 目标目录 C:\msys64 已存在，略过解压。"
} else {
    & $msys2File -y -oC:\
}

# =========================================
# === 4. 删除安装包 ===
# =========================================
Write-Host "🧹 清理安装包..."
Remove-Item $msys2File -Force

# =========================================
# === 5. 添加 Mandatory ASLR 排除项 ===
# =========================================
Write-Host "🔒 为可执行文件添加 ASLR 排除项..."
Get-ChildItem -Recurse -File -Path 'C:\msys64\*.exe' | ForEach-Object {
    try {
        Set-ProcessMitigation -Name $_.Name -Disable ForceRelocateImages -ErrorAction SilentlyContinue
    } catch {
        Write-Warning "无法为 $($_.Name) 设置 Process Mitigation。"
    }
}

# =========================================
# === 6. 初始化 MSYS2 ===
# =========================================
Write-Host "🚀 初始化 MSYS2 环境..."
& "C:\msys64\usr\bin\bash.exe" -lc " "

# =========================================
# === 7. 更新 MSYS2 (core) ===
# =========================================
Write-Host "⬆️ 更新 MSYS2 核心包..."
& "C:\msys64\usr\bin\bash.exe" -lc "pacman --noconfirm -Syuu"

# =========================================
# === 8. 更新 MSYS2 (normal) ===
# =========================================
Write-Host "⬆️ 再次更新 MSYS2..."
& "C:\msys64\usr\bin\bash.exe" -lc "pacman --noconfirm -Syuu"

# =========================================
# === 9. 安装编译工具链 ===
# =========================================
Write-Host "🛠️ 安装编译工具链 (GCC + Clang + Base-devel)..."
& "C:\msys64\usr\bin\bash.exe" -lc "pacman --noconfirm -Syu --needed base-devel vim nasm mingw-w64-ucrt-x86_64-toolchain mingw-w64-x86_64-toolchain mingw-w64-i686-toolchain mingw-w64-ucrt-x86_64-clang mingw-w64-x86_64-clang mingw-w64-clang-x86_64-toolchain"

# =========================================
# === 10. 设置环境变量 & 测试工具链 ===
# =========================================
Write-Host "⚙️ 设置环境变量并检测编译器..."
$env:CHERE_INVOKING = 'yes'
$env:MSYSTEM = 'UCRT64'
& "C:\msys64\usr\bin\bash.exe" -lc "gcc --version && clang --version"

# =========================================
# === 完成 ===
# =========================================
Write-Host ""
Write-Host "✅ MSYS2 安装与配置已全部完成！" -ForegroundColor Green
Write-Host "🎉 你现在可以使用 MSYS2 构建环境。" -ForegroundColor Cyan
