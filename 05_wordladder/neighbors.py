#!/usr/bin/python
import sys

def OrdinaryComparison(a,b):
    if a < b: return -1
    if a == b: return 0
    return 1

def f_comp(a,b):
    if len(a) < len(b): return -1
    if len(a) == len(b): return 0
    return 1

class Pqueue:
    def __init__ (self, comp = OrdinaryComparison, init=None):
        self.cmpfunc = comp
        self.size = 0
        self.list = [None]
        if init: self.push_all(init)

    def push (self, data):
        if self.size == len(self.list) - 1:
            self.list.append(data)
        else:
            if self.size == 0:
                self.list[1] = data
            else:
                self.list[self.size + 1] = data

        self.size += 1
        if self.size == 1:
            return

        c_ind = self.size
        p_ind = c_ind // 2

        while self.cmpfunc(self.list[p_ind], self.list[c_ind]) == 1 and c_ind != 0:
            self.list[p_ind], self.list[c_ind] = self.list[c_ind], self.list[p_ind]
            c_ind = p_ind
            p_ind = c_ind // 2

            if p_ind == 0 or c_ind == 1:
                break


    def pop (self):
        popped = self.list[1]
        self.list[1] = self.list[self.size]
        self.list[self.size] = None
        self.size -= 1
        if self.size == 1:
            return popped

        pos = 0
        c_ind = 1

        while c_ind < self.size and pos < self.size:
            pos += 1

            if (c_ind * 2 + 1 > self.size or c_ind * 2 + 1 > self.size) or (self.list[c_ind * 2 + 1] == None and self.list[c_ind * 2] == None):
                break

            if self.list[c_ind * 2] == None and self.list[c_ind * 2 + 1] and self.cmpfunc(self.list[c_ind], self.list[c_ind * 2 + 1]) == 1:
                        self.list[c_ind], self.list[c_ind * 2 + 1] = self.list[c_ind * 2 + 1], self.list[c_ind]

            elif self.list[c_ind * 2 + 1] == None and self.list[c_ind * 2] and self.cmpfunc(self.list[c_ind], self.list[c_ind * 2]) == 1:
                        self.list[c_ind], self.list[c_ind * 2] = self.list[c_ind * 2], self.list[c_ind]

            else:
                if self.cmpfunc(self.list[c_ind], self.list[c_ind * 2]) == 1 or self.cmpfunc(self.list[c_ind], self.list[c_ind * 2 + 1]) == 1:
                    if self.cmpfunc(self.list[c_ind * 2], self.list[c_ind * 2 + 1]) == 1:
                        self.list[c_ind], self.list[c_ind * 2 + 1] = self.list[c_ind * 2 + 1], self.list[c_ind]
                        c_ind = c_ind * 2 + 1
                    else:
                        self.list[c_ind], self.list[c_ind * 2] = self.list[c_ind * 2], self.list[c_ind]
                        c_ind = c_ind * 2
                #print("c_ind: " + str(c_ind) + "\tdata: " +  str(self.list[c_ind]) + "\n" + str(self.list))

        return popped

    def peek (self):
        return self.list[1]

    def tolist (self):
        size = self.size
        return [self.pop() for i in range(size)]

    def push_all(self, lst):
        for i in lst:
            self.push(i)

    def internal_list(self):
        #return [i if i is not None for i in self.list]
        return self.list[1 : self.size + 1]

def dctnry (lngth):
    try:
        ln = range(lngth)

        fin = open("dictall.txt","r")
        d_file = [i for i in fin.read().split("\n") if i != "" and len(i) == lngth]
        #dct = dict([[i, []] for i in d_file])

        fin.close()

        d = dict([])
        for word in d_file:
            for i in ln:
                s = word[:i] + "_" + word[i+1:]
                d[s] = d.get(s, []) + [word]

        dct = dict([])
        for word in d_file:
            for i in ln:
                s = word[:i] + "_" + word[i+1:]
                dct[word] =  dct.get(word, []) + d[s]
            dct[word] = set(dct.get(word, []))
        return dct

    except FileNotFoundError:
        print("so uh, you don't have a dictionary broski")

def neighbors (lngth):#in_f, out_f):
    try:
        #i_file = open(in_f,"r")
        #input_f = [line.rstrip().split(",") for line in i_file]
        #i_file.close()

        #print(input_f)
        #lngth = len(input_f[0])

        dct = dctnry(lngth)

        #s = ""
        #for i in input_f:
            #print(dct[i] - set([i]))
            #s += i + "," + str(len(dct[i] - set([i]))) + "\n" + str(dct[i] - set([i])) + "\n"

        #o_file = open(out_f, "w+")
        #o_file.write(s)
        #o_file.close()

        return dct

    except FileNotFoundError:
        print("so uh, " + in_f + " don't exist broski")


def search (dct,start,end) :
    #dct,words = neighbors(in_f, out_f)
    #print(dct)
    u = [[start,i] for i in dct[start] - set([start])] #[[w, [[w,i] for i in dct[w] - set([w])]] for w in words] #+ list(dct[i] - set([i,w]))
    print(u)
    f = Pqueue(f_comp,u)
    e = set([])

    #print (u)

    #for i in u:
        #print(i)
        #print(i[1])
        #f.push_all(i[1])
    e.add(start)
    #print("f:\t" + str(f.internal_list()) + "\n")

    while f.size > 0:
        w = f.pop()
        #print(w[-1])
        e.add(w[-1])
        l = dct[w[-1]] - e
        #print(dct.get(w[-1], set()))
        dct[w[-1]] = set([])
        #print(w)
        #print("to add\t" + str(l)) #str(w) + "\t"
        for s in l:
            if s == end:
                print("\n\nexplored:\t" + str(e))
                print(str(len(w + [s])) + "\t" + str(w + [s]))
                return s
        f.push_all([w + [n] for n in l])
        #print("\nf:\t" + str(f.internal_list()) + "\n")
        #print("\n\n")
    print("\n\nexplored:\t" + str(e))

    # #print(set(u[0][1].internal_list()))
    #print(set(u[1][1].internal_list()))
    #print(set.intersection(*[i for i in f]))
    #print(set([u[0][1].pop() for i in range(u[0][1].size)]) & set([u[1][1].pop() for i in range(u[1][1].size)]))
    #print(set())

    #print(set(u[0][1].internal_list()).intersection())
    print("\nf:\t" + str(f.internal_list()) + "\n")


if __name__ == "__main__":
    #neighbors(sys.argv[1], sys.argv[2])
    search(dctnry(4),"head","tail")#neighbors(sys.argv[1], sys.argv[2]),"head","tails")
    print("\n\n\n")


    #python3 neighbors.py  harry.txt  answers.txt
