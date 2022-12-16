import sys
from math import prod
infile = sys.argv[1] if len(sys.argv) > 1 else 'day11.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day11test.txt'
rounds = 20

                
WORRYS = []
OPS = []
TESTS = []
TRUES = []
FALSES = []





monkeys = open(infile).read().split('\n\n')
for monkey in monkeys:
    info = monkey.split('\n')
    _, values = info[1].split(':')
    items = values.split(',')
    items = [int(item.strip()) for item in items]
    WORRYS.append(items)
    opp = info[2].split(':')[1]
    op = opp.split('=')[1]
    OPS.append(op)
    test = info[3].split(':')[1].split(' ')[-1]
    TESTS.append(int(test))
    outcomeTrue = int(info[4][-1])
    TRUES.append(outcomeTrue)
    outcomeFalse = int(info[5][-1])
    FALSES.append(outcomeFalse)
M = prod(TESTS)
print(M)
# print(WORRYS[1])
inspections = [0 for i in range(len(WORRYS))]
# print(WORRYS, OPS, TESTS, TRUES, FALSES)

def runRound(worrys):
    for i in range(8):
        R = []
        for j in range(len(worrys[i])):
            # print(i, j)
            old = worrys[i][j]
            new_ = eval(OPS[i])
            # new_ = new_ // 3
            # print(old, new_)
            # if true - pass to certain monkey
            if new_ % int(TESTS[i]) == 0:
                worrys[TRUES[i]].append(new_ % M)
                # worrys[i].remove(old)
                # print(worrys)
            # if false - pass to different monkey
            else:
                worrys[FALSES[i]].append(new_ % M)
                # print(worrys)
            R.append(old)
        # worrys[i].remove(old)
        inspections[i] += len(R)
        for r in R:
            worrys[i].remove(r)


for z in range(10000):
    runRound(WORRYS)
# print(WORRYS)
# print(inspections)
print(prod(sorted(inspections)[-2:]))


    

    

    





