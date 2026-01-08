# 🔒 安全事件深度分析报告

**交易哈希:** `{{txn_hash}}`  
**链:** {{chain_name}} (Chain ID: {{chain_id}})  
**区块高度:** {{block_number}}  
**时间戳:** {{timestamp}}  
**状态:** {{status}}

---

## 📊 基础分析

### 攻击者
- **地址:** `{{attacker_address}}`
- **角色:** {{attacker_role}}

### 受害合约
- **地址:** `{{victim_address}}`
- **标签:** {{victim_label}}
- **合约类型:** {{contract_type}}

### 攻击流程概览
>使用mermaid 语法

{{attack_flow}}

---

## 💰 资金流向分析

### 关键资金流动路径
>使用mermaid 语法
```
{{fundflow_details}}
```


---

## ⚠️ 可疑状态变化

{{state_changes}}

---

## 🎯 漏洞函数深度分析

{{vuln_functions}}

---

## 🔍 漏洞根因分析

### 权限控制缺陷 - 核心问题

{{permission_analysis}}

### 🔥 漏洞类型确认

{{vulnerability_type}}

**可能的攻击场景：**

{{attack_scenarios}}

---

## 💡 攻击时间线

```
{{attack_timeline}}
```

---



*报告生成时间: {{report_time}}*  
*分析工具: blocksec-chrome + Qoder AI*
