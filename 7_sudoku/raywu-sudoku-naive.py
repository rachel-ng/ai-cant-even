#! /usr/bin/python3

# Raymond Wu

import sys

# Simple list implementation of a Stack (FILO)

class Stack:

    def __init__ (self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def tolist(self):
        return self.list

    def clear(self):
        self.list = []

cliques=[[0,1,2,3,4,5,6,7,8],\
         [9,10,11,12,13,14,15,16,17],\
         [18,19,20,21,22,23,24,25,26],\
         [27,28,29,30,31,32,33,34,35],\
         [36,37,38,39,40,41,42,43,44],\
         [45,46,47,48,49,50,51,52,53],\
         [54,55,56,57,58,59,60,61,62],\
         [63,64,65,66,67,68,69,70,71],\
         [72,73,74,75,76,77,78,79,80],\
         [0,9,18,27,36,45,54,63,72],\
         [1,10,19,28,37,46,55,64,73],\
         [2,11,20,29,38,47,56,65,74],\
         [3,12,21,30,39,48,57,66,75],\
         [4,13,22,31,40,49,58,67,76],\
         [5,14,23,32,41,50,59,68,77],\
         [6,15,24,33,42,51,60,69,78],\
         [7,16,25,34,43,52,61,70,79],\
         [8,17,26,35,44,53,62,71,80],\
         [0,1,2,9,10,11,18,19,20],\
         [3,4,5,12,13,14,21,22,23],\
         [6,7,8,15,16,17,24,25,26],\
         [27,28,29,36,37,38,45,46,47],\
         [30,31,32,39,40,41,48,49,50],\
         [33,34,35,42,43,44,51,52,53],\
         [54,55,56,63,64,65,72,73,74],\
         [57,58,59,66,67,68,75,76,77],\
         [60,61,62,69,70,71,78,79,80]\
]

def getBoard(argv):
    input_file = open(INPUT_FILE,'r').read().strip().split('\n')
    board = []
    trip = False
    i = 0
    for line in input_file:
        if trip and i < 9:
            board += line.split(',')
            i += 1
        elif i >= 9:
            break
        if line == argv:
            trip = True
    return argv, board

def makeNeighbors():
    global d
    d = {}
    for i in range(81):
        neighbors = set()
        for clique in cliques:
            if i in clique:
                for clique_member in clique:
                    if clique_member != i:
                        neighbors.add(clique_member)
        d[i] = neighbors
    return d

def nextOpenCell(board, start):
    try:
        retVal = board.index('_', start+1)
    except ValueError:
        retVal = None
    return retVal

def nextValidGuess(board, cell, n):
    neighbors_values = [ board[neighbor] for neighbor in d[cell] ]
    # print(neighbors_values)
    # while True:
    #     if str(n) in neighbors_values or int(n) in neighbors_values:
    #         n += 1
    #         if n > 9:
    #             return False, False
    #     else:
    #         break
    # # print(n)
    # return n, False
    possibilities = AllVals - { int(value) for value in neighbors_values if value != '_' }
    while n not in possibilities and n <= 9:
        n += 1
    if n in AllVals:
        return n, len(possibilities) < 1
    return None, False
    
def printBoard(board):
    i = 0
    line_str = ""
    for s in board:
        line_str += str(s) + ','
        i += 1
        if i == 9:
            print (line_str[:-1])
            line_str = ""
            i = 0

def writeBoard(argv, name, board):
    with open(OUTPUT_FILE, 'w') as output_file:
        i = 0
        line_str = ""
        for s in board:
            line_str += str(s) + ','
            i += 1
            if i == 9:
                output_file.write(line_str[:-1] + '\n')
                line_str = ""
                i = 0

# States
NEW_CELL = 0
FIND_NEXT_CELL = 1
BACKTRACK = 2
AllVals = set([1,2,3,4,5,6,7,8,9])

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
BOARD_TO_SOLVE = sys.argv[3]
    
def main(argv=None):
    if not argv:
        argv = sys.argv
    
    name,board = getBoard(BOARD_TO_SOLVE)
    mystack = Stack()
    makeNeighbors()
    nback = 0
    ntrials = 0
    cell = nextOpenCell(board,-1)
    state = NEW_CELL
    while True:
        ntrials += 1
        #if ntrials % 10000 == 0: print ('ntrials,nback',ntrials,nback)
        
        # we're on a new open cell
        if state == NEW_CELL:
            guess,forced = nextValidGuess(board,cell,1)
            #print ("NEW_CELL,cell,guess,forced",cell,guess,forced)
            if not guess:
                # failed to find a valid guess for this cell, backtrack
                state = BACKTRACK
            else:
                board[cell] = guess
                if not forced:
                    mystack.push([cell,board[:]])
                    state = FIND_NEXT_CELL
            continue
        
        # find a new open cell
        if state == FIND_NEXT_CELL:
            cell = nextOpenCell(board,cell)
            if not cell:
                # Solution!
                break
            state = NEW_CELL
            continue
        
        # backtrack
        if state == BACKTRACK:
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
        
    print ('Solution!, with ntrials, backtracks: ', ntrials,nback)
    # print(board)
    printBoard(board)
    writeBoard(argv,name,board)

main()
