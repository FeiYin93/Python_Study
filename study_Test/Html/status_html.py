#coding=UTF-8
'''
Created on 2016��9��21��

@author: Shark
'''
import requests
code=requests.get("https://www.zhihu.com/people/CodeShark").status_code
print code
