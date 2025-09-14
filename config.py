import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Audio processing configuration
SAMPLE_RATE = 22050
HOP_LENGTH = 512
FRAME_LENGTH = 2048

# Dance generation configuration
BEATS_PER_SEGMENT = 8  # 8-beat segments for choreography
DANCE_STYLES = [
    "Hip-Hop", "Jazz", "K-pop", "House", "Contemporary", 
    "Breaking", "Popping", "Locking", "Waacking", "Voguing"
]
