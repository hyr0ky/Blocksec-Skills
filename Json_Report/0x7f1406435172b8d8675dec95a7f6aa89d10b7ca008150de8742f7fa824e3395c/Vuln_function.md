# 关键函数调用与代码映射

> **分析范围**: 攻击者直接调用 + 攻击合约调用外部 + 受害者合约被调用

## Trace
```text
[0] CALL 0xed5a32...118391(Valinity DeFi Exploiter) -> 0x88f51f...7a82b0 :: swap(address,address,uint256,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=3166007, value=0
      args: _fromToken:address=0x7b4d07929c256367a47ec0d8ecebf6bf8fc2bf74, _toToken:address=0xf5b31637ba156bd876bc7e2d71bc9237654a485a, _amountIn:uint256=177,535,000,000, _minAmountOut:uint256=1,888,000,000,000,000,000

[941] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: increaseCollateralizedVY(address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=9424, value=0
      args: asset:address=0x45804880de22913dafe09f4980848ece6ecbaf78, vyAmount:uint256=38,400,273,000,000,000,000,000,000

[1058] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: increaseCollateralizedVY(address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=7424, value=0
      args: asset:address=0x2260fac5e5542a773aa44fbcfedf7c193bc2c599, vyAmount:uint256=19,800,000,000,000,000,000,000

[1157] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: increaseCollateralizedVY(address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=7424, value=0
      args: asset:address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, vyAmount:uint256=143,380,960,699,260,165,940,944

[961] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=23019, value=0
      args: asset:address=0x45804880de22913dafe09f4980848ece6ecbaf78, to:address=0x8c86bc7d11a5817357a8d897a0cd636078b6d2d9, amount:uint256=24,359,881,667,550,512

[981] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=11419, value=0
      args: asset:address=0x45804880de22913dafe09f4980848ece6ecbaf78, to:address=0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0, amount:uint256=2,411,628,285,087,500,719

[1078] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=14970, value=0
      args: asset:address=0x2260fac5e5542a773aa44fbcfedf7c193bc2c599, to:address=0x8c86bc7d11a5817357a8d897a0cd636078b6d2d9, amount:uint256=82,050

[1089] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=29270, value=0
      args: asset:address=0x2260fac5e5542a773aa44fbcfedf7c193bc2c599, to:address=0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0, amount:uint256=8,122,975

[1177] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=11329, value=0
      args: asset:address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, to:address=0x8c86bc7d11a5817357a8d897a0cd636078b6d2d9, amount:uint256=170,173,935,315,528,453

[1187] CALL 0x7b4d07...c2bf74(0x7b4d_ERC1967Proxy) -> 0x86e811...33250a(ValinityReserveTreasury) :: transferToken(address,address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=28429, value=0
      args: asset:address=0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2, to:address=0x7b4d07929c256367a47ec0d8ecebf6bf8fc2bf74, amount:uint256=16,847,219,596,237,316,941

```

## Code
### swap(address,address,uint256,uint256)
**合约地址:** `0x88f51f2c2c0b5b1ee60c6fadde7e5cc2aa7a82b0`
**调用类型:** 攻击者直接调用

```text
未找到函数定义位置
```

### increaseCollateralizedVY(address,uint256)
**合约地址:** `0x86e811bbb86348753195bef72e200e946133250a`
**调用类型:** 受害者合约被调用

**函数定义文件:** `ValinityReserveTreasury.sol`

```solidity
  52 |     function increaseCollateralizedVY(address asset, uint256 vyAmount) external onlyRole(OFFICER_ROLE) {
  53 |         if (asset == address(0)) {
  54 |             revert InvalidAsset();
  55 |         }
  56 |         if (vyAmount == 0) {
  57 |             revert ZeroAmount();
  58 |         }
  59 | 
  60 |         _collateralizedVY[asset] += vyAmount;
  61 | 
  62 |         emit CollateralizedVYUpdated(asset, int256(vyAmount));
  63 |     }
```

**调用位置:** `ValinityLoanOfficer.sol` (行 468-468)

```solidity
 468 |         ValinityReserveTreasury(_registrar.getContract(VRT)).decreaseCollateralizedVY(asset, vyAmount);
```

### transferToken(address,address,uint256)
**合约地址:** `0x86e811bbb86348753195bef72e200e946133250a`
**调用类型:** 受害者合约被调用

**函数定义文件:** `ValinityReserveTreasury.sol`

```solidity
  37 |     function transferToken(address asset, address to, uint256 amount) external onlyRole(OFFICER_ROLE) {
  38 |         if (amount == 0) {
  39 |             revert ZeroAmount();
  40 |         }
  41 |         if (asset == address(0)) {
  42 |             revert InvalidAsset();
  43 |         }
  44 | 
  45 |         IERC20 token = IERC20(asset);
  46 | 
  47 |         token.safeTransfer(to, amount);
  48 | 
  49 |         emit TokenTransferred(asset, to, amount);
  50 |     }
```

**调用位置:** `ValinityLoanOfficer.sol` (行 490-490)

```solidity
 490 |             vrt.transferToken(asset, processingFeeRecipient, fee);
```
