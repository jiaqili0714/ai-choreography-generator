import streamlit as st
import os
import json
import tempfile
import base64
# 自动选择生成器版本
try:
    # 尝试导入专业版本（需要高级库）
    from enhanced_choreography_generator_pro import EnhancedChoreographyGeneratorPro
    GENERATOR_CLASS = EnhancedChoreographyGeneratorPro
    GENERATION_MODE = "professional_enhanced"
    print("🎭 使用专业版编舞生成器（支持madmom、essentia、musicnn）")
except ImportError as e:
    # 回退到兼容版本
    from streamlit_cloud_choreography_generator import StreamlitCloudChoreographyGenerator
    GENERATOR_CLASS = StreamlitCloudChoreographyGenerator
    GENERATION_MODE = "enhanced_compatible"
    print(f"🔄 使用兼容版编舞生成器（{e}）")
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

# 显示生成模式
st.sidebar.markdown("---")
if GENERATION_MODE == "professional_enhanced":
    st.sidebar.success("🎭 专业模式")
    st.sidebar.info("支持madmom、essentia、musicnn等高级音频分析库")
else:
    st.sidebar.info("🔄 兼容模式")
    st.sidebar.info("使用librosa增强分析，适合云部署")

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
    # 确保seconds是标量
    seconds = float(seconds)
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
        st.success(f"✅ {get_text('file_uploaded', language)}: {uploaded_file.name}")
        st.info(f"📊 {get_text('file_size_mb', language)}: {uploaded_file.size / 1024 / 1024:.2f} MB")
        
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
                    
                    # 初始化生成器（自动选择版本）
                    generator = GENERATOR_CLASS()
                    
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
                    st.success(f"🎉 {get_text('choreography_generated', language)}")
                    
                    # 基本信息
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("BPM", f"{float(result['audio_info']['bpm']):.1f}")
                    with col2:
                        st.metric("时长", f"{float(result['audio_info']['duration']):.1f}秒")
                    with col3:
                        st.metric("舞蹈风格", result['choreography']['dance_style'])
                    with col4:
                        st.metric("片段数", result['choreography']['total_segments'])
                    
                    # 编舞总结
                    st.subheader(f"📝 {get_text('choreography_summary', language)}")
                    st.write(result['choreography']['summary'])
                    
                    # 跳转到播放器标签页
                    st.info(f"🎬 {get_text('switch_to_player_tab', language)}")
                    
                except Exception as e:
                    st.error(f"{get_text('error', language)}: {str(e)}")
                    if 'tmp_file_path' in locals() and os.path.exists(tmp_file_path):
                        os.unlink(tmp_file_path)

with tab2:
    st.header(get_text('music_player', language))
    
    if st.session_state.choreography_result is None:
        st.warning(f"⚠️ {get_text('upload_first_warning', language)}")
    else:
        result = st.session_state.choreography_result
        audio_file = st.session_state.audio_file
        
        # 获取音频数据
        audio_bytes = audio_file.getvalue()
        b64 = base64.b64encode(audio_bytes).decode()
        
        # 音乐播放器
        st.subheader("🎵 音乐播放器")
        
        # 创建播放器HTML
        audio_html = f"""
        <audio controls style="width: 100%;">
            <source src="data:audio/wav;base64,{b64}" type="audio/wav">
            您的浏览器不支持音频播放。
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
        
        # 当前时间输入
        st.subheader("⏰ 当前播放时间")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            current_time = st.slider(
                "选择时间 (秒)",
                min_value=0.0,
                max_value=float(result['audio_info']['duration']),
                value=float(st.session_state.current_time) if isinstance(st.session_state.current_time, (int, float)) else 0.0,
                step=0.1,
                format="%.1f"
            )
            st.session_state.current_time = current_time
        
        with col2:
            st.metric("当前时间", format_time(current_time))
        
        # 获取当前片段的舞蹈信息
        segment_index, current_segment = get_current_segment_info(current_time, result['segments'])
        
        if segment_index is not None:
            # 显示当前片段的舞蹈建议
            st.subheader(f"💃 当前片段舞蹈建议 (第{segment_index + 1}段)")
            
            segment_choreo = result['choreography']['segments'][segment_index]
            
            # 片段时间信息
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("开始时间", format_time(current_segment['start_time']))
            with col2:
                st.metric("结束时间", format_time(current_segment['end_time']))
            with col3:
                st.metric("持续时间", f"{float(current_segment['duration']):.1f}秒")
            
            # 简洁的舞蹈建议显示
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # 节奏分析
                if 'rhythm_analysis' in segment_choreo:
                    st.write("**🎵 节奏要点:**")
                    st.info(segment_choreo['rhythm_analysis'])
                
                # 舞蹈元素
                if 'dance_elements' in segment_choreo:
                    st.write("**💃 舞蹈元素:**")
                    for element in segment_choreo['dance_elements']:
                        st.write(f"• {element}")
                
                # 关键提示
                if 'key_tips' in segment_choreo:
                    st.write("**💡 关键提示:**")
                    st.success(segment_choreo['key_tips'])
            
            with col2:
                # 难度和能量等级
                st.write("**📊 难度等级:**")
                st.progress(segment_choreo['difficulty'] / 5)
                st.write("**⚡ 能量等级:**")
                st.progress(segment_choreo['energy_level'] / 5)
                
                # 参考动作
                if 'reference_moves' in segment_choreo:
                    st.write("**🎬 参考动作:**")
                    for move in segment_choreo['reference_moves']:
                        st.write(f"• {move}")
            
            # 兼容旧格式的显示
            if 'description' in segment_choreo:
                with st.expander("📝 详细描述", expanded=False):
                    st.write(segment_choreo['description'])
            
            if 'beat_breakdown' in segment_choreo:
                with st.expander("⏰ 节拍分解", expanded=False):
                    st.write(segment_choreo['beat_breakdown'])
            
            if 'learning_tips' in segment_choreo:
                with st.expander("💡 学习建议", expanded=False):
                    st.write(segment_choreo['learning_tips'])
            
            # 显示参考视频搜索建议
            if 'reference_moves' in segment_choreo and segment_choreo['reference_moves']:
                st.subheader("🎬 参考视频搜索")
                dance_style = result['choreography']['dance_style']
                
                for move in segment_choreo['reference_moves']:
                    with st.expander(f"🔍 搜索 {move} 的教学视频"):
                        # 生成YouTube搜索链接
                        search_url = get_youtube_search_url(dance_style, move)
                        st.markdown(f"**[在YouTube搜索 {move}]({search_url})**")
                        
                        # 提供搜索建议
                        search_suggestion = get_video_search_suggestions(dance_style, move)
                        st.write(f"搜索建议: {search_suggestion}")
                        
                        # 提供搜索关键词
                        from dance_references import get_all_search_terms
                        search_terms = get_all_search_terms(dance_style, move)
                        st.write("**搜索关键词:**")
                        for term in search_terms:
                            st.write(f"• {term}")
        else:
            st.info("🎵 当前时间没有对应的舞蹈片段")
        
        # 显示所有片段的时间轴
        st.subheader("📅 完整时间轴")
        
        # 创建时间轴
        timeline_data = []
        for i, segment in enumerate(result['segments']):
            segment_choreo = result['choreography']['segments'][i]
            timeline_data.append({
                '片段': f"第{i+1}段",
                '开始时间': format_time(segment['start_time']),
                '结束时间': format_time(segment['end_time']),
                '持续时间': f"{float(segment['duration']):.1f}秒",
                '参考动作': ', '.join(segment_choreo.get('reference_moves', ['基础动作'])),
                '难度': f"{segment_choreo['difficulty']}/5",
                '能量': f"{segment_choreo['energy_level']}/5"
            })
        
        # 显示时间轴表格
        import pandas as pd
        df = pd.DataFrame(timeline_data)
        st.dataframe(df, use_container_width=True)
        
        # 下载按钮
        st.subheader(f"💾 {get_text('download_choreography', language)}")
        json_str = json.dumps(result, ensure_ascii=False, indent=2)
        st.download_button(
            label=f"📥 {get_text('download_json', language)}",
            data=json_str,
            file_name=f"choreography_{audio_file.name.split('.')[0]}.json",
            mime="application/json"
        )

# 页脚
st.markdown("---")
st.markdown(f"""
<div style='text-align: center'>
    <p>🎵 {get_text('footer_title', language)}</p>
    <p>💡 {get_text('footer_tip', language)}</p>
</div>
""", unsafe_allow_html=True)
