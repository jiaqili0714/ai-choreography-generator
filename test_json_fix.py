#!/usr/bin/env python3
"""
测试JSON解析修复
"""

import json
import re

def test_json_cleaning():
    """测试JSON清理功能"""
    print("🧪 测试JSON解析修复...")
    
    # 模拟API返回的内容（包含markdown标记）
    api_response = '''```json
{
    "description": "在8拍片段中，以快速的步伐踏步为主要动作，配合上身的摆动和手臂的挥动，强调舞者的节奏感和动感。",
    "reference_moves": ["Running Man", "Shuffle", "T-Step"],
    "video_references": ["https://www.youtube.com/watch?v=Jm02rT8Wb88", "https://www.youtube.com/watch?v=5q_G6rJ4CvU", "https://www.youtube.com/watch?v=9tD5Wk2FD-0"],
    "difficulty": 3,
    "energy_level": 4,
    "key_moves": ["快速的踏步", "上身的摆动", "手臂的挥动"],
    "learning_tips": "建议从慢速开始练习，逐渐加快节奏。注意保持身体的平衡和控制手臂的力度，同时注重整体的舞蹈节奏感。"
}
```'''
    
    print("📝 原始API响应:")
    print(api_response)
    print("\n" + "="*60)
    
    # 清理JSON响应
    def clean_json_response(content):
        # 移除markdown代码块标记
        content = re.sub(r'```json\s*', '', content)
        content = re.sub(r'```\s*$', '', content)
        content = content.strip()
        
        # 如果内容以```开头，移除它
        if content.startswith('```'):
            content = content[3:]
        if content.endswith('```'):
            content = content[:-3]
        
        return content.strip()
    
    cleaned_content = clean_json_response(api_response)
    print("🧹 清理后的内容:")
    print(cleaned_content)
    print("\n" + "="*60)
    
    # 尝试解析JSON
    try:
        choreography = json.loads(cleaned_content)
        print("✅ JSON解析成功！")
        print("📋 解析结果:")
        print(f"  描述: {choreography['description']}")
        print(f"  参考动作: {choreography['reference_moves']}")
        print(f"  难度: {choreography['difficulty']}/5")
        print(f"  能量: {choreography['energy_level']}/5")
        print(f"  学习建议: {choreography['learning_tips']}")
        return True
    except json.JSONDecodeError as e:
        print(f"❌ JSON解析失败: {e}")
        return False

def test_video_search_suggestions():
    """测试视频搜索建议功能"""
    print("\n🔍 测试视频搜索建议...")
    
    from dance_references import get_video_search_suggestions
    
    test_cases = [
        ("Hip-Hop", "Harlem Shake"),
        ("Hip-Hop", "Running Man"),
        ("Jazz", "Pirouette"),
        ("K-pop", "Point Dance"),
        ("Unknown Style", "Unknown Move")
    ]
    
    for dance_style, move_name in test_cases:
        suggestion = get_video_search_suggestions(dance_style, move_name)
        print(f"  {dance_style} - {move_name}: {suggestion}")

if __name__ == "__main__":
    success = test_json_cleaning()
    test_video_search_suggestions()
    
    if success:
        print("\n🎉 所有测试通过！JSON解析问题已修复。")
    else:
        print("\n⚠️ 测试失败，需要进一步调试。")
