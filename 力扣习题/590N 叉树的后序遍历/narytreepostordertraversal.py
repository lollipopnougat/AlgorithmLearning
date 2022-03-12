from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.helper(root)
        return self.res
        
    def helper(self, root: 'Node'):
        if root:
            for i in root.children:
                self.helper(i)
            self.res.append(root.val)
        