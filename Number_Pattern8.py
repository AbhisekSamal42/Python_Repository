var=int(input("Enter a number: "))
for st in range(var,0,-1):
    for val in range(st,var+1,1):
        print(val,end='')
    print()