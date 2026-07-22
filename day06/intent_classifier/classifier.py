from config import intent_keywords


def clean_text(text):
    """清除首尾空白并统一英文大小写"""
    new_text = text.strip().lower()
    # punctuation = ["，", "。", "！", "？", ",", ".", "!", "?"]
    # for punc in punctuation:
    #     new_text = new_text.replace(punc, "")
    return new_text


def contains_keyword(text, keywords):
    """判断 text 中是否包含 keywords 中的任意一个关键词"""
    for word in keywords:
        if word in text:
            return True
    return False


def classify_intent(text):
    """遍历 intent_keywords 字典，返回首个匹配的意图类别"""
    cleaned_text = clean_text(text)
    for intent, keywords in intent_keywords.items():
        if contains_keyword(cleaned_text, keywords):
            return intent
    return "未知"
