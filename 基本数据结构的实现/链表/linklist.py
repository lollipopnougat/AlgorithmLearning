class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.val = value

class LinkList:
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
        else:
            self.head = node

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
        p.next = node
        return True
    
    def insert_value(self, value, index: int) -> bool:
        node = Node(value)
        return self.insert_node(node, index)

    def swap_nodes(self, indexl: int, indexr: int) -> bool:
        if indexl > self.length or indexr > self.length or indexl == indexr:
            return False
        head = Node(None)
        if indexl > indexr:
            indexl, indexr = indexr, indexl
        head.next = self.head
        tmp = None
        if indexl == 0:
            tmp = head
        else:
            p = self.head
            i = 0
            while i < indexl - 1:
                p = p.next
                i += 1
            tmp = p
        i = 0
        p = self.head
        while i < indexr - 1:
            p = p.next
        
        





        



li = LinkList()

li.add_value(1)
li.add_value(2)
li.add_value(3)
li.add_value(4)
li.add_value(5)
li.insert_value(7, 1)
print(li.to_list())

        


        



