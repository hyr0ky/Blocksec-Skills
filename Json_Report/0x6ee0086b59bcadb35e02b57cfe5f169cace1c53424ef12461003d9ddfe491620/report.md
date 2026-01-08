# 安全事件分析报告

## 事件概览

- **交易哈希**: `0x6ee0086b59bcadb35e02b57cfe5f169cace1c53424ef12461003d9ddfe491620`
- **链ID**: 56
- **状态**: True
- **区块高度**: 71642266
- **时间戳**: 1765733499000
- **Gas消耗**: 1358855
- **发送者**: `0xdbdcc7625c993253ea38d2cc7ec0b00aea23022f`
- **接收者**: `0x724c2be714e21299917ee8a2b69cf0bfd09b9a55`

## 攻击者与受害者

### 攻击者
- **地址**: `0x724c2be714e21299917ee8a2b69cf0bfd09b9a55`
### 受害者
- **地址**: `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f`
- **标签**: WADJET
## 资金流向

1. `0x8f73b65b4caaf64fba2af91cc5d4a2a1318e5d8c` (ERC1967Proxy) → `0x724c2be714e21299917ee8a2b69cf0bfd09b9a55`
   - Token: `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`, Amount: `22.22`
2. `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c` (WBNB) → `0x724c2be714e21299917ee8a2b69cf0bfd09b9a55`
   - Token: `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`, Amount: `22.22`
3. `0x724c2be714e21299917ee8a2b69cf0bfd09b9a55` → `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c` (WBNB)
   - Token: `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`, Amount: `22.22`
4. `0x724c2be714e21299917ee8a2b69cf0bfd09b9a55` → `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f` (WADJET)
   - Token: `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`, Amount: `22.22`
5. `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f` (WADJET) → `0xd79a0810810a203a7ce90b116a2e6cb411e50761`
   - Token: `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`, Amount: `4.464061279232036044`
6. `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f` (WADJET) → `0xd0fe8275a0f9255a33f53a8ccc2f1bb5ef113d30`
   - Token: `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`, Amount: `4.464061279232036044`
7. `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f` (WADJET) → `0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1`
   - Token: `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`, Amount: `4.464061279232036044`
8. `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f` (WADJET) → `0xd2b31e62fe910594bc034cfd5d805fba8c655727`
   - Token: `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`, Amount: `4.464061279232036044`
9. `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f` (WADJET) → `0x8ef857e9b92e3bd503c9495d5ecc16f09f71df19`
   - Token: `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`, Amount: `4.464061279232036044`
10. `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f` (WADJET) → `0x1f28a74214f7ea6f1badb74f7ce3e15ebec14c28`
   - Token: `0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`, Amount: `19.542806396160180224`

... 还有 4 条资金流动记录

## 可疑状态变化

## 分析总结

本次安全事件中，攻击者 `0x724c2be714e21299917ee8a2b69cf0bfd09b9a55` 对受害合约 `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f` 发起了攻击。
资金流动共 14 笔。
