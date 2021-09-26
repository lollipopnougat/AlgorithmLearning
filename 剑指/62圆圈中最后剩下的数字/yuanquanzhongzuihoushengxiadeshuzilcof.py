# 
''' 参考 https://blog.csdn.net/u011500062/article/details/72855826 约瑟夫环
约瑟夫问题是个著名的问题：N个人围成一圈，第一个人从1开始报数，报M的将被杀掉，
下一个人接着从1开始报。如此反复，最后剩下一个，求最后的胜利者。

公式

f(N, M) = (f(N − 1, M) + M) % N

f(N,M)表示，N个人报数，每报到M时杀掉那个人，最终胜利者的编号
f(N − 1, M)表示，N - 1个人报数，每报到 M 时杀掉那个人，最终胜利者的编号
'''

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2, n + 1):
            res = (res + m) % i
        return res