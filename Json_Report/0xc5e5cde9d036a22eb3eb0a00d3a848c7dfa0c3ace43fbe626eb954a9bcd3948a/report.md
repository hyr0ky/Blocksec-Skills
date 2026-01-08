# 安全事件分析报告

## 事件概览

- **交易哈希**: `0xc5e5cde9d036a22eb3eb0a00d3a848c7dfa0c3ace43fbe626eb954a9bcd3948a`
- **链ID**: 1
- **状态**: True
- **区块高度**: 23577734
- **时间戳**: 1760466587000
- **Gas消耗**: 450554
- **发送者**: `0x706ccdc380bae0ee0288cfcf833e45e387f29769`
- **接收者**: `0x2b899428178821a053c61c099e3cdc9c89e2179d`

## 攻击者与受害者

### 攻击者
- **地址**: `0x0000000000000000000000000000000000000000`
### 受害者
- **地址**: `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d`
- **标签**: 0x2a11_SLP
## 资金流向

1. `0xbcda9e0658f4eecf56a0bd099e6dbc0c91f6a8c2` (sil) → `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d` (0x2a11_SLP)
   - Token: `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d`, Amount: `0.000000004`
2. `0x0000000000000000000000000000000000000000` → `0x5ad6211cd3fde39a9cecb5df6f380b8263d1e277` (SushiSwap: WethMaker)
   - Token: `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d`, Amount: `0.000000000001132443`
3. `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d` (0x2a11_SLP) → `0x0000000000000000000000000000000000000000`
   - Token: `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d`, Amount: `0.000000004`
4. `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d` (0x2a11_SLP) → `0xbcda9e0658f4eecf56a0bd099e6dbc0c91f6a8c2` (sil)
   - Token: `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599`, Amount: `0.18859151`
5. `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d` (0x2a11_SLP) → `0xbcda9e0658f4eecf56a0bd099e6dbc0c91f6a8c2` (sil)
   - Token: `0xbcda9e0658f4eecf56a0bd099e6dbc0c91f6a8c2`, Amount: `9,102.42933684`
6. `0xbcda9e0658f4eecf56a0bd099e6dbc0c91f6a8c2` (sil) → `0xd9d097b05862b73269e6eecd2e9912a815bbe7d6`
   - Token: `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599`, Amount: `0.18859151`
7. `0xbcda9e0658f4eecf56a0bd099e6dbc0c91f6a8c2` (sil) → `0xd9d097b05862b73269e6eecd2e9912a815bbe7d6`
   - Token: `0xbcda9e0658f4eecf56a0bd099e6dbc0c91f6a8c2`, Amount: `9,102.42933684`
8. `0xd9d097b05862b73269e6eecd2e9912a815bbe7d6` → `0x0000000000000000000000000000000000000000`
   - Token: `0xbcda9e0658f4eecf56a0bd099e6dbc0c91f6a8c2`, Amount: `8,012.9353975`
9. `0xd9d097b05862b73269e6eecd2e9912a815bbe7d6` → `0x2b899428178821a053c61c099e3cdc9c89e2179d`
   - Token: `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599`, Amount: `0.18859151`
10. `0x2b899428178821a053c61c099e3cdc9c89e2179d` → `0xceff51756c56ceffca006cd410b03ffc46dd3a58` (0xceff_SLP)
   - Token: `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599`, Amount: `0.003`

... 还有 5 条资金流动记录

## 可疑状态变化

## 分析总结

本次安全事件中，攻击者 `0x0000000000000000000000000000000000000000` 对受害合约 `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d` 发起了攻击。
资金流动共 15 笔。
