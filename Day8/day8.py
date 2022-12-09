import sys
from math import prod
import numpy as np
infile = sys.argv[1] if len(sys.argv) > 1 else 'day8.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day8test.txt'
values = open(infile).read().split()
vis = 0
edges = 0
inside = 0
grid = []
scenic = 0
for value in values:
    grid.append(value)
sides = (len(grid[0]) - 1) * 4
# print(sides)
# print(grid)



cols = []

for i in range(len(grid[0])):
    col = ""
    for j in range(len(grid)):
        col += grid[j][i]
    cols.append(col)
# print(cols)


# up - 2
# left - 2
# down - 1
# right - 2
for y in range(len(grid)):
    for x in range(len(grid[0])):
        # gets perimeter vis count
        if y == 0 or x == 0 or y == len(grid[0]) - 1 or x == len(grid) - 1:
            edges += 1
        # check left, right, down, up
        else:
            check = int(grid[x][y])
            left = reversed(grid[x][:y]) 
            right = grid[x][y+1:]
            up = reversed(cols[y][:x])
            down = cols[y][x+1:]
            
         
            view = []
            dirs = []
            scores = []
            score = 0
            blocked = False
            for u in up:
                if not blocked:
                    if check > int(u):
                        view.append(True)
                        score += 1
                    else:
                        score += 1
                        blocked = True
                        view.append(False)
            scores.append(score)
            if all(view):
                dirs.append(True)
            else:
                dirs.append(False)
            view = []
            score = 0
            blocked = False
            for d in down:
                if not blocked:
                    if check > int(d):
                        view.append(True)
                        score += 1
                    else:
                        score += 1
                        blocked = True
                        view.append(False)
            scores.append(score)
            if all(view):
                dirs.append(True)
            else:
                dirs.append(False)
            view = []
            score = 0
            blocked = False
            for l in left:
                if not blocked:
                    if check > int(l):
                        view.append(True)
                        score += 1
                    else:
                        score += 1
                        blocked = True
                        view.append(False)
            scores.append(score)
            if all(view):
                dirs.append(True)
            else:
                dirs.append(False)
            view = []
            score = 0
            blocked = False
            for r in right:
                if not blocked:
                    if check > int(r):
                        view.append(True)
                        score += 1
                    else:
                        blocked = True
                        score += 1
                        view.append(False)
            scores.append(score)
            if all(view):
                dirs.append(True)
            else:
                dirs.append(False)
            if any(dirs):
                inside += 1
            scenic = max(scenic, prod(scores))
            

print(edges + inside)
print(scenic)
# 863460

