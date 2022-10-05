from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        ans = 0
        for i in range(n - 2):
            target = nums[i + 1] - nums[i]
            for j in range(i + 1, n - 1):
                if nums[j + 1] - nums[j] == target:
                    ans += 1
                else:
                    break
        return ans

class Solution2:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [([0] * n) for _ in range(n)]
        if n < 3:
            return 0
        for i in range(n - 2):
            ld = nums[i + 1] - nums[i]
            for j in range(i + 2, n):
                d = nums[j] - nums[j - 1]
                if ld == d:
                    dp[i][j] = dp[i][j] + dp[i][j - 1] + 1
                    ld = d
                else:
                    dp[i][j] = dp[i][j] + dp[i][j - 1]
                    for k in range(j + 1, n):
                        dp[i][k] = dp[i][k] + dp[i][k - 1]
                    break
        res = 0
        for i in range(n):
            res += dp[i][n - 1]
        return res

s = Solution()

print(s.numberOfArithmeticSlices([1, 2, 3, 4]))
print(s.numberOfArithmeticSlices([1, 2, 3, 4, 5]))
print(s.numberOfArithmeticSlices([1, 2, 3, 8, 9, 10]))
