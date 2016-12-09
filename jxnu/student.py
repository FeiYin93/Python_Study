#coding= UTF-8
'''
Created on 2016��9��26��

@author: Shark
'''
from jxnu.jxnu_getStudent import getStudent
from jxnu.jxun_getPhoto import getIMG



def main():
    for id in range(1467004001,1467004099):
        stuID = id
        student = getStudent(stuID) 
        html = student.getHtml(stuID)
        stu = student.getStu(html, stuID)
        print stu[0],stu[1],stu[2],stu[3]
        stuImg = getIMG(stu)
        Html = stuImg.gethtml(stu)
        stuImg.getStuImg(stu, Html)
if __name__ == '__main__':
    main()