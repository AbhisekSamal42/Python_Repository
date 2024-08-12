#Wap to print Pyramid pattern star program.
var=int(input("Enter a number: "))
star=1
space=var-1
for row in range(var):
    for sp in range(space):
        print(" ",end=" ")
    for st in range(star):
        print("*",end=" ")
    space=space-1
    star=star+2
    print()    