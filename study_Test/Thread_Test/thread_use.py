#coding=UTF-8
'''
Created on 2016��9��23��

@author: Shark
'''
import thread
import time

def print_time(threadName,delay):
    count = 0;
    while count<5:
        time.sleep(delay)
        count += 1
        print "%s:%s" % (threadName,time.ctime(time.time()))

try:
    thread.start_new_thread( print_time, ("first",2))
    thread.start_new_thread( print_time, ("second",3))
except:
    print "error : unable to start thread"
    
while 1:
    pass  
