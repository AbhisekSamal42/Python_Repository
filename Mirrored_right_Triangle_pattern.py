#Wap to print Mirrored Rightangle triangle pattern star program.
var=int(input("Enter a number: "))
space=var-1
star=1
for row in range(var):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star):
        print("*",end=' ')
    space=space-1
    star=star+1
    print()