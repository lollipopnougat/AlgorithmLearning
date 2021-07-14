from typing import List
class Solution:
    # 一边读后面的，一边往前面填
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for e in nums:
            if i < 2 or e > nums[i - 2]:
                nums[i] = e
                i += 1
        return i

class Solution2:
    # 抖机灵
    def removeDuplicates(self, nums: List[int]) -> int:
        count = i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                count = 1
                i += 1
            elif count == 2:
                nums.pop(i)
            else:
                count += 1
                i += 1
        return len(nums)

        




