# 所有message都会被去掉开头和结尾的空格!

# 是否以关键字开头，返回bool
def on_prefix(msg : str, keyword : str) -> bool:
    try:
        msg = msg.strip()
        return msg.startswith(keyword)
    except Exception as e:
        print('on_prefix error:' + str(e))

# 是否以关键字结尾，返回bool
def on_suffix(msg : str, keyword : str) -> bool:
    try:
        msg = msg.strip()
        return msg.endswith(keyword)
    except Exception as e:
        print('on_suffix error:' + str(e))

# 是否包含关键字，返回bool
def on_keyword(msg : str, keyword : str) -> bool:
    try:
        msg = msg.strip()
        return keyword in msg
    except Exception as e:
        print('on_keyword error:' + str(e))

# 是否完全相等，返回bool
def on_fullmatch(msg : str, keyword : str) -> bool:
    try:
        msg = msg.strip()
        return msg == keyword
    except Exception as e:
        print('on_fullmatch error:' + str(e))

# 是否以@Bot开头，返回bool
def on_atbot_prefix(msg : str, bot_id : int | str) -> bool:
    try:
        msg = msg.strip()
        return msg.startswith('[CQ:at,qq={}]'.format(bot_id))
    except Exception as e:
        print('on_atbot_prefix error:' + str(e))

# 是否包含@Bot，返回bool
def on_atbot_keyword(msg : str, bot_id : int | str) -> bool:
    try:
        msg = msg.strip()
        return '[CQ:at,qq={}]'.format(bot_id) in msg
    except Exception as e:
        print('on_atbot_prefix error:' + str(e))
        