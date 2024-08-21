line=int(input("Enter a number: "))
for row in range(line):
    for col in range(line):
        if row==col or row+col==line-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()