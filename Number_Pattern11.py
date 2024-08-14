var=int(input("Enter a number: "))
space=0
for ev in range(var+1,1,-1):
    for sp in range(space):
        print(" ",end="")
    for val in range(1,ev,1):
        print(val,end="")
    print()
    space=space+1

    #output is
    '''
    12345
     1234
      123
       12
        1
    '''