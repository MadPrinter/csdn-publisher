# 🦐 CSDN Publisher - 快速启动指南

## ✅ 已完成的工作

### 1. 优化了 CSDN 发布器

**文件：** `C:\blog-auto-publishing-tools\publisher\csdn_publisher.py`

**优化内容：**
- ✅ 自动处理弹窗（关闭按钮）
- ✅ 自动滚动页面确保按钮可见
- ✅ 标签为必填项，优先使用 front-matter 中的 tags
- ✅ 其他字段可选（摘要、专栏、可见范围）
- ✅ 增强元素定位和等待机制
- ✅ 修复编码问题（Unicode → ASCII）

### 2. 封装为 OpenClaw Skill

**目录：** `C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher\`

**文件结构：**
```
csdn-publisher/
├── SKILL.md              # Skill 描述和用法
├── README.md             # 完整文档
├── QUICKSTART.md         # 本文件
├── publish-to-csdn.ps1   # PowerShell 封装脚本
└── config-template.yaml  # 配置模板
```

### 3. 更新 TOOLS.md

**文件：** `C:\Users\Administrator\.openclaw\workspace\TOOLS.md`

添加了 CSDN Publisher 的配置说明和故障排查指南。

---

## 🚀 立即使用

### 方法 1：通过 OpenClaw（推荐）

直接对 OpenClaw 说：

```
把 blogs/output/2026-03-18-openclaw-gateway-diagnosis.md 发布到 CSDN
```

OpenClaw 会自动：
1. 检查 Chrome 调试模式
2. 启动发布脚本
3. 填充标题、内容、标签
4. 滚动页面并点击发布

### 方法 2：PowerShell 脚本

```powershell
cd C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher
.\publish-to-csdn.ps1 -MarkdownFile "C:\path\to\blog.md" -StartChrome
```

### 方法 3：直接调用 Python

```powershell
cd C:\blog-auto-publishing-tools
.\venv\Scripts\python.exe publisher/csdn_publisher.py "C:\path\to\blog.md"
```

---

## 📋 博客格式要求

```markdown
---
title: 文章标题（必填）
tags:
  - 标签 1（必填）
  - 标签 2（必填）
categories:
  - 分类 1（可选）
summary: 文章摘要（可选）
image: https://example.com/cover.jpg（可选）
---

# 正文开始

这里是文章内容...
```

---

## ⚙️ 配置说明

### 必填配置

**文件：** `C:\blog-auto-publishing-tools\config\common.yaml`

```yaml
service_location: ''
debugger_address: 127.0.0.1:9222
driver_type: chrome
auto_publish: true  # 自动点击发布
wait_login: true    # 等待登录
```

**文件：** `C:\blog-auto-publishing-tools\config\csdn.yaml`

```yaml
site: https://editor.csdn.net/md/
tags:
  - AI
  - OpenClaw
categories:
  - AI
visibility: 粉丝可见
```

---

## 🔧 故障排查

### Chrome 未运行

```powershell
# 手动启动
"C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --remote-debugging-port=9222 `
  --user-data-dir="%LOCALAPPDATA%\Google\Chrome\User Data"
```

### CSDN 未登录

1. 访问：https://passport.csdn.net/
2. 登录账号
3. 重新运行发布脚本

### 标签按钮未找到

- 确保 CSDN 编辑器完全加载
- 检查是否有弹窗遮挡
- 手动刷新页面后重试

### 发布按钮被遮挡

- 脚本会自动滚动页面
- 自动关闭弹窗
- 如仍失败，手动访问编辑器发布

---

## 📊 发布流程

```
1. 启动 Chrome 调试模式
   ↓
2. 打开 CSDN 编辑器
   ↓
3. 等待登录（如需要）
   ↓
4. 填写标题 ✓
   ↓
5. 粘贴内容 ✓
   ↓
6. 添加标签 ✓
   ↓
7. 设置封面（可选）
   ↓
8. 填写摘要（可选）
   ↓
9. 选择专栏（可选）
   ↓
10. 设置可见范围（可选）
    ↓
11. 滚动页面 + 关闭弹窗 ✓
    ↓
12. 点击发布按钮 ✓
    ↓
13. 验证发布结果 ✓
```

---

## 🎯 跨会话使用

Skill 已保存在：

```
C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher\
```

**无论何时开始新会话，都可以：**

1. 直接说："把这篇博客发布到 CSDN"
2. OpenClaw 会自动加载 csdn-publisher skill
3. 使用已配置的工具和脚本

**无需重复配置！**

---

## 📝 更新日志

### 2026-03-18 - 优化版

- ✅ 弹窗自动处理
- ✅ 滚动页面确保按钮可见
- ✅ 标签必填逻辑优化
- ✅ 编码问题修复
- ✅ 封装为 OpenClaw Skill
- ✅ 添加 PowerShell 封装脚本

### 2026-03-18 - 初始版

- 基于 blog-auto-publishing-tools
- Selenium + Chrome 调试模式

---

## 📚 资源链接

- **Skill 目录**: `C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher\`
- **发布工具**: `C:\blog-auto-publishing-tools\`
- **CSDN 编辑器**: https://editor.csdn.net/md/
- **OpenClaw 文档**: https://docs.openclaw.ai

---

**Made with ❤️ by [@MadPrinter](https://github.com/MadPrinter)**
