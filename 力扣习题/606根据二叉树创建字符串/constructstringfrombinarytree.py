from typing import List, Optional
import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = []
        self.helper(root)
        return ''.join(self.res)

    def helper(self, root: Optional[TreeNode]):
        if root:
            self.res.append(str(root.val))
            if root.left:
                self.res.append('(')
                self.helper(root.left)
                self.res.append(')')
                if root.right:
                    self.res.append('(')
                    self.helper(root.right)
                    self.res.append(')')     
            elif root.right:
                self.res.append('()')    
                self.res.append('(')
                self.helper(root.right)
                self.res.append(')')




def build_tree2(li: List[int]) -> TreeNode:
    '''
    半完全层序构造二叉树
    '''
    l = len(li)
    if l == 0:
        return None
    lt = [None] * l
    lt[0] = TreeNode(li[0])
    depth = math.floor(math.log(l, 2))
    for i in range(1, l):
        if li[i] != None:
            lt[i] = TreeNode(li[i])
            if i % 2 == 0:
                lt[(i - 1) // 2].right = lt[i]
            else:
                lt[i // 2].left = lt[i]
    return lt[0]

li1 = [1,2,3,4]
li2 = [1,2,3,None,4]

s = Solution()
t1 = build_tree2(li1)
t2 = build_tree2(li2)
print(s.tree2str(t1))
print(s.tree2str(t2))


        