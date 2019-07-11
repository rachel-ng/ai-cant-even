#! /usr/bin/python3

# Raymond Wu
# Rachel Ng

import sys
import time


# start = time.time()
# print(time.time() - start)


'''
things that don't work (well):

def nextOpenCell(board):
    try:
        cell = (places - set([n for n,p in enumerate(board) if p != 0])).pop()
        return cell
    except KeyError: return None

notes: made them all slower, some (S O M E) had fewer backtracks, other didn't


- look at neighbors
  - if one of it's neighbors' possible values are the same, then that's the next one you should try
  - if there's only 2 possible values then it has to be one or the other - these possible values can also be eliminated from other neighbors, but that'd be tested when you proceed to the next open cell (?)

- would be faster if you could check the ones with the fewest possible values first
  - lmao use a priority queue and reorder them by doing the ones with fewest possible values first wait no that'd change every time and you'd have to calculate all of them



'''

sols = {'A1-1,Easy-NYTimes,unsolved': [0, 0, 4, 1, 0, 0, 5, 2, 7, 2, 1, 3, 7, 0, 0, 0, 0, 0, 0, 0, 7, 6, 2, 4, 0, 0, 0, 3, 5, 0, 2, 7, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 8, 7, 5, 0, 4, 0, 0, 0, 6, 0, 1, 3, 4, 7, 2, 0, 1, 0, 0, 5, 0, 0, 3, 1, 0, 6, 2, 0, 0, 9, 9, 0, 0, 0, 0, 0, 1, 8, 0], 'A1-2,Easy-NYTimes,solved': [6, 9, 4, 1, 8, 3, 5, 2, 7, 2, 1, 3, 7, 9, 5, 4, 6, 8, 5, 8, 7, 6, 2, 4, 9, 3, 1, 3, 5, 8, 2, 7, 1, 6, 9, 4, 1, 2, 6, 4, 3, 9, 8, 7, 5, 7, 4, 9, 8, 5, 6, 2, 1, 3, 4, 7, 2, 9, 1, 8, 3, 5, 6, 8, 3, 1, 5, 6, 2, 7, 4, 9, 9, 6, 5, 3, 4, 7, 1, 8, 2], 'A2-1,Medium-NYTimes,unsolved': [2, 0, 0, 6, 0, 0, 0, 0, 0, 6, 0, 0, 0, 5, 1, 0, 4, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 4, 0, 0, 5, 0, 6, 0, 0, 0, 0, 0, 1, 9, 0, 4, 0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 0, 2, 5, 0, 0, 0, 9, 0, 0, 0, 8, 0, 8, 9, 0, 0, 0, 0, 4, 0, 0], 'A2-2,Medium-NYTimes,solved': [2, 5, 4, 6, 9, 7, 8, 3, 1, 6, 8, 3, 2, 5, 1, 7, 4, 9, 9, 7, 1, 4, 8, 3, 5, 6, 2, 7, 6, 8, 5, 3, 9, 2, 1, 4, 4, 2, 5, 1, 6, 8, 3, 9, 7, 3, 1, 9, 7, 4, 2, 6, 5, 8, 1, 3, 6, 8, 7, 4, 9, 2, 5, 5, 4, 7, 9, 2, 6, 1, 8, 3, 8, 9, 2, 3, 1, 5, 4, 7, 6], 'A3-1,Hard-NYTimes,unsolved': [0, 0, 6, 0, 9, 0, 0, 0, 0, 1, 7, 0, 0, 0, 3, 0, 9, 0, 0, 0, 0, 7, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 6, 0, 0, 0, 9, 0, 0, 3, 0, 2, 0, 0, 0, 0, 4, 0, 0, 2, 1, 0, 0, 0, 0, 0, 9, 7, 8, 0, 0, 0, 0, 4, 0, 0, 0, 5, 0, 8, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0], 'A3-2,Hard-NYTimes,solved': [3, 5, 6, 2, 9, 4, 8, 7, 1, 1, 7, 8, 6, 5, 3, 4, 9, 2, 4, 2, 9, 7, 8, 1, 3, 6, 5, 8, 1, 2, 5, 4, 9, 6, 3, 7, 6, 9, 5, 1, 3, 7, 2, 4, 8, 7, 3, 4, 8, 6, 2, 1, 5, 9, 2, 6, 3, 9, 7, 8, 5, 1, 4, 9, 4, 1, 3, 2, 5, 7, 8, 6, 5, 8, 7, 4, 1, 6, 9, 2, 3], 'A4-1,WebSudoku-Hard,unsolved': [0, 6, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 6, 0, 0, 1, 5, 7, 0, 0, 0, 5, 0, 0, 8, 0, 0, 7, 0, 0, 0, 0, 5, 9, 3, 0, 0, 2, 0, 0, 7, 0, 0, 1, 0, 0, 9, 6, 1, 0, 0, 0, 0, 4, 0, 0, 2, 0, 0, 6, 0, 0, 0, 9, 5, 8, 0, 0, 4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 7, 0], 'A4-2,WebSudoku-Hard,solved': [8, 6, 5, 2, 1, 7, 4, 9, 3, 2, 3, 9, 6, 4, 8, 1, 5, 7, 4, 1, 7, 5, 9, 3, 8, 2, 6, 7, 8, 1, 4, 6, 5, 9, 3, 2, 3, 2, 4, 8, 7, 9, 6, 1, 5, 5, 9, 6, 1, 3, 2, 7, 8, 4, 1, 7, 2, 3, 8, 6, 5, 4, 9, 9, 5, 8, 7, 2, 4, 3, 6, 1, 6, 4, 3, 9, 5, 1, 2, 7, 8], 'A5-1,WebSudoku-Evil,unsolved': [0, 0, 0, 1, 0, 0, 0, 9, 3, 1, 0, 4, 0, 6, 0, 0, 0, 0, 5, 3, 0, 0, 7, 0, 0, 0, 0, 2, 7, 0, 0, 0, 6, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 9, 0, 0, 0, 4, 7, 0, 0, 0, 0, 3, 0, 0, 6, 2, 0, 0, 0, 0, 4, 0, 8, 0, 9, 7, 6, 0, 0, 0, 1, 0, 0, 0], 'A5-2,WebSudoku-Evil,solved': [6, 8, 7, 1, 2, 4, 5, 9, 3, 1, 9, 4, 5, 6, 3, 7, 2, 8, 5, 3, 2, 8, 7, 9, 6, 1, 4, 2, 7, 3, 4, 5, 6, 9, 8, 1, 4, 1, 9, 3, 8, 7, 2, 5, 6, 8, 5, 6, 9, 1, 2, 3, 4, 7, 9, 4, 5, 7, 3, 8, 1, 6, 2, 3, 2, 1, 6, 4, 5, 8, 7, 9, 7, 6, 8, 2, 9, 1, 4, 3, 5], 'A6-1,hardest-sudoku-telegraph,unsolved': [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 6, 0, 0, 0, 0, 0, 0, 7, 0, 0, 9, 0, 2, 0, 0, 0, 5, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 4, 5, 7, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 6, 8, 0, 0, 8, 5, 0, 0, 0, 1, 0, 0, 9, 0, 0, 0, 0, 4, 0, 0], 'A6-2,hardest-sudoku-telegraph,solved': [8, 1, 2, 7, 5, 3, 6, 4, 9, 9, 4, 3, 6, 8, 2, 1, 7, 5, 6, 7, 5, 4, 9, 1, 2, 8, 3, 1, 5, 4, 2, 3, 7, 8, 9, 6, 3, 6, 9, 8, 4, 5, 7, 2, 1, 2, 8, 7, 1, 6, 9, 5, 3, 4, 5, 2, 1, 9, 7, 4, 3, 6, 8, 4, 3, 8, 5, 2, 6, 9, 1, 7, 7, 9, 6, 3, 1, 8, 4, 5, 2], 'A7-1,sudokugarden.de/files/100sudoku2-en.pdf-Nr-100,unsolved': [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 5, 0, 0, 1, 0, 6, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 4, 0, 0, 0, 0, 6, 0, 0, 0, 0, 9, 0, 3, 0, 0, 2, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 4, 0, 6, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], 'A7-2,sudokugarden.de/files/100sudoku2-en.pdf-Nr-100,solved': [8, 5, 9, 2, 4, 7, 1, 3, 6, 2, 4, 3, 6, 9, 1, 5, 7, 8, 1, 7, 6, 5, 3, 8, 9, 4, 2, 7, 3, 5, 4, 1, 2, 6, 8, 9, 4, 1, 2, 9, 8, 6, 7, 5, 3, 6, 9, 8, 3, 7, 5, 2, 1, 4, 3, 6, 7, 8, 5, 9, 4, 2, 1, 9, 8, 1, 7, 2, 4, 3, 6, 5, 5, 2, 4, 1, 6, 3, 8, 9, 7], 'A8-1,sudokugarden.de/files/100sudoku2-en.pdf-Nr-50,unsolved': [0, 0, 0, 0, 3, 0, 9, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 6, 8, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 6, 0, 8, 0, 0, 0, 0, 1, 6, 0, 0, 0, 0, 0, 0, 4, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 3, 0], 'A8-2,sudokugarden.de/files/100sudoku2-en.pdf-Nr-50,solved': [6, 2, 7, 8, 3, 1, 9, 5, 4, 1, 5, 3, 2, 9, 4, 8, 7, 6, 8, 9, 4, 7, 6, 5, 3, 1, 2, 2, 4, 8, 9, 5, 7, 1, 6, 3, 7, 6, 5, 1, 4, 3, 2, 8, 9, 9, 3, 1, 6, 2, 8, 7, 4, 5, 3, 1, 6, 5, 8, 2, 4, 9, 7, 4, 7, 9, 3, 1, 6, 5, 2, 8, 5, 8, 2, 4, 7, 9, 6, 3, 1]}



class Stack: # FILO
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
         [60,61,62,69,70,71,78,79,80]]

cliques_r = [[0,1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16,17],[18,19,20,21,22,23,24,25,26],[27,28,29,30,31,32,33,34,35],[36,37,38,39,40,41,42,43,44],[45,46,47,48,49,50,51,52,53],[54,55,56,57,58,59,60,61,62],[63,64,65,66,67,68,69,70,71],[72,73,74,75,76,77,78,79,80]]

cliques_c = [[0,9,18,27,36,45,54,63,72],[1,10,19,28,37,46,55,64,73],[2,11,20,29,38,47,56,65,74],[3,12,21,30,39,48,57,66,75],[4,13,22,31,40,49,58,67,76],[5,14,23,32,41,50,59,68,77],[6,15,24,33,42,51,60,69,78],[7,16,25,34,43,52,61,70,79],[8,17,26,35,44,53,62,71,80]]

cliques_s = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]



def getBoard(argv):
    input_file = open(INPUT_FILE,'r+').read().strip().split('\n')
    board = []
    trip = False
    i = 0
    for line in input_file:
        if trip and i < 9:
            board += [int(i) if i != '_' else 0 for i in line.split(',')]
            i += 1
        elif i >= 9:
            break
        if line == argv:
            trip = True
    return argv, board

def makeNeighbors():
    global d
    d = dict([[i,{member for clique in cliques for member in clique if i in clique and i != member}] for i in range(81)])
    return d

def nextOpenCell(board):
      try: return (places - set([n for n,p in enumerate(board) if p != 0])).pop()
      except KeyError: return None

def nextValidGuess(board, cell, n):
    neighbors_values = [board[neighbor] for neighbor in d[cell]]
    possibilities = AllVals - {value for value in neighbors_values if value != 0}
    while n not in possibilities and n <= 9:
        n += 1
    if n in AllVals:
        return n, len(possibilities) < 1
    return None, False

def checkForced(board):
    all_empty = [n for n,p in enumerate(board) if p == 0]
    for i in all_empty:
        belongs = [k for k in cliques if i in k]
        vals = [sum([1 for k in i if board[k] != 0]) for i in belongs]
        if 8 in vals:
            for j in belongs:
                if sum([1 for x in j if board[x] != 0]) == 8:
                    board[i] = list(AllVals - set([board[x] for x in j]))[0]

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

def writeBoard(argv, name, board, ntrials, nback, time):
    #file_name = name[:4] + '_t-' + str(ntrials) + '_b-' + str(nback) + '_t-' + str(time) + 's.txt'
    with open(OUTPUT_FILE, 'a+') as output_file:
        s = name + "\nntrials: " + str(ntrials) + "\nnback: " + str(nback) + "\ntime: " # trials and backtracks
        if time // 60 > 0: s += str(int(time // 60)) + "m " + str(time % 60) + "s\n" # time
        else: s +=  str(time % 60) + "s\n"
        for n,p in enumerate(board):
            if n % 9 == 8: s += str(p) + "\n"
            else: s += str(p) + ","
        output_file.write(s + "\n\n")
    output_file.close()



# States
NEW_CELL = 0
FIND_NEXT_CELL = 1
BACKTRACK = 2
AllVals = set([1,2,3,4,5,6,7,8,9])

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
BOARD_TO_SOLVE = sys.argv[3]
#BOARD_TO_SOLVE = sys.argv[2]



def main(argv=None):
    start = time.time()
    if not argv:
        argv = sys.argv

    name,board = getBoard(BOARD_TO_SOLVE)
    #print(board)

    global places

    possible_places = set(range(81))
    places = possible_places & set([n for n,p in enumerate(board) if p == 0 ])
    mystack = Stack()

    makeNeighbors()

    p_neighbors = dict([[i, d[i] & places] for i in places])
    p_guesses = dict([[i, AllVals - {value for value in [board[neighbor] for neighbor in d[i]] if value != 0}] for i in places])

    #print(p_neighbors)
    #print(p_guesses)
    #print(p_guesses[2].difference(*[p_guesses[i] for i in p_neighbors[2]]))

    set_guesses = {}
    for c in places:
        set_guesses[c] = list(p_guesses[c].difference(*[p_guesses[i] for i in p_neighbors[c]]))

    #print(set_guesses)

    for i in list(places):
        if len(set_guesses[i]) == 1:
            board[i] = list(set_guesses[i])[0]

    nback = 0
    ntrials = 0
    cell = nextOpenCell(board)
    state = NEW_CELL
    while True:
        #printBoard(board)
        #print("")
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
                checkForced(board)
                state = FIND_NEXT_CELL
            continue

        # find a new open cell
        if state == FIND_NEXT_CELL:
            cell = nextOpenCell(board)
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

    print ('\nSolution!, with ntrials, backtracks: ', ntrials,nback)
    # print(board)

    #for c in places:
        #print(board[c], set_guesses[c])

    print(board == sols[BOARD_TO_SOLVE[:3]+"2"+BOARD_TO_SOLVE[4:-8]+"solved"])

    printBoard(board)
    writeBoard(argv,name,board,ntrials,nback, time.time() - start)

main()



'''
time python3 sudoku-smart.py master-boards.txt A1-1,Easy-NYTimes,unsolved
time python3 sudoku-smart.py master-boards.txt A2-1,Medium-NYTimes,unsolved
time python3 sudoku-smart.py master-boards.txt A3-1,Hard-NYTimes,unsolved
time python3 sudoku-smart.py master-boards.txt A4-1,WebSudoku-Hard,unsolved
time python3 sudoku-smart.py master-boards.txt A5-1,WebSudoku-Evil,unsolved
time python3 sudoku-smart.py master-boards.txt A6-1,hardest-sudoku-telegraph,unsolved
time python3 sudoku-smart.py master-boards.txt A7-1,sudokugarden_100sudoku2-Nr-100,unsolved
time python3 sudoku-smart.py master-boards.txt A8-1,sudokugarden_100sudoku2-Nr-50,unsolved
'''

'''
time python3 we.py master-boards.txt mix_out.txt A1-1,Easy-NYTimes,unsolved
time python3 we.py master-boards.txt mix_out.txt A2-1,Medium-NYTimes,unsolved
time python3 we.py master-boards.txt mix_out.txt A3-1,Hard-NYTimes,unsolved
time python3 we.py master-boards.txt mix_out.txt A4-1,WebSudoku-Hard,unsolved
time python3 we.py master-boards.txt mix_out.txt A5-1,WebSudoku-Evil,unsolved
time python3 we.py master-boards.txt mix_out.txt A6-1,hardest-sudoku-telegraph,unsolved
time python3 we.py master-boards.txt mix_out.txt A7-1,sudokugarden_100sudoku2-Nr-100,unsolved
time python3 we.py master-boards.txt mix_out.txt A8-1,sudokugarden_100sudoku2-Nr-50,unsolved
'''
