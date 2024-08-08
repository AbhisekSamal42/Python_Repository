def Square(num,d_sum=0):
    while num!=0:
        rem=num%10
        d_sum=d_sum+(rem)**2
        num=num//10
    return d_sum
def is_Happy(num):
    while num>9:
        num=Square(num)
    return num==1 or num==7
num=int(input("Enter a number:"))
if is_Happy(num):
    print("Happy number")
else:
    print("Not happy number")