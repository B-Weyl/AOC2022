import sys
import numpy as np
from math import dist
infile = sys.argv[1] if len(sys.argv) > 1 else 'day9.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day9test.txt'
values = open(infile).readlines()
hx, hy = 0, 0
tx, ty = 0, 0
# H = (0,0)
# T = (0,0)
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
head_visited = set()
tail_visited = set()
distance = 0

for value in values:
    direction, amt = value.split(' ')
    move = 0
    while move < int(amt):
        h_prev = (hx, hy)
        if direction== 'R':
            hx += 1
            head_visited.add((hx, hy))
        if direction == 'L':
            hx -= 1
            head_visited.add((hx, hy))
        if direction == 'U':
            hy += 1
            head_visited.add((hx, hy))
        if direction == 'D':
            hy -= 1
            head_visited.add((hx, hy))
        if abs(hx - tx) > 1 or abs(hy - ty) > 1:
            tx = h_prev[0]
            ty = h_prev[1]
        
        tail_visited.add((tx, ty))
        move += 1



print(len(head_visited))
print(len(tail_visited))
print((hx, hy))
print((tx, ty))



        

