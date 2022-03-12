from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 2:
            return
        for i in range(l - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                mi = float('inf')
                for j in range(l - 1, i, -1):
                    if nums[j] > nums[i] and nums[j] < (mi if mi == mi + 1 else nums[mi]):
                        mi = j
                nums[i], nums[mi] = nums[mi], nums[i]
                self.qsort(nums, i + 1 , l - 1)
                return
        nums.sort()

    def qsort(self, nums:List[int], l: int, h: int) -> None:
        ol = l
        oh = h
        if l < h:
            t = nums[l]
            while l < h:
                while l < h and nums[h] >= t:
                    h -= 1
                nums[l] = nums[h]
                while l < h and nums[l] <= t:
                    l += 1
                nums[h] = nums[l]
            nums[l] = t
            self.qsort(nums, ol, l - 1) 
            self.qsort(nums, l + 1, oh) 

li = [1, 5, 1]

s = Solution()
s.nextPermutation(li)
print(li)