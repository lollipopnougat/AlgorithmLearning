# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        p = head
        if p and p.val == val:
            return p.next
        l = head
        while p and p.val != val:
            l, p = p, p.next
        l.next = p.next if p else None
        return head
            

        