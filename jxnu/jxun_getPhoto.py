#coding=UTF-8
'''
Created on 2016��9��21��

@author: Shark
'''
import requests
import os

class getIMG(object):
    def __init__(self,stu):
        self.stu = stu
       
    def gethtml(self,stu):
        url = 'http://jwc.jxnu.edu.cn/MyControl/All_PhotoShow.aspx?UserNum=' + str(stu[0]) + '&UserType=Student'
        myHeaders = {"cookie":"_ga=GA1.3.451806236.1474279166; ASP.NET_SessionId=ksun5vyi3vozbzg250wagdc5; JwOAUserSettingNew=UserNum=BWYTz51j93es7pFcSd8tbQ==&UserName=dbDb09VIlEiJrCIYz2yYVA==&UserType=WmTb330+jk8=&UserLoginTime=2016/9/24 15:16:10"}
        Html = requests.get(url, headers = myHeaders)
        code=requests.get(url).status_code
        if code == 200:
            return Html
        else:
            Html = 404
            return Html

    def getStuImg(self,stu,Html):
        position = 'E:\workspace\Python_Test\jxnu\Photo\\'
        if not os.path.isdir(position):
            os.makedirs(position)
        if Html != 404:    
            stuImgName = str(stu[0])+'%s'%stu[1]
            StuImg = open(position+str(stu[0])+'.jpg','wb')
            StuImg.write(Html.content)
            StuImg.close()
            print 'Get The Student Photo For '+str(stu[0])
        else:
            print 'Not GET The Photo For'+str(stu[0])
    

