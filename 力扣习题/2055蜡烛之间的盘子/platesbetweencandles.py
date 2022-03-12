from typing import List
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        n = len(s)
        lcandle = [-1] * n      # lcandle[i] 表示在位置 i 左侧(包括 i )，离 i 最近的蜡烛的位置
        rcandle = [-1] * n      # rcandle[i] 表示在位置 i 右侧(包括 i )，离 i 最近的蜡烛的位置
        prefix_plate = [0] * n  # prefix_plate[i] 表示在位置 i 之前（左侧）的盘子个数

        if s[0] == '|':
            lcandle[0] = 0

        if s[n - 1] == '|':
            rcandle[n - 1] = n - 1

        for i in range(1, n):
            lcandle[i] = i if s[i] == '|' else lcandle[i - 1]

        for i in range(n - 2, -1, -1):
            rcandle[i] = i if s[i] == '|' else rcandle[i + 1]

        for i in range(1, n):
            prefix_plate[i] = prefix_plate[i - 1] + 1 if s[i - 1] == '*' else prefix_plate[i - 1]

        res = []

        for que in queries:
            left, right = que[0], que[1]

            # 首先确定查询区间内，最左侧和最右侧两个蜡烛的位置
            lidx = rcandle[left]    # left 右侧离 left 最近的蜡烛位置
            ridx = lcandle[right]   # right 左侧离 right 最近的蜡烛位置

            if lidx >= right - 1 or ridx <= left + 1:
                res.append(0)  
            else:
                res.append(prefix_plate[ridx] - prefix_plate[lidx])

        return res

inp = '***|**|*****|**||**|*'
qu = [[1,17],[4,5],[14,17],[5,11],[15,16]]

s = Solution()

print(s.platesBetweenCandles(inp, qu))