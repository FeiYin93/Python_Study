#coding=UTf-8
'''
Created on 2016��9��23��

@author: Shark
'''
import threading
import time

class MyThread(threading.thread) :

    def __init__(self, thread_id, name, counter) :
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self) :
        #重写run方法, 添加线程执行逻辑, start函数运行会自动执行
        print  "Starting " + self.name
        threadLock.acquire() #获取所
        print_time(self.name, self.counter, 3)
        threadLock.release() #释放锁

def print_time(thread_name, delay, counter) :
    while counter :
        time.sleep(delay)
        print "%s %s" % (thread_name, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = [] #存放线程对象

thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

#开启线程
thread1.start()
thread2.start()

for t in threads :
    t.join()  #等待线程直到终止
print "Exiting Main Thread"