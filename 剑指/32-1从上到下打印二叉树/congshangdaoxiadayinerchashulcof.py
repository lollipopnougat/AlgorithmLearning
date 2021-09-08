# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = [root]
        i = 0
        while i < len(res):
            if res[i].left:
                res.append(res[i].left)
            if res[i].right:
                res.append(res[i].right)
            i += 1
        return [i.val for i in res]
