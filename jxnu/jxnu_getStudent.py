#coding=UTF-8
'''
Created on 2016��9��24��

@author: Shark
'''
import requests
import re

class getStudent(object):
    def __init__(self,stuID):
        self.stuID = stuID

    def getHtml(self,stuID):
        url = 'http://jwc.jxnu.edu.cn/MyControl/All_Display.aspx?UserControl=All_StudentInfor.ascx&UserType=Student&UserNum='+str(stuID)
        headers = {"cookie":"_ga=GA1.3.451806236.1474279166; ASP.NET_SessionId=ksun5vyi3vozbzg250wagdc5; JwOAUserSettingNew=UserNum=BWYTz51j93es7pFcSd8tbQ==&UserName=dbDb09VIlEiJrCIYz2yYVA==&UserType=WmTb330+jk8=&UserLoginTime=2016/9/24 15:16:10"}
        html = requests.get(url,headers=headers).content
        code=requests.get(url).status_code
        if code == 200:
            return html
        else:
            html = 404
            return html

    def getStu(self,html,stuID):
        reg_getNameDiv = re.compile('<span id="_ctl0_lblXM">(.+?)</span>',re.I)
        reg_getSexDiv = re.compile('<span id="_ctl0_lblXB">(.+?)</span>',re.I)
        reg_getClassDiv = re.compile('<span id="_ctl0_lblBJ">(.+?)</span>',re.I)
        reg_getValue = re.compile('<[^>]+>')
        stuName = reg_getValue.sub("",reg_getNameDiv.search(html).group())
        stuSex = reg_getValue.sub("",reg_getSexDiv.search(html).group())
        stuClass = reg_getValue.sub("",reg_getClassDiv.search(html).group())
        stu = [stuID,stuName,stuSex,stuClass]
        return stu