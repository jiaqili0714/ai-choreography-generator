import openai
from typing import List, Dict, Any
import json
import config
import re
from dance_references import get_random_reference, format_reference_for_prompt

class LLMChoreographer:
    """LLM编舞生成器，使用GPT生成舞蹈动作建议 - 增强版"""
    
    def __init__(self):
        if not config.OPENAI_API_KEY:
            raise ValueError("请设置OPENAI_API_KEY环境变量")
        
        # 使用新版本OpenAI API (1.0.0+)
        self.client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
        print(f"🔧 LLMChoreographer初始化完成，使用增强版舞蹈参考系统")
    
    def _call_openai(self, messages, max_tokens=100, temperature=0.7):
        """统一的OpenAI API调用方法"""
        print(f"📞 调用OpenAI API，消息数量: {len(messages)}")
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            result = response.choices[0].message.content.strip()
            print(f"✅ API调用成功，响应长度: {len(result)}")
            return result
        except Exception as e:
            print(f"❌ API调用失败: {e}")
            raise e
    
    def _clean_json_response(self, content):
        """清理JSON响应，移除markdown标记"""
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
    
    def generate_choreography_style(self, bpm: float, audio_features: Dict[str, Any]) -> str:
        """根据BPM和音频特征推荐舞蹈风格"""
        print(f"🎨 生成舞蹈风格推荐，BPM: {bpm}")
        
        prompt = f"""作为专业的编舞师，请根据以下音乐特征推荐最适合的舞蹈风格：

BPM: {bpm}
音频特征:
- 频谱重心: {audio_features.get('spectral_centroid_mean', 0):.2f}
- 能量: {audio_features.get('energy_mean', 0):.2f}
- 频谱滚降: {audio_features.get('spectral_rolloff_mean', 0):.2f}

可选舞蹈风格: {', '.join(config.DANCE_STYLES)}

请只返回一个最推荐的舞蹈风格名称，不要其他解释。"""
        
        try:
            result = self._call_openai([{"role": "user", "content": prompt}], max_tokens=50)
            print(f"🎭 推荐舞蹈风格: {result}")
            return result
        except Exception as e:
            print(f"❌ 生成舞蹈风格时出错: {e}")
            return "Hip-Hop"
    
    def generate_segment_choreography(self, segment: Dict[str, Any], bpm: float, 
                                    dance_style: str, segment_index: int, audio_features: Dict[str, Any] = None) -> Dict[str, Any]:
        """为单个8拍片段生成舞蹈动作"""
        print(f"💃 生成第{segment_index + 1}段编舞，风格: {dance_style}")
        
        # 根据BPM和片段索引选择难度级别
        if bpm > 140 or segment_index > 2:
            difficulty_level = "进阶动作"
        else:
            difficulty_level = "基础动作"
        
        # 获取舞蹈参考
        reference = get_random_reference(dance_style, difficulty_level)
        reference_text = format_reference_for_prompt(reference) if reference else ""
        
        # 计算节拍间隔
        beat_interval = 60.0 / bpm
        segment_beats = segment['beat_count']
        
        # 分析音乐特征
        if audio_features is None:
            audio_features = {}
        energy_level = "高" if audio_features.get('energy_mean', 0) > 0.3 else "中" if audio_features.get('energy_mean', 0) > 0.15 else "低"
        tempo_feel = "很快" if bpm > 140 else "快" if bpm > 120 else "中等" if bpm > 100 else "慢"
        
        prompt = f"""作为专业编舞师，请为以下音乐片段设计简洁实用的舞蹈动作：

音乐特征:
- BPM: {bpm} ({tempo_feel}节奏)
- 能量: {energy_level}
- 舞蹈风格: {dance_style}
- 节拍数: {segment_beats}

{reference_text}

请分析音乐特点并给出简洁的舞蹈建议，要求：

1. **节奏要点**: 分析这段音乐的特点（如：节奏很快、气氛燥、需要力度大、有低音bass三连音等）
2. **舞蹈元素**: 推荐3-5个适配的舞蹈动作元素
3. **关键提示**: 1-2个最重要的技术要点

请直接返回JSON格式，不要使用markdown代码块标记，包含以下字段：
- "rhythm_analysis": 节奏分析，如"节奏很快，气氛燥，需要力度大，低音bass有三连音"
- "dance_elements": 推荐的舞蹈元素列表，如["Harlem Shake", "Running Man", "Freeze"]
- "key_tips": 关键提示，如"动作要卡在bass上，力度要大"
- "difficulty": 难度等级(1-5)
- "energy_level": 能量等级(1-5)
- "reference_moves": 参考的经典动作名称列表"""
        
        try:
            content = self._call_openai([{"role": "user", "content": prompt}], max_tokens=800, temperature=0.8)
            print(f"📝 API返回内容: {content[:100]}...")
            
            # 清理JSON响应
            cleaned_content = self._clean_json_response(content)
            print(f"🧹 清理后内容: {cleaned_content[:100]}...")
            
            # 尝试解析JSON响应
            try:
                choreography = json.loads(cleaned_content)
                print(f"✅ JSON解析成功")
                
                # 确保包含参考视频信息
                if reference:
                    if "reference_moves" not in choreography:
                        choreography["reference_moves"] = [reference["name"]]
                
                return choreography
            except json.JSONDecodeError as je:
                print(f"⚠️ JSON解析失败: {je}")
                print(f"清理后内容: {cleaned_content}")
                # 如果JSON解析失败，创建默认结构
                choreography = {
                    "rhythm_analysis": f"BPM {bpm}，{tempo_feel}节奏，{energy_level}能量",
                    "dance_elements": [reference["name"]] if reference else ["基础动作"],
                    "key_tips": "跟随节拍，保持身体协调",
                    "difficulty": reference["difficulty"] if reference else 3,
                    "energy_level": reference["energy_level"] if reference else 3,
                    "reference_moves": [reference["name"]] if reference else ["基础动作"]
                }
                print(f"🔄 使用默认结构")
                return choreography
            
        except Exception as e:
            print(f"❌ 生成片段编舞时出错: {e}")
            default_result = {
                "rhythm_analysis": f"BPM {bpm}，{tempo_feel}节奏，{energy_level}能量",
                "dance_elements": [reference["name"]] if reference else ["基础动作"],
                "key_tips": "跟随节拍，保持身体协调",
                "difficulty": reference["difficulty"] if reference else 3,
                "energy_level": reference["energy_level"] if reference else 3,
                "reference_moves": [reference["name"]] if reference else ["基础动作"]
            }
            print(f"🔄 返回默认结果")
            return default_result
    
    def generate_full_choreography(self, segments: List[Dict[str, Any]], 
                                 bpm: float, dance_style: str, audio_features: Dict[str, Any] = None) -> Dict[str, Any]:
        """生成完整的编舞草稿"""
        print(f"🎭 开始生成{dance_style}风格的编舞，共{len(segments)}个片段...")
        
        segment_choreographies = []
        
        for i, segment in enumerate(segments):
            print(f"🔄 正在生成第{i+1}/{len(segments)}个片段的编舞...")
            choreography = self.generate_segment_choreography(segment, bpm, dance_style, i, audio_features)
            segment_choreographies.append(choreography)
        
        # 生成整体编舞总结
        summary_prompt = f"""请为以下编舞生成一个简洁的总结：

舞蹈风格: {dance_style}
BPM: {bpm}
总片段数: {len(segments)}
总时长: {segments[-1]['end_time']:.2f}秒

请提供：
1. 整体编舞风格描述
2. 难度评估
3. 适合的舞者水平
4. 练习建议
5. 推荐的参考视频

请以简洁的格式返回。"""
        
        try:
            summary = self._call_openai([{"role": "user", "content": summary_prompt}], max_tokens=250)
            print(f"📋 编舞总结生成成功")
        except Exception as e:
            print(f"❌ 生成编舞总结时出错: {e}")
            summary = f"这是一个{dance_style}风格的编舞，适合中等水平的舞者练习。"
        
        full_choreography = {
            "dance_style": dance_style,
            "bpm": bpm,
            "total_segments": len(segments),
            "total_duration": segments[-1]['end_time'],
            "summary": summary,
            "segments": segment_choreographies
        }
        
        print(f"🎉 编舞生成完成！")
        return full_choreography
