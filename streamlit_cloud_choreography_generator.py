"""
Streamlit Cloud兼容的增强编舞生成器
使用基础库实现专业级编舞生成功能
"""

import os
import tempfile
from typing import Dict, List, Any
from streamlit_cloud_audio_analyzer import StreamlitCloudAudioAnalyzer
from enhanced_llm_choreographer import EnhancedLLMChoreographer
from action_database import get_action_candidates, get_action_dimensions
import json

class StreamlitCloudChoreographyGenerator:
    """Streamlit Cloud兼容的增强编舞生成器"""
    
    def __init__(self):
        self.audio_analyzer = StreamlitCloudAudioAnalyzer()
        self.llm_choreographer = EnhancedLLMChoreographer()
        self.recent_actions = []  # 记录最近使用的动作，用于避免重复
        self.max_recent_actions = 20  # 最多记录20个最近动作
    
    def generate_choreography_from_file(self, file_path: str) -> Dict:
        """从音频文件生成编舞"""
        print("🎵 开始增强编舞生成流程...")
        
        try:
            # 1. 增强音频分析
            print("📊 步骤1: 增强音频分析...")
            analysis_result = self.audio_analyzer.comprehensive_analysis(file_path)
            
            # 2. 提取关键信息
            audio_info = analysis_result['audio_info']
            features = analysis_result['features']
            segments = analysis_result['segments']
            dance_style = analysis_result['dance_style']
            
            print(f"🎭 检测到舞蹈风格: {dance_style}")
            print(f"📈 音频特征: BPM={float(audio_info['bpm']):.1f}, 时长={float(audio_info['duration']):.1f}s")
            
            # 3. 生成编舞
            print("🎨 步骤2: 生成结构化编舞...")
            choreography = self.llm_choreographer.generate_enhanced_choreography(
                audio_features=features,
                segments=segments,
                dance_style=dance_style,
                avoid_actions=self.recent_actions
            )
            
            # 4. 后处理和增强
            print("✨ 步骤3: 后处理和增强...")
            enhanced_choreography = self._enhance_choreography_output(
                choreography, segments, dance_style
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
                'generation_method': 'enhanced_structured_streamlit_cloud'
            }
            
            print("🎉 增强编舞生成完成！")
            return result
            
        except Exception as e:
            print(f"❌ 生成编舞时出错: {e}")
            raise e
    
    def _enhance_choreography_output(self, choreography: Dict, 
                                   segments: List[Dict], 
                                   dance_style: str) -> Dict:
        """增强编舞输出"""
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
                
                # 添加教学建议
                segment['teaching_tips'] = self._generate_teaching_tips(
                    segment, dance_style
                )
                
                # 添加难度评估
                segment['difficulty'] = self._assess_difficulty(segment)
                
                # 添加能量等级
                segment['energy_level'] = self._assess_energy_level(segment)
        
        # 添加全局建议
        enhanced['global_advice'] = self._generate_global_advice(
            enhanced, dance_style
        )
        
        return enhanced
    
    def _generate_teaching_tips(self, segment: Dict, dance_style: str) -> List[str]:
        """生成教学建议"""
        tips = []
        
        # 根据动作类型生成建议
        moves = segment.get('moves', [])
        level = segment.get('level', 'mid')
        accent = segment.get('accent', 'medium')
        
        if level == 'floor':
            tips.append("注意地板动作的安全性和流畅性")
        elif level == 'high':
            tips.append("保持身体平衡，注意重心控制")
        
        if accent == 'strong':
            tips.append("强调动作的爆发力和节奏感")
        elif accent == 'weak':
            tips.append("保持动作的细腻和连贯性")
        
        # 根据舞蹈风格添加特定建议
        if dance_style == 'Hip-Hop':
            tips.append("注重身体的isolation和bounce感")
        elif dance_style == 'House':
            tips.append("保持groove和flow的连续性")
        elif dance_style == 'K-pop':
            tips.append("注意动作的精确性和同步性")
        
        return tips
    
    def _assess_difficulty(self, segment: Dict) -> str:
        """评估动作难度"""
        moves = segment.get('moves', [])
        level = segment.get('level', 'mid')
        transition = segment.get('transition', 'quarter-turn')
        
        difficulty_score = 0
        
        # 根据动作复杂度评分
        complex_moves = ['windmill', 'headspin', 'flare', 'turtle', 'cricket']
        for move in moves:
            if any(complex_move in move.lower() for complex_move in complex_moves):
                difficulty_score += 3
            elif any(keyword in move.lower() for keyword in ['spin', 'turn', 'jump', 'leap']):
                difficulty_score += 2
            else:
                difficulty_score += 1
        
        # 根据层次评分
        if level == 'floor':
            difficulty_score += 2
        elif level == 'high':
            difficulty_score += 1
        
        # 根据过渡复杂度评分
        complex_transitions = ['full_turn', 'spin', 'level_drop', 'travel_diagonal']
        if any(complex_transition in transition for complex_transition in complex_transitions):
            difficulty_score += 2
        
        # 转换为难度等级
        if difficulty_score <= 3:
            return "初级"
        elif difficulty_score <= 6:
            return "中级"
        else:
            return "高级"
    
    def _assess_energy_level(self, segment: Dict) -> str:
        """评估能量等级"""
        accent = segment.get('accent', 'medium')
        moves = segment.get('moves', [])
        
        energy_score = 0
        
        # 根据重音评分
        if accent == 'strong':
            energy_score += 3
        elif accent == 'medium':
            energy_score += 2
        else:
            energy_score += 1
        
        # 根据动作类型评分
        high_energy_moves = ['jump', 'leap', 'bounce', 'pop', 'hit', 'punch']
        for move in moves:
            if any(energy_move in move.lower() for energy_move in high_energy_moves):
                energy_score += 2
            elif any(keyword in move.lower() for keyword in ['run', 'fast', 'quick']):
                energy_score += 1
        
        # 转换为能量等级
        if energy_score <= 2:
            return "低能量"
        elif energy_score <= 4:
            return "中等能量"
        else:
            return "高能量"
    
    def _generate_global_advice(self, choreography: Dict, dance_style: str) -> Dict:
        """生成全局建议"""
        global_cues = choreography.get('global_cues', {})
        segments = choreography.get('segments', [])
        
        # 分析整体特征
        total_segments = len(segments)
        energy_levels = [seg.get('energy_level', '中等能量') for seg in segments]
        difficulty_levels = [seg.get('difficulty', '中级') for seg in segments]
        
        # 生成建议
        advice = {
            'overall_style': f"整体{dance_style}风格，共{total_segments}个8拍片段",
            'energy_flow': f"能量变化: {' → '.join(energy_levels[:5])}{'...' if len(energy_levels) > 5 else ''}",
            'difficulty_progression': f"难度递进: {' → '.join(difficulty_levels[:5])}{'...' if len(difficulty_levels) > 5 else ''}",
            'key_focus': global_cues.get('key_characteristics', ['节奏感', '表现力']),
            'practice_tips': [
                "先练习单个动作，再组合成片段",
                "注意动作之间的过渡和连接",
                "保持音乐的节拍感和律动",
                "根据个人能力调整动作幅度"
            ]
        }
        
        return advice
    
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
            'recent_actions': self.recent_actions[-10:] if self.recent_actions else []
        }
