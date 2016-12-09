#coding=utf-8
'''
Created on 2016年8月25日

@author: Shark
'''
import urllib
import urllib2
import re

class WYY_Music:
    
    def __init__(self,baseUrl):
        self.baseURL=baseUrl
    
    def getHtml(self):
        try:
            url = self.baseURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            Html = response.read().decode('utf-8')
            print Html
            return Html
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"网易云用户不存在",e.reason
                return None
    

            
        
                
print "请输入网易云用户ID"  
baseURL = 'http://music.163.com/#/user/home?id=' +str(raw_input(u'http://music.163.com/#/user/home?id='))
user = WYY_Music(baseURL)
user.getHtml()

