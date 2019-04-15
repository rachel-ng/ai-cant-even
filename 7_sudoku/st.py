#!/usr/bin/python3
import sys
import copy

class MyStack:
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

cliques = [[0,1,2,3,4,5,6,7,8],
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

cliques_r = [[0,1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16,17],[18,19,20,21,22,23,24,25,26],[27,28,29,30,31,32,33,34,35],[36,37,38,39,40,41,42,43,44],[45,46,47,48,49,50,51,52,53],[54,55,56,57,58,59,60,61,62],[63,64,65,66,67,68,69,70,71],[72,73,74,75,76,77,78,79,80]]

cliques_c = [[0,9,18,27,36,45,54,63,72],[1,10,19,28,37,46,55,64,73],[2,11,20,29,38,47,56,65,74],[3,12,21,30,39,48,57,66,75],[4,13,22,31,40,49,58,67,76],[5,14,23,32,41,50,59,68,77],[6,15,24,33,42,51,60,69,78],[7,16,25,34,43,52,61,70,79],[8,17,26,35,44,53,62,71,80]]

cliques_s = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]

NEW_CELL = 0
FIND_NEXT_CELL = 1
BACKTRACK = 2
AllVals = set([1,2,3,4,5,6,7,8,9])

def s_board (in_f):
    vals = [1,2,3,4,5,6,7,8,9]

    i_file = open(in_f,"r")
    input_f = [line.strip().split(",") for line in i_file]
    i_file.close()

    stacked = MyStack()

    board = [int(n) if n != '_' else 0 for i in input_f for n in i]
    empty = set([n for n,p in enumerate(board) if p == 0])
    possible = dict([[i,None]for i in empty])

    print(board)
    print(len(board))
    print(empty)

    neighbors = dict([i,set([member for clique in cliques if i in clique for member in clique if member != i])] for i in range(81))

    print("")
    print(neighbors)
    print("")

    for i in empty:
        possible[i] = set(vals[:]) - set([board[k] for k in neighbors[i]])
        print(i, possible[i])

   # for i in possible:
        #rs, cs, ss = coords(i)
        #update_b (i, possible[i].pop(), board, r, c, s)
        #if len(possible[i]) == 0:
        #board[i] = possible[i].pop()
        #print(i)
        #r[rs][cs] = board[i]
        #c[cs][rs] = board[i]
        #s[ss][(rs * 3) + cs] = board[i]
        #stacked.push([i,board[:], possible.copy()])

    def nextGuess (cell):
        if len(possible[cell]) > 0:
            return possible[cell].pop(), len(possible[cell]) > 0
        else:
            return False, False

    nback = 0
    ntrials = 0
    cell = empty.pop()
    state = NEW_CELL
    while True:
        ntrials += 1
        #if ntrials % 10000 == 0: print ('ntrials,nback',ntrials,nback)

        #print(stacked)
        print(board)
        print(cell, board[cell])
        if state == NEW_CELL: # we're on a new open cell
            guess,forced = nextGuess(cell)
            board[cell] = guess
            print ("NEW_CELL,cell,guess,forced",cell,guess,forced)
            if not guess: # failed to find a valid guess for this cell, backtrack
                state = BACKTRACK
            else:
                board[cell] = guess
                if not forced:
                    stacked.push([cell, board[:], empty.copy(), possible.copy()])
                state = FIND_NEXT_CELL
            continue

        if state == FIND_NEXT_CELL: # find a new open cell
            cell = empty.pop()
            if not cell: # Solution!
                break
            state = NEW_CELL
            continue

        if state == BACKTRACK: # backtrack
            nback += 1
            cell,board,empty,possible = stacked.pop()
            possible[cell] - {board[cell]}
            guess,forced =  nextGuess(cell) # note: state cannot be forced
            #print('BACKTRACK,cell,guess,forced',cell,guess,forced)
            if not guess:
                state = BACKTRACK
            else:
                board[cell] = guess
                stacked.push([cell, board[:], empty.copy(), possible.copy()])
                state = FIND_NEXT_CELL
            continue

        print("\nstack")

    #print(stacked)
    print(possible)
    #if sum(board) == 1215:
    #    True

    print(board)


if __name__ == "__main__":
     s_board(sys.argv[1])
