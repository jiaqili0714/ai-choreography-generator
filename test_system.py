#!/usr/bin/env python3
"""
系统测试脚本 - 验证各个模块功能
"""

import os
import sys
import numpy as np
import librosa
from audio_processor import AudioProcessor
from llm_choreographer import LLMChoreographer
from choreography_generator import ChoreographyGenerator

def create_test_audio():
    """创建一个测试音频文件"""
    print("🎵 创建测试音频文件...")
    
    # 生成一个简单的测试音频（120 BPM，4拍）
    duration = 4.0  # 4秒
    sample_rate = 22050
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # 创建简单的节拍音
    beat_freq = 120 / 60  # 120 BPM
    beat_times = np.arange(0, duration, 1/beat_freq)
    
    # 生成音频信号
    audio = np.zeros_like(t)
    for beat_time in beat_times:
        beat_idx = int(beat_time * sample_rate)
        if beat_idx < len(audio):
            # 添加一个简单的节拍音
            beat_duration = 0.1
            beat_samples = int(beat_duration * sample_rate)
            end_idx = min(beat_idx + beat_samples, len(audio))
            audio[beat_idx:end_idx] += 0.3 * np.sin(2 * np.pi * 440 * (t[beat_idx:end_idx] - beat_time))
    
    # 添加一些背景音乐
    audio += 0.1 * np.sin(2 * np.pi * 220 * t)  # A3音符
    
    return audio, sample_rate

def test_audio_processor():
    """测试音频处理模块"""
    print("\n🔧 测试音频处理模块...")
    
    try:
        # 创建测试音频
        audio_data, sample_rate = create_test_audio()
        
        # 测试音频处理器
        processor = AudioProcessor()
        
        # 测试BPM检测
        bpm, beat_times = processor.detect_bpm_and_beats(audio_data)
        print(f"✅ BPM检测: {bpm:.1f}")
        print(f"✅ 节拍点数量: {len(beat_times)}")
        
        # 测试8拍分割
        segments = processor.segment_into_8beats(beat_times, bpm)
        print(f"✅ 8拍片段数量: {len(segments)}")
        
        # 测试音频特征分析
        features = processor.analyze_audio_features(audio_data)
        print(f"✅ 音频特征提取完成")
        
        return True
        
    except Exception as e:
        print(f"❌ 音频处理模块测试失败: {e}")
        return False

def test_llm_choreographer():
    """测试LLM编舞生成模块"""
    print("\n🤖 测试LLM编舞生成模块...")
    
    # 检查API密钥
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️ 跳过LLM测试 - 未设置OPENAI_API_KEY")
        return True
    
    try:
        choreographer = LLMChoreographer()
        
        # 测试舞蹈风格推荐
        audio_features = {
            'spectral_centroid_mean': 2000.0,
            'energy_mean': 0.5,
            'spectral_rolloff_mean': 4000.0
        }
        
        dance_style = choreographer.generate_choreography_style(120.0, audio_features)
        print(f"✅ 舞蹈风格推荐: {dance_style}")
        
        # 测试片段编舞生成
        test_segment = {
            'start_time': 0.0,
            'end_time': 4.0,
            'duration': 4.0,
            'beat_count': 8,
            'beats': [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
        }
        
        choreography = choreographer.generate_segment_choreography(
            test_segment, 120.0, dance_style, 0
        )
        print(f"✅ 片段编舞生成: {choreography['description'][:50]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ LLM编舞生成模块测试失败: {e}")
        return False

def test_choreography_generator():
    """测试主生成器"""
    print("\n🎭 测试编舞生成器...")
    
    try:
        generator = ChoreographyGenerator()
        
        # 测试从歌名生成编舞
        result = generator.generate_choreography_from_song_name("测试歌曲")
        print(f"✅ 编舞生成器测试通过")
        print(f"   舞蹈风格: {result['choreography']['dance_style']}")
        print(f"   片段数量: {result['choreography']['total_segments']}")
        
        return True
        
    except Exception as e:
        print(f"❌ 编舞生成器测试失败: {e}")
        return False

def main():
    """运行所有测试"""
    print("🧪 开始系统测试...")
    print("="*50)
    
    tests = [
        ("音频处理模块", test_audio_processor),
        ("LLM编舞生成模块", test_llm_choreographer),
        ("编舞生成器", test_choreography_generator)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 测试: {test_name}")
        if test_func():
            passed += 1
            print(f"✅ {test_name} 测试通过")
        else:
            print(f"❌ {test_name} 测试失败")
    
    print("\n" + "="*50)
    print(f"🎯 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！系统运行正常。")
        return 0
    else:
        print("⚠️ 部分测试失败，请检查相关模块。")
        return 1

if __name__ == "__main__":
    sys.exit(main())
