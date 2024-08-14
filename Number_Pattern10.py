var=int(input("Enter a number: "))
space=var-1
for ev in range(2,var+2,1):
    for sp in range(space):
        print(" ",end="")
    for val in range(1,ev,1):
        print(val,end="")
    print()
    space=space-1

    #output is
    '''
     1
    12
   123
  1234
 12345
    '''