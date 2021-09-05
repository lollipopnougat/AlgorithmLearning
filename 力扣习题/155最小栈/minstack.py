class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.mi = float('inf')


    def push(self, val: int) -> None:
        self.s.append(self.mi)
        if self.mi > val:
            self.mi = val
        self.s.append(val)



    def pop(self) -> None:
        self.s.pop()
        self.mi = self.s[-1]
        self.s.pop()


    def top(self) -> int:
        return self.s[-1]


    def getMin(self) -> int:
        return self.mi



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()