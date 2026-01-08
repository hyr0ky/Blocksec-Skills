"""
Chrome WebDriver 工具类

提供 Chrome 浏览器自动化的基础功能，包括：
- WebDriver 初始化与配置
- 网络请求拦截
- 性能日志捕获
- 控制台日志监控
"""

import json
import time
from typing import Any, Dict, List, Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class ChromeDriver:
    """Chrome WebDriver 封装类"""
    
    def __init__(self, headless: bool = False, enable_performance_log: bool = True):
        """
        初始化 Chrome WebDriver
        
        Args:
            headless: 是否使用无头模式
            enable_performance_log: 是否启用性能日志
        """
        self.driver = self._setup_driver(headless, enable_performance_log)
        self._interceptor_injected = False
    
    def _setup_driver(self, headless: bool, enable_performance_log: bool) -> WebDriver:
        """配置并创建 Chrome WebDriver"""
        chrome_options = Options()
        
        # 屏蔽 Chrome 的错误日志输出
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--log-level=3')  # 只显示 FATAL 级别错误
        
        # 性能日志配置
        if enable_performance_log:
            chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
        
        # 基础配置
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        if headless:
            chrome_options.add_argument('--headless')
        
        return webdriver.Chrome(options=chrome_options)
    
    def get(self, url: str, wait_time: int = 5) -> None:
        """
        访问 URL
        
        Args:
            url: 目标 URL
            wait_time: 加载后等待时间（秒）
        """
        self.driver.get(url)
        time.sleep(wait_time)
    
    def inject_network_interceptor(self, url_pattern: str = None) -> None:
        """
        注入 JavaScript 网络拦截器
        
        Args:
            url_pattern: 需要拦截的 URL 模式（支持 includes 匹配）
        """
        if self._interceptor_injected:
            return
        
        filter_condition = f"url && url.includes('{url_pattern}')" if url_pattern else "true"
        
        script = f"""
        (function() {{
            if (window.__interceptorInjected) return;
            window.__interceptorInjected = true;
            window.__capturedResponses = {{}};
            
            console.log('[ChromeDriver] 网络拦截器已注入');
            
            // 拦截 Fetch
            const oldFetch = window.fetch;
            window.fetch = function(...args) {{
                const url = typeof args[0] === 'string' ? args[0] : args[0].url;
                
                return oldFetch.apply(this, args).then(response => {{
                    if ({filter_condition}) {{
                        console.log('[ChromeDriver] 捕获 Fetch:', url);
                        response.clone().text().then(text => {{
                            window.__capturedResponses[url] = text;
                            console.log('[ChromeDriver] 已保存响应，当前共', Object.keys(window.__capturedResponses).length, '个');
                        }}).catch(err => {{
                            console.error('[ChromeDriver] 读取响应失败:', err);
                        }});
                    }}
                    return response;
                }});
            }};
            
            // 拦截 XMLHttpRequest
            const oldXHROpen = XMLHttpRequest.prototype.open;
            const oldXHRSend = XMLHttpRequest.prototype.send;
            
            XMLHttpRequest.prototype.open = function(method, url) {{
                this._url = url;
                this._method = method;
                return oldXHROpen.apply(this, arguments);
            }};
            
            XMLHttpRequest.prototype.send = function() {{
                const xhr = this;
                this.addEventListener('load', function() {{
                    const url = xhr._url;
                    if ({filter_condition}) {{
                        console.log('[ChromeDriver] 捕获 XHR:', url);
                        window.__capturedResponses[url] = xhr.responseText;
                        console.log('[ChromeDriver] 已保存响应，当前共', Object.keys(window.__capturedResponses).length, '个');
                    }}
                }});
                return oldXHRSend.apply(this, arguments);
            }};
            
            console.log('[ChromeDriver] 拦截器设置完成');
        }})();
        """
        
        self.driver.execute_script(script)
        self._interceptor_injected = True
    
    def get_captured_responses(self) -> Dict[str, str]:
        """
        获取拦截器捕获的所有响应
        
        Returns:
            URL -> 响应文本的字典
        """
        return self.driver.execute_script("return window.__capturedResponses || {};")
    
    def get_interceptor_status(self) -> Dict[str, Any]:
        """
        获取拦截器状态
        
        Returns:
            包含注入状态、捕获数量、URL列表的字典
        """
        return self.driver.execute_script("""
            return {
                injected: window.__interceptorInjected || false,
                count: window.__capturedResponses ? Object.keys(window.__capturedResponses).length : 0,
                urls: window.__capturedResponses ? Object.keys(window.__capturedResponses) : []
            };
        """)
    
    def get_performance_logs(self) -> List[Dict[str, Any]]:
        """
        获取性能日志
        
        Returns:
            性能日志列表
        """
        try:
            logs = self.driver.get_log("performance")
            return logs
        except Exception as e:
            print(f"[!] 获取性能日志失败: {e}")
            return []
    
    def get_console_logs(self, last_n: int = None) -> List[Dict[str, Any]]:
        """
        获取浏览器控制台日志
        
        Args:
            last_n: 只返回最后 N 条日志，None 表示全部
            
        Returns:
            控制台日志列表
        """
        try:
            logs = self.driver.get_log("browser")
            return logs[-last_n:] if last_n else logs
        except Exception as e:
            print(f"[!] 获取控制台日志失败: {e}")
            return []
    
    def get_network_response_body(self, request_id: str) -> Optional[str]:
        """
        通过 Chrome DevTools Protocol 获取网络响应体
        
        Args:
            request_id: 网络请求 ID
            
        Returns:
            响应体文本，失败返回 None
        """
        try:
            response_body = self.driver.execute_cdp_cmd(
                "Network.getResponseBody",
                {"requestId": request_id}
            )
            return response_body.get("body")
        except Exception:
            # 静默失败，不输出错误信息
            return None
    
    def find_network_requests_by_url(self, url_pattern: str) -> List[Dict[str, Any]]:
        """
        从性能日志中查找匹配的网络请求
        
        Args:
            url_pattern: URL 匹配模式
            
        Returns:
            包含 URL 和 requestId 的字典列表
        """
        requests = []
        logs = self.get_performance_logs()
        
        for entry in logs:
            try:
                log = json.loads(entry["message"])["message"]
                
                if log["method"] == "Network.responseReceived":
                    params = log["params"]
                    url = params["response"]["url"]
                    
                    if url_pattern in url:
                        requests.append({
                            "url": url,
                            "requestId": params["requestId"],
                            "status": params["response"].get("status"),
                            "mimeType": params["response"].get("mimeType"),
                        })
            except Exception:
                continue
        
        return requests
    
    def execute_script(self, script: str) -> Any:
        """
        执行 JavaScript 脚本
        
        Args:
            script: JavaScript 代码
            
        Returns:
            脚本执行结果
        """
        return self.driver.execute_script(script)
    
    def quit(self) -> None:
        """关闭浏览器"""
        if self.driver:
            self.driver.quit()
    
    def __enter__(self):
        """上下文管理器入口"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器退出"""
        self.quit()
