"""
# Definition for a Node.
# """
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            l = len(queue)
            while l > 0:
                queue[0].next = queue[1] if l > 1 else None
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
                l -= 1
        return root

class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            for i in range(len(queue) - 1):
                queue[i].next = queue[i + 1]
            t = queue[:]
            queue.clear()
            for i in t:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
        return root

tree = Node(val=1)
tree.left = Node(val=2)
tree.right = Node(val=3)
tree.left.left = Node(val=4)
tree.left.right = Node(val=5)
tree.right.right = Node(val=7)



s = Solution()
tr = s.connect(tree)

def fl(root):
    queue = [root]
    while queue:
        t = queue.pop(0)
        if t:
            print("node: %d next: %d"%(t.val, t.next.val if t.next else -1))
            queue.append(t.left)
            queue.append(t.right)

fl(tr)

