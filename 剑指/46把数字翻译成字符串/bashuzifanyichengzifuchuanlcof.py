import math
class Solution:
    def translateNum(self, num: int) -> int:
        nums = list(map(lambda x:int(x), str(num)))
        le = len(nums)
        if le < 2:
            return 1
        dp = [1] * le
        for i in range(1, le):
            if nums[i - 1] == 1 or (nums[i - 1] == 2 and nums[i] < 6):
                t = dp[i - 2]
            else:
                t = 0
            dp[i] = dp[i - 1] + t
        return dp[-1]
        
        
s = Solution()

print(s.translateNum(12258))

