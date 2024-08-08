def is_Harshad(num,copy,dsum=0):
    while num!=0:
        rem=num%10
        dsum=dsum+rem
        num=num//10
    if copy%dsum==0:
        return "Harshad number"
    else:
        return "Not harshad number"
num=int(input("Enter a number: "))
print(is_Harshad(num,num))