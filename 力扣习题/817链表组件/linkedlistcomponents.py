# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        b = set(nums)
        p = head
        fl = False
        res = 0
        while p:
            if p.val in b and not fl:
                res += 1
                fl = True
            elif p.val not in b:
                fl = False
            p = p.next
        return res


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
li = build_node([0, 1, 2, 3])
li2 = build_node([0, 1, 2, 3, 4])
li3 = build_node([0, 1, 2, 3, 4, 5, 6, 9, 8, 7])
print(s.numComponents(li, [0, 1, 3]))
print(s.numComponents(li2, [0, 3, 1, 4]))
print(s.numComponents(li3, [2, 4, 5, 6, 8]))