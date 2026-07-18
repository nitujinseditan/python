#!/usr/bin/env python3
"""Collect verifiable Git and repository evidence for one 02:00-to-02:00 learning day."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".py", ".md", ".json", ".txt", ".yml", ".yaml", ".toml", ".js", ".html", ".css"}
TODO_SUFFIXES = {".py", ".js", ".ts", ".java", ".c", ".cpp", ".h", ".cs", ".go", ".rs"}
TODO_PATTERN = re.compile(r"\b(TODO|FIXME)\b|NotImplementedError")
TOKEN_PATTERN = re.compile(r"(?i)(sk-[a-z0-9_-]{12,}|api[_-]?key\s*[:=]\s*['\"]?[^\s'\"]+|bearer\s+[a-z0-9._-]{12,})")


def load_config() -> dict:
    return json.loads((ROOT / "learning_log_config.json").read_text(encoding="utf-8"))


def git(*args: str, check: bool = True) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if check and completed.returncode:
        raise RuntimeError(completed.stderr.strip() or f"git {' '.join(args)} failed")
    return completed.stdout.strip()


def learning_window(config: dict, learning_date: str | None) -> tuple[datetime, datetime]:
    zone = ZoneInfo(config["timezone"])
    cutoff = int(config["learning_day_cutoff_hour"])
    if learning_date:
        start_date = date.fromisoformat(learning_date)
    else:
        now = datetime.now(zone)
        end_today = datetime.combine(now.date(), time(cutoff), zone)
        start_date = (end_today.date() - timedelta(days=1)) if now >= end_today else (end_today.date() - timedelta(days=2))
    start = datetime.combine(start_date, time(cutoff), zone)
    return start, start + timedelta(days=1)


def is_ignored(path: str, config: dict) -> bool:
    normalized = path.replace("\\", "/").lower()
    if any(part.lower() in normalized for part in config["ignore_paths"]):
        return True
    name = Path(normalized).name
    return any(pattern.lower() in name for pattern in config["sensitive_file_patterns"])


def redact(value: str) -> str:
    return TOKEN_PATTERN.sub("[REDACTED]", value)


def clipped_diff(base: str | None, path: str, config: dict) -> tuple[str, bool]:
    args = ["diff", "--no-ext-diff", "--unified=3"]
    args.append(base if base else "4b825dc642cb6eb9a060e54bf8d69288fbee4904")
    args.extend(["HEAD", "--", path])
    diff = redact(git(*args, check=False))
    lines = diff.splitlines()
    limit = int(config["max_diff_lines_per_file"])
    return "\n".join(lines[:limit]), len(lines) > limit


def collect_todos(config: dict) -> list[dict]:
    todos: list[dict] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TODO_SUFFIXES:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if is_ignored(rel, config):
            continue
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for index, line in enumerate(lines, start=1):
            if TODO_PATTERN.search(line):
                todos.append({"id": f"todo:{rel}:{index}", "path": rel, "line": index, "text": redact(line.strip())})
    return todos[:100]


def readme_excerpts(config: dict) -> list[dict]:
    excerpts: list[dict] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        if "readme" not in path.name.lower() or is_ignored(rel, config):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        excerpts.append({"id": f"readme:{rel}", "path": rel, "content": redact(text[:6000])})
    return excerpts[:12]


def collect(config: dict, learning_date: str | None) -> dict:
    start, end = learning_window(config, learning_date)
    since, before = start.isoformat(), end.isoformat()
    records = git("log", "HEAD", f"--since={since}", f"--before={before}", "--format=%H%x1f%h%x1f%aI%x1f%s").splitlines()
    commits = []
    for record in records:
        parts = record.split("\x1f")
        if len(parts) == 4:
            full, short, committed_at, subject = parts
            commits.append({"id": f"commit:{short}", "sha": short, "full_sha": full, "committed_at": committed_at, "subject": redact(subject)})
    base = git("rev-list", "-1", f"--before={since}", "HEAD", check=False) or None
    changed: list[dict] = []
    if commits:
        comparison = [base or "4b825dc642cb6eb9a060e54bf8d69288fbee4904", "HEAD"]
        for row in git("diff", "--name-status", *comparison).splitlines():
            bits = row.split("\t")
            if len(bits) < 2:
                continue
            status, path = bits[0], bits[-1]
            if is_ignored(path, config):
                continue
            suffix = Path(path).suffix.lower()
            diff, truncated = ("", False) if suffix not in TEXT_SUFFIXES else clipped_diff(base, path, config)
            changed.append({"id": f"file:{path}", "path": path, "status": status, "diff": diff, "diff_truncated": truncated})
    all_diff_lines = 0
    for item in changed:
        lines = item["diff"].splitlines()
        remaining = max(0, int(config["max_total_diff_lines"]) - all_diff_lines)
        item["diff"] = "\n".join(lines[:remaining])
        item["diff_truncated"] = item["diff_truncated"] or len(lines) > remaining
        all_diff_lines += len(item["diff"].splitlines())
    return {
        "window": {"learning_date": start.date().isoformat(), "start": start.isoformat(), "end": end.isoformat(), "timezone": config["timezone"]},
        "git": {"head": git("rev-parse", "--short", "HEAD"), "base": (base[:7] if base else None), "commits": commits, "changed_files": changed},
        "todos": collect_todos(config),
        "readme_excerpts": readme_excerpts(config),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--learning-date", help="Window start date (YYYY-MM-DD); it starts at 02:00 Asia/Shanghai.")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(collect(load_config(), args.learning_date), ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
