# 
from typing import List
class Solution:
    # 暴力
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        tmp = [-1, -1]
        l = len(nums)
        
        if l > 0 and nums[0] <= target <= nums[-1]:
            for i in range(l):
                if nums[i] == target and tmp[0] == -1:
                    tmp[0] = i
                elif nums[i] == target and tmp[0] != -1:
                    tmp[1] = i
                elif i > 0 and nums[i - 1] == target:
                    tmp[1] = i - 1
            if tmp[0] != -1 and tmp[1] == -1:
                tmp[1] = l - 1
        return tmp

class Solution2:
    # 二分
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        tmp = [-1, -1]
        length = len(nums)
        l, r = 0, length - 1
        while l < length and nums[l] != target:
            l += 1
        if l == length:
            return tmp
        while r >= 0 and nums[r] != target:
            r -= 1
        if r == -1:
            return tmp
        return [l, r]

s = Solution2()

print(s.searchRange([1,3,3], 1))
print(s.searchRange([1,1], 1))
print(s.searchRange([1, 1, 2], 1))
print(s.searchRange([1], 1))
print(s.searchRange([1,1,1,1], 1))
