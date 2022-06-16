from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums) - 1)

    def helper(self, nums: List[int], target, l: int, h: int) -> int:
        le = h - l + 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return m
            elif nums[m] <= nums[h]:
                if nums[m] < target <= nums[h]:
                    return self.binser(nums, target, m + 1, h)
                else:
                    return self.helper(nums, target, l, m - 1)
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    return self.binser(nums, target, l, m - 1)
                else:
                    return self.helper(nums, target, m + 1, h)
        return -1
    def binser(self, nums: List[int], target, l: int, h: int) -> int:
        le = h - l + 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                h = m - 1
            else:
                l = m + 1
        return -1

class Solutionr:
    '''
    纯纯的抖机灵
    '''
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1

s = Solution()

print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search([4, 5, 6, 0, 1, 2, 3], 0))
print(s.search([1], 0))
