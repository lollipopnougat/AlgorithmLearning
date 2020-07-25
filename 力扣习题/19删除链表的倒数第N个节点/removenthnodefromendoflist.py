# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 一趟实现
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp = []
        while head != None:
            tmp.append(head)
            head = head.next
        if n == len(tmp):
            if n == 1:
                return None
            else:
                return tmp[1]
        elif n == 1:
            tmp[-(n + 1)].next = None
        else:
            tmp[-(n + 1)].next = tmp[-(n - 1)]
        return tmp[0]