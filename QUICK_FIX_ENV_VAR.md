# 🚨 快速修复: Streamlit Cloud 环境变量问题

## 立即解决步骤

### 步骤1: 访问Streamlit Cloud管理页面
1. 打开: https://share.streamlit.io
2. 登录你的GitHub账户
3. 找到你的应用: `ai-choreography-generator`
4. 点击应用名称

### 步骤2: 设置环境变量
1. 在应用页面，点击右上角的 "⚙️ Settings" 按钮
2. 在左侧菜单中找到 "Secrets" 选项
3. 点击 "Edit secrets"
4. 在文本框中输入:
   ```
   OPENAI_API_KEY = "sk-your-actual-api-key-here"
   ```
   **重要**: 将 `sk-your-actual-api-key-here` 替换为你的真实OpenAI API密钥

### 步骤3: 保存并等待
1. 点击 "Save" 按钮
2. 等待2-3分钟让应用重新部署
3. 刷新应用页面

### 步骤4: 验证修复
1. 尝试上传一个音频文件
2. 点击 "生成编舞" 按钮
3. 如果成功，说明问题已解决

## 🔍 如何获取OpenAI API密钥

1. 访问: https://platform.openai.com/api-keys
2. 点击 "Create new secret key"
3. 给密钥起个名字，比如 "AI Choreography Generator"
4. 复制生成的密钥（以sk-开头）
5. 将密钥粘贴到Streamlit Cloud的Secrets中

## ⚠️ 注意事项

- API密钥以 `sk-` 开头
- 不要在代码中硬编码API密钥
- 确保API密钥有足够的额度
- 保存后应用会自动重新部署

## 🎯 预期结果

设置完成后，你的应用应该能够:
- ✅ 正常加载页面
- ✅ 接受音频文件上传
- ✅ 成功调用OpenAI API
- ✅ 生成编舞建议

## 🆘 如果还是不行

1. **检查API密钥格式**: 确保以 `sk-` 开头
2. **检查API额度**: 确保OpenAI账户有足够余额
3. **查看日志**: 在Streamlit Cloud管理页面查看详细错误日志
4. **重新部署**: 尝试删除并重新创建应用

## 📞 需要帮助？

如果问题仍然存在，请提供:
1. Streamlit Cloud应用URL
2. 具体的错误信息
3. 是否已正确设置环境变量
