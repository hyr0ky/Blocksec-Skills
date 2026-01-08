"""
交易相关数据模型
"""

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Dict, List, Optional


@dataclass
class TransactionBasicInfo:
    """交易基础信息"""
    txn_hash: str
    chain_id: int
    status: Optional[str] = None
    timestamp: Optional[int] = None
    block_number: Optional[int] = None
    gas_used: Optional[int] = None
    sender: Optional[str] = None
    receiver: Optional[str] = None


@dataclass
class AddressInfo:
    """地址信息（攻击者/受害者）"""
    address: str
    label: Optional[str] = None
    profit_loss: Optional[Decimal] = None
    is_contract: bool = False


@dataclass
class FundFlowItem:
    """资金流动项"""
    order: int
    from_address: str
    to_address: str
    token: str
    amount: str
    from_label: Optional[str] = None
    to_label: Optional[str] = None


@dataclass
class StateChangeItem:
    """状态变化项"""
    contract_address: str
    variable_name: str
    variable_type: str
    prev_value: Any
    current_value: Any
    is_suspicious: bool = False  # 是否可疑（如参数清零）


@dataclass
class VulnerabilityReport:
    """漏洞报告"""
    basic_info: TransactionBasicInfo
    attacker: Optional[AddressInfo] = None
    victim: Optional[AddressInfo] = None
    loss_amount_usd: Optional[Decimal] = None
    vulnerability_type: Optional[str] = None
    fund_flow: List[FundFlowItem] = field(default_factory=list)
    state_changes: List[StateChangeItem] = field(default_factory=list)
    key_traces: List[Dict[str, Any]] = field(default_factory=list)
    analysis_summary: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "transaction_hash": self.basic_info.txn_hash,
            "chain_id": self.basic_info.chain_id,
            "basic_info": {
                "status": self.basic_info.status,
                "timestamp": self.basic_info.timestamp,
                "block_number": self.basic_info.block_number,
                "gas_used": self.basic_info.gas_used,
                "sender": self.basic_info.sender,
                "receiver": self.basic_info.receiver,
            },
            "attacker": {
                "address": self.attacker.address if self.attacker else None,
                "label": self.attacker.label if self.attacker else None,
                "profit": str(self.attacker.profit_loss) if self.attacker and self.attacker.profit_loss else None,
            } if self.attacker else None,
            "victim": {
                "address": self.victim.address if self.victim else None,
                "label": self.victim.label if self.victim else None,
                "loss": str(self.victim.profit_loss) if self.victim and self.victim.profit_loss else None,
            } if self.victim else None,
            "loss_amount_usd": str(self.loss_amount_usd) if self.loss_amount_usd else None,
            "vulnerability_type": self.vulnerability_type,
            "fund_flow_count": len(self.fund_flow),
            "state_changes_count": len(self.state_changes),
            "suspicious_state_changes": sum(1 for sc in self.state_changes if sc.is_suspicious),
            "analysis_summary": self.analysis_summary,
        }
    
    def to_markdown(self) -> str:
        """生成 Markdown 格式的报告"""
        lines = ["# 安全事件分析报告\n"]
        
        # 基础信息
        lines.append("## 事件概览\n")
        lines.append(f"- **交易哈希**: `{self.basic_info.txn_hash}`")
        lines.append(f"- **链ID**: {self.basic_info.chain_id}")
        lines.append(f"- **状态**: {self.basic_info.status}")
        lines.append(f"- **区块高度**: {self.basic_info.block_number}")
        lines.append(f"- **时间戳**: {self.basic_info.timestamp}")
        lines.append(f"- **Gas消耗**: {self.basic_info.gas_used}")
        lines.append(f"- **发送者**: `{self.basic_info.sender}`")
        lines.append(f"- **接收者**: `{self.basic_info.receiver}`\n")
        
        # 攻击者和受害者
        lines.append("## 攻击者与受害者\n")
        if self.attacker:
            lines.append(f"### 攻击者")
            lines.append(f"- **地址**: `{self.attacker.address}`")
            if self.attacker.label:
                lines.append(f"- **标签**: {self.attacker.label}")
            if self.attacker.profit_loss:
                lines.append(f"- **获利**: ${self.attacker.profit_loss:,.2f}\n")
        
        if self.victim:
            lines.append(f"### 受害者")
            lines.append(f"- **地址**: `{self.victim.address}`")
            if self.victim.label:
                lines.append(f"- **标签**: {self.victim.label}")
            if self.victim.profit_loss:
                lines.append(f"- **损失**: ${abs(self.victim.profit_loss):,.2f}\n")
        
        # 漏洞类型
        if self.vulnerability_type:
            lines.append("## 漏洞类型\n")
            lines.append(f"{self.vulnerability_type}\n")
        
        # 资金流向
        if self.fund_flow:
            lines.append("## 资金流向\n")
            for flow in self.fund_flow[:10]:  # 只显示前10条
                from_label = f" ({flow.from_label})" if flow.from_label else ""
                to_label = f" ({flow.to_label})" if flow.to_label else ""
                lines.append(f"{flow.order}. `{flow.from_address}`{from_label} → `{flow.to_address}`{to_label}")
                lines.append(f"   - Token: `{flow.token}`, Amount: `{flow.amount}`")
            if len(self.fund_flow) > 10:
                lines.append(f"\n... 还有 {len(self.fund_flow) - 10} 条资金流动记录\n")
        
        # 状态变化
        if self.state_changes:
            lines.append("## 可疑状态变化\n")
            suspicious = [sc for sc in self.state_changes if sc.is_suspicious]
            for sc in suspicious:
                lines.append(f"### 合约: `{sc.contract_address}`")
                lines.append(f"- **变量**: `{sc.variable_name}` ({sc.variable_type})")
                lines.append(f"- **原值**: `{sc.prev_value}`")
                lines.append(f"- **新值**: `{sc.current_value}` ⚠️\n")
        
        # 分析总结
        if self.analysis_summary:
            lines.append("## 分析总结\n")
            lines.append(self.analysis_summary + "\n")
        
        return "\n".join(lines)
