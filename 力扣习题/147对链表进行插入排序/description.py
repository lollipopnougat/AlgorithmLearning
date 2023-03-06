from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solutiond:
    '''
    抖机灵
    '''
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        p = head
        while p:
            res.append(p)
            p = p.next
        res.sort(key=lambda x: x.val)
        n = len(res)
        for i in range(n - 1):
            res[i].next = res[i + 1]
        res[-1].next = None
        return res[0]

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ph = ListNode()
        p = ph
        ph.next = head
        head = head.next
        ph.next.next = None
        while head:
            while p.next and head and p.next.val >= head.val:
                p = p.next
            t = head
            head = head.next
            t.next = p.next
            p.next = t       
        return ph.next


    def swap(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head.next
        q = p.next
        head.next = q
        p.next = q.next
        q.next = p
        return head


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


s = Solution()
li = build_node([4, 2, 1, 3])
res = s.insertionSortList(li)
print(res)