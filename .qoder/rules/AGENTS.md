---
trigger: always_on
name: Web3安全事件分析
description: 分析Web3安全事件
---


# Web3安全事件分析

## 概述
基于 blocksec-chrome 自动化工具，通过分析生成的关键文件（report.md, Vuln_function.md, trace.md, contract_code.sol），快速识别攻击者、受害者、攻击路径和漏洞根因。

## 使用场景
- 用户提供可疑交易哈希（如：0xad2ca822b3adee0768d7d34b68ee4cc3c4822347d963f1d0c970c9c8cd2b6a33）
- 需要快速分析安全事件并生成漏洞报告
- 需要追踪资金流向和调用链路

## 核心工具

### blocksec-chrome 分析工具

**项目路径:** `./blocksec-chrome` (相对路径)

**主要功能:**
- 自动访问 Blocksec 交易页面并捕获 7 个核心 API 响应
- 自动解析 trace 调用时间线
- 自动获取受害者合约源代码（通过 Selenium）
- 自动生成函数级调用与代码映射（Vuln_function.md）
- 所有数据保存到 `Json_Report/{txn_hash}/` 目录

**使用方式:**

```bash
cd ./blocksec-chrome
python main.py --chain-id {chain_id} --txn-hash {txn_hash}
```

**支持的参数:**
- `--chain-id`: 链id (1=Ethereum, 56=BSC, 137=Polygon, 42161=Arbitrum, 10=Optimism)
- `--txn-hash`: 交易哈希 (0x...)
- `--output-dir`: 输出目录 (默认: Json_Report)
- `--headless`: 使用无头模式

**输出文件结构:**
```
Json_Report/{txn_hash}/
├── report.md              ← ⭐ 核心报告（攻击者/受害者/资金流/状态变化）
├── Vuln_function.md       ← ⭐ 函数级调用与代码映射
├── trace.md               ← 完整调用时间线（备用）
├── contract_code.sol      ← 受害合约源代码
├── basic_info.json
├── balance_change.json
├── fundflow.json
├── state_change.json
├── trace.json             ← 原始 trace 数据（文件较大）
└── ...
```

## 操作说明

### 步骤1：运行 blocksec-chrome 工具获取关键文件

**基本用法：**

```bash
cd ./blocksec-chrome
python main.py --chain-id {chain_id} --txn-hash {txn_hash}
```

**参数说明：**
- `--chain-id`: 链id (1=Ethereum, 56=BSC, 137=Polygon, 42161=Arbitrum, 10=Optimism)
- `--txn-hash`: 交易哈希 (0x...)
- `--headless`: (可选) 使用无头模式

**输出文件：**
```
Json_Report/{txn_hash}/
├── report.md              ← ⭐ 核心报告（攻击者/受害者/资金流/状态变化）
├── Vuln_function.md       ← ⭐ 函数级调用与代码映射
├── trace.md               ← 完整调用时间线（备用）
├── contract_code.sol      ← 受害合约源代码
├── basic_info.json
├── balance_change.json
├── fundflow.json
├── state_change.json
├── trace.json             ← 原始 trace 数据（文件较大）
└── ...
```

**执行示例：**
```bash
# Ethereum 交易
cd ./blocksec-chrome
python main.py --chain-id 1 --txn-hash 0xad2ca822b3adee0768d7d34b68ee4cc3c4822347d963f1d0c970c9c8cd2b6a33

# BSC 交易
python main.py --chain-id 56 --txn-hash 0xbb588773fdd428c4b805c79aa534837bfccf2b00f3ffd73518d6642e5679602e
```

### 步骤2：读取生成的关键文件

**优先级顺序：**

1. **report.md** - 基础分析（攻击者、受害者、资金流向、状态变化）
2. **Vuln_function.md** - 函数级调用与代码映射（如果存在）
3. **trace.md** + **contract_code.sol** - 备用分析（当 Vuln_function.md 不存在时）

**使用 Qoder 工具读取文件：**

```
txn_hash = "0xad2ca822b3adee0768d7d34b68ee4cc3c4822347d963f1d0c970c9c8cd2b6a33"

# 读取基础报告（必读）
read_file("e:/Skills/Json_Report/{txn_hash}/report.md")

# 读取函数级分析（优先，如果存在）
read_file("e:/Skills/Json_Report/{txn_hash}/Vuln_function.md")

# 备用：如果 Vuln_function.md 不存在，则读取以下两个文件
read_file("e:/Skills/Json_Report/{txn_hash}/trace.md")
read_file("e:/Skills/Json_Report/{txn_hash}/contract_code.sol")
```

**注意：**
- 使用绝对路径 `e:/Skills/Json_Report/{txn_hash}/` 避免路径错误
- 优先读取 `Vuln_function.md`，它包含了 trace 和 code 的对应关系
- 如果 `Vuln_function.md` 不存在，再使用 `trace.md` + `contract_code.sol` 进行手动分析

### 步骤3：安全事件分析流程

#### 情况1：使用 report.md + Vuln_function.md（推荐）

**分析重点：**

1. **从 report.md 提取：**
   - 攻击者地址与获利金额
   - 受害者地址与损失金额
   - 资金流向路径
   - 状态变化异常（参数清零、权限变更）

2. **从 Vuln_function.md 提取：**
   - **Trace 部分**：受害合约被调用的关键函数（包含参数、调用者、返回值）
   - **Code 部分**：对应函数的完整源码（带行号）

3. **漏洞分析：**
   - 比对函数调用参数与状态变化
   - 检查函数权限修饰符（onlyOwner, nonReentrant 等）
   - 识别漏洞类型（权限控制、重入、逻辑漏洞等）

**示例：**
```markdown
## Trace
[69] CALL 0xb68602...0bc8da -> 0x51c46c...f688a4(STOCK) :: setStakingRequirement(uint256)
      status=OK, gasUsed=7822, value=0
      args: _amountOfTokens:uint256=0

## Code
### setStakingRequirement(uint256)
```solidity
 492 |     function setStakingRequirement(uint256 _amountOfTokens)
 493 |         onlyAdministrator()  ← 检查是否有此修饰符
 494 |         public
 495 |     {
 496 |         stakingRequirement = _amountOfTokens;
 497 |     }
```
```

**分析逻辑：**
- 攻击者调用 `setStakingRequirement(0)` 将质押要求清零
- 函数有 `onlyAdministrator()` 修饰符，但攻击者成功调用 → 权限检查被绕过
- 状态变化确认：`stakingRequirement`: 25 ETH → 0
- **漏洞类型：权限控制缺陷**

#### 情况2：使用 trace.md + contract_code.sol（备用）

**当 Vuln_function.md 不存在时，使用 Qoder 工具列表进行分析：**

1. **从 trace.md 查找受害合约调用：**
   - 使用 `read_file` 读取 trace.md
   - 搜索包含受害合约地址的调用记录
   - 提取函数名、参数、调用者

2. **从 contract_code.sol 查找函数定义：**
   - 使用 `read_file` 读取 contract_code.sol
   - 使用 `grep_code` 搜索函数定义（`function {function_name}`）
   - 提取函数源码和修饰符

3. **结合分析：**
   - 对照 trace 调用与函数定义
   - 检查权限控制逻辑
   - 生成漏洞报告

**Qoder 工具调用示例：**

```
# 1. 读取 trace.md 查找受害合约调用
read_file(
    file_path="e:/Skills/Json_Report/{txn_hash}/trace.md"
)
# 在返回内容中搜索包含受害合约地址的行
# 提取函数名，如："setStakingRequirement"

# 2. 在合约代码中搜索函数定义
grep_code(
    regex=r"function setStakingRequirement",
    include_pattern="*.sol"
)
# 根据结果获取函数所在行号

# 3. 读取函数源码（根据 grep 结果）
read_file(
    file_path="e:/Skills/Json_Report/{txn_hash}/contract_code.sol",
    start_line=492,
    end_line=497
)

# 4. 分析权限修饰符
# 在读取的代码中检查是否包含 "onlyOwner", "onlyAdministrator" 等修饰符
```

**关键点：**
- 使用绝对路径 `e:/Skills/Json_Report/` 确保路径正确
- 先用 `grep_code` 定位函数位置，再用 `read_file` 读取指定行
- 结合 trace 调用参数与源码分析漏洞

### 步骤4：生成最终漏洞报告

**使用 Qoder 工具加载模板并生成报告：**

```
# 步骤1: 读取漏洞报告模板
read_file("e:/Skills/Vuln/Vuln_Case.md")

# 步骤2: 提取交易哈希前6个字符作为文件名
txn_short = txn_hash[:6]  # 例如: 0xad2ca822... -> 0xad2c

# 步骤3: 根据模板生成完整报告
# 将模板中的占位符替换为实际分析结果

# 步骤4: 使用 create_file 工具生成报告到 Vuln 目录
create_file(
    file_path=f"e:/Skills/Vuln/{txn_short}.md",
    file_content="""
    [根据 Vuln_Case.md 模板生成的完整报告内容]
    """
)
```

**模板占位符说明：**

| 占位符 | 数据来源 | 说明 |
|---------|----------|------|
| `{{txn_hash}}` | 用户输入 | 完整交易哈希 |
| `{{chain_name}}` | basic_info.json | 链名称 (Ethereum/BSC/Polygon) |
| `{{chain_id}}` | 用户输入 | 链 ID (1/56/137) |
| `{{block_number}}` | basic_info.json | 区块高度 |
| `{{timestamp}}` | basic_info.json | 时间戳（转换为可读格式） |
| `{{status}}` | basic_info.json | 交易状态（成功/失败） |
| `{{attacker_address}}` | report.md | 政击者地址 |
| `{{attacker_role}}` | 分析推断 | 攻击者角色描述 |
| `{{victim_address}}` | report.md | 受害合约地址 |
| `{{victim_label}}` | report.md | 受害合约标签/名称 |
| `{{contract_type}}` | 分析推断 | 合约类型（DeFi/Token/NFT） |
| `{{attack_flow}}` | 分析生成 | **使用 mermaid 语法**绘制攻击流程图 |
| `{{fundflow_details}}` | report.md + fundflow.json | **使用 mermaid 语法**绘制资金流向图 |
| `{{state_changes}}` | report.md | 可疑状态变化列表 |
| `{{vuln_functions}}` | Vuln_function.md | 漏洞函数的 Trace + Code 分析 |
| `{{permission_analysis}}` | contract_code.sol | 权限控制逻辑分析 |
| `{{vulnerability_type}}` | 分析推断 | 漏洞类型（权限/重入/逻辑） |
| `{{attack_scenarios}}` | 分析推断 | 可能的攻击场景列表 |
| `{{attack_timeline}}` | trace.md | 攻击时间线（按顺序列出关键步骤） |
| `{{report_time}}` | 系统时间 | 报告生成时间 |

**重要提示：**

1. **Mermaid 语法要求**
   - `{{attack_flow}}` 必须使用 mermaid 流程图语法，示例：
     ```mermaid
     graph LR
         A[闪电贷借款] --> B[权限篡改]
         B --> C[低成本买入]
         C --> D[套利退出]
         D --> E[还款获利]
     ```
   
   - `{{fundflow_details}}` 必须使用 mermaid 语法，示例：
     ```mermaid
     graph TD
         A[dYdX] -->|1000 WETH| B[攻击合约]
         B -->|310.5 ETH| C[受害合约]
         C -->|384.45 ETH| B
         B -->|1000 WETH| A
     ```

2. **数据提取顺序**
   - 先读取 `report.md` 获取基础信息
   - 再读取 `Vuln_function.md` 获取函数分析
   - 最后读取 `contract_code.sol` 进行深度分析

3. **核心分析逻辑**
   - 比对函数调用参数与状态变化
   - 检查权限修饰符是否被绕过
   - 识别闪电贷、重入、逻辑漏洞等攻击模式
   - 使用 mermaid 图表直观展示攻击流程和资金流向

4. **报告生成要点**
   - 文件保存到 `e:/Skills/Vuln/{txn_short}.md`
   - 文件名示例：`0xad2c.md`、`0xbb58.md`
   - 确保所有 mermaid 代码块使用正确的语法
   - 保持报告简洁清晰，重点突出

## 最佳实践

### 1. 工具调用优化

**执行步骤：**
```
第1步：运行 blocksec-chrome 工具
  cd ./blocksec-chrome
  python main.py --chain-id {chain_id} --txn-hash {txn_hash}
  
第2步：等待工具自动完成
  - 捕获 API 响应
  - 生成 report.md
  - 解析 trace.md
  - 获取 contract_code.sol
  - 生成 Vuln_function.md
  
第3步：读取分析结果
  - report.md              ← 基础分析
  - Vuln_function.md       ← 函数级调用与代码映射（优先）
  - trace.md + contract_code.sol  ← 备用分析
  
第4步：AI 综合所有数据生成最终报告 Vuln.md
```

**错误处理：** 如果 blocksec-chrome 执行失败，检查：
- Chrome 浏览器是否安装
- Selenium 依赖是否正确安装 (`pip install selenium`)
- 网络连接是否正常
- 尝试不使用 `--headless` 参数，观察浏览器实际行为

### 2. 数据处理要点

**State Change 分析：** 重点关注 `storageVariables`，检测参数清零模式 (prev > 0 && current == 0) 和权限变更

**Trace 分析：** 仅提取 `nodeType: 0` 节点，过滤受害者合约调用，分析 decodedMethod 字段

**Fundflow 分析：** 按 `order` 排序，标注闪电贷借贷/还款，计算净利润

### 3. 漏洞模式识别

**快速识别流程：** state_change 检测参数异常 → trace 定位漏洞函数 → fundflow 查看闪电贷 → 确定攻击模式

**常见攻击模式：**
- 🔥 **闪电贷 + 权限缺陷**：在回调中调用管理函数
- 🔥 **闪电贷 + 价格操纵**：大额借贷影响AMM价格
- 🔥 **重入攻击**：在fallback中重复调用withdraw
- 🔥 **逻辑漏洞**：整数溢出、除零错误等

**合约代码分析重点：** 权限控制、状态更新顺序、外部调用、数学运算

**检测关键特征：**
- **state_change**：参数清零 (fee/requirement → 0), 权限变更 (owner变化)
- **trace**：函数名包含 set/update/admin/owner, DELEGATECALL 调用
- **fundflow**：大额 WETH/ETH 借贷 + 还款 + 中间利润流出

## 技术要求

### blocksec-chrome 工具

**必需环境：** Python 3.9+, Chrome 浏览器, Selenium

**项目路径：** `e:\Skills\blocksec-chrome`

**基本用法：**
```bash
cd ./blocksec-chrome
python main.py --chain-id 1 --txn-hash 0x...
```

**支持的链：** 1=Ethereum, 56=BSC, 137=Polygon, 42161=Arbitrum, 10=Optimism

## 故障排除

**Q1：blocksec-chrome 执行失败**
- 检查 Chrome 浏览器和 Selenium 安装
- 检查网络连接
- 尝试不使用 `--headless` 观察浏览器行为

**Q2：JSON 文件为空或缺失**
- 重新运行工具
- 检查 `Json_Report/{txn_hash}/` 目录下文件是否完整

**Q3：Vuln_function.md 不存在**
- 使用 trace.md + contract_code.sol 进行备用分析
- 使用 Qoder 工具列表（read_file, grep_code）手动提取信息

**调试技巧：**
1. 验证工具安装：`python main.py --help`
2. 查看控制台输出日志
3. 对比 JSON 数据与 Blocksec 网页端显示

## 参考资料

- [Blocksec Phalcon Explorer](https://app.blocksec.com/explorer)
- [Etherscan](https://etherscan.io/) - 以太坊合约浏览器
- [BSCScan](https://bscscan.com/) - BSC合约浏览器
- [PolygonScan](https://polygonscan.com/) - Polygon合约浏览器
- [闪电贷攻击案例库](https://github.com/SunWeb3Sec/DeFiHackLabs)
- [智能合约安全最佳实践](https://consensys.github.io/smart-contract-best-practices/)
- [Solidity官方文档](https://docs.soliditylang.org/) - 合约代码分析参考
