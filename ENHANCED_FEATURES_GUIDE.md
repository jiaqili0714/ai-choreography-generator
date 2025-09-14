# 🎭 增强编舞生成系统功能指南

## 🚀 系统升级概述

你的AI编舞生成器已经升级为专业级系统，具备以下增强功能：

### 1. **专业音频分析** 🎵
- **librosa**: 基础音频特征提取
- **madmom**: 精确节拍和下拍检测
- **Essentia**: 高级音频特征（情绪、亮度、和声）
- **musicnn**: 音乐风格识别

### 2. **结构化输出** 📋
- **JSON Schema**: 严格的结构化输出格式
- **字段完整**: style, global_cues, segments[idx, time, accent, level, plane, motifs, moves, transition]
- **数据验证**: 自动校验输出格式

### 3. **多样性控制** 🎨
- **参数优化**: temperature=0.9, presence_penalty=0.6, frequency_penalty=0.4
- **动作去重**: 避免连续段落动作重复
- **同义词替换**: 丰富动作词汇表达

### 4. **Few-shot示例** 📚
- **示例学习**: 在prompt中包含1-2段示例JSON
- **风格模仿**: 模型学习词汇和结构模式
- **质量提升**: 更专业和一致的输出

### 5. **动作词库 + RAG** 🎭
- **风格分类**: Hip-Hop/House/K-pop/Jazz/Contemporary/Breaking
- **候选动作池**: 每次生成前抽取10-15个候选动作
- **避免重复**: 明确"需避免动作"列表

### 6. **动作维度词汇** 📐
- **level**: high/mid/low/floor
- **plane**: frontal/sagittal/transverse
- **direction**: UL/UR/DL/DR, CW/CCW
- **dynamics**: staccato/legato/groove/hit/melt
- **initiation**: head/shoulder/chest/hip/knee/foot
- **transition**: quarter_turn, spin, level_drop, travel_diagonal

### 7. **后处理增强** ✨
- **JSON校验**: 自动验证输出格式
- **同义词替换**: wave→ripple/undulation/sway
- **节奏占位**: 1-2 two-step | 3 chest pop | 4 hold | 5-6 slide | 7&8 freeze

## 🎯 使用方法

### 基本使用
```python
from enhanced_choreography_generator import EnhancedChoreographyGenerator

generator = EnhancedChoreographyGenerator()
result = generator.generate_choreography_from_file("audio.mp3")
```

### 输出结构
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

## 🔧 技术架构

### 文件结构
```
├── enhanced_audio_analyzer.py      # 增强音频分析器
├── enhanced_llm_choreographer.py   # 增强LLM编舞生成器
├── enhanced_choreography_generator.py # 增强编舞生成器
├── action_database.py              # 动作词库数据库
└── app.py                         # 主应用（已更新）
```

### 依赖库
```
librosa>=0.10.1          # 音频处理
madmom>=0.16.1           # 节拍检测
essentia>=2.1b6.dev1110  # 高级特征
musicnn>=0.1.0           # 风格识别
jsonschema>=4.17.0       # JSON验证
pydantic>=2.0.0          # 数据验证
```

## 🎨 动作词库

### 支持风格
- **Hip-Hop**: two-step, running-man, windmill, headspin, freeze
- **House**: jack, skate, lofting, vogue, waacking, liquid
- **K-pop**: point, wave, formation-change, synchronized-move
- **Jazz**: jazz-square, pas-de-bourree, leap, isolation
- **Contemporary**: contraction, release, spiral, floor-work
- **Breaking**: top-rock, footwork, power-move, windmill

### 动作维度
- **层次变化**: high/mid/low/floor
- **空间平面**: frontal/sagittal/transverse
- **动态变化**: strong/medium/weak accent
- **过渡方式**: quarter_turn, level_drop, travel_diagonal

## 🚀 性能提升

### 生成质量
- ✅ **词汇丰富**: 避免"基础动作"等贫乏表达
- ✅ **结构清晰**: 层次分明，方向明确
- ✅ **风格一致**: 符合特定舞蹈风格特点
- ✅ **节奏精确**: 8拍分割，节拍对应

### 用户体验
- ✅ **实时反馈**: 详细的生成进度显示
- ✅ **错误处理**: 完善的异常处理和备用方案
- ✅ **多语言**: 支持中英文界面
- ✅ **专业输出**: 教学建议和难度评估

## 🎯 使用建议

### 最佳实践
1. **音频质量**: 使用清晰的音频文件
2. **风格选择**: 让系统自动识别或手动指定
3. **动作学习**: 参考YouTube搜索链接
4. **渐进练习**: 从简单动作开始，逐步提升

### 故障排除
- **依赖问题**: 确保所有库正确安装
- **API问题**: 检查OpenAI API密钥和额度
- **音频问题**: 支持MP3/WAV格式，建议时长30秒-5分钟

## 🎉 完成！

你的AI编舞生成器现在是一个专业级系统！

**主要优势**:
- 🎭 专业动作词库
- 📊 高级音频分析
- 🎨 结构化输出
- 🌐 多语言支持
- ✨ 多样性控制

**应用URL**: `https://ai-choreography-generator.streamlit.app/`

让AI为全世界的音乐创作专业级舞蹈！🎵💃🌐
