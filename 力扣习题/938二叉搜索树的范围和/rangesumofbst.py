# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parents = None

    def __str__(self) -> str:
        return f'val: {self.val}, l: {self.left}, r: {self.r}'

    __repr__ = __str__

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



def dlr(root: TreeNode):
    if root:
        print(root.val, end=' ')
        dlr(root.left)
        dlr(root.right)

def bylayers(root: TreeNode):
    queue = [root]
    while queue:
        t = queue.pop(0)
        if t:
            print(t.val, end=' ')
            queue.append(t.left)
            queue.append(t.right)



class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if low > high:
            return 0
        if root:
            if root.val > high:
                return self.rangeSumBST(root.left, low, high)
            elif root.val < low:
                return self.rangeSumBST(root.right, low, high)
            else:
                return root.val + self.rangeSumBST(root.left, low, root.val - 1) + self.rangeSumBST(root.right, root.val + 1, high)
        return 0



lis = [10, 5, 15, 3, 7, None, 18]

tree = build_tree(lis)

bylayers(tree)

print(' ')

s = Solution()

print(s.rangeSumBST(tree, 7, 15))
