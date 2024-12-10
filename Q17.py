var=int(input("Enter a number: "))
space=0
for ev in range(6,1,-1):
    for sp in range(space):
        print(' ',end=' ')
    for val in range(1,ev):
        print(val,end=' ')
    print()
    space=space+1