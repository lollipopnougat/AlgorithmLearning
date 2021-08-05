from typing import List

N = ['A','B','C','D','E','F','G']


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 动态规划 Dijkstra
        dp = [([float('inf')] * n) for _ in range(n)]
        for s, r, t in times:
            dp[s - 1][r - 1] = t
        dis = dp[k - 1]
        queue = [i for i in range(n) if i != k - 1]
        while queue:
            t = queue[0]
            for i in queue:
                if dis[i] < dis[t]:
                    t = i
            queue.remove(t)
            for i in queue:
                dis[i] = min(dis[t] + dp[t][i], dis[i])
        ans = [i for i in dis if i != float('inf')]
        return max(ans) if len(ans) == n - 1 else -1
        
        
    
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [([0] * n) for _ in range(n)]
        for i in times:
            edges[i[0] - 1][i[1] - 1] = i[2]
        path = {}
        queue = [(k - 1, 0)]
        vis = set()
        while queue:
            t = queue.pop(0)
            if not t[0] in vis:
                vis.add(t[0])
                path[t[0]] = t[1]
                for i in range(n):
                    if edges[t[0]][i] != -1:
                        queue.insert(0, (i, t[1] + edges[t[0]][i]))
            else:
                if path[t[0]] > t[1]:
                    path[t[0]] = t[1]
                    for i in range(n):
                        if edges[t[0]][i] != -1:
                            queue.append((i, t[1] + edges[t[0]][i]))
        if len(path) != n:
            return -1
        return max(path.values())


# li = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
li4 = [[1,2,1],[2,1,3]]
li1 = [[1,2,1],[2,3,2],[1,3,4]]
li2 = [[1,2,1]]
li3 = [[1,2,1],[1,3,1],[2,4,1],[4,5,1],[5,6,1],[6,7,1],[3,7,1]]
li5 = [[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]]
n = 5
k = 3

s = Solution()

print(s.networkDelayTime2(li5, n, k))
