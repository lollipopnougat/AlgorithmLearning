class TreeNode:
    val = None
    left = None
    right = None

    def __init__(self, value):
        self.val = value




class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> list:
        self.su = sum
        self.tmp = [root]
        self.res = []
        self.dfs(root)
        return self.res



    def dfs(self, root):
        if not root:
            return
        if not root.left and not root.right:
            tmp = [i.val for i in self.tmp]
            if sum(tmp) == self.su:
                self.res.append(tmp)
        if root.left:
            self.tmp.append(root.left)
            self.dfs(root.left)
            self.tmp.pop()
        if root.right:
            self.tmp.append(root.right)
            self.dfs(root.right)
            self.tmp.pop()


tr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
target = 22

tree = TreeNode(5)
tree.left = TreeNode(4)
tree.right = TreeNode(8)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.left = TreeNode(5)
tree.right.right.right = TreeNode(1)

s = Solution()

print(s.pathSum(tree, 22))
