var=int(input("Enter a number: "))
space=var-1
for st in range(1,6):
    for sp in range(space):
        print(' ',end=' ')
    for val in range(st,0,-1):
        print(val,end=' ')
    print()
    space=space-1