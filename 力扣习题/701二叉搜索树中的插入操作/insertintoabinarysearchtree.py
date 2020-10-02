# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val > val:
                root.left=self.insertIntoBST(root.left, val)
            if root.val < val:
                root.right=self.insertIntoBST(root.right,val)
        else:
            root = TreeNode(val)
        return root

class Solution2:
    '''
    非递归
    '''
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            p = root
            while True:
                if p.val > val:
                    if not p.left:
                        p.left = TreeNode(val)
                        break
                    p = p.left
                if p.val < val:
                    if not p.right:
                        p.right = TreeNode(val)
                        break
                    p = p.right
        else:
            return TreeNode(val)
        return root
        

class Solution3:
    '''
    大佬的高速版
    '''
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        cur = root
        par = root
        while cur:
            par = cur
            if val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        cur = TreeNode(val)
        if par.val > val:
            par.left = cur
        else:
            par.right = cur
        
        return root