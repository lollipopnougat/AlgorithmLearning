from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return max(nums)
        qu1 = nums[0:l - 1]
        qu2 = nums[1:l]
        last1 = now1 = 0
        for i in qu1:
            last1, now1 = now1, max(last1 + i, now1)
        last = now = 0
        for i in qu2:
            last, now = now, max(last + i, now)
        return max(now, now1)