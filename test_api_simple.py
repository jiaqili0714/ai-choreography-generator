#!/usr/bin/env python3
"""
简单的API测试脚本
"""

import os
import openai

def test_simple_api():
    """测试简单的API调用"""
    print("🔍 测试OpenAI API调用...")
    
    # 检查API密钥
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ 请设置OPENAI_API_KEY环境变量")
        print("💡 在Streamlit界面中设置API密钥，或运行:")
        print("   export OPENAI_API_KEY='your_api_key_here'")
        return False
    
    print(f"✅ API密钥已设置: {api_key[:10]}...")
    
    # 测试简单的API调用
    try:
        print("🧪 测试API调用...")
        openai.api_key = api_key
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "请回答：你好，这是一个测试"}],
            max_tokens=20
        )
        
        result = response.choices[0].message.content.strip()
        print(f"✅ API调用成功！")
        print(f"📝 响应: {result}")
        return True
        
    except Exception as e:
        print(f"❌ API调用失败: {e}")
        print("💡 可能的原因:")
        print("   1. API密钥无效")
        print("   2. 网络连接问题")
        print("   3. OpenAI服务暂时不可用")
        print("   4. API配额不足")
        return False

if __name__ == "__main__":
    success = test_simple_api()
    if success:
        print("\n🎉 API测试通过！现在可以正常使用编舞生成功能了。")
    else:
        print("\n⚠️ API测试失败，请检查API密钥和网络连接。")
