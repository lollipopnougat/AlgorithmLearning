from typing import List


class Solutiond:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.le = len(nums)
        return self.qselect(nums, k, 0, self.le - 1)

    def qselect(self, nums: List[int], k: int, l: int, r: int) -> int:
        if l < r:
            ll = l
            lr = r
            c = nums[l]
            while l < r:
                while l < r and nums[r] >= c:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] <= c:
                    l += 1
                nums[r] = nums[l]
            nums[l] = c
            if self.le - k == l:
                return nums[l]
            elif l > self.le - k:
                return self.qselect(nums, k, ll, l - 1)
            else:
                return self.qselect(nums, k, l + 1, lr)
        elif l == r:
            return nums[l]


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
