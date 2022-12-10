import sys
import pprint
import math
infile = sys.argv[1] if len(sys.argv) > 1 else 'day10.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day10test.txt'
ss = []
cycle = 0
x = 1
leds = 0
off = 0

CRT = [['.'] * 40 for x in range(6)]
start = 0
inc = 39
# print(CRT)



values = open(infile).readlines()
for value in values:
    if len(value.split(' ')) > 1:
        cmd, amt = value.split(' ')
        amt = eval(amt)
        for i in range(2):
            if cycle == 120 :
                print(cycle, x, sprite, math.floor(cycle / 40))
            sprite = [x - 1, x, x + 1]
            # print(cycle in sprite)
            # print(cycle, sprite)
            if cycle%40 in sprite:
                row = math.floor(cycle / 40)
                # print(row, cycle)
                CRT[row][(cycle%40)] = '#'
            else:
                row = math.floor(cycle / 40)
                # print(row, cycle)
                CRT[row][(cycle%40)] = '.'
            cycle += 1
            for j in [20, 60, 100, 140, 180, 220]:
                if cycle == j:
                    ss.append(cycle * x)
        x += amt
    else:
        cycle += 1
        sprite = [x - 1, x, x + 1]
        # print(x, sprite)
        # print(cycle in sprite)
        # print(cycle, sprite)
        if cycle%40 in sprite:
            row = math.floor(cycle / 40)
            CRT[row][(cycle%40)] = '#'
            # print(row, cycle)
        else:
            row = math.floor(cycle / 40)
            CRT[row][(cycle%40)] = '.'
            # print(row, cycle)
        
        for j in [20, 60, 100, 140, 180, 220]:
            if cycle == j:
                ss.append(cycle * x)
        if cycle == 239:
            break
for z in range(6):
    print(z)
    print(CRT[z][0:40])

    
# print(leds, off)
print(sum(ss))

