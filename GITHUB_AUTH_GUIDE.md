# 🔐 GitHub认证指南

## 问题
GitHub不再支持密码认证，需要使用Personal Access Token (PAT) 或SSH密钥。

## 解决方案

### 方案1: 使用Personal Access Token (推荐)

1. **创建Personal Access Token**:
   - 访问: https://github.com/settings/tokens
   - 点击 "Generate new token" → "Generate new token (classic)"
   - 填写信息:
     - Note: "AI Choreography Generator"
     - Expiration: 90 days (或更长)
     - 勾选权限: `repo` (完整仓库访问)
   - 点击 "Generate token"
   - **重要**: 复制并保存token，只显示一次！

2. **使用token推送代码**:
   ```bash
   # 方法1: 在URL中包含token
   git remote set-url origin https://jiaqili0714:YOUR_TOKEN@github.com/jiaqili0714/ai-choreography-generator.git
   git push -u origin main
   
   # 方法2: 使用Git凭据管理器
   git push -u origin main
   # 当提示输入用户名时: jiaqili0714
   # 当提示输入密码时: 粘贴你的token
   ```

### 方案2: 使用SSH密钥

1. **生成SSH密钥**:
   ```bash
   ssh-keygen -t ed25519 -C "your-email@example.com"
   # 按回车使用默认路径
   # 可以设置密码或直接回车
   ```

2. **添加SSH密钥到GitHub**:
   ```bash
   # 复制公钥
   cat ~/.ssh/id_ed25519.pub
   ```
   - 访问: https://github.com/settings/ssh/new
   - 粘贴公钥内容
   - 点击 "Add SSH key"

3. **更改远程URL为SSH**:
   ```bash
   git remote set-url origin git@github.com:jiaqili0714/ai-choreography-generator.git
   git push -u origin main
   ```

### 方案3: 使用GitHub CLI (最简单)

1. **安装GitHub CLI**:
   ```bash
   # macOS
   brew install gh
   
   # 或下载: https://cli.github.com/
   ```

2. **登录GitHub**:
   ```bash
   gh auth login
   # 选择: GitHub.com
   # 选择: HTTPS
   # 选择: Yes (使用Git凭据)
   # 选择: Login with a web browser
   ```

3. **推送代码**:
   ```bash
   git push -u origin main
   ```

## 推荐步骤

我建议使用**方案1 (Personal Access Token)**，因为最简单：

1. 创建token: https://github.com/settings/tokens
2. 运行以下命令:
   ```bash
   git push -u origin main
   ```
3. 输入用户名: `jiaqili0714`
4. 输入密码: 粘贴你的token

## 完成后的下一步

推送成功后，就可以部署到Streamlit Cloud了：
1. 访问: https://share.streamlit.io
2. 点击 "New app"
3. Repository: `jiaqili0714/ai-choreography-generator`
4. 其他设置按之前的指南操作
