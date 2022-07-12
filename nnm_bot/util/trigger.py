# 用于判断消息是否触发规则
# 定义了几个常用的判断规则
# 输入的参数详见标识，返回类型全部是bool，可以直接用于判断
# 所有未处理的message都会被去掉开头和结尾的空格再进行处理

# 消息是否以关键字开头
def on_prefix(msg : str, keyword : str) -> bool:
    try:
        msg = msg.strip()
        return msg.startswith(keyword)
    except Exception as e:
        print('on_prefix error:' + str(e))

# 消息是否以关键字结尾
def on_suffix(msg : str, keyword : str) -> bool:
    try:
        msg = msg.strip()
        return msg.endswith(keyword)
    except Exception as e:
        print('on_suffix error:' + str(e))

# 消息中是否包含关键字
def on_keyword(msg : str, keyword : str) -> bool:
    try:
        msg = msg.strip()
        return keyword in msg
    except Exception as e:
        print('on_keyword error:' + str(e))

# 消息与关键字是否完全相等
def on_fullmatch(msg : str, keyword : str) -> bool:
    try:
        msg = msg.strip()
        return msg == keyword
    except Exception as e:
        print('on_fullmatch error:' + str(e))

# 消息是否以@Bot开头
def on_atbot_prefix(msg : str, bot_id : int | str) -> bool:
    try:
        msg = msg.strip()
        return msg.startswith('[CQ:at,qq={}]'.format(bot_id))
    except Exception as e:
        print('on_atbot_prefix error:' + str(e))

# 消息中是否包含@Bot
def on_atbot_keyword(msg : str, bot_id : int | str) -> bool:
    try:
        msg = msg.strip()
        return '[CQ:at,qq={}]'.format(bot_id) in msg
    except Exception as e:
        print('on_atbot_prefix error:' + str(e))
        