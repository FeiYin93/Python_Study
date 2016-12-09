#coding=UTF-8
'''
Created on 2016��11��1��
@author: ZWT
'''
import json
import MySQLdb
from bs4 import BeautifulSoup

def getPersonInfo(PersonID,Person_Html):
    Person_Html = BeautifulSoup(Person_Html,'lxml')
    PersonID = PersonID
    #HostID 用户ID
    HashIDdiv = Person_Html.find('div', class_='zm-profile-header-op-btns')
    if HashIDdiv is not None:
        Person_HashID = HashIDdiv.button['data-id']
    else:
        ga = Person_Html.find('script', attrs={'data-name': 'ga_vars'})
        if ga is not None:
            Person_HashID = json.loads(ga.text)['user_hash']
        else:
            Person_HashID = 0
    #Host_HashID 用户唯一标识hash码
    if Person_Html.find(class_='female') is not None:
        if Person_Html.find(class_='female')['value'] == 1:
            PersonGender = '女'
        else:
            PersonGender = '男' 
    else:
        PersonGender = 'None'
    if Person_HashID :
        PersonName = Person_Html.find_all('span', class_='name')[1].text if Person_Html.find_all('span', class_='name') else 'None'
        PersonBiography = Person_Html.find('div',class_='bio ellipsis').text if Person_Html.find('div',class_='bio ellipsis') else 'None'
        PersonAddress = Person_Html.find('span', class_='location item').text if Person_Html.find('span', class_='location item') else 'None'
        PersonBusiness = Person_Html.find('span', class_='business item').text if Person_Html.find('span', class_='business item') else 'None'
        PersonEmployment = Person_Html.find('span', class_='employment item').text if Person_Html.find('span', class_='employment item') else 'None'
        PersonPosition = Person_Html.find('span',class_='position item').text if Person_Html.find('span',class_='position item') else 'None'
        PersonEducation = Person_Html.find('span',class_='education item').text if Person_Html.find('span',class_='education item') else 'None'
        PersonEducation_extra = Person_Html.find('span',class_='education-extra item').text if Person_Html.find('span',class_='education-extra item')else 'None'
        PersonInfo = [PersonName,PersonGender,PersonBiography,PersonAddress,PersonBusiness,PersonEmployment,PersonPosition,PersonEducation,PersonEducation_extra]
        #HostInfo用户信息（用户名，性别，简介，地址，行业，公司，职位，学校，专业）
        
        PersonFolloweesNum = int(Person_Html.find('div', class_='zm-profile-side-following zg-clear').find_all('a')[0].strong.text) if Person_Html.find('div', class_='zm-profile-side-following zg-clear') else 0
        PersonFollowersNum = int(Person_Html.find('div', class_='zm-profile-side-following zg-clear').find_all('a')[1].strong.text) if Person_Html.find('div', class_='zm-profile-side-following zg-clear') else 0
    #     Div_Section = Person_Html.find_all('div',class_='zm-profile-side-section-title')[0].find('a')
    #     if Div_Section is not None:
    #         if Div_Section.strong is not None:
    #             ColumnsNum = Person_Html.find_all('div',class_='zm-profile-side-section-title')[0].find('a').strong.text
    #             TopicsNum = Person_Html.find_all('div',class_='zm-profile-side-section-title')[1].find('a').strong.text
    #         else:
    #             ColumnsNum = Person_Html.find_all('div',class_='zm-profile-side-section-title')[1].find_all('a')[0].strong.text
    #             TopicsNum = Person_Html.find_all('div',class_='zm-profile-side-section-title')[2].find_all('a')[0].strong.text
    #     else:
    #         ColumnsNum = Person_Html.find_all('div',class_='zm-profile-side-section-title')[1].find_all('a')[0].strong.text
    #         TopicsNum = Person_Html.find_all('div',class_='zm-profile-side-section-title')[2].find_all('a')[0].strong.text
    #     PersonColumnsNum = int(filter(str.isdigit, str(ColumnsNum.encode('utf-8'))))
    #     PersonTopicsNum = int(filter(str.isdigit, str(TopicsNum.encode('utf-8'))))
        PersonFollow = [PersonFolloweesNum,PersonFollowersNum]
        #HostFollow用户关注（关注人数，被关注数）
        PersonAgreeNum = int(Person_Html.find('span',class_='zm-profile-header-user-agree').strong.text) if Person_Html.find('span',class_='zm-profile-header-user-agree') else 0
        PersonThanksNum = int(Person_Html.find('span',class_='zm-profile-header-user-thanks').strong.text) if Person_Html.find('span',class_='zm-profile-header-user-thanks') else 0
        PersonAsksNum = int(Person_Html.find('div',class_='profile-navbar clearfix').find_all('a')[1].span.text) if Person_Html.find('div',class_='profile-navbar clearfix') else 0
        PersonAnswersNum = int(Person_Html.find('div',class_='profile-navbar clearfix').find_all('a')[2].span.text) if Person_Html.find('div',class_='profile-navbar clearfix') else 0
        PersonPostsNum = int(Person_Html.find('div',class_='profile-navbar clearfix').find_all('a')[3].span.text) if Person_Html.find('div',class_='profile-navbar clearfix') else 0
        PersonCollectionsNum = int(Person_Html.find('div',class_='profile-navbar clearfix').find_all('a')[4].span.text) if Person_Html.find('div',class_='profile-navbar clearfix') else 0
        PersonImpression = [PersonAgreeNum,PersonThanksNum,PersonAsksNum,PersonAnswersNum,PersonPostsNum,PersonCollectionsNum]
        #HostImpression用户印象（获得赞同数，感谢数，提问数，回答数，文章数，收藏数）
        
        Person = [PersonID,Person_HashID,PersonInfo,PersonFollow,PersonImpression]
        print  json.dumps(Person,ensure_ascii=False,encoding='UTF-8')
        return Person
    else:
        return 0

def insertDB(Person):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    try:
        SQL_HashID = "INSERT INTO Person_HashID(PersonID,Person_HashID)VALUES(%s,%s)"
        Person_HashID = (Person[0],Person[1])
        cursor.execute(SQL_HashID,Person_HashID)
        ZhiHu_DB.commit()
        SQL_Info = "INSERT INTO Person_Info(PersonID,PersonName,PersonGender,PersonBiography,PersonAddress,PersonBusiness,PersonEmployment,PersonPosition,PersonEducation,PersonEducation_extra)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        Person_Info = (Person[0],Person[2][0],Person[2][1],Person[2][2],Person[2][3],Person[2][4],Person[2][5],Person[2][6],Person[2][7],Person[2][8])
        cursor.execute(SQL_Info,Person_Info)
        ZhiHu_DB.commit()
        SQL_FollowNum = "INSERT INTO Person_FollowNum(PersonID,PersonFolloweesNum,PersonFollowersNum)VALUES(%s,%s,%s)"
        Person_FollowNum = (Person[0],Person[3][0],Person[3][1])
        cursor.execute(SQL_FollowNum,Person_FollowNum)
        ZhiHu_DB.commit()
        SQL_ImpressionNum = "INSERT INTO Person_ImpressionNum(PersonID,PersonAgreeNum,PersonThanksNum,PersonAsksNum,PersonAnswersNum,PersonPostsNum,PersonCollectionsNum)VALUES(%s,%s,%s,%s,%s,%s,%s)"
        Person_FollowNum = (Person[0],Person[4][0],Person[4][1],Person[4][2],Person[4][3],Person[4][4],Person[4][5])
        cursor.execute(SQL_ImpressionNum,Person_FollowNum)
        ZhiHu_DB.commit()
    except:
            ZhiHu_DB.rollback()
    ZhiHu_DB.close()
    print "用户 "+str(Person[0])+" 信息已存储" 