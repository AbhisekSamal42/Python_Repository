def is_composite(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return "Composite number"
    return "Not composite number"
print(is_composite(int(input("Enter a number:"))))