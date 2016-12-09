#coding=UTF-8
'''
Created on 2016年10月6日

@author: ZWT
'''
import sys
import string
import os
import shutil 
def RenameFiles(srcdir, prefix):  
    srcfiles = os.listdir(srcdir)
    print srcfiles  
    index = 1  
    for srcfile in srcfiles:
        print srcfile
        print srcfile.replace('.jpg','')
        print '' 
        srcfilename = os.path.splitext(srcfile)[0][1:]
        sufix = os.path.splitext(srcfile)[1]  
        destfile = srcdir + "//" + prefix + "_%04d"%(index) + sufix  
        srcfile = os.path.join(srcdir, srcfile)  
        os.rename(srcfile, destfile)  
        index += 1  
srcdir = u"E:\迅雷下载\图包"  #文件夹地址
prefix = u"壁纸"   #文件名前缀
RenameFiles(srcdir, prefix) 