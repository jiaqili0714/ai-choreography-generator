import librosa
import numpy as np
from typing import Tuple, List
import config

class AudioProcessor:
    """音频处理类，负责BPM检测和节拍分割"""
    
    def __init__(self):
        self.sample_rate = config.SAMPLE_RATE
        self.hop_length = config.HOP_LENGTH
        self.frame_length = config.FRAME_LENGTH
    
    def load_audio(self, file_path: str) -> Tuple[np.ndarray, float]:
        """
        加载音频文件
        
        Args:
            file_path: 音频文件路径
            
        Returns:
            audio_data: 音频数据
            sample_rate: 采样率
        """
        try:
            audio_data, sr = librosa.load(file_path, sr=self.sample_rate)
            return audio_data, sr
        except Exception as e:
            raise Exception(f"无法加载音频文件: {e}")
    
    def detect_bpm_and_beats(self, audio_data: np.ndarray) -> Tuple[float, np.ndarray]:
        """
        检测BPM和节拍点
        
        Args:
            audio_data: 音频数据
            
        Returns:
            bpm: 每分钟节拍数
            beat_times: 节拍时间点数组
        """
        # 使用librosa检测节拍
        tempo, beats = librosa.beat.beat_track(
            y=audio_data, 
            sr=self.sample_rate,
            hop_length=self.hop_length
        )
        
        # 将节拍帧转换为时间
        beat_times = librosa.frames_to_time(beats, sr=self.sample_rate, hop_length=self.hop_length)
        
        return float(tempo), beat_times
    
    def segment_into_8beats(self, beat_times: np.ndarray, bpm: float) -> List[dict]:
        """
        将音乐分割成8拍片段
        
        Args:
            beat_times: 节拍时间点数组
            bpm: 每分钟节拍数
            
        Returns:
            segments: 8拍片段列表，每个片段包含开始时间、结束时间和节拍数
        """
        segments = []
        beats_per_second = bpm / 60.0
        segment_duration = config.BEATS_PER_SEGMENT / beats_per_second
        
        current_time = 0.0
        segment_index = 0
        
        while current_time < beat_times[-1]:
            end_time = min(current_time + segment_duration, beat_times[-1])
            
            # 找到这个时间段内的节拍
            segment_beats = beat_times[
                (beat_times >= current_time) & (beat_times < end_time)
            ]
            
            segment = {
                'segment_id': segment_index,
                'start_time': current_time,
                'end_time': end_time,
                'duration': end_time - current_time,
                'beat_count': len(segment_beats),
                'beats': segment_beats.tolist()
            }
            
            segments.append(segment)
            current_time = end_time
            segment_index += 1
        
        return segments
    
    def analyze_audio_features(self, audio_data: np.ndarray) -> dict:
        """
        分析音频特征
        
        Args:
            audio_data: 音频数据
            
        Returns:
            features: 音频特征字典
        """
        # 提取音频特征
        spectral_centroids = librosa.feature.spectral_centroid(y=audio_data, sr=self.sample_rate)[0]
        spectral_rolloff = librosa.feature.spectral_rolloff(y=audio_data, sr=self.sample_rate)[0]
        mfccs = librosa.feature.mfcc(y=audio_data, sr=self.sample_rate, n_mfcc=13)
        
        # 计算统计特征
        features = {
            'spectral_centroid_mean': float(np.mean(spectral_centroids)),
            'spectral_centroid_std': float(np.std(spectral_centroids)),
            'spectral_rolloff_mean': float(np.mean(spectral_rolloff)),
            'spectral_rolloff_std': float(np.std(spectral_rolloff)),
            'mfcc_mean': [float(np.mean(mfcc)) for mfcc in mfccs],
            'energy_mean': float(np.mean(librosa.feature.rms(y=audio_data)[0]))
        }
        
        return features
