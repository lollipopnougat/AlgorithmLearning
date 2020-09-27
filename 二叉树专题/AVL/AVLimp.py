# 还未完成
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.height = 0
        self.balance = 0
        self.left = None
        self.right = None

class AVL:
    def __init__(self, li):
        self.nums = li[:]
        self.nums.sort()
        self.root = self.make_tree(0, len(self.nums) - 1, self.root)

    def make_tree(self, low: int, high: int) -> TreeNode:
        if low > high:
            return None
        mid = (low + high) // 2
        node = TreeNode(self.nums[mid])
        node.left = self.make_tree(low, mid - 1)
        node.right = self.make_tree(mid + 1, high)
        return node

    def add_node(self, val):
        node = TreeNode(val)
        p = self.root
        while p.left and p.val >= val:
            p = p.left
        while p.right and p.val < val:
            p = p.right
        if p.val >= val:
            p.left = node
        else:
            p.right = node

    def search(self, val):
        p = self.root
        while p:
            if p.val == val:
                return p
            elif p.val < val:
                p = p.right
            else:
                p = p.left
        return None

    def del_node(self, val):
        p = self.root
        pre = p
        while p.left and p.val > val:
            pre = p
            p = p.left
        while p.right and p.val < val:
            p = p.right
        if p.val == val:

        

    
    def __LDR(self, node: TreeNode):
        if node != None:
            self.__LDR(node.left)
            print(node.val, end=' ')
            self.__LDR(node.right)
    
    def print_tree(self):
        self.__LDR(self.root)

sol = BST([-10, -3, 0, 5, 10])
sol.add_node(4)
sol.print_tree()

