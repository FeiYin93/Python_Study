#coding=UTF-8
'''
Created on 2016��12��3��

@author: ZWT
'''
import time
import datetime

print time.strftime('%Y-%m-%d',time.localtime(time.time()))
print time.time()
# print time.localtime()
# print time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
# 
print datetime.datetime.now()
# time1 = datetime.datetime.now()
# time2 = datetime.datetime.now() 
# print datetime.datetime.strptime(str(time1),'%Y-%m-%d %H:%M:%S.%f')
# print datetime.datetime.strptime(str(time2),'%Y-%m-%d %H:%M:%S.%f')
# print time1-time2

timeStamp = time.time()  
timeArray = time.localtime(timeStamp)  
print timeArray
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray) 
print otherStyleTime
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 