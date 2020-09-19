class Solution:
    def minPathSum(self, grid: list) -> int:
        '''
        动态规划
        '''
        m = len(grid[0])
        n = len(grid)
        dp = [i[:] for i in grid]
        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])
                elif i > 0 and j == 0:
                        dp[i][j] += dp[i - 1][j]
                elif i == 0 and j > 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[n - 1][m - 1]



s = Solution()

print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))