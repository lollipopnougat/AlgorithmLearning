from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        le = len(nums)
        m = {}
        for i in nums:
            m[i] = m.get(i, 0) + 1
            if m[i] > le // 2:
                return i
        for i in m:
            if m[i] > le // 2:
                return i
        return -1