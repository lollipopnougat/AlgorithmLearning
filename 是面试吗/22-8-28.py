from typing import List
class Solution:
    def Find(self, n: int, m: int):
        if n > m:
            return m
        i = n
        c = 2
        while i < m:
            c += 1
            i += (1 + c // 3)
        return (c + 1) % 3

s = Solution()
print(s.Find(3, 10))
