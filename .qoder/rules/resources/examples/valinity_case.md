# Valinity DeFi Rebalancing 案例

## 案例信息
- **交易哈希:** 0x7f1406435172b8d8675dec95a7f6aa89d10b7ca008150de8742f7fa824e3395c
- **链:** Ethereum (Chain ID: 1)
- **攻击类型:** Rebalancing 触发 + 价格操纵
- **漏洞函数:** `acquireByLTVDisparity()`

## 3-token 系统结构
- **VY:** 协议的合成资产（可作为抵押品）
- **USDC:** 中间代币
- **PAXG/ETH/BTC:** 借贷资产

## 关键发现

### 漏洞函数
```solidity
function acquireByLTVDisparity() external nonReentrant returns (bool success) {
    // ... LTV 检查逻辑
    
    // 核心问题：硬编码到小流动性池
    _executeSwaps(netVY, fee, totalVY, targetAsset);
}

function _swapV2(address tokenIn, address tokenOut, address recipient, uint256 amountIn) internal {
    // ❌ 硬编码到流动性很少的 V2 池子（约 $106 USDC）
    uint256[] memory amounts = uniswapV2Router.swapExactTokensForTokens(
        amountIn, 
        0,  // ❌ 没有滑点保护
        path, 
        recipient, 
        block.timestamp + 300
    );
}
```

## 攻击流程

```
1. 攻击者 swap USDC → PAXG（抬高 PAXG 价格）

2. 触发 acquireByLTVDisparity() 函数
   → 由于新的 PAXG 价格，函数判断需要 rebalance
   → 铸造大量 VY 代币
   → 通过 _swapV2() 将 VY 换成 USDC
   → ⚠️ 关键：_swapV2 硬编码到一个几乎空的 UniV2 池子（~$106 USDC）
   → 39M VY 只换回 $106 USDC（异常交易）

3. 攻击者从小池子以极低价格买入 VY

4. 使用 VY 作为抵押品，从协议借出 eth/btc/paxg

5. 退出并获利
```

## 关键教训

1. **不是简单的"价格操纵"**
   - 攻击者是**抬高**借贷资产价格（而非降低）
   - 目的是触发协议的 rebalancing 机制

2. **关注协议的自动化机制**
   - `acquireByLTVDisparity()` 是 `external`，任何人都可以调用
   - 该函数会根据 LTV 差异自动 rebalance
   - 关键在于 `_swapV2()` 硬编码到小池子

3. **验证资金流向的合理性**
   - 39M VY 只换回 $106 USDC → 异常交易
   - 这说明池子流动性极少，是攻击的关键

4. **理解完整的业务逻辑链**
   - 从攻击者调用的 `swap()` 函数入手
   - 追踪到 `acquireByLTVDisparity()` → `_executeSwaps()` → `_swapV2()`
   - 发现硬编码小池子的问题

## 与 MSCST 的对比

| 维度 | Valinity DeFi | MSCST |
|------|---------------|-------|
| **攻击类型** | Rebalancing 触发 + 价格操纵 | Atomic Sandwich Attack |
| **触发函数** | `acquireByLTVDisparity()` | `releaseReward()` |
| **核心机制** | 硬编码到小流动性池 | 向池子注入大量代币 |
| **价格变化方式** | 大额交易到小池子 | 增加池子的代币供应 |
| **共同点** | 都是 `public/external` 无权限函数 | 都涉及 `sync()` 或储备量更新 |
