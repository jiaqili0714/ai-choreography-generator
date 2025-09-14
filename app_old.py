import streamlit as st
import os
import json
import tempfile
from choreography_generator import ChoreographyGenerator
import config
from dance_references import get_video_search_suggestions

# 页面配置
st.set_page_config(
    page_title="AI编舞生成器 - 舞蹈参考版",
    page_icon="💃",
    layout="wide"
)

# 标题和介绍
st.title("🎵 AI编舞生成器 - 舞蹈参考版")
st.markdown("""
### 让AI为你的音乐创作专属舞蹈！

这个工具可以：
- 🎶 分析音频文件的BPM和节拍
- 🕺 推荐最适合的舞蹈风格
- 💃 生成8拍片段的详细动作
- 📝 输出完整的编舞草稿
- 🎬 提供经典舞蹈动作的参考视频

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

# 主界面
tab1, tab2 = st.tabs(["🎵 音频文件上传", "🔍 歌曲搜索"])

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
                    
                    # 分段动作详情
                    st.subheader("🎭 分段动作详情")
                    
                    for i, segment_choreo in enumerate(result['choreography']['segments']):
                        segment_info = result['segments'][i]
                        
                        with st.expander(f"第{i+1}段 ({segment_info['start_time']:.1f}s - {segment_info['end_time']:.1f}s)"):
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                st.write("**动作描述:**")
                                st.write(segment_choreo['description'])
                                
                                # 显示参考动作
                                if 'reference_moves' in segment_choreo:
                                    st.write("**参考动作:**")
                                    for move in segment_choreo['reference_moves']:
                                        st.write(f"• {move}")
                                
                                # 显示学习建议
                                if 'learning_tips' in segment_choreo:
                                    st.write("**学习建议:**")
                                    st.write(segment_choreo['learning_tips'])
                            
                            with col2:
                                st.write("**难度等级:**")
                                st.progress(segment_choreo['difficulty'] / 5)
                                st.write("**能量等级:**")
                                st.progress(segment_choreo['energy_level'] / 5)
                                
                                # 显示关键动作
                                if 'key_moves' in segment_choreo:
                                    st.write("**关键动作:**")
                                    for move in segment_choreo['key_moves']:
                                        st.write(f"• {move}")
                            
                            # 显示参考视频和搜索建议
                            if 'reference_moves' in segment_choreo and segment_choreo['reference_moves']:
                                st.write("**🎬 参考视频搜索建议:**")
                                dance_style = result['choreography']['dance_style']
                                for move in segment_choreo['reference_moves']:
                                    search_suggestion = get_video_search_suggestions(dance_style, move)
                                    st.write(f"• **{move}**: {search_suggestion}")
                                
                                # 显示原始视频链接（如果有）
                                if 'video_references' in segment_choreo and segment_choreo['video_references']:
                                    st.write("**原始视频链接:**")
                                    for video_url in segment_choreo['video_references']:
                                        if video_url:
                                            st.write(f"• {video_url}")
                    
                    # 下载按钮
                    st.subheader("💾 下载编舞文件")
                    json_str = json.dumps(result, ensure_ascii=False, indent=2)
                    st.download_button(
                        label="📥 下载编舞JSON文件",
                        data=json_str,
                        file_name=f"choreography_{uploaded_file.name.split('.')[0]}.json",
                        mime="application/json"
                    )
                    
                except Exception as e:
                    st.error(f"❌ 生成编舞时出错: {str(e)}")
                    if 'tmp_file_path' in locals() and os.path.exists(tmp_file_path):
                        os.unlink(tmp_file_path)

with tab2:
    st.header("搜索歌曲")
    st.info("🔮 此功能正在开发中，未来将支持Spotify和YouTube API集成")
    
    song_name = st.text_input("输入歌曲名称", placeholder="例如: Shape of You - Ed Sheeran")
    
    if st.button("🔍 搜索并生成编舞"):
        if not song_name:
            st.warning("⚠️ 请输入歌曲名称")
        elif not api_key:
            st.error("❌ 请先在侧边栏设置OpenAI API密钥")
        else:
            try:
                # 确保API密钥已设置到环境变量
                os.environ['OPENAI_API_KEY'] = api_key
                
                generator = ChoreographyGenerator()
                result = generator.generate_choreography_from_song_name(song_name)
                
                st.success("🎉 示例编舞生成成功！")
                
                # 显示示例结果
                st.subheader("📝 编舞总结")
                st.write(result['choreography']['summary'])
                
                st.subheader("🎭 示例动作")
                segment = result['choreography']['segments'][0]
                st.write(f"**动作描述:** {segment['description']}")
                if 'reference_moves' in segment:
                    st.write(f"**参考动作:** {', '.join(segment['reference_moves'])}")
                if 'key_moves' in segment:
                    st.write(f"**关键动作:** {', '.join(segment['key_moves'])}")
                
            except Exception as e:
                st.error(f"❌ 生成编舞时出错: {str(e)}")

# 页脚
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🎵 AI编舞生成器 - 舞蹈参考版 | 让音乐与舞蹈完美结合</p>
    <p>💡 提示：使用搜索建议在YouTube上找到真实的舞蹈教学视频</p>
</div>
""", unsafe_allow_html=True)
