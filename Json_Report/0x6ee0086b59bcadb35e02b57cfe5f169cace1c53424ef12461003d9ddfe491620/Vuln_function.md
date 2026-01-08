# 关键函数调用与代码映射

> **分析范围**: 攻击者直接调用 + 攻击合约调用外部 + 受害者合约被调用

## Trace
```text
[1] CALL 0x724c2b...9b9a55 -> 0x8f73b6...8e5d8c(ERC1967Proxy) :: flashLoan(address,uint256,bytes) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=1408100, value=0
      args: token:address=0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c, assets:uint256=22,220,000,000,000,000,000, data:bytes=0x0000000000000000000000004ef1dcfdcf8f4b99deba2567c4110b06b649ae0f00000000000000000000000000000000000000000000000000000000000000160000000000000000000000000000000000000000000000000e043da617250000

[14] CALL 0x724c2b...9b9a55 -> 0xbb4cdb...bc095c(WBNB) :: withdraw(uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=9295, value=0
      args: wad:uint256=22,220,000,000,000,000,000

[19] STATICCALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: devAddress() ⚠️ (攻击者直接调用)
      status=OK, gasUsed=2452, value=0

[21] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=129068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[56] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[91] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[126] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[161] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[196] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[231] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[266] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[301] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[336] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[371] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[406] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[441] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[476] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[511] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[546] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[581] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[616] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[651] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[686] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[721] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[756] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: deposit(address) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=43068, value=1.01
      args: ref:address=0xe793b0b8b19df008205ae8a5ec3984c2f11a39a1

[791] CALL 0x724c2b...9b9a55 -> 0x4ef1dc...49ae0f(WADJET) :: withdraw() ⚠️ (攻击者直接调用)
      status=OK, gasUsed=94139, value=0

[829] CALL 0x724c2b...9b9a55 -> 0xbb4cdb...bc095c(WBNB) :: deposit() ⚠️ (攻击者直接调用)
      status=OK, gasUsed=21974, value=22.22

[833] CALL 0x724c2b...9b9a55 -> 0xbb4cdb...bc095c(WBNB) :: approve(address,uint256) ⚠️ (攻击者直接调用)
      status=OK, gasUsed=24420, value=0
      args: guy:address=0x8f73b65b4caaf64fba2af91cc5d4a2a1318e5d8c, wad:uint256=22,220,000,000,000,000,000

```

## Code
### flashLoan(address,uint256,bytes)
**合约地址:** `0x8f73b65b4caaf64fba2af91cc5d4a2a1318e5d8c`
**调用类型:** 攻击者直接调用

**函数定义文件:** `Proxy.sol`

```solidity
  66 |     fallback() external payable virtual {
  67 |         _fallback();
  68 |     }
```

### withdraw(uint256)
**合约地址:** `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`
**调用类型:** 攻击者直接调用

**函数定义文件:** `WBNB.sol`

```solidity
  27 |     function withdraw(uint wad) public {
  28 |         require(balanceOf[msg.sender] >= wad);
  29 |         balanceOf[msg.sender] -= wad;
  30 |         msg.sender.transfer(wad);
  31 |         Withdrawal(msg.sender, wad);
  32 |     }
```

### devAddress()
**合约地址:** `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f`
**调用类型:** 攻击者直接调用

**函数定义文件:** `WADJET.sol`

```solidity
   9 |     address public devAddress;
```

### deposit(address)
**合约地址:** `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f`
**调用类型:** 攻击者直接调用

**函数定义文件:** `WADJET.sol`

```solidity
 141 |     function deposit(address ref) public payable {
 142 |         require(msg.value >= 2 * 10**17, "invalid amount");
 143 |         if (users[msg.sender].referrer == address(0)) {
 144 |             require(
 145 |                 ref != msg.sender &&
 146 |                     ref != address(0) &&
 147 |                     users[ref].investment > 0,
 148 |                 "invalid referrer"
 149 |             );
 150 |             users[msg.sender].referrer = ref;
 151 |             users[msg.sender].withdrawCheckPoint = now;
 152 |             users[msg.sender].rate = 5;
 153 |             totalUsers += 1;
 154 |             emit newbie(msg.sender, ref);
 155 |         }
 156 | 
 157 |         uint256 fee = devFee(msg.value);
 158 |         ceoAddress.transfer(fee);
 159 |         marketingAddress.transfer(fee);
 160 |         devAddress.transfer(fee);
 161 |         insuranceWallet.transfer(fee);
 162 |         communityWallet.transfer(fee);
 163 |         users[msg.sender].investment += msg.value;
 164 |         users[msg.sender].profit += (users[msg.sender].profit +
 165 |             calculateProfit(msg.sender));
 166 |         users[msg.sender].reinvestCheckPoint = now;
 167 |         users[msg.sender].deposit += msg.value;
 168 |         totalInvestment = SafeMath.add(totalInvestment, msg.value);
 169 | 
 170 |         if (users[msg.sender].referrer != address(0)) {
 171 |             address upline = users[msg.sender].referrer;
 172 |             for (uint256 i = 0; i < 4; i++) {
 173 |                 if (upline != address(0)) {
 174 |                     uint256 profit = (SafeMath.mul(msg.value, refPercents[i]) /
 175 |                         100);
 176 |                     users[upline].deposit += profit;
 177 |                     users[upline].refIncome += profit;
 178 |                     users[upline].refs[i]++;
 179 |                     upline = users[upline].referrer;
 180 |                 } else break;
 181 |             }
 182 |         }
 183 | 
 184 |         emit buyEvent(msg.sender, msg.value, ref);
 185 |     }
```

### withdraw()
**合约地址:** `0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f`
**调用类型:** 攻击者直接调用

**函数定义文件:** `WADJET.sol`

```solidity
 106 |     function withdraw() public {
 107 |         User storage user = users[msg.sender];
 108 |         uint256 passedDays = daysPassed(user.withdrawCheckPoint, now) % 21;
 109 |         require(passedDays == 20, "Withdrawal is closed");
 110 |         require(canWithdraw(msg.sender), "Non-consecutive reinvest");
 111 | 
 112 |         uint256 profit = user.profit + calculateProfit(msg.sender);
 113 |         reset(msg.sender);
 114 |         uint256 fee = devFee(profit);
 115 |         ceoAddress.transfer(fee);
 116 |         marketingAddress.transfer(fee);
 117 |         devAddress.transfer(fee);
 118 |         communityWallet.transfer(fee);
 119 |         insuranceWallet.transfer(fee);
 120 |         supportWallet.transfer(SafeMath.div(SafeMath.mul(profit, 125), 1000));
 121 |         uint256 net = (profit * 85) / 100;
 122 |         net = net + user.withdrawal > 8 * user.investment
 123 |             ? SafeMath.sub(8 * user.investment, user.withdrawal)
 124 |             : net;
 125 |         msg.sender.transfer(net);
 126 |         user.withdrawal = SafeMath.add(user.withdrawal, net);
 127 |         emit sellEvent(msg.sender, profit);
 128 |     }
```

### deposit()
**合约地址:** `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`
**调用类型:** 攻击者直接调用

**函数定义文件:** `WBNB.sol`

```solidity
  23 |     function deposit() public payable {
  24 |         balanceOf[msg.sender] += msg.value;
  25 |         Deposit(msg.sender, msg.value);
  26 |     }
```

### approve(address,uint256)
**合约地址:** `0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c`
**调用类型:** 攻击者直接调用

**函数定义文件:** `WBNB.sol`

```solidity
  38 |     function approve(address guy, uint wad) public returns (bool) {
  39 |         allowance[msg.sender][guy] = wad;
  40 |         Approval(msg.sender, guy, wad);
  41 |         return true;
  42 |     }
```
