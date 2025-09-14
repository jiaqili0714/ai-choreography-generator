# �� 快速部署指南

## 📋 当前状态
✅ 项目已准备就绪，可以部署到GitHub和Streamlit Cloud

## 🎯 3步完成部署

### 步骤1: 创建GitHub仓库
1. 访问: https://github.com/new
2. 仓库名: `ai-choreography-generator`
3. 描述: `AI-powered choreography generator that analyzes music and creates dance suggestions`
4. 选择: Public
5. 不要勾选任何选项 (README, .gitignore, license)
6. 点击 "Create repository"

### 步骤2: 推送代码
```bash
# 添加远程仓库 (替换YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ai-choreography-generator.git

# 推送代码
git push -u origin main
```

### 步骤3: 部署到Streamlit Cloud
1. 访问: https://share.streamlit.io
2. 点击 "New app"
3. 填写信息:
   - Repository: `YOUR_USERNAME/ai-choreography-generator`
   - Branch: `main`
   - Main file path: `app.py`
4. 在 "Secrets" 部分添加:
   ```
   OPENAI_API_KEY = "your-openai-api-key-here"
   ```
5. 点击 "Deploy!"

## 🎉 完成！
部署完成后，你的AI编舞生成器就可以在互联网上访问了！

应用URL: `https://ai-choreography-generator.streamlit.app/`

## 📝 更新README
部署完成后，记得在README.md中更新Streamlit应用的链接：
```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-choreography-generator.streamlit.app/)
```
