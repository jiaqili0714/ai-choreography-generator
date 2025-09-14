# 🚀 Hugging Face Spaces 手动部署指南

## 📋 快速部署步骤

### 步骤1: 创建 Hugging Face 账户
1. 访问: https://huggingface.co/
2. 点击 "Sign Up" 注册账户
3. 验证邮箱

### 步骤2: 创建新的 Space
1. 访问: https://huggingface.co/new-space
2. 填写信息:
   - **Space name**: `ai-choreography-generator`
   - **License**: `MIT`
   - **SDK**: `Streamlit`
   - **Hardware**: `CPU basic` (免费)
   - **Visibility**: `Public`
3. 点击 "Create Space"

### 步骤3: 上传文件
在Space创建后，点击 "Files and versions" 标签页，然后上传以下文件：

#### 必需文件列表:
1. **app.py** - 主应用文件
2. **requirements.txt** - 依赖文件 (使用 requirements_huggingface.txt 的内容)
3. **README.md** - 说明文档 (使用 README_huggingface.md 的内容)
4. **streamlit_cloud_choreography_generator.py** - 编舞生成器
5. **streamlit_cloud_audio_analyzer.py** - 音频分析器
6. **enhanced_llm_choreographer.py** - LLM编舞器
7. **action_database.py** - 动作数据库
8. **language_config.py** - 多语言配置
9. **dance_references.py** - 舞蹈参考
10. **config.py** - 配置文件

### 步骤4: 设置环境变量
1. 点击 "Settings" 标签页
2. 在 "Repository secrets" 部分添加:
   - **Name**: `OPENAI_API_KEY`
   - **Value**: 你的OpenAI API密钥
3. 点击 "Add secret"

### 步骤5: 等待部署
1. 返回 "App" 标签页
2. 等待应用启动 (通常需要2-5分钟)
3. 查看日志确保没有错误

## 🔧 文件内容

### requirements.txt 内容:
```
# AI Choreography Generator - Hugging Face Spaces Optimized Dependencies
librosa==0.10.1
numpy==1.24.3
scipy==1.11.1
soundfile==0.12.1
openai==1.3.0
streamlit==1.28.1
matplotlib==3.7.2
pandas==2.0.3
jsonschema==4.17.2
pydantic==2.0.0
python-dotenv==1.0.0
setuptools==68.0.0
wheel==0.40.0
huggingface-hub==0.17.0
```

### README.md 内容:
```markdown
---
title: AI Choreography Generator
emoji: ��
colorFrom: pink
colorTo: purple
sdk: streamlit
sdk_version: 1.28.1
app_file: app.py
pinned: false
license: mit
short_description: AI-powered choreography generator that analyzes music and creates dance suggestions
---

# 🎵 AI Choreography Generator

一个基于AI的智能编舞生成系统，能够分析音乐特征并生成专业的舞蹈建议。

## ✨ 功能特点

- 🎶 **音频分析**: 自动检测BPM、节拍点和音频特征
- 🎭 **舞蹈风格推荐**: 根据音乐特征智能推荐最适合的舞蹈风格
- 💃 **编舞生成**: 为每个8拍片段生成详细的舞蹈动作建议
- 🎬 **视频搜索**: 提供YouTube搜索链接，方便学习参考动作
- ⏰ **实时同步**: 音乐播放与舞蹈建议实时同步显示
- 🌐 **多语言支持**: 支持中文和英文界面

## 🚀 快速开始

1. **设置API密钥**: 在侧边栏输入你的OpenAI API密钥
2. **上传音频**: 选择MP3或WAV格式的音频文件
3. **生成编舞**: 点击"生成编舞"按钮
4. **查看结果**: 在音乐播放器中查看舞蹈建议

## 🔑 获取OpenAI API密钥

1. 访问: https://platform.openai.com/api-keys
2. 点击 "Create new secret key"
3. 复制生成的密钥（以sk-开头）
4. 在应用中粘贴使用

---

**让AI为全世界的音乐创作专属舞蹈！** 🎵💃
```

## 🎯 部署后配置

### 环境变量设置
在Space的Settings中添加以下环境变量：
- `OPENAI_API_KEY`: 你的OpenAI API密钥

### 硬件配置
- **CPU**: 免费提供，足够运行音频分析
- **内存**: 自动分配，支持临时文件处理
- **存储**: 支持音频文件上传和处理

## 🎉 完成！

部署完成后，你的AI编舞生成器将在Hugging Face Spaces上运行！

**访问地址**: `https://huggingface.co/spaces/your-username/ai-choreography-generator`

**优势**:
- 🚀 更稳定的部署
- 🎭 完整的功能支持
- 🌐 更好的用户体验
- 💰 完全免费使用

让AI为全世界的音乐创作专业级舞蹈！🎵💃🌐
