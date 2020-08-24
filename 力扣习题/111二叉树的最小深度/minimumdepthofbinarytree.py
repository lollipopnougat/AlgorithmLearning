# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 1
        queue = []
        queue.append((1, root))
        while queue:
            t = queue.pop(0)
            depth = t[0]
            if t[1].left == None and t[1].right == None:
                return depth
            if t[1].left:
                queue.append((depth + 1, t[1].left))
            if t[1].right:
                queue.append((depth + 1, t[1].right))
        