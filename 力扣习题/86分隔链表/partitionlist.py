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

def print_node(nodes: ListNode):
    p = nodes
    while p:
        print(f'-> {p.val}', end=' ')
        p = p.next
    print('')



class Solution:
    # 维护两个链表 一个比x小，一个比x大
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = ListNode(0)
        p1 = h1
        h2 = ListNode(0)
        p2 = h2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            if p.next:
                p = p.next
            else:
                break
        p1.next = h2.next
        p2.next = None
        return h1.next

oli = [1,4,3,2,5,2]
oli2 = [2,1]
li = build_node(oli)
li2 = build_node(oli2)
s = Solution()
res = s.partition(li, 3)
res2 = s.partition(li2, 2)
print_node(res)
print_node(res2)
