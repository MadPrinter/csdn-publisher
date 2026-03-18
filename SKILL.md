---
name: csdn-publisher
description: "Publish blog posts to CSDN fully automatically. Use when: user wants to publish markdown blogs to CSDN platform with one click. Auto-fills title, content, tags, and clicks publish button. Requires blog-auto-publishing-tools and Chrome debug mode."
homepage: https://github.com/ddean2009/blog-auto-publishing-tools
metadata: { "openclaw": { "emoji": "🚀", "requires": { "bins": ["chrome"], "pip": ["selenium", "pyyaml", "pyperclip", "requests"], "paths": ["C:\\blog-auto-publishing-tools"] } } }
---

# CSDN Publisher Skill

**Automate CSDN blog publishing with Selenium + Chrome debug mode.**

## When to Use

✅ **USE this skill when:**

- User wants to publish a markdown blog to CSDN **with full automation**
- Automate blog cross-posting workflow
- User provides a markdown file and asks to "publish to CSDN"
- Batch publish multiple articles
- **Auto-click publish button** (no manual intervention needed)

❌ **DON'T use this skill when:**

- User wants to publish to other platforms (use platform-specific publisher)
- No CSDN account/login available
- Simple text post (use web interface directly)

---

## Prerequisites

### 1. Install blog-auto-publishing-tools

```powershell
# Clone the repository
git clone https://github.com/ddean2009/blog-auto-publishing-tools.git C:\blog-auto-publishing-tools

# Install Python dependencies
cd C:\blog-auto-publishing-tools
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure CSDN

Edit `C:\blog-auto-publishing-tools\config\csdn.yaml`:

```yaml
site: https://editor.csdn.net/md/

# Article tags (default)
tags:
  - AI
  - OpenClaw

# Article categories (default)
categories:
  - AI

# Visibility: 全部可见，仅我可见，粉丝可见，VIP 可见
visibility: 粉丝可见
```

Edit `C:\blog-auto-publishing-tools\config\common.yaml`:

```yaml
service_location: ''
debugger_address: 127.0.0.1:9222
driver_type: chrome
include_footer: false
auto_publish: true
wait_login: true
wait_login_time: 120
title: ''
summary: ''
content: ''
enable:
  csdn: true
  jianshu: false
  juejin: false
  # ... other platforms
```

### 3. Chrome Debug Mode

```powershell
# Start Chrome with debug port
Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  -ArgumentList "--remote-debugging-port=9222", `
                "--user-data-dir=$env:LOCALAPPDATA\Google\Chrome\User Data"
```

---

## Usage

### Method 1: Direct Python Script

```powershell
cd C:\blog-auto-publishing-tools
.\venv\Scripts\python.exe publisher/csdn_publisher.py "C:\path\to\blog.md"
```

### Method 2: OpenClaw Skill

```markdown
User: 把这篇博客发布到 CSDN
Assistant: 好的，我来帮您发布到 CSDN。

[Uses csdn-publisher skill to publish]
```

### Method 3: PowerShell Wrapper

```powershell
# Create publish-csdn.ps1
param([string]$MarkdownFile)
cd C:\blog-auto-publishing-tools
.\venv\Scripts\python.exe publisher/csdn_publisher.py $MarkdownFile
```

---

## Blog Format

Your markdown file should include front matter:

```markdown
---
title: 文章标题
tags:
  - 标签 1
  - 标签 2
categories:
  - 分类 1
summary: 文章摘要（可选）
image: https://example.com/cover.jpg（可选）
---

# 文章正文

这里是文章内容...
```

---

## Workflow

```
1. Start Chrome debug mode (port 9222)
   ↓
2. Load markdown file
   ↓
3. Open CSDN editor (new tab)
   ↓
4. Wait for login (if needed)
   ↓
5. Fill title (required)
   ↓
6. Paste content (required)
   ↓
7. Add tags (required)
   ↓
8. Set cover image (optional)
   ↓
9. Add summary (optional)
   ↓
10. Select categories (optional)
    ↓
11. Set visibility (optional)
    ↓
12. Scroll & close popups
    ↓
13. Click publish button
    ↓
14. Verify publication
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Chrome not reachable | Restart Chrome with `--remote-debugging-port=9222` |
| Login required | Manually login at https://passport.csdn.net/ |
| Publish button not found | Scroll down, close popups, wait 2 seconds |
| Element click intercepted | Close modal overlays, retry |
| Tags not found | Use exact tag names from CSDN |
| Encoding error | Save markdown as UTF-8 |

---

## Advanced: Custom Publisher Script

Create `publish_single.py`:

```python
import sys
sys.path.insert(0, 'C:\\blog-auto-publishing-tools')

from publisher.csdn_publisher import csdn_publisher
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Start Chrome
options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(options=options)

# Publish
csdn_publisher(driver, 'C:\\path\\to\\blog.md')

driver.quit()
```

---

## Notes

- **Login persistence**: CSDN login is saved in Chrome user data
- **Rate limiting**: Don't publish too frequently (CSDN may flag spam)
- **Content review**: CSDN may review articles before public visibility
- **Auto-publish**: Set `auto_publish: true` for full automation
- **Manual fallback**: If auto-publish fails, editor is pre-filled for manual publish

---

## Example Session

```
User: 把 blogs/output/2026-03-18-openclaw-gateway-diagnosis.md 发布到 CSDN

Assistant: 好的，正在发布到 CSDN...

[CSDN] 准备发布：OpenClaw Gateway 卡死假死问题完整诊断与预防方案
[CSDN] ✓ 标题：OpenClaw Gateway 卡死假死问题完整诊断与预防方案
[CSDN] ✓ 内容已粘贴 (7951 字符)
[CSDN] ✓ 标签：OpenClaw
[CSDN] ✓ 标签：AI Agent
[CSDN] ✓ 标签：Gateway
[CSDN] ✓ 标签：运维
[CSDN] ✓ 标签：故障排查
[CSDN] ✓ 封面：C:\Users\ADMINI~1\AppData\Local\Temp\2\400
[CSDN] ✅ 文章已发布！
[CSDN] 🎉 发布成功！链接：https://blog.csdn.net/xxx/article/details/xxx

发布完成！🦐
```

---

## Security

- **Credentials**: CSDN login stored in Chrome (not in scripts)
- **API keys**: None required (uses browser automation)
- **Privacy**: All processing is local

---

## Resources

- **blog-auto-publishing-tools**: https://github.com/ddean2009/blog-auto-publishing-tools
- **CSDN Editor**: https://editor.csdn.net/md/
- **CSDN Help**: https://blog.csdn.net/blogdevteam/article/details/113836297
