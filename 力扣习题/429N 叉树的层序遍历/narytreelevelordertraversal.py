from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        tmp = []
        res = []
        while queue:
            tmp.extend(queue)
            queue.clear()
            res.append([i.val for i in tmp])
            for i in tmp:
                if len(i.children) != 0:
                    queue.extend(i.children)
            tmp.clear()
        return res

