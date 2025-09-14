# 🔐 Streamlit Cloud 环境变量设置指南

## 问题描述
部署后出现错误: "请设置OPENAI_API_KEY环境变量"

## 解决方案

### 方法1: 在Streamlit Cloud中设置Secrets

1. **访问你的应用管理页面**
   - 打开: https://share.streamlit.io
   - 找到你的应用: `ai-choreography-generator`
   - 点击应用名称进入管理页面

2. **设置Secrets**
   - 点击 "Settings" 或 "⚙️" 图标
   - 找到 "Secrets" 部分
   - 点击 "Edit secrets"
   - 添加以下内容:
   ```
   OPENAI_API_KEY = "your-actual-openai-api-key-here"
   ```
   - 点击 "Save"

3. **重新部署**
   - 保存后，应用会自动重新部署
   - 等待2-3分钟完成部署

### 方法2: 通过.toml文件设置

如果方法1不工作，可以创建 `.streamlit/secrets.toml` 文件:

1. **创建目录结构**
   ```bash
   mkdir -p .streamlit
   ```

2. **创建secrets.toml文件**
   ```bash
   cat > .streamlit/secrets.toml << 'EOF'
   OPENAI_API_KEY = "your-actual-openai-api-key-here"
   EOF
   ```

3. **提交到GitHub**
   ```bash
   git add .streamlit/secrets.toml
   git commit -m "Add Streamlit secrets configuration"
   git push
   ```

### 方法3: 检查config.py文件

确保 `config.py` 文件正确读取环境变量:

```python
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 获取API密钥
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    print("警告: 未找到OPENAI_API_KEY环境变量")
```

## 验证步骤

1. **检查应用日志**
   - 在Streamlit Cloud管理页面查看 "Logs"
   - 确认没有环境变量相关错误

2. **测试API调用**
   - 上传一个音频文件
   - 尝试生成编舞
   - 如果成功，说明环境变量设置正确

## 常见问题

### Q: 为什么设置后还是报错？
A: 可能需要等待几分钟让应用重新部署，或者检查API密钥是否正确。

### Q: 如何获取OpenAI API密钥？
A: 访问 https://platform.openai.com/api-keys 创建新的API密钥。

### Q: 环境变量设置后多久生效？
A: 通常2-5分钟内生效，应用会自动重新部署。

## 最终检查清单

- [ ] 在Streamlit Cloud中设置了OPENAI_API_KEY
- [ ] API密钥格式正确（以sk-开头）
- [ ] 应用已重新部署
- [ ] 测试上传音频文件功能
- [ ] 确认编舞生成功能正常

## 如果问题仍然存在

1. 检查API密钥是否有效
2. 确认API密钥有足够的额度
3. 查看Streamlit Cloud的详细日志
4. 尝试重新部署应用
