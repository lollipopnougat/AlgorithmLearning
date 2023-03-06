from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in nums:
            res *= i
        if res == 0:
            return 0
        elif res > 0:
            return 1
        else:
            return -1