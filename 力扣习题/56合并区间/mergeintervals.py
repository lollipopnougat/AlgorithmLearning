from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        if n < 2:
            return intervals
        res = []
        p = intervals[0]
        for i in intervals[1:]:
            if p[1] < i[0]:
                res.append(p)
                p = i
            elif i[1] > p[1]:
                p[1] = i[1]
        res.append(p)
        return res