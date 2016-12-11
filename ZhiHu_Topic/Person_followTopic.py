#coding=UTF-8
'''
Created on Dec 11, 2016

@author: ZWT
'''
import MySQL_Operation

import requests
import json
from bs4 import BeautifulSoup

Default_Header = {'X-Requested-with':'XMLHttpRequest',
                  'Referer':'http://www.zhihu.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'Host':'www.zhihu.com'}
ZhiHu_session = requests.session()
ZhiHu_session.headers.update(Default_Header)

BaseUrl = 'https://www.zhihu.com/'
#######获取XSRF
BaseHtml = BeautifulSoup(ZhiHu_session.get(BaseUrl).content,'lxml')
Xsrf = BaseHtml.find('input',attrs={'name':'_xsrf'})['value']
#######LogIn登录
print"知乎模拟登录："
method = raw_input("    请输入 1 选择手机登录，输入 2 选择邮箱的登录：")
# CaptureUrl = BaseUrl + 'captcha.gif?type=login'
CaptureUrl = 'https://www.zhihu.com/captcha.gif?r=1481427841553&type=login'
with open('LogInParams/cap.gif','wb')as capFile:
    capFile.write(ZhiHu_session.get(CaptureUrl).content)
if method == '1':
    LogInName = raw_input("    请输入手机号：")
    Password = raw_input("    请输入密码：")
    Login_Url = BaseUrl + 'login/phone_num'
    Captcha = raw_input("    请输入验证码：")
    Data = {'_xsrf':Xsrf,'password':Password,'captcha':Captcha,'phone_num':LogInName}
elif method == '2':
    LogInName = raw_input("    请输入邮箱：")
    Password = raw_input("    请输入密码：")
    Login_Url = BaseUrl + 'login/email'
    Captcha = raw_input("    请输入验证码：")
    Data = {'email':LogInName,'password':Password,'captcha':Captcha}
else:
    print "登录方法选择错误"
LogInState = ZhiHu_session.post(Login_Url,data=Data)
print (LogInState.json())['msg']


def getFollowTopic(PersonID):
    try:
        print '正在获取用户 '+str(PersonID)+' 话题关注列表'
        headers = dict(Default_Header)
        headers['Referer'] = 'https://www.zhihu.com/people/CodeZWT/following/topics'
        headers['authorization'] = 'Bearer Mi4wQUFDQXJsc3FBQUFBVUVBRzdvX0hDaGNBQUFCaEFsVk5zY2QwV0FEWXVrN2ZmUndoWVNtNTdUc2pSQmZxQVp2eWx3|1481456612|5d7b5586007081c4ee89c5674127bf795f520de4'
        ZhiHu_session.headers.update(headers)
        list_followTopic = []
        
        NextUrl = 'https://www.zhihu.com/api/v4/members/'+str(PersonID)+'/following-topic-contributions?include=data%5B*%5D.topic.introduction&offset=0&per_page=10&limit=10'
        sign = True
        while sign :
            Temp = ZhiHu_session.get(NextUrl)
    #         print json.dumps(Temp.json(),ensure_ascii=False,encoding='UTF-8')
            NextUrl = (Temp.json())['paging']['next']
            if (Temp.json())['paging']['is_end']:
                sign = False
            list_topic = (Temp.json())['data']
            for n in list_topic:
                id = n["topic"]['id']
                list_followTopic.append(id)
        print len(set(list_followTopic))
    #     print set(list_followTopic)
        return  list_followTopic
    except:
        print 'error'+str(PersonID)
        return 0


list_person = MySQL_Operation.selectDB_Person()
for PersonID in list_person:
    list_followTopic = getFollowTopic(PersonID)
    if list_followTopic:
        MySQL_Operation.insertDB_followTopic(PersonID, list_followTopic)
    
