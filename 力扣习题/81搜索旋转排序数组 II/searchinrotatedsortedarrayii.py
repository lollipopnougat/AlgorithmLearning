from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        k = 1
        le = len(nums)
        if le < 2:
            return target == nums[0]
        while nums[k] >= nums[k - 1]:
            k += 1
            if k == le:
                k = 0
                break
        if k < le and target == nums[k]:
            return True
        l = k
        r = le + k
        while l <= r:
            m = l + (r - l) // 2
            real = m % le
            if target == nums[real]:
                return True
            elif nums[real] < target:
                l = m + 1
            else:
                r = m - 1
        return False


class Solutionlz:
    def search(self, nums: List[int], target: int) -> bool:
        le = len(nums)
        if le < 2:
            return target in nums
        t = le - 1
        while t > 0 and nums[t] == nums[0]:
            t -= 1
        if t == 0:
            return nums[0] == target
        l = 0
        r = t
        while l < r:
            m = l + r >> 1
            if nums[m] < nums[0]:
                r = m
            else:
                l = m + 1
        if nums[r] >= nums[0]:
                l = 0
        elif target > nums[0]:
            r -= 1
            l = 0
        elif target == nums[0]:
            return True
        else:
            r = t
        while l < r:
            m = l + r >> 1
            if target <= nums[m]:
                r = m
            else:
                l = m + 1
        return nums[r] == target

class Solutiond:
    # 奇怪的姿势

    def search(self, nums: List[int], target: int) -> bool:
        # 直接暴力
        return target in nums

    def s2(self, nums:List[int], target: int) -> bool:
        # 迭代器加速
        it = iter(nums)
        for i in it:
            if target == i:
                return True
        return False
    

    def search3(self, nums: List[int], target: int) -> bool:
        # 排序后二分
        nums.sort()
        le = len(nums)
        l = 0
        r = le - 1
        while l <= r:
            mid = l + r >> 1
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False


li = [2,2,2,3,2,2,2]
li3 = [3,1,1]
li2 = [4,5,6,7,0,1,2]
li3 = [1,2]
t = 3

s = Solutionlz()

print(s.search(li3, 1))
print(s.search(li2, 2))