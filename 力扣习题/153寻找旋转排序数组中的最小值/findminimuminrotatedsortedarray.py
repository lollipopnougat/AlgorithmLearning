from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 1
        le = len(nums)
        if le == 1:
            return nums[0]
        while nums[i] > nums[i - 1]:
            i += 1
            if i == le:
                return nums[0]
        return nums[i]


class Solutiond:
    # 击败83%(草)
    def findMin(self, nums: List[int]) -> int:
        return min(nums)