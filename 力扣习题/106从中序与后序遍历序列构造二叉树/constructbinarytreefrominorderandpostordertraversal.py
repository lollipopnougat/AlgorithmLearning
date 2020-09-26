# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        if not postorder:
            return None
        nodeval = postorder[-1]
        node = TreeNode(nodeval)
        ls = inorder.index(nodeval)
        node.left = self.buildTree(inorder[0:ls],postorder[0:ls])
        node.right = self.buildTree(inorder[ls+1:],postorder[ls:-1])
        return node