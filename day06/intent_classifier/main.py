from classifier import clean_text, classify_intent
from test_classifier import run_tests


def run_interactive():
    """交互模式：持续接收用户输入并输出意图分类"""
    print("\n进入交互模式")
    print("输入 exit、quit、q 或「退出」结束程序。\n")

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


def main():
    """主入口：提供菜单选择（测试 / 交互 / 退出）"""
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


if __name__ == "__main__":
    main()
