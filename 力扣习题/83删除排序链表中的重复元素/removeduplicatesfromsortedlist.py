# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p = head
        his = p
        p = p.next
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            head = head.next
        return head