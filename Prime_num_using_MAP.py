#Wap to check the number is prime or not in a given range by using MAP function.
def is_prime(num):
    if num<=1:
        return "Not prime number"
    for fa in range(2,num//2+1):
        if num%fa==0:
          return "Not prime number"
    return "Prime number"
for val in map(is_prime,range(10,15)):
    print(val)