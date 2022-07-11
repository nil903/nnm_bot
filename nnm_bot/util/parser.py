import re
# 所有message都会被去掉开头和结尾的空格!

# 获得关键字开头之后的语句
# 务必结合on_prefix使用，否则值可能不对
def get_prefix(msg : str, keyword : str) -> str:
    try:
        msg = msg.strip()
        start = len(keyword)
        end = len(msg)
        return msg[start : end]
    except Exception as e:
        print('get_prefix error:' + str(e))

# 获得关键字结尾之前的语句
# 务必结合on_suffix使用，否则值可能不对
def get_suffix(msg : str, keyword : str) -> str:
    try:
        msg = msg.strip()
        start = 0
        end = len(msg) - len(keyword)
        return msg[start : end]
    except Exception as e:
        print('get_suffix error:' + str(e))

# 获得@Bot开头之后的语句
# 务必结合on_atbot_prefix使用，否则值可能不对
def get_atbot_prefix(msg : str, bot_id: int | str) -> str:
    try:
        msg = msg.strip()
        start = len('[CQ:at,qq={}]'.format(bot_id)) + 1
        end = len(msg)
        return msg[start : end]
    except Exception as e:
        print('get_atbot_prefix error:' + str(e))

# 获得@某人的QQ号，暂时不可以结合@Bot使用
# 正则表达式匹配第一个CQ:at,qq=开头的数字串
def get_at_user(msg : str) -> int | None:
    try:
        msg = msg.strip()
        keyword = re.search('(?<=CQ:at,qq=)\d+\.?\d*', msg)
        if(keyword is None):
            return None
        else:
            keyword = int(keyword.group())
            return keyword
    except Exception as e:
        print('get_at_user error:' + str(e))   
