# 🦐 CSDN Publisher Skill

**OpenClaw Skill for automated CSDN blog publishing.**

---

## 🚀 Quick Start

### 首次使用（One-Time Setup）

```powershell
# 1. 克隆发布工具
git clone https://github.com/ddean2009/blog-auto-publishing-tools.git C:\blog-auto-publishing-tools

# 2. 安装 Python 依赖
cd C:\blog-auto-publishing-tools
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# 3. 配置 CSDN
cp C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher\config-template.yaml `
   C:\blog-auto-publishing-tools\config\common.yaml

# 4. 编辑 CSDN 配置（标签、专栏等）
notepad C:\blog-auto-publishing-tools\config\csdn.yaml
```

### 日常使用（Daily Use）

```powershell
# 方法 1: 使用 PowerShell 脚本（推荐）
cd C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher
.\publish-to-csdn.ps1 -MarkdownFile "C:\path\to\blog.md" -StartChrome

# 方法 2: 直接调用 Python
cd C:\blog-auto-publishing-tools
.\venv\Scripts\python.exe publisher/csdn_publisher.py "C:\path\to\blog.md"

# 方法 3: 通过 OpenClaw（自动）
# 对 OpenClaw 说："把这篇博客发布到 CSDN"
```

---

## 📋 博客格式

Markdown 文件应包含 front-matter：

```markdown
---
title: 文章标题
tags:
  - OpenClaw
  - AI Agent
  - 运维
categories:
  - AI
summary: 文章摘要（可选）
image: https://example.com/cover.jpg（可选）
---

# 正文开始

这里是文章内容...
```

---

## ⚙️ 配置说明

### common.yaml

| 配置项 | 说明 | 默认值 |
|-------|------|-------|
| `debugger_address` | Chrome 调试端口 | `127.0.0.1:9222` |
| `auto_publish` | 自动发布 | `true` |
| `wait_login` | 等待登录 | `true` |
| `wait_login_time` | 登录超时（秒） | `120` |

### csdn.yaml

| 配置项 | 说明 | 示例 |
|-------|------|------|
| `site` | CSDN 编辑器地址 | `https://editor.csdn.net/md/` |
| `tags` | 默认标签 | `["AI", "OpenClaw"]` |
| `categories` | 默认专栏 | `["AI"]` |
| `visibility` | 可见范围 | `粉丝可见` |

---

## 🔧 常见问题

### Chrome 无法启动

```powershell
# 手动启动 Chrome 调试模式
"C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --remote-debugging-port=9222 `
  --user-data-dir="%LOCALAPPDATA%\Google\Chrome\User Data"
```

### CSDN 未登录

1. 访问：https://passport.csdn.net/
2. 登录账号
3. 重新运行发布脚本

### 发布按钮找不到

- 确保页面已完全加载
- 滚动到页面底部
- 关闭所有弹窗广告

### 标签设置失败

- 使用 CSDN 上已有的标签名称
- 标签区分大小写
- 不要使用生僻标签

---

## 📊 发布流程

```
┌─────────────────────────────────────┐
│  1. 启动 Chrome 调试模式 (端口 9222)   │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  2. 打开 CSDN 编辑器                  │
│     https://editor.csdn.net/md/     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  3. 等待登录（如需要）                │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  4. 填写标题（必填）                  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  5. 粘贴内容（必填）                  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  6. 添加标签（必填）                  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  7. 设置封面（可选）                  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  8. 填写摘要（可选）                  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  9. 选择专栏（可选）                  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  10. 设置可见范围（可选）             │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  11. 滚动页面，关闭弹窗               │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  12. 点击发布按钮                    │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  13. 验证发布结果                    │
└─────────────────────────────────────┘
```

---

## 🛠️ 高级用法

### 批量发布

```powershell
$blogs = Get-ChildItem "C:\blogs\output\*.md"
foreach ($blog in $blogs) {
  .\publish-to-csdn.ps1 -MarkdownFile $blog.FullName
  Start-Sleep -Seconds 30  # 避免发布过快
}
```

### 自定义发布脚本

```python
# my_publisher.py
import sys
sys.path.insert(0, 'C:\\blog-auto-publishing-tools')

from publisher.csdn_publisher import csdn_publisher
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(options=options)

csdn_publisher(driver, 'C:\\blogs\\my-article.md')
driver.quit()
```

---

## 📝 更新日志

- **2026-03-18**: 优化弹窗处理、滚动定位、标签必填逻辑
- **2026-03-18**: 封装为 OpenClaw Skill
- **2026-03-18**: 添加 PowerShell 封装脚本

---

## 📚 资源链接

- **blog-auto-publishing-tools**: https://github.com/ddean2009/blog-auto-publishing-tools
- **CSDN 编辑器**: https://editor.csdn.net/md/
- **OpenClaw 文档**: https://docs.openclaw.ai

---

**Made with ❤️ by [@MadPrinter](https://github.com/MadPrinter)**
