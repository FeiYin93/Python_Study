#coding=UTF-8
'''
Created on 2016年8月19日

@author: Shark
'''
import urllib
import urllib2
import cookielib

#url地址 ，data登录参数，headers浏览器参数
url = "https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
values = {"userName":"13027202882","password":"zwt@1314"}
data = urllib.urlencode(values)
headers = {"User-Agent":user_agent}

request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request,timeout=10)
html = response.read()
print html