def is_revrese(num,rev=0):
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
print(is_revrese(int(input("enter a number:"))))