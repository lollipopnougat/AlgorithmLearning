from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = len(nums)
        s = 0
        res = 0
        i = 0
        for j in range(i, l):
            s += nums[j]
            while s >= target:
                res = (j - i + 1) if res == 0 else min(res, j - i + 1)
                s -= nums[i]
                i += 1
        return res

class Solutiono:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        6000ms O(n^2)
        '''
        l = len(nums)
        ps = [0] * l
        ps[0] = nums[0]
        for i in range(1, l):
            ps[i] = ps[i - 1] + nums[i]
        for i in range(1, l + 1):
            if ps[i - 1] >= target:
                return i
            for j in range(l - i):
                if ps[i + j] - ps[j] >= target:
                    return i
        return 0

s = Solution()

print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(4, [1,4,4]))
print(s.minSubArrayLen(11, [1,1,1,1,1,1]))
print(s.minSubArrayLen(11, [3,1,8,1,1,1]))
print(s.minSubArrayLen(8, [3,1,8,7,1,1]))