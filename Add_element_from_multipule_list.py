l1=list(map(int,input("Enter 1st list: ").split()))
l2=list(map(int,input("Enter 2nd list: ").split()))
sum=[]
for ind in range(len(l1)):
    sum.append(l1[ind]+l2[ind])
print(sum)