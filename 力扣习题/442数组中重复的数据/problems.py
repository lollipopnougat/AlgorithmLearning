class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        l = len(nums)
        for i in range(l):
            ind = abs(nums[i])
            if nums[ind - 1] > 0:
                nums[ind - 1] *= -1
            else:
                res.append(ind)
        return res 