class Node:
    linked_nodes = []
    name = ''

    def __init__(self, myname: str):
        self.name = myname

    def is_linked(self, ndnm: str):
        return ndnm in self.linked_nodes


class Graph:
    node_map = {}
    edge_map = {}

    def __init__(self, node: Node = None):
        if node:
            self.add_node(node)

    def has_node(self, ndnm: str) -> bool:
        return ndnm in self.node_map

    def add_nodeo(self, node: Node) -> bool:
        if not self.has_node(node.name):
            self.node_map[node.name] = node
            self.edge_map[(node.name, node.name)] = 0
            return True
        return False

    def add_node(self, name: str) -> bool:
        if not self.has_node(name):
            new_one = Node(name)
            self.edge_map[(name, name)] = 0
            return self.add_nodeo(new_one)
        return False

    def add_nodes(self, node_name_list: list) -> bool:
        for i in node_name_list:
            if self.has_node(i):
                return False
        for i in node_name_list:
            self.add_node(i)
        return True

    def add_edge(self, ndnm1: str, ndnm2: str, w: int or float = 1):
        if not self.is_linked(ndnm1, ndnm2):
            self.edge_map[(ndnm1, ndnm2)] = w
            self.edge_map[(ndnm2, ndnm1)] = w
            self.node_map[ndnm1].linked_nodes.append(ndnm2)
            self.node_map[ndnm2].linked_nodes.append(ndnm1)

    def is_linked(self, ndnm1: str, ndnm2: str) -> bool:
        return (ndnm1, ndnm2) in self.edge_map

    def get_edge_weight(self, ndnm1: str, ndnm2: str):
        res = float('inf')
        if self.is_linked(ndnm1, ndnm2):
            res = self.edge_map[(ndnm1, ndnm2)]
        return res

    def cut_off_nodes(self, ndnm1: str, ndnm2: str):
        if not self.is_linked(ndnm1, ndnm2):
            self.edge_map.pop((ndnm1, ndnm2))
            self.edge_map.pop((ndnm2, ndnm1))
            self.node_map[ndnm1].linked_nodes.remove(ndnm2)
            self.node_map[ndnm2].linked_nodes.remove(ndnm1)

    def get_nodes_nums(self) -> int:
        return len(self.node_map)

    def dfs(self, ndnm: str):
        res = []
        if self.has_node(ndnm):
            vistied = set()
            stack = [ndnm]
            while len(stack) != 0:
                ndnm = stack.pop()
                tmp_node = self.node_map[ndnm]
                if not ndnm in vistied:
                    res.append(tmp_node)
                    stack.extend(tmp_node.linked_nodes)
                    vistied.add(ndnm)
        return res

    def bfs_edge_set(self, ndnm:str):
        res = []
        if not self.has_node(ndnm):
            return res
        queue = [ndnm]
        vis = set()
        #vis.add(ndnm)
        while queue:
            t = queue.pop(0)
            if t in vis:
                continue
            res.append(t)
            vis.add(t)
            for i in self.node_map:
                if not i in vis and i != t and (t, i) in self.edge_map:
                    queue.append(i)
                    
                
        return res
        



    def bfs(self, ndnm: str):
        res = []
        if self.has_node(ndnm):
            vistied = set()
            queue = [ndnm]
            while len(queue) != 0:
                ndnm = queue.pop(0)
                if not ndnm in vistied:
                    tmp_node = self.node_map[ndnm]
                    res.append(tmp_node)
                    queue.extend(tmp_node.linked_nodes)
                    vistied.add(ndnm)
        return res

    def dijkstra(self, s: str):
        S = {}
        if not self.has_node(s):
            return S
        S[s] = 0
        U = {}
        for i in self.node_map:
            if i != s:
                U[i] = self.get_edge_weight(s, i)
        while U:
            mi = None
            for i in U:
                if not mi:
                    mi = i
                    continue
                if U[i] < U[mi]:
                    mi = i
            S[mi] = U.pop(mi)
            for i in U:
                tmp = self.get_edge_weight(i, mi)
                if tmp < float('inf') and tmp + S[mi] < U[i]:
                    U[i] = tmp + S[mi]
        return S

        return res


g = Graph()
g.add_nodes(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 2)
g.add_edge('A', 'D', 7)
g.add_edge('C', 'D', 4)
g.add_edge('C', 'F', 2)
g.add_edge('G', 'F', 6)
g.add_edge('G', 'E', 1)
g.add_edge('D', 'E', 1)

print(g.get_nodes_nums())

res = g.bfs_edge_set('A')
#for i in res:
print(res)
input()
