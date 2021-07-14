# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        h = ListNode(0)
        h.next = head
        p = h
        i = 0
        while p.next and i < left - 1:
            p = p.next
            i += 1
        p.next = self.helper(p.next, right - left + 1)
        return h.next
        


    def helper(self, head: ListNode, nums: int) -> ListNode:
        # k个一组反转链表用的helper，有修改
        if nums == 1:
            return head
        h = node = self.helper(head.next, nums - 1)
        for i in range(1, nums - 1):
            node = node.next
        head.next = node.next
        node.next = head
        return h

oli = [1,2,3,4,5]
l = 1
r = 2

li = build_node(oli)

s = Solution()
res = s.reverseBetween(li, l, r)
print_node(res)

