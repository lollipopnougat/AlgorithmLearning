class StockSpanner:
    def __init__(self):
        self.stack = [(-1, float('inf'))]
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]

class StockSpanner2(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner2()
param1 = [[100], [80], [60], [70], [60], [75], [85]]
res = []
for i in param1:
    res.append(obj.next(i[0]))
print(res)