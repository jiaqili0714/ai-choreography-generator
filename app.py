import streamlit as st
import os
import json
import tempfile
import base64
from choreography_generator import ChoreographyGenerator
import config
from dance_references import get_youtube_search_url, get_video_search_suggestions

# 页面配置
st.set_page_config(
    page_title="AI编舞生成器 - 音乐播放器版",
    page_icon="💃",
    layout="wide"
)

# 标题和介绍
st.title("🎵 AI编舞生成器 - 音乐播放器版")
st.markdown("""
### 让AI为你的音乐创作专属舞蹈！

这个工具可以：
- 🎶 分析音频文件的BPM和节拍
- 🕺 推荐最适合的舞蹈风格
- 💃 生成8拍片段的详细动作
- 📝 输出完整的编舞草稿
- 🎬 提供经典舞蹈动作的参考视频
- 🎵 集成音乐播放器，实时显示舞蹈建议

支持格式：MP3, WAV
""")

# 侧边栏配置
st.sidebar.header("⚙️ 配置")
st.sidebar.markdown("### API设置")
api_key = st.sidebar.text_input("OpenAI API Key", type="password", 
                               help="请输入你的OpenAI API密钥")

# 立即设置环境变量
if api_key:
    os.environ['OPENAI_API_KEY'] = api_key
    st.sidebar.success("✅ API密钥已设置")
else:
    st.sidebar.warning("⚠️ 请设置OpenAI API密钥")

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
tab1, tab2 = st.tabs(["🎵 音频文件上传", "🎬 音乐播放器"])

with tab1:
    st.header("上传音频文件")
    
    uploaded_file = st.file_uploader(
        "选择音频文件 (MP3/WAV)",
        type=['mp3', 'wav'],
        help="支持MP3和WAV格式的音频文件"
    )
    
    if uploaded_file is not None:
        # 显示文件信息
        st.success(f"✅ 文件上传成功: {uploaded_file.name}")
        st.info(f"📊 文件大小: {uploaded_file.size / 1024 / 1024:.2f} MB")
        
        # 生成编舞按钮
        if st.button("🎭 生成编舞", type="primary"):
            if not api_key:
                st.error("❌ 请先在侧边栏设置OpenAI API密钥")
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
                    status_text.text("🎵 正在分析音频...")
                    progress_bar.progress(20)
                    
                    result = generator.generate_choreography_from_file(tmp_file_path)
                    
                    status_text.text("🎭 正在生成编舞...")
                    progress_bar.progress(80)
                    
                    # 显示结果
                    progress_bar.progress(100)
                    status_text.text("✅ 编舞生成完成！")
                    
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
                        st.metric("舞蹈风格", result['choreography']['dance_style'])
                    with col4:
                        st.metric("片段数", result['choreography']['total_segments'])
                    
                    # 编舞总结
                    st.subheader("📝 编舞总结")
                    st.write(result['choreography']['summary'])
                    
                    # 跳转到播放器标签页
                    st.info("🎬 编舞生成完成！请切换到'音乐播放器'标签页开始练习。")
                    
                except Exception as e:
                    st.error(f"❌ 生成编舞时出错: {str(e)}")
                    if 'tmp_file_path' in locals() and os.path.exists(tmp_file_path):
                        os.unlink(tmp_file_path)

with tab2:
    st.header("🎬 音乐播放器")
    
    if st.session_state.choreography_result is None:
        st.warning("⚠️ 请先上传音频文件并生成编舞")
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
                st.metric("持续时间", f"{current_segment['duration']:.1f}秒")
            
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
                '持续时间': f"{segment['duration']:.1f}秒",
                '参考动作': ', '.join(segment_choreo.get('reference_moves', ['基础动作'])),
                '难度': f"{segment_choreo['difficulty']}/5",
                '能量': f"{segment_choreo['energy_level']}/5"
            })
        
        # 显示时间轴表格
        import pandas as pd
        df = pd.DataFrame(timeline_data)
        st.dataframe(df, use_container_width=True)
        
        # 下载按钮
        st.subheader("💾 下载编舞文件")
        json_str = json.dumps(result, ensure_ascii=False, indent=2)
        st.download_button(
            label="📥 下载编舞JSON文件",
            data=json_str,
            file_name=f"choreography_{audio_file.name.split('.')[0]}.json",
            mime="application/json"
        )

# 页脚
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🎵 AI编舞生成器 - 音乐播放器版 | 让音乐与舞蹈完美结合</p>
    <p>💡 提示：使用时间滑块查看不同时间点的舞蹈建议，点击搜索链接找到教学视频</p>
</div>
""", unsafe_allow_html=True)
