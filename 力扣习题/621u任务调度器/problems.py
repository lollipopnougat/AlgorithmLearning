from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = {}
        for i in tasks:
            taskMap[i] = taskMap.get(i, 0) + 1
        pass



s = Solution()
print(s.leastInterval(['a', 'a', 'a', 'b', 'b', 'b'], 2))