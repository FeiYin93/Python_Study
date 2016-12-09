#coding=UTF-8

import pyodbc

class Database_Connect(object):
	"""docstring for Database_Connect"""
	def __init__(self, DRIVER,SERVER,DATABASE):
		super(Database_Connect, self).__init__()
		self.DRIVER = DRIVER
		self.SERVER = SERVER
		self.DATABASE = DATABASE
		#self.USER_ID =USER_ID
		#self.PASSWORD = PASSWORD
	def __getConnection(self):
		if not self.DRIVER:
			raise(NameError,'No DRIVER')
		if not self.SERVER:
			raise(NameError,'No SERVER')
		if not self.DATABASE:
			raise(NameError,'NO DATABASE')

		self.databaseConnect = pyodbc.connect(DRIVER = self.DRIVER,SERVER = self.SERVER,DATABASE = self.DATABASE,charset = 'UTF-8')
		databaseCursor = self.databaseConnect.cursor()
		if not databaseCursor:
			raise(NameError,'Database Connect failed')
		else:
			return databaseCursor
	def execQuery(self,SQL):
		databaseCursor = self.__getConnection()
		databaseCursor.execute(SQL)
		dataReturn = databaseCursor.fetchall()
		databaseCursor.close()
		self.databaseConnect.close()
		return dataReturn
	def execNoQuery(self,SQL):
		databaseCursor = self.__getConnection()
		databaseCursor.execute(SQL)
		self.databaseConnect.commit()
		databaseCursor.close()
		self.databaseConnect.close()

def main():
	myDatabase = Database_Connect('{SQL Server}','DESKTOP-3I24U8I','Bilibili')
	SQL = u"""
	INSERT INTO VideoScore(AVid,AVname,AVview,AVdanmaku,AVreply,AVfavorite,AVshare,AVcoin,AVrank)
	VALUES(639511,'【废柴君】盘点动画中的十大终极必杀狂拽酷炫吊炸天',87790,3921,388,2256,108,839,0)
	"""
	myDatabase.execNoQuery(SQL)
	SQL2 = u"""
	SELECT top 1 *
	FROM VideoScore
	"""
	DATA = myDatabase.execQuery(SQL2)
	print DATA
if __name__ == '__main__':
	main()

