"""
增强音频分析器
集成librosa、madmom、Essentia、musicnn等专业音频分析库
"""

import librosa
import numpy as np
import soundfile as sf
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

try:
    import madmom
    MADMOM_AVAILABLE = True
except ImportError:
    MADMOM_AVAILABLE = False
    print("Warning: madmom not available, using librosa beat tracking")

try:
    import essentia.standard as es
    ESSENTIA_AVAILABLE = True
except ImportError:
    ESSENTIA_AVAILABLE = False
    print("Warning: essentia not available, using basic features")

try:
    import musicnn
    MUSICNN_AVAILABLE = True
except ImportError:
    MUSICNN_AVAILABLE = False
    print("Warning: musicnn not available, using basic genre detection")

class EnhancedAudioAnalyzer:
    """增强音频分析器"""
    
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
    
    def extract_basic_features(self, y: np.ndarray, sr: int) -> Dict:
        """提取基础音频特征"""
        # BPM检测
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=self.hop_length)
        
        # 频谱特征
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        rms = librosa.feature.rms(y=y)[0]
        
        # 节拍点
        beat_times = librosa.frames_to_time(beats, sr=sr, hop_length=self.hop_length)
        
        return {
            'tempo': float(tempo),
            'beats': beats,
            'beat_times': beat_times,
            'spectral_centroid_mean': float(np.mean(spectral_centroids)),
            'spectral_rolloff_mean': float(np.mean(spectral_rolloff)),
            'mfcc_mean': [float(x) for x in np.mean(mfccs, axis=1)],
            'rms_mean': float(np.mean(rms)),
            'duration': len(y) / sr
        }
    
    def extract_madmom_features(self, file_path: str) -> Dict:
        """使用madmom提取精确节拍特征"""
        if not MADMOM_AVAILABLE:
            return {}
        
        try:
            # 使用madmom的DBNDownBeatTrackingProcessor
            proc = madmom.features.downbeat.DBNDownBeatTrackingProcessor(beats_per_bar=[4])
            act = madmom.features.downbeat.RNNDownBeatProcessor()(file_path)
            downbeats = proc(act)
            
            # 提取节拍点
            beats = []
            for beat in downbeats:
                beats.append(beat[0])  # 时间点
            
            # 计算BPM
            if len(beats) > 1:
                intervals = np.diff(beats)
                bpm = 60.0 / np.mean(intervals)
            else:
                bpm = 120.0
            
            return {
                'madmom_bpm': float(bpm),
                'madmom_beats': beats,
                'downbeats': downbeats.tolist()
            }
        except Exception as e:
            print(f"Madmom analysis failed: {e}")
            return {}
    
    def extract_essentia_features(self, file_path: str) -> Dict:
        """使用Essentia提取高级音频特征"""
        if not ESSENTIA_AVAILABLE:
            return {}
        
        try:
            # 加载音频
            loader = es.MonoLoader(filename=file_path, sampleRate=self.sample_rate)
            audio = loader()
            
            # 提取特征
            rhythm_extractor = es.RhythmExtractor2013(method="multifeature")
            bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)
            
            # 情绪和能量特征
            mood_extractor = es.PredominantPitchMelodia()
            pitch, pitch_confidence = mood_extractor(audio)
            
            # 频谱特征
            spectral_peaks = es.SpectralPeaks()
            frequencies, magnitudes = spectral_peaks(audio)
            
            # 和声特征
            hpcp = es.HPCP()
            hpcp_values = hpcp(frequencies, magnitudes)
            
            return {
                'essentia_bpm': float(bpm),
                'essentia_beats': beats.tolist(),
                'beats_confidence': float(np.mean(beats_confidence)),
                'pitch_mean': float(np.mean(pitch)) if len(pitch) > 0 else 0,
                'pitch_confidence': float(np.mean(pitch_confidence)) if len(pitch_confidence) > 0 else 0,
                'hpcp_mean': [float(x) for x in np.mean(hpcp_values, axis=0)],
                'energy': float(np.mean(audio**2))
            }
        except Exception as e:
            print(f"Essentia analysis failed: {e}")
            return {}
    
    def extract_musicnn_features(self, file_path: str) -> Dict:
        """使用musicnn进行音乐风格识别"""
        if not MUSICNN_AVAILABLE:
            return self._basic_genre_detection()
        
        try:
            # 使用musicnn进行风格识别
            taggram, tags, features = musicnn.predict(file_path)
            
            # 获取最可能的风格标签
            top_tags = tags[np.argsort(taggram.mean(axis=0))[-5:]]
            
            # 映射到舞蹈风格
            dance_style = self._map_genre_to_dance_style(top_tags)
            
            return {
                'musicnn_tags': top_tags.tolist(),
                'dance_style': dance_style,
                'style_confidence': float(np.max(taggram.mean(axis=0)))
            }
        except Exception as e:
            print(f"Musicnn analysis failed: {e}")
            return self._basic_genre_detection()
    
    def _basic_genre_detection(self) -> Dict:
        """基础风格检测（当musicnn不可用时）"""
        return {
            'dance_style': 'Hip-Hop',
            'style_confidence': 0.5,
            'musicnn_tags': ['electronic', 'dance', 'hip-hop']
        }
    
    def _map_genre_to_dance_style(self, tags: List[str]) -> str:
        """将音乐风格标签映射到舞蹈风格"""
        tag_str = ' '.join(tags).lower()
        
        if any(word in tag_str for word in ['hip', 'hop', 'rap', 'urban']):
            return 'Hip-Hop'
        elif any(word in tag_str for word in ['house', 'electronic', 'techno', 'edm']):
            return 'House'
        elif any(word in tag_str for word in ['k-pop', 'pop', 'korean']):
            return 'K-pop'
        elif any(word in tag_str for word in ['jazz', 'blues', 'swing']):
            return 'Jazz'
        elif any(word in tag_str for word in ['contemporary', 'modern', 'ballet']):
            return 'Contemporary'
        elif any(word in tag_str for word in ['break', 'breaking', 'b-boy']):
            return 'Breaking'
        else:
            return 'Hip-Hop'  # 默认风格
    
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
        
        return {
            'tempo': float(tempo),
            'energy': float(np.mean(rms)),
            'brightness': float(np.mean(spectral_centroid)),
            'complexity': float(np.std(spectral_centroid))
        }
    
    def comprehensive_analysis(self, file_path: str) -> Dict:
        """综合分析音频文件"""
        print("🎵 开始综合分析音频...")
        
        # 加载音频
        y, sr = self.load_audio(file_path)
        
        # 基础特征
        print("📊 提取基础特征...")
        basic_features = self.extract_basic_features(y, sr)
        
        # Madmom特征
        print("🎯 提取精确节拍特征...")
        madmom_features = self.extract_madmom_features(file_path)
        
        # Essentia特征
        print("🎨 提取高级音频特征...")
        essentia_features = self.extract_essentia_features(file_path)
        
        # Musicnn特征
        print("🎭 识别音乐风格...")
        musicnn_features = self.extract_musicnn_features(file_path)
        
        # 选择最佳BPM
        bpm_candidates = [basic_features['tempo']]
        if 'madmom_bpm' in madmom_features:
            bpm_candidates.append(madmom_features['madmom_bpm'])
        if 'essentia_bpm' in essentia_features:
            bpm_candidates.append(essentia_features['essentia_bpm'])
        
        final_bpm = np.median(bpm_candidates)
        
        # 选择最佳节拍点
        if 'madmom_beats' in madmom_features and len(madmom_features['madmom_beats']) > 0:
            beat_times = np.array(madmom_features['madmom_beats'])
        else:
            beat_times = basic_features['beat_times']
        
        # 分割音频
        segments = self.segment_audio_by_beats(beat_times)
        
        # 分析每个片段
        segment_features = []
        for segment in segments:
            seg_features = self.analyze_audio_segment(
                y, sr, segment['start_time'], segment['end_time']
            )
            segment_features.append({**segment, **seg_features})
        
        # 合并所有特征
        result = {
            'audio_info': {
                'duration': basic_features['duration'],
                'bpm': final_bpm,
                'total_beats': len(beat_times),
                'sample_rate': sr
            },
            'features': {
                **basic_features,
                **madmom_features,
                **essentia_features,
                **musicnn_features
            },
            'segments': segment_features,
            'dance_style': musicnn_features.get('dance_style', 'Hip-Hop'),
            'style_confidence': musicnn_features.get('style_confidence', 0.5)
        }
        
        print(f"✅ 分析完成！检测到 {len(segments)} 个8拍片段，BPM: {final_bpm:.1f}")
        print(f"🎭 推荐舞蹈风格: {result['dance_style']}")
        
        return result
