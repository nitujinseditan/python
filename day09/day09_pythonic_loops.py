def print_section(title):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50 + "\n")

print_section("for")
#for 循环 Python 更常见的思维：直接遍历元素
messages = ["你好", "学习 Python", "今天天气不错"]

for message in messages:
    print(message)

tasks = ["吉他","做饭","想你"]

for task in tasks:
    print(f"待办：{task}")

#range()
print_section("range")
for number in range(5):
    print(number)

#range(n)生成从0开始到（n-1）结束的整数序列，不包含n
#range(n)本质是一个range对象而非列表
print(range(5),end = "\t")
print(list(range(5)),end = "\n\n")#强转
#它不会立刻把所有数字都创建出来，因此比直接创建一个很大的数字列表更节省内存。

#三种写法
#range(end)

#range(start,end) 左闭右开
for number in range(2, 6):
    print(number,end = " ")

print()

#range(start,end,length) 左闭右开
for number in range(1,11,2):
    print(number,end = " ")
print()

#也可以倒着走，神奇吧
for num in range(11,1,-2):
    print(num,end = " ")
print()

for num in range(1,6):
    print(num,end = " ")
print()

for num in range(2,11,2):
    print(num,end = " ")
print()

for num in range(3,0,-1):
    print(num,end = " ")
print("开始！")
print()

#enumerate(输出的对象,start=开始的下标) 
# class enumerate(
#     iterable: Iterable[str],
#     start: int = 0
# )
print_section("enumerate")
#如果涉及编号输入，可以想到的一个想法是：
messages = ["Lucas", "loves", "Coco"]
for i in range(len(messages)):
    print(f"{i+1}. {messages[i]}")

#enumerate 简化了表达
for index,message in enumerate(messages):
    print(f"{index}. {message}")

#会发现输出的计数从0开始，我们可以传入start参数表示计数开始的数字
for index,message in enumerate(messages,start = 1): #enumerate(messages,1) also worked 
    print(f"{index}. {message}")

# enumerate产生了一个元素为元组的列表
# [
#     (0, "Lucas"),
#     (1, "loves"),
#     (2, "Coco")
# ]
# 每次循环取出其中一组数据，再分别交给两个变量

courses = ["Python", "数据结构", "线性代数"]

for num,course in enumerate(courses, 1):
    print(f"第{num}门课程：{course}")

print_section("zip")

#zip
# class zip(
#     iter1: Iterable[_T1@__new__],
#     iter2: Iterable[_T2@__new__],
#     /,
#     *,
#     strict: bool = False
# )
# 得到一个元素位元组的列表
# enumerate() ：同时取得一个列表的编号和元素。
# zip() ：      同时遍历两个或多个序列中位置对应的元素。
courses = ["Python", "数据结构", "线性代数"]
minutes = [90, 60, 45]

print("一个常见的想法：下表对应")
for i in range(len(courses)):
    print(f"{courses[i]}: {minutes[i]}分钟")

print("\nzip提供了不需要下标的方法")

for course, minute in zip(courses, minutes):
    print(f"{course}：{minute}分钟")

# 这个程序真正关心的是“课程和对应时间”，并不关心下标 i。因此 zip() 更直接
# 两个列表长度不同会怎样？  只会完成短链
# 如果两个列表本应一一对应，就要检查它们的长度是否一致，否则可能悄悄漏掉数据。
courses = ["Python", "数据结构", "线性代数"]
minutes = [90, 60]

for course, minute in zip(courses, minutes):
    print(course, minute)
print()

#break 结束当前最近的一层循环
messages = ["你好", "学习 Python", "今天天气不错", "退出", "不应该看到我"]
for message in messages:
    if message == "退出":
        break
    print(message)

messages = ["你好", "学习 Python", "讲解 enumerate", "退出", "这条不应输出"]
for num, message in enumerate(messages, 1):
    if message == "退出":
        break
    print(f"{num}. {message}")