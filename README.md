# 🦐 CSDN Publisher - Production Ready

**生产环境级别的 CSDN 博客发布工具**

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/openclaw/openclaw)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![Status](https://img.shields.io/badge/status-production-green.svg)](https://github.com/openclaw/openclaw)

---

## 🚀 特性

- ⚡ **快速** - 20 秒内发布完成
- 🛡️ **可靠** - 完整的错误处理
- 📦 **独立** - 零外部依赖
- 🧪 **测试** - 单元测试覆盖
- 📖 **文档** - 完整使用指南

---

## 📦 安装

### 1. 克隆/复制 Skill

```bash
# 复制到 OpenClaw workspace
cp -r csdn-publisher ~/.openclaw/workspace/skills/
```

### 2. 安装依赖

```bash
pip install selenium pyperclip
```

### 3. 验证安装

```bash
cd skills/csdn-publisher
python tests/test_parser.py
```

---

## 🚀 使用

### 方法 1: 命令行

```bash
python csdn_publisher_fast.py blog.md
```

### 方法 2: PowerShell

```powershell
.\publish-to-csdn.ps1 -MarkdownFile "blog.md" -StartChrome
```

### 方法 3: Python API

```python
from csdn_publisher_fast import publish_to_csdn

success, link = publish_to_csdn("blog.md")
if success:
    print(f"发布成功：{link}")
```

---

## 📝 博客格式

```markdown
---
title: 文章标题
tags:
  - AI
  - OpenClaw
  - 自动化
summary: 文章摘要（可选）
---

# 正文内容

...
```

---

## 🔄 发布流程

```
┌─────────────────────────────────────────┐
│  1. 解析 markdown                        │
│     提取标题、标签、内容                 │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  2. 打开 CSDN 编辑器                      │
│     https://editor.csdn.net/md/         │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  3. 等待登录（最多 10 秒）                 │
│     检查标题输入框                       │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  4. 填写标题                            │
│     send_keys(title)                    │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  5. 粘贴正文                            │
│     pyperclip.copy() + Ctrl+V           │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  6. 关闭弹窗                            │
│     click close button                  │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  7. 点击发布                            │
│     scroll + click "发布文章"            │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  8. 填写弹窗标签（必填）                 │
│     send_keys + ENTER                   │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  9. 点击确认发布                        │
│     JavaScript click "发布文章"          │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  10. 等待发布完成（最多 30 秒）            │
│     检查"发布成功！正在审核中"           │
└─────────────────────────────────────────┘
                    ↓
              ✅ 发布成功
```

---

## ✅ 成功标志

- 页面显示：**"发布成功！正在审核中"**
- 返回文章链接：`https://blog.csdn.net/article/details/xxxxx`

---

## 🛡️ 错误处理

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| 文件不存在 | 路径错误 | 检查文件路径 |
| 未登录 | 未登录 CSDN | 访问 passport.csdn.net 登录 |
| Chrome 无法连接 | 未启动调试模式 | `chrome.exe --remote-debugging-port=9222` |
| 依赖缺失 | 未安装 Python 包 | `pip install selenium pyperclip` |

---

## 📊 性能

| 指标 | 目标 | 实际 |
|------|------|------|
| 发布时间 | <20 秒 | ~15 秒 |
| 成功率 | >95% | 待统计 |
| 最大内容 | - | 10KB+ |

---

## 🧪 测试

### 单元测试

```bash
python tests/test_parser.py
```

### 端到端测试

```bash
python csdn_publisher_fast.py examples/blog_template.md
```

---

## 📖 文档

- **[SKILL.md](SKILL.md)** - Skill 定义
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - 架构设计
- **[examples/](examples/)** - 示例代码

---

## 🔧 开发

### 代码风格

- 遵循 PEP 8
- 类型注解
- 文档字符串

### 提交规范

```
feat: 新功能
fix: 修复 bug
docs: 文档更新
test: 测试相关
```

---

## 📄 许可证

MIT License

---

## 🤝 贡献

1. Fork 项目
2. 创建分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📞 支持

- **问题**: GitHub Issues
- **文档**: ARCHITECTURE.md
- **示例**: examples/

---

**🎉 Happy Publishing!**
