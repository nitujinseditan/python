def print_section(title):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50 + "\n")


#input(),int(),float(),str() are the built-in functions used for type conversion in Python.
#input() 和强制类型转换是处理用户输出的好方法
print_section("Input")
name = input("Enter your name: ")
print(f"Hello, {name}")
#input() :
#1. 如果你传了 prompt，就先把 prompt 打印出来
#2. 暂停程序，等待用户在终端输入
#3. 用户按 Enter 后，读取这一整行内容
#4. 去掉最后的换行符
#5. 把结果作为 str 返回（即使是数字也是 "20"）

print_section("Type Conversion")
#一个没有类型转换引起的小错误例子
birth_year = input("Enter your birth year: ")
#age = 2026 - birth_year  这里没有进行类型转换，birth_year 是 str 类型，不能直接参与减法运算
age = 2026 - int(birth_year)  #这里使用了 int() 函数将 str 类型的 birth_year 转换为 int 类型    
print(age)

#int() 转换为int类型
#float() 转换为float类型
#str() 转换为str类型
#小数转换

print_section("Float Conversion")

daily_minutes_text = input("How many minutes do you study today? ")
daily_minutes = float(daily_minutes_text)

daily_hours = daily_minutes / 60

print(f"You studied {daily_minutes:.0f} minutes today.")
print(f"That is about {daily_hours:.2f} hours.")
print(type(daily_minutes_text))
print(type(daily_minutes))


#异常处理：如果输入的不是数据但是用了数字的强制类型转换：
#一般的没有防止异常输入的：
#def age_calculator_normal():    
#    birth_year = input("Enter your birth year: ")
#    age = 2026 - int(birth_year)
#    print(f"You are {age} years old.")

#age_calculator_normal(Lucas) 会被提醒不要输入非数字的内容
#不让程序直接崩溃，而是捕获错误并提示用户重新输入
#只提示错误：
try:
    birth_year = input("Enter your birth year: ")
    age = 2026 - int(birth_year)
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid year.")

#提醒重新输入：一直问，直到输入合法
while True:
    try:
        birth_year = input("Enter your birth year: ")
        age = 2026 - int(birth_year)
        print(f"You are {age} years old.")
        break  # 如果输入正确，跳出循环
    except ValueError:
            print("Please enter a valid year.")