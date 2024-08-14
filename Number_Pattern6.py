var=int(input("Enter a number: "))
for ev in range(var-1,-1,-1):
    for val in range(var,ev,-1):
        print(val,end='')
    print()

    #output is
    '''
    5
    54
    543
    5432
    54321
    '''