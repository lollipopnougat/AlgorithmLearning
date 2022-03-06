from typing import List
from functools import cmp_to_key
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        s = sorted(properties, key=cmp_to_key(lambda x, y: (y[0] - x[0]) if x[0] != y[0] else (x[1] - y[1])))
        l = len(properties)
        ma = s[0][1]
        count = 0
        for i in range(1, l):
            if s[i][1] < ma:
                count += 1
                continue
            ma = max(ma, s[i][1])
        return count                 
s = Solution()
# print(s.numberOfWeakCharacters([[1,5],[10,4],[4,3]]))
# print(s.numberOfWeakCharacters([[5,5],[6,3],[3,6]]))
# print(s.numberOfWeakCharacters([[2,2],[3,3]]))
# print(s.numberOfWeakCharacters([[2,2],[3,3],[4,4],[5,15]]))
print(s.numberOfWeakCharacters([[1,1],[2,1],[2,2],[1,2]]))