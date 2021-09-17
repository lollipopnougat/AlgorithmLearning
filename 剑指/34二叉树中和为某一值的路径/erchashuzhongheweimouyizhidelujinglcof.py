# Definition for a binary tree node.
from typing import List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.res = []
        self.t = target
        self.dfs(root, 0, [])
        return self.res
    def dfs(self, root: TreeNode, su: int, tmp: List[int]):
        if root:
            if su + root.val == self.t:
                tmp.append(root.val)
                self.res.append(tmp[:])
                tmp.pop()
            elif su + root.val < self.t:
                self.dfs(root.left, su + root.val, tmp)
                self.dfs(root.right, su + root.val, tmp)


def check_tree(root: TreeNode):
    if root:
        if root.left and not root.left.val:
            root.left = None
        if root.right and not root.right.val:
            root.right = None
        if root.left:
            check_tree(root.left)
        if root.right:
            check_tree(root.right)


def build_tree(li: list) -> TreeNode:
    root = TreeNode()
    queue = [root]
    le = len(li)
    layers = math.ceil(math.log(le + 1, 2))
    limits = 2**(layers - 1) - 1
    i = 0
    while i < le:
        t = queue.pop(0)
        if li[i]:
            t.val = li[i]
        if i < limits:
            t.left = TreeNode()
            t.left.parents = t
            t.right = TreeNode()
            t.right.parents = t
            queue.append(t.left)
            queue.append(t.right)
        i += 1
    check_tree(root)
    return root

def dlr(root: TreeNode):
    if root:
        print(root.val, end = ' ')
        dlr(root.left)
        dlr(root.right)

def ldr(root: TreeNode):
    if root:
        dlr(root.left)
        print(root.val, end = ' ')
        dlr(root.right)

s = Solution()

tree_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]

tree = build_tree(tree_list)
dlr(tree)
print(' ')
ldr(tree)
print(' ')
res = s.pathSum(tree, 22)

print(res)

