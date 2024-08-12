def is_prime(num):
    if num<=1:
       return "Not prime"
    for fa in range(2,num//2+1):
        if num%fa==0:
            return "Not prime"
    return "Prime"
def check_prime_in_range(start,end):
    for num in range(start,end+1):
        print(f"{num} is {is_prime(num)}")
start=int(input("Enter start number: "))
end=int(input("Enter end number: "))
print(check_prime_in_range(start,end))