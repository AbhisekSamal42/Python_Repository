var=int(input("Enter a number: "))
for row in range(var+1):
    for col in range(row):
        print(row,end='')
    print()

    #output is
    '''
    1
    22
    333
    4444
    55555
    666666
    '''