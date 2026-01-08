"""
数据模型

定义项目中使用的数据结构
"""

from .transaction import (
    TransactionBasicInfo,
    AddressInfo,
    FundFlowItem,
    StateChangeItem,
    VulnerabilityReport,
)

__all__ = [
    'TransactionBasicInfo',
    'AddressInfo',
    'FundFlowItem',
    'StateChangeItem',
    'VulnerabilityReport',
]
