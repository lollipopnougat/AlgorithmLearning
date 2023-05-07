import math


class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        j并不是从2*i开始，而是i*i开始，i也不需要到n，到sqrt(n)即可
        '''
        if n == 0 or n == 1:
            return 0
        p = [1] * n
        i = 2
        while i * i < n:
            if p[i]:
                for j in range(i * i, n, i):
                    p[j] = 0
            i += 1
        return p[2:n].count(1)

s = Solution()

print(s.countPrimes(10))