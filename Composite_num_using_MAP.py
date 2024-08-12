#Wap to check the number is prime or not in a given range by using MAP function.
def is_composite(num):
    if num<=1:
        return "Not composte number"
    for fa in range(2,num//2+1):
        if num%fa==0:
            return "Composite number"
    return "Not composite number"
for val in map(is_composite,range(15,23)):
    print(val)