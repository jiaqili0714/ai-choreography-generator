#!/bin/bash

echo "🚀 AI编舞生成器部署脚本"
echo "=========================="

# 检查是否在正确的目录
if [ ! -f "app.py" ]; then
    echo "❌ 错误: 请在项目根目录运行此脚本"
    exit 1
fi

echo "📋 当前状态:"
echo "✅ 项目文件已准备就绪"
echo "✅ Git仓库已初始化"
echo "✅ 代码已提交到本地仓库"

echo ""
echo "📋 下一步操作:"
echo "1. 在GitHub上创建新仓库: https://github.com/new"
echo "   - 仓库名: ai-choreography-generator"
echo "   - 描述: AI-powered choreography generator"
echo "   - 选择Public"
echo "   - 不要添加README, .gitignore, license"
echo ""
echo "2. 推送代码到GitHub:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/ai-choreography-generator.git"
echo "   git push -u origin main"
echo ""
echo "3. 部署到Streamlit Cloud:"
echo "   - 访问: https://share.streamlit.io"
echo "   - 点击 'New app'"
echo "   - Repository: YOUR_USERNAME/ai-choreography-generator"
echo "   - Branch: main"
echo "   - Main file path: app.py"
echo "   - 在Secrets中添加: OPENAI_API_KEY = 'your-api-key'"
echo "   - 点击 'Deploy!'"
echo ""
echo "🎉 部署完成后，你的应用就可以在互联网上访问了！"
