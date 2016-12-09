#coding=UTF-8
'''
Created on 2016年9月30日

@author: Shark
'''
import csv


def conversion_CSV_to_Matrix_A():
    reader = csv.reader(file('data.csv','rb'))
    data = []
    for Line in reader:
        data.append(Line)
    List = [[0 for col in range(6)]for row in range(4)]
    #初始化矩阵A为零矩阵
    for m in range(len(data)):
        i = int(data[m][0])-1
        j = int(data[m][1])-1
        List[i][j] = 1
    return List
def transposeList(List):
    transposeList = map(list,zip(*List))
    #transposeList = [[row[col] for row in A] for col in range(len(A[0]))]
    #两种进行句子的行列互换即进行转置的方法
    return transposeList

def getDegree_Diag(List):
    #getDegree_Diag函数是求矩阵每行的度
    listDegree = []
    #listDegree为矩阵的行的度或列的度
    count = 0
    for row in range(len(List)):
        for col in range(len(List[0])):
            count += List[row][col]
        listDegree.append(count)
        count = 0
    diag = [[0 for col in range(len(listDegree))]for row in range(len(listDegree))]
    #初始化对角矩阵为零矩阵
    for n in range(len(diag)):
        diag[n][n] = listDegree[n]
    return diag
def det(m):
    if len(m) <= 0:
        return None
    if len(m) == 1:
        return m[0][0]
    else:
        s = 0
        for i in range(len(m)):
            n = [[row[a] for a in range(len(m)) if a != i] for row in m[1:]]
            if i % 2 == 0:
                s += m[0][i] * det(n)
            else:
                s -= m[0][i] * det(n)
        return s

A = conversion_CSV_to_Matrix_A()
print A
B = transposeList(A)
print B
du = getDegree_Diag(A)
print du
di = getDegree_Diag(B)

s = det(du)
print s


          


           
