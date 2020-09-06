# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(None)
        pre.next = head
        t = pre
        while pre and pre.next and pre.next.next:
            cur = pre.next
            aft = cur.next
            cur.next = aft.next
            pre.next = aft
            aft.next = cur
            pre = pre.next.next
        return t.next

class Solutions:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        q = head.next
        head.next = self.swapPairs(q.next)
        q.next = head
        return q

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)

s = Solution()
p = s.swapPairs(h)

while p:
    print(str(p.val) + '->')
    p = p.next
