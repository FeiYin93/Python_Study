#coding=UTF-8
'''
Created on 2016��12��1��

@author: ZWT
'''
import requests
import MySQLdb
from bs4 import BeautifulSoup

def selectDB_Question():
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    SQL = "SELECT DISTINCT(questionid) FROM Question GROUP BY questionid"
    cursor.execute(SQL)
    result = cursor.fetchall()
    ZhiHu_DB.close()
    
    list_Question = []
    for row in result:
        list_Question.append(row[1])
    return list_Question
    

def insertDB_Answer(QuestionID,PersonID,AnswerID,content):
    ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu',charset='utf8')
    cursor = ZhiHu_DB.cursor()
    try:
        SQL = "INSERT INTO Answer(QuestionID,PersonID,AnswerID,content)VALUES(%s,%s,%s,%s)"
        Param = (QuestionID,PersonID,AnswerID,content)
        cursor.execute(SQL,Param)
        ZhiHu_DB.commit()
        print "问题 "+str(QuestionID)+" 的回答 "+str(AnswerID)+" 存储成功"
    except:
        ZhiHu_DB.rollback()
    ZhiHu_DB.close()



Default_Header = {'X-Requested-with':'XMLHttpRequest',
                  'Referer':'http://www.zhihu.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'Host':'www.zhihu.com'}
ZhiHu_session = requests.session()
ZhiHu_session.headers.update(Default_Header)


# list_Question = selectDB_Question()
# print len(list_Question)

list_Question = ['28070036']

for n in range(len(list_Question)):
    QuestionID = list_Question[n]
    
    QuestionURL = 'https://www.zhihu.com/question/'+str(list_Question[n])
    QuestionHTML = ZhiHu_session.get(QuestionURL).content
#     print QuestionHTML
    QuestionHTML = BeautifulSoup(QuestionHTML,'lxml')
#     print QuestionHTML.find_all('div',class_="zm-item-answer zm-item-expanded")
    if QuestionHTML.find_all('div',class_="zm-item-answer zm-item-expanded"):
        
        list_Answer = QuestionHTML.find_all('div',class_="zm-item-answer zm-item-expanded")
        for m in range(len(list_Answer)):
            if QuestionHTML.find_all('div',class_="zm-item-answer zm-item-expanded")[m].find('a',class_="author-link"):
                PersonID = QuestionHTML.find_all('div',class_="zm-item-answer zm-item-expanded")[m].find('a',class_="author-link")['href'].replace('/people/','')
            else:
                PersonID = 'None'
            AnswerID = QuestionHTML.find_all('div',class_="zm-item-answer zm-item-expanded")[m]['data-atoken']
            content = QuestionHTML.find_all('div',class_="zm-item-answer zm-item-expanded")[m].find('div',class_="zm-editable-content clearfix").text
#             print PersonID
#             print AnswerID
#             print content
            insertDB_Answer(QuestionID, PersonID, AnswerID, content)
    else:
        print str(QuestionID)+' error'

