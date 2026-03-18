# CSDN 博客发布工具 - PowerShell 封装
# 用法：.\publish-to-csdn.ps1 -MarkdownFile "C:\path\to\blog.md"

param(
    [Parameter(Mandatory=$true)]
    [string]$MarkdownFile,
    
    [switch]$CheckChrome,
    
    [switch]$StartChrome
)

$ErrorActionPreference = "Stop"
$CSDN_TOOLS_PATH = "C:\blog-auto-publishing-tools"
$CHROME_PORT = 9222

function Write-Color {
    param([string]$Text, [string]$Color = "White")
    Write-Host $Text -ForegroundColor $Color
}

function Test-ChromeRunning {
    $port = Get-NetTCPConnection -LocalPort $CHROME_PORT -ErrorAction SilentlyContinue
    return $null -ne $port
}

function Start-ChromeDebug {
    Write-Color "🚀 启动 Chrome 调试模式..." "Cyan"
    $chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    if (-not (Test-Path $chromePath)) {
        throw "Chrome 未安装：$chromePath"
    }
    
    $args = @(
        "--remote-debugging-port=$CHROME_PORT",
        "--user-data-dir=$env:LOCALAPPDATA\Google\Chrome\User Data",
        "--no-first-run"
    )
    
    Start-Process $chromePath -ArgumentList $args -WindowStyle Hidden
    Start-Sleep -Seconds 5
    
    if (Test-ChromeRunning) {
        Write-Color "✅ Chrome 已启动 (端口 $CHROME_PORT)" "Green"
    } else {
        throw "Chrome 启动失败"
    }
}

function Test-PythonEnv {
    $pythonPath = Join-Path $CSDN_TOOLS_PATH "venv\Scripts\python.exe"
    if (-not (Test-Path $pythonPath)) {
        throw "Python 虚拟环境未找到：$pythonPath`n请先运行：cd $CSDN_TOOLS_PATH; py -m venv venv; .\venv\Scripts\activate; pip install -r requirements.txt"
    }
    return $pythonPath
}

function Test-MarkdownFile {
    param([string]$Path)
    if (-not (Test-Path $Path)) {
        throw "文件不存在：$Path"
    }
    if (-not $Path.EndsWith('.md')) {
        throw "不是 markdown 文件：$Path"
    }
}

function Publish-ToCSDN {
    param([string]$MarkdownFile)
    
    Write-Color "" "White"
    Write-Color "🦐 CSDN 博客发布助手" "Cyan"
    Write-Color "=====================" "Cyan"
    Write-Color "" "White"
    
    # 1. 检查 Chrome
    if ($CheckChrome -or -not (Test-ChromeRunning)) {
        if ($StartChrome) {
            Start-ChromeDebug
        } else {
            Write-Color "⚠️  Chrome 调试模式未运行" "Yellow"
            Write-Color "  请运行：Start-ChromeDebug 或手动启动 Chrome" "Yellow"
            Write-Color "" "White"
            $response = Read-Host "是否现在启动 Chrome？(y/n)"
            if ($response -eq 'y') {
                Start-ChromeDebug
            } else {
                throw "需要 Chrome 调试模式才能继续"
            }
        }
    }
    
    # 2. 检查 Python 环境
    $pythonPath = Test-PythonEnv
    Write-Color "✅ Python 环境：$pythonPath" "Green"
    
    # 3. 检查文件
    Test-MarkdownFile -Path $MarkdownFile
    Write-Color "✅ 博客文件：$MarkdownFile" "Green"
    
    # 4. 执行发布
    Write-Color "" "White"
    Write-Color "📝 开始发布到 CSDN..." "Cyan"
    Write-Color "" "White"
    
    Set-Location $CSDN_TOOLS_PATH
    & $pythonPath "publisher/csdn_publisher.py" $MarkdownFile 2>&1
    
    Write-Color "" "White"
    Write-Color "=====================" "Cyan"
    Write-Color "🎉 发布流程完成！" "Green"
    Write-Color "" "White"
}

# Main
if ($CheckChrome) {
    if (Test-ChromeRunning) {
        Write-Color "✅ Chrome 调试模式运行中 (端口 $CHROME_PORT)" "Green"
    } else {
        Write-Color "❌ Chrome 调试模式未运行" "Red"
    }
    exit 0
}

if ($StartChrome) {
    Start-ChromeDebug
    exit 0
}

if ($MarkdownFile) {
    Publish-ToCSDN -MarkdownFile $MarkdownFile
}
