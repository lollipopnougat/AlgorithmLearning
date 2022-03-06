# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List
class NestedInteger:
    resnum = None
    reslis = []
    typ = None
    def __init__(self, type: int, value: int or List['NestedInteger']):
        self.typ = type
        if type == 0:
            self.resnum = value
        else:
            self.reslis = value

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self.typ == 0

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.resnum

    def getList(self) -> List['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.reslis

class NestedIterator:
    def __init__(self, nestedList: List['NestedInteger']):
        self.list = nestedList
        
    
    def next(self) -> int:
        return self.list.pop(0).getInteger()
    
    def hasNext(self) -> bool:
        while self.list:
            if self.list[0].isInteger():
                return True
            else:
                t = self.list.pop(0).getList()
                for i in range(len(t)):
                    self.list.insert(i, t[i])
        return False

def build_nested(li: list) -> List[NestedInteger]:
    head = []
    for i in li:
        if isinstance(i, int):
            head.append(NestedInteger(0, i))
        else:
            head.append(NestedInteger(1, build_nested(i)))
    return head

lis_o = [[1,1],2,[1,1]]

li = build_nested(lis_o)

s = NestedIterator(li)

lis = []
while s.hasNext():
    lis.append(s.next())
print(lis)



         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())