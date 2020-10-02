# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        self.res = []
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if root:
            self.helper(root.left)
            self.helper(root.right)
            self.res.append(root.val)


class Solution2:
    '''
    进阶：非递归算法
    '''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        tmp = []
        res = []
        stack.append(root)
        while len(stack) != 0:
            node = stack[-1]
            if len(tmp) != 0 and tmp[-1] == node:
                res.append(node.val)
                tmp.pop()
                stack.pop()
            elif node == None:
                stack.pop()
                continue
            else:
                tmp.append(node)
                stack.append(node.right)
                stack.append(node.left)
        return res
    
        