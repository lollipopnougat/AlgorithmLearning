# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    简单粗暴hashset
    '''
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        m = set()
        p = headA
        while p:
            m.add(p)
            p = p.next
        p = headB
        while p:
            if p in m:
                return p
            p = p.next
        return None


class Solutiond:
    '''
    双指针
    '''
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        p = headA
        q = headB
        flag = 0
        while p and q:
            pv = p.val
            qv = q.val
            if p == q:
                return p
            p = p.next
            q = q.next
            if not p and flag < 2:
                p = headB
                flag += 1
            if not q and flag:
                q = headA
                flag += 1
        return None
        
        

pos = 8
l1 = [4, 1, 8, 4, 5]
l2 = [5, 6, 1, 8, 4, 5]
ai = 2
bi = 3


def build_list(a: list) -> ListNode:
    l = len(a)
    if l == 0:
        return None
    head = p = ListNode(a[0])
    for i in range(1, l):
        p.next = ListNode(a[i])
        p = p.next
    return head

def nodes_to_list(head: ListNode) -> list:
    t = []
    p = head
    while p:
        t.append(p)
        p = p.next
    return t

def nodes_to_listv(head: ListNode) -> list:
    t = []
    p = head
    while p:
        t.append(p.val)
        p = p.next
    return t

def build_ilist(a: list, b: list, ai: int, bi: int) -> tuple:
    l1 = len(a)
    l2 = len(b)
    if l1 == 0 and l2 == 0:
        return None
    A = build_list(a)
    B = build_list(b[0:bi])
    p = B
    count = 0
    q = A
    while count < ai:
        q = q.next
        count += 1
    count = 0
    while p:
        p = p.next
        count += 1
        if count + 1 == bi:
            p.next = q
    return A, B


A, B = build_ilist(l1, l2, ai, bi)
s = Solutiond()

node = s.getIntersectionNode(A, B)
print(node.val)
