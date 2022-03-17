from typing import List
class Solutiondp:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        dp = [[0, 0] for _ in range(l)]
        dp[0][0] = height[0]
        dp[l - 1][1] = height[l - 1]
        for i in range(1, l):
            dp[i][0] = max(dp[i - 1][0], height[i])
            dp[l - i - 1][1] = max(dp[l - i][1], height[l - i - 1])
        res = 0
        for i in range(1, l - 1):
            res += min(dp[i][0], dp[i][1]) - height[i]
        return res

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = h1 = h2 = 0
        l = len(height)
        for i in range(l):
            h1 = max(h1, height[i])
            h2 = max(h2, height[-i - 1])
            ans += (h1 + h2 - height[i])
        return  ans - l * h1

s = Solution()

print(s.trap([4,2,0,3,2,5]))
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))