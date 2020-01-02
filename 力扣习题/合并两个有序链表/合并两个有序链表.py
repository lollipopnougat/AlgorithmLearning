# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        st_node = None
        ret_node = st_node
        if l1 != None and l2 != None:
            if l1.val < l2.val:
                st_node = ListNode(l1.val)
                ret_node = st_node
                l1 = l1.next
            else:
                st_node = ListNode(l2.val)
                ret_node = st_node
                l2 = l2.next
        elif l1 == None and l2 == None:
            return None
        elif l2 == None:
            return l1
        elif l1 == None:
            return l2
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                st_node.next = ListNode(l1.val)
                st_node = st_node.next
                l1 = l1.next
            else:
                st_node.next = ListNode(l2.val)
                st_node = st_node.next
                l2 = l2.next
        while l1 != None:
            st_node.next = ListNode(l1.val)
            l1 = l1.next
            st_node = st_node.next
        while l2 != None:
            st_node.next = ListNode(l2.val)
            l2 = l2.next
            st_node = st_node.next
        return ret_node

# 大佬的解答
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = header = ListNode(-1)
        # current = header
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 if l1 is not None else l2 # 奇妙的写法
        return header.next

l1 = ListNode(1)
p = l1
p.next = ListNode(2)
p = p.next
p.next = ListNode(4)

#l1 = None
#l2 = None#ListNode(5)
l2 = ListNode(1)
p = l2
p.next = ListNode(3)
p = p.next
p.next = ListNode(4)

s = Solution2()

node = s.mergeTwoLists(l1, l2)

while node != None:
    print(str(node.val) + ' -> ', end='')
    node = node.next

print('end')