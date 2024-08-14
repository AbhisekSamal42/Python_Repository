var=int(input("Enter a number: "))
num=var
for row in range(1,var+1):
    for col in range(row):
        print(num,end='')
    print()
    num=num-1

    #output is 
    '''
    5
    44
    333
    2222
    11111
    '''