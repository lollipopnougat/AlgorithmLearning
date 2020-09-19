class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.time = 0


    def get(self, key: int) -> int:
        self.time += 1
        if key in self.cache.keys():
            self.cache[key][1] = self.time 
            return self.cache[key][0]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        self.time += 1
        if len(self.cache) <= self.capacity - 1 or key in self.cache.keys():
            self.cache[key] = [value, self.time]
        else:
            ma = None
            for i in self.cache:
                if not ma or self.time - self.cache[ma][1] < self.time - self.cache[i][1]:
                    ma = i
            self.cache.pop(ma)
            self.cache[key] = [value, self.time]


obj = LRUCache(2)
print(obj.get(2))
print(obj.put(2, 6))
print(obj.get(1))
print(obj.put(1, 5))
print(obj.put(1, 2))
print(obj.get(1))
print(obj.get(2))


# print(obj.put(1, 1))
# print(obj.put(2, 2))
# print(obj.get(1))
# print(obj.put(3, 3))
# print(obj.get(2))
# print(obj.put(4, 4))
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))

class LRUCachenp(dict):

    def __init__(self, capacity: int):
        self.c = capacity

    def get(self, key: int) -> int:
        if key in self:
            self[key] = self.pop(key)
            return self[key]    
        return -1    

    def put(self, key: int, value: int) -> None:
        key in self and self.pop(key) 
        self[key] = value
        len(self) > self.c and self.pop(next(iter(self)))



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)