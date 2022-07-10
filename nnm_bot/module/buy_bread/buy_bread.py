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
#     "bread": 面包数
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


def buyBread(user_id):
    for user in data:
        # 非首次领取
        if (user['user_id'] == user_id):
            status = checkTime(user['time'])

            if status == 1:
                bread = random.randint(1, 10) * 2
                user['bread'] += bread
                user['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                saveJson()
                return '本日首次！甜点数*2，买了{}个甜点，你已拥有{}个甜点'.format(bread, user['bread'])
            elif status == 2:
                bread = random.randint(1, 10)
                user['bread'] += bread
                user['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                saveJson()
                return '你已成功购买{}个甜点，你已拥有{}个甜点'.format(bread, user['bread'])
            else:
                return '还要再等{}分钟才可以买甜点哦'.format(status)

    # 循环结束仍未匹配视为首次领取
    bread = random.randint(1, 10) * 5
    newUser = {'user_id': user_id, 'bread': bread, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    data.append(newUser)
    saveJson()
    return '首次买甜品！甜点数*5，你已拥有{}个甜点，记得每小时都来一次哦'.format(bread)


def myBread(user_id):
    for user in data:
        if (user['user_id'] == user_id):
            return '你现在有{}个甜点'.format(user['bread'])
    # 循环结束仍未匹配视为未买过面包
    return '你还没有买过甜点哦，发送买甜点试试看吧'


def eatBread(user_id):
    for user in data:
        if (user['user_id'] == user_id):
            bread = random.randint(1, 10)
            user['bread'] -= bread
            saveJson()
            return '吃掉了{}个甜点，你还有{}个甜点\n诶？你问nnm有什么用吗，nnm也不知道哦'.format(bread, user['bread'])
    # 循环结束仍未匹配视为未买过面包
    return '你还没有买过甜点哦，发送买甜点试试看吧'


# 整活功能，数值还要斟酌一下
def grabBread(host_id, object_id):
    if (host_id == object_id):
        return '不可以抢自己！'

    # 判断双方是否购买过面包
    isHostExist = False
    isObjectExist = False

    for user in data:
        if (user['user_id'] == host_id):
            isHostExist = True
        elif (user['user_id'] == object_id):
            isObjectExist = True

    if (isHostExist == False or isObjectExist == False):
        return '自己或者对方还没有买过甜点哦'

    dice = random.randint(1, 100)
    if (dice > 70):
        bread = random.randint(1, 10)
        for user in data:
            if (user['user_id'] == host_id):
                user['bread'] += bread
            elif (user['user_id'] == object_id):
                user['bread'] -= bread
        saveJson()
        return '1D100={}>70，判定成功，抢走了对方{}个甜点'.format(dice, bread)
    else:
        bread = random.randint(1, 10)
        for user in data:
            if (user['user_id'] == host_id):
                user['bread'] -= bread
            elif (user['user_id'] == object_id):
                user['bread'] += bread
        saveJson()
        return '1D100={}<70，判定失败，反而被对方抢走了{}个甜点'.format(dice, bread)