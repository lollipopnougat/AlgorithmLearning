import math
from typing import Optional
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root, 0)
    
    def helper(self, root: Optional[TreeNode], addVal: int) -> Optional[TreeNode]:
        if root:
            rt = self.helper(root.right, addVal)
            val = self.rightMax(rt)
            if val == 0:
                val = addVal
            val += root.val
            lt = self.helper(root.left, val)
            node = TreeNode(val, lt, rt)
            return node
        return None
    def rightMax(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.left:
                return self.rightMax(root.left)
            else:
                return root.val
        return 0
                
class Solution2:
    '''
    暂存大法
    '''
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.res = []
        self.lrr(root)
        n = len(self.res)
        for i in range(n - 2, -1, -1):
            self.res[i].val += self.res[i + 1].val
        return root

    def lrr(self, root: TreeNode):
        if root:
            self.lrr(root.left)
            self.res.append(root)
            self.lrr(root.right)

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
    root = TreeNode(None)
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
            t.left = TreeNode(None)
            t.left.parents = t
            t.right = TreeNode(None)
            t.right.parents = t
            queue.append(t.left)
            queue.append(t.right)
        i += 1
    check_tree(root)
    return root


def levelOrder(root: TreeNode) -> List[List[int]]:
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


t = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
tree = build_tree(t)
s = Solution()
res = s.convertBST(tree)
rr = levelOrder(res)
print(rr)