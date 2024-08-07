def is_Disarium(num,dup,ndig,sol=0):
    #dup=num
    #ndig=len(str(num))
    while num!=0:
        rem=num%10
        sol=sol+(rem)**ndig
        ndig=ndig-1
        num=num//10
    return dup==sol
num=int(input("Enter a number:"))
if is_Disarium(num,num,len(str(num))):
    print("Disarium number")
else:
    print("Not disarium number")