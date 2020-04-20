# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 在写两数相加1的时候就想到了

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def nodeToInt(lis: ListNode) -> int:
            p = lis
            res_str = ''
            while p:
                res_str += str(p.val)
                p = p.next
            return int(res_str)

        def intToNode(num: int) -> ListNode:
            res_str = str(num)
            t = 1
            head_node = ListNode(int(res_str[0]))
            p = head_node
            while t < len(res_str):
                p.next = ListNode(int(res_str[t]))
                t += 1
                p = p.next
    
            return head_node

        if l1 == None and l2 == None:
            return None
        return intToNode(nodeToInt(l1) + nodeToInt(l2))