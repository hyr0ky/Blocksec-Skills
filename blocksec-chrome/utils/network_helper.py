"""
网络请求辅助工具

提供网络请求相关的辅助功能
"""

import json
from typing import Any, Dict, List, Optional, Callable

from .chrome_driver import ChromeDriver


class NetworkHelper:
    """网络请求辅助类"""
    
    def __init__(self, driver: ChromeDriver):
        """
        初始化网络辅助工具
        
        Args:
            driver: ChromeDriver 实例
        """
        self.driver = driver
    
    def capture_api_responses(
        self,
        url: str,
        url_pattern: str,
        wait_time: int = 10,
        use_interceptor: bool = True,
    ) -> Dict[str, Any]:
        """
        捕获指定模式的 API 响应
        
        Args:
            url: 目标页面 URL
            url_pattern: API URL 匹配模式
            wait_time: 等待时间（秒）
            use_interceptor: 是否使用 JavaScript 拦截器
            
        Returns:
            API 响应字典 {url: response_json}
        """
        responses = {}
        
        # 先访问空白页注入拦截器
        if use_interceptor:
            self.driver.get("about:blank", wait_time=0)
            self.driver.inject_network_interceptor(url_pattern)
        
        # 访问目标页面
        self.driver.get(url, wait_time=wait_time)
        
        # 尝试从拦截器获取
        if use_interceptor:
            captured = self.driver.get_captured_responses()
            for api_url, response_text in captured.items():
                if url_pattern in api_url:
                    try:
                        responses[api_url] = json.loads(response_text)
                    except json.JSONDecodeError:
                        responses[api_url] = {"raw_text": response_text}
        
        # 备用方案：从性能日志获取
        if not responses:
            responses = self._fetch_from_performance_log(url_pattern)
        
        return responses
    
    def _fetch_from_performance_log(self, url_pattern: str) -> Dict[str, Any]:
        """
        从性能日志中获取 API 响应（备用方案）
        
        Args:
            url_pattern: URL 匹配模式
            
        Returns:
            API 响应字典
        """
        responses = {}
        
        # 查找匹配的网络请求
        requests = self.driver.find_network_requests_by_url(url_pattern)
        
        for req in requests:
            url = req["url"]
            request_id = req["requestId"]
            
            # 获取响应体
            body = self.driver.get_network_response_body(request_id)
            if body:
                try:
                    responses[url] = json.loads(body)
                except json.JSONDecodeError:
                    responses[url] = {"raw_text": body}
        
        return responses
    
    def parse_responses_by_path_mapping(
        self,
        responses: Dict[str, Any],
        path_mapping: Dict[str, str],
    ) -> Dict[str, Any]:
        """
        根据路径映射解析响应
        
        Args:
            responses: API 响应字典 {url: response}
            path_mapping: 路径映射 {name: path_fragment}
            
        Returns:
            解析后的响应字典 {name: response}
        """
        parsed = {}
        
        for url, response in responses.items():
            for name, path in path_mapping.items():
                if path in url:
                    parsed[name] = response
                    break
        
        return parsed
    
    def batch_capture_with_retry(
        self,
        url: str,
        url_patterns: List[str],
        max_retries: int = 3,
        wait_time: int = 10,
    ) -> Dict[str, Dict[str, Any]]:
        """
        批量捕获多个 API 响应（支持重试）
        
        Args:
            url: 目标页面 URL
            url_patterns: API URL 模式列表
            max_retries: 最大重试次数
            wait_time: 每次等待时间
            
        Returns:
            分类的响应字典 {pattern: {url: response}}
        """
        all_responses = {}
        
        for pattern in url_patterns:
            all_responses[pattern] = {}
        
        for attempt in range(max_retries):
            print(f"[*] 尝试 {attempt + 1}/{max_retries}...")
            
            # 合并所有模式为一个模式（使用通用前缀）
            combined_pattern = url_patterns[0].split('/')[0] if url_patterns else ""
            responses = self.capture_api_responses(url, combined_pattern, wait_time)
            
            # 分类到各个模式
            for url_key, response in responses.items():
                for pattern in url_patterns:
                    if pattern in url_key:
                        all_responses[pattern][url_key] = response
                        break
            
            # 检查是否所有模式都捕获到
            missing_patterns = [p for p in url_patterns if not all_responses[p]]
            if not missing_patterns:
                print(f"[✓] 所有 API 响应已捕获")
                break
            
            print(f"[!] 还有 {len(missing_patterns)} 个模式未捕获: {missing_patterns}")
        
        return all_responses
    
    def wait_for_api(
        self,
        url_pattern: str,
        timeout: int = 30,
        check_interval: float = 0.5,
    ) -> bool:
        """
        等待特定 API 请求完成
        
        Args:
            url_pattern: API URL 匹配模式
            timeout: 超时时间（秒）
            check_interval: 检查间隔（秒）
            
        Returns:
            是否成功捕获
        """
        import time
        elapsed = 0
        
        while elapsed < timeout:
            status = self.driver.get_interceptor_status()
            urls = status.get("urls", [])
            
            for url in urls:
                if url_pattern in url:
                    return True
            
            time.sleep(check_interval)
            elapsed += check_interval
        
        return False
    
    def print_capture_summary(self) -> None:
        """打印捕获摘要"""
        status = self.driver.get_interceptor_status()
        print(f"\n[*] 拦截器状态:")
        print(f"    - 已注入: {status['injected']}")
        print(f"    - 捕获数: {status['count']}")
        
        if status['urls']:
            print(f"[*] 捕获的 URL:")
            for url in status['urls']:
                print(f"    - {url}")
