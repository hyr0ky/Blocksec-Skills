# 安全事件分析报告

## 事件概览

- **交易哈希**: `0x7f1406435172b8d8675dec95a7f6aa89d10b7ca008150de8742f7fa824e3395c`
- **链ID**: 1
- **状态**: True
- **区块高度**: 24151247
- **时间戳**: 1767408683000
- **Gas消耗**: 3166007
- **发送者**: `0xed5a324865875dc7fadbb2f4fe43fce78a118391`
- **接收者**: `0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0`

## 攻击者与受害者

### 攻击者
- **地址**: `0xed5a324865875dc7fadbb2f4fe43fce78a118391`
- **标签**: Valinity DeFi Exploiter
### 受害者
- **地址**: `0x86e811bbb86348753195bef72e200e946133250a`
- **标签**: ValinityReserveTreasury
## 资金流向

1. `0xbbbbbbbbbb9cc5e90e3b3af64bdaf62c37eeffcb` (Morpho: Morpho Blue) → `0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0`
   - Token: `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`, Amount: `177,535`
2. `0xb431c70f800100d87554ac1142c4a94c5fe4c0c4` (Uniswap: V3 Pool) → `0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0`
   - Token: `0x45804880de22913dafe09f4980848ece6ecbaf78`, Amount: `16.780164999839019699`
3. `0xb431c70f800100d87554ac1142c4a94c5fe4c0c4` (Uniswap: V3 Pool) → `0x38699d04656ff537ef8671b6b595402ebdbdf6f4`
   - Token: `0x45804880de22913dafe09f4980848ece6ecbaf78`, Amount: `0`
4. `0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0` → `0xb431c70f800100d87554ac1142c4a94c5fe4c0c4` (Uniswap: V3 Pool)
   - Token: `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`, Amount: `177,515`
5. `0x0000000000000000000000000000000000000000` → `0x7f00dbc381f81da281faf1fee3bbb35f60b9f8e6` (ValinityAcquisitionTreasury)
   - Token: `0x768f408bbafa6d5bdc7386e84834f37aa7389a94`, Amount: `39,645,619.576378794699219855`
6. `0x7f00dbc381f81da281faf1fee3bbb35f60b9f8e6` (ValinityAcquisitionTreasury) → `0xf5b31637ba156bd876bc7e2d71bc9237654a485a` (0xf5b3_ERC1967Proxy)
   - Token: `0x768f408bbafa6d5bdc7386e84834f37aa7389a94`, Amount: `39,645,619.576378794699219855`
7. `0xf5b31637ba156bd876bc7e2d71bc9237654a485a` (0xf5b3_ERC1967Proxy) → `0x8c86bc7d11a5817357a8d897a0cd636078b6d2d9`
   - Token: `0x768f408bbafa6d5bdc7386e84834f37aa7389a94`, Amount: `396,456.195763787946992198`
8. `0xf5b31637ba156bd876bc7e2d71bc9237654a485a` (0xf5b3_ERC1967Proxy) → `0x43f485702ea85546b5ed91cb836c1bc130e5ef19` (UNI-V2)
   - Token: `0x768f408bbafa6d5bdc7386e84834f37aa7389a94`, Amount: `39,249,163.380615006752227657`
9. `0x43f485702ea85546b5ed91cb836c1bc130e5ef19` (UNI-V2) → `0xf5b31637ba156bd876bc7e2d71bc9237654a485a` (0xf5b3_ERC1967Proxy)
   - Token: `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`, Amount: `106.072372`
10. `0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8` (Uniswap V3: USDC 2) → `0x86e811bbb86348753195bef72e200e946133250a` (ValinityReserveTreasury)
   - Token: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`, Amount: `0.033801983873772348`

... 还有 31 条资金流动记录

## 可疑状态变化

## 分析总结

本次安全事件中，攻击者 `0xed5a324865875dc7fadbb2f4fe43fce78a118391` 对受害合约 `0x86e811bbb86348753195bef72e200e946133250a` 发起了攻击。
资金流动共 41 笔。
