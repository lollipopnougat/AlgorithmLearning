from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        queue = deque()
        l = len(isConnected)
        vis = [False for _ in range(l)]
        for i in range(l):
            if vis[i]:
                continue
            vis[i] = True
            res += 1
            for j in range(l):
                if isConnected[i][j] == 1 and not vis[j]:
                    queue.append(j)
            while queue:
                t = queue.popleft()
                vis[t] = True
                for j in range(l):
                    if isConnected[t][j] == 1 and not vis[j]:
                        queue.append(j)
        return res


class Solutionrn:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        queue = deque()
        l = len(isConnected)
        vis = set()
        for i in range(l):
            if i in vis:
                continue
            res += 1
            queue.append(i)
            while queue:
                t = queue.popleft()
                vis.add(t)
                for j in range(l):
                    if isConnected[t][j] == 1 and j not in vis:
                        queue.append(j)
        return res

class Solutionn:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        self.ic = isConnected
        self.cities = len(isConnected)
        self.visited = set()
        provinces = 0

        for i in range(self.cities):
            if i not in self.visited:
                self.dfs(i)
                provinces += 1
        
        return provinces
    def dfs(self, i: int):
            for j in range(self.cities):
                if self.ic[i][j] == 1 and j not in self.visited:
                    self.visited.add(j)
                    self.dfs(j)

li = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
l2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
l5 = [[1, 0, 1, 0, 0], [0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 0, 0, 1, 0],
      [0, 1, 0, 0, 1]]
l6 = [[1, 0, 1, 0, 0], [0, 1, 0, 0, 1], [1, 0, 1, 1, 0], [0, 0, 1, 1, 0],
      [0, 1, 0, 0, 1]]
s = Solutionrn()

print(s.findCircleNum(li))
print(s.findCircleNum(l2))
print(s.findCircleNum(l5))
print(s.findCircleNum(l6))