from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

li0 = [[0,1],[1,0]]
li1 = [[1,3,1],[1,5,1],[4,2,1]]
li2 = [[2,3,5,8],[1,5,1,1],[4,2,1,1],[1,2,2,5]]

s = Solution()
print(s.maxValue(li0))
print(s.maxValue(li1))
print(s.maxValue(li2))
