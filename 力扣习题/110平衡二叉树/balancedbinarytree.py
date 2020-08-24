# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(p:TreeNode) -> int:
            if p == None:
                return 0
            left = dfs(p.left)
            if left == -1:
                return -1
            right = dfs(p.right)
            if right == -1:
                return -1
            return -1 if abs(left - right) > 1 else 1 + max(left, right)
        return dfs(root) != -1