#coding=UTF-8
'''
Created on 2016年10月6日

@author: ZWT
'''
import sqlserver.Database_Cn
import requests

def getStockNo():
    MyDateBase = sqlserver.Database_Cn.Database_Connect('{SQL Server}','DESKTOP-NO5JCR8','Stock')
    SQL = u'SELECT * FROM StockList'
    StockList = MyDateBase.execQuery(SQL)
    return StockList
    
def getCSV(stockNo):
    if int(stockNo) >= 600000:
        url = "http://table.finance.yahoo.com/table.csv?s="+str(stockNo)+".ss"
    else:
        url = "http://table.finance.yahoo.com/table.csv?s="+str(stockNo)+".sz"
    stockCSV = requests.get(url)
    Path = u'E:\WorkSpace\Python_Test\YaHoo_Finance\Stock_CSV\\'
    if stockCSV.status_code == 404:
        print 'No GET the Date For Code' + str(stockNo)
        Txt = open(Path+str(stockNo)+'.csv','wb')
        Txt.write(stockCSV.content)
        Txt.close()
    else:        
        CSV = open(Path+str(stockNo)+'.csv','wb')
        CSV.write(stockCSV.content)
        CSV.close()
def getDate(beginNo):
    StockList = getStockNo()
    for n in range(len(StockList)):
        print StockList[n][0],StockList[n][1],StockList[n][2].decode('gbk').encode('utf-8'),StockList[n][3],StockList[n][4],StockList[n][5]
        StockNo = StockList[n][1]
        if StockNo < beginNo:
            print '已下载'
        else:
            print '正在下载: ' + str(StockNo) + ' 数据'
            getCSV(StockNo)
            print '股票代码' + str(StockNo) + '数据下载成功'
        print ''
getDate()