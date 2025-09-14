"""
专业级编舞生成器
集成所有高级音频分析库和LLM功能
"""

import os
import tempfile
from typing import Dict, List, Any
from enhanced_audio_analyzer_pro import EnhancedAudioAnalyzerPro
from enhanced_llm_choreographer import EnhancedLLMChoreographer
from action_database import get_action_candidates, get_action_dimensions
import json

class EnhancedChoreographyGeneratorPro:
    """专业级编舞生成器"""
    
    def __init__(self):
        self.audio_analyzer = EnhancedAudioAnalyzerPro()
        self.llm_choreographer = EnhancedLLMChoreographer()
        self.recent_actions = []  # 记录最近使用的动作，用于避免重复
        self.max_recent_actions = 20  # 最多记录20个最近动作
    
    def generate_choreography_from_file(self, file_path: str) -> Dict:
        """从音频文件生成专业级编舞"""
        print("🎵 开始专业级编舞生成流程...")
        
        try:
            # 1. 专业级音频分析
            print("📊 步骤1: 专业级音频分析...")
            analysis_result = self.audio_analyzer.comprehensive_analysis(file_path)
            
            # 2. 提取关键信息
            audio_info = analysis_result['audio_info']
            features = analysis_result['features']
            segments = analysis_result['segments']
            dance_style = analysis_result['dance_style']
            analysis_method = analysis_result.get('analysis_method', 'professional_enhanced')
            
            print(f"🎭 检测到舞蹈风格: {dance_style}")
            print(f"📈 音频特征: BPM={audio_info['bpm']:.1f}, 时长={audio_info['duration']:.1f}s")
            print(f"🔧 分析方法: {analysis_method}")
            
            # 3. 生成编舞
            print("🎨 步骤2: 生成专业级结构化编舞...")
            choreography = self.llm_choreographer.generate_enhanced_choreography(
                audio_features=features,
                segments=segments,
                dance_style=dance_style,
                avoid_actions=self.recent_actions
            )
            
            # 4. 后处理和增强
            print("✨ 步骤3: 专业级后处理和增强...")
            enhanced_choreography = self._enhance_choreography_output_pro(
                choreography, segments, dance_style, features
            )
            
            # 5. 更新最近动作记录
            self._update_recent_actions(enhanced_choreography)
            
            # 6. 构建最终结果
            result = {
                'audio_info': audio_info,
                'features': features,
                'choreography': enhanced_choreography,
                'segments': segments,
                'dance_style': dance_style,
                'style_confidence': analysis_result.get('style_confidence', 0.5),
                'generation_method': 'professional_enhanced_pro',
                'analysis_method': analysis_method,
                'advanced_libraries': {
                    'madmom': features.get('madmom_available', False),
                    'essentia': features.get('essentia_available', False),
                    'musicnn': features.get('musicnn_available', False)
                }
            }
            
            print("🎉 专业级编舞生成完成！")
            return result
            
        except Exception as e:
            print(f"❌ 生成编舞时出错: {e}")
            raise e
    
    def _enhance_choreography_output_pro(self, choreography: Dict, 
                                       segments: List[Dict], 
                                       dance_style: str,
                                       features: Dict) -> Dict:
        """专业级编舞输出增强"""
        enhanced = choreography.copy()
        
        # 为每个片段添加详细信息
        for i, segment in enumerate(enhanced.get('segments', [])):
            if i < len(segments):
                segment_info = segments[i]
                
                # 添加音频特征信息
                segment['audio_features'] = {
                    'tempo': segment_info.get('tempo', 120),
                    'energy': segment_info.get('energy', 0.5),
                    'brightness': segment_info.get('brightness', 0.5),
                    'complexity': segment_info.get('complexity', 0.5)
                }
                
                # 添加动作维度信息
                segment['action_dimensions'] = {
                    'level': segment.get('level', 'mid'),
                    'plane': segment.get('plane', 'frontal'),
                    'accent': segment.get('accent', 'medium'),
                    'transition': segment.get('transition', 'quarter-turn')
                }
                
                # 添加专业教学建议
                segment['teaching_tips'] = self._generate_professional_teaching_tips(
                    segment, dance_style, features
                )
                
                # 添加难度评估
                segment['difficulty'] = self._assess_difficulty_pro(segment)
                
                # 添加能量等级
                segment['energy_level'] = self._assess_energy_level_pro(segment)
                
                # 添加技术要点
                segment['technical_points'] = self._generate_technical_points(
                    segment, dance_style
                )
        
        # 添加全局建议
        enhanced['global_advice'] = self._generate_global_advice_pro(
            enhanced, dance_style, features
        )
        
        # 添加专业分析信息
        enhanced['professional_analysis'] = self._generate_professional_analysis(
            features, dance_style
        )
        
        return enhanced
    
    def _generate_professional_teaching_tips(self, segment: Dict, dance_style: str, features: Dict) -> List[str]:
        """生成专业教学建议"""
        tips = []
        
        # 根据动作类型生成建议
        moves = segment.get('moves', [])
        level = segment.get('level', 'mid')
        accent = segment.get('accent', 'medium')
        
        if level == 'floor':
            tips.append("注意地板动作的安全性和流畅性")
            tips.append("保持身体核心稳定，避免受伤")
        elif level == 'high':
            tips.append("保持身体平衡，注意重心控制")
            tips.append("利用手臂和躯干保持稳定")
        
        if accent == 'strong':
            tips.append("强调动作的爆发力和节奏感")
            tips.append("注意动作的起始和结束点")
        elif accent == 'weak':
            tips.append("保持动作的细腻和连贯性")
            tips.append("注重动作的质感和流动性")
        
        # 根据舞蹈风格添加特定建议
        if dance_style == 'Hip-Hop':
            tips.append("注重身体的isolation和bounce感")
            tips.append("保持groove和swag的感觉")
        elif dance_style == 'House':
            tips.append("保持groove和flow的连续性")
            tips.append("注重脚步的复杂性和流畅性")
        elif dance_style == 'K-pop':
            tips.append("注意动作的精确性和同步性")
            tips.append("保持表情和表现力")
        elif dance_style == 'Jazz':
            tips.append("注重动作的线条和延伸感")
            tips.append("保持优雅和表现力")
        
        # 根据音频特征添加建议
        if features.get('essentia_available', False):
            essentia_features = features.get('essentia_features', {})
            if essentia_features.get('pitch_std', 0) > 0.5:
                tips.append("注意音高变化，动作要有层次感")
        
        return tips
    
    def _assess_difficulty_pro(self, segment: Dict) -> str:
        """专业级难度评估"""
        moves = segment.get('moves', [])
        level = segment.get('level', 'mid')
        transition = segment.get('transition', 'quarter-turn')
        
        difficulty_score = 0
        
        # 根据动作复杂度评分
        complex_moves = ['windmill', 'headspin', 'flare', 'turtle', 'cricket', 'airflare']
        intermediate_moves = ['spin', 'turn', 'jump', 'leap', 'slide', 'freeze']
        
        for move in moves:
            if any(complex_move in move.lower() for complex_move in complex_moves):
                difficulty_score += 4
            elif any(intermediate_move in move.lower() for intermediate_move in intermediate_moves):
                difficulty_score += 2
            else:
                difficulty_score += 1
        
        # 根据层次评分
        if level == 'floor':
            difficulty_score += 3
        elif level == 'high':
            difficulty_score += 2
        
        # 根据过渡复杂度评分
        complex_transitions = ['full_turn', 'spin', 'level_drop', 'travel_diagonal', 'air_step']
        if any(complex_transition in transition for complex_transition in complex_transitions):
            difficulty_score += 3
        
        # 转换为难度等级
        if difficulty_score <= 4:
            return "初级"
        elif difficulty_score <= 8:
            return "中级"
        elif difficulty_score <= 12:
            return "高级"
        else:
            return "专业级"
    
    def _assess_energy_level_pro(self, segment: Dict) -> str:
        """专业级能量评估"""
        accent = segment.get('accent', 'medium')
        moves = segment.get('moves', [])
        
        energy_score = 0
        
        # 根据重音评分
        if accent == 'strong':
            energy_score += 4
        elif accent == 'medium':
            energy_score += 2
        else:
            energy_score += 1
        
        # 根据动作类型评分
        high_energy_moves = ['jump', 'leap', 'bounce', 'pop', 'hit', 'punch', 'explosive']
        medium_energy_moves = ['run', 'fast', 'quick', 'dynamic']
        
        for move in moves:
            if any(energy_move in move.lower() for energy_move in high_energy_moves):
                energy_score += 3
            elif any(energy_move in move.lower() for energy_move in medium_energy_moves):
                energy_score += 1
        
        # 转换为能量等级
        if energy_score <= 3:
            return "低能量"
        elif energy_score <= 6:
            return "中等能量"
        elif energy_score <= 9:
            return "高能量"
        else:
            return "超高能量"
    
    def _generate_technical_points(self, segment: Dict, dance_style: str) -> List[str]:
        """生成技术要点"""
        technical_points = []
        
        moves = segment.get('moves', [])
        level = segment.get('level', 'mid')
        
        # 通用技术要点
        if level == 'floor':
            technical_points.append("保持身体核心稳定")
            technical_points.append("注意手腕和膝盖的保护")
        
        # 根据舞蹈风格的技术要点
        if dance_style == 'Hip-Hop':
            technical_points.append("保持身体的isolation")
            technical_points.append("注重rhythm和groove")
        elif dance_style == 'House':
            technical_points.append("保持脚步的灵活性")
            technical_points.append("注重身体的flow")
        elif dance_style == 'K-pop':
            technical_points.append("保持动作的精确性")
            technical_points.append("注重团队同步")
        
        return technical_points
    
    def _generate_global_advice_pro(self, choreography: Dict, dance_style: str, features: Dict) -> Dict:
        """生成专业级全局建议"""
        global_cues = choreography.get('global_cues', {})
        segments = choreography.get('segments', [])
        
        # 分析整体特征
        total_segments = len(segments)
        energy_levels = [seg.get('energy_level', '中等能量') for seg in segments]
        difficulty_levels = [seg.get('difficulty', '中级') for seg in segments]
        
        # 生成专业建议
        advice = {
            'overall_style': f"整体{dance_style}风格，共{total_segments}个8拍片段",
            'energy_flow': f"能量变化: {' → '.join(energy_levels[:5])}{'...' if len(energy_levels) > 5 else ''}",
            'difficulty_progression': f"难度递进: {' → '.join(difficulty_levels[:5])}{'...' if len(difficulty_levels) > 5 else ''}",
            'key_focus': global_cues.get('key_characteristics', ['节奏感', '表现力']),
            'practice_tips': [
                "先练习单个动作，再组合成片段",
                "注意动作之间的过渡和连接",
                "保持音乐的节拍感和律动",
                "根据个人能力调整动作幅度",
                "注重动作的质感和表现力"
            ],
            'professional_notes': [
                "建议分段练习，逐步提高难度",
                "注意动作的起始和结束点",
                "保持身体的稳定性和控制力",
                "注重与音乐的完美配合"
            ]
        }
        
        return advice
    
    def _generate_professional_analysis(self, features: Dict, dance_style: str) -> Dict:
        """生成专业分析信息"""
        analysis = {
            'audio_analysis': {
                'bpm': features.get('tempo', 120),
                'tempo_confidence': features.get('tempo_confidence', 0.5),
                'energy_level': features.get('energy', 0.5),
                'complexity': features.get('spectral_centroid_std', 0.5)
            },
            'style_analysis': {
                'detected_style': dance_style,
                'style_confidence': features.get('style_features', {}).get('style_confidence', 0.5),
                'mood': features.get('mood_features', {}).get('mood', 'neutral'),
                'valence': features.get('mood_features', {}).get('valence', 0.5)
            },
            'technical_analysis': {
                'advanced_libraries_used': {
                    'madmom': features.get('madmom_available', False),
                    'essentia': features.get('essentia_available', False),
                    'musicnn': features.get('musicnn_available', False)
                },
                'analysis_quality': 'professional' if any([
                    features.get('madmom_available', False),
                    features.get('essentia_available', False),
                    features.get('musicnn_available', False)
                ]) else 'standard'
            }
        }
        
        return analysis
    
    def _update_recent_actions(self, choreography: Dict):
        """更新最近使用的动作记录"""
        segments = choreography.get('segments', [])
        
        for segment in segments:
            moves = segment.get('moves', [])
            for move in moves:
                if move not in self.recent_actions:
                    self.recent_actions.append(move)
        
        # 保持最近动作列表的长度
        if len(self.recent_actions) > self.max_recent_actions:
            self.recent_actions = self.recent_actions[-self.max_recent_actions:]
    
    def get_action_database_info(self) -> Dict:
        """获取动作数据库信息"""
        return {
            'available_styles': ['Hip-Hop', 'House', 'K-pop', 'Jazz', 'Contemporary', 'Breaking'],
            'action_dimensions': get_action_dimensions(),
            'recent_actions_count': len(self.recent_actions),
            'recent_actions': self.recent_actions[-10:] if self.recent_actions else [],
            'advanced_libraries': {
                'madmom': True,
                'essentia': True,
                'musicnn': True
            }
        }
