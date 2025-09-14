#!/usr/bin/env python3
"""
AI编舞生成器 - 命令行版本
使用方法: python main.py <音频文件路径>
"""

import sys
import os
import argparse
from choreography_generator import ChoreographyGenerator

def main():
    parser = argparse.ArgumentParser(description='AI编舞生成器')
    parser.add_argument('audio_file', help='音频文件路径 (MP3/WAV)')
    parser.add_argument('-o', '--output', help='输出JSON文件路径')
    parser.add_argument('--api-key', help='OpenAI API密钥')
    
    args = parser.parse_args()
    
    # 检查API密钥
    if args.api_key:
        os.environ['OPENAI_API_KEY'] = args.api_key
    elif not os.getenv('OPENAI_API_KEY'):
        print("❌ 错误: 请设置OpenAI API密钥")
        print("方法1: 设置环境变量 OPENAI_API_KEY")
        print("方法2: 使用 --api-key 参数")
        sys.exit(1)
    
    # 检查音频文件
    if not os.path.exists(args.audio_file):
        print(f"❌ 错误: 音频文件不存在: {args.audio_file}")
        sys.exit(1)
    
    try:
        print("🎵 AI编舞生成器启动...")
        print(f"📁 处理文件: {args.audio_file}")
        
        # 创建生成器并处理
        generator = ChoreographyGenerator()
        result = generator.generate_choreography_from_file(args.audio_file)
        
        # 打印结果摘要
        generator.print_choreography_summary(result)
        
        # 保存结果
        if args.output:
            generator.save_choreography(result, args.output)
        else:
            # 默认输出文件名
            base_name = os.path.splitext(os.path.basename(args.audio_file))[0]
            output_file = f"{base_name}_choreography.json"
            generator.save_choreography(result, output_file)
        
        print("\n🎉 编舞生成完成！")
        
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
