# 关键函数调用与代码映射

> **分析范围**: 攻击者直接调用 + 攻击合约调用外部 + 受害者合约被调用

> **攻击者创建的合约**: 2 个
>   - `0xfbb9224f20163a044dd2cb55f01a94e0fd140a24`
>   - `0xc8d7963a59f0c298822c3d42931fa2bab9065825`

## Trace
```text
[1] CREATE 0xfbb922...140a24 -> 0xc8d796...065825 ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=244479, value=0

[2] CALL 0xfbb922...140a24 -> 0xc8d796...065825 ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=279861, value=0

[3] CALL 0xc8d796...065825 -> 0x000000...e08a90(Uniswap V4: Pool Manager) :: unlock(bytes) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=271381, value=0
      args: data:bytes=0x

[5] CALL 0xc8d796...065825 -> 0x000000...e08a90(Uniswap V4: Pool Manager) :: take(address,address,uint256) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=8223, value=0
      args: currency:address=0x0000000000000000000000000000000000000000, to:address=0xc8d7963a59f0c298822c3d42931fa2bab9065825, amount:uint256=3,000,000,000,000,000,000

[7] CALL 0xc8d796...065825 -> 0xe6329d...dca145 ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=81744, value=0.1

[23] CALL 0xc8d796...065825 -> 0xe6329d...dca145 ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=80282, value=0.9

[73] CALL 0xc8d796...065825 -> 0xe6329d...dca145 ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=66562, value=1.699999999999999998

[123] CALL 0xc8d796...065825 -> 0x000000...e08a90(Uniswap V4: Pool Manager) :: settle() ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=1273, value=3

[124] SELFDESTRUCT 0xc8d796...065825 -> 0xfbb922...140a24 ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=0, value=0.566666666666666636

[0] CREATE 0xb56125...1d444c -> 0xfbb922...140a24 ⚠️ (攻击者直接调用)
      status=OK, gasUsed=637557, value=0

[125] SELFDESTRUCT 0xfbb922...140a24 -> 0xb56125...1d444c ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=0, value=0.566666666666666636

```

## Code
### unknown()
**合约地址:** `0xc8d7963a59f0c298822c3d42931fa2bab9065825`
**调用类型:** 攻击合约调用外部

```text
未找到函数定义位置
```

### unlock(bytes)
**合约地址:** `0x000000000004444c5dc75cb358380d2e3de08a90`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `PoolManager.sol`

```solidity
 103 |     function unlock(bytes calldata data) external override returns (bytes memory result) {
 104 |         if (Lock.isUnlocked()) AlreadyUnlocked.selector.revertWith();
 105 | 
 106 |         Lock.unlock();
 107 | 
 108 |         // the caller does everything in this callback, including paying what they owe via calls to settle
 109 |         result = IUnlockCallback(msg.sender).unlockCallback(data);
 110 | 
 111 |         if (NonzeroDeltaCount.read() != 0) CurrencyNotSettled.selector.revertWith();
 112 |         Lock.lock();
 113 |     }
```

### take(address,address,uint256)
**合约地址:** `0x000000000004444c5dc75cb358380d2e3de08a90`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `PoolManager.sol`

```solidity
 289 |     function take(Currency currency, address to, uint256 amount) external onlyWhenUnlocked {
 290 |         unchecked {
 291 |             // negation must be safe as amount is not negative
 292 |             _accountDelta(currency, -(amount.toInt128()), msg.sender);
 293 |             currency.transfer(to, amount);
 294 |         }
 295 |     }
```

### unknown()
**合约地址:** `0xe6329d65ebcc5cbccdd719d7b18ac9e220dca145`
**调用类型:** 攻击合约调用外部

```text
未找到函数定义位置
```

### settle()
**合约地址:** `0x000000000004444c5dc75cb358380d2e3de08a90`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `PoolManager.sol`

```solidity
 298 |     function settle() external payable onlyWhenUnlocked returns (uint256) {
 299 |         return _settle(msg.sender);
 300 |     }
```

### unknown()
**合约地址:** `0xfbb9224f20163a044dd2cb55f01a94e0fd140a24`
**调用类型:** 攻击合约调用外部

```text
未找到函数定义位置
```

### unknown()
**合约地址:** `0xb561258b4bf282d1e5329d675b6f399d691d444c`
**调用类型:** 攻击合约调用外部

```text
未找到函数定义位置
```
