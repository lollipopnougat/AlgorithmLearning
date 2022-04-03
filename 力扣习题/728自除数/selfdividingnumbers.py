from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            t = i
            while t:
                tt = t % 10
                if tt == 0 or i % tt != 0:
                    break
                t //= 10
            if t == 0:
                res.append(i)
        return res

s = Solution()

print(s.selfDividingNumbers(1,22))