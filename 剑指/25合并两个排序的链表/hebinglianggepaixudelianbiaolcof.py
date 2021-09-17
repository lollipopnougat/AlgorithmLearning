# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self) -> str:
        i = 0
        p = self
        st = ''
        while p:
            i += 1
            st += f'-> {p.val} '
            p = p.next
        return st



def build_node(l: list) -> ListNode:
    head = ListNode(0)
    p = head
    for i in l:
        p.next = ListNode(i)
        p = p.next
    return head.next

def node_tolist(nodes: ListNode, nums=-1) -> str:
    i = 0
    p = nodes
    st = ''
    while p:
        i += 1
        st += f'-> {p.val} '
        p = p.next
        if nums != -1 and i == nums:
            break
    return st

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = ListNode(None)
        p = h
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return h.next

class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = ListNode(None)
        p = h.next = l1
        q = h
        while p and l2:
            if p.val >= l2.val:
                q.next = l2
                l2 = l2.next
                q = q.next
                q.next = p
            else:
                p = p.next
                q = q.next
        return h.next

nodes1 = build_node([1,2,4])
nodes2 = build_node([1,3,4])
s = Solution2()
res = node_tolist(s.mergeTwoLists(nodes1,nodes2))
print(res)