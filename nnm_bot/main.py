import datetime
import time
from module.musicScoreEasy import musicScoreEasy
from module.musicScoreHard.musicScoreHardEx import musicScoreHardEx
from module.musicScoreHard.musicScoreHardSp import musicScoreHardSp
from module.musicScoreNormal.musicScoreNormalEx import musicScoreNormalEx
from module.musicScoreNormal.musicScoreNormalSp import musicScoreNormalSp
from util.receiver import rev_msg
from util.sender import *
from util.trigger import *
from util.parser import *
import random
from bs4 import BeautifulSoup
import requests, os
from module.buy_bread import buy_bread
from module.nickname import nickname
from module.musicScore import musicScore
from module.musicScoreSp import musicScoreSp
from module.cv_nickname import cv_nickname
import re

qq_robot = eval(input('请输入机器人QQ号：'))
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}

img_list1 = []
img_list2 = []


def timePass(time1, time2):
    d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + time1, '%Y-%m-%d%H:%M')
    d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + time2, '%Y-%m-%d%H:%M')
    n_time = datetime.datetime.now()
    if n_time > d_time and n_time < d_time1:
        return True
    else:
        return False


def get_img_list(key):
    img_list = []
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
    img_list = []
    for j in [0, 24, 48, 72, 96, 120]:
        url = requests.get('https://www.duitang.com/search/?kw={}&type=feed&start={}'.format(key, j))
        # url.encoding = 'utf-8'
        html = url.text
        soup = BeautifulSoup(html, 'html.parser')
        movie = soup.find_all('div', class_='mbpho')
        for i in movie:
            imgsrc = i.find_all('img')[0].get('src')
            img_list.append(imgsrc)
    return img_list


img_list1 = get_img_list('bang_dream')
img_list2 = get_img_list1('二次元')

id_list = []

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
            message = rev['raw_message']
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
                path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                    'q{}.png'.format(i))
                msg = '[CQ:image,file=file:///{}]'.format(path)
                send_group(group, msg)

            elif "[CQ:at,qq={}]".format(qq_robot) in rev["raw_message"]:
                try:
                    # 如果单独@，不追加任何消息，会触发list index out of range
                    message = rev['raw_message'].split(' ')[1]
                except:
                    continue

                if on_fullmatch(message, '买面包'):
                    msg = '买面包'
                    send_group(group, msg)

                # 改
                elif on_fullmatch(message, 'help') or on_fullmatch(message, '使用说明'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q54.jpg')
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '七深') or on_fullmatch(message, 'nnm') or on_fullmatch(message, 'nanami') or \
                        on_fullmatch(message, '广町七深'):
                    msg = '找七深有什么事吗'
                    send_group(group, msg)

                elif on_fullmatch(message, '骂我'):
                    msg = '八嘎変態无路赛'
                    send_group(group, msg)

                elif on_fullmatch(message, '买nnm'):
                    msg = '不可以买七深哦'
                    send_group(group, msg)

                elif on_fullmatch(message, '卖nnm'):
                    msg = 'nnm是非卖品哦'
                    send_group(group, msg)

                # 改
                elif on_fullmatch(message, 'toko') or on_fullmatch(message, '透子'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '和透子还有morfonica演奏的日子每天都很开心'})

                elif on_fullmatch(message, '早上好') or on_fullmatch(message, '早')\
                        or on_fullmatch(message, '早安'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '早上好！今天也要过普通的一天哟！'})

                elif on_fullmatch(message, '晚安') or on_fullmatch(message, '睡觉'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '晚安！做个好梦'})

                elif on_fullmatch(message, '可爱'):
                    i = random.randint(7, 9)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '看看你的'):
                    i = random.randint(11, 12)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)


                elif on_fullmatch(message, '老婆'):
                    i = random.randint(14, 18)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '贴贴'):
                    i = random.randint(28, 31)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '亲亲'):
                    i = random.randint(32, 33)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '爬') or on_fullmatch(message, '快爬'):
                    i = random.randint(34, 35)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '来点普通的邦邦日常'):
                    try:
                        url = img_list1[random.randint(0, len(img_list1))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '这张图好像不太普通哟'})

                elif on_fullmatch(message, '来点纸片人') or on_fullmatch(message, '来点二次元'):
                    try:
                        url = img_list2[random.randint(0, len(img_list2))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '这张图好像不太普通哟'})

                elif on_fullmatch(message, '少女漫画') or on_fullmatch(message, '四格漫画'):
                    try:
                        i = random.randint(1, 245)
                        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'public',
                                            '{}.jpg'.format(i))
                        msg = '[CQ:image,file=file:///{}]'.format(path)
                        send_group(group, msg)
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': 'nnm也还没有看到漫画内容呢~'})

                elif on_fullmatch(message, '二次元测试'):
                    qq = rev['sender']['user_id']
                    i = random.randint(0, 4)
                    j = random.randint(0, 6)
                    k = random.randint(0, 1)
                    type1 = ['圆脸', '椭圆型脸', '方形脸', '长方形脸', '长脸']
                    face = type1[i]
                    height = random.randint(160, 200)
                    type2 = ['双马尾', '麻花辫', '长发', '短发', '杀马特']
                    hair = type2[i]
                    type3 = ['红', '橙', '粉', '绿', '黄', '蓝', '紫']
                    color = type3[j]
                    type4 = ['A', 'B', 'C', 'D', 'E']
                    cup = type4[i]
                    type5 = ['傲娇', '腹黑', '三无', '萌', '病娇']
                    char = type5[i]
                    type6 = ['偶像', '笨蛋', '千金小姐', '网瘾少女', '打工人']
                    identity = type6[i]
                    type7 = ['浅', '深']
                    ds = type7[k]

                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:at,qq={}] 二次元的你,长着{},身高{}，{}{}{}，{}cup, 瞳色{}色,{}, 是{}'
                             .format(qq, face, height, ds, color, hair, cup, color, char, identity)})

            else:

                if on_fullmatch(message, '成分查询') or on_fullmatch(message, '群友成分'):
                    msg = 'nnm认为群友成分过于复杂， 内部错误！'
                    send_group(group, msg)

                elif on_fullmatch(message, '来点wlp'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': 'nnm也很喜欢哟'})

                elif on_fullmatch(message, 'nnm买面包'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '买面包'})

                elif on_fullmatch(message, '查卡msr') or on_fullmatch(message, '查卡真白'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '小真白真可爱~'})

                elif on_fullmatch(message, '查卡947'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '普通路过的邪神日菜酱'})

                elif on_prefix(message, '抽卡模拟'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': 'nnm希望你有好运哦'})

                elif on_fullmatch(message, '邪神'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '查卡947'})

                elif on_fullmatch(message, 'nnm'):
                    i = random.randint(0, 25)
                    if i == 0:
                        msg = ' nnm一直想了解什么是普通，是害怕又变回独自一人，想要融入大家，想要跟大家一起去体验青春。现在nnm明白了，' \
                              '其实自己想知道的答案不就在摔倒之后的前方吗？' \
                              '从始至终nnm追寻的都不是什么普通，而是可以信赖和依靠的同伴，是知道我的秘密也会不离不弃的羁绊。其实这些nnm早就拥有了这些宝物了。' \
                              '从现在起不会再隐藏自己了，要向最喜欢的乐队成员展现nnm最耀眼美好的那一面，这就是告别过去懦弱的我，和大家一起看闪耀景色的决心。' \
                              '谢谢大家在nnm最迷茫的时候拯救了我，这些由我和大家友谊组成并且不会随时间褪色的画面会被nnm当作最珍贵的宝物永远守护在心底。'
                        send_group(group, msg)
                    else:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '找七深有什么事吗'})

                elif on_fullmatch(message, '机票模拟') or on_fullmatch(message, '必四模拟') or on_fullmatch(message, '必三模拟'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '七深收集的米歇鲁贴纸又多起来了~'})

                elif on_fullmatch(message, '查卡1385'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '一般路过的邪神lock酱'})

                elif on_fullmatch(message, '查卡1384'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '一般路过的邪神lisa酱'})

                elif on_fullmatch(message, '您') or on_fullmatch(message, '您您您'):
                    j = random.randint(0, 4)  # 加图片
                    if j == 0:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '和透子一样是天才呢'})
                    elif j == 1:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '您您您您'})
                    else:
                        i = random.randint(38, 40)
                        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                            'q{}.png'.format(i))
                        msg = '[CQ:image,file=file:///{}]'.format(path)
                        send_group(group, msg)

                elif on_fullmatch(message, 'nnm骂我'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '八嘎変態无路赛'})

                elif on_fullmatch(message, '买nnm'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '不可以买七深哦'})

                elif on_fullmatch(message, '买摩卡'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '买摩卡会赠送114514个赠品哦'})

                elif on_fullmatch(message, '买茨菇'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '记得要把买茨菇的赠品送给七深哟'})

                elif on_fullmatch(message, 'toko') \
                        or on_fullmatch(message, '透子'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '和透子还有morfonica演奏的日子每天都很开心!'})

                elif on_fullmatch(message, '害怕'):
                    i = random.randint(1, 3)
                    j = random.randint(0, 2)
                    if j == 0:
                        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                            'q{}.png'.format(i))
                        msg = '[CQ:image,file=file:///{}]'.format(path)
                        send_group(group, msg)
                    elif j == 1:
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '已经没什么好怕的了'})
                    else:
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '  もう何も怖くない'})

                elif on_fullmatch(message, '好耶'):
                    i = random.randint(4, 6)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '早上好') or on_fullmatch(message, '早') \
                        or on_fullmatch(message, '早安'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '早上好！今天也要过普通的一天哟！'})

                elif on_fullmatch(message, '晚安') or on_fullmatch(message, '睡觉') or on_fullmatch(message, '睡了'):
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '晚安！做个好梦!'})

                elif on_fullmatch(message, '哈卡奶') or on_fullmatch(message, '儚い') or on_fullmatch(message, '哈卡乃') or on_fullmatch(message, '哈卡奈'):
                    j = random.randint(0, 3)  # 加图片
                    if j == 0:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '哈卡奶'})
                    else:
                        i = random.randint(49, 51)
                        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                            'q{}.jpg'.format(i))
                        msg = '[CQ:image,file=file:///{}]'.format(path)
                        send_group(group, msg)

                elif on_fullmatch(message, '薰') or on_fullmatch(message, '濑田薰'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q52.jpg')
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif '小薰' in rev['raw_message']:
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '刚刚薰前辈来店里让我转告千圣前辈: 不要叫我小熏！'})

                elif on_fullmatch(message, '美竹兰') or on_fullmatch(message, '兰') or on_fullmatch(message, 'ran') or on_fullmatch(message, '红挑染'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q51.jpg')
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '一天放学，七深路过听到ykn前辈对兰前辈说“兰同学，你也不想以后摩卡没有面包吃吧？” 七深很好奇地问了强迫千圣同学来店里一起喝茶的薰同学。 可是薰同学却用着一些七深从未听过的表达， 像这样的情节如此梦幻啊，'
                                     '果然这就是命运的邂逅啊什么的，最后七深也没明白发生了什么。 不过薰同学那种说话方式才是最普通的说话方式吗？七深明天要不要也跟mornica的大家试试那种说话方式呢...'
                                     '[CQ:image,file=file:///{}]'.format(path)
                              })

                elif  on_fullmatch(message, '八潮瑠唯') or on_fullmatch(message, '瑠唯') or on_fullmatch(message, 'rui') or on_fullmatch(message, 'ruirui'):
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '唯唯昨天跟我说一天练习十小时以上是非常正常的一件事哦。 既然对于大家非常普通的事，那七深也要开始加油练习！'})

                elif on_fullmatch(message, '千圣') or on_fullmatch(message, '千圣同学') or on_fullmatch(message, 'cst'):
                    j = random.randint(0, 1)
                    if j == 0:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '千圣同学这里遇到你真是命运的安排，多么梦幻啊！怎么了千圣前辈，这是薰前辈教我的普通说话方式，难道有什么问题吗?'})
                    else:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '我可爱的千圣同学，不要这么冷漠，和我一起吃晚餐是多么梦幻的一件事啊！原来这就是普通的表达方式啊，千圣前辈的怎么了，怎么脸色有点难看?'})

                elif on_fullmatch(message, '花音') or on_fullmatch(message, 'kanon') or on_fullmatch(message, '水母'):
                    j = random.randint(0, 3)
                    if j == 0:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '薰: cst和你在一起，那我呢？'})
                    else:
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '第一次，有了喜欢的人，还得到了一生的挚友，两份喜悦相互重叠，这双重的喜悦又带来了更多更多的'
                                         '喜悦。本应已经得到了梦幻一般的幸福时光，然而，为什么，她和你在一起。是我，是我先，明明都是我先来'
                                         '的，接吻也好，拥抱也好，还是喜欢上那家伙也好。那我，就选择永远留在你身边。…即便，需要我舍弃所有的一切也好。'
                                         '恋爱的伤痛，要用恋爱来治愈。如果一旦说爱你的话，你就会变成这世界上最重要的人了！一旦抱住你，就绝对再也不会放手了啊！'})

                elif on_fullmatch(message, 'ksm'):
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': 'nnm也不知道ksm学姐追求的kirakira dokidoki是不是普通，但nnm稍微可以理解ksm学姐了呢。'
                                     '因为这也是monica所追求的地方，我也希望有一天能和大家站在那个向往不已而又充满魅力的舞台上聆听心灵的悸动，'
                                     '和所有成员一起前往那个令梦想闪闪发光的场所。'
                                     '所以学姐一起加油吧，坐上未来列车去享受旅途中的每一个风景，去阅读和成员一起谱写的友谊的华丽乐章，'
                                     '即便是因为看向湿润一千次天空而迷茫时，也永远要不要忘记和最喜欢的大家一起相处的时光和'
                                     '那份永远不会令人迷失的星之鼓动吧！'})  # 发病小作文

                elif on_fullmatch(message, '蝶组') or on_fullmatch(message, 'mornica') or on_fullmatch(message,'morfornica') or on_fullmatch( message, '毛二力') \
                        or on_fullmatch(message, '蝶团') or on_fullmatch(message, '蝶'):
                    i = random.randint(0, 1)
                    if i == 0:
                        msg = ' nnm一直想了解什么是普通，是害怕又变回独自一人，想要融入大家，想要跟大家一起去体验青春。现在nnm明白了，\n' \
                              '其实我从始至终追寻的都不是什么普通，而是可以信赖和依靠的同伴，是知道我的秘密也会不离不弃的羁绊。其实这些nnm早就拥有了这些宝物了。\n' \
                              '从现在起不会再隐藏自己了，要向最喜欢的乐队成员展现nnm最耀眼美好的那一面，这就是告别过去懦弱的我，向未来踏出坚定的一步的决心。\n' \
                              '谢谢大家在nnm最迷茫的时候拯救了我，这些由我和大家友谊组成并且不会随时间褪色的画面会被nnm当作最珍贵的宝物永远守护在心底。'
                        send_group(group, msg)
                    else:
                        msg = '太阳落下后的昏暗夜晚内心唯剩劣等感 \n每每心中翻涌憧憬的梦想都会伸出双手 \n终于在这互相纠缠的命运中感受到了温暖 \n我们一同欢笑哭泣交织出属于你我的歌声若你能宽恕\n' \
                              '不复从前的我就请你让我 用尽余生陪伴在你身旁 \n我们每一人都是不可或缺的存在你于我来说就是必要的存在希望与绝望并存 痛伤自己后又再将自己拥入怀中不断重复以往\n' \
                              '我现在正骄傲地站在起跑线上怯怕着焦急着期望着能被光芒照耀我已知晓 这世间一切都在渐渐改变 \n我们已经没有退路无法回到最初不论会有多么沉重的\n' \
                              '代价在等待着我们我都不愿离开大家身旁似在呼唤身后的双翼一般坚信心中祈愿展翅飞向天空我感受到细微的阳光\n' \
                              '挥洒照耀在脸颊上 零落的泪水透出丝丝温暖我多希望能一如此时 \n伙伴围绕身旁直到永远 \n\n                      --致最爱的morfornica'
                        send_group(group, msg)


                elif on_fullmatch(message, 'help') or on_fullmatch(message, '使用说明') or on_fullmatch(message, '菜单'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q54.jpg')
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_prefix(message, 'nnm决定'):
                    qq = rev['sender']['user_id']
                    if len(message) == 5:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '请输入决策内容'})
                    else:
                        i = random.randint(0, 1)
                        if i == 0:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq={}]我的答案是YES'.format(qq)})
                        else:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:at,qq={}]我的答案是NO'.format(qq)})

                elif on_fullmatch(message, '二次元测试'):
                    qq = rev['sender']['user_id']
                    i = random.randint(0, 4)
                    w = random.randint(0, 4)
                    e = random.randint(0, 4)
                    r = random.randint(0, 4)
                    j = random.randint(0, 6)
                    q = random.randint(0, 6)
                    k = random.randint(0, 1)
                    type1 = ['圆脸', '椭圆型脸', '方形脸', '长方形脸', '长脸']
                    face = type1[i]
                    height = random.randint(140, 170)
                    type2 = ['双马尾', '麻花辫', '长发', '短发', '杀马特']
                    hair = type2[w]
                    type3 = ['红', '橙', '粉', '绿', '青', '蓝', '紫']
                    color = type3[j]
                    eye = type3[q]
                    type4 = ['A', 'B', 'C', 'D', 'E']
                    cup = type4[w]
                    type5 = ['傲娇', '腹黑', '三无', '萌', '病娇']
                    char = type5[e]
                    type6 = ['偶像', '笨蛋', '千金小姐', '网瘾少女', '打工人']
                    identity = type6[r]
                    type7 = ['浅', '深']
                    ds = type7[k]
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:at,qq={}] 二次元的你,长着{},身高{}，{}{}{}，{}cup, 瞳色{}色,{}属性, 是{}'
                             .format(qq, face, height, ds, color, hair, cup, eye, char, identity)})


                elif on_fullmatch(message, 'nnm可爱'):
                    i = random.randint(7, 9)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '寄'):
                    i = random.randint(0, 2)
                    if i == 1:
                        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                            'q10.png')
                        msg = '[CQ:image,file=file:///{}]'.format(path)
                        send_group(group, msg)
                    elif i == 2:
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '不要停下来啊！只要不停下来，道路就会不断延续'})
                    else:
                        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                            'q53.jpg')
                        msg = '[CQ:image,file=file:///{}]'.format(path)
                        send_group(group, msg)

                elif on_fullmatch(message, 'nnm看看你的'):
                    i = random.randint(11, 12)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '草'):
                    j = random.randint(0, 2)
                    if j == 0:
                        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                            'q13.png')
                        msg = '[CQ:image,file=file:///{}]'.format(path)
                        send_group(group, msg)
                    elif j == 1:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': 'ww'})
                    elif j == 2:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '草生'})

                elif on_fullmatch(message, 'nnm老婆'):
                    i = random.randint(14, 18)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '润') or on_fullmatch(message, '润了') or on_fullmatch(message, '我先润了'):
                    i = random.randint(19, 21)
                    j = random.randint(0, 3)
                    if j == 0:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '这个邦多利炸梦趴体我是一秒也待不下去了'})
                    else:
                        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                            'q{}.png'.format(i))
                        msg = '[CQ:image,file=file:///{}]'.format(path)
                        send_group(group, msg)

                elif on_fullmatch(message, '谢谢') or on_fullmatch(message, '谢谢你'):
                    i = random.randint(22, 23)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '茨菇寄了'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q24.png')
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '摩卡寄了'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q25.png')
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '茨菇老婆'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q26.png')
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '摩卡老婆'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q27.png')
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, 'nnm贴贴'):
                    i = random.randint(28, 31)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)
                elif on_fullmatch(message, 'nnm亲亲'):
                    i = random.randint(32, 33)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, 'nnm爬'):
                    i = random.randint(34, 35)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q{}.png'.format(i))
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '茨菇可爱'):
                    qq = 3605447298
                    send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:poke,qq={}]'.format(qq)})

                elif on_fullmatch(message, 'ycm') or on_fullmatch(message, '有车没') or on_fullmatch(message, '有车吗'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q36.png')
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '女同好'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q41.png')
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '？') or on_fullmatch(message, '?') or on_fullmatch(message, '？？？') or on_fullmatch(message, '???'):
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'emoji',
                                        'q37.png')
                    msg = '[CQ:image,file=file:///{}]'.format(path)
                    send_group(group, msg)

                elif on_fullmatch(message, '来点普通的邦邦日常'):
                    try:
                        url = img_list1[random.randint(0, len(img_list1))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '这张图好像不太普通哟'})

                elif on_fullmatch(message, '来点纸片人') or on_fullmatch(message, '来点二次元'):
                    try:
                        url = img_list2[random.randint(0, len(img_list2))]
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '[CQ:image,file={}]'.format(url)})
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '这张图好像不太普通哟'})

                elif on_fullmatch(message, '四格漫画') or on_fullmatch(message, '少女漫画'):
                    try:
                        i = random.randint(1, 245)
                        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'public',
                                            '{}.jpg'.format(i))
                        msg = '[CQ:image,file=file:///{}]'.format(path)
                        send_group(group, msg)
                    except:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': 'nnm也还没有看到漫画内容呢~'})

                elif on_fullmatch(message, '买甜点'):
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.buyBread(user_id)
                    send_msg({'msg_type': 'group', 'number': group,
                                'msg': '[CQ:at,qq={}] {}'
                                .format(user_id, responseText)})

                elif on_fullmatch(message, '查甜点'):
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.myBread(user_id)
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:at,qq={}] {}'
                             .format(user_id, responseText)})

                elif on_fullmatch(message, '吃甜点'):
                    user_id = rev['sender']['user_id']
                    responseText = buy_bread.eatBread(user_id)
                    send_msg({'msg_type': 'group', 'number': group,
                              'msg': '[CQ:at,qq={}] {}'
                             .format(user_id, responseText)})

                elif rev['raw_message'].startswith('抢甜点'):
                    user_id = rev['sender']['user_id']
                    # 正则表达式，匹配CQ:at,qq=开头的数字
                    # 当然如果有人手动发送那就没办法了，暂时先这样
                    object_id = re.search('(?<=CQ:at,qq=)\d+\.?\d*', rev['raw_message'])

                    if (object_id is None):
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



                elif rev['raw_message'].startswith('透') or on_suffix(message, '透'):
                    user_id = rev['sender']['user_id']
                    object_id = re.search('(?<=CQ:at,qq=)\d+\.?\d*', rev['raw_message'])
                    if (object_id is None):
                        continue

                    elif "[CQ:at,qq={}]".format(int(object_id.group())) in rev["raw_message"]:
                        # 用group()获取匹配到的第一个对象，从str转换为int
                        object_id = int(object_id.group())
                        user_id = rev['sender']['nickname']
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '{}透了[CQ:at,qq={}]'
                                 .format(user_id, object_id)})

                elif rev['raw_message'].startswith('贴贴') or on_suffix(message, '贴贴'):
                    user_id = rev['sender']['user_id']
                    object_id = re.search('(?<=CQ:at,qq=)\d+\.?\d*', rev['raw_message'])
                    if (object_id is None):
                        continue

                    elif "[CQ:at,qq={}]".format(int(object_id.group())) in rev["raw_message"]:
                        # 用group()获取匹配到的第一个对象，从str转换为int
                        object_id = int(object_id.group())
                        user_id = rev['sender']['nickname']
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '{}和[CQ:at,qq={}]贴贴'
                                 .format(user_id, object_id)})

                elif on_prefix(message, '来点'):
                    name = get_prefix(message, '来点')
                    index, guessText = cv_nickname.search(name)
                    print(index, guessText)
                    if '可爱的灯酱' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            i = random.randint(1, 149)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'light', '{}.png'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif '项羽あいな' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(1, 145)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'roselia', 'i83', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)
                    elif '志崎桦音' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(1, 80)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'roselia', 'non', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif '工藤晴香' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(1, 104)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'roselia', 'kdhr', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif '明坂聡美' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(1, 4)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'roselia', 'xiaoming', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif '中島由貴' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(1, 113)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'roselia', 'yuuki', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif '远藤祐里香' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(1, 21)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'roselia', 'yrs', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif '樱川惠' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(1, 77)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'roselia', 'mgchi', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif '西尾夕香' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(10001, 10258)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'morfornica', 'yuuka', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif '进藤天音' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(10001, 10079)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'morfornica', 'msr', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif 'mika' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(10001, 10024)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'morfornica', 'mika', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif '岛村绚沙' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(10001, 10098)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'morfornica', 'ayasa', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)

                    elif '直田姬奈' in guessText:
                        responseText = guessText + ', ' + buy_bread.eatBreadImage(user_id)
                        text = '吃掉了'
                        if text in responseText:
                            # 此处需要修改路径，修改图片编号
                            i = random.randint(10001, 10063)
                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'nick_name',
                                                'morfornica', 'toko', '{}.jpg'.format(i))
                            msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                            send_group(group, msg)
                        else:
                            responseText = buy_bread.eatBreadImage(user_id)
                            msg = '[CQ:at,qq={}] {}'.format(user_id, responseText)
                            send_group(group, msg)


                elif on_suffix(message, '是谁'):
                    name = get_suffix(message, '是谁')
                    index, responseText = nickname.search(name)
                    # 写成相对路径
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'character',
                                        '{}.png'.format(index))
                    msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                    send_group(group, msg)

                elif on_suffix(message, '谱面模拟') or on_suffix(message, '谱面模拟ex') or on_suffix(message, '谱面模拟EX'):
                    if on_suffix(message, '谱面模拟'):
                        name = get_suffix(message, '谱面模拟')
                    elif on_suffix(message, '谱面模拟ex'):
                        name = get_suffix(message, '谱面模拟ex')
                    else:
                        name = get_suffix(message, '谱面模拟EX')
                    index, responseText = musicScore.search(name)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'musicScore',
                                        '{}.png'.format(index))
                    msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                    send_group(group, msg)

                elif on_suffix(message, '谱面模拟sp') or on_suffix(message, '谱面模拟SP'):
                    if on_suffix(message, '谱面模拟sp'):
                        name = get_suffix(message, '谱面模拟sp')
                    else:
                        name = get_suffix(message, '谱面模拟SP')
                    index, responseText = musicScoreSp.search(name)
                    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'imageOnHtml', 'musicScoreSp',
                                        '{}.png'.format(index))
                    msg = '[CQ:at,qq={}] {}\n[CQ:image,file=file:///{}]'.format(user_id, responseText, path)
                    send_group(group, msg)

                elif on_fullmatch(message, '谱面挑战') and (timePass('12:30', '18:30') == True or group == 820651903 or group == 164839398):
                    num = 0
                    msg = '请选择难度（easy/normal/hard/expert/special)(今天摸了，还没做计时，一定要手动放弃)'
                    send_group(group, msg)
                    while True:
                        try:
                            rev1 = rev_msg()
                            id1 = rev1['message_id']
                            if (len(id_list) >= 50):
                                id_list = []
                            if id1 not in id_list:
                                id_list.append(id1)
                            else:
                                continue
                        except:
                            continue
                        if rev1["post_type"] == "message":
                            if rev1["message_type"] == "group":
                                group1 = rev1['group_id']
                                user_id1 = rev1['sender']['user_id']
                                message1 = rev1['raw_message']
                                if message1 in rev1["raw_message"]:
                                    if group1 == group:
                                        if on_fullmatch(message1, 'hard'):
                                            responseText = '这是这首歌的谱面哦'
                                            i = random.randint(1, 100)
                                            r = random.randint(1, 25)
                                            k = random.randint(0, 3)
                                            if k != 3:
                                                path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                                    'imageOnHtml', 'musicScoreHard', 'musicScoreHardEx',
                                                                    '{}.png'.format(i))
                                                msg = '选择难度hard: 将从所有27以上ex和sp难度和一些的25和26难度的歌里选取, 答对可以获得10份甜点哦\n记得歌的结尾要加ex或者sp哦\n' \
                                                      'ps:没买过甜点不可以获得哦\n{}, 为ex难度\n[CQ:image,file=file:///{}]'.format(
                                                    responseText, path)
                                                send_group(group, msg)
                                            else:
                                                path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                                    'imageOnHtml', 'musicScoreHard', 'musicScoreHardSp',
                                                                    '{}.png'.format(r))
                                                msg = '选择难度hard: 将从所有27以上ex和sp难度和一些的25和26难度的歌里选取, 答对可以获得10份甜点哦\n记得歌的结尾要加ex或者sp哦\n' \
                                                      'ps:没买过甜点不可以获得哦\n{}，为sp难度\n[CQ:image,file=file:///{}]'.format(
                                                    responseText, path)
                                                send_group(group, msg)
                                            while True:
                                                try:
                                                    rev1 = rev_msg()
                                                    id1 = rev1['message_id']
                                                    if (len(id_list) >= 50):
                                                        id_list = []
                                                    if id1 not in id_list:
                                                        id_list.append(id1)
                                                    else:
                                                        continue
                                                except:
                                                    continue
                                                if rev1["post_type"] == "message":
                                                    if rev1["message_type"] == "group":
                                                        group1 = rev1['group_id']
                                                        user_id1 = rev1['sender']['user_id']
                                                        message1 = rev1['raw_message']
                                                        if message1 in rev1["raw_message"]:
                                                            if group1 == group:
                                                                if on_suffix(message1, 'ex'):
                                                                    name = get_suffix(message1, 'ex')
                                                                    index, responseText = musicScoreHardEx.search(name)
                                                                    if int(index) == i:
                                                                        responseText = buy_bread.BreadChallenge(
                                                                            user_id1, 10)
                                                                        send_msg({'msg_type': 'group', 'number': group,
                                                                                  'msg': '[CQ:at,qq={}]回答正确！ {}'
                                                                                 .format(user_id1, responseText)})
                                                                        break
                                                                    else:
                                                                        if num < 5:
                                                                            msg = '回答错误（如果不知道答案的话，可以输入放弃哦）'
                                                                            send_group(group, msg)
                                                                            num += 1
                                                                            continue
                                                                        else:
                                                                            if k != 3:
                                                                                musicName, responseText = musicScoreHardEx.get_musicName(
                                                                                    i)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的ex难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            elif k == 3:
                                                                                musicName, responseText = musicScoreHardSp.get_musicName(
                                                                                    r)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的sp难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            break
                                                                elif on_suffix(message1, 'sp'):
                                                                    name = get_suffix(message1, 'sp')
                                                                    index, responseText = musicScoreHardSp.search(name)
                                                                    if int(index) == r:
                                                                        responseText = buy_bread.BreadChallenge(
                                                                            user_id1, 10)
                                                                        send_msg({'msg_type': 'group', 'number': group,
                                                                                  'msg': '[CQ:at,qq={}]回答正确！ {}'
                                                                                 .format(user_id1, responseText)})
                                                                        break
                                                                    else:
                                                                        if num < 5:
                                                                            msg = '回答错误（如果不知道答案的话，可以输入放弃哦）'
                                                                            send_group(group, msg)
                                                                            num += 1
                                                                            continue
                                                                        else:
                                                                            if k != 3:
                                                                                musicName, responseText = musicScoreHardEx.get_musicName(
                                                                                    i)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的ex难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            elif k == 3:
                                                                                musicName, responseText = musicScoreHardSp.get_musicName(
                                                                                    r)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的sp难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            break
                                                                elif on_fullmatch(message1, '放弃'):
                                                                    if k != 3:
                                                                        musicName, responseText = musicScoreHardEx.get_musicName(
                                                                            i)
                                                                        msg = '已放弃, 这首歌的名字是{}的ex难度'.format(responseText)
                                                                        send_group(group, msg)
                                                                    elif k == 3:
                                                                        musicName, responseText = musicScoreHardSp.get_musicName(
                                                                            r)
                                                                        msg = '已放弃, 这首歌的名字是{}的sp难度'.format(responseText)
                                                                        send_group(group, msg)
                                                                    break
                                                                else:
                                                                    continue
                                                            else:
                                                                continue
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                else:
                                                    break

                                        elif on_fullmatch(message1, 'expert'):
                                            responseText = '这是这首歌的谱面哦'
                                            i = random.randint(1, 415)
                                            r = random.randint(1, 85)
                                            k = random.randint(0, 3)
                                            if k != 3:
                                                path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                                    'imageOnHtml', 'musicScore', '{}.png'.format(i))
                                                msg = '选择难度expert(无人生还): 将从所有歌里选取, 答对可以获得20份甜点哦\n记得歌的结尾要加ex或者sp哦\n' \
                                                      'ps:没买过甜点不可以获得哦\n{}, 为ex难度\n[CQ:image,file=file:///{}]'.format(
                                                    responseText, path)
                                                send_group(group, msg)
                                            else:
                                                path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                                    'imageOnHtml', 'musicScoreSp', '{}.png'.format(r))
                                                msg = '选择难度expert(无人生还): 将从所有歌里选取, 答对可以获得20份甜点哦\n记得歌的结尾要加ex或者sp哦\n' \
                                                      'ps:没买过甜点不可以获得哦\n{}，为sp难度\n[CQ:image,file=file:///{}]'.format(
                                                    responseText, path)
                                                send_group(group, msg)
                                            while True:
                                                try:
                                                    rev1 = rev_msg()
                                                    id1 = rev1['message_id']
                                                    if (len(id_list) >= 50):
                                                        id_list = []
                                                    if id1 not in id_list:
                                                        id_list.append(id1)
                                                    else:
                                                        continue
                                                except:
                                                    continue
                                                if rev1["post_type"] == "message":
                                                    if rev1["message_type"] == "group":
                                                        group1 = rev1['group_id']
                                                        user_id1 = rev1['sender']['user_id']
                                                        message1 = rev1['raw_message']
                                                        if message1 in rev1["raw_message"]:
                                                            if group1 == group:
                                                                if on_suffix(message1, 'ex'):
                                                                    name = get_suffix(message1, 'ex')
                                                                    index, responseText = musicScore.search(name)
                                                                    if int(index) == i:
                                                                        responseText = buy_bread.BreadChallenge(
                                                                            user_id1, 20)
                                                                        send_msg({'msg_type': 'group', 'number': group,
                                                                                  'msg': '[CQ:at,qq={}]回答正确！ {}'
                                                                                 .format(user_id1, responseText)})
                                                                        break
                                                                    else:
                                                                        if num < 5:
                                                                            msg = '回答错误（如果不知道答案的话，可以输入放弃哦）'
                                                                            send_group(group, msg)
                                                                            num += 1
                                                                            continue
                                                                        else:
                                                                            if k != 3:
                                                                                musicName, responseText = musicScore.get_musicName(
                                                                                    i)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的ex难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            elif k == 3:
                                                                                musicName, responseText = musicScoreSp.get_musicName(
                                                                                    r)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的sp难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            break
                                                                elif on_suffix(message1, 'sp'):
                                                                    name = get_suffix(message1, 'sp')
                                                                    index, responseText = musicScoreSp.search(name)
                                                                    if int(index) == r:
                                                                        responseText = buy_bread.BreadChallenge(
                                                                            user_id1, 20)
                                                                        send_msg({'msg_type': 'group', 'number': group,
                                                                                  'msg': '[CQ:at,qq={}]回答正确！ {}'
                                                                                 .format(user_id1, responseText)})
                                                                        break
                                                                    else:
                                                                        if num < 5:
                                                                            msg = '回答错误（如果不知道答案的话，可以输入放弃哦）'
                                                                            send_group(group, msg)
                                                                            num += 1
                                                                            continue
                                                                        else:
                                                                            if k != 3:
                                                                                musicName, responseText = musicScore.get_musicName(
                                                                                    i)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的ex难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            elif k == 3:
                                                                                musicName, responseText = musicScoreSp.get_musicName(
                                                                                    r)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的sp难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            break
                                                                elif on_fullmatch(message1, '放弃'):
                                                                    if k != 3:
                                                                        musicName, responseText = musicScore.get_musicName(
                                                                            i)
                                                                        msg = '已放弃, 这首歌的名字是{}的ex难度'.format(responseText)
                                                                        send_group(group, msg)
                                                                    elif k == 3:
                                                                        musicName, responseText = musicScoreSp.get_musicName(
                                                                            r)
                                                                        msg = '已放弃, 这首歌的名字是{}的sp难度'.format(responseText)
                                                                        send_group(group, msg)
                                                                    break
                                                                else:
                                                                    continue
                                                            else:
                                                                continue
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                else:
                                                    break

                                        elif on_fullmatch(message1, 'normal'):
                                            responseText = '这是这首歌的谱面哦'
                                            i = random.randint(1, 52)
                                            r = random.randint(1, 15)
                                            k = random.randint(0, 3)
                                            if k != 3:
                                                path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                                    'imageOnHtml', 'musicScoreNormal',
                                                                    'musicScoreNormalEx', '{}.png'.format(i))
                                                msg = '选择难度normal: 将从所有27以上ex和sp难度和国服所有带左右滑键sp的歌里选取, 答对可以获得5份甜点哦\n记得歌的结尾要加ex或者sp哦\n' \
                                                      'ps:没买过甜点不可以获得哦\n{}, 为ex难度\n[CQ:image,file=file:///{}]'.format(
                                                    responseText, path)
                                                send_group(group, msg)
                                            else:
                                                path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                                    'imageOnHtml', 'musicScoreNormal',
                                                                    'musicScoreNormalSp', '{}.png'.format(r))
                                                msg = '选择难度normal: 将从所有27以上ex和sp难度和国服所有带左右滑键sp的歌里选取, 答对可以获得5份甜点哦\n记得歌的结尾要加ex或者sp哦\n' \
                                                      'ps:没买过甜点不可以获得哦\n{}，为sp难度\n[CQ:image,file=file:///{}]'.format(
                                                    responseText, path)
                                                send_group(group, msg)
                                            while True:
                                                try:
                                                    rev1 = rev_msg()
                                                    id1 = rev1['message_id']
                                                    if (len(id_list) >= 50):
                                                        id_list = []
                                                    if id1 not in id_list:
                                                        id_list.append(id1)
                                                    else:
                                                        continue
                                                except:
                                                    continue
                                                if rev1["post_type"] == "message":
                                                    if rev1["message_type"] == "group":
                                                        group1 = rev1['group_id']
                                                        user_id1 = rev1['sender']['user_id']
                                                        message1 = rev1['raw_message']
                                                        if message1 in rev1["raw_message"]:
                                                            if group1 == group:
                                                                if on_suffix(message1, 'ex'):
                                                                    name = get_suffix(message1, 'ex')
                                                                    index, responseText = musicScoreNormalEx.search(
                                                                        name)
                                                                    if int(index) == i:
                                                                        responseText = buy_bread.BreadChallenge(
                                                                            user_id1, 5)
                                                                        send_msg({'msg_type': 'group', 'number': group,
                                                                                  'msg': '[CQ:at,qq={}]回答正确！ {}'
                                                                                 .format(user_id1, responseText)})
                                                                        break
                                                                    else:
                                                                        if num < 5:
                                                                            msg = '回答错误（如果不知道答案的话，可以输入放弃哦）'
                                                                            send_group(group, msg)
                                                                            num += 1
                                                                            continue
                                                                        else:
                                                                            if k != 3:
                                                                                musicName, responseText = musicScoreNormalEx.get_musicName(
                                                                                    i)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的ex难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            elif k == 3:
                                                                                musicName, responseText = musicScoreNormalSp.get_musicName(
                                                                                    r)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的sp难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            break
                                                                elif on_suffix(message1, 'sp'):
                                                                    name = get_suffix(message1, 'sp')
                                                                    index, responseText = musicScoreNormalSp.search(
                                                                        name)
                                                                    if int(index) == r:
                                                                        responseText = buy_bread.BreadChallenge(
                                                                            user_id1, 5)
                                                                        send_msg({'msg_type': 'group', 'number': group,
                                                                                  'msg': '[CQ:at,qq={}]回答正确！ {}'
                                                                                 .format(user_id1, responseText)})
                                                                        break
                                                                    else:
                                                                        if num < 5:
                                                                            msg = '回答错误（如果不知道答案的话，可以输入放弃哦）'
                                                                            send_group(group, msg)
                                                                            num += 1
                                                                            continue
                                                                        else:
                                                                            if k != 3:
                                                                                musicName, responseText = musicScoreNormalEx.get_musicName(
                                                                                    i)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的ex难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            elif k == 3:
                                                                                musicName, responseText = musicScoreNormalSp.get_musicName(
                                                                                    r)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的sp难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                            break
                                                                elif on_fullmatch(message1, '放弃'):
                                                                    if k != 3:
                                                                        musicName, responseText = musicScoreNormalEx.get_musicName(
                                                                            i)
                                                                        msg = '已放弃, 这首歌的名字是{}的ex难度'.format(responseText)
                                                                        send_group(group, msg)
                                                                    elif k == 3:
                                                                        musicName, responseText = musicScoreNormalSp.get_musicName(
                                                                            r)
                                                                        msg = '已放弃, 这首歌的名字是{}的sp难度'.format(responseText)
                                                                        send_group(group, msg)
                                                                    break
                                                                else:
                                                                    continue
                                                            else:
                                                                continue
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                else:
                                                    break

                                        elif on_fullmatch(message1, 'easy'):
                                            responseText = '这是这首歌的谱面哦'
                                            i = random.randint(1, 52)
                                            path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                                'imageOnHtml', 'musicScoreEasy', '{}.png'.format(i))
                                            msg = '选择难度easy: 将从所有27以上ex难度的歌里选取,记得歌的结尾要加ex或者sp哦\n' \
                                                  ' 答对可以获得3份甜点哦\nps:没买过甜点不可以获得哦\n{}\n[CQ:image,file=file:///{}]'.format(
                                                responseText, path)
                                            send_group(group, msg)
                                            while True:
                                                try:
                                                    rev1 = rev_msg()
                                                    id1 = rev1['message_id']
                                                    if (len(id_list) >= 50):
                                                        id_list = []
                                                    if id1 not in id_list:
                                                        id_list.append(id1)
                                                    else:
                                                        continue
                                                except:
                                                    continue
                                                if rev1["post_type"] == "message":
                                                    if rev1["message_type"] == "group":
                                                        group1 = rev1['group_id']
                                                        user_id1 = rev1['sender']['user_id']
                                                        message1 = rev1['raw_message']
                                                        if message1 in rev1["raw_message"]:
                                                            if group1 == group:
                                                                if on_suffix(message1, 'ex') or on_fullmatch(message1,
                                                                                                             '放弃'):
                                                                    if on_suffix(message1, 'ex'):
                                                                        name = get_suffix(message1, 'ex')
                                                                        index, responseText = musicScoreEasy.search(
                                                                            name)
                                                                        if int(index) == i:
                                                                            responseText = buy_bread.BreadChallenge(
                                                                                user_id1, 3)
                                                                            send_msg(
                                                                                {'msg_type': 'group', 'number': group,
                                                                                 'msg': '[CQ:at,qq={}]回答正确！ {}'
                                                                                 .format(user_id1, responseText)})
                                                                            break
                                                                        else:
                                                                            if num < 5:
                                                                                msg = '回答错误（如果不知道答案的话，可以输入放弃哦）'
                                                                                send_group(group, msg)
                                                                                num += 1
                                                                                continue
                                                                            else:
                                                                                musicName, responseText = musicScoreEasy.get_musicName(
                                                                                    i)
                                                                                msg = '你已回答错误超过5次，挑战结束！这首歌的名字是{}的ex难度'.format(
                                                                                    responseText)
                                                                                send_group(group, msg)
                                                                                break

                                                                    else:
                                                                        musicName, responseText = musicScoreEasy.get_musicName(
                                                                            i)
                                                                        msg = '已放弃, {}'.format(responseText)
                                                                        send_group(group, msg)
                                                                        break

                                                                else:
                                                                    continue

                                                            else:
                                                                continue
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                else:
                                                    break

                                        elif on_fullmatch(message1, 'special'):
                                            responseText = '这是这首歌的谱面哦'
                                            i = random.randint(1, 415)
                                            r = random.randint(1, 85)
                                            k = random.randint(0, 3)
                                            x = 0
                                            n = 1
                                            option = ['A', 'B', 'C', 'D', 'E']
                                            answer = []
                                            if k != 3:
                                                musicName, text = musicScore.get_musicName(i)
                                                answer.append(musicName)
                                                while x < 4:
                                                    m = random.randint(1, 415)
                                                    musicName, text = musicScore.get_musicName(m)
                                                    answer.append(musicName)
                                                    x += 1
                                            else:
                                                musicName, text = musicScoreSp.get_musicName(r)
                                                answer.append(musicName)
                                                while x < 4:
                                                    m = random.randint(1, 85)
                                                    musicName, text = musicScoreSp.get_musicName(m)
                                                    answer.append(musicName)
                                                    x += 1
                                            random.shuffle(answer)

                                            if k != 3:
                                                path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                                    'imageOnHtml', 'musicScore', '{}.png'.format(i))
                                                msg = '选择难度special: 将从所有歌曲里选择并给出选项进行选择, 答对可以获得5份甜点哦\n' \
                                                      'ps:没买过甜点不可以获得哦\n{}, 为ex难度,记得选项前加答案两个字哦\n[CQ:image,file=file:///{}]\n\n' \
                                                      '{} {}\n{} {}\n{} {}\n{} {}\n{} {}\n'.format(responseText, path,
                                                                                                   option[0], answer[0],
                                                                                                   option[1], answer[1],
                                                                                                   option[2], answer[2],
                                                                                                   option[3], answer[3],
                                                                                                   option[4], answer[4])
                                                send_group(group, msg)
                                            else:
                                                path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                                    'imageOnHtml', 'musicScoreSp', '{}.png'.format(r))
                                                msg = '选择难度special: 将从所有歌曲里选择并给出选项进行选择, 答对可以获得5份甜点哦\n' \
                                                      'ps:没买过甜点不可以获得哦\n{}，为sp难度\n[CQ:image,file=file:///{}]\n\n' \
                                                      '{} {}\n{} {}\n{} {}\n{} {}\n{} {}\n'.format(responseText, path,
                                                                                                   option[0], answer[0],
                                                                                                   option[1], answer[1],
                                                                                                   option[2], answer[2],
                                                                                                   option[3], answer[3],
                                                                                                   option[4], answer[4])
                                                send_group(group, msg)
                                            while True:
                                                try:
                                                    rev1 = rev_msg()
                                                    id1 = rev1['message_id']
                                                    if (len(id_list) >= 50):
                                                        id_list = []
                                                    if id1 not in id_list:
                                                        id_list.append(id1)
                                                    else:
                                                        continue
                                                except:
                                                    continue
                                                if rev1["post_type"] == "message":
                                                    if rev1["message_type"] == "group":
                                                        group1 = rev1['group_id']
                                                        user_id1 = rev1['sender']['user_id']
                                                        message1 = rev1['raw_message']
                                                        if message1 in rev1["raw_message"]:
                                                            if group1 == group:
                                                                if k != 3:
                                                                    if on_prefix(message1, '答案'):
                                                                        name = get_prefix(message1, '答案')
                                                                        name = name.upper()
                                                                        print(name)
                                                                        number = 5
                                                                        musicName, text = musicScore.get_musicName(i)
                                                                        for num in range(0, 4):
                                                                            if name == option[num]:
                                                                                number = num
                                                                                break
                                                                            else:
                                                                                num += 1
                                                                        print(num)
                                                                        if number != 5 and musicName == answer[number]:
                                                                            print(answer[number])
                                                                            responseText = buy_bread.BreadChallenge(
                                                                                user_id1, 5)
                                                                            send_msg(
                                                                                {'msg_type': 'group', 'number': group,
                                                                                 'msg': '[CQ:at,qq={}]回答正确！ {}'
                                                                                .format(user_id1, responseText)})
                                                                            break
                                                                        else:
                                                                            if n < 3:
                                                                                msg = '回答错误（如果不知道答案的话，可以输入放弃哦）'
                                                                                send_group(group, msg)
                                                                                n += 1
                                                                                continue
                                                                            else:
                                                                                if k != 3:
                                                                                    musicName, responseText = musicScore.get_musicName(
                                                                                        i)
                                                                                    msg = '你已回答错误超过3次，挑战结束！这首歌的名字是{}的ex难度'.format(
                                                                                        responseText)
                                                                                    send_group(group, msg)
                                                                                elif k == 3:
                                                                                    musicName, responseText = musicScoreSp.get_musicName(
                                                                                        r)
                                                                                    msg = '你已回答错误超过3次，挑战结束！这首歌的名字是{}的sp难度'.format(
                                                                                        responseText)
                                                                                    send_group(group, msg)
                                                                                break
                                                                    elif on_fullmatch(message1, '放弃'):
                                                                        if k != 3:
                                                                            musicName, responseText = musicScore.get_musicName(
                                                                                i)
                                                                            msg = '已放弃, 这首歌的名字是{}的ex难度'.format(
                                                                                responseText)
                                                                            send_group(group, msg)
                                                                        elif k == 3:
                                                                            musicName, responseText = musicScoreSp.get_musicName(
                                                                                r)
                                                                            msg = '已放弃, 这首歌的名字是{}的sp难度'.format(
                                                                                responseText)
                                                                            send_group(group, msg)
                                                                        break
                                                                    else:
                                                                        continue

                                                                if k == 3:
                                                                    if on_prefix(message1, '答案'):
                                                                        name = get_prefix(message1, '答案')
                                                                        name = name.upper()
                                                                        print(name)
                                                                        number = 5
                                                                        musicName, text = musicScoreSp.get_musicName(r)
                                                                        for num in range(0, 4):
                                                                            if name == option[num]:
                                                                                number = num
                                                                                break
                                                                            else:
                                                                                num += 1
                                                                        print(num)

                                                                        if number != 5 and musicName == answer[number]:
                                                                            print(answer[number])
                                                                            responseText = buy_bread.BreadChallenge(
                                                                                user_id1, 5)
                                                                            send_msg(
                                                                                {'msg_type': 'group', 'number': group,
                                                                                 'msg': '[CQ:at,qq={}]回答正确！ {}'
                                                                                .format(user_id1, responseText)})
                                                                            break
                                                                        else:
                                                                            if n < 3:
                                                                                msg = '回答错误（如果不知道答案的话，可以输入放弃哦）'
                                                                                send_group(group, msg)
                                                                                n += 1
                                                                                continue
                                                                            else:
                                                                                if k != 3:
                                                                                    musicName, responseText = musicScore.get_musicName(
                                                                                        i)
                                                                                    msg = '你已回答错误超过3次，挑战结束！这首歌的名字是{}的ex难度'.format(
                                                                                        responseText)
                                                                                    send_group(group, msg)
                                                                                elif k == 3:
                                                                                    musicName, responseText = musicScoreSp.get_musicName(
                                                                                        r)
                                                                                    msg = '你已回答错误超过3次，挑战结束！这首歌的名字是{}的sp难度'.format(
                                                                                        responseText)
                                                                                    send_group(group, msg)
                                                                                break

                                                                    elif on_fullmatch(message1, '放弃'):
                                                                        if k != 3:
                                                                            musicName, responseText = musicScore.get_musicName(
                                                                                i)
                                                                            msg = '已放弃, 这首歌的名字是{}的ex难度'.format(
                                                                                responseText)
                                                                            send_group(group, msg)
                                                                        elif k == 3:
                                                                            musicName, responseText = musicScoreSp.get_musicName(
                                                                                r)
                                                                            msg = '已放弃, 这首歌的名字是{}的sp难度'.format(
                                                                                responseText)
                                                                            send_group(group, msg)
                                                                        break
                                                                    else:
                                                                        continue
                                                                else:
                                                                    continue
                                                            else:
                                                                continue
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                else:
                                                    break

                                        else:
                                            continue
                                    else:
                                        continue
                                else:
                                    break
                            else:
                                break
                        else:
                            break
                        break

        else:
            continue
    else:
        continue
