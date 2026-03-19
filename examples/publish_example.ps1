# CSDN Publisher 使用示例
# ==========================

# 示例 1: 基本发布
# -----------------
cd C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher
python csdn_publisher_fast.py "C:\path\to\blog.md"


# 示例 2: 使用 PowerShell 脚本（自动启动 Chrome）
# -----------------------------------------------
.\publish-to-csdn.ps1 -MarkdownFile "C:\path\to\blog.md" -StartChrome


# 示例 3: 批量发布
# ----------------
$blogs = @(
    "C:\blogs\blog1.md",
    "C:\blogs\blog2.md",
    "C:\blogs\blog3.md"
)

foreach ($blog in $blogs) {
    Write-Host "发布：$blog"
    python csdn_publisher_fast.py $blog
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ 成功" -ForegroundColor Green
    } else {
        Write-Host "❌ 失败" -ForegroundColor Red
    }
    
    Start-Sleep -Seconds 2
}


# 示例 4: 检查发布状态
# --------------------
# 访问 CSDN 内容管理页面
Start-Process "https://i.csdn.net/#/content"
