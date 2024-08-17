def Interpolation(l,user):
    low=0
    high=len(l)-1
    while low<=high:
        user>=l[low] and user<=l[high]
        ind=int(low+((low-high)/(l[low]-l[high]))*(user-l[low]))
        if l[ind]>user:
            high=ind-1
        elif l[ind]<user:
            low=ind+1
        elif l[ind]==user:
            return ind
    return -1
l=[10,14,11,12,13,15,16,17]
user=int(input("Enter a number from the list: "))
print(Interpolation(l,user))