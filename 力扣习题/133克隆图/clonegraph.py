"""
# Definition for a Node."""
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        return copy.deepcopy(node)


