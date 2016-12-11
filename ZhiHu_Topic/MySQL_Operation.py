#coding=UTF-8
'''
Created on Dec 11, 2016

@author: ZWT
'''
import MySQLdb

def selectDB_TopicList():
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu_data',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    SQL = "SELECT * FROM topic_id"
    cursor.execute(SQL)
    result = cursor.fetchall()
    ZhiHu_DB.close()
    list_Topic = []
    for row in result:
        list_Topic.append(row[1])
    return list_Topic

def insertDB_TopicFollow(TopicID,list_follow):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu_data',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    for PersonID in list_follow:
        try:
            SQL = "INSERT INTO TopicFollow(TopicID,PersonID)VALUES(\'"+str(TopicID)+"\',\'"+str(PersonID)+'\')'
            cursor.execute(SQL)
            ZhiHu_DB.commit()
        except:
            ZhiHu_DB.rollback()
    ZhiHu_DB.close()
    print '话题 '+str(TopicID)+' 存储完成\n'
    
    
def selectDB_Person():
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu_data',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    SQL = "SELECT * FROM person_id"
    cursor.execute(SQL)
    result = cursor.fetchall()
    ZhiHu_DB.close()
    list_person = []
    for row in result:
        list_person.append(row[1])
    return list_person

def insertDB_followTopic(PersonID,list_followTopic):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu_data',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    for topicID in list_followTopic:
        try:
            SQL = "INSERT INTO followTopic(PersonID,TopicID)VALUES(\'"+str(PersonID)+"\',\'"+str(topicID)+'\')'
            cursor.execute(SQL)
            ZhiHu_DB.commit()
        except:
            ZhiHu_DB.rollback()
    ZhiHu_DB.close()
    print '用户 '+str(PersonID)+' 关注话题列表存储完成\n'