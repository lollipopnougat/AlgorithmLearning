"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    '''
    正解 70ms
    '''
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        root.next = None
        
        # leftmost 指向每层最左边的一个节点
        leftmost = root
        while leftmost:
            # cur 从当前层最左节点, 通过 next 往右遍历, 填充下一层节点的 next
            cur = leftmost
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right:
                    cur.right.next = cur.next.left if cur.next else None
                cur = cur.next
            # 切到下一层最左的节点
            leftmost = leftmost.left
        return root
        
class Solutionnre:
    '''
    递归法 70ms
    '''
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        nt = root.next
        if root.left:
            root.left.next = root.right
            if nt == None:
                root.right.next = None
            else:
                root.right.next = nt.left
        self.connect(root.left)
        self.connect(root.right)
        return root

class Solutionre:
    '''
    my递归法 100ms
    '''
    def connect(self, root: 'Node') -> 'Node':
        return self.helper(root, None)
        
        
    def helper(self, root, parent):
        if not root:
            return root
        if parent:
            if root == parent.left:
                root.next = parent.right
            else:
                if parent.next:
                    root.next = parent.next.left
        self.helper(root.left, root)
        self.helper(root.right, root)
        return root


class Solution2:
    '''
    117解法 未优化 空间复杂度不合要求
    '''
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


class Solution3:
    '''
    117解法 优化后 空间复杂度不合要求
    '''
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