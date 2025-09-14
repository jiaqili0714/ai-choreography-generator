import os
import json
from typing import Dict, Any, Optional
from audio_processor import AudioProcessor
from llm_choreographer import LLMChoreographer
import config

class ChoreographyGenerator:
    """编舞生成器主类，整合音频处理和LLM生成功能"""
    
    def __init__(self):
        self.audio_processor = AudioProcessor()
        self.llm_choreographer = LLMChoreographer()
    
    def generate_choreography_from_file(self, audio_file_path: str) -> Dict[str, Any]:
        """
        从音频文件生成编舞
        
        Args:
            audio_file_path: 音频文件路径
            
        Returns:
            choreography_result: 编舞结果
        """
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"音频文件不存在: {audio_file_path}")
        
        print(f"开始处理音频文件: {audio_file_path}")
        
        # 1. 加载音频
        audio_data, sample_rate = self.audio_processor.load_audio(audio_file_path)
        print(f"音频加载完成，采样率: {sample_rate}Hz，时长: {len(audio_data)/sample_rate:.2f}秒")
        
        # 2. 检测BPM和节拍
        bpm, beat_times = self.audio_processor.detect_bpm_and_beats(audio_data)
        print(f"BPM检测完成: {bpm:.1f}，检测到{len(beat_times)}个节拍点")
        
        # 3. 分析音频特征
        audio_features = self.audio_processor.analyze_audio_features(audio_data)
        print("音频特征分析完成")
        
        # 4. 分割成8拍片段
        segments = self.audio_processor.segment_into_8beats(beat_times, bpm)
        print(f"音乐分割完成，共{len(segments)}个8拍片段")
        
        # 5. 推荐舞蹈风格
        dance_style = self.llm_choreographer.generate_choreography_style(bpm, audio_features)
        print(f"推荐舞蹈风格: {dance_style}")
        
        # 6. 生成编舞
        choreography = self.llm_choreographer.generate_full_choreography(segments, bpm, dance_style, audio_features)
        
        # 7. 整理结果
        result = {
            "audio_info": {
                "file_path": audio_file_path,
                "duration": len(audio_data) / sample_rate,
                "sample_rate": sample_rate,
                "bpm": bpm,
                "total_beats": len(beat_times)
            },
            "audio_features": audio_features,
            "segments": segments,
            "choreography": choreography
        }
        
        return result
    
    def save_choreography(self, choreography_result: Dict[str, Any], 
                         output_path: str) -> None:
        """
        保存编舞结果到文件
        
        Args:
            choreography_result: 编舞结果
            output_path: 输出文件路径
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(choreography_result, f, ensure_ascii=False, indent=2)
        print(f"编舞结果已保存到: {output_path}")
    
    def print_choreography_summary(self, choreography_result: Dict[str, Any]) -> None:
        """
        打印编舞摘要
        
        Args:
            choreography_result: 编舞结果
        """
        audio_info = choreography_result["audio_info"]
        choreography = choreography_result["choreography"]
        
        print("\n" + "="*50)
        print("🎵 编舞生成完成！")
        print("="*50)
        print(f"📁 音频文件: {os.path.basename(audio_info['file_path'])}")
        print(f"⏱️  时长: {audio_info['duration']:.2f}秒")
        print(f"🎶 BPM: {audio_info['bpm']:.1f}")
        print(f"💃 舞蹈风格: {choreography['dance_style']}")
        print(f"📊 总片段数: {choreography['total_segments']}")
        print(f"📝 编舞总结: {choreography['summary']}")
        print("="*50)
        
        # 打印每个片段的动作
        print("\n🎭 分段动作详情:")
        print("-"*50)
        
        for i, segment_choreo in enumerate(choreography['segments']):
            print(f"\n第{i+1}段 ({choreography_result['segments'][i]['start_time']:.1f}s - {choreography_result['segments'][i]['end_time']:.1f}s):")
            print(f"  动作描述: {segment_choreo['description']}")
            print(f"  动作序列: {segment_choreo['emoji_sequence']}")
            print(f"  难度等级: {segment_choreo['difficulty']}/5")
            print(f"  能量等级: {segment_choreo['energy_level']}/5")
            print(f"  关键动作: {', '.join(segment_choreo['key_moves'])}")
    
    def generate_choreography_from_song_name(self, song_name: str) -> Dict[str, Any]:
        """
        从歌名生成编舞（未来可扩展为Spotify/YouTube API集成）
        
        Args:
            song_name: 歌曲名称
            
        Returns:
            choreography_result: 编舞结果
        """
        # 这里可以集成Spotify或YouTube API来获取音频
        # 目前返回一个示例结果
        print(f"正在搜索歌曲: {song_name}")
        print("注意: 此功能需要集成Spotify/YouTube API，目前返回示例结果")
        
        # 示例编舞结果
        example_result = {
            "audio_info": {
                "file_path": f"搜索歌曲: {song_name}",
                "duration": 180.0,
                "sample_rate": 22050,
                "bpm": 120.0,
                "total_beats": 360
            },
            "audio_features": {
                "spectral_centroid_mean": 2000.0,
                "energy_mean": 0.5
            },
            "segments": [
                {
                    "segment_id": 0,
                    "start_time": 0.0,
                    "end_time": 4.0,
                    "duration": 4.0,
                    "beat_count": 8,
                    "beats": [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
                }
            ],
            "choreography": {
                "dance_style": "Hip-Hop",
                "bpm": 120.0,
                "total_segments": 1,
                "total_duration": 4.0,
                "summary": f"为歌曲'{song_name}'生成的Hip-Hop风格编舞示例",
                "segments": [{
                    "description": "开场动作：跟随节拍的基础步伐",
                    "emoji_sequence": "👟➡️🕺 Freeze 🤸‍♂️ Slide Clap",
                    "difficulty": 3,
                    "energy_level": 4,
                    "key_moves": ["基础步伐", "Freeze", "Slide", "Clap"]
                }]
            }
        }
        
        return example_result
