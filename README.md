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
short_description: AI choreography generator for music and dance
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
- 📱 **现代化界面**: 基于Streamlit的响应式用户界面

## 🚀 快速开始

### 在线体验
直接使用本应用，无需安装任何软件！

### 使用步骤
1. **设置API密钥**: 在侧边栏输入你的OpenAI API密钥
2. **上传音频**: 选择MP3或WAV格式的音频文件
3. **生成编舞**: 点击"生成编舞"按钮
4. **查看结果**: 在音乐播放器中查看舞蹈建议

## 🔑 获取OpenAI API密钥

1. 访问: https://platform.openai.com/api-keys
2. 点击 "Create new secret key"
3. 复制生成的密钥（以sk-开头）
4. 在应用中粘贴使用

**注意事项**:
- ✅ API密钥以 `sk-` 开头
- ✅ 密钥只显示一次，请妥善保存
- ✅ 确保账户有足够余额
- ✅ 密钥只在当前会话中有效

## 🎯 支持的舞蹈风格

- **Hip-Hop**: two-step, running-man, windmill, headspin, freeze
- **House**: jack, skate, lofting, vogue, waacking, liquid
- **K-pop**: point, wave, formation-change, synchronized-move
- **Jazz**: jazz-square, pas-de-bourree, leap, isolation
- **Contemporary**: contraction, release, spiral, floor-work
- **Breaking**: top-rock, footwork, power-move, windmill

## 🎨 技术特点

### 专业音频分析
- 使用librosa进行高精度音频特征提取
- 自动检测BPM和节拍点
- 智能识别音乐风格和情绪

### 结构化输出
- JSON格式的结构化编舞数据
- 包含动作层次、空间平面、动态变化
- 节奏占位符和教学建议

### 多样性控制
- 优化的LLM参数设置
- 动作去重和同义词替换
- Few-shot示例学习

## 📊 输出示例

```json
{
  "style": "Hip-Hop",
  "global_cues": {
    "energy_level": "high",
    "mood": "aggressive and confident",
    "key_characteristics": ["bounce", "isolation", "rhythmic precision"]
  },
  "segments": [
    {
      "idx": 0,
      "time": "0:00-0:16",
      "accent": "strong",
      "level": "mid",
      "plane": "frontal",
      "motifs": ["bounce", "rock"],
      "moves": ["two-step", "chest-pop", "shoulder-roll", "freeze"],
      "transition": "quarter-turn",
      "rhythm_breakdown": "1-2 two-step | 3 chest-pop | 4 hold | 5-6 shoulder-roll | 7&8 freeze"
    }
  ]
}
```

## 🌐 多语言支持

- 🇨🇳 **中文**: 完整的中文界面和帮助文档
- 🇺🇸 **English**: Complete English interface and documentation
- 🔄 **实时切换**: 支持运行时语言切换

## 🎭 使用方法

1. **上传音频文件**: 支持MP3/WAV格式
2. **生成编舞**: 点击"生成编舞"按钮
3. **查看建议**: 切换到"音乐播放器"标签页
4. **学习动作**: 点击YouTube搜索链接学习参考动作

## 🔧 技术栈

- **音频处理**: librosa, numpy, scipy
- **AI生成**: OpenAI GPT-3.5-turbo
- **前端界面**: Streamlit
- **部署平台**: Hugging Face Spaces

## 📝 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📞 联系方式

如有问题或建议，请通过GitHub Issues联系我们。

---

**让AI为全世界的音乐创作专属舞蹈！** 🎵💃
