from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        用栈暂存需要更新的下标
        '''
        n = len(temperatures)
        stk = [0]
        res = [0] * n
        for i in range(1, n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                k = stk.pop()
                res[k] = i - k
            stk.append(i)
        return res


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([10, 9, 7, 8, 4, 2, 3, 1]))
