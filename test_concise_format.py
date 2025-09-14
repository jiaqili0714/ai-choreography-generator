#!/usr/bin/env python3
"""
测试简洁格式的编舞生成器
"""

def test_concise_format():
    """测试简洁格式"""
    print("🎭 测试简洁格式编舞生成器")
    print("=" * 50)
    
    # 模拟音频特征
    audio_features = {
        'energy_mean': 0.25,
        'spectral_centroid_mean': 2215.72
    }
    
    # 模拟片段数据
    segment = {
        "start_time": 0.0,
        "end_time": 3.72,
        "duration": 3.72,
        "beat_count": 8
    }
    
    bpm = 129.2
    dance_style = "Hip-Hop"
    segment_index = 0
    
    # 分析音乐特征
    energy_level = "高" if audio_features.get('energy_mean', 0) > 0.3 else "中" if audio_features.get('energy_mean', 0) > 0.15 else "低"
    tempo_feel = "很快" if bpm > 140 else "快" if bpm > 120 else "中等" if bpm > 100 else "慢"
    
    print(f"📊 音乐特征分析:")
    print(f"  - BPM: {bpm} ({tempo_feel}节奏)")
    print(f"  - 能量: {energy_level}")
    print(f"  - 舞蹈风格: {dance_style}")
    print(f"  - 节拍数: {segment['beat_count']}")
    
    print(f"\n🎯 新的简洁格式要求:")
    print(f"  1. 节奏要点: 分析音乐特点（如：节奏很快、气氛燥、需要力度大、有低音bass三连音等）")
    print(f"  2. 舞蹈元素: 推荐3-5个适配的舞蹈动作元素")
    print(f"  3. 关键提示: 1-2个最重要的技术要点")
    
    print(f"\n📋 新的输出字段:")
    fields = [
        "rhythm_analysis - 节奏分析",
        "dance_elements - 推荐的舞蹈元素列表",
        "key_tips - 关键提示",
        "difficulty - 难度等级(1-5)",
        "energy_level - 能量等级(1-5)",
        "reference_moves - 参考的经典动作名称列表"
    ]
    
    for i, field in enumerate(fields, 1):
        print(f"  {i}. {field}")
    
    print(f"\n✨ 改进效果:")
    print(f"  ✅ 更简洁的信息展示")
    print(f"  ✅ 重点突出节奏要点")
    print(f"  ✅ 实用的舞蹈元素推荐")
    print(f"  ✅ 关键提示一目了然")
    print(f"  ✅ 减少文字阅读负担")

def show_example_output():
    """显示示例输出"""
    print(f"\n" + "=" * 50)
    print("📝 示例输出对比")
    print("=" * 50)
    
    print("❌ 改进前 (太冗长):")
    old_output = {
        "description": "这个舞蹈片段采用House风格，以快节奏的音乐为基础，结合复杂的脚步动作展示出节奏感和力量感...",
        "beat_breakdown": "第1拍：右脚前踏，重心前移；第2拍：左脚后撤，手臂上举；第3拍：右脚外侧滑动，身体右侧倾斜...",
        "body_parts": "头部：保持自然，跟随身体律动；肩膀：放松，跟随手臂动作；手臂：配合脚步动作，展现流畅感...",
        "technical_points": "重心保持在两脚之间，膝盖微弯，保持核心稳定，手臂动作要与脚步配合流畅...",
        "common_mistakes": "1. 脚步不准确导致节奏混乱；2. 手臂动作缺乏协调性；3. 身体姿态不稳定...",
        "practice_steps": "1. 先练习脚步的基本节奏和动作；2. 逐步加入手臂动作，并与脚步配合练习..."
    }
    
    for key, value in old_output.items():
        print(f"  {key}: {value[:50]}...")
    
    print(f"\n✅ 改进后 (简洁实用):")
    new_output = {
        "rhythm_analysis": "节奏很快，气氛燥，需要力度大，低音bass有三连音",
        "dance_elements": ["Harlem Shake", "Running Man", "Freeze", "Slide"],
        "key_tips": "动作要卡在bass上，力度要大",
        "difficulty": 4,
        "energy_level": 5,
        "reference_moves": ["Harlem Shake", "Running Man"]
    }
    
    for key, value in new_output.items():
        print(f"  {key}: {value}")
    
    print(f"\n🎯 界面展示效果:")
    print(f"  🎵 节奏要点: 节奏很快，气氛燥，需要力度大，低音bass有三连音")
    print(f"  💃 舞蹈元素:")
    print(f"    • Harlem Shake")
    print(f"    • Running Man") 
    print(f"    • Freeze")
    print(f"    • Slide")
    print(f"  �� 关键提示: 动作要卡在bass上，力度要大")
    print(f"  📊 难度等级: ████████░░ 4/5")
    print(f"  ⚡ 能量等级: ██████████ 5/5")

def main():
    """主函数"""
    test_concise_format()
    show_example_output()
    
    print(f"\n" + "=" * 50)
    print("🎉 简洁格式编舞生成器改进完成！")
    print("=" * 50)
    print("🚀 现在信息更简洁，重点更突出！")
    print("💡 启动命令: streamlit run app.py")

if __name__ == "__main__":
    main()
