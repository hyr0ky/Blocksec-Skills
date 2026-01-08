# 关键函数调用与代码映射

> **分析范围**: 攻击者直接调用 + 攻击合约调用外部 + 受害者合约被调用

## Trace
```text
[15] CALL 0xbcda9e...f6a8c2(sil) -> 0x2a11cc...035f3d(0x2a11_SLP) :: transfer(address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=29876, value=0
      args: to:address=0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d, value:uint256=4,000,000,000

[21] CALL 0xbcda9e...f6a8c2(sil) -> 0x2a11cc...035f3d(0x2a11_SLP) :: burn(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=119059, value=0
      args: to:address=0xbcda9e0658f4eecf56a0bd099e6dbc0c91f6a8c2

```

## Code
### transfer(address,uint256)
**合约地址:** `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d`
**调用类型:** 受害者合约被调用

**函数定义文件:** `UniswapV2Pair.sol`

```solidity
 110 |     function transfer(address to, uint value) external returns (bool) {
 111 |         _transfer(msg.sender, to, value);
 112 |         return true;
 113 |     }
```

**调用位置:** `SushiswapV2SingleSidedILProtection.sol` (行 45-45)

```solidity
  45 |         (bool success, bytes memory returndata) = address(token).call(data);
```

### burn(address)
**合约地址:** `0x2a11ccfb96223bd35ec24b2aac046fcc85035f3d`
**调用类型:** 受害者合约被调用

**函数定义文件:** `UniswapV2Pair.sol`

```solidity
 361 |     function burn(address to) external lock returns (uint amount0, uint amount1) {
 362 |         (uint112 _reserve0, uint112 _reserve1,) = getReserves(); // gas savings
 363 |         address _token0 = token0;                                // gas savings
 364 |         address _token1 = token1;                                // gas savings
 365 |         uint balance0 = IERC20Uniswap(_token0).balanceOf(address(this));
 366 |         uint balance1 = IERC20Uniswap(_token1).balanceOf(address(this));
 367 |         uint liquidity = balanceOf[address(this)];
 368 | 
 369 |         bool feeOn = _mintFee(_reserve0, _reserve1);
 370 |         uint _totalSupply = totalSupply; // gas savings, must be defined here since totalSupply can update in _mintFee
 371 |         amount0 = liquidity.mul(balance0) / _totalSupply; // using balances ensures pro-rata distribution
 372 |         amount1 = liquidity.mul(balance1) / _totalSupply; // using balances ensures pro-rata distribution
 373 |         require(amount0 > 0 && amount1 > 0, 'UniswapV2: INSUFFICIENT_LIQUIDITY_BURNED');
 374 |         _burn(address(this), liquidity);
 375 |         _safeTransfer(_token0, to, amount0);
 376 |         _safeTransfer(_token1, to, amount1);
 377 |         balance0 = IERC20Uniswap(_token0).balanceOf(address(this));
 378 |         balance1 = IERC20Uniswap(_token1).balanceOf(address(this));
 379 | 
 380 |         _update(balance0, balance1, _reserve0, _reserve1);
 381 |         if (feeOn) kLast = uint(reserve0).mul(reserve1); // reserve0 and reserve1 are up-to-date
 382 |         emit Burn(msg.sender, amount0, amount1, to);
 383 |     }
```

**调用位置:** `SushiswapV2SingleSidedILProtection.sol` (行 348-348)

```solidity
 348 |         (uint amountA, uint amountB) = ISushiswapV2Pair(pair).burn(address(this));
```
