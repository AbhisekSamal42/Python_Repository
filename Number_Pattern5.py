var=int(input("Enter a number: "))
for ev in range(var+1,1,-1):
    for val in range(1,ev):
        print(val,end='')
    print()

    #output is
    '''
    12345
    1234
    123
    12
    1
    '''