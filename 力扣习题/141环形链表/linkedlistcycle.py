# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    快慢指针法
    '''
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        s, f = head, head.next
        while s != f:
            if not f or not f.next:
                return False
            s, f = s.next, f.next.next
        return True

class Solutions:
    '''
    hashset hashmap
    '''
    def hasCycle(self, head: ListNode) -> bool:
        se = set()
        while head:
            if head in se:
                return True
            se.add(head)
            head = head.next
        return False

class Solutionm:
    def hasCycle(self, head: ListNode) -> bool:
        m = {}
        while head:
            if head in m:
                return True
            else:
                m[head] = True
                head = head.next
        return False



class Solutiond:
    '''
    抖机灵之损坏链表法
    '''
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val == 'bjfuvth':
                return True
            else:
                head.val = 'bjfuvth'
            head = head.next
        return False