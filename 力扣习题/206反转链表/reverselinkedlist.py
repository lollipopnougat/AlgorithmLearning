# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev

def build_node(l: list) -> ListNode:
    head = ListNode(0)
    p = head
    for i in l:
        p.next = ListNode(i)
        p = p.next
    return head.next

def print_node(nodes: ListNode, nums=-1):
    i = 0
    p = nodes
    while p:
        i += 1
        print(f'-> {p.val}', end=' ')
        p = p.next
        if nums != -1 and i == nums:
            break
    print('')

s = Solution()
n = build_node([1,2,3,4,5,6])
k = s.reverseList(n)
print_node(k)