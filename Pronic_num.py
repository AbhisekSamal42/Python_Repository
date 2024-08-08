def is_Pronic(num,n=0):
    while num*(n+1)<=num:
        if n*(n+1)==num:
            return "Promic number"
            break
        n=n+1
    else:
        return "Not pronic number"
num=int(input("Enter a number:"))
print(is_Pronic(num))