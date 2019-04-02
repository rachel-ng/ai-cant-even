#!/usr/bin/python3
import sys

def s_board (in_f):
    i_file = open(in_f,"r")
    input_f = [line.rstrip().split(",") for line in i_file]
    i_file.close()
    board = [[int(n) if n != '_' else 0 for n in i] for i in input_f]
    for i in board:
        print (i)
    rec = dict([[i,[[0] * 9,[0] * 9]] for i in range(10)[1:]])
    rec_2 = dict([[i,[[],[]]] for i in range(10)[1:]])
    possible = dict([[i,[[],[]]] for i in range(10)[1:]])
    print(possible)
    r = 0
    while r < 9:
        c = 0
        while c < 9:
            n = board[r][c]
            if n > 0:
                rec[n][0][r] = n
                rec[n][1][c] = n
                rec_2[n][0].append(r)
                rec_2[n][1].append(c)
            c += 1
        r += 1

    for i in rec:
        possible[i][0] =  [n for n,p in enumerate(rec[i][0],0) if p == 0]#r
        possible[i][1] =  [n for n,p in enumerate(rec[i][1],0) if p == 0]#c

    print(rec)
    print(rec_2)
    print(possible)

if __name__ == "__main__":
     s_board(sys.argv[1])
