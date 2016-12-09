#coding=UTF-8
'''
Created on 2016年9月21日

@author: Shark
'''
import requests

def getHtml(stuID):
    url = 'http://jwc.jxnu.edu.cn/MyControl/All_Display.aspx?UserControl=All_StudentInfor.ascx&UserType=Student&UserNum='+str(stuID)
    headers = {"cookie":"ASP.NET_SessionId=hhmifniht4oo4ujyjhrb5ohv; JwOAUserSettingNew=UserNum=BWYTz51j93es7pFcSd8tbQ==&UserName=dbDb09VIlEiJrCIYz2yYVA==&UserType=WmTb330+jk8=&UserLoginTime=2016/9/21 16:03:05"}
    request = requests.get(url,headers=headers)
    print request.content
getHtml(1467004070)