from typing import List
import math
class Solution:
    def findEarliestMonth(self, sp: List[int]):
        n = len(sp)
        su = [0] * n
        su[0] = sp[0]
        for i in range(1, n):
            su[i] = su[i - 1] + sp[i]
        mi = float('inf')
        res = -1
        for i in range(1, n):
            t = abs(su[i - 1] / i - (su[-1] - su[i - 1]) / (n - i))
            if mi > t:
                mi = t
                res = i
        return res

s = Solution()

print(s.findEarliestMonth([1, 3, 2, 4, 5]))
print(s.findEarliestMonth([1, 1, 1, 1, 1]))