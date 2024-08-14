var=int(input("Enter a number: "))
space=var-1
for sv in range(1,var+1,1):
    for sp in range(space):
        print(" ",end="")
    for val in range(sv,0,-1):
        print(val,end="")
    print()
    space=space-1

    #output is
    '''
    1
   21
  321
 4321
54321
'''