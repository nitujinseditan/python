const weeks = [
  {
    title: "先让代码跑起来", subtitle: "认识 Python，建立“写—跑—看—改”的最小循环",
    days: [
      ["环境与第一行代码", "会在终端运行 .py 文件，并读懂输出。", ["安装/确认 Python 与编辑器，运行 python --version", "新建 hello_agent.py，打印姓名与学习目标", "故意删掉一个引号，观察并记录 SyntaxError"]],
      ["变量与基本类型", "能用变量描述一个 Agent 用户。", ["学习 str、int、float、bool 与 type()", "创建用户画像的 5 个变量并打印", "用 f-string 生成一句完整自我介绍"]],
      ["输入、输出与类型转换", "写出会询问用户的命令行程序。", ["练习 input()、int()、float()", "编写年龄计算器：输入出生年，输出年龄", "测试字母输入年龄时会发生什么并记录"]],
      ["条件判断", "让程序根据不同输入作决定。", ["学习 if / elif / else、比较运算", "写一个学习时长建议器", "至少测试 0、30、90、非法输入四种情况"]],
      ["字符串处理", "能清洗用户输入，这是 Agent 的日常。", ["练习 strip、lower、split、replace", "把一段杂乱输入清洗成关键词列表", "打印清洗前后结果并解释每一步"]],
      ["本周小项目：意图分类器", "用规则判断用户想“学习、查询还是闲聊”。", ["定义 3 类关键词", "输入一句话并输出意图类别", "准备 6 条测试句并记录误判"]],
      ["复盘与重构", "不看答案重写本周项目。", ["从空文件重写意图分类器", "为变量改成有意义的英文名", "写本周复盘：3 个会了、2 个易错、1 个问题"]]
    ]
  },
  {
    title: "迁移到 Python 数据模型", subtitle: "利用 C/Java 基础，重点掌握 Python 容器、迭代与动态类型",
    days: [
      ["列表：保存多条消息", "能增删改查对话消息。", ["学习 list、索引、切片、append、remove", "创建 messages 列表并加入 5 条消息", "打印第一条、最后两条和消息数量"]],
      ["Python 式循环", "用迭代而不是下标思维处理消息流。", ["练习 for、range、enumerate、zip 与 break", "逐条为消息添加编号并打印", "对比 Python for 与 C/Java for"]],
      ["字典：结构化信息", "用字典表示一条 Agent 消息。", ["学习 dict 的增删改查与 get()", "创建含 role/content 的消息字典", "读取不存在的 key，对比 [] 与 get()"]],
      ["嵌套数据", "读写对话历史这种真实结构。", ["创建“列表里放字典”的 4 轮对话", "只打印所有 user 消息", "统计 user 与 assistant 各有几条"]],
      ["推导式、集合与元组", "写出紧凑但仍可读的数据转换。", ["练习列表/字典推导式与 set 去重", "把消息过滤和转换各写两种版本", "用元组保存不可修改的工具配置"]],
      ["本周小项目：对话记录器", "可添加、查看、搜索命令行对话。", ["设计 messages 数据结构", "支持 add/list/search 三条命令", "录入 5 条消息并验证搜索结果"]],
      ["调试实验室 I", "学会读 traceback，而不是害怕红字。", ["制造 IndexError、KeyError、TypeError", "从 traceback 最后一行向上定位", "建立 debug_log.md：错误/原因/修复"]]
    ]
  },
  {
    title: "补齐 Python 工程前置", subtitle: "函数、文件、异常、类、测试与环境：三周后直接进入 Hello-Agents",
    days: [
      ["Python 函数速迁移", "掌握 Python 参数模型与返回值。", ["练习默认/关键字参数、*args、**kwargs", "把意图分类拆成 3 个小函数", "避免用全局变量传递状态"]],
      ["模块、文件与 JSON", "能跨文件复用并持久化结构化数据。", ["建立 utils.py 与 main.py，解释 __name__", "用 with open 和 UTF-8 读写文件", "用 json.dump/load 保存 messages"]],
      ["异常与边界", "让非法输入和外部失败可控。", ["练习 try/except/else/finally", "捕获数字转换、文件不存在与坏 JSON", "为错误提供可行动提示"]],
      ["类、dataclass 与类型提示", "读懂 Agent 库常见的对象设计。", ["对照 Java class 学习 __init__ 与 self", "用 @dataclass 实现 Message", "为已有函数补参数和返回类型"]],
      ["pytest 与调试器", "让正确性可重复验证。", ["给 clean_text 和 Message 写 6 个测试", "故意制造失败并读 traceback", "用断点定位一个人为 bug"]],
      ["环境、依赖与 HTTP", "具备调用 LLM API 的工程前置。", ["创建 .venv 与 requirements.txt", "认识 GET/POST、状态码、timeout 与 JSON", "用 .env 保存测试配置并确认未被 Git 跟踪"]],
      ["阶段项目：可靠聊天日志", "交付一个有测试、有异常处理的小包。", ["实现可重启的 JSON 对话记录器", "测试保存、加载、搜索和坏文件", "整理 src/tests 并补 README"]]
    ]
  },
  {
    title: "进入 Hello-Agents", subtitle: "第一至三章：先建立 Agent 与大语言模型的正确心智模型",
    days: [
      ["第一章：智能体是什么", "能用“感知—决策—行动”解释 Agent。", ["阅读 1.1 与 1.2，整理 Agent 四要素", "用 PEAS 描述一个学习助手", "对比普通聊天机器人与 Agent"]],
      ["第一章：Agent 架构", "理解规划、记忆、工具和行动如何协作。", ["画出 LLM Agent 基本结构", "为学习助手列出 2 个工具与 1 种记忆", "完成章末习题并记录疑问"]],
      ["第二章：发展脉络", "知道 ReAct、工具调用与多智能体从何而来。", ["阅读第二章并制作时间线", "为 3 个关键节点各写一句意义", "不查资料复述发展主线"]],
      ["第三章：LLM 基础", "理解 Transformer、Token、上下文与生成。", ["阅读 3.1—3.3", "用自己的话解释 Token 与上下文窗口", "记录温度、最大输出等常用参数"]],
      ["第三章：提示与能力边界", "会写有目标、约束和格式的提示词。", ["拆分 system/user 消息职责", "写一个结构化学习助手提示词", "列出幻觉、时效性、上下文限制"]],
      ["最小 LLM 调用", "安全完成一次模型请求。", ["创建 .venv，安装 openai 与 python-dotenv", "用 .env 保存模型配置并加入 .gitignore", "调用兼容 OpenAI 的 API；无 Key 时用固定 mock"]],
      ["第一部分复盘", "把前三章压缩成一张可讲清楚的图。", ["画“用户→Agent→工具→环境”流程图", "整理 10 个核心术语", "写 300 字复盘并完成章末题"]]
    ]
  },
  {
    title: "手搓经典 Agent 范式", subtitle: "第四章：从零实现 ReAct、Plan-and-Solve 与 Reflection",
    days: [
      ["第四章环境与 LLM 封装", "读懂并运行 HelloAgentsLLM。", ["安装章节依赖并配置 .env", "逐行阅读 LLM 客户端类", "为缺配置和 API 异常加清晰提示"]],
      ["ReAct 原理", "理解 Thought—Action—Observation 循环。", ["阅读 4.2 并画循环图", "定义 calculator 与 search mock 工具", "手写一条完整 ReAct 轨迹"]],
      ["实现 ReAct", "让 Agent 能选择并调用工具。", ["实现提示、输出解析与工具注册表", "加入 max_steps 防止死循环", "运行 3 个成功案例"]],
      ["调试 ReAct", "能定位解析、工具与循环错误。", ["测试格式错误、未知工具、工具异常", "记录 action/observation 日志", "修复至少 2 个失败案例"]],
      ["Plan-and-Solve", "理解先规划后执行的取舍。", ["阅读 4.3 并实现规划器", "逐步执行计划并保留结果", "与 ReAct 比较步骤数和失败方式"]],
      ["Reflection", "让模型对初稿进行批评与改写。", ["阅读 4.4 并实现生成—反思—优化", "设置最大反思次数", "保存初稿、反馈与终稿"]],
      ["三范式评测", "用证据比较范式，而不是凭感觉。", ["准备 6 条固定任务", "记录成功率、步数、耗时与错误", "写一页选型结论"]]
    ]
  },
  {
    title: "先会用轮子", subtitle: "第五至六章：体验低代码平台与主流代码框架，理解抽象的代价",
    days: [
      ["第五章：低代码全景", "知道 Coze、Dify、n8n 各自适合什么。", ["阅读第五章三种平台定位", "按控制力、部署、扩展性做对比表", "选择一个平台作为体验对象"]],
      ["低代码实践", "搭出一个带工具的可运行工作流。", ["创建最小对话 Agent", "加入一个知识或 HTTP 工具", "保存流程截图与一次运行记录"]],
      ["低代码复盘", "能说清低代码的便利和边界。", ["测试正常、缺参数、工具失败", "记录可观测性与调试体验", "写“何时不用低代码”"]],
      ["第六章：框架地图", "理解 AutoGen、AgentScope、LangGraph 的差异。", ["阅读第六章总览", "整理核心抽象与适用场景", "选 LangGraph 作为重点实践"]],
      ["LangGraph 状态与节点", "用图表达有状态工作流。", ["定义 State、node 与 edge", "实现两节点最小图", "打印每一步状态变化"]],
      ["LangGraph 工具循环", "实现带条件分支的工具调用。", ["加入工具节点与条件边", "设置递归/步数上限", "测试成功与工具失败路径"]],
      ["框架对照实验", "理解框架帮你做了什么。", ["用同一任务比较手写 ReAct 与 LangGraph", "记录代码量、透明度、恢复能力", "写框架选型结论"]]
    ]
  },
  {
    title: "造自己的轮子", subtitle: "第七章：按分层架构实现 HelloAgents 的核心骨架",
    days: [
      ["架构蓝图", "理解 core、agents、tools 三层职责。", ["阅读 7.1 并画包结构", "写每个模块的单一职责", "创建项目与 tests 目录"]],
      ["消息与配置系统", "建立稳定的模型输入和配置边界。", ["实现 Message 数据结构", "实现环境变量配置与校验", "测试缺字段和非法 role"]],
      ["LLM 统一接口", "把模型供应商细节隔离在一处。", ["实现同步 invoke 接口", "加入超时与统一异常", "用 FakeLLM 完成无费用测试"]],
      ["工具抽象与注册", "让普通函数可发现、可校验、可执行。", ["实现 BaseTool 与参数 schema", "实现 ToolRegistry", "加入 calculator 并写测试"]],
      ["Agent 基类与 SimpleAgent", "跑通最小消息—模型—回复链路。", ["定义 Agent 基类契约", "实现 SimpleAgent", "用 FakeLLM 验证消息传递"]],
      ["三种 Agent 实现", "把第四章范式纳入统一框架。", ["实现 ReActAgent", "接入 PlanAndSolve 与 Reflection", "复用统一工具和异常体系"]],
      ["框架验收", "得到可安装、可测试、可解释的小框架。", ["运行全部单元测试", "补 README 与最小示例", "对照官方第七章列出差异"]]
    ]
  },
  {
    title: "记忆、检索与上下文", subtitle: "第八至九章：让 Agent 记得住、找得到、喂得准",
    days: [
      ["第八章：记忆系统", "区分短期、长期与语义记忆。", ["阅读记忆章节并画数据流", "实现窗口消息记忆", "验证裁剪后仍保留关键上下文"]],
      ["Embedding 与向量检索", "理解语义检索的最小闭环。", ["把 5 段文本转成向量或用 mock", "计算相似度并返回 Top-K", "用 3 个查询检查召回结果"]],
      ["RAG 最小实现", "完成检索—组装—生成链路。", ["准备一个小型本地知识库", "实现 chunk、retrieve、prompt 组装", "保存带引用的回答"]],
      ["RAG 调试", "识别分块、召回和生成三类问题。", ["设计 6 条含答案的问题", "记录召回命中与最终正确性", "调整 chunk/Top-K 并比较"]],
      ["第九章：上下文工程", "把上下文当作有限资源管理。", ["阅读上下文工程章节", "区分系统指令、历史、工具结果、检索内容", "制定上下文优先级规则"]],
      ["上下文压缩与隔离", "降低噪声、泄漏与超窗风险。", ["实现历史摘要或截断策略", "隔离不可信工具内容", "测试长对话与提示注入样例"]],
      ["记忆 + RAG 集成", "让框架同时使用对话状态和外部知识。", ["将 Memory/RAG 注册为工具", "完成一次多轮知识问答", "记录失败案例与限制"]]
    ]
  },
  {
    title: "协议、训练与评估", subtitle: "第十至十二章：重点掌握 MCP 与评估，Agentic RL 先建立地图",
    days: [
      ["第十章：MCP 原理", "理解 Host、Client、Server 与能力发现。", ["阅读 MCP 部分并画交互图", "区分 tools/resources/prompts", "解释 MCP 与普通函数调用的差别"]],
      ["MCP 实践", "连接或实现一个最小 MCP Server。", ["选择文件或天气工具", "完成能力发现与一次调用", "记录权限、超时和错误边界"]],
      ["A2A 与 ANP", "知道智能体间协议解决什么问题。", ["阅读 A2A/ANP 小节", "比较 MCP、A2A、ANP 的通信对象", "为多 Agent 场景选择协议"]],
      ["第十一章：Agentic RL 地图", "理解 SFT、奖励与 GRPO 的位置。", ["阅读概念与数据流程", "整理训练样本、奖励、更新三阶段", "标记数学或算力门槛，暂不盲目训练"]],
      ["第十二章：评估设计", "把“效果好”变成可检查指标。", ["定义任务成功、正确性、成本、延迟", "建立 10 条 eval_cases.json", "覆盖正常、模糊、越界和工具故障"]],
      ["评估运行器", "一条命令产出可复现报告。", ["实现批量运行与断言", "输出通过率、失败清单、耗时", "保存 eval_report.json"]],
      ["故障注入与复盘", "证明系统失败时可解释、可恢复。", ["模拟超时、坏 JSON、工具异常", "检查日志与降级行为", "写现象→根因→修复报告"]]
    ]
  },
  {
    title: "拆解综合案例", subtitle: "第十三至十五章：选一个主做，其余案例重在读架构与取舍",
    days: [
      ["第十三章：旅行助手架构", "理解 MCP 与多智能体如何协作。", ["阅读需求、角色与数据流", "画 Planner/Executor/工具关系", "列出外部依赖与失败点"]],
      ["旅行助手最小切片", "跑通一个可验证的端到端场景。", ["只保留一个目的地和两个工具", "完成规划—查询—汇总", "保存运行轨迹"]],
      ["第十四章：DeepResearch", "理解搜索、筛选、综合与引用链路。", ["阅读整体架构", "拆出 query planning 与 source synthesis", "检查引用是否支持结论"]],
      ["研究 Agent 最小切片", "完成一轮带来源的短研究。", ["限定 3 个来源和 1 个问题", "生成带引用的结构化报告", "记录遗漏与冲突信息"]],
      ["第十五章：赛博小镇", "理解角色状态、事件与多 Agent 调度。", ["阅读核心数据结构", "画一轮世界更新时序", "比较它与单 Agent 循环"]],
      ["确定毕业项目", "从三个案例中选择一个可交付切片。", ["写 3 条必须有和 3 条明确不做", "定义 10 条验收案例", "确定数据、工具与风险"]],
      ["项目设计评审", "在编码前暴露架构问题。", ["画组件图与状态流", "定义模块接口和目录", "检查密钥、权限、成本与降级"]]
    ]
  },
  {
    title: "毕业设计与发布", subtitle: "第十六章：交付一个可运行、可评估、可解释的 Agent",
    days: [
      ["项目脚手架", "建立清晰目录、配置与运行入口。", ["创建 src/tests/data/docs", "准备配置、日志、模型与工具模块", "写最小 README 和启动命令"]],
      ["核心成功路径", "让最短端到端流程完整跑通。", ["实现状态、模型接口与工具注册", "跑通一个真实请求", "保存可工作的基线版本"]],
      ["记忆与工具", "支持至少两个工具和多轮上下文。", ["实现并测试两个工具", "接入窗口记忆或 RAG", "验证第二轮能引用前文"]],
      ["错误恢复与可观测性", "失败时用户有提示、后台有证据。", ["加入超时、重试上限与降级", "接入结构化日志", "用三种故障验证恢复"]],
      ["完整评估与修复", "用固定案例验证质量。", ["运行 10 条评测", "修复影响最大的两类失败", "保存前后两版报告"]],
      ["文档与演示", "让陌生人能够安装、运行和理解。", ["补全安装、配置、示例与限制", "保存一次完整演示", "检查仓库中没有密钥和隐私数据"]],
      ["77 天毕业复盘", "总结能力边界并确定下一阶段。", ["对照第十六章完成验收", "写会了什么、仍不会什么、证据在哪", "制定下一阶段 30 天目标"]]
    ]
  }
];

const STORAGE_KEY = "agent-roadmap-v3";
function localDateOffset(daysAgo = 0) {
  const date = new Date();
  date.setDate(date.getDate() - daysAgo);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}
const defaultState = {
  startDate: localDateOffset(3),
  completed: { 0: true, 1: true, 2: true },
  tasks: { "0-0": true, "0-1": true, "0-2": true, "1-0": true, "1-1": true, "1-2": true, "2-0": true, "2-1": true, "2-2": true },
  reflections: {}
};
let state = loadState();
let activeDay = null;
let activeFilter = "all";

const allDays = weeks.flatMap((week, weekIndex) =>
  week.days.map((day, dayIndex) => ({ week, weekIndex, dayIndex, globalIndex: weekIndex * 7 + dayIndex, data: day }))
);
const totalDays = allDays.length;

function loadState() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || localStorage.getItem("agent-roadmap-v2") || localStorage.getItem("agent-roadmap-v1") || "null");
    if (!saved) return { ...defaultState };
    return {
      ...defaultState,
      ...saved,
      completed: { ...saved.completed, ...defaultState.completed },
      tasks: { ...saved.tasks, ...defaultState.tasks },
      reflections: { ...defaultState.reflections, ...saved.reflections }
    };
  }
  catch { return { ...defaultState }; }
}
function saveState() { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); updateDashboard(); }
function dateFor(index) {
  const date = new Date(`${state.startDate}T12:00:00`);
  date.setDate(date.getDate() + index);
  return date;
}
function currentIndex() {
  const start = new Date(`${state.startDate}T00:00:00`);
  const today = new Date(); today.setHours(0, 0, 0, 0);
  return Math.max(0, Math.min(totalDays - 1, Math.floor((today - start) / 86400000)));
}
function formatDate(date) { return `${date.getMonth() + 1}月${date.getDate()}日`; }

function render() {
  const roadmap = document.querySelector("#roadmap");
  const currentWeek = Math.floor(currentIndex() / 7);
  let shown = 0;
  roadmap.innerHTML = weeks.map((week, weekIndex) => {
    const cards = week.days.map((day, dayIndex) => {
      const index = weekIndex * 7 + dayIndex;
      const complete = Boolean(state.completed[index]);
      const visible = activeFilter === "all" || (activeFilter === "current" && weekIndex === currentWeek) || (activeFilter === "pending" && !complete);
      if (!visible) return "";
      shown++;
      return `<article class="day-card ${complete ? "complete" : ""} ${index === currentIndex() ? "is-today" : ""}" data-day="${index}">
        <div class="day-index">DAY ${String(index + 1).padStart(2, "0")}<span class="day-date">${formatDate(dateFor(index))}</span></div>
        <div class="day-main"><h3>${day[0]}</h3><p>${day[1]}</p></div>
        <button class="check" data-check="${index}" aria-label="${complete ? "取消完成" : "标记完成"}">${complete ? "✓" : ""}</button>
      </article>`;
    }).join("");
    if (!cards) return "";
    return `<section class="week" data-week="${weekIndex}">
      <header class="week-header"><span class="week-number">WEEK ${String(weekIndex + 1).padStart(2, "0")}</span><h2>${week.title}</h2><p>${week.subtitle}</p></header>
      <div class="day-list">${cards}</div>
    </section>`;
  }).join("");
  if (!shown) roadmap.innerHTML = `<div class="empty">好家伙，全部完成了。去终点线签收你的 Agent 吧。</div>`;
}

function updateDashboard() {
  const completed = Object.values(state.completed).filter(Boolean).length;
  const tasks = Object.values(state.tasks).filter(Boolean).length;
  const percent = Math.round(completed / totalDays * 100);
  document.querySelector("#progressPercent").textContent = `${percent}%`;
  document.querySelector("#progressText").textContent = `${completed} / ${totalDays} 天完成`;
  document.querySelector("#progressBar").style.width = `${percent}%`;
  document.querySelector("#taskCount").textContent = tasks;
  document.querySelector("#minutesCount").textContent = completed * 90;
  let streak = 0;
  for (let i = currentIndex(); i >= 0 && state.completed[i]; i--) streak++;
  document.querySelector("#streakCount").textContent = streak;
  const today = allDays[currentIndex()];
  document.querySelector("#todayTitle").textContent = `Day ${today.globalIndex + 1} · ${today.data[0]}`;
  document.querySelector("#todayOutcome").textContent = today.data[1];
}

function openDay(index) {
  activeDay = Number(index);
  const item = allDays[activeDay];
  document.querySelector("#dialogWeek").textContent = `WEEK ${item.weekIndex + 1} / DAY ${activeDay + 1}`;
  document.querySelector("#dialogTitle").textContent = item.data[0];
  document.querySelector("#dialogGoal").textContent = `今日验收：${item.data[1]}`;
  document.querySelector("#dialogTasks").innerHTML = item.data[2].map((task, i) => {
    const key = `${activeDay}-${i}`;
    return `<label class="task-row"><input type="checkbox" data-task="${key}" ${state.tasks[key] ? "checked" : ""}><div>${task}<span>约 ${i === 0 ? 25 : i === 1 ? 45 : 20} 分钟</span></div></label>`;
  }).join("");
  document.querySelector("#reflection").value = state.reflections[activeDay] || "";
  document.querySelector("#dayDialog").showModal();
}

document.querySelector("#roadmap").addEventListener("click", event => {
  const check = event.target.closest("[data-check]");
  if (check) {
    event.stopPropagation();
    const index = check.dataset.check;
    state.completed[index] = !state.completed[index];
    saveState(); render(); return;
  }
  const card = event.target.closest("[data-day]");
  if (card) openDay(card.dataset.day);
});
document.querySelector("#dialogTasks").addEventListener("change", event => {
  if (event.target.dataset.task) { state.tasks[event.target.dataset.task] = event.target.checked; saveState(); }
});
document.querySelector(".dialog-close").addEventListener("click", () => document.querySelector("#dayDialog").close());
document.querySelector("#saveReflection").addEventListener("click", () => {
  state.reflections[activeDay] = document.querySelector("#reflection").value;
  saveState(); document.querySelector("#dayDialog").close();
});
document.querySelector("#startDate").value = state.startDate;
document.querySelector("#startDate").addEventListener("change", event => { state.startDate = event.target.value; saveState(); render(); });
document.querySelectorAll(".filter").forEach(button => button.addEventListener("click", () => {
  document.querySelectorAll(".filter").forEach(item => item.classList.remove("active"));
  button.classList.add("active"); activeFilter = button.dataset.filter; render();
}));
document.querySelector("#todayButton").addEventListener("click", () => {
  activeFilter = "all"; document.querySelectorAll(".filter").forEach((item, i) => item.classList.toggle("active", i === 0)); render();
  setTimeout(() => document.querySelector(`[data-day="${currentIndex()}"]`)?.scrollIntoView({ behavior: "smooth", block: "center" }), 0);
});
document.querySelector("#exportBtn").addEventListener("click", () => {
  const blob = new Blob([JSON.stringify(state, null, 2)], { type: "application/json" });
  const link = Object.assign(document.createElement("a"), { href: URL.createObjectURL(blob), download: "agent-roadmap-progress.json" });
  link.click(); URL.revokeObjectURL(link.href);
});
document.querySelector("#importBtn").addEventListener("click", () => document.querySelector("#importInput").click());
document.querySelector("#importInput").addEventListener("change", async event => {
  try { state = { ...defaultState, ...JSON.parse(await event.target.files[0].text()) }; saveState(); render(); document.querySelector("#startDate").value = state.startDate; }
  catch { alert("进度文件无法读取，请确认它是从本页面导出的 JSON。"); }
});
document.querySelector("#resetBtn").addEventListener("click", () => {
  if (confirm("确定清空所有打卡、任务和复盘吗？此操作无法撤销。")) { state = { ...defaultState, completed: {}, tasks: {}, reflections: {} }; saveState(); render(); }
});

render();
updateDashboard();
