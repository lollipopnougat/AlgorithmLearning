from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        st = zero = nums.count(0)
        le = len(nums)
        last = nums[st]
        i = st + 1
        while i < le:
            if nums[i] - last > 1:
                if zero > 0:
                    last += 1
                    zero -= 1
                else:
                    return False
            elif nums[i] - last == 1:
                last = nums[i]
                i += 1
            else:
                return False
        return True