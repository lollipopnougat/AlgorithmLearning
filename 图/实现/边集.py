class Node:
    linked_nodes = []
    name = ''
    def __init__(self, myname:str):
        self.name = myname
    def is_linked(self, ndnm:str):
        return ndnm in self.linked_nodes

class Graph:
    node_map = {}
    edge_list = []

    def __init__(self, node: Node = None):
        if node:
            self.add_node(node)

    def has_node(self, ndnm:str) -> bool:
        return ndnm in self.node_map

    def add_nodeo(self, node: Node) -> bool:
        if not self.has_node(node.name):
            self.node_map[node.name] = node
            return True
        return False
    
    def add_node(self, name: str) -> bool:
        if not self.has_node(name):
            new_one = Node(name)
            return self.add_nodeo(new_one)
        return False
    
    def add_nodes(self, node_name_list:list) -> bool:
        for i in node_name_list:
            if self.has_node(i):
                return False
        for i in node_name_list:
            self.add_node(i)
        return True

    def link_nodes(self, ndnm1:str, ndnm2:str):
        if not self.is_linked(ndnm1, ndnm2):
            self.edge_list.append((ndnm1,ndnm2))
            self.node_map[ndnm1].linked_nodes.append(ndnm2)
            self.node_map[ndnm2].linked_nodes.append(ndnm1)
    
    def is_linked(self, ndnm1:str, ndnm2:str) -> bool:
        return (ndnm1,ndnm2) in self.edge_list

    def cut_off_nodes(self, ndnm1:str, ndnm2:str):
        if not self.is_linked(ndnm1, ndnm2):
            self.edge_list.remove((ndnm1,ndnm2))
            self.node_map[ndnm1].linked_nodes.remove(ndnm2)
            self.node_map[ndnm2].linked_nodes.remove(ndnm1)

    def get_nodes_nums(self) -> int:
        return len(self.node_map)

    def dfs(self, ndnm:str):
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

    def bfs(self, ndnm:str):
        res = []
        if self.has_node(
            ndnm):
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

g = Graph()
g.add_nodes(['A','B','C','D'])
g.link_nodes('A', 'B')
g.link_nodes('A', 'C')
g.link_nodes('B', 'D')
g.link_nodes('C', 'D')

print(g.get_nodes_nums())

res = g.dfs('A')
for i in res:
    print(i.name)
input()









        

