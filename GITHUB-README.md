# 🚀 CSDN Publisher Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://docs.openclaw.ai)
[![GitHub stars](https://img.shields.io/github/stars/MadPrinter/csdn-publisher.svg?style=social&label=Star)](https://github.com/MadPrinter/csdn-publisher)

**🤖 完全自动化的 CSDN 博客发布工具 | OpenClaw Skill**

---

## ✨ 功能特性

- ✅ **完全自动化** - 从打开编辑器到点击发布，全程无需手动操作
- ✅ **智能填充** - 自动填写标题、内容、标签
- ✅ **两次点击流程** - 自动处理发布弹窗，完整点击流程
- ✅ **弹窗处理** - 5 种选择器策略，自动关闭弹窗
- ✅ **可选字段** - 支持封面、摘要、专栏、可见范围设置
- ✅ **自然语言触发** - 直接说"把这篇博客发布到 CSDN"即可

---

## 🎯 使用示例

### 基本使用

```
用户：把 blogs/output/xxx.md 发布到 CSDN
```

### 发布流程

```
1. 打开 CSDN 编辑器
2. 自动填写标题
3. 自动粘贴内容
4. 自动添加标签
5. 自动关闭弹窗
6. 自动点击发布按钮（两次）
7. 验证发布结果
```

---

## 📋 前置要求

- ✅ **OpenClaw** - 已安装并配置
- ✅ **Chrome 浏览器** - 支持调试模式
- ✅ **Python 3.x** - 运行发布脚本
- ✅ **CSDN 账号** - 已登录状态

---

## 🚀 快速开始

### 1. 安装 Skill

```powershell
# 克隆到 OpenClaw Skills 目录
git clone https://github.com/MadPrinter/csdn-publisher.git `
  C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher
```

### 2. 安装依赖

```powershell
cd C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher
pip install -r requirements.txt
```

### 3. 配置 Chrome

```powershell
# 启动 Chrome 调试模式
"C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --remote-debugging-port=9222 `
  --user-data-dir="%LOCALAPPDATA%\Google\Chrome\User Data"
```

### 4. 使用 Skill

```
"把这篇博客发布到 CSDN"
```

---

## 📁 文件结构

```
csdn-publisher/
├── SKILL.md                  # OpenClaw Skill 核心指令
├── README.md                 # 本文档
├── QUICKSTART.md             # 快速开始指南
├── FINAL_REPORT.md           # 完成报告
├── COMPLETION_REPORT.md      # 技术细节
├── publish-to-csdn.ps1       # PowerShell 发布脚本
├── config-template.yaml      # 配置模板
├── requirements.txt          # Python 依赖
├── LICENSE                   # MIT 开源协议
└── .gitignore                # Git 忽略文件
```

---

## 🛠️ 高级用法

### 使用 PowerShell 脚本

```powershell
cd C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher
.\publish-to-csdn.ps1 -MarkdownFile "C:\path\to\blog.md" -StartChrome
```

### 使用 Python 直接调用

```powershell
cd C:\blog-auto-publishing-tools
.\venv\Scripts\python.exe publisher/csdn_publisher.py "C:\path\to\blog.md"
```

---

## 📖 博客格式要求

你的 Markdown 文件应包含 front-matter：

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

## 🔧 故障排查

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

### 发布按钮未找到

- 确保页面已完全加载
- 检查是否有弹窗遮挡
- 手动刷新页面后重试

---

## 📊 发布流程详解

```
┌─────────────────────────────────────┐
│  1. 打开 CSDN 编辑器                  │
│     https://editor.csdn.net/md/     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  2. 等待登录（如需要）                │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  3. 填写标题 ✓                       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  4. 粘贴内容 ✓                       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  5. 添加标签 ✓                       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  6. 关闭弹窗 ✓                       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  7. 第一次点击：打开发布弹窗 ✓        │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  8. 第二次点击：确认发布 ✓            │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  9. 验证发布结果 ✓                    │
└─────────────────────────────────────┘
```

---

## 🎯 技术亮点

### 1. 两次点击流程

```python
# 第一次点击：打开发布弹窗
publish_btn.click()
time.sleep(3)

# 处理弹窗中的标签
# ...

# 第二次点击：确认发布
confirm_btn.click()
```

### 2. 智能弹窗处理

```python
def close_popups(driver):
    popup_selectors = [
        '//button[@title="关闭"]',
        '//button[contains(text(),"关闭")]',
        '//button[contains(text(),"取消")]',
        '//span[@class="close"]',
        '//div[contains(@class,"modal")]//button',
    ]
    # 自动检测并关闭
```

### 3. 多策略元素定位

```python
tag_btn_selectors = [
    '//button[contains(@class,"tag__btn-tag") and contains(text(),"添加")]',
    '//button[contains(@class,"tag__btn-tag") and contains(text(),"选择")]',
    '//button[contains(@class,"tag__btn") and contains(text(),"标签")]',
]
```

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 贡献方式

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

本项目采用 MIT 开源协议 - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- 基于 [blog-auto-publishing-tools](https://github.com/ddean2009/blog-auto-publishing-tools) 开发
- 感谢 [OpenClaw](https://github.com/openclaw/openclaw) 团队
- 感谢所有贡献者

---

## 📚 相关资源

- [OpenClaw 文档](https://docs.openclaw.ai)
- [OpenClaw Skills](https://clawhub.com)
- [CSDN 编辑器](https://editor.csdn.net/md/)
- [blog-auto-publishing-tools](https://github.com/ddean2009/blog-auto-publishing-tools)

---

## 📬 联系方式

- **GitHub:** [@MadPrinter](https://github.com/MadPrinter)
- **Issues:** [提交 Issue](https://github.com/MadPrinter/csdn-publisher/issues)

---

<div align="center">

**🌟 如果这个项目对你有帮助，请给一个 Star！**

Made with ❤️ by MadPrinter

</div>
