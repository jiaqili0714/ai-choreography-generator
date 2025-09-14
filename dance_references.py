"""
舞蹈参考视频数据库 - 增强版
包含经典舞蹈动作的真实视频链接和描述
"""

DANCE_REFERENCES = {
    "Hip-Hop": {
        "基础动作": [
            {
                "name": "Harlem Shake",
                "description": "经典的头部和肩膀摇摆动作",
                "search_terms": ["Harlem Shake dance tutorial", "Harlem Shake original", "Harlem Shake how to"],
                "difficulty": 2,
                "energy_level": 4
            },
            {
                "name": "Running Man",
                "description": "经典的跑步动作，适合节拍感建立",
                "search_terms": ["Running Man dance tutorial", "Running Man hip hop", "Running Man dance move"],
                "difficulty": 3,
                "energy_level": 4
            },
            {
                "name": "Cabbage Patch",
                "description": "手臂和身体的协调动作",
                "search_terms": ["Cabbage Patch dance", "Cabbage Patch tutorial", "Hip hop cabbage patch"],
                "difficulty": 2,
                "energy_level": 3
            }
        ],
        "进阶动作": [
            {
                "name": "Freeze",
                "description": "突然停止的定格动作",
                "search_terms": ["Freeze dance tutorial", "Hip hop freeze moves", "Breakdance freeze"],
                "difficulty": 4,
                "energy_level": 5
            },
            {
                "name": "Slide",
                "description": "滑步动作，需要良好的平衡感",
                "search_terms": ["Slide dance tutorial", "Hip hop slide moves", "Dance slide technique"],
                "difficulty": 4,
                "energy_level": 4
            }
        ]
    },
    
    "Jazz": {
        "基础动作": [
            {
                "name": "Jazz Square",
                "description": "经典的爵士舞方形步伐",
                "search_terms": ["Jazz Square dance tutorial", "Jazz dance basics", "Jazz Square steps"],
                "difficulty": 2,
                "energy_level": 3
            },
            {
                "name": "Pirouette",
                "description": "单脚旋转动作",
                "search_terms": ["Pirouette tutorial", "Jazz pirouette", "Dance turn tutorial"],
                "difficulty": 3,
                "energy_level": 3
            }
        ],
        "进阶动作": [
            {
                "name": "Grand Jeté",
                "description": "大跳跃动作",
                "search_terms": ["Grand Jete tutorial", "Jazz leap tutorial", "Dance jump tutorial"],
                "difficulty": 5,
                "energy_level": 5
            }
        ]
    },
    
    "K-pop": {
        "基础动作": [
            {
                "name": "Point Dance",
                "description": "经典的指向性动作",
                "search_terms": ["K-pop point dance tutorial", "K-pop choreography", "K-pop dance moves"],
                "difficulty": 2,
                "energy_level": 4
            },
            {
                "name": "Wave",
                "description": "波浪形身体动作",
                "search_terms": ["K-pop wave tutorial", "K-pop body wave", "Dance wave tutorial"],
                "difficulty": 3,
                "energy_level": 3
            }
        ],
        "进阶动作": [
            {
                "name": "Isolation",
                "description": "身体部位独立运动",
                "search_terms": ["K-pop isolation tutorial", "Body isolation dance", "Dance isolation technique"],
                "difficulty": 4,
                "energy_level": 4
            }
        ]
    },
    
    "House": {
        "基础动作": [
            {
                "name": "Jacking",
                "description": "House舞的基础动作",
                "search_terms": ["House jacking tutorial", "House dance basics", "Jacking dance move"],
                "difficulty": 3,
                "energy_level": 4
            },
            {
                "name": "Footwork",
                "description": "复杂的脚步动作",
                "search_terms": ["House footwork tutorial", "House dance footwork", "Dance footwork basics"],
                "difficulty": 4,
                "energy_level": 4
            }
        ]
    },
    
    "Breaking": {
        "基础动作": [
            {
                "name": "Toprock",
                "description": "Breaking的站立部分",
                "search_terms": ["Toprock tutorial", "Breakdance toprock", "Breaking basics"],
                "difficulty": 3,
                "energy_level": 4
            },
            {
                "name": "Six Step",
                "description": "经典的地面动作",
                "search_terms": ["Six Step tutorial", "Breakdance six step", "Breaking footwork"],
                "difficulty": 4,
                "energy_level": 4
            }
        ],
        "进阶动作": [
            {
                "name": "Windmill",
                "description": "风车动作",
                "search_terms": ["Windmill tutorial", "Breakdance windmill", "Breaking power moves"],
                "difficulty": 5,
                "energy_level": 5
            }
        ]
    }
}

def get_dance_references(dance_style, difficulty_level="基础动作"):
    """获取指定舞蹈风格和难度级别的参考视频"""
    if dance_style not in DANCE_REFERENCES:
        return []
    
    style_refs = DANCE_REFERENCES[dance_style]
    if difficulty_level not in style_refs:
        return []
    
    return style_refs[difficulty_level]

def get_random_reference(dance_style, difficulty_level="基础动作"):
    """随机获取一个参考视频"""
    import random
    references = get_dance_references(dance_style, difficulty_level)
    if references:
        return random.choice(references)
    return None

def format_reference_for_prompt(reference):
    """将参考视频信息格式化为提示词"""
    if not reference:
        return ""
    
    return f"""
参考动作: {reference['name']}
描述: {reference['description']}
搜索关键词: {', '.join(reference['search_terms'])}
难度: {reference['difficulty']}/5
能量: {reference['energy_level']}/5
"""

def get_youtube_search_url(dance_style, move_name):
    """生成YouTube搜索URL"""
    # 查找对应的参考信息
    for difficulty in ["基础动作", "进阶动作"]:
        references = get_dance_references(dance_style, difficulty)
        for ref in references:
            if ref['name'] == move_name:
                # 使用第一个搜索词生成URL
                search_term = ref['search_terms'][0].replace(' ', '+')
                return f"https://www.youtube.com/results?search_query={search_term}"
    
    # 如果没有找到，返回通用搜索URL
    search_term = f"{move_name}+{dance_style}+dance+tutorial".replace(' ', '+')
    return f"https://www.youtube.com/results?search_query={search_term}"

def get_video_search_suggestions(dance_style, move_name):
    """获取视频搜索建议"""
    # 查找对应的参考信息
    for difficulty in ["基础动作", "进阶动作"]:
        references = get_dance_references(dance_style, difficulty)
        for ref in references:
            if ref['name'] == move_name:
                return f"在YouTube搜索: {', '.join(ref['search_terms'])}"
    
    # 如果没有找到，返回通用搜索建议
    return f"在YouTube搜索: '{move_name} {dance_style} dance tutorial'"

def get_all_search_terms(dance_style, move_name):
    """获取所有搜索词"""
    # 查找对应的参考信息
    for difficulty in ["基础动作", "进阶动作"]:
        references = get_dance_references(dance_style, difficulty)
        for ref in references:
            if ref['name'] == move_name:
                return ref['search_terms']
    
    # 如果没有找到，返回通用搜索词
    return [f"{move_name} {dance_style} dance tutorial"]
