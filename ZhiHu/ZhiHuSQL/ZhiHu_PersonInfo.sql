CREATE TABLE Person_Info
(
PersonID NVARCHAR(100)NOT NULL PRIMARY KEY,
#ID表地址
PersonName NVARCHAR(100),
PersonGender NVARCHAR(100),
PersonBiography NVARCHAR(100),
PersonAddress NVARCHAR(100),
PersonBusiness NVARCHAR(100),
PersonEmployment NVARCHAR(100),
PersonPosition NVARCHAR(100),
PersonEducation NVARCHAR(100),
PersonEducation_extra NVARCHAR(100),
#HostInfo用户信息（用户名，性别，简介，地址，行业，公司，职位，学校，专业）
PersonFolloweesNum INT,
PersonFollowersNum INT,
PersonColumnsNum INT,
PersonTopicsNum INT,
#HostFollow用户关注（关注人数，被关注数，关注专栏数，关注话题数）
PersonAgreeNum INT,
PersonThanksNum INT,
PersonAsksNum INT,
PersonAnswersNum INT,
PersonPostsNum INT,
PersonCollectionsNum INT
#HostImpression用户印象（获得赞同数，感谢数，提问数，回答数，文章数，收藏数）`userinfo``followees`
FOREIGN KEY(PersonID) REFERENCES Person_HashID(PersonID)
)