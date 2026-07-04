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
    title: "掌握数据容器", subtitle: "列表、字典、集合：Agent 保存状态与工具结果的基础",
    days: [
      ["列表：保存多条消息", "能增删改查对话消息。", ["学习 list、索引、切片、append、remove", "创建 messages 列表并加入 5 条消息", "打印第一条、最后两条和消息数量"]],
      ["循环：批量处理", "用 for/while 处理消息流。", ["学习 for、range、while、break", "逐条为消息添加编号并打印", "找出第一条含“错误”的消息后停止"]],
      ["字典：结构化信息", "用字典表示一条 Agent 消息。", ["学习 dict 的增删改查与 get()", "创建含 role/content 的消息字典", "读取不存在的 key，对比 [] 与 get()"]],
      ["嵌套数据", "读写对话历史这种真实结构。", ["创建“列表里放字典”的 4 轮对话", "只打印所有 user 消息", "统计 user 与 assistant 各有几条"]],
      ["集合与元组", "会在合适场景去重和保护数据。", ["学习 set 去重、tuple 不可变性", "对关键词列表去重", "用元组保存不可修改的工具配置"]],
      ["本周小项目：对话记录器", "可添加、查看、搜索命令行对话。", ["设计 messages 数据结构", "支持 add/list/search 三条命令", "录入 5 条消息并验证搜索结果"]],
      ["调试实验室 I", "学会读 traceback，而不是害怕红字。", ["制造 IndexError、KeyError、TypeError", "从 traceback 最后一行向上定位", "建立 debug_log.md：错误/原因/修复"]]
    ]
  },
  {
    title: "把代码组织起来", subtitle: "函数、模块、文件，让程序从练习题变成小系统",
    days: [
      ["函数基础", "把重复逻辑包装成可复用函数。", ["学习 def、参数、return", "把文本清洗逻辑改成 clean_text()", "用 4 组输入验证返回值"]],
      ["参数与作用域", "理解数据怎样进入和离开函数。", ["练习默认参数、关键字参数", "比较局部变量与全局变量", "写 format_message(role, content)"]],
      ["拆分与组合函数", "用多个小函数完成一个任务。", ["把意图分类拆为清洗/匹配/输出", "每个函数只负责一件事", "画出数据在三个函数间的流向"]],
      ["模块与导入", "能跨文件复用自己的代码。", ["建立 utils.py 与 main.py", "从 utils 导入文本清洗函数", "尝试直接运行两文件并解释 __name__"]],
      ["文件读写", "让程序重启后仍保留数据。", ["学习 with open 与 UTF-8", "把对话写入 text 文件", "重新读取并逐行打印"]],
      ["JSON：Agent 的通用语言", "保存和读取结构化对话。", ["学习 json.dump/load", "将 messages 写入 history.json", "读取后验证类型和原数据一致"]],
      ["本周小项目：持久化聊天日志", "完成可重启的对话记录器。", ["启动时加载 JSON，不存在则创建", "每次新增消息后自动保存", "把使用方法写入 README"]]
    ]
  },
  {
    title: "获得可靠性", subtitle: "异常、测试、面向对象与调试器，让代码可以放心修改",
    days: [
      ["异常处理", "优雅处理用户和文件错误。", ["学习 try/except/else/finally", "捕获非法数字输入与文件不存在", "错误时给出用户能行动的提示"]],
      ["断言与边界", "主动定义“什么才算正确”。", ["学习 assert 与前置条件", "为消息 role/content 加检查", "测试空字符串、None、超长文本"]],
      ["单元测试入门", "让函数的正确性可重复验证。", ["学习 pytest 的 test_ 命名和 assert", "给 clean_text 写 5 个测试", "运行测试并故意制造一次失败"]],
      ["调试器与断点", "能暂停程序观察真实状态。", ["在编辑器设置 breakpoint", "单步进入函数并观察变量", "用断点定位一个人为植入的 bug"]],
      ["类与对象", "理解库中常见的对象写法。", ["学习 class、__init__、self", "创建 Message 类", "实例化 user/assistant 两条消息"]],
      ["数据类与类型提示", "让数据结构更清晰、更易检查。", ["学习 @dataclass 与基础类型提示", "把 Message 改成 dataclass", "给三个已有函数补参数和返回类型"]],
      ["阶段项目：测试过的日志器", "交付一个有测试、有错误处理的小包。", ["整理 src/tests 目录", "测试保存、加载、搜索三类行为", "运行全部测试并保存通过截图或日志"]]
    ]
  },
  {
    title: "连接真实世界", subtitle: "环境变量、HTTP、API 与异步概念：Agent 的外部感官",
    days: [
      ["虚拟环境与依赖", "为项目创建隔离、可复现环境。", ["创建并激活 .venv", "用 pip 安装 requests 与 python-dotenv", "生成 requirements.txt"]],
      ["HTTP 与 API 概念", "读懂请求、响应、状态码和 JSON。", ["认识 GET/POST、header、body", "调用一个公开测试 API", "打印状态码与响应 JSON"]],
      ["请求参数与超时", "写出不会无限等待的网络代码。", ["传递 query params", "为请求设置 timeout", "分别处理 200、404 与连接失败"]],
      ["密钥与环境变量", "不把 API Key 写进代码或 Git。", ["创建 .env 与 .gitignore", "用 dotenv 读取测试密钥", "确认 git status 不显示 .env"]],
      ["调用大模型 API（可选）", "完成一次“输入 → 模型 → 输出”。", ["阅读所选模型官方 quickstart", "从环境变量读取 API Key", "发送最小请求并打印回复；无 Key 用 mock"]],
      ["结构化输出", "把模型文本约束成程序可用的数据。", ["设计 intent/reason/confidence JSON", "解析模型或 mock 的 JSON 输出", "处理缺字段和无效 JSON"]],
      ["本周小项目：API 意图分类器", "用模型分类，并在失败时降级到规则。", ["封装 classify_intent()", "API 失败时调用规则分类器", "准备 10 条输入对比两种结果"]]
    ]
  },
  {
    title: "理解 Agent 的骨架", subtitle: "提示、工具调用、循环、状态：不靠框架先看清本质",
    days: [
      ["提示词结构", "写出角色、目标、边界、输出格式。", ["拆解 system/user 消息职责", "为学习助手写系统提示词", "用 5 个刁钻输入检查边界"]],
      ["工具函数", "把普通函数设计成可被 Agent 使用的工具。", ["写 calculator(expression) 与 get_time()", "为工具补名称、描述、参数说明", "为每个工具写正常与异常测试"]],
      ["工具选择", "根据意图选择正确工具。", ["定义工具注册表 dictionary", "实现 select_tool(intent)", "测试未知工具并返回友好错误"]],
      ["Agent 循环", "实现观察—思考—行动—结果循环。", ["画出循环流程图", "用 while + 最大步数实现循环", "记录每一步 action 与 observation"]],
      ["状态与短期记忆", "在多轮交互中保留必要上下文。", ["设计 AgentState 数据结构", "保存最近 6 条消息", "超出窗口后裁剪并验证"]],
      ["停止条件与安全边界", "避免无限循环和危险输入。", ["加入 max_steps 与完成标记", "为 calculator 限制允许字符", "测试循环超限、工具报错、正常完成"]],
      ["本周小项目：无框架 Agent", "做一个能选用两个工具的命令行 Agent。", ["串联输入、选择、执行、观察、回答", "完整记录一次运行轨迹", "写清它为何不是普通聊天机器人"]]
    ]
  },
  {
    title: "像工程师一样调 Agent", subtitle: "日志、评测、Mock、故障注入，把玄学变成证据",
    days: [
      ["结构化日志", "每次运行都留下可搜索的轨迹。", ["用 logging 代替 print", "记录时间、step、tool、latency、error", "输出到 console 与 agent.log"]],
      ["评测集", "用固定问题衡量改动是否更好。", ["建立 eval_cases.json", "编写 10 条含输入与期望行为的案例", "覆盖正常、模糊、越界、工具失败"]],
      ["评测运行器", "一条命令跑完全部案例。", ["逐条运行并比较预期", "统计通过率和失败列表", "把结果保存为 eval_report.json"]],
      ["Mock 与可重复测试", "不花 API 费用也能稳定测试。", ["创建 FakeModel 固定返回值", "注入模型依赖而非写死", "用 mock 测工具调用与停止条件"]],
      ["故障注入", "证明系统出错时仍可解释、可恢复。", ["模拟超时、坏 JSON、工具异常", "为三类故障设计降级行为", "检查日志能否定位根因"]],
      ["提示词版本对比", "用数据而非感觉选择提示词。", ["保存 prompt_v1/v2", "在同一评测集运行两版", "比较通过率并记录取舍"]],
      ["调试报告", "完成一份真实工程复盘。", ["选择 3 个失败案例", "写现象→假设→实验→根因→修复", "列出尚未解决的限制"]]
    ]
  },
  {
    title: "交付你的第一个 Agent", subtitle: "从需求、实现到测试与说明，完成可展示的闭环",
    days: [
      ["确定题目与范围", "选一个两周内能讲清楚的小 Agent。", ["从学习助手/文件整理/信息查询中选题", "写 3 条必须有与 3 条明确不做", "定义用户成功的一次完整流程"]],
      ["项目脚手架", "建立清晰目录与运行入口。", ["创建 src/tests/data/docs", "准备配置、日志、模型与工具模块", "写最小 README 和启动命令"]],
      ["实现核心循环", "让最短成功路径完整跑通。", ["实现状态、模型接口、工具注册", "跑通一次用户请求", "提交或记录一个可工作的基线版本"]],
      ["加入工具与记忆", "支持至少两个工具和多轮上下文。", ["实现并测试两个真实工具", "加入窗口记忆", "验证第二轮能引用第一轮信息"]],
      ["错误恢复与可观测性", "失败时给提示，后台有证据。", ["加入超时、重试上限与降级", "接入结构化日志", "用三种故障验证恢复路径"]],
      ["完整评测与修复", "用 10 条案例达到至少 80% 通过率。", ["运行固定评测集", "修复影响最大的两类失败", "再次运行并保存前后报告"]],
      ["发布与毕业复盘", "让陌生人能运行，并知道下一步学什么。", ["补全安装、配置、示例与限制", "录制或保存一次完整演示", "写 56 天复盘与下一阶段 30 天目标"]]
    ]
  }
];

const STORAGE_KEY = "agent-roadmap-v1";
const defaultState = { startDate: new Date().toISOString().slice(0, 10), completed: {}, tasks: {}, reflections: {} };
let state = loadState();
let activeDay = null;
let activeFilter = "all";

const allDays = weeks.flatMap((week, weekIndex) =>
  week.days.map((day, dayIndex) => ({ week, weekIndex, dayIndex, globalIndex: weekIndex * 7 + dayIndex, data: day }))
);

function loadState() {
  try { return { ...defaultState, ...JSON.parse(localStorage.getItem(STORAGE_KEY)) }; }
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
  return Math.max(0, Math.min(55, Math.floor((today - start) / 86400000)));
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
  const percent = Math.round(completed / 56 * 100);
  document.querySelector("#progressPercent").textContent = `${percent}%`;
  document.querySelector("#progressText").textContent = `${completed} / 56 天完成`;
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
