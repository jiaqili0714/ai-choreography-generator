#!/bin/bash

# AI编舞生成器 - Hugging Face Spaces 快速部署脚本

echo "🚀 AI编舞生成器 - Hugging Face Spaces 部署"
echo "=============================================="

# 检查必要文件
echo "📁 检查部署文件..."
required_files=(
    "app.py"
    "streamlit_cloud_choreography_generator.py"
    "streamlit_cloud_audio_analyzer.py"
    "enhanced_llm_choreographer.py"
    "action_database.py"
    "language_config.py"
    "dance_references.py"
    "config.py"
)

missing_files=()
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -ne 0 ]; then
    echo "❌ 缺少文件: ${missing_files[*]}"
    exit 1
fi

echo "✅ 所有必要文件已准备就绪"

# 准备requirements.txt
echo "📦 准备依赖文件..."
if [ -f "requirements_huggingface.txt" ]; then
    cp requirements_huggingface.txt requirements.txt
    echo "✅ 使用Hugging Face优化的requirements.txt"
else
    echo "⚠️ 使用默认requirements.txt"
fi

# 准备README.md
echo "📝 准备说明文档..."
if [ -f "README_huggingface.md" ]; then
    cp README_huggingface.md README.md
    echo "✅ 使用Hugging Face优化的README.md"
else
    echo "⚠️ 使用默认README.md"
fi

echo ""
echo "🎉 文件准备完成！"
echo ""
echo "📋 下一步操作："
echo "1. 访问: https://huggingface.co/new-space"
echo "2. 创建新的Streamlit Space"
echo "3. 上传所有文件到Space"
echo "4. 在Settings中添加OPENAI_API_KEY环境变量"
echo "5. 等待应用启动完成"
echo ""
echo "📁 需要上传的文件："
for file in "${required_files[@]}"; do
    echo "   - $file"
done
echo "   - requirements.txt"
echo "   - README.md"
echo ""
echo "🌐 部署完成后，你的应用将在以下地址运行："
echo "   https://huggingface.co/spaces/your-username/ai-choreography-generator"
echo ""
echo "🎭 让AI为全世界的音乐创作专业级舞蹈！🎵💃"
