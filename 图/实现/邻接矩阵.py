# 邻接矩阵


class Graph:
    adjm = None
    name = None
    node_nums = 0
    edge_nums = 0

    def __init__(self, n: int):
        self.adjm = [[0] * n for _ in range(n)]
        self.name = [str(i) for i in range(n)]
        self.node_nums = n

    def __init__(self):
        pass

    def __init__(self, lis: list):
        n = len(lis)
        self.adjm = [[0] * n for _ in range(n)]
        self.name = [i for i in lis]
        self.node_nums = n

    def add_edge(self, fr: str, to: str, weight: int):
        i, j = self.name.index(fr), self.name.index(to)
        if i == -1 and j == -1:
            return False
        self.adjm[i][j] = weight
        self.adjm[j][i] = weight
        self.edge_nums += 1
        return True
    
    def remove_edge(self, fr: str, to: str):
        tmp = self.add_edge(fr, to, 0)
        self.edge_nums -= 2
        return tmp

    def add_node(self, name: str):
        if name in self.name:
            return False
        self.name.append(name)
        for i in range(self.node_nums):
            self.adjm[i].append(0)
        self.node_nums += 1
        self.adjm.append([0] * self.node_nums)
        return True

    def dfs(self, ind: str):
        res = []
        if ind not in self.name:
            return res
        index = self.name.index(ind)
        stack = []
        stack.append(index)
        while len(stack) != 0:
            tmp = stack.pop()
            if tmp in res:
                continue
            else:
                res.append(tmp)

            for i in range(self.node_nums):
                if self.adjm[tmp][i] > 0:
                    stack.append(i)
        return [self.name[i] for i in res]

    def dijkstra(self, ind: str):
        res = {}
        if ind not in self.name:
            return res
        index = self.name.index(ind)
        dis = [32768] * self.node_nums
        dis[index] = 0
        for j in range(self.node_nums):
            mint = 1000000
            for i in range(self.node_nums):
                if self.adjm[index][i] > 0 and self.adjm[index][i] < mint:
                    mint = self.adjm[index][i]
            if mint == 1000000:
                pass
            dis.append(self.adjm[index][mint])
            S.append(mint)



g = Graph(lis=['A','B','C','D'])
    
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 2)
g.add_edge('A', 'D', 7)
g.add_edge('C', 'D', 4)

print(g.dfs('A'))




            


        
        

