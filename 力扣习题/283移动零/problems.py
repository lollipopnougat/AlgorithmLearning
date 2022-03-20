from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                l -= 1
            else:
                i += 1

class Solutionn:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] == 0:
                j = i + 1
                while j < l and nums[j] == 0:
                    j += 1
                if j < l:
                    nums[i] = nums[j]
                    nums[j] = 0
                    i += 1
                else:
                    break
            else:
                i += 1

s = Solutionn()
li = [0,1,0,3,12]
li = [0]
s.moveZeroes(li)
print(li)