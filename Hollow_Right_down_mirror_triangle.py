line=int(input("Enter a number: "))
space=0
for ln in range(line,0,-1):
    for sp in range(space):
        print(" ",end=" ")
    for st in range(ln):
        if ln==line or st==0 or st==ln-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    space=space+1