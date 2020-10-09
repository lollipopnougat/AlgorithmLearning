# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        while head:
            if head in s:
                return head
            s.add(head)
            head = head.next
        return None


class Solution:
    '''
    快慢指针
    '''
    def detectCycle(self, head: ListNode) -> ListNode:
        if head and head.next:
            fast = head.next.next
            slow = head.next
        else:
            return None  # 说明无环

        # 进行循环，首先让快指针和慢指针第一次相遇
        while fast:
            if fast != slow:

                # 快指针走两步
                if fast.next:
                    fast = fast.next.next
                else:
                    return None  # 说明无环

                # 慢指针走一步
                slow = slow.next
            else:
                detection = head
                while detection != slow:  # 此时由于slow和fast是一样的，用哪个都行
                    slow = slow.next
                    detection = detection.next

                return detection