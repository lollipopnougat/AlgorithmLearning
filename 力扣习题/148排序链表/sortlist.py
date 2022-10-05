# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dat = []
        p = head
        while p:
            dat.append(p)
            p = p.next
        n = len(dat)
        if n == 0:
            return None
        dat.sort(key=lambda x: x.val)
        for i in range(n - 1):
            dat[i].next = dat[i + 1]
        dat[-1].next = None
        return dat[0]


def build_node(l: list) -> ListNode:
    head = ListNode(0)
    p = head
    for i in l:
        p.next = ListNode(i)
        p = p.next
    return head.next


def print_node(nodes: ListNode, nums=-1):
    i = 0
    p = nodes
    while p:
        i += 1
        print(f'-> {p.val}', end=' ')
        p = p.next
        if nums != -1 and i == nums:
            break
    print('')


s = Solution()
a = [-1, 5, 3, 4, 0]
l = build_node(a)
print_node(s.sortList(l))
