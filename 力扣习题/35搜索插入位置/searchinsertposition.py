class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        return len([i for i in nums if i < target])

class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i + 1