from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        h = ListNode(None)
        h.next = head
        p = h
        while p:
            if p.next and p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return h.next
