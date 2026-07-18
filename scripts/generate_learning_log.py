#!/usr/bin/env python3
"""Ask DeepSeek for a JSON learning-log draft, with a local fallback when no key is available."""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fallback(bundle: dict, reason: str) -> dict:
    commits = bundle["evidence"]["git"]["commits"]
    files = bundle["evidence"]["git"]["changed_files"]
    todos = bundle["evidence"]["todos"]
    return {
        "summary": "未调用模型；此草稿仅整理了可核对的 Git 与仓库事实。" if commits else "本学习窗口没有发现已提交的学习改动。",
        "new_learning": [],
        "understood": [],
        "unresolved": [{"item": todo["text"], "evidence_ids": [todo["id"]]} for todo in todos],
        "next_steps": {
            "must_do": [{"item": f"检查：{todo['text']}", "evidence_ids": [todo["id"]]} for todo in todos],
            "reinforcement": [],
            "project_revisit": [],
        },
        "tomorrow_suggestion": {"item": "先核对当天的提交与 TODO，再决定下一步。", "evidence_ids": [item["id"] for item in commits[:1] or files[:1]]},
        "observations_to_confirm": [{"item": reason, "evidence_ids": []}],
        "context_update_proposal": {"learning_map": [], "project_notes": []},
        "generation": {"mode": "fallback", "reason": reason},
    }


def call_model(bundle: dict, config: dict) -> dict:
    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        return fallback(bundle, "未设置 DEEPSEEK_API_KEY，已跳过模型总结。")
    prompt = (ROOT / "prompts" / "learning_log_prompt.md").read_text(encoding="utf-8")
    payload = {
        "model": config["model"]["name"],
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": json.dumps(bundle, ensure_ascii=False)},
        ],
        "thinking": {"type": config["model"]["thinking"]},
        "response_format": {"type": "json_object"},
        "max_tokens": config["model"]["max_output_tokens"],
        "stream": False,
    }
    request = urllib.request.Request(
        config["model"]["base_url"],
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=75) as response:
            result = json.loads(response.read().decode("utf-8"))
        content = result["choices"][0]["message"]["content"]
        draft = json.loads(content)
        draft["generation"] = {"mode": "deepseek", "model": config["model"]["name"], "usage": result.get("usage", {})}
        return draft
    except Exception as exc:  # A failed optional model call must not prevent the evidence artifact from uploading.
        return fallback(bundle, f"模型调用或 JSON 解析失败：{exc}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--context", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    config = json.loads((ROOT / "learning_log_config.json").read_text(encoding="utf-8"))
    draft = call_model(json.loads(args.context.read_text(encoding="utf-8")), config)
    args.output.write_text(json.dumps(draft, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
