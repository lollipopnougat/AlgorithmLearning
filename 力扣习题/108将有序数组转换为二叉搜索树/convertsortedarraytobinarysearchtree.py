from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = len(nums)
        if l == 0:
            return None
        if l == 1:
            return TreeNode(nums[0])
        c = l // 2
        node = TreeNode(nums[c])
        node.left = self.sortedArrayToBST(nums[0:c])
        node.right = self.sortedArrayToBST(nums[c + 1:l])
        return node


li = [-10, -3, 0, 5, 9]
li = [1, 3]

s = Solution()

node = s.sortedArrayToBST(li)
print(node)

