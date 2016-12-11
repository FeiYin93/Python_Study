#coding=UTF-8
'''
Created on Dec 11, 2016

@author: ZWT
'''
import MySQLdb
import requests
from bs4 import BeautifulSoup



def selectDB_TopicList():
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu_data',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    SQL = "SELECT * FROM topic_id"
    cursor.execute(SQL)
    result = cursor.fetchall()
    ZhiHu_DB.close()
    return result

def insertDB_TopicFollow(topic,introduction):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu_data',charset='utf8')
    cursor = ZhiHu_DB.cursor()
#     try:
    SQL = "INSERT INTO Topic_id_copy(ID,TopicID,TopicName,TopicIntroduction)VALUES(%s,%s,%s,%s)"
    Params = (topic[0],topic[1],topic[2],introduction)
    cursor.execute(SQL,Params)
    ZhiHu_DB.commit()
#     except:
#         ZhiHu_DB.rollback()
    ZhiHu_DB.close()
    print '话题 '+str(Topic[1])+' 存储完成\n'





Default_Header = {'X-Requested-with':'XMLHttpRequest',
                  'Referer':'http://www.zhihu.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'Host':'www.zhihu.com'}
ZhiHu_session = requests.session()
ZhiHu_session.headers.update(Default_Header)
RootTopicID = 19776749




def getTopicIntroduction(Topic):
    print Topic
    TopicURL = 'https://www.zhihu.com/topic/'+str(Topic[1])+'/hot'
    try:
        TopicHTML = ZhiHu_session.get(TopicURL).content
        TopicHTML = BeautifulSoup(TopicHTML,'lxml')
        if TopicHTML.find('div',class_="zm-editable-content"):
            Introduction = TopicHTML.find('div',class_="zm-editable-content").text
            insertDB_TopicFollow(Topic, Introduction)
    except:
        print str(Topic[1])+'error'
        
list_topic = selectDB_TopicList()
for Topic in list_topic:
    getTopicIntroduction(Topic)
    