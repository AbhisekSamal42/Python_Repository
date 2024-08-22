line = int(input("Enter a number: "))
space = line - 1

for row in range(line):
    for sp in range(space):
        print(' ', end=' ')
    for st in range(2 * row + 1):
        if st == 0 or st == 2 * row or row == line - 1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
    space=space-1
