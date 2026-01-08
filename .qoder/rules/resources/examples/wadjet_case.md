# WADJET 利润翻倍漏洞案例

## 基本信息
- 链：BSC (ChainID 56)
- 交易哈希：`0x6ee0086b59bcadb35e02b57cfe5f169cace1c53424ef12461003d9ddfe491620`
- 合约：`0x4ef1dcfdcf8f4b99deba2567c4110b06b649ae0f`（WADJET，高收益 BNB ROI 合约）
- 攻击者：`0x724c2be714e21299917ee8a2b69cf0bfd09b9a55`
- 模式：闪电贷 + 利润计算公式错误（利润指数级放大）

## 攻击流程（高层）
1. 攻击者地址在此前通过正常参与，累积出一小部分时间收益 `calculateProfit(attacker)` 作为种子利润（seed）。
2. 在攻击交易中，通过 `ERC1967Proxy.flashLoan` 闪电贷借入 22.22 WBNB，并 `withdraw` 成 22.22 BNB。
3. 在同一笔交易中，攻击者多次调用 `WADJET.deposit(ref)`，每次携带 1.01 BNB，一共 22 次：
   - 每次调用都会更新 `users[attacker].profit`，由于公式实现错误，导致利润近似 **翻倍**。
4. 多次 `deposit` 后，攻击者账户上的 `profit` 字段从最初的 seed，指数级膨胀到约 156.34 BNB 对应的数值。
5. 攻击者调用一次 `withdraw()`：
   - 合约按虚高的 `profit` 结算，将 85% 的利润（约 132.89 BNB）打给攻击者；
   - 同时向若干项目钱包地址（ceo/marketing/dev/community/insurance 等）支付多次 `fee`。
6. 攻击者用部分 BNB 再存入 WBNB，归还闪电贷，剩余 BNB 即为净利润，实际来源为普通用户之前存入 WADJET 的资金。

## 关键代码与漏洞根因

### 1. 存款函数 `deposit(address ref)`

```solidity
function deposit(address ref) public payable {
    require(msg.value >= 2 * 10**17, "invalid amount");

    if (users[msg.sender].referrer == address(0)) {
        require(
            ref != msg.sender &&
                ref != address(0) &&
                users[ref].investment > 0,
            "invalid referrer"
        );
        users[msg.sender].referrer = ref;
        users[msg.sender].withdrawCheckPoint = now;
        users[msg.sender].rate = 5;
        totalUsers += 1;
        emit newbie(msg.sender, ref);
    }

    uint256 fee = devFee(msg.value);
    ceoAddress.transfer(fee);
    marketingAddress.transfer(fee);
    devAddress.transfer(fee);
    insuranceWallet.transfer(fee);
    communityWallet.transfer(fee);

    users[msg.sender].investment += msg.value;

    // ⚠️ 漏洞行：错误的利润累计方式
    users[msg.sender].profit += (users[msg.sender].profit +
        calculateProfit(msg.sender));

    users[msg.sender].reinvestCheckPoint = now;
    users[msg.sender].deposit += msg.value;
    totalInvestment = SafeMath.add(totalInvestment, msg.value);
    ...
}
```

令：
- \(P = users[msg.sender].profit\)
- \(C = calculateProfit(msg.sender)\)

则更新后：
\[
profit_{new} = P + (P + C) = 2P + C
\]

在多次 `deposit` 场景下：
- 第 1 次：\( profit_1 = C \)
- 第 2 次：\( profit_2 \approx 2C \)
- 第 3 次：\( profit_3 \approx 4C \)
- ...
- 第 N 次：\( profit_N \approx C \cdot 2^{N-1} \)

外部研究验证：
- 在该交易中共进行了 22 次 `deposit`；
- seed `C ≈ 0.071642265 BNB`（在前一块高度通过脚本读取）；
- 最终 \(profit_N ≈ 0.071642265 * 2^{21} ≈ 156.34 BNB\)；
- withdraw 将其中 85%（约 132.89 BNB）打给攻击者，与链上数据吻合。

本质上，**这条语句把历史利润又加了一次**，导致利润字段在可重复调用的 `deposit` 下出现 **指数级膨胀**。

### 2. 提现函数 `withdraw()`

```solidity
function withdraw() public {
    User storage user = users[msg.sender];

    uint256 passedDays = daysPassed(user.withdrawCheckPoint, now) % 21;
    require(passedDays == 20, "Withdrawal is closed");
    require(canWithdraw(msg.sender), "Non-consecutive reinvest");

    uint256 profit = user.profit + calculateProfit(msg.sender);
    reset(msg.sender);

    uint256 fee = devFee(profit);
    ceoAddress.transfer(fee);
    marketingAddress.transfer(fee);
    devAddress.transfer(fee);
    communityWallet.transfer(fee);
    insuranceWallet.transfer(fee);
    supportWallet.transfer(SafeMath.div(SafeMath.mul(profit, 125), 1000));

    uint256 net = (profit * 85) / 100;

    net = net + user.withdrawal > 8 * user.investment
        ? SafeMath.sub(8 * user.investment, user.withdrawal)
        : net;

    msg.sender.transfer(net);
    user.withdrawal = SafeMath.add(user.withdrawal, net);

    emit sellEvent(msg.sender, profit);
}
```

- `withdraw()` 会直接使用已经被指数放大的 `user.profit`；
- 只做了“最多 8 倍投资额”的粗略上限，但在指数膨胀的场景下依然足以抽走大量 BNB；
- 手续费和净收益全部从合约当前 BNB 余额中支付，**来源是所有参与者历史存款**。

## 攻击模式总结

- **漏洞类型**：业务逻辑 / 经济模型缺陷（奖励公式实现错误）
- **攻击模式**：
  - 利用时间收益生成 seed 利润；
  - 通过闪电贷在单交易内反复 `deposit`，让 `profit` 按 2^N 放大；
  - 利用 `withdraw()` 将放大的 `profit` 一次性变成真实 BNB；
  - 归还闪电贷，剩余为净盗取的用户资金。
- **角色获利结构**：
  - 攻击者：得到 85% 的膨胀利润净额；
  - 项目钱包（ceo/marketing/dev/community/insurance 等）：因多次 `deposit` 额外获得大量手续费；
  - 普通用户：合约余额被抽空，实际损失资金。

## 关键教训

1. **见到 `x += (x + f(...))` 这种模式要高度警惕**：
   - 通常意味着历史值被重复计入，可能导致指数级增长；
   - 对 `profit/reward/interest` 等字段尤其危险。

2. **分析收益类合约时要考虑“多次调用的迭代效果”**：
   - 单次调用看似只是“多给一点奖励”；
   - 多次循环后可能是 `2^N` 级别爆炸（尤其在同一笔交易中多次调用时）。

3. **闪电贷在这里是放大器而不是根因**：
   - 根因是奖励公式错误，闪电贷只是降低资金门槛；
   - 没有闪电贷，资金充足的攻击者依旧可以利用该逻辑。

4. **项目钱包可能在攻击中“获益”，但用户承担损失**：
   - 每次 `deposit` 的手续费都流向项目地址；
   - 攻击中大量 `deposit`，导致这些地址获得额外 BNB；
   - 评估损失时应明确区分“攻击者获利”和“项目地址获利”。

5. **审计收益/ROl 合约时的必查项**：
   - 所有与 `profit/reward/interest` 相关的变量更新逻辑；
   - 是否有 `profit = profit + (profit + ...)`、`profit = profit * k + c` 这类在循环调用下可能指数膨胀的模式；
   - `withdraw/claim` 是否直接基于这些变量结算，以及是否有限制上限。
