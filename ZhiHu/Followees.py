#coding=UTF-8
'''
Created on 2016��11��5��

@author: ZWT
'''
import requests
import json
from bs4 import BeautifulSoup
import MySQLdb
import PersonInfo

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
print Login_Url
print Xsrf
print Data
print (LogInState.json())['msg']

    
def getHashID(PersonUrl):
    PersonHtml = BeautifulSoup(ZhiHu_session.get(PersonUrl).content,'lxml')
    HashIDdiv = PersonHtml.find('div', class_='zm-profile-header-op-btns')
    if HashIDdiv is not None:
        Person_HashID = HashIDdiv.button['data-id']
    else:
        ga = PersonHtml.find('script', attrs={'data-name': 'ga_vars'})
        if ga is not None:
            Person_HashID = json.loads(ga.text)['user_hash']
        else:
            Person_HashID = 0
    return Person_HashID

def getFolloweesList(PersonID):
    print "正在获取 "+str(PersonID)+" 的关注列表："
    try:
        PersonUrl = 'https://www.zhihu.com/people/' + PersonID.strip('\n')
        HashID = getHashID(PersonUrl)
        if HashID:
            headers =dict(Default_Header)
            headers['Referer'] = PersonUrl + '/followees'
            FolloweesUrl = 'https://www.zhihu.com/node/ProfileFolloweesListV2'
            Params = {'offset':0,'order_by':'created','hash_id':HashID}
            Params_encode =json.dumps(Params)
            Data = {'method':'next','params':Params_encode,'_xsrf':Xsrf}
            
            FolloweesList = []
            TempIndex = 20
            offset = 0
            while TempIndex == 20:
                Params['offset'] = offset
                Data['params'] = json.dumps(Params)
                followUrlJSON = ZhiHu_session.post(FolloweesUrl,data=Data,headers=headers)
                TempIndex = len((followUrlJSON.json())['msg'])
                offset = offset + TempIndex
                followeesHtml = (followUrlJSON.json())['msg']
                for everHtml in followeesHtml:
                    everHtml = BeautifulSoup(everHtml,'lxml')
                    FolloweesID = everHtml.a['href']
                    FolloweesID = FolloweesID.replace(u'/people/','')
                    FolloweesList.append(FolloweesID)
            print FolloweesList
            return FolloweesList
    except:
        return 0

def selectDB_Followees(PersonID):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    SQL = "SELECT * FROM followees WHERE PersonID = \'"+str(PersonID)+'\''
    cursor.execute(SQL)
    result = cursor.fetchall()
    existFolloweesList = []
    for row in result:
        existFolloweesList.append(row[1])
    return existFolloweesList
def selectDB_Exist(PersonID):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    SQL = "SELECT * FROM Person_HashID WHERE PersonID = \'"+str(PersonID)+'\''
    cursor.execute(SQL)
    result = cursor.fetchone()
    if result is not None:
        return True
    else:
        return False
def insertDB_Followees(PersonID,FolloweesList):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    for Followees in FolloweesList:
        try:
            SQL = "INSERT INTO Followees(PersonID,FolloweesID)VALUES(\'"+str(PersonID)+"\',\'"+str(Followees)+'\')'
            cursor.execute(SQL)
            ZhiHu_DB.commit()
        except:
            ZhiHu_DB.rollback()
    ZhiHu_DB.close()
def insertDB_PersonInfo(PersonID):
    PersonUrl = 'https://www.zhihu.com/people/' + PersonID.strip('\n')
    Person_Html = ZhiHu_session.get(PersonUrl).content
    Person = PersonInfo.getPersonInfo(PersonID,Person_Html)
    if Person :
        PersonInfo.insertDB(Person)
    else:
        print "获取 "+str(PersonID)+" 的信息失败"
        return 0    
def DB_Followees(PersonID):
    if selectDB_Exist(PersonID):
        print "\n用户 "+str(PersonID)+" 的信息已存在"
    else:
        print "\n正在获取 "+str(PersonID)+" 的信息："
        insertDB_PersonInfo(PersonID)
        FolloweesList = getFolloweesList(PersonID)
        if FolloweesList:
            insertDB_Followees(PersonID, FolloweesList)
            print '用户 '+str(PersonID)+' 的关注列表插入完成'
        else:
            print '用户 '+str(PersonID)+' 的关注列表不存在'
  
PersonID = 'root'
existFolloweesList = selectDB_Followees(PersonID)
for followees_1 in existFolloweesList:
    try:
        DB_Followees(followees_1)
        existFolloweesList = selectDB_Followees(followees_1)
        for followees_2 in existFolloweesList:
            try:
                DB_Followees(followees_2)
                existFolloweesList = selectDB_Followees(followees_2)
                for followees_3 in existFolloweesList:
                    try:
                        DB_Followees(followees_3)
                    except:
                        print "Error"
            except:
                print "Error"
    except:
        print "Error"
print "success"
        
    
    
        
