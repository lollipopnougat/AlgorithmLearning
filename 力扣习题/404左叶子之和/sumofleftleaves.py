# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        s = 0
        stack = [(root, False)]
        while stack:
            t = stack.pop()
            if t[1] and not t[0].left and not t[0].right:
                s += t[0].val
                continue
            if t[0].left:
                stack.append((t[0].left, True))
            if t[0].right:
                stack.append((t[0].right, False))
        return s
#[3,9,20,None,None,15,7]
r = TreeNode(3)
r.left = TreeNode(9)
r.right = TreeNode(20)
t = r.right
t.left = TreeNode(15)
t.right = TreeNode(7)

s = Solution()
print(s.sumOfLeftLeaves(r))