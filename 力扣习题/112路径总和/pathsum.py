# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.su = sum
        self.tmp = [root]
        #self.res = []
        return self.dfs(root)
        #return True if self.res else False



    def dfs(self, root):
        if not root:
            return False
        if not root.left and not root.right:
            tmp = [i.val for i in self.tmp]
            if sum(tmp) == self.su:
                return True
                #self.res.append(tmp)
        if root.left:
            self.tmp.append(root.left)
            t = self.dfs(root.left)
            if t:
                return True
            self.tmp.pop()
        if root.right:
            self.tmp.append(root.right)
            t = self.dfs(root.right)
            if t:
                return True
            self.tmp.pop()
        return False