line=int(input("Enter a number: "))
for ln in range(1,line+1):
    for st in range(ln):
        if st==0 or ln==line or st==ln-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()