USE Bilibili

CREATE TABLE VideoScore
(
AVid INT PRIMARY KEY,
/*视频ID号*/
AVname NVARCHAR(80),
/*视频名称*/
AVview INT,
/*播放次数*/
AVdanmaku INT,
/*弹幕数*/
AVreply INT,
/*评论数*/
AVfavorite INT,
/*收藏数*/
AVshare INT,
/*分享数*/
AVcoin INT,
/*硬币数*/
AVrank INT,
/*排行数*/
)