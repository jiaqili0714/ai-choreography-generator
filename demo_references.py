#!/usr/bin/env python3
"""
舞蹈参考功能演示
"""

from dance_references import DANCE_REFERENCES, get_dance_references, get_random_reference

def demo_dance_references():
    """演示舞蹈参考功能"""
    print("🎬 舞蹈参考功能演示")
    print("=" * 60)
    
    # 显示所有可用的舞蹈风格
    print("�� 可用的舞蹈风格:")
    for style in DANCE_REFERENCES.keys():
        print(f"  • {style}")
    
    print("\n" + "=" * 60)
    
    # 演示Hip-Hop风格的参考
    print("🕺 Hip-Hop风格参考演示:")
    print("-" * 40)
    
    # 基础动作
    basic_refs = get_dance_references("Hip-Hop", "基础动作")
    print("📚 基础动作:")
    for ref in basic_refs:
        print(f"  • {ref['name']}: {ref['description']}")
        print(f"    视频: {ref['video_url']}")
        print(f"    难度: {ref['difficulty']}/5, 能量: {ref['energy_level']}/5")
        print()
    
    # 进阶动作
    advanced_refs = get_dance_references("Hip-Hop", "进阶动作")
    print("�� 进阶动作:")
    for ref in advanced_refs:
        print(f"  • {ref['name']}: {ref['description']}")
        print(f"    视频: {ref['video_url']}")
        print(f"    难度: {ref['difficulty']}/5, 能量: {ref['energy_level']}/5")
        print()
    
    print("=" * 60)
    
    # 演示随机选择
    print("🎲 随机选择演示:")
    print("-" * 40)
    
    for style in ["Hip-Hop", "Jazz", "K-pop"]:
        ref = get_random_reference(style, "基础动作")
        if ref:
            print(f"{style} 随机选择: {ref['name']}")
            print(f"  描述: {ref['description']}")
            print(f"  视频: {ref['video_url']}")
            print()

def demo_choreography_with_references():
    """演示带参考的编舞生成"""
    print("🎭 编舞生成演示 (带舞蹈参考)")
    print("=" * 60)
    
    # 模拟编舞结果
    demo_choreography = {
        "dance_style": "Hip-Hop",
        "bpm": 120.0,
        "total_segments": 3,
        "total_duration": 12.0,
        "summary": "这是一个充满活力的Hip-Hop编舞，包含经典动作如Harlem Shake和Running Man。",
        "segments": [
            {
                "description": "开场：使用Harlem Shake建立节奏感，配合基础步伐",
                "reference_moves": ["Harlem Shake"],
                "video_references": ["https://www.youtube.com/watch?v=8v9yUVgrmPY"],
                "difficulty": 2,
                "energy_level": 4,
                "key_moves": ["Harlem Shake", "基础步伐"],
                "learning_tips": "先练习头部和肩膀的协调动作，再配合脚步"
            },
            {
                "description": "第二段：加入Running Man动作，增加动感",
                "reference_moves": ["Running Man"],
                "video_references": ["https://www.youtube.com/watch?v=4v9yUVgrmPY"],
                "difficulty": 3,
                "energy_level": 4,
                "key_moves": ["Running Man", "节奏感"],
                "learning_tips": "注意脚步的节奏，保持身体的平衡"
            },
            {
                "description": "高潮段：Freeze技巧展示，突然定格",
                "reference_moves": ["Freeze"],
                "video_references": ["https://www.youtube.com/watch?v=6v9yUVgrmPY"],
                "difficulty": 4,
                "energy_level": 5,
                "key_moves": ["Freeze", "定格技巧"],
                "learning_tips": "练习突然停止的技巧，保持姿势稳定"
            }
        ]
    }
    
    print(f"💃 舞蹈风格: {demo_choreography['dance_style']}")
    print(f"🎶 BPM: {demo_choreography['bpm']}")
    print(f"📊 总片段数: {demo_choreography['total_segments']}")
    print(f"⏱️ 总时长: {demo_choreography['total_duration']}秒")
    print(f"\n📝 编舞总结:")
    print(f"   {demo_choreography['summary']}")
    
    print(f"\n🎭 分段动作详情:")
    for i, segment in enumerate(demo_choreography['segments']):
        print(f"\n   第{i+1}段:")
        print(f"   📝 描述: {segment['description']}")
        print(f"   🎬 参考动作: {', '.join(segment['reference_moves'])}")
        print(f"   📺 参考视频: {', '.join(segment['video_references'])}")
        print(f"   📊 难度: {segment['difficulty']}/5")
        print(f"   ⚡ 能量: {segment['energy_level']}/5")
        print(f"   🎯 关键动作: {', '.join(segment['key_moves'])}")
        print(f"   💡 学习建议: {segment['learning_tips']}")

def main():
    """主函数"""
    demo_dance_references()
    print("\n" + "=" * 60)
    demo_choreography_with_references()
    
    print("\n" + "=" * 60)
    print("🎉 演示完成！")
    print("💡 现在系统会为每个编舞片段提供:")
    print("   • 经典舞蹈动作参考")
    print("   • 参考视频链接")
    print("   • 详细的学习建议")
    print("   • 难度和能量评估")

if __name__ == "__main__":
    main()
