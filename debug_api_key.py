#!/usr/bin/env python3
"""
API密钥调试脚本
用于诊断API密钥设置问题
"""

import os
import sys

def debug_api_key():
    print("🔍 API密钥调试信息:")
    print(f"Python版本: {sys.version}")
    print(f"当前工作目录: {os.getcwd()}")
    
    # 检查环境变量
    api_key = os.getenv('OPENAI_API_KEY')
    print(f"OPENAI_API_KEY环境变量: {'已设置' if api_key else '未设置'}")
    if api_key:
        print(f"API密钥长度: {len(api_key)}")
        print(f"API密钥前缀: {api_key[:10]}...")
    
    # 检查config模块
    try:
        import config
        print(f"config.OPENAI_API_KEY: {'已设置' if config.OPENAI_API_KEY else '未设置'}")
        if config.OPENAI_API_KEY:
            print(f"config API密钥长度: {len(config.OPENAI_API_KEY)}")
            print(f"config API密钥前缀: {config.OPENAI_API_KEY[:10]}...")
    except Exception as e:
        print(f"config模块错误: {e}")
    
    # 测试环境变量设置
    print("\n🧪 测试环境变量设置:")
    test_key = "sk-test123456789"
    os.environ['OPENAI_API_KEY'] = test_key
    retrieved_key = os.getenv('OPENAI_API_KEY')
    print(f"设置测试密钥: {test_key}")
    print(f"检索到的密钥: {retrieved_key}")
    print(f"设置成功: {test_key == retrieved_key}")
    
    # 测试OpenAI客户端初始化
    print("\n🤖 测试OpenAI客户端初始化:")
    try:
        import openai
        client = openai.OpenAI(api_key=test_key)
        print("✅ OpenAI客户端初始化成功")
    except Exception as e:
        print(f"❌ OpenAI客户端初始化失败: {e}")

if __name__ == "__main__":
    debug_api_key()
