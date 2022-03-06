from typing import List


class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        if n == 0:
            return [newInterval]
        while i < n and newInterval[0] > intervals[i][0]:
            i += 1
        intervals.insert(i, newInterval)
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


class Solution:
    '''
    超级复杂
    '''
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        l = len(intervals)
        if l == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        elif newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        i = 0
        while i < l and newInterval[0] > intervals[i][1]:
            i += 1
        if i == l:
            intervals.append(newInterval)
            return intervals
        elif intervals[i][0] > newInterval[1]:
            intervals.insert(i, newInterval)
            return intervals
        elif intervals[i][0] == newInterval[1]:
            intervals[i][0] = newInterval[0];
            return intervals
        elif intervals[i][0] > newInterval[0]:
            intervals[i][0] = newInterval[0]
        if intervals[i][1] < newInterval[1]:
            intervals[i][1] = newInterval[1]
            j = i + 1
            while j < len(intervals) and intervals[i][1] >= intervals[j][1]:
                intervals.pop(j)
            if j < len(intervals):
                if intervals[j][0] <= intervals[i][1]:
                    intervals[i][1] = intervals[j][1]
                    intervals.pop(j)
        return intervals
            
s = Solution2()
print(s.insert([[1, 5]], [2, 3]))
print(s.insert([[1, 5]], [0, 3]))
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(s.insert([[1, 3], [6, 9]], [2, 5]))
print(s.insert([[1, 3], [6, 9]], [2, 7]))
print(s.insert([[1, 3], [6, 9]], [4, 5]))
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 12]))
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [10, 12]))
