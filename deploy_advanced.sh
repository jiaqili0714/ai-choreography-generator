#!/bin/bash

# AI Choreography Generator - Advanced Deployment Script
# Supports multiple deployment platforms with full audio analysis libraries

set -e

echo "🎵 AI Choreography Generator - Advanced Deployment"
echo "=================================================="

# Function to deploy to Hugging Face Spaces
deploy_huggingface() {
    echo "🚀 Deploying to Hugging Face Spaces..."
    
    # Check if huggingface_hub is installed
    if ! command -v huggingface-cli &> /dev/null; then
        echo "Installing huggingface_hub..."
        pip install huggingface_hub
    fi
    
    # Login to Hugging Face
    echo "Please login to Hugging Face:"
    huggingface-cli login
    
    # Create or update space
    echo "Creating/updating Hugging Face Space..."
    huggingface-cli repo create ai-choreography-generator --type space --sdk docker
    
    # Copy files
    cp README_HF.md README.md
    cp requirements_full.txt requirements.txt
    cp Dockerfile .
    
    # Push to Hugging Face
    git add .
    git commit -m "Deploy to Hugging Face Spaces with full audio analysis"
    git push origin main
    
    echo "✅ Deployed to Hugging Face Spaces!"
    echo "🌐 URL: https://huggingface.co/spaces/YOUR_USERNAME/ai-choreography-generator"
}

# Function to deploy to Railway
deploy_railway() {
    echo "🚂 Deploying to Railway..."
    
    # Check if Railway CLI is installed
    if ! command -v railway &> /dev/null; then
        echo "Installing Railway CLI..."
        npm install -g @railway/cli
    fi
    
    # Login to Railway
    railway login
    
    # Initialize Railway project
    railway init
    
    # Deploy
    railway up
    
    echo "✅ Deployed to Railway!"
    echo "🌐 Check your Railway dashboard for the URL"
}

# Function to deploy to Render
deploy_render() {
    echo "🎨 Deploying to Render..."
    
    # Create render.yaml
    cat > render.yaml << 'RENDER_EOF'
services:
  - type: web
    name: ai-choreography-generator
    env: docker
    dockerfilePath: ./Dockerfile
    envVars:
      - key: OPENAI_API_KEY
        sync: false
    healthCheckPath: /_stcore/health
RENDER_EOF
    
    echo "✅ Created render.yaml"
    echo "📝 Please connect your GitHub repository to Render manually"
    echo "🌐 Visit: https://render.com"
}

# Function to build and test locally
test_local() {
    echo "🧪 Testing locally with Docker..."
    
    # Build Docker image
    docker build -t ai-choreography-generator .
    
    # Run container
    docker run -p 8501:8501 -e OPENAI_API_KEY=your_key_here ai-choreography-generator
    
    echo "✅ Local test complete!"
    echo "🌐 URL: http://localhost:8501"
}

# Function to show deployment options
show_options() {
    echo "🎯 Available deployment options:"
    echo ""
    echo "1. Hugging Face Spaces (Recommended - Free)"
    echo "   - Free hosting with GPU support"
    echo "   - Automatic HTTPS and custom domain"
    echo "   - Community-friendly platform"
    echo ""
    echo "2. Railway (Modern - $5/month)"
    echo "   - Modern deployment platform"
    echo "   - Automatic deployments from GitHub"
    echo "   - Built-in monitoring and logs"
    echo ""
    echo "3. Render (Simple - $7/month)"
    echo "   - Simple and reliable"
    echo "   - Automatic deployments"
    echo "   - Good for small to medium apps"
    echo ""
    echo "4. Local Docker Test"
    echo "   - Test the full version locally"
    echo "   - No cloud dependencies"
    echo "   - Perfect for development"
    echo ""
    echo "5. AWS/Google Cloud (Enterprise)"
    echo "   - Full control and scalability"
    echo "   - Higher cost but maximum flexibility"
    echo "   - Best for production applications"
}

# Main menu
case "${1:-menu}" in
    "huggingface"|"hf")
        deploy_huggingface
        ;;
    "railway")
        deploy_railway
        ;;
    "render")
        deploy_render
        ;;
    "local"|"test")
        test_local
        ;;
    "menu"|"help"|"")
        show_options
        ;;
    *)
        echo "❌ Unknown option: $1"
        echo "Usage: $0 [huggingface|railway|render|local|menu]"
        exit 1
        ;;
esac

echo ""
echo "🎉 Deployment script complete!"
echo "📚 For more details, see DEPLOYMENT_ALTERNATIVES.md"
