# 🚀 Hugging Face Space 部署步骤指南

## 📋 你已经完成：✅ 创建Space

现在需要完成以下步骤来部署你的AI编舞生成器：

## 🎯 下一步操作

### 步骤1: 准备部署文件
我已经为你准备好了所有必要的文件，现在需要复制到正确的位置：

```bash
# 复制Hugging Face优化的文件
cp requirements_huggingface.txt requirements.txt
cp README_huggingface.md README.md
```

### 步骤2: 上传文件到Space
在你的Hugging Face Space页面：

1. **点击 "Files and versions" 标签页**
2. **点击 "Add file" → "Upload files"**
3. **上传以下文件**：

#### 必需文件列表：
- ✅ `app.py` - 主应用文件
- ✅ `requirements.txt` - 依赖文件 (使用Hugging Face优化版本)
- ✅ `README.md` - 说明文档 (使用Hugging Face优化版本)

#### 功能模块文件：
- ✅ `streamlit_cloud_choreography_generator.py` - 编舞生成器
- ✅ `streamlit_cloud_audio_analyzer.py` - 音频分析器
- ✅ `enhanced_llm_choreographer.py` - LLM编舞器
- ✅ `action_database.py` - 动作数据库
- ✅ `language_config.py` - 多语言配置
- ✅ `dance_references.py` - 舞蹈参考
- ✅ `config.py` - 配置文件

### 步骤3: 设置环境变量
1. **点击 "Settings" 标签页**
2. **在 "Repository secrets" 部分**：
   - 点击 "New secret"
   - **Name**: `OPENAI_API_KEY`
   - **Value**: 你的OpenAI API密钥 (以sk-开头)
   - 点击 "Add secret"

### 步骤4: 等待部署
1. **返回 "App" 标签页**
2. **等待应用启动** (通常需要2-5分钟)
3. **查看日志** 确保没有错误

## 🔧 文件内容

### requirements.txt 内容：
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

### README.md 内容：
```markdown
---
title: AI Choreography Generator
emoji: 💃
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

## 🎯 部署检查清单

### 文件上传检查：
- [ ] `app.py` 已上传
- [ ] `requirements.txt` 已上传 (Hugging Face优化版本)
- [ ] `README.md` 已上传 (Hugging Face优化版本)
- [ ] 所有功能模块文件已上传
- [ ] 配置文件已上传

### 环境变量检查：
- [ ] `OPENAI_API_KEY` 已设置
- [ ] API密钥格式正确 (以sk-开头)
- [ ] 密钥有效且有余额

### 部署状态检查：
- [ ] 应用正在启动
- [ ] 没有错误日志
- [ ] 可以访问应用界面

## 🎉 完成！

部署完成后，你的应用将在以下地址运行：
`https://huggingface.co/spaces/your-username/your-space-name`

## 🔧 故障排除

### 如果部署失败：
1. 检查所有文件是否已上传
2. 验证requirements.txt内容
3. 确认README.md格式正确
4. 检查环境变量设置

### 如果应用无法启动：
1. 查看日志中的错误信息
2. 检查依赖库版本兼容性
3. 验证API密钥有效性

### 如果功能异常：
1. 测试API密钥是否有效
2. 检查音频文件格式
3. 验证网络连接

## 🎭 功能特点

部署成功后，你将拥有：
- ✅ 专业音频分析
- ✅ 结构化编舞输出
- ✅ 多语言界面
- ✅ 动作词库
- ✅ 多样性控制
- ✅ 实时音乐播放

让AI为全世界的音乐创作专业级舞蹈！🎵💃🌐
