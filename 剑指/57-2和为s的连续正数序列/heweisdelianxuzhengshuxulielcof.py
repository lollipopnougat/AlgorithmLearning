import math
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        hal = target // 2 + 1
        res = []
        for i in range(1, hal):
            n = math.sqrt(target + target + (i + i - 1)**2 / 4) - i + 0.5
            if n - math.floor(n) != 0:
                continue
            res.append([j for j in range(i, i + int(n))])
        return res


class Solutionr:
    '''
    牛哇
    '''
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ma = int(math.sqrt(2 * target))
        res = []
        for n in range(ma, 1, -1):
            t1 = (2 * target + n - n ** 2)
            t2 = 2 * n
            if t1 % t2 == 0:
                i =  t1 // t2
                res.append([i + j for j in range(n)])
        return res

class Solutionn:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        max_n = int(math.sqrt(2 * target))
        res = []
        for n in range(max_n, 1, -1):
            if (2 * target + n - n**2) % (2 * n) == 0:
                a1 = (2 * target + n - n**2) // (2 * n)
                res.append([a1 + i for i in range(n)])
        return res


s = Solutionr()

print(s.findContinuousSequence(9))