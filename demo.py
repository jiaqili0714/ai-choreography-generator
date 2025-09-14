#!/usr/bin/env python3
"""
AI编舞生成器演示脚本
展示系统的主要功能，无需API密钥
"""

import numpy as np
import librosa
from audio_processor import AudioProcessor
import json

def create_demo_audio():
    """创建一个演示音频文件"""
    print("🎵 创建演示音频文件...")
    
    # 生成一个120 BPM的演示音频
    duration = 16.0  # 16秒
    sample_rate = 22050
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # 创建节拍音
    beat_freq = 120 / 60  # 120 BPM
    beat_times = np.arange(0, duration, 1/beat_freq)
    
    # 生成音频信号
    audio = np.zeros_like(t)
    
    # 添加节拍
    for i, beat_time in enumerate(beat_times):
        beat_idx = int(beat_time * sample_rate)
        if beat_idx < len(audio):
            # 每4拍一个重音
            if i % 4 == 0:
                # 重音
                beat_duration = 0.2
                beat_samples = int(beat_duration * sample_rate)
                end_idx = min(beat_idx + beat_samples, len(audio))
                audio[beat_idx:end_idx] += 0.5 * np.sin(2 * np.pi * 440 * (t[beat_idx:end_idx] - beat_time))
            else:
                # 轻音
                beat_duration = 0.1
                beat_samples = int(beat_duration * sample_rate)
                end_idx = min(beat_idx + beat_samples, len(audio))
                audio[beat_idx:end_idx] += 0.2 * np.sin(2 * np.pi * 220 * (t[beat_idx:end_idx] - beat_time))
    
    # 添加背景音乐
    audio += 0.1 * np.sin(2 * np.pi * 220 * t)  # A3音符
    audio += 0.05 * np.sin(2 * np.pi * 330 * t)  # E4音符
    
    return audio, sample_rate

def demo_audio_analysis():
    """演示音频分析功能"""
    print("\n" + "="*60)
    print("🎵 音频分析演示")
    print("="*60)
    
    # 创建演示音频
    audio_data, sample_rate = create_demo_audio()
    print(f"✅ 创建了{len(audio_data)/sample_rate:.1f}秒的演示音频")
    
    # 初始化音频处理器
    processor = AudioProcessor()
    
    # 检测BPM和节拍
    print("\n🔍 正在分析音频...")
    bpm, beat_times = processor.detect_bpm_and_beats(audio_data)
    print(f"🎶 检测到的BPM: {bpm:.1f}")
    print(f"🥁 检测到的节拍点数量: {len(beat_times)}")
    
    # 分割成8拍片段
    segments = processor.segment_into_8beats(beat_times, bpm)
    print(f"📊 分割成{len(segments)}个8拍片段")
    
    # 分析音频特征
    features = processor.analyze_audio_features(audio_data)
    print(f"🎨 音频特征分析完成")
    
    return {
        'bpm': bpm,
        'beat_times': beat_times,
        'segments': segments,
        'features': features
    }

def demo_choreography_structure():
    """演示编舞结构"""
    print("\n" + "="*60)
    print("🎭 编舞结构演示")
    print("="*60)
    
    # 模拟编舞生成结果
    demo_choreography = {
        "dance_style": "Hip-Hop",
        "bpm": 120.0,
        "total_segments": 4,
        "total_duration": 16.0,
        "summary": "这是一个充满活力的Hip-Hop编舞，适合中级舞者。包含基础步伐、转身动作和Freeze技巧。",
        "segments": [
            {
                "description": "开场：跟随节拍的基础步伐，建立节奏感",
                "emoji_sequence": "👟➡️👟➡️🕺💃",
                "difficulty": 2,
                "energy_level": 3,
                "key_moves": ["基础步伐", "节奏感建立"]
            },
            {
                "description": "第二段：加入转身和手臂动作，增加表现力",
                "emoji_sequence": "🔄💫🤸‍♂️✨",
                "difficulty": 3,
                "energy_level": 4,
                "key_moves": ["转身", "手臂动作", "表现力"]
            },
            {
                "description": "高潮段：Freeze技巧和快速步伐组合",
                "emoji_sequence": "🕺 Freeze 🤸‍♂️ Slide Clap",
                "difficulty": 4,
                "energy_level": 5,
                "key_moves": ["Freeze", "Slide", "快速步伐"]
            },
            {
                "description": "结尾：收尾动作，回到基础步伐",
                "emoji_sequence": "👟➡️👟➡️🎵✨",
                "difficulty": 2,
                "energy_level": 3,
                "key_moves": ["收尾", "基础步伐"]
            }
        ]
    }
    
    print(f"💃 舞蹈风格: {demo_choreography['dance_style']}")
    print(f"🎶 BPM: {demo_choreography['bpm']}")
    print(f"📊 总片段数: {demo_choreography['total_segments']}")
    print(f"⏱️ 总时长: {demo_choreography['total_duration']}秒")
    print(f"\n📝 编舞总结:")
    print(f"   {demo_choreography['summary']}")
    
    print(f"\n🎭 分段动作详情:")
    for i, segment in enumerate(demo_choreography['segments']):
        print(f"\n   第{i+1}段:")
        print(f"   📝 描述: {segment['description']}")
        print(f"   🎨 动作序列: {segment['emoji_sequence']}")
        print(f"   📊 难度: {segment['difficulty']}/5")
        print(f"   ⚡ 能量: {segment['energy_level']}/5")
        print(f"   🎯 关键动作: {', '.join(segment['key_moves'])}")
    
    return demo_choreography

def demo_output_format():
    """演示输出格式"""
    print("\n" + "="*60)
    print("📄 输出格式演示")
    print("="*60)
    
    # 模拟完整的编舞结果
    full_result = {
        "audio_info": {
            "file_path": "demo_audio.wav",
            "duration": 16.0,
            "sample_rate": 22050,
            "bpm": 120.0,
            "total_beats": 32
        },
        "audio_features": {
            "spectral_centroid_mean": 2000.0,
            "spectral_centroid_std": 500.0,
            "spectral_rolloff_mean": 4000.0,
            "spectral_rolloff_std": 1000.0,
            "energy_mean": 0.3,
            "mfcc_mean": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
        },
        "segments": [
            {
                "segment_id": 0,
                "start_time": 0.0,
                "end_time": 4.0,
                "duration": 4.0,
                "beat_count": 8,
                "beats": [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
            },
            {
                "segment_id": 1,
                "start_time": 4.0,
                "end_time": 8.0,
                "duration": 4.0,
                "beat_count": 8,
                "beats": [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5]
            }
        ],
        "choreography": {
            "dance_style": "Hip-Hop",
            "bpm": 120.0,
            "total_segments": 2,
            "total_duration": 8.0,
            "summary": "这是一个充满活力的Hip-Hop编舞演示",
            "segments": [
                {
                    "description": "开场动作：跟随节拍的基础步伐",
                    "emoji_sequence": "👟➡️🕺💃",
                    "difficulty": 2,
                    "energy_level": 3,
                    "key_moves": ["基础步伐", "节奏感"]
                },
                {
                    "description": "第二段：加入转身和手臂动作",
                    "emoji_sequence": "🔄💫🤸‍♂️✨",
                    "difficulty": 3,
                    "energy_level": 4,
                    "key_moves": ["转身", "手臂动作"]
                }
            ]
        }
    }
    
    print("📋 完整的编舞结果包含以下信息:")
    print("   🎵 音频信息 (BPM, 时长, 节拍数等)")
    print("   🎨 音频特征 (频谱特征, 能量等)")
    print("   📊 分段信息 (时间范围, 节拍数等)")
    print("   🎭 编舞内容 (风格, 动作描述, emoji序列等)")
    
    print(f"\n💾 保存为JSON格式:")
    json_output = json.dumps(full_result, ensure_ascii=False, indent=2)
    print("   ✅ 支持中文输出")
    print("   ✅ 结构化数据")
    print("   ✅ 易于解析和扩展")
    
    return full_result

def main():
    """运行演示"""
    print("🎵 AI编舞生成器 - 功能演示")
    print("="*60)
    print("本演示展示系统的主要功能，无需API密钥")
    
    try:
        # 1. 音频分析演示
        audio_result = demo_audio_analysis()
        
        # 2. 编舞结构演示
        choreography_result = demo_choreography_structure()
        
        # 3. 输出格式演示
        output_result = demo_output_format()
        
        print("\n" + "="*60)
        print("🎉 演示完成！")
        print("="*60)
        print("✅ 音频分析功能正常")
        print("✅ 编舞结构设计合理")
        print("✅ 输出格式完整")
        print("\n💡 要使用完整功能，请:")
        print("   1. 设置OpenAI API密钥")
        print("   2. 运行 'streamlit run app.py' 启动Web界面")
        print("   3. 或使用 'python main.py <音频文件>' 命令行工具")
        
    except Exception as e:
        print(f"❌ 演示过程中出错: {e}")

if __name__ == "__main__":
    main()
