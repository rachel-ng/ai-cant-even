#!/usr/bin/python3
import sys

def s_board (in_f):
    i_file = open(in_f,"r")
    input_f = [line.rstrip().split(",") for line in i_file]
    i_file.close()
    board = [[int(n) if n != '_' else 0 for n in i] for i in input_f]

    print("board")
    for i in board:
        print (i)

    rec = dict([[i,[[0] * 9,[0] * 9]] for i in range(10)[1:]])
    possible = dict([[i,[[],[]]] for i in range(10)[1:]])
    squares =  dict([[i,[[0] * 3,[0] * 3,[0] * 3]] for i in range(10)[1:]])
    squares_2 =  dict([[i,[0] * 9] for i in range(10)[1:]])
    #print(possible)

    r = 0
    while r < 9:
        c = 0
        while c < 9:
            n = board[r][c]
            rs = r // 3 + 1
            cs = c // 3 + 1
            box = (rs - 1)* 3 + cs
            if n > 0:
                rec[n][0][r] = n
                rec[n][1][c] = n
                squares[box][r % 3][c % 3] = n
                squares_2[box][(r % 3) * 3 + (c % 3)] = n
            c += 1
        r += 1

    print("squares")
    for i in squares:
        print(i)
        for x in squares[i]:
            print(x)
        print("")
    print("squares 2")
    for i in squares_2:
        print(squares_2[i])
    print("board")
    for i in board:
        print (i)
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
