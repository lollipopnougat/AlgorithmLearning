# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        tmp = []
        p = self.next
        while p:
            tmp.append(str(p.val))
            p = p.next
        return f'[{",".join(tmp)}]'
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = ListNode()
        flag = False
        h.next = head
        q = h
        p = h.next if q else None
        f = p.next if p else None
        while p and f:
            if f.val == p.val:
                p.next = f.next
                f = f.next
                flag = True
            elif flag:
                q.next = f
                p = f
                f = f.next if f else None
                flag = False
            else:
                q = q.next
                p = p.next if p else None
                f = f.next if f else None
        if flag:
            q.next = None
        return h.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solutionr:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        m = {}
        h = p = ListNode(None)
        while head:
            m[head.val] = m.get(head.val, 0) + 1
            head = head.next
        for i in m:
            if m[i] == 1:
                p.next = ListNode(i)
                p = p.next
        return h.next

def build_list(li: List[int]) -> ListNode:
    res = []
    l = len(li)
    for i in li:
        res.append(ListNode(i))
    for i in range(l - 1):
        res[i].next = res[i + 1]
    return res[0]

def to_list(head: ListNode) -> List[int]:
    res = []
    p = head
    while p:
        res.append(p.val)
        p = p.next
    return res

s = Solution()
li = build_list([1, 2, 2])
li2 = s.deleteDuplicates(li)
res = to_list(li2)
print(res)

li = build_list([1, 1, 2])
li2 = s.deleteDuplicates(li)
res = to_list(li2)
print(res)

li = build_list([1, 1, 2, 2])
li2 = s.deleteDuplicates(li)
res = to_list(li2)
print(res)


li = build_list([1, 1, 2, 3, 3])
li2 = s.deleteDuplicates(li)
res = to_list(li2)
print(res)
            