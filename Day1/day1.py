values = open('day1.txt').readlines()
# print(values)

amts = []
total = 0
for v in values:
    # print(v)
    if v != '\n':
        total += int(v)
    else:
        amts.append(total)
        total = 0
amts.append(total)
# part 1 - return the max of all the calories the differet elves were carrying
print(max(amts))
# part 2 - return the sum of the highest calorie carrying elves
print(sum(sorted(amts, reverse=True)[0:3]))

    
    
