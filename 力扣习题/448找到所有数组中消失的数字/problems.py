from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        al = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in al:
                res.append(i)
        return res