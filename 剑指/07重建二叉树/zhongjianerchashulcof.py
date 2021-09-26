# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        nodeval = preorder[0]
        node = TreeNode(nodeval)
        ls = inorder.index(nodeval)
        node.left = self.buildTree(preorder[1:ls + 1], inorder[0:ls])
        node.right = self.buildTree(preorder[ls + 1:], inorder[ls + 1:])
        return node