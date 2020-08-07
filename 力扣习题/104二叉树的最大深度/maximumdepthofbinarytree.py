import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        n = 0
        stack = [(root, 1)]
        while stack:
            tmp = stack.pop()
            if tmp[0]:
                if n < tmp[1]:
                    n = tmp[1]
                stack.append((tmp[0].left, tmp[1] + 1))
                stack.append((tmp[0].right, tmp[1] + 1))
        return n

class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if root == None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

s = Solution2()

node = TreeNode(0)

print(s.maxDepth(node))