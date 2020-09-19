class Queue:
    def __init__(self) -> None:
        self.stack = []
        self.length = 0

    def enqueue(self, x) -> None:
        self.stack.append(x)
        self.length += 1
    
    def dequeue(self):
        if self.length > 0:
            return self.stack.pop(0)
        else:
            return None
    
    def front(self):
        if self.length > 0:
            return self.stack[0]
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

st = Queue()
st.enqueue(1)
st.enqueue(6)
st.enqueue(4)
print(max(st))
print(len(st))
print(st.dequeue())
print(st.dequeue())
print(st.dequeue())
