CREATE DATABASE Bilibili
ON PRIMARY
(
NAME ='Bilibili_data',
FILENAME = 'E:\workspace\T-SQL\Database\Bilibili_data.mdf',
SIZE = 5MB,
MAXSIZE = 100MB,
FILEGROWTH = 15%
)
LOG ON 
(
NAME = 'Bilibili_log',
FILENAME = 'E:\workspace\T-SQL\Database\Bilibili_log.ldf',
SIZE = 5MB,
MAXSIZE = 10MB,
FILEGROWTH = 1MB
)