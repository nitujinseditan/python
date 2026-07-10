#关键词
study_keywords = [
    "学习",
    "复习",
    "练习",
    "教程",
    "讲解",
    "掌握",
    "作业",
    "怎么学",
    "如何学",
]

query_keywords = [
    "查询",
    "搜索",
    "查找",
    "什么",
    "为什么",
    "多少",
    "如何",
    "天气",
    "气温",
    "怎么",
]

chat_keywords = [
    "你好",
    "谢谢",
    "再见",
    "笑话",
    "心情",
    "聊天",
    "开心",
]

intent_keywords = {
    "学习" : study_keywords,
    "查询": query_keywords,
    "闲聊": chat_keywords,
}
# print(study_keywords)
# print(type(study_keywords))
# print(len(study_keywords))

#文本清理函数：当前版本暂不移除标点，因为子串关键词匹配通常不受句末标点影响。
#后续若改为完整字符串比较、分词或更复杂的文本处理，再加入标点清洗。
def clean_text(text):
    new_text = text.strip().lower()
    # punctuation = ["，", "。", "！", "？", ",", ".", "!", "?"]
    # for punc in punctuation:
    #     new_text = new_text.replace(punc,"")
    return new_text

#关键词匹配
def contains_keyword (text,keywords):
    for word in keywords:
        if word in text:
            return True
    return False


#输出函数
def classify_intent(text):
    cleaned_text = clean_text(text)
    for intent,keywords in intent_keywords.items():
        if contains_keyword(cleaned_text,keywords):
            return intent
        
    return "闲聊"

#测试输出函数
# print(classify_intent("我想学习 Python"))
# print(classify_intent("今天气温多少度？"))
# print(classify_intent("你好呀"))
# print(classify_intent("如何高效复习？"))
# print(classify_intent("帮我订一张机票"))
# print(classify_intent("我不想学习，我只想和你聊天"))
             
# 输入函数
def run_interactive():
    print("\n进入交互模式")
    print("输入 exit、quit、q 或“退出”结束程序。\n")

    while True:
        user_word = input("请输入：")
        cleaned_text = clean_text(user_word)

        if cleaned_text in ["exit", "退出", "q", "quit"]:
            print("程序已退出")
            break

        if not cleaned_text:
            print("输入不能为空")
            continue

        intent = classify_intent(user_word)
        print(f"意图：{intent}")


# 测试函数
# 自动测试函数
def run_tests():
    test_cases = [
        ("我想学习 Python", "学习"),
        ("今天气温多少度？", "查询"),
        ("你好呀", "闲聊"),
        ("如何高效复习？", "学习"),
        ("帮我查找一下资料", "查询"),
        ("我不想学习，我只想和你聊天", "闲聊"),
    ]

    passed_count = 0

    for text, expected_intent in test_cases:
        actual_intent = classify_intent(text)

        if actual_intent == expected_intent:
            print(f"✅ 输入：{text}")
            print(f"   预期：{expected_intent}")
            print(f"   实际：{actual_intent}")
            passed_count += 1
        else:
            print(f"❌ 输入：{text}")
            print(f"   预期：{expected_intent}")
            print(f"   实际：{actual_intent}")

        print("-" * 40)

    total_count = len(test_cases)
    pass_rate = passed_count / total_count * 100

    print(f"测试完成：{passed_count} / {total_count}")
    print(f"通过率：{pass_rate:.1f}%")

#主函数入口：提供测试或交互两个选项
def main():
    while True:
        print("\n请选择运行模式：")
        print("1. 自动测试")
        print("2. 交互模式")
        print("3. 自动测试后进入交互模式")
        print("q. 退出")

        choice = input("请选择：").strip().lower()

        if choice == "1":
            run_tests()

        elif choice == "2":
            run_interactive()

        elif choice == "3":
            run_tests()
            run_interactive()

        elif choice in ["q", "quit", "exit", "退出"]:
            print("程序已退出")
            break

        else:
            print("输入无效，请输入 1、2、3 或 q。")
print(__name__) #__name__ 变量：在直接执行当前文件的时候解释器解释为__main__ ,否则为文件名
if __name__ == "__main__":
    main()


        