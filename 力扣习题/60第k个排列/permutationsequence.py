import itertools
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = ''
        l = list(range(1, n + 1))
        cur = k - 1
        for i in range(n):
            every_count = math.factorial(len(l) - 1) 
            pos = cur // every_count 
            s += str(l[pos])
            l.pop(pos)
            cur = cur % every_count 
        return s

class Solutiontl:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i + 1) for i in range(n)]
        li = itertools.permutations(nums)
        j = 0
        for i in li:
            if j < k - 1:
                j += 1
                continue
            else:
                return ''.join(i)

