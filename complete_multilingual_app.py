import streamlit as st
import os
import json
import tempfile
import base64
from choreography_generator import ChoreographyGenerator
import config
from dance_references import get_youtube_search_url, get_video_search_suggestions
from language_config import get_text, language_selector, init_language

# 初始化语言设置
language = init_language()

# 页面配置
st.set_page_config(
    page_title=get_text('title', language),
    page_icon="💃",
    layout="wide"
)

# 标题和介绍
st.title(get_text('title', language))
st.markdown(f"""
### {get_text('subtitle', language)}

{get_text('description', language)}
""")

# 侧边栏配置
st.sidebar.header(get_text('config_title', language))

# 语言选择器
language = language_selector()

st.sidebar.markdown(f"### {get_text('api_settings', language)}")

# 用户输入API密钥
api_key = st.sidebar.text_input(get_text('api_key_input', language), type="password", 
                               help=get_text('api_key_help', language))

# 设置环境变量
if api_key:
    os.environ['OPENAI_API_KEY'] = api_key
    st.sidebar.success(get_text('api_key_success', language))
else:
    st.sidebar.warning(get_text('api_key_warning', language))

# 添加API密钥获取帮助
with st.sidebar.expander(get_text('api_key_guide_title', language)):
    st.markdown(get_text('api_key_guide', language))

# 初始化session state
if 'choreography_result' not in st.session_state:
    st.session_state.choreography_result = None
if 'audio_file' not in st.session_state:
    st.session_state.audio_file = None
if 'current_time' not in st.session_state:
    st.session_state.current_time = 0.0

def get_audio_download_link(audio_file):
    """生成音频文件下载链接"""
    audio_bytes = audio_file.getvalue()
    b64 = base64.b64encode(audio_bytes).decode()
    return f"data:audio/wav;base64,{b64}"

def get_current_segment_info(current_time, segments):
    """根据当前时间获取对应的舞蹈片段信息"""
    for i, segment in enumerate(segments):
        if segment['start_time'] <= current_time <= segment['end_time']:
            return i, segment
    return None, None

def format_time(seconds):
    """格式化时间显示"""
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

# 主界面
tab1, tab2 = st.tabs([get_text('upload_tab', language), get_text('player_tab', language)])

with tab1:
    st.header(get_text('upload_title', language))
    
    uploaded_file = st.file_uploader(
        f"{get_text('upload_title', language)} (MP3/WAV)",
        type=['mp3', 'wav'],
        help=get_text('upload_help', language)
    )
    
    if uploaded_file is not None:
        # 显示文件信息
        st.success(f"✅ 文件上传成功: {uploaded_file.name}")
        st.info(f"📊 文件大小: {uploaded_file.size / 1024 / 1024:.2f} MB")
        
        # 生成编舞按钮
        if st.button(get_text('generate_button', language), type="primary"):
            if not api_key:
                st.error(get_text('no_api_key_error', language))
            else:
                try:
                    # 确保API密钥已设置到环境变量
                    os.environ['OPENAI_API_KEY'] = api_key
                    
                    # 创建临时文件
                    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_file_path = tmp_file.name
                    
                    # 显示进度
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    # 初始化生成器
                    generator = ChoreographyGenerator()
                    
                    # 生成编舞
                    status_text.text(get_text('analyzing', language))
                    progress_bar.progress(20)
                    
                    result = generator.generate_choreography_from_file(tmp_file_path)
                    
                    status_text.text(get_text('generating', language))
                    progress_bar.progress(80)
                    
                    # 显示结果
                    progress_bar.progress(100)
                    status_text.text(get_text('complete', language))
                    
                    # 清理临时文件
                    os.unlink(tmp_file_path)
                    
                    # 保存到session state
                    st.session_state.choreography_result = result
                    st.session_state.audio_file = uploaded_file
                    
                    # 显示编舞结果
                    st.success("🎉 编舞生成成功！")
                    
                    # 基本信息
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("BPM", f"{result['audio_info']['bpm']:.1f}")
                    with col2:
                        st.metric("时长", f"{result['audio_info']['duration']:.1f}秒")
                    with col3:
                        st.metric("节拍数", result['audio_info']['total_beats'])
                    with col4:
                        st.metric("片段数", len(result['choreography']['segments']))
                    
                    # 整体风格推荐
                    st.subheader(get_text('overall_style', language))
                    st.write(result['choreography']['summary'])
                    
                    # 跳转到播放器标签页
                    st.info("🎬 编舞生成完成！请切换到'音乐播放器'标签页开始练习。")
                    
                except Exception as e:
                    st.error(f"{get_text('error', language)}: {str(e)}")
                    if 'tmp_file_path' in locals() and os.path.exists(tmp_file_path):
                        os.unlink(tmp_file_path)

with tab2:
    st.header(get_text('music_player', language))
    
    if st.session_state.choreography_result is None:
        st.warning("⚠️ 请先上传音频文件并生成编舞")
    else:
        result = st.session_state.choreography_result
        audio_file = st.session_state.audio_file
        
        # 获取音频数据
        audio_bytes = audio_file.getvalue()
        
        # 音频播放器
        st.audio(audio_bytes, format='audio/wav')
        
        # 时间滑块
        duration = result['audio_info']['duration']
        current_time = st.slider(
            get_text('current_time', language),
            min_value=0.0,
            max_value=duration,
            value=float(st.session_state.current_time) if isinstance(st.session_state.current_time, (int, float)) else 0.0,
            step=0.1,
            format="%.1f"
        )
        
        # 更新session state
        st.session_state.current_time = current_time
        
        # 获取当前时间对应的舞蹈片段
        segment_index, current_segment = get_current_segment_info(current_time, result['choreography']['segments'])
        
        # 显示当前舞蹈建议
        st.subheader(get_text('dance_suggestions', language))
        
        if current_segment:
            # 显示当前片段信息
            st.info(f"🎵 {get_text('segment', language)} {segment_index + 1}: {format_time(current_segment['start_time'])} - {format_time(current_segment['end_time'])}")
            
            # 显示舞蹈建议
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # 节奏分析
                if 'rhythm_analysis' in current_segment:
                    st.info(f"🎵 {get_text('rhythm_analysis', language)}: {current_segment['rhythm_analysis']}")
                
                # 舞蹈元素
                if 'dance_elements' in current_segment:
                    st.success(f"💃 {get_text('dance_elements', language)}:")
                    for element in current_segment['dance_elements']:
                        st.write(f"• {element}")
                
                # 关键提示
                if 'key_tips' in current_segment:
                    st.warning(f"💡 {get_text('key_tips', language)}:")
                    for tip in current_segment['key_tips']:
                        st.write(f"• {tip}")
            
            with col2:
                # 难度和能量等级
                if 'difficulty' in current_segment:
                    st.metric(get_text('difficulty', language), current_segment['difficulty'])
                
                if 'energy_level' in current_segment:
                    st.metric(get_text('energy_level', language), current_segment['energy_level'])
                
                # 参考动作
                if 'reference_moves' in current_segment and current_segment['reference_moves']:
                    st.markdown(f"**{get_text('reference_moves', language)}:**")
                    for move in current_segment['reference_moves']:
                        st.write(f"• {move}")
            
            # YouTube搜索链接
            if 'youtube_search_urls' in current_segment and current_segment['youtube_search_urls']:
                st.markdown(f"**{get_text('youtube_search', language)}:**")
                for i, url in enumerate(current_segment['youtube_search_urls']):
                    if url:
                        st.markdown(f"[搜索 {i+1}]({url})")
            
            # 搜索建议
            if 'search_suggestions' in current_segment and current_segment['search_suggestions']:
                st.markdown(f"**{get_text('search_suggestions', language)}:**")
                for suggestion in current_segment['search_suggestions']:
                    st.write(f"• {suggestion}")
        else:
            st.info(get_text('no_suggestions', language))
        
        # 下载音频文件
        st.markdown("---")
        st.markdown(f"**{get_text('download_audio', language)}:**")
        download_link = get_audio_download_link(audio_file)
        st.markdown(f'<a href="{download_link}" download="{audio_file.name}">📥 下载 {audio_file.name}</a>', unsafe_allow_html=True)
