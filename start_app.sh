#!/bin/bash

# AI编舞生成器 - 启动脚本
# 修复Streamlit权限问题并启动应用

echo "🎭 AI编舞生成器 - 启动脚本"
echo "=========================="

# 检查是否在正确的目录
if [ ! -f "app.py" ]; then
    echo "❌ 请在项目根目录运行此脚本"
    exit 1
fi

# 创建.streamlit目录
echo "📁 创建.streamlit目录..."
mkdir -p .streamlit

# 设置环境变量
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
export STREAMLIT_GLOBAL_DEVELOPMENT_MODE=false

echo "✅ 环境变量已设置"

# 检查Python环境
echo "🐍 检查Python环境..."
python --version

# 检查Streamlit
echo "📦 检查Streamlit..."
python -c "import streamlit; print(f'Streamlit版本: {streamlit.__version__}')"

# 启动应用
echo "🚀 启动Streamlit应用..."
echo "🌐 访问地址: http://localhost:8501"
echo "⏹️  按 Ctrl+C 停止应用"
echo ""

# 运行Streamlit
python -m streamlit run app.py --server.port=8501 --server.headless=true
