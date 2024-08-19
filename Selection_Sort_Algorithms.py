L=[12,67,98,768,46,85,45,86,13,43,23,69]
for ind1 in range(len(L)):
    low=ind1
    for ind2 in range(ind1+1,len(L)):
        if L[low]>L[ind2]:
            low=ind2
    L[ind1],L[low]=L[low],L[ind1]
print(L)


