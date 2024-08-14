var=int(input("Enter a number: "))
space=var-1
for ev in range(var-1,-1,-1):
    for sp in range(space):
        print(" ",end="")
    for val in range(var,ev,-1):
        print(val,end="")
    print()
    space=space-1
    
    #output is
    '''
    5
   54
  543
 5432
54321
    '''