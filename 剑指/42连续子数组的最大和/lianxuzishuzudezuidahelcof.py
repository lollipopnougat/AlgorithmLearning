from typing import List

class Solution:
    def maxSubArraym(self, nums: List[int]) -> int:
        # 状态转移方程 dp[i] = max(dp[i-1] + nums[i], nums[i])
        le = len(nums)
        dp = [0] * le
        dp[0], m = nums[0], nums[0]
        for i in range(1, le):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            m = max(m, dp[i])
        return m

    def maxSubArray(self, nums: List[int]) -> int:
        le = len(nums)
        for i in range(1, le):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)


s = Solution()

li = [-2,1,-3,4,-1,2,1,-5,4]

print(s.maxSubArraym(li))
