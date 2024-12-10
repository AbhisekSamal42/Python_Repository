var=int(input("Enter a number: "))
space=var-1
for ev in range(2,7):
    for sp in range(space):
        print(' ',end=' ')
    for val in range(1,ev):
        print(val,end=' ')
    print()
    space=space-1