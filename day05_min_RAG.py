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
    return (
        text.strip()
        .lower()
        .replace("?", "")
        .replace("？", "")
        .replace("!", "")
        .replace("！", "")
        .replace(".", "")
        .replace("。", "")
        .replace(",", "")
        .replace("，", "")
    )

#清洗语料
corpus = []
#这是个列表，每个元素是一个字典
for doc in docs:
    item = {
        "raw": doc,
        "clean": clean_text(doc)
    }
    corpus.append(item)

#进行搜索retrieve
def retrieve(que,corpus):
    que = clean_text(que)
    results = []
    keywords = ["strip", "lower", "upper", "split", "replace", "rag"]#用数据结构（列表）减少重复if
    for item in corpus:
        clean_doc = item["clean"]

        for keyword in keywords:
            if keyword in que and keyword in clean_doc:
                results.append(item["raw"])
                break

    return results

question = input("请输入问题：")
results = retrieve(question, corpus)

print("检索到的资料：")
print(results)