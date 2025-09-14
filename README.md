# 🎵 AI编舞生成器

一个基于AI的智能编舞生成系统，能够分析音乐特征并生成专业的舞蹈建议。

## ✨ 功能特点

- 🎶 **音频分析**: 自动检测BPM、节拍点和音频特征
- 🎭 **舞蹈风格推荐**: 根据音乐特征智能推荐最适合的舞蹈风格
- 💃 **编舞生成**: 为每个8拍片段生成详细的舞蹈动作建议
- 🎬 **视频搜索**: 提供YouTube搜索链接，方便学习参考动作
- ⏰ **实时同步**: 音乐播放与舞蹈建议实时同步显示
- 📱 **Web界面**: 基于Streamlit的现代化用户界面

## 🚀 快速开始

### 在线体验
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app/)

### 本地运行

1. **克隆项目**
```bash
git clone https://github.com/your-username/ai-choreography-generator.git
cd ai-choreography-generator
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **设置API密钥**
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

4. **启动应用**
```bash
streamlit run app.py
```

## 🎯 使用方法

1. **上传音频文件**: 支持MP3/WAV格式
2. **生成编舞**: 点击"生成编舞"按钮
3. **查看建议**: 切换到"音乐播放器"标签页
4. **学习动作**: 点击YouTube搜索链接学习参考动作

## 🎭 支持的舞蹈风格

- **Hip-Hop**: Harlem Shake, Running Man, Freeze, Slide
- **House**: Jacking, Footwork, Groove
- **Jazz**: Jazz Square, Pirouette, Grand Jeté
- **K-pop**: Point Dance, Wave, Isolation
- **Breaking**: Toprock, Six Step, Windmill
- **Contemporary**: 现代舞基础动作
- **Popping**: 机械舞技巧
- **Locking**: 锁舞动作
- **Waacking**: 甩手舞
- **Voguing**: 时尚舞

## 🔧 技术架构

### 音频处理
- **librosa**: 音乐信息检索和BPM检测
- **numpy**: 数值计算和数组处理
- **scipy**: 科学计算

### AI生成
- **OpenAI GPT-3.5-turbo**: 舞蹈建议生成
- **JSON解析**: 结构化输出处理

### 前端界面
- **Streamlit**: Web应用框架
- **HTML5 Audio**: 音频播放
- **实时更新**: 时间同步显示

## 📊 项目结构

```
ai-choreography-generator/
├── app.py                    # 主应用文件
├── choreography_generator.py # 编舞生成器
├── llm_choreographer.py     # LLM编舞生成器
├── audio_processor.py       # 音频处理器
├── dance_references.py      # 舞蹈参考数据库
├── config.py               # 配置文件
├── requirements.txt        # 依赖包列表
└── README.md              # 项目说明
```

## 🎵 工作原理

1. **音频分析**: 使用librosa分析音频的BPM、节拍点和频谱特征
2. **音乐分割**: 将音乐分割成8拍片段，便于编舞设计
3. **风格推荐**: AI根据音乐特征推荐最适合的舞蹈风格
4. **动作生成**: 为每个片段生成具体的舞蹈动作建议
5. **实时展示**: 在Web界面中实时显示舞蹈建议

## 📝 输出格式

每个音乐片段会生成以下信息：

- **🎵 节奏要点**: 音乐特征分析（如："节奏很快，气氛燥，需要力度大"）
- **💃 舞蹈元素**: 推荐的舞蹈动作列表
- **💡 关键提示**: 重要的技术要点
- **📊 难度等级**: 1-5级难度评估
- **⚡ 能量等级**: 1-5级能量评估
- **🎬 参考动作**: 经典舞蹈动作名称

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

MIT License

## 🙏 致谢

- [librosa](https://librosa.org/) - 音乐信息检索库
- [OpenAI](https://openai.com/) - AI语言模型
- [Streamlit](https://streamlit.io/) - Web应用框架

---

🎵 **让AI为你的音乐创作专属舞蹈！** 💃
