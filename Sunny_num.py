def is_Sunny(num,n=0):
    while n*n<=num+1:
        if n*n==num+1:
            return "Sunny number"
            break
        n=n+1
    else:
        return "Not sunny number"
num=int(input("Enter a number: "))
print(is_Sunny(num))