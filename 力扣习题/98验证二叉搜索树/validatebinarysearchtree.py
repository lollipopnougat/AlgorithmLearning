# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
class Solution:
    pre = -sys.maxsize
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        tmp = self.isValidBST(root.left) and self.isValidBST(root.right) and self.pre < root.val
        self.pre = root.val
        return tmp

class SolutionLDR:
    def __init__(self):
        self.res = []
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.LDR(root)
        last = self.res[0]
        for i in range(1, len(self.res)):
            if last >= self.res[i]:
                return False
            last = self.res[i]
        return True
        
    def LDR(self, root):
        if root:
            self.LDR(root.left)
            self.res.append(root.val)
            self.LDR(root.right)


