# CSDN Publisher 一键发布到 GitHub
# 用法：.\publish-to-github.ps1

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CSDN Publisher - GitHub 发布工具" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 配置
$repoName = "csdn-publisher"
$githubUser = "MadPrinter"
$repoPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$githubURL = "https://github.com/$githubUser/$repoName.git"

Write-Host "仓库信息：" -ForegroundColor Yellow
Write-Host "  用户名：$githubUser"
Write-Host "  仓库名：$repoName"
Write-Host "  地址：$githubURL"
Write-Host ""

# 检查 Git 是否安装
try {
    $gitVersion = git --version
    Write-Host "✅ Git 已安装：$gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git 未安装！请先安装 Git: https://git-scm.com/" -ForegroundColor Red
    exit 1
}

# 检查是否已有远程仓库
Write-Host "`n 检查远程仓库..." -ForegroundColor Yellow
try {
    $existing = git remote get-url origin 2>$null
    if ($existing) {
        Write-Host "⚠️  已存在远程仓库：$existing" -ForegroundColor Yellow
        $response = Read-Host "是否继续推送？(y/n)"
        if ($response -ne 'y') {
            Write-Host "已取消" -ForegroundColor Yellow
            exit 0
        }
    }
} catch {
    Write-Host "ℹ️  尚未配置远程仓库" -ForegroundColor Cyan
}

# 提示用户在 GitHub 创建仓库
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  请在 GitHub 创建仓库" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. 访问：https://github.com/new" -ForegroundColor White
Write-Host "2. 填写：" -ForegroundColor White
Write-Host "   Repository name: $repoName"
Write-Host "   Description: CSDN Publisher Skill for OpenClaw"
Write-Host "   Visibility: Public"
Write-Host "   ☐ Add a README file (不勾选)"
Write-Host "   ☐ Add .gitignore (不勾选)"
Write-Host "   ☐ Choose a license (不勾选)"
Write-Host ""

$response = Read-Host "创建完成后按回车继续..."

# 设置远程仓库
Write-Host "`n 配置远程仓库..." -ForegroundColor Yellow
try {
    git remote remove origin 2>$null
} catch {}

git remote add origin $githubURL
Write-Host "✅ 远程仓库已配置" -ForegroundColor Green

# 推送
Write-Host "`n 推送到 GitHub..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n========================================" -ForegroundColor Green
    Write-Host "  ✅ 发布成功！" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "🎉 仓库地址：$githubURL" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "下一步：" -ForegroundColor Yellow
    Write-Host "1. 访问仓库查看代码"
    Write-Host "2. 创建第一个 Release"
    Write-Host "3. 分享给其他人"
    Write-Host ""
} else {
    Write-Host "`n❌ 推送失败！请检查：" -ForegroundColor Red
    Write-Host "1. GitHub 仓库是否已创建"
    Write-Host "2. 网络连接是否正常"
    Write-Host "3. 是否有 GitHub 访问权限"
    Write-Host ""
    Write-Host "错误信息：" -ForegroundColor Yellow
    Write-Host "  请查看上面的错误提示" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "按任意键退出..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
