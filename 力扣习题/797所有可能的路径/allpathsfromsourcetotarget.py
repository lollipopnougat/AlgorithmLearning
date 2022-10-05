from typing import List
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.n = len(graph)
        self.bfs(graph, [], 0)
        return self.res

    def bfs(self, graph: List[List[int]], path: List[int], i: int):
        tmp = path[:]
        tmp.append(i)
        if i == self.n - 1:
            self.res.append(tmp)
            return
        for j in graph[i]:
            self.bfs(graph, tmp, j)

class Solution2:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph) 
        qu = deque([(0, [])])
        while qu:
            t = qu.popleft()
            tmp = t[1][:]
            tmp.append(t[0])
            if t[0] == n - 1:
                res.append(tmp)
                continue
            for i in graph[t[0]]:
                qu.append((i, tmp)) 
        return res
s = Solution()
s2 = Solution2()
print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
print(s2.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))