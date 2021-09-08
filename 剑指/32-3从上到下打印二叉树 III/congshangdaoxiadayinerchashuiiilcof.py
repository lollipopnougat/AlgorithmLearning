# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        cur = [root]
        result = []
        while len(cur):
            culen = len(cur)
            tmp = []
            for i in range(culen):
                p = cur.pop(0)
                if p:
                    tmp.append(p.val)
                    cur.append(p.left)
                    cur.append(p.right)
            if len(tmp):
                result.append(tmp)
        le = len(result)
        for i in range(1, le, 2):
            result[i].reverse()
        return result