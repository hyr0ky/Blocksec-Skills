# 安全事件分析报告

## 事件概览

- **交易哈希**: `0xcc1884e9934d516df9d80a38706bc0fa1d4437e0cd3d02a4b2e4e95fafe94dfe`
- **链ID**: 56
- **状态**: True
- **区块高度**: 67717829
- **时间戳**: 1762789374000
- **Gas消耗**: 7215204
- **发送者**: `0xc484ecd341f8e02d6685da4f6670684a7675303b`
- **接收者**: `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a`

## 攻击者与受害者

### 攻击者
- **地址**: `0xc484ecd341f8e02d6685da4f6670684a7675303b`
- **标签**: Unidentified Exploiter
### 受害者
- **地址**: `0x480f51beded3fc0c42f4a86f923700ea7859fbba`
- **标签**: Cake-LP
## 资金流向

1. `0xc484ecd341f8e02d6685da4f6670684a7675303b` (Unidentified Exploiter) → `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a`
   - Token: `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`, Amount: `0.0001`
2. `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a` → `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c` (WBNB)
   - Token: `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`, Amount: `0.0001`
3. `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c` (WBNB) → `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a`
   - Token: `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`, Amount: `0.0001`
4. `0xb67e5eaf770a384ab28029d08b9bc5ebe32beb0f` (0xb67e_PancakeV3Pool) → `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a`
   - Token: `0x55d398326f99059ff775485246999027b3197955`, Amount: `138,569,971.449597288562091805`
5. `0x92b7807bf19b7dddf89b706143896d05228f3121` (0x92b7_PancakeV3Pool) → `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a`
   - Token: `0x55d398326f99059ff775485246999027b3197955`, Amount: `24,110,094.318067589694287385`
6. `0xcf59b8c8baa2dea520e3d549f97d4e49ade17057` (0xcf59_PancakeV3Pool) → `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a`
   - Token: `0x55d398326f99059ff775485246999027b3197955`, Amount: `18,254,187.370694200162345167`
7. `0x81c7294b66955824bc04acb642ae8dc58e6ce507` (0x81c7_UniswapV3Pool) → `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a`
   - Token: `0x55d398326f99059ff775485246999027b3197955`, Amount: `7,798,457.689119955579137756`
8. `0x9c4ee895e4f6ce07ada631c508d1306db7502cce` (0x9c4e_PancakeV3Pool) → `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a`
   - Token: `0x55d398326f99059ff775485246999027b3197955`, Amount: `6,279,071.523429635137551349`
9. `0x9f8f4615ff5143aee365fa34f34196fb85be7650` (0x9f8f_PancakeV3Pool) → `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a`
   - Token: `0x55d398326f99059ff775485246999027b3197955`, Amount: `3,597,051.004623833291130212`
10. `0x172fcd41e0913e95784454622d1c3724f546f849` (0x172f_PancakeV3Pool) → `0xfc8311f5242be8165ff3c005b9db16e62cebbe1a`
   - Token: `0x55d398326f99059ff775485246999027b3197955`, Amount: `5,145,182.954994078026174644`

... 还有 149 条资金流动记录

## 可疑状态变化

## 分析总结

本次安全事件中，攻击者 `0xc484ecd341f8e02d6685da4f6670684a7675303b` 对受害合约 `0x480f51beded3fc0c42f4a86f923700ea7859fbba` 发起了攻击。
资金流动共 159 笔。
