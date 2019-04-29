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



class Cell:
    def __init__ (self, cell, neighbors, empty_neighbors, values):
        self.cell = cell
        self.neighbors = neighbors
        self.empty_neighbors = empty_neighbors
        self.current_neighbors = empty_neighbors
        self.values = values # possible values
        self.current_values = values

    def __str__ (self):
        s = str(self.cell) + "\t" + str(self.values) + "\n" + str(self.empty_neighbors) + "\n" + str(self.neighbors)
        return (s)

    def neighbors (self,neighbor):
        self.current_neighbors.discard(neighbor)


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

def makeNeighbors2():
    global r, c, s
    r = dict([[i,{member for clique in cliques_r for member in clique if i in clique and i != member}] for i in range(81)]) # n // 9
    c = dict([[i,{member for clique in cliques_c for member in clique if i in clique and i != member}] for i in range(81)]) # n % 9
    s = dict([[i,{member for clique in cliques_s for member in clique if i in clique and i != member}] for i in range(81)]) # (rs // 3) * 3 + (cs // 3)
    return r, c, s

# def nextOpenCell(board, start):
#     try: return board.index(0, start+1)
#     except ValueError: return None


def nextOpenCell(board):
    try:
        return min(p_guesses, key= lambda x: len(p_guesses[x]))
    except: return None


def nextValidGuess(board, cell,possible = None,prev_guess = {}):
    #neighbors_values = [board[neighbor] for neighbor in d[cell]]
    #possibilities = AllVals - {value for value in neighbors_values if value != 0}
    #while n not in possibilities and n <= 9:
        #n += 1
    if possible == None:
        possibilities = p_guesses.pop(cell)
        print(possibilities)
        if len(possibilities) > 1:
            return possibilities, len(possibilities) - 1 < 1
        return None, False
    else:
        print(possible)
        if len(possible) > 1:
            return possible - prev_guess, len(possible) - 1 < 1
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
    possible_places = set(range(81))
    places = possible_places & set([n for n,p in enumerate(board) if p != 0 ])
    #print(places)
    mystack = Stack()

    makeNeighbors()
    makeNeighbors2()

    global p_neighbors, p_guesses

    p_neighbors = dict([[i, d[i] & places] for i in places])
    p_guesses = dict([[i, AllVals - {value for value in [board[neighbor] for neighbor in d[i]] if value != 0}] for i in places])

    print(p_neighbors)
    print(p_guesses)

    print(min(p_guesses, key=lambda k: p_guesses[k]))

    empty_cells = dict([[i,Cell(i,d[i],d[i] & places,AllVals - {value for value in [board[neighbor] for neighbor in d[i]] if value != 0})] for i in places])

    # for i in empty_cells:
    #     print(i)
    #     print(empty_cells[i])
    #     print("")

    print("\nsums")

    print([sum([board[k] for k in i]) for i in cliques_r])
    print([[board[k] for k in i] for i in cliques_r])
    print([sum([board[k] for k in i]) for i in cliques_c])
    print([[board[k] for k in i] for i in cliques_c])
    print([sum([board[k] for k in i]) for i in cliques_s])
    print([[board[k] for k in i] for i in cliques_s])


    nback = 0
    ntrials = 0
    cell = nextOpenCell(board)#,-1)
    state = NEW_CELL
    print(cell)
    while True:
        #printBoard(board)
        #print("")
        ntrials += 1
        #if ntrials % 10000 == 0: print ('ntrials,nback',ntrials,nback)

        # we're on a new open cell
        if state == NEW_CELL:
            possible,forced = nextValidGuess(board,cell)
            if not possible or len(possible) == 0:
                # failed to find a valid guess for this cell, backtrack
                state = BACKTRACK
            else:
                guess = possible.pop()
                print ("NEW_CELL,cell,guess,forced",cell,guess,forced)
                for i in p_neighbors[cell]:
                    if i in p_guesses:
                        p_guesses[i].discard(guess)
                board[cell] = guess
                if not forced:
                    mystack.push([cell,board[:],possible])
                    state = FIND_NEXT_CELL
            continue

        # find a new open cell
        if state == FIND_NEXT_CELL:
            cell = nextOpenCell(board)#, cell)
            if not cell:
                # Solution!
                break
            state = NEW_CELL
            continue

        # backtrack
        if state == BACKTRACK:
            nback += 1
            cell,board,possible = mystack.pop()
            old_guess = board[cell]
            possible,forced = nextValidGuess(board,cell,possible,old_guess)  # note: state cannot be forced
            #print('BACKTRACK,cell,guess,forced',cell,guess,forced)
            if not possible or len(possible) == 0:
                state = BACKTRACK
            else:
                guess = possible.pop()
                for i in p_neighbors[cell]:
                    if i in p_guesses:
                        p_guesses[i].add(guess)
                board[cell] = guess
                mystack.push([cell,board[:]],possible)
                state = FIND_NEXT_CELL
            continue

    print ('\nSolution!, with ntrials, backtracks: ', ntrials,nback)
    # print(board)
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
time python3 sudoku-smart.py master-boards.txt smart_out.txt A1-1,Easy-NYTimes,unsolved
time python3 sudoku-smart.py master-boards.txt smart_out.txt A2-1,Medium-NYTimes,unsolved
time python3 sudoku-smart.py master-boards.txt smart_out.txt A3-1,Hard-NYTimes,unsolved
time python3 sudoku-smart.py master-boards.txt smart_out.txt A4-1,WebSudoku-Hard,unsolved
time python3 sudoku-smart.py master-boards.txt smart_out.txt A5-1,WebSudoku-Evil,unsolved
time python3 sudoku-smart.py master-boards.txt smart_out.txt A6-1,hardest-sudoku-telegraph,unsolved
time python3 sudoku-smart.py master-boards.txt smart_out.txt A7-1,sudokugarden_100sudoku2-Nr-100,unsolved
time python3 sudoku-smart.py master-boards.txt smart_out.txt A8-1,sudokugarden_100sudoku2-Nr-50,unsolved
'''
