#!/usr/bin/env python3
"""
快速API检查脚本 - 兼容OpenAI 1.3.0
"""

import os
import openai

def quick_check():
    """快速检查API状态"""
    print("🔍 快速API检查 (OpenAI 1.3.0)...")
    
    # 1. 检查API密钥
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ 未设置OPENAI_API_KEY")
        print("💡 解决方案:")
        print("   1. 在Streamlit界面设置API密钥")
        print("   2. 或运行: export OPENAI_API_KEY='your_key'")
        return False
    
    print(f"✅ API密钥已设置: {api_key[:10]}...")
    
    # 2. 测试API调用 - 使用新版本API
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "测试"}],
            max_tokens=5
        )
        
        result = response.choices[0].message.content.strip()
        print(f"✅ API调用成功: {result}")
        return True
        
    except openai.AuthenticationError:
        print("❌ API密钥无效或已过期")
        print("💡 解决方案: 检查API密钥是否正确")
        return False
    except openai.RateLimitError:
        print("❌ API调用频率超限")
        print("💡 解决方案: 稍后再试或检查配额")
        return False
    except Exception as e:
        print(f"❌ API调用失败: {e}")
        print("💡 解决方案: 检查网络连接")
        return False

if __name__ == "__main__":
    success = quick_check()
    if success:
        print("\n🎉 API正常，可以开始使用编舞生成功能！")
    else:
        print("\n⚠️ API有问题，请先解决上述问题。")
