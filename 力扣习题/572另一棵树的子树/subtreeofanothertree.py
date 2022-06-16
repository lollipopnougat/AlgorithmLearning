# Definition for a binary tree node.
from typing import List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root and subRoot:
            return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        elif root == subRoot == None:
            return True
        else:
            return False
    def isSameTree(self, root: TreeNode, rt2: TreeNode) -> bool:
        if root and rt2:
            return root.val == rt2.val and self.isSameTree(root.left, rt2.left) and self.isSameTree(root.right, rt2.right)
        elif root == rt2 == None:
            return True
        else:
            return False


def build_tree2(li: List[int]) -> TreeNode:
    '''
    半完全层序构造二叉树
    '''
    l = len(li)
    if l == 0:
        return None
    lt = [None] * l
    lt[0] = TreeNode(li[0])
    depth = math.floor(math.log(l, 2))
    for i in range(1, l):
        if li[i] != None:
            lt[i] = TreeNode(li[i])
            if i % 2 == 0:
                lt[(i - 1) // 2].right = lt[i]
            else:
                lt[i // 2].left = lt[i]
    return lt[0]


s = Solution()
tree = build_tree2([3, 4, 5, 1, 2, None, None, None, None, 0])
tree2 = build_tree2([4, 1, 2])

root = build_tree2([3,4,5,1,2])
subRoot = build_tree2([4,1,2])
print(s.isSubtree(tree, tree2))
print(s.isSubtree(root, subRoot))
root = build_tree2([1,1])
subRoot = build_tree2([1])
print(s.isSubtree(root, subRoot))
