def is_Palindrome(num,copy,rev=0):
    #copy=num
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return copy==rev
def is_prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return True
num=int(input("Enter a number: "))
if is_Palindrome(num,num) and is_prime(num):
    print("Palprime number")
else:
    print("Not paliprime number")
