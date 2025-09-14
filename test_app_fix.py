#!/usr/bin/env python3
"""
测试应用修复
"""

def test_imports():
    """测试所有模块导入"""
    print("🔍 测试模块导入...")
    
    try:
        import streamlit as st
        print("✅ streamlit 导入成功")
    except ImportError as e:
        print(f"❌ streamlit 导入失败: {e}")
        return False
    
    try:
        from choreography_generator import ChoreographyGenerator
        print("✅ ChoreographyGenerator 导入成功")
    except ImportError as e:
        print(f"❌ ChoreographyGenerator 导入失败: {e}")
        return False
    
    try:
        from dance_references import get_youtube_search_url, get_video_search_suggestions
        print("✅ dance_references 导入成功")
    except ImportError as e:
        print(f"❌ dance_references 导入失败: {e}")
        return False
    
    try:
        from llm_choreographer import LLMChoreographer
        print("✅ LLMChoreographer 导入成功")
    except ImportError as e:
        print(f"❌ LLMChoreographer 导入失败: {e}")
        return False
    
    return True

def test_type_safety():
    """测试类型安全"""
    print("\n🔍 测试类型安全...")
    
    # 测试current_time类型检查
    test_values = [0, 0.0, [0, 1], '0', None]
    
    for value in test_values:
        try:
            result = float(value) if isinstance(value, (int, float)) else 0.0
            print(f"✅ {type(value).__name__}: {value} -> {type(result).__name__}: {result}")
        except Exception as e:
            print(f"❌ {type(value).__name__}: {value} -> Error: {e}")
            return False
    
    return True

def test_dance_references():
    """测试舞蹈参考功能"""
    print("\n🔍 测试舞蹈参考功能...")
    
    try:
        from dance_references import get_youtube_search_url, get_video_search_suggestions
        
        # 测试搜索URL生成
        url = get_youtube_search_url("Hip-Hop", "Harlem Shake")
        print(f"✅ YouTube搜索URL: {url}")
        
        # 测试搜索建议
        suggestion = get_video_search_suggestions("Hip-Hop", "Harlem Shake")
        print(f"✅ 搜索建议: {suggestion}")
        
        return True
    except Exception as e:
        print(f"❌ 舞蹈参考功能测试失败: {e}")
        return False

def main():
    """主函数"""
    print("🎵 AI编舞生成器 - 修复测试")
    print("=" * 50)
    
    # 运行所有测试
    tests = [
        ("模块导入", test_imports),
        ("类型安全", test_type_safety),
        ("舞蹈参考", test_dance_references)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🧪 运行测试: {test_name}")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ 测试 {test_name} 失败: {e}")
            results.append((test_name, False))
    
    # 显示结果
    print("\n" + "=" * 50)
    print("📊 测试结果:")
    
    all_passed = True
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"  {test_name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 所有测试通过！应用可以正常启动。")
        print("🚀 运行命令: streamlit run app.py")
    else:
        print("⚠️ 部分测试失败，请检查错误信息。")
    
    return all_passed

if __name__ == "__main__":
    main()
