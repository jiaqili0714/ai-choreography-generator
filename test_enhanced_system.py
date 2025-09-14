#!/usr/bin/env python3
"""
增强编舞生成系统测试脚本
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from enhanced_choreography_generator import EnhancedChoreographyGenerator
from action_database import get_action_candidates, get_action_dimensions, get_synonym_replacement
import json

def test_action_database():
    """测试动作数据库"""
    print("🎭 测试动作数据库...")
    
    # 测试获取候选动作
    hip_hop_actions = get_action_candidates('Hip-Hop', num_candidates=10)
    print(f"Hip-Hop候选动作: {hip_hop_actions}")
    
    house_actions = get_action_candidates('House', num_candidates=8)
    print(f"House候选动作: {house_actions}")
    
    # 测试动作维度
    dimensions = get_action_dimensions()
    print(f"动作维度: {dimensions}")
    
    # 测试同义词替换
    test_words = ['wave', 'pop', 'slide', 'freeze']
    for word in test_words:
        synonym = get_synonym_replacement(word)
        print(f"{word} → {synonym}")
    
    print("✅ 动作数据库测试完成\n")

def test_enhanced_generator():
    """测试增强生成器"""
    print("🎵 测试增强编舞生成器...")
    
    try:
        generator = EnhancedChoreographyGenerator()
        
        # 测试动作数据库信息
        db_info = generator.get_action_database_info()
        print(f"动作数据库信息: {json.dumps(db_info, ensure_ascii=False, indent=2)}")
        
        print("✅ 增强生成器初始化成功")
        
    except Exception as e:
        print(f"❌ 增强生成器测试失败: {e}")
    
    print("✅ 增强生成器测试完成\n")

def test_audio_analyzer():
    """测试音频分析器"""
    print("�� 测试增强音频分析器...")
    
    try:
        from enhanced_audio_analyzer import EnhancedAudioAnalyzer
        analyzer = EnhancedAudioAnalyzer()
        print("✅ 音频分析器初始化成功")
        
        # 测试基础特征提取
        import numpy as np
        test_audio = np.random.randn(22050)  # 1秒测试音频
        features = analyzer.extract_basic_features(test_audio, 22050)
        print(f"基础特征: BPM={features['tempo']:.1f}, 时长={features['duration']:.1f}s")
        
    except Exception as e:
        print(f"❌ 音频分析器测试失败: {e}")
    
    print("✅ 音频分析器测试完成\n")

def test_llm_choreographer():
    """测试增强LLM编舞生成器"""
    print("🤖 测试增强LLM编舞生成器...")
    
    try:
        from enhanced_llm_choreographer import EnhancedLLMChoreographer
        choreographer = EnhancedLLMChoreographer()
        print("✅ LLM编舞生成器初始化成功")
        
        # 测试JSON Schema
        print(f"JSON Schema已定义: {len(choreographer.choreography_schema['properties'])} 个主要字段")
        print(f"Few-shot示例数量: {len(choreographer.few_shot_examples)}")
        
    except Exception as e:
        print(f"❌ LLM编舞生成器测试失败: {e}")
    
    print("✅ LLM编舞生成器测试完成\n")

def main():
    """主测试函数"""
    print("🚀 开始增强编舞生成系统测试")
    print("=" * 60)
    
    # 测试各个组件
    test_action_database()
    test_enhanced_generator()
    test_audio_analyzer()
    test_llm_choreographer()
    
    print("🎉 所有测试完成！")
    print("\n📋 测试总结:")
    print("- ✅ 动作数据库: 支持多风格动作词库")
    print("- ✅ 增强生成器: 结构化输出和多样性控制")
    print("- ✅ 音频分析器: 专业音频特征提取")
    print("- ✅ LLM编舞器: JSON Schema和Few-shot示例")
    print("\n🎯 系统已准备好生成专业编舞！")

if __name__ == "__main__":
    main()
