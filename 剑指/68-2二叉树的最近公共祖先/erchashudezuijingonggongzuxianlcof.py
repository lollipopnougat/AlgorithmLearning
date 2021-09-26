# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left = None
        st = [[root, False]]
        right = []
        while not left or not right:
            t = st[-1]
            if t[1]:
                st.pop()
                continue
            t[1] = True
            if t[0] == p:
                left = [i[0] for i in st if i[1]]
            elif t[0] == q:
                right = [i[0] for i in st if i[1]]
            if t[0].left:
                st.append([t[0].left, False])
            if t[0].right:
                st.append([t[0].right, False])
        i = j = 0
        lef = len(left)
        rig = len(right)
        while i < lef and j < rig:
            if left[i] == right[j]:
                i += 1
                j += 1
            else:
                return left[i - 1]
        if i == lef or j == rig:
            return left[i - 1]


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


li = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

tr = build_tree(li)

le = tr.left
#ri = tr.right
ri = tr.left.right.right

s = Solution()

print(s.lowestCommonAncestor(tr, le, ri).val)
