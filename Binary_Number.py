# Converting Number to Binary value.
def is_Binary(num,pos,ans=0):
    while num!=0:
        rem=num%2
        ans=ans+(rem*pos)
        pos=pos*10
        num=num//2
    return ans
num=int(input("Enter a number: "))
pos=1
print(is_Binary(num,pos))
