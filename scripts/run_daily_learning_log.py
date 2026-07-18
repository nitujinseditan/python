#!/usr/bin/env python3
"""Build a complete review artifact for the most recently completed learning day."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(script: str, *args: str) -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / script), *args], cwd=ROOT, check=True)


def bullet_items(items: list[dict], key: str) -> list[str]:
    return [f"- {item.get(key, '（无内容）')}" for item in items] or ["- 无"]


def render_markdown(evidence: dict, draft: dict) -> str:
    window = evidence["window"]
    commits = evidence["git"]["commits"]
    files = evidence["git"]["changed_files"]
    next_steps = draft.get("next_steps", {})
    lines = [
        f"# {window['learning_date']} 学习日志（草稿）",
        "",
        f"学习窗口：{window['start']} 至 {window['end']}",
        "",
        "## 一句话总结",
        "",
        draft.get("summary", "未生成总结。"),
        "",
        "## 今天新增的内容",
        "",
    ]
    for item in draft.get("new_learning", []):
        lines.extend([f"### {item.get('title', '未命名主题')}", *bullet_items([{"text": detail} for detail in item.get("details", [])], "text"), ""])
    if not draft.get("new_learning"):
        lines.append("- 未从本次材料中确认新的学习主题。")
    lines.extend(["", "## 今天真正理解的内容", ""])
    lines.extend(bullet_items(draft.get("understood", []), "statement"))
    lines.extend(["", "## 尚未解决的问题", ""])
    lines.extend(bullet_items(draft.get("unresolved", []), "item"))
    lines.extend(["", "## 下一步待办", "", "### 必做", ""])
    lines.extend(bullet_items(next_steps.get("must_do", []), "item"))
    lines.extend(["", "### 巩固", ""])
    lines.extend(bullet_items(next_steps.get("reinforcement", []), "item"))
    lines.extend(["", "### 旧项目回访", ""])
    lines.extend(bullet_items(next_steps.get("project_revisit", []), "item"))
    suggestion = draft.get("tomorrow_suggestion", {}).get("item", "无")
    lines.extend(["", "## 明日建议", "", suggestion, "", "## 今日提交", ""])
    if commits:
        lines.extend([f"- `{item['sha']}` {item['subject']}" for item in commits])
    else:
        lines.append("- 本学习窗口没有发现已提交内容。")
    lines.extend(["", "## 本次变更文件", ""])
    lines.extend([f"- `{item['path']}`（{item['status']}）" for item in files] or ["- 无"])
    lines.extend(["", "## 待确认的观察", ""])
    lines.extend(bullet_items(draft.get("observations_to_confirm", []), "item"))
    lines.extend(["", "## 长期上下文更新建议", "", "### 学习地图", ""])
    lines.extend([f"- {item}" for item in draft.get("context_update_proposal", {}).get("learning_map", [])] or ["- 无"])
    lines.extend(["", "### 项目档案", ""])
    lines.extend([f"- {item}" for item in draft.get("context_update_proposal", {}).get("project_notes", [])] or ["- 无"])
    lines.extend(["", "## 生成依据", "", "- 本次 Artifact 中的 `evidence.json`、`context-bundle.json` 和 `validation-report.md`。", "- 模型建议仅为草稿，须人工确认后才能写入长期学习档案。"])
    return "\n".join(lines) + "\n"


def render_context_proposal(draft: dict) -> str:
    proposal = draft.get("context_update_proposal", {})
    lines = ["# 长期学习上下文更新建议（草稿）", "", "以下内容由日志生成器提出，尚未写入仓库。请审核后手动更新相应文件。", "", "## 学习地图", ""]
    lines.extend([f"- {item}" for item in proposal.get("learning_map", [])] or ["- 无建议。"])
    lines.extend(["", "## 项目档案", ""])
    lines.extend([f"- {item}" for item in proposal.get("project_notes", [])] or ["- 无建议。"])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / ".learning-log-artifacts")
    parser.add_argument("--learning-date", help="Window start date (YYYY-MM-DD), starting at 02:00 China time.")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    evidence_path = output / "evidence.json"
    context_path = output / "context-bundle.json"
    draft_path = output / "model-draft.json"
    validation_path = output / "validation-report.md"
    command_args = ["--output", str(evidence_path)]
    if args.learning_date:
        command_args.extend(["--learning-date", args.learning_date])
    run("collect_daily_changes.py", *command_args)
    run("build_context.py", "--evidence", str(evidence_path), "--output", str(context_path))
    run("generate_learning_log.py", "--context", str(context_path), "--output", str(draft_path))
    run("validate_log.py", "--context", str(context_path), "--draft", str(draft_path), "--output", str(validation_path))
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    draft = json.loads(draft_path.read_text(encoding="utf-8"))
    learning_date = evidence["window"]["learning_date"]
    log_dir = output / "learning_logs"
    log_dir.mkdir(exist_ok=True)
    (log_dir / f"{learning_date}.md").write_text(render_markdown(evidence, draft), encoding="utf-8")
    (output / "context-update-proposal.md").write_text(render_context_proposal(draft), encoding="utf-8")
    print(f"Created review artifact: {output}")


if __name__ == "__main__":
    main()
