from typing import List
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        res = nums[:]
        n = len(nums)
        if n == 1:
            return nums[-1]
        m = n // 2
        tmp = [0] * m
        for i in range(m):
            if i % 2 == 0:
                tmp[i] = min(nums[2 * i], nums[2 * i + 1])
            else:
                tmp[i] = max(nums[2 * i], nums[2 * i + 1])
        return self.minMaxGame(tmp)