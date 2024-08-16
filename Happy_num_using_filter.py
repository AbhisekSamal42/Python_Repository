#Wap to print Happy number by using filter function in given range.
def is_Happy(num):
    while num>9:
        d_sum=0
        while num!=0:
            rem=num%10
            d_sum=d_sum+rem**2
            num=num//10
        num=d_sum
    return num==1 or num==7
for val in filter(is_Happy,range(10,20)):
    print(val)