import socket

# 用于发送消息
# 在原有的消息发送函数的基础上定义两个工具函数
# 参数输入群号/QQ号和消息就可以直接发送
# 参数类型见标注分别为int和str

# 发送群消息
def send_group(group : int, msg : str):
    resp_dict = {'msg_type': 'group', 'number': group, 'msg': '{}'.format(msg)}
    try:
        send_msg(resp_dict)
    except Exception as e:
        print('send_group error:' + str(e))

# 发送私聊消息
def send_private(private : int, msg : str):
    resp_dict = {'msg_type': 'private', 'number': private, 'msg': '{}'.format(msg)}
    try:
        send_msg(resp_dict)
    except Exception as e:
        print('send_private error:' + str(e))

# 原消息发送函数
def send_msg(resp_dict):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = '127.0.0.1'
    client.connect((ip, 5700))
    msg_type = resp_dict['msg_type']
    number = resp_dict['number']
    msg = resp_dict['msg']
    # 将字符中的特殊字符进行url编码
    # 必须先处理百分号，不然后面的编码会乱套
    msg = msg.replace("%", "%25")
    msg = msg.replace(" ", "%20")
    msg = msg.replace("\n", "%0a")

    if msg_type == 'group':
        payload = "GET /send_group_msg?group_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    elif msg_type == 'private':
        payload = "GET /send_private_msg?user_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"

    print("发送" + payload)
    client.send(payload.encode("utf-8"))
    client.close()
    return 0
