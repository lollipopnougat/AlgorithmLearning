class Solution:
    def subsets(self, nums: list) -> list:
        res = [[]]
        l = len(nums)
        for i in range(l):
            t = res[:]
            for j in t: 
                res.append(j + [nums[i]])
        return res

class Solution2:
    def subsets(self, nums: list) -> list:
        res = [[]]
        for i in nums:
            for j in res[:]: 
                res.append(j + [i])
        return res