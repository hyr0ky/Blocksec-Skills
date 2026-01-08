"""
合约代码获取器

使用 Chrome DevTools MCP 从区块链浏览器获取合约源代码
"""

import re
from pathlib import Path
from typing import Optional, Dict


class ContractFetcher:
    """合约代码获取器"""
    
    # 区块链浏览器 URL 映射
    EXPLORER_URLS = {
        1: "https://etherscan.io/address/{address}#code",
        56: "https://bscscan.com/address/{address}#code",
        137: "https://polygonscan.com/address/{address}#code",
        42161: "https://arbiscan.io/address/{address}#code",
        10: "https://optimistic.etherscan.io/address/{address}#code",
    }
    
    def __init__(self, chain_id: int):
        """
        初始化合约代码获取器
        
        Args:
            chain_id: 链ID
        """
        self.chain_id = chain_id
    
    def get_explorer_url(self, address: str) -> Optional[str]:
        """
        获取区块链浏览器 URL
        
        Args:
            address: 合约地址
            
        Returns:
            浏览器 URL，如果链ID不支持则返回 None
        """
        if self.chain_id not in self.EXPLORER_URLS:
            return None
        
        return self.EXPLORER_URLS[self.chain_id].format(address=address)
    
    def extract_contract_code_from_snapshot(self, snapshot_text: str) -> Optional[str]:
        """
        从快照文本中提取合约代码
        
        Args:
            snapshot_text: Chrome DevTools 快照文本
            
        Returns:
            合约源代码，如果提取失败则返回 None
        """
        # 尝试匹配合约代码区域
        # 这里需要根据实际的快照格式进行调整
        patterns = [
            r'contract\s+\w+\s*{[\s\S]+?}',  # 匹配 Solidity 合约
            r'pragma\s+solidity[\s\S]+?}',   # 从 pragma 开始匹配
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, snapshot_text, re.MULTILINE)
            if matches:
                return '\n\n'.join(matches)
        
        return None
    
    def save_contract_code(self, code: str, output_path: Path, contract_name: str = "contract_code"):
        """
        保存合约代码到文件
        
        Args:
            code: 合约代码
            output_path: 输出目录路径
            contract_name: 合约文件名（不含扩展名）
        """
        contract_file = output_path / f"{contract_name}.sol"
        contract_file.write_text(code, encoding="utf-8")
    
    def fetch_contract_code_with_selenium(self, driver, address: str, wait_time: int = 8) -> Optional[str]:
        """使用 Selenium 从区块链浏览器获取合约源代码

        Args:
            driver: ChromeDriver 实例（需要已初始化的浏览器）
            address: 合约地址
            wait_time: 页面加载后的等待时间（秒）

        Returns:
            合约源代码字符串，获取失败返回 None
        """
        explorer_url = self.get_explorer_url(address)
        if not explorer_url:
            return None
        
        try:
            # 复用现有的 ChromeDriver
            driver.get(explorer_url, wait_time=wait_time)

            script = """
                return (function() {
                    // 1. 优先使用复制按钮对应的隐藏 textarea（BscScan/Etherscan 通用）
                    var ta = document.getElementById('js-clipboard-sourceCode-textarea');
                    if (ta && ta.value && ta.value.length > 0) {
                        return ta.value;
                    }

                    // 2. 如果页面使用 Ace 编辑器（BscScan 新版），优先从编辑器读取完整源码
                    if (window.ace) {
                        try {
                            var editor = window.ace.edit("editor");
                            if (editor) {
                                var value = editor.getValue();
                                if (value && value.length > 0) {
                                    return value;
                                }
                            }
                        } catch (e) {}
                    }

                    // 3. 兼容其它 textarea 命名，查找包含 pragma solidity 的大块文本
                    var tas = Array.from(document.querySelectorAll('textarea'));
                    for (var i = 0; i < tas.length; i++) {
                        var t = tas[i];
                        var v = t.value || t.innerText || t.textContent || "";
                        if (v && v.includes("pragma solidity") && v.length > 200) {
                            return v;
                        }
                    }

                    // 4. 兜底：从 pre 标签中提取（注意 pre 可能只包含可视区域）
                    var pres = Array.from(document.querySelectorAll('pre'));
                    var best = "";
                    for (var j = 0; j < pres.length; j++) {
                        var pre = pres[j];
                        var text = pre.innerText || pre.textContent || "";
                        // 去掉可能存在的纯数字行号
                        var cleaned = text.replace(/^\s*\d+\s*$/gm, "");
                        if (cleaned.includes("pragma solidity") && cleaned.length > 200) {
                            if (!best || cleaned.length > best.length) {
                                best = cleaned;
                            }
                        }
                    }
                    return best || null;
                })();
            """
            code = driver.execute_script(script)
            if not code:
                return None

            return code
        except Exception as e:
            return None
    def get_chain_name(self) -> str:
        """
        获取链名称
        
        Returns:
            链名称
        """
        chain_names = {
            1: "Ethereum",
            56: "BSC",
            137: "Polygon",
            42161: "Arbitrum",
            10: "Optimism",
        }
        return chain_names.get(self.chain_id, f"Chain-{self.chain_id}")


def extract_contract_address_from_report(report_content: str, address_type: str = "victim") -> Optional[str]:
    """
    从报告中提取合约地址
    
    Args:
        report_content: 报告内容
        address_type: 地址类型 ("victim" 或 "attacker")
        
    Returns:
        合约地址，如果提取失败则返回 None
    """
    # 根据地址类型选择匹配模式
    if address_type == "victim":
        pattern = r'###\s*受害者.*?\n.*?地址.*?`(0x[a-fA-F0-9]{40})`'
    elif address_type == "attacker":
        pattern = r'###\s*攻击者.*?\n.*?地址.*?`(0x[a-fA-F0-9]{40})`'
    else:
        return None
    
    match = re.search(pattern, report_content, re.DOTALL)
    if match:
        return match.group(1)
    
    return None


def build_mcp_instructions(chain_id: int, contract_address: str) -> Dict[str, str]:
    """
    构建 Chrome DevTools MCP 指令
    
    Args:
        chain_id: 链ID
        contract_address: 合约地址
        
    Returns:
        包含 MCP 指令的字典
    """
    fetcher = ContractFetcher(chain_id)
    explorer_url = fetcher.get_explorer_url(contract_address)
    
    if not explorer_url:
        return {
            "error": f"不支持的链ID: {chain_id}"
        }
    
    return {
        "step1": f"使用 mcp_chrome-devtools_new_page 打开: {explorer_url}",
        "step2": "使用 mcp_chrome-devtools_wait_for 等待 'Contract Source Code' 文本出现",
        "step3": "使用 mcp_chrome-devtools_take_snapshot 获取页面快照",
        "step4": "从快照中提取合约源代码",
        "step5": f"保存到 Json_report/{{txn_hash}}/contract_code.sol"
    }
