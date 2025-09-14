# 🚀 快速开始指南

## 📋 系统要求

- Python 3.8+
- OpenAI API密钥（用于AI生成功能）

## ⚡ 一键启动

```bash
./start.sh
```

## 🎯 三种使用方式

### 1. 🌐 Web界面（推荐新手）

```bash
streamlit run app.py
```

**特点：**
- 友好的图形界面
- 拖拽上传音频文件
- 实时显示生成进度
- 可视化编舞结果

### 2. 💻 命令行工具（适合批量处理）

```bash
# 基本使用
python main.py your_audio_file.mp3

# 指定输出文件
python main.py your_audio_file.mp3 -o my_choreography.json

# 指定API密钥
python main.py your_audio_file.mp3 --api-key your_api_key
```

### 3. 🎭 功能演示（无需API密钥）

```bash
python demo.py
```

**特点：**
- 展示系统核心功能
- 无需API密钥
- 了解输出格式

## 🔑 API密钥设置

### 方法1：环境变量
```bash
export OPENAI_API_KEY="your_api_key_here"
```

### 方法2：Web界面
在侧边栏输入API密钥

### 方法3：命令行参数
```bash
python main.py audio.mp3 --api-key your_api_key
```

## 📁 支持的音频格式

- ✅ MP3
- ✅ WAV
- ⚠️ 其他格式（需要转换）

## 🎵 示例输出

```json
{
  "audio_info": {
    "bpm": 120.0,
    "duration": 16.0,
    "total_beats": 32
  },
  "choreography": {
    "dance_style": "Hip-Hop",
    "summary": "充满活力的Hip-Hop编舞",
    "segments": [
      {
        "description": "开场：跟随节拍的基础步伐",
        "emoji_sequence": "👟➡️🕺💃",
        "difficulty": 2,
        "energy_level": 3,
        "key_moves": ["基础步伐", "节奏感"]
      }
    ]
  }
}
```

## 🆘 常见问题

### Q: 没有API密钥怎么办？
A: 可以运行 `python demo.py` 查看功能演示

### Q: 音频文件无法处理？
A: 确保文件格式为MP3或WAV，文件大小不超过100MB

### Q: BPM检测不准确？
A: 确保音频质量良好，节拍清晰

### Q: 生成的编舞不满意？
A: 可以尝试不同的音频文件，或调整API参数

## 🎯 使用技巧

1. **音频质量**: 使用清晰的音频文件获得更好的BPM检测
2. **文件大小**: 建议使用3-5分钟的音频文件
3. **节拍清晰**: 选择节拍明显的音乐
4. **风格匹配**: 系统会根据BPM自动推荐合适的舞蹈风格

## 📞 获取帮助

- 运行 `python test_system.py` 检查系统状态
- 查看 `README.md` 了解详细功能
- 查看 `PROJECT_SUMMARY.md` 了解项目架构

---

🎉 **开始你的AI编舞之旅吧！**
