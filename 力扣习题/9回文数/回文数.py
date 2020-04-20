# -*- coding = UTF-8 -*-
# 回文数
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            if x == int(str(x)[::-1]):
                return True 
            else:
                return False   
        else:
            return False
'''
# 我的想法是将数字转字符串，反转以后再转换成整型比较，一致就是回文


def isPalindrome1(x: int) -> bool:
    if x >= 0:
        if x == int(str(x)[::-1]):
            return True
        else:
            return False
    else:  # 负数肯定不是回文数
        return False


#  优化：
def isPalindrome2(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


def isPalindrome3(x: int) -> bool:
    if x < 0:
        return False
    else:
        tmp = x
        res = 0
        while tmp > 0:
            res = res * 10 + tmp % 10
            tmp //= 10
        if res == x:
            return True
        else:
            return False


while (True):
    y = int(input("请输入数字: "))
    print(isPalindrome3(y))

# 思考：如果不用字符串怎么办？
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0): #个位是0本身不是0的肯定不是回文数
            return False
        ret=0
        while(ret<x):
            ret=ret*10+x%10
            x=x//10
        return x==ret or x==ret//10
'''
# 通过除10和取余能把原数的反转数求出来