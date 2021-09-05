class MinStack:
    # 把每次的最小值都放进去，一次入出栈两个元素
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.mi = float('inf')

    def push(self, x: int) -> None:
        self.s.append(self.mi)
        if self.mi > x:
            self.mi = x
        self.s.append(x)


    def pop(self) -> None:
        self.s.pop()
        self.mi = self.s[-1]
        self.s.pop()


    def top(self) -> int:
        return self.s[-1]


    def min(self) -> int:
        return self.mi



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()