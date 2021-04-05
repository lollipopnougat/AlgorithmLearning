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
    # 空间复杂度O(1)解法 核心在递归...
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        myhead = ListNode(0)
        myhead.next = head
        store = myhead
        p = head
        i = 0
        while True:
            if i < k and p:
                i += 1
                p = p.next
                if p == None and i != k:
                    break
            elif i == k:
                store.next = self.helper(store.next, k)
                print(f'{k}list = ', end='') 
                print_node(store.next, k)
                q = store.next
                j = 0
                while j < k - 1:
                    j += 1
                    q = q.next
                q.next = p
                store = q
                i = 0
            else:
                break
        return myhead.next

    def helper(self, head: ListNode, nums: int) -> ListNode:
        if nums == 1:
            return head
        h = node = self.helper(head.next, nums - 1)
        for i in range(1, nums - 1):
            node = node.next
        node.next = head
        return h

class Solutiond:
    # 抖机灵大法
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        lis = []
        res = []
        p = head
        l = i = 0
        while p:
            if len(lis) == k:
                lis.reverse()
                res.extend(lis)
                lis.clear()
                i = 0
            lis.append(p)
            i += 1
            l += 1
            p = p.next
        if len(lis) == k:
                lis.reverse()
        res.extend(lis)
        if l == 0:
            return None
        for i in range(l - 1):
            res[i].next = res[i + 1]
        res[-1].next = None
        return res[0]


oli = [1,2,3,4,5]
li = build_node(oli)

s = Solutiond()

res = s.reverseKGroup(li, 2)
print_node(res)
# [2,1,4,3,5]

#li = build_node(oli)
#res = s.reverseKGroup(li, 3)

#print_node(res)
# [3,2,1,4,5]
