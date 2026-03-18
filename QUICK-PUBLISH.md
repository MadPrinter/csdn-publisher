# 🚀 快速发布到 GitHub（3 种方法）

**选择最适合你的方法！**

---

## 方法 1：GitHub CLI（最简单）⭐ 推荐

**一条命令搞定！**

### 安装 GitHub CLI

```powershell
# Windows (winget)
winget install GitHub.cli

# 或下载：https://cli.github.com/
```

### 登录

```powershell
gh auth login
```

按提示操作：
1. 选择 "GitHub.com"
2. 选择 "HTTPS"
3. 登录账号
4. 完成验证

### 一键发布

```powershell
cd C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher
gh repo create csdn-publisher --public --source=. --push
```

**完成！** ✅ 仓库已创建并推送！

---

## 方法 2：PowerShell 脚本（自动化）

### 运行脚本

```powershell
cd C:\Users\Administrator\.openclaw\workspace\skills\csdn-publisher
.\publish-to-github.ps1
```

**脚本会：**
1. ✅ 检查 Git 安装
2. ✅ 提示创建仓库
3. ✅ 配置远程地址
4. ✅ 自动推送

---

## 方法 3：网页上传（无需工具）

### 步骤 1：创建仓库

1. 访问：https://github.com/new
2. 填写：
   ```
   Repository name: csdn-publisher
   Description: CSDN Publisher Skill for OpenClaw
   Visibility: Public
   ```
3. **不要勾选** "Add a README file"
4. 点击 "Create repository"

### 步骤 2：上传文件

1. 点击 "uploading an existing file"
2. 拖拽所有文件
3. 填写提交信息
4. 点击 "Commit changes"

---

## 📊 方法对比

| 方法 | 难度 | 速度 | 推荐度 |
|-----|------|------|--------|
| **GitHub CLI** | ⭐ 简单 | ⚡ 最快 | ⭐⭐⭐⭐⭐ |
| **PowerShell 脚本** | ⭐⭐ 中等 | ⚡ 快 | ⭐⭐⭐⭐ |
| **网页上传** | ⭐⭐⭐ 手动 | 🐢 慢 | ⭐⭐⭐ |

---

## 🎯 推荐流程

**如果你有 GitHub CLI：**
```powershell
gh repo create csdn-publisher --public --source=. --push
```

**如果没有：**
```powershell
.\publish-to-github.ps1
```

**都不想安装：**
→ 使用网页上传

---

## 📝 发布后

**创建仓库后：**

1. **查看仓库：**
   ```
   https://github.com/MadPrinter/csdn-publisher
   ```

2. **创建 Release：**
   - 进入仓库 → Releases → Create a new release
   - Tag: v1.0.0
   - 填写发布说明
   - 点击 "Publish release"

3. **分享：**
   - 复制链接分享给朋友
   - 发到社交媒体
   - 提交到 OpenClaw 社区

---

## 🦐 皮皮虾建议

**最简单的方法：**

```
安装 GitHub CLI → 一条命令搞定
```

**现在选择：**
1. 安装 GitHub CLI（推荐）
2. 运行 PowerShell 脚本
3. 网页手动上传

**选哪个？** 🤔
