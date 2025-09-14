"""
专业动作词库数据库
按舞蹈风格分类，包含丰富的动作词汇和维度描述
"""

# 动作维度词汇
ACTION_DIMENSIONS = {
    'level': ['high', 'mid', 'low', 'floor'],
    'plane': ['frontal', 'sagittal', 'transverse'],
    'direction': ['UL', 'UR', 'DL', 'DR', 'CW', 'CCW', 'forward', 'backward', 'side', 'diagonal'],
    'dynamics': ['staccato', 'legato', 'groove', 'hit', 'melt', 'sharp', 'smooth', 'bouncy', 'fluid'],
    'initiation': ['head', 'shoulder', 'chest', 'hip', 'knee', 'foot', 'arm', 'torso', 'spine'],
    'transition': ['quarter_turn', 'half_turn', 'full_turn', 'spin', 'level_drop', 'level_rise', 
                   'travel_diagonal', 'travel_forward', 'travel_backward', 'travel_side']
}

# 同义词替换库
SYNONYMS = {
    'wave': ['ripple', 'undulation', 'sway', 'flow', 'cascade'],
    'pop': ['hit', 'snap', 'punch', 'strike', 'jab'],
    'slide': ['glide', 'drift', 'float', 'sweep', 'skim'],
    'freeze': ['hold', 'pause', 'stop', 'lock', 'still'],
    'spin': ['turn', 'rotate', 'twirl', 'whirl', 'pivot'],
    'jump': ['leap', 'hop', 'bounce', 'spring', 'bound'],
    'drop': ['fall', 'sink', 'lower', 'descend', 'plunge'],
    'rise': ['lift', 'elevate', 'ascend', 'climb', 'soar']
}

# 按风格分类的动作词库
DANCE_ACTION_DATABASE = {
    'Hip-Hop': {
        'basic_moves': [
            'two-step', 'running-man', 'roger-rabbit', 'cabbage-patch', 'reject',
            'wop', 'smurf', 'butterfly', 'robocop', 'alf', 'bart-simpson'
        ],
        'advanced_moves': [
            'windmill', 'headspin', 'backspin', 'flare', 'swipe', '1990', '2000',
            'turtle', 'cricket', 'jackhammer', 'pump', 'chair-freeze', 'baby-freeze'
        ],
        'grooves': [
            'bounce', 'rock', 'sway', 'lean', 'dip', 'pump', 'pulse', 'vibe',
            'stutter', 'hesitation', 'syncopation', 'off-beat', 'laid-back'
        ],
        'transitions': [
            'quarter-turn', 'half-turn', 'full-turn', 'level-drop', 'level-rise',
            'travel-diagonal', 'step-slide', 'cross-step', 'pivot-turn'
        ]
    },
    
    'House': {
        'basic_moves': [
            'jack', 'skate', 'lofting', 'shuffle', 'two-step', 'cross-step',
            'side-step', 'back-step', 'forward-step', 'diagonal-step'
        ],
        'advanced_moves': [
            'vogue', 'waacking', 'liquid', 'tutting', 'finger-tut', 'digits',
            'waving', 'gliding', 'floating', 'skating', 'lofting-combo'
        ],
        'grooves': [
            'groove', 'sway', 'rock', 'bounce', 'pulse', 'vibe', 'flow',
            'smooth', 'fluid', 'laid-back', 'deep', 'soulful'
        ],
        'transitions': [
            'smooth-transition', 'flow-transition', 'glide-transition',
            'level-change', 'direction-change', 'tempo-change'
        ]
    },
    
    'K-pop': {
        'basic_moves': [
            'point', 'wave', 'clap', 'snap', 'flick', 'swipe', 'punch',
            'kick', 'step-touch', 'grapevine', 'chasse', 'pas-de-bourree'
        ],
        'advanced_moves': [
            'formation-change', 'synchronized-move', 'power-move',
            'isolation', 'body-wave', 'chest-pop', 'shoulder-roll',
            'hip-roll', 'arm-wave', 'finger-tut'
        ],
        'grooves': [
            'sharp', 'precise', 'synchronized', 'powerful', 'dynamic',
            'energetic', 'crisp', 'clean', 'tight', 'controlled'
        ],
        'transitions': [
            'formation-transition', 'level-transition', 'direction-transition',
            'synchronized-transition', 'power-transition'
        ]
    },
    
    'Jazz': {
        'basic_moves': [
            'jazz-square', 'pas-de-bourree', 'chasse', 'grapevine',
            'step-touch', 'kick-ball-change', 'pivot-turn', 'pirouette'
        ],
        'advanced_moves': [
            'leap', 'jump', 'turn', 'isolation', 'body-wave', 'contraction',
            'release', 'spiral', 'fall', 'recovery', 'suspension'
        ],
        'grooves': [
            'smooth', 'fluid', 'expressive', 'dramatic', 'emotional',
            'lyrical', 'melodic', 'rhythmic', 'syncopated', 'swung'
        ],
        'transitions': [
            'smooth-transition', 'flowing-transition', 'dramatic-transition',
            'level-transition', 'direction-transition', 'tempo-transition'
        ]
    },
    
    'Contemporary': {
        'basic_moves': [
            'contraction', 'release', 'spiral', 'fall', 'recovery',
            'suspension', 'swing', 'momentum', 'weight-shift', 'gravity'
        ],
        'advanced_moves': [
            'floor-work', 'partner-work', 'lift', 'support', 'balance',
            'off-balance', 'fall-recovery', 'spiral-turn', 'release-turn'
        ],
        'grooves': [
            'organic', 'natural', 'flowing', 'expressive', 'emotional',
            'dramatic', 'lyrical', 'abstract', 'interpretive', 'artistic'
        ],
        'transitions': [
            'organic-transition', 'flowing-transition', 'dramatic-transition',
            'level-transition', 'space-transition', 'energy-transition'
        ]
    },
    
    'Breaking': {
        'basic_moves': [
            'top-rock', 'footwork', 'freeze', 'power-move', 'transition',
            'six-step', 'three-step', 'cc', 'indian-step', 'russian-step'
        ],
        'advanced_moves': [
            'windmill', 'headspin', 'backspin', 'flare', 'swipe', '1990',
            '2000', 'turtle', 'cricket', 'jackhammer', 'pump', 'chair-freeze'
        ],
        'grooves': [
            'aggressive', 'powerful', 'dynamic', 'explosive', 'intense',
            'rhythmic', 'syncopated', 'off-beat', 'laid-back', 'smooth'
        ],
        'transitions': [
            'power-transition', 'freeze-transition', 'level-transition',
            'direction-transition', 'momentum-transition'
        ]
    }
}

def get_action_candidates(style, num_candidates=12, avoid_actions=None):
    """
    根据舞蹈风格获取候选动作
    
    Args:
        style: 舞蹈风格
        num_candidates: 候选动作数量
        avoid_actions: 需要避免的动作列表
    
    Returns:
        候选动作列表
    """
    if avoid_actions is None:
        avoid_actions = []
    
    if style not in DANCE_ACTION_DATABASE:
        style = 'Hip-Hop'  # 默认风格
    
    style_actions = DANCE_ACTION_DATABASE[style]
    all_actions = []
    
    # 收集所有动作
    for category, actions in style_actions.items():
        all_actions.extend(actions)
    
    # 过滤掉需要避免的动作
    available_actions = [action for action in all_actions if action not in avoid_actions]
    
    # 如果可用动作不足，从其他风格补充
    if len(available_actions) < num_candidates:
        for other_style, other_actions in DANCE_ACTION_DATABASE.items():
            if other_style != style:
                for category, actions in other_actions.items():
                    available_actions.extend([action for action in actions if action not in avoid_actions])
    
    # 随机选择候选动作
    import random
    return random.sample(available_actions, min(num_candidates, len(available_actions)))

def get_synonym_replacement(word):
    """
    获取同义词替换
    
    Args:
        word: 原词
    
    Returns:
        同义词或原词
    """
    import random
    
    for key, synonyms in SYNONYMS.items():
        if key in word.lower():
            return word.lower().replace(key, random.choice(synonyms))
    
    return word

def get_action_dimensions():
    """
    获取动作维度词汇
    
    Returns:
        动作维度字典
    """
    return ACTION_DIMENSIONS

def create_rhythm_placeholder(moves, beats=8):
    """
    为动作创建节奏占位符
    
    Args:
        moves: 动作列表
        beats: 节拍数
    
    Returns:
        带节奏占位的动作字符串
    """
    if not moves:
        return "1-8 basic groove"
    
    # 简单的节奏分配
    beats_per_move = beats // len(moves)
    result = []
    
    for i, move in enumerate(moves):
        start_beat = i * beats_per_move + 1
        end_beat = (i + 1) * beats_per_move
        
        if start_beat == end_beat:
            result.append(f"{start_beat} {move}")
        else:
            result.append(f"{start_beat}-{end_beat} {move}")
    
    return " | ".join(result)
