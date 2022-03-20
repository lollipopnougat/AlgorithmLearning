'''
6029. 射箭比赛中的最大得分 显示英文描述 

题目难度Medium
Alice 和 Bob 是一场射箭比赛中的对手。比赛规则如下：

Alice 先射 numArrows 支箭，然后 Bob 也射 numArrows 支箭。
分数按下述规则计算：
箭靶有若干整数计分区域，范围从 0 到 11 （含 0 和 11）。
箭靶上每个区域都对应一个得分 k（范围是 0 到 11），Alice 和 Bob 分别在得分 k 区域射中 ak 和 bk 支箭。如果 ak >= bk ，那么 Alice 得 k 分。如果 ak < bk ，则 Bob 得 k 分
如果 ak == bk == 0 ，那么无人得到 k 分。
例如，Alice 和 Bob 都向计分为 11 的区域射 2 支箭，那么 Alice 得 11 分。如果 Alice 向计分为 11 的区域射 0 支箭，但 Bob 向同一个区域射 2 支箭，那么 Bob 得 11 分。

给你整数 numArrows 和一个长度为 12 的整数数组 aliceArrows ，该数组表示 Alice 射中 0 到 11 每个计分区域的箭数量。现在，Bob 想要尽可能 最大化 他所能获得的总分。

返回数组 bobArrows ，该数组表示 Bob 射中 0 到 11 每个 计分区域的箭数量。且 bobArrows 的总和应当等于 numArrows 。

如果存在多种方法都可以使 Bob 获得最大总分，返回其中 任意一种 即可。

 

示例 1：

![](image1.png)

输入：numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
输出：[0,0,0,0,1,1,0,0,1,2,3,1]
解释：上表显示了比赛得分情况。
Bob 获得总分 4 + 5 + 8 + 9 + 10 + 11 = 47 。
可以证明 Bob 无法获得比 47 更高的分数。
示例 2：

![](image2.png)

输入：numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]
输出：[0,0,0,0,0,0,0,0,1,1,1,0]
解释：上表显示了比赛得分情况。
Bob 获得总分 8 + 9 + 10 = 27 。
可以证明 Bob 无法获得比 27 更高的分数。
 

提示：

1 <= numArrows <= 105
aliceArrows.length == bobArrows.length == 12
0 <= aliceArrows[i], bobArrows[i] <= numArrows
sum(aliceArrows[i]) == numArrows
'''

from typing import List

class Solution:
    # 超时
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        dp = [([0] * (numArrows + 1)) for _ in range(12)]
        dpr = [([0] * (numArrows + 1)) for _ in range(12)]
        for i in range(1, 12):
            j = numArrows
            while j >= 0:
                if j >= aliceArrows[i] + 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - aliceArrows[i] - 1] + i)
                    if dp[i][j] == dp[i - 1][j - aliceArrows[i] - 1] + i:
                        dpr[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j]
                j -= 1
        j = numArrows
        res = [0] * 12
        k = 0
        for i in range(11, 0, -1):
            if dpr[i][j]:
                x = aliceArrows[i] + 1
                res[i] = x
                j -= x
                k += x
        res[0] = numArrows - k
        return res


class Solutionc:
    '''
    超时
    '''
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        dp = [([0] * (numArrows + 1)) for _ in range(12)]
        dpr = [([0] * (numArrows + 1)) for _ in range(12)]
        for i in range(1, l):
            for j in range(numArrows + 1):
                v = aliceArrows[i]
                p = i
                if v == 0:
                    if j >= 1:
                        if dp[i - 1][j - 1] + p >= dp[i - 1][j]:
                            dp[i][j] = dp[i - 1][j - 1] + p
                            dpr[i][j] = 1
                        else:
                            dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if j - v >= 1:
                        if dp[i - 1][j - v - 1] + p >= dp[i - 1][j]:
                            dp[i][j] = dp[i - 1][j - v - 1] + p
                            dpr[i][j] = v + 1
                        else:
                            dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]
        c = numArrows
        res = [0] * 12
        i = 11
        while i >= 0 and c >= 0:
            res[i] = dpr[i][c]
            c -= res[i]
            i -= 1
        res[0] = c
        return res

s = Solution()
l = [1,1,0,1,0,0,2,1,0,1,2,0]
print(s.maximumBobPoints(9, l))
print(s.maximumBobPoints(3, [0,0,1,0,0,0,0,0,0,0,0,2]))
print(s.maximumBobPoints(89,[3,2,28,1,7,1,16,7,3,13,3,5]))

