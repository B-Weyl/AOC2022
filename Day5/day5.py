from copy import deepcopy
num_cols = 9
values = open('day5.txt').read().split('\n\n')
c = values[0].split("\n")
commands = values[1].split('\n')
cols = [[] for x in range(num_cols)]

for y in range(num_cols - 1):
    row = c[y]
    crates = row[1::4] 
    for z in range(len(crates)):
        if crates[z] != ' ':
            cols[z].append(crates[z])


cols = [col[::-1] for col in cols]
cols1 = deepcopy(cols)
cols2 = deepcopy(cols)

for command in commands:
    com = command.split()
    amt, source, dest = map(int, [com[1], com[3], com[5]])
    source -= 1
    dest -= 1

    for a in range(amt):
        moving = cols1[source].pop()
        cols1[dest].append(moving)
    cols2[dest].extend(cols2[source][-amt:])
    cols2[source] = cols2[source][:-amt]
    
print(''.join(co1[-1] for co1 in cols1))
print(''.join(co2[-1] for co2 in cols2))









