import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'day6.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day6test.txt'
values = open(infile).read()
packet = 4
message = 14

lines = [x.strip() for x in values.split('\n)')]
for z in [packet, message]:
    for x in range(len(values) - z):
        if len(set(values[x:x+z])) == z:
            print(values[x:x+z])
            print(x + z)
            break
        else:
            continue
