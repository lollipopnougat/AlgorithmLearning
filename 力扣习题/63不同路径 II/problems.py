from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        l = len(obstacleGrid)
        w = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [([0] * w) for _ in range(l)]
        dp[0][0] = 1
        for i in range(l):
            for j in range(w):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j]
                elif i == 0 and j == 0:
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


s = Solution()

print(s.uniquePathsWithObstacles([[1, 0]]))
print(s.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]))
print(s.uniquePathsWithObstacles([[0, 0, 0], [1, 1, 1], [0, 0, 0]]))
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 0, 0]]))
