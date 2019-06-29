# -*- coding = utf-8 -*-
# 很简单的题目不是吗？


#  第一次的解法 52ms
class Solution:
    def reverse(self, x: int) -> int:
        isf = False
        if x < 0:
            isf = True
            tmp = -x
        else:
            tmp = x
        i = 0
        res = 0
        while tmp > 0:
            res *= 10
            i = tmp % 10
            res += i
            tmp //= 10
        if isf:
            res = -res
        if res > 2147483647 or res < -2147483648:
            return 0
        else:
            return res
        print(res)


#  字符串的解法 52ms
class Solution2:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            res = -int(str(-x)[::-1])
        else:
            res = int(str(x)[::-1])
        if res > 2147483647 or res < -2147483648:
            return 0
        else:
            return res


s = Solution2()
print(s.reverse(int(input("输入数字"))))
input()
