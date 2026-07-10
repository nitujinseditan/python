docs = [
    "strip()用于去掉字符串开头和结尾，默认是去除空白，也可以增加参数",
    "lower() 用来把英文字母转换成小写。",
    "upper() 用来把字母转换成大写，不会改变原字符串",
    "split() 用来把字符串切成列表。",
    "replace() 用来替换字符串中的内容。",
    "RAG 是检索增强生成，先检索资料，再让模型生成回答。"
]

#处理问题和语料的函数
def clean_text(text):
    res = text.strip().lower().replace("?","").replace("？","")
    return res

#清洗语料
corpus = []
for doc in docs:
    item = {
        "raw": doc,
        "clean": clean_text(doc)
    }
    corpus.append(item)

#进行搜索retrieve
def retrive(que,corpus):
    que = clean_text(que)
    results = []
    for item in corpus:
        clean_doc = item["clean"]
        if "split" in que and "split" in clean_doc:
            results.append(item["raw"])
        elif "strip" in que and "strip" in clean_doc:
            results.append(item["raw"])
        elif "lower" in que and "lower" in clean_doc:
            results.append(item["raw"])
        elif "replace" in que and "replace" in clean_doc:
            results.append(item["raw"])
        elif "rag" in que and "rag" in clean_doc:
            results.append(item["raw"])

    return results