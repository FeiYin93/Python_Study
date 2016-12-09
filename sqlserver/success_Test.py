#coding=UTF-8
'''
Created on 2016��9��20��

@author: Shark
'''
import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-3I24U8I;DATABASE=Northwind')
cursor =cnxn.cursor()
cursor.execute("select * from Products")
row = cursor.fetchone()
print row   
cnxn.commit()
cnxn.close()