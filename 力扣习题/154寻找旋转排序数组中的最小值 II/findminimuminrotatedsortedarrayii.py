from typing import List
class Solution:
    '''
    和 I 的做法类似, 都是二分法, 每次进入无序的那部分找出最小值
        但是由于有重复值的情况, 需要加入 mid 元素等于 hi 元素的情况
        此时应该将 hi 减 1 防止重复数字是最小元素
    '''
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        return nums[r]


class Solutiond:
    # 击败87%(草草草)
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
    