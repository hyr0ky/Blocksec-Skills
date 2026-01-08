---
trigger: always_on
name: Web3安全事件分析
description: 分析Web3安全事件，识别攻击者、受害者、攻击路径和漏洞根因
---

# Web3安全事件分析

## 概述
基于 blocksec-chrome 自动化工具，通过分析生成的关键文件（report.md, Vuln_function.md, trace.md），快速识别攻击者、受害者、攻击路径和漏洞根因。

## 核心工作流程

### 步骤1：运行工具获取数据（必做）
```bash
cd ./blocksec-chrome
python main.py --chain-id {chain_id} --txn-hash {txn_hash}
```

工具会在项目根目录生成：
```
./Json_Report/{txn_hash}/
├── report.md              # 攻击者/受害者/资金流/状态变化
├── Vuln_function.md       # 函数级调用与代码映射（⚠️ 优先）
├── trace.md               # 调用时间线
└── Code/                  # 合约源代码（按地址哈希分组）
```

### 步骤2：加载关键数据（必做）
使用 Qoder 自身的 file 工具读取核心文件：
```python
read_file(f"./Json_Report/{txn_hash}/report.md")
read_file(f"./Json_Report/{txn_hash}/Vuln_function.md")
# 如需要再按需读取 trace.md / Code 目录下的合约源码
```

### 步骤3：按需加载详细检查清单（推荐）
当需要更系统的分步分析时，再按需加载 checklist 资源：
```python
read_file("./.qoder/rules/resources/references/analysis_checklist.md")
```
该清单包含：
- 四个分析阶段：信息收集 / 初步判断 / 深度分析 / 报告生成
- 对权限、参数、副作用、资金流向、代币经济系统的详细检查项
- Valinity / MSCST 等案例教训与常见陷阱

### 步骤4：按需加载典型案例（可选）
当发现攻击模式疑似与典型案例相似时，可按需加载对应案例资源作对比分析：
```python
# 流动性计算缺陷 + 未验证合约（如 RWB）
read_file("./.qoder/rules/resources/examples/flawed_liquidity_calc_case.md")

# Atomic Sandwich & 三明治攻击
read_file("./.qoder/rules/resources/examples/mscst_case.md")

# Rebalancing + 小池子业务逻辑缺陷
read_file("./.qoder/rules/resources/examples/valinity_case.md")

# Vault withdraw 访问控制缺失
read_file("./.qoder/rules/resources/examples/vault_case.md")

# ROI / Ponzi 利润翻倍公式错误（如 WADJET）
read_file("./.qoder/rules/resources/examples/wadjet_case.md")
```

### 步骤5：生成漏洞报告
仅在需要输出完整报告时，才使用模板和 create_file：
```python
# 1. 读取通用报告模板
read_file("./Vuln/Vuln_Case.md")

# 2. 提取交易哈希前缀
txn_short = txn_hash[:6]  # 例如: 0xad2c

# 3. 根据分析结果渲染模板，使用 Mermaid 绘制攻击流程/资金流向
create_file(
    file_path=f"./Vuln/{txn_short}.md",
    file_content="[根据当前分析生成的完整报告内容]"
)
```

## 故障排除（概要）

如在使用工具或读取文件时遇到问题，只在需要时再使用 shell 工具排查路径：
```powershell
# 搜索 report.md 实际位置
Get-ChildItem -Path . -Filter "report.md" -Recurse | Select-Object FullName

# 递归搜索特定合约名称（Code 目录按地址哈希分组）
Get-ChildItem -Path "./Json_Report/{txn_hash}/Code" -Recurse -Filter "*ContractName*"
```

## 参考资源

- 详细步骤清单：`./.qoder/rules/resources/references/analysis_checklist.md`
- 典型案例：
  - `flawed_liquidity_calc_case.md` - 流动性计算缺陷利用（如 RWB）
  - `mscst_case.md` - MSCST Atomic Sandwich 案例
  - `valinity_case.md` - Valinity Rebalancing 案例
  - `vault_case.md` - Vault withdraw 访问控制缺失案例
  - `wadjet_case.md` - WADJET 利润翻倍 ROI 案例
- 外部链接：
  - [Blocksec Phalcon Explorer](https://app.blocksec.com/explorer)
  - [闪电贷攻击案例库](https://github.com/SunWeb3Sec/DeFiHackLabs)
