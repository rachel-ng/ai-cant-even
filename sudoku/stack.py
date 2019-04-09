class Stack:
    def __init__ (self, size=100):
        self.size = 0 # self.size - 1 == index of item at position
        self.stack = [None] * size

    def push (self, data):
        if self.size - 1 > len(self.stack): self.stack + [data]
        else: self.stack[self.size] = data
        self.size += 1

    def pop (self):
        popped, self.stack[self.size - 1] = self.stack[self.size - 1], None
        self.size -= 1
        return popped

    def peek(self):
        return self.stack[self.size - 1]

st = Stack(10)
print(st.peek())
print(st.pop())
st.push(1)
st.push(2)
st.push(9)
print(st.peek())
print(st.pop())
st.push(5)
st.push(7)
print(st.peek())
print(st.pop())
st.push(3)
st.push(5)
st.push(9)
print(st.stack)
print(st.peek())
print(st.pop())
print(st.stack)
