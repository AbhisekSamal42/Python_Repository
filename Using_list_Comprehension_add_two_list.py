l1=list(map(int,input("Enter 1st list: ").split()))
l2=list(map(int,input("Enter 2nd list: ").split()))
print([l1[ind]+l2[ind] for ind in range(len(l1))])