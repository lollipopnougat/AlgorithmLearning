"""
# Definition for a Node.
# """


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return
        m = {}
        cur = head
        while cur:
            m[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            m[cur].next = m[cur.next] if cur.next != None else None
            m[cur].random = m[cur.random] if cur.random != None else None
            cur = cur.next
        return m[head]


def build_list(li: list) -> Node:
    le = len(li)
    res = []
    for i in range(le):
        res.append(Node(li[i][0]))
    for i in range(le - 1):
        res[i].next = res[i + 1]
        res[i].random = res[li[i][1]] if li[i][1] != None else None
    res[le - 1].random = res[li[le - 1][1]] if li[le - 1][1] != None else None
    return res[0]

def tolist(node: Node) -> list:
    cur = node
    m = {}
    c = 0
    while cur:
        m[cur] = c
        c += 1
        cur = cur.next
    res = []
    cur = node
    while cur:
        res.append([cur.val, m[cur.random] if cur.random != None else None])
        cur = cur.next
    return res



h = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

ll = build_list(h)
s = Solution()
ttt = s.copyRandomList(ll)

st = tolist(ttt)
ot = tolist(ll)
print(ot)
print(st)

