"""
多语言配置文件
"""
import streamlit as st

# 语言配置
LANGUAGES = {
    'zh': '中文',
    'en': 'English'
}

# 中文文本
TEXTS_ZH = {
    'title': '🎵 AI编舞生成器',
    'subtitle': '让AI为你的音乐创作专属舞蹈！',
    'description': '''
这个工具可以：
- 🎶 分析音频文件的BPM和节拍
- 🕺 推荐最适合的舞蹈风格
- 💃 生成8拍片段的详细动作
- 📝 输出完整的编舞草稿
- 🎬 提供经典舞蹈动作的参考视频
- 🎵 集成音乐播放器，实时显示舞蹈建议

支持格式：MP3, WAV
''',
    'config_title': '⚙️ 配置',
    'api_settings': 'API设置',
    'api_key_input': 'OpenAI API Key',
    'api_key_help': '请输入你的OpenAI API密钥',
    'api_key_success': '✅ API密钥已设置',
    'api_key_warning': '⚠️ 请设置OpenAI API密钥',
    'api_key_guide_title': '🔑 如何获取API密钥',
    'api_key_guide': '''
1. 访问: https://platform.openai.com/api-keys
2. 点击 "Create new secret key"
3. 复制生成的密钥（以sk-开头）
4. 粘贴到上方输入框中

**注意**: 你的API密钥只会在当前会话中使用，不会被保存。
''',
    'upload_tab': '🎵 音频文件上传',
    'player_tab': '🎬 音乐播放器',
    'upload_title': '上传音频文件',
    'upload_help': '支持MP3和WAV格式的音频文件',
    'generate_button': '🎭 生成编舞',
    'no_api_key_error': '❌ 请先在侧边栏设置OpenAI API密钥',
    'analyzing': '🎵 正在分析音频...',
    'generating': '🎭 正在生成编舞...',
    'complete': '✅ 编舞生成完成！',
    'error': '❌ 生成编舞时出错',
    'choreography_title': '编舞结果',
    'overall_style': '整体风格推荐',
    'segments': '分段建议',
    'segment': '片段',
    'time_range': '时间范围',
    'rhythm_analysis': '节奏分析',
    'dance_elements': '舞蹈元素',
    'key_tips': '关键提示',
    'difficulty': '难度',
    'energy_level': '能量等级',
    'reference_moves': '参考动作',
    'youtube_search': 'YouTube搜索',
    'search_suggestions': '搜索建议',
    'music_player': '音乐播放器',
    'current_time': '当前时间',
    'dance_suggestions': '舞蹈建议',
    'no_suggestions': '暂无建议',
    'download_audio': '下载音频文件',
    'language_selector': '语言选择'
}

# 英文文本
TEXTS_EN = {
    'title': '🎵 AI Choreography Generator',
    'subtitle': 'Let AI create exclusive dance for your music!',
    'description': '''
This tool can:
- 🎶 Analyze BPM and beats of audio files
- 🕺 Recommend the most suitable dance styles
- 💃 Generate detailed movements for 8-beat segments
- 📝 Output complete choreography drafts
- 🎬 Provide reference videos for classic dance moves
- 🎵 Integrated music player with real-time dance suggestions

Supported formats: MP3, WAV
''',
    'config_title': '⚙️ Configuration',
    'api_settings': 'API Settings',
    'api_key_input': 'OpenAI API Key',
    'api_key_help': 'Please enter your OpenAI API key',
    'api_key_success': '✅ API key has been set',
    'api_key_warning': '⚠️ Please set your OpenAI API key',
    'api_key_guide_title': '🔑 How to get API key',
    'api_key_guide': '''
1. Visit: https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the generated key (starts with sk-)
4. Paste it in the input box above

**Note**: Your API key will only be used in the current session and will not be saved.
''',
    'upload_tab': '🎵 Audio Upload',
    'player_tab': '🎬 Music Player',
    'upload_title': 'Upload Audio File',
    'upload_help': 'Supports MP3 and WAV format audio files',
    'generate_button': '🎭 Generate Choreography',
    'no_api_key_error': '❌ Please set your OpenAI API key in the sidebar first',
    'analyzing': '🎵 Analyzing audio...',
    'generating': '🎭 Generating choreography...',
    'complete': '✅ Choreography generation complete!',
    'error': '❌ Error generating choreography',
    'choreography_title': 'Choreography Results',
    'overall_style': 'Overall Style Recommendation',
    'segments': 'Segment Suggestions',
    'segment': 'Segment',
    'time_range': 'Time Range',
    'rhythm_analysis': 'Rhythm Analysis',
    'dance_elements': 'Dance Elements',
    'key_tips': 'Key Tips',
    'difficulty': 'Difficulty',
    'energy_level': 'Energy Level',
    'reference_moves': 'Reference Moves',
    'youtube_search': 'YouTube Search',
    'search_suggestions': 'Search Suggestions',
    'music_player': 'Music Player',
    'current_time': 'Current Time',
    'dance_suggestions': 'Dance Suggestions',
    'no_suggestions': 'No suggestions available',
    'download_audio': 'Download Audio File',
    'language_selector': 'Language'
}

def get_text(key, language='zh'):
    """获取指定语言的文本"""
    if language == 'en':
        return TEXTS_EN.get(key, key)
    else:
        return TEXTS_ZH.get(key, key)

def init_language():
    """初始化语言设置"""
    if 'language' not in st.session_state:
        st.session_state.language = 'zh'
    
    return st.session_state.language

def language_selector():
    """语言选择器"""
    current_lang = init_language()
    
    # 在侧边栏添加语言选择器
    with st.sidebar:
        st.markdown("### 🌐 Language / 语言")
        selected_lang = st.selectbox(
            "Select Language / 选择语言",
            options=list(LANGUAGES.keys()),
            format_func=lambda x: LANGUAGES[x],
            index=list(LANGUAGES.keys()).index(current_lang)
        )
        
        if selected_lang != current_lang:
            st.session_state.language = selected_lang
            st.rerun()
    
    return st.session_state.language
