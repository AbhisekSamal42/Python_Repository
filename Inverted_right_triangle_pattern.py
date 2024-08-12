#Wap to print inverted Rightangle triangle pattern star program.
var=int(input("Enter a number: "))
for row in range(var,0,-1):
    for col in range(row):
        print("*",end=' ')
    print()