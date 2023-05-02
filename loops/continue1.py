while True:
    line = input('Input anything')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print('Done!')

