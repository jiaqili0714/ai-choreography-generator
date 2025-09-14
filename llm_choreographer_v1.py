import openai
from typing import List, Dict, Any
import json
import config

class LLMChoreographer:
    """LLM编舞生成器，使用GPT生成舞蹈动作建议"""
    
    def __init__(self):
        if not config.OPENAI_API_KEY:
            raise ValueError("请设置OPENAI_API_KEY环境变量")
        
        # 使用更安全的初始化方式
        try:
            self.client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
        except Exception as e:
            print(f"OpenAI客户端初始化失败: {e}")
            # 尝试使用旧版本API
            openai.api_key = config.OPENAI_API_KEY
            self.client = None
    
    def generate_choreography_style(self, bpm: float, audio_features: Dict[str, Any]) -> str:
        """
        根据BPM和音频特征推荐舞蹈风格
        """
        prompt = f"""
        作为专业的编舞师，请根据以下音乐特征推荐最适合的舞蹈风格：

        BPM: {bpm}
        音频特征:
        - 频谱重心: {audio_features.get('spectral_centroid_mean', 0):.2f}
        - 能量: {audio_features.get('energy_mean', 0):.2f}
        - 频谱滚降: {audio_features.get('spectral_rolloff_mean', 0):.2f}

        可选舞蹈风格: {', '.join(config.DANCE_STYLES)}

        请只返回一个最推荐的舞蹈风格名称，不要其他解释。
        """
        
        try:
            if self.client:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=50,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()
            else:
                # 使用旧版本API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=50,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"生成舞蹈风格时出错: {e}")
            return "Hip-Hop"  # 默认风格
    
    def generate_segment_choreography(self, segment: Dict[str, Any], bpm: float, 
                                    dance_style: str, segment_index: int) -> Dict[str, Any]:
        """
        为单个8拍片段生成舞蹈动作
        """
        prompt = f"""
        作为专业编舞师，请为以下音乐片段设计舞蹈动作：

        片段信息:
        - 片段编号: {segment_index + 1}
        - 时间范围: {segment['start_time']:.2f}s - {segment['end_time']:.2f}s
        - 持续时间: {segment['duration']:.2f}s
        - BPM: {bpm}
        - 舞蹈风格: {dance_style}
        - 节拍数: {segment['beat_count']}

        请为这个8拍片段设计具体的舞蹈动作，使用以下格式：
        1. 用文字描述主要动作
        2. 用emoji表示动作的视觉效果
        3. 考虑节拍和音乐节奏

        请以JSON格式返回，包含以下字段：
        - "description": 动作的文字描述
        - "emoji_sequence": emoji动作序列
        - "difficulty": 难度等级(1-5)
        - "energy_level": 能量等级(1-5)
        - "key_moves": 关键动作列表
        """
        
        try:
            if self.client:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=300,
                    temperature=0.8
                )
                content = response.choices[0].message.content.strip()
            else:
                # 使用旧版本API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=300,
                    temperature=0.8
                )
                content = response.choices[0].message.content.strip()
            
            # 尝试解析JSON响应
            try:
                choreography = json.loads(content)
            except json.JSONDecodeError:
                # 如果JSON解析失败，创建默认结构
                choreography = {
                    "description": content,
                    "emoji_sequence": "🕺💃🎵",
                    "difficulty": 3,
                    "energy_level": 3,
                    "key_moves": ["基础动作"]
                }
            
            return choreography
            
        except Exception as e:
            print(f"生成片段编舞时出错: {e}")
            return {
                "description": f"第{segment_index + 1}段：跟随节拍的基础动作",
                "emoji_sequence": "🕺💃🎵",
                "difficulty": 3,
                "energy_level": 3,
                "key_moves": ["基础动作"]
            }
    
    def generate_full_choreography(self, segments: List[Dict[str, Any]], 
                                 bpm: float, dance_style: str) -> Dict[str, Any]:
        """
        生成完整的编舞草稿
        """
        print(f"开始生成{dance_style}风格的编舞，共{len(segments)}个片段...")
        
        segment_choreographies = []
        
        for i, segment in enumerate(segments):
            print(f"正在生成第{i+1}/{len(segments)}个片段的编舞...")
            choreography = self.generate_segment_choreography(segment, bpm, dance_style, i)
            segment_choreographies.append(choreography)
        
        # 生成整体编舞总结
        summary_prompt = f"""
        请为以下编舞生成一个简洁的总结：

        舞蹈风格: {dance_style}
        BPM: {bpm}
        总片段数: {len(segments)}
        总时长: {segments[-1]['end_time']:.2f}秒

        请提供：
        1. 整体编舞风格描述
        2. 难度评估
        3. 适合的舞者水平
        4. 练习建议

        请以简洁的格式返回。
        """
        
        try:
            if self.client:
                summary_response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": summary_prompt}],
                    max_tokens=200,
                    temperature=0.7
                )
                summary = summary_response.choices[0].message.content.strip()
            else:
                # 使用旧版本API
                summary_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": summary_prompt}],
                    max_tokens=200,
                    temperature=0.7
                )
                summary = summary_response.choices[0].message.content.strip()
        except Exception as e:
            print(f"生成编舞总结时出错: {e}")
            summary = f"这是一个{dance_style}风格的编舞，适合中等水平的舞者练习。"
        
        full_choreography = {
            "dance_style": dance_style,
            "bpm": bpm,
            "total_segments": len(segments),
            "total_duration": segments[-1]['end_time'],
            "summary": summary,
            "segments": segment_choreographies
        }
        
        return full_choreography
