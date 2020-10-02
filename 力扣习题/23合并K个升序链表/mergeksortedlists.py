# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildlinklist(li):
    root = ListNode(None)
    p = root
    for i in li:
        p.next = ListNode(i)
        p = p.next
    return root.next

def printli(root):
    while root:
        print(root.val, end=' ')
        root = root.next
    print(' ')

class Solution:
    '''
    超时😂 
    '''
    def mergeKLists(self, lists: list) -> ListNode:
        head = ListNode(None)
        p = head
        n = len(lists)
        nums = 0
        for i in lists:
            t = i
            while t:
                t = t.next
                nums += 1
        c = 0
        while c < nums:
            minval = 0
            for i in range(n):
                if lists[i] and lists[i].val < lists[minval].val if lists[minval] else float('inf'):
                    minval = i
            p.next = lists[minval]
            p = p.next
            c += 1
            if lists[minval]:
                lists[minval] = lists[minval].next
        return head.next


class Solution2:
    def mergeKLists(self, lists: list) -> ListNode:
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next

ln1 = buildlinklist([1, 4, 5])
ln2 = buildlinklist([1, 3, 4])
ln3 = buildlinklist([2, 6])

s = Solution()

sss = s.mergeKLists([ln1,ln2,ln3])




printli(sss)


