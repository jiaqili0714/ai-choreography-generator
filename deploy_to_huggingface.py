#!/usr/bin/env python3
"""
Hugging Face Spaces 部署脚本
自动准备和部署AI编舞生成器到Hugging Face Spaces
"""

import os
import shutil
import subprocess
import sys

def create_huggingface_space():
    """创建Hugging Face Space"""
    print("🚀 开始部署到Hugging Face Spaces...")
    
    # 检查是否安装了huggingface_hub
    try:
        import huggingface_hub
        print("✅ huggingface_hub 已安装")
    except ImportError:
        print("📦 安装 huggingface_hub...")
        subprocess.run([sys.executable, "-m", "pip", "install", "huggingface_hub"], check=True)
    
    # 创建Space
    from huggingface_hub import HfApi, create_repo
    
    api = HfApi()
    
    # 获取用户输入
    space_name = input("请输入Space名称 (默认: ai-choreography-generator): ").strip()
    if not space_name:
        space_name = "ai-choreography-generator"
    
    username = input("请输入你的Hugging Face用户名: ").strip()
    if not username:
        print("❌ 用户名不能为空")
        return False
    
    try:
        # 创建Space
        print(f"📝 创建Space: {username}/{space_name}")
        create_repo(
            repo_id=f"{username}/{space_name}",
            repo_type="space",
            space_sdk="streamlit",
            private=False
        )
        print("✅ Space创建成功！")
        
        # 准备文件
        print("📁 准备部署文件...")
        prepare_deployment_files()
        
        # 上传文件
        print("⬆️ 上传文件到Hugging Face...")
        upload_files_to_space(username, space_name)
        
        print("🎉 部署完成！")
        print(f"🌐 访问地址: https://huggingface.co/spaces/{username}/{space_name}")
        
        return True
        
    except Exception as e:
        print(f"❌ 部署失败: {e}")
        return False

def prepare_deployment_files():
    """准备部署文件"""
    # 复制requirements.txt
    if os.path.exists("requirements_huggingface.txt"):
        shutil.copy("requirements_huggingface.txt", "requirements.txt")
        print("✅ 使用Hugging Face优化的requirements.txt")
    
    # 复制README.md
    if os.path.exists("README_huggingface.md"):
        shutil.copy("README_huggingface.md", "README.md")
        print("✅ 使用Hugging Face优化的README.md")
    
    # 确保所有必要文件存在
    required_files = [
        "app.py",
        "requirements.txt",
        "README.md",
        "streamlit_cloud_choreography_generator.py",
        "streamlit_cloud_audio_analyzer.py",
        "enhanced_llm_choreographer.py",
        "action_database.py",
        "language_config.py",
        "dance_references.py",
        "config.py"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"⚠️ 缺少文件: {missing_files}")
        return False
    
    print("✅ 所有必要文件已准备就绪")
    return True

def upload_files_to_space(username, space_name):
    """上传文件到Space"""
    from huggingface_hub import HfApi
    
    api = HfApi()
    
    # 要上传的文件列表
    files_to_upload = [
        "app.py",
        "requirements.txt", 
        "README.md",
        "streamlit_cloud_choreography_generator.py",
        "streamlit_cloud_audio_analyzer.py",
        "enhanced_llm_choreographer.py",
        "action_database.py",
        "language_config.py",
        "dance_references.py",
        "config.py"
    ]
    
    for file in files_to_upload:
        if os.path.exists(file):
            print(f"⬆️ 上传 {file}...")
            api.upload_file(
                path_or_fileobj=file,
                path_in_repo=file,
                repo_id=f"{username}/{space_name}",
                repo_type="space"
            )
            print(f"✅ {file} 上传成功")
        else:
            print(f"⚠️ 文件不存在: {file}")

def main():
    """主函数"""
    print("🎭 AI编舞生成器 - Hugging Face Spaces部署工具")
    print("=" * 50)
    
    # 检查当前目录
    if not os.path.exists("app.py"):
        print("❌ 请在项目根目录运行此脚本")
        return
    
    # 检查Git状态
    try:
        result = subprocess.run(["git", "status", "--porcelain"], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            print("⚠️ 检测到未提交的更改，建议先提交到Git")
            response = input("是否继续部署？(y/N): ").strip().lower()
            if response != 'y':
                print("部署已取消")
                return
    except:
        print("⚠️ 无法检查Git状态，继续部署...")
    
    # 开始部署
    success = create_huggingface_space()
    
    if success:
        print("\n🎉 部署成功！")
        print("\n📋 后续步骤:")
        print("1. 访问你的Space页面")
        print("2. 在Settings中添加环境变量 OPENAI_API_KEY")
        print("3. 等待应用启动完成")
        print("4. 测试功能是否正常")
    else:
        print("\n❌ 部署失败，请检查错误信息")

if __name__ == "__main__":
    main()
