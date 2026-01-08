# 关键函数调用与代码映射

> **分析范围**: 攻击者直接调用 + 攻击合约调用外部 + 受害者合约被调用

## Trace
```text
[321] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: transfer(address,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=36806, value=0
      args: recipient:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, amount:uint256=559,895,451,526,345,725,040,240,046,257

[501] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: transfer(address,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=4106, value=0
      args: recipient:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, amount:uint256=43,977,465,419,499,361,191,837,514,604

[657] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: transfer(address,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=4106, value=0
      args: recipient:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, amount:uint256=241,751,391,804,059,065,791,369,193,518

[1262] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: transfer(address,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=4106, value=0
      args: recipient:address=0x4250569cdce5065c96b597b5982f6e6d9c329714, amount:uint256=1,668,594,984,594,785,041,041,914,948

[1330] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: transfer(address,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=4106, value=0
      args: recipient:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91, amount:uint256=1,497,773,934,185,705,183,558,875,637

[331] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=624, value=0
      args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[417] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=624, value=0
      args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[511] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=624, value=0
      args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[574] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=624, value=0
      args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[667] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=624, value=0
      args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[730] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=624, value=0
      args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[1272] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=624, value=0
      args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[1340] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=624, value=0
      args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[1400] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0x698250...311933(PEPE) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=624, value=0
      args: account:address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[333] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=534, value=0
      args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[419] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=534, value=0
      args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[513] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=534, value=0
      args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[576] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=534, value=0
      args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[669] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=534, value=0
      args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[732] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=534, value=0
      args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[1274] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=534, value=0
      args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[1342] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=534, value=0
      args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[1402] STATICCALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: balanceOf(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=534, value=0
      args: :address=0xa43fe16908251ee70ef74718545e4fe6c5ccec9f

[411] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: transfer(address,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=3262, value=0
      args: dst:address=0x5f9b7e441e00373a83eee20f1366a7d32ec53d56, wad:uint256=6,189,330,984,939,294,868

[568] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: transfer(address,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=3262, value=0
      args: dst:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, wad:uint256=6,291,836,319,852,228,923

[724] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: transfer(address,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=3262, value=0
      args: dst:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, wad:uint256=8,909,107,977,050,340,696

[1394] CALL 0xa43fe1...ccec9f(0xa43f_UNI-V2) -> 0xc02aaa...756cc2(WETH) :: transfer(address,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=3262, value=0
      args: dst:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, wad:uint256=2,091,978,752,136,290,103,338

[127] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: approve(address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=24700, value=0
      args: spender:address=0x7a250d5630b4cf539739df2c5dacb4c659f2488d, amount:uint256=115,792,089,237,316,195,423,570,985,008,687,907,853,269,984,665,640,564,039,457,584,007,913,129,639,935

[184] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=2598, value=0
      args: account:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045

[219] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f

[233] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045

[556] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=2598, value=0
      args: account:address=0x000000000000000000000000000000000000dead

[619] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f

[628] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0x000000000000000000000000000000000000dead

[712] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0x000000000000000000000000000000000000dead

[775] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f

[784] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0x000000000000000000000000000000000000dead

[793] STATICCALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045

[831] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f

[845] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f

[892] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f

[906] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f

[1080] STATICCALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f

[1094] STATICCALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: balanceOf(address) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=598, value=0
      args: account:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f

[196] CALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transfer(address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=61237, value=0
      args: recipient:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, amount:uint256=498,164,804,028,113,414,588,264,283

[593] CALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transfer(address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=16173, value=0
      args: recipient:address=0x000000000000000000000000000000000000dead, amount:uint256=66,873,000,451,532,696,492,459,691

[749] CALL 0xa72fec...a3fe6f(0xa72f_UNI-V2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transfer(address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=9373, value=0
      args: recipient:address=0x000000000000000000000000000000000000dead, amount:uint256=32,153,277,176,072,554,601,717,142

[1045] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transfer(address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=111023, value=0
      args: recipient:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, amount:uint256=1

[523] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: sellPepe(uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=152359, value=0
      args: orderId:uint256=8

[679] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: sellPepe(uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=130659, value=0
      args: orderId:uint256=5

[796] CALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transferFrom(address,address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=130995, value=0
      args: sender:address=0x7f07e5771e32f76b86e9b0ab42834f689ce4b045, recipient:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, amount:uint256=448,348,323,625,302,073,129,437,755

[814] CALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transferFrom(address,address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=9139, value=0
      args: sender:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91, recipient:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, amount:uint256=10,000,000,000,000,000,000,000,000

[1063] CALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: transferFrom(address,address,uint256) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=7139, value=0
      args: sender:address=0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91, recipient:address=0xa72fecc67208490fbf0eaf851ceea6e174a3fe6f, amount:uint256=10,000,000,000,000,000,000,000,000

[861] CALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=55, value=3.76040520678740417

[1110] CALL 0x7a250d...f2488d(Uniswap V2: Router 2) -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=55, value=0.053245868976619947

[1223] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) ⚠️ (受害者合约被调用)
      status=OK, gasUsed=55, value=1.288435604855704584

[1298] CALL 0x7f07e5...e4b045 -> 0xa89f4c...0e1f91(0xa89f_PEPESTR) :: buyPepe() ⚠️ (受害者合约被调用)
      status=OK, gasUsed=156101, value=0

```

## Code
### transfer(address,uint256)
**合约地址:** `0x6982508145454ce325ddbe47a25d4ec3d2311933`
**调用类型:** 攻击者直接调用

**函数定义文件:** `PepeToken.sol`

```solidity
 337 |     function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
 338 |         _transfer(_msgSender(), recipient, amount);
 339 |         return true;
 340 |     }
```

**调用位置:** `UniswapV2Pair.sol` (行 344-344)

```solidity
 344 |         (bool success, bytes memory data) = token.call(abi.encodeWithSelector(SELECTOR, to, value));
```

### balanceOf(address)
**合约地址:** `0x6982508145454ce325ddbe47a25d4ec3d2311933`
**调用类型:** 攻击者直接调用

**函数定义文件:** `PepeToken.sol`

```solidity
 325 |     function balanceOf(address account) public view virtual override returns (uint256) {
 326 |         return _balances[account];
 327 |     }
```

**调用位置:** `UniswapV2Pair.sol` (行 472-472)

```solidity
 472 |         balance0 = IERC20(_token0).balanceOf(address(this));
```

### balanceOf(address)
**合约地址:** `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`
**调用类型:** 攻击者直接调用

**函数定义文件:** `WETH9.sol`

```solidity
  28 |     mapping (address => uint)                       public  balanceOf;
```

**调用位置:** `UniswapV2Pair.sol` (行 473-473)

```solidity
 473 |         balance1 = IERC20(_token1).balanceOf(address(this));
```

### transfer(address,uint256)
**合约地址:** `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`
**调用类型:** 攻击者直接调用

**函数定义文件:** `WETH9.sol`

```solidity
  55 |     function transfer(address dst, uint wad) public returns (bool) {
  56 |         return transferFrom(msg.sender, dst, wad);
  57 |     }
```

**调用位置:** `UniswapV2Pair.sol` (行 344-344)

```solidity
 344 |         (bool success, bytes memory data) = token.call(abi.encodeWithSelector(SELECTOR, to, value));
```

### approve(address,uint256)
**合约地址:** `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91`
**调用类型:** 受害者合约被调用

**函数定义文件:** `PEPE_STRATEGY.sol`

```solidity
 773 |     function approve(address spender, uint256 amount) public virtual override returns (bool) {
 774 |         _approve(_msgSender(), spender, amount);
 775 |         return true;
 776 |     }
```

### balanceOf(address)
**合约地址:** `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91`
**调用类型:** 受害者合约被调用

**函数定义文件:** `PEPE_STRATEGY.sol`

```solidity
 742 |     function balanceOf(address account) public view virtual override returns (uint256) {
 743 |         return _balances[account];
 744 |     }
```

**调用位置:** `UniswapV2Router02.sol` (行 564-564)

```solidity
 564 |         uint balanceBefore = IERC20(path[path.length - 1]).balanceOf(to);
```

### transfer(address,uint256)
**合约地址:** `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91`
**调用类型:** 受害者合约被调用

**函数定义文件:** `PEPE_STRATEGY.sol`

```solidity
 754 |     function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
 755 |         _transfer(_msgSender(), recipient, amount);
 756 |         return true;
 757 |     }
```

**调用位置:** `UniswapV2Pair.sol` (行 344-344)

```solidity
 344 |         (bool success, bytes memory data) = token.call(abi.encodeWithSelector(SELECTOR, to, value));
```

### sellPepe(uint256)
**合约地址:** `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91`
**调用类型:** 受害者合约被调用

**函数定义文件:** `PEPE_STRATEGY.sol`

```solidity
1460 |     function sellPepe(uint256 orderId) external nonReentrant{
1461 |         Order storage order = orders[orderId];
1462 |         require(!order.sold, "Already sold");
1463 |         require(previewSell(order.pepeBought) * 1000 >= order.ethSpent * PROFIT_BPS, "Profit threshold not met");
1464 | 
1465 |         require(IERC20(PEPE_TOKEN).balanceOf(address(this)) >= order.pepeBought, "Not enough PEPE in contract");
1466 | 
1467 |         IERC20(PEPE_TOKEN).approve(address(uniswapRouter), order.pepeBought);
1468 | 
1469 |         address[] memory path = new address[](3);
1470 |         path[0] = PEPE_TOKEN;
1471 |         path[1] = uniswapRouter.WETH();
1472 |         path[2] = address(this);
1473 | 
1474 |         uniswapRouter.swapExactTokensForTokensSupportingFeeOnTransferTokens(
1475 |             order.pepeBought,
1476 |             0,
1477 |             path,
1478 |             address(DEAD_ADDRESS),
1479 |             block.timestamp
1480 |         );
1481 | 
1482 |         order.sold = true;
1483 | 
1484 |         payable(msg.sender).transfer(txReward);
1485 | 
1486 |     }
```

### transferFrom(address,address,uint256)
**合约地址:** `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91`
**调用类型:** 受害者合约被调用

**函数定义文件:** `PEPE_STRATEGY.sol`

```solidity
 791 |     function transferFrom(
 792 |         address sender,
 793 |         address recipient,
 794 |         uint256 amount
 795 |     ) public virtual override returns (bool) {
 796 |         _transfer(sender, recipient, amount);
 797 | 
 798 |         uint256 currentAllowance = _allowances[sender][_msgSender()];
 799 |         require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
 800 |         unchecked {
 801 |             _approve(sender, _msgSender(), currentAllowance - amount);
 802 |         }
 803 | 
 804 |         return true;
 805 |     }
```

**调用位置:** `UniswapV2Router02.sol` (行 772-772)

```solidity
 772 |         (bool success, bytes memory data) = token.call(abi.encodeWithSelector(0x23b872dd, from, to, value));
```

### unknown()
**合约地址:** `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91`
**调用类型:** 受害者合约被调用

**函数定义文件:** `PEPE_STRATEGY.sol`

```solidity
1178 |     receive() external payable {}
```

**调用位置:** `UniswapV2Router02.sol` (行 777-777)

```solidity
 777 |         (bool success,) = to.call{value:value}(new bytes(0));
```

### buyPepe()
**合约地址:** `0xa89f4ca08f729364f0e1ce657c4b6d5ea60e1f91`
**调用类型:** 受害者合约被调用

**函数定义文件:** `PEPE_STRATEGY.sol`

```solidity
1430 |     function buyPepe() external nonReentrant{
1431 |         uint256 treasuryBalance = address(this).balance;
1432 |         require(treasuryBalance >= minPepeBuy + txReward, "Not enough ETH in treasury");
1433 | 
1434 |         uint256 beforePepeBalance = IERC20(PEPE_TOKEN).balanceOf(address(this));
1435 |         address[] memory path = new address[](2);
1436 |         path[0] = uniswapRouter.WETH();
1437 |         path[1] = PEPE_TOKEN;
1438 | 
1439 |         uniswapRouter.swapExactETHForTokensSupportingFeeOnTransferTokens{value: treasuryBalance - txReward}(
1440 |             0, 
1441 |             path,
1442 |             address(this),
1443 |             block.timestamp
1444 |         );
1445 |         uint256 afterPepeBalance = IERC20(PEPE_TOKEN).balanceOf(address(this));
1446 |         uint256 pepeBought = afterPepeBalance - beforePepeBalance;
1447 | 
1448 |         uint256 orderId = nextOrderId++;
1449 |         orders[orderId] = Order({
1450 |             ethSpent: treasuryBalance - txReward,
1451 |             pepeBought: pepeBought,
1452 |             timestamp: block.timestamp,
1453 |             sold: false
1454 |         });
1455 | 
1456 |         payable(msg.sender).transfer(txReward);
1457 | 
1458 |     }
```
