def print_section(title):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50 + "\n")


#str
print_section("String Operations")
name = "Lucas"
major = "Software Engineering"
goal = "build an agent"

#字符串可以相加
first_name = "Lucas"
message = "Hello, " + first_name

print(message)


#字符串+数字会报错
age = 20
#message = "I am " + age
#TypeError: can only concatenate str (not "int") to str

#先转换类型
message = "I am " + str(age)
print(message)

#或者用f-string
message = f"I am {age}"
print(message)
info = f"My name is {name}, I am majoring in {major}, and my goal is to {goal}."
print(info)

#int
#float 没有double 底层就是C语言的double精度浮点数
print_section("Numeric Operations")
confidence = 0.82

#值得一提的是，python的/并不会向下取整，而是得到float
total = 100
price1 = 10
price2 = 15
num1 = total / price1
num2 = total / price2
print(num1)
print(num2)#float 的十进制显示结果，可能会出现很多位近似值。
#控制位数用f-string
print(f"{num2:.2f}")#保留两位小数

#向下取整用//
num2 = total // price2
print(num2)

print_section("Boolean Operations")
#bool
is_beginner = True
has_api_key = False#首字母大写
print(f"Is beginner: {is_beginner}")
print(f"Has API key: {has_api_key}")

#type 查看变量类型
print(type(name))
print(type(age))
print(type(confidence))
print(type(is_beginner))

#""的存在会变成str
day1 = 1
day2 = "1"
print(type(day1))
print(type(day2))

#f-string 把变量放在一句话里，甚至可以接受运算
print_section("f-string Demonstration")
#普通写法
name = "Lucas"
age = 20
print("My name is " + name + ". I am " + str(age) + " years old.")

#f-string写法
print(f"My name is {name}. I am {age} years old.")

#演示可以运算
print(f"I am {age + 1} years old next year.")

#tips：
print_section("Variable Naming Rules and Memory Mechanism")
#变量命名规则：
#1. 只能包含字母、数字和下划线，不能以数字开头
#2. 不能使用python的关键字如：if、else、for、while、def等
#变量名二次赋值时的内存机制：
#当变量名被重新赋值时，原来的对象可能被回收，新的对象被创建并绑定到变量名上
#用id()函数可以查看对象的内存地址


message = "Hello, Lucas"
print(message)
print(id(message))

message = "I am 20"
print(message)
print(id(message))

message = "I am 21"
print(message)
print(id(message))

#btw,print()会自动换行
#怎么解决想不换行的print请求呢？
#print函数本身默认的结构为print(x, end="\n")
#只需要这样就好啦
print_section("Print Function Demonstration")
print("Hello, ",end = "")
print("World!")

#学一下print吧，print的完整形式大概是：
#print(*objects, sep=' ', end='\n', file=None, flush=False)
#*object 表示可以传入多个对象，sep表示分隔符，end表示结尾符，file表示输出文件，flush表示是否立即刷新缓冲区
items = [1, 2, 3, 4, "hello"]
print(*items, sep=", ", end=".\n")#输出1, 2, 3, 4, hello.
#file,flush在写日志，保存输出，实时显示进度的时候用的上，但是现在就先不管了
#验收环节：真正描述agent用户
print_section("Acceptance Test")
print_section("Agent User Profile")

user_name = "Lucas"
user_major = "Software Engineering"
user_goal = "build an agent"
daily_study_minutes = 90
current_day = 2
is_python_beginner = True
confidence = 0.82

print(f"User name: {user_name}")
print(f"Major: {user_major}")
print(f"Goal: {user_goal}")
print(f"Daily study time: {daily_study_minutes} minutes")
print(f"Current day: Day {current_day}")
print(f"Python beginner: {is_python_beginner}")
print(f"Current confidence: {confidence:.2f}")

print(type(user_name))
print(type(daily_study_minutes))
print(type(current_day))
print(type(is_python_beginner))
print(type(confidence))