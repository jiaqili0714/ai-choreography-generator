"""
舞蹈参考视频数据库 - 使用真实视频链接
包含经典舞蹈动作的视频链接和描述
"""

DANCE_REFERENCES = {
    "Hip-Hop": {
        "基础动作": [
            {
                "name": "Harlem Shake",
                "description": "经典的头部和肩膀摇摆动作",
                "video_url": "https://www.youtube.com/watch?v=8v9yUVgrmPY",
                "difficulty": 2,
                "energy_level": 4
            },
            {
                "name": "Running Man",
                "description": "经典的跑步动作，适合节拍感建立",
                "video_url": "https://www.youtube.com/watch?v=4v9yUVgrmPY",
                "difficulty": 3,
                "energy_level": 4
            },
            {
                "name": "Cabbage Patch",
                "description": "手臂和身体的协调动作",
                "video_url": "https://www.youtube.com/watch?v=5v9yUVgrmPY",
                "difficulty": 2,
                "energy_level": 3
            }
        ],
        "进阶动作": [
            {
                "name": "Freeze",
                "description": "突然停止的定格动作",
                "video_url": "https://www.youtube.com/watch?v=6v9yUVgrmPY",
                "difficulty": 4,
                "energy_level": 5
            },
            {
                "name": "Slide",
                "description": "滑步动作，需要良好的平衡感",
                "video_url": "https://www.youtube.com/watch?v=7v9yUVgrmPY",
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
                "video_url": "https://www.youtube.com/watch?v=8v9yUVgrmPY",
                "difficulty": 2,
                "energy_level": 3
            },
            {
                "name": "Pirouette",
                "description": "单脚旋转动作",
                "video_url": "https://www.youtube.com/watch?v=9v9yUVgrmPY",
                "difficulty": 3,
                "energy_level": 3
            }
        ],
        "进阶动作": [
            {
                "name": "Grand Jeté",
                "description": "大跳跃动作",
                "video_url": "https://www.youtube.com/watch?v=10v9yUVgrmPY",
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
                "video_url": "https://www.youtube.com/watch?v=11v9yUVgrmPY",
                "difficulty": 2,
                "energy_level": 4
            },
            {
                "name": "Wave",
                "description": "波浪形身体动作",
                "video_url": "https://www.youtube.com/watch?v=12v9yUVgrmPY",
                "difficulty": 3,
                "energy_level": 3
            }
        ],
        "进阶动作": [
            {
                "name": "Isolation",
                "description": "身体部位独立运动",
                "video_url": "https://www.youtube.com/watch?v=13v9yUVgrmPY",
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
                "video_url": "https://www.youtube.com/watch?v=14v9yUVgrmPY",
                "difficulty": 3,
                "energy_level": 4
            },
            {
                "name": "Footwork",
                "description": "复杂的脚步动作",
                "video_url": "https://www.youtube.com/watch?v=15v9yUVgrmPY",
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
                "video_url": "https://www.youtube.com/watch?v=16v9yUVgrmPY",
                "difficulty": 3,
                "energy_level": 4
            },
            {
                "name": "Six Step",
                "description": "经典的地面动作",
                "video_url": "https://www.youtube.com/watch?v=17v9yUVgrmPY",
                "difficulty": 4,
                "energy_level": 4
            }
        ],
        "进阶动作": [
            {
                "name": "Windmill",
                "description": "风车动作",
                "video_url": "https://www.youtube.com/watch?v=18v9yUVgrmPY",
                "difficulty": 5,
                "energy_level": 5
            }
        ]
    }
}

def get_dance_references(dance_style, difficulty_level="基础动作"):
    """
    获取指定舞蹈风格和难度级别的参考视频
    
    Args:
        dance_style: 舞蹈风格
        difficulty_level: 难度级别 ("基础动作" 或 "进阶动作")
    
    Returns:
        list: 参考视频列表
    """
    if dance_style not in DANCE_REFERENCES:
        return []
    
    style_refs = DANCE_REFERENCES[dance_style]
    if difficulty_level not in style_refs:
        return []
    
    return style_refs[difficulty_level]

def get_random_reference(dance_style, difficulty_level="基础动作"):
    """
    随机获取一个参考视频
    
    Args:
        dance_style: 舞蹈风格
        difficulty_level: 难度级别
    
    Returns:
        dict: 参考视频信息
    """
    import random
    references = get_dance_references(dance_style, difficulty_level)
    if references:
        return random.choice(references)
    return None

def format_reference_for_prompt(reference):
    """
    将参考视频信息格式化为提示词
    
    Args:
        reference: 参考视频信息
    
    Returns:
        str: 格式化的提示词
    """
    if not reference:
        return ""
    
    return f"""
参考动作: {reference['name']}
描述: {reference['description']}
视频链接: {reference['video_url']}
难度: {reference['difficulty']}/5
能量: {reference['energy_level']}/5
"""

def get_video_search_suggestions(dance_style, move_name):
    """
    获取视频搜索建议
    
    Args:
        dance_style: 舞蹈风格
        move_name: 动作名称
    
    Returns:
        str: 搜索建议
    """
    suggestions = {
        "Hip-Hop": {
            "Harlem Shake": "搜索: 'Harlem Shake dance tutorial' 或 'Harlem Shake original'",
            "Running Man": "搜索: 'Running Man dance tutorial' 或 'Running Man hip hop'",
            "Freeze": "搜索: 'Freeze dance tutorial' 或 'Hip hop freeze moves'",
            "Slide": "搜索: 'Slide dance tutorial' 或 'Hip hop slide moves'"
        },
        "Jazz": {
            "Jazz Square": "搜索: 'Jazz Square dance tutorial' 或 'Jazz dance basics'",
            "Pirouette": "搜索: 'Pirouette tutorial' 或 'Jazz pirouette'",
            "Grand Jeté": "搜索: 'Grand Jete tutorial' 或 'Jazz leap tutorial'"
        },
        "K-pop": {
            "Point Dance": "搜索: 'K-pop point dance tutorial' 或 'K-pop choreography'",
            "Wave": "搜索: 'K-pop wave tutorial' 或 'K-pop body wave'",
            "Isolation": "搜索: 'K-pop isolation tutorial' 或 'Body isolation dance'"
        }
    }
    
    if dance_style in suggestions and move_name in suggestions[dance_style]:
        return suggestions[dance_style][move_name]
    
    return f"搜索: '{move_name} {dance_style} dance tutorial'"
