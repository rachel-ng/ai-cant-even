''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# layouts look like "_x_ox__o_"

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode
numchild = 0
xwin = 0
owin = 0
draws = 0
noend = 0

class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.parents = [] # all layouts that can lead to this one, by one move
        self.children = [] # all layouts that can be reached with a single move

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('parents:',self.parents)
        print ('children:',self.children)

def CreateAllBoards(layout,parent = None):
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary
    move = 'x'
    numx = 0
    numo = 0
    for i in layout:
        if i == 'x':
            numx += 1
        elif i == 'o':
            numo += 1
    if numx > numo:
        move = 'o'
    b = BoardNode(layout)
    if layout not in AllBoards:
        AllBoards[layout] = b
    if parent:
        b.parents.append(parent)
        parent.children.append(layout)
    b.endState = check_win(layout)
    if check_win(layout):
        return
    for i in range(len(layout)):
        if layout[i] == '_':
            CreateAllBoards(layout[:i] + move + layout[i+1:],b)

def check_win(l):
    for i in Wins:
        x = [x for x in i if l[x] == 'x']
        o = [o for o in i if l[o] == 'o']
        if (len(x) == 3):
            return 'x'
        elif (len(o) == 3):
            return 'o'
    d = [d for d in l if (d == 'x' or d == 'o')]
    if (len(d) == 9):
        return 'draw'
    else:
        return None

CreateAllBoards('_________')

for i in AllBoards.values():
    for j in i.children:
        numchild += 1
    if i.endState == 'x':
        xwin += 1
    if i.endState == 'o':
        owin += 1
    if i.endState == 'draw':
        draws += 1
    if not i.endState:
        noend += 1

print(len(AllBoards))
print(xwin)
print(owin)
print(draws)
print(noend)
print(numchild)
