import string
values = open('day3.txt').readlines()
p1 =0
p2 = 0
common = []
common_group = []

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
low_score = [x for x in range(1, 27)]
up_score = [x for x in range(27, 53)]
ld = dict(zip(lower, low_score))
ud = dict(zip(upper, up_score))


# part 1 - finding the sum of all common compartment letters
for value in values:
    half = len(value) // 2
    x, y = value[:half], value[half:]
    for xx in x:
        if xx in y:
            common.append(xx)
            break


for c in common:
    if ord(c) < 97:
        p1 += ud[c]
    else:
        p1 += ld[c]
print(p1)

# part 2 - make groups of three and take the common "badge" scores
groups = []
start = 0
end = len(values)
step = 3

for x in range(start, end, step):
    y = x
    groups.append(values[y:y+step])

for group in groups:
    a, b, c = group[0], group[1], group[2]
    for aa in a:
        if aa in b and aa in c:
            common_group.append(aa)
            break

for com in common_group:
    if ord(com) < 97:
        p2 += ud[com]
    else:
        p2 += ld[com]
print(p2)


