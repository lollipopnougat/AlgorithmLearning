from cgitb import reset
from typing import List
import functools


class Solution:
    def move(self, src: int, tar: int) -> int:
        res = 0
        op = [8, 4, 2]
        while src != tar:
            fl = True
            if tar > src:
                for i in op:
                    t = src * i
                    res += 1
                    if t > tar:
                        res -= 1
                        continue
                    else:
                        src = t
                        fl = False
                        break
            else:
                for i in op:
                    if src % i != 0:
                        continue
                    t = src / i
                    res += 1
                    if t < tar:
                        res -= 1
                        continue
                    else:
                        src = t
                        fl = False
                        break
            if fl:
                return -1
        return res


s = Solution()

print(s.move(3, 6))
print(s.move(16, 2))
print(s.move(12, 4))
print(s.move(1024, 1))
