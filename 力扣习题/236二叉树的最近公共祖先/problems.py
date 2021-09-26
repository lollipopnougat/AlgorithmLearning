# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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