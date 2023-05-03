fhand = open('hey.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@gmail') == -1:
        continue
    print(line)

