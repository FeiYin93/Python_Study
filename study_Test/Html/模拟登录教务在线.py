#coding:utf-8
'''
Created on 2016��8��19��

@author: Shark
'''
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

pastdata = urllib.urlencode({'StuName':'1467004077','PassWord':'love1314'})
logiUrl = 'http://jwc.jxnu.edu.cn/Default_Login.aspx?preurl='

result = opener.open(logiUrl,pastdata)
cookie.save(ignore_discard=True, ignore_expires=True)

gradeUrl = 'http://jwc.jxnu.edu.cn/MyControl/All_Display.aspx?UserControl=xfz_cj.ascx&Action=Personal'
result = opener.open(gradeUrl)
print result.read()