---
name: csdn-publisher
description: "Production-ready CSDN blog publisher. Publishes markdown blogs to CSDN in <20 seconds. Auto-fills title, content, tags, and clicks publish button. Requires Chrome debug mode. Fully independent."
homepage: https://github.com/openclaw/openclaw
metadata:
  openclaw:
    emoji: "🚀"
    requires:
      bins: ["chrome"]
      pip: ["selenium>=4.0.0", "pyperclip>=1.8.0"]
---

# CSDN Publisher Skill - Production v3.0

**20 秒内发布完成，生产环境就绪**

---

## ✅ 核心特性

- ⚡ **快速发布** - 目标 20 秒，实际 ~15 秒
- 🛡️ **生产就绪** - 完整的错误处理和日志
- 📦 **独立部署** - 不依赖任何外部工具
- 🧪 **测试覆盖** - 单元测试 + 集成测试
- 📖 **完整文档** - ARCHITECTURE.md + README.md

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install selenium pyperclip
```

### 2. 启动 Chrome

```bash
chrome.exe --remote-debugging-port=9222
```

### 3. 发布博客

```bash
cd skills/csdn-publisher
python csdn_publisher_fast.py blog.md
```

---

## 📝 博客格式

```markdown
---
title: 文章标题
tags:
  - 标签 1
  - 标签 2
  - 标签 3
summary: 文章摘要（可选）
---

# 正文内容
```

---

## 🔄 发布流程

```
1. 解析 markdown → 提取标题、标签、内容
   ↓
2. 打开编辑器 → https://editor.csdn.net/md/
   ↓
3. 等待登录 → 最多 10 秒
   ↓
4. 填写标题 → 0.5 秒
   ↓
5. 粘贴正文 → 2.5 秒
   ↓
6. 关闭弹窗 → 0.5 秒
   ↓
7. 点击发布 → 2 秒
   ↓
8. 填写弹窗标签 → 2 秒（必填）
   ↓
9. 点击确认发布 → 1 秒
   ↓
10. 等待完成 → 5-10 秒
    ↓
✅ 发布成功
```

---

## ✅ 成功标志

页面显示：**"发布成功！正在审核中"**

返回格式：`(True, "https://blog.csdn.net/article/details/xxxxx")`

---

## 🛡️ 错误处理

| 错误 | 处理 | 提示 |
|------|------|------|
| 文件不存在 | 立即返回 | "文件不存在：xxx" |
| 未登录 | 等待 10 秒 | "未登录 CSDN" |
| 元素找不到 | 重试 3 次 | "操作超时" |
| 点击被遮挡 | JavaScript 点击 | 自动处理 |

---

## 📊 性能指标

| 指标 | 目标 | 实际 |
|------|------|------|
| 发布时间 | <20 秒 | ~15 秒 |
| 成功率 | >95% | 待统计 |
| 支持标签数 | ≥3 | 3 |
| 最大内容 | 无限制 | 实测 10KB+ |

---

## 🧪 测试

```bash
# 运行单元测试
python tests/test_parser.py

# 端到端测试
python csdn_publisher_fast.py examples/blog_template.md
```

---

## 📖 文档

- **README.md** - 使用指南
- **ARCHITECTURE.md** - 架构设计
- **examples/** - 示例代码
- **tests/** - 测试用例

---

## 🔧 故障排查

### Chrome 无法连接

```bash
# 检查 Chrome 是否运行
chrome.exe --remote-debugging-port=9222
```

### 依赖缺失

```bash
pip install selenium pyperclip
```

### 未登录 CSDN

```bash
# 手动登录
start https://passport.csdn.net/
```

---

## 📞 API

```python
from csdn_publisher_fast import publish_to_csdn

success, message = publish_to_csdn("blog.md")
if success:
    print(f"发布成功：{message}")
else:
    print(f"发布失败：{message}")
```

---

**版本:** 3.0.0 (Production)  
**最后更新:** 2026-03-19  
**维护者:** OpenClaw Team
