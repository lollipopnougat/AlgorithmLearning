from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = sorted(nums)
        p = 0
        q = len(nums) - 1
        while p <= q and s[p] == nums[p]:
            p += 1
        while p <= q and s[q] == nums[q]:
            q -= 1
        return q - p + 1
    
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        # O(n)
        le = len(nums)
        if le < 2:
            return 0
        ma = nums[0]
        mi = nums[-1]
        h = 0
        l = le - 1
        for i in range(le):
            ma = max(ma, nums[i])
            mi = min(mi, nums[le - 1 - i])
            if nums[i] < ma:
                h = i
            if nums[le - 1 - i] > mi:
                l = le - 1 - i
        return h - l + 1 if h > l else 0





