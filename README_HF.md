---
title: AI Choreography Generator
emoji: 💃
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
license: mit
short_description: Professional AI-powered choreography generation with advanced audio analysis
---

# 🎵 AI Choreography Generator

A professional-grade AI system that analyzes music and generates structured dance choreography with advanced audio processing.

## ✨ Features

- 🎶 **Advanced Audio Analysis**: Uses madmom, Essentia, and musicnn for professional-grade audio processing
- 🎭 **Structured Output**: JSON schema with detailed choreography breakdown
- 🎨 **Diversity Control**: Optimized parameters to avoid repetitive movements
- 📚 **Few-shot Learning**: Professional examples for consistent quality
- 🎪 **Action Database**: Comprehensive vocabulary for 6 dance styles
- ✨ **Post-processing**: Synonym replacement and rhythm placeholders
- 🌐 **Multilingual**: Chinese and English interface support

## 🎯 Supported Dance Styles

- **Hip-Hop**: two-step, running-man, windmill, headspin, freeze
- **House**: jack, skate, lofting, vogue, waacking, liquid
- **K-pop**: point, wave, formation-change, synchronized-move
- **Jazz**: jazz-square, pas-de-bourree, leap, isolation
- **Contemporary**: contraction, release, spiral, floor-work
- **Breaking**: top-rock, footwork, power-move, windmill

## 🚀 Usage

1. Upload an audio file (MP3/WAV)
2. Enter your OpenAI API key
3. Generate professional choreography
4. View structured dance suggestions with rhythm breakdown

## 🔧 Technical Stack

- **Audio Processing**: librosa, madmom, Essentia, musicnn
- **AI Generation**: OpenAI GPT-3.5-turbo
- **Web Framework**: Streamlit
- **Validation**: JSON Schema, Pydantic

## 📊 Output Format

```json
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
      "transition": "quarter-turn",
      "rhythm_breakdown": "1-2 two-step | 3 chest-pop | 4 hold | 5-6 shoulder-roll | 7&8 freeze"
    }
  ]
}
```

## 🎉 Perfect for

- Dance instructors and choreographers
- Music producers and DJs
- Dance students and enthusiasts
- Creative professionals
- Anyone who loves music and dance!

Let AI create professional choreography for your music! 🎵💃
