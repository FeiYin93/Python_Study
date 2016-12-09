#coding=UTF-8
'''
Created on 2016��9��21��

@author: Shark
'''
import requests
code=requests.get("http://jwc.jxnu.edu.cn/MyControl/All_Display.aspx?UserControl=All_StudentInfor.ascx&UserType=Student&UserNum=1467004070").status_code
print code

