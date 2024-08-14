var=int(input("Enter a number: "))
for row in range(var+1):
    for col in range(row):
        print("1",end='')
    print()

    #output is
    '''
    1
    11
    111
    1111
    11111
    '''