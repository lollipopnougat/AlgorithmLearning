# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 快慢指针
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        f = s = head
        c = 0
        while c < k:
            f = f.next
            c += 1
        while f:
            f = f.next
            s = s.next
        return s