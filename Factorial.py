def is_factorial(num,fact=1):
    for num in range(1,num+1):
        fact=fact*num
    return fact
print(is_factorial(int(input("Enter a number:"))))