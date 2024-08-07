def is_Armstrong(num,dup,ndig,sol=0):
    #dup=num
    #ndig=len(str(num))
    while num!=0:
        rem=num%10
        sol=sol+(rem)**ndig
        num=num//10
    return dup==sol
num=int(input("Enter a number:"))
if is_Armstrong(num,num,len(str(num))):
    print("Armstrong number")
else:
    print("Not armstrong number")