from typing import List


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        i = 0
        il = len(intervals)
        while i < il and intervals[i][1] < newInterval[0]:
            i += 1
        if intervals[i][0] < newInterval[0]:
            intervals[i][1] = newInterval[1]
            if i < il - 1 and intervals[i + 1][0] <= newInterval[1]:
                intervals[i][1] = intervals[i + 1][1]
                intervals.pop(i + 1)
                return intervals
        else:
            intervals.insert(i, newInterval)
        return intervals


s = Solution()

print(s.insert([[1, 3], [6, 9]], [2, 5]))
print(s.insert([[1, 3], [6, 9]], [2, 7]))
print(s.insert([[1, 3], [6, 9]], [4, 5]))
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
