from typing import List
import random

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

class Solution2:
    '''
    没问题,替换DP中对应位置
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        res = 0
        for i in nums:
            idx = self.binser(dp, 0, res, i)
            idx = -idx - 1 if idx < 0 else idx
            dp[idx] = i
            if idx == res:
                res += 1
        return res
    def binser(self, nums: List[int], l: int, r: int, val: int) -> int:
        while l < r:
            m = (l + r) // 2
            if val <= nums[m]:
                r = m
            else:
                l = m + 1
        return l

def gen(l: int) -> List[int]:
    tmp = [0] * l
    for i in range(l):
        tmp[i] = random.randint(-10, 10)
    return tmp

s = Solution2()

print([4, 10, 4, 3, 8, 9])
print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))
res1 = gen(5)
print(res1)
print(s.lengthOfLIS(res1))
res2 = gen(7)
print(res2)
print(s.lengthOfLIS(res2))
res3 = gen(6)
print(res3)
print(s.lengthOfLIS(res3))