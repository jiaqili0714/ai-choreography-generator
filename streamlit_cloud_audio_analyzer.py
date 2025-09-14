"""
Streamlit Cloud兼容的音频分析器
使用基础库实现专业级音频分析功能
"""

import librosa
import numpy as np
import soundfile as sf
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

class StreamlitCloudAudioAnalyzer:
    """Streamlit Cloud兼容的音频分析器"""
    
    def __init__(self):
        self.sample_rate = 22050
        self.hop_length = 512
        self.frame_length = 2048
        
    def load_audio(self, file_path: str) -> Tuple[np.ndarray, int]:
        """加载音频文件"""
        try:
            y, sr = librosa.load(file_path, sr=self.sample_rate)
            return y, sr
        except Exception as e:
            raise Exception(f"Error loading audio: {e}")
    
    def extract_enhanced_features(self, y: np.ndarray, sr: int) -> Dict:
        """提取增强音频特征"""
        # BPM检测
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=self.hop_length)
        
        # 频谱特征
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        rms = librosa.feature.rms(y=y)[0]
        
        # 节拍点
        beat_times = librosa.frames_to_time(beats, sr=sr, hop_length=self.hop_length)
        
        # 高级特征计算
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0]
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        
        # 能量和动态特征
        energy = np.mean(rms)
        energy_std = np.std(rms)
        spectral_centroid_mean = np.mean(spectral_centroids)
        spectral_centroid_std = np.std(spectral_centroids)
        
        # 节奏特征
        tempo_confidence = self._calculate_tempo_confidence(beats, sr)
        
        # 情绪和风格特征
        mood_features = self._extract_mood_features(y, sr)
        style_features = self._extract_style_features(y, sr)
        
        return {
            'tempo': float(tempo),
            'tempo_confidence': float(tempo_confidence),
            'beats': beats,
            'beat_times': beat_times,
            'energy': float(energy),
            'energy_std': float(energy_std),
            'spectral_centroid_mean': float(spectral_centroid_mean),
            'spectral_centroid_std': float(spectral_centroid_std),
            'spectral_rolloff_mean': float(np.mean(spectral_rolloff)),
            'spectral_bandwidth_mean': float(np.mean(spectral_bandwidth)),
            'mfcc_mean': [float(x) for x in np.mean(mfccs, axis=1)],
            'zero_crossing_rate_mean': float(np.mean(zero_crossing_rate)),
            'chroma_mean': [float(x) for x in np.mean(chroma, axis=1)],
            'tonnetz_mean': [float(x) for x in np.mean(tonnetz, axis=1)],
            'duration': len(y) / sr,
            'mood_features': mood_features,
            'style_features': style_features
        }
    
    def _calculate_tempo_confidence(self, beats: np.ndarray, sr: int) -> float:
        """计算节拍检测置信度"""
        if len(beats) < 2:
            return 0.0
        
        # 计算节拍间隔的一致性
        intervals = np.diff(beats)
        if len(intervals) == 0:
            return 0.0
        
        # 使用变异系数作为置信度指标
        cv = np.std(intervals) / np.mean(intervals) if np.mean(intervals) > 0 else 1.0
        confidence = max(0.0, 1.0 - cv)
        return confidence
    
    def _extract_mood_features(self, y: np.ndarray, sr: int) -> Dict:
        """提取情绪特征"""
        # 使用频谱特征推断情绪
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        rms = librosa.feature.rms(y=y)[0]
        
        # 计算情绪指标
        brightness = np.mean(spectral_centroids)
        energy = np.mean(rms)
        energy_variation = np.std(rms)
        
        # 情绪分类
        if brightness > np.percentile(spectral_centroids, 75) and energy > np.percentile(rms, 75):
            mood = "energetic"
            valence = 0.8
        elif brightness < np.percentile(spectral_centroids, 25) and energy < np.percentile(rms, 25):
            mood = "calm"
            valence = 0.3
        elif energy_variation > np.percentile(rms, 75):
            mood = "dynamic"
            valence = 0.6
        else:
            mood = "neutral"
            valence = 0.5
        
        return {
            'mood': mood,
            'valence': float(valence),
            'brightness': float(brightness),
            'energy': float(energy),
            'energy_variation': float(energy_variation)
        }
    
    def _extract_style_features(self, y: np.ndarray, sr: int) -> Dict:
        """提取风格特征"""
        # 使用MFCC和频谱特征推断风格
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        rms = librosa.feature.rms(y=y)[0]
        
        # 计算风格指标
        mfcc_mean = np.mean(mfccs, axis=1)
        spectral_centroid_mean = np.mean(spectral_centroids)
        energy_mean = np.mean(rms)
        
        # 风格分类逻辑
        if energy_mean > 0.1 and spectral_centroid_mean > 2000:
            if mfcc_mean[1] > 0:  # 高频成分多
                style = "Hip-Hop"
                confidence = 0.8
            else:
                style = "House"
                confidence = 0.7
        elif energy_mean < 0.05 and spectral_centroid_mean < 1500:
            style = "Jazz"
            confidence = 0.6
        elif mfcc_mean[0] < -5:  # 低频成分多
            style = "Breaking"
            confidence = 0.7
        else:
            style = "K-pop"
            confidence = 0.5
        
        return {
            'dance_style': style,
            'style_confidence': float(confidence),
            'mfcc_features': [float(x) for x in mfcc_mean],
            'spectral_features': {
                'centroid': float(spectral_centroid_mean),
                'energy': float(energy_mean)
            }
        }
    
    def segment_audio_by_beats(self, beat_times: np.ndarray, beats_per_segment: int = 8) -> List[Dict]:
        """按节拍分割音频"""
        segments = []
        
        for i in range(0, len(beat_times) - beats_per_segment + 1, beats_per_segment):
            start_time = beat_times[i]
            end_time = beat_times[i + beats_per_segment - 1] if i + beats_per_segment < len(beat_times) else beat_times[-1]
            
            segments.append({
                'segment_id': len(segments),
                'start_time': float(start_time),
                'end_time': float(end_time),
                'duration': float(end_time - start_time),
                'start_beat': i,
                'end_beat': i + beats_per_segment - 1
            })
        
        return segments
    
    def analyze_audio_segment(self, y: np.ndarray, sr: int, start_time: float, end_time: float) -> Dict:
        """分析音频片段特征"""
        start_sample = int(start_time * sr)
        end_sample = int(end_time * sr)
        segment = y[start_sample:end_sample]
        
        if len(segment) == 0:
            return {}
        
        # 提取片段特征
        tempo, _ = librosa.beat.beat_track(y=segment, sr=sr)
        spectral_centroid = librosa.feature.spectral_centroid(y=segment, sr=sr)[0]
        rms = librosa.feature.rms(y=segment)[0]
        mfccs = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=13)
        
        # 计算复杂度
        complexity = np.std(spectral_centroid) / np.mean(spectral_centroid) if np.mean(spectral_centroid) > 0 else 0
        
        return {
            'tempo': float(tempo),
            'energy': float(np.mean(rms)),
            'brightness': float(np.mean(spectral_centroid)),
            'complexity': float(complexity),
            'mfcc_mean': [float(x) for x in np.mean(mfccs, axis=1)]
        }
    
    def comprehensive_analysis(self, file_path: str) -> Dict:
        """综合分析音频文件"""
        print("🎵 开始综合分析音频...")
        
        # 加载音频
        y, sr = self.load_audio(file_path)
        
        # 提取增强特征
        print("📊 提取增强特征...")
        features = self.extract_enhanced_features(y, sr)
        
        # 分割音频
        segments = self.segment_audio_by_beats(features['beat_times'])
        
        # 分析每个片段
        segment_features = []
        for segment in segments:
            seg_features = self.analyze_audio_segment(
                y, sr, segment['start_time'], segment['end_time']
            )
            segment_features.append({**segment, **seg_features})
        
        # 构建结果
        result = {
            'audio_info': {
                'duration': float(features['duration']),
                'bpm': float(features['tempo']),
                'total_beats': len(features['beat_times']),
                'sample_rate': sr
            },
            'features': features,
            'segments': segment_features,
            'dance_style': features['style_features']['dance_style'],
            'style_confidence': features['style_features']['style_confidence']
        }
        
        print(f"✅ 分析完成！检测到 {len(segments)} 个8拍片段，BPM: {features['tempo']:.1f}")
        print(f"🎭 推荐舞蹈风格: {result['dance_style']}")
        
        return result
