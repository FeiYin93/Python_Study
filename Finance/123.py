#coding=UTF-8
'''
Created on 2016��10��7��

@author: ZWT
'''
import os
import requests

def reDown(srcdir):
    srcfiles = os.listdir(srcdir)
    for srcfile in srcfiles:
        stockNo = srcfile.replace('.csv','')
        print stockNo
        print '正在下载: ' + str(stockNo) + ' 数据'
        if int(stockNo) >= 600000:
            url = "http://table.finance.yahoo.com/table.csv?s="+str(stockNo)+".ss"
        else:
            url = "http://table.finance.yahoo.com/table.csv?s="+str(stockNo)+".sz"
        stockCSV = requests.get(url)
        Path = u'E:\WorkSpace\Python_Test\YaHoo_Finance\MyCSV\\'
        if stockCSV.status_code == 404:
            print 'No GET the Date For Code' + str(stockNo)
            Txt = open(Path+str(stockNo)+'.txt','wb')
            Txt.write(stockCSV.content)
            Txt.close()
        else:        
            CSV = open(Path+str(stockNo)+'.csv','wb')
            CSV.write(stockCSV.content)
            CSV.close()
            print '股票代码' + str(stockNo) + '数据下载成功'
        print ''

srcdir = u'E:\WorkSpace\Python_Test\YaHoo_Finance\GetCSV'
#reDown(srcdir)
print requests.get('http://table.finance.yahoo.com/table.csv?s=603159.ss').content
        
        