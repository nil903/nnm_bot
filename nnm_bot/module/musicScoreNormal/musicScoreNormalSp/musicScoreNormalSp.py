import os, json
from fuzzywuzzy import process

data = {}
path = os.path.join(os.path.dirname(__file__), 'data.json')

# 角色基础数据来源于HoshinoBot开发群，思路来源于Whois功能，非常感谢大佬们
#
# 懒得写生成和校验了，请确保目录下有一名为'data'的json文件，且指定格式如下：
# {
#   序号  昵称列表，请确保首个元素为角色名称
#   "1": ["丸山彩","aya","彩","彩彩","修哇修哇"],
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

def get_musicName(i):
    if str(i) is not None:
        result = data[str(i)][0]
        return result, '这首歌的名字是是{}'.format(result)
    else:
        print('没找到')
        return None, None
# 直接匹配，返回昵称对应键的值
def get_name(name):
    if name in processed_data:
        index =  processed_data[name]
        result = data[index][0]
        return index, result
    else:
        return None, None

# 用fuzzywuzzy库模糊匹配最佳项，同时返回匹配率
def guess_name(name):
    guess, score = process.extractOne(name, processed_data.keys())
    index = processed_data[guess]
    result = data[index][0]
    return guess, score, index, result

def search(name):
    index, result = get_name(name)
    if index is not None:
        return index, '是{}的ex谱面.（有亿点小，建议放大看哦）'.format(result)
    else:
        guess, score, index, result = guess_name(name)
        return index, '没有找到{}，你有{}%的可能在找{}，它是{}的ex'.format(name, score, guess, result)
