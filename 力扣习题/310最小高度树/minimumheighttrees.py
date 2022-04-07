from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        超时
        '''
        if n == 2:
            return edges[0]
        di = [[] for _ in range(n)]
        for i in edges:
            di[i[0]].append(i[1])
            di[i[1]].append(i[0])
        vis = set()
        tmp = []
        midp = float('inf')
        for i in range(n):
            if len(di[i]) == 1:
                continue
            depth = 1
            vis.clear()
            queue = [(i, depth)]
            madp = 0
            while queue:
                t = queue.pop()
                vis.add(t[0])
                madp = max(madp, t[1])
                for j in di[t[0]]:
                    if not j in vis:
                        queue.append((j, t[1] + 1))
            midp = min(midp, madp)
            tmp.append((madp, i))
        return [i[1] for i in tmp if i[0] == midp]

    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        nice
        '''
        if n == 1:
            return [0]
        di = defaultdict(list)
        degree = [0] * n
        for i in edges:
            di[i[0]].append(i[1])
            di[i[1]].append(i[0])
            degree[i[0]] += 1
            degree[i[1]] += 1
        leaf = deque([i for i in range(n) if degree[i] == 1])
        res = n
        while res > 2:
            length = len(leaf)
            for _ in range(length):
                c = leaf.popleft()
                degree[c] = 0
                res -= 1
                for nxt in di[c]:
                    degree[nxt] = max(degree[nxt] - 1, 0)
                    if degree[nxt] == 1:
                        leaf.append(nxt)
        return list(leaf)
                    
                    

class Solutionn:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [([0] * n) for _ in range(n)]
        l = len(edges)
        for i in range(l):
            g[edges[i][0]][edges[i][1]] = 1
            g[edges[i][1]][edges[i][0]] = 1
        while n > 2:
            pass


class Solution3:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        官方...
        '''
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x
        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]

s = Solution()

print(s.findMinHeightTrees2(4, [[1, 0], [1, 2], [1, 3]]))
print(s.findMinHeightTrees2(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
print(s.findMinHeightTrees2(2, [[0, 1]]))
