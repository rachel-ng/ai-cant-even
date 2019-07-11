import sys
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

AllVals = set([1,2,3,4,5,6,7,8,9])

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
BOARD_TO_SOLVE = sys.argv[3]

def main(argv=None):
    name,board = getBoard(BOARD_TO_SOLVE)

    possible_places = set(range(81))

    places = possible_places & set([n for n,p in enumerate(board) if p == 0 ])
    mystack = Stack()

    print(places)

    d = dict([[i,{member for clique in cliques for member in clique if i in clique and i != member}] for i in range(81)])

    p_neighbors = dict([[i, d[i] & places] for i in places])
    p_guesses = dict([[i, AllVals - {value for value in [board[neighbor] for neighbor in d[i]] if value != 0}] for i in places])
    set_guesses = {}

    for c in places:
        set_guesses[c] = list(p_guesses[c].difference(*[p_guesses[i] for i in p_neighbors[c]]))

    print(set_guesses)

    for i in set_guesses:
        if len(set_guesses[i]) == 1:
            board[i] = set_guesses[i][0]

    print(board)


if __name__ == "__main__":
     main()
