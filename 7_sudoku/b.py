#!/usr/bin/python3
import sys
from datetime import datetime

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

cliques_r = [[0,1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16,17],[18,19,20,21,22,23,24,25,26],[27,28,29,30,31,32,33,34,35],[36,37,38,39,40,41,42,43,44],[45,46,47,48,49,50,51,52,53],[54,55,56,57,58,59,60,61,62],[63,64,65,66,67,68,69,70,71],[72,73,74,75,76,77,78,79,80]]

cliques_c = [[0,9,18,27,36,45,54,63,72],[1,10,19,28,37,46,55,64,73],[2,11,20,29,38,47,56,65,74],[3,12,21,30,39,48,57,66,75],[4,13,22,31,40,49,58,67,76],[5,14,23,32,41,50,59,68,77],[6,15,24,33,42,51,60,69,78],[7,16,25,34,43,52,61,70,79],[8,17,26,35,44,53,62,71,80]]

cliques_s = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]

def coords (n) :
    r = n // 9 # row
    c = n % 9 # col
    s = (r // 3) * 3 + (c // 3) # square
    #s_pos = (r % 3) * 3 + (c % 3)
    #pos = r * 9 + c # calculate the original position
    return r, c, s

# States
NEW_CELL = 0
FIND_NEXT_CELL = 1
BACKTRACK = 2
AllVals = set([1,2,3,4,5,6,7,8,9])

def getBoard(argv):
    i_file = open(argv[1],"r")
    input_f = [line.rstrip().split(",") for line in i_file]
    i_file.close()
    boards = dict()
    prev = ""
    for i in input_f:
        if len(i) == 3:
            prev = i[1] +"-"+i[2]
            if i[2] == 'solved':
                boards[prev] = [] # do i need to solve this board?
            else:
                boards[prev] = []
        elif i[0] != '':
            boards[prev].append([int(n) if n != '_' else 0 for n in i])
    n = argv[3].split(',')
    if n[1] + "-solved" in boards.keys(): solution = [n for i in boards[n[1] + "-solved"] for n in i]
    else: solution = "no sol in file"
    return n[1] + '-' + n[2], [n for i in boards[n[1] + '-' + n[2]] for n in i], solution

def makeNeighbors(board):
    global r, c, s
    r = dict([[n,[board[k] for k in i]] for n,i in enumerate(cliques_r)]) # n // 9
    c = dict([[n,[board[k] for k in i]] for n,i in enumerate(cliques_c)]) # n % 9
    s = dict([[n,[board[k] for k in i]] for n,i in enumerate(cliques_s)]) # (rs // 3) * 3 + (cs // 3)
    return r, c, s

def nextOpenCell (board, start):
    try: return board.index(0, start+1)
    except ValueError: return None

def coords (n) :
    r = n // 9 # row
    c = n % 9 # col
    s = (r // 3) * 3 + (c // 3) # square
    s_pos = (r % 3) * 3 + (c % 3)
    pos = r * 9 + c # calculate the original position
    return r, c, s

def nextValidGuess(board, cell, start):
    rs, cs, ss = coords(cell)
    makeNeighbors(board)
    pos = (AllVals - set(r[rs])) & (AllVals - set(c[cs])) & (AllVals - set(s[ss]))
    while start in r[rs] or start in c[cs] or start in s[ss]: start+= 1
    if start in AllVals:return start, len(pos) < 1
    else: return False, False

def printBoard(board):
    rip = ""
    print("rows")
    for i in [[board[k] for k in i] for n,i in enumerate(cliques_r)]:
        rip += str(i) + "\t" + sum(i) + "\n"
        if sum(i) != 45: rip += "oh shieeeeeet, you done fucked up broski " + str(i)
        if set(i) - AllVals != set(): rip += "oh shieeeeeet dawg, you REALLY really done fucked up " + str(i)
    print("cols")
    for i in [[board[k] for k in i] for n,i in enumerate(cliques_c)]:
        rip += str(i) + "\t" + sum(i) + "\n"
        if sum(i) != 45: rip += "oh shieeeeeet, you done fucked up broski " + str(i)
        if set(i) - AllVals != set(): rip += "oh shieeeeeet dawg, you REALLY really done fucked up " + str(i)
    print("squares")
    for i in [[board[k] for k in i] for n,i in enumerate(cliques_s)]:
        rip += str(i) + "\t" + sum(i) + "\n"
        if sum(i) != 45: rip += "oh shieeeeeet, you done fucked up broski " + str(i)
        if set(i) - AllVals != set(): rip += "oh shieeeeeet dawg, you REALLY really done fucked up " + str(i)

def writeBoard(argv,name,board,nback):
    o_file = open(argv[3].replace(".","_").split(",")[1], "w+")
    s = str(nback) + "\n"

    for n,p in enumerate(board):
        if n % 9 == 8: s += str(p) + "\n"
        else: s += str(p) + ","

    o_file.write(s)
    o_file.close()

def main(argv=None):
    start = datetime.now()
    if not argv:
        argv = sys.argv
    name,board,solution = getBoard(argv)
    #print(name, board)
    mystack = MyStack()
    makeNeighbors(board)
    nback = 0
    ntrials = 0
    cell = nextOpenCell(board,-1)
    state = NEW_CELL
    while True:
        ntrials += 1
        if ntrials % 10000 == 0: print ('ntrials,nback',ntrials,nback)

        if state == NEW_CELL: # we're on a new open cell
            guess,forced = nextValidGuess(board,cell,1)
            #print ("NEW_CELL,cell,guess,forced",cell,guess,forced)
            if not guess: # failed to find a valid guess for this cell, backtrack
                state = BACKTRACK
            else:
                board[cell] = guess
                if not forced:
                    mystack.push([cell,board[:]])
                state = FIND_NEXT_CELL
            continue

        if state == FIND_NEXT_CELL: # find a new open cell
            cell = nextOpenCell(board,cell)
            if not cell: # Solution!
                break
            state = NEW_CELL
            continue

        if state == BACKTRACK: # backtrack
            nback += 1
            cell,board = mystack.pop()
            old_guess = board[cell]
            guess,forced = nextValidGuess(board,cell,old_guess+1)  # note: state cannot be forced
            #print('BACKTRACK,cell,guess,forced',cell,guess,forced)
            if not guess:
                state = BACKTRACK
            else:
                board[cell] = guess
                mystack.push([cell,board[:]])
                state = FIND_NEXT_CELL
            continue

    end = datetime.now()-start
    print(nback)
    if solution == "no sol in file":
        print(writeBoard(argv,name,board,str(nback) + "\t" + str(end) + "\n"+ printBoard(board)))
    else:print(board == solution)






if __name__ == "__main__":
     main()
