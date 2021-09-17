class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        res = 0
        r = 10
        if k >= 9:
            r = (k - 7) * 10
        for i in range(m):
            j = 0
            while j < n and i + j < r:
                si = i // 100 + i // 10 + i % 10
                sj = j // 100 + j // 10 + j % 10
                if si + sj <= k:
                    res += 1
                j += 1
        return res

class Solution2:
    def movingCount(self, m: int, n: int, k: int) -> int:
        self.vis = [([False] * n) for _ in range(m)]
        self.m = m
        self.n = n
        self.k = k
        return self.dfs(0, 0)
        
    def dfs(self, x, y):
        if x >= self.m or y >= self.n or self.vis[x][y] or x % 10 + x // 10 + y % 10 + y // 10 > self.k:
            return 0
        self.vis[x][y] = True
        return 1 + self.dfs(x + 1, y) + self.dfs(x, y + 1) 


