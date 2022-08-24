import os, json
from fuzzywuzzy import process

data = {}
path = os.path.join(os.path.dirname(__file__), 'data.json')

# 懒得写生成和校验了，请确保目录下有一名为'data'的json文件，且指定格式如下：
# {
#   序号  昵称列表，不需要返回姓名就没有限制，需要的话参考另一个花名册
#   "1": ["进藤天音","天音","妹妹","進藤天音","音宝","amane"],
# }

def loadJson():
    global data
    with open(path, 'r', encoding='utf8') as f:
        data = json.load(f)

loadJson()

processed_data = {}

def insert():
    items = data.items()
    # 遍历获得序号和昵称列表
    for index, nicknames in items:
        # 遍历昵称列表，加入字典，键为昵称，值为序号
        for nickname in nicknames:
            if nickname not in processed_data:
                processed_data[nickname] = index

insert()

# 直接匹配，返回序号
def get_name(name):
    if name in processed_data:
        index = processed_data[name]
        result = data[index][0]
        return index, result
    else:
        return None, None

# 用fuzzywuzzy库模糊匹配最佳项，同时返回匹配率
def guess_name(name):
    guess, score = process.extractOne(name, processed_data.keys())
    index = processed_data[guess]
    return guess, score, index

def search(name):
    index, result = get_name(name)
    if index is not None:
        return index, '是{}哦'.format(result)
    else:
        guess, score, index = guess_name(name)
        result = data[index][0]
        return index, '没有找到{}，你有{}%的可能在找{}, 她是{}\n'.format(name, score, guess,result)
