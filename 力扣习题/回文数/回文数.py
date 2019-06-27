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

def isis(x: int) -> bool:
    if x >= 0:
        if x == int(str(x)[::-1]):
            return True
        else:
            return False
    else:
        return False


while (True):
    y = int(input("请输入数字: "))
    print(isis(y))