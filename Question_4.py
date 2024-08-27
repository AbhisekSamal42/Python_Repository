#Adding all element present in the list.
l1=list(map(int,input("Enter a list: ").split()))
print(l1)
sum=0
for ind in range(len(l1)):
    sum=sum+l1[ind]
print(sum)