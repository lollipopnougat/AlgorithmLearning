from tkinter import SOLID
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        fl, sl = len(firstList), len(secondList)
        res = []
        while i < fl and j < sl:
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif firstList[i][0] > secondList[j][1]:
                j += 1
            elif firstList[i][0] <= secondList[j][0] and secondList[j][1] <= firstList[i][1]:
                res.append([secondList[j][0], secondList[j][1]])
                j += 1
            elif secondList[j][0] <= firstList[i][0] and firstList[i][1] <= secondList[j][1]:
                res.append([firstList[i][0], firstList[i][1]])
                i += 1
            elif firstList[i][0] <= secondList[j][0] <= firstList[i][1] and secondList[j][1] >= firstList[i][1]:
                res.append([secondList[j][0], firstList[i][1]])
                i += 1
            elif secondList[j][0] <= firstList[i][0] <= secondList[j][1] and firstList[i][1] >= secondList[j][1]:
                res.append([firstList[i][0], secondList[j][1]])
                j += 1
        return res


s = Solution()
li1 = [[0, 2], [5, 10], [13, 23], [24, 25]]
li2 = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(s.intervalIntersection(li1, li2))
li1 = [[3,10]]
li2 = [[5,10]]
print(s.intervalIntersection(li1, li2))
