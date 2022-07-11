# nnm_bot

一个简易QQ机器人，套用`Bangdream`中`广町七深`的设定

# 项目结构

+ imageOnHtml 图片素材文件，用HTML进行拼接形成四格漫画
+ nnm_bot 机器人主体
+ config.yml go-cqhttp配置文件

# 如何部署

本项目依赖无头QQ客户端[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)：
1. 运行go-cqhttp，配置文件的`servers:`部分更换成仓库内的版本
2. 安装依赖`pip install -r requirements.txt`
3. 运行`nnm_bot/main.py`

# 实现功能

- [x] 群内关键词响应
- [x] Bangdream图片发送
- [x] 四格漫画发送
- [x] 买甜品
- [ ] 花名册
- [ ] 抽牌
