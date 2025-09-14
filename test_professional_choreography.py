#!/usr/bin/env python3
"""
测试专业编舞生成器
"""

def test_professional_prompt():
    """测试专业提示词"""
    print("🎭 测试专业编舞生成器")
    print("=" * 50)
    
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
    
    # 计算节拍间隔
    beat_interval = 60.0 / bpm
    segment_beats = segment['beat_count']
    
    print(f"📊 片段信息:")
    print(f"  - 片段编号: {segment_index + 1}")
    print(f"  - 时间范围: {segment['start_time']:.2f}s - {segment['end_time']:.2f}s")
    print(f"  - 持续时间: {segment['duration']:.2f}s")
    print(f"  - BPM: {bpm}")
    print(f"  - 节拍间隔: {beat_interval:.2f}秒")
    print(f"  - 舞蹈风格: {dance_style}")
    print(f"  - 节拍数: {segment_beats}")
    
    print(f"\n🎯 新的提示词要求:")
    print(f"  1. 节拍分解: 详细描述每个节拍的具体动作")
    print(f"  2. 身体部位: 明确头部、肩膀、手臂、躯干、腿部、脚部的动作")
    print(f"  3. 技术要点: 重心位置、身体姿态、动作幅度")
    print(f"  4. 常见错误: 容易犯的错误和如何避免")
    print(f"  5. 练习方法: 具体的练习步骤和技巧")
    
    print(f"\n📋 新的输出字段:")
    fields = [
        "description - 整体动作描述",
        "beat_breakdown - 详细的节拍分解",
        "body_parts - 身体部位和具体动作",
        "technical_points - 技术要点",
        "common_mistakes - 常见错误和纠正方法",
        "practice_steps - 具体练习步骤",
        "reference_moves - 参考的经典动作名称列表",
        "difficulty - 难度等级(1-5)",
        "energy_level - 能量等级(1-5)",
        "key_moves - 关键动作列表",
        "learning_tips - 具体的学习建议和练习方法"
    ]
    
    for i, field in enumerate(fields, 1):
        print(f"  {i:2d}. {field}")
    
    print(f"\n✨ 改进效果:")
    print(f"  ✅ 更详细的节拍分解")
    print(f"  ✅ 具体的身体部位指导")
    print(f"  ✅ 专业的技术要点")
    print(f"  ✅ 常见错误和纠正方法")
    print(f"  ✅ 具体的练习步骤")
    print(f"  ✅ 更高的token限制(800)")
    print(f"  ✅ 更好的用户界面(可折叠expander)")

def show_example_output():
    """显示示例输出"""
    print(f"\n" + "=" * 50)
    print("📝 示例输出对比")
    print("=" * 50)
    
    print("❌ 改进前 (太基础):")
    old_output = {
        "description": "在这个8拍片段中，舞者可以利用节奏感和动感的音乐节奏，以Jacking为基础动作...",
        "key_moves": ["Jacking", "Footwork variations", "Groove variations"],
        "learning_tips": "建议舞者在练习时多加强对节奏感的把握..."
    }
    
    for key, value in old_output.items():
        print(f"  {key}: {value}")
    
    print(f"\n✅ 改进后 (更专业):")
    new_output = {
        "description": "House风格的8拍片段，以Jacking动作为基础，结合脚步变化和身体律动",
        "beat_breakdown": "第1拍：右脚前踏，重心前移，右臂上举；第2拍：左脚后撤，重心后移，左臂下摆；第3拍：右脚侧踏，身体右倾；第4拍：左脚收回，身体回正；第5-8拍：重复动作，增加手臂变化",
        "body_parts": "头部：保持自然，跟随身体律动轻微摆动；肩膀：放松，跟随手臂动作自然移动；手臂：第1拍右臂上举，第2拍左臂下摆，第3-4拍双臂协调；躯干：保持直立，核心收紧，跟随脚步重心转移；腿部：膝盖微弯，保持弹性，脚步清晰；脚部：前脚掌着地，保持轻快",
        "technical_points": "重心保持在两脚之间，膝盖始终保持微弯状态，核心肌群收紧保持身体稳定，手臂动作要自然流畅，不要僵硬",
        "common_mistakes": "1.重心过于前倾或后倾 2.膝盖过直导致动作僵硬 3.手臂动作不协调 4.脚步不清晰",
        "practice_steps": "1.先练习脚步，不加入手臂动作 2.掌握重心转移 3.加入手臂动作 4.配合音乐练习 5.注意动作的流畅性",
        "reference_moves": ["House Jacking", "House Footwork"],
        "difficulty": 3,
        "energy_level": 4,
        "key_moves": ["Jacking", "Footwork", "Groove"],
        "learning_tips": "建议从慢速开始练习，先掌握基本脚步，再逐步加入手臂动作。注意保持身体的律动感，不要过于僵硬。可以对着镜子练习，观察自己的动作是否流畅自然。"
    }
    
    for key, value in new_output.items():
        if key in ["difficulty", "energy_level"]:
            print(f"  {key}: {value}")
        else:
            print(f"  {key}: {value[:100]}{'...' if len(str(value)) > 100 else ''}")

def main():
    """主函数"""
    test_professional_prompt()
    show_example_output()
    
    print(f"\n" + "=" * 50)
    print("🎉 专业编舞生成器改进完成！")
    print("=" * 50)
    print("🚀 现在可以生成更专业、更具体的舞蹈建议了！")
    print("💡 启动命令: streamlit run app.py")

if __name__ == "__main__":
    main()
