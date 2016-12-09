#coding=UTF-8
'''
Created on 2016��12��1��

@author: ZWT
'''
import requests
from bs4 import BeautifulSoup
import MySQLdb
import json

def insertDB_Question(Topic,list_Question):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    for Que in list_Question:
        QueID = Que[0]
        QueName = Que[1]
        try:
            SQL = "INSERT INTO Question(QuestionID,QuestionName,FromTopicID,FromTopicName)VALUES(%s,%s,%s,%s)"
            Param = (QueID,QueName,Topic[1],Topic[0])
            cursor.execute(SQL,Param)
            ZhiHu_DB.commit()
        except:
            ZhiHu_DB.rollback()
    ZhiHu_DB.close()

def insertDB_Topic(Topic,list_ChildTopic):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    for ChildTopic in list_ChildTopic:
        ChildTopicName = ChildTopic[0]
        ChildTopicID = ChildTopic[1]
        try:
            SQL = "INSERT INTO Topic(Father_Topic,Father_Topic_ID,Child_Topic,Child_Topic_ID)VALUES(%s,%s,%s,%s)"
            Param = (Topic[0],Topic[1],ChildTopicName,ChildTopicID)
            cursor.execute(SQL,Param)
            ZhiHu_DB.commit()
        except:
            ZhiHu_DB.rollback()
    ZhiHu_DB.close()


Default_Header = {'X-Requested-with':'XMLHttpRequest',
                  'Referer':'http://www.zhihu.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'Host':'www.zhihu.com'}
ZhiHu_session = requests.session()
ZhiHu_session.headers.update(Default_Header)
RootTopicID = 19776749
RootTopicName = '【根话题】'
RootTopic = [RootTopicName,RootTopicID]

def getChildTopic(ChildTopic_List):
    List_Child = []
    
    for Child in ChildTopic_List: 
        TopicURL = 'https://www.zhihu.com/topic/'+str(Child[1])+'/hot'
        try:
            TopicHTML = ZhiHu_session.get(TopicURL).content
            TopicHTML = BeautifulSoup(TopicHTML,'lxml')
            if TopicHTML.find('div',class_="zm-side-section-inner child-topic"):
                DIV_ChildTopic = TopicHTML.find('div',class_="zm-side-section-inner child-topic").find_all('a')
                list_ChildTopic = []
                for n in range(len(DIV_ChildTopic)):
                    ChildTopic = [DIV_ChildTopic[n].text,DIV_ChildTopic[n]['data-token']]
                    list_ChildTopic.append(ChildTopic)
                
                
                if TopicHTML.find_all('div',class_="feed-content"):
                    list_HotQuestion = TopicHTML.find_all('div',class_="feed-content")
                    list_Question = []
                    for n in range(len(list_HotQuestion)):
                        QuestionID = TopicHTML.find_all('div',class_="feed-content")[n].find_all('a')[0]['href'].replace('/question/','')
                        QuestionName = TopicHTML.find_all('div',class_="feed-content")[n].find_all('a')[0].text
                        Question = [QuestionID,QuestionName]
                        list_Question.append(Question)
                    
                    insertDB_Question(Child, list_Question)
                
                
                
    #                 insertDB_Topic(Child, list_ChildTopic)
            else:
                list_ChildTopic = []
            if list_ChildTopic:
                print json.dumps(list_ChildTopic,ensure_ascii=False,encoding='UTF-8')
        except:
            print  "Didn't get the ChildTopic For "+str(Child[0])
        if list_ChildTopic:
            for childTipic in list_ChildTopic:
                List_Child.append(childTipic)
    return  List_Child


def main(List_Child,count):
    print '第 '+ str(count)+ '层，长度为：' +str(len(List_Child))
    if List_Child:    
        allList_Child = getChildTopic(List_Child)
        count += 1
        main(allList_Child,count)
    else:
        print 'Finish'
         
FatherTopic =[RootTopic]
count = 1
main(FatherTopic,count)