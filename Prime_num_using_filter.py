#Wap to print prime number by using filter function in given range.
def is_Prime(num):
    if num<=1:
        return False
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return True
for val in filter(is_Prime,range(12,30)):
    print(val)