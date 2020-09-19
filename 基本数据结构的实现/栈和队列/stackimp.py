class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.length = 0

    def push(self, x) -> None:
        self.stack.append(x)
        self.length += 1
    
    def pop(self):
        if self.length > 0:
            return self.stack.pop()
        else:
            return None
    
    def top(self):
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

st = Stack()
st.push(1)
st.push(3)
st.push(4)
print(sum(st))
print(len(st))
print(st.pop())
print(st.pop())
print(st.pop())

