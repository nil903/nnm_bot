from util.receiver import rev_msg
from util.sender import *
from util.trigger import *
from util.parser import *
import random
from bs4 import BeautifulSoup
import requests, os
from module.buy_bread import buy_bread
from module.nickname import nickname
from module.cv_nickname import cv_nickname
import re

qq_robot=eval(input('请输入机器人QQ号：'))
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}

img_list1 = []
img_list2 = []

def get_img_list(key):
    img_list=[]
    n = 42
    i = random.randint(1, 212)
    j = n * i
    url = requests.get('https://gelbooru.com/index.php?page=post&s=list&tags={}%21+&pid={}'.format(key, j))
    # url.encoding = 'utf-8'
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    movie = soup.find_all('article', class_='thumbnail-preview')
    for i in movie:
        imgsrc = i.find_all('img')[0].get('src')
        img_list.append(imgsrc)
    return img_list

def get_img_list1(key):
    img_list=[]
    for j in [0,24,48,72,96,120]:
        url = requests.get('https://www.duitang.com/search/?kw={}&type=feed&start={}'.format(key,j))
        # url.encoding = 'utf-8'
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        movie = soup.find_all('div', class_='mbpho')
        for i in movie:
            imgsrc = i.find_all('img')[0].get('src')
            img_list.append(imgsrc)
    return img_list

img_list1=get_img_list('bang_dream')
img_list2=get_img_list1('二次元')


id_list=[]
while True:
    qq_list = []
    try:
        rev = rev_msg()
        id = rev['message_id']
        if (len(id_list) >= 50):
            id_list = []
        print(id_list)
        # print(time1==time2)
        if id not in id_list:
            id_list.append(id)
            print(rev)
        else:
            continue
    except:
        continue
    if rev["post_type"] == "message":
        if rev["message_type"] == "private":
            message=rev['raw_message']
            qq = rev['sender']['user_id']

        elif rev["message_type"] == "group":
            # 提前定义好，后面直接用，无须重复获取
            # 群号：int
            group = rev['group_id']
            # 发送者QQ号：int
            user_id = rev['sender']['user_id']
            # 消息：str
            message = rev['raw_message']

            if "[CQ:reply" in rev["raw_message"] and "[CQ:at,qq={}]".format(qq_robot) in rev["raw_message"]:
                message = rev['raw_message']
                i = random.randint(42, 48)
                send_msg({'msg_type': 'group', 'number': group,
                          'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                              i)})

            elif "[CQ:at,qq={}]".format(qq_robot) in rev["raw_message"]:
                try:
                    # 如果单独@，不追加任何消息，会触发list index out of range
                    message = rev['raw_message'].split(' ')[1]
                except:
                    continue

                if '买面包' in rev['raw_message'] and len(message) == 3:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '买面包'})

                elif 'help' in rev['raw_message']and len(message) == 4 or '使用说明' in rev['raw_message']and len(message) == 4:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': 'morfonica: \n\n'
                                                                               ' 真白： 天音 妹妹 進藤天音 进藤天音 音宝 amane\n\n'
                                                                               ' 七深： 热水酱 西尾夕香 yuuka oyu oyu酱 热水 西尾 夕香\n\n'
                                                                               ' 瑠唯： 島村絢沙 小提琴ayasa 绚沙 岛村绚沙\n'
                                                                               ' 筑紫： mika みか\n\n'
                                                                               ' 透子： 直田姬奈 姬奈\n'})

                elif 'nnm' in rev['raw_message'] and len(message) == 3:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '找七深有什么事吗'})

                elif '骂我' in rev['raw_message'] and len(message) == 2:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '八嘎変態无路赛'})

                elif '买nnm' in rev['raw_message'] and len(message) == 4:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '不可以买七深哦'})


                elif 'toko' in rev['raw_message'] and len(message) == 4 \
                    or '透子' in rev['raw_message'] and len(message) == 2:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '和透子还有morfonica演奏的日子每天都很开心'})

                elif '早上好' in rev['raw_message'] and len(message) == 3 or '早' in rev['raw_message'] and len(message) == 1 \
                    or '早安' in rev['raw_message'] and len(message) == 2:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '早上好！今天也要过普通的一天哟！'})

                elif '晚安' in rev['raw_message'] and len(message) == 2 or '睡觉' in rev['raw_message'] and len(message) == 2:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '晚安！做个好梦'})

                elif '可爱' in rev['raw_message'] and len(message) == 2:
                    i = random.randint(7, 9)
                    send_msg({'msg_type': 'group', 'number': group,
                          'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                              i)})

                elif '看看你的' in rev['raw_message'] and len(message) == 4:
                    i = random.randint(11, 12)
                    send_msg({'msg_type': 'group', 'number': group,
                          'msg': '这是我的[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                              i)})


                elif '老婆' in rev['raw_message'] and len(message) == 2:
                    i = random.randint(14, 18)
                    send_msg({'msg_type': 'group', 'number': group,
                          'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                              i)})

                elif '贴贴' in rev['raw_message'] and len(message) == 2:
                    i = random.randint(28, 31)
                    send_msg({'msg_type': 'group', 'number': group,
                          'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                              i)})

                elif '亲亲' in rev['raw_message'] and len(message) == 2:
                    i = random.randint(32, 33)
                    send_msg({'msg_type': 'group', 'number': group,
                          'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                              i)})

                elif '爬' in rev['raw_message'] and len(message) == 1 \
                    or '快爬' in rev['raw_message'] and len(message) == 2:
                    i = random.randint(34, 35)
                    send_msg({'msg_type': 'group', 'number': group,
                          'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                              i)})

                elif '来点普通的邦邦日常' in rev['raw_message'] and len(message) == 9:
                    try:
                        url = img_list1[random.randint(0, len(img_list1))]
                        send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '这张图好像不太普通哟'})

                elif ('来点纸片人' or '来点二次元') in rev['raw_message'] and len(message) == 5:
                    try:
                        url = img_list2[random.randint(0, len(img_list2))]
                        send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '这张图好像不太普通哟'})

                elif '少女漫画' in rev['raw_message'] and len(message) == 4:
                    try:
                        i = random.randint(1, 245)
                        send_msg({'msg_type': 'group', 'number': group,
                             'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/{}.jpg]'.format(
                                    i)})
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': 'nnm也还没有看到漫画内容呢~'})

                elif '二次元测试' in rev['raw_message'] and len(message) == 5:
                    qq = rev['sender']['user_id']
                    i = random.randint(0, 4)
                    j = random.randint(0, 6)
                    k = random.randint(0, 1)
                    type1 = ['圆脸','椭圆型脸', '方形脸', '长方形脸', '长脸']
                    face = type1[i]
                    height = random.randint(160, 200)
                    type2 =['双马尾','麻花辫', '长发', '短发', '杀马特']
                    hair = type2[i]
                    type3 = ['红','橙', '粉', '绿', '黄' ,'蓝', '紫']
                    color = type3[j]
                    type4 = ['A','B', 'C', 'D', 'E']
                    cup = type4[i]
                    type5 = ['傲娇', '腹黑', '三无', '萌', '病娇']
                    char = type5[i]
                    type6 = ['偶像', '笨蛋', '千金小姐', '网瘾少女', '打工人']
                    identity = type6[i]
                    type7 = ['浅', '深']
                    ds = type7[k]

                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq={}] 二次元的你,长着{},身高{}，{}{}{}，{}cup, 瞳色{}色,{}, 是{}'
                             .format(qq,face,height,ds,color,hair,cup,color,char,identity)})

            else:

                if '来点wlp' in rev['raw_message'] and len(message) == 5:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': 'nnm也很喜欢哟'})

                elif 'nnm买面包' in rev['raw_message'] and len(message) == 6:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '买面包'})

                elif '查卡msr' in rev['raw_message'] and len(message) == 5 or '查卡真白' in rev['raw_message'] and len(message) == 4:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '小真白真可爱~'})

                elif '查卡947' in rev['raw_message'] and len(message) == 5:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '普通路过的邪神日菜酱'})

                elif '抽卡模拟' in rev['raw_message'] and len(message) == 4:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': 'nnm希望你有好运哦'})

                elif '邪神' in rev['raw_message'] and len(message) == 2:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '查卡947'})

                elif 'nnm' in rev['raw_message'] and len(message) == 3:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '找七深有什么事吗'})

                elif ('机票模拟' or '必三模拟') in rev['raw_message'] and len(message) == 4:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '七深收集的米歇鲁贴纸又多起来了~'})

                elif '查卡1385' in rev['raw_message'] and len(message) == 6:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '一般路过的邪神lock酱'})

                elif '您' in rev['raw_message'] and len(message) == 1 or '您您您' in rev['raw_message'] and len(message) == 3:
                    j = random.randint(0, 4)#加图片
                    if j==0:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '和透子一样是天才呢'})
                    elif j==1:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '您您您'})
                    else:
                        i = random.randint(38, 40)
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                                      i)})

                elif 'nnm骂我' in rev['raw_message'] and len(message) == 5:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '八嘎変態无路赛'})

                elif '买nnm' in rev['raw_message'] and len(message) == 4:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '不可以买七深哦'})

                elif '买摩卡' in rev['raw_message'] and len(message) == 3:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '买摩卡会赠送114514个赠品哦'})

                elif '买茨菇' in rev['raw_message'] and len(message) == 3:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '记得要把买茨菇的赠品送给七深哟'})

                elif 'toko' in rev['raw_message'] and len(message) == 4\
                        or '透子' in rev['raw_message'] and len(message) == 2:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '和透子还有morfonica演奏的日子每天都很开心!'})

                elif '害怕' in rev['raw_message']and len(message) == 2:
                        i = random.randint(1, 3)
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(i)})

                elif '好耶' in rev['raw_message']and len(message) == 2:
                        i = random.randint(4, 6)
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(i)})

                elif '早上好' in rev['raw_message']and len(message) == 3 or '早' in rev['raw_message']and len(message) == 1\
                        or '早安' in rev['raw_message']and len(message) == 2:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '早上好！今天也要过普通的一天哟！'})

                elif '晚安' in rev['raw_message']and len(message) == 2 or '睡觉' in rev['raw_message']and len(message) == 2 or '睡了' in rev['raw_message']and len(message) == 2:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '晚安！做个好梦!'})

                elif 'help' in rev['raw_message']and len(message) == 4 or '使用说明' in rev['raw_message']and len(message) == 4:
                    send_msg({'msg_type': 'group', 'number': group, 'msg': 'morfonica: \n\n'
                                                                           ' 真白： 天音 妹妹 進藤天音 进藤天音 音宝 amane\n\n'
                                                                           ' 七深： 热水酱 西尾夕香 yuuka oyu oyu酱 热水 西尾 夕香\n\n'
                                                                           ' 瑠唯： 島村絢沙 小提琴ayasa 绚沙 岛村绚沙\n'
                                                                           ' 筑紫： mika みか\n\n'
                                                                           ' 透子： 直田姬奈 姬奈\n'})

                elif 'nnm决定' in rev['raw_message']:
                    qq = rev['sender']['user_id']
                    if len(message) == 5:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '请输入决策内容'})
                    elif '不' in rev['raw_message']:
                        i = random.randint(0, 1)
                        if i == 0:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq={}]我的答案是YES'.format(qq)})
                        else:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq={}]我的答案是NO'.format(qq)})

                elif '二次元测试' in rev['raw_message'] and len(message) == 5:
                    qq = rev['sender']['user_id']
                    i = random.randint(0, 4)
                    w = random.randint(0, 4)
                    e = random.randint(0, 4)
                    r = random.randint(0, 4)
                    j = random.randint(0, 6)
                    q = random.randint(0, 6)
                    k = random.randint(0, 1)
                    type1 = ['圆脸','椭圆型脸', '方形脸', '长方形脸', '长脸']
                    face = type1[i]
                    height = random.randint(140, 170)
                    type2 =['双马尾','麻花辫', '长发', '短发', '杀马特']
                    hair = type2[w]
                    type3 = ['红','橙', '粉', '绿', '青' ,'蓝', '紫']
                    color = type3[j]
                    eye = type3[q]
                    type4 = ['A','B', 'C', 'D', 'E']
                    cup = type4[w]
                    type5 = ['傲娇', '腹黑', '三无', '萌', '病娇']
                    char = type5[e]
                    type6 = ['偶像', '笨蛋', '千金小姐', '网瘾少女', '打工人']
                    identity = type6[r]
                    type7 = ['浅', '深']
                    ds = type7[k]
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq={}] 二次元的你,长着{},身高{}，{}{}{}，{}cup, 瞳色{}色,{}属性, 是{}'
                             .format(qq, face, height, ds, color, hair, cup, eye, char, identity)})


                elif 'nnm可爱' in rev['raw_message'] and len(message) == 5:
                    i = random.randint(7, 9)
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                                  i)})

                elif '寄' in rev['raw_message'] and len(message) == 1:
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q10.png]'})

                elif 'nnm看看你的' in rev['raw_message'] and len(message) == 7:
                    i = random.randint(11, 12)
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '这是我的[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                                  i)})

                elif '草' in rev['raw_message'] and len(message) == 1:
                    j = random.randint(0, 2)
                    if j == 0:
                        send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q13.png]'})
                    elif j == 1:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': 'ww'})
                    elif j == 2:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '草生'})

                elif 'nnm老婆' in rev['raw_message'] and len(message) == 5:
                    i = random.randint(14, 18)
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                                  i)})

                elif '润' in rev['raw_message'] and len(message) == 1\
                        or '润了' in rev['raw_message'] and len(message) == 2\
                        or '我先润了' in rev['raw_message'] and len(message) == 4:
                    i = random.randint(19, 21)
                    j = random.randint(0, 3)
                    if j == 0:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '这个邦多利炸梦趴体我是一秒也待不下去了'})
                    else:
                        send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                                  i)})

                elif '谢谢' in rev['raw_message'] and len(message) == 2\
                        or '谢了' in rev['raw_message'] and len(message) == 2\
                        or '非常感谢' in rev['raw_message'] and len(message) == 4:
                    i = random.randint(22, 23)
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                                  i)})

                elif '茨菇寄了' in rev['raw_message'] and len(message) == 4:
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q24.png]'})

                elif '摩卡寄了' in rev['raw_message'] and len(message) == 4:
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q25.png]'})

                elif '茨菇老婆' in rev['raw_message'] and len(message) == 4:
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q26.png]'})

                elif '摩卡老婆' in rev['raw_message'] and len(message) == 4:
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q27.png]'})

                elif 'nnm贴贴' in rev['raw_message'] and len(message) == 5:
                    i = random.randint(28, 31)
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                                  i)})
                elif 'nnm亲亲' in rev['raw_message'] and len(message) == 5:
                    i = random.randint(32, 33)
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                                  i)})
                elif 'nnm爬' in rev['raw_message'] and len(message) == 4\
                        or 'nnm快爬' in rev['raw_message'] and len(message) == 5:
                    i = random.randint(34, 35)
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q{}.png]'.format(
                                  i)})

                elif '茨菇可爱' in rev['raw_message'] and len(message) == 4:
                    qq = 3605447298
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:poke,qq={}]'.format(qq)})

                elif ('ycm' or '有车没' or '有车吗') in rev['raw_message'] and len(message) == 3:
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q36.png]'})

                elif '女同好' in rev['raw_message'] and len(message) == 3:
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q41.png]'})

                elif ('？' or '?') in rev['raw_message'] and len(message) == 1\
                        or ('？？？' or '???') in rev['raw_message'] and len(message) == 3:
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/q37.png]'})

                elif '来点普通的邦邦日常' in rev['raw_message']and len(message) == 9:
                    try:
                        url = img_list1[random.randint(0, len(img_list1))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '这张图好像不太普通哟'})

                elif ('nnm来点纸片人' or 'nnm来点二次元') in rev['raw_message'] and len(message) == 8:
                    try:
                        url = img_list2[random.randint(0, len(img_list2))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,file={}]'.format(url)})
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '这张图好像不太普通哟'})

                elif '四格漫画' in rev['raw_message']and len(message) == 4:
                    try:
                        i = random.randint(1, 245)
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/{}.jpg]'.format(i)})
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': 'nnm也还没有看到漫画内容呢~'})

                elif '买甜点' in rev['raw_message']and len(message) == 3:
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.buyBread(user_id)
                    send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:at,qq={}] {}'
                                 .format(user_id, responseText)})

                elif '查甜点' in rev['raw_message']and len(message) == 3:
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.myBread(user_id)
                    send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:at,qq={}] {}'
                                 .format(user_id, responseText)})

                elif '吃甜点' in rev['raw_message']and len(message) == 3:
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.eatBread(user_id)
                    send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:at,qq={}] {}'
                                 .format(user_id, responseText)})

                elif rev['raw_message'].startswith('抢甜点'):
                    user_id = rev['sender']['user_id']
                    # 正则表达式，匹配CQ:at,qq=开头的数字
                    # 当然如果有人手动发送那就没办法了，暂时先这样
                    object_id= re.search('(?<=CQ:at,qq=)\d+\.?\d*', rev['raw_message'])

                    if(object_id is None):
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:at,qq={}] 需要@一个群友哦'
                                 .format(user_id)})
                    else:
                        # 用group()获取匹配到的第一个对象，从str转换为int
                        object_id = int(object_id.group())
                        responseText = buy_bread.grabBread(user_id, object_id)
                        send_msg({'msg_type': 'group', 'number': group,
                                    'msg': '[CQ:at,qq={}] {}'
                                    .format(user_id, responseText)})



                elif rev['raw_message'].startswith('透'):
                    user_id = rev['sender']['user_id']
                    object_id= re.search('(?<=CQ:at,qq=)\d+\.?\d*', rev['raw_message'])
                    if (object_id is None):
                        continue

                    elif "[CQ:at,qq={}]".format(int(object_id.group())) in rev["raw_message"]:
                        # 用group()获取匹配到的第一个对象，从str转换为int
                        object_id = int(object_id.group())
                        user_id = rev['sender']['nickname']
                        send_msg({'msg_type': 'group', 'number': group,
                                'msg': '{}透了[CQ:at,qq={}]'
                                    .format(user_id, object_id)})

                elif ('来点热水酱' in rev['raw_message']and len(message) == 5) or\
                        ('来点西尾夕香' in rev['raw_message']and len(message) == 6)or\
                        ('来点yuuka' in rev['raw_message']and len(message) == 7) or\
                        ('来点oyu' in rev['raw_message']and len(message) == 5) or\
                        ('来点oyu酱' in rev['raw_message']and len(message) == 6) or\
                        ('来点热水' in rev['raw_message']and len(message) == 4) or\
                        ('来点西尾' in rev['raw_message']and len(message) == 4)or\
                        ('来点夕香' in rev['raw_message']and len(message) == 4):
                    i = random.randint(10001, 10258)
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.eatBreadImage(user_id)
                    text = '吃掉了'
                    if text in responseText:
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:at,qq={}] {}[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/yuuka/{}.jpg]'.format(user_id, responseText, i)})
                    else:
                        send_msg({'msg_type': 'group', 'number': group,'msg': '[CQ:at,qq={}] {}'.format(user_id, responseText)})

                elif ('来点天音' in rev['raw_message']and len(message) == 4) or\
                        ('来点妹妹' in rev['raw_message']and len(message) == 4)or\
                        ('来点進藤天音' in rev['raw_message']and len(message) == 6) or\
                        ('来点进藤天音' in rev['raw_message']and len(message) == 6) or \
                        ('来点音宝' in rev['raw_message'] and len(message) == 4) or \
                        ('来点amane' in rev['raw_message']and len(message) == 7):
                    i = random.randint(10001, 10080)
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.eatBreadImage(user_id)
                    text = '吃掉了'
                    if text in responseText:
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:at,qq={}] {}[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/msr/{}.jpg]'.format(user_id, responseText, i)})
                    else:
                        send_msg({'msg_type': 'group', 'number': group,'msg': '[CQ:at,qq={}] {}'.format(user_id, responseText)})

                elif ('来点mika' in rev['raw_message']and len(message) == 6) or\
                        ('来点みか' in rev['raw_message']and len(message) == 4):
                    i = random.randint(10001, 10024)
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.eatBreadImage(user_id)
                    text = '吃掉了'
                    if text in responseText:
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:at,qq={}] {}[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/mika/{}.jpg]'.format(user_id, responseText, i)})
                    else:
                        send_msg({'msg_type': 'group', 'number': group,'msg': '[CQ:at,qq={}] {}'.format(user_id, responseText)})

                elif ('来点島村絢沙' in rev['raw_message']and len(message) == 6) or \
                        ('来点小提琴ayasa' in rev['raw_message'] and len(message) == 10) or \
                        ('来点绚沙' in rev['raw_message'] and len(message) == 4) or \
                        ('来点絢沙' in rev['raw_message'] and len(message) == 4) or \
                        ('来点岛村绚沙' in rev['raw_message']and len(message) == 6):
                    i = random.randint(10001, 10098)
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.eatBreadImage(user_id)
                    text = '吃掉了'
                    if text in responseText:
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:at,qq={}] {}[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/ayasa/{}.jpg]'.format(user_id, responseText, i)})
                    else:
                        send_msg({'msg_type': 'group', 'number': group,'msg': '[CQ:at,qq={}] {}'.format(user_id, responseText)})

                elif ('来点直田姬奈' in rev['raw_message']and len(message) == 6) or\
                        ('来点姬奈' in rev['raw_message'] and len(message) == 4):
                    i = random.randint(10001, 10065)
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.eatBreadImage(user_id)
                    text = '吃掉了'
                    if text in responseText:
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:at,qq={}] {}[CQ:image,file=file:///C:/Users/yudong/Documents/study/cse2231/workspace/nnm_bot/public/toko/{}.jpg]'.format(user_id, responseText, i)})
                    else:
                        send_msg({'msg_type': 'group', 'number': group,'msg': '[CQ:at,qq={}] {}'.format(user_id, responseText)})

                elif on_suffix(message, '是谁'):
                    name = get_suffix(message, '是谁')
                    index, responseText = nickname.search(name)
                    # 写成相对路径
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'character', '{}.png'.format(index))
                    msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                    send_group(group, msg)

                # 这一块结合module/cv_nickname，就可以替代繁杂的判断
                # cv_nickname返回一个角色编号index，支持模糊查询
                # 之后只需要维护那个json，以及放入对应编号的人物图片就好了
                
                # elif on_prefix(message, '来点'):
                #     name = get_prefix(message, '来点')
                #     index, guessText = cv_nickname.search(name)
                #     print(index, guessText)
                #     responseText = guessText + buy_bread.eatBreadImage(user_id)
                #     text = '吃掉了'
                #     if text in responseText:
                #         # 此处需要修改路径，修改图片编号
                #         msg = '[CQ:at,qq={}] {}\n[CQ:image,file={}.jpg]'.format(user_id, responseText, index)
                #         send_group(group, msg)
                #     else:
                #         msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                #         send_group(group, msg)

        else:
            continue
    else:
        continue