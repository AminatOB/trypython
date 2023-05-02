largest = None
for itervar in [3, 74, 12, 9, 41, 15]:
    if largest is None or itervar > largest:
        largest = itervar
        print('Largest:', largest)

