# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        r = self.depth(root.left) + self.depth(root.right)
        return max(r, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def depth(self, root: TreeNode):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1


class Solutionn:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max = 0
        self.depth(root)
        return self.max

    def depth(self, root: TreeNode):
        if not root:
            return 0
        ls, rs = ((self.depth(root.left) + 1) if root.left else 0), ((self.depth(root.right) + 1) if root.right else 0)
        self.max = max(self.max, ls + rs)
        return max(ls, rs)

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

t = build_tree(li)

s = Solution()

print(s.diameterOfBinaryTree(t))
