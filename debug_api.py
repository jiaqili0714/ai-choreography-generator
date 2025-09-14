#!/usr/bin/env python3
"""
调试API调用问题
"""

import os
import openai
from llm_choreographer import LLMChoreographer

def test_api_call():
    """测试API调用"""
    print("🔍 开始调试API调用...")
    
    # 检查API密钥
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ 未设置OPENAI_API_KEY环境变量")
        return
    
    print(f"✅ API密钥已设置: {api_key[:10]}...")
    
    # 测试直接API调用
    print("\n🧪 测试直接API调用...")
    try:
        # 尝试新版本API
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "请回答：你好"}],
            max_tokens=10
        )
        print("✅ 新版本API调用成功")
        print(f"响应: {response.choices[0].message.content}")
    except Exception as e:
        print(f"❌ 新版本API调用失败: {e}")
        
        # 尝试旧版本API
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "请回答：你好"}],
                max_tokens=10
            )
            print("✅ 旧版本API调用成功")
            print(f"响应: {response.choices[0].message.content}")
        except Exception as e2:
            print(f"❌ 旧版本API调用也失败: {e2}")
    
    # 测试LLMChoreographer
    print("\n🎭 测试LLMChoreographer...")
    try:
        choreographer = LLMChoreographer()
        
        # 测试舞蹈风格推荐
        print("测试舞蹈风格推荐...")
        style = choreographer.generate_choreography_style(120.0, {
            'spectral_centroid_mean': 2000.0,
            'energy_mean': 0.5
        })
        print(f"推荐风格: {style}")
        
        # 测试片段编舞生成
        print("测试片段编舞生成...")
        test_segment = {
            'start_time': 0.0,
            'end_time': 4.0,
            'duration': 4.0,
            'beat_count': 8,
            'beats': [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
        }
        
        choreography = choreographer.generate_segment_choreography(
            test_segment, 120.0, "Hip-Hop", 0
        )
        print(f"生成的编舞: {choreography}")
        
    except Exception as e:
        print(f"❌ LLMChoreographer测试失败: {e}")

if __name__ == "__main__":
    test_api_call()
