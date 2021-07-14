# Definition for a binary tree node.
from typing import List

'''
对于连续整数序列[left, right]中的一点i，若要生成以i为根节点的BST，则有如下规律：

i左边的序列可以作为左子树结点，且左儿子可能有多个，所以有left_nodes = helper(left, i - 1)
i右边的序列可以作为右子树结点，同上所以有right_nodes = helper(i + 1, right)
产生的以当前i为根结点的BST（子）树有len(left_nodes) * len(right_nodes)个，遍历每种情况，即可生成以i为根节点的BST序列；
然后以for循环使得[left, right]中每个结点都能生成子树序列。
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n:
            return self.helper(1, n)
        else:
            return []
    
    def helper(self, l: int, r: int) -> TreeNode:
        ans = []
        if l > r:
            ans.append(None)
            return ans
        for i in range(l, r + 1):
            lns = self.helper(l, i - 1);
            rns = self.helper(i + 1, r)
            for ln in lns:
                for rn in rns:
                    t = TreeNode(i)
                    t.left = ln
                    t.right = rn
                    ans.append(t)
        return ans



