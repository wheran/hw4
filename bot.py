import itchat

#获取微信好友头像
#登录微信
itchat.auto_login()
#获取微信好友列表
for friends in itchat.get_friends():
    print(friends['NickName']), friends['RemarkName'], friends['Sex']#微信名
    img = itchat.get_head_img(userName=friends['UserName'])
    #定义路径 保存
    path = '/Users/apple/PycharmProjects/pythonProject2/img' + friends['NickName'] + '.jpg'
    #open
    with open(path, 'wb') as f:
        f.write(img)
itchat.run()
'''
求微信好友的好友比例
'''
itchat.auto_login(hotReload=True)#自动登录
male = female = other = 0
friends = itchat.get_friends()
print(type(friends))
for friend in itchat.get_friends()[1:]:#除了自己
    sex = friend['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
print(male)
#求微信好友总数
total = len(friends)
#男女比例 输出一个百分号%%
print('男性好友:%.2f%%'%(_float(male)/total * 100))
print('女性好友:%.2f%%'%(_float(male)/total * 100))
print('其他:%.2f%%'%(_float(male)/total * 100))

#apiurl = 'http://openapi.tuling123.com/openapi/api/v2'

def get_message():
    data = {
         'key': 'weizhi',
         'userId' : 'robot',
         'info' : message

    }
    try:
        r = requests.post(apiurl, data=data).json()
        print('root的回复%s'%r['text'])
        return r['text']
    except:
        return''

get_message('你好')

@itchat.msg_register(itchat.content.TEXT) #装饰器 给函数新增功能
def auto_reply(msg):
    defaulRreply = '你好'
    friend = itchat.search_friend('小天')
    #获取微信朋友姓名
    #readFriendUserName = friend[0]

itchat.run()



