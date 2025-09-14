#!/usr/bin/env python3
"""
音乐播放器版编舞生成器演示
"""

from dance_references import get_youtube_search_url, get_video_search_suggestions, get_all_search_terms

def demo_music_player_features():
    """演示音乐播放器功能"""
    print("🎬 音乐播放器版编舞生成器演示")
    print("=" * 60)
    
    # 模拟编舞结果
    demo_choreography = {
        "audio_info": {
            "duration": 54.49,
            "bpm": 129.2
        },
        "choreography": {
            "dance_style": "Hip-Hop",
            "total_segments": 15
        },
        "segments": [
            {
                "segment_id": 0,
                "start_time": 0.0,
                "end_time": 3.72,
                "duration": 3.72,
                "beat_count": 7
            },
            {
                "segment_id": 1,
                "start_time": 3.72,
                "end_time": 7.43,
                "duration": 3.72,
                "beat_count": 8
            }
        ],
        "choreography": {
            "segments": [
                {
                    "description": "开场：使用Harlem Shake建立节奏感，配合基础步伐",
                    "reference_moves": ["Harlem Shake"],
                    "difficulty": 2,
                    "energy_level": 4,
                    "key_moves": ["Harlem Shake", "基础步伐"],
                    "learning_tips": "先练习头部和肩膀的协调动作，再配合脚步"
                },
                {
                    "description": "第二段：加入Running Man动作，增加动感",
                    "reference_moves": ["Running Man"],
                    "difficulty": 3,
                    "energy_level": 4,
                    "key_moves": ["Running Man", "节奏感"],
                    "learning_tips": "注意脚步的节奏，保持身体的平衡"
                }
            ]
        }
    }
    
    print("🎵 音乐播放器功能演示")
    print("-" * 40)
    
    # 模拟不同时间点的舞蹈建议
    time_points = [0.0, 2.0, 5.0, 10.0]
    
    for current_time in time_points:
        print(f"\n⏰ 当前时间: {current_time:.1f}秒")
        
        # 找到对应的片段
        for i, segment in enumerate(demo_choreography['segments']):
            if segment['start_time'] <= current_time <= segment['end_time']:
                segment_choreo = demo_choreography['choreography']['segments'][i]
                
                print(f"   📍 当前片段: 第{i+1}段 ({segment['start_time']:.1f}s - {segment['end_time']:.1f}s)")
                print(f"   🎭 动作描述: {segment_choreo['description']}")
                print(f"   🎬 参考动作: {', '.join(segment_choreo['reference_moves'])}")
                print(f"   📊 难度: {segment_choreo['difficulty']}/5, 能量: {segment_choreo['energy_level']}/5")
                print(f"   💡 学习建议: {segment_choreo['learning_tips']}")
                
                # 显示视频搜索建议
                for move in segment_choreo['reference_moves']:
                    search_url = get_youtube_search_url("Hip-Hop", move)
                    search_suggestion = get_video_search_suggestions("Hip-Hop", move)
                    print(f"   🔍 {move} 搜索: {search_url}")
                    print(f"      {search_suggestion}")
                break
        else:
            print("   🎵 当前时间没有对应的舞蹈片段")
    
    print("\n" + "=" * 60)
    print("🎬 视频搜索功能演示")
    print("-" * 40)
    
    # 演示视频搜索功能
    dance_moves = [
        ("Hip-Hop", "Harlem Shake"),
        ("Hip-Hop", "Running Man"),
        ("Jazz", "Pirouette"),
        ("K-pop", "Point Dance")
    ]
    
    for dance_style, move_name in dance_moves:
        print(f"\n🎭 {dance_style} - {move_name}:")
        
        # 生成搜索URL
        search_url = get_youtube_search_url(dance_style, move_name)
        print(f"   🔗 YouTube搜索链接: {search_url}")
        
        # 获取搜索建议
        search_suggestion = get_video_search_suggestions(dance_style, move_name)
        print(f"   💡 搜索建议: {search_suggestion}")
        
        # 获取所有搜索词
        search_terms = get_all_search_terms(dance_style, move_name)
        print(f"   📝 搜索关键词: {', '.join(search_terms)}")
    
    print("\n" + "=" * 60)
    print("📅 时间轴功能演示")
    print("-" * 40)
    
    # 显示完整时间轴
    print("完整编舞时间轴:")
    for i, segment in enumerate(demo_choreography['segments']):
        segment_choreo = demo_choreography['choreography']['segments'][i]
        print(f"  第{i+1}段: {segment['start_time']:.1f}s - {segment['end_time']:.1f}s")
        print(f"    动作: {', '.join(segment_choreo['reference_moves'])}")
        print(f"    难度: {segment_choreo['difficulty']}/5, 能量: {segment_choreo['energy_level']}/5")

def main():
    """主函数"""
    demo_music_player_features()
    
    print("\n" + "=" * 60)
    print("🎉 音乐播放器版功能演示完成！")
    print("=" * 60)
    print("✨ 新功能特点:")
    print("   • 🎵 集成音乐播放器")
    print("   • ⏰ 实时时间显示")
    print("   • 🎭 根据播放时间显示对应舞蹈建议")
    print("   • 🔍 直接跳转到YouTube搜索")
    print("   • 📅 完整时间轴视图")
    print("   • 💡 详细的学习建议")
    print("\n🚀 使用方法:")
    print("   1. 启动: streamlit run app.py")
    print("   2. 上传音频文件并生成编舞")
    print("   3. 切换到'音乐播放器'标签页")
    print("   4. 播放音乐并查看实时舞蹈建议")

if __name__ == "__main__":
    main()
