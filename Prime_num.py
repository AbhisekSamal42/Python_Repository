def is_prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return "Not prime number"
    return "Prine number"
print(is_prime(int(input("Enter a number:"))))
    