from typing import List
import collections
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        map = collections.Counter()
        for a, b in items1:
            map[a] += b
        for a, b in items2:
            map[a] += b
        return sorted([a, b] for a, b in map.items())
s