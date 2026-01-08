"""
Blocksec 交易安全分析器

基于 Blocksec API，提供自动化的 Web3 安全事件分析功能
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from models import (
    TransactionBasicInfo,
    AddressInfo,
    FundFlowItem,
    StateChangeItem,
    VulnerabilityReport,
)
from utils import ChromeDriver, NetworkHelper


class BlocksecAnalyzer:
    """Blocksec 交易安全分析器"""
    
    # Blocksec API 路径映射
    API_PATHS = {
        "basic_info": "/api/v1/onchain/tx/basic-info",
        "balance_change": "/api/v1/onchain/tx/balance-change",
        "top_profit_loss": "/api/v1/onchain/tx/top-profit-loss",
        "address_label": "/api/v1/onchain/tx/address-label",
        "fundflow": "/api/v1/onchain/tx/fundflow",
        "state_change": "/api/v1/onchain/tx/state-change",
        "trace": "/api/v1/onchain/tx/trace",
    }
    
    # 链ID到名称的映射
    CHAIN_NAMES = {
        1: "eth",
        56: "bsc",
        137: "polygon",
        42161: "arbitrum",
        10: "optimism",
    }
    
    def __init__(self, driver: ChromeDriver = None, headless: bool = False):
        """
        初始化分析器
        
        Args:
            driver: ChromeDriver 实例（可选，不传则自动创建）
            headless: 是否使用无头模式
        """
        self.driver = driver or ChromeDriver(headless=headless)
        self.network_helper = NetworkHelper(self.driver)
        self.api_responses = {}
        self._own_driver = driver is None  # 标记是否自己创建的 driver
    
    def analyze_transaction(
        self,
        chain_id: int,
        txn_hash: str,
        output_dir: str = "analysis_output",
    ) -> VulnerabilityReport:
        """
        分析交易的完整流程
        
        Args:
            chain_id: 链ID
            txn_hash: 交易哈希
            output_dir: 输出目录
            
        Returns:
            VulnerabilityReport 对象
        """
        # 1. 构建 URL
        url = self._build_tx_url(chain_id, txn_hash)
        
        # 2. 捕获 API 响应
        self._fetch_api_responses(url)
        
        # 3. 解析并生成报告
        report = self._build_report(chain_id, txn_hash)
        
        # 4. 保存报告
        self._save_report(report, txn_hash, output_dir)
        
        return report
    
    def _build_tx_url(self, chain_id: int, txn_hash: str) -> str:
        """构建交易 URL"""
        chain_name = self.CHAIN_NAMES.get(chain_id, "eth")
        return f"https://app.blocksec.com/explorer/tx/{chain_name}/{txn_hash}"
    
    def _fetch_api_responses(self, url: str) -> None:
        """捕获 API 响应"""
        # 捕获所有 Blocksec API
        responses = self.network_helper.capture_api_responses(
            url=url,
            url_pattern="/api/v1/onchain/tx/",
            wait_time=12,
        )
        
        # 解析响应到各个 API
        self.api_responses = self.network_helper.parse_responses_by_path_mapping(
            responses=responses,
            path_mapping=self.API_PATHS,
        )
    
    def _build_report(
        self,
        chain_id: int,
        txn_hash: str,
    ) -> VulnerabilityReport:
        """构建漏洞报告"""
        # 解析基础信息
        basic_info = self._parse_basic_info(chain_id, txn_hash)
        
        # 解析攻击者/受害者
        attacker, victim = self._parse_attacker_victim()
        
        # 解析资金流向
        fund_flow = self._parse_fund_flow()
        
        # 解析状态变化
        state_changes = self._parse_state_changes()
        
        # 生成报告
        report = VulnerabilityReport(
            basic_info=basic_info,
            attacker=attacker,
            victim=victim,
            vulnerability_type=None,
            fund_flow=fund_flow,
            state_changes=state_changes,
        )
        
        # 生成分析总结
        report.analysis_summary = self._generate_summary(report)
        
        return report
    
    # ==========================================
    # 数据解析方法
    # ==========================================
    
    def _parse_basic_info(
        self,
        chain_id: int,
        txn_hash: str,
    ) -> TransactionBasicInfo:
        """解析交易基础信息"""
        data = self.api_responses.get("basic_info", {})
        
        return TransactionBasicInfo(
            txn_hash=txn_hash,
            chain_id=chain_id,
            status=data.get("status"),
            timestamp=data.get("timestamp"),
            block_number=data.get("blockNumber"),
            gas_used=data.get("gasUsed"),
            sender=data.get("sender"),
            receiver=data.get("receiver"),
        )
    
    def _parse_attacker_victim(
        self,
    ) -> Tuple[Optional[AddressInfo], Optional[AddressInfo]]:
        """解析攻击者和受害者"""
        attacker = None
        victim = None
        
        # 从 top_profit_loss 获取
        top_pl = self.api_responses.get("top_profit_loss", {})
        
        if top_pl:
            attacker_addr = top_pl.get("topProfitAddress")
            victim_addr = top_pl.get("topLossAddress")
            
            if attacker_addr:
                attacker = AddressInfo(address=attacker_addr)
            if victim_addr:
                victim = AddressInfo(address=victim_addr)
        
        # 补充标签信息
        labels = self._get_address_labels()
        if attacker and attacker.address in labels:
            attacker.label = labels[attacker.address]
        if victim and victim.address in labels:
            victim.label = labels[victim.address]
        
        return attacker, victim
    
    def _get_address_labels(self) -> Dict[str, str]:
        """获取地址标签映射"""
        labels = {}
        label_data = self.api_responses.get("address_label", [])
        
        # address_label 是数组格式
        if isinstance(label_data, list):
            for item in label_data:
                if isinstance(item, dict) and "address" in item:
                    labels[item["address"]] = item.get("label") or item.get("name", "")
        
        return labels
    
    def _parse_fund_flow(self) -> List[FundFlowItem]:
        """解析资金流向"""
        flow_data = self.api_responses.get("fundflow", [])
        
        # fundflow 是数组格式
        if not isinstance(flow_data, list):
            return []
        
        labels = self._get_address_labels()
        flows = []
        
        for item in flow_data:
            if not isinstance(item, dict):
                continue
            flow = FundFlowItem(
                order=item.get("order", 0),
                from_address=item.get("from", ""),
                to_address=item.get("to", ""),
                token=item.get("token", ""),
                amount=item.get("amount", "0"),
                from_label=labels.get(item.get("from", "")),
                to_label=labels.get(item.get("to", "")),
            )
            flows.append(flow)
        
        return flows
    
    def _parse_state_changes(self) -> List[StateChangeItem]:
        """解析状态变化"""
        state_data = self.api_responses.get("state_change", [])
        
        # state_change 是数组格式
        if not isinstance(state_data, list):
            return []
        
        changes = []
        for item in state_data:
            if not isinstance(item, dict):
                continue
            
            contract_addr = item.get("address", "")
            storage_vars = item.get("storageVariables", [])
            
            for var in storage_vars:
                if not isinstance(var, dict):
                    continue
                
                var_name = var.get("name", "")
                var_type = var.get("type", "")
                value_info = var.get("value", {})
                prev_val = value_info.get("prev") if isinstance(value_info, dict) else None
                curr_val = value_info.get("current") if isinstance(value_info, dict) else None
                
                # 识别可疑模式
                is_suspicious = self._is_suspicious_change(var_name, prev_val, curr_val)
                
                change = StateChangeItem(
                    contract_address=contract_addr,
                    variable_name=var_name,
                    variable_type=var_type,
                    prev_value=prev_val,
                    current_value=curr_val,
                    is_suspicious=is_suspicious,
                )
                changes.append(change)
        
        return changes
    
    def _is_suspicious_change(
        self,
        var_name: str,
        prev_val: Any,
        curr_val: Any,
    ) -> bool:
        """判断状态变化是否可疑"""
        # 参数清零检测
        if any(keyword in var_name.lower() for keyword in ["fee", "require", "rate", "limit"]):
            if prev_val and (curr_val == "0" or curr_val == 0):
                return True
        
        # 权限修改检测
        if any(keyword in var_name.lower() for keyword in ["owner", "admin"]):
            if prev_val and prev_val != curr_val:
                return True
        
        return False
    

    
    def _generate_summary(self, report: VulnerabilityReport) -> str:
        """生成分析总结"""
        lines = []
        
        if report.attacker and report.victim:
            lines.append(f"本次安全事件中，攻击者 `{report.attacker.address}` 对受害合约 `{report.victim.address}` 发起了攻击。")
        
        suspicious = [sc for sc in report.state_changes if sc.is_suspicious]
        if suspicious:
            lines.append(f"检测到 {len(suspicious)} 处可疑状态变化，包括：")
            for sc in suspicious[:3]:
                lines.append(f"- 合约 `{sc.contract_address}` 的 `{sc.variable_name}` 从 `{sc.prev_value}` 变为 `{sc.current_value}`")
        
        if report.fund_flow:
            lines.append(f"资金流动共 {len(report.fund_flow)} 笔。")
        
        if not lines:
            lines.append("暂无足够信息生成详细总结，建议查看原始数据。")
        
        return "\n".join(lines)
    
    # ==========================================
    # 报告保存
    # ==========================================
    
    def _save_report(
        self,
        report: VulnerabilityReport,
        txn_hash: str,
        output_dir: str,
    ) -> None:
        """保存报告到文件"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # 创建交易专属目录
        tx_dir = output_path / txn_hash
        tx_dir.mkdir(parents=True, exist_ok=True)
        
        # 保存 Markdown 报告
        md_file = tx_dir / "report.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(report.to_markdown())
        print(f"[✓] report.md")

        # 为每个 API 单独保存响应数据
        for name, data in self.api_responses.items():
            single_api_file = tx_dir / f"{name}.json"
            with open(single_api_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            # 对 trace 特殊打印大小信息
            if name == "trace":
                file_size = single_api_file.stat().st_size / (1024 * 1024)
                print(f"[✓] trace.json ({file_size:.2f} MB)")
    
    def close(self) -> None:
        """关闭分析器（释放资源）"""
        if self._own_driver and self.driver:
            self.driver.quit()
    
    def __enter__(self):
        """上下文管理器入口"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器退出"""
        self.close()
