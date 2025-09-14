"""
增强LLM编舞生成器
实现结构化输出、多样性控制、Few-shot示例和动作词库集成
"""

import openai
import json
import jsonschema
import os
from typing import List, Dict, Any, Optional
import config
from action_database import get_action_candidates, get_synonym_replacement, create_rhythm_placeholder
import random

class EnhancedLLMChoreographer:
    """增强LLM编舞生成器"""
    
    def __init__(self):
        # 动态获取API密钥
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("请设置OPENAI_API_KEY环境变量")
        
        self.client = openai.OpenAI(api_key=api_key)
        
        # JSON Schema定义
        self.choreography_schema = {
            "type": "object",
            "properties": {
                "style": {"type": "string"},
                "global_cues": {
                    "type": "object",
                    "properties": {
                        "energy_level": {"type": "string", "enum": ["low", "medium", "high", "very_high"]},
                        "mood": {"type": "string"},
                        "key_characteristics": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["energy_level", "mood", "key_characteristics"]
                },
                "segments": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "idx": {"type": "integer"},
                            "time": {"type": "string"},
                            "accent": {"type": "string", "enum": ["strong", "medium", "weak"]},
                            "level": {"type": "string", "enum": ["high", "mid", "low", "floor"]},
                            "plane": {"type": "string", "enum": ["frontal", "sagittal", "transverse"]},
                            "motifs": {"type": "array", "items": {"type": "string"}},
                            "moves": {"type": "array", "items": {"type": "string"}},
                            "transition": {"type": "string"}
                        },
                        "required": ["idx", "time", "accent", "level", "plane", "motifs", "moves", "transition"]
                    }
                }
            },
            "required": ["style", "global_cues", "segments"]
        }
        
        # Few-shot示例
        self.few_shot_examples = [
            {
                "style": "Hip-Hop",
                "global_cues": {
                    "energy_level": "high",
                    "mood": "aggressive and confident",
                    "key_characteristics": ["bounce", "isolation", "rhythmic precision"]
                },
                "segments": [
                    {
                        "idx": 0,
                        "time": "0:00-0:16",
                        "accent": "strong",
                        "level": "mid",
                        "plane": "frontal",
                        "motifs": ["bounce", "rock"],
                        "moves": ["two-step", "chest-pop", "shoulder-roll", "freeze"],
                        "transition": "quarter-turn"
                    },
                    {
                        "idx": 1,
                        "time": "0:16-0:32",
                        "accent": "medium",
                        "level": "low",
                        "plane": "sagittal",
                        "motifs": ["groove", "sway"],
                        "moves": ["running-man", "body-wave", "hip-roll", "level-drop"],
                        "transition": "travel-diagonal"
                    }
                ]
            },
            {
                "style": "House",
                "global_cues": {
                    "energy_level": "medium",
                    "mood": "smooth and flowing",
                    "key_characteristics": ["groove", "flow", "smooth transitions"]
                },
                "segments": [
                    {
                        "idx": 0,
                        "time": "0:00-0:16",
                        "accent": "medium",
                        "level": "mid",
                        "plane": "transverse",
                        "motifs": ["groove", "sway"],
                        "moves": ["jack", "skate", "lofting", "shuffle"],
                        "transition": "smooth-transition"
                    },
                    {
                        "idx": 1,
                        "time": "0:16-0:32",
                        "accent": "weak",
                        "level": "high",
                        "plane": "frontal",
                        "motifs": ["flow", "liquid"],
                        "moves": ["vogue", "waacking", "liquid", "tutting"],
                        "transition": "flow-transition"
                    }
                ]
            }
        ]
    
    def _call_openai_enhanced(self, messages: List[Dict], max_tokens: int = 1000, 
                            temperature: float = 0.9, presence_penalty: float = 0.6, 
                            frequency_penalty: float = 0.4) -> str:
        """增强的OpenAI API调用"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                presence_penalty=presence_penalty,
                frequency_penalty=frequency_penalty
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"❌ API调用失败: {e}")
            raise e
    
    def _clean_json_response(self, content: str) -> str:
        """清理JSON响应"""
        import re
        
        # 移除markdown代码块标记
        content = re.sub(r'```json\s*', '', content)
        content = re.sub(r'```\s*$', '', content)
        content = content.strip()
        
        # 如果内容以```开头，移除它
        if content.startswith('```'):
            content = content[3:]
        if content.endswith('```'):
            content = content[:-3]
        
        return content.strip()
    
    def _validate_json_schema(self, json_data: Dict) -> bool:
        """验证JSON Schema"""
        try:
            jsonschema.validate(json_data, self.choreography_schema)
            return True
        except jsonschema.ValidationError as e:
            print(f"❌ JSON Schema验证失败: {e}")
            return False
    
    def _apply_synonym_replacement(self, moves: List[str]) -> List[str]:
        """应用同义词替换"""
        return [get_synonym_replacement(move) for move in moves]
    
    def _add_rhythm_placeholders(self, moves: List[str]) -> str:
        """添加节奏占位符"""
        return create_rhythm_placeholder(moves)
    
    def generate_enhanced_choreography(self, audio_features: Dict, 
                                     segments: List[Dict], 
                                     dance_style: str,
                                     avoid_actions: List[str] = None) -> Dict:
        """生成增强编舞"""
        if avoid_actions is None:
            avoid_actions = []
        
        print(f"🎭 开始生成{dance_style}风格编舞...")
        
        # 获取候选动作
        action_candidates = get_action_candidates(dance_style, num_candidates=15, avoid_actions=avoid_actions)
        
        # 构建Few-shot示例字符串
        examples_str = "\n\n".join([json.dumps(example, ensure_ascii=False, indent=2) 
                                   for example in self.few_shot_examples])
        
        # 构建系统提示
        system_prompt = f"""你是一个专业的编舞师，擅长{dance_style}风格。请根据音频特征生成结构化的编舞建议。

要求：
1. 输出必须是有效的JSON格式，严格遵循提供的schema
2. 使用丰富的动作词汇，避免重复
3. 考虑动作的层次、方向和动态变化
4. 每个片段包含4-6个具体动作
5. 动作要符合{dance_style}风格特点

候选动作池：{', '.join(action_candidates)}
需避免动作：{', '.join(avoid_actions) if avoid_actions else '无'}

Few-shot示例：
{examples_str}

请严格按照以下JSON Schema输出："""

        # 构建用户提示
        user_prompt = f"""音频特征分析：
- BPM: {audio_features.get('bpm', 120):.1f}
- 能量等级: {audio_features.get('energy_level', 'medium')}
- 舞蹈风格: {dance_style}
- 片段数量: {len(segments)}

请为每个片段生成详细的编舞建议，包含：
- 动作层次变化 (high/mid/low/floor)
- 空间平面 (frontal/sagittal/transverse)  
- 动态变化 (strong/medium/weak accent)
- 具体动作组合
- 过渡方式

确保动作多样性和{dance_style}风格特色。"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        # 调用API
        try:
            response = self._call_openai_enhanced(messages, max_tokens=1200, temperature=0.9)
            cleaned_response = self._clean_json_response(response)
            
            # 解析JSON
            try:
                choreography_data = json.loads(cleaned_response)
            except json.JSONDecodeError as e:
                print(f"❌ JSON解析失败: {e}")
                print(f"原始内容: {cleaned_response}")
                return self._generate_fallback_choreography(segments, dance_style, action_candidates)
            
            # 验证Schema
            if not self._validate_json_schema(choreography_data):
                print("⚠️ Schema验证失败，使用备用方案")
                return self._generate_fallback_choreography(segments, dance_style, action_candidates)
            
            # 后处理：同义词替换和节奏占位
            for segment in choreography_data.get('segments', []):
                if 'moves' in segment:
                    # 应用同义词替换
                    segment['moves'] = self._apply_synonym_replacement(segment['moves'])
                    # 添加节奏占位
                    segment['rhythm_breakdown'] = self._add_rhythm_placeholders(segment['moves'])
            
            print("✅ 增强编舞生成成功！")
            return choreography_data
            
        except Exception as e:
            print(f"❌ 生成编舞时出错: {e}")
            return self._generate_fallback_choreography(segments, dance_style, action_candidates)
    
    def _generate_fallback_choreography(self, segments: List[Dict], 
                                      dance_style: str, 
                                      action_candidates: List[str]) -> Dict:
        """生成备用编舞方案"""
        print("🔄 使用备用编舞方案...")
        
        fallback_segments = []
        for i, segment in enumerate(segments):
            # 随机选择动作
            selected_moves = random.sample(action_candidates, min(4, len(action_candidates)))
            
            # 应用同义词替换
            enhanced_moves = self._apply_synonym_replacement(selected_moves)
            
            fallback_segment = {
                "idx": i,
                "time": f"{segment['start_time']:.1f}s-{segment['end_time']:.1f}s",
                "accent": random.choice(["strong", "medium", "weak"]),
                "level": random.choice(["high", "mid", "low", "floor"]),
                "plane": random.choice(["frontal", "sagittal", "transverse"]),
                "motifs": [random.choice(["groove", "bounce", "flow", "hit"])],
                "moves": enhanced_moves,
                "transition": random.choice(["quarter-turn", "level-drop", "travel-diagonal"]),
                "rhythm_breakdown": self._add_rhythm_placeholders(enhanced_moves)
            }
            fallback_segments.append(fallback_segment)
        
        return {
            "style": dance_style,
            "global_cues": {
                "energy_level": "medium",
                "mood": f"dynamic {dance_style.lower()} style",
                "key_characteristics": ["rhythmic", "expressive", "structured"]
            },
            "segments": fallback_segments
        }
    
    def generate_segment_choreography(self, segment_features: Dict, 
                                    dance_style: str, 
                                    action_candidates: List[str],
                                    avoid_actions: List[str] = None) -> Dict:
        """生成单个片段的编舞"""
        if avoid_actions is None:
            avoid_actions = []
        
        # 根据片段特征调整动作选择
        energy = segment_features.get('energy', 0.5)
        tempo = segment_features.get('tempo', 120)
        
        # 根据能量和节拍调整动作类型
        if energy > 0.7:
            accent = "strong"
            level = random.choice(["high", "mid"])
        elif energy < 0.3:
            accent = "weak"
            level = random.choice(["low", "floor"])
        else:
            accent = "medium"
            level = "mid"
        
        # 选择动作
        available_actions = [action for action in action_candidates if action not in avoid_actions]
        selected_moves = random.sample(available_actions, min(4, len(available_actions)))
        
        # 应用同义词替换
        enhanced_moves = self._apply_synonym_replacement(selected_moves)
        
        return {
            "accent": accent,
            "level": level,
            "plane": random.choice(["frontal", "sagittal", "transverse"]),
            "motifs": [random.choice(["groove", "bounce", "flow", "hit"])],
            "moves": enhanced_moves,
            "transition": random.choice(["quarter-turn", "level-drop", "travel-diagonal"]),
            "rhythm_breakdown": self._add_rhythm_placeholders(enhanced_moves)
        }
