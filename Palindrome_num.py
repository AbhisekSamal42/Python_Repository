def is_palindrome(num,copy,rev=0):
    #copy=num
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return copy==rev
num=int(input("Enter a number:"))
if is_palindrome(num,num):
    print("Palindrome number")
else:
    print("Not palindrome number")