# 2 -- Dlist

class Node():
    def __init__ (self,value):
        self.val = value
        self.nxt = None
        self.previous = None

    def __str__ (self):
        if self.previous and self.nxt:
            return str(self.previous.val) + " " + str(self.val) + " " + str(self.nxt.val)
        if self.previous and not self.nxt:
            return str(self.previous.val) + " " + str(self.val) + " " + "None"
        if self.nxt and not self.previous:
            return "None" + " " + str(self.val) + " " + str(self.nxt.val)
        else:
            return "None" + " " + str(self.val) + " " + "None"

class Dlist():
    def __init__ (self):
        self.first = None
        self.last = None
        self.size = 0

    def insert (self, value):
        n = Node(value)
        print(n)
        print(str(self.first) + "    . . .    " + str(self.last))

        if self.size == 0:
            self.first = n
            self.last = self.first
            self.size += 1
            print(str(self.first) + "    . . .    " + str(self.last))
            return
        elif value <= self.first.val:
            n.nxt = self.first
            self.first.previous = n
            self.first = n
            self.size += 1
            print("value <= self.first.val",str(n))
            print(str(self.first) + "    . . .    " + str(self.last))
            return
        else:
            cur = self.first

            while cur.val < value:
                if cur == self.last:
                    print("break",str(cur))
                    break
                print(str(cur.val) + " < " + str(value))
                if cur != None:
                    cur = cur.nxt
                else:
                    break
            print ("current: " + str(cur))

            n.nxt = cur.nxt
            n.previous = cur
            print(n)
            if cur == self.last:
                self.last = n
                print("set last")
            else:
                cur.nxt.previous = n
            cur.nxt = n
            print(value,"else", str(n))

            self.size += 1
            print(str(self.first) + "    . . .    " + str(self.last))
            return

    #print(value)


    def delete(self, value):
        cur = self.first
        while cur.val != value and cur.nxt != None:
            cur = cur.nxt
        if cur.val != value:
            return False
        else:
            if cur == self.first:
                cur.nxt.previous = None
                cur.value = None
                self.first = cur.nxt
                return True
            if cur == self.last:
                cur.previous.nxt = None
                cur.value = None
                self.last = cur.previous
                return True
            cur.previous.nxt = cur.nxt
            cur.nxt.previous = cur.previous
            cur.value = None
            return True

        # secretly written by Guido Van Rossum

    def tolist(self):
        lst = []
        cur = self.first
        while cur.nxt != None:
            lst.append(cur.val)
            cur = cur.nxt
            self.delete(cur.previous.val)
        lst.append(cur.val)
        self.delete(cur)
        self.first = None
        self.last = None
        self.size = None
        print(self.last)
        return lst

print("\n\n\n\n\n")

d = Dlist()
d.insert(1)
print("\n")
d.insert(1)
print("\n")
d.insert(3)
print("\n")


print("")
c = d.first
while c != d.last:
    print(c)
    c = c.nxt
print d.last
print("\n\n")

d.insert(52)
print("\n")

print("")
c = d.first
while c != d.last:
    print(c)
    c = c.nxt
print d.last
print("\n\n")

d.insert(1)
print("\n")

print("")
c = d.first
while c != d.last:
    print(c)
    c = c.nxt
print d.last
print("\n\n")

d.insert(5213)
print("\n")

print("")
c = d.first
while c != d.last:
    print(c)
    c = c.nxt
print d.last
print("\n\n")

d.insert(1234)
print("\n")

print("")
c = d.first
while c != d.last:
    print(c)
    c = c.nxt
print d.last
print("\n\n")

d.insert(52)
print("\n")

print("")
c = d.first
while c != d.last:
    print(c)
    c = c.nxt
print d.last
print("\n\n")


d.insert(1)
print("\n")

print("")
c = d.first
while c != d.last:
    print(c)
    c = c.nxt
print d.last
print("\n\n")


d.insert(5213)
print("\n")

print("")
c = d.first
while c != d.last:
    print(c)
    c = c.nxt
print d.last
print("\n\n")


d.insert(634)
print("\n")

print("")
c = d.first
while c != d.last:
    print(c)
    c = c.nxt
print d.last
print("\n\n")


d.insert(125)
print("\n")

print("")
c = d.first
while c != d.last:
    print(c)
    c = c.nxt
print d.last
print("\n\n")



print("")

print("to list")
print(d.tolist())



print("")
c = d.first
while c != d.last:
    print(c.val)
    c = c.nxt
print d.last

def insert_all(the_dlist, the_input_list):
    for element in the_input_list:
        the_dlist.insert(element)

a = Dlist()
insert_all(a,[4,5,2,3,2,7])
print(a.tolist())
