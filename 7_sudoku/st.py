#!/usr/bin/python3
import sys

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

Cliques=[[0,1,2,3,4,5,6,7,8],
[9,10,11,12,13,14,15,16,17],
[18,19,20,21,22,23,24,25,26],
[27,28,29,30,31,32,33,34,35],
[36,37,38,39,40,41,42,43,44],
[45,46,47,48,49,50,51,52,53],
[54,55,56,57,58,59,60,61,62],
[63,64,65,66,67,68,69,70,71],
[72,73,74,75,76,77,78,79,80],
[0,9,18,27,36,45,54,63,72],
[1,10,19,28,37,46,55,64,73],
[2,11,20,29,38,47,56,65,74],
[3,12,21,30,39,48,57,66,75],
[4,13,22,31,40,49,58,67,76],
[5,14,23,32,41,50,59,68,77],
[6,15,24,33,42,51,60,69,78],
[7,16,25,34,43,52,61,70,79],
[8,17,26,35,44,53,62,71,80],
[0,1,2,9,10,11,18,19,20],
[3,4,5,12,13,14,21,22,23],
[6,7,8,15,16,17,24,25,26],
[27,28,29,36,37,38,45,46,47],
[30,31,32,39,40,41,48,49,50],
[33,34,35,42,43,44,51,52,53],
[54,55,56,63,64,65,72,73,74],
[57,58,59,66,67,68,75,76,77],
[60,61,62,69,70,71,78,79,80]]

cliques_r = [[0,1,2,3,4,5,6,7,8],
[9,10,11,12,13,14,15,16,17],
[18,19,20,21,22,23,24,25,26],
[27,28,29,30,31,32,33,34,35],
[36,37,38,39,40,41,42,43,44],
[45,46,47,48,49,50,51,52,53],
[54,55,56,57,58,59,60,61,62],
[63,64,65,66,67,68,69,70,71],
[72,73,74,75,76,77,78,79,80]]

cliques_c = [[0,9,18,27,36,45,54,63,72],
[1,10,19,28,37,46,55,64,73],
[2,11,20,29,38,47,56,65,74],
[3,12,21,30,39,48,57,66,75],
[4,13,22,31,40,49,58,67,76],
[5,14,23,32,41,50,59,68,77],
[6,15,24,33,42,51,60,69,78],
[7,16,25,34,43,52,61,70,79],
[8,17,26,35,44,53,62,71,80]]

cliques_s = [[0,1,2,9,10,11,18,19,20],
[3,4,5,12,13,14,21,22,23],
[6,7,8,15,16,17,24,25,26],
[27,28,29,36,37,38,45,46,47],
[30,31,32,39,40,41,48,49,50],
[33,34,35,42,43,44,51,52,53],
[54,55,56,63,64,65,72,73,74],
[57,58,59,66,67,68,75,76,77],
[60,61,62,69,70,71,78,79,80]]

def s_board (in_f):
    i_file = open(in_f,"r")
    input_f = [line.strip().split(",") for line in i_file]
    i_file.close()
    board = [int(n) if n != '_' else 0
                   for i in input_f
                   for n in i]
    print(board)
    print(len(board))
    rec = dict([[i,[[0] * 9,[0] * 9]] for i in range(10)[1:]])
    possible = dict([[i,[[],[]]] for i in range(10)[1:]])
    squares =  dict([[i,[[0] * 3,[0] * 3,[0] * 3]] for i in range(10)[1:]])
    squares_2 =  dict([[i,[0] * 9] for i in range(10)[1:]])

    print(rec)
    print(possible)
    print(squares)
    print(squares_2)

    # for n,p in enumerate(board):
    #     print(n,p)
    #     rs = n % 9 // 3 + 1#n // 9 +  1
    #     cs = n % 3 // 3 + 1#n // 3 + 1
    #     box = (rs - 1)* 3 + cs
    #     print(rs,cs,box)
    #     print((n + 1) % 9)
    #     print((n + 1) % 3)

        print("")

    print("squares")
    for i in squares:
        print(i)
        for x in squares[i]:
            print(x)
        print("")

    print("squares 2")
    for i in squares_2:
        print(squares_2[i])
    for i in rec:
        possible[i][0] =  [n for n,p in enumerate(rec[i][0],0) if p == 0]#r
        possible[i][1] =  [n for n,p in enumerate(rec[i][1],0) if p == 0]#c

    print("rec",rec)
    print("possible",possible)
    #print(possible == rec_2)
    print("squares",squares)
    # for i in range(9):
    #     print(i)
    #     print(i % 3)
    #     print(i // 3 + 1)
    #     print('\n')

if __name__ == "__main__":
     s_board(sys.argv[1])
