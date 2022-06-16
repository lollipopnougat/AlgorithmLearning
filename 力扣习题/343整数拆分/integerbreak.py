class Solution:
    '''
    数学方法 贪心
    '''
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        a = 1
        while n > 4:
            n = n - 3
            a = a * 3
        return a * n

class Solution2:
    def integerBreak(self, n: int) -> int:
        return [0, 0, 1, 2, 4, 6, 9, 12, 18, 27, 36, 54, 81, 108, 162, 243, 324, 486, 729, 972, 1458, 2187, 2916, 4374, 6561, 8748, 13122, 19683, 26244, 39366, 59049, 78732, 118098, 177147, 236196, 354294, 531441, 708588, 1062882, 1594323, 2125764, 3188646, 4782969, 6377292, 9565938, 14348907, 19131876, 28697814, 43046721, 57395628, 86093442, 129140163, 172186884, 258280326, 387420489, 516560652, 774840978, 1162261467, 1549681956, 2324522934][n]

class Solutionnn:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i - 1, 0, -1):
                dp[i] = max(dp[i], dp[j] * (i - j))
                dp[i] = max(dp[i], j * (i - j))
        return dp[n]

class Solutionrr:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0: 
            return 3 ** a
        if b == 1: 
            return 3 ** (a - 1) * 4
        return 3 ** a * 2