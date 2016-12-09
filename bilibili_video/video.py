#coding=UTF-8
'''
Created on 2016��9��23��

@author: Shark
'''
import requests
import BeautifulSoup
import json
import sqlserver.Database_Cn
import thread
import re


class getHtml(object):
    def __init__(self,avID,baseurl):
        self.avID = avID
        self.baseurl = baseurl
        
    def getHtml(self,avID,baseurl):
        url = baseurl + str(avID)
        html = requests.get(url).content
        return html

class getVideo(object):
    def __init__(self,avID):
        self.avID = avID
        
    def getTitle(self,avID):
        baseurl = 'http://www.bilibili.com/video/av'
        html = getHtml(avID,baseurl).getHtml(avID, baseurl)
        soup = BeautifulSoup.BeautifulSoup(html)
        if soup.h1 != None:
            return soup.h1.string.replace("'","")#删除引号防止插入数据库出错
        else:
            return None
    
    def getScore(self,avID):
        baseurl = 'http://api.bilibili.com/archive_stat/stat?aid='
        Value = getHtml(avID,baseurl).getHtml(avID, baseurl)
        score =  json.loads(Value.decode('UTF-8'))
        return score   
class intoData(object):
    def __init__(self,avID,title,score):
        self.avID = avID
        self.title = title
        self.score = score
        
    def intoData(self,avID,title,score):
        avID = str(avID)
        data = score["data"]
        v_view = str(data["view"])
        v_danmaku = str(data["danmaku"])
        v_reply = str(data["reply"])
        v_favorite = str(data["favorite"])
        v_share = str(data["share"])
        v_coin = str(data["coin"])
        v_rank = str(data["his_rank"])
        print avID,title,v_view,v_danmaku,v_reply,v_favorite,v_share,v_coin,v_rank
        myDatabase = sqlserver.Database_Cn.Database_Connect('{SQL Server}','DESKTOP-NO5JCR8','Bilibili')
        #SQL = "INSERT INTO VideoScore(AVid,AVname,AVview,AVdanmaku,AVreply,AVfavorite,AVshare,AVcoin,AVrank)VALUES("+avID+','+('%s')%title+','+v_view+','+v_danmaku+','+v_reply+','+v_favorite+','+v_share+','+v_coin+','+v_rank+')'
        #SQL = "INSERT INTO VideoScore(AVid)VALUES("+avID+')'
        SQL = "INSERT INTO VideoScore(AVname,AVid,AVview,AVdanmaku,AVreply,AVfavorite,AVshare,AVcoin,AVrank)VALUES(('%s')"%title+','+avID+','+v_view+','+v_danmaku+','+v_reply+','+v_favorite+','+v_share+','+v_coin+','+v_rank+')'
        #myDatabase.execNoQuery(SQL)
        myDatabase.execNoQuery(SQL)
        print "INSERT INTO DATABASE SUCCESS"
        print ""


def ForVideo(startID,endID):
    for id in range(startID,endID):
        avID = id
        video = getVideo(avID)
        score = video.getScore(avID)
        if score["data"]["view"] != 0:
            #print score
            title = video.getTitle(avID)
            if title != None:
                data = intoData(avID,title,score)
                data.intoData(avID, title, score)
        else:
            print str(avID)+" ID Not Found "
            print ""

def main():
    ForVideo(30000, 50000)
#     try:
#         thread.start_new_thread(ForVideo(9000, 10000))
#     except:
#         print "Error : unable to start thread"
#     while 1:
#         pass

if __name__ == '__main__':
    main()
        
        
                
