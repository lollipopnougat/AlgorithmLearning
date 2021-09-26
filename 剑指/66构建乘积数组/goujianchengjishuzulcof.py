from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        b = [0] * n
        pr = 1
        # 先左累乘
        for i in range(n):
            b[i] = pr
            pr *= a[i]
        pr = 1
        # 再右累乘
        for i in range(n - 1, -1, -1):
            b[i] *= pr
            pr *= a[i]
        return b