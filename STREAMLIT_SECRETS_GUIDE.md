# 🔐 Streamlit Cloud Secrets 设置完整指南

## 🚨 问题解决

你的错误 "请设置OPENAI_API_KEY环境变量" 是因为在Streamlit Cloud中需要正确设置Secrets。

## 📋 详细步骤

### 步骤1: 访问Streamlit Cloud管理页面
1. 打开浏览器，访问: https://share.streamlit.io
2. 使用GitHub账户登录
3. 找到你的应用: `ai-choreography-generator`
4. 点击应用名称进入管理页面

### 步骤2: 设置Secrets
1. 在应用管理页面，点击右上角的 **"⚙️ Settings"** 按钮
2. 在左侧菜单中找到 **"Secrets"** 选项
3. 点击 **"Edit secrets"** 按钮
4. 在文本框中输入以下内容:

```
OPENAI_API_KEY = "sk-your-actual-openai-api-key-here"
```

**重要说明:**
- 将 `sk-your-actual-openai-api-key-here` 替换为你的真实OpenAI API密钥
- API密钥以 `sk-` 开头
- 不要包含引号外的任何内容

### 步骤3: 保存并等待部署
1. 点击 **"Save"** 按钮
2. 等待2-3分钟让应用自动重新部署
3. 你会看到部署进度条

### 步骤4: 验证修复
1. 部署完成后，访问你的应用URL
2. 你应该看到侧边栏显示: "✅ API密钥已从配置中加载"
3. 尝试上传音频文件并生成编舞

## 🔑 如何获取OpenAI API密钥

### 方法1: 创建新的API密钥
1. 访问: https://platform.openai.com/api-keys
2. 点击 **"Create new secret key"**
3. 给密钥起个名字，比如 "AI Choreography Generator"
4. 选择权限范围（建议选择 "All"）
5. 点击 **"Create secret key"**
6. **立即复制密钥**（只显示一次）

### 方法2: 使用现有密钥
1. 访问: https://platform.openai.com/api-keys
2. 找到现有的密钥
3. 点击 **"Copy"** 按钮复制密钥

## ⚠️ 重要注意事项

### API密钥格式
- ✅ 正确格式: `sk-proj-abc123def456...`
- ❌ 错误格式: `sk-abc123` (太短)
- ❌ 错误格式: 包含空格或特殊字符

### 安全提醒
- 🔒 不要在代码中硬编码API密钥
- 🔒 不要在公开的GitHub仓库中暴露API密钥
- 🔒 定期轮换API密钥
- 🔒 监控API使用情况

### 额度检查
- 💰 确保OpenAI账户有足够余额
- 💰 检查API使用限制
- �� 考虑设置使用限制

## 🎯 预期结果

设置完成后，你应该看到:

### 侧边栏显示
```
✅ API密钥已从配置中加载
```

### 功能测试
1. 上传音频文件 ✅
2. 点击"生成编舞" ✅
3. 看到编舞结果 ✅
4. 音乐播放器正常工作 ✅

## 🆘 故障排除

### 问题1: 设置后还是报错
**解决方案:**
- 等待5分钟让应用完全重新部署
- 检查API密钥格式是否正确
- 确认API密钥有效且有额度

### 问题2: 找不到Secrets选项
**解决方案:**
- 确保你是应用的所有者
- 尝试刷新页面
- 检查是否在正确的应用管理页面

### 问题3: API密钥无效
**解决方案:**
- 重新生成API密钥
- 检查OpenAI账户状态
- 确认API密钥权限设置

### 问题4: 部署失败
**解决方案:**
- 检查Secrets格式是否正确
- 查看部署日志
- 尝试重新部署

## 📞 获取帮助

如果问题仍然存在，请提供以下信息:
1. Streamlit Cloud应用URL
2. 具体的错误信息截图
3. 是否已正确设置Secrets
4. API密钥是否有效

## 🎉 完成！

设置完成后，你的AI编舞生成器就可以正常工作了！

**应用URL**: `https://ai-choreography-generator.streamlit.app/`

让AI为全世界的音乐创作专属舞蹈！🎵💃
