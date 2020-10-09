# 邻接矩阵
class Graph:
    adjm = None
    node_names = None
    node_nums = 0
    edge_nums = 0

    def __init__(self, n: int = 0):
        self.adjm = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            self.adjm[i][i] = 0
        self.node_names = [str(i) for i in range(n)]
        self.node_nums = n

    @staticmethod
    def buildbylist(lis: list):
        n = len(lis)
        t = Graph(n)
        t.adjm = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            t.adjm[i][i] = 0
        t.node_names = lis[:]
        return t

    def add_edge(self, fr: str, to: str, weight: int):
        i, j = self.node_names.index(fr), self.node_names.index(to)
        if i == -1 or j == -1:
            return False
        self.adjm[i][j] = weight
        self.adjm[j][i] = weight
        self.edge_nums += 1
        return True
    
    def remove_edge(self, fr: str, to: str):
        if self.add_edge(fr, to, float('inf')):
            self.edge_nums -= 1
            return True
        return False

    def add_node(self, name: str):
        if name in self.node_names:
            return False
        self.node_names.append(name)
        for i in range(self.node_nums):
            self.adjm[i].append(float('inf'))
        self.node_nums += 1
        self.adjm.append([float('inf')] * self.node_nums)
        self.adjm[self.node_nums - 1][self.node_nums - 1] = 0
        return True

    def dfs(self, ind: str):
        res = []
        index = self.node_names.index(ind)
        if index == -1:
            return res
        stack = [index]
        while stack:
            tmp = stack.pop()
            if tmp in res:
                continue
            res.append(tmp)

            for i in range(self.node_nums):
                if self.adjm[tmp][i] < float('inf'):
                    stack.append(i)
        return [self.node_names[i] for i in res]

    def dijkstra(self, st_node: str):
        dist = [float('inf')] * self.node_nums
        index = self.node_names.index(st_node)
        if index == -1:
            return dist
        dist[index] = 0
        S = []
        Q = [i for i in range(self.node_nums)]
        dist_init = [i for i in self.adjm[index]]
        while Q:
            u_dist = min([d for v, d in enumerate(dist_init) if v in Q])
            u = dist_init.index(u_dist)

            S.append(u)
            Q.remove(u)

            for v, d in enumerate(self.adjm[u]):
                if 0 < d < float('inf'):
                    if dist[v] > dist[u] + d:
                        dist[v] = dist[u] + d
                        dist_init[v] = dist[v]
        return dist

        


        



g = Graph.buildbylist(lis=['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 2)
g.add_edge('A', 'D', 7)
g.add_edge('C', 'D', 4)
g.add_edge('C', 'F', 2)
g.add_edge('G', 'F', 6)
g.add_edge('G', 'E', 1)
g.add_edge('D', 'E', 1)

print(g.dijkstra('A'))




            


        
        

