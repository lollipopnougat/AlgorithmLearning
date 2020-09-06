# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root:
            return []
        que = [(root, 1)]
        cur = 1
        res = []
        each = []
        while que:
            tmp = que.pop(0)
            if tmp[1] != cur:
                cur = tmp[1]
                res.insert(0, each[:])
                each.clear()
            each.append(tmp[0].val)
            if tmp[0].left:
                que.append((tmp[0].left, cur + 1))
            if tmp[0].right:
                que.append((tmp[0].right, cur + 1))
        res.insert(0,each)
        return res


s = Solution()
li = [3, 9, 20, None, None, 15, 7]
head = TreeNode(3)

'''
    3
   / \
  9  20
    /  \
   15   7
'''
head.left = TreeNode(9)
head.right = TreeNode(20)
p = head.right
p.left = TreeNode(15)
p.right = TreeNode(7)

print(s.levelOrderBottom(head))
