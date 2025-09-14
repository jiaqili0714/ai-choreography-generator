#!/bin/bash

# AI编舞生成器启动脚本

echo "🎵 AI编舞生成器"
echo "=================="

# 检查Python环境
if ! command -v python &> /dev/null; then
    echo "❌ 错误: 未找到Python，请先安装Python 3.8+"
    exit 1
fi

# 检查依赖包
echo "🔍 检查依赖包..."
python -c "import librosa, streamlit, openai" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 安装依赖包..."
    pip install -r requirements.txt
fi

# 显示菜单
echo ""
echo "请选择运行模式:"
echo "1) 🌐 启动Web界面 (推荐)"
echo "2) 🎭 运行功能演示"
echo "3) 🧪 运行系统测试"
echo "4) 💻 命令行模式帮助"
echo "5) ❌ 退出"

read -p "请输入选择 (1-5): " choice

case $choice in
    1)
        echo "🚀 启动Web界面..."
        echo "📱 浏览器将自动打开 http://localhost:8501"
        echo "💡 提示: 请在侧边栏设置OpenAI API密钥"
        streamlit run app.py
        ;;
    2)
        echo "🎭 运行功能演示..."
        python demo.py
        ;;
    3)
        echo "🧪 运行系统测试..."
        python test_system.py
        ;;
    4)
        echo "💻 命令行模式使用方法:"
        echo "   python main.py <音频文件路径>"
        echo "   python main.py <音频文件路径> -o <输出文件>"
        echo "   python main.py <音频文件路径> --api-key <API密钥>"
        echo ""
        echo "📁 支持的音频格式: MP3, WAV"
        echo "🔑 需要设置OPENAI_API_KEY环境变量或使用--api-key参数"
        ;;
    5)
        echo "👋 再见！"
        exit 0
        ;;
    *)
        echo "❌ 无效选择，请重新运行脚本"
        exit 1
        ;;
esac
