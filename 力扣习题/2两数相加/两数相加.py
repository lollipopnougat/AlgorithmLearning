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
        carry = 0
        currentNode = headNode = ListNode(0)
        while l1 or l2:
            theSum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            val = theSum % 10
            carry = theSum // 10
            currentNode.val = val
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2:
                currentNode.next = ListNode(0)
                currentNode = currentNode.next
        if carry:
            currentNode.next = ListNode(carry)

        return headNode


# 角度刁钻版 突然想到的实现 非常真实
class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        num1 = self.nodeToInt(l1)
        num2 = self.nodeToInt(l2)
        res = num1 + num2
        return self.intToNode(res)

    def nodeToInt(self, lis: ListNode) -> int:
        p = lis
        res = 0
        t = 0
        while p:
            res += p.val * 10**t
            p = p.next
            t += 1
        return res

    def intToNode(self, num: int) -> ListNode:
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

s = Solution3()

res = s.addTwoNumbers(l1, l2)

while res:
    print(str(res.val) + ' -> ', end='')
    res = res.next
print('end')