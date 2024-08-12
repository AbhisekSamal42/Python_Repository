#Wap to print Inverted pyramid pattern star program.
var=5
space=0
star=9
for row in range(var):
    for sp in range(space):
        print(" ",end=" ")
    for st in range(star):
        print("*",end=" ")
    space=space+1
    star=star-2
    print()