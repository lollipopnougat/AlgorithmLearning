# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        n = 0
        stack = [(root, 1)]
        while stack:
            tmp = stack.pop()
            if tmp[0]:
                n = max(n, tmp[1])
                stack.append((tmp[0].left, tmp[1] + 1))
                stack.append((tmp[0].right, tmp[1] + 1))
        return n