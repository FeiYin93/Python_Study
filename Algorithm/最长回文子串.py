#coding=UTF-8
'''
Created on 2016年10月24日

@author: ZWT
'''
from operator import le

#暴力解法
class BaoLi(object):
    def isPalindrome(self,String,start,end):
        while start < end:
            if String[start] != String[end]:
                return False
            start += 1
            end -= 1
        return True
    def longestPalindrome(self,TestString):
        MaxLen,left,right = 0,0,0
        for start in range(0,len(TestString)):
            for end in range(start,len(TestString)):
                    if self.isPalindrome(TestString,start,end):
                        if (end-start+1) > MaxLen:
                            MaxLen = end - start + 1
                            left,right = start,end
            end += 1                
        print MaxLen,TestString[left:right+1]
class Manacher(object):
    def longestPalindrome(self,TestString):
        tempString = '#'+'#'.join(TestString)+'#'#将#加入到字符串使其长度为奇数
        
        RL = [0]*len(tempString)#RL记录第i个字符为对称轴的回文串的最右边字符与字符i的距离，既是回文半径
        MaxRight = 0 #记录最长回文字串的最后边字符的位置
        pos = 0 #记录当前最长回文字串的中心字符位置
        MaxLen = 0 #记录最长回文字串的长度
        for i in range(len(tempString)):
            print "这是第"+str(i)+"个字符"
            if i < MaxRight:
                RL[i] = min(RL[2*pos-i],MaxRight-i)
                print "当前字符的最长回文半径为："+str(RL[i])
            else:
                RL[i] = 1
            #往后扩展以i为中心的最长回文字串，注意边界处理
            while i-RL[i] >= 0 and i+RL[i] < len(tempString) and tempString[i-RL[i]] == tempString[i+RL[i]]:
                print tempString[i-RL[i]:i+RL[i]+1] 
                RL[i] += 1
            if RL[i]+i-1 >MaxRight:
                MaxRight = RL[i]+i-1
                pos = i
                longestPalindrome = tempString[i-RL[i]+1:i+RL[i]].replace('#','')
                print "当前最长回文为："+str(longestPalindrome)
            MaxLen = max(MaxLen,RL[i])
        print "最长回文字串为: "+str(longestPalindrome)+" 长度为： "+str(MaxLen-1)
        
TestString = "abcgefsjosfeghihgefsojs"
method = raw_input("请输入 1 选择暴力穷举法，输入 2 选择manacher法：")        
if method == '1':
    longestPalindrome = BaoLi()
elif method == '2':
    longestPalindrome = Manacher()
else:
    print "输入有误"
longestPalindrome.longestPalindrome(TestString)
                 
    