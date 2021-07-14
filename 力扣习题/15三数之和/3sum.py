from typing import List

class Solutionm:
    # 击败9%(丢人，你给我退出码厂)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = len(nums)
        if l < 3:
            return res
        for i in range(l - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            m = {}
            for j in range(i + 1, l):
                t = -nums[i] - nums[j]
                if t in m:
                    ins = [nums[i], nums[j], t]
                    if not ins in res:
                        res.append(ins)
                m[nums[j]] = j
        return res

class Solutiond:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if n < 3:
            return res
        nums.sort()
        for first in range(n - 2):
            if nums[first] > 0:
                return res
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            left = first + 1
            right = n - 1
            tar = -nums[first]
            while left < right:
                total = nums[left] + nums[right]
                if total == tar:
                    res.append([nums[first],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total > tar:
                    right -= 1
                else:
                    left += 1
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = len(nums)
        if l < 3:
            return res
        for i in range(l - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            m = {}
            for j in range(i + 1, l):
                t = -(nums[i] + nums[j])
                if t in m:
                    ins = [nums[i], t, nums[j]]
                    if not ins in res:
                        res.append(ins)
                m[nums[j]] = j
        return res

s = Solution()

li = [-1,0,1,2,-1,-4]

print(s.threeSum(li))