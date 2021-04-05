# # Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_node(l: list) -> ListNode:
    head = ListNode(0)
    p = head
    for i in l:
        p.next = ListNode(i)
        p = p.next
    return head.next

def print_node(nodes: ListNode):
    p = nodes
    while p:
        print(f'-> {p.val}', end=' ')
        p = p.next
    print('')

class Solution:
    # 列表
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 0
        arr = []
        p = head
        while p:
            arr.append(p)
            p = p.next
            length += 1
        if length == 0:
            return None
        k = k % length
        arr[-1].next = arr[0]
        h = arr[-k]
        arr[-k-1].next = None
        #print(length)
        return h

class Solution2:
    # 迭代
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 0
        p = head
        while p:
            if p.next:
                p = p.next
            else:
                p.next = head
                length += 1
                break
            length += 1
        if length == 0:
            return None
        k = k % length
        p, i = head, 0
        while i < length - k - 1:
            p = p.next
            i += 1
        h = p.next
        p.next = None
        return h

oli = [1,2,3,4,5]
oli2 = [2,1]
oli3 = [1]
li = build_node(oli)
li2 = build_node(oli2)
li3 = build_node(oli3)

s = Solution2()

res = s.rotateRight(li, 1)
print_node(res)
li = build_node(oli)
res = s.rotateRight(li, 2)
print_node(res)
li = build_node(oli)
res = s.rotateRight(li, 3)
print_node(res)

res = s.rotateRight(li2, 1)
print_node(res)
li2 = build_node(oli2)
res = s.rotateRight(li2, 2)
print_node(res)

res = s.rotateRight(li3, 1)
print_node(res)




