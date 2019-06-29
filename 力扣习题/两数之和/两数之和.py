# -*- coding=utf-8 -*-
# 两数之和
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if target-nums[i]==nums[j]:
                    return [i,j]
                else:
                    return [-1,-1]
'''


#  我的原解答：平均 6000ms
class Solutiono:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                #print("nums[%d] = %d,num[%d] = %d" %(i,nums[i],j,nums[j]))
                if (target - nums[i]) == nums[j]:
                    return [i, j]
        return [-1, -1]


#  后期优化： 平均1000ms
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            j = target - nums[i]
            if j in nums[i + 1:]:
                return [i, i + 1 + nums[i + 1:].index(j)]
        return [-1, -1]


#  leetcode上的大佬：
class Solution2:
    def twoSum(self, nums: list, target: int) -> list:
        map = {}
        for i, j in enumerate(nums):
            if j in map and i != map[j][1]:
                return [map[j][1], i]
            else:
                map[target - j] = (j, i)


s = Solution()
print(s.twoSum([3,2,4], 6))
input()