# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    真不错
    '''
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p = pp = head
        #i = 0
        while p and pp and pp.next:
            #i += 1
            p = p.next
            pp = pp.next.next
        tmp = []
        while p:
            tmp.append(p)
            p = p.next
        p = head
        #print(p.val)
        #j = 0
        l = len(tmp)
        while tmp:  #j < i:
            t = p.next
            p.next = tmp.pop()
            p.next.next = t
            p = t
            #j += 1
        if l & 0:
            p.next = None
        else:
            p.next.next = None
        return head

        #print(j)


s = Solution()


def buildln(li: list):
    p = h = ListNode()
    for i in li:
        p.next = ListNode(val=i)
        p = p.next
    return h.next


def println(h):
    while h:
        print(h.val, end=' -> ')
        h = h.next
    print('None')


l1 = [1, 2, 3, 4, 5]
li1 = buildln(l1)

println(li1)

println(s.reorderList(li1))