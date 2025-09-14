#!/usr/bin/env python3
"""
测试改进的编舞生成系统
"""

def test_dance_vocabulary():
    """测试舞蹈词库系统"""
    print("🎭 测试舞蹈词库系统")
    print("=" * 50)
    
    from dance_vocabulary import get_candidate_moves, get_rhythm_analysis, get_dance_dimensions
    
    # 测试不同风格的候选动作
    styles = ["Hip-Hop", "House", "Jazz", "K-pop"]
    
    for style in styles:
        print(f"\n🎨 {style} 风格:")
        candidate_moves = get_candidate_moves(style, 8)
        print(f"  候选动作: {', '.join(candidate_moves)}")
        
        dimensions = get_dance_dimensions(style)
        print(f"  层次: {', '.join(dimensions['levels'])}")
        print(f"  平面: {', '.join(dimensions['planes'])}")
        print(f"  方向: {', '.join(dimensions['directions'])}")
    
    # 测试节奏分析
    print(f"\n🎵 节奏分析测试:")
    test_cases = [
        (129.2, 0.25, 2215.72),
        (140.0, 0.35, 3000.0),
        (90.0, 0.15, 1500.0)
    ]
    
    for bpm, energy, spectral_centroid in test_cases:
        rhythm_analysis = get_rhythm_analysis(bpm, energy, spectral_centroid)
        print(f"  BPM {bpm}, 能量 {energy:.2f}: {rhythm_analysis}")

def show_improvement_comparison():
    """显示改进对比"""
    print(f"\n" + "=" * 50)
    print("📊 改进对比")
    print("=" * 50)
    
    print("❌ 改进前 (问题):")
    print("  - 输出词汇贫乏，常重复 'wave / slide / groove' 等动作")
    print("  - 建议过于单一，缺少层次、方向、过渡等多样性")
    print("  - BPM一直都是129.2，风格都是hiphop")
    print("  - 节奏要点全都是'低音bass'")
    print("  - AI提示词只是一个例子，但AI完全用一样的")
    
    print(f"\n✅ 改进后 (解决方案):")
    print("  - 使用舞蹈动作词库，提供丰富的动作选择")
    print("  - 结构化JSON输出，包含层次、平面、方向等维度")
    print("  - 多样化的节奏分析，避免重复描述")
    print("  - 候选动作池 + 避免重复机制")
    print("  - 高温参数 + 频率惩罚，增加多样性")
    print("  - 后处理去重和同义词替换")
    
    print(f"\n🎯 新的输出格式:")
    new_output = {
        "rhythm_analysis": "节奏适中，气氛轻松，节拍器突出",
        "accent": "on 1 & 3",
        "level": "mid",
        "plane": "frontal",
        "dance_elements": ["step-touch", "chest pop", "hip roll", "grapevine"],
        "transition": "turn 90° to DL",
        "key_tips": "保持身体协调，注意重心转移",
        "difficulty": 3,
        "energy_level": 4
    }
    
    for key, value in new_output.items():
        print(f"  {key}: {value}")

def main():
    """主函数"""
    test_dance_vocabulary()
    show_improvement_comparison()
    
    print(f"\n" + "=" * 50)
    print("🎉 改进的编舞生成系统测试完成！")
    print("=" * 50)
    print("✨ 主要改进:")
    print("  • 舞蹈动作词库系统")
    print("  • 结构化JSON输出")
    print("  • 多样化节奏分析")
    print("  • 候选动作池 + 避免重复")
    print("  • 高温参数 + 频率惩罚")
    print("  • 后处理去重和同义词替换")
    print("\n🚀 现在可以生成更丰富、更多样的舞蹈建议了！")

if __name__ == "__main__":
    main()
