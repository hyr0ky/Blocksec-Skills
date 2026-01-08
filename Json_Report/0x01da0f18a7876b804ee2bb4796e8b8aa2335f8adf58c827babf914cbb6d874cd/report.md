# 安全事件分析报告

## 事件概览

- **交易哈希**: `0x01da0f18a7876b804ee2bb4796e8b8aa2335f8adf58c827babf914cbb6d874cd`
- **链ID**: 1
- **状态**: True
- **区块高度**: 24147099
- **时间戳**: 1767358691000
- **Gas消耗**: 5727364
- **发送者**: `0x7fdbfb45aa3f5345f9b6ae7c6afc2b190cfcded2`
- **接收者**: `0x903f2374d5e17d4789cc6feab60e3e43fa04ed47`

## 攻击者与受害者

### 攻击者
- **地址**: `0xa43fe16908251ee70ef74718545e4fe6c5ccec9f`
- **标签**: 0xa43f_UNI-V2
### 受害者
- **地址**: `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91`
- **标签**: 0xa89f_PEPESTR
## 资金流向

1. `0xbbbbbbbbbb9cc5e90e3b3af64bdaf62c37eeffcb` (Morpho: Morpho Blue) → `0x7f07e5771e32f76b86e9b0ab42834f689ce4b045`
   - Token: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`, Amount: `4,500`
2. `0xbbbbbbbbbb9cc5e90e3b3af64bdaf62c37eeffcb` (Morpho: Morpho Blue) → `0x7f07e5771e32f76b86e9b0ab42834f689ce4b045`
   - Token: `0xcbb7c0000ab88b473b1f5afd9ef808440eed33bf`, Amount: `1`
3. `0x7f07e5771e32f76b86e9b0ab42834f689ce4b045` → `0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f` (0xa72f_UNI-V2)
   - Token: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`, Amount: `6`
4. `0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f` (0xa72f_UNI-V2) → `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91` (0xa89f_PEPESTR)
   - Token: `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91`, Amount: `59,719,108.165571866568244111`
5. `0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f` (0xa72f_UNI-V2) → `0x7f07e5771e32f76b86e9b0ab42834f689ce4b045`
   - Token: `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91`, Amount: `448,348,323.625302073129437855`
6. `0x7f07e5771e32f76b86e9b0ab42834f689ce4b045` → `0x5f9b7e441e00373a83eee20f1366a7d32ec53d56` (0x5f9b_UNI-V2)
   - Token: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`, Amount: `3.59`
7. `0x5f9b7e441e00373a83eee20f1366a7d32ec53d56` (0x5f9b_UNI-V2) → `0x4250569cdce5065c96b597b5982f6e6d9c329714` (0x4250_PEPESTR)
   - Token: `0x4250569cdce5065c96b597b5982f6e6d9c329714`, Amount: `50,353,342.487915184800334257`
8. `0x5f9b7e441e00373a83eee20f1366a7d32ec53d56` (0x5f9b_UNI-V2) → `0x7f07e5771e32f76b86e9b0ab42834f689ce4b045`
   - Token: `0x4250569cdce5065c96b597b5982f6e6d9c329714`, Amount: `354,778,079.87235750337675752`
9. `0x7f07e5771e32f76b86e9b0ab42834f689ce4b045` → `0xa43fe16908251ee70ef74718545e4fe6c5ccec9f` (0xa43f_UNI-V2)
   - Token: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`, Amount: `2,105`
10. `0xa43fe16908251ee70ef74718545e4fe6c5ccec9f` (0xa43f_UNI-V2) → `0x7f07e5771e32f76b86e9b0ab42834f689ce4b045`
   - Token: `0x6982508145454ce325ddbe47a25d4ec3d2311933`, Amount: `845,624,308,749.904152023446754379`

... 还有 41 条资金流动记录

## 可疑状态变化

## 分析总结

本次安全事件中，攻击者 `0xa43fe16908251ee70ef74718545e4fe6c5ccec9f` 对受害合约 `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91` 发起了攻击。
资金流动共 51 笔。
