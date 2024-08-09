# Converting Binary to Number value.
def is_Number(num,val,ans=0):
    while num!=0:
        rem=num%10
        ans=ans+rem*val
        val=val*2
        num=num//10
    return ans
num=int(input("Enter a binary value: "))
val=1
print(is_Number(num,val))
