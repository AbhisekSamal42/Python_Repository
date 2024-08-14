var=int(input("Enter a number: "))
for ev in range(0,var):
    for val in range(var,ev,-1):
        print(val,end='')
    print()

    #output is

    '''
    54321
    5432
    543
    54
    5
    '''