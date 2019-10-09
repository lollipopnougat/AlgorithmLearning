
class Node:
    def __init__(self, val: int):
        self.value = val
        self.left = None
        self.right = None

    value = 0
    left = None 
    right = None


class Solution:
    def __init__(self, num: list):
        self.nums = num
        self.tree_node = self.make_tree(0, len(num) - 1)

    nums: list
    tree_node: Node

    def make_tree(self, low: int, high: int) -> Node:
        if low > high:
            return None
        mid = int((low + high) / 2)
        node = Node(self.nums[mid])
        node.left = self.make_tree(low, mid - 1)
        node.right = self.make_tree(mid + 1, high)
        return node

    def print_tree(self, node: Node):
        if node != None:
            print(node.value, end=' ')
            print('左孩子', end=' ')
            self.print_tree(node.left)
            print('右孩子', end=' ')
            self.print_tree(node.right)
        else:
            print('空节点', end=' ')


if __name__ == "__main__":
    sol = Solution([-10, -3, 0, 5, 10])
    sol.print_tree(sol.tree_node)
