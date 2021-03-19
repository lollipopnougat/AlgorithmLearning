from typing import List
import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        for i in arr:
            m[i] = m.get(i, 0) + 1
        s = set()
        for i in m:
            if not m[i] in s:
                s.add(m[i])
            else:
                return False
        return True

class Solution2:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return (lambda c: len(c) == len(set(c)))(collections.Counter(arr).values())

s = Solution()

print(s.uniqueOccurrences([1,2]))