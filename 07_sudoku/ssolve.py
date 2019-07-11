#!/usr/bin/python3
import sys

def s_board (in_f):
    i_file = open(in_f,"r")
    input_f = [line.rstrip().split(",") for line in i_file]
    i_file.close()
    boards = dict()
    prev = ""
    print(input_f)
    for i in input_f:
        if len(i) == 3:
            prev = i[0] #i[1]+"-"+i[2]
            if i[2] == 'solved':
                boards[prev] = [False] # do i need to solve this board?
            else:
                boards[prev] = [True]
        elif i[0] != '':
            boards[prev].append([int(n) if n != '_' else 0 for n in i])
            print(boards[prev])
    print(boards)
    solve = dict([[i,boards[i][1:]] for i in boards if boards[i][0]])
    rec = dict([[i,[[[0] * 9,[0] * 9]] * 10] for i in solve])
    for i in rec:
        print(i)
        for x in rec[i]:
            print(x[0],x[1])
    for i in solve:
        r = 0
        while r < 9:
            c = 0
            print(solve[i][r])
            while c < 9:
                n = solve[i][r][c]
                if n > 0:
                    print(r,c,n)
                    print(n)
                    print(rec[i][n])
                    rec[i][n][0][r] = n
                    rec[i][n][1][c] = n
                    print(rec[i][n])
                    print("\n")
                c += 1

            r += 1
            for x in rec[i]:
                print (x)
        break
    print("\n\n")
    for i in rec:
        print(i)
        for x in rec[i]:
            print(x)

if __name__ == "__main__":
     s_board(sys.argv[1])
