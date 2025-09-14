#!/usr/bin/env python3
"""
最终测试脚本 - 验证API调用
"""

import os
import openai

def test_api():
    """测试API调用"""
    print("🔍 测试OpenAI API调用...")
    
    # 检查API密钥
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ 未设置OPENAI_API_KEY环境变量")
        print("💡 请在Streamlit界面设置API密钥")
        return False
    
    print(f"✅ API密钥已设置: {api_key[:10]}...")
    
    # 测试API调用
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "请回答：你好"}],
            max_tokens=10
        )
        
        result = response.choices[0].message.content.strip()
        print(f"✅ API调用成功: {result}")
        return True
        
    except Exception as e:
        print(f"❌ API调用失败: {e}")
        return False

if __name__ == "__main__":
    success = test_api()
    if success:
        print("\n🎉 API测试通过！现在可以正常使用编舞生成功能了。")
        print("💡 启动Streamlit: streamlit run app.py")
    else:
        print("\n⚠️ API测试失败，请检查API密钥。")
