class Stack:
    def __init__ (self, size=100):
        self.size = 0 # self.size - 1 == index of item at position
        self.list = [None] * size

    def push (self, data):
        if self.size - 1 > len(self.list): self.stack + [data]
        else: self.list[self.size] = data
        self.size += 1

    def pop (self):
        if self.size < 1:
            return None
        else:
            popped, self.list[self.size - 1] = self.list[self.size - 1], None
            self.size -= 1
            return popped

    def peek(self):
        return self.list[self.size - 1]

    def stack(self):
        return self.list[:self.size]

st = Stack(10)

print(st.stack())
print(st.peek())
print(st.pop())

te = [1,2,9,5,7,16,17,5,9,10]
for i in te:
    if i % 3 == 0:
        print(st.peek())
        print(st.pop())
    else:
        st.push(i)
        print(st.stack())
