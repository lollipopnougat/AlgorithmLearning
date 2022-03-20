# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        if root == None:
            return res
        stack.append(root)
        flag = False
        while len(stack) != 0:
            root = stack[-1]
            if root.left != None and not flag:
                stack.append(root.left)
            else:
                res.append(root.val)
                stack.pop()
                if root.right != None:
                    stack.append(root.right)
                    flag = False
                else:
                    flag = True
        return res