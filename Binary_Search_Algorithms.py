def binary(l,user,low=0):
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]>user:
            high=mid-1
        elif l[mid]<user:
            low=mid+1
        elif l[mid]==user:
            return mid
    return -1
l=[0,7,8,11,12,22,40,45,57]
user=int(input("Enter a number from the list: "))
print(binary(l,user))