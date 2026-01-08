"""
主程序入口

区块链安全事件分析工具
"""

import argparse
import sys
import json
from pathlib import Path
from analyzers import BlocksecAnalyzer
from utils.contract_fetcher import ContractFetcher


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
            report_file = contract_output_path / "report.md"
            trace_file = contract_output_path / "trace.json"
            label_file = contract_output_path / "address_label.json"

            victim_address = ""
            if report_file.exists():
                report_content = report_file.read_text(encoding="utf-8")
                victim_address = extract_victim_address(report_content)

            # 先解析 trace 调用时间线，方便人工定位
            if trace_file.exists():
                trace_md = _generate_trace_markdown(
                    trace_path=trace_file,
                    label_path=label_file if label_file.exists() else None,
                    only_contract=victim_address or None,
                )
                trace_md_file = contract_output_path / "trace.md"
                trace_md_file.write_text(trace_md, encoding="utf-8")
                print(f"[✓] trace.md")

            # 然后使用 Selenium 获取受害者合约源代码
            if report_file.exists():
                if victim_address:
                    fetcher = ContractFetcher(chain_id)
                    code = fetcher.fetch_contract_code_with_selenium(
                        driver=analyzer.driver,
                        address=victim_address,
                        wait_time=8,
                    )
                    if code:
                        contract_output_path.mkdir(parents=True, exist_ok=True)
                        fetcher.save_contract_code(code, contract_output_path)
                        # 生成函数调用与代码映射报告
                        vuln_md = _generate_vuln_function_markdown(
                            trace_md_path=contract_output_path / "trace.md",
                            contract_path=contract_output_path / "contract_code.sol",
                            victim_address=victim_address,
                        )
                        vuln_file = contract_output_path / "Vuln_function.md"
                        vuln_file.write_text(vuln_md, encoding="utf-8")
                        print(f"[✓] contract_code.sol + Vuln_function.md")
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


def _generate_trace_markdown(trace_path: Path, label_path: Path = None, only_contract: str = None) -> str:
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
    call_stack = []  # 简单的基于 fromAddress 的调用栈

    lines = []
    lines.append("# TRACE 调用时间线")
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


def _generate_vuln_function_markdown(trace_md_path: Path, contract_path: Path, victim_address: str) -> str:
    """根据 trace.md 和合约源码生成 Vuln_function.md 内容"""
    if not trace_md_path.exists():
        return f"[⚠️] trace.md 文件不存在: {trace_md_path}"
    if not contract_path.exists():
        return f"[⚠️] contract_code.sol 文件不存在: {contract_path}"

    trace_text = trace_md_path.read_text(encoding="utf-8")
    trace_lines = trace_text.splitlines()

    # 计算受害者地址的缩写形式，便于匹配 "-> 0xb9d195...d158"
    short_victim = _short_addr(victim_address)

    # 从 trace 中收集 "调用受害合约" 的片段，按函数分组
    func_traces: Dict[str, Dict[str, Any]] = {}
    i = 0
    while i < len(trace_lines):
        line = trace_lines[i]
        # 只关注包含 "::" 且指向受害合约的调用行
        if "::" in line and "->" in line and short_victim in line:
            # 函数签名在 "::" 之后
            try:
                func_part = line.split("::", 1)[1].strip()
            except Exception:
                i += 1
                continue
            if not func_part:
                i += 1
                continue
            func_name = func_part.split("(", 1)[0].strip()

            # 捕获从这一行开始，到下一段空行前的所有内容，作为该调用的 trace 片段
            snippet_lines = [line]
            j = i + 1
            while j < len(trace_lines) and trace_lines[j].strip() != "":
                snippet_lines.append(trace_lines[j])
                j += 1

            if func_name not in func_traces:
                func_traces[func_name] = {
                    "signature": func_part,
                    "trace": snippet_lines,
                }

            i = j
        else:
            i += 1

    # 解析合约源码，按函数名提取起止行号
    source_text = contract_path.read_text(encoding="utf-8")
    source_lines = source_text.splitlines()
    func_spans: Dict[str, Any] = {}

    line_count = len(source_lines)
    idx = 0
    while idx < line_count:
        line = source_lines[idx]
        if "function " in line:
            # 尝试从这一行提取函数名
            sig_part = line.split("function ", 1)[1]
            sig_part = sig_part.strip()
            if not sig_part:
                idx += 1
                continue
            name_token = sig_part.split("(", 1)[0].strip().split()[0]
            func_name = name_token

            # 找到函数体的花括号范围
            brace_count = line.count("{") - line.count("}")
            start_idx = idx
            j = idx
            # 如果当前行没有 "{"，向后寻找
            while brace_count <= 0 and j + 1 < line_count:
                j += 1
                brace_count += source_lines[j].count("{") - source_lines[j].count("}")
            # 继续直到花括号平衡
            while brace_count > 0 and j + 1 < line_count:
                j += 1
                brace_count += source_lines[j].count("{") - source_lines[j].count("}")

            end_idx = j
            start_line_no = start_idx + 1  # 1-based
            end_line_no = end_idx + 1

            # 只记录第一次出现的 span
            if func_name not in func_spans:
                func_spans[func_name] = {
                    "start": start_line_no,
                    "end": end_line_no,
                }

            idx = j + 1
        else:
            idx += 1

    # 组装 Vuln_function.md
    lines = []
    lines.append("# 受害合约函数调用与代码映射")
    lines.append("")
    lines.append("## Trace")
    lines.append("```text")
    for func_name, info in func_traces.items():
        for l in info["trace"]:
            lines.append(l)
        lines.append("")
    lines.append("```")
    lines.append("")

    lines.append("## Code")
    for func_name, info in func_traces.items():
        signature = info["signature"]
        display_name = signature if signature else f"{func_name}()"
        lines.append(f"### {display_name}")
        span = func_spans.get(func_name)
        if span:
            start = span["start"] - 1  # 转为 0-based
            end = span["end"]  # end 本身是 1-based inclusive，用作切片的右边界
            func_code_lines = source_lines[start:end]
            lines.append("```solidity")
            for line_no in range(start, end):
                actual_line = source_lines[line_no] if line_no < len(source_lines) else ""
                lines.append(f"{line_no + 1:4d} | {actual_line}")
            lines.append("```")
        else:
            lines.append("```text")
            lines.append("未在 contract_code.sol 中找到该函数定义")
            lines.append("```")
        lines.append("")

    return "\n".join(lines)


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
