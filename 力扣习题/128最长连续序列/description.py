from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        res = 0
        val = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] - nums[i - 1] != 1:
                res = max(res, val)
                val = 1
            else:
                val += 1
        res = max(res, val)
        return res


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
