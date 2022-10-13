from operator import truediv
import os, json
from datetime import datetime
import random

data = []
path = os.path.join(os.path.dirname(__file__), 'data.json')


# 懒得写生成和校验了，请确保目录下有一名为'data'的json文件，且其中至少包括一对中括号
# 生成的json格式如下：
# [
#   {
#     "user_id": qq号,
#     "bread": id
#     "time": 最后一次领取时间
#   },
# ]

def loadJson():
    global data
    with open(path, 'r', encoding='utf8') as f:
        data = json.load(f)


loadJson()


def saveJson():
    with open(path, 'w', encoding='utf8') as f:
        # 关闭ascii码输出， 缩进2
        json.dump(data, f, ensure_ascii=False, indent=2)


def checkTime(time):
    now = datetime.now()
    # 从str转换为datetime
    time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    hourLimit = (now - time).seconds / 60
    dayLimit = (now - time).days

    # seconds不会跨日计算，要分开判断
    if (dayLimit >= 1 or hourLimit >= 60):
        if (dayLimit) >= 1:
            # 状态1，表示当天第一次领取
            return 1
        else:
            # 状态2，表示当天非第一次领取
            return 2
    else:
        # 状态0，返回距离下一次领取的时间
        return int(60 - hourLimit)

#偷懒直接用的buy bread 把bread换成id
def getID(user_id, id):
    for user in data:
        # 非首次领取
        if (user['user_id'] == user_id):

            return '你已经绑定过了哦，如果需要更换id发送nnm更换玩家id试试吧'

    # 循环结束仍未匹配视为首次领取
    if id == '':
        return '请输入id！'
    else:
        if id.isdigit():
            bread = id
            newUser = {'user_id': user_id, 'bread': bread, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            data.append(newUser)
            saveJson()
            return '绑定成功(如果是日服id需要输入绑定日服玩家+id，更多信息请输入help查看)'
        else:
            return 'id包含非数字字符！（不需要空格哦）'


def myID(user_id):
    bread = 0
    for user in data:
        if (user['user_id'] == user_id):
            bread = user['bread']
            return bread
    # 循环结束仍未匹配视为未买过面包
    return bread

def exchangeID(user_id, id):
    for user in data:
        # 非首次领取
        if (user['user_id'] == user_id):
            if id != '':
                if id.isdigit():
                    user['bread'] = id
                    user['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    bread = user['bread']
                    saveJson()
                    return '更换id成功'
                else:
                    return 'id包含非数字字符！（不需要空格哦）'
            else:
                return '请输入id！'
    return '你还没有绑定玩家哦，发送nnm绑定玩家试试吧'


