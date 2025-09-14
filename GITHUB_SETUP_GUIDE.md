# 🚀 GitHub仓库设置和Streamlit部署指南

## 📋 步骤1: 创建GitHub仓库

### 方法1: 通过GitHub网站创建

1. **访问GitHub**: 打开 https://github.com
2. **登录账户**: 使用你的GitHub账户登录
3. **创建新仓库**: 点击右上角的 "+" 按钮，选择 "New repository"
4. **填写仓库信息**:
   - Repository name: `ai-choreography-generator`
   - Description: `AI-powered choreography generator that analyzes music and creates dance suggestions`
   - 选择 Public (公开)
   - 不要勾选 "Add a README file" (我们已经有了)
   - 不要勾选 "Add .gitignore" (我们已经有了)
   - 不要选择 license (可选)
5. **点击 "Create repository"**

### 方法2: 通过命令行创建 (需要安装GitHub CLI)

```bash
# 安装GitHub CLI (macOS)
brew install gh

# 登录GitHub
gh auth login

# 创建仓库
gh repo create ai-choreography-generator --public --description "AI-powered choreography generator that analyzes music and creates dance suggestions"
```

## 📋 步骤2: 推送代码到GitHub

```bash
# 添加远程仓库 (替换YOUR_USERNAME为你的GitHub用户名)
git remote add origin https://github.com/YOUR_USERNAME/ai-choreography-generator.git

# 推送代码到GitHub
git push -u origin main
```

## 📋 步骤3: 部署到Streamlit Cloud

### 方法1: 通过Streamlit网站部署

1. **访问Streamlit Cloud**: 打开 https://share.streamlit.io
2. **登录**: 使用GitHub账户登录
3. **新建应用**: 点击 "New app"
4. **填写部署信息**:
   - Repository: `YOUR_USERNAME/ai-choreography-generator`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL: 可以自定义，如 `ai-choreography-generator`
5. **高级设置**:
   - 在 "Secrets" 部分添加:
     ```
     OPENAI_API_KEY = "your-openai-api-key-here"
     ```
6. **点击 "Deploy!"**

### 方法2: 通过命令行部署 (需要安装Streamlit CLI)

```bash
# 安装Streamlit CLI
pip install streamlit

# 登录Streamlit
streamlit login

# 部署应用
streamlit deploy app.py --name ai-choreography-generator
```

## 🔧 环境变量设置

在Streamlit Cloud部署时，需要在 "Secrets" 部分添加以下环境变量：

```
OPENAI_API_KEY = "your-openai-api-key-here"
```

## 📝 部署后的配置

1. **获取应用URL**: 部署完成后，Streamlit会提供一个公开的URL
2. **测试应用**: 访问URL测试应用是否正常工作
3. **更新README**: 在README.md中更新Streamlit应用的链接

## 🎯 部署检查清单

- [ ] GitHub仓库已创建
- [ ] 代码已推送到GitHub
- [ ] Streamlit Cloud应用已创建
- [ ] 环境变量已设置
- [ ] 应用可以正常访问
- [ ] README.md中的链接已更新

## 🚨 常见问题

### 1. 部署失败
- 检查 `requirements.txt` 是否包含所有必要的依赖
- 确保 `app.py` 文件在根目录
- 检查环境变量是否正确设置

### 2. API密钥问题
- 确保在Streamlit Cloud的Secrets中正确设置了 `OPENAI_API_KEY`
- 检查API密钥是否有效且有足够的额度

### 3. 依赖问题
- 确保所有依赖都在 `requirements.txt` 中
- 检查Python版本兼容性

## �� 完成！

部署完成后，你的AI编舞生成器就可以在互联网上访问了！

应用URL格式: `https://ai-choreography-generator.streamlit.app/`
