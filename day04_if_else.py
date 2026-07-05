#ifelse 条件判断
def print_section(title):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50 + "\n")

#if 条件:
#    条件成立时执行(条件返回True)
#else:
#    条件不成立时执行(条件返回False)

print_section("If-Else Statement")
study_minutes = 90
def is_study_enough(minutes):
    if minutes >= 90:
        return True
    else:
        return False
#批判一下自己：这个函数可以写得更简单：return minutes >= 90
# 为什么呢
# 因为比较表达式本身就是一个boolean值，只有True或者False

if is_study_enough(study_minutes):
    print("今天学习量达标")
else:
    print("今天还需要继续")

#if 后面跟的是是判断表达式，会被python解释器解释成True或False
# 其实甚至可以不跟判断表达式，朋友truthy/falsy的概念：
# 0、0.0、""、[]、{}、None → False
# 非零数字、非空字符串、非空列表等 → True
if 0:
    print("True")
else :
    print("False")

#elif 
#if 条件1:
#    条件1成立时执行
#elif 条件2:
#    条件1不成立，但条件2成立时执行
#else:
#    前面所有条件都不成立时执行
#从上往下判断，遇到满足的就执行然后跳过后面的


print_section("If-Elif-Else Statement")
score = 85
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

print(f"Your grade is {score}, you get a {grade(score)}.")

#学习时长建议器
while True:
    try:
        minutes = int(input("请输入今天学习的分钟数: "))
        if minutes < 0:
            print("请输入一个非负数的分钟数。")
            continue
        if minutes >= 90:
            print("今天学习很刻苦")
        elif minutes >= 60:
            print("今天学习量达标")
        else:
            print("今天还需要继续")
        break
    except ValueError:
        print("请输入一个整数。")
#当然也可以升级成能处理整数小数的版本
while True:
    try:
        minutes = float(input("请输入今天学习的分钟数: "))
        if minutes < 0:
            print("请输入一个非负数的分钟数。")
            continue
        if minutes >= 90:
            print("今天学习很刻苦")
        elif minutes >= 60:
            print("今天学习量达标")
        else:
            print("今天还需要继续")
        break
    except ValueError:
        print("请输入一个数字。")

#其实不需要分开int和float的情况，因为float可以处理整数和小数，int只能处理整数。
#python还有一个不同于C语言逻辑的写法
# Day 04: Conditionals

while True:
    minutes_text = input("请输入今天学习了多少分钟：")

    try:
        minutes = int(minutes_text)

        if minutes < 0:
            print("学习时长不能是负数，请重新输入。")
            continue

        break

    except ValueError:
        print("输入无效，请输入整数，比如 0、30、90。")


if minutes >= 90:
    print("很好，今天学习量达标。")
elif minutes >= 30:
    print("还可以，但建议再补一点。")
elif minutes > 0:
    print("今天开始了，但学习量偏少。")
else:
    print("今天还没有开始学习。")

# minutes在循环内被定义：在C/Java，如果变量是在循环代码块（块很重要）中被生成，循环外通常不能访问，但是py可以
# 因为python的变量作用域是函数级别的，而不是块级别的。
# 在C和Java，{}会形成块级作用域，但Python没有。
# python的缩进只是为了表示代码块的层级关系，并不会影响变量的作用域。
# 要格外注意变量的作用域。
# if / elif / else 不创建新作用域
# while 不创建新作用域
# for 不创建新作用域
# try / except 不创建新作用域
# 函数 def 会创建新作用域
# 如果忽略这一点会怎样？
print_section("Variable Scope Demonstration")
current_user = "Lucas"

users = ["Tom", "Jerry", "Alice"]

for current_user in users:
    print("正在检查用户：", current_user)

print("当前登录用户：", current_user)
#输出：
#正在检查用户： Tom
#正在检查用户： Jerry
#正在检查用户： Alice
#当前登录用户： Alice
#Python 的 for 不会创建新的块级作用域，所以循环变量 current_user 会直接覆盖外面的 current_user。
#正确写法：
print("正确写法：")
current_user = "Lucas"
for current_check_user in users:
    print("正在检查用户：", current_check_user)
print("当前登录用户：", current_user)

#输入校验,学习时长建议可以写成函数
def get_valid_minutes():
    while True:
        try:
            minutes = float(input("请输入今天学习的分钟数: "))

            if minutes < 0:
                print("请输入一个非负数的分钟数。")
                continue

            return minutes

        except ValueError:
            print("请输入一个数字，比如 0、30、90、45.5。")

def give_study_advice(minutes):
    if minutes >= 90:
        print("今天学习很刻苦")
    elif minutes >= 60:
        print("今天学习量达标")
    else:
        print("今天还需要继续")

minutes = get_valid_minutes#不加括号也不会报错？
#不加括号就是不调用函数，把函数本身赋值给minutes
print(type(minutes)) # <class 'function'>
minutes = get_valid_minutes()
give_study_advice(minutes)
