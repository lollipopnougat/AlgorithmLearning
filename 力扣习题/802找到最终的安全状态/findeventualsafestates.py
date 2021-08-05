from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.res = set()
        self.graph = graph
        # self.no = set()
        self.l = len(graph)
        self.vis = set()
        for i in range(self.l - 1, -1, -1):
            if i in self.vis:
                continue
            else:
                self.dfs(i)
        return sorted(list(self.res))


    def dfs(self, node: int):
        if node in self.res:
            return True
        # elif node in self.no:
        #     return False
        elif node in self.vis:
            # self.no.add(node)
            return False
        elif len(self.graph[node]) == 0:
            self.vis.add(node)
            self.res.add(node)
            return True
        else:
            self.vis.add(node)
            for i in self.graph[node]:
                if not self.dfs(i):
                    return False
            self.res.add(node)
            return True

            
        

s = Solution()

li = [[1,2],[2,3],[5],[0],[5],[],[]]
li2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]]

print(s.eventualSafeNodes(li))
print(s.eventualSafeNodes(li2))