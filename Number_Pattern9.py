var=int(input("Enter a number: "))
for sv in range(1,var+1,1):
    for val in range(sv,var+1,1):
        print(val,end="")
    print()

    #output is 
    '''
    12345
    2345
    345
    45
    5
    '''