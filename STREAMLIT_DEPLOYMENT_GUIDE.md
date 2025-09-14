# 🚀 Streamlit Cloud 部署指南

## ✅ GitHub仓库已准备就绪
你的代码已经成功推送到: https://github.com/jiaqili0714/ai-choreography-generator

## 📋 Streamlit Cloud 部署步骤

### 步骤1: 访问Streamlit Cloud
1. 打开浏览器，访问: https://share.streamlit.io
2. 点击 "Sign in with GitHub" 使用你的GitHub账户登录

### 步骤2: 创建新应用
1. 点击 "New app" 按钮
2. 填写以下信息:
   - **Repository**: `jiaqili0714/ai-choreography-generator`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: `ai-choreography-generator` (可以自定义)

### 步骤3: 配置环境变量
在 "Advanced settings" 部分，点击 "Secrets" 选项卡，添加:
```
OPENAI_API_KEY = "your-openai-api-key-here"
```
**重要**: 将 `your-openai-api-key-here` 替换为你的真实OpenAI API密钥

### 步骤4: 部署应用
1. 点击 "Deploy!" 按钮
2. 等待部署完成 (通常需要2-5分钟)
3. 部署成功后，你会看到一个公开的URL

## 🎯 部署后的应用URL
你的应用将可以通过以下URL访问:
`https://ai-choreography-generator.streamlit.app/`

## 📝 部署检查清单
- [ ] GitHub仓库: https://github.com/jiaqili0714/ai-choreography-generator
- [ ] Streamlit Cloud应用已创建
- [ ] 环境变量 OPENAI_API_KEY 已设置
- [ ] 应用可以正常访问
- [ ] 测试上传音频文件功能

## 🔧 如果遇到问题

### 常见问题1: 部署失败
- 检查 `requirements.txt` 是否包含所有依赖
- 确保 `app.py` 文件在根目录
- 检查环境变量是否正确设置

### 常见问题2: API密钥问题
- 确保在Streamlit Cloud的Secrets中正确设置了 `OPENAI_API_KEY`
- 检查API密钥是否有效且有足够额度

### 常见问题3: 依赖问题
- 确保所有依赖都在 `requirements.txt` 中
- 检查Python版本兼容性

## 🎉 完成！
部署完成后，你的AI编舞生成器就可以在互联网上访问了！

## 📱 分享你的应用
部署成功后，你可以:
1. 分享应用URL给朋友
2. 在社交媒体上推广
3. 添加到你的GitHub README中
4. 创建演示视频展示功能

让AI为全世界的音乐创作专属舞蹈！🎵💃
