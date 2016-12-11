#coding=UTF-8
'''
Created on Dec 11, 2016

@author: ZWT
'''
import MySQL_Operation

import requests
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



def getTopicFollow(TopicID):
    print '正在获取话题 '+str(TopicID)+' 关注列表:'
    list_Follow = []
    TopicURL = 'https://www.zhihu.com/topic/'+str(TopicID)+'/followers'
    TopicHtml = BeautifulSoup(ZhiHu_session.get(TopicURL).content,'lxml')
    FollowNum = int(TopicHtml.find('div',class_="zm-topic-side-followers-info").a.strong.text)
    followPerson = TopicHtml.find_all('div',class_="zm-person-item")
    for person in followPerson:
        uid = person['id']
        PersonID = person.h2.a['href'].replace('/people/','')
#         print PersonID,uid
        list_Follow.append(PersonID)
        
    headers = dict(Default_Header)
    headers['Referer'] = 'https://www.zhihu.com/topic/19776749/followers'
    offset = 40
    start = uid
    while FollowNum > len(list_Follow):
        print FollowNum,len(list_Follow),offset,uid
        Data = {'offset':offset,'start':uid,'_xsrf':Xsrf}
        follow = ZhiHu_session.post(TopicURL,data=Data,headers=headers)
        
        Temphtml = BeautifulSoup((follow.json())['msg'][1],'lxml')
        TempfollowPerson = Temphtml.find_all('div',class_='zm-person-item')
        followlength = len(TempfollowPerson)
        offset += followlength
        for person in TempfollowPerson:
            uid = person['id']
            PersonID = person.h2.a['href'].replace('/people/','')
            list_Follow.append(PersonID)
    print len(list_Follow)
    return list_Follow
            
            
        
        
# TopicID = '19746428'
list_topic = MySQL_Operation.selectDB_TopicList()
for TopicID in list_topic:
    print TopicID
    list_follow = getTopicFollow(TopicID)
    MySQL_Operation.insertDB_TopicFollow(TopicID, list_follow)



