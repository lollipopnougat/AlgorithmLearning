from typing import List
import heapq


class Solution:
    def nthSuperUglyNumbern(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        dp[0] = 1
        l = len(primes)
        index = [0] * l
        i = 0
        for i in range(n - 1):
            m = float('inf')
            for j in range(l):
                m = min(m, primes[j] * dp[index[j]])
            dp[i + 1] = m
            for j in range(l):
                if primes[j] * dp[index[j]] == m:
                    index[j] += 1
        return dp[-1]

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # dp
        l = len(primes)
        index = [0] * l
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            m = float('inf')
            for j in range(l):
                m = min(m, primes[j] * dp[index[j]])
            dp[i] = m
            for j in range(l):
                if m == primes[j] * dp[index[j]]:
                    index[j] += 1
        return dp[n - 1]

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 优先队列
        dp = [1]
        his = {1}
        heap = []

        for prime in primes:
            heapq.heappush(heap, (prime, 0, prime))
            his.add(prime)

        for i in range(1, n):
            num, j, prime = heapq.heappop(heap)
            dp.append(num)
            while num in his:
                num = dp[j] * prime
                j += 1
            heapq.heappush(heap, (num, j, prime))
            his.add(num)

        return dp[-1]


class Solution2():
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

    def nthSuperUglyNumbern(self, n: int, primes: List[int]) -> int:
        # yes!
        res = [0] * n
        res[0] = 1
        l = len(primes)
        tmp = primes[:]
        index = [0] * l
        for i in range(1, n):
            res[i] = min(tmp)
            for j in range(l):
                if tmp[j] == res[i]:
                    index[j] += 1
                    tmp[j] = res[index[j]] * primes[j]
        return res[-1]

class Solution3:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 因为每一个超级丑数只能由质数列表中的质数组合而成，因此可以考虑递推的方法。
        # 第一个丑数必然是1，将其加入超级丑数列表。
        # 此时，下一个超级丑数只能由第一个丑数与质数列表中各个质数乘积的最小者形成。
        # 但此后情况会变得复杂，为防止重复计算，
        # 应该记录与各个质数相乘（用于得到下一个超级丑数的候选值）的已知超级丑数的位置，
        # 当然初始时都是超级丑数1对应的位置。
        # 当计算得到一个超级丑数后，应该更新那些位置，以防止同一个超级丑数被生成两次。
        # 这样递推下去，即可得到第n个超级丑数。

        m = len(primes)
        dp = [1 for _ in range(n)]
        cand = primes[::]
        pos = [0 for _ in range(m)]

        for i in range(1, n):
            dp[i] = min(cand)
            for k in range(m):
                if cand[k] == dp[i]:
                    pos[k] += 1
                    cand[k] = dp[pos[k]] * primes[k]

        return dp[-1]
s = Solution2()

li = [2, 7, 13, 19]

print(s.nthSuperUglyNumbern(17, li))
