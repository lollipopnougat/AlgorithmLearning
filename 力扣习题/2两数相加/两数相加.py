# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 我的思路 主要是按位计算
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None or l2 == None:
            return l1 if l1 != None else l2
        p = l1
        q = l2
        res_node = ListNode((p.val + q.val) % 10)
        ret_node = res_node
        c = (p.val + q.val) // 10
        p = p.next
        q = q.next
        while p and q:
            res_node.next = ListNode((p.val + q.val + c) % 10)
            c = (p.val + q.val + c) // 10
            res_node = res_node.next
            p = p.next
            q = q.next
        while p:
            res_node.next = ListNode((p.val + c) % 10)
            c = (p.val + c) // 10
            res_node = res_node.next
            p = p.next
        while q:
            res_node.next = ListNode((q.val + c) % 10)
            c = (q.val + c) // 10
            res_node = res_node.next
            q = q.next
        if c != 0:
            res_node.next = ListNode(c)
        return ret_node


# 是大佬 awsl
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            temp = carry
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            cur.next = ListNode(temp % 10)
            carry = temp // 10
            cur = cur.next
        return dummy.next


# 角度刁钻版 突然想到的实现 非常真实
class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def nodeToInt(lis: ListNode) -> int:
            p = lis
            res = 0
            t = 0
            while p:
                res += p.val * 10**t
                p = p.next
                t += 1
            return res

        def intToNode(num: int) -> ListNode:
            head_node = ListNode(num % 10)
            l = num // 10
            p = head_node
            while l != 0:
                p.next = ListNode(l % 10)
                l = l // 10
                p = p.next
            return head_node

        if l1 == None and l2 == None:
            return None
        return intToNode(nodeToInt(l1) + nodeToInt(l2))


def int_to_node(num: int) -> ListNode:
            head_node = ListNode(num % 10)
            l = num // 10
            p = head_node
            while l != 0:
                p.next = ListNode(l % 10)
                l = l // 10
                p = p.next
            return head_node


l1 = ListNode(5)
p = l1
p.next = ListNode(6)
p = p.next
p.next = ListNode(4)

l2 = ListNode(2)
p = l2
p.next = ListNode(4)
p = p.next
p.next = ListNode(3)

l3 = int_to_node(999)
l4 = int_to_node(1)
s = Solution3()
s2 = Solution2()

res = s.addTwoNumbers(l1, l2)
res2 = s2.addTwoNumbers(l3,l4)
while res:
    print(str(res.val) + ' -> ', end='')
    res = res.next
print('end1')

while res2:
    print(str(res2.val) + ' -> ', end='')
    res2 = res2.next
print('end2')