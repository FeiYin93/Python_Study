USE Stock
CREATE TABLE StockData
(
StockNo NVARCHAR(6),
[Date] date,
[Open] FLOAT,
[High] FLOAT,
[Low] FLOAT,
[Close] FLOAT,
[VOLUME] FLOAT,
[Adj_Close] FLOAT
FOREIGN KEY(StockNo) references StockList(StockNo)
)