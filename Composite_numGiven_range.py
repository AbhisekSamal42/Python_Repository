def is_composite(num):
    if num<=1:
        return "Not composite"
    for fa in range(2,num//2+1):
        if num%fa==0:
            return "Composite number"
    return "Not composite number"
def check_composite_in_range(start,end):
    for num in range(start,end+1):
        print(f"{num} is {is_composite(num)}")
start=int(input("Enter a number: "))
end=int(input("Enter a number: "))
print(check_composite_in_range(start,end))