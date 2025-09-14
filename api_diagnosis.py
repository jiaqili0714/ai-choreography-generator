#!/usr/bin/env python3
"""
OpenAI API调用失败原因自查工具
"""

import os
import sys
import openai
import requests
import json
from datetime import datetime

class APIDiagnosis:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.results = []
    
    def log_result(self, test_name, success, message, details=None):
        """记录测试结果"""
        status = "✅" if success else "❌"
        result = {
            'test': test_name,
            'success': success,
            'message': message,
            'details': details,
            'timestamp': datetime.now().strftime("%H:%M:%S")
        }
        self.results.append(result)
        print(f"{status} {test_name}: {message}")
        if details:
            print(f"   详情: {details}")
    
    def test_1_api_key_exists(self):
        """测试1: 检查API密钥是否存在"""
        if not self.api_key:
            self.log_result(
                "API密钥检查", 
                False, 
                "未设置OPENAI_API_KEY环境变量",
                "请在Streamlit界面设置API密钥或运行: export OPENAI_API_KEY='your_key'"
            )
            return False
        else:
            self.log_result(
                "API密钥检查", 
                True, 
                f"API密钥已设置: {self.api_key[:10]}...",
                f"密钥长度: {len(self.api_key)} 字符"
            )
            return True
    
    def test_2_api_key_format(self):
        """测试2: 检查API密钥格式"""
        if not self.api_key:
            return False
        
        # OpenAI API密钥通常以sk-开头
        if not self.api_key.startswith('sk-'):
            self.log_result(
                "API密钥格式", 
                False, 
                "API密钥格式可能不正确",
                "OpenAI API密钥通常以'sk-'开头"
            )
            return False
        else:
            self.log_result(
                "API密钥格式", 
                True, 
                "API密钥格式正确",
                "密钥以'sk-'开头"
            )
            return True
    
    def test_3_network_connectivity(self):
        """测试3: 检查网络连接"""
        try:
            response = requests.get('https://api.openai.com/v1/models', timeout=10)
            if response.status_code == 401:
                self.log_result(
                    "网络连接", 
                    True, 
                    "网络连接正常，但API密钥无效",
                    f"HTTP状态码: {response.status_code}"
                )
                return True
            elif response.status_code == 200:
                self.log_result(
                    "网络连接", 
                    True, 
                    "网络连接正常",
                    f"HTTP状态码: {response.status_code}"
                )
                return True
            else:
                self.log_result(
                    "网络连接", 
                    False, 
                    f"网络连接异常",
                    f"HTTP状态码: {response.status_code}"
                )
                return False
        except requests.exceptions.Timeout:
            self.log_result(
                "网络连接", 
                False, 
                "网络连接超时",
                "请检查网络连接或防火墙设置"
            )
            return False
        except requests.exceptions.ConnectionError:
            self.log_result(
                "网络连接", 
                False, 
                "无法连接到OpenAI服务器",
                "请检查网络连接或尝试使用VPN"
            )
            return False
        except Exception as e:
            self.log_result(
                "网络连接", 
                False, 
                f"网络连接测试失败: {str(e)}",
                "未知网络错误"
            )
            return False
    
    def test_4_openai_package(self):
        """测试4: 检查OpenAI包版本"""
        try:
            import openai
            version = openai.__version__
            self.log_result(
                "OpenAI包版本", 
                True, 
                f"OpenAI包已安装，版本: {version}",
                "版本检查通过"
            )
            return True
        except ImportError:
            self.log_result(
                "OpenAI包版本", 
                False, 
                "OpenAI包未安装",
                "请运行: pip install openai"
            )
            return False
        except Exception as e:
            self.log_result(
                "OpenAI包版本", 
                False, 
                f"OpenAI包检查失败: {str(e)}",
                "包可能损坏，尝试重新安装"
            )
            return False
    
    def test_5_simple_api_call(self):
        """测试5: 简单API调用"""
        if not self.api_key:
            return False
        
        try:
            openai.api_key = self.api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=5
            )
            
            result = response.choices[0].message.content.strip()
            self.log_result(
                "简单API调用", 
                True, 
                "API调用成功",
                f"响应: {result}"
            )
            return True
            
        except openai.error.AuthenticationError:
            self.log_result(
                "简单API调用", 
                False, 
                "API密钥无效或已过期",
                "请检查API密钥是否正确"
            )
            return False
        except openai.error.RateLimitError:
            self.log_result(
                "简单API调用", 
                False, 
                "API调用频率超限",
                "请稍后再试或检查API配额"
            )
            return False
        except openai.error.InvalidRequestError as e:
            self.log_result(
                "简单API调用", 
                False, 
                f"API请求无效: {str(e)}",
                "请检查请求参数"
            )
            return False
        except openai.error.APIError as e:
            self.log_result(
                "简单API调用", 
                False, 
                f"OpenAI API错误: {str(e)}",
                "服务器端错误，请稍后重试"
            )
            return False
        except Exception as e:
            self.log_result(
                "简单API调用", 
                False, 
                f"API调用失败: {str(e)}",
                "未知错误"
            )
            return False
    
    def test_6_json_response(self):
        """测试6: 测试JSON响应解析"""
        if not self.api_key:
            return False
        
        try:
            openai.api_key = self.api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "请以JSON格式返回: {\"test\": \"success\"}"}],
                max_tokens=20
            )
            
            result = response.choices[0].message.content.strip()
            
            # 尝试解析JSON
            try:
                json_data = json.loads(result)
                self.log_result(
                    "JSON响应解析", 
                    True, 
                    "JSON解析成功",
                    f"解析结果: {json_data}"
                )
                return True
            except json.JSONDecodeError:
                self.log_result(
                    "JSON响应解析", 
                    False, 
                    "JSON解析失败",
                    f"原始响应: {result}"
                )
                return False
                
        except Exception as e:
            self.log_result(
                "JSON响应解析", 
                False, 
                f"JSON测试失败: {str(e)}",
                "无法测试JSON解析"
            )
            return False
    
    def run_all_tests(self):
        """运行所有测试"""
        print("�� 开始OpenAI API诊断...")
        print("=" * 60)
        
        tests = [
            self.test_1_api_key_exists,
            self.test_2_api_key_format,
            self.test_3_network_connectivity,
            self.test_4_openai_package,
            self.test_5_simple_api_call,
            self.test_6_json_response
        ]
        
        passed = 0
        total = len(tests)
        
        for test in tests:
            try:
                if test():
                    passed += 1
            except Exception as e:
                self.log_result(
                    test.__name__, 
                    False, 
                    f"测试执行失败: {str(e)}",
                    "测试本身出现错误"
                )
            print()
        
        # 生成总结报告
        self.generate_report(passed, total)
    
    def generate_report(self, passed, total):
        """生成诊断报告"""
        print("=" * 60)
        print("📋 诊断报告")
        print("=" * 60)
        
        print(f"🎯 总体结果: {passed}/{total} 测试通过")
        
        if passed == total:
            print("🎉 所有测试通过！API应该可以正常工作。")
            print("💡 如果仍然遇到'基础动作'问题，可能是:")
            print("   - 编舞生成逻辑问题")
            print("   - 音频处理问题")
            print("   - 其他代码逻辑问题")
        else:
            print("⚠️ 发现问题，请根据以下建议修复:")
            print()
            
            failed_tests = [r for r in self.results if not r['success']]
            for test in failed_tests:
                print(f"❌ {test['test']}: {test['message']}")
                if test['details']:
                    print(f"   💡 建议: {test['details']}")
                print()
        
        # 保存详细报告
        self.save_report()
    
    def save_report(self):
        """保存详细报告到文件"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'api_key_set': bool(self.api_key),
            'api_key_preview': self.api_key[:10] + "..." if self.api_key else None,
            'results': self.results
        }
        
        with open('api_diagnosis_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"📄 详细报告已保存到: api_diagnosis_report.json")

def main():
    """主函数"""
    print("🩺 OpenAI API调用失败原因自查工具")
    print("=" * 60)
    
    diagnosis = APIDiagnosis()
    diagnosis.run_all_tests()

if __name__ == "__main__":
    main()
