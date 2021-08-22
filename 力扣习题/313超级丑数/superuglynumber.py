from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 超时.....
        res = [1]
        l = len(primes)
        index = [0] * l
        i = 0
        while len(res) < n:
            tmp = []
            t = (float('inf'), -1)
            for j in range(l):
                tmp.append(res[index[j]] * primes[j])
                if tmp[-1] < t[0]:
                    t = (tmp[-1], j)
            if not t[0] in res:
                res.append(t[0])
            index[t[1]] += 1
            i += 1
        return res[-1]

s = Solution()

li = [2, 7, 13, 19]

print(s.nthSuperUglyNumber(12, li))
