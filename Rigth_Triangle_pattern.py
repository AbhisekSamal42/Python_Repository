#Wap to print Rightangle triangle pattern star program.
var=int(input("Enter a number: "))
for row in range(1,var+1):
    for col in range(row):
        print("*",end=' ')
    print()