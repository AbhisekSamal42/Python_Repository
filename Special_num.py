def factorial(num,fact=1):
    for num in range(1,num+1):
        fact=fact*num
    return fact
def is_digit(num,copy,dsum=0):
    #copy=num
    while num!=0:
        rem=num%10
        dsum=dsum+factorial(rem)
        num=num//10
    return copy==dsum
def is_Special(num):
    return is_digit(num,num)
num=int(input("Enter a number: "))
if is_Special(num):
    print("Special number")
else:
    print("Not special number")