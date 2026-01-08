# Blocksec-Skills

🔒 **区块链安全事件智能分析工具** - 基于 Blocksec Phalcon Explorer 的自动化漏洞分析系统

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📖 项目简介

Blocksec-Skills 是一个专为区块链安全研究人员和审计人员设计的智能分析工具，能够自动化分析链上安全事件，快速识别攻击者、受害者、攻击路径和漏洞根因。

### 核心功能

- 🚀 **自动化数据采集**：自动访问 Blocksec 交易页面并捕获 7 个核心 API 响应
- 🔍 **智能 Trace 解析**：自动解析交易调用时间线，生成人类可读的调用链路
- 📄 **合约源码获取**：通过 Selenium 自动获取受害者合约完整源代码
- 🎯 **函数级映射分析**：自动生成函数调用与代码映射（Vuln_function.md）
- 📊 **可视化报告**：使用 Mermaid 图表展示攻击流程和资金流向
- 🤖 **AI 辅助分析**：配合 Qoder AI 生成专业的漏洞分析报告

### 支持的区块链

- ✅ Ethereum (Chain ID: 1)
- ✅ BSC (Chain ID: 56)
- ✅ Polygon (Chain ID: 137)
- ✅ Arbitrum (Chain ID: 42161)
- ✅ Optimism (Chain ID: 10)

---

## 🏗️ 项目结构

```
Blocksec-Skills/
├── blocksec-chrome/           # 核心分析工具
│   ├── analyzers/             # 分析器模块
│   │   ├── __init__.py
│   │   └── blocksec_analyzer.py
│   ├── models/                # 数据模型
│   │   ├── __init__.py
│   │   └── transaction.py
│   ├── utils/                 # 工具函数
│   │   ├── __init__.py
│   │   ├── chrome_driver.py
│   │   ├── contract_fetcher.py
│   │   └── network_helper.py
│   ├── examples/              # 示例脚本
│   │   └── analyze_custom_website.py
│   ├── main.py               # 主程序入口
│   └── requirements.txt      # Python 依赖
├── Json_Report/              # 分析结果输出目录
│   └── {txn_hash}/
│       ├── report.md         # 核心报告
│       ├── Vuln_function.md  # 函数级调用与代码映射
│       ├── trace.md          # 完整调用时间线
│       ├── contract_code.sol # 受害合约源代码
│       ├── basic_info.json
│       ├── balance_change.json
│       ├── fundflow.json
│       ├── state_change.json
│       └── trace.json
├── Vuln/                     # AI 生成的漏洞报告
│   ├── Vuln_Case.md         # 报告模板
│   └── {tx前6位}.md         # 完整分析报告
├── .qoder/                   # Qoder AI 配置
│   └── rules/
│       └── AGENTS.md        # AI 分析规则
└── README.md
```

---

## 🚀 快速开始

### 环境要求

- Python 3.9+
- Chrome 浏览器
- Selenium WebDriver

### 安装步骤

1. **克隆仓库**

```bash
git clone https://github.com/hyr0ky/Blocksec-Skills.git
cd Blocksec-Skills
```

2. **安装依赖**

```bash
cd blocksec-chrome
pip install -r requirements.txt
```

3. **运行分析**

```bash
# 分析以太坊交易
python main.py --chain-id 1 --txn-hash 0xad2ca822b3adee0768d7d34b68ee4cc3c4822347d963f1d0c970c9c8cd2b6a33

# 分析 BSC 交易（无头模式）
python main.py --chain-id 56 --txn-hash 0xbb588773fdd428c4b805c79aa534837bfccf2b00f3ffd73518d6642e5679602e --headless

# 指定输出目录
python main.py --chain-id 1 --txn-hash 0x... --output-dir /custom/path
```

### 参数说明

| 参数 | 说明 | 必需 | 默认值 |
|------|------|------|--------|
| `--chain-id` | 链 ID (1=Ethereum, 56=BSC, 137=Polygon) | ✅ | - |
| `--txn-hash` | 交易哈希 (0x...) | ✅ | - |
| `--output-dir` | 输出目录路径 | ❌ | `../Json_Report` |
| `--headless` | 使用无头模式（不显示浏览器） | ❌ | `False` |

---

## 📊 输出文件说明

### 核心文件

#### 1. `report.md` - 基础分析报告
包含：
- 攻击者和受害者地址
- 资金流向路径
- 可疑状态变化（参数清零、权限变更）
- 攻击流程概览

#### 2. `Vuln_function.md` - 函数级调用与代码映射
包含：
- **Trace 部分**：受害合约被调用的关键函数（包含参数、调用者、返回值）
- **Code 部分**：对应函数的完整源码（带行号）

示例：
```markdown
## Trace
[69] CALL 0xb68602...0bc8da -> 0x51c46c...f688a4(STOCK) :: setStakingRequirement(uint256)
      status=OK, gasUsed=7822, value=0
      args: _amountOfTokens:uint256=0

## Code
### setStakingRequirement(uint256)
```solidity
 492 |     function setStakingRequirement(uint256 _amountOfTokens)
 493 |         onlyAdministrator()
 494 |         public
 495 |     {
 496 |         stakingRequirement = _amountOfTokens;
 497 |     }
```

#### 3. `trace.md` - 完整调用时间线
- 按时间顺序展示所有函数调用
- 包含调用深度、Gas 消耗、返回值等详细信息

#### 4. `contract_code.sol` - 受害合约源代码
- 通过 Selenium 自动从区块链浏览器获取
- 包含完整的合约源码和注释

### JSON 数据文件

- `basic_info.json` - 交易基本信息
- `balance_change.json` - 余额变化详情
- `fundflow.json` - 资金流向数据
- `state_change.json` - 状态变化记录
- `trace.json` - 原始 trace 数据（用于深度分析）

---

## 🤖 AI 辅助分析

本项目配合 **Qoder AI** 可以自动生成专业的漏洞分析报告。

### 使用 Qoder AI 生成报告

1. **配置 Qoder AI**
   - 项目已包含 `.qoder/rules/AGENTS.md` 配置文件
   - AI 会自动加载 `Vuln/Vuln_Case.md` 模板

2. **分析流程**
   ```
   步骤1: 运行 blocksec-chrome 工具
   步骤2: AI 读取 report.md 和 Vuln_function.md
   步骤3: AI 根据模板生成完整分析报告
   步骤4: 报告保存到 Vuln/{tx前6位}.md
   ```

3. **报告特点**
   - 📊 使用 Mermaid 图表展示攻击流程
   - 🎯 函数级代码分析
   - 🔍 漏洞根因推断
   - 🛡️ 修复建议
   - ⏱️ 攻击时间线

---

## 🔍 使用示例

### 示例 1：分析权限控制漏洞

```bash
cd blocksec-chrome
python main.py --chain-id 1 --txn-hash 0xad2ca822b3adee0768d7d34b68ee4cc3c4822347d963f1d0c970c9c8cd2b6a33
```

**输出结果：**
```
[ℹ️] Chain: 1 | TxHash: 0xad2ca822...
[✓] report.md
[✓] trace.json (0.40 MB)
[✓] trace.md
[✓] contract_code.sol + Vuln_function.md
[✓] 分析完成
```

**生成的文件：**
- `Json_Report/0xad2ca822.../report.md` - 发现攻击者将 `stakingRequirement` 从 25 ETH 清零
- `Json_Report/0xad2ca822.../Vuln_function.md` - 定位到 `setStakingRequirement()` 函数
- `Vuln/0xad2c.md` - AI 生成的完整分析报告（权限控制缺陷）

### 示例 2：批量分析多个交易

```bash
# 创建批量分析脚本
cat > batch_analyze.sh << 'EOF'
#!/bin/bash
transactions=(
    "1:0xad2ca822b3adee0768d7d34b68ee4cc3c4822347d963f1d0c970c9c8cd2b6a33"
    "56:0xbb588773fdd428c4b805c79aa534837bfccf2b00f3ffd73518d6642e5679602e"
    "137:0x..."
)

for tx in "${transactions[@]}"; do
    chain_id="${tx%%:*}"
    txn_hash="${tx#*:}"
    echo "Analyzing $txn_hash on chain $chain_id"
    python main.py --chain-id "$chain_id" --txn-hash "$txn_hash" --headless
done
EOF

chmod +x batch_analyze.sh
./batch_analyze.sh
```

---

## 🛠️ 高级功能

### 1. 自定义分析器

您可以扩展 `BlocksecAnalyzer` 类来添加自定义分析逻辑：

```python
from analyzers import BlocksecAnalyzer

class CustomAnalyzer(BlocksecAnalyzer):
    def analyze_transaction(self, chain_id, txn_hash, output_dir):
        report = super().analyze_transaction(chain_id, txn_hash, output_dir)
        
        # 添加自定义分析逻辑
        custom_analysis = self.perform_custom_analysis(report)
        
        return report
    
    def perform_custom_analysis(self, report):
        # 实现自定义分析
        pass
```

### 2. 集成到其他工具

```python
from blocksec_chrome.analyzers import BlocksecAnalyzer

# 在您的代码中使用
with BlocksecAnalyzer(headless=True) as analyzer:
    report = analyzer.analyze_transaction(
        chain_id=1,
        txn_hash="0x...",
        output_dir="./my_output"
    )
    
    # 处理分析结果
    print(f"Attacker: {report.get('attacker_address')}")
    print(f"Victim: {report.get('victim_address')}")
```

---

## 📚 常见攻击模式识别

本工具可以自动识别以下常见攻击模式：

### 🔥 闪电贷 + 权限缺陷
- **特征**：大额 WETH/ETH 借贷 → 调用管理函数 → 参数清零
- **示例**：攻击者在闪电贷回调中调用 `setStakingRequirement(0)`

### 🔥 闪电贷 + 价格操纵
- **特征**：大额借贷影响 AMM 价格 → 套利交易
- **示例**：操纵 Uniswap 池价格进行套利

### 🔥 重入攻击
- **特征**：在 fallback 中重复调用 withdraw
- **示例**：The DAO 攻击模式

### 🔥 逻辑漏洞
- **特征**：整数溢出、除零错误、权限检查缺失
- **示例**：`onlyAdministrator()` 修饰符被绕过

---

## 🐛 故障排除

### Q1: blocksec-chrome 执行失败

**解决方案：**
- 检查 Chrome 浏览器是否安装
- 确认 Selenium 依赖已正确安装：`pip install selenium`
- 检查网络连接是否正常
- 尝试不使用 `--headless` 参数，观察浏览器实际行为

### Q2: JSON 文件为空或缺失

**解决方案：**
- 重新运行工具
- 检查 `Json_Report/{txn_hash}/` 目录下文件是否完整
- 确认交易哈希正确

### Q3: Vuln_function.md 不存在

**解决方案：**
- 使用 `trace.md` + `contract_code.sol` 进行备用分析
- 检查受害合约源码是否成功获取

### Q4: Selenium WebDriver 错误

**解决方案：**
```bash
# 更新 Chrome 浏览器到最新版本
# 重新安装 Selenium
pip uninstall selenium
pip install selenium --upgrade
```

---

## 🤝 贡献指南

欢迎贡献代码、报告 Bug 或提出新功能建议！

### 贡献流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码规范

- 遵循 PEP 8 Python 代码风格
- 添加必要的注释和文档字符串
- 更新相关文档

---

## 💻 如何上传到 GitHub

### 方法 1：使用 Git 命令行（推荐）

```bash
# 1. 进入项目目录
cd e:\Skills

# 2. 初始化 Git 仓库
git init

# 3. 添加所有文件
git add .

# 4. 提交更改
git commit -m "Initial commit: Blocksec-Skills blockchain security analysis tool"

# 5. 添加远程仓库
git remote add origin https://github.com/hyr0ky/Blocksec-Skills.git

# 6. 推送到 GitHub
git branch -M main
git push -u origin main
```

### 方法 2：使用 GitHub Desktop

1. 下载并安装 [GitHub Desktop](https://desktop.github.com/)
2. 打开 GitHub Desktop
3. 点击 `File` -> `Add Local Repository`
4. 选择 `e:\Skills` 目录
5. 点击 `Publish repository`
6. 输入仓库名称：`Blocksec-Skills`
7. 点击 `Publish Repository`

### 方法 3：使用 GitHub 网页界面

1. 访问 https://github.com/hyr0ky/Blocksec-Skills
2. 点击 `Add file` -> `Upload files`
3. 拖动所有文件到浏览器
4. 填写提交信息
5. 点击 `Commit changes`

### 注意事项

- 确保 `.gitignore` 文件已创建，避免上传不必要的文件
- `Json_Report/` 和 `Vuln/*.md` （除了 `Vuln_Case.md`）不会被上传
- `.qoder/` 目录不会被上传（本地 AI 配置）

---

## 📝 上传后的后续步骤

### 1. 配置仓库设置

在 GitHub 仓库页面：
- 点击 `Settings`
- 添加仓库描述：`🔒 Blockchain Security Event Analysis Tool - Automated vulnerability analysis based on Blocksec Phalcon Explorer`
- 添加标签：`blockchain`, `security`, `ethereum`, `defi`, `vulnerability-analysis`
- 设置主题：`blockchain-security`, `web3-security`, `smart-contracts`

### 2. 启用 GitHub Pages（可选）

如果想展示项目文档：
- 进入 `Settings` -> `Pages`
- 选择 `Source`: `main` branch
- 点击 `Save`

### 3. 添加 Topics

在仓库主页，点击齿轮图标添加：
- `blockchain-security`
- `ethereum-security`
- `smart-contract-audit`
- `defi-security`
- `vulnerability-scanner`
- `python`
- `selenium`

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

## 🔗 相关资源

- [Blocksec Phalcon Explorer](https://app.blocksec.com/explorer) - 区块链安全分析平台
- [Etherscan](https://etherscan.io/) - 以太坊区块链浏览器
- [BSCScan](https://bscscan.com/) - BSC 区块链浏览器
- [DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs) - 闪电贷攻击案例库
- [Smart Contract Best Practices](https://consensys.github.io/smart-contract-best-practices/) - 智能合约安全最佳实践

---

## 📧 联系方式

- **Issues**: [GitHub Issues](https://github.com/hyr0ky/Blocksec-Skills/issues)
- **Discussions**: [GitHub Discussions](https://github.com/hyr0ky/Blocksec-Skills/discussions)

---

## ⭐ Star History

如果这个项目对您有帮助，请给我们一个 Star ⭐

---

<div align="center">
<b>Made with ❤️ for Blockchain Security Researchers</b>
</div>
