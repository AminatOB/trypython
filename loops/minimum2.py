smallest = None
for itervar in [3, 41, 12, 9, 74, 2]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        print('Smallest:', smallest)

