from typing import List

class Solution:
    '''
    超时...
    '''
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        t = set()
        while nums:
            ma = nums.pop(0)
            t.add(ma)
            if nums and nums[0] in t:
                res += ma + 1 - nums[0]
                nums[0] = ma + 1
        return res

class Solutionn:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        l = len(nums)
        for i in range(1, l):
            if nums[i] <= nums[i - 1]:
                pre = nums[i]
                nums[i] = nums[i - 1] + 1
                res += nums[i] - pre 
        return res

s = Solution()

print(s.minIncrementForUnique([1,1,1,1,1,1]))
print(s.minIncrementForUnique([1,1]))