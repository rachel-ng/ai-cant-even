#!/usr/bin/python3
import sys

class Stack:
    def __init__ (self, size=100):
        self.size = 0 # self.size - 1 == index of item at position
        self.list = [None] * size

    def __str__ (self):
        s = ""
        for i in self.stack():
            s += str(i) + "\n"
        return s

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

cliques_r = [[0,1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16,17],[18,19,20,21,22,23,24,25,26],[27,28,29,30,31,32,33,34,35],[36,37,38,39,40,41,42,43,44],[45,46,47,48,49,50,51,52,53],[54,55,56,57,58,59,60,61,62],[63,64,65,66,67,68,69,70,71],[72,73,74,75,76,77,78,79,80]]

cliques_c = [[0,9,18,27,36,45,54,63,72],[1,10,19,28,37,46,55,64,73],[2,11,20,29,38,47,56,65,74],[3,12,21,30,39,48,57,66,75],[4,13,22,31,40,49,58,67,76],[5,14,23,32,41,50,59,68,77],[6,15,24,33,42,51,60,69,78],[7,16,25,34,43,52,61,70,79],[8,17,26,35,44,53,62,71,80]]

cliques_s = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]

def coords (n) :
    r = n // 9 # row
    c = n % 9 # col
    s = (r // 3) * 3 + (c // 3) # square
    s_pos = (r % 3) * 3 + (c % 3)
    pos = r * 9 + c # calculate the original position
    return r, c, s

def update_b (p, val, board, r, c, s):
    rs, cs, ss = coords(p)
    board[p] = val
    r[rs][cs] = val
    c[cs][rs] = val
    s[ss][(rs % 3) * 3 + (cs % 3)]

def s_board (in_f):
    vals = [1,2,3,4,5,6,7,8,9]

    i_file = open(in_f,"r")
    input_f = [line.strip().split(",") for line in i_file]
    i_file.close()

    stacked = Stack()

    board = [int(n) if n != '_' else 0 for i in input_f for n in i]
    empty = set([n for n,p in enumerate(board) if p == 0])
    possible = dict([[i,None]for i in empty])

    print(board)
    print(len(board))
    print(empty)

    # k = rs * 9 + cs
    r = dict([[n,[board[k] for k in i]] for n,i in enumerate(cliques_r)]) # n // 9
    c = dict([[n,[board[k] for k in i]] for n,i in enumerate(cliques_c)]) # n % 9
    s = dict([[n,[board[k] for k in i]] for n,i in enumerate(cliques_s)]) # (rs // 3) * 3 + (cs // 3)

    print("r\n",r)
    print("c\n",c)
    print("s\n",s)

    for i in empty:
        #print(i)
        rs, cs, ss = coords(i)
        pos_r = set(vals[:]) - set(r[rs])
        pos_c = set(vals[:]) - set(c[cs])
        pos_s = set(vals[:]) - set(s[ss])
        # print(rs, r[rs], set(vals[:]) - set(r[rs]))
        # print(cs, c[cs], set(vals[:]) - set(c[cs]))
        # print(ss, s[ss], set(vals[:]) - set(s[ss]))
        pos_each = pos_r & pos_c & pos_s
        #print(len(pos_each),"\t", pos_each)
        possible[i] = pos_each

    for i in possible:
        if len(possible[i]) == 1:
            rs, cs, ss = coords(i)
            #board[i] = list(possible[i])[0]
            #print("place in sqaure",(rs % 3) * 3 + (cs % 3))
            #print(rs,cs,ss)
            #print(cliques_s[ss])
            #print(s[ss])
            update_b (i, possible[i].pop(), board, r, c, s)
            #print(s[ss])
            stacked.push([i,board[:]])
            possible[i] = None
            #print (i,"\t\n")

    print("\nstack")

    print(stacked)
    print(possible)
    #if sum(board) == 1215:
    #    True



if __name__ == "__main__":
     s_board(sys.argv[1])
