# 安全事件分析报告

## 事件概览

- **交易哈希**: `0x6c9ed4c2d81b6abfdf297b0cbc13585ed91f2a5e69e3545d3ea4316f50021b56`
- **链ID**: 56
- **状态**: True
- **区块高度**: 73309656
- **时间戳**: 1766984382000
- **Gas消耗**: 1441528
- **发送者**: `0xb0720d8541cd2b6fc35ccc39ec84e84383a7000b`
- **接收者**: `0x486da49a56b564b824ea140fa4a5ff74de6cf34b`

## 攻击者与受害者

### 攻击者
- **地址**: `0xb0720d8541cd2b6fc35ccc39ec84e84383a7000b`
- **标签**: Unidentified Exploiter
### 受害者
- **地址**: `0x12dabfce08ef59c24cdee6c488e05179fb8d64d9`
- **标签**: 0x12da_Cake-LP
## 资金流向

1. `0xe3cba5c0a8efaedce84751af2efddcf071d311a9` (0xe3cb_Cake-LP) → `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5`
   - Token: `0xd3c304697f63b279cd314f92c19cdbe5e5b1631a`, Amount: `46,841,803.215322280406440238`
2. `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5` → `0x12dabfce08ef59c24cdee6c488e05179fb8d64d9` (0x12da_Cake-LP)
   - Token: `0xd3c304697f63b279cd314f92c19cdbe5e5b1631a`, Amount: `46,841,803.215322280406440238`
3. `0x12dabfce08ef59c24cdee6c488e05179fb8d64d9` (0x12da_Cake-LP) → `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5`
   - Token: `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`, Amount: `205.635720265951753886`
4. `0x91334d03dd9b9de8d48b50fe389337eeb759aeb1` (MSCST) → `0xaae35c003a323d291b7293618506aa612302b7cf` (0xaae3_Cake-LP)
   - Token: `0x713630359cc9046869ad1642a7b61c23956425cc`, Amount: `6,664,790.00372305416759768`
5. `0xaae35c003a323d291b7293618506aa612302b7cf` (0xaae3_Cake-LP) → `0x12dabfce08ef59c24cdee6c488e05179fb8d64d9` (0x12da_Cake-LP)
   - Token: `0xd3c304697f63b279cd314f92c19cdbe5e5b1631a`, Amount: `71,551,581.422663723226014917`
6. `0x91334d03dd9b9de8d48b50fe389337eeb759aeb1` (MSCST) → `0x6278fa23fbe28b9736214e03cf2030f5ee1ccac9` (GnosisSafeProxy)
   - Token: `0x713630359cc9046869ad1642a7b61c23956425cc`, Amount: `6,664,790.00372305416759768`
7. `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5` → `0x12dabfce08ef59c24cdee6c488e05179fb8d64d9` (0x12da_Cake-LP)
   - Token: `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`, Amount: `55.891753120913728774`
8. `0x12dabfce08ef59c24cdee6c488e05179fb8d64d9` (0x12da_Cake-LP) → `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5`
   - Token: `0xd3c304697f63b279cd314f92c19cdbe5e5b1631a`, Amount: `46,959,201.218368200908712019`
9. `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5` → `0xe3cba5c0a8efaedce84751af2efddcf071d311a9` (0xe3cb_Cake-LP)
   - Token: `0xd3c304697f63b279cd314f92c19cdbe5e5b1631a`, Amount: `46,959,201.218368200908712019`
10. `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5` → `0xb0720d8541cd2b6fc35ccc39ec84e84383a7000b` (Unidentified Exploiter)
   - Token: `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`, Amount: `149.743967145038025112`
## 可疑状态变化

## 分析总结

本次安全事件中，攻击者 `0xb0720d8541cd2b6fc35ccc39ec84e84383a7000b` 对受害合约 `0x12dabfce08ef59c24cdee6c488e05179fb8d64d9` 发起了攻击。
资金流动共 10 笔。
