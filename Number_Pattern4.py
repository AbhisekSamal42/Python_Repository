var=int(input("Enter a number: "))
for ev in range(2,var+2):
    for val in range(1,ev):
        print(val,end='')
    print()

    #output is
    '''
    1
    12
    123
    1234
    12345
    '''