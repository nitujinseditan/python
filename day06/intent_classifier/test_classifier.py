from classifier import classify_intent


def run_tests():
    """自动测试：遍历测试用例，统计通过率"""
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

if __name__ == "__main__":
    run_tests()
