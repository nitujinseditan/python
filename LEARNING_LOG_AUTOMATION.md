# 学习日志自动化

这个工具在每天凌晨 02:00（中国时区）生成上一轮学习的审核包。

例如在 2026-07-19 02:00 运行时，它汇总 2026-07-18 02:00（含）至 2026-07-19 02:00（不含）的已提交内容，并将日志命名为 `2026-07-18.md`。

它只上传 GitHub Actions Artifact，不会自动提交、修改源码或创建 Issue。

## 需要配置一次

在 GitHub 仓库打开 **Settings → Secrets and variables → Actions → New repository secret**，添加：

```text
Name: DEEPSEEK_API_KEY
Secret: 你的 DeepSeek API Key
```

不要把密钥写入代码、配置文件或提交信息。

未配置密钥时，工作流仍会完成：它会生成事实材料和基础日志，但跳过模型总结；Artifact 中会写明原因。

## 手动运行

在仓库的 **Actions → Daily learning log draft → Run workflow** 中：

- 留空日期：生成最近一个完整的 02:00 到 02:00 学习窗口；
- 填写 `2026-07-18`：生成 2026-07-18 02:00 至 2026-07-19 02:00 的草稿。

也可以在本地运行（需要 Python 3.10+）：

```powershell
py -3 scripts/run_daily_learning_log.py --learning-date 2026-07-18 --output .learning-log-artifacts
```

## Artifact 内容

```text
daily-learning-log-artifact/
├── learning_logs/YYYY-MM-DD.md   # 供你阅读的日志草稿
├── evidence.json                 # Git、文件、README、TODO 等事实材料
├── context-bundle.json           # 提供给模型的受控上下文
├── model-draft.json              # 模型的结构化输出或无密钥降级输出
├── context-update-proposal.md    # 供你审核的长期上下文更新建议
└── validation-report.md          # 证据 ID 校验结果
```

## 长期学习上下文

- `learning_context/learning_map.json`：学习阶段、主题和长期目标。
- `learning_context/projects/`：重点项目的演进、限制和可回访方向。

模型只会在日志中提出更新建议；请你审核后，手工更新这些文件。这样长期学习记忆可追溯，也不会被一次错误总结污染。

## 安全与边界

- 仅收集指定学习窗口内的已提交 Git 改动。
- 自动忽略 `.env`、密钥、私钥、缓存和 IDE 文件。
- 对疑似 API Key 和 Bearer Token 做脱敏。
- 每条模型结论必须引用已提供的证据 ID；校验报告会标出未知引用。
- 代码、注释和 README 会被作为数据而非指令传给模型。

模型使用 `deepseek-v4-flash` 的非思考模式，输出严格 JSON，再由本地脚本渲染为 Markdown。
