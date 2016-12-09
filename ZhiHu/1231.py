#coding=UTF-8
'''
Created on 2016年11月9日

@author: ZWT
'''
# import MySQLdb
# 
# PersonID = 'CodeShark'
# ZhiHu_DB = MySQLdb.connect('localhost','root','zwt@1314','ZhiHu',charset='utf8')
# cursor = ZhiHu_DB.cursor()
# SQL = "SELECT * FROM Person_HashID WHERE PersonID = \'"+str(PersonID)+'\''
# cursor.execute(SQL)
# result = cursor.fetchone()
# print result
# if result is not None:
#     print '1'

import requests
from bs4 import BeautifulSoup


Default_Header = {'X-Requested-with':'XMLHttpRequest',
                  'Referer':'http://www.zhihu.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'Host':'www.zhihu.com'}
ZhiHu_session = requests.session()
ZhiHu_session.headers.update(Default_Header)
RootTopicID = 19776749
RootTopicName = '【根话题】'
RootTopic = [RootTopicName,RootTopicID]

TopicURL = 'https://www.zhihu.com/topic/'+str(RootTopic[1])+'/hot'
HTML = ZhiHu_session.get(TopicURL).content
html = BeautifulSoup(HTML,'lxml')
print html.find('h1',class_="zm-editable-content").text
print html.find_all('div',class_="feed-content")[0].find_all('a')[0]
print html.find_all('div',class_="feed-content")[0].find_all('a')[0]['href'].replace('/question/','')
print html.find_all('div',class_="feed-content")[0].find_all('a')[0].text
