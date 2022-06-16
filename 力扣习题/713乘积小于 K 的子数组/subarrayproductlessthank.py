from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = len(nums)
        s = 1
        # res = []
        res = 0
        for i in range(l):
            if nums[i] < k:
                # res.append([nums[i]])
                res += 1
            s = nums[i]
            for j in range(i + 1, l):
                s *= nums[j]
                if s < k:
                    # res.append(nums[i: j + 1])
                    res += 1
                else:
                    break
        return res

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        cur = 1
        left = 0
        n = len(nums)
        res = 0
        for right in range(n):
            cur *= nums[right]
            while cur >= k:
                cur //= nums[left]
                left += 1
            res += right - left + 1
        return res




s = Solution()

print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
