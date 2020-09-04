# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def dfs(r, s):
            if not r:
                return
            s = str(r.val) if s == '' else s + '->' + str(r.val)
            if not r.left and not r.right:
                res.append(s) 
            dfs(r.left, s)
            dfs(r.right, s)
        dfs(root, '')
        return res


class Solution2:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        stack = [(root, '')]
        while stack:
            tmp = stack.pop()
            if tmp[1] == '':
                st = str(tmp[0].val)  
            else:
                st = tmp[1] + '->' + str(tmp[0].val)
            if tmp[0].right:
                stack.append((tmp[0].right, st))
            if tmp[0].left:
                stack.append((tmp[0].left, st))
            if not tmp[0].right and not tmp[0].left:
                res.append(st)
        return res