line = int(input("Enter a number: "))
space = 0

for row in range(line, 0, -1):
    for sp in range(space):
        print(" ", end=" ")
    space += 1
    for st in range(2 * row - 1):
        if row == line or st == 0 or st == 2 * row - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
