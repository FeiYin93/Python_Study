#coding=UTF-8
'''
Created on 2016年10月7日

@author: ZWT
'''
import os
import csv
import sqlserver.Database_Cn

srcPath = 'E:\WorkSpace\Python_Test\Finance\Stock_CSV'
csvfiles = os.listdir(srcPath)
for csvfile in csvfiles:
    StockNo = csvfile.replace('.csv','')
    filePath = 'E:\WorkSpace\Python_Test\Finance\Stock_CSV\\'
    csvfile = open(filePath + StockNo + '.csv','rb')
    Data = csv.reader(csvfile)
    line_num = 0
    for line in Data:
        line_num += 1
        if line_num != 1:
            StockNo = str(StockNo)
            Date = str(line[0])
            Open = str(line[1])
            High = str(line[2])
            Low = str(line[3])
            Close = str(line[4])
            VOLUME = str(line[5])
            Adj_Class = str(line[6])
            print StockNo,Date,Open,High,Low,Close,VOLUME,Adj_Class
            print '正在插入 ' + StockNo +' '+ Date
            myDatabase = sqlserver.Database_Cn.Database_Connect('{SQL Server}','DESKTOP-NO5JCR8','Stock')
            SQL = "INSERT INTO StockData([StockNo],[Date],[Open],[High],[Low],[Close],[VOLUME],[Adj_Close])VALUES(\'"+StockNo+'\','+'\''+Date+'\''+','+Open+','+High+','+Low+','+Close+','+VOLUME+','+Adj_Class+')'
            myDatabase.execNoQuery(SQL)
    print StockNo + "已成功存入Database"
print "SUCCESS"
    
    