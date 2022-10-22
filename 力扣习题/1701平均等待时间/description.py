from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        cur = customers[0][0]
        res = 0
        for i in customers:
            if cur < i[0]:
                cur = i[0] + i[1]
            else:
                cur += i[1]
            res += cur - i[0]
        return res / n


s = Solution()
print(s.averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
print(s.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))
