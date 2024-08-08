def is_prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return True
def is_Reverse(num,sol=0):
    while num!=0:
        rem=num%10
        sol=(sol*10)+rem
        num=num//10
    return sol
num=int(input("Enter a number: "))
reverse_num=is_Reverse(num)
if (num!=reverse_num) and is_prime(num) and is_prime(reverse_num):
    print("Emrip number")
else:
    print("Not emrip number")