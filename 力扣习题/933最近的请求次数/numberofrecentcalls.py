from collections import deque
class RecentCounter:

    # 注意减少遍历
    def __init__(self):
        self.count = deque()
        


    def ping(self, t: int) -> int:
        self.count.append(t)
        while self.count[0] < t - 3000:
            self.count.popleft()
        return len(self.count)
        



s = RecentCounter()

print(s.ping(1))
print(s.ping(2))
print(s.ping(3))
print(s.ping(4))
print(s.ping(5))
print(s.ping(10))
print(s.ping(3001))
print(s.ping(3002))
print(s.ping(3003))
print(s.ping(3004))
print(s.ping(3005))
print(s.ping(3011))
s = RecentCounter()
args = [1, 100, 3001, 3002]
res = list(map(lambda x: s.ping(x), args))
print(res)