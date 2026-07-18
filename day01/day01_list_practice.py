# ============================================================
# 第 1 部分：创建列表（对标 Java 的 ArrayList<String>）
# Java: ArrayList<String> names = new ArrayList<>();
# Python: 直接用方括号，不用 new，不用写类型
# ============================================================
print("=" * 50)
print("第1部分：创建列表")
print("=" * 50)

# 场景：存放 RAG 系统里待处理的文档文件名
file_names = ["readme.txt", "api_doc.pdf", "data.json"]
print(f"原始列表：{file_names}")

# 空列表怎么创建？两种方式，推荐第一种
empty_list = []
# empty_list = list()  # 这是另一种写法，但很少用
print(f"空列表：{empty_list}")

# ----------------------------- 分割线 -----------------------------

# ============================================================
# 第 2 部分：增删改查（基础 CRUD）
# Java: add(), get(), set(), remove()
# ============================================================
print("\n" + "=" * 50)
print("第2部分：增删改查")
print("=" * 50)

# 2.1 追加（Java 的 add 尾部追加）
file_names.append("user_guide.docx")
print(f"尾部追加后：{file_names}")

# 2.2 插入到指定位置（Java 的 add(index, element)）
# RAG 场景：想把最重要的配置文件插到最前面，索引 0 是第一个位置
file_names.insert(0, "config.ini")
print(f"插入到最前面后：{file_names}")

# 2.3 根据索引取值（Java 的 get(index)）
first_file = file_names[0]
print(f"取第 1 个元素：{first_file}")

# 2.4 根据索引修改（Java 的 set(index, element)）
# 把第 2 个文件改名
file_names[1] = "new_readme.txt"
print(f"修改第 2 个元素后：{file_names}")

# 2.5 根据索引删除（Java 的 remove(index)）
# 删除最后一个元素（索引 -1 代表最后一个，这个后面会讲）
removed_item = file_names.pop()  # pop() 不传参数默认删除最后一个
print(f"删除了最后一个元素：{removed_item}")
print(f"删除后剩余列表：{file_names}")

# 2.6 根据值删除（Java 的 remove(Object o)）
# 注意：remove 会删除第一个匹配到的值
file_names.append("temp.log")
file_names.append("temp.log")  # 故意加两个重复的
print(f"加入两个重复日志后：{file_names}")
file_names.remove("temp.log")  # 只删除第一个
print(f"删除一次 'temp.log' 后：{file_names}")

# ----------------------------- 分割线 -----------------------------

# ============================================================
# 第 3 部分：切片（Slicing）—— Python 的王牌功能
# Java 里写 subList(1, 4) 很啰嗦，Python 用 [开始:结束] 一步到位
# 记住一个原则：左闭右开（包含开始，不包含结束）
# ============================================================
print("\n" + "=" * 50)
print("第3部分：切片（截取子列表）")
print("=" * 50)

chunks = ["第1段", "第2段", "第3段", "第4段", "第5段"]
print(f"完整列表：{chunks}")

# 3.1 取前 3 个（索引 0, 1, 2）
# 写法：[开始:结束]  ->  [:3] 等价于 [0:3]
top_3 = chunks[:3]
print(f"取前 3 个：{top_3}")

# 3.2 取从索引 2 到末尾（索引 2, 3, 4）
# 写法：[2:] 表示从索引 2 一直取到最后
from_2_to_end = chunks[2:]
print(f"从第 3 个取到最后：{from_2_to_end}")

# 3.3 取倒数 2 个（负索引代表从末尾数）
# -1 是最后一个，-2 是倒数第二个
last_2 = chunks[-2:]
print(f"取倒数 2 个：{last_2}")

# 3.4 取中间 3 个（索引 1, 2, 3）
middle_3 = chunks[1:4]  # 注意：结束索引是 4，但取到的是 3，因为左闭右开
print(f"取中间 3 个（索引1到3）：{middle_3}")

# 3.5 带步长的切片（每隔几个取一个）
# 语法：[开始:结束:步长]，步长为 2 表示隔一个取一个
every_other = chunks[::2]  # 取索引 0, 2, 4
print(f"隔一个取一个：{every_other}")

# 【RAG 实战映射】
# 假设 AI 返回了 10 个相关文档块，但你的大模型最多只能塞进 3 个
# 你就用切片 [:3] 取前 3 个最相关的，剩下的丢弃，防止 Token 超限
print("\n>>> RAG 实战：截取前 3 个文档块喂给 AI")
retrieved = ["doc1", "doc2", "doc3", "doc4", "doc5"]
final_context = retrieved[:3]
print(f"原始检索到 5 个，只取前 3 个：{final_context}")

# ----------------------------- 分割线 -----------------------------

# ============================================================
# 第 4 部分：列表推导式（List Comprehension）—— 一行代替 for 循环
# Java 里你要写 for 循环 + if 判断，需要 5 行
# Python 一行搞定，而且速度更快（底层是 C 语言循环）
# ============================================================
print("\n" + "=" * 50)
print("第4部分：列表推导式（过滤 + 转换）")
print("=" * 50)

docs = ["hello.txt", "world.pdf", "readme.md", "data.txt", "image.png"]

# 4.1 过滤：只保留 .txt 结尾的文件
# 传统 for 循环写法（你肯定看得懂）：
txt_files_old = []
for file in docs:
    if file.endswith(".txt"):
        txt_files_old.append(file)
print(f"传统 for 循环过滤出 .txt：{txt_files_old}")

# 列表推导式写法（以后就用这个）：
# 结构：[ (你要放进去的内容) for (临时变量) in (原列表) if (条件) ]
txt_files_new = [file for file in docs if file.endswith(".txt")]
print(f"列表推导式过滤出 .txt：{txt_files_new}")

# 4.2 转换：把所有文件名转成大写
# 结构：没有 if 就是纯转换
upper_files = [file.upper() for file in docs]
print(f"转成大写：{upper_files}")

# 4.3 过滤 + 转换 一起做：把 .txt 文件名提取出来，并去掉后缀 .txt
# 比如 "hello.txt" -> "hello"
clean_names = [file.replace(".txt", "") for file in docs if file.endswith(".txt")]
print(f"过滤 .txt 并去掉后缀：{clean_names}")

# 【RAG 实战映射】
# 你的知识库里存的是字典列表：[{"title": "A", "content": "xxx"}, ...]
# 你想快速提取所有的 content 组成新列表，一行搞定
print("\n>>> RAG 实战：提取所有文档的内容字段")
doc_list = [
    {"title": "文档1", "content": "这是内容1"},
    {"title": "文档2", "content": "这是内容2"},
]
contents = [doc["content"] for doc in doc_list]
print(f"提取出的内容列表：{contents}")

# ----------------------------- 分割线 -----------------------------

# ============================================================
# 第 5 部分：合并列表（Java 的 addAll）
# Python 有两种方式：extend（改原列表）和 +（生成新列表）
# ============================================================
print("\n" + "=" * 50)
print("第5部分：合并列表")
print("=" * 50)

local_docs = ["本地文件1", "本地文件2"]
web_docs = ["网页文件1", "网页文件2"]

# 5.1 使用 extend（把 web_docs 的元素加到 local_docs 里）
# 注意：extend 会改变 local_docs 本身，不产生新列表
local_docs.extend(web_docs)
print(f"使用 extend 合并后（原列表被修改）：{local_docs}")

# 5.2 使用 + 号（生成全新的列表，原列表不变）
list_a = [1, 2]
list_b = [3, 4]
list_c = list_a + list_b
print(f"list_a 不变：{list_a}")
print(f"list_b 不变：{list_b}")
print(f"合并生成的新列表 list_c：{list_c}")

# 【RAG 实战映射】
# 你的数据可能来自多个源：本地硬盘、网络爬虫、数据库
# 最后全部 merge 到一个大列表里统一处理
print("\n>>> RAG 实战：多数据源合并")
source1 = ["本地PDF1", "本地PDF2"]
source2 = ["网页抓取1"]
source3 = ["数据库记录1"]
all_sources = source1 + source2 + source3
print(f"合并三个数据源：{all_sources}")

# ----------------------------- 分割线 -----------------------------

# ============================================================
# 第 6 部分：查找与计数（Java 的 contains, indexOf, 遍历）
# ============================================================
print("\n" + "=" * 50)
print("第6部分：查找与计数")
print("=" * 50)

scores = [95, 80, 95, 70, 95, 60]

# 6.1 统计某个值出现了几次（Java 需要自己写循环数）
count_95 = scores.count(95)
print(f"95 分出现了 {count_95} 次")

# 6.2 查找某个值第一次出现的位置（Java 的 indexOf）
position_80 = scores.index(80)
print(f"80 分第一次出现在索引 {position_80}")

# 6.3 判断某个值存不存在（Java 的 contains）
# 方法1：直接用 in（推荐，最 Pythonic）
if 100 in scores:
    print("列表里有 100 分")
else:
    print("列表里没有 100 分")

# 方法2：用 index 配合 try，但新手不推荐，暂时不碰异常处理
# 就记住：想判断有没有，直接用 in

# 【RAG 实战映射】
# 检查检索结果里有没有重复的文档 ID，或者看看是否包含特定关键词
print("\n>>> RAG 实战：检查重复 ID")
doc_ids = [101, 102, 101, 103]
if doc_ids.count(101) > 1:
    print(f"警告：文档 ID 101 出现了 {doc_ids.count(101)} 次，存在重复！")
else:
    print("没有重复 ID")

# ----------------------------- 分割线 -----------------------------

# ============================================================
# 第 7 部分：排序与反转（Java 的 Collections.sort() 和 Collections.reverse()）
# ============================================================
print("\n" + "=" * 50)
print("第7部分：排序与反转")
print("=" * 50)

numbers = [3, 1, 4, 1, 5, 9, 2]

# 7.1 原地排序（改变原列表，相当于 Java 的 Collections.sort()）
numbers.sort()
print(f"升序排序后：{numbers}")

# 7.2 降序排序（加 reverse=True）
numbers.sort(reverse=True)
print(f"降序排序后：{numbers}")

# 7.3 不改变原列表的排序（生成新列表，相当于 Java 的 Stream.sorted()）
original = [5, 2, 8, 1]
sorted_new = sorted(original)  # 注意是 sorted() 函数，不是 .sort() 方法
print(f"原列表不变：{original}")
print(f"新排序列表：{sorted_new}")

# 7.4 反转列表（相当于 Java 的 Collections.reverse()）
original.reverse()
print(f"反转原列表：{original}")

# 【RAG 实战映射】
# AI 返回的结果通常有个相似度分数，按分数从高到低排序，取第一个
print("\n>>> RAG 实战：按相似度排序")
# 假设这是 (文档名, 相似度分数) 的列表
results = [("文档A", 0.95), ("文档B", 0.87), ("文档C", 0.99)]
# 按分数从高到低排（降序）
results.sort(key=lambda x: x[1], reverse=True)  # lambda 先不管，知道是取第2个元素排序就行
print(f"按相似度排序后：{results}")
best_doc = results[0]
print(f"最相关的文档是：{best_doc[0]}，分数：{best_doc[1]}")

# ----------------------------- 分割线 -----------------------------

# ============================================================
# 终极综合实战：模拟一个完整的 RAG 检索后处理流程
# 把今天学的所有东西串在一起
# ============================================================
print("\n" + "=" * 50)
print("【最终大实战】RAG 检索结果处理器")
print("=" * 50)

# 1. 模拟原始检索结果（AI 返回的 6 个文档块，附带分数）
raw_results = [
    {"id": "doc_1", "content": "Python 是解释型语言", "score": 0.92},
    {"id": "doc_2", "content": "Java 是编译型语言", "score": 0.45},
    {"id": "doc_3", "content": "RAG 可以减少幻觉", "score": 0.98},
    {"id": "doc_4", "content": "Python 适合 AI", "score": 0.88},
    {"id": "doc_5", "content": "RAG 需要向量数据库", "score": 0.76},
    {"id": "doc_6", "content": "暑假学习 RAG", "score": 0.50},
]

print("原始检索结果：")
for item in raw_results:
    print(f"  {item}")

# 2. 第一步：过滤掉分数低于 0.6 的（低质量结果不要了）
# 使用列表推导式 + if 条件
filtered = [item for item in raw_results if item["score"] >= 0.6]
print(f"\n第1步过滤（>=0.6）后，剩余 {len(filtered)} 条")

# 3. 第二步：按分数从高到低排序（.sort 降序）
filtered.sort(key=lambda x: x["score"], reverse=True)
print(f"第2步排序后（最高分在前）：")
for item in filtered:
    print(f"  {item['id']} -> 分数：{item['score']}")

# 4. 第三步：只取前 3 个最相关的（切片）
top_3_results = filtered[:3]
print(f"\n第3步取 Top 3：")
for item in top_3_results:
    print(f"  {item['id']}")

# 5. 第四步：提取这 3 个的内容，准备拼成提示词喂给大模型
final_contents = [item["content"] for item in top_3_results]
print(f"\n第4步提取内容文本：{final_contents}")

# 6. 第五步：把内容拼接成一个长字符串（未来就是你的 Prompt 上下文）
context_string = "\n".join(final_contents)  # join 是字符串的方法，用换行符连接
print(f"\n第5步最终拼成的上下文：\n{context_string}")

print("\n" + "=" * 50)
print("恭喜！你今天跑通了 list_practice.py 全部内容！")
print("=" * 50)



