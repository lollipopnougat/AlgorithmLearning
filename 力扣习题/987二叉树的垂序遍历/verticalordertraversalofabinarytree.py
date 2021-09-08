# Definition for a binary tree node.
from typing import List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.res = {}
        self.helper(root,0,0)
        tmp = sorted(self.res)
        res_l = []
        for i in tmp:
            t = []
            tm = {}
            for j in self.res[i]:
                if not j[0] in tm:
                    tm[j[0]] = []
                tm[j[0]].append(j[1])
            tt = sorted(tm)
            for j in tt:
                t.extend(sorted(tm[j]))
            res_l.append(t)
        return res_l
                


            

    def helper(self, root: TreeNode, i:int, j:int):
        if root:
            if not j in self.res:
                self.res[j] = []
            self.res[j].append((i, root.val))
            self.helper(root.left, i + 1, j - 1)
            self.helper(root.right, i + 1, j + 1)

def build_tree(li:list) -> TreeNode:
    root = TreeNode()
    queue = [root]
    le = len(li)
    layers = math.ceil(math.log(le + 1, 2))
    limits = 2 ** (layers - 1) - 1
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

def check_tree(root:TreeNode):
    if root:
        if root.left and not root.left.val:
            root.left = None
        if root.right and not root.right.val:
            root.right = None
        if root.left:
            check_tree(root.left)
        if root.right:
            check_tree(root.right)


s = Solution()
tree = build_tree([1,2,3,4,5,6,7])


print(s.verticalTraversal(tree))
