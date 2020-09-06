class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        眼熟不？ 就是斐波那契数列哦
        '''
        if n <= 2:
            return n
        i1 = 1
        i2 = 2
        for i in range(n - 2):
            tmp = i1 + i2
            i1 = i2
            i2 = tmp
        return i2