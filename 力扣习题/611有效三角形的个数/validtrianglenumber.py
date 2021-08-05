from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        le = len(nums)
        for i in range(le - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += (r - 1) - l + 1
                    r -= 1
                else:
                    l += 1
        return res

    def triangleNumbern(self, nums: List[int]) -> int:
        # 暴力 但是超时了
        nums.sort()
        res = 0
        le = len(nums)
        for i in range(le - 2):
            for j in range(i + 1, le - 1):
                for k in range(j + 1, le):
                    if nums[i] + nums[j] > nums[k]:
                        res += 1
        return res
