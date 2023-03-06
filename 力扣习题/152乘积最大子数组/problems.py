from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        求最大值，可以看成求被0拆分的各个子数组的最大值。

        当一个数组中没有0存在，则分为两种情况：

        1.负数为偶数个，则整个数组的各个值相乘为最大值；

        2.负数为奇数个，则从左边开始，乘到最后一个负数停止有一个“最大值”，从右边也有一个“最大值”，比较，得出最大值。
        '''
        n = len(nums)
        r = 1
        ma = nums[0]
        for i in nums:
            r *= i
            ma = max(ma, r)
            if i == 0:
                r = 1
        r = 1
        for i in range(n - 1, -1, -1):
            r *= nums[i]
            ma = max(ma, r)
            if nums[i] == 0:
                r = 1
        return ma

        
