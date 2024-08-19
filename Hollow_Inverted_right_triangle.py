line=int(input("Enter a number: "))
for ln in range(line,0,-1):
    for st in range(ln):
        if ln==line or st==0 or st==ln-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()