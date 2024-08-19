line=int(input("Enter a number: "))
space=line-1
for ln in range(1,line+1):
    for sp in range(space):
        print(" ",end=" ")
    for st in range(ln):
        if st==0 or line==ln or st==ln-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    space=space-1