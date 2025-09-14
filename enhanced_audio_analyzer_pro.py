"""
专业级音频分析器
集成librosa、madmom、essentia、musicnn等高级音频分析库
"""

import librosa
import numpy as np
import soundfile as sf
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

# 尝试导入高级音频分析库
try:
    import madmom
    MADMOM_AVAILABLE = True
    print("✅ madmom 已加载")
except ImportError:
    MADMOM_AVAILABLE = False
    print("⚠️ madmom 不可用，使用librosa替代")

try:
    import essentia.standard as es
    ESSENTIA_AVAILABLE = True
    print("✅ essentia 已加载")
except ImportError:
    ESSENTIA_AVAILABLE = False
    print("⚠️ essentia 不可用，使用librosa替代")

try:
    import musicnn
    MUSICNN_AVAILABLE = True
    print("✅ musicnn 已加载")
except ImportError:
    MUSICNN_AVAILABLE = False
    print("⚠️ musicnn 不可用，使用特征工程替代")

class EnhancedAudioAnalyzerPro:
    """专业级音频分析器"""
    
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
        print("🎵 开始专业级音频分析...")
        
        # 基础特征 (librosa)
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=self.hop_length)
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        rms = librosa.feature.rms(y=y)[0]
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0]
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        
        # 高级节拍检测 (madmom)
        if MADMOM_AVAILABLE:
            print("🎯 使用madmom进行精确节拍检测...")
            try:
                # 使用madmom的DBNDownBeatTrackingProcessor
                proc = madmom.features.downbeats.DBNDownBeatTrackingProcessor(
                    beats_per_bar=[3, 4], fps=100)
                act = madmom.features.downbeats.RNNDownBeatProcessor()(file_path)
                downbeats = proc(act)
                
                # 提取节拍信息
                beat_times = downbeats[:, 0]
                beat_labels = downbeats[:, 1]
                
                # 计算节拍置信度
                tempo_confidence = self._calculate_madmom_confidence(beat_times, sr)
                
                print(f"✅ madmom检测到 {len(beat_times)} 个节拍点")
                
            except Exception as e:
                print(f"⚠️ madmom处理失败: {e}")
                beat_times = librosa.frames_to_time(beats, sr=sr, hop_length=self.hop_length)
                beat_labels = np.ones(len(beat_times))
                tempo_confidence = 0.7
        else:
            beat_times = librosa.frames_to_time(beats, sr=sr, hop_length=self.hop_length)
            beat_labels = np.ones(len(beat_times))
            tempo_confidence = 0.7
        
        # 高级音频特征 (essentia)
        if ESSENTIA_AVAILABLE:
            print("🎨 使用essentia提取高级特征...")
            try:
                # 加载音频到essentia
                loader = es.MonoLoader(filename=file_path, sampleRate=sr)
                audio = loader()
                
                # 提取高级特征
                rhythm_extractor = es.RhythmExtractor2013(method="multifeature")
                bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)
                
                # 情绪和风格特征
                mood_extractor = es.PredominantPitchMelodia()
                pitch, pitch_confidence = mood_extractor(audio)
                
                # 频谱特征
                spectral_peaks = es.SpectralPeaks()
                frequencies, magnitudes = spectral_peaks(audio)
                
                # 和声特征
                hpcp = es.HPCP()
                hpcp_values = hpcp(frequencies, magnitudes)
                
                # 构建essentia特征
                essentia_features = {
                    'bpm_essentia': float(bpm),
                    'beats_confidence': float(beats_confidence),
                    'pitch_mean': float(np.mean(pitch)),
                    'pitch_std': float(np.std(pitch)),
                    'hpcp_mean': [float(x) for x in np.mean(hpcp_values, axis=0)],
                    'spectral_peaks_count': len(frequencies)
                }
                
                print("✅ essentia特征提取完成")
                
            except Exception as e:
                print(f"⚠️ essentia处理失败: {e}")
                essentia_features = {}
        else:
            essentia_features = {}
        
        # 音乐风格识别 (musicnn)
        if MUSICNN_AVAILABLE:
            print("🎭 使用musicnn进行风格识别...")
            try:
                # 使用musicnn进行风格识别
                taggram, tags, features = musicnn.extract(file_path, model='MSD_musicnn', extract_features=True)
                
                # 获取最可能的风格标签
                top_tags = tags[np.argsort(taggram.mean(axis=0))[-5:]]
                style_confidence = float(np.max(taggram.mean(axis=0)))
                
                # 构建风格特征
                musicnn_features = {
                    'top_tags': [str(tag) for tag in top_tags],
                    'style_confidence': style_confidence,
                    'taggram_mean': [float(x) for x in taggram.mean(axis=0)]
                }
                
                print(f"✅ musicnn识别风格: {top_tags}")
                
            except Exception as e:
                print(f"⚠️ musicnn处理失败: {e}")
                musicnn_features = {}
        else:
            musicnn_features = {}
        
        # 计算基础特征
        energy = np.mean(rms)
        energy_std = np.std(rms)
        spectral_centroid_mean = np.mean(spectral_centroids)
        spectral_centroid_std = np.std(spectral_centroids)
        
        # 情绪和风格特征
        mood_features = self._extract_mood_features_enhanced(y, sr, essentia_features)
        style_features = self._extract_style_features_enhanced(y, sr, musicnn_features)
        
        # 构建结果
        result = {
            'tempo': float(tempo),
            'tempo_confidence': float(tempo_confidence),
            'beats': beats,
            'beat_times': beat_times,
            'beat_labels': beat_labels,
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
            'style_features': style_features,
            'essentia_features': essentia_features,
            'musicnn_features': musicnn_features,
            'madmom_available': MADMOM_AVAILABLE,
            'essentia_available': ESSENTIA_AVAILABLE,
            'musicnn_available': MUSICNN_AVAILABLE
        }
        
        print(f"✅ 专业级分析完成！BPM: {tempo:.1f}, 置信度: {tempo_confidence:.2f}")
        return result
    
    def _calculate_madmom_confidence(self, beat_times: np.ndarray, sr: int) -> float:
        """计算madmom节拍检测置信度"""
        if len(beat_times) < 2:
            return 0.0
        
        intervals = np.diff(beat_times)
        if len(intervals) == 0:
            return 0.0
        
        # 使用变异系数作为置信度指标
        cv = np.std(intervals) / np.mean(intervals) if np.mean(intervals) > 0 else 1.0
        confidence = max(0.0, 1.0 - cv)
        return confidence
    
    def _extract_mood_features_enhanced(self, y: np.ndarray, sr: int, essentia_features: Dict) -> Dict:
        """提取增强情绪特征"""
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        rms = librosa.feature.rms(y=y)[0]
        
        # 基础情绪指标
        brightness = np.mean(spectral_centroids)
        energy = np.mean(rms)
        energy_variation = np.std(rms)
        
        # 如果有essentia特征，使用更精确的情绪分析
        if essentia_features:
            pitch_mean = essentia_features.get('pitch_mean', brightness)
            pitch_std = essentia_features.get('pitch_std', energy_variation)
            
            # 更精确的情绪分类
            if pitch_mean > np.percentile(spectral_centroids, 80) and energy > np.percentile(rms, 80):
                mood = "energetic"
                valence = 0.9
            elif pitch_mean < np.percentile(spectral_centroids, 20) and energy < np.percentile(rms, 20):
                mood = "calm"
                valence = 0.2
            elif pitch_std > np.percentile(rms, 80):
                mood = "dynamic"
                valence = 0.7
            else:
                mood = "neutral"
                valence = 0.5
        else:
            # 基础情绪分类
            if brightness > np.percentile(spectral_centroids, 75) and energy > np.percentile(rms, 75):
                mood = "energetic"
                valence = 0.8
            elif brightness < np.percentile(spectral_centroids, 25) and energy < np.percentile(rms, 25):
                mood = "calm"
                valence = 0.3
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
    
    def _extract_style_features_enhanced(self, y: np.ndarray, sr: int, musicnn_features: Dict) -> Dict:
        """提取增强风格特征"""
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        rms = librosa.feature.rms(y=y)[0]
        
        # 如果有musicnn特征，使用更精确的风格识别
        if musicnn_features:
            top_tags = musicnn_features.get('top_tags', [])
            style_confidence = musicnn_features.get('style_confidence', 0.5)
            
            # 根据musicnn标签确定舞蹈风格
            if any(tag in ['hip hop', 'rap', 'urban'] for tag in top_tags):
                style = "Hip-Hop"
                confidence = style_confidence
            elif any(tag in ['house', 'electronic', 'dance'] for tag in top_tags):
                style = "House"
                confidence = style_confidence
            elif any(tag in ['jazz', 'blues', 'soul'] for tag in top_tags):
                style = "Jazz"
                confidence = style_confidence
            elif any(tag in ['pop', 'k-pop', 'korean'] for tag in top_tags):
                style = "K-pop"
                confidence = style_confidence
            else:
                style = "Contemporary"
                confidence = style_confidence * 0.8
        else:
            # 基础风格分类
            mfcc_mean = np.mean(mfccs, axis=1)
            spectral_centroid_mean = np.mean(spectral_centroids)
            energy_mean = np.mean(rms)
            
            if energy_mean > 0.1 and spectral_centroid_mean > 2000:
                if mfcc_mean[1] > 0:
                    style = "Hip-Hop"
                    confidence = 0.8
                else:
                    style = "House"
                    confidence = 0.7
            elif energy_mean < 0.05 and spectral_centroid_mean < 1500:
                style = "Jazz"
                confidence = 0.6
            else:
                style = "K-pop"
                confidence = 0.5
        
        return {
            'dance_style': style,
            'style_confidence': float(confidence),
            'mfcc_features': [float(x) for x in np.mean(mfccs, axis=1)],
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
        print("🎵 开始专业级综合分析...")
        
        # 加载音频
        y, sr = self.load_audio(file_path)
        
        # 提取增强特征
        print("📊 提取专业级特征...")
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
                'duration': features['duration'],
                'bpm': features['tempo'],
                'total_beats': len(features['beat_times']),
                'sample_rate': sr
            },
            'features': features,
            'segments': segment_features,
            'dance_style': features['style_features']['dance_style'],
            'style_confidence': features['style_features']['style_confidence'],
            'analysis_method': 'professional_enhanced'
        }
        
        print(f"✅ 专业级分析完成！检测到 {len(segments)} 个8拍片段，BPM: {features['tempo']:.1f}")
        print(f"🎭 推荐舞蹈风格: {result['dance_style']}")
        print(f"🔧 使用的高级库: madmom={MADMOM_AVAILABLE}, essentia={ESSENTIA_AVAILABLE}, musicnn={MUSICNN_AVAILABLE}")
        
        return result
