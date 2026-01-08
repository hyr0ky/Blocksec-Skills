"""
示例：使用工具类分析其他网站

展示如何使用 utils 模块分析任意网站的 API 请求
"""

import sys
sys.path.insert(0, '..')

from utils import ChromeDriver, NetworkHelper
import json


def example1_simple_api_capture():
    """示例1：简单的 API 捕获"""
    print("\n=== 示例1：简单的 API 捕获 ===\n")
    
    with ChromeDriver(headless=False) as driver:
        helper = NetworkHelper(driver)
        
        # 捕获网站的 API 请求
        responses = helper.capture_api_responses(
            url="https://jsonplaceholder.typicode.com",
            url_pattern="/posts",
            wait_time=5
        )
        
        print(f"捕获到 {len(responses)} 个响应")
        for url, data in responses.items():
            print(f"- {url}")


def example2_github_api_monitoring():
    """示例2：监控 GitHub 用户页面的 API 请求"""
    print("\n=== 示例2：GitHub API 监控 ===\n")
    
    with ChromeDriver(headless=False) as driver:
        helper = NetworkHelper(driver)
        
        # 访问 GitHub 用户页面
        responses = helper.capture_api_responses(
            url="https://github.com/trending",
            url_pattern="/trending",
            wait_time=8
        )
        
        # 打印捕获摘要
        helper.print_capture_summary()
        
        # 保存响应
        if responses:
            with open("github_api_responses.json", "w", encoding="utf-8") as f:
                json.dump(responses, f, indent=2, ensure_ascii=False)
            print("\n[✓] 响应已保存到 github_api_responses.json")


def example3_custom_interceptor():
    """示例3：自定义拦截器模式"""
    print("\n=== 示例3：自定义拦截器 ===\n")
    
    with ChromeDriver() as driver:
        # 先访问空白页注入拦截器
        driver.get("about:blank", wait_time=0)
        driver.inject_network_interceptor(url_pattern="/api/")
        
        # 访问目标网站
        driver.get("https://example.com", wait_time=5)
        
        # 获取捕获的响应
        responses = driver.get_captured_responses()
        
        # 检查拦截器状态
        status = driver.get_interceptor_status()
        print(f"拦截器状态: {status}")
        print(f"捕获的 URL: {list(responses.keys())}")


def example4_performance_log_analysis():
    """示例4：分析性能日志"""
    print("\n=== 示例4：性能日志分析 ===\n")
    
    with ChromeDriver() as driver:
        # 访问网页
        driver.get("https://example.com", wait_time=5)
        
        # 查找特定的网络请求
        requests = driver.find_network_requests_by_url("example")
        
        print(f"找到 {len(requests)} 个匹配的请求:")
        for req in requests:
            print(f"- [{req['status']}] {req['url']}")
            print(f"  类型: {req['mimeType']}")


def example5_batch_api_capture():
    """示例5：批量捕获多个 API"""
    print("\n=== 示例5：批量 API 捕获 ===\n")
    
    with ChromeDriver() as driver:
        helper = NetworkHelper(driver)
        
        # 定义要监控的多个 API 模式
        api_patterns = [
            "/api/v1/users",
            "/api/v1/posts",
            "/api/v1/comments"
        ]
        
        # 批量捕获（支持重试）
        all_responses = helper.batch_capture_with_retry(
            url="https://jsonplaceholder.typicode.com",
            url_patterns=api_patterns,
            max_retries=2,
            wait_time=5
        )
        
        # 打印结果
        for pattern, responses in all_responses.items():
            print(f"\n模式: {pattern}")
            print(f"捕获数: {len(responses)}")


def example6_console_log_monitoring():
    """示例6：监控浏览器控制台日志"""
    print("\n=== 示例6：控制台日志监控 ===\n")
    
    with ChromeDriver() as driver:
        # 访问网页
        driver.get("https://example.com", wait_time=5)
        
        # 获取控制台日志
        console_logs = driver.get_console_logs(last_n=10)
        
        print(f"最近 {len(console_logs)} 条控制台日志:")
        for log in console_logs:
            print(f"[{log['level']}] {log['message']}")


def example7_etherscan_transaction_analysis():
    """示例7：Etherscan 交易分析"""
    print("\n=== 示例7：Etherscan 交易分析 ===\n")
    
    class EtherscanAnalyzer:
        """Etherscan 交易分析器示例"""
        
        def __init__(self):
            self.driver = ChromeDriver()
            self.helper = NetworkHelper(self.driver)
        
        def analyze_transaction(self, txn_hash: str):
            """分析交易"""
            url = f"https://etherscan.io/tx/{txn_hash}"
            
            print(f"[*] 分析交易: {txn_hash}")
            print(f"[*] URL: {url}")
            
            # 捕获 API 响应
            responses = self.helper.capture_api_responses(
                url=url,
                url_pattern="/api",
                wait_time=8
            )
            
            print(f"[✓] 捕获到 {len(responses)} 个 API 响应")
            
            # 打印摘要
            self.helper.print_capture_summary()
            
            return responses
        
        def close(self):
            """关闭浏览器"""
            self.driver.quit()
    
    # 使用示例
    analyzer = EtherscanAnalyzer()
    try:
        responses = analyzer.analyze_transaction(
            "0xad2ca822b3adee0768d7d34b68ee4cc3c4822347d963f1d0c970c9c8cd2b6a33"
        )
    finally:
        analyzer.close()


def main():
    """运行所有示例"""
    examples = [
        ("简单 API 捕获", example1_simple_api_capture),
        ("GitHub API 监控", example2_github_api_monitoring),
        ("自定义拦截器", example3_custom_interceptor),
        ("性能日志分析", example4_performance_log_analysis),
        ("批量 API 捕获", example5_batch_api_capture),
        ("控制台日志监控", example6_console_log_monitoring),
        ("Etherscan 分析", example7_etherscan_transaction_analysis),
    ]
    
    print("=" * 60)
    print("通用工具类使用示例")
    print("=" * 60)
    
    for i, (name, func) in enumerate(examples, 1):
        print(f"\n{i}. {name}")
    
    choice = input("\n请选择要运行的示例（1-7，0 运行所有）: ")
    
    try:
        if choice == "0":
            for name, func in examples:
                try:
                    func()
                except Exception as e:
                    print(f"[!] 示例失败: {e}")
        else:
            idx = int(choice) - 1
            if 0 <= idx < len(examples):
                examples[idx][1]()
            else:
                print("无效的选择")
    except Exception as e:
        print(f"[!] 执行失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
