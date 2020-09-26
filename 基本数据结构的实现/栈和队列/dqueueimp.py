class Dqueue:
    def __init__(self) -> None:
        self.stack = []
        self.length = 0

    def add_front(self, x) -> None:
        self.stack.insert(0, x)
        self.length += 1
    
    def add_rear(self, x) -> None:
        self.stack.append(x)
        self.length += 1
    
    def remove_front(self):
        if self.length > 0:
            return self.stack.pop(0)
        else:
            return None

    def remove_rear(self):
        if self.length > 0:
            return self.stack.pop()
        else:
            return None
    
    def front(self):
        if self.length > 0:
            return self.stack[0]
        else:
            return None
    
    def rear(self):
        if self.length > 0:
            return self.stack[-1]
        else:
            return None
    
    def clear(self) -> None:
        self.stack.clear()
        self.length = 0
    
    def empty(self) -> bool:
        if self.length == 0:
            return True
        else:
            return False

    def __iter__(self):
        return self.stack.__iter__()
    
    def __len__(self):
        return self.length

st = Dqueue()
st.add_front(1)
st.add_rear(6)
st.add_front(4)
print(max(st))
print(len(st))
print(st.front())
print(st.remove_rear())
print(st.rear())
