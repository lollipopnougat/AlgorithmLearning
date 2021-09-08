# Definition for a binary tree node.
from typing import List
import math
class TreeNode:
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None
        self.parents = None


# Definition for a binary tree node.

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        cur = [root]
        result = []
        while len(cur):
            culen = len(cur)
            tmp = []
            for i in range(culen):
                p = cur.pop(0)
                if p:
                    tmp.append(p.val)
                    cur.append(p.left)
                    cur.append(p.right)
            if len(tmp):
                result.append(tmp)
        return result
        
            



        
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

li = [1,2,3,4,5]
tr = build_tree(li)

s = Solution()

print(s.levelOrder(tr))