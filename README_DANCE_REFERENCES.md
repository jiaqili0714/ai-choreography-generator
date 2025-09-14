# 🎬 AI编舞生成器 - 舞蹈参考版

## ✨ 新功能特点

### 🎯 舞蹈参考视频系统
- **经典动作库**: 包含Harlem Shake、Running Man、Freeze等经典舞蹈动作
- **视频链接**: 每个动作都提供参考视频链接
- **难度分级**: 基础动作和进阶动作分类
- **学习建议**: 针对每个动作的详细学习指导

### 🕺 支持的舞蹈风格和动作

#### Hip-Hop
- **基础动作**: Harlem Shake, Running Man, Cabbage Patch
- **进阶动作**: Freeze, Slide

#### Jazz
- **基础动作**: Jazz Square, Pirouette
- **进阶动作**: Grand Jeté

#### K-pop
- **基础动作**: Point Dance, Wave
- **进阶动作**: Isolation

#### House
- **基础动作**: Jacking, Footwork

#### Breaking
- **基础动作**: Toprock, Six Step
- **进阶动作**: Windmill

## 🚀 使用方法

### 1. 启动系统
```bash
streamlit run app.py
```

### 2. 上传音频文件
- 支持MP3/WAV格式
- 系统会自动分析BPM和节拍

### 3. 生成编舞
- 系统会根据BPM推荐舞蹈风格
- 为每个8拍片段生成具体动作
- 提供经典动作参考和视频链接

### 4. 查看结果
- **动作描述**: 详细的文字说明
- **参考动作**: 经典舞蹈动作名称
- **参考视频**: 学习视频链接
- **学习建议**: 针对性的练习指导
- **难度评估**: 1-5级难度和能量评估

## 📋 输出格式示例

```json
{
  "description": "开场：使用Harlem Shake建立节奏感，配合基础步伐",
  "reference_moves": ["Harlem Shake"],
  "video_references": ["https://www.youtube.com/watch?v=8v9yUVgrmPY"],
  "difficulty": 2,
  "energy_level": 4,
  "key_moves": ["Harlem Shake", "基础步伐"],
  "learning_tips": "先练习头部和肩膀的协调动作，再配合脚步"
}
```

## 🎬 参考视频说明

### 当前状态
- 视频链接为示例链接
- 实际使用时需要替换为真实的舞蹈教学视频

### 建议的视频来源
- YouTube舞蹈教学频道
- 专业舞蹈工作室视频
- 经典舞蹈表演片段
- 舞蹈比赛视频

## 🔧 自定义舞蹈参考

### 添加新的舞蹈动作
编辑 `dance_references.py` 文件：

```python
"新动作": {
    "name": "动作名称",
    "description": "动作描述",
    "video_url": "视频链接",
    "difficulty": 3,
    "energy_level": 4
}
```

### 添加新的舞蹈风格
在 `DANCE_REFERENCES` 字典中添加新的风格分类。

## 💡 使用建议

1. **选择合适的参考视频**: 确保视频质量高，动作清晰
2. **循序渐进**: 从基础动作开始，逐步学习进阶动作
3. **反复练习**: 参考视频只是指导，需要大量练习
4. **结合音乐**: 将动作与音乐的节拍和情感结合

## 🎯 未来计划

- [ ] 集成真实的舞蹈教学视频API
- [ ] 添加更多舞蹈风格和动作
- [ ] 支持用户自定义动作库
- [ ] 添加动作难度自动调节
- [ ] 集成视频播放功能

## 📞 技术支持

如有问题或建议，请查看项目文档或联系开发团队。

---

🎵 **让AI为你的音乐创作专属舞蹈，现在有了更直观的参考视频！**
