from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        l = len(grid)
        if l == 0:
            return None
        elif l == 1:
            return Node(grid[0][0], 1, None, None, None, None)
        else:
            half = l // 2
            tl = self.construct(list(map(lambda x:x[0:half], grid[0:half])))
            tr = self.construct(list(map(lambda x:x[half:l], grid[0:half])))
            bl = self.construct(list(map(lambda x:x[0:half], grid[half:l])))
            br = self.construct(list(map(lambda x:x[half:l], grid[half:l])))
            if all([tl.isLeaf, tr.isLeaf, bl.isLeaf, br.isLeaf]) and tl.val == tr.val == bl.val == br.val:
                root = Node(tl.val, 1, None, None, None, None)
            else:
                root = Node(1, 0, tl, tr, bl, br)
            return root

def to_list(node: Node) -> List[List[int]]:
    res = []
    stack = [node]
    while stack:
        t = stack.pop(0)
        if t != None:
            res.append([1 if t.isLeaf else 0, t.val])
            stack.append(t.topLeft)
            stack.append(t.topRight)
            stack.append(t.bottomLeft)
            stack.append(t.bottomRight)
        else:
            res.append(None)
    while len(res) > 0 and res[-1] == None:
        res.pop()
    return res

s = Solution()
res = s.construct([[0,1],[1,0]])
print(to_list(res))
a = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]

print(to_list(s.construct(a)))