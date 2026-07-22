# 字典是一种用键和值保存数据的数据结构。
# 空字典
message = {}

# 值几乎可以是任何类型
message = {
    "content": "我想学习 Python",   # str
    "day": 10,                     # int
    "processed": False,            # bool
    "score": 9.5,                  # float
    "keywords": ["Python", "字典"], # list
    "metadata": {"source": "user"}  # dict
}

# 键必须是可哈希的类型（最常见最常用还是str）list,set,dict 不能作为键因为他们是可修改的,但是元组可以
data = {
    "name": "Lucas",  # str
    10: "Day 10",     # int
    3.14: "圆周率",   # float
    True: "是",       # bool
    (1, 2): "坐标"    # tuple
}

message = {
    "role": "Lucas",
    "content": "I wanna be better",
    "day": 10
}
# 一个字典可以同时保存不同类型的值：
# "role"       → str
# "content"    → str
# "day"        → int

print(message)

# 查 通过键读取对应的值
print(message["role"])
print(message["content"])
print(message["day"])

#不存在的键怎么办？会报错呀不够安全
# print(message["intent"])
# in <module>
#     print(message["intent"])
#           ~~~~~~~^^^^^^^^^^
# KeyError: 'intent'
# get方法更安全，不存在时返回None(默认返回值可修改)
print(message.get("intent"))
print(message.get("intent","未分类"))


# 改
message["content"] = "I dont want to be a loser"
message["day"] = 22
print(message)

# 增 如果这个键原来不存在，赋值操作就会新增一个键值对：
message["intent"] = "思念"
print(message)

# 删 del pop
del message["day"]
print(message)
# pop 不仅删除还返回被删除的value
intent = message.pop("intent")
print(intent)
print(message)

# 遍历方法
# 直接遍历字典，默认得到键
for a in message:
    print(a)

# equals to
for a in message.keys():
    print(a)

# 只遍历值
for a in message.values():
    print(a)

# 遍历键值对
for key, value in message.items():
    print(key,value)
# role Lucas
# content I dont want to be a loser
    print(f"{key}: {value}")

messages = [
    "你好",
    "我想学习 Python",
    "exit",
    "这条消息不会被处理"
]

# 改写成列表加字典
messages = [
    {
        "role": "user",
        "content": "你好",
        "processed": False
    },
    {
        "role": "user",
        "content": "我想学习python",
        "processed": False
    },
    {
        "role": "user",
        "content": "exit",
        "processed": False
    },
    {
        "role": "user",
        "content": "这条消息不会被处理",
        "processed": False
    },
]

sum = 0
for message in messages:
    if message["content"] == "exit":
        break
    print(message["role"],message["content"])
    message["processed"] = True
    sum = sum + 1
print(sum)