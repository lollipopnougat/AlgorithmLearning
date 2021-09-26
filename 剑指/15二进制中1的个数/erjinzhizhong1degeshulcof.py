import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 1
        res = 0
        if n == 0:
            return 0
        le = math.floor(math.log(n, 2) + 1)
        for _ in range(le):
            if i & n:
                res += 1
            i <<= 1
        return res

class Solution2:
    '''
    位运算
    '''
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n & (n - 1)
            res += 1
        return res

    def hammingWeight2(self, n: int) -> int:
        n = ((n >> 1) & 0x55555555) + (n & 0x55555555)
        n = ((n >> 2) & 0x33333333) + (n & 0x33333333)
        n = ((n >> 4) & 0x0f0f0f0f) + (n & 0x0f0f0f0f)
        n = ((n >> 8) & 0x00ff00ff) + (n & 0x00ff00ff)
        n = ((n >> 16) & 0x0000ffff) + (n & 0x0000ffff)
        return n

s = Solution()

print(s.hammingWeight(0))