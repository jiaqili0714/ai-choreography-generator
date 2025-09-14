#!/usr/bin/env python3
"""
修复Streamlit权限问题的脚本
解决PermissionError: [Errno 13] Permission denied: '/.streamlit'错误
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path

def fix_streamlit_permissions():
    """修复Streamlit权限问题"""
    print("🔧 修复Streamlit权限问题...")
    
    # 获取当前工作目录
    current_dir = os.getcwd()
    print(f"📁 当前目录: {current_dir}")
    
    # 创建.streamlit目录
    streamlit_dir = os.path.join(current_dir, '.streamlit')
    if not os.path.exists(streamlit_dir):
        os.makedirs(streamlit_dir, exist_ok=True)
        print(f"✅ 创建.streamlit目录: {streamlit_dir}")
    else:
        print(f"✅ .streamlit目录已存在: {streamlit_dir}")
    
    # 创建config.toml文件
    config_file = os.path.join(streamlit_dir, 'config.toml')
    config_content = """[global]
developmentMode = false

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
"""
    
    with open(config_file, 'w') as f:
        f.write(config_content)
    print(f"✅ 创建config.toml: {config_file}")
    
    # 设置环境变量
    env_vars = {
        'STREAMLIT_SERVER_HEADLESS': 'true',
        'STREAMLIT_SERVER_PORT': '8501',
        'STREAMLIT_BROWSER_GATHER_USAGE_STATS': 'false',
        'STREAMLIT_GLOBAL_DEVELOPMENT_MODE': 'false'
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
        print(f"✅ 设置环境变量: {key}={value}")
    
    # 检查权限
    if os.access(streamlit_dir, os.W_OK):
        print("✅ .streamlit目录权限正常")
    else:
        print("❌ .streamlit目录权限异常")
        return False
    
    print("🎉 Streamlit权限问题修复完成！")
    return True

def run_streamlit_safely():
    """安全运行Streamlit"""
    print("🚀 启动Streamlit应用...")
    
    # 修复权限
    if not fix_streamlit_permissions():
        print("❌ 权限修复失败")
        return False
    
    # 运行Streamlit
    try:
        cmd = [sys.executable, "-m", "streamlit", "run", "app.py", "--server.port=8501"]
        print(f"📝 执行命令: {' '.join(cmd)}")
        
        # 使用subprocess运行
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        print("✅ Streamlit应用已启动")
        print("🌐 访问地址: http://localhost:8501")
        print("⏹️  按 Ctrl+C 停止应用")
        
        # 等待进程结束
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\n⏹️  正在停止应用...")
            process.terminate()
            process.wait()
            print("✅ 应用已停止")
        
        return True
        
    except Exception as e:
        print(f"❌ 启动Streamlit失败: {e}")
        return False

def main():
    """主函数"""
    print("🎭 AI编舞生成器 - Streamlit权限修复工具")
    print("=" * 50)
    
    # 检查是否在正确的目录
    if not os.path.exists("app.py"):
        print("❌ 请在项目根目录运行此脚本")
        return
    
    # 修复权限并启动应用
    success = run_streamlit_safely()
    
    if success:
        print("\n🎉 应用运行成功！")
    else:
        print("\n❌ 应用运行失败，请检查错误信息")

if __name__ == "__main__":
    main()
