# MSCST Atomic Sandwich Attack 案例

## 案例信息
- **交易哈希:** 0x6c9ed4c2d81b6abfdf297b0cbc13585ed91f2a5e69e3545d3ea4316f50021b56
- **链:** BSC (Chain ID: 56)
- **攻击类型:** Atomic Sandwich Attack
- **漏洞函数:** `releaseReward(uint256)`

## 攻击合约结构

```markdown
> **攻击者创建的合约**: 2 个
>   - `0x486da49a56b564b824ea140fa4a5ff74de6cf34b` (攻击者直接创建)
>   - `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5` (第2层子合约)
```

## 关键 Trace

```text
[84] CALL 0x1e70f1...2291e5 -> 0x91334d...59aeb1(MSCST) :: releaseReward(uint256) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=143280, value=0
      args: fee:uint256=13,329,580,007,446,108,335,195,360
```

## 漏洞函数代码

```solidity
325 |     function releaseReward(uint256 fee) public{  ← ⚠️ 没有权限控制！
326 | 
327 |         uint256 burnFee = fee/2;
328 |         uint256 profitFee = fee-burnFee;
329 |         swapTokenForGPC(burnFee,uniswapV2PairGpc);
330 |         IPancakePair(uniswapV2PairGpc).sync();
331 |         IERC20(msc).safeTransfer(profit,profitFee);
332 |     }
```

## 分析逻辑

1. **3-token 系统结构:**
   - MSC: 质押代币（只能与 GPC 配对）
   - GPC: 中间代币（与 BNB 有交易对）
   - BNB: 价值出口（唯一的稳定价值）

2. **攻击流程:**
   ```
   前置交易: GPC → BNB（在 GPC-BNB 池子卖出 GPC）
   中间交易: 调用 releaseReward(fee = MSC.balanceOf(MSCST))
             → 用合约全部 MSC 购买 GPC
             → GPC 转入 GPC-BNB 池子（增加供应）
             → sync() 更新储备量
             → GPC 价格下降 ⚠️
   后置交易: BNB → GPC（以更低价格买回 GPC）
   ```

3. **漏洞特征:**
   - ❌ 函数是 `public` 且没有任何权限修饰符
   - ❌ 没有参数验证（可传入合约全部余额）
   - ❌ 函数会向池子转入大量代币（改变供应）
   - ❌ 调用 `sync()` 更新储备量

4. **攻击类型:** Atomic Sandwich Attack + 访问控制缺失

5. **获利:** 约 150 WBNB

## 关键教训

1. **不要过度关注"访问控制缺失"**
   - 虽然没有权限控制是问题
   - 但更核心的问题是**函数会向池子转入大量代币**

2. **理解函数的副作用**
   - `releaseReward()` 表面作用：释放奖励
   - 真正副作用：向 GPC-BNB 池子注入大量 GPC
   - **副作用才是攻击的核心利用点**

3. **识别 Atomic Sandwich 模式**
   - 攻击者控制中间交易（通过调用合约函数）
   - 在一个原子交易内完成前置/中间/后置三步
   - 与传统 Sandwich（等待受害者交易）不同
