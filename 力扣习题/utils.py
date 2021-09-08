import math

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None, pre: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.pre = pre
        self.random = random

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def check_tree(root:TreeNode):
    if root:
        if root.left and not root.left.val:
            root.left = None
        if root.right and not root.right.val:
            root.right = None
        if root.left:
            check_tree(root.left)
        if root.right:
            check_tree(root.right)

def build_tree(li:list) -> TreeNode:
    root = TreeNode()
    queue = [root]
    le = len(li)
    layers = math.ceil(math.log(le + 1, 2))
    limits = 2 ** (layers - 1) - 1
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

def build_list(li: list) -> Node:
    le = len(li)
    res = []
    for i in range(le):
        res.append(Node(li[i][0]))
    for i in range(le - 1):
        res[i].next = res[i + 1]
        res[i].random = res[li[i][1]] if li[i][1] != None else None
    res[le - 1].random = res[li[le - 1][1]] if li[le - 1][1] != None else None
    return res[0]

def node_tolist(node: Node) -> list:
    cur = node
    m = {}
    c = 0
    while cur:
        m[cur] = c
        c += 1
        cur = cur.next
    res = []
    cur = node
    while cur:
        res.append([cur.val, m[cur.random] if cur.random != None else None])
        cur = cur.next
    return res