from typing import List

class Solution:
    '''
    暴力 超时警告
    '''
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        l = len(nums)
        for i in range(l):
            mi = nums[i]
            ma = nums[i]
            for j in range(i + 1, l):
                ma = max(ma, nums[j])
                mi = min(mi, nums[j])
                res += (ma - mi)
        return res

class Solution2:
    '''
    单调栈
    '''
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        minLeft, maxLeft = [0] * n, [0] * n
        minStack, maxStack = [], []
        for i in range(n):
            while minStack and nums[minStack[-1]] > nums[i]:
                minStack.pop()
            minLeft[i] = minStack[-1] if minStack else -1
            minStack.append(i)

            # 如果 nums[maxStack[-1]] == num, 那么根据定义，
            # nums[maxStack[-1]] 逻辑上小于 num，因为 maxStack[-1] < i
            while maxStack and nums[maxStack[-1]] <= nums[i]:
                maxStack.pop()
            maxLeft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)

        minRight, maxRight = [0] * n, [0] * n
        minStack, maxStack = [], []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            # 如果 nums[minStack[-1]] == num, 那么根据定义，
            # nums[minStack[-1]] 逻辑上大于 num，因为 minStack[-1] > i
            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop()
            maxRight[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)

        sumMax, sumMin = 0, 0
        for i in range(n):
            sumMax += (maxRight[i] - i) * (i - maxLeft[i]) * nums[i]
            sumMin += (minRight[i] - i) * (i - minLeft[i]) * nums[i]
        return sumMax - sumMin

s = Solution2()

print(s.subArrayRanges([1,2,3]))