def print_section(title):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50 + "\n")


#strip():去除首尾空白(空格，换行，制表符，回车)
print_section("strip()")
test = "  hello Lucas  \t"
print(f"\"{test.strip()}722\"")

#strip()并不会修改原字符串。要么直接print(test.strip()),要么把test.strip()赋值给新的变量
test.strip()
print(test)

#strip()括号中的参数默认为空白，会去除首尾空白，但是可以用strip("!")去除首尾“！”
test = "!!!I LOVE!!! YOU!!!!!!"
print(test.strip("!"))#不会去除中间的

#参数是字符集
text = "www.pythonandc.com"
print(text.strip("w.com")) # 会理解为删除两边的w,.,c,o,m,得到pythonand，它不是“删除前缀 www. 和后缀 .com”

#拓展：删除前缀后缀可以是removeprefix(),removesuffix(),这里的参数是字符串，核心是字符串完全匹配，不做展开说明

#strip() 的亲戚 ：lstrip() rstrip() 处理左右
print(test.lstrip("!"))
print(test.rstrip("!"))

#lower(),upper()----转大小写
#llm处理语义问题的时候会遇到大小写问题，
#有的时候python和Python对人来说差不多，但是对于机器是两个字符
#先统一转小写会更好判断(某些情况下)
print_section("upper  lower")
test ="LUCAS i love YOU!!!"
print(test.upper())
print(test.lower())

#同样的，这两个函数不会改变字符串本身
print(test)

#这俩不影响数字空格标点中文
test = "Lucas 我想你了。TaT 55555"
print(test.upper(),end = "\n")#顺便复习一下print的参数
print(test.lower(),end = "\r\n")

test = ["Lucas","i","love","U",100,"年"]
#c
#会报错，test现在是一个列表而upper lower 是字符串方法
new_test = []
for item in test:
    new_test.append(str(item).upper())
print(*new_test,sep = " ",end = "!\n")

#strip() lower() 一起用
yonghushuru = "  i WANT to Study Python  \n\t"
print(yonghushuru.strip().lower())



#split() : 分割字符串为列表
print_section("split()")
text = "   I   \tlove Python"
words = text.split()

print(words)

#默认是空白字符 " " \t \n \r 自动处理多个空格
text = "哈喽，Lucas"
print(text.split("，"))
text = ", , ,hello,lucas"
print(text.split(","))#得到空白，空格，空格，hello，lucas

#可以限制分割次数
text = "I love  \t Claire but it's impossible"
print(text.split(maxsplit=3))
print(text.split(None,3))
#str.split("sep",maxsplit)



#中文没有空格和每个字词之间的间隔符号，怎么解决？要么用in，要么试试第三方库

#replace  替换掉所有old匹配到的内容
print_section("replace()")
#str.replace("old","new")
text = "Lucas loves jujube"
print(text.replace("jujube","Claire"))
print(text.replace("loves","misses"))

#用于删除，new = ""
text = "Hello!!! Lucas???"
text = text.replace("!", "").replace("?", "")
print(text)

#把一段杂乱输入清洗成关键词列表
print_section("clean messy input to keywords")


def clean_to_keywords(text):
    text = text.strip()
    text = text.lower()

    text = text.replace("?", "")
    text = text.replace("？", "")
    text = text.replace("!", "")
    text = text.replace("！", "")
    text = text.replace(".", "")
    text = text.replace("。", "")
    text = text.replace(",", " ")
    text = text.replace("，", " ")

    keywords = text.split()
    return keywords


messy_text = "   I WANT to Study Python!!!  And, I love RAG？？？   "

print("清洗前：", messy_text)
print("关键词列表：", clean_to_keywords(messy_text))



