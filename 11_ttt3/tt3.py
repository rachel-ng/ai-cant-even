#! /usr/bin/python3

import random
import sys
from functools import reduce


''' Layout positions:
0 1 2
3 4 5
6 7 8
'''

# layouts look like "_x_ox__o_"

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode

xw = []
ow = []
dw = []
no_end = 0
ne = []

class BoardNode:
    def __init__ (self,layout):
        self.layout = layout
        self.endState = self.win() # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.parents = [] # all layouts that can lead to this one, by one move
        self.children = [] # all layouts that can be reached with a single move
        
        self.best_move = -1 # cell position (0-8) of the best move from this layout, or -1 if this is a final layout
        self.best_move_ind = -1
        self.moves_to_end = -1 # how many moves until the end of the game, if played perfectly.  0 if this is a final layout
        self.final_state  = self.fin_state() # expected final state ('x' if 'x' wins, 'o' if 'o' wins, else 'd' for a draw)
        
    def win (self):
        all_poss = [[self.layout[k] for k in i if self.layout[k] != '_'] for i in Wins]
        for i in all_poss: 
            if i == ['x'] * 3:
                self.endState = i[0]
                return 'x'
            elif i == ['o'] * 3:
                self.endState = i[0]
                return 'o'
        if '_' not in self.layout:
            self.endState = 'd'
            return 'd'
        else:
            return None
            
    def fin_state (self):
        if self.endState != None:
            return self.endState
        else: 
            return
        
def CreateAllBoards(layout,parent = None):
    move = 'x'
    nums_x = 0
    nums_o = 0
    for i in layout:
        if i == 'x':
            nums_x += 1
        elif i == 'o':
            nums_o += 1
    if nums_x > nums_o:
        move = 'o'
    b = BoardNode(layout)
    
    if layout not in AllBoards:
        AllBoards[layout] = b
        
    if parent:
        b.parents.append(parent)
        parent.children.append(b)
        
    if b.endState:
        if b.endState == 'x': xw.append(b)
        if b.endState == 'o': ow.append(b)
        if b.endState == 'd': dw.append(b)
        return
    if b.endState == None: ne.append(b)
    for i in range(len(layout)):
        if layout[i] == '_':
            CreateAllBoards(layout[:i] + move + layout[i+1:],b)

CreateAllBoards('_________')



def position (num):
    rows = ["top", "middle", "bottom"]
    cols = ["right", "middle", "left"]
    return rows[num // 3] + " " + cols[num % 3]



fins = [i for i in AllBoards.values() if i.endState != None]
p1 = []

#print([i.layout for i in fins])

for i in fins: 
    i.moves_to_end += 1
    p1 += i.parents[:]
    
#print([(i.layout, i.moves_to_end,[(k.layout, k.moves_to_end) for k in i.parents]) for i in fins])

p2 = []
for i in p1: 
    kids = [[k,k.moves_to_end] for k in i.children if k.moves_to_end > -1]
    m = min([j[1] for j in kids])
    i.best_move = [k for k in kids if k[1] == m][0][0]
    i.best_move_ind = [k for k,n in enumerate([j for j in i.layout]) if n != [j for j in i.best_move.layout][k]][0]
    i.moves_to_end = i.best_move.moves_to_end + 1
    p2 += i.parents[:]

p3 = []
for i in p2: 
    kids = [[k,k.moves_to_end] for k in i.children if k.moves_to_end > -1]
    m = min([j[1] for j in kids])
    i.best_move = [k for k in kids if k[1] == m][0][0]
    i.best_move_ind = [k for k,n in enumerate([j for j in i.layout]) if n != [j for j in i.best_move.layout][k]][0]
    i.moves_to_end = i.best_move.moves_to_end + 1
    p3 += i.parents[:]

p4 = []
for i in p3: 
    kids = [[k,k.moves_to_end] for k in i.children if k.moves_to_end > -1]
    m = min([j[1] for j in kids])
    i.best_move = [k for k in kids if k[1] == m][0][0]
    i.best_move_ind = [k for k,n in enumerate([j for j in i.layout]) if n != [j for j in i.best_move.layout][k]][0]
    i.moves_to_end = i.best_move.moves_to_end + 1
    p4 += i.parents[:]

p5 = []
for i in p4: 
    kids = [[k,k.moves_to_end] for k in i.children if k.moves_to_end > -1]
    m = min([j[1] for j in kids])
    i.best_move = [k for k in kids if k[1] == m][0][0]
    i.best_move_ind = [k for k,n in enumerate([j for j in i.layout]) if n != [j for j in i.best_move.layout][k]][0]
    i.moves_to_end = i.best_move.moves_to_end + 1
    p5 += i.parents[:]

p6 = []
for i in p5: 
    kids = [[k,k.moves_to_end] for k in i.children if k.moves_to_end > -1]
    m = min([j[1] for j in kids])
    i.best_move = [k for k in kids if k[1] == m][0][0]
    i.best_move_ind = [k for k,n in enumerate([j for j in i.layout]) if n != [j for j in i.best_move.layout][k]][0]
    i.moves_to_end = i.best_move.moves_to_end + 1
    p6 += i.parents[:]

p7 = []
for i in p6: 
    kids = [[k,k.moves_to_end] for k in i.children if k.moves_to_end > -1]
    m = min([j[1] for j in kids])
    i.best_move = [k for k in kids if k[1] == m][0][0]
    i.best_move_ind = [k for k,n in enumerate([j for j in i.layout]) if n != [j for j in i.best_move.layout][k]][0]
    i.moves_to_end = i.best_move.moves_to_end + 1
    p7 += i.parents[:]

p8 = []
for i in p7: 
    kids = [[k,k.moves_to_end] for k in i.children if k.moves_to_end > -1]
    m = min([j[1] for j in kids])
    i.best_move = [k for k in kids if k[1] == m][0][0]
    i.best_move_ind = [k for k,n in enumerate([j for j in i.layout]) if n != [j for j in i.best_move.layout][k]][0]
    i.moves_to_end = i.best_move.moves_to_end + 1
    p8 += i.parents[:]

p9 = []
for i in p8: 
    kids = [[k,k.moves_to_end] for k in i.children if k.moves_to_end > -1]
    m = min([j[1] for j in kids])
    i.best_move = [k for k in kids if k[1] == m][0][0]
    i.best_move_ind = [k for k,n in enumerate([j for j in i.layout]) if n != [j for j in i.best_move.layout][k]][0]
    i.moves_to_end = i.best_move.moves_to_end + 1
    p9 += i.parents[:]

p9 = []
for i in p8: 
    kids = [[k,k.moves_to_end] for k in i.children if k.moves_to_end > -1]
    m = min([j[1] for j in kids])
    i.best_move = [k for k in kids if k[1] == m][0][0]
    i.best_move_ind = [k for k,n in enumerate([j for j in i.layout]) if n != [j for j in i.best_move.layout][k]][0]
    i.moves_to_end = i.best_move.moves_to_end + 1
    p9 += i.parents[:]

#print([(i.layout, i.moves_to_end,[(k.layout, k.moves_to_end) for k in i.parents]) for i in p8])
#print([(i.layout, i.moves_to_end, i.best_move.layout, i.best_move_ind,position(i.best_move_ind)) for i in p9])

print(set([position(i.best_move_ind) for i in p9]))

#if __name__ == '__main__':
#    CreateAllBoards(sys.argv[1])
#    board_node = AllBoards[sys.argv[1]]
#    print(string_board(sys.argv[1]))
#    process(sys.argv[1])
#    print([(AllBoards[child].final_state, AllBoards[child].layout) for child in AllBoards[sys.argv[1]].children])
