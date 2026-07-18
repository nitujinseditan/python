#!/usr/bin/env python3
"""Validate that model claims point to evidence IDs supplied in the context bundle."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def walk(value, location="root"):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "evidence_ids" and isinstance(child, list):
                yield location, child
            else:
                yield from walk(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{location}[{index}]")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--context", type=Path, required=True)
    parser.add_argument("--draft", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    known = set(json.loads(args.context.read_text(encoding="utf-8"))["available_evidence_ids"])
    draft = json.loads(args.draft.read_text(encoding="utf-8"))
    warnings = []
    checked = 0
    for location, ids in walk(draft):
        checked += 1
        unknown = [item for item in ids if item not in known]
        if unknown:
            warnings.append(f"{location} 引用了未知证据：{', '.join(unknown)}")
    mode = draft.get("generation", {}).get("mode", "unknown")
    lines = ["# 学习日志校验报告", "", f"生成模式：`{mode}`", f"检查到的证据引用字段：{checked}", ""]
    if warnings:
        lines.extend(["## 需要人工复核", "", *[f"- {warning}" for warning in warnings]])
    else:
        lines.extend(["## 结果", "", "- 所有已给出的证据 ID 均可在本次上下文包中找到。", "- 这只校验证据引用，不代表模型的解释一定正确；请仍然审核草稿。"])
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
