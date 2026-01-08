"""
主程序入口

区块链安全事件分析工具
"""

import argparse
import sys
import json
from pathlib import Path
from analyzers import BlocksecAnalyzer


def analyze_blocksec_transaction(
    chain_id: int,
    txn_hash: str,
    output_dir: str = "Json_Report",
    headless: bool = False,  # 默认不使用无头模式，方便调试
    deep_analysis: bool = False  # 是否执行深度漏洞分析
):
    """
    分析 Blocksec 交易
    
    Args:
        chain_id: 链id
        txn_hash: 交易哈希
        output_dir: 输出目录
        headless: 是否使用无头模式
        deep_analysis: 是否执行深度漏洞函数分析
    """
    # 使用上下文管理器自动管理资源
    with BlocksecAnalyzer(headless=headless) as analyzer:
        # 分析交易
        report = analyzer.analyze_transaction(chain_id, txn_hash, output_dir)
        
        # 报告已保存到文件，不再打印到控制台
        
        # 深度分析标志已保留但不输出额外信息
        
        # 使用 Selenium 获取受害者合约源代码
        try:
            contract_output_path = Path(output_dir) / txn_hash
            json_dir = contract_output_path / "Json"
            
            report_file = contract_output_path / "report.md"
            trace_file = json_dir / "trace.json"
            label_file = json_dir / "address_label.json"
            debug_code_file = json_dir / "debug_code.json"

            victim_address = ""
            attacker_address = ""
            if report_file.exists():
                report_content = report_file.read_text(encoding="utf-8")
                victim_address = extract_victim_address(report_content)
                attacker_address = extract_attacker_address(report_content)

            # 先解析 trace 调用时间线，方便人工定位
            if trace_file.exists():
                trace_md = _generate_trace_markdown(
                    trace_path=trace_file,
                    label_path=label_file if label_file.exists() else None,
                    only_contract=victim_address or None,
                    attacker_address=attacker_address or "",
                )
                trace_md_file = contract_output_path / "trace.md"
                trace_md_file.write_text(trace_md, encoding="utf-8")
                print(f"[✓] trace.md")

            # 使用 debug_code.json 生成合约代码和 Vuln_function.md
            if debug_code_file.exists():
                # 提取并保存所有合约源代码到 Code 目录
                _extract_contract_codes_from_debug(
                    debug_code_path=debug_code_file,
                    output_path=contract_output_path,
                )
                
                # 生成 Vuln_function.md
                if victim_address:
                    vuln_md = _generate_vuln_function_from_debug_code(
                        debug_code_path=debug_code_file,
                        trace_path=trace_file,
                        label_path=label_file if label_file.exists() else None,
                        victim_address=victim_address,
                        attacker_address=attacker_address,
                    )
                    if vuln_md:
                        vuln_file = contract_output_path / "Vuln_function.md"
                        vuln_file.write_text(vuln_md, encoding="utf-8")
                        print(f"[✓] Vuln_function.md")
        except Exception as e:
            print(f"[⚠️] 获取受害者合约源代码或解析 trace 失败: {e}")
        
        return report


def extract_attacker_address(report_content: str) -> str:
    """从 report.md 提取攻击者地址"""
    import re
    # 匹配 "### 攻击者" 下的地址
    match = re.search(r'###\s*攻击者.*?\n.*?地址.*?`(0x[a-fA-F0-9]{40})`', report_content, re.DOTALL)
    if match:
        return match.group(1)
    return ""


def extract_victim_address(report_content: str) -> str:
    """从 report.md 提取受害者地址"""
    import re
    # 匹配 "### 受害者" 下的地址
    match = re.search(r'###\s*受害者.*?\n.*?地址.*?`(0x[a-fA-F0-9]{40})`', report_content, re.DOTALL)
    if match:
        return match.group(1)
    return ""


def _short_addr(addr: str, length: int = 6) -> str:
    """地址缩写显示"""
    if not addr or not addr.startswith("0x") or len(addr) <= 2 * length + 2:
        return addr
    return f"{addr[:2 + length]}...{addr[-length:]}"


def _load_labels(label_path: Path) -> dict:
    """从 address_label.json 读取地址标签映射"""
    if not label_path or not label_path.exists():
        return {}
    try:
        data = json.loads(label_path.read_text(encoding="utf-8"))
    except Exception:
        return {}

    labels = {}
    for item in data:
        addr = (item.get("address") or "").lower()
        label = item.get("label") or ""
        if addr and label:
            labels[addr] = label
    return labels


def _extract_contract_codes_from_debug(
    debug_code_path: Path,
    output_path: Path,
) -> None:
    """从 debug_code.json 提取所有合约源代码并保存为 .sol 文件"""
    if not debug_code_path.exists():
        print(f"[⚠️] debug_code.json 文件不存在: {debug_code_path}")
        return

    try:
        # 读取 debug_code.json
        with open(debug_code_path, 'r', encoding='utf-8') as f:
            debug_data = json.load(f)
        
        code_files_map = debug_data.get("codeFilesMap", {})
        
        if not code_files_map or not isinstance(code_files_map, dict):
            print("[⚠️] debug_code.json 中未找到有效的 codeFilesMap")
            return
        
        # 创建 Code 目录
        code_dir = output_path / "Code"
        code_dir.mkdir(parents=True, exist_ok=True)
        
        saved_count = 0
        # 遍历所有合约哈希
        for code_hash, files in code_files_map.items():
            if not isinstance(files, list):
                continue
            
            # 为每个合约哈希创建子目录 (使用哈希前8位作为目录名)
            hash_short = code_hash[:10] if code_hash.startswith("0x") else code_hash[:8]
            contract_dir = code_dir / hash_short
            contract_dir.mkdir(parents=True, exist_ok=True)
            
            # 保存该合约的所有文件
            for file_info in files:
                if not isinstance(file_info, dict):
                    continue
                
                code_content = file_info.get("code", "")
                file_name = file_info.get("fileName", "")
                file_path_str = file_info.get("path", "")
                
                if not code_content or not file_name:
                    continue
                
                # 保存文件
                sol_file = contract_dir / file_name
                sol_file.write_text(code_content, encoding="utf-8")
                saved_count += 1
        
        if saved_count > 0:
            print(f"[✓] 已提取 {saved_count} 个合约文件到 Code 目录")
        else:
            print("[⚠️] 未提取到任何合约文件")
            
    except Exception as e:
        print(f"[⚠️] 提取合约代码失败: {e}")


def _format_addr(addr: str, labels: dict) -> str:
    if not addr:
        return ""
    base = _short_addr(addr)
    label = labels.get(addr.lower())
    if label:
        return f"{base}({label})"
    return base


def _pretty_print_trace(trace_path: Path, label_path: Path = None, only_contract: str = None) -> None:
    """将 trace.json 解析为人类可读的调用/状态变化时间线并打印到控制台"""
    if not trace_path.exists():
        print(f"[⚠️] trace.json 文件不存在: {trace_path}")
        return

    try:
        data = json.loads(trace_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[⚠️] 读取 trace.json 失败: {e}")
        return

    data_map = data.get("dataMap", {}) or {}
    labels = _load_labels(label_path) if label_path else {}

    # 将 key 转为 int，并按升序排序，形成执行时间线
    items = []
    for k, v in data_map.items():
        try:
            node_id = int(k)
        except ValueError:
            continue
        items.append((node_id, v))
    items.sort(key=lambda x: x[0])

    only_contract = (only_contract or "").lower()
    call_stack = []  # 简单的基于 fromAddress 的调用栈

    print("\n=============================================")
    print("===============  TRACE 调用时间线  ===============")

    for node_id, node in items:
        node_type = node.get("nodeType")

        # 计算调用深度
        depth = len(call_stack)
        if node_type == 0:
            inv = node.get("invocation", {}) or {}
            from_addr = (inv.get("fromAddress") or "").lower()
            to_addr = (inv.get("address") or "").lower()

            if not call_stack:
                call_stack = [{"address": to_addr}]
                depth = 0
            else:
                idx = None
                for i, frame in enumerate(call_stack):
                    if frame["address"] == from_addr:
                        idx = i
                        break
                if idx is None:
                    # 找不到父节点，当作新的调用链
                    call_stack = [{"address": to_addr}]
                    depth = 0
                else:
                    call_stack = call_stack[: idx + 1]
                    depth = len(call_stack)
                    call_stack.append({"address": to_addr})
        else:
            depth = len(call_stack)

        # 过滤 only_contract（如指定则只保留与该合约直接相关的节点）
        if only_contract:
            addr = ""
            if node_type == 0:
                inv = node.get("invocation", {}) or {}
                addr_to = (inv.get("address") or "").lower()
                addr_from = (inv.get("fromAddress") or "").lower()
                if addr_to != only_contract and addr_from != only_contract:
                    continue
            elif node_type == 3:
                rd = node.get("slotReadData", {}) or {}
                addr = (rd.get("contract") or "").lower()
                if addr != only_contract:
                    continue
            elif node_type == 4:
                wd = node.get("slotWriteData", {}) or {}
                addr = (wd.get("contract") or "").lower()
                if addr != only_contract:
                    continue

        indent = "  " * depth

        if node_type == 0:
            inv = node.get("invocation", {}) or {}
            to_addr = inv.get("address", "")
            from_addr = inv.get("fromAddress", "")
            op = inv.get("operation", "") or "CALL"
            gas_used = inv.get("gasUsed", 0)
            status = inv.get("status", False)
            value = inv.get("value", "0")
            decoded = inv.get("decodedMethod") or {}
            if not isinstance(decoded, dict):
                decoded = {}

            name = decoded.get("name") or "unknown"
            signature = decoded.get("signature") or ""
            selector = inv.get("selector", "")

            header = f"[{node_id}] {op} {_format_addr(from_addr, labels)} -> {_format_addr(to_addr, labels)}"
            if signature:
                header += f" :: {signature}"
            elif name != "unknown":
                header += f" :: {name}"
            elif selector:
                header += f" :: <selector {selector}>"

            print(indent + header)
            print(indent + f"      status={'OK' if status else 'FAIL'}, gasUsed={gas_used}, value={value}")

            call_params = decoded.get("callParams") or []
            if call_params:
                arg_strs = []
                for p in call_params:
                    arg_name = p.get("name") or ""
                    arg_type = p.get("type") or ""
                    arg_val = p.get("value")
                    arg_strs.append(f"{arg_name}:{arg_type}={arg_val}")
                print(indent + "      args: " + ", ".join(arg_strs))

            ret_params = decoded.get("returnParams") or []
            if ret_params:
                ret_strs = []
                for r in ret_params:
                    r_type = r.get("type") or ""
                    r_val = r.get("value")
                    ret_strs.append(f"{r_type}={r_val}")
                print(indent + "      returns: " + ", ".join(ret_strs))

        elif node_type == 3:
            rd = node.get("slotReadData", {}) or {}
            contract = rd.get("contract", "")
            key = rd.get("key", "")
            value = rd.get("value", "")
            try:
                value_int = int(value, 16)
                value_repr = f"{value} ({value_int})"
            except Exception:
                value_repr = value
            print(indent + f"[{node_id}] SLOT READ  contract={_format_addr(contract, labels)}")
            print(indent + f"      key={key}")
            print(indent + f"      value={value_repr}")

        elif node_type == 4:
            wd = node.get("slotWriteData", {}) or {}
            contract = wd.get("contract", "")
            key = wd.get("key", "")
            prev = wd.get("prev", "")
            current = wd.get("current", "")
            try:
                prev_int = int(prev, 16)
                prev_repr = f"{prev} ({prev_int})"
            except Exception:
                prev_repr = prev
            try:
                curr_int = int(current, 16)
                curr_repr = f"{current} ({curr_int})"
            except Exception:
                curr_repr = current
            print(indent + f"[{node_id}] SLOT WRITE contract={_format_addr(contract, labels)}")
            print(indent + f"      key={key}")
            print(indent + f"      prev={prev_repr}")
            print(indent + f"      curr={curr_repr}")

        else:
            print(indent + f"[{node_id}] nodeType={node_type} (unsupported)")

        print()

    print("=============================================")
    print("===============  TRACE 解析结束  ===============")


def _generate_trace_markdown(
    trace_path: Path,
    label_path: Path = None,
    only_contract: str = None,
    attacker_address: str = "",
) -> str:
    """生成 trace.json 的人类可读 Markdown 文本"""
    if not trace_path.exists():
        return f"[⚠️] trace.json 文件不存在: {trace_path}"

    try:
        data = json.loads(trace_path.read_text(encoding="utf-8"))
    except Exception as e:
        return f"[⚠️] 读取 trace.json 失败: {e}"

    data_map = data.get("dataMap", {}) or {}
    labels = _load_labels(label_path) if label_path else {}

    # 将 key 转为 int，并按升序排序，形成执行时间线
    items = []
    for k, v in data_map.items():
        try:
            node_id = int(k)
        except ValueError:
            continue
        items.append((node_id, v))
    items.sort(key=lambda x: x[0])

    only_contract = (only_contract or "").lower()
    attacker_address = (attacker_address or "").lower()
    call_stack = []  # 简单的基于 fromAddress 的调用栈

    lines = []
    lines.append("# TRACE 调用时间线")
    lines.append("")
    lines.append("> **过滤规则**: 只显示攻击者对外部合约的调用 + 受害者合约相关调用")
    lines.append("")

    for node_id, node in items:
        node_type = node.get("nodeType")

        # 计算调用深度
        depth = len(call_stack)
        if node_type == 0:
            inv = node.get("invocation", {}) or {}
            from_addr = (inv.get("fromAddress") or "").lower()
            to_addr = (inv.get("address") or "").lower()

            if not call_stack:
                call_stack = [{"address": to_addr}]
                depth = 0
            else:
                idx = None
                for i, frame in enumerate(call_stack):
                    if frame["address"] == from_addr:
                        idx = i
                        break
                if idx is None:
                    # 找不到父节点，当作新的调用链
                    call_stack = [{"address": to_addr}]
                    depth = 0
                else:
                    call_stack = call_stack[: idx + 1]
                    depth = len(call_stack)
                    call_stack.append({"address": to_addr})
        else:
            depth = len(call_stack)

        # 新的过滤逻辑：只保留政击者对外部合约的调用 + 受害者合约相关调用
        should_include = False
        
        if node_type == 0:
            inv = node.get("invocation", {}) or {}
            addr_to = (inv.get("address") or "").lower()
            addr_from = (inv.get("fromAddress") or "").lower()
            
            # 情兵1：攻击者直接调用外部合约
            if attacker_address and addr_from == attacker_address:
                should_include = True
            
            # 情兵2：与受害者合约相关的调用
            if only_contract and (addr_to == only_contract or addr_from == only_contract):
                should_include = True
                
        elif node_type in [3, 4]:  # SLOT READ/WRITE
            # 只保留受害者合约的状态变化
            if node_type == 3:
                rd = node.get("slotReadData", {}) or {}
                addr = (rd.get("contract") or "").lower()
            else:
                wd = node.get("slotWriteData", {}) or {}
                addr = (wd.get("contract") or "").lower()
            
            if only_contract and addr == only_contract:
                should_include = True
        
        if not should_include:
            continue

        indent = "  " * depth

        if node_type == 0:
            inv = node.get("invocation", {}) or {}
            to_addr = inv.get("address", "")
            from_addr = inv.get("fromAddress", "")
            op = inv.get("operation", "") or "CALL"
            gas_used = inv.get("gasUsed", 0)
            status = inv.get("status", False)
            value = inv.get("value", "0")
            decoded = inv.get("decodedMethod") or {}
            if not isinstance(decoded, dict):
                decoded = {}

            name = decoded.get("name") or "unknown"
            signature = decoded.get("signature") or ""
            selector = inv.get("selector", "")

            header = f"[{node_id}] {op} {_format_addr(from_addr, labels)} -> {_format_addr(to_addr, labels)}"
            if signature:
                header += f" :: {signature}"
            elif name != "unknown":
                header += f" :: {name}"
            elif selector:
                header += f" :: <selector {selector}>"

            lines.append(indent + header)
            lines.append(indent + f"      status={'OK' if status else 'FAIL'}, gasUsed={gas_used}, value={value}")

            call_params = decoded.get("callParams") or []
            if call_params:
                arg_strs = []
                for p in call_params:
                    arg_name = p.get("name") or ""
                    arg_type = p.get("type") or ""
                    arg_val = p.get("value")
                    arg_strs.append(f"{arg_name}:{arg_type}={arg_val}")
                lines.append(indent + "      args: " + ", ".join(arg_strs))

            ret_params = decoded.get("returnParams") or []
            if ret_params:
                ret_strs = []
                for r in ret_params:
                    r_type = r.get("type") or ""
                    r_val = r.get("value")
                    ret_strs.append(f"{r_type}={r_val}")
                lines.append(indent + "      returns: " + ", ".join(ret_strs))

        elif node_type == 3:
            rd = node.get("slotReadData", {}) or {}
            contract = rd.get("contract", "")
            key = rd.get("key", "")
            value = rd.get("value", "")
            try:
                value_int = int(value, 16)
                value_repr = f"{value} ({value_int})"
            except Exception:
                value_repr = value
            lines.append(indent + f"[{node_id}] SLOT READ  contract={_format_addr(contract, labels)}")
            lines.append(indent + f"      key={key}")
            lines.append(indent + f"      value={value_repr}")

        elif node_type == 4:
            wd = node.get("slotWriteData", {}) or {}
            contract = wd.get("contract", "")
            key = wd.get("key", "")
            prev = wd.get("prev", "")
            current = wd.get("current", "")
            try:
                prev_int = int(prev, 16)
                prev_repr = f"{prev} ({prev_int})"
            except Exception:
                prev_repr = prev
            try:
                curr_int = int(current, 16)
                curr_repr = f"{current} ({curr_int})"
            except Exception:
                curr_repr = current
            lines.append(indent + f"[{node_id}] SLOT WRITE contract={_format_addr(contract, labels)}")
            lines.append(indent + f"      key={key}")
            lines.append(indent + f"      prev={prev_repr}")
            lines.append(indent + f"      curr={curr_repr}")

        else:
            lines.append(indent + f"[{node_id}] nodeType={node_type} (unsupported)")

        lines.append("")

    return "\n".join(lines)


def _generate_vuln_function_from_debug_code(
    debug_code_path: Path,
    trace_path: Path,
    label_path: Path = None,
    victim_address: str = "",
    attacker_address: str = "",
) -> str:
    """根据 debug_code.json 和 trace.json 生成 Vuln_function.md 内容"""
    if not debug_code_path.exists():
        return f"[⚠️] debug_code.json 文件不存在: {debug_code_path}"
    if not trace_path.exists():
        return f"[⚠️] trace.json 文件不存在: {trace_path}"

    try:
        # 读取 debug_code.json
        with open(debug_code_path, 'r', encoding='utf-8') as f:
            debug_data = json.load(f)
        
        # 读取 trace.json
        with open(trace_path, 'r', encoding='utf-8') as f:
            trace_data = json.load(f)
        
        # 读取标签
        labels = _load_labels(label_path) if label_path else {}
        
        code_data_map = debug_data.get("codeDataMap", {})
        code_files_map = debug_data.get("codeFilesMap", {})
        code_location_map = debug_data.get("codeLocationMap", {})
        trace_data_map = trace_data.get("dataMap", {})
        
        victim_address_lower = victim_address.lower()
        attacker_address_lower = attacker_address.lower()
        short_victim = _short_addr(victim_address)
        
        # 构建文件索引到源代码的映射
        file_index_to_code = {}
        for code_hash, files in code_files_map.items():
            if isinstance(files, list):
                for file_info in files:
                    file_idx = file_info.get("fileIndex")
                    code_content = file_info.get("code", "")
                    file_name = file_info.get("fileName", "")
                    if file_idx is not None:
                        file_index_to_code[(code_hash, file_idx)] = {
                            "code": code_content,
                            "name": file_name,
                        }
        
        # 第1步：递归识别攻击者创建的所有合约（包括子合约、孙合约等）
        attacker_created_contracts = set()
        if attacker_address_lower:
            # 第一轮：找攻击者直接创建的合约
            first_gen = set()
            for node_id, node in trace_data_map.items():
                if node.get("nodeType") == 0:
                    inv = node.get("invocation", {})
                    op = inv.get("operation", "")
                    from_addr = (inv.get("fromAddress") or "").lower()
                    to_addr = (inv.get("address") or "").lower()
                    
                    if op in ["CREATE", "CREATE2"] and from_addr == attacker_address_lower:
                        if to_addr:
                            first_gen.add(to_addr)
                            attacker_created_contracts.add(to_addr)
                            print(f"[DEBUG] 攻击者直接创建: {to_addr}")
            
            # 递归查找子合约（最多3层）
            current_gen = first_gen
            for depth in range(3):
                if not current_gen:
                    break
                next_gen = set()
                for node_id, node in trace_data_map.items():
                    if node.get("nodeType") == 0:
                        inv = node.get("invocation", {})
                        op = inv.get("operation", "")
                        from_addr = (inv.get("fromAddress") or "").lower()
                        to_addr = (inv.get("address") or "").lower()
                        
                        if op in ["CREATE", "CREATE2"] and from_addr in current_gen:
                            if to_addr and to_addr not in attacker_created_contracts:
                                next_gen.add(to_addr)
                                attacker_created_contracts.add(to_addr)
                                print(f"[DEBUG] 第{depth+2}层子合约: {to_addr} (由 {from_addr[:10]}... 创建)")
                current_gen = next_gen
        
        # 第2步：收集关键调用（扩展过滤逻辑）
        important_calls = []
        
        for node_id, node in trace_data_map.items():
            if node.get("nodeType") == 0:  # 调用类型
                inv = node.get("invocation", {})
                to_addr = (inv.get("address") or "").lower()
                from_addr = (inv.get("fromAddress") or "").lower()
                
                decoded = inv.get("decodedMethod") or {}
                func_name = decoded.get("name", "unknown")
                func_sig = decoded.get("signature", "")
                
                is_important = False
                call_type = ""
                priority = 0  # 优先级，数字越大越重要
                
                # 情兵1: 调用了受害者合约
                if to_addr == victim_address_lower:
                    is_important = True
                    call_type = "受害者合约被调用"
                    priority = 2
                
                # 情兵2: 攻击者直接调用
                if attacker_address_lower and from_addr == attacker_address_lower:
                    is_important = True
                    call_type = "攻击者直接调用"
                    priority = 3
                
                # 情兵3: 攻击者创建的合约调用外部合约（⚠️ 关键改进）
                if from_addr in attacker_created_contracts:
                    is_important = True
                    call_type = "攻击合约调用外部"
                    priority = 4  # 最高优先级，因为这可能是漏洞入口
                
                if is_important:
                    important_calls.append({
                        "node_id": node_id,
                        "func_name": func_name,
                        "func_sig": func_sig,
                        "from_addr": from_addr,
                        "to_addr": to_addr,
                        "invocation": inv,
                        "call_type": call_type,
                        "priority": priority,
                    })
        
        if not important_calls:
            return "[⚠️] 未找到与受害者合约或攻击者相关的调用"
        
        # 按优先级和 node_id 排序
        important_calls.sort(key=lambda x: (-x["priority"], int(x["node_id"])))
        
        # 按函数名分组
        func_groups = {}
        for call in important_calls:
            key = f"{call['to_addr']}_{call['func_name']}"
            if key not in func_groups:
                func_groups[key] = []
            func_groups[key].append(call)
        
        # 生成 Markdown
        lines = []
        lines.append("# 关键函数调用与代码映射")
        lines.append("")
        lines.append("> **分析范围**: 攻击者直接调用 + 攻击合约调用外部 + 受害者合约被调用")
        lines.append("")
        
        # 统计信息
        if attacker_created_contracts:
            lines.append(f"> **攻击者创建的合约**: {len(attacker_created_contracts)} 个")
            for addr in list(attacker_created_contracts)[:3]:
                lines.append(f">   - `{addr}`")
            lines.append("")
        
        # 输出 Trace 部分
        lines.append("## Trace")
        lines.append("```text")
        for key, calls in func_groups.items():
            for call in calls:
                node_id = call["node_id"]
                inv = call["invocation"]
                op = inv.get("operation", "CALL")
                status = inv.get("status", False)
                gas_used = inv.get("gasUsed", 0)
                value = inv.get("value", "0")
                
                from_fmt = _format_addr(call["from_addr"], labels)
                to_fmt = _format_addr(call["to_addr"], labels)
                
                header = f"[{node_id}] {op} {from_fmt} -> {to_fmt}"
                if call["func_sig"]:
                    header += f" :: {call['func_sig']}"
                elif call["func_name"] != "unknown":
                    header += f" :: {call['func_name']}"
                
                header += f" \u26a0\ufe0f ({call['call_type']})"
                
                lines.append(header)
                lines.append(f"      status={'OK' if status else 'FAIL'}, gasUsed={gas_used}, value={value}")
                
                # 输出参数
                decoded = inv.get("decodedMethod", {}) or {}
                call_params = decoded.get("callParams", [])
                if call_params:
                    arg_strs = []
                    for p in call_params:
                        arg_name = p.get("name", "")
                        arg_type = p.get("type", "")
                        arg_val = p.get("value")
                        arg_strs.append(f"{arg_name}:{arg_type}={arg_val}")
                    lines.append("      args: " + ", ".join(arg_strs))
                
                lines.append("")
        lines.append("```")
        lines.append("")
        
        # 输出 Code 部分
        lines.append("## Code")
        for key, calls in func_groups.items():
            if not calls or len(calls) == 0:
                continue
                
            # 使用第一个调用的签名
            first_call = calls[0]
            func_sig = first_call.get("func_sig", "")
            func_name = first_call.get("func_name", "unknown")
            to_addr = first_call.get("to_addr", "")
            call_type = first_call.get("call_type", "")
            display_name = func_sig if func_sig else f"{func_name}()"
            
            lines.append(f"### {display_name}")
            lines.append(f"**合约地址:** `{to_addr}`")
            lines.append(f"**调用类型:** {call_type}")
            lines.append("")
            
            # 查找函数定义位置和调用位置
            node_id = first_call.get("node_id", "")
            location = code_location_map.get(str(node_id), {})
            def_location = location.get("defCodeLocation", {}) if location else {}
            call_location = location.get("callCodeLocation", {}) if location else {}
            
            # 显示函数定义
            def_code_hash = def_location.get("codeHash", "")
            def_file_index = def_location.get("fileIndex", 0)
            def_start_line = def_location.get("startLine", 0)
            def_end_line = def_location.get("endLine", 0)
            def_sourced = def_location.get("sourced", False)
            
            if def_sourced and def_code_hash and (def_code_hash, def_file_index) in file_index_to_code:
                file_data = file_index_to_code[(def_code_hash, def_file_index)]
                code_content = file_data["code"]
                file_name = file_data["name"]
                
                code_lines = code_content.splitlines()
                
                lines.append(f"**函数定义文件:** `{file_name}`")
                lines.append("")
                lines.append("```solidity")
                
                # 输出函数代码 (1-based line numbers)
                for line_no in range(def_start_line, def_end_line + 1):
                    if line_no > 0 and line_no <= len(code_lines):
                        actual_line = code_lines[line_no - 1]
                        lines.append(f"{line_no:4d} | {actual_line}")
                
                lines.append("```")
            else:
                lines.append("```text")
                lines.append("未找到函数定义位置")
                lines.append("```")
            
            lines.append("")
            
            # 显示调用位置（如果存在）
            call_code_hash = call_location.get("codeHash", "")
            call_file_index = call_location.get("fileIndex", 0)
            call_start_line = call_location.get("startLine", 0)
            call_end_line = call_location.get("endLine", 0)
            call_sourced = call_location.get("sourced", False)
            
            if call_sourced and call_code_hash and (call_code_hash, call_file_index) in file_index_to_code:
                call_file_data = file_index_to_code[(call_code_hash, call_file_index)]
                call_code_content = call_file_data["code"]
                call_file_name = call_file_data["name"]
                
                call_code_lines = call_code_content.splitlines()
                
                lines.append(f"**调用位置:** `{call_file_name}` (行 {call_start_line}-{call_end_line})")
                lines.append("")
                lines.append("```solidity")
                
                # 输出调用代码 (1-based line numbers)
                for line_no in range(call_start_line, call_end_line + 1):
                    if line_no > 0 and line_no <= len(call_code_lines):
                        actual_line = call_code_lines[line_no - 1]
                        lines.append(f"{line_no:4d} | {actual_line}")
                
                lines.append("```")
                lines.append("")
        
        return "\n".join(lines)
        
    except Exception as e:
        import traceback
        traceback_str = traceback.format_exc()
        return f"[⚠️] 生成 Vuln_function.md 失败: {e}\n\n{traceback_str}"

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='区块链安全事件分析工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
使用示例:
  # 分析以太坊主网交易
  python main.py --chain-id 1 --txn-hash 0xad2ca822b3adee0768d7d34b68ee4cc3c4822347d963f1d0c970c9c8cd2b6a33
  
  # 使用无头模式（适合服务器环境）
  python main.py --chain-id 1 --txn-hash 0x... --headless
  
  # 指定输出目录
  python main.py --chain-id 1 --txn-hash 0x... --output-dir /path/to/output
  
支持的链:
  1  - Ethereum Mainnet
  56 - BSC
  137 - Polygon
  42161 - Arbitrum
  10 - Optimism
        '''
    )
    
    parser.add_argument(
        '--chain-id',
        type=int,
        default=1,
        help='链id (1=Ethereum, 56=BSC, 137=Polygon, 默认: 1)'
    )
    
    parser.add_argument(
        '--txn-hash',
        type=str,
        help='交易哈希 (0x...)',
        required=False
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='../Json_Report',
        help='输出目录路径 (默认: ../Json_Report)'
    )
    
    parser.add_argument(
        '--headless',
        action='store_true',
        default=False,
        help='使用无头模式运行浏览器（默认：显示浏览器窗口）'
    )
    
    parser.add_argument(
        '--deep-analysis',
        action='store_true',
        default=False,
        help='执行深度漏洞函数分析（需要读取 trace.json）'
    )
    
    args = parser.parse_args()
    
    # 如果没有提供参数，使用默认示例交易
    if not args.txn_hash:
        args.txn_hash = "0xad2ca822b3adee0768d7d34b68ee4cc3c4822347d963f1d0c970c9c8cd2b6a33"
    
    print(f"\n[ℹ️] Chain: {args.chain_id} | TxHash: {args.txn_hash}")
    
    try:
        report = analyze_blocksec_transaction(
            chain_id=args.chain_id,
            txn_hash=args.txn_hash,
            output_dir=args.output_dir,
            headless=args.headless,
            deep_analysis=args.deep_analysis
        )
        print("\n[✓] 分析完成")
        return report
    except KeyboardInterrupt:
        print("\n[!] 用户中断")
        sys.exit(0)
    except Exception as e:
        # 精简错误输出，只显示核心错误信息
        error_msg = str(e).split('\n')[0] if '\n' in str(e) else str(e)
        print(f"\n[✗] 分析失败: {error_msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
