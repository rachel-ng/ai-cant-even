#!/usr/bin/python
import sys

def OrdinaryComparison(a,b):
    if a < b: return -1
    if a == b: return 0
    return 1

def len_comp(a,b):
    if len(a) == len(b):
        if a[0] < b[0]:
            return -1
        if a[0] > b[0]:
            return 1
        else:
            return 0
    if len(a) < len(b):
        return -1
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
        return self.list[1 : self.size + 1]

def dctnry (lngth):
    try:
        ln = range(lngth)
        fin = open("dictall.txt","r")
        d_file = [i for i in fin.read().split("\n") if i != "" and len(i) == lngth]
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

def word_diff (a,b):
    sim = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            sim += 1
    return sim

def letters (a,b):
    a_l = list(a)
    b_l = list(b)
    a_l.sort()
    b_l.sort()
    if a_l == b_l:return True
    else: return False

def search (dct,lngth,start,end):
    if end in dct[start] or start in dct[end]:
        return [start,end]
    u = dct[start].copy()
    f = Pqueue(len_comp,[[word_diff(start,end) + word_diff(i,end),start,i] for i in dct[start] - set([start])])
    e = set([start])
    while f.size > 0:
        w = f.pop()
        e.add(w[-1])
        l = dct[w[-1]] - e - u
        u |= l
        if end in l:
            ans = w[1:] + [end]
            return ans
        f.push_all([[w[0] + word_diff(w[-1],end)] + w[1:] + [n] for n in l])
    return [start,end]


def wordladder (in_f,out_f):
    try:
        i_file = open(in_f,"r")
        input_f = [line.rstrip().split(",") for line in i_file]
        i_file.close()
        s = ""
        lngth = len(input_f[0][0])
        dct = dctnry(lngth)
        for i in input_f:
            for l in search(dct,lngth,i[0],i[1]):
                s += l + ","
            s = s[:-1]
            s += "\n"
        o_file = open(out_f, "w+")
        o_file.write(s)
        o_file.close()
    except FileNotFoundError:
        print("so uh," + in_f + "doesn't exist broski")


if __name__ == "__main__":
    #wordladder(sys.argv[1], sys.argv[2])
    n = 5
    d = dctnry(n)
    #print(d)
    s = ""

    place = dict([[i, set([])] for i in "abcdefghijklmnopqrstuvwxyz"])


    searched = set()
    for i in d:
        c = 1
        af_2 = [i]
        if i not in searched:
            searched.add(i)
            for x in d:
                if x not in searched:
                    if letters(i,x):
                        af_2.append(x)
                        c += 1
                        searched.add(x)
            #else:
                #print(i + "\t" + x)
        if c > 2:
            s += i + " " + str(c) + "\t" + str(af_2) + "\n\n"
    #print("\n\n\n")
    o_file = open("anagrams" + str(n) + ".txt", "w+")
    o_file.write(s)
    o_file.close()

    print (place)

    #python3 neighbors.py  harry.txt  answers.txt
    #python3 neighbors.py doublets.txt adfjkls.txt
