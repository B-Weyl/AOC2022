values = open('day4.txt').readlines()
total1 = 0
total2 = 0
for value in values:
    p1, p2 = value.split(',')
    l1, l2 = p1.split('-')
    r1, r2, = p2.split('-')
    # e1 = [x for x in range(int(p1[0]), int(p1[2]))]
    # e2 = [x for x in range(int(p2[0]), int(p2[2]))]
    e1 = set(range(int(l1), int(l2) + 1))
    e2 = set(range(int(r1), int(r2) + 1))
    # part 1
    if len(e1.union(e2)) == len(e1) or len(e1.union(e2)) == len(e2):
        total1 += 1
    # part 2 
    if len(e1) + len(e2) > len(e1.union(e2)):
        total2 += 1

print(total1)
print(total2)