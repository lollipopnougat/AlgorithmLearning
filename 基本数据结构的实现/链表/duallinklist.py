class Node:
    def __init__(self, value) -> None:
        self.pre = None
        self.next = None
        self.val = value


class DualLinkList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def add_node(self, node: Node) -> None:
        self.length += 1
        if self.head:
            p = self.head
            while p.next:
                p = p.next
            p.next = node
            node.pre = p
        else:
            self.head = node
        node.next = None

    def add_value(self, value) -> None:
        node = Node(value)
        self.add_node(node)
    
    def del_node(self, index: int) -> bool:
        if index >= self.length:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        p = self.head
        num = 0
        while num < index - 1:
            p = p.next
            num += 1
        p.next = p.next.next
        if p.next.next:
            p.next.next.pre = p
        return True
    
    def to_list(self) -> list:
        res = []
        p = self.head
        while p:
            res.append(p.val)
            p = p.next
        return res
        
    def insert_node(self, node:Node, index: int) -> bool:
        if index >= self.length:
            return False
        if index == 0:
            node.next = self.head
            self.head = node
            return True
        p = self.head
        num = 0
        while num < index - 1:
            p = p.next
            num += 1
        node.next = p.next
        if p.next:
            p.next.pre = node
        p.next = node
        node.pre = p
        return True
    
    def insert_value(self, value, index: int) -> bool:
        node = Node(value)
        return self.insert_node(node, index)

    def swap_nodes(self, indexl: int, indexr: int) -> bool:
        if self.length < 2 or indexl > self.length or indexr > self.length or indexl == indexr:
            return False
        head = Node(None)
        if indexl > indexr:
            indexl, indexr = indexr, indexl
        head.next = self.head
        count = 0
        w1, p1 = head.next, head
        a1 = w1.next
        while count < indexl:
            p1, w1 = w1, w1.next
            a1 = w1.next
            count += 1
        p2, w2, a2 = p1, w1, a1
        while count < indexr:
            p2, w2 = w2, w2.next
            a2 = w2.next
            count += 1
        p1.next = w2
        w1.next = a2
        if p1 != head:
            w2.pre = p1
        if w2 != a1:
            w2.next = a1
            p2.next = w1
            w1.pre = p2
            a1.pre = w2
        else:
            w2.next = w1
            w1.pre = w2
        if a2:
            a2.pre = w1
        self.head = head.next

li = DualLinkList()

li.add_value(1)
li.add_value(2)
li.add_value(3)
li.add_value(4)
li.add_value(5)
li.insert_value(7, 1)
li.swap_nodes(1, 5)
print(li.to_list())